import os
#import all the libraries - SEE https://pypi.org/project/Office365-REST-Python-Client/
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File 
import io
import pandas as pd
import getpass



def readSharepointfile():
    #target url taken from sharepoint and credentials
    url = 'https://elkarlan-my.sharepoint.com/personal/inigo-quintana_euskadi_eus'
    #relative_url  = '/Documents/Attachments/test.xlsx'
    relative_url  = 'test.xlsx'
    username = 'inigo-quintana@euskadi.eus'
    password = getpass.getpass('Password:')

    ctx_auth = AuthenticationContext(url)
    if ctx_auth.acquire_token_for_user(username, password):
        ctx = ClientContext(url, ctx_auth)
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()
        print("Web title: {0}".format(web.properties['Title']))
        
        response = File.open_binary(ctx, relative_url)
        #save data to BytesIO stream
        bytes_file_obj = io.BytesIO()
        bytes_file_obj.write(response.content)
        bytes_file_obj.seek(0) #set file object to start

        #read file into pandas dataframe
        # if file_extension == 'xlsx':
        #     df = pd.read_excel(file.read(), engine='openpyxl')
        # elif file_extension == 'xls':
        #     df = pd.read_excel(file.read(), engine='xlrd')
        # elif file_extension == 'csv':
        #     df = pd.read_csv(file.read())
        #xlsx
        df = pd.read_excel(bytes_file_obj, engine='openpyxl')
        #xls
        #df = pd.read_excel(bytes_file_obj, engine='xlrd')
        
        print(df)
    
    else:
        print(ctx_auth.get_last_error())

def inputPing():
    ip = input("IP o nombre del ordenador a consultar: ")
    response = os.system("ping -n 1 " + ip)
    #and then check the response...
    if response == 0:
        print(f"{ip} is up!")
    else:
        print(f"{ip} is down!")
        print("**************************")
        print("**************************")
    
    return response,ip

def checkUser(ip):
    # r is for raw string
    # we compose the path for the Users directory with the active profiles
    users= r"\\" + ip + r"\c$\Users\."
    
    # we change actual dir to remote environment
    os.chdir(users)
    
    # we listir . remote environment
    # we list only dirs -> isdir
    # array indexed by getmtype
    # reverse -> most actual is first - [0] we get the 1st one only
    lastActiveUser = sorted(filter(os.path.isdir, os.listdir('.')), key=os.path.getmtime, reverse = True)[0]
    print("Ultimo usuario activo en PC: " + lastActiveUser)
    print("**************************")
    print("**************************")
    
if __name__ == "__main__":
  #  while True:
  #      response,ip = inputPing()
  #      if response == 0:
  #          checkUser(ip)
  readSharepointfile()