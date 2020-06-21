# fampay-youtube-django

First, we will install all the required packages for this demo. 

```sh
$ sudo apt-get install nginx supervisor python3-pip python3-virtualenv
```
Then we will create a virtual environment called venv in our project directory.
```sh
$ mkdir myproj
$ cd myproj
$ virtualenv venv
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


