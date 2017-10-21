import os

# db conection settings
db_host = os.environ.get('DB_HOST', 'localhost')
db_name = os.environ.get('DB_NAME', 'Pebble_Fitness_Dev')
db_user = os.environ.get('DB_USER', 'postgres')
db_pass = os.environ.get('DB_PASS', 'admin')