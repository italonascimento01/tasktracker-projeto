"""
TaskTracker - Sistema de Gerenciamento de Tarefas
Bootcamp II - Fase 2 (Entrega Intermediaria)

Aplicacao de linha de comando (CLI) que implementa a receita logica
definida no planejamento da Fase 1.
"""

# Lista que guarda todas as tarefas durante a execucao do programa.
# Cada tarefa e um dicionario com titulo, descricao, prioridade,
# data limite e status.
tarefas = []


def exibir_menu():
    """Mostra o menu principal na tela."""
    print("\n" + "=" * 40)
    print("        TASKTRACKER - MENU PRINCIPAL")
    print("=" * 40)
    print("1 - Cadastrar nova tarefa")
    print("2 - Visualizar tarefas cadastradas")
    print("3 - Sair da aplicacao")
    print("=" * 40)



def cadastrar_tarefa():
    """
    Cadastra uma nova tarefa seguindo o passo a passo da Fase 1:
    pede o titulo, valida, pede a descricao, pede a prioridade,
    valida, pede a data limite, define o status e salva na lista.
    """
    print("\n--- CADASTRO DE NOVA TAREFA ---")

    titulo = input("Titulo da tarefa: ").strip()
    descricao = input("Descricao (opcional): ").strip()
    prioridade = input("Prioridade (Alta / Media / Baixa): ").strip()
    data_limite = input("Data limite (DD/MM/AAAA): ").strip()

    # O status sempre nasce como "Pendente", sem o usuario digitar.
    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente",
    }

    tarefas.append(tarefa)
    print(f"\nSUCESSO: a tarefa '{titulo}' foi cadastrada.")


def visualizar_tarefas():
    """
    Exibe todas as tarefas cadastradas.

    REGRA DE NEGOCIO: se a lista estiver vazia, avisa o usuario
    em vez de mostrar uma tela em branco.
    """
    print("\n--- TAREFAS CADASTRADAS ---")

    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada ate o momento.")
        return

    # Percorre a lista mostrando uma tarefa por vez, numerada.
    for numero, tarefa in enumerate(tarefas, start=1):
        descricao = tarefa["descricao"] if tarefa["descricao"] else "(sem descricao)"
        data_limite = tarefa["data_limite"] if tarefa["data_limite"] else "(sem data)"

        print(f"\nTarefa {numero}")
        print(f"  Titulo......: {tarefa['titulo']}")
        print(f"  Descricao...: {descricao}")
        print(f"  Prioridade..: {tarefa['prioridade']}")
        print(f"  Data limite.: {data_limite}")
        print(f"  Status......: {tarefa['status']}")

    print(f"\nTotal de tarefas: {len(tarefas)}")


def main():
    """
    Loop principal da aplicacao. Mostra o menu, le a opcao do usuario
    e chama a funcao correspondente, repetindo ate que o usuario
    escolha a opcao 3 (sair).
    """
    print("Bem-vindo ao TaskTracker!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("\nEncerrando o TaskTracker. Ate logo!")
            break
        else:
            print("ERRO: opcao invalida. Digite 1, 2 ou 3.")


# Garante que o programa so rode quando o arquivo for executado
# diretamente, e nao quando for importado por outro modulo.
if __name__ == "__main__":
    main()
