## Cookiecutter-FastAPI

This is a [cookiecutter](https://cookiecutter.readthedocs.io/) template for creating [FastAPI](https://fastapi.tiangolo.com/) applications.


### Explanation of variables in cookiecutter.json

|Variable|Explanation|Default value|
|---|---|---|
|project_name|The name of your project||
|project_slug|The name of your project with the spaces replaced with underscores. This is also the name of the folder that will contain your project. **This is automatically calculated.**||
|project_environment|The environment the app is currently running in (`dev`, `prod`). This only affects things like the number of workers running the API.|dev|
|fastapi_title|Name that will be displayed in the API documentation.||
|fastapi_description|Description that will be displayed in the API documentation.||
|fastapi_version|API version that will be displayed in the API documentation.|0.0.1|
|gunicorn_port|Port to run the API on|8000|
|postgres_username|Username to connect to Postgres with||
|postgres_password|Password to connect to Postgres with||
|postgres_database|Postgres database to connect to||
|postgres_host|Server running the Postgres database|localhost|
|postgres_port|Port the Postgres database is listening on|5432|

### How to use this template
1. Create a new project using this template
   1. `cookiecutter gh:andrewguest/cookiecutter-fastapi`
2. Fill in the Cookiecutter prompts
3. cd into the new project folder
   1. `cd <project_slug>`
4. Rename the .env template file
   1. `mv .env.template .env`
5. Create and setup a Python virtual environment
   1. `python -m venv venv`
   2. `source venv/bin/activate`
   3. `pip install -r requirements.txt`
6. Start the database in a Docker container
   1. `docker-compose up`
7. Run the application
   1. `gunicorn`
8. Test out the interactive API documentation at `http://localhost:8000/docs`
9.  Run pytest tests
   1. `pytest`