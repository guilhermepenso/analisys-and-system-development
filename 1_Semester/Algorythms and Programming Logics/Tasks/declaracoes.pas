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
	
	writeln ('O valor Inteiro é: ', numeroInteiro);
	writeln ('O valor Real é: ', numeroReal);
	writeln ('O valor Caractere é: ', valorCaractere);
	writeln ('O valor String é: ', valorString);
	writeln ('O valor Lógico é: ', valorLogico);
	writeln ('O valor Constante de PI é: ', PI);  
End.