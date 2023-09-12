import cmd
import os
import platform


from topologies import *

if platform.system() == "Windows":
    import pyreadline

    clear = "cls"
else:
    import readline

    clear = "clear"


def case_insensitive_onecmd(self, line):
    cmd, arg, line = self.parseline(line)
    if not cmd:
        return self.emptyline()
    self.lastcmd = line
    if line == "EOF":
        self.lastcmd = ""
    cmd = cmd.lower()
    try:
        func = getattr(self, "do_" + cmd)
    except AttributeError:
        return self.default(line)
    return func(arg)


cmd.Cmd.onecmd = case_insensitive_onecmd


class TCPShell(cmd.Cmd):
    intro = "Welcome to TCP stack simulator. Type help or ? to list commands.\n"
    prompt = "root@tcp_stack> $ "
    commands = ["show", "help", "config", "cls", "build"]
    completekey = "tab"
    config = False

    def emptyline(self):
        return

    def do_exit(self, args):
        """Exit from the CLI."""
        if self.config:
            self.prompt = "root@tcp_stack> $ "
            self.config = False
        else:
            print("Goodbye!")
            return True

    def do_config(self, args):
        """Enter configuration mode."""
        self.prompt = "root@tcp_stack(config)> $ "
        self.config = True

    def do_build(self, args):
        """Build a topology"""
        if self.config:
            pass
        else:
            print("You must be config mode to build.")

    def do_show(self, args: str):
        """Display <argument>"""
        arg_list = args.split()
        if len(arg_list) >= 1:
            if arg_list[0] == "topologies":
                try:
                    print("\n")
                    star = build_star_topology()
                    print(star)
                except:
                    pass
        else:
            print("<show> command requires an <argument>.")

    def do_cls(self, args):
        """Clear the screen."""
        os.system(clear)

    def completedefault(self, text, line, begidx, endidx):
        if text:
            return [i for i in self.commands if i.startswith(text)]

    def complete_show(self, text, line, begidx, endidx):
        options = ["topologies"]
        if text:
            return [i for i in options if i.startswith(text)]

    def complete_config(self, text, line, begidx, endidx):
        options = [""]
        if text:
            return [i for i in options if i.startswith(text)]
