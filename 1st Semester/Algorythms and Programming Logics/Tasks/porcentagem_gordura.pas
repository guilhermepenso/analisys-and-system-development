Program Porcentagem_de_Gordura ;
	var
		peso, gord, prot: real;
Begin
	write ('Peso da Carne(g): ');
	read (peso);
	prot := (peso * 28) / 100;
	gord := (peso * 18.6) / 100;
	write ('Uma carne de ', peso:0:2,'g contém ',prot:0:2,'g de proteína e ',gord:0:2,'g de gordura');
	  
End.