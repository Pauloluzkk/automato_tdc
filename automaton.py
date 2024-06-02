import json
import csv
import time
import sys

def ler_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        return json.load(arquivo)

def ler_csv(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        leitor = csv.reader(arquivo, delimiter=';')
        return [linha for linha in leitor]

def atualizar_estados(estado_atual, automato, simbolo):
    novos_estados = set()
    for transicao in automato['transitions']:
        if transicao['from'] == estado_atual and transicao['read'] == simbolo:
            novos_estados.add(transicao['to'])
    return novos_estados

def atualizar_estados_nulos(estados, automato):
    novos_estados = set()
    for estado in estados:
        for transicao in automato['transitions']:
            if transicao['from'] == estado and transicao['read'] is None:
                novos_estados.add(transicao['to'])
    return novos_estados

def simular_automato(automato, entrada):
    estados_atuais = {automato['initial']}
    for simbolo in entrada:
        novos_estados = set()
        estados_atuais.update(atualizar_estados_nulos(estados_atuais, automato))
        for estado in estados_atuais:
            novos_estados.update(atualizar_estados(estado, automato, simbolo))
        if not novos_estados:
            return 0
        estados_atuais = novos_estados
    return 1 if any(estado in automato['final'] for estado in estados_atuais) else 0

def main(arquivo_automato, arquivo_entradas, arquivo_saida):
    automato = ler_json(arquivo_automato)
    entradas = ler_csv(arquivo_entradas)
    if not entradas:
        return
    try:
        with open(arquivo_saida, 'w', newline='') as arquivo:
            escritor = csv.writer(arquivo, delimiter=';')
            for linha in entradas:
                entrada = linha[0]
                resultado_esperado = int(linha[1])
                inicio = time.time()
                resultado_obtido = simular_automato(automato, entrada)
                fim = time.time()
                tempo_gasto = fim - inicio
                escritor.writerow([entrada, resultado_esperado, resultado_obtido, f"{tempo_gasto:.6f}"])
    except Exception as erro:
        print(f"Erro no arquivo de saída {arquivo_saida}: {erro}")

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Uso: python simulador.py <arquivo_do_automato.aut> <arquivo_de_testes.in> <arquivo_de_saida.out>")
        sys.exit(1)
    arquivo_automato = sys.argv[1]
    arquivo_entradas = sys.argv[2]
    arquivo_saida = sys.argv[3]
    main(arquivo_automato, arquivo_entradas, arquivo_saida)
