


def bem_vindo():
    print("Ola seja bem vindo a lookfacil")
    nome = input("digite seu nome por favor: ")
    cpf = input("digite seu cpf por favor: ")
    email = input("digite seu email por favor: ")

def fazer_pedido():
        print("=== Fazer pedido ===")
        nome = input("digite seu nome por favor: ")
        cpf = int (input("digite seu cpf por favor: "))
        print("1 para Ação \n 2 para terror \n 3 para animaçao \n 4 para comedia")

        acao = input("Qual categoria do seu filme?: ")
        if acao == "1":
         escolha1 = input(" digite 1 para John Wick, 2 para Veloses e furiosos, 3 para tropa de elite ")
        elif acao == "2":
            escolha2 = input(" digite 1 para Annabelle, 2 para Panico, 3 para A freira ")
        elif acao ==   "3":
            escolha3 = input(" digite 1 para Mulan, 2 para incriveis, 3 para wall-e ")
        elif acao == "4":
            escolha4 = input(" digite 1 Todo mundo em panico, 2 para Minha mãe é uma peça, 3 para gente grande ")
        else:
           print("Irmao nao estamos com essa categoria")

        def menu():

         comprar = int(input("Digite 1 para comprar ou  2 para alugar? \n"))
         if comprar == 1:
            print("Excelente escolha")
         elif comprar == 2:
            print("Excelente escolha")
         else:
             print("Deu erro, tente novamente")
             print("Otima escolha", escolha)



fazer_pedido()














