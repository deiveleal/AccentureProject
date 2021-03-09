from datetime import date, datetime
from API import API as conn_API
from BD import BD as conn_BD
from BKP import BKP as conn_BKP

class Gerenciador(object):

    print(f"{datetime.now().strftime('%H:%M:%S')}: "
            f"Iniciando a aplicação...")   

    conectorAPI = conn_API().conecta_API()
    
    while True:
        confeccionar_BKP = input('Deseja criar um BKP em formato .csv dos dados (S/N)? ').strip().title()
        if confeccionar_BKP == 'S' or confeccionar_BKP == 'Sim':
            BKP = conn_BKP().criar_BKP(conectorAPI)
            print(f"{datetime.now().strftime('%H:%M:%S')}: "
                f"BKP criado com sucesso!")
            break
        elif confeccionar_BKP == 'N' or confeccionar_BKP == 'Não':
            break
        else:
            print('Opção inválida! Por gentileza, digite novamente...')

    conectorBD = conn_BD().conecta_BD()

    if conectorAPI != 0 and conectorBD != 0:

        print(f"{datetime.now().strftime('%H:%M:%S')}: "
                f"Inserção de dados no BD iniciada...\n")

        print('1º carga: Países')
        # conn_BD().armazena_paises(conectorBD, conectorAPI)
        print('2º carga: Casos confirmados')
        # conn_BD().armazena_casos_confirmados(conectorBD, conectorAPI)
        print('3º carga: Mortes')
        # conn_BD().armazena_mortes(conectorBD, conectorAPI)

    pass

if __name__ == "__main__":

    Gerenciador()