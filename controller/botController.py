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

from docxtpl import DocxTemplate
import falcon
import uuid
from datetime import datetime
from bson import json_util
from commons.jsonconfig import JsonConfig
import simplejson as json
from commons.loggy import set_up_logging
from commons.utils import Utils
logger = set_up_logging("botController")
config = JsonConfig("app.config")



# -----------------------------------------------------
# Singleton class for
# -----------------------------------------------------
class botController(object):

    def on_get(self, req, resp):
        try:
            logger.info(req.context)
            
            doc = {
                'success': "True",
                'message': "Zoom meetings retrieved successfully",
                'data' : []
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
            loginurl = req.json['loginurl']
            username = req.json['username']
            password = req.json['password']
            botController.make_zoom_invitation(loginurl,username,password)

            doc = {
                'success': True,
                'message': "Zoom meeting has been scheduled successfully"
               
            }
            resp.status = falcon.HTTP_200
        except Exception as e:
            doc = {
                'success': False,
                'message': str(e)}
            resp.status = falcon.HTTP_500
        resp.media = doc
        resp.content_type = falcon.MEDIA_JSON

    def make_zoom_invitation(loginurl,username, password):
        logger.info("Inside make_zoom_invitation")
        logger.info(config.params["zynomi"]["host"])
        
        try:
            from playwright.sync_api import sync_playwright

            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False, slow_mo=5)
                page = browser.new_page()
                page.goto(loginurl)
                page.fill('input#email',username)
                page.fill('input#password',password)
                page.click('button:has-text("Sign In")') 
                page.is_visible('div.content-body')    
                page.wait_for_load_state()
                page.screenshot(path="my-zoom-home.png")
                page.click('#btnScheduleMeeting')
                page.wait_for_load_state()
                page.fill('input#topic','Weekly sync-up meeting with zypress team')
                
                page.click("[placeholder=\"select date\"]")
                # Click [aria-label="January 24 2022 Monday"]
                page.click("[aria-label=\"January 17 2022 Monday\"]")
                # Click [placeholder="select"]
                page.click("[placeholder=\"select\"]")
                # Click :nth-match(:text("09:30"), 2)
                page.click(":nth-match(:text(\"08:30\"), 2)")
                # Click text=PM
                page.click("text=PM")
                # Click :nth-match(:text("PM"), 3)
                page.click(":nth-match(:text(\"PM\"), 3)")
                page.screenshot(path="my-zoom-schedule.png")
                page.locator('span:has-text("Save")').click()
                browser.close() 
        except Exception as e:
            return str(e)