#!/usr/bin/python3
''' command line for AirBnb '''
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    ''' entry point of CMD.
    Attributes:
        prompts: prompt of CMD.
    '''

    CLSs = ["BaseModel", "User", "Amenity", "Place", "Review", "State", "City"]
    prompt = "(hbnb) "

    def do_EOF(self, line):
        ''' Exit program While prssing "Ctrl+D" '''
        print('')
        return True

    def do_quit(self, line):
        ''' Quit program '''
        return True

    def emptyline(self):
        ''' Dont execite anything if it is emty line'''
        pass

    def do_create(self, line):
        ''' Creates new instance of class '''
        lis = shlex.split(line)
        if len(lis) == 0:
            print("** class name missing **")

        elif len(lis) == 1:
            if lis[0] not in self.CLSs:
                print("** class doesn't exist **")
            else:
                inst = eval(lis[0])()
                inst.save()
                print(inst.id)

    def do_show(self, line):
        ''' Show all string representation of Instance. '''
        lis = shlex.split(line)
        if len(lis) == 0:
            print("** class name missing **")
        elif len(lis) == 1:
            if lis[0] not in self.CLSs:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(lis) == 2 and lis[0] in self.CLSs:
            storage.reload()
            objs = storage.all()
            if "{}.{}".format(lis[0], lis[1]) not in objs:
                print("** no instance found **")
            else:
                print(objs["{}.{}".format(lis[0], lis[1])])

    def do_destroy(self, line):
        ''' Deletes an instance based on ID.'''
        lis = shlex.split(line)
        if len(lis) == 0:
            print("** class name missing **")
        elif len(lis) == 1:
            if lis[0] not in self.CLSs:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(lis) == 2 and lis[0] in self.CLSs:
            storage.reload()
            objs = storage.all()
            if "{}.{}".format(lis[0], lis[1]) not in objs:
                print("** no instance found **")
            else:
                del objs["{}.{}".format(lis[0], lis[1])]
                storage.save()

    def do_all(self, line):
        ''' Show all string representation of entire class.'''
        lis = shlex.split(line)
        storage.reload()
        ob = []
        if len(lis) == 1:
            if lis[0] not in self.CLSs:
                print("** class doesn't exist **")
            else:
                for i in storage.all().values():
                    if i.__class__.__name__ == lis[0]:
                        ob.extend(["{}".format(i.__str__())])
                print(ob)
        elif len(lis) == 0:
            ob.extend(
                    ["{}".format(i.__str__()) for i in storage.all().values()]
                    )
            print(ob)

    def do_update(self, line):
        ''' Update Instance attribute value.'''
        storage.reload()
        objs = storage.all()
        lis = shlex.split(line)
        if len(lis) == 0:
            print("** class name missing **")
            return
        elif len(lis) == 1:
            if lis[0] not in self.CLSs:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
            return
        elif len(lis) == 2:
            try:
                objs["{}.{}".format(lis[0], lis[1])]
            except KeyError:
                print("** no instance found **")
                return
            print("** attribute name missing **")
            return
        elif len(lis) == 3:
            print("** value missing **")
            return
        elif len(lis) == 4:
            try:
                Att_type = type(objs["{}.{}".format(lis[0], lis[1])].__dict__[lis[2]])
            except KeyError:
                return
            objs["{}.{}".format(lis[0], lis[1])].__dict__[lis[2]] = eval(Att_type)(lis[3])
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
