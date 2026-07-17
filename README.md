# Portfólio de Projetos

## Sobre

Projetos focados em Backend e APIs utilizando o ecossistema Python. Minhas principais competências técnicas incluem:

- **Linguagens e Frameworks:** Python e FastAPI.
- **Arquitetura:** REST
- **Banco de Dados e Migrations:** PostgreSQL, SQLAlchemy e Alembic.
- **Segurança:** Autenticação JWT e criptografia de senhas.
- **Containerização:** Docker e Docker Compose.

------

## Projetos

### Template API

Template de API REST baseado no template oficial do FastAPI, configurado para acelerar o desenvolvimento de novos projetos.

[![Repository](https://img.shields.io/badge/repository-template--api-blue?style=flat-square)](https://github.com/lincolntaranto/template-api) [![CI / Tests](https://img.shields.io/github/actions/workflow/status/lincolntaranto/template-api/ci.yml?label=CI%20/%20Tests&style=flat-square&logo=github-actions)](https://github.com/lincolntaranto/template-api) [![Linter: Ruff](https://img.shields.io/badge/linter-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff) [![Dependabot](https://img.shields.io/badge/dependabot-active-brightgreen?style=flat-square&logo=dependabot)](https://github.com/lincolntaranto/template-api/blob/main/.github/dependabot.yml) [![Deploy](https://img.shields.io/badge/deploy-render-purple)](https://claude.ai/new?incognito=) [![Status](https://img.shields.io/badge/status-online-success)](https://template-api-89m8.onrender.com/docs) [![Email: Resend](https://img.shields.io/badge/email-Resend-000000?style=flat-square&logo=resend)](https://resend.com/)

#### Especificações Técnicas

| Componente          | Ferramenta Utilizada          | Finalidade                                                   |
| ------------------- | ----------------------------- | ------------------------------------------------------------ |
| **Framework**       | FastAPI                       | Criação das rotas e documentação automática                  |
| **ORM**             | SQLAlchemy 2.0                | Mapeamento e consultas ao banco de dados                     |
| **Database**        | PostgreSQL                    | Armazenamento relacional dos dados                           |
| **Migrations**      | Alembic                       | Controle de versão do banco de dados                         |
| **Configurações**   | Pydantic Settings             | Gerenciamento de variáveis via arquivo `.env`                |
| **Segurança**       | pwdlib (Argon2) & PyJWT       | Criptografia de senhas e geração de tokens JWT               |
| **Comunicação**     | Resend + Jinja2               | Estruturação e envio automatizado de emails                  |
| **Qualidade**       | Pytest, testcontainers & Ruff | Testes de integração com banco isolado e linter de código    |
| **Containerização** | Docker & Docker Compose       | Isolamento do ambiente e orquestração dos serviços (App + Banco) |

#### Funcionalidades Prontas

- Autenticação e Login JWT.
- CRUD completo de Usuários com hash seguro.
- Sistema integrado para disparo de emails.
- Suíte completa de testes automatizados e esteira de CI.

> **Acesse o código completo:** [Repositório Template API](https://github.com/lincolntaranto/template-api)

------

### API Sistema Escola

API REST para gestão escolar, cobrindo alunos, turmas, notas e controle de acesso com sistema de convites.

[![Repository](https://img.shields.io/badge/repository-API--Sistema--Escola-blue?style=flat-square)](https://github.com/lincolntaranto/API-Sistema-Escola) ![CI / Tests](https://img.shields.io/github/actions/workflow/status/lincolntaranto/API-Sistema-Escola/ci.yml?label=CI%20/%20Tests&style=flat-square&logo=github-actions) [![Linter: Ruff](https://img.shields.io/badge/linter-ruff-black?style=flat-square&logo=ruff)](https://github.com/astral-sh/ruff) [![Docker](https://img.shields.io/badge/docker-ready-2496ED?style=flat-square&logo=docker)](https://www.docker.com/)

#### Especificações Técnicas

| Componente          | Ferramenta Utilizada          | Finalidade                                                   |
| ------------------- | ----------------------------- | ------------------------------------------------------------ |
| **Framework**       | FastAPI                       | Criação das rotas e documentação automática                  |
| **Arquitetura**     | Camadas (Router → Service → Model) | Separação entre transporte HTTP, regras de negócio e persistência |
| **ORM**             | SQLAlchemy 2.0                | Mapeamento e consultas ao banco de dados                     |
| **Database**        | PostgreSQL                    | Armazenamento relacional dos dados                           |
| **Migrations**      | Alembic                       | Controle de versão do banco de dados                         |
| **Configurações**   | Pydantic Settings             | Gerenciamento de variáveis via arquivo `.env`                |
| **Segurança**       | Argon2 & PyJWT                | Criptografia de senhas e geração de tokens JWT               |
| **Containerização** | Docker & Docker Compose       | Isolamento do ambiente e orquestração dos serviços (App + Banco) |
| **Qualidade**       | Pytest, testcontainers & Ruff | Testes de integração com banco isolado e linter de código    |

#### Funcionalidades Prontas

- Arquitetura em camadas (routers, services e exceções de domínio) com tratamento de erros centralizado.
- Versionamento de API com prefixo `/api/v1`.
- Rotas RESTful (recurso no path, verbos HTTP semânticos).
- Autenticação e Login JWT, com suporte a refresh token.
- CRUD completo de alunos, com exclusão via **soft delete** para preservar histórico.
- Listagem de alunos com filtros e paginação.
- CRUD completo de turmas.
- CRUD completo de cargos.
- CRUD completo de notas.
- Sistema de convite para controle de cadastro de novos usuários.
- Log de auditoria das ações realizadas no sistema.
- Ambiente containerizado com Docker Compose.
- Suíte de testes de integração com Postgres isolado via testcontainers.

> **Acesse o código completo:** [API-Sistema-Escola](https://github.com/lincolntaranto/API-Sistema-Escola)

------

## Contato

- **LinkedIn:** [linkedin.com/in/lincolntaranto](https://linkedin.com/in/lincolntaranto)
