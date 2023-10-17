GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

CREATE USER 'replica_user'@'%' IDENTIFIED BY 'abdelemjidessaid';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%' IDENTIFIED BY 'abdelemjidessaid';
FLUSH PRIVILEGES;
