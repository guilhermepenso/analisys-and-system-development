peso = float (input ('Escreva seu peso(kg): '))
altura = float (input ('Escreva sua altura(m): '))

imc = peso / (altura **2) 

print ('Seu IMC é: ', round(imc))