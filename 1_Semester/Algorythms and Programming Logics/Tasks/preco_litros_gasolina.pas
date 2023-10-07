Program Preco_Litros_Gasolina ;
	var
		preco, litro: real;
		         
	const
		rs=5.89;
Begin
	write ('Quantos litros vai ser abastecido? ');
	read (litro);
	preco := (litro * rs);
	write (litro:0:2, ' litros de gasolina ficará R$', preco:0:2);
End.