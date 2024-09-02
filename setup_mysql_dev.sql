-- sql script


CREATE DATABASE IF NOT EXISTS flask_project_db;
    CREATE USER IF NOT EXISTS 'flask-user'@'localhost' IDENTIFIED BY 'flask_pwd';
        GRANT ALL PRIVILEGES ON flask_project_db.* TO 'flask-user'@'localhost';
            GRANT SELECT ON performance_schema.* TO 'flask-user'@'localhost';
FLUSH PRIVILEGES;