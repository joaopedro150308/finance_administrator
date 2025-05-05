import os

class Menu:

    def __init__(self, title=str, description=str, options=tuple, options_text=tuple, menu_functions=tuple):
        self.title = title
        self.description = description
        self.options = options
        self.options_text = options_text
        self.menu_functions = menu_functions


    def init_menu_visuals(self):
        # Title show
        print(f'{"="*10} {self.title.upper()} {"="*10}')
        # Description show
        print('-'*10)
        print(self.description)
        print('-'*10)


    def show_menu_options(self):
        print('Options:')
        print('-'*10)
        for i, option in enumerate(self.options):
            print(f'[{option}] {self.options_text[i]}')
        print('-'*10)


    def get_user_response(self):
        while True:
            try:
                user_response = int(input('Your option: '))
                if user_response in self.options:
                    break
                else:
                    print('Resposta inválida. Por favor tente novamente.')
            except ValueError:
                print('Resposta inválida. Por favor tente novamente.')
        return user_response


    def init_menu_functions(self):
        os.system('cls')
        self.init_menu_visuals()
        print('')
        self.show_menu_options()
        user_response = self.get_user_response()
        function_to_execute = self.menu_functions[user_response]
        function_to_execute()