class Veritas(dict):
    """
        Veritas is the class to handle user visualization
        for the object.
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

    def show_object( self, object_id ):
        print()
        object_data = self.vniversvs.read_object( object_id ).via.get_current_data()
        print('basic data for', object_data['basic']['name'])
        for key in object_data['basic']:
            print(key, object_data['basic'][key])
        print()
        print('advanced data for', object_data['basic']['name'])
        for key in object_data['advanced']:
            print(key, object_data['advanced'][key])
        print()


#
