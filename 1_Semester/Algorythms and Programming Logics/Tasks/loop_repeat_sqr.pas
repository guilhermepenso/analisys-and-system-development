Program loop_repeat_sqr;
	var
		n, r: integer;
		decision: char;
Begin
	decision := 'N';
	repeat
		write ('Informe um n�mero inteiro: '); 
		readln (n);
		r := n * n;
		writeln ('O valor de ', n, ' ao quadrado �: ', r);
		write ('Deseja encerrar? [S/N]: ');
		read (decision);
	until (decision = 'S');
	writeln ('FIM')
		 
End.