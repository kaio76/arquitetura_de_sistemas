from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Modelo para representar uma venda
class Venda(BaseModel):
    id_venda: int
    produto: str
    quantidade: int
    preco: float

vendas = []

@app.get("/")
async def root():
    return {"QUANTIDADE DE VENDAS": len(vendas)}

@app.get("/busca_vendas/{id_venda}")
async def pegar_venda_por_id(id_venda: int):
    for venda in vendas:
        if venda.id_venda == id_venda: 
            return venda
    raise HTTPException(status_code=404, detail="Venda não localizada")

@app.post("/vendas/")
async def adicionar_venda(venda: Venda):
    vendas.append(venda)
    return {"id_venda": len(vendas) - 1, "mensagem": "Venda adicionada com sucesso"}

@app.put("/vendas/{id_venda}")
async def atualizar_venda(id_venda: int, venda_atualizada: Venda):
    for idx, venda in enumerate(vendas):
        if venda.id_venda == id_venda:
            vendas[idx] = venda_atualizada
            return {"mensagem": "Venda atualizada com sucesso", "venda": venda_atualizada}
    raise HTTPException(status_code=404, detail="Venda não localizada")

@app.delete("/vendas/{id_venda}")
async def excluir_venda(id_venda: int):
    for idx, venda in enumerate(vendas):
        if venda.id_venda == id_venda:
            del vendas[idx]
            return {"mensagem": "Venda excluída com sucesso"}
    raise HTTPException(status_code=404, detail="Venda não localizada")
    
@app.get("/vendas/")
async def listar_vendas():
    if vendas:
        return vendas
    raise HTTPException(status_code=404, detail="Nenhuma venda encontrada")