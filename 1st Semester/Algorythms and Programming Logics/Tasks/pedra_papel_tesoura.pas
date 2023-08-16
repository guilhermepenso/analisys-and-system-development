Program pedra_papel_tesoura;
	const
		pedra = 0;
		papel = 1;
		tesoura = 2;
	var
		jogada, pc: integer;
		fim: boolean;
		resp: char;
Begin
	repeat
	  clrscr;
		writeln ('Pedra, Papel Tesoura');
		writeln ('--------------------');
		writeln ('----[1] Pedra ------');
		writeln ('----[2] Papel ------');
		writeln ('----[3] Tesoura ----');
		writeln ('--------------------');
		read (jogada);
		jogada := (jogada - 1);		
		if (jogada < 0) or (jogada > 2) then
			begin
				clrscr;
				delay (500);
				writeln ('Jogada Inválida');
			end
		else
			begin
				pc := random(3);
				if (jogada = pc) then
					begin
						writeln('Empate');
					end
				else 
					if ((jogada = 1) and (pc = 3)) or ((jogada = 2) and (pc = 1)) or ((jogada = 3) and (pc = 2)) then
						begin
							writeln('Humano Ganhou!!');	
						end
					else
					writeln ('Humano Perdeu!!');	
		writeln;
		writeln('-------------------------');
		write('Deseja continuar? [S/N]: ');
		read(resp);
	until (resp = 'N') or (resp = 'n');  
End.