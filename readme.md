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
![](/img/Screenshot-2018-1-18%20MyFlaskApp.png "Index")  
From there you could either add a new feed to the Database by clicking the Green Add Feed Button near the top and you would be presented with a page that looks like the one below
![](/img/Screenshot-2018-1-18%20MyFlaskApp(2).png "Add Feed")   
After filling out at least the first 3 fields you would click the add article button at the bottom where you would be sent back to the homepage with the new feed in the table and a small notification on the top  
![](/img/Screenshot-2018-1-18%20MyFlaskApp(1).png "Add Successful")  
Or, You can edit an existing feed by pressing the edit button that is in the same row and a web-page similar to the one below except the fields would be filled with your information instead
![](/img/Screenshot-2018-1-18%20MyFlaskApp(3).png "Edit Feed")  
After editing the field that you would like, by pressing the edit article button, you would be brought back to the homepage with a similar notification as when you added a feed
![](/img/Screenshot-2018-1-18%20MyFlaskApp(4).png "Edit Successful")
Finally, if you want to delete an RSS Feed then all you need to do is press the delete button in the row of the feed that you want to delete and the webpage will be refreshed with the feed deleted and a notification on the top saying it was successful
![](/img/Screenshot-2018-1-18%20MyFlaskApp(5).png "Delete Successful")
