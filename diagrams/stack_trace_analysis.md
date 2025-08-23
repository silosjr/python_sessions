---
file: stack_trace_analysis.md
author: Enock Silos
version: 1.0.0
vtatus: Analysis
date: 2025-08-23
---

# Análise de Fluxo de Execução e Pilha de Chamadas

Este documento detalha o comportamento de um script Python, rastreando a execução linha por linha, a interação entre as funções e o estado da pilha de chamadas (*call stack*) em cada etapa crucial.

## Código Fonte em Análise

```python
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square

x = 1
y = x + 1
print(c(x, y+3, x+y))
```

### Rastreamento da Execução (Passo a Passo)

A execução de um script Python começa no escopo global.

1. Escopo Global
O interpretador executa as linhas fora de qualquer definição de função:

x = 1: Uma variável x é criada no escopo global e recebe o valor 1.

y = x + 1: Uma variável y é criada. A expressão x + 1 é avaliada (1 + 1 = 2), e y recebe o valor 2.

print(c(x, y+3, x+y)): Esta é a linha principal. Antes que print possa ser executado, sua expressão interna, a chamada da função c(...), deve ser resolvida.

x é 1.

y+3 é 2+3 = 5.

x+y é 1+2 = 3.

O Python se prepara para chamar a função c com os argumentos 1, 5 e 3.

#### Chamada da Função c(x=1, y=5, z=3)

Um novo frame (quadro) é empilhado na pilha de chamadas.

Pilha de Chamadas: [global, c]

Dentro de c:

Os parâmetros x, y e z são criados como variáveis locais neste frame, recebendo os valores 1, 5 e 3, respectivamente.

total = x + y + z: A variável local total é criada e recebe o resultado de 1 + 5 + 3, que é 9.

square = b(total)**2: Para resolver esta linha, a função b deve ser chamada primeiro, com o argumento total (valor 9).

##### Chamada da Função b(z=9)

Um novo frame é empilhado sobre o de c.

Pilha de Chamadas: [global, c, b]

Dentro de b:

O parâmetro z é criado como uma variável local, recebendo o valor 9.

prod = a(z, z): Para resolver esta linha, a função a é chamada. Ambos os argumentos são z, que tem o valor 9.

###### Chamada da Função a(x=9, y=9)

Este é o ponto mais profundo da pilha. Um novo frame é empilhado sobre o de b.

Pilha de Chamadas: [global, c, b, a]

Dentro de a:

Os parâmetros x e y são criados como variáveis locais, recebendo os valores 9 e 9.

x = x + 1: O valor da variável local x é atualizado para 9 + 1 = 10. A variável y permanece 9.

return `x * y`: A função a finaliza sua execução e retorna o valor de 10 * 9, que é 90.

###### Retorno para a Função b

O frame da função a é desempilhado. A execução continua de onde parou em b.

Pilha de Chamadas: [global, c, b]

Dentro de b:

prod = a(z, z): A variável local prod recebe o valor de retorno de a, que é 90.

print(z, prod): O programa imprime o valor das variáveis locais z e prod. Saída no console: 9 90.

return prod: A função b finaliza e retorna o valor de prod, que é 90.

###### Retorno para a Função c

O frame da função b é desempilhado. A execução continua em c.

Pilha de Chamadas: [global, c]

Dentro de c:

square = b(total)**2: A variável local square recebe o valor de retorno de b (90) elevado ao quadrado. 90**2 é 8100.

return square: A função c finaliza e retorna o valor de square, que é 8100.

###### Retorno para o Escopo Global

O frame da função c é desempilhado. A execução retorna à linha original.

Pilha de Chamadas: [global]

print(c(x, y+3, x+y)): A chamada da função c foi resolvida e retornou 8100. Agora, a função print pode finalmente ser executada com este valor. Saída no console: 8100.

``` text
