import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from src.task_manager import TaskManager


def test_adicionar_tarefa():
    manager = TaskManager()

    tarefa = manager.adicionar_tarefa(
        "Estudar GitHub",
        "Alta"
    )

    assert tarefa["titulo"] == "Estudar GitHub"
    assert tarefa["prioridade"] == "Alta"
    assert tarefa["id"] == 1


def test_listar_tarefas():
    manager = TaskManager()

    manager.adicionar_tarefa("Tarefa 1")
    manager.adicionar_tarefa("Tarefa 2")

    tarefas = manager.listar_tarefas()

    assert len(tarefas) == 2


def test_buscar_tarefa_existente():
    manager = TaskManager()

    manager.adicionar_tarefa("Estudar Python")

    tarefa = manager.buscar_tarefa(1)

    assert tarefa is not None
    assert tarefa["titulo"] == "Estudar Python"


def test_buscar_tarefa_inexistente():
    manager = TaskManager()

    tarefa = manager.buscar_tarefa(99)

    assert tarefa is None


def test_atualizar_tarefa():
    manager = TaskManager()

    manager.adicionar_tarefa(
        "Estudar Python",
        "Média"
    )

    resultado = manager.atualizar_tarefa(
        1,
        "Estudar GitHub Actions",
        "Alta"
    )

    tarefa = manager.buscar_tarefa(1)

    assert resultado is True
    assert tarefa["titulo"] == "Estudar GitHub Actions"
    assert tarefa["prioridade"] == "Alta"


def test_atualizar_tarefa_inexistente():
    manager = TaskManager()

    resultado = manager.atualizar_tarefa(
        99,
        "Nova tarefa",
        "Alta"
    )

    assert resultado is False


def test_remover_tarefa():
    manager = TaskManager()

    manager.adicionar_tarefa("Tarefa para remover")

    resultado = manager.remover_tarefa(1)

    assert resultado is True
    assert len(manager.listar_tarefas()) == 0


def test_remover_tarefa_inexistente():
    manager = TaskManager()

    resultado = manager.remover_tarefa(99)

    assert resultado is False