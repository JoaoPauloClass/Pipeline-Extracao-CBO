import ftplib
import pyreaddbc
from simpledbf import Dbf5

def converter_dbc_para_csv(ano_mes, uf="PR"):
	arquivo_dbc = f"PF{uf}{ano_mes}.dbc"
	arquivo_dbf = f"PF{uf}{ano_mes}.dbf"
	arquivo_csv = f"cnes_{uf}_{ano_mes}.csv"

	ftp_host = "ftp.datasus.gov.br"
	diretorio = "/dissemin/publicos/CNES/200508_/Dados/PF/"

	try:
		ftp = ftplib.FTP(ftp_host)
		ftp.login()
		ftp.cwd(diretorio)
		with open(arquivo_dbc, "wb") as f:
			ftp.retrbinary(f"RETR {arquivo_dbc}", f.write)
		ftp.quit()

		pyreaddbc.readdbc.dbc2dbf(arquivo_dbc, arquivo_dbf)

		dbf = Dbf5(arquivo_dbf, codec='iso-8859-1')
		df = dbf.to_dataframe()

		df.to_csv(arquivo_csv, index=False, sep=";")

		print("Finalizado")

	except Exception as e:
		print("Um erro ocorreu: " + e)

converter_dbc_para_csv("2601", "PR")
