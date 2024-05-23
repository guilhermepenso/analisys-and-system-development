CREATE TABLE cliente(
	cpf BIGINT NOT NULL,
	nome VARCHAR(50) NOT NULL,
	sobrenome VARCHAR(50) NOT NULL,
	PRIMARY KEY(cpf)
);

CREATE TABLE excursao(
	id INT NOT NULL,
	nome VARCHAR(50) NOT NULL,
	num_dias INT NOT NULL,
	guia_matricula BIGINT NOT NULL,
	PRIMARY KEY(id),
	CONSTRAINT fk_excursao_guia_matricula
		FOREIGN KEY (guia_matricula) REFERENCES guia(matricula)
);

CREATE TABLE cidade(
	codigo INT NOT NULL,
	nome VARCHAR(50) NOT NULL,
	PRIMARY KEY(codigo)
);

CREATE TABLE guia(
	matricula BIGINT NOT NULL,
	nome VARCHAR(50) NOT NULL,
	sobrenome VARCHAR(50) NOT NULL,
	PRIMARY KEY(matricula)
);

CREATE TABLE inscricao (
	cliente_cpf BIGINT NOT NULL,
	excursao_id INT NOT NULL,
	data DATE NULL,
	PRIMARY KEY(cliente_cpf, excursao_id),
	CONSTRAINT fk_inscricao_cliente_cpf
		FOREIGN KEY (cliente_cpf) REFERENCES cliente(cpf),
	CONSTRAINT fk_inscricao_cliente_id
		FOREIGN KEY (excursao_id) REFERENCES excursao(id)
);

CREATE TABLE parada (
	excursao_id INT NOT NULL,
	cidade_codigo INT NOT NULL,
	dt_saida DATE NULL,
	dt_chegada DATE NULL,
	PRIMARY KEY(excursao_id, cidade_codigo),
	CONSTRAINT fk_parada_excursao_id
		FOREIGN KEY (excursao_id) REFERENCES excursao(id),
	CONSTRAINT fk_parada_excursao_codigo
		FOREIGN KEY (cidade_codigo) REFERENCES cidade(codigo)
);