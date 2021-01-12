# Noveltea-📖🍵
Intensive 1.1 (2020)<br>
[Heroku Live Link (currently works without login/signup and authetication)](https://noveltea.herokuapp.com/)


 ## Table of Contents
 * [About this Project](#about-this-project)
 * [Functions to Highlight](#functions-to-highlight)
 * [Deployment](#deployment)
 
## About this Project
Noveltea is created to bring together readers to one place in which they can read their favorite books, join fandoms, and even share their expereince with the community.
<br>
The website requires that users signup/login and stores the autheticated information in an SQLite. Once signed in, the user is taken to their profile page through which they have the option to also search for books. 
The book search utilizes Google Books API to allow users to perform searches to find their favorite books.

## Functions to highlight
* Signup / Login / Book Search / Backend authetication code


## Deployment
Download
```bash
git clone git@github.com:sree-chikati/noveltea-website.git
git remote set-url origin git@github.com:YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin master
```
Deploy virtual environment.
```
python3 -m venv auth
source auth/bin/activate
```

Run the following commands from your virtual environment to install the needed packages
```bash 
(auth)$ pip3 install flask flask-sqlalchemy flask-login
```

Deploy database
```python
# enter Python REPL to perform this
flask shell
>>> from app import db, create_app, models
>>> db.create_all(app=create_app())
```

Install requirements
```bash 
# install python requirements
python3 -m pip install -r requirements.txt
```

Set FLASK_APP to run project folder
```bash 
(auth)$ export FLASK_APP=project
(auth)$ export FLASK_DEBUG=1
```

On a development server
```bash 
# run
flask run
```

For more information visit websites:
> Learn how to [add authetication to your app with Flask-Login](https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login)
