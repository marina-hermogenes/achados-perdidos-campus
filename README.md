# 🎒 Achados e Perdidos — Campus UFLA

Sistema web para registro e gerenciamento de itens achados e perdidos no campus da Universidade Federal de Lavras (UFLA).

> Projeto desenvolvido para a disciplina **Programação WEB (GAC116)** — UFLA, 2026/1

---

## 📋 Sobre o Projeto

O **Achados e Perdidos Campus** é uma aplicação web desenvolvida com Django que permite que estudantes, professores e funcionários registrem itens perdidos ou encontrados no campus, facilitando a devolução dos pertences aos seus donos.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.12**
- **Django 5.x**
- **HTML5 / CSS3**
- **SQLite** (banco de dados padrão para desenvolvimento)

---

## 📁 Estrutura do Projeto

```
achados-perdidos-campus/
├── core/               # App principal (models, views, urls, templates)
├── docs/               # Documentação do projeto
├── setup/              # Configurações do Django (settings, urls, wsgi)
├── manage.py           # Utilitário de linha de comando do Django
├── requirements.txt    # Dependências do projeto
└── .gitignore
```

---

## ⚙️ Como Rodar o Projeto

### Pré-requisitos

- Python 3.12+
- pip

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/marina-hermogenes/achados-perdidos-campus.git
   cd achados-perdidos-campus
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/Mac
   venv\Scripts\activate         # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Aplique as migrações:**
   ```bash
   python manage.py migrate
   ```

5. **Inicie o servidor de desenvolvimento:**
   ```bash
   python manage.py runserver
   ```

6. Acesse em: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---
 
## 🔑 Primeiro Acesso
 
Para acessar o painel administrativo, crie um superusuário:
 
```bash
python manage.py createsuperuser
```
 
Preencha os dados solicitados (usuário, e-mail e senha) e acesse:
 
👉 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)
 
---

## 👥 Contribuidores

Desenvolvido pelas estudantes:
- Ana Clara Carvalho Nascimento
- Isadora Gomes Melo Cunha
- Marina Hermógenes Siqueira

---
