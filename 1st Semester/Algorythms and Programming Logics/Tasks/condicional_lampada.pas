Program condicional_lampada ;
	var
		lamp: char;
Begin
	writeln ('A l�mpada est� queimada? [S/N]: ');
	read (lamp);
	
	if (lamp = 'S') then
		begin	
			writeln ('A l�mpada precisa ser trocada');
		end
	else
		if (lamp = 'N') then
			begin
				writeln ('A l�mpada est� ligada');
			end	
End.