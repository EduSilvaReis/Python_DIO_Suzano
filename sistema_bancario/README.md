# Sistema Bancário Simples 🏦

Este projeto é um sistema bancário em linha de comando que simula as operações básicas de uma conta: depósito, saque e extrato. Foi desenvolvido como parte de um desafio de um curso de Python para praticar conceitos como funções, controle de fluxo e manipulação de variáveis.

---

### Funcionalidades ✔️

O sistema possui as seguintes operações:

* **Depósito**: Permite depositar valores positivos na conta. 💵
* **Saque**: Permite sacar valores com as seguintes regras:
    * Limite de **3 saques** por dia. 🔄
    * Valor máximo de **R$ 500,00** por saque. 💸
* **Extrato**: Exibe todas as movimentações (depósitos e saques) e o saldo atual da conta. 📜
* **Novo Usuário**: Permite cadastrar um novo usuário com nome, data de nascimento e endereço, garantindo que o CPF seja único. 👥
* **Nova Conta**: Permite criar uma nova conta bancária e vinculá-la a um usuário existente. 💳
* **Listar Contas**: Exibe todas as contas cadastradas no sistema. 📋
* **Acessar Conta**: Permite selecionar uma conta para realizar as operações de depósito, saque e extrato. 🔑

---

### Como Executar ▶️

Para rodar este programa, você precisa ter o Python 3 instalado.

1.  Certifique-se de estar no diretório do projeto.
2.  Execute o script no terminal:
    `python sistema_bancario.py`

---

### Tecnologias Utilizadas 🐍

* **Python 3**
* **Funções**
* **Controle de Fluxo** (`if`, `elif`, `else`, `while`)
* **Variáveis e Tipos de Dados**

---

### Próximos Passos 🚀

Este projeto pode ser expandido para incluir mais funcionalidades, como:

* Refatorar o sistema para que as operações de depósito, saque e extrato sejam realizadas por conta e não mais de forma global.
