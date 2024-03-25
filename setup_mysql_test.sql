-- Created a server of mysql for this project.
-- Created a database called 'hbnb_test_db' in the server.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;

USE hbnb_test_db;
-- Created a new user in this database with its respective password.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- We give all privileges to the user 'hbnb_test' on the database 'hbnb_test_db'.
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- We give privilege to 'hbnb_dev' in the performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
