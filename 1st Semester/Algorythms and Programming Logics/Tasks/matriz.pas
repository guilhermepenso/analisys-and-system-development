Program matrizSoma ;
	const
		linha=10;
		coluna=10;
	var
		matA, matB, matC: array[1..linha, 1..coluna] of integer;
		i, j, matS: integer;
Begin
	writeln;
	writeln('A + B = C');
	writeln;
	writeln('[A]= ');
	for i:= 1 to linha do
		begin 
			writeln;    
			for j:= 1 to coluna do
				begin
					matA[i,j]:= random(101);
					write(matA[i,j], '   '); 		
				end
		end;
	writeln;
	writeln;
	writeln ('[B]= ');
	for i:= 1 to linha do
		begin 
			writeln;    
			for j:= 1 to coluna do
				begin
					matB[i,j]:= random(101);
					write(matB[i,j], '   '); 		
				end
		end;
	writeln;
	writeln;
	writeln ('[C]= ');
	for i:= 1 to linha do
		begin 
			writeln;    
			for j:= 1 to coluna do
				begin
					matC[i,j]:= (matA[i,j] + matB[i,j]);
					write(matC[i,j], '   '); 		
					matS := (matS + matC[i,j]);
				end
		end;
	writeln;
	writeln;
	writeln ('Soma das matrizes C: ', matS);
	
End.