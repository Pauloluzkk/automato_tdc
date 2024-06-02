# 💻 Simulador de Autômato

Um simples simulador de Autômatos Finitos escrito em Python. Este projeto foi feito como uma tarefa da matéria de Teoria da Computação na UENP.

Para simular um Autômato Finito Determinístico ou um Não Determinístico, você precisará de três arquivos:

- Este é um arquivo JSON que contém todas as informações sobre o autômato: o estado inicial, o(s) estado(s) final(is) e as transições.

    O arquivo json deve seguir o modelo padrão a seguir:
    
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

- Este é um arquivo CSV que contém palavras que passam pelo autômato. Separado por ponto e vírgula está a própria palavra e o resultado esperado para essa palavra.

    Ele deve seguir este padrão:

    ```csv
    aab;1
    aa;0
    aaaa;0
    ```

- Este também é um arquivo CSV. É muito semelhante ao arquivo de entrada, mas além disso, contém o resultado obtido do autômato e o tempo que levou para processar a palavra (em segundos).

    Este arquivo será gerado pelo programa:

    ```csv
    aab;1;1;0.008151
    aa;0;0;0.003580
    aaaa;0;0;0.003910
    ```

## Executando

Para executar este programa, você precisará ter o [Python](https://www.python.org/) versão 3.12.3 ou superior instalado.
E executar o seguinte código em seu terminal:

(pode ser que o programa encontre erros em ler os arquivos).
```csv
$ python automaton.py Exemplos/ex1.json Exemplos/ex1_input.csv Exemplos/ex1_output.out.csv
```
Sendo necessário implementar o nome dos 3 arquivos para rodar.
