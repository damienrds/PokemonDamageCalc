# -------------------------------------------------------------------------------------------------
# -- Imports
# -------------------------------------------------------------------------------------------------
import requests
import json
import sys
# -------------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------------
def display( inContent ):
    print(inContent, end="\r")
    sys.stdout.write("\033[K")
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
# -- generate
# -------------------------------------------------------------------------------------------------
vID = 1
vContent = ""

# vCat = "move"
# vCat = "pokemon"
# vCat = "item"
vCat = "nature"


vReq = requests.get( f"http://pokeapi.co/api/v2/{vCat}/{vID}/" )
vStatus = vReq.status_code

while vStatus == 200:
    vName = json.loads( vReq.content.decode( ) )[ 'name' ].upper( ).replace("-", "_")
    vContent += f"{vName:70}= {vID}\n"
    display( f"ID = {vID} | Name : {vName}" )
    
    vID += 1
    vReq = requests.get( f"http://pokeapi.co/api/v2/{vCat}/{vID}/" )
    vStatus = vReq.status_code
    
with open( f"src/_config/{vCat}.txt", "w" ) as vFile:
    vFile.write( vContent )
    
print( "Done" )
# -------------------------------------------------------------------------------------------------