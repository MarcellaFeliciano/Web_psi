

DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(255) NOT NULL
);


DROP TABLE IF EXISTS consultas;

CREATE TABLE consultas(
    id_consulta INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    dia VARCHAR(100) NOT NULL,
    horario VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    motivo VARCHAR(100) NOT NULL

);

DROP TABLE IF EXISTS ficha_paciente;


CREATE TABLE ficha_paciente(
    id_ficha INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nasc VARCHAR(100) NOT NULL,
    genero VARCHAR(100) NOT NULL,
    endereco VARCHAR(100) NOT NULL,
    telefone VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    motivo VARCHAR(100) NOT NULL,
    data_consulta VARCHAR(100) NOT NULL,
    historico VARCHAR(100) NOT NULL,
    medicamentos VARCHAR(100) NOT NULL
);