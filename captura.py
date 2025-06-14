# captura.py
import requests
from bs4 import BeautifulSoup

def capturar_temperatura_umidade():
    try:
        url = 'https://weather.com/weather/today/l/-23.55,-46.63?Goto=Redirected'  # São Paulo
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        temperatura_elemento = soup.find('span', {'data-testid': 'TemperatureValue'})
        umidade_elemento = soup.find('span', {'data-testid': 'PercentageValue'})

        temperatura = temperatura_elemento.text if temperatura_elemento else "N/A"
        umidade = umidade_elemento.text if umidade_elemento else "N/A"

        return temperatura, umidade

    except Exception as e:
        print(f"Erro ao capturar dados: {e}")
        return None, None
