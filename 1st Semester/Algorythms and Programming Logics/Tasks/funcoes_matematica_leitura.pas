Program Funcao_Matematica_Leitura;
	var
		h, i, j, k, l: integer;
		r,m, n, o: real;
Begin
	write ('Escreva um n�mero inteiro: ');
	read (h);
	write ('Escreva um n�mero inteiro: ');
	read (i);                           
	write ('Escreva um n�mero inteiro: ');
	read (j);                              
	write ('Escreva um n�mero inteiro: ');
	read (k);
	write ('Escreva um n�mero inteiro: ');
	read (l);

	write ('Escreva um n�mero real: ');
	read (r);
	write ('Escreva um n�mero real: ');
	read (m);
	write ('Escreva um n�mero real: ');
	read (n);
	write ('Escreva um n�mero real: ');
	read (o);
	
	writeln ('(', i,')mod(', j,')..: ',(i)mod(j));	
	writeln ('(', i,')div(', j,')..: ',(i)div(j));
	writeln ('(', k,')mod(', l,')..: ',(k)mod(l));
	writeln ('(', k,')div(', l,')..: ',(k)div(l));
	writeln ('int(', m,')...: ', int(m));
	writeln ('frac(', m,')..: ', frac(m));
	writeln ('abs(', h,')....: ', abs(h));
	writeln ('sqr(', l,')......: ', sqr(l));
	writeln ('sqrt(', l,').....: ', sqrt(l));
		
End.