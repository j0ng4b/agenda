import flet as ft
from flet import ElevatedButton


from .components.inputField import InputField 
from .components.itemListCommit import ItemListCommit 
from .layouts.form_layout import FormLayout
from .layouts.auth_layout import Auth

bgColor = "#0CA6E9"


def home(page: ft.Page, **kwargs) -> ft.View:
    view = ft.View()
    
    view.bgcolor= bgColor
        
    body = FormLayout([
        InputField('E-mail'),
        InputField('Senha'),
        ElevatedButton(text="Entrar",width=250,height=50.7,bgcolor="#00FFA3", on_click=lambda _: page.route_forward("/compromissos"))
    ], 'Primeira vez?', 'Registre-se', page, 'cadastro')

    view.controls.append(body)

   
    
    # Return the view
    return view



##ft.app(name=agenda, target=home)

def cadastro(page: ft.Page) -> ft.View:
    view = ft.View()
    view.bgcolor= bgColor
    body = FormLayout([
        InputField('Nome'),
        InputField('E-mail'),
        InputField('Senha'),
        ElevatedButton(text="Criar conta",width=250,height=50.7,bgcolor="#00FFA3")
    ], 'Já tem conta?', 'Clique aqui', page, '')
    view.controls.append(body)
    return view

 
userDados = {
    'id': 0,
    'name': 'Rennê',
    'email': 'renne@dugrau.com'
}
def compromissos(page: ft.Page) -> ft.View:
    
    listItem = [
        {
            'id': 0,
            'item': 'Ir para a academia',
        },
        {
            'id': 1,
            'item': 'Tocar violão',
        },
        {
            'id': 2,
            'item': 'Ir ao mercado',
        },
        {
            'id': 3,
            'item': 'Aproveitar a universidade',
        },
        {
            'id': 4,
            'item': 'Estudar TC',
        },
        {
            'id': 5,
            'item': 'Estudar TEP',
        }
    ]
    
    def returnItemCommit(listItem):
        itemsComponent = []
        for item in listItem:
            if(item['id'] % 2 == 0):
                itemsComponent.append(ItemListCommit(item['item'], '#C8EAF9'))
            else:
                itemsComponent.append(ItemListCommit(item['item'], '#98CCE3'))
        return itemsComponent

    view = ft.View()
    
    body = Auth(view, userDados, bgColor, page, ft.Column(
            returnItemCommit(listItem),
            alignment = ft.MainAxisAlignment.CENTER
        ), "Lista de Compromissos")
    view.controls.append(body)
    return view



def calendario(page: ft.Page) -> ft.View:
    
    view = ft.View()
    body = Auth(view, userDados, bgColor, page, ft.Column([
            ft.Container(ft.Text("Em breve")),
        ],
        
        alignment = ft.MainAxisAlignment.CENTER
    ), "Seu Calendário")
    
    view.controls.append(body)
    return view

def contatos(page: ft.Page) -> ft.View:
    
    view = ft.View()

    return view