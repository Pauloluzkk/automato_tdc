# Simulador de Autômato

Um simples simulador de DFA e NFA escrito em Python. Este projeto foi feito como uma tarefa de Teoria da Computação na UENP.

Para simular um DFA ou um NFA, você precisará de três arquivos:
- `automato.aut` Este é um arquivo JSON que contém todas as informações sobre o autômato: o estado inicial, o(s) estado(s) final(is) e as transições.

    Ele deve seguir este padrão, caso contrário o programa falhará:
    
    ```json
    {
      "initial": 0,
      "final" : [2],
      "transitions": [
        {
          "from": "0",
          "to": "0",
          "read": "a"
        },
        {
          "from": "0",
          "to": "1",
          "read": "a"
        },
        {
          "from": "1",
          "to": "2",
          "read": "b"
        }
      ]
    }
    ```

- `entradas.in` Este é um arquivo CSV que contém palavras que passam pelo autômato. Separado por ponto e vírgula está a própria palavra e o resultado esperado para essa palavra (se deve ou não ser uma palavra válida de acordo com o autômato).

    Ele deve seguir este padrão, caso contrário o programa falhará:

    ```csv
    aab;1
    aa;0
    aaaa;0
    ```

- `saida.out` Este também é um arquivo CSV. É muito semelhante ao arquivo de entrada, mas além disso, contém o resultado obtido do autômato e o tempo que levou para processar a palavra (em segundos).

    Este arquivo será gerado pelo programa:

    ```csv
    aab;1;1;0.008151
    aa;0;0;0.003580
    aaaa;0;0;0.003910
    ```

## Agradecimentos

Para executar este programa, você precisará ter o [Python](https://www.python.org/) versão 3.12.3 ou superior instalado.

## Instalação

Clone este repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio
