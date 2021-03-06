import clr
clr.AddReference('RevitAPI')
from Autodesk.Revit.DB import *

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
path = IN[0]

if doc.IsFamilyDocument:
	path += '.rfa'
else:
	path += '.rvt'
OUT = doc.SaveAs(path)