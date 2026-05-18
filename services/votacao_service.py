from database.conexao import supabase


def listar_desafios_votacao():

    resposta = (
        supabase
        .table("desafios")
        .select("*")
        .eq("status", "concluido")
        .execute()
    )

    return resposta.data


def buscar_voto_usuario(
    desafio_id,
    usuario_id
):

    resposta = (
        supabase
        .table("votos")
        .select("*")
        .eq("desafio_id", desafio_id)
        .eq("usuario_id", usuario_id)
        .execute()
    )

    if resposta.data:

        return resposta.data[0]

    return None


def salvar_voto(
    desafio_id,
    usuario_id,
    nota
):

    voto_existente = buscar_voto_usuario(
        desafio_id,
        usuario_id
    )

    if voto_existente:

        supabase.table(
            "votos"
        ).update({

            "nota": nota

        }).eq(
            "id",
            voto_existente["id"]
        ).execute()

    else:

        supabase.table(
            "votos"
        ).insert({

            "desafio_id": desafio_id,
            "usuario_id": usuario_id,
            "nota": nota

        }).execute()


def listar_votos_desafio(
    desafio_id
):

    resposta = (
        supabase
        .table("votos")
        .select("*")
        .eq("desafio_id", desafio_id)
        .execute()
    )

    return resposta.data
