# AirBnB clone - The console

Welcome to the AirBnB clone project!

### Getting Started

This team project is part of the ALX Software Engineer program. It is an educational purpose clone project from [AirBnB] and it is the first step towards building a first full web application. This first step consists of a custom command-line interface for data management, and the base classes for the storage of this data.

## Description

For this task a basic console was created using the Cmd Python module, to manage the objects of the whole project, being able to implement the methods create, show, update, all, and destroy to the existing classes and subclasses.

## Functionalities of this command interpreter:

* Create a new object (ex: a new User or a new Place)
* Retrieve an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc...)
* Update attributes of an object
* Destroy an object

## File Storage

The presented classes are stored in FileStorage class file. When the console is initialized, the console redirects an instance of FileStorage named storage. #Storage object is loaded or reloaded from any class instances stored in the JSON file file.json. Class instances are created, updated, or deleted and storage object registers changes intofile.json.

A FileStorage class is defined in file_storage.py with methods to follow this flow: <object> -> to_dict() -> <dictionary> -> JSON dump -> <json string> -> FILE -> <json string> -> JSON load -> <dictionary> -> <object>

The init.py file contains the instantiation of the FileStorage class called storage, followed by a call to the method reload() on that instance. This allows the storage to be reloaded automatically at initialization, which recovers the serialized data.

## Console

The console is a CLI that allows the use of data as backend tool. It can be used to handle all classes predefined previously called into storage object.

## Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt and waits for the user for input:

### Interactive Mode

* Run the console	--> ./console.py
* Quit the console	-->(hbnb) quit
* Display the help for a command	-->(hbnb) help <command>
* Create an object (prints its id)	-->(hbnb) create <class>
* Show an object	-->(hbnb) show <class> <id> or (hbnb) <class>.show(<id>)
* Destroy an object	-->(hbnb) destroy <class> <id> or (hbnb) <class>.destroy(<id>)
* Show all objects, or all instances of a class 	-->(hbnb) all or (hbnb) all <class>
* Update an attribute of an object	-->(hbnb) update <class> <id> <attribute name> "<attribute value>" or (hbnb) <class>.update(<id>, <attribute name>, "<attribute
 value>")                                

### Non-interactive mode example

$ echo "help" | ./console.py             (hbnb)                                                                            Documented commands (type help <topic>): ========================================
EOF  all  count  create  destroy  help  quit  show  update

## Tests


All the code is tested with the unittest module. The test for the classes are in the test_models folder

## Further information

For further information on python version, and documentation visit python.org     

## Authors

Emmanuel Oguntade

Nike Oni

# License
Public Domain. No copy write protection
