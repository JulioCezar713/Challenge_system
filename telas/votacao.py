import streamlit as st

from services.votacao_service import (
    listar_desafios_votacao
)


def tela_votacao():

    st.title("Votação")

    pesquisa = st.text_input(
        "Pesquisar desafio"
    )

    desafios = listar_desafios_votacao()

    if pesquisa:

        desafios = [
            d for d in desafios
            if pesquisa.lower() in d["titulo"].lower()
        ]

    if not desafios:

        st.warning(
            "Nenhum desafio encontrado"
        )

        return

    for desafio in desafios:

        with st.container(border=True):

            st.subheader(
                desafio["titulo"]
            )

            st.write(
                f"Prazo: {desafio['data_limite']}"
            )

            if st.button(
                "Abrir",
                key=f"abrir_{desafio['id']}"
            ):

                st.session_state.desafio_voto = desafio

                st.session_state.pagina = "voto"

                st.rerun()
