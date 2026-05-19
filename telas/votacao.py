import streamlit as st
import pandas as pd

from services.votacao_service import (
    listar_desafios_votacao,
    registrar_voto,
    listar_votos
)


def tela_votacao():

    st.title("Votação")

    usuario = st.session_state.usuario_logado

    desafios = listar_desafios_votacao()

    if not desafios:

        st.warning(
            "Nenhum desafio disponível"
        )

        return

    for desafio in desafios:

        with st.container(border=True):

            st.subheader(
                desafio["titulo"]
            )

            st.write(
                desafio["descricao"]
            )

            st.write(
                f"Nível: {desafio['nivel']}"
            )

            st.write(
                f"Prazo: {desafio['prazo']}"
            )

            voto = st.radio(
                "Escolha seu voto",
                ["Bom", "Regular", "Ruim"],
                key=f"radio_{desafio['id']}"
            )

            if st.button(
                "Enviar voto",
                key=f"botao_{desafio['id']}"
            ):

                sucesso = registrar_voto(
                    usuario["email"],
                    desafio["titulo"],
                    voto
                )

                if sucesso:

                    st.success(
                        "Voto registrado"
                    )

                    st.rerun()

                else:

                    st.warning(
                        "Você já votou neste desafio"
                    )

    st.divider()

    st.subheader(
        "Resultado Geral"
    )

    votos = listar_votos()

    if votos:

        df = pd.DataFrame(votos)

        contagem = (
            df["voto"]
            .value_counts()
        )

        contagem = contagem.reindex(
            ["Bom", "Regular", "Ruim"],
            fill_value=0
        )

        st.bar_chart(contagem)

        st.write(
            "Quantidade de votos:"
        )

        st.write(contagem)

    else:

        st.info(
            "Nenhum voto registrado"
        )
