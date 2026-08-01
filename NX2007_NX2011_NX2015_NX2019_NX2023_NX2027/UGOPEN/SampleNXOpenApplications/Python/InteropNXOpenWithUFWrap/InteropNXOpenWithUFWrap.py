import NXOpen
import NXOpen.UF


theSession = NXOpen.Session.GetSession()

theUFSession = NXOpen.UF.UFSession.GetUFSession()

try:
    myPart = theSession.Parts.NewDisplay("InteropNXOpenWithUFWrap", NXOpen.Part.Units.Millimeters)
    part = myPart.Tag

    name = theUFSession.Part.AskPartName(part)

    point3d1 = NXOpen.Point3d(-2.45197396411307, 3.58206319143819, 0.0)
    point3d2 = NXOpen.Point3d(5.32514590979158, -1.0012853802839, 0.0)
    line1 = theSession.Parts.Work.Curves.CreateLine(point3d1, point3d2)
    uf_curve = theUFSession.Curve
    line_coords = theUFSession.Curve.AskLineData(line1.Tag)

    arc_coords = NXOpen.UF.Curve.Arc()

    arc_coords.StartAngle = 0.0
    arc_coords.EndAngle = 3.0
    arc_coords.ArcCenter.append(0.0)
    arc_coords.ArcCenter.append(0.0)
    arc_coords.ArcCenter.append(1.0)
    arc_coords.Radius = 2.0

    wcs_tag = theUFSession.Csys.AskWcs()
    arc_coords.MatrixTag = theUFSession.Csys.AskMatrixOfObject(wcs_tag)
    arc_tag = theUFSession.Curve.CreateArc(arc_coords)
    
    tagged_object_manager = NXOpen.TaggedObjectManager()
    NXArc = tagged_object_manager.GetTaggedObject(arc_tag)

    start_angle = NXArc.StartAngle
    end_angle = NXArc.EndAngle
    arc_center = NXArc.CenterPoint

    theUFSession.Part.Save()
except NXOpen.NXException as e:
    print("Exception is: {0}".format(e.ErrorMessage))

