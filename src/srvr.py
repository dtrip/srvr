import sys
import os
from colorama import init, Fore, Back, Style
from cement.core.foundation import CementApp
# from cement.core.controller import CementBaseController, expose
from cement.core import handler,backend

sys.path.append(os.getcwd())

import config



class Srvr:
    class Meta:
        label = 'srvr'
        base_controller = 'Base'
        define_handlers = [SrvrBase]

    def run(self):
        label


def main():
    with Srvr() as app:
        try:
            app.run()
            # s = Srvr()
            # s.run()
        except Exception as e:
            print "\n%s%s%s[!] Error: %s%s\n" % (Style.BRIGHT, Back.RED,Fore.WHITE, str(e), Style.RESET_ALL)
        finally:
            app.close()
            # app.__exit__


# def __exit__(self, type, value, traceback):
#     print "Exit called"


