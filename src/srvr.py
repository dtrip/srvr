
from colorama import init, Fore, Back, Style
from cement.core.foundation import CementApp
from cement.core.controller import CementBaseController, expose
from cement.core import handler

sys.path.append(os.getcwd())

class Srvr():
    class Meta:
        label = 'base'
        description = "Receive real time custom updates from your server via socket"
        self.config = "~/.config/srvr/config.json"
        arguments = [
                (['-s', '--server'], dict(action='store', help='Start server instance')),
                (['-p', '--port'], dict(action='store', help='Port for server to listen on')),
                (['-H', '--host'], dict(action='store', help='Server hostname or IP address'))
                ]


    @expose(hide=True)
    def client(self):
        pass

class Srvr(CementApp):
    class:
        label = 'srvr'
        base_controller = 'base'
        handlers = [Srvr]


with Srvr() as srvr:

    try
        srvr.run()
    except Exception as e:
        print "%s%s[!] Error: %s%s" % (Style.BRIGHT, Fore.WHITE, str(e), Style.RESET_ALL)
