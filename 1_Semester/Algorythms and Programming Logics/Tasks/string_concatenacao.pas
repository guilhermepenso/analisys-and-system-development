Program concatenacao;                   
	var
		str1, str2, str3, str4, str5, str6, aux: string;
Begin
	str1 := '1';
	str2 := '_2_';
	str3 := 'Olá';
	str4 := 'Mundo';
	str5 := '!';
	str6 := ' ';
	                    
	writeln (concat(str1, str2)); 
	writeln (concat(str3, str4)); 
	writeln (concat(str3, str4, str5)); 
	writeln (concat(str3, str6, str4, str5));  
	
	aux := concat (str3, str6, str4, str5);
	writeln (upcase(aux));
End.