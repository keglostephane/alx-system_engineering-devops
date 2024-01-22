# set up client SSH config file to connect to a server without password

$str = "Host 98512-web-01
   Hostname 18.207.234.107
   User ubuntu
   IdentityFile ~/.ssh/school
   PubkeyAuthentication yes
"
file { 'config':
  ensure  => file,
  path    => '/home/vagrant/.ssh/config',
  content => $str,
}
