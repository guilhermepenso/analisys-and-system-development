Program numero_aleatorio_letra;  
	var
		n1, n2, n3, n4, n5: integer;
		c1, c2, c3, c4, c5: string;
Begin                      
	n1 := random(65);
	n2 := random(65);
	n3 := random(65);
	n4 := random(65);
	n5 := random(65);
	// ASCII A=97   -  Z=122   -> tem q limitar os caracteres para formar só letras ??
	c1 := chr(n1);
	c2 := chr(n2);
	c3 := chr(n3);
	c4 := chr(n4);
	c5 := chr(n5);
	
	writeln(concat(c1, c2, c3, c4, c5));
	  
End.