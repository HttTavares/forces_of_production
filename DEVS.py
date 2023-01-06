from devs.arcanum import Arcanum
from devs.logos import Logos
from devs.nebula import Nebula
from devs.alpha import Alpha
from devs.omega import Omega
from devs.regula import Regula
from devs.via import Via
from devs.veritas import Veritas
from devs.vita import Vita
from devs.topos import Topos
from devs.kronos import Kronos

from vniversvs.vniversvs import VNIVERSVS


class DEVS(dict):
    """
        DEVS is the "absoulute" class that creates
        and handles everything in the project
    """
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.alpha = Alpha()
        self.vniversal_objects = [
            'vniversvs',
            'devs',
            'via',
        ]

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def make_object_metadata( self, object ):
        object.vniversvs = self.vniversvs
        object.devs = self
        object.via = Via()

    def fiat( self ):
        self.fiat_vniversvs()
        self.fiat_omega()
        self.fiat_regula()
        self.fiat_logos()
        self.fiat_commands()

    def fiat_vniversvs( self ):
        self.vniversvs = VNIVERSVS(
            initialization_data = self.alpha.vniversvs
        )
        self.vniversvs.devs = self
        self.vniversvs.topos = Topos()
        self.make_object_metadata(self.vniversvs.topos)        
        self.vniversvs.kronos = Kronos()
        self.make_object_metadata(self.vniversvs.kronos)        
        self.vniversvs.veritas = Veritas()
        self.vniversvs.veritas.vniversvs = self.vniversvs
        print('vniversvs created')
        return self.vniversvs

    def fiat_omega( self ):
        self.omega = Omega()
        self.make_object_metadata( self.omega )
        print('omega created')
        return self.omega

    def fiat_regula( self ):
        self.regula = Regula()
        self.make_object_metadata( self.regula )
        print('regula created')
        return self.regula

    def fiat_logos( self ):
        self.logos = Logos()
        self.make_object_metadata( self.logos )
        print('logos created')
        return self.logos

    def fiat_nebula( self ):
        self.nebula = Nebula()
        self.make_object_metadata( self.nebula )
        print('nebula created')
        return self.nebula

    def run_logos( self ):
        self.logos.next_command = ''
        while self.logos.next_command != 'q':
            self.logos.next_command = input("type a command: ")
            self.logos.parsed_command = self.logos.parse_commands( self.logos.next_command )
            self.logos.execute_command( self.logos.current_command )
            self.vniversvs.update()
        print('bye bye')

    def fiat_commands( self ):
        with open('devs/logos.py') as tmp:
            tmp = tmp.read().split('\n')
            for line in tmp:
                if 'def command_' in line and '#' not in line:
                    command_name = line[8:]
                    command_name = command_name.split('(')[0]
                    command_key = command_name[8:]
                    self.logos.commands[command_key] = getattr(self.logos, command_name)



#
