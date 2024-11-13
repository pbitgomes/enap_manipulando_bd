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
resposta = st.slider('Escolha um valor de 0 a 100', 0, 100)
st.write(resposta)

# questão 4
data = {'nomeServidor': ['Adriana', 'Mônica', 'Samara'], 'salario': [1200, 300, 5000]}
df = pd.DataFrame(data)
st.df(df)
servidor = st.selectbox('Qual servidor você gostaria de selecionar?',df[nomeServidor])
st.write('Você selecionou: ', servidor)

st.title('Tipos de campos possíveis')

# criando elementos gráficos
'''Informar como colher os dados através de variáveis'''
x = st.checkbox('Sim')
st.write(x)

# fazer o mesmo com alguns dos comandos abaixo
st.title(x)
st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')

# mensagens de status
st.success("Você conseguiu!")
st.error("Erro!")
st.warning("Advertência")
st.info("Esta é uma informação")
