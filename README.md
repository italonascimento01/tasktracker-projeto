# TaskTracker

Sistema de gerenciamento de tarefas em linha de comando, desenvolvido como projeto cumulativo da disciplina **Bootcamp II** (CEUB).

## Sobre o projeto

O TaskTracker resolve um problema simples e comum: quem organiza as tarefas do dia sem nenhum sistema acaba espalhando essas informações entre papel, mensagens para si mesmo e memória. Nenhum desses lugares guarda o conjunto completo.

A aplicação centraliza o cadastro e a consulta das tarefas em um único lugar, com validação dos dados na entrada.

## Funcionalidades

* **Cadastrar tarefa** — registra título, descrição, prioridade e data limite
* **Visualizar tarefas** — lista todas as tarefas cadastradas com seus dados e status
* **Sair** — encerra a aplicação

## Regras de negócio implementadas

|Regra|Comportamento|
|-|-|
|Título obrigatório|Entradas vazias ou compostas apenas por espaços são rejeitadas; o sistema pede nova digitação|
|Prioridade restrita|Aceita exclusivamente `Alta`, `Média` (ou `Media`) e `Baixa`; outros valores geram erro e repetem o prompt|
|Status automático|Toda tarefa nasce com status `Pendente`, sem intervenção do usuário|
|Lista vazia|Exibe mensagem informativa em vez de uma tela em branco|

## Tecnologias

* Python 3 (biblioteca padrão, sem dependências externas)
* Git e GitHub para versionamento

## Instalação e execução

```bash
# Clonar o repositório
git clone https://github.com/italonascimento01/tasktracker-projeto.git
cd tasktracker-projeto

# Executar a aplicação
python3 src/main.py
```

Não há dependências a instalar: o projeto usa apenas a biblioteca padrão do Python.

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                     # Este arquivo
├── .gitignore                    # Arquivos ignorados pelo Git
├── docs/
│   └── planejamento\\\\\\\_logico.pdf   # Planejamento lógico da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## Fases do projeto

* **Fase 1** — Planejamento lógico, decomposição do problema e algoritmo em português *(concluída)*
* **Fase 2** — Estruturação do repositório, versionamento e implementação em Python *(atual)*
* **Fase 3** — Containerização com Docker, testes e deploy

As funções de concluir e remover tarefa, previstas no planejamento da Fase 1, ficaram fora do escopo desta entrega, cujo requisito é o menu de três opções. Elas entram na Fase 3.

## Autor

Italo Nascimento de Sousa — Ciência de Dados e Machine Learning, CEUB

