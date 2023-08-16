Program loop_salary_sqr;
	var
		salary: real;
		counter: integer;
Begin
	salary := 0.05; 
	counter := 1; 
	while (counter <= 26) do
		begin                         
			writeln (counter, '° Mês: R$', salary:0:2);
			salary := (salary * 2);
			inc(counter);
		end
		  
End.