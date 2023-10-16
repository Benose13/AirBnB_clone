#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(args):
    curly_braces = re.search(r"\{(.*?)\}", args)
    brackets = re.search(r"\[(.*?)\]", args)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(args)]
        else:
            lexer = split(args[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(args[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    """

    prompt = "(hbnb) "
    __class_s = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, args):
        """Default behavior for cmd module when input is invalid"""
        argsdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", args)
        if match is not None:
            argument = [args[:match.span()[0]], args[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argument[1])
            if match is not None:
                command = [argument[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argsdict.keys():
                    call = "{} {}".format(argument[0], command[1])
                    return argsdict[command[0]](call)
        print("*** Unknown syntax: {}".format(args))
        return False

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, args):
        """
        Create a new class instance and print its id.
        """
        argument = parse(args)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__class_s:
            print("** class doesn't exist **")
        else:
            print(eval(argument[0])().id)
            storage.save()

    def do_show(self, args):
        """Display the string representation of a class instance of a given id.
        """
        argument = parse(args)
        objdict = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__class_s:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argument[0], argument[1])])

    def do_destroy(self, args):
        """Delete a class instance of a given id."""
        argument = parse(args)
        objdict = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__class_s:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argument[0], argument[1])]
            storage.save()

    def do_all(self, args):
        """Display string representations of all instances of a given class."""
        argument = parse(args)
        if len(argument) > 0 and argument[0] not in HBNBCommand.__class_s:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argument) > 0 and argument[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argument) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, args):
        """Retrieve the number of instances of a given class."""
        argument = parse(args)
        count = 0
        for obj in storage.all().values():
            if argument[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, args):
        """Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argument = parse(args)
        objdict = storage.all()

        if len(argument) == 0:
            print("** class name missing **")
            return False
        if argument[0] not in HBNBCommand.__class_s:
            print("** class doesn't exist **")
            return False
        if len(argument) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argument[0], argument[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argument) == 2:
            print("** attribute name missing **")
            return False
        if len(argument) == 3:
            try:
                type(eval(argument[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argument) == 4:
            obj = objdict["{}.{}".format(argument[0], argument[1])]
            if argument[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argument[2]])
                obj.__dict__[argument[2]] = valtype(argument[3])
            else:
                obj.__dict__[argument[2]] = argument[3]
        elif type(eval(argument[2])) == dict:
            obj = objdict["{}.{}".format(argument[0], argument[1])]
            for k, v in eval(argument[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
