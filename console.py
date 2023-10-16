#!/usr/bin/python3
""" This module contains the console interface for the HBNB system.
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class_s = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'Review': Review
}

def lists_objects(args):
    """Returns the list of objects in the storage"""

    objects = models.storage.all()
    lists_objects = []
    for key, value in objects.items():
        if args[0] == "":
            lists_objects.append(str(value))
            continue
        if args[0] == key[:len(args[0])]:
            lists_objects.append(str(value))
    return lists_objects


def do_parenthesis(args):
    """ Find, handle  and extracts argument within parenthesis"""

    if args.find("(") + 1 == args.find(")"):
        return "{}".format(args[:args.find(".")])

    return "{} {}".format(
        args[:args.find(".")],
        args[args.find(
            "(") + 1:-1].replace('"', '').replace(",", "")
        )


class HBNBCommand(cmd.Cmd):
    """ Defines the entry point of our command interpreter."""

    prompt = "(hbnb) "

    def newcmd(self, args):
        """Handles user input such as for all classes and description
        """
        arguments = args.split(" . ")
        if len(arguments) > 1:
            inside_p = args[args.index(".") + 1:args.index("(")]
            if inside_p == "all":
                return self.do_all(args[:args.index(".")])
            elif inside_p == "show":
                return self.do_show(do_parenthesis(args))
            elif inside_p == "destroy":
                return self.do_destroy(do_parenthesis(args))
            elif inside_p == "count":
                print(len(lists_objects(do_parenthesis(args))))
                return
            elif inside_p == "update":
                return self.do_update(do_parenthesis(args))
        return super(HBNBCommand, self).newcmd(args)

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

    def do_create(self, args):
        """
        Creates a new instance of a class, saves it to the JSON file,
        and prints the ID.
        """
        if not args:
            print("** class name missing **")
        if args not in class_s:
            print("** class doesn't exist **")
        else:
            new_instance = class_s[args]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and ID.
        """
        if not args:
            print("** class name missing **")
        else:
            arguments = args.split(" ")
            if arguments[0] not in class_s:
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            else:
                objs = models.storage.all()
                key = f"{arguments[0]}.{arguments[1]}"
                if key in objs.keys():
                    print(objs[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if not args:
            print("** class name missing **")
        else:
            arguments = args.split(" ")
            if arguments[0] not in class_s:
                print("** class doesn't exist **")
            elif len(arguments) < 2:
                print("** instance id missing **")
            else:
                objs = models.storage.all()
                key = arguments[0] + "." + arguments[1]
                if key in objs.keys():
                    del objs[key]
                    models.storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances based
        or not on the class name"""
        objs = models.storage.all()

        arguments = args.split(" ")

        if arguments[0] != "" and arguments[0] not in class_s:
            print("** class doesn't exist **")
        else:
            print(lists_objects(arguments))

    def do_update(self, args):
        """ Updates an instance based on the class name and id (save the change into the JSON file)
        """
        arguments = args.split(" ")

        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] not in class_s:
            print("** class doesn't exist **")
        elif len(arguments) < 2:
            print("** instance id missing **")
        else:
            obj_key = arguments[0] + "." + arguments[1]
            objs = models.storage.all()
            if obj_key in objs.keys():
                if len(arguments) < 3:
                    print("** attribute name missing **")
                elif len(arguments) < 4:
                    print("** value missing **")
                else:
                    instance = objs[obj_key]
                    setattr(instance, arguments[2], arguments[3])
                    instance.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
