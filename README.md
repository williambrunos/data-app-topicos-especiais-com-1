# Data App - Tópicos Especiais em Computação I | UFC 2024.1

Este é um data app para análise de dados de acidentes de trânsito no Brasil.

O dataset utilizado foi o de [Acidentes 2024 (Agrupados por ocorrência)](https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf) disponibilizado pela Polícia Rodoviária Federal no portal de dados abertos do governo.

Além disso, foi elaborado um Jupyter Notebook para a [análise exploratória dos dados](https://colab.research.google.com/drive/1s5Xt1rJYR8Pt-g9hPRmP453kHKxvxXb8?usp=sharing), este notebook também está [disponível neste repositório](./Notebook.ipynb).

## Equipe

1. Gabriel Vasconcelos Santos - 497688
2. Izaias Machado Pessoa Neto - 497372
3. Márcio Bruno Loiola Gomes - 473740
4. Vinicius Costa dos Santos - 473003
5. Vitor Hugo Muniz de Sousa Santos - 475767
6. Wendel Manfrini de Andrade Mendes - 494899
7. William Bruno Sales de Paula Lima - 497345

## Como executar o projeto localmente

Certifique-se de que o python 3.10 ou superior está instalado em sua máquina.

### Clone do projeto

Primeiramente, realize o clone do projeto:

```Bash
git clone https://github.com/williambrunos/data-app-topicos-especiais-com-1.git
```

### Inicialização do ambiente virtual do python

```Bash
python -m venv venv
```

### Instalação das dependências

```Bash
pip install -r requirements.txt
```

### Inicialização da aplicação

```Bash
streamlit run Home.py
```
