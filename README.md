# App Budget

## Description

This repository holds the source code for App Budget. App Budget is a CRUD Web API that I created for transaction tracking and budgeting using Python, FastAPI and SQL. It is deployed to Azure using docker and GitHub Actions. You can access the app documentation [here] (TODO).

## I'm completely lost, where should I start?

If you want to **consume the API**, check the API documentation [here] (TODO).

If you want to **set up the project** on your machine for developing, check the [... Set up using devcontainer (Option 1)](#set-up-the-project-using-devcontainer-option-1), [... Set up like in the old days (Option 2)](#set-up-the-project-like-in-the-good-ol-days-option-2) and [... Serve locally](#serve-the-app-locally) sections.

If you want to **understand the code**, check the `app/main.py` file and the `app/router/` folder.

## How to ...

### ... Set up the project using devcontainer (Option 1)

You can develop the project inside a development container by following these steps in VSCode:

1. Open VSCode
1. Install the [devcontainer](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension
1. Open the command palette (press `F1` key), select the command "Git: Clone" and clone this repository https://github.com/GiuseppeTT/app-budget.git
1. Open the command palette (press `F1` key) and select the command "Dev Containers: Open Folder in Container..."

After that, the project will be all set up.

> Note: You may need to install [docker](https://www.docker.com/).

> Note: You can check more instructions on the [devcontainer documentation](https://code.visualstudio.com/docs/devcontainers/containers)

### ... Set up the project like in the good ol' days (Option 2)

You can develop the project like in the good ol' days. To do that, follow these steps:

1. Open your favorite IDE (perhaps a terminal)
1. Clone this repository https://github.com/GiuseppeTT/app-budget.git
1. Install poetry `python -m install poetry`
1. Install python dependencies `. script/install-packages.sh`
1. Activate the virtual environment `. script/activate-poetry.sh`

After that, the project will be all set up.

> Note: You may need to run `. script/activate-poetry.sh` every time to activate the python virtual environment. Some IDEs have feature to permanently set up a python interpreter based on a virtual environment to avoid this work.

### ... Test the app

To test the app, simply run `. script/test-app.sh`

### ... Lint / format the pythons files

To format the python files, simply run `. script/format-python-files.sh`

To format the python types, simply run `. script/lint-python-files.sh`

To format the python files, simply run `. script/lint-python-files.sh`

### ... Serve the app locally

To serve the app locally, simply run `. script/serve-locally-app.sh`

After that, you can check the endpoints at `TODO`.

### ... Build the docker image and run locally

To build the docker image and run it locally to serve the app, simply run `. script/build-docker-image.sh` and then `. script/build-docker-image.sh`

After that, you can check the endpoints at `TODO`.

### ... Deploy

TODO.

## Project structure

```
.
├── .devcontainer/           # Devcontainer's config
├── .git/                    # [Git ignored] [Auto generated] Git files
├── .github/workflows/       # GitHub Actions's workflows (CI / CD)
├── .mypy_cache/             # [Git ignored] [Auto generated] Mypy's cache
├── .pytest_cache/           # [Git ignored] [Auto generated] Pytest's cache
├── .venv/                   # [Git ignored] [Auto generated] Python virtual environment
├── .vscode/                 # VSCode's config
├── app                      # App's code
│   ├── crud                 # CRUD's code
│   ├── model                # Model's code (input data, output data, database data and update data)
│   ├── router               # Endpoints's code
│   └── test                 # App's tests
│       ├── crud             # CRUD's tests
│       └── router           # Endpoints's tests
│   ├── database.py          # Database's code
│   ├── dependency.py        # Dependency injection's code
│   └── main.py              # Responsible for defining the app and connecting all the app's code
├── script/                  # Auxiliary scripts
├── .gitignore               # List of files ignored by git
├── .pre-commit-config.yaml  # pre-commit's config
├── Dockerfile               # Docker image instructions
├── LICENSE                  # Project's license
├── README.md                # This very file you are reading
├── budget.db                # [Git ignored] SQLite database
├── debug.py                 # [Git ignored] An auxiliary script for debugging, like a whiteboard
├── poetry.lock              # [Auto generated] Python dependency versions
├── poetry.toml              # [Auto generated] Poetry's config
├── pyproject.toml           # Project's config
```
