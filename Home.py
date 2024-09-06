import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Home Page", page_icon=":car:", layout="wide")

# Load CSS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css("styles.css")

# Top row: 3 columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📞 Tempo médio de ligações", "10 min")
    # Placeholder for chart (Example: st.plotly_chart() or st.line_chart())
with col2:
    st.metric("📞 Tempo médio de ligações", "10 min")
    # Placeholder for chart
with col3:
    st.metric("💵 Ticket médio", "R$ 200")
    # Placeholder for chart

# Right side column for metrics
with st.sidebar:
    st.image("Files\image.png")
    st.divider()
    st.title("**Dashboard de Vendas**")
    st.subheader("**Resumo do mês**")
    st.metric(label="Faturamento", value="R$ 120,000")
    st.metric(label="Total de vendas", value="530")
    st.metric(label="Ligações totais", value="1200")

# Dados fictícios
oportunidades = np.random.randint(10, 100, size=10)
vendas = np.random.randint(5, 80, size=10)
etapas = ['Etapa 1', 'Etapa 2', 'Etapa 3', 'Etapa 4']
controle_etapas = np.random.randint(1, 10, size=len(etapas))
produtos = ['Produto A', 'Produto B', 'Produto C']
vendas_produto = np.random.randint(20, 100, size=len(produtos))
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
vendas_mes = np.random.randint(50, 200, size=len(meses))
origens = ['Origem 1', 'Origem 2', 'Origem 3']
vendas_origem = np.random.randint(30, 150, size=len(origens))
# Paleta de cores roxa monocromática clara
colors = ['#9370DB', '#8A2BE2', '#7B68EE', '#6A5ACD', '#483D8B']


col4, col5 = st.columns([1, 1])
with col4:
    st.header("Oportunidades x Vendas")
    fig, ax = plt.subplots(figsize=(3.5, 2))
    ax.plot(oportunidades, label='Oportunidades', color=colors[0])
    ax.plot(vendas, label='Vendas', color=colors[1])
    ax.legend(fontsize='x-small')
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('#333333')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    st.pyplot(fig)

with col5:
    st.header("Controle de etapas de ligações")
    fig, ax = plt.subplots(figsize=(3.5, 2))
    ax.bar(etapas, controle_etapas, color=colors)
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('#333333')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    st.pyplot(fig)

# Bottom row: 3 columns
col6, col7, col8 = st.columns(3)
with col6:
    st.header("Venda por produto")
    fig, ax = plt.subplots()
    ax.bar(produtos, vendas_produto, color=colors)
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('#333333')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    st.pyplot(fig)

with col7:
    st.header("Vendas por mês")
    fig, ax = plt.subplots()
    ax.plot(meses, vendas_mes, color=colors[4])
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('#333333')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    st.pyplot(fig)

with col8:
    st.header("Venda por Origem")
    fig, ax = plt.subplots()
    ax.bar(origens, vendas_origem, color=colors)
    fig.patch.set_alpha(0.0)
    ax.set_facecolor('#333333')
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.yaxis.label.set_color('white')
    ax.xaxis.label.set_color('white')
    st.pyplot(fig)