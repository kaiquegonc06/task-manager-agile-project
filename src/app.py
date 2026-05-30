from task_manager import TaskManager


def exibir_menu():
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Remover tarefa")
    print("5 - Sair")


def listar(manager):
    tarefas = manager.listar_tarefas()

    if not tarefas:
        print("\nNenhuma tarefa cadastrada.")
        return

    print("\n===== LISTA DE TAREFAS =====")

    for tarefa in tarefas:
        print(
            f"ID: {tarefa['id']} | "
            f"Título: {tarefa['titulo']} | "
            f"Prioridade: {tarefa['prioridade']}"
        )


def adicionar(manager):
    titulo = input("Digite o título da tarefa: ")

    prioridade = input(
        "Prioridade (Alta/Média/Baixa): "
    ).capitalize()

    if prioridade not in ["Alta", "Média", "Baixa"]:
        prioridade = "Média"

    tarefa = manager.adicionar_tarefa(titulo, prioridade)

    print(f"\nTarefa criada com sucesso! ID: {tarefa['id']}")


def atualizar(manager):
    try:
        tarefa_id = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        return

    novo_titulo = input(
        "Novo título (Enter para manter): "
    )

    nova_prioridade = input(
        "Nova prioridade (Alta/Média/Baixa): "
    ).capitalize()

    if nova_prioridade not in ["Alta", "Média", "Baixa", ""]:
        nova_prioridade = None

    sucesso = manager.atualizar_tarefa(
        tarefa_id,
        novo_titulo if novo_titulo else None,
        nova_prioridade if nova_prioridade else None
    )

    if sucesso:
        print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa não encontrada.")


def remover(manager):
    try:
        tarefa_id = int(input("Digite o ID da tarefa: "))
    except ValueError:
        print("ID inválido.")
        return

    sucesso = manager.remover_tarefa(tarefa_id)

    if sucesso:
        print("Tarefa removida com sucesso!")
    else:
        print("Tarefa não encontrada.")


def main():
    manager = TaskManager()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar(manager)

        elif opcao == "2":
            listar(manager)

        elif opcao == "3":
            atualizar(manager)

        elif opcao == "4":
            remover(manager)

        elif opcao == "5":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()