class Via(dict):
    """
        Via is the class to handle the object's
        data, state and history.
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

    def get_current_data( self ):
        self.data = {
            'basic': {},
            'advanced': {}
        }
        for property_name in self.object.keys():
            if type(self.object[property_name]) == type(1) or type(self.object[property_name]) == type(1.1) or type(self.object[property_name]) == type('1'):
                self.data['basic'][property_name] = self.object[property_name]
        return self.data



#
