# [Porto Seguro Data Challenge | Kaggle](https://www.kaggle.com/c/porto-seguro-data-challenge)
Modelo de propensão de aquisição a novos produtos.

## Configurações

Necessitamos configurar a [API do Kaggle](https://www.kaggle.com/docs/api) para obter os dados do desafio e para realizar a submissão da solução.

1. Obter token de autenticação `kaggle.json`.
2. Salvar o token no diretório `~/.kaggle/kaggle.json`.
3. Ajustar permissões do token `chmod 600 ~/.kaggle/kaggle.json`.

## Dados

Os dados podem ser obtidos mediante o comando `kaggle competitions download -c porto-seguro-data-challenge`.

1. Salvar os dados no diretório [data](data).

## Execução

O código da solução se encontra no notebook [solution.ipynb](solution.ipynb).