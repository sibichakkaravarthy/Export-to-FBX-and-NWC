import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference('RevitAPI')
clr.AddReference('RevitAPIUI')
from Autodesk.Revit.DB import *
from Autodesk.Revit import DB
from Autodesk.Revit.UI import *

clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference('System')
from System.Collections.Generic import List
#The inputs to this node will be stored as a list in the IN variables.
dataEnteringNode = IN

doc = DocumentManager.Instance.CurrentDBDocument

solid = IN[0]
category = UnwrapElement(IN[1])
solidList = []
solidIds = []
catId = category.Id

TransactionManager.Instance.EnsureInTransaction(doc)

for i in range(len(solid)):
	ds = DirectShape.CreateElement(doc, catId)
	ds.SetShape(solid[i].ToRevitType())
	ds.Name = "Sibi Chakkaravarthy S"
	solidList.append(ds)
	solidIds.append(ds.Id)

TransactionManager.Instance.ForceCloseTransaction()

fileLoc = "C:/Users/Sibi Chakkaravarthy/Documents/Revi"
fileName = "sibi"
fileName1 = "sibi1.fbx"

#doc = __revit__.ActiveUIDocument.Document

doc1 = DocumentManager.Instance.CurrentDBDocument
#uidoc1 = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

export_ops = DB.FBXExportOptions()
views = DB.ViewSet()
# view must be a 3D view
views.Insert(DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument.ActiveGraphicalView)
#__revit__.ActiveUIDocument.ActiveGraphicalView

doc1.Export(fileLoc, fileName1, views, export_ops)

navOp = NavisworksExportOptions()
col1 = List[ElementId](solidIds)
navOp.SetSelectedElementIds(col1)
navOp.ExportScope = navOp.ExportScope.SelectedElements
navOp.ExportRoomGeometry = False
doc.Export(fileLoc, fileName, navOp)

TransactionManager.Instance.EnsureInTransaction(doc)
TransactionManager.Instance.TransactionTaskDone()

#Assign your output to the OUT variable.
OUT = solidIds
