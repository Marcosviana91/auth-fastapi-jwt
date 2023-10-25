# Autenticação no FastAPI com JWT
> por [Diogo Dev](https://www.youtube.com/@diogodev)
> + Veja a [playlist](https://youtube.com/playlist?list=PLyIsgi-C8ysKOAUEWI-Ehv37AiEKGtWj1&si=BUkOrLLmOBXBIgm_) no youtube
> + Repositório do [GitHub](https://github.com/diogoduartec/auth-fastapi-jwt-youtube)

Neste projeto substituí o banco Postgres, pelo TinyDB (um banco de dados JSON)

## Estrutura do Projeto

1)  na pasta **app**
    + main.py // _criação do app e chamda das rotas_
    + auth_user.py // _rotina da autentcação de usuário_
    + routes.py // _rotas dos endpoints_
    + schemas.py // _esquemas do pydantic (tipagem)_
2) na pasta **app/db** // _pasta com os scripts relacionados ao DB_
    + base.py // _o banco de dados em si_
    + connection.py // _inicia a conexão com o banco_
    + models.py // _modelagem dos dados_
3) na pasta **db_server** // _pasta com os scripts relacionados ao servidor do DB_ **criado por mim**
    + main.py // lógica do bonco de dados
    + user_auth_db.json // _o banco de dados em si_

## 

Gerar chave secreta:
`openssl rand -hex 32`