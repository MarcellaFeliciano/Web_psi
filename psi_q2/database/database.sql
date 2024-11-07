CREATE TABLE IF NOT EXISTS tb_medicos (
    id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS tb_pacientes (
    id_paciente INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_completo TEXT NOT NULL,
    genero TEXT NOT NULL,
    idade INT NOT NULL,
    telefone TEXT NOT NULL
);


CREATE TABLE IF NOT EXISTS tb_consultas (
    id_consulta INTEGER PRIMARY KEY AUTOINCREMENT,
    con_data TEXT NOT NULL,
    con_medico_id INT NOT NULL,
    con_paciente_id INT NOT NULL,
    sintomas TEXT NOT NULL,
    descricao TEXT,
    FOREIGN KEY(con_medico_id) REFERENCES tb_medicos(id_medico),
    FOREIGN KEY(con_paciente_id) REFERENCES tb_pacientes(id_paciente)
);