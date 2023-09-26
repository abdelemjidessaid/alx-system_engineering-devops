<h1 align="center"> 0x0C-web_server </h1>

<br><br>
In this project we will learn many concepts about:

* `nginx`: Nginx (pronounced "engine-x") is a popular open-source web server, reverse proxy server, and load balancer. It is designed to efficiently handle high concurrent connections and deliver static and dynamic content with low resource usage. Nginx is known for its performance, scalability, and ability to handle heavy web traffic.

    Originally created by Igor Sysoev in 2004, Nginx has gained significant popularity and is widely used by many large-scale websites, web applications, and web services. It has a modular architecture that allows it to be extended with various add-ons and modules to enhance its functionality.

    Here are some key features and use cases of Nginx:

    * Web Server: Nginx can serve web content, such as HTML pages, images, CSS files, and JavaScript files, directly to clients. It is known for its efficiency in handling static content and can handle a large number of concurrent connections.

    * Reverse Proxy Server: Nginx can act as a reverse proxy, sitting between clients and backend servers. It can distribute incoming requests to multiple backend servers based on various load balancing algorithms, helping to improve application performance and reliability.

    * Load Balancer: Nginx's load balancing capabilities allow it to distribute incoming traffic across multiple backend servers to share the workload. It can help increase the capacity and scalability of web applications by efficiently utilizing server resources.

    * SSL/TLS Termination: Nginx can handle SSL/TLS encryption and decryption, relieving the backend servers from the processing overhead. It can act as an SSL/TLS termination point, improving security and performance.

    * Caching: Nginx includes built-in caching capabilities, allowing it to cache and serve static content or even cache dynamic content to reduce the load on backend servers and improve response times.

    * High Availability: Nginx can be configured in a high availability setup, where multiple instances of Nginx are deployed to ensure redundancy and failover. This helps in maintaining service availability even if one or more servers become unavailable.

    Nginx is highly customizable through its configuration files and supports a wide range of operating systems. It has a large and active community, providing extensive documentation, tutorials, and support. Nginx is often used in combination with other software components to build robust and scalable web architectures.


* `child process`:
    In computer programming and operating systems, a child process refers to a process that is created by another process, known as the parent process. The parent process typically spawns or creates one or more child processes to perform specific tasks or execute certain programs.

* `root domain`:
    Root Domain: The root domain, also known as the top-level domain (TLD), is the highest level in the domain name hierarchy. It is represented by the last portion of a domain name, following the final dot. Examples of common root domains include .com, .org, .net, .gov, .edu, and so on. The root domain represents the global naming system and is managed by designated organizations, such as ICANN (Internet Corporation for Assigned Names and Numbers).

* `subdomain`:
    Subdomain: A subdomain is a subdivision of a larger domain. It is created by adding a prefix to the root domain, separating it with a dot. Subdomains allow for further organization and categorization of websites or services under a parent domain. For instance, in the domain name example.com, "example" is the root domain. By adding a subdomain like "blog," the resulting subdomain would be "blog.example.com." Subdomains can be used to host separate websites, create distinct services, or organize content within a larger website.


* `HTTP requests`:
    HTTP (Hypertext Transfer Protocol) requests are the primary means by which clients (such as web browsers) communicate with servers to retrieve or send data over the web. HTTP requests consist of a request method, URL, headers, and an optional request body. Here are the main HTTP request methods:

    * GET: The GET method is used to retrieve data from a server. It requests a representation of a resource specified by the URL. GET requests are typically used to fetch web pages, images, or other static content.

    * POST: The POST method is used to submit data to a server to create a new resource or perform some action. It sends data in the request body and is commonly used for submitting forms, uploading files, or sending data to APIs.

    * PUT: The PUT method is used to update or replace an existing resource on the server. It sends the new representation of the resource in the request body, replacing the previous version entirely.

    * DELETE: The DELETE method is used to delete a specified resource on the server. It requests the removal of the resource identified by the URL.

    * PATCH: The PATCH method is used to partially update a resource on the server. It sends a set of changes to be applied to the resource rather than replacing the entire representation.

    * HEAD: The HEAD method is similar to the GET method but retrieves only the headers of the response, without the actual content. It is often used to retrieve metadata or check the availability of a resource.

    * OPTIONS: The OPTIONS method is used to retrieve the communication options available for a resource or server. It provides information about the supported methods, headers, and other capabilities.

    These HTTP request methods allow clients to interact with servers, retrieve data, send data, update resources, and perform various actions over the web. The appropriate method to use depends on the desired operation and the semantics of the resource being accessed.


* `HTTP redirection`:
    HTTP redirection is a mechanism used by web servers to instruct clients (such as web browsers) to navigate to a different URL. This can be useful for various purposes, including redirecting users to a new location, handling outdated URLs, or implementing load balancing.

    HTTP redirection is typically implemented using HTTP status codes and corresponding response headers. Here are some commonly used HTTP redirection codes:

    * `301 Moved Permanently`  : This status code indicates that the requested resource has been permanently moved to a new URL. The client should update its bookmarks or references to the old URL and use the new URL for future requests.

    * `302 Found (or 303 See Other)`: These status codes indicate a temporary redirection. The requested resource is temporarily available at a different URL. The client should use the new URL for the current request, but future requests may still use the original URL.

    * `307 Temporary Redirect`: Similar to 302, this status code indicates a temporary redirect. The client should continue to use the original URL for future requests.

    * `308 Permanent Redirect`: This status code is similar to 301 but is used for indicating a permanent redirection.



#### main or help:

* `scp`:
    SCP (Secure Copy Protocol) is a network protocol that enables secure file transfer between a local host and a remote host or between two remote hosts. It is a secure alternative to the traditional FTP (File Transfer Protocol) and allows files and directories to be transferred over SSH (Secure Shell) connections.

    The syntax for using SCP is as follows:
    ```
    scp [options] source_file destination_file
    ```

    Some commonly used options with SCP include:

    * `-r`: Recursively copy directories and their contents.
    * `-P` port: Specify a non-default SSH port for the SCP connection.
    * `-p`: Preserve the file attributes such as timestamps and permissions during the copy.
    * `-v`: Verbose output, displaying detailed information about the SCP transfer.

    Examples:

    Copy a local file to a remote host:
    ```
    scp localfile.txt user@remotehost:/path/to/destination/
    ```


* `curl`:
    Curl, short for "Client for URLs," is a command-line tool and library for making HTTP requests and interacting with various network protocols. It supports a wide range of protocols, including HTTP, HTTPS, FTP, SMTP, POP3, IMAP, SCP, and more. Curl is available on most operating systems and is commonly used for tasks such as testing APIs, downloading files, and automating web-related tasks.

    The basic syntax for using curl is as follows:

    ```
    curl [options] [URL]
    ```

    Here are some commonly used options with curl:

    * `-X, --request <HTTP method>`: Specify the HTTP request method (GET, POST, PUT, DELETE, etc.).
    * `-H, --header <header>`: Add custom headers to the request.
    * `-d, --data <data>`: Include data in the request body for methods like POST or PUT.
    * `-F, --form <name=content>`: Send form data as a multipart/form-data request.
    * `-o, --output <file>`: Save the output to a file.
    * `-O, --remote-name`: Save the output using the remote file name.
    * `-L, --location`: Follow HTTP redirects.
    * `-u, --user <username:password>`: Provide authentication credentials.
    * `-v, --verbose`: Output detailed information about the request and response.
    * `--insecure`: Disable SSL certificate verification (useful for testing self-signed certificates).

    Examples:

    Send a GET request to a URL:

    ```
    curl https://example.com
    ```

    Send a POST request with JSON data:

    ```
    curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' https://api.example.com/endpoint
    ```

    Download a file:

    ```
    curl -O https://example.com/file.txt
    ```

    Upload a file using FTP:

    ```
    curl -u username:password -T localfile.txt ftp://ftp.example.com/destination/
    ```


* `DNS record types`:
    DNS (Domain Name System) is responsible for translating domain names into IP addresses and managing various types of resource records. Here are the explanations of the DNS record types you mentioned:

    * `A (Address) Record`: The A record is the most common type of DNS record. It maps a domain name to an IPv4 address. It associates a domain name (such as example.com) with the corresponding IP address (such as 192.0.2.1). When you type a domain name into a web browser, the A record is used to find the corresponding IP address and establish a connection to the web server.

    * `CNAME (Canonical Name) Record`: A CNAME record is used to create an alias or a nickname for a domain name. It points a domain name to another domain name (canonical name). This is useful when you want multiple domain names to resolve to the same IP address. For example, if you have both www.example.com and blog.example.com pointing to the same website, you can create a CNAME record for blog.example.com that points to www.example.com.

    * `TXT (Text) Record`: The TXT record is used to store arbitrary text data associated with a domain name. It is commonly used for various purposes, such as adding descriptive information, verifying domain ownership, or configuring services like SPF (Sender Policy Framework) for email. The text data can be in any format, but it is often used for human-readable information.

    * `MX (Mail Exchanger) Record`: The MX record specifies the mail servers responsible for receiving emails for a domain. It points to the domain names of the mail servers that handle incoming email for the domain. When someone sends an email to an address at a particular domain, the MX record is used to determine the mail server that should receive the email. The MX record has a priority value (MX preference) that determines the order in which mail servers should be contacted.

    These are just a few examples of DNS record types. There are many other types, such as AAAA (IPv6 address), NS (Name Server), SOA (Start of Authority), PTR (Pointer), and more. Each record type serves a specific purpose in managing domain names, IP addresses, email routing, and other DNS-related functionalities.


<br><br>______________________________________<br><br>

## Tasks:

### 0. Transfer a file to your server:

Write a Bash script that transfers a file from our client to a server:

Requirements:

* Accepts 4 parameters
    * 1- The path to the file to be transferred
    * 2- The IP of the server we want to transfer the file to
    * 3- The username `scp` connects with
    * 4- The path to the SSH private key that `scp` uses
* Display `Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY` if less than 3 parameters passed
* scp must transfer the file to the user home directory `~/`
* Strict host key checking must be disabled when using `scp`

Example:

```
sylvain@ubuntu$ ./0-transfer_file
Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY
sylvain@ubuntu$
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/sylvain 'ls ~/'
afile
sylvain@ubuntu$ 
sylvain@ubuntu$ touch some_page.html
sylvain@ubuntu$ ./0-transfer_file some_page.html 8.8.8.8 sylvain /vagrant/private_key
some_page.html                                     100%   12     0.1KB/s   00:00
sylvain@ubuntu$ ssh ubuntu@8.8.8.8 -i /vagrant/private_key 'ls ~/'
afile
some_page.html
sylvain@ubuntu$
```

In this example, I:

* remotely execute the `ls ~/` command via `ssh` to see what `~/` contains
* create a file named `some_page.html`
* execute my `0-transfer_file script`
* remotely execute the `ls ~/ `command via `ssh` to see that the file `some_page.html` has been successfully transferred

That is one way of publishing your website pages to your server.



#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x0C-web_server`
* File: `0-transfer_file`


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


