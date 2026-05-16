from jogo import iniciar_jogo

iniciar_jogo()

PALAVRAS = ["python", "programacao", "computador", "desenvolvimento"]

def escolher_palavra():
    return PALAVRAS[0]

def mostrar_palavra(palavra, letras_corretas):
    exibicao = ""

    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "

    return exibicao.strip()

def iniciar_jogo():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    print("=== JOGO DA FORCA ===")

    while tentativas > 0:
        print("\nPalavra:", mostrar_palavra(palavra, letras_corretas))
        print("Letras erradas:", " ".join(letras_erradas))
        print("Tentativas restantes:", tentativas)

        letra = input("Digite uma letra: ").lower()

        if letra in letras_corretas or letra in letras_erradas:
            print("Você já tentou essa letra.")
            continue

        if letra in palavra:
            letras_corretas.append(letra)
            print("Letra correta!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Letra errada!")

        venceu = True

        for letra_palavra in palavra:
            if letra_palavra not in letras_corretas:
                venceu = False
                break

        if venceu:
            print("\nParabéns! Você venceu!")
            print("A palavra era:", palavra)
            return

    print("\nGame Over!")
    print("A palavra era:", palavra)

    from jogo import mostrar_palavra, escolher_palavra


# 5 casos válidos
def testar_casos_validos():
    palavra = "python"

    assert mostrar_palavra(palavra, ["p"]) == "p _ _ _ _ _"
    assert mostrar_palavra(palavra, ["p", "y"]) == "p y _ _ _ _"
    assert mostrar_palavra(palavra, list("python")) == "p y t h o n"
    assert mostrar_palavra(palavra, []) == "_ _ _ _ _ _"
    assert escolher_palavra() in ["python", "programacao", "computador"]


# 5 casos inválidos
def testar_casos_invalidos():
    palavra = "python"

    assert mostrar_palavra(palavra, ["d"]) == "_ _ _ _ _ _"
    assert mostrar_palavra(palavra, ["l"]) == "_ _ _ _ _ _"
    assert mostrar_palavra(palavra, ["a"]) == "_ _ _ _ _ _"
    assert mostrar_palavra(palavra, ["python"]) != "python"
    assert mostrar_palavra(palavra, [" "]) == "_ _ _ _ _ _"
