from pymilvus import connections,utility,Collection
import os

from dotenv import load_dotenv
load_dotenv()
host=os.getenv('HOST')
port=os.getenv('PORT')

def drop_collection(collection_name:str):
    conn = connections.connect(host=host, port=port) # test

    utility.drop_collection(collection_name)
    
    # utility.drop_collection( "CgFourWheelers")
    # utility.drop_collection( "avatr_CgFourWheelers")
    # utility.drop_collection( "aion_y_CgFourWheelers")
    # utility.drop_collection( "king_long_CgFourWheelers")
    # utility.drop_collection( "neta_CgFourWheelers")
    # utility.drop_collection( "riddara_CgFourWheelers")
    # utility.drop_collection( "smart_CgFourWheelers")
    # # utility.drop_collection( "neta_CgFourWheelers")
    # utility.drop_collection( "xpeng_CgFourWheelers")
    # utility.drop_collection( "aion_y_CgFourWheelers_charging_station")

    print("After",utility.list_collections())