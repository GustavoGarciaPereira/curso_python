-- Active: 1731066669296@@127.0.0.1@3306@saude

create DATABASE saude;
use saude;


CREATE TABLE pessoas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    idade INT NOT NULL,
    peso FLOAT NOT NULL,
    altura INT NOT NULL,
    sexo ENUM('homem', 'mulher') NOT NULL,
    imc FLOAT NOT NULL
);


SELECT * FROM pessoas;

