#!/usr/bin/python3

import cmd, sys
from turtle import *


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to our AirBnB clone project. " \
            "Type help or ? to see list of commands"

    prompt = "(hbnb)"
    file = None




if __name__ == '__main__':
    HBNBCommand().cmdloop()

