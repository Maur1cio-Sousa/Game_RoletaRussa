# Parte 1 - importar biblioteca
import random

# Parte 2 - criar a função do código

def roletaRussa():
    # 1 cartucho com bala, 0 cartuchos livres
    tambor = [1] + [0]*5  # Concateno as duas listas
    random.shuffle(tambor) # Embaralhar os dados da lista

    # laço de repetição
    for i in range(6):
        # i + 1 porque o range ira exibir 0,1,2,3,4,5... Dessa forma o 0 passa a ser 1 etc..
        print(f"Disparo Relizado... Chambreamento {i + 1}")

        # Condicional
        if tambor[i] == 1:
            print("Se fodeu!")
            return
        else:
            print("Sortudo! Próximo..")
            input("Tecle enter para um novo disparo. \n"
                  "")


# Parte 3 - Chamar a função
roletaRussa()
