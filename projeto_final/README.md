# [PIZZARIA DELICIA]

> API da Pizzaria

API REST desenvolvida em Python com Flask e banco de dados SQLite.

**Disciplina:** Programação no Desenvolvimento de Sistemas  
**Dupla:** [Nome do integrante 1] e [Nome do integrante 2]

---

## 📋 Sobre o projeto

Esta API gerencia uma pizzaria. É possível cadastrar categorias de pizzas e as pizzas pertencentes a cada categoria. A API permite listar, criar, atualizar, excluir e pesquisar registros, além de realizar consultas utilizando JOIN e filtros.

---

## 🗂️ Tabelas do banco

Descreva suas duas tabelas e como elas se relacionam.

### Tabela `categorias` (ex: autores)

| Campo | Tipo    | Descrição                               |
| ----- | ------- | --------------------------------------- |
| id    | INTEGER | Chave primária (gerada automaticamente) |
| nome  | TEXT    | Nome da categoria da pizza              |

### Tabela `pizzas` (ex: livros)

| Campo | Tipo | Descrição |
| ----- | ---- | --------- |
| id | INTEGER | Chave primária (gerada automaticamente) |
| nome | TEXT | Nome da pizza |
| preco | REAL | Preço da pizza |
| categoria_id | INTEGER | Chave estrangeira → aponta para categorias |

**Relação:** cada pizza pertence a uma categoria, e uma categoria pode possuir várias pizzas.

---

## 🚀 Como rodar o projeto

```bash
# 1. Instalar o Flask (caso não tenha)
pip install flask

# 2. Rodar a API
python app.py

# 3. A API estará disponível em:
# http://127.0.0.1:5000
```

O banco de dados (`pizzaria.db`) é criado automaticamente na primeira execução.

---

## 🛣️ Rotas da API

Liste todas as rotas que você criou. Exemplo:

### Tabela [pai]

| Método | Rota | O que faz |
| ------ | ---- | --------- |
| GET | `/categorias` | Lista todas as categorias |
| GET | `/categorias/<id>` | Busca uma categoria pelo id |
| POST | `/categorias` | Cria uma nova categoria |
| PUT | `/categorias/<id>` | Atualiza uma categoria |
| DELETE | `/categorias/<id>` | Apaga uma categoria |

### Tabela [filho]

| Método | Rota | O que faz |
| ------ | ---- | --------- |
| GET | `/pizzas` | Lista todas as pizzas |
| GET | `/pizzas/<id>` | Busca uma pizza pelo id |
| POST | `/pizzas` | Cria uma nova pizza |
| PUT | `/pizzas/<id>` | Atualiza uma pizza |
| DELETE | `/pizzas/<id>` | Apaga uma pizza |

### Rotas especiais

| Método | Rota | O que faz |
| ------ | ---- | --------- |
| GET | `/pizzas/detalhes` | Lista pizzas com o nome da categoria (JOIN) |
| GET | `/categorias/<id>/pizzas` | Lista as pizzas de uma categoria (filtro por caminho) |
| GET | `/pizzas/busca?nome=x` | Busca pizzas por nome (filtro por query) |

---

## 🧪 Como testar

Os testes estão no arquivo [`testes.http`](./testes.http) *(ou* *`testes.md`* *se usou curl)*.

Exemplo de requisição para criar uma categoria:

```http
POST http://127.0.0.1:5000/categorias
Content-Type: application/json

{
    "nome": "Tradicionais"
}

---

## 👥 Integrantes

- Luiza Angelina Locatelli Loureiro — Fez tudo.
