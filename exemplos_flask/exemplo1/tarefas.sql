
CREATE DATABASE tasks_db;
USE tasks_db;




CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    task TEXT NOT NULL
);




SELECT * FROM tasks;

INSERT INTO tasks (task) VALUES ("cadastrar certificados");




DELETE from tasks WHERE id=1;