# Sistema de Gerenciamento de Tarefas

## Descrição

Projeto desenvolvido para a disciplina de Engenharia de Software com o objetivo de aplicar conceitos de desenvolvimento ágil, modelagem, controle de qualidade, integração contínua e gerenciamento de mudanças.

## Objetivo

Desenvolver um sistema de gerenciamento de tarefas capaz de auxiliar equipes na organização de atividades, permitindo acompanhamento e priorização de tarefas.

## Escopo Inicial

O projeto foi planejado para oferecer as seguintes funcionalidades:

- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Remover tarefas

## Mudança de Escopo

Durante o desenvolvimento foi identificada a necessidade de priorizar tarefas de acordo com sua importância.

Foi adicionada a funcionalidade:

- Definição de prioridade (Alta, Média e Baixa)

A alteração foi registrada no Kanban e implementada durante o desenvolvimento do sistema.

## Metodologia Utilizada

Foi utilizada a metodologia Kanban através do GitHub Projects para acompanhamento das tarefas do projeto.

As atividades foram organizadas nas colunas:

- To Do
- In Progress
- Done

## Tecnologias Utilizadas

- Python
- Git
- GitHub
- Pytest
- GitHub Actions

## Estrutura do Projeto

```
task-manager-agile-project/

├── src/
│   ├── app.py
│   └── task_manager.py
│
├── tests/
│   └── test_task_manager.py
│
├── docs/
│   ├── Diagrama de Classes.png
│   └── Diagrama simplificado.png
│
├── .github/
│   └── workflows/
│       └── tests.yml
│
└── README.md
```

## Como Executar

Instalar dependências:

```bash
pip install -r requirements.txt
```

Executar aplicação:

```bash
python src/app.py
```

## Testes Automatizados

Executar:

```bash
pytest
```

Resultado obtido:

- 8 testes executados
- 8 testes aprovados

## Integração Contínua

Foi configurado um pipeline utilizando GitHub Actions para executar automaticamente os testes a cada alteração enviada para o repositório.

## Diagramas UML

O projeto contém:

- Diagrama de Casos de Uso
- Diagrama de Classes

## Autor

Projeto desenvolvido para fins acadêmicos na disciplina de Engenharia de Software.