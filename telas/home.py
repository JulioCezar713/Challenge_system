import streamlit as st
from services.desafio_service import listar_desafios
from services.batalha_de_equipes_service import listar_batalhas, time_do_usuario

def tela_home():

    usuario = st.session_state.usuario_logado

    st.title(
        f"Bem-vindo(a), {usuario['nome']}"
    )

    st.divider()

    st.subheader(
        "Desafios disponíveis"
    )
    desafios = listar_desafios()

    if desafios:

        for desafio in desafios[:5]:
            with st.container(border=True):
                st.write(
                    f" {desafio['titulo']}"
                )

                st.caption(
                    f"Nível: {desafio['nivel']}"
                )

                st.write(
                    desafio['descricao']
                )

                st.write(
                    f"Prazo: {desafio['data_limite']}"
                )

    else:

        st.info(
            "Nenhum desafio disponível"
        )

    st.divider()

    # Votação
    st.subheader(
        "Votação disponíveis"
    )

    if desafios:

        for desafio in desafios[:5]:
            st.write(
                f" {desafio['titulo']}"
            )

    else:

        st.info(
            "Nenhum desafio disponível para voto"
        )

    st.divider()

    st.subheader(
        "Mini-provas"
    )

    st.warning(
        "Sistema em construção"
    )

    st.divider()

    st.subheader(
        "Quiz ao Vivo"
    )

    st.warning(
        "Sistema em construção"
    )

    st.divider()

    # ── Batalha de Equipes ─────────────────────────────────────────
    st.subheader("⚔️ Batalha de Equipes")

    batalhas = listar_batalhas()
    batalhas_ativas = [b for b in batalhas if b.get("status") == "em_andamento"]
    meu_time = time_do_usuario(usuario["id"])

    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.metric("Batalhas ativas", len(batalhas_ativas))

    with col2:
        with st.container(border=True):
            if meu_time:
                time_nome = meu_time.get("times", {}).get("nome", "—")
                st.metric("Seu time", time_nome)
            else:
                st.metric("Seu time", "Sem time")

    if batalhas_ativas:
        st.write("**Em andamento agora:**")
        for b in batalhas_ativas[:3]:
            time_a = b.get("times_a", {}).get("nome", "Time A")
            time_b = b.get("times_b", {}).get("nome", "Time B")
            st.write(f"• **{b['titulo']}** — 🔵 {time_a} vs 🔴 {time_b}")

    if st.button("Ver todas as batalhas →"):
        st.session_state.pagina = "batalha_de_equipes"
        st.session_state.batalha_sub_pagina = "hub"
        st.rerun()
