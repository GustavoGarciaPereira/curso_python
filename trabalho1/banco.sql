-- Active: 1731020124241@@127.0.0.1@3306
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

INSERT INTO pessoas (nome, idade, peso, altura, sexo, imc) 
VALUES 
    ('João Silva', 30, 80.5, 175, 'homem', 26.3),
    ('Maria Souza', 25, 65.0, 160, 'mulher', 25.4),
    ('Carlos Oliveira', 40, 95.0, 180, 'homem', 29.3);