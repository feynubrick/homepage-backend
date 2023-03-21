# Requirements

1. `.env` file
2. Pyenv
3. Docker and Docker Compose

## `.env` file

Please refer to `.env.template` file to make your own `.env` file.
`.env` file should be placed on the project root directory

## Pyenv

I recommend you to use "pyenv" to match the python version for this repo.
The version can be automatically set using "pyenv".
To do that, the matching version should already be installed on you "pyenv".
The version is specified in `.python-version` file in the root directory.

## Docker and Docker Compose

If you want to deploy this server, it is recommended to use Docker.
Using Docker Compose, you can run your server with NginX.

# How to run

## Using `.env` file

You can use `.env` file to load the environment variables needed by the following command:

```
$ set -a; source .env; set +a;
```

`local.env` and `production.env` files are prepared for examples.
If you want to use it as your `.env` file, please do not use it as-is.
After you modify it as you want, use one of the following commands to make `.env` file from it.

```
$ cp local.env .env 
```

OR

```
$ cp production.env .env
```

## Using "venv" to make virtual environment

You can make and use a virtual environment using following command:

```
$ python -m venv venv
$ source venv/bin/activate
```

### Installing Packages Required: `requirements.txt`

Then, you can install python packages required for this repo.

```
$ pip install -r requirements.txt
```

### run server

A script to run server is provided in this repo: `run.sh`.
You can execute it by `./run.sh` command.

## Using "docker-compose"

You can run server by the following command:

```
$ docker compose up --build --detach
```