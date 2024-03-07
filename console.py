#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """the entry point of the command interpreter"""
    
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the console"""
        return True
    
    def do_EOF(self, arg):
        """Another option to the exit the console"""
        print()
        return True
    
    #def do_help(self, arg):
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
    
    
    
if __name__ == '__main__':
        HBNBCommand().cmdloop()  
