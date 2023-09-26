<h1 align="center"> 0x0D-web_stack_debugging_0 </h1>

## Concepts:



For this project, we expect you to look at these concepts:

* [Network basics](https://intranet.alxswe.com/concepts/33)
* [Docker](https://intranet.alxswe.com/concepts/65)
* [Web stack debugging](https://intranet.alxswe.com/concepts/68)


<h2 align="center"> Background Context </h1>


The Webstack debugging series will train you in the art of debugging. Computers and software rarely work the way we want (that’s the “fun” part of the job!).

Being able to debug a webstack is essential for a Full-Stack Software Engineer, and it takes practice to be a master of it.

In this debugging series, broken/bugged webstacks will be given to you, the final goal is to come up with a Bash script that once executed, will bring the webstack to a working state. But before writing this Bash script, you should figure out what is going on and fix it manually.

Let’s start with a very simple example. My server must:

* have a copy of the `/etc/passwd` file in `/tmp`
* have a file named `/tmp/isworking` containing the string `OK`

Let’s pretend that without these 2 elements, my web application cannot work.

Let’s go through this example and fix the server.

```
vagrant@vagrant:~$ docker run -d -ti ubuntu:14.04
Unable to find image 'ubuntu:14.04' locally
14.04: Pulling from library/ubuntu
34667c7e4631: Already exists
d18d76a881a4: Already exists
119c7358fbfc: Already exists
2aaf13f3eff0: Already exists
Digest: sha256:58d0da8bc2f434983c6ca4713b08be00ff5586eb5cdff47bcde4b2e88fd40f88
Status: Downloaded newer image for ubuntu:14.04
76f44c0da25e1fdf6bcd4fbc49f4d7b658aba89684080ea5d6e8a0d832be9ff9
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
76f44c0da25e        ubuntu:14.04        "/bin/bash"         13 seconds ago      Up 12 seconds                           infallible_bhabha
vagrant@vagrant:~$ docker exec -ti 76f44c0da25e /bin/bash
root@76f44c0da25e:/# ls /tmp/
root@76f44c0da25e:/# cp /etc/passwd /tmp/
root@76f44c0da25e:/# echo OK > /tmp/isworking
root@76f44c0da25e:/# ls /tmp/
isworking  passwd
root@76f44c0da25e:/#
vagrant@vagrant:~$
```

Then my answer file would contain:

```
sylvain@ubuntu:~$ cat answerfile
#!/usr/bin/env bash
# Fix my server with these magic 2 lines
cp /etc/passwd /tmp/
echo OK > /tmp/isworking
sylvain@ubuntu:~$
```

Note that as you cannot use interactive software such as `emacs` or `vi` in your Bash script, everything needs to be done from the command line (including file edition).


<h2 align="center"> Installing Docker </h2>

For this project you will be given a container which you can use to solve the task. If you would like to have Docker so that you can experiment with it and/or solve this problem locally, you can install it on your machine, your Ubuntu 14.04 VM, or your Ubuntu 16.04 VM if you upgraded.

* [Mac OS](https://intranet.alxswe.com/rltoken/wuCgR0pVioCnvtMKTeMgdQ)
* [Windows](https://intranet.alxswe.com/rltoken/9nVKpuQIDJhZoLP4mZmbRA)
* [Ubuntu 14.04](https://intranet.alxswe.com/rltoken/crVTooJdN8U8wATMvG2-og) (Note that Docker for Ubuntu 14 is deprecated and you will have to make some adjustments to the instructions when installing)
* [Ubuntu 16.04](https://intranet.alxswe.com/rltoken/wTjFrD8iy96EZW9MFYwa9Q)


<h2 align="center"> Resources <h2>

#### man or help:

* curl


<h2 align="center"> Requirements <h2>

### General:


* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash scripts must pass `Shellcheck` without any error
* Your Bash scripts must run without error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing


<br><br>________________________<br><br>

## Tasks:

### 0. Give me a page!

Be sure to read the Docker concept page

In this first debugging project, you will need to get [Apache](https://intranet.alxswe.com/rltoken/HVGgLL51qmuulmw802M-Jg) to run on the container and to return a page containing `Hello Holberton` when querying the root of it.

Example:

```
vagrant@vagrant:~$ docker run -p 8080:80 -d -it holbertonschool/265-0
47ca3994a4910bbc29d1d8925b1c70e1bdd799f5442040365a7cb9a0db218021
vagrant@vagrant:~$ docker ps
CONTAINER ID        IMAGE                   COMMAND             CREATED             STATUS              PORTS                  NAMES
47ca3994a491        holbertonschool/265-0   "/bin/bash"         3 seconds ago       Up 2 seconds        0.0.0.0:8080->80/tcp   vigilant_tesla
vagrant@vagrant:~$ curl 0:8080
curl: (52) Empty reply from server
vagrant@vagrant:~$
```

Here we can see that after starting my Docker container, I `curl` the port `8080` mapped to the Docker container port `80`, it does not return a page but an error message. Note that you might also get the error message `curl: (52) Empty reply from server.`

```
vagrant@vagrant:~$ curl 0:8080
Hello Holberton
vagrant@vagrant:~$
```

After connecting to the container and fixing whatever needed to be fixed (here is your mission), you can see that curling port 80 return a page that contains `Hello Holberton`. Paste the command(s) you used to fix the issue in your answer file.



#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x0D-web_stack_debugging_0`
* File: `0-give_me_a_page`

<br>
_____
<br>

### 1. Install nginx web server

Readme:

* [-y on apt-get command](https://intranet.alxswe.com/rltoken/KJiFZ4yJyTGp_cv3DYQLaQ)

Web servers are the piece of software generating and serving HTML pages, let’s install one!

Requirements:

* Install `nginx` on your `web-01`
* server
* Nginx should be listening on port 80
* When querying Nginx at its root `/` with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
* As an answer file, write a Bash script that configures a new Ubuntu machine to respect above requirements (this script will be run on the server itself)
* You can’t use `systemctl` for restarting `nginx`

Server terminal:

```
root@sy-web-01$ ./1-install_nginx_web_server > /dev/null 2>&1
root@sy-web-01$ 
root@sy-web-01$ curl localhost
Hello World!
root@sy-web-01$ 
```

Local terminal:

```
sylvain@ubuntu$ curl 34.198.248.145/
Hello World!
sylvain@ubuntu$ curl -sI 34.198.248.145/
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 23:43:22 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
Connection: keep-alive
ETag: "58abea7c-1e"
Accept-Ranges: bytes

sylvain@ubuntu$
```

In this example `34.198.248.145` is the IP of my `web-01` server. If you want to query the Nginx that is locally installed on your server, you can use `curl 127.0.0.1`.

If things are not going as expected, make sure to check out Nginx logs, they can be found in `/var/log/`.



#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x0C-web_server`
* File: `1-install_nginx_web_server`

<br>
_____
<br>


### 2. Setup a domain name

[.TECH Domains](https://intranet.alxswe.com/rltoken/Hcb-pfK8UiDBfwsDJPyZZw) is one of the top domain providers. They are known for the stability and quality of their DNS hosting solution. We partnered with .TECH Domains so that you can learn about DNS.

.TECH Domains worked with domain name registrars to give you access to a free domain name for a year. Please get the promo code in your [tools space](https://intranet.alxswe.com/rltoken/CprZO4m1rUm5C6ZgvROpgg). Feel free to drop a thank you tweet for [.TECH Domains](https://intranet.alxswe.com/rltoken/y3_YCbJ5bGKgPYqP0LyVBA).

Provide the domain name in your answer file.

Requirement:

* provide the domain name only (example: `foobar.tech`), no subdomain (example: `www.foobar.tech`)
* configure your DNS records with an A entry so that your root domain points to your `web-01` IP address <b>Warning: the propagation of your records can take time (~1-2 hours).</b>
* go to [your profile](https://intranet.alxswe.com/rltoken/hH2hPj0jwETzZL-AvFJkwQ) and enter your domain in the `Project website url` field

Example:

```
sylvain@ubuntu$ cat 2-setup_a_domain_name
myschool.tech
sylvain@ubuntu$
sylvain@ubuntu$ dig myschool.tech

; <<>> DiG 9.10.6 <<>> myschool.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 26785
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 512
;; QUESTION SECTION:
;myschool.tech.     IN  A

;; ANSWER SECTION:
myschool.tech.  7199    IN  A   184.72.193.201

;; Query time: 65 msec
;; SERVER: 8.8.8.8#53(8.8.8.8)
;; WHEN: Fri Aug 02 09:44:36 PDT 2019
;; MSG SIZE  rcvd: 65

sylvain@ubuntu$
```

When your domain name is setup, please verify the Registrar here: [https://whois.whoisxmlapi.com/](https://intranet.alxswe.com/rltoken/UVCb6LeF54ktxR6lZSUyTQ) and you must see in the JSON response: `"registrarName": "Dotserve Inc"`


#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x0C-web_server`
* File: `2-setup_a_domain_name`

<br>
_____
<br>

### 3. Redirection

Readme:

* [Replace a line with multiple lines with sed](https://intranet.alxswe.com/rltoken/RRP9hX3MlQdABaKZD-Y_cA)

Configure your Nginx server so that `/redirect_me is` redirecting to another page.

Requirements:

* The redirection must be a “301 Moved Permanently”
* You answer file should be a Bash script containing commands to automatically configure a Ubuntu machine to respect above requirements
* Using what you did with `1-install_nginx_web_server`, write `3-redirection` so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:

```
sylvain@ubuntu$ curl -sI 34.198.248.145/redirect_me/
HTTP/1.1 301 Moved Permanently
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:36:04 GMT
Content-Type: text/html
Content-Length: 193
Connection: keep-alive
Location: https://www.youtube.com/watch?v=QH2-TGUlwu4

sylvain@ubuntu$
```

#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x0C-web_server`
* File: `3-redirection`


<br>
_____
<br>

###  4. Not found page 404

Configure your Nginx server to have a custom 404 page that contains the string `Ceci n'est pas une page.`

Requirements:

* The page must return an HTTP 404 error code
* The page must contain the string `Ceci n'est pas une page`
* Using what you did with `3-redirection`, write `4-not_found_page_404` so that it configures a brand new Ubuntu machine to the requirements asked in this task

Example:

```
sylvain@ubuntu$ curl -sI 34.198.248.145/xyz
HTTP/1.1 404 Not Found
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 21 Feb 2017 21:46:43 GMT
Content-Type: text/html
Content-Length: 26
Connection: keep-alive
ETag: "58acb50e-1a"

sylvain@ubuntu$ curl 34.198.248.145/xyzfoo
Ceci n'est pas une page

sylvain@ubuntu$
```

#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x0C-web_server`
* File: `4-not_found_page_404`

<br>
_____
<br>

### 5. Install Nginx web server (w/ Puppet)

Time to practice configuring your server with Puppet! Just as you did before, we’d like you to install and configure an Nginx server using Puppet instead of Bash. To save time and effort, you should also include resources in your manifest to perform a 301 redirect when querying /redirect_me.

Requirements:

* Nginx should be listening on port 80
* When querying Nginx at its root \ with a GET request (requesting a page) using `curl`, it must return a page that contains the string `Hello World!`
* The redirection must be a “301 Moved Permanently”
* Your answer file should be a Puppet manifest containing commands to automatically configure an Ubuntu machine to respect above requirements

#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x0C-web_server`
* File: `7-puppet_install_nginx_web_server.pp`


