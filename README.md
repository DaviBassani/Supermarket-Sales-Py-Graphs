# Documentação do Código

Este código é uma aplicação Streamlit que lê dados de um arquivo CSV chamado "supermarket_sales.csv" e gera visualizações interativas com a biblioteca Plotly Express. A aplicação permite analisar dados de vendas em supermercados, com foco em diferentes aspectos, como faturamento por unidade, tipo de produto mais vendido, desempenho de formas de pagamento e avaliações das filiais.

### Bibliotecas Utilizadas

- `streamlit`: Streamlit é uma biblioteca para criação de aplicativos da web com Python. Ela é usada para construir a interface de usuário e criar elementos interativos.
- `pandas`: Pandas é uma biblioteca popular para manipulação e análise de dados em Python. É usada para ler e processar os dados do arquivo CSV.
- `plotly.express`: Plotly Express é uma biblioteca de visualização de dados que permite criar gráficos interativos de maneira simples e rápida.

### Configuração da Página

- `st.set_page_config(layout="wide")`: Configura a página do aplicativo Streamlit para um layout amplo, permitindo a exibição de várias visualizações lado a lado.

### Leitura e Processamento de Dados

- `df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")`: Lê os dados do arquivo CSV "supermarket_sales.csv". Os parâmetros `sep` e `decimal` são usados para especificar o separador de campo e o separador decimal no arquivo CSV.
- `df["Date"] = pd.to_datetime(df["Date"])`: Converte a coluna "Date" em objetos DateTime para que possam ser usados em análises temporais.
- `df = df.sort_values("Date")`: Classifica o DataFrame pelos valores na coluna "Date" em ordem crescente.
- `df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))`: Cria uma nova coluna chamada "Month" que combina o ano e o mês da coluna "Date".

### Seleção de Mês

- `month = st.sidebar.selectbox("Mês", df["Month"].unique())`: Cria um seletor de mês na barra lateral do aplicativo e permite ao usuário escolher um mês específico para análise.
- `df_filtered = df[df["Month"] == month]`: Filtra o DataFrame original para conter apenas os dados do mês selecionado.

### Visualizações

O código cria cinco visualizações diferentes, que são exibidas em colunas separadas na página do aplicativo.

#### Visualização 1 - Faturamento por Dia

- `fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")`: Cria um gráfico de barras utilizando o Plotly Express para mostrar o faturamento por dia, colorido por filial.

#### Visualização 2 - Faturamento por Tipo de Produto

- `fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", orientation="h", title="Faturamento por tipo de produto")`: Cria um gráfico de barras horizontais que exibe o faturamento por tipo de produto, colorido por filial.

#### Visualização 3 - Faturamento por Filial

- `city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()`: Calcula o faturamento total por filial.
- `fig_city = px.bar(df_filtered, x="City", y="Total", title="Faturamento por filial")`: Cria um gráfico de barras que mostra o faturamento total por filial.

#### Visualização 4 - Faturamento por Tipo de Pagamento

- `fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")`: Cria um gráfico de pizza que exibe a distribuição do faturamento por tipo de pagamento.

#### Visualização 5 - Avaliações das Filiais

- `city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()`: Calcula a média das avaliações por filial.
- `fig_rating = px.bar(df_filtered, y="Rating", x="City", title="Avaliação")`: Cria um gráfico de barras que mostra a avaliação média por filial.

### Exibição das Visualizações

- `col1.plotly_chart(fig_date)`: Exibe a primeira visualização na primeira coluna.
- `col2.plotly_chart(fig_prod)`: Exibe a segunda visualização na segunda coluna.
- `col3.plotly_chart(fig_city)`: Exibe a terceira visualização na terceira coluna.
- `col4.plotly_chart(fig_kind, use_container_width=True)`: Exibe a quarta visualização na quarta coluna com largura ajustada ao container.
- `col5.plotly_chart(fig_rating, use_container_width=True)`: Exibe a quinta visualização na quinta coluna com largura ajustada ao container.

Este código cria um aplicativo interativo que permite a análise de dados de vendas em supermercados de várias perspectivas. O usuário pode selecionar um mês específico e visualizar os dados de faturamento, tipos de produtos, desempenho de formas de pagamento e avaliações das filiais. As visualizações são atualizadas dinamicamente com base na seleção do mês.


# Rodando localmente

Para rodar localmente este código, faça o download de todos os arquivos pelo Github, e, dentro da pasta baixada com todos os arquivos, rode o comando `python3 -m streamlit run dash.py`. Isso fará com que o python rode a aplicação, e você poderá visualizar os gráficos em seu navegador de preferência.


Obs: note que é necessário ter o python e as demais bibliotecas corretamente instalados em seu computador.
