def uniao(set1, set2):
    return set1 | set2

def intersecao(set1, set2):
    return set1 & set2

def diferenca(set1, set2):
    return set1 - set2

def cartesiano(set1, set2):
    return {(x, y) for x in set1 for y in set2}
#as funcoes definidas a cima sao para o calculo da uniao, intersecao, diferenca e produto cartesiano de dois conjuntos(set 1 e set 2)

def operacao(operacao, set1, set2):
    if operacao == 'U':
        resultado = uniao(set1, set2)
        nome_operacao = "União"
    elif operacao == 'I':
        resultado = intersecao(set1, set2)
        nome_operacao = "Interseção"
    elif operacao == 'D':
        resultado = diferenca(set1, set2)
        nome_operacao = "Diferença"
    elif operacao == 'C':
        resultado = cartesiano(set1, set2)
        nome_operacao = "Plano Cartesiano"
    return nome_operacao, resultado
#atrelando as letras as funcoes ja criadas, para que ao ser digitada a letra por exemplo a letra U, chamar a funcao definida como uniao


def main():
    operacao_tipo = input(
        "Escolha a operação desejada (U para União, I para Interseção, D para Diferença, C para Plano Cartesiano): ").upper()
    if operacao_tipo not in ["U", "I", "D", "C"]:
        print("Letra invalida, reinicie o codigo")
        #Pede ao usuario inserir uma letra para dar inicio ao programa, caso nao escolha uma das 4 opcoes de letra pedidas, o codigo ira gerar um aviso dizendo para reinicar

    with open("input1.txt", "r") as file:
        numero_operacoes = int(file.readline().strip())
        for _ in range(numero_operacoes):
            operacao_arquivo = file.readline().strip()
            set1 = set(file.readline().strip().split(","))
            set2 = set(file.readline().strip().split(","))
            if operacao_arquivo == operacao_tipo:
                nome_operacao, resultado = operacao(operacao_tipo, set1, set2)
                print(f"input1.txt {nome_operacao}: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}")
        
    with open("input2.txt", "r") as file:
        numero_operacoes = int(file.readline().strip())
        for _ in range(numero_operacoes):
            operacao_arquivo = file.readline().strip()
            set1 = set(file.readline().strip().split(","))
            set2 = set(file.readline().strip().split(","))
            if operacao_arquivo == operacao_tipo:
                nome_operacao, resultado = operacao(operacao_tipo, set1, set2)
                print(f"input2.txt {nome_operacao}: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}")

    with open("input3.txt", "r") as file:
        numero_operacoes = int(file.readline().strip())
        for _ in range(numero_operacoes):
            operacao_arquivo = file.readline().strip()
            set1 = set(file.readline().strip().split(","))
            set2 = set(file.readline().strip().split(","))
            if operacao_arquivo == operacao_tipo:
                nome_operacao, resultado = operacao(operacao_tipo, set1, set2)
                print(f"input3.txt {nome_operacao}: conjunto 1 {set1}, conjunto 2 {set2}. Resultado: {resultado}")
        #realiza as operacoes de cada arquivo em especifico, printando o resultado e especificando de qual arquivo foi gerado

if __name__ == "__main__":
    main()
