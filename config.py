import os

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']
# is_db = os.environ['IS_DB']

user = 'postgres'
password = 'password'
host = '0.0.0.0'
database = 'postgres'
port = 5342
is_db=False

DATABASE_CONNECTION_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'
