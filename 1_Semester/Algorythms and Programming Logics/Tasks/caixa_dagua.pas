Program caixa_dagua;
	var
		v, d, r, h: real;
		
	const
		PI=3.14;		
Begin
  //v=PI²*h
  write ('Qual é a altura da caixa de água?(m): ');
  read (h);
  write ('Qual o diametro da caixa de água?(m): ');
  read (d);
  r := (d / 2);
  v := PI*sqr(r)*h *1000;
  writeln ('Caberá ', v:0:0, ' litros na caixa de água.');
End.