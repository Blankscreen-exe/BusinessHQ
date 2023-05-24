# BusinessHQ
makeshift  readme. will do a better one afterwards

## Installation
1- In your terminal, go inside your preferred directory and run the following

    mkdir BHQ
    cd BHQ
    git clone https://github.com/Blankscreen-exe/BusinessHQ.git

2- rename the `.env example` file inside `./business_hq/business_hq`  to `.env` (with a dot at the beginning)

3- once the download is complete, create a virtual environment and activate it.

	virtualenv venv
	
	# if on windows
	./venv/Scripts/activate
	
	# if on linux/mac
	source venv/bin/activate

3- after activating the virtual environment install the dependencies

    cd business_hq
    pip install -r requirements.txt

4- run the migrations to create tables in the database

    python manage.py migrate

5- while inside the first `business_hq` folder, create your superuser. Give it any password or email you like.

    python manage.py createsuperuser

6- after the creating your superuser, run the server

    python manage.py runserver
    
7- visit the URL `localhost:8000/admin/` and use the credentials of the superuser you created to be able to see the admin panel. Some routes are also working including `JWT authentication`.


## Routes for User's JWT authentication

1- user register
```
http://localhost:8000/api/v1/users/register/
```

2- user login
```
http://localhost:8000/api/v1/users/login/
```
3- get token
```
http://localhost:8000/token/
```

4- token refresh
```
http://localhost:8000/token/refresh/
```