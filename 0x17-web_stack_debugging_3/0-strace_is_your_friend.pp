# Fixing wordpress error 500


exec{ "fixing-wordpress":
  command => 'sed -i s/phpp/php/g /var/ww/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
