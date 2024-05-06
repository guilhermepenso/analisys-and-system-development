Program Pzim ;
	var
		x,y: string;
			
	function concatenacao(concX, concY: string):string;
		var
			concatenar: string;
		begin
			concatenar:= concat(concX, concY);
			concatenacao:= concatenar;
		end;
		
Begin
	writeln ('Digite a primeira String: ');
	read(x);
	writeln ('Digite a segunda String: ');
	read(y);
	writeln ('Concatenação: ', concatenacao(x,y));  
End.