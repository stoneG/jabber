Jabber
======

A little Python CLI tool for messaging a HipChat room.  

Based on [HipChat `rooms/message` API](https://www.hipchat.com/docs/api/method/rooms/message)  

Requires:  
* An Admin/Notification authentication token from the admin of your HipChat account.
* [Requests](http://docs.python-requests.org/en/latest/)

Installation
------------

Clone repo:
```
git clone https://github.com/stoneG/jabber.git
```
Get requests via [pip](http://www.pip-installer.org/en/latest/): (hopefully into a virtualenv)
```
pip install requests
```
Setup your `conf.py` file, or feel free to use the sample template (`sample_conf.py`):  
```
vim conf.py
```
Start jabbering:  
```
python jabber.py 'Hello World!'
```

License
-------
MIT
