
from cement.core.controller import CementBaseController, expose

class SrvrBase(CementBaseController):
    class Meta:
        label = 'Base'
        description = "Receive real time custom updates from your server via socket"
        # self.config = config()
        arguments = [
                (['-d', '--debug'], dict(action='store_false', help='Enable debugging')),
                (['-H', '--host'], dict(action='store', help='Server hostname or IP address')),
                (['-p', '--port'], dict(action='store', help='Port for server to listen on')),
                (['-s', '--server'], dict(action='store', help='Start server instance'))
                ]


    @expose(hide=True)
    def default(self):
        self.app.log.info("Test")

    @expose(hide=True)
    def client(self):
        pass
