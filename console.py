#!/usr/bin/python3
""" This module contains the console interface for the HBNB system.
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
