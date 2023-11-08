# 0x18-webstack_monitoring

#### Install or Update to the latest Agent 7 version on Ubuntu

##### Run this command to install or update...

```
DD_API_KEY=723138ee24dfd489a3a094c1239b00c3 DD_SITE="datadoghq.com" bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"
```

- This will install the APT packages for the Datadog Agent and will prompt you for your password.
- If the Agent is not already installed on your machine and you don't want it to start automatically after the installation, just prepend DD_INSTALL_ONLY=true to the above script before running it.
- If you have an existing agent configuration file, those values will be retained during the update.
