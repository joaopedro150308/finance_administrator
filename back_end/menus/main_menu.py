from back_end.modelos.menus import Menu

menu_title = 'Main Menu'
menu_description = '''This is the main menu.
Please, chose a option.'''
menu_options = (0,1,2,3)
menu_options_text = ('Add Spents', 'See Spents', 'Remove Spents', 'Close')

def add_spent():
    pass

def show_all_spents():
    pass

def remove_spents():
    pass

def close():
    pass

menu_functions = (add_spent, show_all_spents, remove_spents, close)


menu_pricipal = Menu(menu_title, menu_description, menu_options, menu_options_text, menu_functions)