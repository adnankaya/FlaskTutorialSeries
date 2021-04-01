# YouTubeChannel
Repository for my Youtube channel : https://www.youtube.com/channel/UCtw7bDE_-qfjgjBlK1dEsRA

## Dependencies
- `python3.x`, `pip`, `virtualenv`
- create a new virtualenv by `virtualenv -p python3 env` command.
- install dependencies by `pip install -r requirements.txt`

## `Run Project`
```bash
$ virtualenv -p python3 env
$ source env/bin/activate # in Linux, MacOS
# $ .\env\Scripts\activate.bat # in Windows
(env) $ export FLASK_APP=main.py
(env) $ export FLASK_ENV=development # DO NOT Activate this in Production
(env) $ flask run
```

### To Fix Errors
1. **ERROR:**
```bash
WTForms: Install 'email_validator' for email validation support
```
1. **SOLUTION** `pip install wtforms[email]`
---
2. **ERROR** 
```bash
 from flask_uploads import UploadSet, IMAGES, configure_uploads
  File "/home/adnan/github-projects/FlaskTutorialSeries/myproject/env/lib/python3.8/site-packages/flask_uploads.py", line 26, in <module>
    from werkzeug import secure_filename, FileStorage
ImportError: cannot import name 'secure_filename' from 'werkzeug
```
2. **SOLUTION** `pip install -U Werkzeug==0.16.0`
---
3. **ERROR**
```bash
sqlalchemy.exc.OperationalError
sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: user...
```
3. **SOLUTION** : Do the database migrations!

## Database Migration
 1. `(env) $ flask db init`
 2. `(env) $ flask db migrate`
 3. `(env) $ flask db upgrade`

- Now you can run project with `flask run` and register to the application