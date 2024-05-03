# using Puppet, install flask using pip3

pakage { 'flask':
  ensure => '2.1.0',
  provider => 'pip3'
}
