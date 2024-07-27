# Some Backend

This is our backend to make a million dollars.

We use `uv` as our python package manager.

## Setup
1. Install python 3.12+ (`pyenv install 3.12`) and activate `pyenv shell 3.12.3`
2. `make setup`

To access `python` and `pip` directly, you can `source .venv/bin/activate`. This is also where your 
interpreter is for the IDE (`.venv/bin/python`).

Otherwise, you can use `uv` to run your tools. Like `uv tool run ipython` for a shell. It will
automatically install any deps temporarily, start the process, and then uninstall them to keep your virtual
env clean.

## Python setup

We use `uv` to manage packages, but it's not a totally complete tool yet. So we manage our lockfile
a bit manually. Here's how.

### Installing packages
`uv` doesn't have a `uv add` yet, so simply add the package to the pyproject.toml and run `make sync`. This will install 
the package and update the lock file

You cannot accidentally push a bad change to main, because during the PR, a check will be made to see if the `requirements.lock` 
and `requirements.dev.lock` are in sync with pyproject.toml. It will fail the PR test if not.

## Format, Lint, Test
Simply `make` them (`make format`, `make lint`, `make test`)

## Docker
The image is an alpine python build because the ubuntu python image was a lot larger and had 2 "Critical" security bugs. 

Build the API with `docker compose build` and run with `docker compose up`. API is running at http://localhost:8000/docs

You can interactively run the image with:
`docker run -it --entrypoint sh -p 8000:8000 --name my-api --rm my-api:latest`

This will drop you into a shell in api. You should have a virtual env at `.venv` and you can run
`source .venv/bin/activate` in the image to get your python packages.