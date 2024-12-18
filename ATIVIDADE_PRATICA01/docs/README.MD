# 🚀 **API de Gerenciamento de Vendas** 📦

Este projeto é uma **API RESTful** simples, desenvolvida como parte de um trabalho escolar na disciplina de **Arquitetura de Sistemas**. O objetivo é gerenciar informações sobre vendas, permitindo a adição, busca, atualização e exclusão de registros de vendas em uma plataforma de e-commerce ou loja.

---

## 🎯 **Problema que a API Resolve**

A **API de Gerenciamento de Vendas** resolve o problema de **gerenciamento e controle de vendas**, facilitando o armazenamento, consulta e atualização de informações relacionadas às transações de uma loja. Com ela, é possível:

- 📋 **Adicionar novas vendas** à lista.
- 🔍 **Buscar uma venda específica** através do ID.
- 🔄 **Atualizar informações de uma venda** existente.
- ❌ **Excluir vendas** que não são mais necessárias.

A API permite que desenvolvedores integrem esse sistema em outros aplicativos ou plataformas que necessitem de um gerenciamento simples e eficiente das transações de vendas.

---

## 🛠️ **Como Executar o Projeto Localmente**

### 1. **Clone o Repositório**

Primeiro, clone o repositório para o seu ambiente local:

```bash

git clone https://github.com/kaio76/arquitetura_de_sistemas/tree/main/ATIVIDADE_PRATICA01
´´´
2. Instale as Dependências
Instale as bibliotecas e dependências necessárias utilizando o pip:

bash
Copiar código
cd ATIVIDADE_PRATICA01
pip install -r requirements.txt

3. Execute o Servidor
Para rodar a API localmente, execute o seguinte comando:

bash
Copiar código
uvicorn main:app --reload
Isso iniciará a API no endereço http://localhost:8000. Agora você pode acessar e testar a API localmente.

📚 Exemplos de Uso das Rotas
A API oferece as seguintes rotas principais para interação:

1. Adicionar uma Venda (POST) 📝

Requisição
Método: POST
URL: http://localhost:8000/vendas/
Body (JSON):
json
Copiar código
{
  "id_venda": 1,
  "produto": "Produto X",
  "quantidade": 2,
  "preco": 100.0
}
Resposta (sucesso)
json
Copiar código
    {
      "id_venda": 0,
      "mensagem": "Venda adicionada com sucesso"
    }
2. Buscar uma Venda por ID (GET) 🔍
Requisição
Método: GET
URL: http://localhost:8000/busca_vendas/{id_venda}
Exemplo: http://localhost:8000/busca_vendas/1
Resposta (sucesso)
json
Copiar código
{
  "id_venda": 1,
  "produto": "Produto X",
  "quantidade": 2,
  "preco": 100.0
}
Resposta (venda não encontrada)
json
Copiar código
{
  "detail": "Venda não localizada"
}
3. Atualizar uma Venda (PUT) 🔄
Requisição
Método: PUT
URL: http://localhost:8000/vendas/{id_venda}
Exemplo: http://localhost:8000/vendas/1
Body (JSON):
json
Copiar código
{
  "id_venda": 1,
  "produto": "Produto Y",
  "quantidade": 3,
  "preco": 150.0
}
Resposta (sucesso)
json
Copiar código
{
  "mensagem": "Venda atualizada com sucesso",
  "venda": {
    "id_venda": 1,
    "produto": "Produto Y",
    "quantidade": 3,
    "preco": 150.0
  }
}
4. Excluir uma Venda (DELETE) ❌
Requisição
Método: DELETE
URL: http://localhost:8000/vendas/{id_venda}
Exemplo: http://localhost:8000/vendas/1
Resposta (sucesso)
json
Copiar código
{
  "mensagem": "Venda excluída com sucesso"
}

📜 Tecnologias Utilizadas
Este projeto foi desenvolvido utilizando as seguintes tecnologias:

Python 🐍
FastAPI 🚀
Uvicorn 🦄
Pydantic 📦

🔧 Considerações Finais
Este projeto foi desenvolvido para fins educacionais, buscando aplicar os conceitos de Arquitetura de Sistemas e Desenvolvimento de APIs. A API tem uma estrutura simples e pode ser expandida para incluir novas funcionalidades, como autenticação de usuários ou integração com banco de dados real.

Link da documentação do postman:
[text](https://documenter.getpostman.com/view/40506200/2sAYJ1k2a2)
