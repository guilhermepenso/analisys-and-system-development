CREATE TABLE IF NOT EXISTS `Empresa`.`Funcionario` (
`cpf` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT, 
`p_nome` VARCHAR(50) NOT NULL, 
`m_nome` VARCHAR(50) NULL 
`sobrenome` VARCHAR(50) NOT NULL, 
`telefone` VARCHAR(11) NULL, 
`salario` DECIMAL(10,2) NULL, 
`dt_nasc_func` DATE NULL, 
`sexo` CHAR(1) NULL, 
`rua` VARCHAR(60) NOT NULL, 
`numero` VARCHAR(15) NULL, 
`complemento` VARCHAR(60) NULL, 
`cidade` VARCHAR(50) NULL, 
`estado` VARCHAR(50) NULL, 
`cep` VARCHAR(8) NULL, 
PRIMARY KEY (`cpf`)
);