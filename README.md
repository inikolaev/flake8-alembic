# flake8-alembic

Flake8 plugin for checking Alembic migrations. Currently it only checks if index is being created concurently or not.

### How to test 

#### Create and activate virtual environment

```bash
python3 -m venv ~/.local/share/virtualenvs/flake8-alembic
source ~/.local/share/virtualenvs/flake8-alembic/bin/activate
```

#### Install `flake8`

```bash
pip install flake8
```

#### Install plugin 

Install plugin from the working directory

```bash
pip install -e .
```

and verify that `flake8` can find it

```bash
flake8 --help | grep 'Installed plugins'
```

Now it should be possible to run plugin against some code.

### Possible improvements

* Currently plugin will run against each file - wonder if there's a way to limit it to the alembic directory