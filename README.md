# Internal API - Gateway

### Introduction
The **Gateway** service is one of **ECOM** services. Its objective is to process incoming
requests by directly executing them or dispatch them to corresponding services. In this guide, we
will demonstrate how to install and run this application in our local machine.

### Installation
Before we begin we must make sure the following requirements are installed and running.
- python 3.8+
- pip 3+
- docker

Depending on you operating system install/update the above requirements.

With `virtualenv` installed, we can start forming our application. Let's create and move into a
new directory:

	$ mkdir gateway
	$ cd gateway

Create an empty *git* repo:

    $ git init

Add remote origin:

	$ git remote add origin https://github.com/-

Now let's pull:

	$ git pull

Switch to 'develop' branch:

	$ git checkout develop


### Setup the Application
We are going to build the docker compose project:

    $ cd deployment
	$ docker-compose build

Create and open a *.env* file:

	$ vim .env

Write the following:

    api_env=development
    secret_key=
    pg_db_name=e_gateway
    pg_db_user=postgres
    pg_db_pass=1234
    pg_db_host=localhost
    pg_db_port=5432
    
    sentry_dsn=
    
    redis_host=localhost
    redis_port=6379
    
    customers_host=http://localhost:8001
    customers_key=
    
    catalog_host=http://localhost:8002
    catalog_key=


We have successfully finished setting up and configuring our **Gateway** service.

### Running the Application
make sure you're in the `deployment` directory

	docker-compose up


### Running Migrations
Open a bash session inside the gateway container
    
    docker-compose exec gateway /bin/bash

    $ ./scripts/makemigrations
    $ ./scripts/migrate


# Running without docker
>running without docker-compose is not recommend

run the fastapi application using uvicorn

    $ uvicorn main:app --port 8000 --debug
