### Alexa RSS Skill Companion Web App  

This is a web app built using Python Flask to interact with the [Alexa RSS Skill](https://github.com/frybin/Alexa-RSS-Skill) MySQL Database  

To configure the web app to connect to the correct database a config_keys.py has to be created in the main directory following the template right underneath

```Python
secretkey ='String'
DB_USERNAME ='String'
DB_HOST = 'String'
DB_PASSWORD = 'String'
DB = 'String'
```
After being configured correctly and made sure that the correct modules are installed, running the application should give you a link that looks similar to : http://127.0.0.1:5000

After going to the link the webpage should look like the picture underneath
![alt text](/home/frybin/Documents/microblog/img/Screenshot-2018-1-18 MyFlaskApp.png "Logo Title Text 1")
