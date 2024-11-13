import streamlit as st

st.title('Isso é um título')

st.write('Vamos aprender streamlit juntos')

# questão 2
st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

# questão 3
resposta = st.select_slider('Escolha um valor de 0 a 100', 0, 100)
st.write(resposta)
