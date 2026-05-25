import streamlit as st
    assunto = st.text_input("Assunto")

    quantidade_total = st.number_input(
        "Quantidade total de perguntas",
        min_value=1,
        step=1
    )

    st.subheader("Quantidade por dificuldade")

    quantidade_faceis = st.number_input(
        "Fáceis",
        min_value=0,
        step=1
    )

    quantidade_medias = st.number_input(
        "Médias",
        min_value=0,
        step=1
    )

    quantidade_dificeis = st.number_input(
        "Difíceis",
        min_value=0,
        step=1
    )

    tempo = st.number_input(
        "Tempo em minutos",
        min_value=1,
        step=1
    )

    pontos = st.number_input(
        "Pontuação",
        min_value=0.1,
        step=0.1
    )

    soma = (
        quantidade_faceis +
        quantidade_medias +
        quantidade_dificeis
    )

    if soma != quantidade_total:

        st.error(
            "A soma das dificuldades deve bater com o total"
        )

    if st.button("Cadastrar Mini Prova"):

        st.success(
            "Mini prova cadastrada visualmente"
        )

    st.divider()

    if st.button("Voltar"):

        st.switch_page(
            "telas/mini_provas/mini_provas_professor.py"
        )
