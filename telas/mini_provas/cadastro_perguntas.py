import streamlit as st
from services.mini_prova_service import criar_questao


def tela_cadastro_perguntas():
    st.title("Cadastro de Perguntas")

    disciplina = st.text_input("Disciplina")
    assunto = st.text_input("Assunto")
    dificuldade = st.selectbox(
        "Dificuldade",
        ["facil", "media", "dificil"]
    )

    pergunta = st.text_area("Pergunta")

    alternativa_a = st.text_input("Alternativa A")
    alternativa_b = st.text_input("Alternativa B")
    alternativa_c = st.text_input("Alternativa C")
    alternativa_d = st.text_input("Alternativa D")
    alternativa_e = st.text_input("Alternativa E")

    resposta_correta = st.selectbox(
        "Resposta correta",
        ["a", "b", "c", "d", "e"]
    )

    if st.button("Cadastrar Pergunta"):
        dados = {
            "disciplina": disciplina,
            "assunto": assunto,
            "dificuldade": dificuldade,
            "pergunta": pergunta,
            "alternativa_a": alternativa_a,
            "alternativa_b": alternativa_b,
            "alternativa_c": alternativa_c,
            "alternativa_d": alternativa_d,
            "alternativa_e": alternativa_e,
            "resposta_correta": resposta_correta
        }

        criar_questao(dados)

        st.success("Pergunta cadastrada com sucesso")
