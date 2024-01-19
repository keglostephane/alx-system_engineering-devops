# kill a process named `killmenow`
# command_name: pkill

exec { 'pkill':
  command  => 'pkill -15 killmenow',
  provider => 'shell',
  }
