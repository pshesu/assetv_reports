import os

basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'c\xf5D\x909AF\xb0\xd6\x83<\x7fr\x83\xa7\xe5\x98\x96\x07\x7f\x97\x9fs\xb1\x92VI\xecS\x18\xaf('

SQLALCHEMY_TRACK_MODIFICATIONS = False


#SQLALCHEMY_DATABASE_URI ='mssql+pymssql://jxthomas:sixers2016@192.168.168.111/?charset=utf8'

SQLALCHEMY_DATABASE_URI ='mssql+pyodbc://sa:coffee2016@reportsdb_odbc'
SQLALCHEMY_ECHO = True
#SQLALCHEMY_DATABASE_URI ='mssql+pymssql://jxthomas:sixers2016@192.168.168.111/?charset=utf8'
#SQLALCHEMY_DATABASE_URI ='mssql+pymssql://sa:coffee2016@192.168.168.111:1433/reportsdb'
