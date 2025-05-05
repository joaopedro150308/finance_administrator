from back_end.modelos.debt import create_debt
from back_end.modelos.spent import create_spent
from back_end.menus.main_menu import menu_pricipal
from back_end.data_base import data_base

conexao = data_base.conectar('database.bd')

menu_pricipal.init_menu_functions()
