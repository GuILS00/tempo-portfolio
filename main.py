# main.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from captura import capturar_temperatura_umidade
from planilha import salvar_em_planilha

def executar_captura():
    temperatura, umidade = capturar_temperatura_umidade()
    if temperatura and umidade:
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        salvar_em_planilha(agora, temperatura, umidade)
        messagebox.showinfo("Sucesso", f"Temperatura: {temperatura}\nUmidade: {umidade}")
    else:
        messagebox.showerror("Erro", "Falha ao obter dados.")

janela = tk.Tk()
janela.title("Captador de Temperatura")
janela.geometry("300x150")

btn_capturar = tk.Button(janela, text="Capturar Agora", command=executar_captura, width=20, height=2)
btn_capturar.pack(pady=40)

janela.mainloop()
