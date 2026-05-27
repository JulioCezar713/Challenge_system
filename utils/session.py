import streamlit as st


def iniciar_session():

    if "usuario_logado" not in st.session_state:
        st.session_state.usuario_logado = None

    if "pagina" not in st.session_state:
        st.session_state.pagina = "login"
        
    if "tipo_usuario" not in st.session_state:
        st.session_state.tipo_usuario = "aluno"

    if "alto_contraste" not in st.session_state:
        st.session_state.alto_contraste = False
        
     if "batalha_sub_pagina" not in st.session_state:
        st.session_state.batalha_sub_pagina = "hub"

    if "batalha_selecionada_id" not in st.session_state:
        st.session_state.batalha_selecionada_id = None
