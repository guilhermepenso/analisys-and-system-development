Program loop_divider ;
	var
		x: real;
		y: integer;
Begin
	write ('Digite um valor a ser dividido: ');
	read (x); 
	
	while (x >= 5) do
		begin
			write (x:0:2, ' / 2 = ');
			x := x/2;
			write (x:0:2);
			inc(y);
			writeln (' (Foi realizado ', y ,' divisoes sucessivas)');
		end 
End.