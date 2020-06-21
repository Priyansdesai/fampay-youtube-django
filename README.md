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
Then we will activate the virtual environment
```sh
$ source venv/bin/activate
```
Install the dependencies we will need for this project. 
```sh
$ pip3 install gunicorn flask 
```
Create a file called app.py using the command below and add the text below. 
```sh
$ sudo vim app.py 
```
Add this text to app.py
```sh
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
```
Now, run the following command as a sanity check to see if the Flask app is running. 
```sh
$ python app.py 
```
Close the Flask app and now we will run a WSGI server. In this demo, we will be using gunicorn. So, run the following command to start the server. 
```sh
$ gunicorn app:app -b localhost:8000 &
```
For a sanity check, check localhost:8000 that Hello World is displayed. 
You can keep this running in the background and then to start Nginx server follow the instructions given below. 
```sh
$ sudo vim /etc/nginx/conf.d/virtual.conf
```
And then add the following content
```sh
server {
    listen       80;
    server_name  your_public_dnsname_here;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```
The proxy pass must be the same on which gunicorn is running. 
Now, just run the commands below and see it work on your IP address. 
```sh
$ sudo nginx -t
$ sudo service nginx restart
```
If restart does not work, try the command below
```sh
$ sudo service nginx start
```
To stop the server, just run
```sh
$ sudo service nginx stop
```


