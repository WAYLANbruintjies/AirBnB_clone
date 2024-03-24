#!/usr/bin/python3
"""Bash script that defines HBnB console"""

import cmd
import re
import json
import shlex
import ast
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def split_braces(extra_arg):
    """
    Splits the curly braces for the update feature/method
    """
    curly_b = re.search(r"\{(.*?)\}", extra_arg)

    if curly_b:
        id_comma = shlex.split(extra_arg[:curly_b.span()[0]])
        id = [i.strip(",") for i in id_comma][0]

        data = curly_b.group(1)
        try:
            arg_dict = ast.literal_eval("{" + data + "}")
        except Exception:
            print("**  invalid dictionary format **")
            return
        return id, arg_dict
    else:
        commands = extra_arg.split(",")
        if commands:
            try:
                id = commands[0]
            except Exception:
                return "", ""
            try:
                attr_name = commands[1]
            except Exception:
                return id, ""
            try:
                attr_value = commands[2]
            except Exception:
                return id, attr_name
            return f"{id}", f"{attr_name} {attr_value}"

class HBNBCommand(cmd.Cmd):
    """HBNBCommand console"""
    prompt = "(hbnb) "
    my_classes = ['Basemodel', 'User', 'City', 'State', 'Place', 'Amenity', 'Review']

    def emptyline(self):
        """Execute nothing if empty line is TRUE"""
        pass

    def do_EOF(self, line):
        """ 
        End-Of-File signal to exit the programme
        (Ctrl+D)
        """
        print()
        return True

    def do_quit(self, line):
        """ Quit command to exit"""
        return True

    def do_create(self, line):
        """Create new User"""
        
        commands = shlex.split(arg)
        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.my_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]()}")
            storage.save()
            print(new_instance.id)

    def do_destroy(self, line):
        """Delete an instance by given class name and id"""
        
        splitline = split(line)

        if not splitline:
            print("** class name missing **")
            return False

        elif splitline[0] not in my_classes:
            print("** class doesn't exist **")

        elif len(splitline) < 2:
            print("** instance id missing **")

        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[new_instance]
                models.storage.save()

    def do_update(self, line):
        """
        Update command to update an instance base,
        Usage: <class>.update(<id>, <dictionary>).
        Updates a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        
        splitline = split(line)

        if not splitline:
            print("** class name missing **")

        elif splitline[0] not in my_classes:
            print("** class doesn't exist **")

        elif len(splitline) < 2:
            print("** instance id missing **")

        elif len(splitline) < 3:
            print("** attribute name missing **")

        elif len(splitline) < 4:
            print("** value missing **")

        else:
            new_instance = splitline[0] + '.' + splitline[1]
            if new_instance not in models.storage.all():
                print("** no instance found **")
            else:
                setattr(models.storage.all()[new_instance],
                        splitline[2], splitline[3])
                models.storage.save()

    def do_show(self, line):
        """Prints the command to show an instance string representation"""
        
        if not line:
            print("** class name missing **")
        elif line.split()[0] not in my_classes.keys():
            print("** class doesn't exist **")
        elif len(line.split()) < 2:
            print("** instance id missing **")
        else:
            new_instance = "{}.{}".format(line.split()[0], line.split()[1])
            obj = models.storage.all()

            if new_instance not in obj:
                print("** no instance found **")
            else:
                print(obj[new_instance])

    def do_all(self, line):
        """Print all string representations of all instances"""
        
        strings_li = []

        if not line:
            for new_instance in models.storage.all().values():
                strings_li.append(str(new_instance))
        else:
            splitline = split(line)
            if splitline[0] in my_classes:
                for key, value in models.storage.all().items():
                    if value.__class__.__name__ == splitline[0]:
                        strings_li.append(str(value))
            else:
                print("** class doesn't exist **")
                return False
        print(strings_li)

    def default(self, line):
        """Parse and interpretates a line if not found on regular commands"""
        
        splitline = line.split('.', 1)
        count = 0
        if len(splitline) >= 2:
            line = splitline[1].split('(')
            """Execute <class name>.all()"""
            if line[0] == 'all':
                self.do_all(splitline[0])
                """Execute <class name>.count() """
            elif line[0] == 'count':
                for key in models.storage.all():
                    if splitline[0] == key.split(".")[0]:
                        count += 1
                print(count)
                """Execute <class name>.show(<id>) """
            elif line[0] == 'show':
                id = line[1].split(')')
                str_id = str(splitline[0]) + " " + str(id[0])
                self.do_show(str_id)
                """Execute <class name>.destroy(<id>)"""
            elif line[0] == 'destroy':
                id = line[1].split(')')
                str_id = str(splitline[0]) + " " + str(id[0])
                self.do_destroy(str_id)
                """Execute <class name>.update(<id>"""
            elif line[0] == 'update':
                update = line[1].split(')')
                split = update[0].split('{')
                if len(split) == 1:
                    line = update[0].split(",")
                    str_id = str(splitline[0]) + " " + str(line[0]) + \
                        " " + str(line[1]) + " " + str(line[2])
                    self.do_update(str_id)
                else:
                    id = split[0][:-2]
                    str_dict = split[1][:-1]
                    delim = str_dict.split(',')
                    for row in delim:
                        key_value = row.split(':')
                        str_id = str(splitline[0]) + " " + str(id) + \
                            " " + str(key_value[0]) + " " + str(key_value[1])
                        self.do_update(str_id)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
