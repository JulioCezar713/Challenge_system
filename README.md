# Challenge_system

Para visualização no streamlit: https://challengesystem-nhyjiafgjapzerhlwhposx.streamlit.app/

Acesso ao Notion: https://www.notion.so/invite/03cf63e02886c912d8564c84ba2dc3bb0aa55498

Observação: Em cada commit, comentar o que foi feito e colocar o nome dos participantes (# e @)


COMO A MAIN ESTÁ ORGANIZADA:

#app.py
É o arquivo que o Streamlit executa quando você roda. Só vai aparecer no streamlit se você colocar/chamar seu código aqui.

#requirements.txt
Lista todas as bibliotecas do projeto.

#streamlit/ secrets.toml/
Pasta de configurações do Streamlit./ Guarda informações sensíveis.

#database/ conexao.py/
Tudo relacionado ao banco de dados./ conexão com o supabase

#services/ auth_service.py/
Ela guarda as regras de negócio do sistema (back-end)./ Responsável por autenticação.

#telas/
todas as telas que terão (front-end)

#utils/ session.py/ permissao.py/
Utilidades gerais do sistema.Coisas que ajudam várias partes do projeto.
Controla sessão do usuário. 
Controla permissões.

#components/ navbar.py/
Partes visuais reutilizáveis. Componentes que se repetem (Barra de navegação do sistema - navbar).
