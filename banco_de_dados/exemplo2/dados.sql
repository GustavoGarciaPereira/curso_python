CREATE DATABASE varejo;
USE varejo;


CREATE TABLE clientes (
    cliente_id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    telefone VARCHAR(15),
    email VARCHAR(100),
    cidade VARCHAR(50),
    estado VARCHAR(2)
);

CREATE TABLE comandas (
    comanda_id INT PRIMARY KEY AUTO_INCREMENT,
    cliente_id INT NOT NULL,
    data_comanda DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(cliente_id)
);

CREATE TABLE pedidos (
    pedido_id INT PRIMARY KEY AUTO_INCREMENT,
    comanda_id INT NOT NULL,
    item VARCHAR(100) NOT NULL,
    quantidade INT NOT NULL,
    preco_unitario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (comanda_id) REFERENCES comandas(comanda_id)
);

-- Inserindo clientes
INSERT INTO clientes (nome, telefone, email, cidade, estado) VALUES
('Alice Santos', '11988887777', 'alice@gmail.com', 'São Paulo', 'SP'),
('Bruno Silva', '21988887777', 'bruno@gmail.com', 'Rio de Janeiro', 'RJ'),
('Carla Mendes', '31988887777', 'carla@gmail.com', 'Belo Horizonte', 'MG');

-- Inserindo comandas (cada cliente tem uma comanda)
INSERT INTO comandas (cliente_id, data_comanda, status) VALUES
(1, '2024-10-20', 'Fechada'),
(2, '2024-10-21', 'Fechada'),
(3, '2024-10-22', 'Aberta');

-- Inserindo pedidos
INSERT INTO pedidos (comanda_id, item, quantidade, preco_unitario) VALUES
(1, 'Pizza', 2, 35.00),
(1, 'Refrigerante', 2, 5.50),
(2, 'Salada', 1, 15.00),
(2, 'Suco', 1, 7.50),
(3, 'Frango Grelhado', 1, 30.00),
(3, 'Água', 1, 3.00);




SELECT * from clientes;


SELECT p.*,
(SELECT comanda_id  from comandas WHERE p.comanda_id = comanda_id),
(SELECT status  from comandas WHERE p.comanda_id = comanda_id)
from pedidos p;


SELECT SUM(preco_unitario * quantidade),
(SELECT comanda_id  from comandas WHERE p.comanda_id = comanda_id) as comandas
from pedidos p 
GROUP BY(p.comanda_id);



SELECT 
    c.comanda_id,
    c.status,
    SUM(p.preco_unitario * p.quantidade) AS valor_total
FROM 
    pedidos p
Inner JOIN 
    comandas c ON p.comanda_id = c.comanda_id
WHERE 
    p.comanda_id = 3
GROUP BY 
    c.comanda_id, c.status;


SELECT 
    c.comanda_id,
    c.status,
    (SELECT SUM(p.preco_unitario * p.quantidade)
     FROM pedidos p
     WHERE p.comanda_id = c.comanda_id) AS valor_total
FROM 
    comandas c
WHERE c.status = "Aberta";


SELECT comanda_id  from comandas;
SELECT *  from pedidos where comanda_id = 3;
SELECT * from comandas WHERE comanda_id = 3;

INSERT INTO pedidos (comanda_id, item, quantidade, preco_unitario) VALUES 
(3, "seveja", 2, 11.0)



SELECT GROUP_CONCAT(item) FROM pedidos GROUP BY(comanda_id);
SELECT GROUP_CONCAT(item SEPARATOR ', ') AS lista_itens
FROM pedidos
WHERE item IS NOT NULL AND TRIM(item) <> ''
GROUP BY(comanda_id);

SELECT comanda_id, GROUP_CONCAT(item) AS itens, SUM(quantidade) AS total_quantidade, SUM(quantidade * preco_unitario) AS total_valor
FROM pedidos
GROUP BY comanda_id;

drop Table pedidos;
drop Table comandas;

drop Table clientes;



