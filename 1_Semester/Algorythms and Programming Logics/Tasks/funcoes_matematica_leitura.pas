Program Funcao_Matematica_Leitura;
	var
		h, i, j, k, l: integer;
		r,m, n, o: real;
Begin
	write ('Escreva um número inteiro: ');
	read (h);
	write ('Escreva um número inteiro: ');
	read (i);                           
	write ('Escreva um número inteiro: ');
	read (j);                              
	write ('Escreva um número inteiro: ');
	read (k);
	write ('Escreva um número inteiro: ');
	read (l);

	write ('Escreva um número real: ');
	read (r);
	write ('Escreva um número real: ');
	read (m);
	write ('Escreva um número real: ');
	read (n);
	write ('Escreva um número real: ');
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