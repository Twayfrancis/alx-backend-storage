-- script that creates table users
-- id, int, never null, auto increment and primary key
-- email, string(255), never null and unique
-- name, string(255)
-- country, enumearation of countries: US, CO, and TN, never null

CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM ('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
