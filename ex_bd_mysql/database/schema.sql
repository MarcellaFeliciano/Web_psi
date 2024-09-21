-- Criar tabela usuarios


DROP TABLE IF EXISTS tb_usuarios;

CREATE TABLE tb_usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);