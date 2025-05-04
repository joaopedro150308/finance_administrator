from back_end.modelos.debt import create_debt
from back_end.modelos.spent import create_spent
from back_end.data_base import data_base


conexao = data_base.conectar('database.bd')

spents = []
for c in range(0, 2):
    spent = create_spent()
    spents.append(spent)

for i,spent in enumerate(spents):
    print(spent)
    print(spent.date)
    data_base.insert_new_spent(conexao, spent, i)
