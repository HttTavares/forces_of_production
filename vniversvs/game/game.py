class Game(dict):
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
        self.players = {}

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def init_player( self, player_number ):
        self.players[player_number] = self.vniversvs.create_object(
            'Player',
            object_initialization_data = {
                'name': f'player {player_number}',
            }    
        )
        self.players[player_number].society = self.vniversvs.create_object(
            'Society',
            object_initialization_data = {
                'name': f'player{player_number}.society',
            }    
        )
        self.players[player_number].society.population = self.vniversvs.create_object(
            'Population',
            object_initialization_data = {
                'name': f'player{player_number}.society.population',
                'total': 100
            }    
        )
        self.players[player_number].capital = self.vniversvs.create_object(
            'Capital',
            object_initialization_data = {
                'name': f'player{player_number}.capital',
                'materials': {
                    'wood': 100,
                    'food': 100,
                    'metal': 100,
                }
            }    
        )


#
