import sqlite3

# Conect to a DataBase
def conectar(database):
    conexao = sqlite3.connect('database.db')
    return conexao

def criar_tabela_spents(conexao):
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Spents(
                id INTEGRER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                price TEXT NOT NULL,
                date TEXT NOT NULL
                )''')
    conexao.commit()

def insert_new_spent(conexao, spent):
    last_spent_id = get_last_spent(conexao)[0]
    new_spent_id = last_spent_id + 1
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO Spents VALUES (?, ?, ?, ?, ?)', (new_spent_id, spent.title, spent.description, str(spent.price), spent.date))
    conexao.commit()
    print('Spent registred sucessfully')

def get_all_spents(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Spents')
    spents_registred = cursor.fetchall()
    return spents_registred


def get_last_spent(conexao):
    all_spents = get_all_spents(conexao)
    last_spent = all_spents[len(all_spents)-1]
    return last_spent