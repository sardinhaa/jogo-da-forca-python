import os

def display_word(palavra, letras_certas):
    return ''.join( letra if letra in letras_certas else '_' for letra in palavra)

def game():
    os.system('cls') # limpar ecra
    palavra = input("Jogador 1, escolha a sua palavra:").lower()
    letras_certas = set()

    tries = 0
    while tries < 8:
        os.system('cls') # limpar ecra

        print("Palavra secreta:")
        print(display_word(palavra, letras_certas))

        letra = input("Jogador 2, escolha uma letra:").lower()

        if letra in letras_certas:
            print("Você já tentou essa letra!")
        elif letra in palavra:
            letras_certas.add(letra)

            if set(palavra).issubset(letras_certas):
                break
        else:
            tries += 1

    os.system('cls') # limpar ecra
    print("Palavra secreta:", palavra)
    print("Letras corretas:", ', '.join(sorted(letras_certas)))
    print("Parabéns! Você adivinhou a palavra secreta!")
if __name__ == "__main__":
    game()