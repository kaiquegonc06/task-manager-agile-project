class TaskManager:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, titulo, prioridade="Média"):
        tarefa = {
            "id": self.proximo_id,
            "titulo": titulo,
            "prioridade": prioridade
        }

        self.tarefas.append(tarefa)
        self.proximo_id += 1

        return tarefa

    def listar_tarefas(self):
        return self.tarefas

    def buscar_tarefa(self, tarefa_id):
        for tarefa in self.tarefas:
            if tarefa["id"] == tarefa_id:
                return tarefa
        return None

    def atualizar_tarefa(self, tarefa_id, novo_titulo=None, nova_prioridade=None):
        tarefa = self.buscar_tarefa(tarefa_id)

        if tarefa is None:
            return False

        if novo_titulo:
            tarefa["titulo"] = novo_titulo

        if nova_prioridade:
            tarefa["prioridade"] = nova_prioridade

        return True

    def remover_tarefa(self, tarefa_id):
        tarefa = self.buscar_tarefa(tarefa_id)

        if tarefa is None:
            return False

        self.tarefas.remove(tarefa)
        return True