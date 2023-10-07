Program Pzim ;
	var
		i: integer;
		nota: array[1..3] of real;
		med: real;
Begin     
	for i := 1 to 3 do
		begin
			if (i = 1) then	
					write ('Digite o RA: ')
				else   
					begin
					write ('Informe a nota ', i-1, '..: ');
				end;
		 	read(nota[i]);
		end;
		med:= ((nota[2] + nota[3]) / 2);
		writeln ('RA: ', nota[1]:0:0);
		writeln ('Média: ', med:0:1);
		if (med >= 7) then
			write ('Aprovado')
		else
			write ('Reprovado');
End.