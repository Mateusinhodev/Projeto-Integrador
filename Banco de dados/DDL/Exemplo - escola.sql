-- Criação do Banco de Dados
CREATE DATABASE escola;

-- Selecionar o BD para uso
USE escola;

-- Criar tabela alunos 
-- Armazena os dados dos estudantes
CREATE TABLE alunos(
	-- Identificador únido (PK - chave primária)
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Nome completo do aluno (obrigatório - NOT NULL)
    nome VARCHAR(100) NOT NULL,
    
    -- Data de nascimento
    data_nascimento DATE NOT NULL,
    
    -- CPF único p/ cada aluno (Restição de unicidade - UNIQUE)
    cpf VARCHAR(14) UNIQUE,
    
    -- Email do aluno
    email VARCHAR(100) NOT NULL UNIQUE,
    
    -- Telefone de contato
    telefone VARCHAR(20) NOT NULL,
    
    -- Data em que o aluno foi matriculado
    data_matricula DATE NOT NULL
);

-- Tabela Professores
-- Armazena os dados dos professores

CREATE TABLE professores(
	-- Identificador único professor
    id_professor INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Nome do professor (Obrigatório - NOT NULL)
    nome VARCHAR(100) NOT NULL,
    
    -- Área de especialização (ex: Matemática, Informática)
    especialidade VARCHAR (100) NOT NULL,
    
    -- Email do professor
    email VARCHAR(100) NOT NULL UNIQUE,
    
    -- Telefone de contato
    telefone VARCHAR(20)
);

-- Tabela de Cursos
-- Representa cursos oferecidos pela escola

CREATE TABLE cursos(
	-- Identificador único do curso
    id_curso INT AUTO_INCREMENT PRIMARY KEY,
    
    -- Nome do curso (obrigatório - NOT NULL)
    nome VARCHAR(100) NOT NULL,
    
    -- Carga horária total do curso em horas
    carga_horaria INT NOT NULL
);