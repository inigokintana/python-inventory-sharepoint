import os
import subprocess
from pandasql import sqldf
import pandas as pd

def getXlsxInventoryFilePC():
    
    inventoryFile = input("Path completo del fichero Excel de inventario y con formato xlsx: ")
    hoja = input("Nombre de la pestaña/hoja: ")
    #df is the variable where all the Excel data is loaded
    df = pd.read_excel(open(inventoryFile, 'rb'), sheet_name=hoja, engine='openpyxl')  
    #shows first 3 lines
    print(df.head(3))
   
    # Query the Excel data in df
    #print(sqldf('''SELECT "Etiqueta de activo"
    #    FROM df 
    #    WHERE Category="PC" '''))
    return sqldf('''SELECT "Asset tag" FROM df WHERE Category="PC" ''')
      
def pcPing(pcName):
    #ip = input("IP o nombre del ordenador a consultar: ")
    response = os.system("ping -n 1 " + pcName)
    #and then check the response...
    if response == 0:
        print(f"{pcName} is up!")
    else:
        print(f"{pcName} is down!")
        print("**************************")
        print("**************************")

    return response,pcName

def pcPing2(pcName):
    ARGS = ["ping", "-n", "1", pcName]
    output = subprocess.Popen(ARGS, stdout=subprocess.PIPE).communicate()[0]
    print(output)

    if (b'TTL=' in output):
        print(pcName + "Up & Running")
        response = 0
    else:
        print(pcName + " is KO")
        print("**************************")
        response = 1
    return response,pcName
    
def checkUser(pcName):
    # r is for raw string
    # we compose the path for the Users directory with the active profiles
    users= r"\\" + pcName + r"\c$\Users\."
    
    # we change actual dir to remote environment
    os.chdir(users)
    
    # we listir . remote environment
    # we list only dirs -> isdir
    # array indexed by getmtype
    # reverse -> most actual is first - [0] we get the 1st one only
    print("Ultimo usuario activo en PC: " + pcName + " - " + sorted(filter(os.path.isdir, os.listdir('.')), key=os.path.getmtime, reverse = True)[0])
    print("**************************")

if __name__ == "__main__":
    #Get PC names in the Excel file
    pcNames=getXlsxInventoryFilePC()
    # For each PC see if 1) it is connected (ping)  2) Get user  3) Update master DF 
    for index, row in pcNames.iterrows():
        #print(row['c1'], row['c2'])
        #response,pcName = pcPing(row['Etiqueta de activo'])
        response,pcName = pcPing2(row['Asset tag'])
        if response == 0:
            checkUser(pcName)
            #buscar equipo y actualizar DF maestro

    #Write Updated master dataframe into Excel