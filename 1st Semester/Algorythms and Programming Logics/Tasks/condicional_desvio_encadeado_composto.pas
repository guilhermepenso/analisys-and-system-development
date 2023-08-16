Program condicional _desvio_encadeado_composto;
	var
		condicao1, condicao2: boolean;
Begin
	condicao1 := true;
	condicao2 := true;
	
	if (condicao1) then
		if (condicao2) then
			writeln (condicao1,' ', condicao2, 'linha 12'); 
		else
			writeln (condicao1,' ', condicao2, 'linha 14');
	else
		writeln (condicao1,' ', condicao2, 'linha 16'); 
End.