Program arrays ;
	var
		v: array[1..5] of integer;
		i: integer;
		  
Begin
  	
	
		v[1] := 7;
		v[2] := 89;
		v[3] := 3;
		v[4] := 26;
		v[5] := 2;	
		
		i := 1;
		
		repeat 
			write (v[i], ' ');
			inc (i);
		until (i = 5)
			
End.