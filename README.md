# Portfólio de Projetos

## Sobre

Projetos focados em Backend e APIs utilizando o ecossistema Python. Minhas principais competências técnicas incluem:

* **Linguagens e Frameworks:** Python e FastAPI.
* **Arquitetura:** REST
* **Banco de Dados e Migrations:** PostgreSQL, SQLAlchemy e Alembic.
* **Segurança:** Autenticação JWT e criptografia de senhas.

---

## Projetos

### Template API

Template de API REST baseado no template oficial do FastAPI, configurado para acelerar o desenvolvimento de novos projetos.

[![Repository](https://img.shields.io/badge/repository-template--api-blue?style=flat-square)](https://github.com/lincolntaranto/template-api)
[![CI / Tests](https://img.shields.io/github/actions/workflow/status/lincolntaranto/template-api/ci.yml?label=CI%20/%20Tests&style=flat-square&logo=github-actions)](https://github.com/lincolntaranto/template-api)
[![Linter: Ruff](https://img.shields.io/badge/linter-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)
[![Dependabot](https://img.shields.io/badge/dependabot-active-brightgreen?style=flat-square&logo=dependabot)](https://github.com/lincolntaranto/template-api/blob/main/.github/dependabot.yml)
[![Deploy](https://img.shields.io/badge/deploy-render-purple)]()
[![Status](https://img.shields.io/badge/status-online-success)](https://template-api-89m8.onrender.com/docs)
[![Email: Resend](https://img.shields.io/badge/email-Resend-000000?style=flat-square&logo=resend)](https://resend.com/)

#### Especificações Técnicas

| Componente        | Ferramenta Utilizada    | Finalidade                                     |
| :---------------- | :---------------------- | :--------------------------------------------- |
| **Framework**     | FastAPI                 | Criação das rotas e documentação automática    |
| **ORM**           | SQLAlchemy 2.0          | Mapeamento e consultas ao banco de dados       |
| **Database**      | PostgreSQL              | Armazenamento relacional dos dados             |
| **Migrations**    | Alembic                 | Controle de versão do banco de dados           |
| **Configurações** | Pydantic Settings       | Gerenciamento de variáveis via arquivo `.env`  |
| **Segurança**     | pwdlib (Argon2) & PyJWT | Criptografia de senhas e geração de tokens JWT |
| **Comunicação**   | Resend + Jinja2         | Estruturação e envio automatizado de emails    |
| **Qualidade**     | Pytest & Ruff           | Testes integrados e linter de código           |

#### Funcionalidades Prontas

* Autenticação e Login JWT.
* CRUD completo de Usuários com hash seguro.
* Sistema integrado para disparo de emails.
* Suíte completa de testes automatizados e esteira de CI.

> **Acesse o código completo:** [Repositório Template API](https://github.com/lincolntaranto/template-api)

---

### API Sistema Escola

API REST para gestão escolar, cobrindo alunos, turmas, notas e controle de acesso com sistema de convites.

[![Repository](https://img.shields.io/badge/repository-API--Sistema--Escola-blue?style=flat-square)](https://github.com/lincolntaranto/API-Sistema-Escola)

[![Linter: Ruff](https://img.shields.io/badge/linter-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff)

#### Especificações Técnicas

| Componente        | Ferramenta Utilizada | Finalidade                                       |
| :---------------- | :------------------- | :----------------------------------------------- |
| **Framework**     | FastAPI              | Criação das rotas e documentação automática      |
| **ORM**           | SQLAlchemy           | Mapeamento e consultas ao banco de dados         |
| **Database**      | PostgreSQL           | Armazenamento relacional dos dados               |
| **Migrations**    | Alembic              | Controle de versão do banco de dados             |
| **Configurações** | Pydantic Settings    | Gerenciamento de variáveis via arquivo `.env`    |
| **Segurança**     | Bcrypt & Python-Jose | *Criptografia de senhas e geração de tokens JWT* |
| **Qualidade**     | Ruff                 | Linter de código                                 |

#### Funcionalidades Prontas

* Autenticação e Login JWT.
* CRUD completo de alunos com hash seguro.
* CRUD completo de turmas com hash seguro.
* CRUD completo de cargos com hash seguro.
* CRUD completo de notas com hash seguro.
* Sistema de convite.

> **Acesse o código completo:** [API-Sistema-Escola](https://github.com/lincolntaranto/API-Sistema-Escola)

---

## Contato

* **LinkedIn:** [linkedin.com/in/lincolntaranto](https://linkedin.com/in/lincolntaranto)
