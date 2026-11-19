from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
## 
##         Represents the class for a Contactless Inspection Arc Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureArcBuilder  NXOpen::ContactlessInspection::MeasureArcBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ArcMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Arc Measurement.
    """
    pass


## 
##         Represents the class for a Contactless Inspection Circle Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureCircleBuilder  NXOpen::ContactlessInspection::MeasureCircleBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class CircleMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Circle Measurement.
    """
    pass


## 
##         Represents the class for a Contactless Inspection Cone Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureConeSurfaceBuilder  NXOpen::ContactlessInspection::MeasureConeSurfaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ConeMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Cone Measurement.
    """
    pass


## 
##         Represents the class for a Contactless Inspection Curve Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureCurveBuilder  NXOpen::ContactlessInspection::MeasureCurveBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class CurveMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Curve Measurement.
    """
    pass


## 
##         Represents the class for a Contactless Inspection Cylinder Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureCylinderSurfaceBuilder  NXOpen::ContactlessInspection::MeasureCylinderSurfaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class CylinderMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Cylinder Measurement.
    """
    pass


## 
##         Represents the base class for an Contactless Inspection Point Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureExtremePointBuilder  NXOpen::ContactlessInspection::MeasureExtremePointBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ExtremePointMeasurement(PointMeasurement): 
    """
        Represents the base class for an Contactless Inspection Point Measurement.
    """
    pass


import NXOpen
## 
##         Represents the base class for an Inspection Element.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class InspectionElement(NXOpen.NXObject): 
    """
        Represents the base class for an Inspection Element.
    """
    pass


import NXOpen
##  The builder class to create\edit @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateInspectionGroupBuilder  NXOpen::ContactlessInspection::Manager::CreateInspectionGroupBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class InspectionGroupBuilder(NXOpen.Builder): 
    """ The builder class to create\edit <ja_class>ContactlessInspection.InspectionGroup</ja_class>"""


    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information for the created\edited @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information for the created\edited @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink    
            
         
        """
        pass
    
## 
##         Represents the class for an Contactless Inspection Group.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::InspectionGroupBuilder  NXOpen::ContactlessInspection::InspectionGroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class InspectionGroup(InspectionElement): 
    """
        Represents the class for an Contactless Inspection Group.
    """
    pass


## 
##         Represents the class for a Contactless Inspection Line Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureLineBuilder  NXOpen::ContactlessInspection::MeasureLineBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class LineMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Line Measurement.
    """
    pass


import NXOpen
##  The builder class to create\edit @link ContactlessInspection::ConeMeasurement ContactlessInspection::ConeMeasurement@endlink  <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasureConeSurfaceBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasureConeSurfaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasureConeSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit <ja_class>ContactlessInspection.ConeMeasurement</ja_class>"""


    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information for the created\edited @link ContactlessInspection::ConeMeasurement ContactlessInspection::ConeMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information for the created\edited @link ContactlessInspection::ConeMeasurement ContactlessInspection::ConeMeasurement@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalCone
    ##  Returns the nominal cone(s) defining the @link ContactlessInspection::ConeMeasurement ContactlessInspection::ConeMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def NominalCone(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalCone
         Returns the nominal cone(s) defining the @link ContactlessInspection::ConeMeasurement ContactlessInspection::ConeMeasurement@endlink    
            
         
        """
        pass
    
import NXOpen
##  The builder class to create\edit @link ContactlessInspection::CylinderMeasurement ContactlessInspection::CylinderMeasurement@endlink  <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasureCylinderSurfaceBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasureCylinderSurfaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasureCylinderSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit <ja_class>ContactlessInspection.CylinderMeasurement</ja_class>"""


    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information for the created\edited @link ContactlessInspection::CylinderMeasurement ContactlessInspection::CylinderMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information for the created\edited @link ContactlessInspection::CylinderMeasurement ContactlessInspection::CylinderMeasurement@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalCylinder
    ##  Returns the nominal cylinder(s) defining the @link ContactlessInspection::CylinderMeasurement ContactlessInspection::CylinderMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def NominalCylinder(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalCylinder
         Returns the nominal cylinder(s) defining the @link ContactlessInspection::CylinderMeasurement ContactlessInspection::CylinderMeasurement@endlink    
            
         
        """
        pass
    
import NXOpen
##   @brief  The builder class to create/edit a @link ContactlessInspection::ExtremePointMeasurement ContactlessInspection::ExtremePointMeasurement@endlink  object in Contactless Inspection Application.  
## 
##   
##      Use <method> ContactlessInspection.Manager.CreateMeasureExtremePointBuilder</method> to create this object   <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasureExtremePointBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasureExtremePointBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasureExtremePointBuilder(NXOpen.Builder): 
    """ <summary> The builder class to create/edit a <ja_class>ContactlessInspection.ExtremePointMeasurement</ja_class> object in Contactless Inspection Application. </summary> 
    <remarks> Use <method> ContactlessInspection.Manager.CreateMeasureExtremePointBuilder</method> to create this object </remarks> """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection
    ##  Returns the measurement direction in which the actual point will be detected  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def MeasurementDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection

    ##  Returns the measurement direction in which the actual point will be detected  
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MeasurementDirection.setter
    def MeasurementDirection(self, measurementDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    
    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information related to the measurment like the Measurment's group and label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint
    ##  Returns the nominal point used for measuring the actual point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def NominalPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint

    ##  Returns the nominal point used for measuring the actual point   
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NominalPoint.setter
    def NominalPoint(self, nominalPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionPlaneNormal
    ##  Returns the section plane normal to be used to create the actual section   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def SectionPlaneNormal(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionPlaneNormal
         Returns the section plane normal to be used to create the actual section   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionPlaneNormal

    ##  Returns the section plane normal to be used to create the actual section   
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SectionPlaneNormal.setter
    def SectionPlaneNormal(self, sectionPlaneNormal: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) SectionPlaneNormal
         Returns the section plane normal to be used to create the actual section   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents the information related to the measurement like the Measurement's group and label 
## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasurementInformation(NXOpen.TaggedObject): 
    """ Represents the information related to the measurement like the Measurement's group and label """


    ## Getter for property: (str) InspectionGroup
    ##  Returns the inspection group of the Measurement or Inspecton Group.  
    ##    This defines the @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  that the 
    ##         @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink  or @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  will be the member of.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def InspectionGroup(self) -> str:
        """
        Getter for property: (str) InspectionGroup
         Returns the inspection group of the Measurement or Inspecton Group.  
           This defines the @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  that the 
                @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink  or @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  will be the member of.  
         
        """
        pass
    
    ## Setter for property: (str) InspectionGroup

    ##  Returns the inspection group of the Measurement or Inspecton Group.  
    ##    This defines the @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  that the 
    ##         @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink  or @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  will be the member of.  
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @InspectionGroup.setter
    def InspectionGroup(self, inspectionGroup: str):
        """
        Setter for property: (str) InspectionGroup
         Returns the inspection group of the Measurement or Inspecton Group.  
           This defines the @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  that the 
                @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink  or @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  will be the member of.  
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##  Returns the label of the @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label of the @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink   
            
         
        """
        pass
    
    ## Setter for property: (str) Label

    ##  Returns the label of the @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink   
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Label.setter
    def Label(self, label: str):
        """
        Setter for property: (str) Label
         Returns the label of the @link ContactlessInspection::Measurement ContactlessInspection::Measurement@endlink   
            
         
        """
        pass
    
    ##  Get all the @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  in part
    ##  @return inspectionGroupNames (List[str]): The array of Inspection Groups Names.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetAllInspectionGroupsNames(self) -> List[str]:
        """
         Get all the @link ContactlessInspection::InspectionGroup ContactlessInspection::InspectionGroup@endlink  in part
         @return inspectionGroupNames (List[str]): The array of Inspection Groups Names.
        """
        pass
    
## 
##         Represents the base class for an Contactless Inspection Measurement.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Measurement(InspectionElement): 
    """
        Represents the base class for an Contactless Inspection Measurement.
    """
    pass


import NXOpen
##  The builder class to create\edit @link ContactlessInspection::PlaneMeasurement ContactlessInspection::PlaneMeasurement@endlink  <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasurePlaneSurfaceBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasurePlaneSurfaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasurePlaneSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit <ja_class>ContactlessInspection.PlaneMeasurement</ja_class>"""


    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information for the created\edited @link ContactlessInspection::PlaneMeasurement ContactlessInspection::PlaneMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information for the created\edited @link ContactlessInspection::PlaneMeasurement ContactlessInspection::PlaneMeasurement@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalPlane
    ##  Returns the nominal plane(s) defining the @link ContactlessInspection::PlaneMeasurement ContactlessInspection::PlaneMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def NominalPlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalPlane
         Returns the nominal plane(s) defining the @link ContactlessInspection::PlaneMeasurement ContactlessInspection::PlaneMeasurement@endlink    
            
         
        """
        pass
    
import NXOpen
##  The builder class to create\edit Primitive Surface Measurements <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasurePrimitiveSurfaceBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasurePrimitiveSurfaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConeMeasurement.MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## CylinderMeasurement.MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## PlaneMeasurement.MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## SphereMeasurement.MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasurePrimitiveSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit Primitive Surface Measurements"""


    ##  The enum defining the types of Primitive Surface Measurement
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Plane</term><description> 
    ## Creates a measurement of type @link ContactlessInspection::PlaneMeasurement ContactlessInspection::PlaneMeasurement@endlink </description> </item><item><term> 
    ## Sphere</term><description> 
    ## Creates a measurement of type @link ContactlessInspection::SphereMeasurement ContactlessInspection::SphereMeasurement@endlink </description> </item><item><term> 
    ## Cylinder</term><description> 
    ## Creates a measurement of type @link ContactlessInspection::CylinderMeasurement ContactlessInspection::CylinderMeasurement@endlink </description> </item><item><term> 
    ## Cone</term><description> 
    ## Creates a measurement of type @link ContactlessInspection::ConeMeasurement ContactlessInspection::ConeMeasurement@endlink </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Plane> <Sphere> <Cylinder> <Cone>
        """
        Plane: int
        Sphere: int
        Cylinder: int
        Cone: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeasurePrimitiveSurfaceBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link MeasureConeSurfaceBuilder NXOpen.ContactlessInspection.MeasureConeSurfaceBuilder@endlink) ConeMeasurement
    ##  Returns the data for creating cone measurement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasureConeSurfaceBuilder
    @property
    def ConeMeasurement(self) -> MeasureConeSurfaceBuilder:
        """
        Getter for property: (@link MeasureConeSurfaceBuilder NXOpen.ContactlessInspection.MeasureConeSurfaceBuilder@endlink) ConeMeasurement
         Returns the data for creating cone measurement  
            
         
        """
        pass
    
    ## Getter for property: (@link MeasureCylinderSurfaceBuilder NXOpen.ContactlessInspection.MeasureCylinderSurfaceBuilder@endlink) CylinderMeasurement
    ##  Returns the data for creating cylinder measurement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasureCylinderSurfaceBuilder
    @property
    def CylinderMeasurement(self) -> MeasureCylinderSurfaceBuilder:
        """
        Getter for property: (@link MeasureCylinderSurfaceBuilder NXOpen.ContactlessInspection.MeasureCylinderSurfaceBuilder@endlink) CylinderMeasurement
         Returns the data for creating cylinder measurement  
            
         
        """
        pass
    
    ## Getter for property: (@link MeasurePlaneSurfaceBuilder NXOpen.ContactlessInspection.MeasurePlaneSurfaceBuilder@endlink) PlaneMeasurement
    ##  Returns the data for creating plane measurement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurePlaneSurfaceBuilder
    @property
    def PlaneMeasurement(self) -> MeasurePlaneSurfaceBuilder:
        """
        Getter for property: (@link MeasurePlaneSurfaceBuilder NXOpen.ContactlessInspection.MeasurePlaneSurfaceBuilder@endlink) PlaneMeasurement
         Returns the data for creating plane measurement  
            
         
        """
        pass
    
    ## Getter for property: (@link MeasureSphereSurfaceBuilder NXOpen.ContactlessInspection.MeasureSphereSurfaceBuilder@endlink) SphereMeasurement
    ##  Returns the data for creating sphere measurement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasureSphereSurfaceBuilder
    @property
    def SphereMeasurement(self) -> MeasureSphereSurfaceBuilder:
        """
        Getter for property: (@link MeasureSphereSurfaceBuilder NXOpen.ContactlessInspection.MeasureSphereSurfaceBuilder@endlink) SphereMeasurement
         Returns the data for creating sphere measurement  
            
         
        """
        pass
    
    ## Getter for property: (@link MeasurePrimitiveSurfaceBuilder.Types NXOpen.ContactlessInspection.MeasurePrimitiveSurfaceBuilder.Types@endlink) Type
    ##  Returns the type of @link ContactlessInspection::PrimitiveSurfaceMeasurement ContactlessInspection::PrimitiveSurfaceMeasurement@endlink  desired  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurePrimitiveSurfaceBuilder.Types
    @property
    def Type(self) -> MeasurePrimitiveSurfaceBuilder.Types:
        """
        Getter for property: (@link MeasurePrimitiveSurfaceBuilder.Types NXOpen.ContactlessInspection.MeasurePrimitiveSurfaceBuilder.Types@endlink) Type
         Returns the type of @link ContactlessInspection::PrimitiveSurfaceMeasurement ContactlessInspection::PrimitiveSurfaceMeasurement@endlink  desired  
            
         
        """
        pass
    
    ## Setter for property: (@link MeasurePrimitiveSurfaceBuilder.Types NXOpen.ContactlessInspection.MeasurePrimitiveSurfaceBuilder.Types@endlink) Type

    ##  Returns the type of @link ContactlessInspection::PrimitiveSurfaceMeasurement ContactlessInspection::PrimitiveSurfaceMeasurement@endlink  desired  
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Type.setter
    def Type(self, type: MeasurePrimitiveSurfaceBuilder.Types):
        """
        Setter for property: (@link MeasurePrimitiveSurfaceBuilder.Types NXOpen.ContactlessInspection.MeasurePrimitiveSurfaceBuilder.Types@endlink) Type
         Returns the type of @link ContactlessInspection::PrimitiveSurfaceMeasurement ContactlessInspection::PrimitiveSurfaceMeasurement@endlink  desired  
            
         
        """
        pass
    
import NXOpen
##  The builder class to create\edit @link ContactlessInspection::SphereMeasurement ContactlessInspection::SphereMeasurement@endlink  <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasureSphereSurfaceBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasureSphereSurfaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasureSphereSurfaceBuilder(NXOpen.Builder): 
    """ The builder class to create\edit <ja_class>ContactlessInspection.SphereMeasurement</ja_class>"""


    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information for the created\edited @link ContactlessInspection::SphereMeasurement ContactlessInspection::SphereMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information for the created\edited @link ContactlessInspection::SphereMeasurement ContactlessInspection::SphereMeasurement@endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalSphere
    ##  Returns the nominal sphere(s) defining the @link ContactlessInspection::SphereMeasurement ContactlessInspection::SphereMeasurement@endlink    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def NominalSphere(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalSphere
         Returns the nominal sphere(s) defining the @link ContactlessInspection::SphereMeasurement ContactlessInspection::SphereMeasurement@endlink    
            
         
        """
        pass
    
import NXOpen
##   @brief  The builder class to create\edit a @link ContactlessInspection::SurfaceMeasurement ContactlessInspection::SurfaceMeasurement@endlink  object in Contactless Inspection Application.  
## 
##   
##          Use <method> ContactlessInspection.Manager.CreateMeasureSurfaceBuilder</method> to create this object   <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasureSurfaceBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasureSurfaceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasureSurfaceBuilder(NXOpen.Builder): 
    """ <summary> The builder class to create\edit a <ja_class>ContactlessInspection.SurfaceMeasurement</ja_class> object in Contactless Inspection Application. </summary> 
        <remarks> Use <method> ContactlessInspection.Manager.CreateMeasureSurfaceBuilder</method> to create this object </remarks> """


    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information related to the measurment like the Measurment's group and label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalSurface
    ##  Returns the nominal surface belonging to the nominal body  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def NominalSurface(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) NominalSurface
         Returns the nominal surface belonging to the nominal body  
            
         
        """
        pass
    
import NXOpen
##   @brief  The builder class to create/edit a @link ContactlessInspection::SurfacePointMeasurement ContactlessInspection::SurfacePointMeasurement@endlink  object in Contactless Inspection Application.  
## 
##   
##      Use <method> ContactlessInspection.Manager.CreateMeasureSurfacePointBuilder</method> to create this object   <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasureSurfacePointBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasureSurfacePointBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasureSurfacePointBuilder(NXOpen.Builder): 
    """ <summary> The builder class to create/edit a <ja_class>ContactlessInspection.SurfacePointMeasurement</ja_class> object in Contactless Inspection Application. </summary> 
    <remarks> Use <method> ContactlessInspection.Manager.CreateMeasureSurfacePointBuilder</method> to create this object </remarks> """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection
    ##  Returns the measurement direction in which the actual point will be detected  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def MeasurementDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection

    ##  Returns the measurement direction in which the actual point will be detected  
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MeasurementDirection.setter
    def MeasurementDirection(self, measurementDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) MeasurementDirection
         Returns the measurement direction in which the actual point will be detected  
            
         
        """
        pass
    
    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information related to the measurment like the Measurment's group and label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint
    ##  Returns the nominal point used for measuring the actual point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def NominalPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint

    ##  Returns the nominal point used for measuring the actual point   
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NominalPoint.setter
    def NominalPoint(self, nominalPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) NominalPoint
         Returns the nominal point used for measuring the actual point   
            
         
        """
        pass
    
import NXOpen
##   @brief  The builder class to create/edit a @link ContactlessInspection::SymmetryPointMeasurement ContactlessInspection::SymmetryPointMeasurement@endlink  object in Contactless Inspection Application.  
## 
##   
##      Use <method> ContactlessInspection.Manager.CreateMeasureSymmetryPointBuilder</method> to create this object   <br> To create a new instance of this class, use @link NXOpen::ContactlessInspection::Manager::CreateMeasureSymmetryPointBuilder  NXOpen::ContactlessInspection::Manager::CreateMeasureSymmetryPointBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeasurementInformation.InspectionGroup </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## Point2Type </term> <description> 
##  
## Measured </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class MeasureSymmetryPointBuilder(NXOpen.Builder): 
    """ <summary> The builder class to create/edit a <ja_class>ContactlessInspection.SymmetryPointMeasurement</ja_class> object in Contactless Inspection Application. </summary> 
    <remarks> Use <method> ContactlessInspection.Manager.CreateMeasureSymmetryPointBuilder</method> to create this object </remarks> """


    ##  The enum to specify if the second point is a measured entity or a fixed (nominal) point for symmetry point measurement
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Measured</term><description> 
    ## </description> </item><item><term> 
    ## Fixed</term><description> 
    ## </description> </item></list>
    class Point2Types(Enum):
        """
        Members Include: <Measured> <Fixed>
        """
        Measured: int
        Fixed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeasureSymmetryPointBuilder.Point2Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
    ##  Returns the measurement information related to the measurment like the Measurment's group and label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasurementInformation
    @property
    def MeasurementInformation(self) -> MeasurementInformation:
        """
        Getter for property: (@link MeasurementInformation NXOpen.ContactlessInspection.MeasurementInformation@endlink) MeasurementInformation
         Returns the measurement information related to the measurment like the Measurment's group and label   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) Point1Measurement
    ##  Returns the first point measurement of type point, arc, circle, or sphere measurement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SelectPointMeasurement
    @property
    def Point1Measurement(self) -> SelectPointMeasurement:
        """
        Getter for property: (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) Point1Measurement
         Returns the first point measurement of type point, arc, circle, or sphere measurement   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2Fixed
    ##  Returns the nominal point for second point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point2Fixed(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2Fixed
         Returns the nominal point for second point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2Fixed

    ##  Returns the nominal point for second point   
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Point2Fixed.setter
    def Point2Fixed(self, point2Fixed: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2Fixed
         Returns the nominal point for second point   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) Point2Measurement
    ##  Returns the second point measurement of type point, arc, circle, or sphere measurement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SelectPointMeasurement
    @property
    def Point2Measurement(self) -> SelectPointMeasurement:
        """
        Getter for property: (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) Point2Measurement
         Returns the second point measurement of type point, arc, circle, or sphere measurement  
            
         
        """
        pass
    
    ## Getter for property: (@link MeasureSymmetryPointBuilder.Point2Types NXOpen.ContactlessInspection.MeasureSymmetryPointBuilder.Point2Types@endlink) Point2Type
    ##  Returns the second point measurement type for symmetry point measurement  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return MeasureSymmetryPointBuilder.Point2Types
    @property
    def Point2Type(self) -> MeasureSymmetryPointBuilder.Point2Types:
        """
        Getter for property: (@link MeasureSymmetryPointBuilder.Point2Types NXOpen.ContactlessInspection.MeasureSymmetryPointBuilder.Point2Types@endlink) Point2Type
         Returns the second point measurement type for symmetry point measurement  
            
         
        """
        pass
    
    ## Setter for property: (@link MeasureSymmetryPointBuilder.Point2Types NXOpen.ContactlessInspection.MeasureSymmetryPointBuilder.Point2Types@endlink) Point2Type

    ##  Returns the second point measurement type for symmetry point measurement  
    ##     
    ##  
    ## Setter License requirements: nx_contctles_inspect (" NX Contactless Inspection")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Point2Type.setter
    def Point2Type(self, point2Type: MeasureSymmetryPointBuilder.Point2Types):
        """
        Setter for property: (@link MeasureSymmetryPointBuilder.Point2Types NXOpen.ContactlessInspection.MeasureSymmetryPointBuilder.Point2Types@endlink) Point2Type
         Returns the second point measurement type for symmetry point measurement  
            
         
        """
        pass
    
## 
##         Represents the class for a Contactless Inspection Plane Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasurePlaneSurfaceBuilder  NXOpen::ContactlessInspection::MeasurePlaneSurfaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PlaneMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Plane Measurement.
    """
    pass


## 
##         Represents the base class for an Contactless Inspection Point Measurement.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PointMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Point Measurement.
    """
    pass


## 
##         Represents the base class for an Contactless Inspection Primitive Curve Measurements.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PrimitiveCurveMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Primitive Curve Measurements.
    """
    pass


## 
##         Represents the base class for an Contactless Inspection Primitive Surface Measurements.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PrimitiveSurfaceMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Primitive Surface Measurements.
    """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a single object selection.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectPointMeasurement(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink) Value
    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return PointMeasurement
    @property
    def Value(self) -> PointMeasurement:
        """
        Getter for property: (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink) Value

    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: PointMeasurement):
        """
        Setter for property: (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[PointMeasurement, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, PointMeasurement, NXOpen.View, NXOpen.Point3d, PointMeasurement, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[PointMeasurement, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) </param>
    ## <param name="selection"> (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def SetValue(self, selection: PointMeasurement, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  first selected object point</param>
    ## <param name="selection2"> (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink)  second selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: PointMeasurement, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: PointMeasurement, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::SetValue NXOpen::SelectObject::SetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPointMeasurement NXOpen.ContactlessInspection.SelectPointMeasurement@endlink) </param>
    ## <param name="selection"> (@link PointMeasurement NXOpen.ContactlessInspection.PointMeasurement@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def SetValue(self, selection: PointMeasurement, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
## 
##         Represents the class for a Contactless Inspection Sphere Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureSphereSurfaceBuilder  NXOpen::ContactlessInspection::MeasureSphereSurfaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SphereMeasurement(Measurement): 
    """
        Represents the class for a Contactless Inspection Sphere Measurement.
    """
    pass


## 
##         Represents the base class for an Contactless Inspection Surface Measurements.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureSurfaceBuilder  NXOpen::ContactlessInspection::MeasureSurfaceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SurfaceMeasurement(Measurement): 
    """
        Represents the base class for an Contactless Inspection Surface Measurements.
    """
    pass


## 
##         Represents the base class for an Contactless Inspection Surface Point Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureSurfacePointBuilder  NXOpen::ContactlessInspection::MeasureSurfacePointBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SurfacePointMeasurement(PointMeasurement): 
    """
        Represents the base class for an Contactless Inspection Surface Point Measurement.
    """
    pass


## 
##         Represents the base class for an Contactless Inspection Point Measurement.
##      <br> To create or edit an instance of this class, use @link NXOpen::ContactlessInspection::MeasureSymmetryPointBuilder  NXOpen::ContactlessInspection::MeasureSymmetryPointBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class SymmetryPointMeasurement(PointMeasurement): 
    """
        Represents the base class for an Contactless Inspection Point Measurement.
    """
    pass


## @package NXOpen.ContactlessInspection
## Classes, Enums and Structs under NXOpen.ContactlessInspection namespace

##  @link MeasurePrimitiveSurfaceBuilderTypes NXOpen.ContactlessInspection.MeasurePrimitiveSurfaceBuilderTypes @endlink is an alias for @link MeasurePrimitiveSurfaceBuilder.Types NXOpen.ContactlessInspection.MeasurePrimitiveSurfaceBuilder.Types@endlink
MeasurePrimitiveSurfaceBuilderTypes = MeasurePrimitiveSurfaceBuilder.Types


##  @link MeasureSymmetryPointBuilderPoint2Types NXOpen.ContactlessInspection.MeasureSymmetryPointBuilderPoint2Types @endlink is an alias for @link MeasureSymmetryPointBuilder.Point2Types NXOpen.ContactlessInspection.MeasureSymmetryPointBuilder.Point2Types@endlink
MeasureSymmetryPointBuilderPoint2Types = MeasureSymmetryPointBuilder.Point2Types


