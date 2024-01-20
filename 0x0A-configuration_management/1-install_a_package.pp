# Install a python package
# package_name: flask
# package_version: 2.1.0
# package_manager: pip3

package { 'python3-pip':
  ensure  => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
