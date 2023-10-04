Program condicional_lampada ;
	var
		lamp: char;
Begin
	writeln ('A lâmpada está queimada? [S/N]: ');
	read (lamp);
	
	if (lamp = 'S') then
		begin	
			writeln ('A lâmpada precisa ser trocada');
		end
	else
		if (lamp = 'N') then
			begin
				writeln ('A lâmpada está ligada');
			end	
End.