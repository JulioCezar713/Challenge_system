from database.conexao import supabase


def buscar_voto_usuario(
    usuario_id,
    apresentacao_id
):

    resposta = (
        supabase
        .table("votos")
        .select("*")
        .eq("usuario_id", usuario_id)
        .eq("apresentacao_id", apresentacao_id)
        .execute()
    )

    if resposta.data:

        return resposta.data[0]

    return None


def registrar_voto(
    usuario_id,
    apresentacao_id,
    nota
):

    voto_existente = (
        buscar_voto_usuario(
            usuario_id,
            apresentacao_id
        )
    )

    # EDITA O VOTO

    if voto_existente:

        return (
            supabase
            .table("votos")
            .update({

                "nota": nota

            })
            .eq(
                "id",
                voto_existente["id"]
            )
            .execute()
        )

    # CRIA O VOTO

    return (
        supabase
        .table("votos")
        .insert({

            "usuario_id": usuario_id,
            "apresentacao_id": apresentacao_id,
            "nota": nota

        })
        .execute()
    )


def listar_votos():

    resposta = (
        supabase
        .table("votos")
        .select("*")
        .execute()
    )

    return resposta.data


def listar_votos_apresentacao(
    apresentacao_id
):

    resposta = (
        supabase
        .table("votos")
        .select("*")
        .eq(
            "apresentacao_id",
            apresentacao_id
        )
        .execute()
    )

    return resposta.data
