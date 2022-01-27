# -----------------------------------------------------
#
#
# -----------------------------------------------------
# {Modification Log}
# -----------------------------------------------------
# Author: {author}
# Maintainer: {maintainer}
# Created At:
# Last Modified:
# Status: {dev_status}
# -----------------------------------------------------

import os
import json


# -----------------------------------------------------
# Singleton class for configuration manager instance creations
# -----------------------------------------------------
class JsonConfig(object):
    __instance = None

    # -----------------------------------------------------
    #
    # -----------------------------------------------------
    def __new__(cls, val):
        if JsonConfig.__instance is None:
            app_root_folder = os.path.abspath(os.curdir)
            JsonConfig.__instance = object.__new__(cls)
            with open(app_root_folder + "/data/config/" + val) as json_file:
                JsonConfig.__instance.params = json.load(json_file)
        return JsonConfig.__instance

