Program IMC ;                                                  	
var                                                       
	altura, peso, resultado: real;
Begin
	writeln (' ====== CALCULO IMC =====');
  write ('  Qual sua Altura(m)? ');
  readln (altura);
  write ('  Qual o seu Peso(Kg)? ');
  readln (peso);                  
  resultado := peso/(altura*altura);
  writeln (' ======= RESULTADO ======'); 
  write ('  Seu IMC é: ', resultado);
  //imc=peso/altura x altura
End.