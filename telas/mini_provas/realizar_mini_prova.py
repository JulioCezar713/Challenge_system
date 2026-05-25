import streamlit as st


def tela_realizar_mini_prova():

    st.title("Realizar Mini Prova")

    st.warning(
        """
        Ao iniciar a mini prova:
        
        - o tempo começará imediatamente;
        - você não poderá sair da tela;
        - caso saia, a prova será encerrada;
        - somente o professor poderá liberar nova tentativa.
        """
    )

    if st.button("Começar"):

        st.success("Mini prova iniciada")

        st.write("Questão 1")

        st.radio(
            "Escolha uma alternativa",
            [
                "Alternativa A",
                "Alternativa B",
                "Alternativa C",
                "Alternativa D",
                "Alternativa E"
            ]
        )

        st.progress(20)

    st.divider()

    if st.button("Voltar"):

        st.session_state.pagina = "mini_provas"

        st.rerun()
