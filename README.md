# Steam-like API

```bash
steam_api_fastapi/
 ├─ app/
 │   ├─ main.py # onde ficam as rotas
 │   ├─ models.py # tabelas do banco
 │   ├─ schemas.py # formatos de respostas
 │   ├─ crud.py # logica de buscas e filtros
 │   ├─ database.py # conexao SQLite
 │   └─ seed.py # popula o banco
 └─ requirements.txt
```


Para rodar a aplicacao:
```bash
python -m app.seed
uvicorn app.main:app --reload
```

Acesse a [Doc](http://127.0.0.1:8000/docs#/) para testar localmente!

```bash
http://127.0.0.1:8000 -> mostra a raiz da API
http://127.0.0.1:8000/docs -> Interface visual para testar rotas
http://127.0.0.1:8000/redoc -> documentacao

```