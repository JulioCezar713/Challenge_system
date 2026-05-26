import streamlit as st
from services.mini_provas_service import listar_mini_provas

import streamlit as st

def tela_mini_provas():
    
    if "alto_contraste" not in st.session_state:
        st.session_state.alto_contraste = False

    if st.session_state.alto_contraste:

        st.markdown(
            """
            <style>

            .stApp {
                background-color: black;
                color: white;
            }

            </style>
            """,
            unsafe_allow_html=True
        )

    st.title("Mini Provas")

    col1, col2, col3 = st.columns(3)

    with col1:

        if st.button(
            "Minha Pontuação"
        ):

            st.session_state.pagina = (
                "pontuacao_mini_provas"
            )

            st.rerun()

    with col2:

        if st.button(
            "Desempenho"
        ):

            st.session_state.pagina = (
                "desempenho_mini_provas"
            )

            st.rerun()

    with col3:

        with st.popover(
            "Acessibilidade"
        ):

            alto = st.checkbox(
                "Alto contraste",
                value=st.session_state.alto_contraste
            )

            st.session_state.alto_contraste = alto

            leitura = st.checkbox(
                "Leitura por questão"
            )

            st.divider()

            st.subheader(
                "Solicitar tempo extra"
            )

            prova = st.selectbox(
                "Mini prova",
                [
                    "Mini prova 1",
                    "Mini prova 2"
                ]
            )

            justificativa = st.text_area(
                "Justificativa"
            )

            if st.button(
                "Enviar solicitação"
            ):

                st.success(
                    "Solicitação enviada"
                )

    st.divider()

    pesquisa = st.text_input(
        "Pesquisar mini prova"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "Mini Provas Disponíveis"
        )

    with col2:

        if st.button(
            "Resultados"
        ):

            st.session_state.pagina = (
                "resultados_mini_provas"
            )

            st.rerun()

    mini_provas = listar_mini_provas().data

    for prova in mini_provas:

        with st.container(border=True):

            st.write(
                prova["titulo"]
            )

            st.write(
                f"Descrição: {prova['descricao']}"
            )

            st.write(
                "Mini prova disponível"
            )

            st.write(
                f"Criada em: {prova['data_criacao']}"
            )

            if st.button(
                    f"Fazer prova {prova['id']}"

            ):

                st.session_state.pagina = (
                    "realizar_mini_prova"
                )

                st.rerun()