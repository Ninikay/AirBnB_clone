#!/usr/bin/python3
"""
BaseModel is a class that defines all common attributes/methods for other classes
"""
import cmd
#import shlex
from models.base_model import BaseModel
#from models.user import User
#from models.place import Place
#from models.state import State
#from models.city import City
#from models.amenity import Amenity
#from models.review import Review
from models import storage
from re import search


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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
