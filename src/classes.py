import dbtools
#import gui
import dataclasses

class validator: # objects of this class will validate the data supplied
    def __init__(self, to_validate):
        self.validate(to_validate)

    def validate(self, to_validate): # to_validate is passed as pair - data type and the data being validated
        # if no data is passed raise error
        if not to_validate:
            raise ValueError(f"Error, argument is empty.")
        # set variables for the expected data type and the actual data type passed
        expected = to_validate[1]
        actual = to_validate[0]
        # check if the expected data type and the actual data type are the same
        if expected == "str":
            if not isinstance(str, actual):
                actual_type = type(actual).__name__
                raise ValueError(f"Error: Incorrect data type. Expected string but got {actual_type} instead.")
        elif expected == "int":
            if not isinstance(int, actual):
                actual_type = type(actual).__name__
                raise ValueError(f"Error: Incorrect data type. Expected string but got {actual_type} instead.")
        
        # if the data is valid return the actual data  
        return actual
    
class Db_Entry:
    def __init__(self):
        self.table_payload = ''
        self.db = dbtools.dbtools()
    
    def collect_data(self, which): # which represents the data to be collected. For a single element use the data"s name i.e. "id", "name", etc. for a full plant of data use "all"
        # convert which into lower case
        which = which.lower()
        # if which is entered as "all" collect the values of all attributes and set them.
        if which.lower() == "all":
            for attr in self.types:
                self.set_value(attr)
            return 
        # if which is entered as a valid attribute of the plant class
        elif hasattr(self, which):
            try:
                # collect plant info for single value
                response = input(f"Please enter the {which}: ")
                res_pack = [self.types[which], response]
                # send data to be validated
                if validator(res_pack) == response:
                    pass
            except ValueError as e:
                print(f"Validation falure. {e}") # remember to loop
                    
        elif not which:
            raise ValueError(f"Data field left empty, please try again.")
        else:
            raise ValueError(f"Data type {which} not recognized, please try again.")

        return response
    
    def set_value(self, value_type):
        value_type = value_type.lower()
        if hasattr(self, value_type):  # Ensure the attribute exists
            setattr(self, value_type, self.collect_data(value_type))  # Dynamically set the value
        else:
            whoami = __class__.__name__
            raise ValueError(f"Error: {value_type} is not a valid attribute of {whoami}].")
        
    # getter for all attributes
    def get_value(self, value_type):
        if hasattr(self, value_type):  # Check if the attribute exists
            return getattr(self, value_type)  # Dynamically fetch the value
        else:
            whoami = __class__.__name__
            raise ValueError(f"Error: {value_type} is not a valid attribute of {whoami}.")
        
   # sends a full object item to the database  
    def send_data_all(self, what):
        what = what.lower()

       
        if what == "all":
            data = (self.table_payload,)
            for key in self.types.keys():
                    part = (self.get_value(key),)
                    data = data + part

            self.db.add_data(data)

        else:
            raise ValueError(f"Error: {what} is not a valid attribute of Plant.")

    # updates db
    def update_data(self, data_queary): # data order select(*), class name(table), desired update(...)
        data_queary = ("name", "rose", "lilly")
    
        if len(data_queary) == 2 and data_queary[0] in self.types and validator(data_queary[1]) == data_queary[1]:
            table = __class__.__name__
            data_to_find = ("id", table, data_queary[0], data_queary[1])
            try:
                id = self.db.find(data_to_find)
            except: LookupError(f"Error, there is no database item named {data_queary[1]}.")
            else: 
                data_to_send = (table, data_queary[2], id)
                self.db.update(data_to_send)

            
            






    

class Plant(Db_Entry):
    def __init__(self, id, quantity, name, description, isgreenhouse, supplier):
        self.name = name #string
        self.description = description #string
        self.isgreenhouse = isgreenhouse #bool
        self.supplier = supplier #int
        self.quantity = quantity #int
        self.id = id #int
        self.types = {
            "id": "int", 
            "quantity": "int", 
            "name": "str", 
            "description": "str", 
            "isgreenhouse": "int", 
            "supplier": "int",
        }
        self.table_payload = "plants (id, quantity ,name ,description ,greenhouse ,supplier_id)"

    
        
class Supplier:
    def __init__(self, id, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.id = id

test = Plant(10, 30, "Rose", "A thorny red bush!", 1, 20)

test.collect_data("all")
test.send_data("all")

test.collect_data("quantity")
test.send_data("quantity")
