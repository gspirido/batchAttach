import arcpy
import pythonaddins
import os

class BatchAttach(object):
    """Implementation for BatchAttach_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
		#load and run toolbox
		tbxPath = os.path.join(os.path.dirname(__file__), "scripts.tbx")
		pythonaddins.GPToolDialog(tbxPath, "BatchAttach");