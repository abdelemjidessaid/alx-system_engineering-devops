# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'pkill':
  provider => 'shell',
  command  => 'pkill -f killmenow',
}
