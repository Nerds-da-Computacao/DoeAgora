from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager

main_kv = '''
MDScreenManager:
    Navegar
    Entrar
    
'''

Builder.load_file('layout/navegar.kv')
Builder.load_file('layout/entrar.kv')

class App(MDApp):
    root: MDScreenManager

    def build(self):
        return Builder.load_string(main_kv)
    
    def acao_entrar(self):
        self.root.transition.direction = 'right'
        self.root.current = 'entrar'
    
    def acao_navegar(self):
        self.root.transition.direction = 'left'
        self.root.current = 'navegar'

if __name__ == '__main__':
    App().run()
    
