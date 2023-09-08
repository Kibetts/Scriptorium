import os

# Specify the database file name
db_file = 'scriptorium_base.db'

# Check if the file exists and delete it
if os.path.exists(db_file):
    os.remove(db_file)
