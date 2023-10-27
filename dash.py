import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    # Carrega os dados do arquivo CSV
    df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")
    return df

def filter_data_by_month(df, selected_month):
    # Filtra os dados com base no mês selecionado
    return df[df["Month"] == selected_month]

def generate_revenue_by_day_chart(df_filtered):
    # Gera um gráfico de barras de faturamento por dia
    fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
    return fig_date

def generate_revenue_by_product_chart(df_filtered):
    # Gera um gráfico de barras horizontais de faturamento por tipo de produto
    fig_prod = px.bar(df_filtered, x="Date", y="Product line", color="City", orientation="h", title="Faturamento por tipo de produto")
    return fig_prod

def generate_revenue_by_branch_chart(df_filtered):
    # Gera um gráfico de barras de faturamento por filial
    city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
    fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
    return fig_city

def generate_revenue_by_payment_type_chart(df_filtered):
    # Gera um gráfico de pizza do faturamento por tipo de pagamento
    fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
    return fig_kind

def generate_branch_ratings_chart(df_filtered):
    # Gera um gráfico de barras das avaliações das filiais
    city_avg_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
    fig_rating = px.bar(city_avg_rating, x="City", y="Rating", title="Avaliação")
    return fig_rating

def main():
    st.set_page_config(layout="wide")
    
    df = load_data()
    
    df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))
    unique_months = df["Month"].unique()
    
    selected_month = st.sidebar.selectbox("Selecione um Mês", unique_months)
    
    df_filtered = filter_data_by_month(df, selected_month)
    
    col1, col2 = st.columns(2)
    col3, col4, col5 = st.columns(3)
    
    col1.plotly_chart(generate_revenue_by_day_chart(df_filtered))
    col2.plotly_chart(generate_revenue_by_product_chart(df_filtered))
    col3.plotly_chart(generate_revenue_by_branch_chart(df_filtered))
    col4.plotly_chart(generate_revenue_by_payment_type_chart(df_filtered), use_container_width=True)
    col5.plotly_chart(generate_branch_ratings_chart(df_filtered), use_container_width=True)

if __name__ == "__main__":
    main()
