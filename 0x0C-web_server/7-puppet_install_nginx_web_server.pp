# Install and configure a Nginx server on ubuntu with following requirements:
# Nginx should be listening on port 80
# request / using curl must return a page that contain "Hello World!"
# redirection must be a "301 Moved Permanently"

$config = "
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;

	index index.html index.htm index.nginx-debian.html;

	server_name _;

	location / {
		try_files ${uri} ${uri}/ =404;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	error_page 404 /404.html;
}
"

# updage package repositories
exec { 'update repositories':
  command => '/usr/bin/apt update',
}

# install nginx package
package { 'nginx':
  ensure   => installed,
  provider => apt,
  require  => Exec['update repositories'],
}

# create and add content to index file
file { 'index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
}

# configure nginx server
file { 'default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  content => $config,
}

# restart nginx server
service { 'nginx':
  ensure   => running,
  require  => Package['nginx'],
}
