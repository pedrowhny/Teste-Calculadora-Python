import tkinter as tk

class Calculadora:
    def __init__(self, root):
        
        # Inicializa a janela principal da calculadora
        
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("320x300")
        
        # Inicializa a equação como uma string vazia
       
        self.equation = ""
        
        # Cria o display da calculadora
        
        self.display = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="solid")
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20)
        
        # Define os botões da calculadora
        
        buttons = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        row_val = 1
        col_val = 0
        
        # Cria e posiciona os botões na interface
        
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(root, text=button, width=10, height=3, command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    
    def on_button_click(self, char):
    # Lida com o clique dos botões
        
        if char == "=":
            try:
                # Avalia a expressão matemática
                self.equation = str(eval(self.equation))
            except:
                # Em caso de erro, exibe "Erro"
                self.equation = "Erro"
        else:
            # Adiciona o caractere à equação
            self.equation += str(char)
        
        # Atualiza o display da calculadora
        
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.equation)

if __name__ == "__main__":
    # Cria a janela principal e inicia a calculadora
    
    root = tk.Tk()
    calc = Calculadora(root)
    root.mainloop()