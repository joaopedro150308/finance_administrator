from back_end.modelos.debt import create_debt
from back_end.modelos.spent import create_spent

# debt_list = []
# for c in range(0, 2):
#     debt = create_debt()
#     debt_list.append(debt)

# for debt in debt_list:
#     debt.print_debts_info()

spents = []
for c in range(0, 2):
    spent = create_spent()
    spents.append(spent)

for spent in spents:
    print(spent)
    print(spent.date)
    spent.print_spent_info()