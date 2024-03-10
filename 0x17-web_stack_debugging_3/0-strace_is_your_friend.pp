# Fix Wordpress config files
exec {'Fix wp-settings.php':
  command  => "sed -i '/.phpp/ s/.phpp/.php/g' /var/www/html/wp-settings.php",
  provider => 'shell'
}
