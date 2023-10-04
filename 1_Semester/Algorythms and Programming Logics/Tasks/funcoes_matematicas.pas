Program Funcao_Matematica;
	var
		h, i, j, k, l: integer;
		r,m, n, o: real;
Begin
	h := -20;
	i := 15;
	j := 7;
	k := 40;
	l := 4;
	
	r := 20.5;
	m := 40.7;
	n := 100.0;
	o := 50.0;
	
	writeln ('(15)mod(7)..: ',(i)mod(j));	
	writeln ('(15)div(7)..: ',(i)div(j));	
	writeln ('(40)mod(4)..: ',(k)mod(l));
	writeln ('(40)div(4)..: ',(k)div(l));
	writeln ('int(40.7)...: ', int(m));
	writeln ('frac(40.7)..: ', frac(m));
	writeln ('abs(-20)....: ', abs(h));
	writeln ('sqr(4)......: ', sqr(l));
	writeln ('sqrt(4).....: ', sqrt(l));
		
End.