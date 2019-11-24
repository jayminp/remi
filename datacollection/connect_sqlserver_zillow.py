'''
Server Name: zillowdata.cnyrvm7s6vwa.us-east-1.rds.amazonaws.com
Port: 1433
Username:  
Password: 

Database Name: Zillow
Main Table Name: dbo.zillow_data_input
Main Dataframe Name: zillow_data_input

'''


#import pypyodbc 
import pyodbc
import pandas as pd

cnxn = pyodbc.connect(driver='FreeTDS',tds_version='7.4', server='zillowdata.cnyrvm7s6vwa.us-east-1.rds.amazonaws.com', database='Zillow',user = "Admin", password = "", port = 1433 )
cursor = cnxn.cursor()

##Main table with union of data from all users
zillow_data_input = pd.read_sql('Select * from dbo.zillow_data_input',cnxn ) ## <-- table/dataframe we will use for Linear Regression


#Individual user tables
#zillow_data_shrikanth = pd.read_sql('Select * from dbo.zillow_data_shrikanth',cnxn )
#zillow_data_karthick = pd.read_sql('Select * from dbo.zillow_data_karthick',cnxn )
#zillow_data_kaushik = pd.read_sql('Select * from dbo.zillow_data_kaushik',cnxn )

#zillow_data_jaymin = pd.read_sql('Select * from dbo.zillow_data_jaymin',cnxn )
#zillow_data_santhosh = pd.read_sql('Select * from dbo.zillow_data_santhosh',cnxn )
#zillow_data_rodger = pd.read_sql('Select * from dbo.zillow_data_rodger',cnxn )


cnxn.close()
cursor.close()

