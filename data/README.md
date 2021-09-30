# Dados

Para executar o notebook [solution.ipynb](../src/solution.ipynb) devemos obter os seguintes arquivos de dados:

- `train.csv.zip`
- `test.csv.zip`

Os arquivos de dados estão disponíveis no site da competição. Alternativamente, podemos invocar a API do Kaggle com os seguintes comandos:

- `kaggle competitions download -c porto-seguro-data-challenge -f train.csv`
- `kaggle competitions download -c porto-seguro-data-challenge -f test.csv`

O procedimento para configurar a API do Kaggle é descrito a continuação:

## Configuração da [API do Kaggle](https://www.kaggle.com/docs/api) 

Primeiramente, devemos obter token de autenticação `kaggle.json` diretamento do site do Kaggle. Em seguida, realizamos os seguintes procedimentos:

- Salvar o token no diretório `~/.kaggle/kaggle.json`.
- Ajustar permissões do token: `chmod 600 ~/.kaggle/kaggle.json`.