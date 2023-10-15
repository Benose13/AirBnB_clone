#!/usr/bin/python3
""" This module contains the console interface for the HBNB system.
"""
import cmd
from models.base_model import BaseModel
from models.user import User


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

    class_s = {
            'BaseModel': BaseModel,
            'User': User
    }

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
        """new instance of BaseModel, saved to the JSON file"""
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            try:
                model_class = getattr(models, class_name)
                new_instance = model_class()
                new_instance.save()
                print(new_instance.id)
            except AttributeError:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the instance based on the class name and id."""
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            try:
                model_class = getattr(models, class_name)
            except AttributeError:
                print("** class doesn't exist **")

            if len(args) < 2:
                print("** instance id missing **")

            instance_id = args[1]
            instance = models.storage.get(model_class, instance_id)
            if not instance:
                print("** no instance found **")
            else:
                print(instance)

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]

            try:
                model_class = getattr(models, class_name)
            except AttributeError:
                print("** class doesn't exist **")

            if len(args) < 2:
                print("** instance id missing **")
            instance_id = args[1]
            instance = models.storage.get(model_class, instance_id)

            if not instance:
                print("** no instance found **")
            else:
                models.storage.delete(instance)
                models.storage.save()

    def do_all(self, args):
        """Prints the string representation of all instances"""
        model_classes = models.all_classes()

        if not args:
            for class_name in model_classes:
                try:
                    model_class = getattr(models, class_name)
                    instances = models.storage.all(model_class)
                    for instance in instances.values():
                        print(instance)
                except AttributeError:
                    print("** class doesn't exist **")
        else:
            class_name = args[0]
            try:
                model_class = getattr(models, class_name)
                instances = models.storage.all(model_class)
                for instance in instances.values():
                    print(instance)
            except AttributeError:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance."""
        if not args:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]

            try:
                model_class = getattr(models, class_name)
                instance = models.storage.get(model_class, instance_id)

                if not instance:
                    print("** no instance found **")
                else:
                    setattr(instance, attribute_name, attribute_value)
                    instance.save()
            except AttributeError:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
