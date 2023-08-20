-- create test database
CREATE DATABASE IF NOT EXIST hbnb_test_db;
-- create user and password for the test db
CREATE USER IF NOT EXIST 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant priviledge on the database
GRANT ALL PRIVILEGES ON `hbnb_test_db` TO 'hbnb_test'@'localhost';
-- grant priviledges fot performance_schema
GRANT SELECT ON `performance_schema` TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;