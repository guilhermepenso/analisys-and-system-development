Program usuariosenha;
//ALUNOS:
//Lucas Iaremchuk Gomes / 2221982
//Guilherme Penso / 2320311
//Emanoel andre Hacke de britto / 2320048
//Murilo Lustosa / 2320028
//Kauan Vinicius de Moraes / 2320551
//Mauricio de Oliveira Luiz / 2221901
uses Graph;
var
resp:char;
user, password, novasenha, porta: string;
usuario, senha: array [1..3] of string;
nav, x, alterar, escolha, escolhalog: integer;
fechadura ,tentativas ,TPorta ,altsenha , ativa5: boolean;
Begin
  
  
  
  repeat    //MENU PRINCIPAL
    clrscr;
    altsenha := false;
    resp := (' ');
    fechadura := false;
    tentativas := false;
    
    if(TPorta = false) then
    begin
      porta :=('Fechada ');
    end;
    if(TPorta = true) then
    begin
      porta :=('Aberta  ');
    end;
    // Centralizando o texto
    SetTextJustify(CenterText, CenterText);
    
    writeln (' ----------------------------');
    writeln (' -- A Porta está ',Porta, '----');
    writeln (' ----------------------------');
    writeln (' ---------- MENU ------------');
    writeln (' ----------------------------');
    writeln (' ----- [1] CADASTRO ---------');
    writeln (' ----- [2] LOGIN ------------');
    writeln (' ----- [3] Alterar senha ----');
    writeln (' ----- [4] Sair do programa -');
    if(TPorta = true) then
    begin
      writeln (' ----- [5] Deslogar ---------');
    end;
    writeln (' ----------------------------');
    read (nav);
    
    if (nav <1) or (nav > 5) then
    begin
      write ('Opcao Inexistente');
      delay(1000);
    end
    else
    case nav of
      1:
      begin
        repeat      //MENU DE CADASTRO -- COMEÇO --
          clrscr;
          writeln (' --------------------------');
          writeln (' -------- CADASTRO --------');
          writeln (' --------------------------');
          write (' Digite o Nome do Usuario: ');
          readln (user);
          
          //IDENTIFICA SE É O PRIMEIRO, SEGUNDO OU TERCEIRO CADASTRO E PREENCHE O CORRETO
          
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
        until (resp = 'N') or (resp = 'n');   //MENU DE CADASTRO -- FIM --
        
        if (resp = 'N') or (resp = 'n')then
        begin
          write ('Voltar ao Menu? [S/N]: ');  //fica fora da repetição do menu de cadastro pois serve para peguntar se quer sair do programa apos ter terminado de cadastrar os usuarios
          read (resp);
          
          if(resp = 'N') or (resp = 'n') then
          begin
            nav :=3;
          end
        end
        
      end;
      2:
      begin
        repeat   //MENU DE LOGIN   -- COMEÇO --
          clrscr;
          writeln (' -----------------------------');
          writeln (' ------- [1]LOGIN ------------');
          writeln (' ------- [2]Voltar ao Menu ---');
          writeln (' -----------------------------');
          read(escolhalog);
          if (escolhalog <1) or (escolhalog > 2) then
          
          begin
            write ('Opcao Inexistente');
            delay(1000);
          end;
          
          if(escolhalog =1) then
          begin
            write ('Usuario: ');
            readln (user);
            write ('Senha: ');
            readln (password);
            
            // IDENTIFICA SE O LOGIN INFORMADO ESTA CADASTRADO
            
            if (user = usuario[1]) and (password = senha[1]) then
            begin
              clrscr;
              writeln ('Bem Vindo, ', usuario[1]);
              fechadura := true;
              TPorta :=true;
              delay(3000);
              escolhalog := 2;
              ativa5 := true;
              x:= 0;
            end;
            
            if (user = usuario[2]) and (password = senha[2]) then
            begin
              clrscr;
              writeln ('Bem Vindo, ', usuario[2]);
              fechadura := true;
              TPorta :=true;
              delay(3000);
              escolhalog := 2;
              ativa5 := true;
              x:= 0;
            end;
            
            if (user = usuario[3]) and (password = senha[3]) then
            begin
              clrscr;
              writeln ('Bem Vindo, ', usuario[3]);
              fechadura := true;
              TPorta :=true;
              delay(3000);
              escolhalog := 2;
              ativa5 := true;
              x:= 0;
            end;
            
            if(fechadura = false) then     //CASO NAO ESTEJA CADASTRADO ADICIONA UMA TENTATIVA PARA A VARIANTE X
            begin
              writeln ('Usuario ou Senha incorreta');
              inc(x);
              delay(1000);
            end;
            
            if(x>2) then
            begin
              tentativas := true       // CASO A VARIANTE X CHEGUE A 3 ELE DEFINE A VARIANTE DE TENTATIVA COMO TRUE
            end;
            
            if(Fechadura = true) then
            
          end;
          
        until(escolhalog = 2) or (tentativas = true);   //MENU DE LOGIN   -- FIM --
      end;
      3:
      begin    //MENU DE ALTERAÇÃO DE SENHA   -- COMEÇO --
        clrscr;
        if(TPorta = false) then
        begin
          writeln('Voce ainda nao esta logado!');
          delay(2000);
          altsenha := true
        end;
        while altsenha = false do
        begin
          writeln (' --------------------------------');
          writeln (' ----- Alteração de senha -------');
          writeln (' --------------------------------');
          write('Digite sua senha atual: ');
          readln(password);
          
          if (password = senha[1]) and (user = usuario[1]) then
          begin
            write('Digite sua nova senha: ');
            readln(novasenha);
            senha[1] := novasenha; // atualiza a senha no array de senhas
            writeln('Senha alterada com sucesso!');
            altsenha := true;
            delay(1000);
          end;
          if (password = senha[2]) and (user = usuario[2]) then
          begin
            write('Digite sua nova senha: ');
            readln(novasenha);
            senha[2] := novasenha; // atualiza a senha no array de senhas
            writeln('Senha alterada com sucesso!');
            altsenha := true;
            delay(1000);
          end;
          if (password = senha[3]) and (user = usuario[3]) then
          begin
            write('Digite sua nova senha: ');
            readln(novasenha);
            senha[3] := novasenha; // atualiza a senha no array de senhas
            writeln('Senha alterada com sucesso!');
            altsenha := true;
            delay(1000);
          end
          else
          begin
            clrscr;
            writeln('Senha incorreta!');
            delay(2000);
            clrscr;
          end;
        end
      end;  //MENU DE ALTERAÇÃO DE SENHA   -- FIM --
      5:
      begin
        if(ativa5 = true) then
        TPorta := false;
        user := (' ');
        password := (' ');
      end
    end;
  until(nav = 4) or (tentativas = true);
  
  if(nav = 4) then
  begin
    clrscr;
    writeln('Voce escolheu sair');
  end;
  
  if(tentativas = true ) then
  begin
    clrscr;
    writeln('Voce excedeu o limite de tentativas, contante um administrador');
  end;
End.