from topologies import *
from network_graph import NetworkGraph


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


def exit_function(self) -> bool:
    if self.config_flag:
        self.prompt = "root@tcp_stack> $ "
        self.config_flag = False
        return False
    else:
        print("Goodbye!")
        return True


def build_function(self) -> NetworkGraph | None:
    if self.config_flag:
        return NetworkGraph("")
    else:
        print("You must be config mode to build.")


def show_function(self, args: str) -> None:
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
