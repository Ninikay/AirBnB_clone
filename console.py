#!/usr/bin/python3
"""
BaseModel is a class that defines all
common attributes/methods for other classes
"""
import cmd
from models.base_model import BaseModel
from models import storage
from re import search
import shlex


class HBNBCommand(cmd.Cmd):
    """
        Summary: Aclass that define the command interpreter:
    """
    prompt = "(hbnb) "
    list_classes = ["BaseModel", "User", "Place", "State", "City",
                    "Amenity", "Review"]

    doc_header = "Documented commands (type help <topic>):"
    ruler = '='

    def do_EOF(self, line):
        "Exit the program with Ctrl+D"
        return True

    def do_quit(slef, line):
        "Quit command to exit the program"
        return True

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything
            If the line is empty, emptyline() is called,
            the method was modified because the default
            implementation runs the previous command again
            and we want it to pass not executing anything.
        """
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        args_list = arg.split(" ")
        if not args_list[0]:
            print("** class name missing **")
        elif args_list[0] in HBNBCommand.list_classes:
            new_instance = globals()[args_list[0]]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance
            based on the class name and id
        """
        args_list = args.split(" ")
        if args_list[0] == "":
            print("** class name is missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** The class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            """ We need to check if the 'id' exists, to do so we need to
            create id_object with the form Classname.id that is the key that
            we will ask if is in Storage and retrieve the value for that key
            """
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                """print the string representation based on the
                   class name and the ID
                """
                print(storage.all()[id_object])

    def do_destroy(self, args):
        """
        Usage: destroy <class name> <id>
        pops the required entry from the file storage __objects
        dictionary
        """
        args_list = args.split(" ")
        if args_list[0] == "":
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        else:
            obj_key = "{}.{}".format(args_list[0], args_list[1])
            if obj_key in storage.all():

                storage.all().pop(obj_key)
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """ Prints all string representation of all instances based or not
            on the class name
        """
        element_list = []
        args_list = args.split()

        if len(args_list) == 0:
            for key, value in storage.all().items():
                element_list.append(str(value))
            print(element_list)

        elif args_list[0] in HBNBCommand.list_classes:
            for key, value in storage.all().items():
                if value.__class__.__name__ == args_list[0]:
                    element_list.append(str(value))
            print(element_list)

        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id
            by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234
            email "aibnb@mail.com """

        args_list = shlex.split(arg[:])
        arg = arg.split(" ")
        if len(args_list) == 0:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.list_classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print("** instance id missing **")
        elif len(args_list) < 3:
            print("** attribute name missing **")
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            "if the instance of the class name doesn’t exist for the id"
            id_object = "{}.{}".format(args_list[0], args_list[1])
            if id_object not in storage.all():
                print("** no instance found **")
            else:
                dog = r"\d+\.\d+"
                id_object = "{}.{}".format(args_list[0], args_list[1])
                name_attr = args_list[2]
                value = args_list[3]
                """ Only “simple” arguments can be updated: string,
                    integer and float. """
                if '"' in arg[3]:
                    pass
                elif search(dog, arg[3]):
                    value = float(value)
                elif arg[3].isdigit():
                    value = int(value)
                setattr(storage.all()[id_object], name_attr, value)
                storage.all()[id_object].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
