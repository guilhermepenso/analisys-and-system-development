Program Pzim ;
	var
		ac, r: real;
		
	const
		PI=3.14;
Begin
	write ('Qual o raio do c�rculo(m): ');
	read (r);
	ac := 2*PI*sqr(r);
	write ('A �rea da circunfer�ncia � de: ', ac); 
  
End.