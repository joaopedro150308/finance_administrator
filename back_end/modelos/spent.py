import time

class Spent:

    def __init__(self, title, description, price, date):
        self.title = title
        self.description = description
        self.price = price
        self.date = date

    def __str__(self):
        return f'{self.title}: R$ {self.price}'
    
    def print_spent_info(self):
        print(f'{self.title}|{self.description}|{self.price}|{self.date}')
    
def create_spent():
    title = str(input('Type the spent title: ')).strip()
    description = str(input('Type the spent description: ')).strip()
    price = float(input('Type the spent price: '))
    date = time.strftime('%d/%m/%Y', time.localtime())

    spent = Spent(title, description, price, date)
    print('Spent created!')
    return spent
