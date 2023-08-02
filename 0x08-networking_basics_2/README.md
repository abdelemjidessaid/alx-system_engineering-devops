### 0x08-networking_basics_2

##### In this project we will learn and solve tasks about __Basics of Networking__.

* `0-change_your_home_IP` Bash script that configures an Ubuntu server with the below requirements.

	`localhost` resolves to `127.0.0.2`
	`facebook.com` resolves to `8.8.8.8`

* `1-show_attached_IPs` Bash script that displays all active IPv4 IPs on the machine it’s executed on.

	Example:
		```
		sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
		10.0.2.15$
		127.0.0.1$
		sylvain@ubuntu$
		```
