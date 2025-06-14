# planilha.py
import openpyxl
import os

def salvar_em_planilha(data_hora, temperatura, umidade):
    nome_arquivo = "dados_temperatura.xlsx"

    if os.path.exists(nome_arquivo):
        wb = openpyxl.load_workbook(nome_arquivo)
        sheet = wb.active
    else:
        wb = openpyxl.Workbook()
        sheet = wb.active
        sheet.append(["Data e Hora", "Temperatura", "Umidade"])

    sheet.append([data_hora, temperatura, umidade])
    wb.save(nome_arquivo)
