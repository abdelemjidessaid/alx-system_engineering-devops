CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6 (
	id INT PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(50)
);

GRANT SELECT, INSERT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

INSERT INTO nexus6 (name) VALUES ("Essaid"), ("Sharpminded"), ("Heroshima");

SELECT * FROM nexus6;
