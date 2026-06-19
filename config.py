import os
from fastapi import FastAPI

app = FastAPI()

# O Render vai preencher isso automaticamente em produção
DATABASE_URL = os.getenv("DATABASE_URL")
API_SECRET_KEY = os.getenv("MINHA_CHAVE_SECRETA")

@app.get("/")
def read_root():
    # Apenas um teste para saber se a variável foi lida (não exiba senhas reais no print/retorno!)
    if API_SECRET_KEY:
        return {"status": "API configurada corretamente e chave encontrada!"}
    return {"status": "Erro: Chave não encontrada."}