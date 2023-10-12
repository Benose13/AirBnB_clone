#!/usr/bin/python3
""" This module contains the command-line/console interface for the HBNB system.
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Defines the entry point of our command interpreter."""

    prompt = "(hbnb) "

    def emptyline(self):
        """ Do nothing upon receiving an empty line. """
        pass

    def do_quit(self, args):
        """ Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """ EOF command to exit the program with ctrl+D
        """
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
