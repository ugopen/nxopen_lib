from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Builder for Face Annotation functionality used in formboard. It allows 
##          importing CGM or Pattern file geometry and placing it on a drawing sheet
##          or model view. As a result of this a group of dumb geometry is placed such
##          that defined origin is located at the lower left hand of the bounding box 
##          containing the group of geometry.
##       <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreateFaceAnnotationBuilder  NXOpen::Formboard::FormboardManager::CreateFaceAnnotationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DestEnum </term> <description> 
##  
## DrawingSheet </description> </item> 
## 
## <item><term> 
##  
## TogBlank </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class FaceAnnotationBuilder(NXOpen.Builder): 
    """ Builder for Face Annotation functionality used in formboard. It allows 
         importing CGM or Pattern file geometry and placing it on a drawing sheet
         or model view. As a result of this a group of dumb geometry is placed such
         that defined origin is located at the lower left hand of the bounding box 
         containing the group of geometry.
     """


    ##  Enum which defines where the geometry is to be placed. The geometry
    ##             can be placed either in model or drawing sheet.
    ##         
    ##  Place geometry in drawing sheet 
    class DrwDestination(Enum):
        """
        Members Include: <DrawingSheet> <Model>
        """
        DrawingSheet: int
        Model: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceAnnotationBuilder.DrwDestination:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Enum which defines the type to import CGM/Pattern file
    ##  Import CGM file by selecting a component
    class Types(Enum):
        """
        Members Include: <ComponentAttribute> <CgmFileSelection> <PatternFileSelection>
        """
        ComponentAttribute: int
        CgmFileSelection: int
        PatternFileSelection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FaceAnnotationBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) CgmflBrsr
    ##   the browser which enables selection of CGM file when @link 
    ##            Formboard::FaceAnnotationBuilder::Types 
    ##            Formboard::FaceAnnotationBuilder::Types@endlink  is @link 
    ##            Formboard::FaceAnnotationBuilder::TypesCgmFileSelection  
    ##            Formboard::FaceAnnotationBuilder::TypesCgmFileSelection @endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def CgmflBrsr(self) -> str:
        """
        Getter for property: (str) CgmflBrsr
          the browser which enables selection of CGM file when @link 
                   Formboard::FaceAnnotationBuilder::Types 
                   Formboard::FaceAnnotationBuilder::Types@endlink  is @link 
                   Formboard::FaceAnnotationBuilder::TypesCgmFileSelection  
                   Formboard::FaceAnnotationBuilder::TypesCgmFileSelection @endlink .  
          
                  
         
        """
        pass
    
    ## Setter for property: (str) CgmflBrsr

    ##   the browser which enables selection of CGM file when @link 
    ##            Formboard::FaceAnnotationBuilder::Types 
    ##            Formboard::FaceAnnotationBuilder::Types@endlink  is @link 
    ##            Formboard::FaceAnnotationBuilder::TypesCgmFileSelection  
    ##            Formboard::FaceAnnotationBuilder::TypesCgmFileSelection @endlink .  
    ##   
    ##           
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CgmflBrsr.setter
    def CgmflBrsr(self, filename: str):
        """
        Setter for property: (str) CgmflBrsr
          the browser which enables selection of CGM file when @link 
                   Formboard::FaceAnnotationBuilder::Types 
                   Formboard::FaceAnnotationBuilder::Types@endlink  is @link 
                   Formboard::FaceAnnotationBuilder::TypesCgmFileSelection  
                   Formboard::FaceAnnotationBuilder::TypesCgmFileSelection @endlink .  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) CompSel
    ##   the user selected component which has a CGM_FILE or PATTERN_FILE attribute defined.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def CompSel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) CompSel
          the user selected component which has a CGM_FILE or PATTERN_FILE attribute defined.  
             
         
        """
        pass
    
    ## Getter for property: (@link FaceAnnotationBuilder.DrwDestination NXOpen.Formboard.FaceAnnotationBuilder.DrwDestination@endlink) DestEnum
    ##   the @link  NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination   NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination @endlink  selected by
    ##             user to place the geometry   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return FaceAnnotationBuilder.DrwDestination
    @property
    def DestEnum(self) -> FaceAnnotationBuilder.DrwDestination:
        """
        Getter for property: (@link FaceAnnotationBuilder.DrwDestination NXOpen.Formboard.FaceAnnotationBuilder.DrwDestination@endlink) DestEnum
          the @link  NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination   NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination @endlink  selected by
                    user to place the geometry   
            
         
        """
        pass
    
    ## Setter for property: (@link FaceAnnotationBuilder.DrwDestination NXOpen.Formboard.FaceAnnotationBuilder.DrwDestination@endlink) DestEnum

    ##   the @link  NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination   NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination @endlink  selected by
    ##             user to place the geometry   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @DestEnum.setter
    def DestEnum(self, destEnum: FaceAnnotationBuilder.DrwDestination):
        """
        Setter for property: (@link FaceAnnotationBuilder.DrwDestination NXOpen.Formboard.FaceAnnotationBuilder.DrwDestination@endlink) DestEnum
          the @link  NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination   NXOpen::Formboard::FaceAnnotationBuilder::DrwDestination @endlink  selected by
                    user to place the geometry   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PntOrigin
    ##   the user selected point where geometry will be placed   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Point
    @property
    def PntOrigin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PntOrigin
          the user selected point where geometry will be placed   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PntOrigin

    ##   the user selected point where geometry will be placed   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @PntOrigin.setter
    def PntOrigin(self, pntOrigin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PntOrigin
          the user selected point where geometry will be placed   
            
         
        """
        pass
    
    ## Getter for property: (str) StrAnnot
    ##   the string to display the name of Pattern file name selected by user.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def StrAnnot(self) -> str:
        """
        Getter for property: (str) StrAnnot
          the string to display the name of Pattern file name selected by user.  
             
         
        """
        pass
    
    ## Setter for property: (str) StrAnnot

    ##   the string to display the name of Pattern file name selected by user.  
    ##      
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @StrAnnot.setter
    def StrAnnot(self, strAnnot: str):
        """
        Setter for property: (str) StrAnnot
          the string to display the name of Pattern file name selected by user.  
             
         
        """
        pass
    
    ## Getter for property: (str) StrAnnotFileName
    ##   the string to display the name of CGM name selected by user.  
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def StrAnnotFileName(self) -> str:
        """
        Getter for property: (str) StrAnnotFileName
          the string to display the name of CGM name selected by user.  
            
         
        """
        pass
    
    ## Setter for property: (str) StrAnnotFileName

    ##   the string to display the name of CGM name selected by user.  
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @StrAnnotFileName.setter
    def StrAnnotFileName(self, strAnnot: str):
        """
        Setter for property: (str) StrAnnotFileName
          the string to display the name of CGM name selected by user.  
            
         
        """
        pass
    
    ## Getter for property: (bool) TogBlank
    ##   the toggle which defines whether the selected component is to be blanked or not   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def TogBlank(self) -> bool:
        """
        Getter for property: (bool) TogBlank
          the toggle which defines whether the selected component is to be blanked or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) TogBlank

    ##   the toggle which defines whether the selected component is to be blanked or not   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @TogBlank.setter
    def TogBlank(self, togBlank: bool):
        """
        Setter for property: (bool) TogBlank
          the toggle which defines whether the selected component is to be blanked or not   
            
         
        """
        pass
    
    ## Getter for property: (@link FaceAnnotationBuilder.Types NXOpen.Formboard.FaceAnnotationBuilder.Types@endlink) Type
    ##   the @link  NXOpen::Formboard::FaceAnnotationBuilder::Types   NXOpen::Formboard::FaceAnnotationBuilder::Types @endlink 
    ##             selected by user   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return FaceAnnotationBuilder.Types
    @property
    def Type(self) -> FaceAnnotationBuilder.Types:
        """
        Getter for property: (@link FaceAnnotationBuilder.Types NXOpen.Formboard.FaceAnnotationBuilder.Types@endlink) Type
          the @link  NXOpen::Formboard::FaceAnnotationBuilder::Types   NXOpen::Formboard::FaceAnnotationBuilder::Types @endlink 
                    selected by user   
            
         
        """
        pass
    
    ## Setter for property: (@link FaceAnnotationBuilder.Types NXOpen.Formboard.FaceAnnotationBuilder.Types@endlink) Type

    ##   the @link  NXOpen::Formboard::FaceAnnotationBuilder::Types   NXOpen::Formboard::FaceAnnotationBuilder::Types @endlink 
    ##             selected by user   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Type.setter
    def Type(self, type: FaceAnnotationBuilder.Types):
        """
        Setter for property: (@link FaceAnnotationBuilder.Types NXOpen.Formboard.FaceAnnotationBuilder.Types@endlink) Type
          the @link  NXOpen::Formboard::FaceAnnotationBuilder::Types   NXOpen::Formboard::FaceAnnotationBuilder::Types @endlink 
                    selected by user   
            
         
        """
        pass
    
import NXOpen
##  Builder for flip component operation used in formboard.
##         Allows user to flip the component by 180 degrees about an axis which is
##         orthogonal to Z axis so that after flipping , the component lies in XY plane.
##      <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreateFlipComponentBuilder  NXOpen::Formboard::FormboardManager::CreateFlipComponentBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AxisTypeEnum </term> <description> 
##  
## PathLocations </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class FlipComponentBuilder(NXOpen.Builder): 
    """ Builder for flip component operation used in formboard.
        Allows user to flip the component by 180 degrees about an axis which is
        orthogonal to Z axis so that after flipping , the component lies in XY plane.
    """


    ##  Enum for the selection of axis type for flipping formboard component
    ##  Flip component by path locations
    class AxisType(Enum):
        """
        Members Include: <PathLocations> <Custom>
        """
        PathLocations: int
        Custom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlipComponentBuilder.AxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FlipComponentBuilder.AxisType NXOpen.Formboard.FlipComponentBuilder.AxisType@endlink) AxisTypeEnum
    ##   the user selected @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  method   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return FlipComponentBuilder.AxisType
    @property
    def AxisTypeEnum(self) -> FlipComponentBuilder.AxisType:
        """
        Getter for property: (@link FlipComponentBuilder.AxisType NXOpen.Formboard.FlipComponentBuilder.AxisType@endlink) AxisTypeEnum
          the user selected @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  method   
            
         
        """
        pass
    
    ## Setter for property: (@link FlipComponentBuilder.AxisType NXOpen.Formboard.FlipComponentBuilder.AxisType@endlink) AxisTypeEnum

    ##   the user selected @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  method   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @AxisTypeEnum.setter
    def AxisTypeEnum(self, axisTypeEnum: FlipComponentBuilder.AxisType):
        """
        Setter for property: (@link FlipComponentBuilder.AxisType NXOpen.Formboard.FlipComponentBuilder.AxisType@endlink) AxisTypeEnum
          the user selected @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) CompSel
    ##   the formboard component selected by user for flipping operation   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def CompSel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) CompSel
          the formboard component selected by user for flipping operation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CustomAxis
    ##   the custom axis which is created when 
    ##             @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  is
    ##             @link NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom@endlink 
    ##           
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Axis
    @property
    def CustomAxis(self) -> NXOpen.Axis:
        """
        Getter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CustomAxis
          the custom axis which is created when 
                    @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  is
                    @link NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom@endlink 
                  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CustomAxis

    ##   the custom axis which is created when 
    ##             @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  is
    ##             @link NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom@endlink 
    ##           
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @CustomAxis.setter
    def CustomAxis(self, customAxis: NXOpen.Axis):
        """
        Setter for property: (@link NXOpen.Axis NXOpen.Axis@endlink) CustomAxis
          the custom axis which is created when 
                    @link NXOpen::Formboard::FlipComponentBuilder::AxisType NXOpen::Formboard::FlipComponentBuilder::AxisType@endlink  is
                    @link NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom NXOpen::Formboard::FlipComponentBuilder::AxisTypeCustom@endlink 
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) PathAxisSel
    ##   the axis selected by user about which selected formboard component 
    ##             will be flipped.  
    ##   
    ##           
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def PathAxisSel(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) PathAxisSel
          the axis selected by user about which selected formboard component 
                    will be flipped.  
          
                  
         
        """
        pass
    
    ##  Creates datums axis at locations where selected formboard component 
    ##             is connected to path.
    ##         
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateDatumAxis(builder: FlipComponentBuilder) -> List[NXOpen.NXObject]:
        """
         Creates datums axis at locations where selected formboard component 
                    is connected to path.
                
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  .
        """
        pass
    
    ##  Flips the selected formboard component by rotation angle 
    ##            about selected axis.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def FlipComponent(builder: FlipComponentBuilder) -> None:
        """
         Flips the selected formboard component by rotation angle 
                   about selected axis.
                
        """
        pass
    
    ##  Initializes or resets ( start or stop ) drag operation based on the 
    ##            component selected for flipping operation.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def InitializeFromComponent(builder: FlipComponentBuilder) -> None:
        """
         Initializes or resets ( start or stop ) drag operation based on the 
                   component selected for flipping operation.
                
        """
        pass
    
    ##  Set the angle to rotate the component.
    ##         
    ## 
    ##   <br>  Created in NX7.5.3  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  Rotation angle
    def SetRotationAngle(builder: FlipComponentBuilder, angle: float) -> None:
        """
         Set the angle to rotate the component.
                
        """
        pass
    
    ##  Starts the drag operation of selected object. Does nothing if drag has
    ##             already been started.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def StartDrag(builder: FlipComponentBuilder) -> None:
        """
         Starts the drag operation of selected object. Does nothing if drag has
                    already been started.
                
        """
        pass
    
    ##  Stop the drag operation of selected object. Does nothing if drag has
    ##             not been started.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def StopDrag(builder: FlipComponentBuilder) -> None:
        """
         Stop the drag operation of selected object. Does nothing if drag has
                    not been started.
                
        """
        pass
    
import NXOpen
import NXOpen.Routing
##  Class that performs the "layout" of Formboard geometry.  Creates all geometry
##         chosen by the user to flatten into a drawing and orients the geometry to
##         match the criteria specified in this builder class.   This builder must only
##         be instantiated and used after the harnesses have been specified and stored
##         using the @link NXOpen::Formboard::FormboardManager::StoreHarnessesToFlatten NXOpen::Formboard::FormboardManager::StoreHarnessesToFlatten@endlink  method.  <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreateLayoutBuilder  NXOpen::Formboard::FormboardManager::CreateLayoutBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class FormboardLayoutBuilder(NXOpen.Builder): 
    """ Class that performs the "layout" of Formboard geometry.  Creates all geometry
        chosen by the user to flatten into a drawing and orients the geometry to
        match the criteria specified in this builder class.   This builder must only
        be instantiated and used after the harnesses have been specified and stored
        using the <ja_method>NXOpen.Formboard.FormboardManager.StoreHarnessesToFlatten</ja_method> method. """


    ##  Methods for determining which angles to apply at each branch of the Formboard. 
    ##  Use the angle equal to the 3D angle
    ##                                                             of the branch in the 3D harness. 
    class BranchAngle(Enum):
        """
        Members Include: <AsDesigned> <StandardAngles> <MaximumAngles> <RandomAngles>
        """
        AsDesigned: int
        StandardAngles: int
        MaximumAngles: int
        RandomAngles: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FormboardLayoutBuilder.BranchAngle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Shape option for the branches. 
    ##  Each branch forms a straight line. 
    class BranchShape(Enum):
        """
        Members Include: <Straight> <Angled>
        """
        Straight: int
        Angled: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FormboardLayoutBuilder.BranchShape:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Selection method for the set of segments that define the main
    ##             run of the formboard geometry. 
    ##  Path of longest wire. 
    class MainRunType(Enum):
        """
        Members Include: <Longest> <Thickest> <UserSelection>
        """
        Longest: int
        Thickest: int
        UserSelection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FormboardLayoutBuilder.MainRunType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FormboardLayoutBuilder.BranchAngle NXOpen.Formboard.FormboardLayoutBuilder.BranchAngle@endlink) BranchAngleMethod
    ##   the branch angle type.  
    ##     Specifies how the layout algorithm determines the angle
    ##             between each child branch and its parent branch.    
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return FormboardLayoutBuilder.BranchAngle
    @property
    def BranchAngleMethod(self) -> FormboardLayoutBuilder.BranchAngle:
        """
        Getter for property: (@link FormboardLayoutBuilder.BranchAngle NXOpen.Formboard.FormboardLayoutBuilder.BranchAngle@endlink) BranchAngleMethod
          the branch angle type.  
            Specifies how the layout algorithm determines the angle
                    between each child branch and its parent branch.    
         
        """
        pass
    
    ## Setter for property: (@link FormboardLayoutBuilder.BranchAngle NXOpen.Formboard.FormboardLayoutBuilder.BranchAngle@endlink) BranchAngleMethod

    ##   the branch angle type.  
    ##     Specifies how the layout algorithm determines the angle
    ##             between each child branch and its parent branch.    
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @BranchAngleMethod.setter
    def BranchAngleMethod(self, branchAngle: FormboardLayoutBuilder.BranchAngle):
        """
        Setter for property: (@link FormboardLayoutBuilder.BranchAngle NXOpen.Formboard.FormboardLayoutBuilder.BranchAngle@endlink) BranchAngleMethod
          the branch angle type.  
            Specifies how the layout algorithm determines the angle
                    between each child branch and its parent branch.    
         
        """
        pass
    
    ## Getter for property: (@link FormboardLayoutBuilder.BranchShape NXOpen.Formboard.FormboardLayoutBuilder.BranchShape@endlink) BranchShapeType
    ##   the branch shape type.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return FormboardLayoutBuilder.BranchShape
    @property
    def BranchShapeType(self) -> FormboardLayoutBuilder.BranchShape:
        """
        Getter for property: (@link FormboardLayoutBuilder.BranchShape NXOpen.Formboard.FormboardLayoutBuilder.BranchShape@endlink) BranchShapeType
          the branch shape type.  
             
         
        """
        pass
    
    ## Setter for property: (@link FormboardLayoutBuilder.BranchShape NXOpen.Formboard.FormboardLayoutBuilder.BranchShape@endlink) BranchShapeType

    ##   the branch shape type.  
    ##      
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @BranchShapeType.setter
    def BranchShapeType(self, branchShape: FormboardLayoutBuilder.BranchShape):
        """
        Setter for property: (@link FormboardLayoutBuilder.BranchShape NXOpen.Formboard.FormboardLayoutBuilder.BranchShape@endlink) BranchShapeType
          the branch shape type.  
             
         
        """
        pass
    
    ## Getter for property: (@link LayoutLengthOptions NXOpen.Formboard.LayoutLengthOptions@endlink) LengthOptions
    ##   the length options for the layout operation.  
    ##     The length options only have
    ##           any effect if this is the first time that the Formboard geometry is being
    ##           created in the drawing.   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return LayoutLengthOptions
    @property
    def LengthOptions(self) -> LayoutLengthOptions:
        """
        Getter for property: (@link LayoutLengthOptions NXOpen.Formboard.LayoutLengthOptions@endlink) LengthOptions
          the length options for the layout operation.  
            The length options only have
                  any effect if this is the first time that the Formboard geometry is being
                  created in the drawing.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Routing.SelectControlPoint NXOpen.Routing.SelectControlPoint@endlink) MainRunEndSelection
    ##   the end of the main run.  
    ##     Contains the ending control point 
    ##             that defines the main run of the Formboard if the 
    ##             @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunType NXOpen::Formboard::FormboardLayoutBuilder::MainRunType@endlink  is 
    ##             @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection@endlink .   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Routing.SelectControlPoint
    @property
    def MainRunEndSelection(self) -> NXOpen.Routing.SelectControlPoint:
        """
        Getter for property: (@link NXOpen.Routing.SelectControlPoint NXOpen.Routing.SelectControlPoint@endlink) MainRunEndSelection
          the end of the main run.  
            Contains the ending control point 
                    that defines the main run of the Formboard if the 
                    @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunType NXOpen::Formboard::FormboardLayoutBuilder::MainRunType@endlink  is 
                    @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link FormboardLayoutBuilder.MainRunType NXOpen.Formboard.FormboardLayoutBuilder.MainRunType@endlink) MainRunMethod
    ##   the main run method.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return FormboardLayoutBuilder.MainRunType
    @property
    def MainRunMethod(self) -> FormboardLayoutBuilder.MainRunType:
        """
        Getter for property: (@link FormboardLayoutBuilder.MainRunType NXOpen.Formboard.FormboardLayoutBuilder.MainRunType@endlink) MainRunMethod
          the main run method.  
             
         
        """
        pass
    
    ## Setter for property: (@link FormboardLayoutBuilder.MainRunType NXOpen.Formboard.FormboardLayoutBuilder.MainRunType@endlink) MainRunMethod

    ##   the main run method.  
    ##      
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @MainRunMethod.setter
    def MainRunMethod(self, mainRunType: FormboardLayoutBuilder.MainRunType):
        """
        Setter for property: (@link FormboardLayoutBuilder.MainRunType NXOpen.Formboard.FormboardLayoutBuilder.MainRunType@endlink) MainRunMethod
          the main run method.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MainRunOrigin
    ##   the main run origin.  
    ##     The location in modeling space of the start 
    ##             of the main run. The layout operation translates the main run such 
    ##             that it start RCP is located at this location.   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Point
    @property
    def MainRunOrigin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MainRunOrigin
          the main run origin.  
            The location in modeling space of the start 
                    of the main run. The layout operation translates the main run such 
                    that it start RCP is located at this location.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MainRunOrigin

    ##   the main run origin.  
    ##     The location in modeling space of the start 
    ##             of the main run. The layout operation translates the main run such 
    ##             that it start RCP is located at this location.   
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @MainRunOrigin.setter
    def MainRunOrigin(self, mainRunOrigin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MainRunOrigin
          the main run origin.  
            The location in modeling space of the start 
                    of the main run. The layout operation translates the main run such 
                    that it start RCP is located at this location.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Routing.SelectControlPoint NXOpen.Routing.SelectControlPoint@endlink) MainRunStartSelection
    ##   the start of the main run.  
    ##     Contains the starting control point 
    ##             that defines the main run of the Formboard if the 
    ##             @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunType NXOpen::Formboard::FormboardLayoutBuilder::MainRunType@endlink  is 
    ##             @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection@endlink .   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Routing.SelectControlPoint
    @property
    def MainRunStartSelection(self) -> NXOpen.Routing.SelectControlPoint:
        """
        Getter for property: (@link NXOpen.Routing.SelectControlPoint NXOpen.Routing.SelectControlPoint@endlink) MainRunStartSelection
          the start of the main run.  
            Contains the starting control point 
                    that defines the main run of the Formboard if the 
                    @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunType NXOpen::Formboard::FormboardLayoutBuilder::MainRunType@endlink  is 
                    @link NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection NXOpen::Formboard::FormboardLayoutBuilder::MainRunTypeUserSelection@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumRandomAngle
    ##   the maximum random angle.  
    ##     Used when
    ##           @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles@endlink .
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaximumRandomAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaximumRandomAngle
          the maximum random angle.  
            Used when
                  @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles@endlink .
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumRandomAngle
    ##   the minimum random angle.  
    ##     Used when 
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles@endlink .
    ##             
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinimumRandomAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinimumRandomAngle
          the minimum random angle.  
            Used when 
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleRandomAngles@endlink .
                    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PrimaryStandardAngle
    ##   the primary standard angle.  
    ##      The layout algorithm snaps the angle of the
    ##          branch to a multiple of this angle.  
    ##          Only used when the 
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleMethod NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleMethod@endlink  is
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles@endlink .   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PrimaryStandardAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PrimaryStandardAngle
          the primary standard angle.  
             The layout algorithm snaps the angle of the
                 branch to a multiple of this angle.  
                 Only used when the 
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleMethod NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleMethod@endlink  is
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles@endlink .   
         
        """
        pass
    
    ## Getter for property: (bool) ReverseMainRun
    ##   the flag that determines whether the main run is "reversed" or not.  
    ##    If true then
    ##             the direction and order of the main run path is reversed.   The end of the main
    ##             run becomes the start and vice-versa.  The list of path segments is not
    ##             modified or re-ordered, only the order in which the path segments is evaluated
    ##             when laying out the geometry.   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def ReverseMainRun(self) -> bool:
        """
        Getter for property: (bool) ReverseMainRun
          the flag that determines whether the main run is "reversed" or not.  
           If true then
                    the direction and order of the main run path is reversed.   The end of the main
                    run becomes the start and vice-versa.  The list of path segments is not
                    modified or re-ordered, only the order in which the path segments is evaluated
                    when laying out the geometry.   
         
        """
        pass
    
    ## Setter for property: (bool) ReverseMainRun

    ##   the flag that determines whether the main run is "reversed" or not.  
    ##    If true then
    ##             the direction and order of the main run path is reversed.   The end of the main
    ##             run becomes the start and vice-versa.  The list of path segments is not
    ##             modified or re-ordered, only the order in which the path segments is evaluated
    ##             when laying out the geometry.   
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ReverseMainRun.setter
    def ReverseMainRun(self, reverseMainRun: bool):
        """
        Setter for property: (bool) ReverseMainRun
          the flag that determines whether the main run is "reversed" or not.  
           If true then
                    the direction and order of the main run path is reversed.   The end of the main
                    run becomes the start and vice-versa.  The list of path segments is not
                    modified or re-ordered, only the order in which the path segments is evaluated
                    when laying out the geometry.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondaryStandardAngle
    ##   the secondary standard angle.  
    ##      The layout algorithm snaps the angle of the
    ##          branch to a multiple of this angle when all multiples of the primary angle
    ##          have been used.  
    ## 
    ##          Only used when the 
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles@endlink .   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SecondaryStandardAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondaryStandardAngle
          the secondary standard angle.  
             The layout algorithm snaps the angle of the
                 branch to a multiple of this angle when all multiples of the primary angle
                 have been used.  
        
                 Only used when the 
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TertiaryStandardAngle
    ##   the tertiary standard angle.  
    ##      The layout algorithm snaps the angle of the
    ##          branch to a multiple of this angle when all multiples of the primary and secondary 
    ##          angles have been used.  
    ## 
    ##          Only used when the 
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
    ##          @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles@endlink .   
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TertiaryStandardAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TertiaryStandardAngle
          the tertiary standard angle.  
             The layout algorithm snaps the angle of the
                 branch to a multiple of this angle when all multiples of the primary and secondary 
                 angles have been used.  
        
                 Only used when the 
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle NXOpen::Formboard::FormboardLayoutBuilder::BranchAngle@endlink  is
                 @link NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles NXOpen::Formboard::FormboardLayoutBuilder::BranchAngleStandardAngles@endlink .   
         
        """
        pass
    
    ##  Creates the initial set of formboard geometry using the current 
    ##             default values stored in the builder.   This geometry is necessary for the
    ##             UI to allow the user to see and select formboard geometry, for example to define
    ##             a Main Run.   Does nothing if the work part already contains formboard
    ##             geometry.  
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateDefaultGeometry(builder: FormboardLayoutBuilder) -> None:
        """
         Creates the initial set of formboard geometry using the current 
                    default values stored in the builder.   This geometry is necessary for the
                    UI to allow the user to see and select formboard geometry, for example to define
                    a Main Run.   Does nothing if the work part already contains formboard
                    geometry.  
        """
        pass
    
    ##  Translates the formboard geometry so that it matches the new main run origin, this is a more
    ##             lightweight operation than the full UpdateLayout operation.  The assumption here
    ##             is that the only change to the builder is with the main run origin. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def TranslateToNewOrigin(builder: FormboardLayoutBuilder) -> None:
        """
         Translates the formboard geometry so that it matches the new main run origin, this is a more
                    lightweight operation than the full UpdateLayout operation.  The assumption here
                    is that the only change to the builder is with the main run origin. 
        """
        pass
    
    ##  Updates the orientation and placement of the formboard geometry to match
    ##             the current set of layout options stored within the builder. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def UpdateLayout(builder: FormboardLayoutBuilder) -> None:
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
##   Contains information about flattened harness drawing and drafting data for
##          harness manufacturing drawings (Formboard Drawings).
##       <br> To obtain an instance of this class, refer to @link NXOpen::Routing::RouteManager  NXOpen::Routing::RouteManager @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class FormboardManager(NXOpen.Object): 
    """  Contains information about flattened harness drawing and drafting data for
         harness manufacturing drawings (Formboard Drawings).
     """


    ##  Returned from @link FormboardManager::CalculateLegacyComponentClocking FormboardManager::CalculateLegacyComponentClocking@endlink 
    ##             as a measure of the confidence in the calculated clocking.
    ##         
    ##  High confidence indicates no branches and no severe curvature in the path between the components. 
    class LegacyComponentOrientationConfidenceLevel(Enum):
        """
        Members Include: <High> <Medium> <Low>
        """
        High: int
        Medium: int
        Low: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FormboardManager.LegacyComponentOrientationConfidenceLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Used by @link FormboardManager::CalculateLegacyComponentClocking FormboardManager::CalculateLegacyComponentClocking@endlink  to
    ##             display extra information you can use to see how the clocking calculation is made.
    ##         
    ##  No extra display. 
    class LegacyComponentOrientationDisplayStyle(Enum):
        """
        Members Include: <NoDisplay> <DisplayCurveNormals> <DisplaySurface> <DisplayAll>
        """
        NoDisplay: int
        DisplayCurveNormals: int
        DisplaySurface: int
        DisplayAll: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FormboardManager.LegacyComponentOrientationDisplayStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Sets the input part as the part containing the potential harnesses to flatten.
    ##            This method will add the input part as a new component of this assembly if there
    ##            is not already an instance of the input part in the work part assembly.  This
    ##            method is only necessary if the reference between the formboard and it's parent
    ##            3D harness assembly has been removed.
    ## 
    ##            Passing in NULL for the harness part will sever the link between
    ##            the formboard and it's current 3D harness part file.
    ##            
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  Part containing the harnesses to flatten into this part. 
    def AddPartAs3dHarness(route_part: FormboardManager, harness_part: NXOpen.Part) -> None:
        """
         Sets the input part as the part containing the potential harnesses to flatten.
                   This method will add the input part as a new component of this assembly if there
                   is not already an instance of the input part in the work part assembly.  This
                   method is only necessary if the reference between the formboard and it's parent
                   3D harness assembly has been removed.
        
                   Passing in NULL for the harness part will sever the link between
                   the formboard and it's current 3D harness part file.
                   
        """
        pass
    
    ##  Calculates the clocking or twist between the two components along their connecting path.
    ## 
    ##             The @link FormboardManager::CalculateLegacyComponentClocking FormboardManager::CalculateLegacyComponentClocking@endlink  method uses
    ##             an algorithm similar to the V1 formboard clocking calculated automatically when Routing
    ##             created a formboard to find the clocking angle between two components.
    ## 
    ##             First, it finds a vector representing the "up" direction on the first component.
    ## 
    ##             The "up" direction is the multiport's rotate vector. If the multiport has no rotate
    ##             vector, it uses the Z direction of the multiport's part.
    ## 
    ##             Then, it sweeps this vector along the segments in the path connecting the two components.
    ## 
    ##             Finally, it measures the angle between the swept vector and the second component's "up"
    ##             vector. This angle is the clocking angle.
    ## 
    ##             Throws an error if the component has no multiport or there is no path connecting
    ##             the two components.
    ##         
    ##  @return A tuple consisting of (rotationVector, clockingAngle, confidenceLevel). 
    ##  - rotationVector is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. The rotation vector normal to the curve at the location of the second component's multiport. .
    ##  - clockingAngle is: float. The relative angle between the rotation vector and the second component's multiport's rotate vector. .
    ##  - confidenceLevel is: @link FormboardManager.LegacyComponentOrientationConfidenceLevel NXOpen.Formboard.FormboardManager.LegacyComponentOrientationConfidenceLevel@endlink. High, medium, or low confidence reflecting how many branches the path traversed or whether or not the swept surfaces had problems. .

    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  The first component. The clocking of the second component is always relative to the rotation vector of the first component. 
    @staticmethod
    def CalculateLegacyComponentClocking(objectInPart: FormboardManager, component1: NXOpen.Assemblies.Component, component2: NXOpen.Assemblies.Component, displayStyle: FormboardManager.LegacyComponentOrientationDisplayStyle) -> Tuple[NXOpen.Vector3d, float, FormboardManager.LegacyComponentOrientationConfidenceLevel]:
        """
         Calculates the clocking or twist between the two components along their connecting path.
        
                    The @link FormboardManager::CalculateLegacyComponentClocking FormboardManager::CalculateLegacyComponentClocking@endlink  method uses
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
                
         @return A tuple consisting of (rotationVector, clockingAngle, confidenceLevel). 
         - rotationVector is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink. The rotation vector normal to the curve at the location of the second component's multiport. .
         - clockingAngle is: float. The relative angle between the rotation vector and the second component's multiport's rotate vector. .
         - confidenceLevel is: @link FormboardManager.LegacyComponentOrientationConfidenceLevel NXOpen.Formboard.FormboardManager.LegacyComponentOrientationConfidenceLevel@endlink. High, medium, or low confidence reflecting how many branches the path traversed or whether or not the swept surfaces had problems. .

        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::FaceAnnotationBuilder NXOpen::Formboard::FaceAnnotationBuilder@endlink  object for importing
    ##             CGM or Pattern file geometry and placing it on a drawing sheet or model view.
    ##         
    ##  @return builder (@link FaceAnnotationBuilder NXOpen.Formboard.FaceAnnotationBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateFaceAnnotationBuilder(objectInPart: FormboardManager) -> FaceAnnotationBuilder:
        """
         Creates a @link NXOpen::Formboard::FaceAnnotationBuilder NXOpen::Formboard::FaceAnnotationBuilder@endlink  object for importing
                    CGM or Pattern file geometry and placing it on a drawing sheet or model view.
                
         @return builder (@link FaceAnnotationBuilder NXOpen.Formboard.FaceAnnotationBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::FlipComponentBuilder NXOpen::Formboard::FlipComponentBuilder@endlink  object for
    ##             flipping of formboard component about an axis orthogonal to Z axis to ensure that
    ##             after flipping component lies in XY plane.
    ##         
    ##  @return builder (@link FlipComponentBuilder NXOpen.Formboard.FlipComponentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateFlipComponentBuilder(objectInPart: FormboardManager) -> FlipComponentBuilder:
        """
         Creates a @link NXOpen::Formboard::FlipComponentBuilder NXOpen::Formboard::FlipComponentBuilder@endlink  object for
                    flipping of formboard component about an axis orthogonal to Z axis to ensure that
                    after flipping component lies in XY plane.
                
         @return builder (@link FlipComponentBuilder NXOpen.Formboard.FlipComponentBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::FormboardLayoutBuilder NXOpen::Formboard::FormboardLayoutBuilder@endlink  that can flatten and layout
    ##             new formboard geometry, or modify the layout of existing formboard geometry.
    ##         
    ##  @return builder (@link FormboardLayoutBuilder NXOpen.Formboard.FormboardLayoutBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateLayoutBuilder(objectInPart: FormboardManager) -> FormboardLayoutBuilder:
        """
         Creates a @link NXOpen::Formboard::FormboardLayoutBuilder NXOpen::Formboard::FormboardLayoutBuilder@endlink  that can flatten and layout
                    new formboard geometry, or modify the layout of existing formboard geometry.
                
         @return builder (@link FormboardLayoutBuilder NXOpen.Formboard.FormboardLayoutBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::ObjectAttributeReferenceBuilder NXOpen::Formboard::ObjectAttributeReferenceBuilder@endlink  that creates a tabular note
    ##             object which reads values from the single object selected by the user. It also creates leader for the
    ##             annotation associated with the object selected by user.
    ##         
    ##  @return builder (@link ObjectAttributeReferenceBuilder NXOpen.Formboard.ObjectAttributeReferenceBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateObjectAttributeReferenceBuilder(objectInPart: FormboardManager) -> ObjectAttributeReferenceBuilder:
        """
         Creates a @link NXOpen::Formboard::ObjectAttributeReferenceBuilder NXOpen::Formboard::ObjectAttributeReferenceBuilder@endlink  that creates a tabular note
                    object which reads values from the single object selected by the user. It also creates leader for the
                    annotation associated with the object selected by user.
                
         @return builder (@link ObjectAttributeReferenceBuilder NXOpen.Formboard.ObjectAttributeReferenceBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::OrientBranchBuilder NXOpen::Formboard::OrientBranchBuilder@endlink  object for rotating
    ##             branches in formboard about Z axis.
    ##         
    ##  @return builder (@link OrientBranchBuilder NXOpen.Formboard.OrientBranchBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateOrientBranchBuilder(objectInPart: FormboardManager) -> OrientBranchBuilder:
        """
         Creates a @link NXOpen::Formboard::OrientBranchBuilder NXOpen::Formboard::OrientBranchBuilder@endlink  object for rotating
                    branches in formboard about Z axis.
                
         @return builder (@link OrientBranchBuilder NXOpen.Formboard.OrientBranchBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::PathLengthAnnotationBuilder NXOpen::Formboard::PathLengthAnnotationBuilder@endlink  
    ##  @return builder (@link PathLengthAnnotationBuilder NXOpen.Formboard.PathLengthAnnotationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  The Formboard Path Length annotation. 
    def CreatePathLengthAnnotationBuilder(objectInPart: FormboardManager, annotation: NXOpen.Annotations.Annotation) -> PathLengthAnnotationBuilder:
        """
         Creates a @link NXOpen::Formboard::PathLengthAnnotationBuilder NXOpen::Formboard::PathLengthAnnotationBuilder@endlink  
         @return builder (@link PathLengthAnnotationBuilder NXOpen.Formboard.PathLengthAnnotationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::ShapeSegmentBuilder NXOpen::Formboard::ShapeSegmentBuilder@endlink  that can shape formboard segments.
    ##         
    ##  @return builder (@link ShapeSegmentBuilder NXOpen.Formboard.ShapeSegmentBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  The routing segment to shape. 
    def CreateShapeSegmentBuilder(objectInPart: FormboardManager, segment: NXOpen.Routing.ISegment) -> ShapeSegmentBuilder:
        """
         Creates a @link NXOpen::Formboard::ShapeSegmentBuilder NXOpen::Formboard::ShapeSegmentBuilder@endlink  that can shape formboard segments.
                
         @return builder (@link ShapeSegmentBuilder NXOpen.Formboard.ShapeSegmentBuilder@endlink):  .
        """
        pass
    
    ##  Creates a @link NXOpen::Formboard::UpdateFormboardBuilder NXOpen::Formboard::UpdateFormboardBuilder@endlink  that compares and
    ##             updates formboard geometry to match a modified master 3D harness. 
    ##  @return builder (@link UpdateFormboardBuilder NXOpen.Formboard.UpdateFormboardBuilder@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateUpdateFormboardBuilder(objectInPart: FormboardManager) -> UpdateFormboardBuilder:
        """
         Creates a @link NXOpen::Formboard::UpdateFormboardBuilder NXOpen::Formboard::UpdateFormboardBuilder@endlink  that compares and
                    updates formboard geometry to match a modified master 3D harness. 
         @return builder (@link UpdateFormboardBuilder NXOpen.Formboard.UpdateFormboardBuilder@endlink):  .
        """
        pass
    
    ##  Gets @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  which are associated to the formboard plane.
    ##  @return constraints (@link NXOpen.Positioning.ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def GetFmbdPlaneConstraints(objectInPart: FormboardManager, fmbdPlane: NXOpen.NXObject) -> List[NXOpen.Positioning.ComponentConstraint]:
        """
         Gets @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  which are associated to the formboard plane.
         @return constraints (@link NXOpen.Positioning.ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink):  .
        """
        pass
    
    ##  Hides the formboard constraints. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def HideFormboardConstraints(objectInPart: FormboardManager) -> None:
        """
         Hides the formboard constraints. 
        """
        pass
    
    ##  Returns whether or not the part containing this @link NXOpen::Formboard::FormboardManager NXOpen::Formboard::FormboardManager@endlink  is
    ##           actually a Formboard Drawing part file.  
    ##  @return result (bool):  whether or not the part is a formboard. .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def IsFormboard(route_part: FormboardManager) -> bool:
        """
         Returns whether or not the part containing this @link NXOpen::Formboard::FormboardManager NXOpen::Formboard::FormboardManager@endlink  is
                  actually a Formboard Drawing part file.  
         @return result (bool):  whether or not the part is a formboard. .
        """
        pass
    
    ##  Shows all of the hidden formboard constraints. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def ShowFormboardConstraints(objectInPart: FormboardManager) -> None:
        """
         Shows all of the hidden formboard constraints. 
        """
        pass
    
    ##  Examines the input list of harnesses and stores information from the harnesses into the part containing
    ##          this @link NXOpen::Formboard::FormboardManager NXOpen::Formboard::FormboardManager@endlink .   The harnesses must from a sub-component of
    ##          this part.  The harnesses must form a fully-connected set of geometry.   This method does not actually
    ##          flatten or copy the harness geometry. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  Harnesses to flatten into this part. 
    def StoreHarnessesToFlatten(route_part: FormboardManager, harnesses: List[NXOpen.Routing.Electrical.HarnessDevice]) -> None:
        """
         Examines the input list of harnesses and stores information from the harnesses into the part containing
                 this @link NXOpen::Formboard::FormboardManager NXOpen::Formboard::FormboardManager@endlink .   The harnesses must from a sub-component of
                 this part.  The harnesses must form a fully-connected set of geometry.   This method does not actually
                 flatten or copy the harness geometry. 
        """
        pass
    
import NXOpen
##  Defines the various options for determining the rounded lengths of 
##         formboard geometry during the layout or update process.  <br> Created automatically by containing classes.  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class LayoutLengthOptions(NXOpen.Builder): 
    """ Defines the various options for determining the rounded lengths of 
        formboard geometry during the layout or update process. """


    ##  Methods of rounding lengths for Formboard geometry.  The rounding method determines
    ##             the value of the length in the Formboard by modifying the original length
    ##             values from the 3D harness part file. 
    ##  Lengths are unmodified. 
    class RoundingMethod(Enum):
        """
        Members Include: <Exact> <Nearest> <UpToNearest> <DownToNearest>
        """
        Exact: int
        Nearest: int
        UpToNearest: int
        DownToNearest: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> LayoutLengthOptions.RoundingMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NetlistLengthIncrement
    ##   the connection list length increment.  
    ##     Only used when the  
    ##             @link Formboard::LayoutLengthOptions::NetlistRoundingMethod Formboard::LayoutLengthOptions::NetlistRoundingMethod@endlink  
    ##            is @link Formboard::LayoutLengthOptions::RoundingMethodUpToNearest Formboard::LayoutLengthOptions::RoundingMethodUpToNearest@endlink  or
    ##            @link Formboard::LayoutLengthOptions::RoundingMethodDownToNearest Formboard::LayoutLengthOptions::RoundingMethodDownToNearest@endlink .
    ##         
    ##           
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NetlistLengthIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NetlistLengthIncrement
          the connection list length increment.  
            Only used when the  
                    @link Formboard::LayoutLengthOptions::NetlistRoundingMethod Formboard::LayoutLengthOptions::NetlistRoundingMethod@endlink  
                   is @link Formboard::LayoutLengthOptions::RoundingMethodUpToNearest Formboard::LayoutLengthOptions::RoundingMethodUpToNearest@endlink  or
                   @link Formboard::LayoutLengthOptions::RoundingMethodDownToNearest Formboard::LayoutLengthOptions::RoundingMethodDownToNearest@endlink .
                
                  
         
        """
        pass
    
    ## Getter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) NetlistRoundingMethod
    ##   the rounding method to apply to Connection List lengths.  
    ##       
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return LayoutLengthOptions.RoundingMethod
    @property
    def NetlistRoundingMethod(self) -> LayoutLengthOptions.RoundingMethod:
        """
        Getter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) NetlistRoundingMethod
          the rounding method to apply to Connection List lengths.  
              
         
        """
        pass
    
    ## Setter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) NetlistRoundingMethod

    ##   the rounding method to apply to Connection List lengths.  
    ##       
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @NetlistRoundingMethod.setter
    def NetlistRoundingMethod(self, netlistRoundingMethod: LayoutLengthOptions.RoundingMethod):
        """
        Setter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) NetlistRoundingMethod
          the rounding method to apply to Connection List lengths.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OverstockLengthIncrement
    ##   the overstock length increment.  
    ##     Only used when the 
    ##            @link Formboard::LayoutLengthOptions::OverstockRoundingMethod Formboard::LayoutLengthOptions::OverstockRoundingMethod@endlink  
    ##            is @link Formboard::LayoutLengthOptions::RoundingMethodUpToNearest Formboard::LayoutLengthOptions::RoundingMethodUpToNearest@endlink  or
    ##            @link Formboard::LayoutLengthOptions::RoundingMethodDownToNearest Formboard::LayoutLengthOptions::RoundingMethodDownToNearest@endlink .
    ##              
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OverstockLengthIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OverstockLengthIncrement
          the overstock length increment.  
            Only used when the 
                   @link Formboard::LayoutLengthOptions::OverstockRoundingMethod Formboard::LayoutLengthOptions::OverstockRoundingMethod@endlink  
                   is @link Formboard::LayoutLengthOptions::RoundingMethodUpToNearest Formboard::LayoutLengthOptions::RoundingMethodUpToNearest@endlink  or
                   @link Formboard::LayoutLengthOptions::RoundingMethodDownToNearest Formboard::LayoutLengthOptions::RoundingMethodDownToNearest@endlink .
                     
         
        """
        pass
    
    ## Getter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) OverstockRoundingMethod
    ##   the rounding method to apply to overstock wrapped lengths.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return LayoutLengthOptions.RoundingMethod
    @property
    def OverstockRoundingMethod(self) -> LayoutLengthOptions.RoundingMethod:
        """
        Getter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) OverstockRoundingMethod
          the rounding method to apply to overstock wrapped lengths.  
             
         
        """
        pass
    
    ## Setter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) OverstockRoundingMethod

    ##   the rounding method to apply to overstock wrapped lengths.  
    ##      
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @OverstockRoundingMethod.setter
    def OverstockRoundingMethod(self, overstockRoundingMethod: LayoutLengthOptions.RoundingMethod):
        """
        Setter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) OverstockRoundingMethod
          the rounding method to apply to overstock wrapped lengths.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SegmentLengthIncrement
    ##   the segment length increment.  
    ##     Only used when the
    ##            @link Formboard::LayoutLengthOptions::SegmentRoundingMethod Formboard::LayoutLengthOptions::SegmentRoundingMethod@endlink  
    ##            is @link Formboard::LayoutLengthOptions::RoundingMethodUpToNearest Formboard::LayoutLengthOptions::RoundingMethodUpToNearest@endlink  or
    ##            @link Formboard::LayoutLengthOptions::RoundingMethodDownToNearest Formboard::LayoutLengthOptions::RoundingMethodDownToNearest@endlink .
    ##              
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SegmentLengthIncrement(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SegmentLengthIncrement
          the segment length increment.  
            Only used when the
                   @link Formboard::LayoutLengthOptions::SegmentRoundingMethod Formboard::LayoutLengthOptions::SegmentRoundingMethod@endlink  
                   is @link Formboard::LayoutLengthOptions::RoundingMethodUpToNearest Formboard::LayoutLengthOptions::RoundingMethodUpToNearest@endlink  or
                   @link Formboard::LayoutLengthOptions::RoundingMethodDownToNearest Formboard::LayoutLengthOptions::RoundingMethodDownToNearest@endlink .
                     
         
        """
        pass
    
    ## Getter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) SegmentRoundingMethod
    ##   the rounding method to apply to segment lengths.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return LayoutLengthOptions.RoundingMethod
    @property
    def SegmentRoundingMethod(self) -> LayoutLengthOptions.RoundingMethod:
        """
        Getter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) SegmentRoundingMethod
          the rounding method to apply to segment lengths.  
             
         
        """
        pass
    
    ## Setter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) SegmentRoundingMethod

    ##   the rounding method to apply to segment lengths.  
    ##      
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SegmentRoundingMethod.setter
    def SegmentRoundingMethod(self, segmentRoundingMethod: LayoutLengthOptions.RoundingMethod):
        """
        Setter for property: (@link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink) SegmentRoundingMethod
          the rounding method to apply to segment lengths.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Builder for "object attribute" used in formboard which enbles user to create
##         annotation in drafting functionality. It creates a tabular note and displays
##         object attributes of a single object selected by user.
##      <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreateObjectAttributeReferenceBuilder  NXOpen::Formboard::FormboardManager::CreateObjectAttributeReferenceBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EnumType </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class ObjectAttributeReferenceBuilder(NXOpen.Builder): 
    """ Builder for "object attribute" used in formboard which enbles user to create
        annotation in drafting functionality. It creates a tabular note and displays
        object attributes of a single object selected by user.
    """


    ##  Enum which defines types of leader user wants to associate with the annotation.
    ##             User can either create no leader or one or two leader for the annotation when picking 
    ##             the associated object.
    ##         
    ##  No leader for annotation of selected object.
    class LeaderType(Enum):
        """
        Members Include: <NotSet> <SingleLocation> <StartandEndLocations>
        """
        NotSet: int
        SingleLocation: int
        StartandEndLocations: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ObjectAttributeReferenceBuilder.LeaderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Annotations.LeaderBuilder NXOpen.Annotations.LeaderBuilder@endlink) AnnotLeader
    ##   the @link Annotations::LeaderBuilder Annotations::LeaderBuilder@endlink  for the annotation   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Annotations.LeaderBuilder
    @property
    def AnnotLeader(self) -> NXOpen.Annotations.LeaderBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.LeaderBuilder NXOpen.Annotations.LeaderBuilder@endlink) AnnotLeader
          the @link Annotations::LeaderBuilder Annotations::LeaderBuilder@endlink  for the annotation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) CompOrigin
    ##   the comp origin   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Annotations.OriginBuilder
    @property
    def CompOrigin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) CompOrigin
          the comp origin   
            
         
        """
        pass
    
    ## Getter for property: (@link ObjectAttributeReferenceBuilder.LeaderType NXOpen.Formboard.ObjectAttributeReferenceBuilder.LeaderType@endlink) EnumType
    ##   the enum type   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return ObjectAttributeReferenceBuilder.LeaderType
    @property
    def EnumType(self) -> ObjectAttributeReferenceBuilder.LeaderType:
        """
        Getter for property: (@link ObjectAttributeReferenceBuilder.LeaderType NXOpen.Formboard.ObjectAttributeReferenceBuilder.LeaderType@endlink) EnumType
          the enum type   
            
         
        """
        pass
    
    ## Setter for property: (@link ObjectAttributeReferenceBuilder.LeaderType NXOpen.Formboard.ObjectAttributeReferenceBuilder.LeaderType@endlink) EnumType

    ##   the enum type   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @EnumType.setter
    def EnumType(self, enumType: ObjectAttributeReferenceBuilder.LeaderType):
        """
        Setter for property: (@link ObjectAttributeReferenceBuilder.LeaderType NXOpen.Formboard.ObjectAttributeReferenceBuilder.LeaderType@endlink) EnumType
          the enum type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) ObjectSelection
    ##   the object selected by user to associated annotation   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def ObjectSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) ObjectSelection
          the object selected by user to associated annotation   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Routing
##   Builder for "Orient Branch" operation used in formboard.
##          Allows user to orient the branch by different methods.
##       <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreateOrientBranchBuilder  NXOpen::Formboard::FormboardManager::CreateOrientBranchBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BranchAngleType </term> <description> 
##  
## AnglefromReferenceVector </description> </item> 
## 
## <item><term> 
##  
## RotationAngle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class OrientBranchBuilder(NXOpen.Builder): 
    """  Builder for "Orient Branch" operation used in formboard.
         Allows user to orient the branch by different methods.
     """


    ##  Enum to define the type of method to orient branch. 
    ## method to rotate branch with respect to selected vectors
    class BranchAngleMethod(Enum):
        """
        Members Include: <AnglefromReferenceVector> <Angle> <AlignAxisToVector> <TwoPoints>
        """
        AnglefromReferenceVector: int
        Angle: int
        AlignAxisToVector: int
        TwoPoints: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OrientBranchBuilder.BranchAngleMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link OrientBranchBuilder.BranchAngleMethod NXOpen.Formboard.OrientBranchBuilder.BranchAngleMethod@endlink) BranchAngleType
    ##   the user selected @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink    
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return OrientBranchBuilder.BranchAngleMethod
    @property
    def BranchAngleType(self) -> OrientBranchBuilder.BranchAngleMethod:
        """
        Getter for property: (@link OrientBranchBuilder.BranchAngleMethod NXOpen.Formboard.OrientBranchBuilder.BranchAngleMethod@endlink) BranchAngleType
          the user selected @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink    
            
         
        """
        pass
    
    ## Setter for property: (@link OrientBranchBuilder.BranchAngleMethod NXOpen.Formboard.OrientBranchBuilder.BranchAngleMethod@endlink) BranchAngleType

    ##   the user selected @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink    
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @BranchAngleType.setter
    def BranchAngleType(self, branchAngleType: OrientBranchBuilder.BranchAngleMethod):
        """
        Setter for property: (@link OrientBranchBuilder.BranchAngleMethod NXOpen.Formboard.OrientBranchBuilder.BranchAngleMethod@endlink) BranchAngleType
          the user selected @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FromPoint
    ##   the user selected from point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
    ##   
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  This @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink  is no longer supported.  <br> 

    ## @return NXOpen.Point
    @property
    def FromPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FromPoint
          the user selected from point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
          
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FromPoint

    ##   the user selected from point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
    ##   
    ##            
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  This @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink  is no longer supported.  <br> 

    @FromPoint.setter
    def FromPoint(self, fromPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FromPoint
          the user selected from point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
          
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FromVector
    ##   the user selected from vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
    ##   
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  This builder attribute is no longer required.  <br> 

    ## @return NXOpen.Direction
    @property
    def FromVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FromVector
          the user selected from vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
          
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FromVector

    ##   the user selected from vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
    ##   
    ##            
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  This builder attribute is no longer required.  <br> 

    @FromVector.setter
    def FromVector(self, fromVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) FromVector
          the user selected from vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
          
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RefRotationAngle
    ##   the angle for the rotation of branch when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector @endlink .  
    ##   
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RefRotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RefRotationAngle
          the angle for the rotation of branch when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector @endlink .  
          
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceVector
    ##   the user selected reference vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector @endlink .  
    ##   
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ReferenceVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceVector
          the user selected reference vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector @endlink .  
          
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceVector

    ##   the user selected reference vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector @endlink .  
    ##   
    ##            
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ReferenceVector.setter
    def ReferenceVector(self, referenceVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceVector
          the user selected reference vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAnglefromReferenceVector @endlink .  
          
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationAngle
    ##   the angle for the rotation of branch when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAngle  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAngle@endlink .  
    ##   
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationAngle
          the angle for the rotation of branch when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAngle  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAngle@endlink .  
          
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Routing.RouteObjectCollector NXOpen.Routing.RouteObjectCollector@endlink) SelectBranch
    ##   the user selected branch @link  NXOpen::Routing::ISegment   NXOpen::Routing::ISegment @endlink 
    ##             for rotation.  
    ##   
    ##           
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Routing.RouteObjectCollector
    @property
    def SelectBranch(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: (@link NXOpen.Routing.RouteObjectCollector NXOpen.Routing.RouteObjectCollector@endlink) SelectBranch
          the user selected branch @link  NXOpen::Routing::ISegment   NXOpen::Routing::ISegment @endlink 
                    for rotation.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToPoint
    ##   the user selected to point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
    ##   
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  This @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink  is no longer supported.  <br> 

    ## @return NXOpen.Point
    @property
    def ToPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToPoint
          the user selected to point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
          
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToPoint

    ##   the user selected to point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
    ##   
    ##            
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  This @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink  is no longer supported.  <br> 

    @ToPoint.setter
    def ToPoint(self, toPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ToPoint
          the user selected to point when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodTwoPoints @endlink .  
          
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToVector
    ##   the user selected to vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
    ##   
    ##            
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ToVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToVector
          the user selected to vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
          
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToVector

    ##   the user selected to vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
    ##             @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
    ##   
    ##            
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ToVector.setter
    def ToVector(self, toVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ToVector
          the user selected to vector when @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink  is 
                    @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethodAlignAxisToVector @endlink .  
          
                   
         
        """
        pass
    
    ##  Initializes or resets ( start or stop ) drag operation based on the 
    ##             input branch segment.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.1.  This method is no longer required.  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def InitializeFromSegment(builder: OrientBranchBuilder) -> None:
        """
         Initializes or resets ( start or stop ) drag operation based on the 
                    input branch segment.
                
        """
        pass
    
    ##  Sets the selected branch @link  NXOpen::Routing::ISegment   NXOpen::Routing::ISegment @endlink  when
    ##             a branch is selected by branch method by Routing Object Collector.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  selected seed object 
    def SetBranchSeedObject(builder: OrientBranchBuilder, segmentTag: NXOpen.Routing.ISegment) -> None:
        """
         Sets the selected branch @link  NXOpen::Routing::ISegment   NXOpen::Routing::ISegment @endlink  when
                    a branch is selected by branch method by Routing Object Collector.
                
        """
        pass
    
    ##  Starts the drag operation of selected object. Does nothing if drag has
    ##             already been started.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.1.  This method is no longer required.  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def StartDrag(builder: OrientBranchBuilder) -> None:
        """
         Starts the drag operation of selected object. Does nothing if drag has
                    already been started.
                
        """
        pass
    
    ##  Stop the drag operation of selected object. Does nothing if drag has
    ##             not been started.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.1.  This method is no longer required.  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def StopDrag(builder: OrientBranchBuilder) -> None:
        """
         Stop the drag operation of selected object. Does nothing if drag has
                    not been started.
                
        """
        pass
    
    ##  Suppress the @link NXOpen::Positioning::Constraint  NXOpen::Positioning::Constraint @endlink  associated with selected branch @link  NXOpen::Routing::ISegment   NXOpen::Routing::ISegment @endlink 
    ##             when a branch is selected by branch method by Routing Object Collector.
    ##         
    ## 
    ##   <br>  Created in NX7.5.3  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX7.5.3.  This method is no longer relevant and calls to this can be safely removed.  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def UnSuppressConstraints(builder: OrientBranchBuilder) -> None:
        """
         Suppress the @link NXOpen::Positioning::Constraint  NXOpen::Positioning::Constraint @endlink  associated with selected branch @link  NXOpen::Routing::ISegment   NXOpen::Routing::ISegment @endlink 
                    when a branch is selected by branch method by Routing Object Collector.
                
        """
        pass
    
    ##  Rotates the branch by an appropriate rotation and transformation
    ##             which depends on the @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink 
    ##             selected by user.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.1.  This method is no longer required.  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  angle for rotation 
    def UpdateRotationAngle(builder: OrientBranchBuilder, angle: float) -> None:
        """
         Rotates the branch by an appropriate rotation and transformation
                    which depends on the @link  NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod   NXOpen::Formboard::OrientBranchBuilder::BranchAngleMethod @endlink 
                    selected by user.
                
        """
        pass
    
import NXOpen
import NXOpen.Annotations
import NXOpen.Routing
##  TODO Class documentation  <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreatePathLengthAnnotationBuilder  NXOpen::Formboard::FormboardManager::CreatePathLengthAnnotationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ShowLeadersToggle </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.CustomSymbolScale </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolAspectRatio </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolHeight </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolLength </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolPreferences </term> <description> 
##  
## UseCurrent </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolScale </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolSizeMethod </term> <description> 
##  
## ScaleAndAspectRatio </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX7.5.0  <br> 

class PathLengthAnnotationBuilder(NXOpen.Builder): 
    """ TODO Class documentation """


    ##  TODO: Document the whole type 
    ##  TODO 
    class Types(Enum):
        """
        Members Include: <PointsOnCurves> <RoutingPathLength>
        """
        PointsOnCurves: int
        RoutingPathLength: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PathLengthAnnotationBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) ExpressionName
    ##   the expression name   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def ExpressionName(self) -> str:
        """
        Getter for property: (str) ExpressionName
          the expression name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstEndPoint
    ##   the first end point   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Point
    @property
    def FirstEndPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstEndPoint
          the first end point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstEndPoint

    ##   the first end point   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @FirstEndPoint.setter
    def FirstEndPoint(self, firstEndPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstEndPoint
          the first end point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.LeaderBuilder NXOpen.Annotations.LeaderBuilder@endlink) Leader
    ##   the leader   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Annotations.LeaderBuilder
    @property
    def Leader(self) -> NXOpen.Annotations.LeaderBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.LeaderBuilder NXOpen.Annotations.LeaderBuilder@endlink) Leader
          the leader   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
    ##   the origin   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Annotations.OriginBuilder
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
          the origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Routing.RouteObjectCollector NXOpen.Routing.RouteObjectCollector@endlink) RouteObjectCollector
    ##   the route object collector   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Routing.RouteObjectCollector
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: (@link NXOpen.Routing.RouteObjectCollector NXOpen.Routing.RouteObjectCollector@endlink) RouteObjectCollector
          the route object collector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondEndPoint
    ##   the second end point   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Point
    @property
    def SecondEndPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondEndPoint
          the second end point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondEndPoint

    ##   the second end point   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SecondEndPoint.setter
    def SecondEndPoint(self, secondEndPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondEndPoint
          the second end point   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowLeadersToggle
    ##   the show leaders toggle   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def ShowLeadersToggle(self) -> bool:
        """
        Getter for property: (bool) ShowLeadersToggle
          the show leaders toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowLeadersToggle

    ##   the show leaders toggle   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ShowLeadersToggle.setter
    def ShowLeadersToggle(self, showLeadersToggle: bool):
        """
        Setter for property: (bool) ShowLeadersToggle
          the show leaders toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
    ##   the style   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Annotations.StyleBuilder
    @property
    def Style(self) -> NXOpen.Annotations.StyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.StyleBuilder NXOpen.Annotations.StyleBuilder@endlink) Style
          the style   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.TextWithEditControlsBuilder NXOpen.Annotations.TextWithEditControlsBuilder@endlink) Text
    ##   the u icomp text with symbols0   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.Annotations.TextWithEditControlsBuilder
    @property
    def Text(self) -> NXOpen.Annotations.TextWithEditControlsBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.TextWithEditControlsBuilder NXOpen.Annotations.TextWithEditControlsBuilder@endlink) Text
          the u icomp text with symbols0   
            
         
        """
        pass
    
    ## Getter for property: (@link PathLengthAnnotationBuilder.Types NXOpen.Formboard.PathLengthAnnotationBuilder.Types@endlink) Type
    ##   the type   
    ##     
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return PathLengthAnnotationBuilder.Types
    @property
    def Type(self) -> PathLengthAnnotationBuilder.Types:
        """
        Getter for property: (@link PathLengthAnnotationBuilder.Types NXOpen.Formboard.PathLengthAnnotationBuilder.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ## Setter for property: (@link PathLengthAnnotationBuilder.Types NXOpen.Formboard.PathLengthAnnotationBuilder.Types@endlink) Type

    ##   the type   
    ##     
    ##  
    ## Setter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Type.setter
    def Type(self, type: PathLengthAnnotationBuilder.Types):
        """
        Setter for property: (@link PathLengthAnnotationBuilder.Types NXOpen.Formboard.PathLengthAnnotationBuilder.Types@endlink) Type
          the type   
            
         
        """
        pass
    
    ##  Create builder end points at the RCP locations
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  First Routing control point 
    def CreatePointsAtRcps(builder: PathLengthAnnotationBuilder, firstEndRcp: NXOpen.Routing.ControlPoint, secondEndRcp: NXOpen.Routing.ControlPoint) -> None:
        """
         Create builder end points at the RCP locations
        """
        pass
    
    ##  Create and initialize the Path Length Annotation 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  First end point for the path length annotation 
    def SetPathLengthAnnotationEndPoints(builder: PathLengthAnnotationBuilder, firstEndPoint: NXOpen.Point, secondEndPoint: NXOpen.Point) -> None:
        """
         Create and initialize the Path Length Annotation 
        """
        pass
    
import NXOpen
import NXOpen.Routing
##  Builder for Face Annotation functionality used in formboard. It allows 
##          importing CGM or Pattern file geometry and placing it on a drawing sheet
##          or model view. As a result of this a group of dumb geometry is placed such
##          that defined origin is located at the lower left hand of the bounding box 
##          containing the group of geometry.
##       <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreateShapeSegmentBuilder  NXOpen::Formboard::FormboardManager::CreateShapeSegmentBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class ShapeSegmentBuilder(NXOpen.Builder): 
    """ Builder for Face Annotation functionality used in formboard. It allows 
         importing CGM or Pattern file geometry and placing it on a drawing sheet
         or model view. As a result of this a group of dumb geometry is placed such
         that defined origin is located at the lower left hand of the bounding box 
         containing the group of geometry.
     """


    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def AddRadialPivot(builder: ShapeSegmentBuilder, pivotLocation: NXOpen.Point3d, bendMethod: int, bendValue: float) -> None:
        """
         
                
        """
        pass
    
    ## 
    ##         Adds a point to the existing spline. 
    ##         
    ##  @return pointIndex (int): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def AddSplinePoint(builder: ShapeSegmentBuilder, pointLocation: NXOpen.Point3d) -> int:
        """
        
                Adds a point to the existing spline. 
                
         @return pointIndex (int): .
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def ChangeType(builder: ShapeSegmentBuilder, newType: int) -> None:
        """
         
                
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def CommitCurrentOperation(builder: ShapeSegmentBuilder) -> None:
        """
         
                
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def CreateNewRadialBend(builder: ShapeSegmentBuilder, firstPivot: NXOpen.Point3d, firstBendMethod: int, firstBendValue: float, secondPivot: NXOpen.Point3d, secondBendMethod: int, secondBendValue: float) -> None:
        """
         
                
        """
        pass
    
    ## 
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def CreateNewSpline(builder: ShapeSegmentBuilder, anchorLocation: NXOpen.Point3d, firstPoint: NXOpen.Point3d, secondPoint: NXOpen.Point3d) -> None:
        """
        
                
        """
        pass
    
    ##  
    ##         
    ##  @return A tuple consisting of (anchorSeg, anchorRcp, angle). 
    ##  - anchorSeg is: @link NXOpen.Routing.ISegment NXOpen.Routing.ISegment@endlink. .
    ##  - anchorRcp is: @link NXOpen.Routing.ControlPoint NXOpen.Routing.ControlPoint@endlink. .
    ##  - angle is: float. .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def GetLineData(builder: ShapeSegmentBuilder) -> Tuple[NXOpen.Routing.ISegment, NXOpen.Routing.ControlPoint, float]:
        """
         
                
         @return A tuple consisting of (anchorSeg, anchorRcp, angle). 
         - anchorSeg is: @link NXOpen.Routing.ISegment NXOpen.Routing.ISegment@endlink. .
         - anchorRcp is: @link NXOpen.Routing.ControlPoint NXOpen.Routing.ControlPoint@endlink. .
         - angle is: float. .

        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def NewSegment(builder: ShapeSegmentBuilder, newSegment: NXOpen.Routing.ISegment) -> None:
        """
         
                
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def RemoveRadialPivot(builder: ShapeSegmentBuilder, pivotIndex: int) -> None:
        """
         
                
        """
        pass
    
    ## 
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def RemoveSplinePoint(builder: ShapeSegmentBuilder, pointIndex: int) -> None:
        """
        
                
        """
        pass
    
    ##  Sets the active view for the shape operation.
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def SetActiveView(builder: ShapeSegmentBuilder, view: NXOpen.TaggedObject) -> None:
        """
         Sets the active view for the shape operation.
                
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def SwapAnchorEnd(builder: ShapeSegmentBuilder) -> None:
        """
         
                
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def UpdateLineAngleVec(builder: ShapeSegmentBuilder, newDir: NXOpen.Vector3d) -> None:
        """
         
                
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def UpdateRadialPivot(builder: ShapeSegmentBuilder, pivotIndex: int, newLocation: NXOpen.Point3d, newBendMethod: int, newBendValue: float) -> None:
        """
         
                
        """
        pass
    
    ##  
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def UpdateSplinePoint(builder: ShapeSegmentBuilder, pointIndex: int, pointLocation: NXOpen.Point3d, inDrag: bool) -> None:
        """
         
                
        """
        pass
    
import NXOpen
## 
##         Defines a discrepancy object which contains information about a specific
##         difference between the formboard drawing and the 3D harness model.
##     
## 
##   <br>  Created in NX7.5.0  <br> 

class UpdateDiscrepancy(NXOpen.TransientObject): 
    """
        Defines a discrepancy object which contains information about a specific
        difference between the formboard drawing and the 3D harness model.
    """


    ##  Specifies the type of objects involved in the discrepancy. 
    ##  Unknown type. 
    class ObjectType(Enum):
        """
        Members Include: <Unknown> <Rcp> <Segment> <Clip> <Component> <Harness> <Wire> <Cable> <Shield> <Connector> <Device> <Overstock> <Fillerstock> <FittingOverstock>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UpdateDiscrepancy.ObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The general type of the discrepancy. 
    ##  Unknown type, not valid. 
    class Type(Enum):
        """
        Members Include: <Unknown> <Missing> <Extra> <Modified>
        """
        Unknown: int
        Missing: int
        Extra: int
        Modified: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UpdateDiscrepancy.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Description
    ##   the description string of the discrepancy.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the description string of the discrepancy.  
             
         
        """
        pass
    
    ## Getter for property: (@link UpdateDiscrepancy.ObjectType NXOpen.Formboard.UpdateDiscrepancy.ObjectType@endlink) DiscrepancyObjectType
    ##   the type of object referenced by the discrepancy.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return UpdateDiscrepancy.ObjectType
    @property
    def DiscrepancyObjectType(self) -> UpdateDiscrepancy.ObjectType:
        """
        Getter for property: (@link UpdateDiscrepancy.ObjectType NXOpen.Formboard.UpdateDiscrepancy.ObjectType@endlink) DiscrepancyObjectType
          the type of object referenced by the discrepancy.  
             
         
        """
        pass
    
    ## Getter for property: (@link UpdateDiscrepancy.Type NXOpen.Formboard.UpdateDiscrepancy.Type@endlink) DiscrepancyType
    ##   the general type of the discrepancy.  
    ##      
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return UpdateDiscrepancy.Type
    @property
    def DiscrepancyType(self) -> UpdateDiscrepancy.Type:
        """
        Getter for property: (@link UpdateDiscrepancy.Type NXOpen.Formboard.UpdateDiscrepancy.Type@endlink) DiscrepancyType
          the general type of the discrepancy.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FormboardObject
    ##   the object in the 2D formboard referenced by the discrepancy.  
    ##    This may
    ##           be NULL depending on the type of the discrepancy.  
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def FormboardObject(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) FormboardObject
          the object in the 2D formboard referenced by the discrepancy.  
           This may
                  be NULL depending on the type of the discrepancy.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) HarnessObject
    ##   the object in the 3D harness referenced by the discrepancy.  
    ##     This may
    ##           be NULL depending on the type of the discrepancy.  
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def HarnessObject(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) HarnessObject
          the object in the 3D harness referenced by the discrepancy.  
            This may
                  be NULL depending on the type of the discrepancy.  
         
        """
        pass
    
    ##  Frees the memory associated with this object. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object. 
        """
        pass
    
import NXOpen
import NXOpen.Routing.Electrical
##  Class that performs the "update" of Formboard geometry.  
##       <br> To create a new instance of this class, use @link NXOpen::Formboard::FormboardManager::CreateUpdateFormboardBuilder  NXOpen::Formboard::FormboardManager::CreateUpdateFormboardBuilder @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class UpdateFormboardBuilder(NXOpen.Builder): 
    """ Class that performs the "update" of Formboard geometry.  
     """


    ## Getter for property: (@link LayoutLengthOptions NXOpen.Formboard.LayoutLengthOptions@endlink) LengthOptions
    ##   the length options for the update operation.  
    ##       
    ##  
    ## Getter License requirements: routing_harness ("Routing Harness")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return LayoutLengthOptions
    @property
    def LengthOptions(self) -> LayoutLengthOptions:
        """
        Getter for property: (@link LayoutLengthOptions NXOpen.Formboard.LayoutLengthOptions@endlink) LengthOptions
          the length options for the update operation.  
              
         
        """
        pass
    
    ##  Creates bends for radial bends after all discrepanices have been fixed. This routine
    ##             should be called in conjunction with RemoveBendsOfRadialBends.
    ##         
    ## 
    ##   <br>  Created in NX7.5.5  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    def CreateBendsOfRadialBends(builder: UpdateFormboardBuilder) -> None:
        """
         Creates bends for radial bends after all discrepanices have been fixed. This routine
                    should be called in conjunction with RemoveBendsOfRadialBends.
                
        """
        pass
    
    ##  Once the mapping has been determined, this method can find any discrepancies
    ##            between the 3D harness and the formboard.  
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def DetermineDiscrepancies(builder: UpdateFormboardBuilder) -> None:
        """
         Once the mapping has been determined, this method can find any discrepancies
                   between the 3D harness and the formboard.  
        """
        pass
    
    ##  Compute the mapping between the data in the formboard and the data in the
    ##            3D harness.  This method can take a very long time to execute. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def FindMapping(builder: UpdateFormboardBuilder) -> None:
        """
         Compute the mapping between the data in the formboard and the data in the
                   3D harness.  This method can take a very long time to execute. 
        """
        pass
    
    ##  Returns the discrepancy at the given index.  The index must be
    ##             0 to @link Formboard::UpdateFormboardBuilder::GetNumberOfDiscrepancies Formboard::UpdateFormboardBuilder::GetNumberOfDiscrepancies@endlink .
    ##             
    ##  @return discrep (@link UpdateDiscrepancy NXOpen.Formboard.UpdateDiscrepancy@endlink):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def GetDiscrepancy(builder: UpdateFormboardBuilder, index: int) -> UpdateDiscrepancy:
        """
         Returns the discrepancy at the given index.  The index must be
                    0 to @link Formboard::UpdateFormboardBuilder::GetNumberOfDiscrepancies Formboard::UpdateFormboardBuilder::GetNumberOfDiscrepancies@endlink .
                    
         @return discrep (@link UpdateDiscrepancy NXOpen.Formboard.UpdateDiscrepancy@endlink):  .
        """
        pass
    
    ##  Gets the 3D harness part file to compare the formboard against. 
    ##  @return harnessPart (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def GetHarnessPart(builder: UpdateFormboardBuilder) -> NXOpen.Part:
        """
         Gets the 3D harness part file to compare the formboard against. 
         @return harnessPart (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Returns the number of discrepancies discovered by the 
    ##           @link Formboard::UpdateFormboardBuilder::DetermineDiscrepancies Formboard::UpdateFormboardBuilder::DetermineDiscrepancies@endlink . 
    ##  @return numDiscreps (int):  .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def GetNumberOfDiscrepancies(builder: UpdateFormboardBuilder) -> int:
        """
         Returns the number of discrepancies discovered by the 
                  @link Formboard::UpdateFormboardBuilder::DetermineDiscrepancies Formboard::UpdateFormboardBuilder::DetermineDiscrepancies@endlink . 
         @return numDiscreps (int):  .
        """
        pass
    
    ##  Removes bends in all radial bends and replaces them with a linear segment
    ##             going from the anchor to the free RCP of each radial bend. This is done before
    ##             fixing discrepancies because presence of bends in radial bend causes problems.
    ##             The bends of radial bends are recreated after the discrepancies have been fixed
    ##             using CreateBendsOfRadialBends
    ##         
    ## 
    ##   <br>  Created in NX7.5.5  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    @staticmethod
    def RemoveBendsOfRadialBends(builder: UpdateFormboardBuilder) -> None:
        """
         Removes bends in all radial bends and replaces them with a linear segment
                    going from the anchor to the free RCP of each radial bend. This is done before
                    fixing discrepancies because presence of bends in radial bend causes problems.
                    The bends of radial bends are recreated after the discrepancies have been fixed
                    using CreateBendsOfRadialBends
                
        """
        pass
    
    ##  Sets the 3D harness part file to compare the formboard against. This clears
    ##           any discrepancies that have been discovered against the previous harness
    ##           part.  
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  
    def SetHarnessPart(builder: UpdateFormboardBuilder, harnessPart: NXOpen.Part) -> None:
        """
         Sets the 3D harness part file to compare the formboard against. This clears
                  any discrepancies that have been discovered against the previous harness
                  part.  
        """
        pass
    
    ##  Sets the harnesses within the harness part that the formboard must be 
    ##           compared with. 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: routing_harness ("Routing Harness")
    ##  Harnesses to compare against. 
    def SetHarnesses(builder: UpdateFormboardBuilder, harnesses: List[NXOpen.Routing.Electrical.HarnessDevice]) -> None:
        """
         Sets the harnesses within the harness part that the formboard must be 
                  compared with. 
        """
        pass
    
## @package NXOpen.Formboard
## Classes, Enums and Structs under NXOpen.Formboard namespace

##  @link FaceAnnotationBuilderDrwDestination NXOpen.Formboard.FaceAnnotationBuilderDrwDestination @endlink is an alias for @link FaceAnnotationBuilder.DrwDestination NXOpen.Formboard.FaceAnnotationBuilder.DrwDestination@endlink
FaceAnnotationBuilderDrwDestination = FaceAnnotationBuilder.DrwDestination


##  @link FaceAnnotationBuilderTypes NXOpen.Formboard.FaceAnnotationBuilderTypes @endlink is an alias for @link FaceAnnotationBuilder.Types NXOpen.Formboard.FaceAnnotationBuilder.Types@endlink
FaceAnnotationBuilderTypes = FaceAnnotationBuilder.Types


##  @link FlipComponentBuilderAxisType NXOpen.Formboard.FlipComponentBuilderAxisType @endlink is an alias for @link FlipComponentBuilder.AxisType NXOpen.Formboard.FlipComponentBuilder.AxisType@endlink
FlipComponentBuilderAxisType = FlipComponentBuilder.AxisType


##  @link FormboardLayoutBuilderBranchAngle NXOpen.Formboard.FormboardLayoutBuilderBranchAngle @endlink is an alias for @link FormboardLayoutBuilder.BranchAngle NXOpen.Formboard.FormboardLayoutBuilder.BranchAngle@endlink
FormboardLayoutBuilderBranchAngle = FormboardLayoutBuilder.BranchAngle


##  @link FormboardLayoutBuilderBranchShape NXOpen.Formboard.FormboardLayoutBuilderBranchShape @endlink is an alias for @link FormboardLayoutBuilder.BranchShape NXOpen.Formboard.FormboardLayoutBuilder.BranchShape@endlink
FormboardLayoutBuilderBranchShape = FormboardLayoutBuilder.BranchShape


##  @link FormboardLayoutBuilderMainRunType NXOpen.Formboard.FormboardLayoutBuilderMainRunType @endlink is an alias for @link FormboardLayoutBuilder.MainRunType NXOpen.Formboard.FormboardLayoutBuilder.MainRunType@endlink
FormboardLayoutBuilderMainRunType = FormboardLayoutBuilder.MainRunType


##  @link FormboardManagerLegacyComponentOrientationConfidenceLevel NXOpen.Formboard.FormboardManagerLegacyComponentOrientationConfidenceLevel @endlink is an alias for @link FormboardManager.LegacyComponentOrientationConfidenceLevel NXOpen.Formboard.FormboardManager.LegacyComponentOrientationConfidenceLevel@endlink
FormboardManagerLegacyComponentOrientationConfidenceLevel = FormboardManager.LegacyComponentOrientationConfidenceLevel


##  @link FormboardManagerLegacyComponentOrientationDisplayStyle NXOpen.Formboard.FormboardManagerLegacyComponentOrientationDisplayStyle @endlink is an alias for @link FormboardManager.LegacyComponentOrientationDisplayStyle NXOpen.Formboard.FormboardManager.LegacyComponentOrientationDisplayStyle@endlink
FormboardManagerLegacyComponentOrientationDisplayStyle = FormboardManager.LegacyComponentOrientationDisplayStyle


##  @link LayoutLengthOptionsRoundingMethod NXOpen.Formboard.LayoutLengthOptionsRoundingMethod @endlink is an alias for @link LayoutLengthOptions.RoundingMethod NXOpen.Formboard.LayoutLengthOptions.RoundingMethod@endlink
LayoutLengthOptionsRoundingMethod = LayoutLengthOptions.RoundingMethod


##  @link ObjectAttributeReferenceBuilderLeaderType NXOpen.Formboard.ObjectAttributeReferenceBuilderLeaderType @endlink is an alias for @link ObjectAttributeReferenceBuilder.LeaderType NXOpen.Formboard.ObjectAttributeReferenceBuilder.LeaderType@endlink
ObjectAttributeReferenceBuilderLeaderType = ObjectAttributeReferenceBuilder.LeaderType


##  @link OrientBranchBuilderBranchAngleMethod NXOpen.Formboard.OrientBranchBuilderBranchAngleMethod @endlink is an alias for @link OrientBranchBuilder.BranchAngleMethod NXOpen.Formboard.OrientBranchBuilder.BranchAngleMethod@endlink
OrientBranchBuilderBranchAngleMethod = OrientBranchBuilder.BranchAngleMethod


##  @link PathLengthAnnotationBuilderTypes NXOpen.Formboard.PathLengthAnnotationBuilderTypes @endlink is an alias for @link PathLengthAnnotationBuilder.Types NXOpen.Formboard.PathLengthAnnotationBuilder.Types@endlink
PathLengthAnnotationBuilderTypes = PathLengthAnnotationBuilder.Types


##  @link UpdateDiscrepancyObjectType NXOpen.Formboard.UpdateDiscrepancyObjectType @endlink is an alias for @link UpdateDiscrepancy.ObjectType NXOpen.Formboard.UpdateDiscrepancy.ObjectType@endlink
UpdateDiscrepancyObjectType = UpdateDiscrepancy.ObjectType


##  @link UpdateDiscrepancyType NXOpen.Formboard.UpdateDiscrepancyType @endlink is an alias for @link UpdateDiscrepancy.Type NXOpen.Formboard.UpdateDiscrepancy.Type@endlink
UpdateDiscrepancyType = UpdateDiscrepancy.Type


