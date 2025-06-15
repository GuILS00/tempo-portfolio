# 🌡️ Captador de Temperatura de São Paulo

Este projeto é uma aplicação Python com interface gráfica que **captura automaticamente a temperatura e a umidade do ar na cidade de São Paulo** por meio da web e **registra os dados em uma planilha Excel** com a **data e hora exata da coleta**. A automação é feita com `Selenium`, `openpyxl` e `tkinter`.

---

## ✅ Objetivos

- Automatizar a coleta de temperatura e umidade do ar.
- Armazenar os dados em uma planilha Excel com data e hora.
- Fornecer uma interface gráfica simples para o usuário iniciar a captura.
- Proporcionar uma experiência prática em automação com Python.

---

## 🧰 Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Selenium](https://pypi.org/project/selenium/)
- [OpenPyXL](https://pypi.org/project/openpyxl/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- Navegador compatível (ex: Chrome ou Edge)

---

## 📂 Estrutura do Projeto

captador_temperatura/
├── main.py # Inicia a interface e integra os módulos
├── captura.py # Função que acessa o site e captura dados
├── planilha.py # Função que grava os dados em planilha Excel
├── interface.py # Interface gráfica com botão "Capturar Agora"
├── dados_temperatura.xlsx # Planilha gerada com os registros
├── assets/ # (opcional) Ícones, imagens, etc.


---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/captador-temperatura.git
cd captador-temperatura

Instale as bibliotecas necessárias:
pip install selenium openpyxl

Execute o programa:
python main.py

Clique no botão Capturar Agora para buscar e gravar os dados

Exemplo de Saída (Excel)

Data e Hora	Temperatura	Umidade
2025-06-09 20:12:42	60°	84%

Aprendizados do Projeto
Automatização de tarefas com Selenium

Manipulação de arquivos .xlsx com openpyxl

Criação de interfaces com tkinter

Integração de múltiplos módulos Python em um projeto funcional

Uso de Git e versionamento com GitHub

GuILS00
Projeto para a disciplina de automação com Python.
Instituição: UNIFECAF

link vídeo: https://youtube.com/shorts/iFZwRFpcU8A?si=HgGV6IESntklL4xG