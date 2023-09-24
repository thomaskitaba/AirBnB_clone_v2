-- Create Database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Create new user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant priviledge
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
-- GRANT SELECT ON performance_schema TO hbnb_dev;
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';
--
FLUSH PRIVILEGES;