'''
conexão database
'''

import pyodbc

connection_string = (
    "Driver= {ODBC Driver 11 for SQL Server};" #deve-se conferir para ver qual drive está instlado no pc
    "Server=192.168.69.152;"   #ip do pc
    "Database=DB_BackupOn_Manager;"
    "UID=SA;"
    "PWD=Extr@123;" #senha
)

try:
    conn = pyodbc.connect(connection_string)
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro na conexão: {str(e)}")