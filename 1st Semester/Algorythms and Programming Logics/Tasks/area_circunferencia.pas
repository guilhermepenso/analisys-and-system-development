Program Pzim ;
	var
		ac, r: real;
		
	const
		PI=3.14;
Begin
	write ('Qual o raio do círculo(m): ');
	read (r);
	ac := 2*PI*sqr(r);
	write ('A área da circunferência é de: ', ac); 
  
End.