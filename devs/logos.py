from devs.alpha import Alpha
import json
import pandas as pd

class Logos(dict):
    """
        Logos is a basic user-side CLI to use the app
    """

######################################################
# GENERAL FEATURES ###################################
######################################################

    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.commands = {}
        self.selectable = {
            # 'Classname': {}
        }
        self.selected = None

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def execute_command( self, command_text ):
        if self.devs.env == 'p':
            try:
                self.commands[command_text]()
                print()
            except:
                print('no such command, brah')
                print()
        if self.devs.env == 'd':
            self.commands[command_text]()
            print()

    def get_parameter_list( self, parameter ):
        list1 = parameter.split(',')

    def parse_commands( self, command_text ):
        parameter_list = command_text.split(' @ ')
        ret = {}
        for parameter in parameter_list[1:]:
            if ' = ' in parameter:
                pair = parameter.split(' = ')
                ret[pair[0]] = pair[1]
        self.current_command = parameter_list[0]
        self.current_parameters = ret
        return ret

    def command_q( self ):
        # self.command_save()
        quit()

    def command_test( self ):
        tester = self.devs.tester
        # print(tester.tests[self.current_parameters['name']])
        # print(self.selected)
        tester.tests[self.current_parameters['name']](self.selected)

    # def command_select( self ):
    #     # self.selectable = self.universe.collections['project'].keys()
    #     self.selectable = []
    #     if self.current_parameters['name'] in self.selectable:
    #         self.selected = self.current_parameters['name']
    #         print('you have selected:', self.selected)
    #     else:
    #         print('could not find object', self.current_parameters['name'])
    #         print('did you mean: ')
    #         for selectable_name in self.selectable:
    #             print(selectable_name)

    def command_select( self ):
        self.fill_selectable()
        for object_type in self.selectable:
            if self.current_parameters['name'] in self.selectable[object_type]:
                self.selected = self.current_parameters['name']
                print('you have selected:', self.selected)
        if self.selected == None:
            print('failed to select')


    def command_load( self ):
        self.vniversvs.kronos.save()

    def command_save( self ):
        self.vniversvs.kronos.save()


    def command_create( self ):
        object = self.vniversvs.create_object(
            self.current_parameters['type'],
            object_initialization_data = {
                'name': self.current_parameters['name']
            }
        )
        for parameter_name in self.current_parameters:
            print(parameter_name)
        print('command create succesfull', object.name )

    def fill_selectable( self ):
        for object_type in self.selectable:
            for object_name in self.vniversvs.topos[object_type]:
                self.selectable[object_type][object_name] = self.vniversvs.topos[object_type][object_name]

    def command_show_selected( self ):
        if self.selected != None:
            self.vniversvs.veritas.show_object(self.selected)

######################################################
# PROJECT SPECIFIC ###################################
######################################################



# create @ type = ?? @ name = 



#