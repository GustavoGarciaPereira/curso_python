use gustavo_teste;


-- Criação da Tabela Clientes
CREATE TABLE Clientes (
    ClienteID INT PRIMARY KEY,
    Nome VARCHAR(100) NOT NULL,
    Email VARCHAR(100) NOT NULL,
    Cidade VARCHAR(50) NOT NULL
);

-- Inserção de Dados na Tabela Clientes

CREATE TABLE Produtos (
    ProdutoID INT PRIMARY KEY,
    NomeProduto VARCHAR(100) NOT NULL,
    Preco DECIMAL(10, 2) NOT NULL,
    Estoque INT NOT NULL
);


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



--Exercício 1: Listar os Pedidos com Detalhes dos Clientes e Produtos


CREATE VIEW view_pedidos_detalhados AS
SELECT 
    Pedidos.PedidoID,
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




SELECT * FROM view_pedidos_detalhados;
