class Debt:

    def __init__(self, title=str, description=str, price=float):
        self.title = title
        self.description = description
        self.price = price

    def __str__(self):
        return self.title
    
    def print_debts_info(self):
        print(f'Debt Title: {self.title} | Debt Description: {self.description} | Debt Price: {self.price}')


def create_debt():
    debt_title = input('Type the debt title: ').strip()
    debt_description = input('Tupe the debt discriptions: ').strip()
    debt_price = float(input('Type the debt price: '))
    debt = Debt(debt_title, debt_description, debt_price)

    return debt