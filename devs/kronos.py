from datetime import date


class Kronos(dict):
    """
        Kronos is the class to handle time
        inside and outside the project

        Saves and Loads
    """
    # attrs: []
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

    def save( self ):
        devs_data = {}
        universal_data = {}
        for object_type in self.vniversvs.topos:
            if object_type not in self.devs.vniversal_objects:
                universal_data[object_type] = {}
                for object_instance_name in self.vniversvs.topos[object_type]:
                    universal_data[object_type][object_instance_name] = self.vniversvs.topos[object_type][object_instance_name].via.get_current_data()
        for object_type in universal_data:
            df_object = self.vniversvs.pd.DataFrame( columns = list(universal_data[object_type].values())[0]['basic'].keys() )
            for object_instance in universal_data[object_type]:
                df_object = df_object.append( universal_data[object_type][object_instance]['basic'], ignore_index = True )
        df_object.to_csv(f'{object_type}.csv')


    def load( self ):
        dir_list = self.vniversvs.os.listdir(self.vniversvs.os.getcwd())
        for file_name in dir_list:
            if '.csv' in file_name:
                object_type = file_name[:file_name.find('.csv')]
                df = self.vniversvs.pd.read_csv(file_name)
                df_row_list = df.to_dict(orient = 'records')
                for row in df_row_list:
                    # clean
                    for key in row.keys():
                        if 'Unnamed' in key:
                            delete = key
                    row.pop(delete)
                    #create
                    object = self.vniversvs.create_object( 
                        object_type,    
                        object_initialization_data = row 
                    )

    def get_today_date( self ):
        return str(date.today())
        


#