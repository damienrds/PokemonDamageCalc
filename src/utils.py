# -------------------------------------------------------------------------------------------------
# -- Imports
# -------------------------------------------------------------------------------------------------
from random import randint, random
import requests
import json
# -------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------
gPokemonTypes = [
    "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
    "Fighting", "Poison", "Ground", "Flying", "Psychic",
    "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
]

gDamageTab = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1/2, 0, 1, 1, 1/2, 1],
    [1, 1/2, 1/2, 1, 2, 2, 1, 1, 1, 1, 1, 2, 1/2, 1, 1/2, 1, 2, 1],
    [1, 2, 1/2, 1, 1/2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1/2, 1, 1, 1],
    [1, 1, 2, 1/2, 1/2, 1, 1, 1, 0, 2, 1, 1, 1, 1, 1/2, 1, 1, 1],
    [1, 1/2, 2, 1, 1/2, 1, 1, 1/2, 2, 1/2, 1, 1/2, 2, 1, 1/2, 1, 1/2, 1],
    [1, 1/2, 1/2, 1, 2, 1/2, 1, 1, 2, 2, 1, 1, 1, 1, 2, 1, 1/2, 1],
    [2, 1, 1, 1, 1, 2, 1, 1/2, 1, 1/2, 1/2, 1/2, 2, 0, 1, 2, 2, 1/2],
    [1, 1, 1, 1, 2, 1, 1, 1/2, 1/2, 1, 1, 1, 1/2, 1/2, 1, 1, 0, 2],
    [1, 2, 1, 2, 1/2, 1, 1, 2, 1, 0, 1, 1/2, 2, 1, 1, 1, 2, 1],
    [1, 1, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1/2, 1],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1/2, 1, 1, 1, 1, 0, 1/2, 1],
    [1, 1/2, 1, 1, 2, 1, 1/2, 1/2, 1, 1/2, 2, 1, 1, 1/2, 1, 2, 1/2, 1/2],
    [1, 2, 1, 1, 1, 2, 1/2, 1, 1/2, 2, 1, 2, 1, 1, 1, 1, 1/2, 1],
    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1/2, 0],
    [1, 1, 1, 1, 1, 1, 1/2, 1, 1, 1, 2, 1, 1, 2, 1, 1/2, 1, 1/2],
    [1, 1/2, 1/2, 1/2, 1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1/2, 2],
    [1, 1/2, 1, 1, 1, 1, 2, 1/2, 1, 1, 1, 1, 1, 1, 2, 2, 1/2, 1]
]
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
def damage( inPkmUser, inPkmTarget, inMove ):
    global gPokemonTypes, gDamageTab
    
    if random( ) *100 > inMove.accuracy:
        return -1
    
    vRmd   = randint( 85, 100 ) / 100
    vLvl   = inPkmUser.level
    vPower = inMove.power
    vStab  = 1
    vCrit  = 1
    vEff   = 1
    
    if inMove.category == "Physical":
        vAtk = inPkmUser.Atk
        vDef = inPkmTarget.Def
        
    elif inMove.category == "Special":
        vAtk = inPkmUser.SpeAtk
        vDef = inPkmTarget.SpeDef
    
    if inMove.type in [ inPkmUser.type1, inPkmUser.type2 ]:
        vStab = 1.5
    
    if random( ) * 100 <= 4.17:
        vCrit = 1.5
        
    vEff *= gDamageTab[ gPokemonTypes.index( inMove.type ) ][ gPokemonTypes.index( inPkmTarget.type1 ) ]
    if inPkmTarget.type2 != None:
        vEff *= gDamageTab[ gPokemonTypes.index(inMove.type) ][ gPokemonTypes.index(inPkmTarget.type2) ]
    
    vDamage = int( ( ( ( vLvl * 0.4 + 2 ) * vAtk * vPower ) / ( vDef * 50 ) + 2 ) * vRmd * vStab * vCrit * vEff )
    
    return vDamage
# -------------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------------------
def req( inCategory, inID ):
    return json.loads(requests.get(f"http://pokeapi.co/api/v2/{inCategory}/{inID}/").content.decode( ) )
# -------------------------------------------------------------------------------------------------
