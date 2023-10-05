<h1 align="center"> 0x10. HTTPS SSL </h1>

<br><br><br>

# Concepts


For this project, we expect you to look at these concepts:

* [DNS](https://intranet.alxswe.com/concepts/12)
* [Web stack debugging](https://intranet.alxswe.com/concepts/68)

<br><br>

![concept image](./images/concept.png)

<br><br>

# Resources

#### Read or watch:

* [What is HTTPS?](https://intranet.alxswe.com/rltoken/XT1BAiBL3Jpq1bn1q6IYXQ)
* [What are the 2 main elements that SSL is providing](https://intranet.alxswe.com/rltoken/STj5WkAPACBxOvwB77Ycrw)
* [HAProxy SSL termination on Ubuntu16.04](https://intranet.alxswe.com/rltoken/XD_RckEgjds0UkoMsfxp2A)
* [SSL termination](https://intranet.alxswe.com/rltoken/CKUICfppIWI6UC0coEMB8g)
* [Bash function](https://intranet.alxswe.com/rltoken/zPjZ7-eSSQsLFsGA16C1HQ)

#### man or help:

* awk
* dig



## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/fJ20wsMngb_yNAhGgBwzlQ), without the help of Google:

#### General

* What is HTTPS SSL 2 main roles
* What is the purpose encrypting traffic
* What SSL termination means

## Requirements
#### General

* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
* The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing


<br><br>

# Tasks

### 0. World wide web

Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

#### Requirements:

* Add the subdomain `www` to your domain, point it to your `lb-01` IP (your domain name might be configured with default subdomains, feel free to remove them)
* Add the subdomain `lb-01` to your domain, point it to your `lb-01` IP
* Add the subdomain `web-01` to your domain, point it to your `web-01` IP
    Add the subdomain `web-02` to your domain, point it to your `web-02` IP
* Your Bash script must accept 2 arguments:
    * `domain`:
        * type: string
        * what: domain name to audit
        * mandatory: yes
    * `subdomain`:
        * type: string
        * what: specific subdomain to audit
        * mandatory: no
* Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
* When only the parameter domain is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
* When passing `domain` and `subdomain` parameters, display information for the specified `subdomain`
* Ignore `shellcheck` case `SC2086`
* Must use:
    * `awk`
    * at least one Bash function
* You do not need to handle edge cases such as:
    * Empty parameters
    * Nonexistent domain names
    * Nonexistent subdomains



Example:

```
sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
```


#### Repo:

* GitHub repository: `alx-system_engineering-devops`
* Directory: `0x10-https_ssl`
* File: `0-world_wide_web`



