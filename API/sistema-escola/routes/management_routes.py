from fastapi import APIRouter

management_router = APIRouter(prefix="/management", tags=["management"])

@management_router.get("/alunos")
async def mostrar_alunos():
    """"Rota para mostrar a lista de alunos no sistema."""
    return {"mensagem" : "Você acessou a rota de alunos"}