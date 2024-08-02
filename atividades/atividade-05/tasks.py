import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

# Criar tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY,
    description TEXT,
    completed INTEGER
)
''')
conn.commit()

# Função para criar uma nova tarefa
def create_task(description):
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conn.commit()

# Função para listar todas as tarefas
def list_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Description: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")

# Função para marcar uma tarefa como concluída
def mark_completed(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()

# Função para deletar uma tarefa
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()

# Função para listar tarefas concluídas
def list_completed_tasks():
    cursor.execute("SELECT id, description FROM tasks WHERE completed = 1")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Description: {task[1]}")

# Função para listar tarefas não concluídas
def list_pending_tasks():
    cursor.execute("SELECT id, description FROM tasks WHERE completed = 0")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Description: {task[1]}")

# Exemplo de uso
if __name__ == "__main__":
    create_task("Estudar Python")
    create_task("Estudar Java")
    print("Tarefas antes de marcar como concluídas:")
    list_tasks()
    mark_completed(1)
    print("\nTarefas depois de marcar a tarefa 1 como concluída:")
    list_tasks()
    print("\nTarefas concluídas:")
    list_completed_tasks()
    print("\nTarefas pendentes:")
    list_pending_tasks()
    delete_task(2)
    print("\nTarefas depois de deletar a tarefa 2:")
    list_tasks()

# Fechar a conexão
conn.close()
