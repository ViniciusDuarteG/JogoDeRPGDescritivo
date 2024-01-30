nome = str
raca = int
classe = int
Atributos = {}
Vida = 0
Energia = 0
Magia = 0
Dano = 0
arma = str

def MontandoOPersonagem():
    global nome, raca, Atributos, Vida, Energia, Dano, Magia, classe, arma
    
    nome = str(input("Insira o nome do seu personagem: \n"))
    raca = int(input("Selecione a raça do seu personagem:\n1-Humano\n2-Elfo\n3-Orc\n4-Anão\nR: "))

    if raca == 1:
        raca = 'Humano'
        Vida = 100
        Energia = 100
        Magia = 100
        Dano = 10 

    elif raca == 2:
        raca = 'Elfo'
        Vida = 100
        Energia = 150
        Magia = 120
        Dano = 8 

    elif raca == 3:
        raca = 'Orc'
        Vida = 150
        Energia = 120
        Magia = 80
        Dano = 15 

    elif raca == 4:
        raca = 'Anão'
        Vida = 120
        Energia = 100
        Magia = 90
        Dano = 15 

    else:
        print("Valor digitado incorreto.")

    classe = int(input("Escolha sua classe:\n1-Guerreiro\n2-Mago\n3-Arqueiro\nR: "))

    if classe == 1:
        classe = 'Guerreiro'
        Atributos['Vida'] = Vida + 20
        Atributos['Energia'] = Energia + 10
        Atributos['Magia'] = Magia + 0
        Atributos['Dano'] = Dano + 10
        arma = 'Espada'

    elif classe == 2:
        classe = 'Mago'
        Atributos['Vida'] = Vida + 10
        Atributos['Energia'] = Energia + 10
        Atributos['Magia'] = Magia + 20
        Atributos['Dano'] = Dano + 5
        arma = 'Magia'

    elif classe == 3:
        classe = 'Arqueiro'
        Atributos['Vida'] = Vida + 10
        Atributos['Energia'] = Energia + 20
        Atributos['Magia']= Magia + 5
        Atributos['Dano'] = Dano + 15
        arma = 'Flecha'

    else:
        print("Valor digitado incorreto.")

        

def MensagemDeAcao():
    global nome, raca, Atributos, Vida, Energia, Dano, Magia, classe, arma

    print('O {} atacou usando {} e arrancou {} de dano'.format(classe, arma, Atributos['Dano']))

MontandoOPersonagem()

print("Seu nome é {0} sua raça é {1}".format(nome,raca))
Confirmacao_1 = int(input("Confirma essa informação? \n1-Sim\n2-Não\n"))
ver_atributos = int(input("Deseja ver seus atributos?\n1-Sim\n2-Não "))

if ver_atributos == 1:
    for chave, valor in Atributos.items():
        print(chave, valor)
else:
    print("Fim")

MensagemDeAcao()