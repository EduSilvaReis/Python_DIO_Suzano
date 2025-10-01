# 💳 Sistema Bancário POO

Este projeto é um sistema bancário simples desenvolvido em Python utilizando Programação Orientada a Objetos (POO). Ele permite o gerenciamento de clientes, contas correntes e transações bancárias como depósitos e saques.

## ⚙️ Funcionalidades

- 👤 Cadastro de clientes (Pessoa Física)
- 🏦 Criação de contas correntes
- 💰 Depósito e saque
- 📄 Exibição de extrato
- 📋 Listagem de contas
- 🕒 Histórico de transações
- 🔒 Validação de limites de saque e quantidade de saques

## 🗂️ Estrutura do Código

- `Cliente` e `PessoaFisica`: Representam os clientes do banco.
- `Conta` e `ContaCorrente`: Gerenciam as contas bancárias e aplicam regras de negócio.
- `Transacao`, `Deposito`, `Saque`: Abstraem as operações bancárias.
- `Historico`: Armazena o histórico de transações de cada conta.
- Funções utilitárias para menu, cadastro, operações e listagem.

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Execute o arquivo principal:

   ```bash
   python bancoPOO.py
   ```

3. Siga as instruções do menu interativo para realizar operações bancárias.

## ℹ️ Observações

- O sistema é totalmente em modo texto (console).
- Não utiliza banco de dados; os dados são mantidos em memória enquanto o programa está em execução.
- O código utiliza boas práticas de POO e abstração com classes abstratas.

## 👨‍💻 Autor

Desenvolvido para fins de estudo e prática de Programação Orientada a Objetos em Python.
