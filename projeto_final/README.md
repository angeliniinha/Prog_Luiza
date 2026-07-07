# [NOME DO PROJETO]

> Substitua pelo nome do seu sistema. Ex: "API de Biblioteca", "API da Pizzaria do Zé".

API REST desenvolvida em Python com Flask e banco de dados SQLite.

**Disciplina:** Programação no Desenvolvimento de Sistemas
**Dupla:** [Nome do integrante 1] e [Nome do integrante 2]

---

## 📋 Sobre o projeto

Descreva em 2 ou 3 linhas o que o seu sistema gerencia.

Exemplo: *Esta API gerencia uma biblioteca. É possível cadastrar autores e livros, sendo que cada livro pertence a um autor. A API permite listar, criar, atualizar, apagar e buscar registros.*

---

## 🗂️ Tabelas do banco

Descreva suas duas tabelas e como elas se relacionam.

### Tabela `[nome_tabela_pai]` (ex: autores)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| nome | TEXT | [descrição] |

### Tabela `[nome_tabela_filho]` (ex: livros)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| titulo | TEXT | [descrição] |
| [pai]_id | INTEGER | Chave estrangeira → aponta para [tabela_pai] |

**Relação:** cada [filho] pertence a um(a) [pai]. *(explique a relação do seu tema)*

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

O banco de dados (`[nome].db`) é criado automaticamente na primeira execução.

---

## 🛣️ Rotas da API

Liste todas as rotas que você criou. Exemplo:

### Tabela [pai]
# [NOME DO PROJETO]

> Substitua pelo nome do seu sistema. Ex: "API de Biblioteca", "API da Pizzaria do Zé".

API REST desenvolvida em Python com Flask e banco de dados SQLite.

**Disciplina:** Programação no Desenvolvimento de Sistemas
**Dupla:** [Nome do integrante 1] e [Nome do integrante 2]

---

## 📋 Sobre o projeto

Descreva em 2 ou 3 linhas o que o seu sistema gerencia.

Exemplo: *Esta API gerencia uma biblioteca. É possível cadastrar autores e livros, sendo que cada livro pertence a um autor. A API permite listar, criar, atualizar, apagar e buscar registros.*

---

## 🗂️ Tabelas do banco

Descreva suas duas tabelas e como elas se relacionam.

### Tabela `[nome_tabela_pai]` (ex: autores)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| nome | TEXT | [descrição] |

### Tabela `[nome_tabela_filho]` (ex: livros)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | INTEGER | Chave primária (gerada automaticamente) |
| titulo | TEXT | [descrição] |
| [pai]_id | INTEGER | Chave estrangeira → aponta para [tabela_pai] |

**Relação:** cada [filho] pertence a um(a) [pai]. *(explique a relação do seu tema)*

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

O banco de dados (`[nome].db`) é criado automaticamente na primeira execução.

---

## 🛣️ Rotas da API

Liste todas as rotas que você criou. Exemplo:

### Tabela [pai]

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/autores` | Lista todos os autores |
| GET | `/autores/<id>` | Busca um autor pelo id |
| POST | `/autores` | Cria um novo autor |
| PUT | `/autores/<id>` | Atualiza um autor |
| DELETE | `/autores/<id>` | Apaga um autor |

### Tabela [filho]

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/livros` | Lista todos os livros |
| POST | `/livros` | Cria um novo livro |
| ... | ... | ... |

### Rotas especiais

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/livros-completo` | Lista livros com o nome do autor (JOIN) |
| GET | `/autores/<id>/livros` | Lista os livros de um autor (filtro por caminho) |
| GET | `/livros/busca?titulo=x` | Busca livros por título (filtro por query) |

---

## 🧪 Como testar

Os testes estão no arquivo [`testes.http`](./testes.http) *(ou `testes.md` se usou curl)*.

Exemplo de requisição para criar um autor:

```http
POST http://127.0.0.1:5000/autores
Content-Type: application/json

{
    "nome": "Machado de Assis"
}
```

---

## 👥 Integrantes

- [Nome 1] — [o que fez no projeto]
- [Nome 2] — [o que fez no projeto]
| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/autores` | Lista todos os autores |
| GET | `/autores/<id>` | Busca um autor pelo id |
| POST | `/autores` | Cria um novo autor |
| PUT | `/autores/<id>` | Atualiza um autor |
| DELETE | `/autores/<id>` | Apaga um autor |

### Tabela [filho]

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/livros` | Lista todos os livros |
| POST | `/livros` | Cria um novo livro |
| ... | ... | ... |

### Rotas especiais

| Método | Rota | O que faz |
|--------|------|-----------|
| GET | `/livros-completo` | Lista livros com o nome do autor (JOIN) |
| GET | `/autores/<id>/livros` | Lista os livros de um autor (filtro por caminho) |
| GET | `/livros/busca?titulo=x` | Busca livros por título (filtro por query) |

---

## 🧪 Como testar

Os testes estão no arquivo [`testes.http`](./testes.http) *(ou `testes.md` se usou curl)*.

Exemplo de requisição para criar um autor:

```http
POST http://127.0.0.1:5000/autores
Content-Type: application/json

{
    "nome": "Machado de Assis"
}
```

---

## 👥 Integrantes

- [Nome 1] — [o que fez no projeto]
- [Nome 2] — [o que fez no projeto]
