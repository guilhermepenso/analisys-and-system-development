Program delay_posicionamento;
Begin
	gotoxy (12,2);
	writeln('Olá pessoal...');
	delay(1000);
	clrscr; //clear screen 
	
	gotoxy (4,4);
	writeln('...ainda estou executando...');
	delay(1000);
	clrscr;
	
	gotoxy (6,6);
	writeln('...vou agora terminar.');
	delay(1000);
	clrscr;
	
	gotoxy (8,8);
	writeln('Fim.');
	delay(1000);
	clrscr;
	
	gotoxy (10,10);
	writeln('Tchau!!!!');
	delay(1000);
End.