import json

def bancoFuncionarios():
    file = open('atividadeJason.txt' , 'r')
    conteudo = json.loads(file.read())
    return conteudo

def media(conteudoJason, dado):
    soma = 0.0
    for item in conteudoJason:
        soma = soma + item[dado]
    return soma / len(conteudoJason)  

#MAIN
    
conteudoJason = bancoFuncionarios()

option = int(input("1 - Media das idades\n2 - Media Salarial"))
if option == 1:
    idade = media(conteudoJason, "idade")
    print(idade)
elif option == 2:
    salario = media(conteudoJason, "Salario")
    print(salario)
else:
    print('Valor incorreto')



