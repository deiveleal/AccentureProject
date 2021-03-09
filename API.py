import requests
from datetime import date, datetime

class API(object):

    def conecta_API(self):
        try:
            print(f"{datetime.now().strftime('%H:%M:%S')}: "
                f"Conectando a API....")
            response = requests.get('https://api.covid19api.com/countries')
            print(f"{datetime.now().strftime('%H:%M:%S')}: "
                f"Conexão realizada com sucesso!")
            if response.status_code == 200:
                return response.json()
            elif response.status_code == 404:
                print("Result not found!")

        except requests.exceptions.HTTPError as errh:
            print(errh)
        except requests.exceptions.ConnectionError as errc:
            print(errc)
        except requests.exceptions.Timeout as errt:
            print(errt)
        except requests.exceptions.RequestException as err:
            print(err)
        return 0   
        pass