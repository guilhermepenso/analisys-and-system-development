Program usuariosenhatestefunction;
var
user, password, resp, in_retorno, novasenha: string;
usuario, senha: array [1..3] of string;
teste, retorno: boolean;
nav, x, y: integer;

Begin
  usuario[1] := 'gui';
  senha[1] := '111';
  
  usuario[2] := 'lucas';
  senha[2] := '222';
  
  usuario[3] := 'kauan';
  senha[3] := '333';
  
  // MENU DE OPÇÕES //
	
	repeat  
	  
		clrscr;
	  writeln (' ----------------------------');
	  writeln (' ---------- MENU ------------');
	  writeln (' ----------------------------');
	  writeln (' ----- [1] CADASTRO ---------');
	  writeln (' ----- [2] LOGIN ------------');
	  writeln (' ----- [3] ALTERAR SENHA ----');
	  writeln (' ----------------------------');
	  read (nav);
	  
	  if (nav <1) or (nav > 3) then
	  begin
	    write ('Opcao Inexistente');
	  end
	  else
	  case nav of
	  
	  // OPÇÃO 1 = CADASTRO //
	  
	    1:
	    begin
	      repeat
	        clrscr;
	        writeln (' --------------------------');
	        writeln (' -------- CADASTRO --------');
	        writeln (' --------------------------');
	        write (' Digite o Nome do Usuario: ');
	        readln (user);
	        
	        if (usuario[1] = '') then
	        begin
	          usuario[1] := user;
	          
	          write (' Digite a Senha: ');
	          readln (senha[1]);
	        end
	        
	        else
	        if (usuario[2] = '') then
	        begin
	          usuario[2] := user;
	          
	          write ('Digite a Senha: ');
	          readln (senha[2]);
	        end
	        
	        else
	        if (usuario[3] = '') then
	        begin
	          usuario[3] := user;
	          
	          write (' Digite a Senha: ');
	          readln (senha[3]);
	        end
	        
	        else
	        begin
	          writeln (' --------------------------');
	          writeln (' Nao há mais espaços disponíveis para cadastro.');
	        end;
	        writeln (' --------------------------');
	        write ('Deseja realizar mais um cadastro? [S/N]:  ');
	        read (resp);
	      until (resp = 'N');
	      if (resp = 'N') then
	      begin
	        write ('Voltar ao Menu? [S/N]: ');
	        read (resp);
	      end
	      
	    end;
	    
	    // OPÇÃO 2 = LOGIN //
	    
	    2:
	    begin
	      
	      repeat
	      	clrscr;
	        writeln (' --------------------------');
	        writeln (' --------- LOGIN ----------');
	        writeln (' --------------------------');
	        write ('Usuario: ');
	        readln (user);
	        write ('Senha: ');
	        readln (password);
	        
	        if (user = usuario[1]) and (password = senha[1]) then
	        begin
	          clrscr;
	          
						writeln ('Bem Vindo ', usuario[1]);
	          inc(x); 
	      		delay(2000);
	      		clrscr;
	      		teste := true;
	      		
	      		writeln ('---------------------------');
	    							write ('Deseja retornar ao menu inicial? [S/N]: ');
	    							read (in_retorno);
	        end;
	        
	        if (user = usuario[2]) and (password = senha[2]) then
	        begin
	        	clrscr;
	          writeln ('Bem Vindo ', usuario[2]);
	          inc(x);
	      		delay(2000);
	      		clrscr;
	      		teste := true;
	      		
	      		writeln ('---------------------------');
	    							write ('Deseja retornar ao menu inicial? [S/N]: ');
	    							read (in_retorno);
	        end;
	        
	        if (user = usuario[3]) and (password = senha[3]) then
	        begin
	        	clrscr;
	          writeln ('Bem Vindo ', usuario[3]);
	          inc(x);
	      		delay(2000);
	      		clrscr;
	      		teste := true;
	      		
	      		writeln ('---------------------------');
	    							write ('Deseja retornar ao menu inicial? [S/N]: ');
	    							read (in_retorno);
	        end;
	        
	        if(teste = false) then
	    		begin
	    			clrscr;
	    			writeln('Usuario ou senha incorretos.');
	    			inc(y);
	    			delay (2000);
	    		end;
	  		
					if(y > 2)then
	  			begin
	   				inc(x);
	 				end;
	        
	      until (x > 0);
	      
	      if(y > 2 )then
				begin
					clrscr;
				  writeln('Voce excedeu o limite de tentativas');
				  
				  delay(2000);  
	    		writeln ('---------------------------');
	    		write ('Deseja retornar ao menu inicial? [S/N]: ');
	    		read (in_retorno);
	 
	  			
				end;
	
				if(y < 3 )then
				begin
				  writeln('Você está logado!');
				end;
				
	    end;
	    
	    // OPÇÃO 3 = ALTERAR SENHA //
	    
	    3:
                begin
                  clrscr;
                  writeln('-----ALTERAR SENHA-----');
                  write('Digite sua senha atual: ');
                  readln(password);
                  
                  if (password = senha[1]) and (user = usuario[1]) then
                  begin
                    write('Digite sua nova senha: ');
                    readln(novasenha);
                    senha[1] := novasenha; // atualiza a senha no array de senhas
                    writeln('Senha alterada com sucesso!');
                    delay(1000);
                    
                    writeln ('---------------------------');
	    							write ('Deseja retornar ao menu inicial? [S/N]: ');
	    							read (in_retorno);
                  end;
                  
                  if (password = senha[2]) and (user = usuario[2]) then
                  begin
                    write('Digite sua nova senha: ');
                    readln(novasenha);
                    senha[2] := novasenha; // atualiza a senha no array de senhas
                    writeln('Senha alterada com sucesso!');
                    delay(1000);
                    
                    writeln ('---------------------------');
	    							write ('Deseja retornar ao menu inicial? [S/N]: ');
	    							read (in_retorno);
                  end;
                  
                  if (password = senha[3]) and (user = usuario[3]) then
                  begin
                    write('Digite sua nova senha: ');
                    readln(novasenha);
                    senha[3] := novasenha; // atualiza a senha no array de senhas
                    writeln('Senha alterada com sucesso!');
                    delay(1000);
                      
	    							writeln ('---------------------------');
	    							write ('Deseja retornar ao menu inicial? [S/N]: ');
	    							read (in_retorno);
                  end
                  else
                  begin
                    writeln('Senha incorreta!');
                    
                    
				  						delay(2000);  
	    								writeln ('---------------------------');
	    								write ('Deseja retornar ao menu inicial? [S/N]: ');
	    								read (in_retorno);
                  end;
                end;
                
                
                
              end;
              
              if (in_retorno = 'N') then
	   						begin
	   							retorno := true;		
	   					end
	   			
	   					else
	   						x := 0;
	   						y := 0;
	   						
  until (retorno = true);
End.