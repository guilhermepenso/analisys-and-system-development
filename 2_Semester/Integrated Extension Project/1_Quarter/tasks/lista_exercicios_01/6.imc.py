# Nome: Guilherme Penso
# R.A.: 2320311

# 5. MC
# Escreva um programa que calcule o IMC de uma pessoa. Utilize o seguintecálculo: imc = peso / altura^2. Classifique o resultado de acordo com a tabela abaixo:

peso = float(input('Escreva seu peso(kg): '))
altura = float(input('Escreva sua altura(m): '))

imc = peso / (altura **2) 

print ('Seu IMC é: ', round(imc))
       
if (imc < 18.6):
    print ("Você está abaixo do peso")
elif (imc > 18.5) and (imc < 25):
    print ("Você está com o Peso Ideal, Parabéns!")
elif (imc > 24.9) and (imc < 30):
    print ("Você está levemente acima do peso")
elif (imc > 29.9) and (imc < 35):
    print ("Você está com Obesidade Grau 1")
elif (imc > 34.9) and (imc < 40):
    print ("Você está com Obesidade Grau 2(Severa)")
elif (imc > 39.9):
    print ("Você está com Obesidade Grau 1(Mórbida)")
    