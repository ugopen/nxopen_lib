from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class ArcMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Arc Measurement.
    """
    pass
class CircleMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Circle Measurement.
    """
    pass
class ConeMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Cone Measurement.
    """
    pass
class CurveMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Curve Measurement.
    """
    pass
class CylinderMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Cylinder Measurement.
    """
    pass
class ExtremePointMeasurement(PointMeasurement): 
    """
        Represents the base class for an Contactless Inspection Point Measurement.
    """
    pass
import NXOpen
class InspectionElement(NXOpen.NXObject): 
    """
        Represents the base class for an Inspection Element.
    """
    pass
import NXOpen
class InspectionGroupBuilder(NXOpen.Builder): 
    """ The builder class to create\edit ContactlessInspection.InspectionGroup"""
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information for the created\edited  ContactlessInspection::InspectionGroup    
            
         
        """
        pass
class InspectionGroup(InspectionElement): 
    """
        Represents the class for an Contactless Inspection Group.
    """
    pass
class LineMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Line Measurement.
    """
    pass
import NXOpen
class MeasureConeSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit ContactlessInspection.ConeMeasurement"""
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information for the created\edited  ContactlessInspection::ConeMeasurement    
            
         
        """
        pass
    @property
    def NominalCone(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) NominalCone
         Returns the nominal cone(s) defining the  ContactlessInspection::ConeMeasurement    
            
         
        """
        pass
import NXOpen
class MeasureCylinderSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit ContactlessInspection.CylinderMeasurement"""
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information for the created\edited  ContactlessInspection::CylinderMeasurement    
            
         
        """
        pass
    @property
    def NominalCylinder(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) NominalCylinder
         Returns the nominal cylinder(s) defining the  ContactlessInspection::CylinderMeasurement    
            
         
        """
        pass
import NXOpen
class MeasureExtremePointBuilder(NXOpen.Builder): 
    """  The builder class to createedit a ContactlessInspection.ExtremePointMeasurement object in Contactless Inspection Application.  
     Use  ContactlessInspection.Manager.CreateMeasureExtremePointBuilder to create this object  """
    @property
    def MeasurementDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    @MeasurementDirection.setter
    def MeasurementDirection(self, measurementDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    @property
    def NominalPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
    @NominalPoint.setter
    def NominalPoint(self, nominalPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
    @property
    def SectionPlaneNormal(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SectionPlaneNormal
         Returns the section plane normal to be used to create the actual section   
            
         
        """
        pass
    @SectionPlaneNormal.setter
    def SectionPlaneNormal(self, sectionPlaneNormal: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SectionPlaneNormal
         Returns the section plane normal to be used to create the actual section   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class MeasurementInformation(NXOpen.TaggedObject): 
    """ Represents the information related to the measurement like the Measurement's group and label """
    @property
    def InspectionGroup(self) -> str:
        """
        Getter for property: (str) InspectionGroup
         Returns the inspection group of the Measurement or Inspecton Group.  
           This defines the  ContactlessInspection::InspectionGroup  that the 
                 ContactlessInspection::Measurement  or  ContactlessInspection::InspectionGroup  will be the member of.  
         
        """
        pass
    @InspectionGroup.setter
    def InspectionGroup(self, inspectionGroup: str):
        """
        Setter for property: (str) InspectionGroup
         Returns the inspection group of the Measurement or Inspecton Group.  
           This defines the  ContactlessInspection::InspectionGroup  that the 
                 ContactlessInspection::Measurement  or  ContactlessInspection::InspectionGroup  will be the member of.  
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label of the  ContactlessInspection::Measurement   
            
         
        """
        pass
    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
         Returns the label of the  ContactlessInspection::Measurement   
            
         
        """
        pass
    def GetAllInspectionGroupsNames(self) -> List[str]:
        """
         Get all the ContactlessInspection.InspectionGroup in part
         Returns inspectionGroupNames (List[str]): The array of Inspection Groups Names.
        """
        pass
class Measurement(InspectionElement): 
    """
        Represents the base class for an Contactless Inspection Measurement.
    """
    pass
import NXOpen
class MeasurePlaneSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit ContactlessInspection.PlaneMeasurement"""
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information for the created\edited  ContactlessInspection::PlaneMeasurement    
            
         
        """
        pass
    @property
    def NominalPlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) NominalPlane
         Returns the nominal plane(s) defining the  ContactlessInspection::PlaneMeasurement    
            
         
        """
        pass
import NXOpen
class MeasurePrimitiveSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit Primitive Surface Measurements"""
    class Types(Enum):
        """
        Members Include: 
         |Plane| Creates a measurement of type ContactlessInspection.PlaneMeasurement
         |Sphere| Creates a measurement of type ContactlessInspection.SphereMeasurement
         |Cylinder| Creates a measurement of type ContactlessInspection.CylinderMeasurement
         |Cone| Creates a measurement of type ContactlessInspection.ConeMeasurement

        """
        Plane: int
        Sphere: int
        Cylinder: int
        Cone: int
        @staticmethod
        def ValueOf(value: int) -> MeasurePrimitiveSurfaceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConeMeasurement(self) -> MeasureConeSurfaceBuilder:
        """
        Getter for property: ( MeasureConeSurfaceBuilder NXOpen.Contac) ConeMeasurement
         Returns the data for creating cone measurement  
            
         
        """
        pass
    @property
    def CylinderMeasurement(self) -> MeasureCylinderSurfaceBuilder:
        """
        Getter for property: ( MeasureCylinderSurfaceBuilder NXOpen.Contac) CylinderMeasurement
         Returns the data for creating cylinder measurement  
            
         
        """
        pass
    @property
    def PlaneMeasurement(self) -> MeasurePlaneSurfaceBuilder:
        """
        Getter for property: ( MeasurePlaneSurfaceBuilder NXOpen.Contac) PlaneMeasurement
         Returns the data for creating plane measurement  
            
         
        """
        pass
    @property
    def SphereMeasurement(self) -> MeasureSphereSurfaceBuilder:
        """
        Getter for property: ( MeasureSphereSurfaceBuilder NXOpen.Contac) SphereMeasurement
         Returns the data for creating sphere measurement  
            
         
        """
        pass
    @property
    def Type(self) -> MeasurePrimitiveSurfaceBuilder.Types:
        """
        Getter for property: ( MeasurePrimitiveSurfaceBuilder.Types NXOpen.Contac) Type
         Returns the type of  ContactlessInspection::PrimitiveSurfaceMeasurement  desired  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: MeasurePrimitiveSurfaceBuilder.Types):
        """
        Setter for property: ( MeasurePrimitiveSurfaceBuilder.Types NXOpen.Contac) Type
         Returns the type of  ContactlessInspection::PrimitiveSurfaceMeasurement  desired  
            
         
        """
        pass
import NXOpen
class MeasureSphereSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit ContactlessInspection.SphereMeasurement"""
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information for the created\edited  ContactlessInspection::SphereMeasurement    
            
         
        """
        pass
    @property
    def NominalSphere(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) NominalSphere
         Returns the nominal sphere(s) defining the  ContactlessInspection::SphereMeasurement    
            
         
        """
        pass
import NXOpen
class MeasureSurfaceBuilder(NXOpen.Builder): 
    """  The builder class to create\edit a ContactlessInspection.SurfaceMeasurement object in Contactless Inspection Application.  
         Use  ContactlessInspection.Manager.CreateMeasureSurfaceBuilder to create this object  """
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    @property
    def NominalSurface(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) NominalSurface
         Returns the nominal surface belonging to the nominal body  
            
         
        """
        pass
import NXOpen
class MeasureSurfacePointBuilder(NXOpen.Builder): 
    """  The builder class to createedit a ContactlessInspection.SurfacePointMeasurement object in Contactless Inspection Application.  
     Use  ContactlessInspection.Manager.CreateMeasureSurfacePointBuilder to create this object  """
    @property
    def MeasurementDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    @MeasurementDirection.setter
    def MeasurementDirection(self, measurementDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    @property
    def NominalPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
    @NominalPoint.setter
    def NominalPoint(self, nominalPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
import NXOpen
class MeasureSymmetryPointBuilder(NXOpen.Builder): 
    """  The builder class to createedit a ContactlessInspection.SymmetryPointMeasurement object in Contactless Inspection Application.  
     Use  ContactlessInspection.Manager.CreateMeasureSymmetryPointBuilder to create this object  """
    class Point2Types(Enum):
        """
        Members Include: 
         |Measured| 
         |Fixed| 

        """
        Measured: int
        Fixed: int
        @staticmethod
        def ValueOf(value: int) -> MeasureSymmetryPointBuilder.Point2Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: ( MeasurementInformation NXOpen.Contac) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    @property
    def Point1Measurement(self) -> SelectPointMeasurement:
        """
        Getter for property: ( SelectPointMeasurement NXOpen.Contac) Point1Measurement
         Returns the first point measurement of type point, arc, circle, or sphere measurement   
            
         
        """
        pass
    @property
    def Point2Fixed(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point2Fixed
         Returns the nominal point for second point   
            
         
        """
        pass
    @Point2Fixed.setter
    def Point2Fixed(self, point2Fixed: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point2Fixed
         Returns the nominal point for second point   
            
         
        """
        pass
    @property
    def Point2Measurement(self) -> SelectPointMeasurement:
        """
        Getter for property: ( SelectPointMeasurement NXOpen.Contac) Point2Measurement
         Returns the second point measurement of type point, arc, circle, or sphere measurement  
            
         
        """
        pass
    @property
    def Point2Type(self) -> MeasureSymmetryPointBuilder.Point2Types:
        """
        Getter for property: ( MeasureSymmetryPointBuilder.Point2Types NXOpen.Contac) Point2Type
         Returns the second point measurement type for symmetry point measurement  
            
         
        """
        pass
    @Point2Type.setter
    def Point2Type(self, point2Type: MeasureSymmetryPointBuilder.Point2Types):
        """
        Setter for property: ( MeasureSymmetryPointBuilder.Point2Types NXOpen.Contac) Point2Type
         Returns the second point measurement type for symmetry point measurement  
            
         
        """
        pass
class PlaneMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Plane Measurement.
    """
    pass
class PointMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Point Measurement.
    """
    pass
class PrimitiveCurveMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Primitive Curve Measurements.
    """
    pass
class PrimitiveSurfaceMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Primitive Surface Measurements.
    """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectPointMeasurement(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> PointMeasurement:
        """
        Getter for property: ( PointMeasurement NXOpen.Contac) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: PointMeasurement):
        """
        Setter for property: ( PointMeasurement NXOpen.Contac) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[PointMeasurement, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  PointMeasurement NXOpen.Contac. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, PointMeasurement, NXOpen.View, NXOpen.Point3d, PointMeasurement, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  PointMeasurement NXOpen.Contac. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  PointMeasurement NXOpen.Contac. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[PointMeasurement, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  PointMeasurement NXOpen.Contac. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: PointMeasurement, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: PointMeasurement, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: PointMeasurement, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: PointMeasurement, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
class SphereMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Sphere Measurement.
    """
    pass
class SurfaceMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Surface Measurements.
    """
    pass
class SurfacePointMeasurement(PointMeasurement): 
    """
        Represents the base class for an Contactless Inspection Surface Point Measurement.
    """
    pass
class SymmetryPointMeasurement(PointMeasurement): 
    """
        Represents the base class for an Contactless Inspection Point Measurement.
    """
    pass
