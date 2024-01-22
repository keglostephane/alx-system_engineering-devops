# set up client SSH config file to connect to a server without password

$str = "Host 18.207.234.107
   IdentityFile ~/.ssh/school
   PasswordAuthentication no
"
file { 'config':
  ensure  => file,
  path    => '/home/vagrant/.ssh/config',
  content => $str,
}
