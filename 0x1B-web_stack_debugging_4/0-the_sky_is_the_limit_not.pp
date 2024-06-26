# Script to increase the amount of traffic an nginx server can handle

# Must increase the ULIMIT of default file
exec { 'fix-for-nginx':
  # Change teh ULIMIT value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Path for sed command
  path    => '/usr/local/bin/:/bin/',
}

# Restarting Nginx
exec { 'nginx-restart':
  # resarting Nginx
  command => '/etc/init.d/nginx restart',
  # path for the init.d script
  path    => '/etc/init.d/',
}

