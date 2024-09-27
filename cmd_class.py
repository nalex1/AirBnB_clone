#!/usr/bin/python3
"""a cmd class that defines all commands of the hbnb clone project"""
import cmd


class HBNBCommand(cmd.Cmd):
    """a cmd module subclass"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""

        return True

    def emptyline(self):
        """ this should handle when the empty line is entered to the program"""
        pass
