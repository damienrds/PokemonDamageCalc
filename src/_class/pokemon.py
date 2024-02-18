# -------------------------------------------------------------------------------------------------
# -- Imports
# -------------------------------------------------------------------------------------------------
from random import choice
from utils import req
# -------------------------------------------------------------------------------------------------

# =================================================================================================
class Pokemon:
    
    # ---------------------------------------------------------------------------------------------
    def __init__( self, inPokemonID ):
        self.pokemon = req( "pokemon", inPokemonID )
        
        # -- Global info
        self.name = None
        
        self.level = 100
        
        self.nature  = None
        self.nature_boost = {
            "attack": 1,
            "defense": 1,
            "special-attack": 1,
            "special-defense": 1,
            "speed": 1
        }
        self.ability = None
        self.sexe    = None
        
        self.itemHeld = None
        self.status   = None
        
        # Base stat
        self.base_HP     = 0
        self.base_Atk    = 0
        self.base_Def    = 0
        self.base_SpeAtk = 0
        self.base_SpeDef = 0
        self.base_Spd    = 0

        # EV stat
        self.EV_HP     = 0
        self.EV_Atk    = 0
        self.EV_Def    = 0
        self.EV_SpeAtk = 0
        self.EV_SpeDef = 0
        self.EV_Spd    = 0

        # IV stat
        self.IV_HP     = 0
        self.IV_Atk    = 0
        self.IV_Def    = 0
        self.IV_SpeAtk = 0
        self.IV_SpeDef = 0
        self.IV_Spd    = 0
        
        # Stat
        self.HP     = 0
        self.Atk    = 0
        self.Def    = 0
        self.SpeAtk = 0
        self.SpeDef = 0
        self.Spd    = 0
        
        self.type1 = None
        self.type2 = None
        
        self.move_1 = None
        self.move_2 = None
        self.move_3 = None
        self.move_4 = None
        
        self.onInit( )
    # ---------------------------------------------------------------------------------------------
    
    
    # ---------------------------------------------------------------------------------------------
    def onInit( self ):
        self.name = self.pokemon[ "name" ]
        
        # Base stat
        self.base_HP     = self.pokemon[ "stats" ][ 0 ][ "base_stat" ]
        self.base_Atk    = self.pokemon[ "stats" ][ 1 ][ "base_stat" ]
        self.base_Def    = self.pokemon[ "stats" ][ 2 ][ "base_stat" ]
        self.base_SpeAtk = self.pokemon[ "stats" ][ 3 ][ "base_stat" ]
        self.base_SpeDef = self.pokemon[ "stats" ][ 4 ][ "base_stat" ]
        self.base_Spd    = self.pokemon[ "stats" ][ 5 ][ "base_stat" ]
        
        # -- Type
        self.type1 = self.pokemon[ "types" ][ 0 ][ "type" ][ "name" ]
        if len( self.pokemon[ "types" ] ) == 2:
            self.type2 = self.pokemon[ "types" ][ 1 ][ "type" ][ "name" ]
        else:
            self.type2 = None
        
        # -- Set HARDY default nature
        self.set_nature( 1 )
    # ---------------------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------------------
    def set_EV( self, inHP, inAtk, inDef, inSpeAtk, inSpeDef, inSpd ):
        self.EV_HP     = inHP
        self.EV_Atk    = inAtk
        self.EV_Def    = inDef
        self.EV_SpeAtk = inSpeAtk
        self.EV_SpeDef = inSpeDef
        self.EV_Spd    = inSpd
        
        self.actualize_stat( )
    # ---------------------------------------------------------------------------------------------

        
    # ---------------------------------------------------------------------------------------------
    def set_IV( self, inHP, inAtk, inDef, inSpeAtk, inSpeDef, inSpd ):
        self.IV_HP     = inHP
        self.IV_Atk    = inAtk
        self.IV_Def    = inDef
        self.IV_SpeAtk = inSpeAtk
        self.IV_SpeDef = inSpeDef
        self.IV_Spd    = inSpd
        
        self.actualize_stat( )
    # ---------------------------------------------------------------------------------------------

        
    # ---------------------------------------------------------------------------------------------
    def set_type( self, inType1, inType2 ):
        self.type1 = inType1
        self.type2 = inType2
    # ---------------------------------------------------------------------------------------------

        
    # ---------------------------------------------------------------------------------------------
    def set_move( self, inMove_1, inMove_2, inMove_3, inMove_4 ):
        self.move_1 = inMove_1
        self.move_2 = inMove_2
        self.move_3 = inMove_3
        self.move_4 = inMove_4
    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def set_nature( self, inNatureID ):
        vNature = req( "nature", inNatureID)
        
        self.nature = vNature[ "name" ]
        
        self.nature_boost = {
            "attack": 1,
            "defense": 1,
            "special-attack": 1,
            "special-defense": 1,
            "speed": 1
        }
        
        if vNature[ "decreased_stat" ] != None and vNature[ "increased_stat" ] != None:
            for lStat, lBoost in [ ("decreased_stat", 0.9), ("increased_stat", 1.1) ]:
                self.nature_boost[ vNature[ lStat ][ "name" ] ] = lBoost
        
        self.actualize_stat( )
    # ---------------------------------------------------------------------------------------------

        
    # ---------------------------------------------------------------------------------------------
    def display_info( self ):
        print( f"Name  : {self.name}"  )
        print( f"Level : {self.level}" )
        print( f"Nature: {self.nature}" )
        print( f"Type  : {self.type1} | {self.type2}\n" )
        print( f"HP    : {self.base_HP:3} | {self.IV_HP:2} | {self.EV_HP:3} || {self.HP:3}" )
        print( f"Atk   : {self.base_Atk:3} | {self.IV_Atk:2} | {self.EV_Atk:3} || {self.Atk:3}" )
        print( f"Def   : {self.base_Def:3} | {self.IV_Def:2} | {self.EV_Def:3} || {self.Def:3}" )
        print( f"SpeAtk: {self.base_SpeAtk:3} | {self.IV_SpeAtk:2} | {self.EV_SpeAtk:3} || {self.SpeAtk:3}" )
        print( f"SpeDef: {self.base_SpeDef:3} | {self.IV_SpeDef:2} | {self.EV_SpeDef:3} || {self.SpeDef:3}" )
        print( f"Spd   : {self.base_Spd:3} | {self.IV_Spd:2} | {self.EV_Spd:3} || {self.Spd:3}\n" )
    # ---------------------------------------------------------------------------------------------


    # ---------------------------------------------------------------------------------------------
    def actualize_stat( self ):
        self.HP     = int( ( 2 * self.base_HP + self.IV_HP + int( self.EV_HP / 4 ) ) * self.level / 100 ) + self.level + 10
        self.Atk    = int( int( ( ( 2 * self.base_Atk + self.IV_Atk + int( self.EV_Atk / 4 ) ) * self.level / 100 ) + 5 ) * self.nature_boost[ "attack" ] )
        self.Def    = int( int( ( ( 2 * self.base_Def + self.IV_Def + int( self.EV_Def / 4 ) ) * self.level / 100 ) + 5 ) * self.nature_boost[ "defense" ] )
        self.SpeAtk = int( int( ( ( 2 * self.base_SpeAtk + self.IV_SpeAtk + int( self.EV_SpeAtk / 4 ) ) * self.level / 100 ) + 5 ) * self.nature_boost[ "special-attack" ] )
        self.SpeDef = int( int( ( ( 2 * self.base_SpeDef + self.IV_SpeDef + int( self.EV_SpeDef / 4 ) ) * self.level / 100 ) + 5 ) * self.nature_boost[ "special-defense" ])
        self.Spd    = int( int( ( ( 2 * self.base_Spd + self.IV_Spd + int( self.EV_Spd / 4 ) ) * self.level / 100 ) + 5 ) *self.nature_boost[ "speed" ] )
    # ---------------------------------------------------------------------------------------------
    
# =================================================================================================