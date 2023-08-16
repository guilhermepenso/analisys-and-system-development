Program funcao_soma_inteiros ;   
var		
	x, y: integer;
		
	function somaInteiros(z:integer):integer;
		var
			soma, y: integer;
		begin
			y:= 20;
			soma:= z + y;
			somaInteiros:=soma;
		end;		

Begin
	y:=10;
	writeln('Escreva um numero: ');
	read(x);
	writeln('A soma é: ', somaInteiros(x));
	writeln('O valor de y é: ', y);  
End.