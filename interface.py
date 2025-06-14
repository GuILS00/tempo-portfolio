import tkinter as tk
from tkinter import messagebox
from captura import capturar_dados
from planilha import salvar_dados

def ao_clicar():
    data, temp, umid = capturar_dados()
    if not temp:
        messagebox.showerror("Erro", "Falha ao obter dados.")
        return

    resultado_label.config(text=f"[{data}]\nTemperatura: {temp} °C\nUmidade: {umid or 'N/D'} %")
    salvar_dados(data, temp, umid or "N/D")
    messagebox.showinfo("Sucesso", "Dados capturados e salvos com sucesso!")

# Janela principal
janela = tk.Tk()
janela.title("Captador de Temperatura")
janela.geometry("350x200")

# Botão
botao = tk.Button(janela, text="Capturar Dados", command=ao_clicar, font=("Arial", 12))
botao.pack(pady=20)

# Label de resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 10))
resultado_label.pack()

# Executar
janela.mainloop()
