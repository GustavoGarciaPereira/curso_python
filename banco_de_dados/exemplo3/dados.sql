-- Criação da Tabela Clientes
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Cidade VARCHAR(50) NOT NULL
);

-- Inserção de Dados na Tabela Clientes
INSERT INTO Clientes (ClienteID, Nome, Email, Cidade) VALUES
(1, 'Ana Silva', 'ana@exemplo.com', 'São Paulo'),
(2, 'Bruno Costa', 'bruno@exemplo.com', 'Rio de Janeiro'),
(3, 'Carla Souza', 'carla@exemplo.com', 'Belo Horizonte'),
(4, 'Daniel Lima', 'daniel@exemplo.com', 'Curitiba');

-- Criação da Tabela Produtos
CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Estoque INT NOT NULL
);

-- Inserção de Dados na Tabela Produtos
INSERT INTO Produtos (ProdutoID, NomeProduto, Preco, Estoque) VALUES
(1, 'Laptop', 3500.00, 10),
(2, 'Smartphone', 1500.00, 25),
(3, 'Tablet', 1200.00, 15),
(4, 'Monitor', 800.00, 20);

-- Criação da Tabela Pedidos
CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY,
    ClienteID INT,
    ProdutoID INT,
    DataPedido DATE NOT NULL,
    Quantidade INT NOT NULL,
    FOREIGN KEY (ClienteID) REFERENCES Clientes(ClienteID),
    FOREIGN KEY (ProdutoID) REFERENCES Produtos(ProdutoID)
);

-- Inserção de Dados na Tabela Pedidos
INSERT INTO Pedidos (PedidoID, ClienteID, ProdutoID, DataPedido, Quantidade) VALUES
(101, 1, 1, '2024-01-15', 2),
(102, 2, 2, '2024-02-20', 1),
(103, 1, 3, '2024-03-05', 3),
(104, 3, 4, '2024-04-10', 1);
-- O PedidoID 105 causará erro devido ao ClienteID inexistente
-- (105, 5, 2, '2024-05-12', 2);


--Exercício 1: Listar os Pedidos com Detalhes dos Clientes e Produtos
SELECT 
    Pedidos.PedidoID,
    Clientes.Nome AS NomeCliente,
    Produtos.NomeProduto,
    Pedidos.Quantidade,
    Pedidos.DataPedido
FROM 
    Pedidos
INNER JOIN 
    Clientes ON Pedidos.ClienteID = Clientes.ClienteID
INNER JOIN 
    Produtos ON Pedidos.ProdutoID = Produtos.ProdutoID
WHERE 
    Clientes.ClienteID IS NOT NULL
    AND Produtos.ProdutoID IS NOT NULL;


-- Exercício 2: Encontrar Todos os Pedidos de um Cliente Específico
SELECT 
    Pedidos.PedidoID,
    Produtos.NomeProduto,
    Pedidos.Quantidade,
    Pedidos.DataPedido
FROM 
    Pedidos
INNER JOIN 
    Produtos ON Pedidos.ProdutoID = Produtos.ProdutoID
WHERE 
    Pedidos.ClienteID = 1;



--  Consulta para verificar se o PedidoID 105 causará erro


Exercício 3: Listar Clientes que Compraram um Produto Específico
SELECT 
    Clientes.Nome AS NomeCliente,
    Pedidos.PedidoID,
    Pedidos.Quantidade,
    Pedidos.DataPedido
FROM 
    Pedidos
INNER JOIN 
    Clientes ON Pedidos.ClienteID = Clientes.ClienteID
WHERE 
    Pedidos.ProdutoID = 2;
