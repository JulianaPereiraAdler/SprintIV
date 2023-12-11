# API de Diligência de Compliance


Este projeto faz parte do MPV da Sprint IV da Pós Graduação em Engenharia de Software da Juliana Pereira Adler

### Descrição
API de Sistema de Previsão de Insuficiência Cardíaca é uma ferramenta vital para o diagnóstico precoce e a prevenção de mortes causadas por doenças cardiovasculares (DCVs), que são a principal causa de morte globalmente, com cerca de 17,9 milhões de óbitos anualmente. Utilizando um conjunto de 918 observações de várias fontes, o sistema analisa 11 características chave, como idade, sexo, tipo de dor no peito, pressão arterial em repouso, colesterol, glicemia em jejum, ECG em repouso, frequência cardíaca máxima, angina induzida por exercício, Oldpeak e a inclinação do segmento ST.

O objetivo do sistema é fornecer uma análise de dados precisa e eficiente para apoiar profissionais de saúde no tratamento e prevenção de doenças cardíacas, contribuindo significativamente para a gestão da saúde cardiovascular.

A API foi implementada seguindo o estilo REST usando Flask.
 - [Flask](https://flask.palletsprojects.com/en/2.3.x/) 

Dataset: https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

---
### Instalação

Certifique-se de ter todas as bibliotecas Python listadas no `requirements.txt` instaladas. Após clonar o repositório, navegue ao diretório raiz pelo terminal para executar os comandos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).
> No Ambiente Windows foi utilizado o comando (python -m venv env) para a criação do ambiente virtual e o comando (env\Scripts\activate) para ativar o ambiente virtual.

```
(env)$ pip install -r requirements.txt
```
Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

---
### Executando o servidor

Para iniciar a API, execute:

```
(env)$ flask run --host 0.0.0.0 --port 5001
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5001 --reload
```

---
### Acesso no browser

Abra o [http://localhost:5001/#/](http://localhost:5001/#/) no navegador para verificar o status da API em execução.

---