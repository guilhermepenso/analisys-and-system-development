Program condicional_desvio_simples;
	var
		nota1, nota2, media: real;
Begin
	writeln ('Entre com um valor da primeira nota: ');
	read (nota1);  
	writeln ('Entre com um valor da segunda nota: ');
	read (nota2);
	
	media := (nota1 + nota2) / 2;
	
	if (media >= 7.0) then
		begin // begin e end para dois ou mais linhas de comando, uma só pode ser sem nenhum dos dois
			writeln ('Aprovado');
		end
	else
		if (media >= 5.0) and (media <= 6.9) then
			begin
				writeln ('Recuperacao');
			end
		else
			begin
				writeln ('Reprovado');
			end
End.