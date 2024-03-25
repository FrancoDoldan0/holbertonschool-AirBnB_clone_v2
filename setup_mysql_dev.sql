-- Create a Server of MySql for this project
-- Create a new database called 'hbnb_dev_db'.
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Created a new user in this database with its respective password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- We give all privileges to the user 'hbnb_dev' on the database 'hbnb_dev_db'
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- We give privilege to 'hbnb_dev' in the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
