import random
import ast
import os 

caminho_arquivo = "palavras.txt"
limpa_terminal = "\n" * os.get_terminal_size().lines
palavras_list = {}
with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        linha = linha.strip()
        try:
            chave, valor = linha.split(':', 1)
            chave = chave.strip().strip("'")
            valor = ast.literal_eval(valor.strip())
            palavras_list[chave] = valor
        except Exception as e:
            print(f"error {e}")

print(f"Insira um dos gêneros abaixo que você gostaria de jogar forca sobre:")
for categoria in palavras_list.keys():
    print(f"'{categoria}'")
escolha = input("Insira a categoria(sem acentos): ").strip().lower()

if escolha in palavras_list:
    palavras = palavras_list[escolha]
    index = random.randint(0, len(palavras) - 1)
    palavra_escolihada = palavras[index]
    lista_letras_palavra = list(palavra_escolihada)
    print(limpa_terminal, "Gênero escolhido com sucesso!")
else:
    print(limpa_terminal, "Escolha inexistente! Insira uma das alternativas fornecidas")
    pass
letras_tentadas = []
estado_palavra = ["_" for _ in lista_letras_palavra]
tentativas = 8
while True:
    if not "_" in estado_palavra:
        print(limpa_terminal, f"Parabéns, você acertou a palavra *{palavra_escolihada}*!")
        break
    if tentativas == 0:
        print(limpa_terminal, f"Suas tentativas acabaram! A palavra era *{palavra_escolihada}*")
        break
    

    tentativas_restantes = print(f"Você possui {tentativas} tentativas restantes!\n")
    print("Palavra: ","".join(estado_palavra))
    
    letra_input = input("Insira uma letra: ")
    
    if len(letra_input) == 1 and letra_input.isalpha():
        if letra_input not in letras_tentadas:
            letras_tentadas.append(letra_input)
            if letra_input in lista_letras_palavra:
                print(limpa_terminal, "A palavra possui a letra inserida!")
                for i, letra in enumerate(lista_letras_palavra):
                    if letra in letras_tentadas:
                        estado_palavra[i] = letra
            else:
                print(limpa_terminal, "A palavra não possui a letra inserida.")
                tentativas -= 1
        else:
            print(limpa_terminal, "Carácter já tentado!")
    else:
        print(limpa_terminal, "Insira um carácter válido!")