import os

# -----------------------------------------------------
# Singleton class for configuration manager instance creations
# -----------------------------------------------------
class Utils(object):
    __instance = None

    def ensure_dir(file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)