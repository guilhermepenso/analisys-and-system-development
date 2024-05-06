Program usuariosenha;
var
user, password, resp: string;
usuario, senha: array [1..3] of string;
nav: integer;
Begin
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
    2:
    begin
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
        writeln ('Bem Vindo, ', usuario[1]);
      end
      
      else
      if (user = usuario[2]) and (password = senha[2]) then
      begin
        clrscr;
        writeln ('Bem Vindo, ', usuario[2]);
      end
      
      else
      if (user = usuario[3]) and (password = senha[3]) then
      begin
        clrscr;
        writeln ('Bem Vindo, ', usuario[3]);
      end
      
      else
      writeln ('Usuario ou Senha incorreta');
      
    end
    
  end
End.