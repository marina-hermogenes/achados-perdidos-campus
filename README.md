# Achados e Perdidos - Campus UFLA

Sistema web para registro e gerenciamento de itens achados e perdidos no campus da Universidade Federal de Lavras (UFLA).

Projeto desenvolvido para a disciplina **Programação Web (GAC116)** - UFLA, 2026/1.

---

## Sobre o Projeto

O Achados e Perdidos Campus é uma aplicação web desenvolvida com Django que permite que estudantes, professores e funcionários registrem itens perdidos ou encontrados no campus, facilitando a devolução dos pertences aos seus donos.

Cada registro conta com título, descrição, categoria, localização, tipo (perdido ou encontrado), status (aberto ou resolvido) e foto opcional. O sistema possui um painel administrativo protegido por login para gerenciamento dos dados.

---

## Tecnologias Utilizadas

- Python 3.10+
- Django 5.x
- Bootstrap 5
- django-jazzmin
- SQLite

---

## Estrutura do Projeto

```
achados-perdidos-campus/
├── core/               # App principal (models, admin, templates)
├── docs/               # Documentação do projeto (diagrama ER)
├── setup/              # Configurações do Django (settings, urls, wsgi)
├── manage.py           # Utilitário de linha de comando do Django
├── requirements.txt    # Dependências do projeto
└── .gitignore
```

---

## Modelo de Dados

O banco de dados é composto por três tabelas principais, além da tabela de usuários fornecida pelo Django:

- **User** (Django) - representa o usuário que publica um registro
- **Categoria** - classifica o tipo do item (ex: Eletrônico, Documento, Roupa)
- **Localizacao** - indica onde o item foi perdido ou encontrado (ex: Biblioteca, Bloco A, Cantina)
- **Item** - tabela central do sistema, com relacionamentos para Categoria, Localizacao e User

O diagrama entidade-relacionamento está disponível em `docs/`.

---

## Como Rodar o Projeto

### Pré-requisitos

- Python 3.10+
- pip
- Git

### Instalação

1. Clone o repositório:

```bash
git clone https://github.com/marina-hermogenes/achados-perdidos-campus.git
cd achados-perdidos-campus
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Aplique as migrações:

```bash
python manage.py migrate
```

4. Crie um superusuário para acessar o painel administrativo:

```bash
python manage.py createsuperuser
```

5. Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

6. Acesse em: http://127.0.0.1:8000/admin

---

## Contribuidoras

- Ana Clara Carvalho Nascimento
- Isadora Gomes Melo Cunha
- Marina Hermógenes Siqueira