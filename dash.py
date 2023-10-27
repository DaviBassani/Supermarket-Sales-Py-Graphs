import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Faturamento por unidade
# Tipo de produto mais vendido
# Desempenho da forma de pagamento
# Como estão as avaliações filiais?

df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df =  df.sort_values("Date")

df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

month = st.sidebar.selectbox("Mês", df["Month"].unique())

df_filtered = df[df["Month"] == month]

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total",
                    color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date)

fig_prod = px.bar(df_filtered, x="Date", y="Product line",
                    color="City", orientation="h", 
                    title="Faturamento por tipo de produto")
col2.plotly_chart(fig_prod)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(df_filtered, x="City",
                    y="Total",title="Faturamento por filial")
col3.plotly_chart(fig_city)

fig_kind = px.pie(df_filtered, values="Total", names="Payment",
                   title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

city_total = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(df_filtered, y="Rating", x="City",
                   title="Avaliação")
col5.plotly_chart(fig_rating, use_container_width=True)
