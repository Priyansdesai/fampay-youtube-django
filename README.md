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
Now we let's run the server and test this app. 
```sh
$ cd fampay-youtube-django/fampay
$ python manage.py runserver
```
Redirect to any of the following URLs to check the data being uploaded. 
```sh
localhost:8000
http://127.0.0.1:8000/
```
