import os

DB_HOST = os.getenv('POSTGRES_HOST', 'db')
DB_NAME = os.getenv('POSTGRES_DB', 'mydatabase')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'mypassword')
DB_PORT = os.getenv('POSTGRES_PORT', '5432')
DB_USER = os.getenv('POSTGRES_USER', 'myuser')
