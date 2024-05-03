# Creates a file in/ tmp directory

file {'school':
  ensure => 'present',
  content => 'I love Puppet',
  group
} 