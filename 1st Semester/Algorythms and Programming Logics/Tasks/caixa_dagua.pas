Program caixa_dagua;
	var
		v, d, r, h: real;
		
	const
		PI=3.14;		
Begin
  //v=PI�*h
  write ('Qual � a altura da caixa de �gua?(m): ');
  read (h);
  write ('Qual o diametro da caixa de �gua?(m): ');
  read (d);
  r := (d / 2);
  v := PI*sqr(r)*h *1000;
  writeln ('Caber� ', v:0:0, ' litros na caixa de �gua.');
End.