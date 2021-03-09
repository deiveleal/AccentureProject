import pyodbc
from datetime import date, datetime

class BD(object):

  def conecta_BD(self):
      try:
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
          f"Conectando ao BD no Azure...")
        conector = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                    'Server=sqlserver23810.database.windows.net;'
                    'Database=projeto_COVID19;'
                    'UID=sqluser;'
                    'PWD=Licesa@123;')
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
          f"Conexão realizada com sucesso com o BD!")
        return conector
      except Exception as error:
        print(f"{datetime.now().strftime('%H:%M:%S')}: "
          f"Não foi possível se conectar com o BD...")
        return 0

  def armazena_paises(self, conectorBD, conectorAPI):
    for item in conectorAPI:
      try:
        conectorBD.execute("INSERT INTO PAIS VALUES (?, ?)") 
        #Necessário preencher com os campos da API selecionada
      except Exception as error:
        self.armazena_erros(conectorBD, item, error)
    conectorBD.commit()
    print(f"{datetime.now().strftime('%H:%M:%S')}: "
          f"Inserção concluída com sucesso!\n")
    pass

  def armazena_casos_confirmados(self, conectorBD, conectorAPI):
    for item in conectorAPI:
      try:
        conectorBD.execute("INSERT INTO CASOS_CONFIRMADOS VALUES (?, ?, ?)")
        #Necessário preencher com os campos da API selecionada
      except Exception as error:
        self.armazena_erros(conectorBD, item, error)
    conectorBD.commit()
    print(f"{datetime.now().strftime('%H:%M:%S')}: "
          f"Inserção concluída com sucesso!\n")
    pass

  def armazena_mortes(self, conectorBD, conectorAPI):
    for item in conectorAPI:
      try:
        conectorBD.execute("INSERT INTO MORTES VALUES (?, ?, ?)")
        #Necessário preencher com os campos da API selecionada
      except Exception as error:
        self.armazena_erros(conectorBD, item, error)
    conectorBD.commit()
    print(f"{datetime.now().strftime('%H:%M:%S')}: "
          f"Inserção concluída com sucesso!")
    pass

  def armazena_erros(self, conectorBD, item, erro):
    conectorBD.execute("INSERT INTO LOG VALUES (GETDATE(), ?)",
                      f"Registro que originou o problema: {item}."
                      f"Informações Técnicas: {str(erro)}")
    conectorBD.commit()
    pass
