from devs.alpha import Alpha
import pandas as pd
import os

from vniversvs.game.game import Game
from vniversvs.game.player import Player
from vniversvs.game.recipe import Recipe

from vniversvs.society.society import Society
from vniversvs.society.population import Population

from vniversvs.capital.capital import Capital
from vniversvs.capital.material import Material

from vniversvs.knowledge.technique import Technique



class VNIVERSVS(dict):
    """
        vniversvs the class to handle project objects
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.objects = {
            ### PLACE EVERY CLASS HERE LIKE SO:
            # 'ClassName': class,
            'Game': Game,
            'Player': Player,

            'Society': Society,
            'Population': Population,
            'Capital': Capital,
            'Material': Material,
            'Recipe': Recipe,
            'Technique': Technique,
            # 'ClassName': class
            # 'ClassName': class
            # 'ClassName': class
            # 'ClassName': class
            # 'ClassName': class
        }
        self.pd = pd
        self.os = os

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


##########################################################################################
# OBJECT HANDLING ########################################################################
##########################################################################################

    def create_object( self, object_name, object_initialization_data ):
        try:
            object = self.objects[object_name](
                initialization_data = object_initialization_data
            )
        except:
            object = self.objects[object_name]()
        if object_name not in self.topos:
            self.topos[object_name] = {}
        self.topos[object_name][object_initialization_data['name']] = object
        self.devs.make_object_metadata(object)
        return object

    def read_object( self, object_id ):
        object = None
        for object_type in self.topos:
            if object_id in self.topos[object_type]:
                object = self.topos[object_type][object_id]
        if object == None:
            print('read_object method returned None')
        return object

    def update_object( self, object_id, new_object_data ):
        print(object_id, new_object_data)
        try:
            object = self.read_object( object_id )
            for key in new_object_data:
                object[key] = new_object_data[key]
        except:
            print( 'could not find or update object', object_id )

    # def delete_object( self, object_name ):
    #     try:
    #         for collection_name in self.collections.keys():
    #             if object_name in self.collections[collection_name].keys():
    #                 self.collections[collection_name].pop(object_name)
    #     except:
    #         print('could not find object', object_name)


##########################################################################################
# PROJECT HANDLING #######################################################################
##########################################################################################

    def init_project( self ):
        self.game = self.create_object(
            'Game',
            object_initialization_data = {
                'name': 'game'
            }
        ) 
        self.game.init_player(1)



#
