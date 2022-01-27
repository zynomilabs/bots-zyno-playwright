import falcon
from wsgiref.simple_server import make_server
from commons.jsonconfig import JsonConfig
from commons.loggy import set_up_logging
from controller.docxController import docxController
#from controller.botController import botController

logger = set_up_logging()
config = JsonConfig("app.config")

app = falcon.App(cors_enable=True)
# Enable CORS policy for example.com and allows credentials
app = falcon.App(middleware=falcon.CORSMiddleware(
    allow_origins='example.com', allow_credentials='*'))
# Attach routes
app.add_route('/', docxController(), suffix='ping')
app.add_route('/export/doc', docxController())
#app.add_route('/schedule/zoom', botController())
