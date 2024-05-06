Program Pzim ;
	var
		nota, RA: array[1..2] of integer;
		i, c: integer; 
		med: real;
Begin

	c := 1;
	repeat
		clrscr;
		writeln ('Digite o RA: ');
		read (RA[c]);
		for i := 1 to 2 do
		begin
			writeln ('Escreva a ', i, 'ª nota: ');
			read (nota[i]);
		end;	
		med := ((nota[1] + nota[2]) / 2);
		clrscr;               
		writeln ('RA: ', RA[c]);
		writeln ('Média: ', med:0:1); 
		inc (c);
		delay (2000);
	until (c = 3)
	  
End.