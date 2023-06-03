import multiprocessing
import os

from dotenv import load_dotenv


load_dotenv()

# Get the `ENVIRONMENT` env variable and convert it to lowercase if it exists
environment = os.getenv("ENVIRONMENT")
environment = environment.lower() if environment else "dev"


# Gunicorn app
# Tell Gunicorn which application to run
wsgi_app = "app.main:app"

# Requests
# Restart workers after so many requests, with some variability.
max_requests = 1000
max_requests_jitter = 50

# Logging
# Use stdout for logging
log_file = "-"

# Workers
bind = "0.0.0.0:{{ cookiecutter.gunicorn_port }}"

# Use this formula for production, otherwise only run 2 workers
workers = (
    multiprocessing.cpu_count() * 2 + 1
    if environment in ["prod", "production"]
    else 2
)
worker_class = "uvicorn.workers.UvicornWorker"
