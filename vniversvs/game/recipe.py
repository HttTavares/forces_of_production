class Recipe(dict):
    """
        Class Description
    """
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def execute( self, player, game ):
        # for requirement in self.requirements:
        #     if not self.check( requirement, player ):
        #         print(f'requirement {requirement} not satisfied by {player}')
        #         return
        # else:
        #     for effect in self.effects:
        #         effect()
        if player.capital.check_input( self.input ):
            print('enough input')
            for material in self.input:
                player.capital.materials[material] -= self.input[material]
            # for requirement in self.requirements:
            #     self.check( requirement )

            for material in self.output:
                player.capital.materials[material] += self.output[material]
            for effect in self.effects.values():
                effect['method']( **effect['parameters'] )
        else:
            print('not enough input')

    def final_input( self, player, game ):
        pass

    def final_output( self, player, game ):
        pass

#
