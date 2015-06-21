
# import Srvr
import os
from cement.core import controller
from Crypto.PublicKey import RSA
from Crypto import Random

class Authenticate(controller.CementBaseController):
    class Meta:
        label = 'authenticate'
        # stacked_on = 'Base'

    def sshKey(self):
        pass
