Program Declaracoes;     
	var               
		numeroInteiro: integer;
		numeroReal: real;
		valorCaractere: char;
		valorString: string;
		valorLogico: boolean;
		
	Const
		PI = 3.14159;
		
Begin
	
	numeroInteiro := 1;
	numeroReal := 1.1; 
	valorCaractere := 'a';
	valorString := 'abc';
	valorLogico := true;
	
	writeln ('O valor Inteiro �: ', numeroInteiro);
	writeln ('O valor Real �: ', numeroReal);
	writeln ('O valor Caractere �: ', valorCaractere);
	writeln ('O valor String �: ', valorString);
	writeln ('O valor L�gico �: ', valorLogico);
	writeln ('O valor Constante de PI �: ', PI);  
End.