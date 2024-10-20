import tkinter as tk
from tkinter import ttk
from sistema import Sistema #Outro modulo do projeto
from config import connection_string #tupla para conexão com DB
from telas import TelaCadastroCliente, TelaRegistrarOcorrencia, TelaConsultarClientes, TelaGerarRelatorio, TelaMenu

class Aplicacao(tk.Tk):
    def __init__(self):
        super().__init__()

        #Configurações iniciais da tela principal
        self.title("Gerenciador Backup Online") 
        self.geometry("900x600")  #Defini um tamanho padrão da tela, tamanho semelhante à telinha do BKP, ideal é deixar responsivo futuramente
        self.configure(bg='#000000') # cor oadrão do sistema

        self.sistema = Sistema() #Instancia um obj da class sistema, criando uma associação
        self.tela_atual = None

        # Menu inicial
        self.menu_frame = tk.Frame(self, bg='#000000') #Frame é um container para organizar widgets
        self.menu_frame.pack(side=tk.TOP, anchor='nw', pady=10, padx=10)

        # Combobox para funcionalidades. São as escolhas disponíveis no menu da tela principal.
        self.combo_funcionalidades = ttk.Combobox(self.menu_frame, state="readonly", width=20) #Cria o campo de seleção.
        self.combo_funcionalidades['values'] = ["Menu", "Cadastrar Cliente", "Registrar Ocorrência", "Consultar Clientes", "Gerar Relatório"]
        self.combo_funcionalidades.current(0) #Define a primeira opção 'menu', como a padrão do Combobox/campo de seleção.
        self.combo_funcionalidades.bind("<<ComboboxSelected>>", self.abrir_tela)#<<ComboboxSelected>> evento que ocorre ao selecionar uma opção no Combobox
        self.combo_funcionalidades.pack()

        # Carrega o menu inicial
        self.abrir_tela(None)

    def abrir_tela(self, event):
        '''
            Abre a tela correspondente à funcionalidade selecionada no Combobox.

            Este método destrói a tela atual (se houver) e instancia a nova tela com base 
            na funcionalidade escolhida pelo usuário. Se a funcionalidade selecionada for 
            "Menu", ele carrega a tela do menu principal.

            Args:
            event: O evento que disparou a chamada do método (pode ser None).
        '''
        funcionalidade = self.combo_funcionalidades.get()
        
        if funcionalidade == "Menu" or funcionalidade == "":
            if self.tela_atual is not None:
                self.tela_atual.destroy()
            self.tela_atual = TelaMenu(self)
            self.tela_atual.pack(fill=tk.BOTH, expand=True)
            return

        if self.tela_atual is not None:
            self.tela_atual.destroy()

        if funcionalidade == "Cadastrar Cliente":
            self.tela_atual = TelaCadastroCliente(self)
        elif funcionalidade == "Registrar Ocorrência":
            self.tela_atual = TelaRegistrarOcorrencia(self)
        elif funcionalidade == "Consultar Clientes":
            self.tela_atual = TelaConsultarClientes(self)
        elif funcionalidade == "Gerar Relatório":
            self.tela_atual = TelaGerarRelatorio(self)

        self.tela_atual.pack(fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = Aplicacao()
    app.mainloop()

