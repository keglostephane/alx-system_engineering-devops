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

# install nginx package
package { 'nginx':
  ensure   => installed,
  provider => apt,
}

# create and add content to index file
file { 'index.html':
  ensure  => 'file',
  path    => '/var/www/html/index.html',
  content => 'Hello World!',
  mode    => '0644',
  owner   => root,
}

# create 404 html file
file { '404.html':
  ensure  => 'file',
  path    => '/var/www/html/404.html',
  content => "Ceci n'est pas une page\n\n",
  mode    => '0644',
  owner   => root,
}

# configure nginx server
file { 'default':
  ensure  => 'file',
  path    => '/etc/nginx/sites-available/default',
  content => $config,
  mode    => '0644',
  owner   => root,
}

# restart nginx server
service { 'nginx':
  provider => 'debian',
  restart  => 'service nginx restart',
}
