Program numero_aleatorio_readkey;
	var
		c: char;
Begin
	writeln('Please press a key: ');
	c := readkey;	            
	writeln('Voce pressionou ', c, ', cujo valor ASCII é ', ord(c), '.');
End.