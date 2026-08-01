from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class FaceAnnotationBuilder(NXOpen.Builder): 
    """ Builder for Face Annotation functionality used in formboard. It allows 
         importing CGM or Pattern file geometry and placing it on a drawing sheet
         or model view. As a result of this a group of dumb geometry is placed such
         that defined origin is located at the lower left hand of the bounding box 
         containing the group of geometry.
     """
    class DrwDestination(Enum):
        """
        Members Include: 
         |DrawingSheet|  Place geometry in drawing sheet 
         |Model|  Place geometry in model 

        """
        DrawingSheet: int
        Model: int
        @staticmethod
        def ValueOf(value: int) -> FaceAnnotationBuilder.DrwDestination:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |ComponentAttribute|  Import CGM file by selecting a component
         |CgmFileSelection|  Import CGM file by browsing a CGM file
         |PatternFileSelection|  Import a pattern file 

        """
        ComponentAttribute: int
        CgmFileSelection: int
        PatternFileSelection: int
        @staticmethod
        def ValueOf(value: int) -> FaceAnnotationBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CgmflBrsr(self) -> str:
        """
        Getter for property: (str) CgmflBrsr
         Returns the browser which enables selection of CGM file when  
                   Formboard::FaceAnnotationBuilder::Types  is  
                   Formboard::FaceAnnotationBuilder::TypesCgmFileSelection  .  
          
                  
         
        """
        pass
    @CgmflBrsr.setter
    def CgmflBrsr(self, filename: str):
        """
        Setter for property: (str) CgmflBrsr
         Returns the browser which enables selection of CGM file when  
                   Formboard::FaceAnnotationBuilder::Types  is  
                   Formboard::FaceAnnotationBuilder::TypesCgmFileSelection  .  
          
                  
         
        """
        pass
    @property
    def CompSel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) CompSel
         Returns the user selected component which has a CGM_FILE or PATTERN_FILE attribute defined.  
             
         
        """
        pass
    @property
    def DestEnum(self) -> FaceAnnotationBuilder.DrwDestination:
        """
        Getter for property: ( FaceAnnotationBuilder.DrwDestination NXOpen.) DestEnum
         Returns the   NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination   selected by
                    user to place the geometry   
            
         
        """
        pass
    @DestEnum.setter
    def DestEnum(self, destEnum: FaceAnnotationBuilder.DrwDestination):
        """
        Setter for property: ( FaceAnnotationBuilder.DrwDestination NXOpen.) DestEnum
         Returns the   NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination   selected by
                    user to place the geometry   
            
         
        """
        pass
    @property
    def PntOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PntOrigin
         Returns the user selected point where geometry will be placed   
            
         
        """
        pass
    @PntOrigin.setter
    def PntOrigin(self, pntOrigin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PntOrigin
         Returns the user selected point where geometry will be placed   
            
         
        """
        pass
    @property
    def StrAnnot(self) -> str:
        """
        Getter for property: (str) StrAnnot
         Returns the string to display the name of Pattern file name selected by user.  
             
         
        """
        pass
    @StrAnnot.setter
    def StrAnnot(self, strAnnot: str):
        """
        Setter for property: (str) StrAnnot
         Returns the string to display the name of Pattern file name selected by user.  
             
         
        """
        pass
    @property
    def StrAnnotFileName(self) -> str:
        """
        Getter for property: (str) StrAnnotFileName
         Returns the string to display the name of CGM name selected by user.  
            
         
        """
        pass
    @StrAnnotFileName.setter
    def StrAnnotFileName(self, strAnnot: str):
        """
        Setter for property: (str) StrAnnotFileName
         Returns the string to display the name of CGM name selected by user.  
            
         
        """
        pass
    @property
    def TogBlank(self) -> bool:
        """
        Getter for property: (bool) TogBlank
         Returns the toggle which defines whether the selected component is to be blanked or not   
            
         
        """
        pass
    @TogBlank.setter
    def TogBlank(self, togBlank: bool):
        """
        Setter for property: (bool) TogBlank
         Returns the toggle which defines whether the selected component is to be blanked or not   
            
         
        """
        pass
    @property
    def Type(self) -> FaceAnnotationBuilder.Types:
        """
        Getter for property: ( FaceAnnotationBuilder.Types NXOpen.) Type
         Returns the   NXOpen::Formboard::FaceAnnotationBuilder::Types  
                    selected by user   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: FaceAnnotationBuilder.Types):
        """
        Setter for property: ( FaceAnnotationBuilder.Types NXOpen.) Type
         Returns the   NXOpen::Formboard::FaceAnnotationBuilder::Types  
                    selected by user   
            
         
        """
        pass
import NXOpen
class FlipComponentBuilder(NXOpen.Builder): 
    """ Builder for flip component operation used in formboard.
        Allows user to flip the component by 180 degrees about an axis which is
        orthogonal to Z axis so that after flipping , the component lies in XY plane.
    """
    class AxisType(Enum):
        """
        Members Include: 
         |PathLocations|  Flip component by path locations
         |Custom|  Flip component by user defined custom axis 

        """
        PathLocations: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> FlipComponentBuilder.AxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AxisTypeEnum(self) -> FlipComponentBuilder.AxisType:
        """
        Getter for property: ( FlipComponentBuilder.AxisType NXOpen.) AxisTypeEnum
         Returns the user selected  NXOpen::Formboard::FlipComponentBuilder::AxisType  method   
            
         
        """
        pass
    @AxisTypeEnum.setter
    def AxisTypeEnum(self, axisTypeEnum: FlipComponentBuilder.AxisType):
        """
        Setter for property: ( FlipComponentBuilder.AxisType NXOpen.) AxisTypeEnum
         Returns the user selected  NXOpen::Formboard::FlipComponentBuilder::AxisType  method   
            
         
        """
        pass
    @property
    def CompSel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) CompSel
         Returns the formboard component selected by user for flipping operation   
            
         
        """
        pass
    @property
    def CustomAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) CustomAxis
         Returns the custom axis which is created when 
                     NXOpen::Formboard::FlipComponentBuilder::AxisType  is
                     NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom 
                  
            
         
        """
        pass
    @CustomAxis.setter
    def CustomAxis(self, customAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) CustomAxis
         Returns the custom axis which is created when 
                     NXOpen::Formboard::FlipComponentBuilder::AxisType  is
                     NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom 
                  
            
         
        """
        pass
    @property
    def PathAxisSel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) PathAxisSel
         Returns the axis selected by user about which selected formboard component 
                    will be flipped.  
          
                  
         
        """
        pass
    def CreateDatumAxis(self) -> List[NXOpen.NXObject]:
        """
         Creates datums axis at locations where selected formboard component 
                    is connected to path.
                
         Returns objects ( NXOpen.NXObject Li):  .
        """
        pass
    def FlipComponent(self) -> None:
        """
         Flips the selected formboard component by rotation angle 
                   about selected axis.
                
        """
        pass
    def InitializeFromComponent(self) -> None:
        """
         Initializes or resets ( start or stop ) drag operation based on the 
                   component selected for flipping operation.
                
        """
        pass
    def SetRotationAngle(self, angle: float) -> None:
        """
         Set the angle to rotate the component.
                
        """
        pass
    def StartDrag(self) -> None:
        """
         Starts the drag operation of selected object. Does nothing if drag has
                    already been started.
                
        """
        pass
    def StopDrag(self) -> None:
        """
         Stop the drag operation of selected object. Does nothing if drag has
                    not been started.
                
        """
        pass
import NXOpen
import NXOpen.Routing
class FormboardLayoutBuilder(NXOpen.Builder): 
    """ Class that performs the "layout" of Formboard geometry.  Creates all geometry
        chosen by the user to flatten into a drawing and orients the geometry to
        match the criteria specified in this builder class.   This builder must only
        be instantiated and used after the harnesses have been specified and stored
        using the NXOpen.Formboard.FormboardManager.StoreHarnessesToFlatten method. """
    class BranchAngle(Enum):
        """
        Members Include: 
         |AsDesigned|  Use the angle equal to the 3D angle
                                                                    of the branch in the 3D harness. 
         |StandardAngles|  Apply a standard angle to the branch,
                                                                    the level of the branch determines
                                                                    which angle to apply. 
         |MaximumAngles|  Apply the largest possible angle values
                                                                    at every branch to force the harness
                                                                    to spread out. 
         |RandomAngles|  Randomly choose an angle for each
                                                                    branch. 

        """
        AsDesigned: int
        StandardAngles: int
        MaximumAngles: int
        RandomAngles: int
        @staticmethod
        def ValueOf(value: int) -> FormboardLayoutBuilder.BranchAngle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BranchShape(Enum):
        """
        Members Include: 
         |Straight|  Each branch forms a straight line. 
         |Angled|  Branch becomes angled at each location
                                                                that forms a new branch. 

        """
        Straight: int
        Angled: int
        @staticmethod
        def ValueOf(value: int) -> FormboardLayoutBuilder.BranchShape:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MainRunType(Enum):
        """
        Members Include: 
         |Longest|  Path of longest wire. 
         |Thickest|  Path of longest wire contained within the
                                                                thickest bundle. 
         |UserSelection|  Manual selection of path. 

        """
        Longest: int
        Thickest: int
        UserSelection: int
        @staticmethod
        def ValueOf(value: int) -> FormboardLayoutBuilder.MainRunType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BranchAngleMethod(self) -> FormboardLayoutBuilder.BranchAngle:
        """
        Getter for property: ( FormboardLayoutBuilder.BranchAngle NXOpen.) BranchAngleMethod
         Returns the branch angle type.  
            Specifies how the layout algorithm determines the angle
                    between each child branch and its parent branch.    
         
        """
        pass
    @BranchAngleMethod.setter
    def BranchAngleMethod(self, branchAngle: FormboardLayoutBuilder.BranchAngle):
        """
        Setter for property: ( FormboardLayoutBuilder.BranchAngle NXOpen.) BranchAngleMethod
         Returns the branch angle type.  
            Specifies how the layout algorithm determines the angle
                    between each child branch and its parent branch.    
         
        """
        pass
    @property
    def BranchShapeType(self) -> FormboardLayoutBuilder.BranchShape:
        """
        Getter for property: ( FormboardLayoutBuilder.BranchShape NXOpen.) BranchShapeType
         Returns the branch shape type.  
             
         
        """
        pass
    @BranchShapeType.setter
    def BranchShapeType(self, branchShape: FormboardLayoutBuilder.BranchShape):
        """
        Setter for property: ( FormboardLayoutBuilder.BranchShape NXOpen.) BranchShapeType
         Returns the branch shape type.  
             
         
        """
        pass
    @property
    def LengthOptions(self) -> LayoutLengthOptions:
        """
        Getter for property: ( LayoutLengthOptions NXOpen.) LengthOptions
         Returns the length options for the layout operation.  
            The length options only have
                  any effect if this is the first time that the Formboard geometry is being
                  created in the drawing.   
         
        """
        pass
    @property
    def MainRunEndSelection(self) -> NXOpen.Routing.SelectControlPoint:
        """
        Getter for property: ( NXOpen.Routing.SelectControlPoint) MainRunEndSelection
         Returns the end of the main run.  
            Contains the ending control point 
                    that defines the main run of the Formboard if the 
                     NXOpen::Formboard::FormboardLayoutBuilder::MainRunType  is 
                     NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection .   
         
        """
        pass
    @property
    def MainRunMethod(self) -> FormboardLayoutBuilder.MainRunType:
        """
        Getter for property: ( FormboardLayoutBuilder.MainRunType NXOpen.) MainRunMethod
         Returns the main run method.  
             
         
        """
        pass
    @MainRunMethod.setter
    def MainRunMethod(self, mainRunType: FormboardLayoutBuilder.MainRunType):
        """
        Setter for property: ( FormboardLayoutBuilder.MainRunType NXOpen.) MainRunMethod
         Returns the main run method.  
             
         
        """
        pass
    @property
    def MainRunOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) MainRunOrigin
         Returns the main run origin.  
            The location in modeling space of the start 
                    of the main run. The layout operation translates the main run such 
                    that it start RCP is located at this location.   
         
        """
        pass
    @MainRunOrigin.setter
    def MainRunOrigin(self, mainRunOrigin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) MainRunOrigin
         Returns the main run origin.  
            The location in modeling space of the start 
                    of the main run. The layout operation translates the main run such 
                    that it start RCP is located at this location.   
         
        """
        pass
    @property
    def MainRunStartSelection(self) -> NXOpen.Routing.SelectControlPoint:
        """
        Getter for property: ( NXOpen.Routing.SelectControlPoint) MainRunStartSelection
         Returns the start of the main run.  
            Contains the starting control point 
                    that defines the main run of the Formboard if the 
                     NXOpen::Formboard::FormboardLayoutBuilder::MainRunType  is 
                     NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection .   
         
        """
        pass
    @property
    def MaximumRandomAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumRandomAngle
         Returns the maximum random angle.  
            Used when
                   NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle  is
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles .
                   
         
        """
        pass
    @property
    def MinimumRandomAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumRandomAngle
         Returns the minimum random angle.  
            Used when 
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle  is
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles .
                    
         
        """
        pass
    @property
    def PrimaryStandardAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PrimaryStandardAngle
         Returns the primary standard angle.  
             The layout algorithm snaps the angle of the
                 branch to a multiple of this angle.  
                 Only used when the 
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleMethod  is
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles .   
         
        """
        pass
    @property
    def ReverseMainRun(self) -> bool:
        """
        Getter for property: (bool) ReverseMainRun
         Returns the flag that determines whether the main run is "reversed" or not.  
           If true then
                    the direction and order of the main run path is reversed.   The end of the main
                    run becomes the start and vice-versa.  The list of path segments is not
                    modified or re-ordered, only the order in which the path segments is evaluated
                    when laying out the geometry.   
         
        """
        pass
    @ReverseMainRun.setter
    def ReverseMainRun(self, reverseMainRun: bool):
        """
        Setter for property: (bool) ReverseMainRun
         Returns the flag that determines whether the main run is "reversed" or not.  
           If true then
                    the direction and order of the main run path is reversed.   The end of the main
                    run becomes the start and vice-versa.  The list of path segments is not
                    modified or re-ordered, only the order in which the path segments is evaluated
                    when laying out the geometry.   
         
        """
        pass
    @property
    def SecondaryStandardAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondaryStandardAngle
         Returns the secondary standard angle.  
             The layout algorithm snaps the angle of the
                 branch to a multiple of this angle when all multiples of the primary angle
                 have been used.  
                 Only used when the 
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle  is
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles .   
         
        """
        pass
    @property
    def TertiaryStandardAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TertiaryStandardAngle
         Returns the tertiary standard angle.  
             The layout algorithm snaps the angle of the
                 branch to a multiple of this angle when all multiples of the primary and secondary 
                 angles have been used.  
                 Only used when the 
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle  is
                  NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles .   
         
        """
        pass
    def CreateDefaultGeometry(self) -> None:
        """
         Creates the initial set of formboard geometry using the current 
                    default values stored in the builder.   This geometry is necessary for the
                    UI to allow the user to see and select formboard geometry, for example to define
                    a Main Run.   Does nothing if the work part already contains formboard
                    geometry.  
        """
        pass
    def TranslateToNewOrigin(self) -> None:
        """
         Translates the formboard geometry so that it matches the new main run origin, this is a more
                    lightweight operation than the full UpdateLayout operation.  The assumption here
                    is that the only change to the builder is with the main run origin. 
        """
        pass
    def UpdateLayout(self) -> None:
        """
         Updates the orientation and placement of the formboard geometry to match
                    the current set of layout options stored within the builder. 
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Assemblies
import NXOpen.Positioning
import NXOpen.Routing
import NXOpen.Routing.Electrical
class FormboardManager(NXOpen.Object): 
    """  Contains information about flattened harness drawing and drafting data for
         harness manufacturing drawings (Formboard Drawings).
     """
    class LegacyComponentOrientationConfidenceLevel(Enum):
        """
        Members Include: 
         |High|  High confidence indicates no branches and no severe curvature in the path between the components. 
         |Medium|  Medium confidence indicates one branch or one curve with severe curvature. 
         |Low|  Low confidenceindicates more than on branch or more than on curve with severe curvature. 

        """
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> FormboardManager.LegacyComponentOrientationConfidenceLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LegacyComponentOrientationDisplayStyle(Enum):
        """
        Members Include: 
         |NoDisplay|  No extra display. 
         |DisplayCurveNormals|  Display the normal of each curve in the path. 
         |DisplaySurface|  Display the surface swept along the curves in the path. 
         |DisplayAll|  Display both the curve normals and surface. 

        """
        NoDisplay: int
        DisplayCurveNormals: int
        DisplaySurface: int
        DisplayAll: int
        @staticmethod
        def ValueOf(value: int) -> FormboardManager.LegacyComponentOrientationDisplayStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddPartAs3dHarness(self, harness_part: NXOpen.Part) -> None:
        """
         Sets the input part as the part containing the potential harnesses to flatten.
                   This method will add the input part as a new component of this assembly if there
                   is not already an instance of the input part in the work part assembly.  This
                   method is only necessary if the reference between the formboard and it's parent
                   3D harness assembly has been removed.
                   Passing in  for the harness part will sever the link between
                   the formboard and it's current 3D harness part file.
                   
        """
        pass
    def CalculateLegacyComponentClocking(self, component1: NXOpen.Assemblies.Component, component2: NXOpen.Assemblies.Component, displayStyle: FormboardManager.LegacyComponentOrientationDisplayStyle) -> Tuple[NXOpen.Vector3d, float, FormboardManager.LegacyComponentOrientationConfidenceLevel]:
        """
         Calculates the clocking or twist between the two components along their connecting path.
                    The FormboardManager.CalculateLegacyComponentClocking method uses
                    an algorithm similar to the V1 formboard clocking calculated automatically when Routing
                    created a formboard to find the clocking angle between two components.
                    First, it finds a vector representing the "up" direction on the first component.
                    The "up" direction is the multiport's rotate vector. If the multiport has no rotate
                    vector, it uses the Z direction of the multiport's part.
                    Then, it sweeps this vector along the segments in the path connecting the two components.
                    Finally, it measures the angle between the swept vector and the second component's "up"
                    vector. This angle is the clocking angle.
                    Throws an error if the component has no multiport or there is no path connecting
                    the two components.
                
         Returns A tuple consisting of (rotationVector, clockingAngle, confidenceLevel). 
         - rotationVector is:  NXOpen.Vector3d. The rotation vector normal to the curve at the location of the second component's multiport. .
         - clockingAngle is: float. The relative angle between the rotation vector and the second component's multiport's rotate vector. .
         - confidenceLevel is:  FormboardManager.LegacyComponentOrientationConfidenceLevel NXOpen.. High, medium, or low confidence reflecting how many branches the path traversed or whether or not the swept surfaces had problems. .

        """
        pass
    def CreateFaceAnnotationBuilder(self) -> FaceAnnotationBuilder:
        """
         Creates a NXOpen.Formboard.FaceAnnotationBuilder object for importing
                    CGM or Pattern file geometry and placing it on a drawing sheet or model view.
                
         Returns builder ( FaceAnnotationBuilder NXOpen.):  .
        """
        pass
    def CreateFlipComponentBuilder(self) -> FlipComponentBuilder:
        """
         Creates a NXOpen.Formboard.FlipComponentBuilder object for
                    flipping of formboard component about an axis orthogonal to Z axis to ensure that
                    after flipping component lies in XY plane.
                
         Returns builder ( FlipComponentBuilder NXOpen.):  .
        """
        pass
    def CreateLayoutBuilder(self) -> FormboardLayoutBuilder:
        """
         Creates a NXOpen.Formboard.FormboardLayoutBuilder that can flatten and layout
                    new formboard geometry, or modify the layout of existing formboard geometry.
                
         Returns builder ( FormboardLayoutBuilder NXOpen.):  .
        """
        pass
    def CreateObjectAttributeReferenceBuilder(self) -> ObjectAttributeReferenceBuilder:
        """
         Creates a NXOpen.Formboard.ObjectAttributeReferenceBuilder that creates a tabular note
                    object which reads values from the single object selected by the user. It also creates leader for the
                    annotation associated with the object selected by user.
                
         Returns builder ( ObjectAttributeReferenceBuilder NXOpen.):  .
        """
        pass
    def CreateOrientBranchBuilder(self) -> OrientBranchBuilder:
        """
         Creates a NXOpen.Formboard.OrientBranchBuilder object for rotating
                    branches in formboard about Z axis.
                
         Returns builder ( OrientBranchBuilder NXOpen.):  .
        """
        pass
    def CreatePathLengthAnnotationBuilder(self, annotation: NXOpen.Annotations.Annotation) -> PathLengthAnnotationBuilder:
        """
         Creates a NXOpen.Formboard.PathLengthAnnotationBuilder 
         Returns builder ( PathLengthAnnotationBuilder NXOpen.): .
        """
        pass
    def CreateShapeSegmentBuilder(self, segment: NXOpen.Routing.ISegment) -> ShapeSegmentBuilder:
        """
         Creates a NXOpen.Formboard.ShapeSegmentBuilder that can shape formboard segments.
                
         Returns builder ( ShapeSegmentBuilder NXOpen.):  .
        """
        pass
    def CreateUpdateFormboardBuilder(self) -> UpdateFormboardBuilder:
        """
         Creates a NXOpen.Formboard.UpdateFormboardBuilder that compares and
                    updates formboard geometry to match a modified master 3D harness. 
         Returns builder ( UpdateFormboardBuilder NXOpen.):  .
        """
        pass
    def GetFmbdPlaneConstraints(self, fmbdPlane: NXOpen.NXObject) -> List[NXOpen.Positioning.ComponentConstraint]:
        """
         Gets NXOpen.Positioning.ComponentConstraint which are associated to the formboard plane.
         Returns constraints ( NXOpen.Positioning.ComponentConstraint Li):  .
        """
        pass
    def HideFormboardConstraints(self) -> None:
        """
         Hides the formboard constraints. 
        """
        pass
    def IsFormboard(self) -> bool:
        """
         Returns whether or not the part containing this NXOpen.Formboard.FormboardManager is
                  actually a Formboard Drawing part file.  
         Returns result (bool):  whether or not the part is a formboard. .
        """
        pass
    def ShowFormboardConstraints(self) -> None:
        """
         Shows all of the hidden formboard constraints. 
        """
        pass
    def StoreHarnessesToFlatten(self, harnesses: List[NXOpen.Routing.Electrical.HarnessDevice]) -> None:
        """
         Examines the input list of harnesses and stores information from the harnesses into the part containing
                 this NXOpen.Formboard.FormboardManager.   The harnesses must from a sub-component of
                 this part.  The harnesses must form a fully-connected set of geometry.   This method does not actually
                 flatten or copy the harness geometry. 
        """
        pass
import NXOpen
class LayoutLengthOptions(NXOpen.Builder): 
    """ Defines the various options for determining the rounded lengths of 
        formboard geometry during the layout or update process. """
    class RoundingMethod(Enum):
        """
        Members Include: 
         |Exact|  Lengths are unmodified. 
         |Nearest|  Lengths are rounded up or down 
                                                               to the nearest increment value. 
         |UpToNearest|  Lengths are rounded up to the 
                                                                   nearest increment value. 
         |DownToNearest|  Lengths are rounded down to
                                                                       the nearest increment value. 

        """
        Exact: int
        Nearest: int
        UpToNearest: int
        DownToNearest: int
        @staticmethod
        def ValueOf(value: int) -> LayoutLengthOptions.RoundingMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def NetlistLengthIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NetlistLengthIncrement
         Returns the connection list length increment.  
            Only used when the  
                     Formboard::LayoutLengthOptions::NetlistRoundingMethod  
                   is  Formboard::LayoutLengthOptions::RoundingMethodUpToNearest  or
                    Formboard::LayoutLengthOptions::RoundingMethodDownToNearest .
                
                  
         
        """
        pass
    @property
    def NetlistRoundingMethod(self) -> LayoutLengthOptions.RoundingMethod:
        """
        Getter for property: ( LayoutLengthOptions.RoundingMethod NXOpen.) NetlistRoundingMethod
         Returns the rounding method to apply to Connection List lengths.  
              
         
        """
        pass
    @NetlistRoundingMethod.setter
    def NetlistRoundingMethod(self, netlistRoundingMethod: LayoutLengthOptions.RoundingMethod):
        """
        Setter for property: ( LayoutLengthOptions.RoundingMethod NXOpen.) NetlistRoundingMethod
         Returns the rounding method to apply to Connection List lengths.  
              
         
        """
        pass
    @property
    def OverstockLengthIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OverstockLengthIncrement
         Returns the overstock length increment.  
            Only used when the 
                    Formboard::LayoutLengthOptions::OverstockRoundingMethod  
                   is  Formboard::LayoutLengthOptions::RoundingMethodUpToNearest  or
                    Formboard::LayoutLengthOptions::RoundingMethodDownToNearest .
                     
         
        """
        pass
    @property
    def OverstockRoundingMethod(self) -> LayoutLengthOptions.RoundingMethod:
        """
        Getter for property: ( LayoutLengthOptions.RoundingMethod NXOpen.) OverstockRoundingMethod
         Returns the rounding method to apply to overstock wrapped lengths.  
             
         
        """
        pass
    @OverstockRoundingMethod.setter
    def OverstockRoundingMethod(self, overstockRoundingMethod: LayoutLengthOptions.RoundingMethod):
        """
        Setter for property: ( LayoutLengthOptions.RoundingMethod NXOpen.) OverstockRoundingMethod
         Returns the rounding method to apply to overstock wrapped lengths.  
             
         
        """
        pass
    @property
    def SegmentLengthIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SegmentLengthIncrement
         Returns the segment length increment.  
            Only used when the
                    Formboard::LayoutLengthOptions::SegmentRoundingMethod  
                   is  Formboard::LayoutLengthOptions::RoundingMethodUpToNearest  or
                    Formboard::LayoutLengthOptions::RoundingMethodDownToNearest .
                     
         
        """
        pass
    @property
    def SegmentRoundingMethod(self) -> LayoutLengthOptions.RoundingMethod:
        """
        Getter for property: ( LayoutLengthOptions.RoundingMethod NXOpen.) SegmentRoundingMethod
         Returns the rounding method to apply to segment lengths.  
             
         
        """
        pass
    @SegmentRoundingMethod.setter
    def SegmentRoundingMethod(self, segmentRoundingMethod: LayoutLengthOptions.RoundingMethod):
        """
        Setter for property: ( LayoutLengthOptions.RoundingMethod NXOpen.) SegmentRoundingMethod
         Returns the rounding method to apply to segment lengths.  
             
         
        """
        pass
import NXOpen
import NXOpen.Annotations
class ObjectAttributeReferenceBuilder(NXOpen.Builder): 
    """ Builder for "object attribute" used in formboard which enbles user to create
        annotation in drafting functionality. It creates a tabular note and displays
        object attributes of a single object selected by user.
    """
    class LeaderType(Enum):
        """
        Members Include: 
         |NotSet|  No leader for annotation of selected object.
         |SingleLocation|  Single leader for the annotation of selected object.
         |StartandEndLocations|  Two leaders for annotation with start and end location.

        """
        NotSet: int
        SingleLocation: int
        StartandEndLocations: int
        @staticmethod
        def ValueOf(value: int) -> ObjectAttributeReferenceBuilder.LeaderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnnotLeader(self) -> NXOpen.Annotations.LeaderBuilder:
        """
        Getter for property: ( NXOpen.Annotations.LeaderBuilder) AnnotLeader
         Returns the  Annotations::LeaderBuilder  for the annotation   
            
         
        """
        pass
    @property
    def CompOrigin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) CompOrigin
         Returns the comp origin   
            
         
        """
        pass
    @property
    def EnumType(self) -> ObjectAttributeReferenceBuilder.LeaderType:
        """
        Getter for property: ( ObjectAttributeReferenceBuilder.LeaderType NXOpen.) EnumType
         Returns the enum type   
            
         
        """
        pass
    @EnumType.setter
    def EnumType(self, enumType: ObjectAttributeReferenceBuilder.LeaderType):
        """
        Setter for property: ( ObjectAttributeReferenceBuilder.LeaderType NXOpen.) EnumType
         Returns the enum type   
            
         
        """
        pass
    @property
    def ObjectSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ObjectSelection
         Returns the object selected by user to associated annotation   
            
         
        """
        pass
import NXOpen
import NXOpen.Routing
class OrientBranchBuilder(NXOpen.Builder): 
    """  Builder for "Orient Branch" operation used in formboard.
         Allows user to orient the branch by different methods.
     """
    class BranchAngleMethod(Enum):
        """
        Members Include: 
         |AnglefromReferenceVector| method to rotate branch with respect to selected vectors
         |Angle|  method to rotate branch by angle
         |AlignAxisToVector|  method to rotate branch by an angle between two vectors
         |TwoPoints|  method to rotate branch by and angle between two points

        """
        AnglefromReferenceVector: int
        Angle: int
        AlignAxisToVector: int
        TwoPoints: int
        @staticmethod
        def ValueOf(value: int) -> OrientBranchBuilder.BranchAngleMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BranchAngleType(self) -> OrientBranchBuilder.BranchAngleMethod:
        """
        Getter for property: ( OrientBranchBuilder.BranchAngleMethod NXOpen.) BranchAngleType
         Returns the user selected   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod     
            
         
        """
        pass
    @BranchAngleType.setter
    def BranchAngleType(self, branchAngleType: OrientBranchBuilder.BranchAngleMethod):
        """
        Setter for property: ( OrientBranchBuilder.BranchAngleMethod NXOpen.) BranchAngleType
         Returns the user selected   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod     
            
         
        """
        pass
    @property
    def FromPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FromPoint
         Returns the user selected from point when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints  .  
          
                   
         
        """
        pass
    @FromPoint.setter
    def FromPoint(self, fromPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FromPoint
         Returns the user selected from point when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints  .  
          
                   
         
        """
        pass
    @property
    def FromVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) FromVector
         Returns the user selected from vector when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector  .  
          
                   
         
        """
        pass
    @FromVector.setter
    def FromVector(self, fromVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) FromVector
         Returns the user selected from vector when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector  .  
          
                   
         
        """
        pass
    @property
    def RefRotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RefRotationAngle
         Returns the angle for the rotation of branch when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector  .  
          
                   
         
        """
        pass
    @property
    def ReferenceVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ReferenceVector
         Returns the user selected reference vector when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector  .  
          
                   
         
        """
        pass
    @ReferenceVector.setter
    def ReferenceVector(self, referenceVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ReferenceVector
         Returns the user selected reference vector when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector  .  
          
                   
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the angle for the rotation of branch when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAngle .  
          
                   
         
        """
        pass
    @property
    def SelectBranch(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SelectBranch
         Returns the user selected branch   NXOpen::Routing::ISegment  
                    for rotation.  
          
                  
         
        """
        pass
    @property
    def ToPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ToPoint
         Returns the user selected to point when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints  .  
          
                   
         
        """
        pass
    @ToPoint.setter
    def ToPoint(self, toPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ToPoint
         Returns the user selected to point when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints  .  
          
                   
         
        """
        pass
    @property
    def ToVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToVector
         Returns the user selected to vector when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector  .  
          
                   
         
        """
        pass
    @ToVector.setter
    def ToVector(self, toVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToVector
         Returns the user selected to vector when   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   is 
                      NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector  .  
          
                   
         
        """
        pass
    def InitializeFromSegment(self) -> None:
        """
         Initializes or resets ( start or stop ) drag operation based on the 
                    input branch segment.
                
        """
        pass
    def SetBranchSeedObject(self, segmentTag: NXOpen.Routing.ISegment) -> None:
        """
         Sets the selected branch  NXOpen.Routing.ISegment  when
                    a branch is selected by branch method by Routing Object Collector.
                
        """
        pass
    def StartDrag(self) -> None:
        """
         Starts the drag operation of selected object. Does nothing if drag has
                    already been started.
                
        """
        pass
    def StopDrag(self) -> None:
        """
         Stop the drag operation of selected object. Does nothing if drag has
                    not been started.
                
        """
        pass
    def UnSuppressConstraints(self) -> None:
        """
         Suppress the NXOpen.Positioning.Constraint  associated with selected branch  NXOpen.Routing.ISegment 
                    when a branch is selected by branch method by Routing Object Collector.
                
        """
        pass
    def UpdateRotationAngle(self, angle: float) -> None:
        """
         Rotates the branch by an appropriate rotation and transformation
                    which depends on the  NXOpen.Formboard.OrientBranchBuilder.BranchAngleMethod 
                    selected by user.
                
        """
        pass
import NXOpen
import NXOpen.Annotations
import NXOpen.Routing
class PathLengthAnnotationBuilder(NXOpen.Builder): 
    """ TODO Class documentation """
    class Types(Enum):
        """
        Members Include: 
         |PointsOnCurves|  TODO 
         |RoutingPathLength|  TODO 

        """
        PointsOnCurves: int
        RoutingPathLength: int
        @staticmethod
        def ValueOf(value: int) -> PathLengthAnnotationBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExpressionName(self) -> str:
        """
        Getter for property: (str) ExpressionName
         Returns the expression name   
            
         
        """
        pass
    @property
    def FirstEndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FirstEndPoint
         Returns the first end point   
            
         
        """
        pass
    @FirstEndPoint.setter
    def FirstEndPoint(self, firstEndPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FirstEndPoint
         Returns the first end point   
            
         
        """
        pass
    @property
    def Leader(self) -> NXOpen.Annotations.LeaderBuilder:
        """
        Getter for property: ( NXOpen.Annotations.LeaderBuilder) Leader
         Returns the leader   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) Origin
         Returns the origin   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the route object collector   
            
         
        """
        pass
    @property
    def SecondEndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SecondEndPoint
         Returns the second end point   
            
         
        """
        pass
    @SecondEndPoint.setter
    def SecondEndPoint(self, secondEndPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SecondEndPoint
         Returns the second end point   
            
         
        """
        pass
    @property
    def ShowLeadersToggle(self) -> bool:
        """
        Getter for property: (bool) ShowLeadersToggle
         Returns the show leaders toggle   
            
         
        """
        pass
    @ShowLeadersToggle.setter
    def ShowLeadersToggle(self, showLeadersToggle: bool):
        """
        Setter for property: (bool) ShowLeadersToggle
         Returns the show leaders toggle   
            
         
        """
        pass
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.StyleBuilder) Style
         Returns the style   
            
         
        """
        pass
    @property
    def Text(self) -> NXOpen.Annotations.TextWithEditControlsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TextWithEditControlsBuilder) Text
         Returns the u icomp text with symbols0   
            
         
        """
        pass
    @property
    def Type(self) -> PathLengthAnnotationBuilder.Types:
        """
        Getter for property: ( PathLengthAnnotationBuilder.Types NXOpen.) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: PathLengthAnnotationBuilder.Types):
        """
        Setter for property: ( PathLengthAnnotationBuilder.Types NXOpen.) Type
         Returns the type   
            
         
        """
        pass
    def CreatePointsAtRcps(self, firstEndRcp: NXOpen.Routing.ControlPoint, secondEndRcp: NXOpen.Routing.ControlPoint) -> None:
        """
         Create builder end points at the RCP locations
        """
        pass
    def SetPathLengthAnnotationEndPoints(self, firstEndPoint: NXOpen.Point, secondEndPoint: NXOpen.Point) -> None:
        """
         Create and initialize the Path Length Annotation 
        """
        pass
import NXOpen
import NXOpen.Routing
class ShapeSegmentBuilder(NXOpen.Builder): 
    """ Builder for Face Annotation functionality used in formboard. It allows 
         importing CGM or Pattern file geometry and placing it on a drawing sheet
         or model view. As a result of this a group of dumb geometry is placed such
         that defined origin is located at the lower left hand of the bounding box 
         containing the group of geometry.
     """
    def AddRadialPivot(self, pivotLocation: NXOpen.Point3d, bendMethod: int, bendValue: float) -> None:
        """
         
                
        """
        pass
    def AddSplinePoint(self, pointLocation: NXOpen.Point3d) -> int:
        """
                Adds a point to the existing spline. 
                
         Returns pointIndex (int): .
        """
        pass
    def ChangeType(self, newType: int) -> None:
        """
         
                
        """
        pass
    def CommitCurrentOperation(self) -> None:
        """
         
                
        """
        pass
    def CreateNewRadialBend(self, firstPivot: NXOpen.Point3d, firstBendMethod: int, firstBendValue: float, secondPivot: NXOpen.Point3d, secondBendMethod: int, secondBendValue: float) -> None:
        """
         
                
        """
        pass
    def CreateNewSpline(self, anchorLocation: NXOpen.Point3d, firstPoint: NXOpen.Point3d, secondPoint: NXOpen.Point3d) -> None:
        """
                
        """
        pass
    def GetLineData(self) -> Tuple[NXOpen.Routing.ISegment, NXOpen.Routing.ControlPoint, float]:
        """
         
                
         Returns A tuple consisting of (anchorSeg, anchorRcp, angle). 
         - anchorSeg is:  NXOpen.Routing.ISegment. .
         - anchorRcp is:  NXOpen.Routing.ControlPoint. .
         - angle is: float. .

        """
        pass
    def NewSegment(self, newSegment: NXOpen.Routing.ISegment) -> None:
        """
         
                
        """
        pass
    def RemoveRadialPivot(self, pivotIndex: int) -> None:
        """
         
                
        """
        pass
    def RemoveSplinePoint(self, pointIndex: int) -> None:
        """
                
        """
        pass
    def SetActiveView(self, view: NXOpen.TaggedObject) -> None:
        """
         Sets the active view for the shape operation.
                
        """
        pass
    def SwapAnchorEnd(self) -> None:
        """
         
                
        """
        pass
    def UpdateLineAngleVec(self, newDir: NXOpen.Vector3d) -> None:
        """
         
                
        """
        pass
    def UpdateRadialPivot(self, pivotIndex: int, newLocation: NXOpen.Point3d, newBendMethod: int, newBendValue: float) -> None:
        """
         
                
        """
        pass
    def UpdateSplinePoint(self, pointIndex: int, pointLocation: NXOpen.Point3d, inDrag: bool) -> None:
        """
         
                
        """
        pass
import NXOpen
class UpdateDiscrepancy(NXOpen.TransientObject): 
    """
        Defines a discrepancy object which contains information about a specific
        difference between the formboard drawing and the 3D harness model.
    """
    class ObjectType(Enum):
        """
        Members Include: 
         |Unknown|  Unknown type. 
         |Rcp|  Routing Control Point. 
         |Segment|  Routing Segment. 
         |Clip|  A component not assigned as a
                                                                electrical connector. 
         |Component|  A component assigned as a
                                                                electrical connector or device. 
         |Harness|  Harness. 
         |Wire|  Wire connection. 
         |Cable|  Cable connection. 
         |Shield|  Shield connection. 
         |Connector|  ConnectorDevice object which 
                                                               has a type of connector. 
         |Device|  ConnectorDevice object which 
                                                               has a type of device. 
         |Overstock|  Overstock. 
         |Fillerstock|  Filler stock. 
         |FittingOverstock|  Overstock applied to fittings. 

        """
        Unknown: int
        Rcp: int
        Segment: int
        Clip: int
        Component: int
        Harness: int
        Wire: int
        Cable: int
        Shield: int
        Connector: int
        Device: int
        Overstock: int
        Fillerstock: int
        FittingOverstock: int
        @staticmethod
        def ValueOf(value: int) -> UpdateDiscrepancy.ObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Unknown|  Unknown type, not valid. 
         |Missing|  Object exits in the 3D harness but is 
                                                        missing from the formboard. 
         |Extra|  Object is in the formboard but not in
                                                        the 3D harness. 
         |Modified|  Object exists in both 3D and the formboard but
                                                        is modified in some way. 

        """
        Unknown: int
        Missing: int
        Extra: int
        Modified: int
        @staticmethod
        def ValueOf(value: int) -> UpdateDiscrepancy.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description string of the discrepancy.  
             
         
        """
        pass
    @property
    def DiscrepancyObjectType(self) -> UpdateDiscrepancy.ObjectType:
        """
        Getter for property: ( UpdateDiscrepancy.ObjectType NXOpen.) DiscrepancyObjectType
         Returns the type of object referenced by the discrepancy.  
             
         
        """
        pass
    @property
    def DiscrepancyType(self) -> UpdateDiscrepancy.Type:
        """
        Getter for property: ( UpdateDiscrepancy.Type NXOpen.) DiscrepancyType
         Returns the general type of the discrepancy.  
             
         
        """
        pass
    @property
    def FormboardObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) FormboardObject
         Returns the object in the 2D formboard referenced by the discrepancy.  
           This may
                  be NULL depending on the type of the discrepancy.  
         
        """
        pass
    @property
    def HarnessObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) HarnessObject
         Returns the object in the 3D harness referenced by the discrepancy.  
            This may
                  be NULL depending on the type of the discrepancy.  
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object. 
        """
        pass
import NXOpen
import NXOpen.Routing.Electrical
class UpdateFormboardBuilder(NXOpen.Builder): 
    """ Class that performs the "update" of Formboard geometry.  
     """
    @property
    def LengthOptions(self) -> LayoutLengthOptions:
        """
        Getter for property: ( LayoutLengthOptions NXOpen.) LengthOptions
         Returns the length options for the update operation.  
              
         
        """
        pass
    def CreateBendsOfRadialBends(self) -> None:
        """
         Creates bends for radial bends after all discrepanices have been fixed. This routine
                    should be called in conjunction with RemoveBendsOfRadialBends.
                
        """
        pass
    def DetermineDiscrepancies(self) -> None:
        """
         Once the mapping has been determined, this method can find any discrepancies
                   between the 3D harness and the formboard.  
        """
        pass
    def FindMapping(self) -> None:
        """
         Compute the mapping between the data in the formboard and the data in the
                   3D harness.  This method can take a very long time to execute. 
        """
        pass
    def GetDiscrepancy(self, index: int) -> UpdateDiscrepancy:
        """
         Returns the discrepancy at the given index.  The index must be
                    0 to Formboard.UpdateFormboardBuilder.GetNumberOfDiscrepancies.
                    
         Returns discrep ( UpdateDiscrepancy NXOpen.):  .
        """
        pass
    def GetHarnessPart(self) -> NXOpen.Part:
        """
         Gets the 3D harness part file to compare the formboard against. 
         Returns harnessPart ( NXOpen.Part): .
        """
        pass
    def GetNumberOfDiscrepancies(self) -> int:
        """
         Returns the number of discrepancies discovered by the 
                  Formboard.UpdateFormboardBuilder.DetermineDiscrepancies. 
         Returns numDiscreps (int):  .
        """
        pass
    def RemoveBendsOfRadialBends(self) -> None:
        """
         Removes bends in all radial bends and replaces them with a linear segment
                    going from the anchor to the free RCP of each radial bend. This is done before
                    fixing discrepancies because presence of bends in radial bend causes problems.
                    The bends of radial bends are recreated after the discrepancies have been fixed
                    using CreateBendsOfRadialBends
                
        """
        pass
    def SetHarnessPart(self, harnessPart: NXOpen.Part) -> None:
        """
         Sets the 3D harness part file to compare the formboard against. This clears
                  any discrepancies that have been discovered against the previous harness
                  part.  
        """
        pass
    def SetHarnesses(self, harnesses: List[NXOpen.Routing.Electrical.HarnessDevice]) -> None:
        """
         Sets the harnesses within the harness part that the formboard must be 
                  compared with. 
        """
        pass
