# fampay-youtube-django

This app is written in the Django framework. This app fetches YouTube videos published after 1st January 2018 in the beginning and then updates the date to be a day later than its previous date, every 10 seconds, fetching new database. 

First, we need to clone this Git repository. Run the command below in whichever directory you wish this project to be. 
```sh
$ git clone https://github.com/Priyansdesai/fampay-youtube-django.git
```
Then, we will have to install the requirements for this Project. So, running the command below will do so. Make sure you have pip installed on the system you are running this app on.  
```sh
$ pip install -r requirements.txt
```
Before you begin running your app, you should add your YouTube API Key in fampay/settings.py 
```sh
DEVELOPER_KEY = ""
```
Now we navigate back to our base directory and let's run the server and test this app. 
```sh
$ cd fampay-youtube-django/fampay
$ python manage.py runserver
```
Redirect to any of the following URLs to check the data being uploaded in table format. 
```sh
localhost:8000
http://127.0.0.1:8000/
```
Few comments on how the table will be populated:

1. Every 10 seconds, when the page refreshes, it loads 1 more video than it loaded last time, so that we have at least 1 video that is different from what already exists in the database. This is done by saving the state in .txt file called total.txt in the fampay directory. 

2. To allow for videos, that are not present in the database, this app when updates every 10 seconds, also updates the publishedAfter argument of the search.list function by a day. 

3. Both of these arguments are persisted in their state by the .txt files in fampay directory. 

4. They are both initialized to 1