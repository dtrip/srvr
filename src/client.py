
from cement.core import controller
# import Srvr
import Authenticate as auth

class Client(controller.CementBaseController):
    class Meta:
        label = 'client'
        stacked_on = 'SrvrBase'

    @expose(hide=True)
    def init(self):

        # self.connect();
        pass

    @expose(hide=False)
    def connect(self):
        self.app.log.info("Logging info about app")
