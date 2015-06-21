
from colorama import init, Fore, Style
# import srvr
import configparser2
import os

class Config:

    def init(self):

        self.configPath = "~/.config/srvr/"

        self.serviceConfig = os.path.realpath(__file__) + 'service.conf'

        self.exampleFileName = "example.conf"
        self.configFileName = "srvr.conf"

        self.configExists = self.checkConfig();

        self.parser = ConfigParser()

        self.__parseConfigFile();

        return self.parser

    # Checks to ensure config has been created
    def checkConfig (self):

        if os.path.isfile(self.configPath + self.configFileName):
            return True
        else:
            if self.app.debug:
                print "%s[*] Setting up local config%s" % (Fore.BLUE, Style.RESET_ALL)

            self.__setupPath()
            self.__copyExample()
            return True

        return False

    # checks if config path exists,
    # if not, creates it
    def __setupPath (self):

        if not os.path.exists(self.configPath):
            os.makedirs(self.configPath)

        return True

    # copies example local config file
    # to users ~/.config/srvr location
    def __copyExample (self):

        src = self.configPath + self.exampleFileName
        dst = self.configPath + self.configFileName

        if self.app.debug:
            print "%s[*] Copying example config %s -> %s%s" % (Fore.BLUE, src, dst, Style.RESET_ALL)

        if copyfile(src, dst):
            return True

        return False

    def __parseConfigFile(self):

        if not self.parser.read(self.serviceConfig):
            raise Exception("Unable to read config: " + self.serviceConfig)

        return True

