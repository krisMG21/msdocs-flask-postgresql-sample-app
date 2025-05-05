import os

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

def main():
    print(DATABASE_URI)
    pass

if __name__ == "__main__":
    main()

# This code is a configuration file for a development environment in a Python application.
# It sets up the database connection string using environment variables for security.
# The connection string is formatted for PostgreSQL using the psycopg2 driver.