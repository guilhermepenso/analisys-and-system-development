Program Idade ;
	var
		nome: string;
		nasc, idade: integer;
		
	const
		ano = 2023;
Begin
	write ('Qual o seu nome? ');
	readln (nome);
	write ('Qual seu ano de nascimento? ');
	readln (nasc);
	idade := ano - nasc;
	write ('Ol� ', nome, ', voc� tem ', idade, ' anos');
End.