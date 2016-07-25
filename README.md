# Drop-your-projects

Know more about the developer on <a href="https://www.linkedin.com/in/bharathi-ranganathan">Linkedin</a>

Click on the link below to check out the fully deployed website: https://drop-your-projects.herokuapp.com/

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
	- [Front-end](#front-end)
	- [Back-end](#back-end)
- [File Guide](#file-guide)

## Introduction
Drops your projects is a fully deployed web application which allows users to launch a social media campaign. By joinning drop your projects, individuals can get an unique referral link which can be shared widely along various social networking sites. By sharing the links among social media, individuals gather a team further by earning points towards referring. Based on their number of reference, the users earn points for specific rewards. The rewards depends on the number of users referred by a particular user. The rewards includes from Streaming, downloading to a 12 Month memebership for making your own projects. 


## Features

**Current Features**

1. Unique referral id generated for each user. 
2. Same user joins again to view their friends and earned points. 
3. Users number of friends, points and rewards automatically loaded on the share page. 
4. Jquery applied for the progress bar to show each users progress in earning points. 
5. South converted app
6. Direct links provided to share with various social networking sites.

**Future Enhancements**

1. Enhancing the present application that helps the users to deploy, stream and download projects. 
2. Allowing the user to maintain a secure account for their memberhsip.
3. Include a chat room for each project team to discuss about their progress.

## Technologies
Python, Django Framework, Jquery, Javascript, HTML, CSS, SQLite3, Bootstrap.

### Front-end
CSS, HTML and Bootstrap runs the frontend of the drop-your-projects app. 

### Back-end
The back-end of drop-your-projects application is maintained by Python and Djano framework. 
Dependencies are given in Drop-your-projects/requirements.txt.

## File Guide
* <kbd>joins/model.py</kbd>  Creates the tables for the database
* <kbd>joins/views.py</kbd>  Handles the web requests and returns Responses
* <kbd>manage.py</kbd>  Implements the backend Python server using Django Framework
* <kbd>dyp/settings/base.py</kbd> Controls the base directory, database, media and template settings required for deployment.
* <kbd>dyp/settings_old.py</kbd>  Controls the base directory, database, media and template settings required for local run.
* <kbd>requirements.txt</kbd>  Dependencies for the virutal environment are provided.

## Installation

```sh
$ mkdir dropyourprojects && cd dropyourprojects
$ git clone [git-repo-url] .
```

```sh
$ virtualenv env 
$ source bin/activate
```

```sh
$ pip install -r requirements.txt
```

```sh
$ cd src
$ python manage.py migrate
```

```sh
$ python manage.py createsuperuser
```

```sh
$ python manage.py runserver
```
