# [Porto Seguro Data Challenge | Kaggle](https://www.kaggle.com/c/porto-seguro-data-challenge)
Modelo de propensão de aquisição a novos produtos.

## Configurações de ambiente no [Google Cloud](https://cloud.google.com/)

Para criar um notebook no ambiente do [Google Cloud](https://cloud.google.com/) com suporte à linguagem de programação **Python**, execute o seguinte comando no [Cloud Shell](https://cloud.google.com/shell):

```console
gcloud notebooks instances create kaggle-20210928 --container-repository=gcr.io/kaggle-images/python --container-tag=latest --machine-type=c2-standard-4 --location us-west1-b
```

Utilizando o terminal do notebook, podemos também configurar a [API do Kaggle](https://www.kaggle.com/docs/api) para obter os dados do desafio e para realizar a submissão da solução.

1. Obter token de autenticação `kaggle.json`.
2. Salvar o token no diretório `~/.kaggle/kaggle.json`.
3. Ajustar permissões do token `chmod 600 ~/.kaggle/kaggle.json`.

## Solução

O código da solução para do desafio se encontra no notebook [solution.ipynb](solution.ipynb). 

## Modelo

O módulo [model.py](model.py) contém a classe `Model` consumida pelo notebook, e fornece métodos para treinamento do modelo e submissão da solução.