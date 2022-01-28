# -----------------------------------------------------
# This class creates the repository a.k.a. data access class
# at runtime.
# -----------------------------------------------------
# {Modification Log}
# -----------------------------------------------------
# Author: {author}
# Maintainer: {maintainer}
# Created At:
# Last Modified:
# Status: {dev_status}
# -----------------------------------------------------

import json
import pandas as pd
import json

from docxtpl import DocxTemplate
import falcon
import uuid
from datetime import datetime
from bson import json_util
from commons.jsonconfig import JsonConfig
import simplejson as json
from commons.loggy import set_up_logging
from commons.utils import Utils
logger = set_up_logging("docxController")
config = JsonConfig("app.config")



# -----------------------------------------------------
# Singleton class for
# -----------------------------------------------------
class docxController(object):

    def on_get_ping(self, req, resp):
        try:
            logger.info(req.context)
            doc = {
                'message': "Pong"
            }
            resp.status = falcon.HTTP_200
        except Exception as e:
            doc = {
                'success': False,
                'message': str(e)}
            resp.status = falcon.HTTP_500

        finally:    
            resp.media = doc
            resp.content_type = falcon.MEDIA_JSON
    
    def on_get_students(self, req, resp):
        try:
            logger.info(req.context)
            df = Utils.read_excel('/opt/senthilnathan/bots-zyno-playwright/students.xlsx')

            doc = df.to_json(orient="records")
            resp.status = falcon.HTTP_200
        except Exception as e:
            doc = {
                'success': False,
                'message': str(e)}
            resp.status = falcon.HTTP_500

        finally:    
            resp.media = doc
            resp.content_type = falcon.MEDIA_JSON

    def on_get(self, req, resp):
        try:
            logger.info(req.context)
            doc = {
                'success': "True",
                'message': "Data Extraction was successful",
                'data': json.loads(json.dumps('{"Connections" : "Oracle"}', default=json_util.default))
            }
            resp.status = falcon.HTTP_200
        except Exception as e:
            doc = {
                'success': False,
                'message': str(e)}
            resp.status = falcon.HTTP_500

        finally:    
            resp.media = doc
            resp.content_type = falcon.MEDIA_JSON
    # -----------------------------------------------------
    #
    # -----------------------------------------------------
    def on_post(self, req, resp):
        logger.info("Inside POST Method")
        try:
            body = req.stream.read()
            req.json = json.loads(body.decode('utf-8'))
            logger.info("req.media = " + json.dumps(req.json))
            user = req.json['user']
            tpl_file = req.json['template']['file']
            
            logger.info("File = " + "./data/templates/" + tpl_file)
            
            tpl = DocxTemplate("./data/templates/" + tpl_file)
         
            tpl.render(user)
            #Utils.ensure_dir("tmp")
            logger.info("Saving")
            output_filename = str(uuid.uuid4()) + '_' + datetime.utcnow().strftime("%Y%m%d%H%M%S") + '.docx'
            tpl.save('./data/output/' + output_filename)

            doc = {
                'success': True,
                'message': "Document generated successfully", #bring it from config
                'data': '{"output_file" : ' + output_filename + '}'
            }
            resp.status = falcon.HTTP_200
        except Exception as e:
            doc = {
                'success': False,
                'message': str(e)}
            resp.status = falcon.HTTP_500
        resp.media = doc
        resp.content_type = falcon.MEDIA_JSON
