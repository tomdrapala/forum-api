# API discussion forum

Django web application providing an API for a simple discussion service (discussion forum with a single thread).   

**Tech Stack:** Django, Django Rest Framework


## Installation

A virtual environment such as [venv](https://docs.python.org/3/library/venv.html) is recommended.

> python3 -m venv \<environment-name\>

Environment activation on Linux/Mac:
> source \<environment-name\>/bin/activate

Environment activation on Windows:
> \<environment-name\>\Scripts\activate.bat

Required libraries are listed in the **requirements.txt** file included in this repository.  
**After activating** the environment run: 

> pip install -r requirements.txt

Repository includes a sample SQLite database, that could be used for testing purposes.  
If you wish to start with a fresh one please delete file **db.sqlite3**, and run:
> python manage.py makemigrations

The app is running on a local server (by default http://127.0.0.1:8000/) that can be started by running:
> python manage.py runserver



## Endpoints
 
- **api/users/** - user list
- **api/users/\<id\>/** - user details
- **api/user-create/** - user creation
- **api/posts/** - post list
- **api/posts/\<id\>/** - post details
- **api/posts/\<id\>/like/** - post like


## CURL Examples

Post list:
> curl http://127.0.0.1:8000/api/posts/

Post creation (by authenticated user):
> curl -u \<username\> -X POST http://127.0.0.1:8000/api/posts/ -H "Content-Type: application/json" -d '{"title":"\<post-title\>","text":"\<post-content\>"}'

Post update (by post author):
> curl -u \<username\> -X PATCH http://127.0.0.1:8000/api/posts/[id]/ -H "Content-Type: application/json" -d '{"\<parameter\>":"\<new-value\>"}'

Post deletion (by post author):
> curl -u \<username\> -X DELETE http://127.0.0.1:8000/api/posts/[id]/

Liking a post (by authenticated user):
> curl -u \<username\> -X POST http://127.0.0.1:8000/api/posts/[id]/like/

User list (by authenticated user):
> curl -u \<username\> http://127.0.0.1:8000/api/users/

Following endpoint is for user creation. This solution is not perfect, and **I would not use nor recommend using it in a real project**.
It was created just to enable fast and easy User creation method, to facilitate application testing.
> curl -X POST http://127.0.0.1:8000/api/user-create/ -H "Content-Type: application/json" -d '{"username":"\<username\>","password":"\<password\>"}'
