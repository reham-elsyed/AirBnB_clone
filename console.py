#!/usr/bin/python3
"""This is our console for AirBnB project"""

import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State

class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""
    
    prompt = "(hbnb) "

    used_classes = {"BaseModel", "Amenity", "City", "Place", "Review", "User", "State"}
    
    def do_quit(self, arg):
        """Quit the console"""
        return True
    
    def do_EOF(self, arg):
        """Another option to the exit the console"""
        print()
        return True
    
    # def do_help(self, arg):
        #"""Help method to print available commands"""
        #cmd.Cmd.do_help(self, arg)

    def help_quit(self):
        """The help documentation for quitting the console """
        print("Quit command to exit the program")
        
    def help_EOF(self):
        """The help documentation for EOF"""
        print("EOF command to exit the program")    

    def emptyline(self):
        """An empty line or ENTER will execute nothing """
        pass
    
    # def default(self, arg):
    
    
    def do_create(self, arg):
        """create a new instance of BaseModel"""
       
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            arg1 = arg.split(" ")
            name_class = arg1[0]
            if name_class not in HBNBCommand.used_classes:
                print("** class doesn't exist **")
                return
            
        new_instance = storage.classes()name_class
        new_instance.save()
        print(new_instance.id)
           
           
    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            arg2 = arg.split(" ")
            if arg2[0] not in HBNBCommand.used_classes:
                print("** class doesn't exist **")
                return
            elif len(arg2) < 2:
                print("** instance id missing **")
            else:
                inst_id = arg2[1]
                key = "{}.{}".format(arg2[0], inst_id)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
        
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            arg1 = arg.split(" ")
            name_class = arg1[0]
            if name_class not in HBNBCommand.used_classes:
                print("** class doesn't exist **")
                return
            elif len(arg1) < 2:
                print("** instance id missing **")
            else:
    
    
    
    
if __name__ == '__main__':
        HBNBCommand().cmdloop()  
