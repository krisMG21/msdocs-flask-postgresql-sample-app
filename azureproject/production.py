import os

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.getenv('AZURE_POSTGRESQL_USER'),
    dbpass=os.getenv('AZURE_POSTGRESQL_PASSWORD'),
    dbhost=os.getenv('AZURE_POSTGRESQL_HOST'),
    dbname=os.getenv('AZURE_POSTGRESQL_NAME')
)

def main():
    print(DATABASE_URI)
    pass

if __name__ == "__main__":
    main()

# This code is a configuration file for a production environment in a Python application.
# It sets up the database connection string using environment variables for security.
# The connection string is formatted for PostgreSQL using the psycopg2 driver.
