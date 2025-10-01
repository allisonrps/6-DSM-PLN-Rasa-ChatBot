# 🍕 Chatbot da Pizzaria – Rasa

Um chatbot desenvolvido com **Rasa** para simular o atendimento de uma pizzaria.
O bot entende intenções, responde dúvidas frequentes, mostra o cardápio e conduz o fluxo de pedido até a finalização.

---

## 📋 Funcionalidades

* 👋 Saudações e despedidas.
* 📖 Exibição de cardápio com sabores, tamanhos, preços e opções de borda.
* ✅ Validação de **sabor**, **tamanho** e **borda** escolhidos pelo cliente.
* 🚚 Informações sobre **entrega** (tempo médio, taxa, promoções).
* 🛒 Fluxo completo de **fazer pedido** até a **confirmação** ou **cancelamento**.
* 🤖 Ações customizadas com **Rasa SDK**.

---

## 🛠️ Tecnologias utilizadas

* [Python 3.10+](https://www.python.org/)
* [Rasa Open Source](https://rasa.com/)
* [Rasa SDK](https://rasa.com/docs/rasa/custom-actions)

---

## ⚙️ Instalação e execução

### 1. Clone este repositório

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```


### 4. Treine o modelo Rasa

```bash
rasa train
```

### 5. Suba o servidor de ações

```bash
rasa run actions
```

### 6. Rode o chatbot no terminal

```bash
rasa shell
```

---

## 📂 Estrutura do projeto

```
.
├── actions/               # Ações customizadas (Python)
│   └── actions.py
├── data/                  # Dados de treino
│   ├── nlu.yml
│   ├── rules.yml
│   └── stories.yml
├── domain.yml             # Intenções, entidades, slots, respostas e ações
├── config.yml             # Configuração do pipeline e políticas
└── README.md              
```

---

## 🚀 Exemplo de uso

```text
Usuário: olá
Bot: Oi, seja bem-vindo à nossa pizzaria. Como posso te ajudar?

Usuário: quero ver o cardápio
Bot: 🍕 Nosso cardápio de pizzas:
- Calabresa → R$ 35,00
- Mussarela → R$ 32,00
- Frango → R$ 38,00
- Portuguesa → R$ 40,00
- Grande: +R$ 10,00 | Média: preço padrão | Pequena: -R$ 5,00
- Borda recheada: +R$ 5,00
```

## 👨‍💻 Autor

Projeto desenvolvido por **Allison Rodrigues**.
