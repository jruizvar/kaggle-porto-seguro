# Modelo

O desafio foi enquadrado como um problema de classificação com variável resposta binária.
A análise exploratória dos dados e a proposta de solução se encontram no notebook [solution.ipynb](solution.ipynb). 

O módulo [model.py](model.py) contém a classe `Model` consumida pelo notebook, e fornece métodos para treinamento do modelo e submissão da solução.
O modelo implementa um pipeline para tratamento de valores faltantes e discretização de variáveis, junto com o algoritmo de regressão logística.

Como estratégia de seleção de variáveis é feita uma iteração recursiva na colunas do dataframe, escolhendo somenta as colunas que trazer um incremento na métrica de avaliação.  