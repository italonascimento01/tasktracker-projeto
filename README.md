# TaskTracker

Sistema de gerenciamento de tarefas em linha de comando, desenvolvido como projeto cumulativo da disciplina **Bootcamp II** (CEUB).

## Sobre o projeto

O TaskTracker resolve um problema simples e comum: quem organiza as tarefas do dia sem nenhum sistema acaba espalhando essas informações entre papel, mensagens para si mesmo e memória. Nenhum desses lugares guarda o conjunto completo.

A aplicação centraliza o cadastro e a consulta das tarefas em um único lugar, com validação dos dados na entrada. Nesta versão final, ela está containerizada com Docker: roda de forma idêntica em qualquer máquina, sem depender da versão de Python instalada no sistema.

## Funcionalidades

- **Cadastrar tarefa** — registra título, descrição, prioridade e data limite
- **Visualizar tarefas** — lista todas as tarefas cadastradas com seus dados e status
- **Sair** — encerra a aplicação

## Regras de negócio implementadas

| Regra | Comportamento |
|---|---|
| Título obrigatório | Entradas vazias ou compostas apenas por espaços são rejeitadas; o sistema pede nova digitação |
| Prioridade restrita | Aceita exclusivamente `Alta`, `Média` (ou `Media`) e `Baixa`; outros valores geram erro e repetem o prompt |
| Status automático | Toda tarefa nasce com status `Pendente`, sem intervenção do usuário |
| Lista vazia | Exibe mensagem informativa em vez de uma tela em branco |

## Tecnologias

- Python 3.11 (biblioteca padrão, sem dependências externas)
- Docker e Docker Compose para containerização e orquestração
- Git e GitHub para versionamento

---

## Como executar com Docker

Pré-requisito: Docker instalado e em execução ([Docker Desktop](https://www.docker.com/products/docker-desktop/) no Windows ou macOS).

### 1. Clonar o repositório

```bash
git clone https://github.com/italonascimento01/tasktracker-projeto.git
cd tasktracker-projeto
```

### 2. Construir a imagem

```bash
docker build -t tasktracker-app .
```

### 3. Rodar o container em modo isolado

```bash
docker run -it tasktracker-app
```

A flag `-it` é obrigatória: `-i` mantém a entrada de dados aberta e `-t` aloca um terminal. Sem ela, a aplicação encerraria sozinha logo após exibir o menu, porque o `input()` receberia fim de arquivo.

### 4. Rodar via orquestração (recomendado)

```bash
docker compose run --rm tasktracker
```

O `docker-compose.yml` já traz `stdin_open: true` e `tty: true`, que cumprem o mesmo papel do `-it` sem precisar passar flags na mão. A opção `--rm` remove o container assim que a aplicação é encerrada, evitando acúmulo de containers parados.

### Executar sem Docker

Se preferir rodar direto na máquina, com Python 3 instalado:

```bash
python3 src/main.py
```

---

## Estrutura do repositório

```
tasktracker-projeto/
├── README.md                     # Este arquivo
├── .gitignore                    # Arquivos ignorados pelo Git
├── Dockerfile                    # Receita de construção da imagem
├── docker-compose.yml            # Orquestração da execução interativa
├── docs/
│   └── planejamento_logico.pdf   # Planejamento lógico da Fase 1
└── src/
    └── main.py                   # Código-fonte da aplicação
```

## Decisões técnicas da containerização

**Imagem base `python:3.11-slim`** — a variante `slim` traz o Python sem bibliotecas de sistema que o projeto não usa, resultando numa imagem bem menor que a `python:3.11` completa. Como a aplicação usa apenas a biblioteca padrão, não há dependências a instalar.

**`ENV PYTHONUNBUFFERED=1`** — por padrão o Python agrupa a saída num buffer antes de exibir. Numa aplicação interativa isso quebra a experiência: o menu só apareceria depois de o usuário digitar algo. A variável desativa esse buffer.

**`COPY src/ /app/src/`** — copia apenas o código-fonte para dentro da imagem. A documentação e os arquivos de configuração ficam de fora, já que não são necessários em tempo de execução.

**`stdin_open` e `tty` no Compose** — um container é isolado por padrão e não recebe entrada do teclado. Essas duas chaves abrem o canal de entrada e alocam um terminal virtual, que é o que permite a uma aplicação CLI funcionar dentro do container.

## Fases do projeto

- **Fase 1** — Planejamento lógico, decomposição do problema e algoritmo em português *(concluída)*
- **Fase 2** — Estruturação do repositório, versionamento e implementação em Python *(concluída)*
- **Fase 3** — Containerização com Docker, orquestração e documentação *(concluída)*

As funções de concluir e remover tarefa, previstas no planejamento da Fase 1, ficaram fora do escopo das entregas, cujo requisito era o menu de três opções.

## Autor

Italo Nascimento de Sousa — Ciência de Dados e Machine Learning, CEUB
