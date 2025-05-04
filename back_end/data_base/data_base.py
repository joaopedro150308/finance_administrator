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

def insert_new_spent(conexao, spent, spent_id):
    
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO Spents VALUES (?, ?, ?, ?, ?)', (spent_id, spent.title, spent.description, str(spent.price), spent.date))
    conexao.commit()
    print('Spent registred sucessfully')

def get_all_spents(conexao):
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM Spents')
    spents_registred = cursor.fetchall()
    return spents_registred