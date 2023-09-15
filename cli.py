import cmd
import os
import platform

from cli_functions import *
from network_graph import NetworkGraph

if platform.system() == "Windows":
    import pyreadline

    clear = "cls"
else:
    import readline

    clear = "clear"


cmd.Cmd.onecmd = case_insensitive_onecmd


class TCPShell(cmd.Cmd):
    intro: str = "Welcome to TCP stack simulator. Type help or ? to list commands.\n"
    prompt: str = "root@tcp_stack> $ "
    commands: list[str] = ["show", "help", "config", "cls", "build"]
    completekey: str = "tab"
    config_flag: bool = False
    network: NetworkGraph | None

    def emptyline(self) -> None:
        return

    def do_exit(self, args) -> bool:
        """Exit from the CLI."""
        return exit_function(self)

    def do_config(self, args) -> None:
        """Enter configuration mode."""
        self.prompt = "root@tcp_stack(config)> $ "
        self.config_flag = True

    def do_build(self, args) -> None:
        """Build a topology"""
        self.network = build_function(self)

    def do_show(self, args: str) -> None:
        """Display <argument>"""
        show_function(self, args)

    def do_cls(self, args) -> None:
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
