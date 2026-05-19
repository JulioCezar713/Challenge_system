from database.conexao import supabase


def listar_desafios_votacao():

    resposta = (
        supabase
        .table("tela_desafio")
        .select("*")
        .execute()
    )

    return resposta.data


def buscar_voto_usuario(usuario, desafio):

    resposta = (
        supabase
        .table("votos")
        .select("*")
        .eq("usuario", usuario)
        .eq("desafio", desafio)
        .execute()
    )

    if resposta.data:

        return resposta.data[0]

    return None


def registrar_voto(usuario, desafio, voto):

    return (
        supabase
        .table("votos")
        .insert({
            "usuario": usuario,
            "desafio": desafio,
            "voto": voto
        })
        .execute()
    )


def atualizar_voto(voto_id, novo_voto):

    return (
        supabase
        .table("votos")
        .update({
            "voto": novo_voto
        })
        .eq("id", voto_id)
        .execute()
    )


def deletar_voto(voto_id):

    return (
        supabase
        .table("votos")
        .delete()
        .eq("id", voto_id)
        .execute()
    )


def listar_votos_desafio(desafio):

    resposta = (
        supabase
        .table("votos")
        .select("*")
        .eq("desafio", desafio)
        .execute()
    )

    return resposta.data
