#!/
-– Create Database
CREATE DATABASE IF NOT EXISTS Ihbnb_dev_db
-- Create new user
CREATE USER hbnb_dev@localhost IDENTIFY BY hbnb_dev_pwd;
-- Grant priviledge
GRANT ALL PRIVILEGE ON hbnb_dev_db TO hbnb_dev@localhost;
-- GRANT SELECT ON performance_schema TO hbnb_dev;
