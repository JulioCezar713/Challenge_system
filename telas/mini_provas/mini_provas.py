import streamlit as st

from services.mini_prova_service import (
    listar_mini_provas
)


def tela_mini_provas():

    st.title("Mini Provas")

    st.button("Minha pontuação: 0")

    pesquisa = st.text_input(
        "Pesquisar mini prova"
    )

    provas = listar_mini_provas().data

    for prova in provas:

        if pesquisa.lower() in prova["titulo"].lower():

            st.subheader(prova["titulo"])

            st.write(
                f"Disciplina: {prova['disciplina']}"
            )

            st.write(
                f"Assunto: {prova['assunto']}"
            )

            st.write(
                f"Pontuação: {prova['pontos']}"
            )

            if st.button(
                f"Iniciar {prova['id']}"
            ):

                st.session_state[
                    "mini_prova"
                ] = prova

                st.switch_page(
                    "telas/mini_provas/realizar_mini_prova.py"
                )
