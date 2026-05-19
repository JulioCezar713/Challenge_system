import streamlit as st
import pandas as pd

from services.votacao_service import (
    listar_desafios_votacao,
    registrar_voto,
    buscar_voto_usuario,
    atualizar_voto,
    listar_votos_desafio,
    deletar_voto
)


def tela_votacao():

    st.title("Votação")

    usuario = st.session_state.usuario_logado

    desafios = listar_desafios_votacao()

    if not desafios:

        st.warning(
            "Nenhum desafio disponível para votação"
        )

        return

    st.subheader(
        "Desafios disponíveis"
    )

    for desafio in desafios:

        with st.container(border=True):

            st.write(
                f"### {desafio['titulo']}"
            )

            st.write(
                f"Prazo: {desafio['prazo']}"
            )

            if st.button(
                "Abrir votação",
                key=f"abrir_{desafio['id']}"
            ):

                st.session_state.desafio_votacao = desafio

                st.rerun()

    if "desafio_votacao" not in st.session_state:

        return

    desafio = st.session_state.desafio_votacao

    st.divider()

    st.subheader(
        f"Votando em: {desafio['titulo']}"
    )

    voto_existente = buscar_voto_usuario(
        usuario["email"],
        desafio["titulo"]
    )

    opcoes = [
        "Bom",
        "Regular",
        "Ruim"
    ]

    voto = st.radio(
        "Escolha seu voto",
        opcoes
    )

    if not voto_existente:

        if st.button(
            "Enviar voto"
        ):

            registrar_voto(
                usuario["email"],
                desafio["titulo"],
                voto
            )

            st.success(
                "Voto registrado"
            )

            st.rerun()

    else:

        st.info(
            f"Seu voto atual: {voto_existente['voto']}"
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "Atualizar voto"
            ):

                atualizar_voto(
                    voto_existente["id"],
                    voto
                )

                st.success(
                    "Voto atualizado"
                )

                st.rerun()

        with col2:

            if st.button(
                "Excluir voto"
            ):

                deletar_voto(
                    voto_existente["id"]
                )

                st.success(
                    "Voto removido"
                )

                st.rerun()

    st.divider()

    st.subheader(
        "Resultado do desafio"
    )

    votos = listar_votos_desafio(
        desafio["titulo"]
    )

    if votos:

        df = pd.DataFrame(votos)

        contagem = df["voto"].value_counts()

        contagem = contagem.reindex(
            ["Bom", "Regular", "Ruim"],
            fill_value=0
        )

        st.bar_chart(contagem)

        st.write(
            f"Total de votos: {len(df)}"
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "Nenhum voto registrado"
        )
