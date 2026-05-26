import streamlit as st
from datetime import date

from services.desafio_service import (
    criar_desafio,
    listar_desafios,
    deletar_desafio
)


def tela_desafios():

    usuario = st.session_state.usuario_logado

    if usuario ["tipo_usuario"] != "professor":
        st.error(
            "Apenas professores podem criar desafios"
        )
        return

    st.title("Desafios")

    menu = st.sidebar.selectbox(
        "Menu",
        ["Criar", "Listar", "Deletar"]
    )


    if menu == "Criar":

        criador_id = usuario["id"]

        st.subheader("Criar novo desafio")

        titulo = st.text_input("Título")

        descricao = st.text_area("Descrição")

        nivel = st.selectbox("Nivel",["Fácil","Médio","Difícil"])


        disciplina_id = st.number_input(
            "ID da Disciplina",
            min_value=1,
            step=1
        )

        data_limite = st.date_input(
            "Data Limite",
            min_value=date.today()
        )

        if st.button("Criar Desafio"):

            resultado = criar_desafio(
                titulo,
                descricao,
                nivel,
                criador_id,
                disciplina_id,
                data_limite,
            )

            if resultado["sucesso"]:
                st.success("Desafio criado com sucesso!")

            else:
                st.error(resultado["mensagem"])

    elif menu == "Listar":

        st.subheader("Lista de desafios")

        desafios = listar_desafios()

        for desafio in desafios:

            st.write(f"ID: {desafio['id']}")
            st.write(f"Título: {desafio['titulo']}")
            st.write(f"Descrição: {desafio['descricao']}")

            st.write("---")

    elif menu == "Deletar":

        st.subheader("Deletar desafio")

        desafios = listar_desafios()

        ids = [d["id"] for d in desafios]

        id_escolhido = st.selectbox(
            "Selecione o desafio",
            ids
        )

        if st.button("Deletar"):

            deletar_desafio(id_escolhido)

            st.warning("Desafio deletado!")