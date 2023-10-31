# Sobre

Este é um aplicativo Streamlit que permite a análise de dados de vendas em supermercados a partir do arquivo CSV "supermarket_sales.csv". Ele oferece visualizações interativas em cinco aspectos principais: faturamento por dia, faturamento por tipo de produto, faturamento por filial, faturamento por tipo de pagamento e avaliações das filiais.

## Bibliotecas Utilizadas

- `streamlit`: Streamlit é uma biblioteca para criação de aplicativos da web com Python. Ela é usada para construir a interface de usuário e criar elementos interativos.

- `pandas`: Pandas é uma biblioteca popular para manipulação e análise de dados em Python. É usada para ler e processar os dados do arquivo CSV.

- `plotly.express`: Plotly Express é uma biblioteca de visualização de dados que permite criar gráficos interativos de maneira simples e rápida.

## Configuração da Página

- `st.set_page_config(layout="wide")`: Configura a página do aplicativo Streamlit para um layout amplo (wide), permitindo a exibição de várias visualizações lado a lado.

## Leitura e Processamento de Dados

- `df = load_data()`: Esta função carrega os dados do arquivo CSV "supermarket_sales.csv" e realiza algumas etapas de pré-processamento, como a conversão da coluna "Date" em objetos DateTime.

- `df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))`: Cria uma nova coluna chamada "Month" que combina o ano e o mês da coluna "Date" para análise temporal.

## Seleção de Mês

- `selected_month = st.sidebar.selectbox("Selecione um Mês", unique_months)`: Permite ao usuário selecionar um mês específico para análise, utilizando um seletor na barra lateral.

## Visualizações

O código cria cinco visualizações diferentes, que são exibidas em colunas separadas na página do aplicativo.

### Visualização 1 - Faturamento por Dia

- `generate_revenue_by_day_chart(df_filtered)`: Gera um gráfico de barras utilizando o Plotly Express para mostrar o faturamento por dia, colorido por filial.

### Visualização 2 - Faturamento por Tipo de Produto

- `generate_revenue_by_product_chart(df_filtered)`: Gera um gráfico de barras horizontais que exibe o faturamento por tipo de produto, colorido por filial.

### Visualização 3 - Faturamento por Filial

- `generate_revenue_by_branch_chart(df_filtered)`: Gera um gráfico de barras que mostra o faturamento total por filial.

### Visualização 4 - Faturamento por Tipo de Pagamento

- `generate_revenue_by_payment_type_chart(df_filtered)`: Gera um gráfico de pizza que exibe a distribuição do faturamento por tipo de pagamento.

### Visualização 5 - Avaliações das Filiais

- `generate_branch_ratings_chart(df_filtered)`: Gera um gráfico de barras que mostra a avaliação média das filiais.

## Exibição das Visualizações

- As visualizações são exibidas em colunas separadas no aplicativo, utilizando as funções `col1.plotly_chart()`, `col2.plotly_chart()`, `col3.plotly_chart()`, `col4.plotly_chart()`, e `col5.plotly_chart()`. O uso de colunas ajuda a organizar as visualizações de forma eficaz.

Este código cria um aplicativo interativo que permite a análise de dados de vendas em supermercados de várias perspectivas. O usuário pode selecionar um mês específico e visualizar os dados de faturamento, tipos de produtos, desempenho de formas de pagamento e avaliações das filiais. As visualizações são atualizadas dinamicamente com base na seleção do mês.

## Rodando Localmente

Para executar este código localmente, siga estas etapas:
1. Faça o download de todos os arquivos do repositório.
2. Abra um terminal na pasta onde os arquivos estão localizados.
3. Execute o comando `python3 -m streamlit run nome_do_arquivo.py`, onde `nome_do_arquivo.py` é o nome do arquivo Python que contém o código Streamlit.

Certifique-se de que você tenha o Python e as bibliotecas necessárias corretamente instaladas em seu ambiente de desenvolvimento.
