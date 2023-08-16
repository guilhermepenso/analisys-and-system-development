Program Conversor_Graus_C_para_F ;
	var
		c, conv: real;
Begin
	write ('Quantos °C está agora?: ');
	read (c);
	conv := (c*1.8) + 32;
  write (C:0:0, '°C é igual a: ', conv:0:2, '°F');
  
End.