Program Contador ;
	var
		c: integer;
Begin
	c := 0;
	while c <= 10 do
		Begin
			write (c, '.. ');
			c := c + 1;
		End
End.