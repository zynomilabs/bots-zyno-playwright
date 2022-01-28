import os
import pandas as pd


# -----------------------------------------------------
# Singleton class for configuration manager instance creations
# -----------------------------------------------------
class Utils(object):
    __instance = None

    def ensure_dir(file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def read_excel(file_path):
        df = pd.read_excel(file_path,index_col=0,engine='openpyxl')
        return df