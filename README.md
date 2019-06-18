# simple_spider
课设


# Clone or Download the project
> ...
```bash
git clone https://github.com/windski/simple_spider.git
cd simple_spider
```

# Environments Setup

Install Virtual Python Environments, I use `virtualenv`

```bash
pip install virtualenv
virtualenv venv
```

activate the environments
```bash
source venv/bin/activate
```

Then install the dependences
```bash
pip install -r requirements.txt
```

# Create the database and fetch data
execute the `connectdb.py` by the following command
```bash
python connectdb.py
```
The database file will appear in the root folder of the project. There is a database file ending with `sqlite3`.

Then, execute the `spider.py` by 
```bash
python spider.py
```
Waiting for the crawler to get the data, with normal exit.

# Launch application
just type the command

```bash
python manage.py runserver
```

then done.


