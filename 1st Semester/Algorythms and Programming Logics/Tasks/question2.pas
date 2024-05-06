Program Quest2;
	var
		x, y, z, w: integer;
Begin

	x := 2;
	y := 5;
	z := 1;
	w := x;
	 
	write (x + y, ' | '); 
	write (y + z, ' | ');
	z:= y * x;
	write (x + z, ' | ');
	write (w + z, ' | ');
End.