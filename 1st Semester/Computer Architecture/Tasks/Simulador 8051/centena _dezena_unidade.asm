                org 00h
                sjmp inicio
                org 30h
inicio:         mov     r1,#00          
                mov     r2,#00
                mov     r3,#00
                mov     a,p1
                mov     b,#64h
                mov     r4,a
                subb    a,b
                mov     a,r4
                jc      dezena
                div     ab
                mov     r1,a
                mov     a,b
dezena:         mov     b,#0ah
                mov     r4,a
                subb    a,b
                mov     a,r4
                jc      unidade
                div     ab
                mov     r2,a
                mov     a,b
unidade:        mov     r3,a
                sjmp    $
