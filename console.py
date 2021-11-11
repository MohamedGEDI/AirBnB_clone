#!/usr/bin/python3
"""our little shell source code"""


import cmd, sys


"""import cmd and turtleshell"""


class HBNBCommand(cmd.Cmd):
    """intro = first message when shell is started"""
    intro = "Welcome to our AirBnB clone project. " \
            "Type help or ? to see list of commands"

    """Prompt that shows before a command"""

    prompt = "(hbnb) "
    file = None

    def do_quit(self, arg):
        """type quit to leave: quit"""
        print("thank you for visiting")
        self.close()
        quit()
        return True

    def do_record(self, arg):
        """Save future commands to filename:  RECORD rose.cmd"""
        self.file = open(arg, 'w')

    def do_playback(self, arg):
        """Playback commands from a file:  PLAYBACK rose.cmd"""
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        if self.file:
            self.file.close()
            self.file = None


if __name__ == '__main__':
    HBNBCommand().cmdloop()

