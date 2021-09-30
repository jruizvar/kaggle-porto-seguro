# [Porto Seguro Data Challenge | Kaggle](https://www.kaggle.com/c/porto-seguro-data-challenge)
Modelo de propensão de aquisição a novos produtos.

## Configurações de ambiente no [Google Cloud](https://cloud.google.com/)

Para criar um notebook no ambiente do [Google Cloud](https://cloud.google.com/) com suporte à linguagem de programação **Python**, executamos o seguinte comando no [Cloud Shell](https://cloud.google.com/shell):

```console
gcloud notebooks instances create kaggle-20210928 --container-repository=gcr.io/kaggle-images/python --container-tag=latest --machine-type=c2-standard-4 --location us-west1-b
```

O comando anterior pressupõe a existência de um projeto no ambiente da Google Cloud com possibilidade de cobranças.