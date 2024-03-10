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

    used_classes = {"BaseModel": BaseModel,
                    "Amenity": Amenity,
                    "City": City,
                    "Place": Place,
                    "Review": Review,
                    "User": User,
                    "State": State}

    def do_quit(self, arg):
        """Quit the console"""
        return True

    def do_EOF(self, arg):
        """Another option to the exit the console"""
        print()
        return True

    def help_quit(self):
        """The help documentation for quitting the console """
        print("Quit command to exit the program")

    def help_EOF(self):
        """The help documentation for EOF"""
        print("EOF command to exit the program")

    def emptyline(self):
        """An empty line or ENTER will execute nothing """
        pass

    # def default(self, arg)

    def do_create(self, arg):
        """create a new instance of BaseModel"""

        args = arg.split()
        if len(args) == 0 or arg is None:
            print("** class name missing **")
        else:
            instance_name = args[0]
            if instance_name in self.used_classes:
                created_instance = self.used_classes.get(args[0])()
                print(created_instance.id)
            else:
                print("** class doesn't exist **")
        storage.save()

    def do_show(self, arg):
        """
            Prints the string representation of an
            instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.used_classes:
            if len(args) < 2:
                print("** instance id missing **")
            else:
                inst_id = args[1]
                key = "{}.{}".format(args[0], inst_id)
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if arg == "" or arg is None:
            print("** class name missing **")
        else:
            arg1 = arg.split()
            name_class = arg1[0]
            if name_class not in self.used_classes:
                print("** class doesn't exist **")
            elif len(arg1) < 2:
                print("** instance id missing **")
            else:
                inst_id = arg1[1]
                key = "{}.{}".format(arg1[0], inst_id)
                all_instances = storage.all()
                if key not in all_instances:
                    print("** no instance found **")
                else:
                    del all_instances[key]
                    storage.save

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        args = arg.split()
        if args[0] not in self.used_classes:
            print("** class doesn't exist **")
        else:
            all_instances = storage.all().values()
            instances = []
            for instance in all_instances:
                if instance.__class__.__name__ == args[0]:
                    instances.append(str(instance))
            print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.used_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            instances = storage.all()
            if key not in instances:
                print("** no instance found **")
            elif len(args) < 3:
                print("** attribute name missing **")
            elif len(args) < 4:
                print("** value missing **")
            else:
                instance = instances[key]
                """if hasattr(instance, args[2]):
                    attr_type = type(getattr(instance, args[2]))
                    try:
                        cast_value = attr_type(args[3])
                        setattr(instance, args[2], cast_value)
                        instance.save()
                    except ValueError:
                        print("** invalid value type **")
                else:
                """
                setattr(instances[key], args[2], args[3])
                instances[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
