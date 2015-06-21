
import Srvr
import Authenticate as auth

class Client(CementApp):
    class Meta:
        label = 'client'
        stacked_on = 'base'

    @expose(hide=True)
    def init(self):

        self.connect();


        return False

    @expose(hide=True)
    def connect(self):
    
        return False
