class Omega(dict):
    """
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

    def run( self ):
        # print(self.vniversvs.game.players[1].capital.check_input(
        #     {
        #         'wood': 99
        #     }
        # ))
        # print(self.vniversvs.game.players[1].capital.check_input(
        #     {
        #         'wood': 100
        #     }
        # ))
        # print(self.vniversvs.game.players[1].capital.check_input(
        #     {
        #         'wood': 101
        #     }
        # ))
        reproduce_people = self.vniversvs.create_object(
            'Recipe',
            object_initialization_data = {
                'name': 'Reproduce People',
                'input': {
                    'food': 10
                },
                'output': {
                    # 'worker': 1
                },
                'effects': {
                    'reproduce people': {
                        'method': self.vniversvs.read_object( 'player 1' ).society.population.increase,
                        'parameters': {
                            'number_of_people': 1
                        }
                    }
                }
            }
        )
        player_1 = self.vniversvs.read_object( 'player 1' )
        # print(player_1.society.population)
        game = self.vniversvs.read_object( 'game' )
        # print(player_1.keys())
        for i in range(18):
            reproduce_people.execute( player_1, game )
        print(player_1.capital.materials)
        print(player_1.society.population.total)
#
