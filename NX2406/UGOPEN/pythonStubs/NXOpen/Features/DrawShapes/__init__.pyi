from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::CurveFromStrokeData   NXOpen::Features::DrawShapes::CurveFromStrokeData @endlink 
##         allowing user to define curve using drag gesture.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateCurveFromStrokeData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateCurveFromStrokeData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanMergeConnectedStrokes </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## DetectionSensitivity </term> <description> 
##  
## Standard </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class CurveFromStrokeData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.CurveFromStrokeData </ja_class>
        allowing user to define curve using drag gesture.
    """


    ##  Detection sensitivity options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Low</term><description> 
    ##  For creating primitives, the strokes can have large deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather smooth with larger deviations to the stroke. </description> </item><item><term> 
    ## Standard</term><description> 
    ##  For creating primitives, the strokes can have medium deviations from an ideal circle, line, etc.; For creating splines, the output spline will be a tradeoff between smoothness and accuracy to the stroke. </description> </item><item><term> 
    ## High</term><description> 
    ##  For creating primitives, the strokes can have only small deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather bumpy with small deviations to the stroke.</description> </item></list>
    class DetectionSensitivityOption(Enum):
        """
        Members Include: <Low> <Standard> <High>
        """
        Low: int
        Standard: int
        High: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CurveFromStrokeData.DetectionSensitivityOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanCreatePrimitives
    ##  Returns the value indicating if primitive curve should be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanCreatePrimitives(self) -> bool:
        """
        Getter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanCreatePrimitives

    ##  Returns the value indicating if primitive curve should be created   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanCreatePrimitives.setter
    def CanCreatePrimitives(self, canCreatePrimitive: bool):
        """
        Setter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    
    ## Getter for property: (bool) CanMergeConnectedStrokes
    ##  Returns the flag indicating if selected strokes should be merged.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanMergeConnectedStrokes(self) -> bool:
        """
        Getter for property: (bool) CanMergeConnectedStrokes
         Returns the flag indicating if selected strokes should be merged.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CanMergeConnectedStrokes

    ##  Returns the flag indicating if selected strokes should be merged.  
    ##      
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanMergeConnectedStrokes.setter
    def CanMergeConnectedStrokes(self, canMergeConnectedStrokes: bool):
        """
        Setter for property: (bool) CanMergeConnectedStrokes
         Returns the flag indicating if selected strokes should be merged.  
             
         
        """
        pass
    
    ## Getter for property: (@link CurveFromStrokeData.DetectionSensitivityOption NXOpen.Features.DrawShapes.CurveFromStrokeData.DetectionSensitivityOption@endlink) DetectionSensitivity
    ##  Returns the value indicating detection sensitivity.  
    ##    The smaller the sensitivity,
    ##             the more accurate the stroke must be to be recognized as primitive.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return CurveFromStrokeData.DetectionSensitivityOption
    @property
    def DetectionSensitivity(self) -> CurveFromStrokeData.DetectionSensitivityOption:
        """
        Getter for property: (@link CurveFromStrokeData.DetectionSensitivityOption NXOpen.Features.DrawShapes.CurveFromStrokeData.DetectionSensitivityOption@endlink) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    
    ## Setter for property: (@link CurveFromStrokeData.DetectionSensitivityOption NXOpen.Features.DrawShapes.CurveFromStrokeData.DetectionSensitivityOption@endlink) DetectionSensitivity

    ##  Returns the value indicating detection sensitivity.  
    ##    The smaller the sensitivity,
    ##             the more accurate the stroke must be to be recognized as primitive.   
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DetectionSensitivity.setter
    def DetectionSensitivity(self, detectionSensitivity: CurveFromStrokeData.DetectionSensitivityOption):
        """
        Setter for property: (@link CurveFromStrokeData.DetectionSensitivityOption NXOpen.Features.DrawShapes.CurveFromStrokeData.DetectionSensitivityOption@endlink) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Strokes
    ##  Returns the object enabling drawing of the curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Strokes(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Strokes
         Returns the object enabling drawing of the curve   
            
         
        """
        pass
    
    ##  Distance tolerance used to decide if two strokes should be merged. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ## <param name="mergeTolerance"> (float) </param>
    def SetMergeTolerance(self, mergeTolerance: float) -> None:
        """
         Distance tolerance used to decide if two strokes should be merged. 
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::DeleteData   NXOpen::Features::DrawShapes::DeleteData @endlink 
##         allowing user to delete strokes and curves.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDeleteData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDeleteData @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class DeleteData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.DeleteData </ja_class>
        allowing user to delete strokes and curves.
    """


    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Objects
    ##  Returns the objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def Objects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Objects
         Returns the objects   
            
         
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::DivideBuilder   NXOpen::Features::DrawShapes::DivideBuilder @endlink 
##             allowing user to divide curves.
##          <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDivideBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDivideBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DivideBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.DivideBuilder </ja_class>
            allowing user to divide curves.
        """


    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Targets
    ##  Returns the curves to be divided   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def Targets(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Targets
         Returns the curves to be divided   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents @link  NXOpen::Features::DrawShapes::DrawCurveData   NXOpen::Features::DrawShapes::DrawCurveData @endlink 
##         allowing user to define curve using drag gesture.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawCurveData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawCurveData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanDrawOnNearestFace </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## DetectionSensitivity </term> <description> 
##  
## Standard </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class DrawCurveData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.DrawCurveData </ja_class>
        allowing user to define curve using drag gesture.
    """


    ##  Detection sensitivity options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Low</term><description> 
    ##  For creating primitives, the strokes can have large deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather smooth with larger deviations to the stroke. </description> </item><item><term> 
    ## Standard</term><description> 
    ##  For creating primitives, the strokes can have medium deviations from an ideal circle, line, etc.; For creating splines, the output spline will be a tradeoff between smoothness and accuracy to the stroke.</description> </item><item><term> 
    ## High</term><description> 
    ##  For creating primitives, the strokes can have only small deviations from an ideal circle, line, etc.; For creating splines, the output spline will be rather bumpy with small deviations to the stroke.</description> </item></list>
    class DetectionSensitivityOption(Enum):
        """
        Members Include: <Low> <Standard> <High>
        """
        Low: int
        Standard: int
        High: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawCurveData.DetectionSensitivityOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   Snap options used during curve drawing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  No snapping. </description> </item><item><term> 
    ## Curve</term><description> 
    ##  Snap to point on curve, including curve end points .</description> </item><item><term> 
    ## CurveWithTangent</term><description> 
    ##  Snap to point on curve with tangent continuity.</description> </item><item><term> 
    ## ParallelCurve</term><description> 
    ##  Snap parallel to curve or tangent continuous string of curves.</description> </item><item><term> 
    ## IsoparametricGrid</term><description> 
    ##  Snap to isoparametric grid.</description> </item></list>
    class SnapToOptions(Enum):
        """
        Members Include: <NotSet> <Curve> <CurveWithTangent> <ParallelCurve> <IsoparametricGrid>
        """
        NotSet: int
        Curve: int
        CurveWithTangent: int
        ParallelCurve: int
        IsoparametricGrid: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawCurveData.SnapToOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   Snap options used during curve drawing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  No snapping. </description> </item><item><term> 
    ## CurveEndPoints</term><description> 
    ##  Snap to curve end points.</description> </item><item><term> 
    ## IsoparametricGrid</term><description> 
    ##  Snap to isoparametric grid.</description> </item></list>
    class SnappingOption(Enum):
        """
        Members Include: <NotSet> <CurveEndPoints> <IsoparametricGrid>
        """
        NotSet: int
        CurveEndPoints: int
        IsoparametricGrid: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawCurveData.SnappingOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanCreatePrimitives
    ##  Returns the value indicating if primitive curve should be created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanCreatePrimitives(self) -> bool:
        """
        Getter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanCreatePrimitives

    ##  Returns the value indicating if primitive curve should be created   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanCreatePrimitives.setter
    def CanCreatePrimitives(self, canCreatePrimitive: bool):
        """
        Setter for property: (bool) CanCreatePrimitives
         Returns the value indicating if primitive curve should be created   
            
         
        """
        pass
    
    ## Getter for property: (bool) CanDrawOnNearestFace
    ##  Returns the flag indicating if curves should be created only on the nearest face in view direction and 
    ##             not on faces on the back of a body.  
    ##    This option decreases the drawing performance.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanDrawOnNearestFace(self) -> bool:
        """
        Getter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if curves should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
        """
        pass
    
    ## Setter for property: (bool) CanDrawOnNearestFace

    ##  Returns the flag indicating if curves should be created only on the nearest face in view direction and 
    ##             not on faces on the back of a body.  
    ##    This option decreases the drawing performance.   
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanDrawOnNearestFace.setter
    def CanDrawOnNearestFace(self, doNearFaceProjection: bool):
        """
        Setter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if curves should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color   
            
         
        """
        pass
    
    ## Getter for property: (@link DrawCurveData.DetectionSensitivityOption NXOpen.Features.DrawShapes.DrawCurveData.DetectionSensitivityOption@endlink) DetectionSensitivity
    ##  Returns the value indicating detection sensitivity.  
    ##    The smaller the sensitivity,
    ##             the more accurate the stroke must be to be recognized as primitive.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return DrawCurveData.DetectionSensitivityOption
    @property
    def DetectionSensitivity(self) -> DrawCurveData.DetectionSensitivityOption:
        """
        Getter for property: (@link DrawCurveData.DetectionSensitivityOption NXOpen.Features.DrawShapes.DrawCurveData.DetectionSensitivityOption@endlink) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    
    ## Setter for property: (@link DrawCurveData.DetectionSensitivityOption NXOpen.Features.DrawShapes.DrawCurveData.DetectionSensitivityOption@endlink) DetectionSensitivity

    ##  Returns the value indicating detection sensitivity.  
    ##    The smaller the sensitivity,
    ##             the more accurate the stroke must be to be recognized as primitive.   
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DetectionSensitivity.setter
    def DetectionSensitivity(self, detectionSensitivity: DrawCurveData.DetectionSensitivityOption):
        """
        Setter for property: (@link DrawCurveData.DetectionSensitivityOption NXOpen.Features.DrawShapes.DrawCurveData.DetectionSensitivityOption@endlink) DetectionSensitivity
         Returns the value indicating detection sensitivity.  
           The smaller the sensitivity,
                    the more accurate the stroke must be to be recognized as primitive.   
         
        """
        pass
    
    ## Getter for property: (bool) OversketchExistingCurves
    ##  Returns the value indicating if existing curves should be over sketched   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def OversketchExistingCurves(self) -> bool:
        """
        Getter for property: (bool) OversketchExistingCurves
         Returns the value indicating if existing curves should be over sketched   
            
         
        """
        pass
    
    ## Setter for property: (bool) OversketchExistingCurves

    ##  Returns the value indicating if existing curves should be over sketched   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @OversketchExistingCurves.setter
    def OversketchExistingCurves(self, oversketchExistingCurves: bool):
        """
        Setter for property: (bool) OversketchExistingCurves
         Returns the value indicating if existing curves should be over sketched   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ParallelCurveTargets
    ##  Returns the target curves of parallel curve drawing   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ParallelCurveTargets(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ParallelCurveTargets
         Returns the target curves of parallel curve drawing   
            
         
        """
        pass
    
    ## Getter for property: (@link DrawCurveData.SnapToOptions NXOpen.Features.DrawShapes.DrawCurveData.SnapToOptions@endlink) SnapToOption
    ##  Returns the value indicating snapping option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DrawCurveData.SnapToOptions
    @property
    def SnapToOption(self) -> DrawCurveData.SnapToOptions:
        """
        Getter for property: (@link DrawCurveData.SnapToOptions NXOpen.Features.DrawShapes.DrawCurveData.SnapToOptions@endlink) SnapToOption
         Returns the value indicating snapping option.  
             
         
        """
        pass
    
    ## Setter for property: (@link DrawCurveData.SnapToOptions NXOpen.Features.DrawShapes.DrawCurveData.SnapToOptions@endlink) SnapToOption

    ##  Returns the value indicating snapping option.  
    ##      
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SnapToOption.setter
    def SnapToOption(self, snapping: DrawCurveData.SnapToOptions):
        """
        Setter for property: (@link DrawCurveData.SnapToOptions NXOpen.Features.DrawShapes.DrawCurveData.SnapToOptions@endlink) SnapToOption
         Returns the value indicating snapping option.  
             
         
        """
        pass
    
    ## Getter for property: (@link DrawCurveData.SnappingOption NXOpen.Features.DrawShapes.DrawCurveData.SnappingOption@endlink) Snapping
    ##  Returns the value indicating snapping option.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return DrawCurveData.SnappingOption
    @property
    def Snapping(self) -> DrawCurveData.SnappingOption:
        """
        Getter for property: (@link DrawCurveData.SnappingOption NXOpen.Features.DrawShapes.DrawCurveData.SnappingOption@endlink) Snapping
         Returns the value indicating snapping option.  
             
         
        """
        pass
    
    ## Setter for property: (@link DrawCurveData.SnappingOption NXOpen.Features.DrawShapes.DrawCurveData.SnappingOption@endlink) Snapping

    ##  Returns the value indicating snapping option.  
    ##      
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Snapping.setter
    def Snapping(self, snapping: DrawCurveData.SnappingOption):
        """
        Setter for property: (@link DrawCurveData.SnappingOption NXOpen.Features.DrawShapes.DrawCurveData.SnappingOption@endlink) Snapping
         Returns the value indicating snapping option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) StrokeGesture
    ##  Returns the object enabling drawing of the curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.StrokeGestureData
    @property
    def StrokeGesture(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) StrokeGesture
         Returns the object enabling drawing of the curve   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
    ##  Returns the thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def Thickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
         Returns the thickness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness

    ##  Returns the thickness   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Thickness.setter
    def Thickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
         Returns the thickness   
            
         
        """
        pass
    
    ##  Distance tolerance used to decide if newly drawn curve is considered as over-sketched curve on pre-existing curve. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ## <param name="overSketchTolerance"> (float) </param>
    def SetOverSketchTolerance(self, overSketchTolerance: float) -> None:
        """
         Distance tolerance used to decide if newly drawn curve is considered as over-sketched curve on pre-existing curve. 
        """
        pass
    
import NXOpen
##  Collection of Draw Shape tools.  <br> To obtain an instance of this class, refer to @link NXOpen::Features::FreeformCurveCollection  NXOpen::Features::FreeformCurveCollection @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class DrawShapeCollection(NXOpen.Object): 
    """ Collection of Draw Shape tools. """


    ##  Creates a @link NXOpen::Features::DrawShapes::CurveFromStrokeData NXOpen::Features::DrawShapes::CurveFromStrokeData@endlink  
    ##  @return builder (@link CurveFromStrokeData NXOpen.Features.DrawShapes.CurveFromStrokeData@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateCurveFromStrokeData(self) -> CurveFromStrokeData:
        """
         Creates a @link NXOpen::Features::DrawShapes::CurveFromStrokeData NXOpen::Features::DrawShapes::CurveFromStrokeData@endlink  
         @return builder (@link CurveFromStrokeData NXOpen.Features.DrawShapes.CurveFromStrokeData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::DeleteData NXOpen::Features::DrawShapes::DeleteData@endlink  
    ##  @return builder (@link DeleteData NXOpen.Features.DrawShapes.DeleteData@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateDeleteData(self) -> DeleteData:
        """
         Creates a @link NXOpen::Features::DrawShapes::DeleteData NXOpen::Features::DrawShapes::DeleteData@endlink  
         @return builder (@link DeleteData NXOpen.Features.DrawShapes.DeleteData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::DivideBuilder NXOpen::Features::DrawShapes::DivideBuilder@endlink  
    ##  @return builder (@link DivideBuilder NXOpen.Features.DrawShapes.DivideBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateDivideBuilder(self) -> DivideBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::DivideBuilder NXOpen::Features::DrawShapes::DivideBuilder@endlink  
         @return builder (@link DivideBuilder NXOpen.Features.DrawShapes.DivideBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::DrawCurveData NXOpen::Features::DrawShapes::DrawCurveData@endlink  
    ##  @return builder (@link DrawCurveData NXOpen.Features.DrawShapes.DrawCurveData@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateDrawCurveData(self) -> DrawCurveData:
        """
         Creates a @link NXOpen::Features::DrawShapes::DrawCurveData NXOpen::Features::DrawShapes::DrawCurveData@endlink  
         @return builder (@link DrawCurveData NXOpen.Features.DrawShapes.DrawCurveData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::DrawShapeData NXOpen::Features::DrawShapes::DrawShapeData@endlink  
    ##  @return builder (@link DrawShapeData NXOpen.Features.DrawShapes.DrawShapeData@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateDrawShapeData(self) -> DrawShapeData:
        """
         Creates a @link NXOpen::Features::DrawShapes::DrawShapeData NXOpen::Features::DrawShapes::DrawShapeData@endlink  
         @return builder (@link DrawShapeData NXOpen.Features.DrawShapes.DrawShapeData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::DrawStrokeData NXOpen::Features::DrawShapes::DrawStrokeData@endlink  
    ##  @return builder (@link DrawStrokeData NXOpen.Features.DrawShapes.DrawStrokeData@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateDrawStrokeData(self) -> DrawStrokeData:
        """
         Creates a @link NXOpen::Features::DrawShapes::DrawStrokeData NXOpen::Features::DrawShapes::DrawStrokeData@endlink  
         @return builder (@link DrawStrokeData NXOpen.Features.DrawShapes.DrawStrokeData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::EditCurveBuilder NXOpen::Features::DrawShapes::EditCurveBuilder@endlink  
    ##  @return builder (@link EditCurveBuilder NXOpen.Features.DrawShapes.EditCurveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ## <param name="curveToEdit"> (@link NXOpen.Curve NXOpen.Curve@endlink) </param>
    def CreateEditCurveBuilder(self, curveToEdit: NXOpen.Curve) -> EditCurveBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::EditCurveBuilder NXOpen::Features::DrawShapes::EditCurveBuilder@endlink  
         @return builder (@link EditCurveBuilder NXOpen.Features.DrawShapes.EditCurveBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::EditDisplayBuilder NXOpen::Features::DrawShapes::EditDisplayBuilder@endlink  
    ##  @return builder (@link EditDisplayBuilder NXOpen.Features.DrawShapes.EditDisplayBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateEditDisplayBuilder(self) -> EditDisplayBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::EditDisplayBuilder NXOpen::Features::DrawShapes::EditDisplayBuilder@endlink  
         @return builder (@link EditDisplayBuilder NXOpen.Features.DrawShapes.EditDisplayBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::EraseBuilder NXOpen::Features::DrawShapes::EraseBuilder@endlink  
    ##  @return builder (@link EraseBuilder NXOpen.Features.DrawShapes.EraseBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateEraseBuilder(self) -> EraseBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::EraseBuilder NXOpen::Features::DrawShapes::EraseBuilder@endlink  
         @return builder (@link EraseBuilder NXOpen.Features.DrawShapes.EraseBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::ExtendBuilder NXOpen::Features::DrawShapes::ExtendBuilder@endlink  
    ##  @return builder (@link ExtendBuilder NXOpen.Features.DrawShapes.ExtendBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateExtendBuilder(self) -> ExtendBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::ExtendBuilder NXOpen::Features::DrawShapes::ExtendBuilder@endlink  
         @return builder (@link ExtendBuilder NXOpen.Features.DrawShapes.ExtendBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::FilletBuilder NXOpen::Features::DrawShapes::FilletBuilder@endlink  
    ##  @return builder (@link FilletBuilder NXOpen.Features.DrawShapes.FilletBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateFilletBuilder(self) -> FilletBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::FilletBuilder NXOpen::Features::DrawShapes::FilletBuilder@endlink  
         @return builder (@link FilletBuilder NXOpen.Features.DrawShapes.FilletBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::IntersectionCurveBuilder NXOpen::Features::DrawShapes::IntersectionCurveBuilder@endlink  
    ##  @return builder (@link IntersectionCurveBuilder NXOpen.Features.DrawShapes.IntersectionCurveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateIntersectionCurveBuilder(self) -> IntersectionCurveBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::IntersectionCurveBuilder NXOpen::Features::DrawShapes::IntersectionCurveBuilder@endlink  
         @return builder (@link IntersectionCurveBuilder NXOpen.Features.DrawShapes.IntersectionCurveBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::MirrorData NXOpen::Features::DrawShapes::MirrorData@endlink  
    ##  @return builder (@link MirrorData NXOpen.Features.DrawShapes.MirrorData@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateMirrorData(self) -> MirrorData:
        """
         Creates a @link NXOpen::Features::DrawShapes::MirrorData NXOpen::Features::DrawShapes::MirrorData@endlink  
         @return builder (@link MirrorData NXOpen.Features.DrawShapes.MirrorData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::OffsetCurveData NXOpen::Features::DrawShapes::OffsetCurveData@endlink  
    ##  @return builder (@link OffsetCurveData NXOpen.Features.DrawShapes.OffsetCurveData@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateOffsetCurveData(self) -> OffsetCurveData:
        """
         Creates a @link NXOpen::Features::DrawShapes::OffsetCurveData NXOpen::Features::DrawShapes::OffsetCurveData@endlink  
         @return builder (@link OffsetCurveData NXOpen.Features.DrawShapes.OffsetCurveData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::ProjectCurveBuilder NXOpen::Features::DrawShapes::ProjectCurveBuilder@endlink  
    ##  @return builder (@link ProjectCurveBuilder NXOpen.Features.DrawShapes.ProjectCurveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateProjectCurveBuilder(self) -> ProjectCurveBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::ProjectCurveBuilder NXOpen::Features::DrawShapes::ProjectCurveBuilder@endlink  
         @return builder (@link ProjectCurveBuilder NXOpen.Features.DrawShapes.ProjectCurveBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::StartSymmetryModeBuilder NXOpen::Features::DrawShapes::StartSymmetryModeBuilder@endlink . 
    ##  @return builder (@link StartSymmetryModeBuilder NXOpen.Features.DrawShapes.StartSymmetryModeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateStartSymmetryModeBuilder(self) -> StartSymmetryModeBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::StartSymmetryModeBuilder NXOpen::Features::DrawShapes::StartSymmetryModeBuilder@endlink . 
         @return builder (@link StartSymmetryModeBuilder NXOpen.Features.DrawShapes.StartSymmetryModeBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::TransformData NXOpen::Features::DrawShapes::TransformData@endlink  
    ##  @return builder (@link TransformData NXOpen.Features.DrawShapes.TransformData@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateTransformData(self) -> TransformData:
        """
         Creates a @link NXOpen::Features::DrawShapes::TransformData NXOpen::Features::DrawShapes::TransformData@endlink  
         @return builder (@link TransformData NXOpen.Features.DrawShapes.TransformData@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Features::DrawShapes::TrimBuilder NXOpen::Features::DrawShapes::TrimBuilder@endlink  
    ##  @return builder (@link TrimBuilder NXOpen.Features.DrawShapes.TrimBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def CreateTrimBuilder(self) -> TrimBuilder:
        """
         Creates a @link NXOpen::Features::DrawShapes::TrimBuilder NXOpen::Features::DrawShapes::TrimBuilder@endlink  
         @return builder (@link TrimBuilder NXOpen.Features.DrawShapes.TrimBuilder@endlink): .
        """
        pass
    
    ##  Stops the symmetry mode. 
    ##  @return atLeastOneSymmetryCurveDeleted (bool):  The flag indicating if at least one curve was deleted during stopping of the symmetry mode.
    ##                 When symmetry mode is stopped, symmetric curves are normally retained. A curve may be deleted if it does not have a drawing base supporting it.
    ##                 This may happen for @link NXOpen::Features::DrawShapes::DrawShapeData::DrawingBaseTypesFaces  NXOpen::Features::DrawShapes::DrawShapeData::DrawingBaseTypesFaces @endlink  type of drawing base. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def StopSymmetryMode(self) -> bool:
        """
         Stops the symmetry mode. 
         @return atLeastOneSymmetryCurveDeleted (bool):  The flag indicating if at least one curve was deleted during stopping of the symmetry mode.
                        When symmetry mode is stopped, symmetric curves are normally retained. A curve may be deleted if it does not have a drawing base supporting it.
                        This may happen for @link NXOpen::Features::DrawShapes::DrawShapeData::DrawingBaseTypesFaces  NXOpen::Features::DrawShapes::DrawShapeData::DrawingBaseTypesFaces @endlink  type of drawing base. .
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::DrawShapeData   NXOpen::Features::DrawShapes::DrawShapeData @endlink 
##         allowing user to define input faces or datums for Draw Shape
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawShapeData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawShapeData @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class DrawShapeData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.DrawShapeData </ja_class>
        allowing user to define input faces or datums for Draw Shape
    """


    ##  the drawing base types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Faces</term><description> 
    ## </description> </item><item><term> 
    ## Plane</term><description> 
    ## </description> </item></list>
    class DrawingBaseTypes(Enum):
        """
        Members Include: <Faces> <Plane>
        """
        Faces: int
        Plane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawShapeData.DrawingBaseTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Associative
    ##  Returns whether to create the associative output or non associative output  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns whether to create the associative output or non associative output  
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##  Returns whether to create the associative output or non associative output  
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns whether to create the associative output or non associative output  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordinateSystem
    ##  Returns the coordinate system.  
    ##    XY Plane of the coordinate system is used as drawing base.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def CoordinateSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system.  
           XY Plane of the coordinate system is used as drawing base.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordinateSystem

    ##  Returns the coordinate system.  
    ##    XY Plane of the coordinate system is used as drawing base.   
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CoordinateSystem.setter
    def CoordinateSystem(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordinateSystem
         Returns the coordinate system.  
           XY Plane of the coordinate system is used as drawing base.   
         
        """
        pass
    
    ## Getter for property: (@link DrawShapeData.DrawingBaseTypes NXOpen.Features.DrawShapes.DrawShapeData.DrawingBaseTypes@endlink) DrawingBaseType
    ##  Returns the drawing base type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return DrawShapeData.DrawingBaseTypes
    @property
    def DrawingBaseType(self) -> DrawShapeData.DrawingBaseTypes:
        """
        Getter for property: (@link DrawShapeData.DrawingBaseTypes NXOpen.Features.DrawShapes.DrawShapeData.DrawingBaseTypes@endlink) DrawingBaseType
         Returns the drawing base type   
            
         
        """
        pass
    
    ## Setter for property: (@link DrawShapeData.DrawingBaseTypes NXOpen.Features.DrawShapes.DrawShapeData.DrawingBaseTypes@endlink) DrawingBaseType

    ##  Returns the drawing base type   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DrawingBaseType.setter
    def DrawingBaseType(self, type: DrawShapeData.DrawingBaseTypes):
        """
        Setter for property: (@link DrawShapeData.DrawingBaseTypes NXOpen.Features.DrawShapes.DrawShapeData.DrawingBaseTypes@endlink) DrawingBaseType
         Returns the drawing base type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Faces
    ##  Returns the faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Faces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Faces
         Returns the faces   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents @link  NXOpen::Features::DrawShapes::DrawStrokeData   NXOpen::Features::DrawShapes::DrawStrokeData @endlink 
##         allowing user to define stroke using drag gesture.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawStrokeData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateDrawStrokeData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanDrawOnNearestFace </term> <description> 
##  
## true </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class DrawStrokeData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.DrawStrokeData </ja_class>
        allowing user to define stroke using drag gesture.
    """


    ## Getter for property: (bool) CanDrawOnNearestFace
    ##  Returns the flag indicating if stroke should be created only on the nearest face in view direction and 
    ##             not on faces on the back of a body.  
    ##    This option decreases the drawing performance.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanDrawOnNearestFace(self) -> bool:
        """
        Getter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if stroke should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
        """
        pass
    
    ## Setter for property: (bool) CanDrawOnNearestFace

    ##  Returns the flag indicating if stroke should be created only on the nearest face in view direction and 
    ##             not on faces on the back of a body.  
    ##    This option decreases the drawing performance.   
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanDrawOnNearestFace.setter
    def CanDrawOnNearestFace(self, doNearFaceProjection: bool):
        """
        Setter for property: (bool) CanDrawOnNearestFace
         Returns the flag indicating if stroke should be created only on the nearest face in view direction and 
                    not on faces on the back of a body.  
           This option decreases the drawing performance.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) StrokeGesture
    ##  Returns the object enabling drawing of the stroke   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.StrokeGestureData
    @property
    def StrokeGesture(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) StrokeGesture
         Returns the object enabling drawing of the stroke   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
    ##  Returns the thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def Thickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
         Returns the thickness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness

    ##  Returns the thickness   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Thickness.setter
    def Thickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
         Returns the thickness   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents @link  NXOpen::Features::DrawShapes::EditCurveBuilder   NXOpen::Features::DrawShapes::EditCurveBuilder @endlink 
##         allowing user to a edit curve.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateEditCurveBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateEditCurveBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class EditCurveBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.EditCurveBuilder </ja_class>
        allowing user to a edit curve.
    """


    ##  Circle definition options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ThreePoints</term><description> 
    ## </description> </item><item><term> 
    ## CenterandRadius</term><description> 
    ## </description> </item></list>
    class CircleDefinitionOption(Enum):
        """
        Members Include: <ThreePoints> <CenterandRadius>
        """
        ThreePoints: int
        CenterandRadius: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EditCurveBuilder.CircleDefinitionOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link EditCurveBuilder.CircleDefinitionOption NXOpen.Features.DrawShapes.EditCurveBuilder.CircleDefinitionOption@endlink) CircleDefinitionOptions
    ##  Returns the circle definition options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return EditCurveBuilder.CircleDefinitionOption
    @property
    def CircleDefinitionOptions(self) -> EditCurveBuilder.CircleDefinitionOption:
        """
        Getter for property: (@link EditCurveBuilder.CircleDefinitionOption NXOpen.Features.DrawShapes.EditCurveBuilder.CircleDefinitionOption@endlink) CircleDefinitionOptions
         Returns the circle definition options   
            
         
        """
        pass
    
    ## Setter for property: (@link EditCurveBuilder.CircleDefinitionOption NXOpen.Features.DrawShapes.EditCurveBuilder.CircleDefinitionOption@endlink) CircleDefinitionOptions

    ##  Returns the circle definition options   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CircleDefinitionOptions.setter
    def CircleDefinitionOptions(self, circleDefinitionOptions: EditCurveBuilder.CircleDefinitionOption):
        """
        Setter for property: (@link EditCurveBuilder.CircleDefinitionOption NXOpen.Features.DrawShapes.EditCurveBuilder.CircleDefinitionOption@endlink) CircleDefinitionOptions
         Returns the circle definition options   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) ConstraintManager
    ##  Returns the constraint manager   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Features.GeometricConstraintDataManager
    @property
    def ConstraintManager(self) -> NXOpen.Features.GeometricConstraintDataManager:
        """
        Getter for property: (@link NXOpen.Features.GeometricConstraintDataManager NXOpen.Features.GeometricConstraintDataManager@endlink) ConstraintManager
         Returns the constraint manager   
            
         
        """
        pass
    
    ## Getter for property: (bool) IsClosed
    ##  Returns the flag indicating if spline can be closed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def IsClosed(self) -> bool:
        """
        Getter for property: (bool) IsClosed
         Returns the flag indicating if spline can be closed   
            
         
        """
        pass
    
    ## Setter for property: (bool) IsClosed

    ##  Returns the flag indicating if spline can be closed   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @IsClosed.setter
    def IsClosed(self, isClosed: bool):
        """
        Setter for property: (bool) IsClosed
         Returns the flag indicating if spline can be closed   
            
         
        """
        pass
    
    ## Getter for property: (int) PointNumber
    ##  Returns the value indicating number of defining points a spline should have.  
    ##    Use this parameter to reduce the number
    ##             of points on a spline.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return int
    @property
    def PointNumber(self) -> int:
        """
        Getter for property: (int) PointNumber
         Returns the value indicating number of defining points a spline should have.  
           Use this parameter to reduce the number
                    of points on a spline.
                  
         
        """
        pass
    
    ## Setter for property: (int) PointNumber

    ##  Returns the value indicating number of defining points a spline should have.  
    ##    Use this parameter to reduce the number
    ##             of points on a spline.
    ##           
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @PointNumber.setter
    def PointNumber(self, pointNumber: int):
        """
        Setter for property: (int) PointNumber
         Returns the value indicating number of defining points a spline should have.  
           Use this parameter to reduce the number
                    of points on a spline.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
    ##  Returns the radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
         Returns the radius   
            
         
        """
        pass
    
    ##  Evaluates the curve after editing defining data. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def EvaluateCurve(self) -> None:
        """
         Evaluates the curve after editing defining data. 
        """
        pass
    
    ##  Updates the constraint manager after point is edited. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    def UpdateConstraintManagerPostPointEdit(self) -> None:
        """
         Updates the constraint manager after point is edited. 
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::EditDisplayBuilder   NXOpen::Features::DrawShapes::EditDisplayBuilder @endlink 
##         allowing user to edit display of strokes and curves.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateEditDisplayBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateEditDisplayBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class EditDisplayBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.EditDisplayBuilder </ja_class>
        allowing user to edit display of strokes and curves.
    """


    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Objects
    ##  Returns the objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def Objects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Objects
         Returns the objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
    ##  Returns the thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def Thickness(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
         Returns the thickness   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness

    ##  Returns the thickness   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Thickness.setter
    def Thickness(self, thickness: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) Thickness
         Returns the thickness   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents @link  NXOpen::Features::DrawShapes::EraseBuilder   NXOpen::Features::DrawShapes::EraseBuilder @endlink 
##             allowing user to erase strokes or curves.
##          <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateEraseBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateEraseBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class EraseBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.EraseBuilder </ja_class>
            allowing user to erase strokes or curves.
        """


    ## Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) StrokeGesture
    ##  Returns the object enabling erasing strokes or curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.StrokeGestureData
    @property
    def StrokeGesture(self) -> NXOpen.GeometricUtilities.StrokeGestureData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.StrokeGestureData NXOpen.GeometricUtilities.StrokeGestureData@endlink) StrokeGesture
         Returns the object enabling erasing strokes or curves   
            
         
        """
        pass
    
    ## Getter for property: (float) Thickness
    ##  Returns the thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness   
            
         
        """
        pass
    
    ## Setter for property: (float) Thickness

    ##  Returns the thickness   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents @link  NXOpen::Features::DrawShapes::ExtendBuilder   NXOpen::Features::DrawShapes::ExtendBuilder @endlink 
##             allowing user to extend strokes or curves.
##          <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateExtendBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateExtendBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ExtendBound </term> <description> 
##  
## True </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class ExtendBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.ExtendBuilder </ja_class>
            allowing user to extend strokes or curves.
        """


    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) BoundaryObjects
    ##  Returns the boundary objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def BoundaryObjects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) BoundaryObjects
         Returns the boundary objects   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExtendBound
    ##  Returns the flag to control the ability to extend to extension of the boundary   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ExtendBound(self) -> bool:
        """
        Getter for property: (bool) ExtendBound
         Returns the flag to control the ability to extend to extension of the boundary   
            
         
        """
        pass
    
    ## Setter for property: (bool) ExtendBound

    ##  Returns the flag to control the ability to extend to extension of the boundary   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ExtendBound.setter
    def ExtendBound(self, extendBound: bool):
        """
        Setter for property: (bool) ExtendBound
         Returns the flag to control the ability to extend to extension of the boundary   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CrayonSelectionData NXOpen.GeometricUtilities.CrayonSelectionData@endlink) Targets
    ##  Returns the points indicating trimming location on the object to be extended   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CrayonSelectionData
    @property
    def Targets(self) -> NXOpen.GeometricUtilities.CrayonSelectionData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CrayonSelectionData NXOpen.GeometricUtilities.CrayonSelectionData@endlink) Targets
         Returns the points indicating trimming location on the object to be extended   
            
         
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::FilletBuilder   NXOpen::Features::DrawShapes::FilletBuilder @endlink 
##             allowing user to create a fillet between two curves.
##          <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateFilletBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateFilletBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## TrimInputCurves </term> <description> 
##  
## True </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class FilletBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.FilletBuilder </ja_class>
            allowing user to create a fillet between two curves.
        """


    ##  Contains placement information for creating a fillet. 
    ## @link FilletBuilderPlacementData_Struct NXOpen.Features.DrawShapes.FilletBuilderPlacementData_Struct@endlink is an alias for @link FilletBuilder.PlacementData NXOpen.Features.DrawShapes.FilletBuilder.PlacementData@endlink.
    class PlacementData:
        """
         Contains placement information for creating a fillet. 
        @link FilletBuilderPlacementData_Struct NXOpen.Features.DrawShapes.FilletBuilderPlacementData_Struct@endlink is an alias for @link FilletBuilder.PlacementData NXOpen.Features.DrawShapes.FilletBuilder.PlacementData@endlink.
        """
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) Position
        ## The point at which fillet is placed
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def Position(self) -> NXOpen.Point3d:
            """
            Getter for property Position
            The point at which fillet is placed

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) Position
        @Position.setter
        def Position(self, value: NXOpen.Point3d):
            """
            Getter for property Position
            The point at which fillet is placed
            Setter for property Position
            The point at which fillet is placed

            """
            pass
        
        ## Getter for property :(@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ViewMatrix
        ## The view matrix while placing the fillet
        ## @return @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink
        @property
        def ViewMatrix(self) -> NXOpen.Matrix3x3:
            """
            Getter for property ViewMatrix
            The view matrix while placing the fillet

            """
            pass
        
        ## Setter for property :(@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ViewMatrix
        @ViewMatrix.setter
        def ViewMatrix(self, value: NXOpen.Matrix3x3):
            """
            Getter for property ViewMatrix
            The view matrix while placing the fillet
            Setter for property ViewMatrix
            The view matrix while placing the fillet

            """
            pass
        
    
    
    ## Getter for property: (bool) CreateAlternateFillet
    ##  Returns the flag to create alternate fillet   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAlternateFillet(self) -> bool:
        """
        Getter for property: (bool) CreateAlternateFillet
         Returns the flag to create alternate fillet   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateAlternateFillet

    ##  Returns the flag to create alternate fillet   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAlternateFillet.setter
    def CreateAlternateFillet(self, createAlternateFillet: bool):
        """
        Setter for property: (bool) CreateAlternateFillet
         Returns the flag to create alternate fillet   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectCurve NXOpen.SelectCurve@endlink) FirstCurve
    ##  Returns the first curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectCurve
    @property
    def FirstCurve(self) -> NXOpen.SelectCurve:
        """
        Getter for property: (@link NXOpen.SelectCurve NXOpen.SelectCurve@endlink) FirstCurve
         Returns the first curve   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectCurve NXOpen.SelectCurve@endlink) SecondCurve
    ##  Returns the second curve   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectCurve
    @property
    def SecondCurve(self) -> NXOpen.SelectCurve:
        """
        Getter for property: (@link NXOpen.SelectCurve NXOpen.SelectCurve@endlink) SecondCurve
         Returns the second curve   
            
         
        """
        pass
    
    ## Getter for property: (bool) TrimInputCurves
    ##  Returns the flag to control the ability to trim input curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def TrimInputCurves(self) -> bool:
        """
        Getter for property: (bool) TrimInputCurves
         Returns the flag to control the ability to trim input curves   
            
         
        """
        pass
    
    ## Setter for property: (bool) TrimInputCurves

    ##  Returns the flag to control the ability to trim input curves   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TrimInputCurves.setter
    def TrimInputCurves(self, trimInputs: bool):
        """
        Setter for property: (bool) TrimInputCurves
         Returns the flag to control the ability to trim input curves   
            
         
        """
        pass
    
    ##  Sets the placement data for fillet. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ## <param name="placementData"> (@link FilletBuilder.PlacementData NXOpen.Features.DrawShapes.FilletBuilder.PlacementData@endlink)  Placement data </param>
    def SetPlacementData(self, placementData: FilletBuilder.PlacementData) -> None:
        """
         Sets the placement data for fillet. 
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::IntersectionCurveBuilder   NXOpen::Features::DrawShapes::IntersectionCurveBuilder @endlink 
##        allowing the user to intersection existing faces and/or planes from outside the Draw Shape feature with the drawing base and create them as drawn curves of the feature.
##     <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateIntersectionCurveBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateIntersectionCurveBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class IntersectionCurveBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.IntersectionCurveBuilder </ja_class>
       allowing the user to intersection existing faces and/or planes from outside the Draw Shape feature with the drawing base and create them as drawn curves of the feature.
   """


    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) DrawingBases
    ##  Returns the faces of the drawing base.  
    ##    These entities can only be a sub-set of drawing bases.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def DrawingBases(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) DrawingBases
         Returns the faces of the drawing base.  
           These entities can only be a sub-set of drawing bases.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacesOrPlane
    ##  Returns the faces or datum planes from outside the Draw Shape feature to intersect them with the drawing base   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FacesOrPlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FacesOrPlane
         Returns the faces or datum planes from outside the Draw Shape feature to intersect them with the drawing base   
            
         
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::MirrorData   NXOpen::Features::DrawShapes::MirrorData @endlink 
##         allowing user to mirror curves.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateMirrorData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateMirrorData @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MirrorData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.MirrorData </ja_class>
        allowing user to mirror curves.
    """


    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Objects
    ##  Returns the objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def Objects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Objects
         Returns the objects   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the plane   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane   
            
         
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::OffsetCurveData   NXOpen::Features::DrawShapes::OffsetCurveData @endlink 
##         allowing user to offset curve.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateOffsetCurveData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateOffsetCurveData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CornerTreatment </term> <description> 
##  
## Keep </description> </item> 
## 
## <item><term> 
##  
## OffsetDistance.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RoundRadius.Value </term> <description> 
##  
## 5 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class OffsetCurveData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.OffsetCurveData </ja_class>
        allowing user to offset curve.
    """


    ##  Sharp corner treatment option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Keep</term><description> 
    ## </description> </item><item><term> 
    ## Round</term><description> 
    ## </description> </item></list>
    class SharpCornerTreatment(Enum):
        """
        Members Include: <Keep> <Round>
        """
        Keep: int
        Round: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OffsetCurveData.SharpCornerTreatment:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link OffsetCurveData.SharpCornerTreatment NXOpen.Features.DrawShapes.OffsetCurveData.SharpCornerTreatment@endlink) CornerTreatment
    ##  Returns the corner treatment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return OffsetCurveData.SharpCornerTreatment
    @property
    def CornerTreatment(self) -> OffsetCurveData.SharpCornerTreatment:
        """
        Getter for property: (@link OffsetCurveData.SharpCornerTreatment NXOpen.Features.DrawShapes.OffsetCurveData.SharpCornerTreatment@endlink) CornerTreatment
         Returns the corner treatment   
            
         
        """
        pass
    
    ## Setter for property: (@link OffsetCurveData.SharpCornerTreatment NXOpen.Features.DrawShapes.OffsetCurveData.SharpCornerTreatment@endlink) CornerTreatment

    ##  Returns the corner treatment   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CornerTreatment.setter
    def CornerTreatment(self, cornerTreatment: OffsetCurveData.SharpCornerTreatment):
        """
        Setter for property: (@link OffsetCurveData.SharpCornerTreatment NXOpen.Features.DrawShapes.OffsetCurveData.SharpCornerTreatment@endlink) CornerTreatment
         Returns the corner treatment   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurvesToOffset
    ##  Returns the curves to offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def CurvesToOffset(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurvesToOffset
         Returns the curves to offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##  Returns the offset distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
         Returns the offset distance   
            
         
        """
        pass
    
    ## Getter for property: (bool) ReverseDirection
    ##  Returns the reverse direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    
    ## Setter for property: (bool) ReverseDirection

    ##  Returns the reverse direction   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RoundRadius
    ##  Returns the round radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RoundRadius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RoundRadius
         Returns the round radius   
            
         
        """
        pass
    
    ##  Displays curve preview. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def DisplayPreviewCurves(self) -> None:
        """
         Displays curve preview. 
        """
        pass
    
    ##  Updates internal data based on the selected seed curve and point. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="seedEntity"> (@link NXOpen.Curve NXOpen.Curve@endlink) </param>
    ## <param name="seedPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def UpdateOnCurveSelection(self, seedEntity: NXOpen.Curve, seedPoint: NXOpen.Point3d) -> None:
        """
         Updates internal data based on the selected seed curve and point. 
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::ProjectCurveBuilder   NXOpen::Features::DrawShapes::ProjectCurveBuilder @endlink 
##             allowing user to project existing curves from outside of Draw Shape feature to the drawing base and create them as drawn curves of the feature.
##          <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateProjectCurveBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateProjectCurveBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class ProjectCurveBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.ProjectCurveBuilder </ja_class>
            allowing user to project existing curves from outside of Draw Shape feature to the drawing base and create them as drawn curves of the feature.
        """


    ##  options to specify the projection direction 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NormaltoDrawingBase</term><description> 
    ##  Curves will be projected along local face normal of drawing base </description> </item><item><term> 
    ## AlongVector</term><description> 
    ##  User specifies a vector for uniform drawing projection </description> </item></list>
    class ProjectionDirectionType(Enum):
        """
        Members Include: <NormaltoDrawingBase> <AlongVector>
        """
        NormaltoDrawingBase: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ProjectCurveBuilder.ProjectionDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Curves
    ##  Returns the curves to project   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Curves(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Curves
         Returns the curves to project   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) DrawingBaseFaces
    ##  Returns the faces or plane to project curves on.  
    ##    These entities can only be a sub-set of drawing bases.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def DrawingBaseFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) DrawingBaseFaces
         Returns the faces or plane to project curves on.  
           These entities can only be a sub-set of drawing bases.   
         
        """
        pass
    
    ## Getter for property: (bool) HideInputCurves
    ##  Returns the value indicating if input curves should be hidden.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def HideInputCurves(self) -> bool:
        """
        Getter for property: (bool) HideInputCurves
         Returns the value indicating if input curves should be hidden.  
             
         
        """
        pass
    
    ## Setter for property: (bool) HideInputCurves

    ##  Returns the value indicating if input curves should be hidden.  
    ##      
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @HideInputCurves.setter
    def HideInputCurves(self, hideInputCurves: bool):
        """
        Setter for property: (bool) HideInputCurves
         Returns the value indicating if input curves should be hidden.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ProjectBothSides
    ##  Returns the value indicating if projection should be done in both the sides of the specified direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ProjectBothSides(self) -> bool:
        """
        Getter for property: (bool) ProjectBothSides
         Returns the value indicating if projection should be done in both the sides of the specified direction.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ProjectBothSides

    ##  Returns the value indicating if projection should be done in both the sides of the specified direction.  
    ##      
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ProjectBothSides.setter
    def ProjectBothSides(self, projectBothSides: bool):
        """
        Setter for property: (bool) ProjectBothSides
         Returns the value indicating if projection should be done in both the sides of the specified direction.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ProjectNearestPoint
    ##  Returns the value indicating if curves should be projected to the nearest point on drawing base in a given direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ProjectNearestPoint(self) -> bool:
        """
        Getter for property: (bool) ProjectNearestPoint
         Returns the value indicating if curves should be projected to the nearest point on drawing base in a given direction.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ProjectNearestPoint

    ##  Returns the value indicating if curves should be projected to the nearest point on drawing base in a given direction.  
    ##      
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ProjectNearestPoint.setter
    def ProjectNearestPoint(self, projectNearestPoint: bool):
        """
        Setter for property: (bool) ProjectNearestPoint
         Returns the value indicating if curves should be projected to the nearest point on drawing base in a given direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionDirection
    ##  Returns the direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ProjectionDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionDirection
         Returns the direction   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionDirection

    ##  Returns the direction   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ProjectionDirection.setter
    def ProjectionDirection(self, direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionDirection
         Returns the direction   
            
         
        """
        pass
    
    ## Getter for property: (@link ProjectCurveBuilder.ProjectionDirectionType NXOpen.Features.DrawShapes.ProjectCurveBuilder.ProjectionDirectionType@endlink) ProjectionDirectionOption
    ##  Returns the projection direction option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return ProjectCurveBuilder.ProjectionDirectionType
    @property
    def ProjectionDirectionOption(self) -> ProjectCurveBuilder.ProjectionDirectionType:
        """
        Getter for property: (@link ProjectCurveBuilder.ProjectionDirectionType NXOpen.Features.DrawShapes.ProjectCurveBuilder.ProjectionDirectionType@endlink) ProjectionDirectionOption
         Returns the projection direction option   
            
         
        """
        pass
    
    ## Setter for property: (@link ProjectCurveBuilder.ProjectionDirectionType NXOpen.Features.DrawShapes.ProjectCurveBuilder.ProjectionDirectionType@endlink) ProjectionDirectionOption

    ##  Returns the projection direction option   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ProjectionDirectionOption.setter
    def ProjectionDirectionOption(self, projectionDir: ProjectCurveBuilder.ProjectionDirectionType):
        """
        Setter for property: (@link ProjectCurveBuilder.ProjectionDirectionType NXOpen.Features.DrawShapes.ProjectCurveBuilder.ProjectionDirectionType@endlink) ProjectionDirectionOption
         Returns the projection direction option   
            
         
        """
        pass
    
import NXOpen
##  Represents @link  NXOpen::Features::DrawShapes::StartSymmetryModeBuilder   NXOpen::Features::DrawShapes::StartSymmetryModeBuilder @endlink 
##         allowing user to start symmetry mode.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateStartSymmetryModeBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateStartSymmetryModeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class StartSymmetryModeBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.StartSymmetryModeBuilder </ja_class>
        allowing user to start symmetry mode.
    """


    ## Getter for property: (bool) CreateSymmetricCopiesOfExistingCurves
    ##  Returns the Create Symmetric Copies of Exisitng Curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CreateSymmetricCopiesOfExistingCurves(self) -> bool:
        """
        Getter for property: (bool) CreateSymmetricCopiesOfExistingCurves
         Returns the Create Symmetric Copies of Exisitng Curves   
            
         
        """
        pass
    
    ## Setter for property: (bool) CreateSymmetricCopiesOfExistingCurves

    ##  Returns the Create Symmetric Copies of Exisitng Curves   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CreateSymmetricCopiesOfExistingCurves.setter
    def CreateSymmetricCopiesOfExistingCurves(self, createSymmetricCopiesOfExistingCurves: bool):
        """
        Setter for property: (bool) CreateSymmetricCopiesOfExistingCurves
         Returns the Create Symmetric Copies of Exisitng Curves   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
    ##  Returns the plane   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane

    ##  Returns the plane   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) Plane
         Returns the plane   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents @link  NXOpen::Features::DrawShapes::TransformData   NXOpen::Features::DrawShapes::TransformData @endlink 
##         allowing user to delete strokes and curves.
##      <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateTransformData  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateTransformData @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CanRelocateToolToSelection </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CanReorientToolToSelection </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## NumberOfCopies </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class TransformData(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.TransformData </ja_class>
        allowing user to delete strokes and curves.
    """


    ##  Transform operation result options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MoveOriginal</term><description> 
    ## </description> </item><item><term> 
    ## CopyOriginal</term><description> 
    ## </description> </item></list>
    class ResultOptions(Enum):
        """
        Members Include: <MoveOriginal> <CopyOriginal>
        """
        MoveOriginal: int
        CopyOriginal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformData.ResultOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Scaling options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ## </description> </item><item><term> 
    ## Planar</term><description> 
    ## </description> </item><item><term> 
    ## Uniform</term><description> 
    ## </description> </item></list>
    class ScalingOptions(Enum):
        """
        Members Include: <Linear> <Planar> <Uniform>
        """
        Linear: int
        Planar: int
        Uniform: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TransformData.ScalingOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CanMoveToolOnly
    ##  Returns the can move tool only   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanMoveToolOnly(self) -> bool:
        """
        Getter for property: (bool) CanMoveToolOnly
         Returns the can move tool only   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanMoveToolOnly

    ##  Returns the can move tool only   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanMoveToolOnly.setter
    def CanMoveToolOnly(self, canMoveToolOnly: bool):
        """
        Setter for property: (bool) CanMoveToolOnly
         Returns the can move tool only   
            
         
        """
        pass
    
    ## Getter for property: (bool) CanRelocateToolToSelection
    ##  Returns the can relocate tool to selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanRelocateToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanRelocateToolToSelection
         Returns the can relocate tool to selection   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanRelocateToolToSelection

    ##  Returns the can relocate tool to selection   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanRelocateToolToSelection.setter
    def CanRelocateToolToSelection(self, canRelocateToolToSelection: bool):
        """
        Setter for property: (bool) CanRelocateToolToSelection
         Returns the can relocate tool to selection   
            
         
        """
        pass
    
    ## Getter for property: (bool) CanReorientToolToSelection
    ##  Returns the can reorient tool to selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def CanReorientToolToSelection(self) -> bool:
        """
        Getter for property: (bool) CanReorientToolToSelection
         Returns the can reorient tool to selection   
            
         
        """
        pass
    
    ## Setter for property: (bool) CanReorientToolToSelection

    ##  Returns the can reorient tool to selection   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CanReorientToolToSelection.setter
    def CanReorientToolToSelection(self, canReorientToolToSelection: bool):
        """
        Setter for property: (bool) CanReorientToolToSelection
         Returns the can reorient tool to selection   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfCopies
    ##  Returns the number of copies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfCopies

    ##  Returns the number of copies   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ObjectsToTransform
    ##  Returns the objects to be transformed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def ObjectsToTransform(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ObjectsToTransform
         Returns the objects to be transformed   
            
         
        """
        pass
    
    ## Getter for property: (@link TransformData.ResultOptions NXOpen.Features.DrawShapes.TransformData.ResultOptions@endlink) ResultOption
    ##  Returns the result option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TransformData.ResultOptions
    @property
    def ResultOption(self) -> TransformData.ResultOptions:
        """
        Getter for property: (@link TransformData.ResultOptions NXOpen.Features.DrawShapes.TransformData.ResultOptions@endlink) ResultOption
         Returns the result option   
            
         
        """
        pass
    
    ## Setter for property: (@link TransformData.ResultOptions NXOpen.Features.DrawShapes.TransformData.ResultOptions@endlink) ResultOption

    ##  Returns the result option   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ResultOption.setter
    def ResultOption(self, resultOption: TransformData.ResultOptions):
        """
        Setter for property: (@link TransformData.ResultOptions NXOpen.Features.DrawShapes.TransformData.ResultOptions@endlink) ResultOption
         Returns the result option   
            
         
        """
        pass
    
    ## Getter for property: (@link TransformData.ScalingOptions NXOpen.Features.DrawShapes.TransformData.ScalingOptions@endlink) Scaling
    ##  Returns the scaling   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TransformData.ScalingOptions
    @property
    def Scaling(self) -> TransformData.ScalingOptions:
        """
        Getter for property: (@link TransformData.ScalingOptions NXOpen.Features.DrawShapes.TransformData.ScalingOptions@endlink) Scaling
         Returns the scaling   
            
         
        """
        pass
    
    ## Setter for property: (@link TransformData.ScalingOptions NXOpen.Features.DrawShapes.TransformData.ScalingOptions@endlink) Scaling

    ##  Returns the scaling   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Scaling.setter
    def Scaling(self, scaling: TransformData.ScalingOptions):
        """
        Setter for property: (@link TransformData.ScalingOptions NXOpen.Features.DrawShapes.TransformData.ScalingOptions@endlink) Scaling
         Returns the scaling   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
    ##  Returns the transformation tool.  
    ##    The tool allows user to transform the pasted topology.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.TransformerData
    @property
    def Transformer(self) -> NXOpen.GeometricUtilities.TransformerData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.TransformerData NXOpen.GeometricUtilities.TransformerData@endlink) Transformer
         Returns the transformation tool.  
           The tool allows user to transform the pasted topology.   
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents @link  NXOpen::Features::DrawShapes::TrimBuilder   NXOpen::Features::DrawShapes::TrimBuilder @endlink 
##             allowing user to trim strokes or curves.
##          <br> To create a new instance of this class, use @link NXOpen::Features::DrawShapes::DrawShapeCollection::CreateTrimBuilder  NXOpen::Features::DrawShapes::DrawShapeCollection::CreateTrimBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ExtendBound </term> <description> 
##  
## True </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class TrimBuilder(NXOpen.Builder): 
    """ Represents <ja_class> NXOpen.Features.DrawShapes.TrimBuilder </ja_class>
            allowing user to trim strokes or curves.
        """


    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) BoundaryObjects
    ##  Returns the boundary objects   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def BoundaryObjects(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) BoundaryObjects
         Returns the boundary objects   
            
         
        """
        pass
    
    ## Getter for property: (bool) ExtendBound
    ##  Returns the flag to control the ability to trim to extension of the boundary   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ExtendBound(self) -> bool:
        """
        Getter for property: (bool) ExtendBound
         Returns the flag to control the ability to trim to extension of the boundary   
            
         
        """
        pass
    
    ## Setter for property: (bool) ExtendBound

    ##  Returns the flag to control the ability to trim to extension of the boundary   
    ##     
    ##  
    ## Setter License requirements: nx_draw_shape (" NX Draw Shape Functionality")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ExtendBound.setter
    def ExtendBound(self, extendBound: bool):
        """
        Setter for property: (bool) ExtendBound
         Returns the flag to control the ability to trim to extension of the boundary   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) Point
    ##  Returns the point indicating snapped location on the object to be trimmed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2007.0.0.  Use @link JA_TRIM_BUILDER_get_Targets JA_TRIM_BUILDER_get_Targets@endlink  instead.  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def Point(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) Point
         Returns the point indicating snapped location on the object to be trimmed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.CrayonSelectionData NXOpen.GeometricUtilities.CrayonSelectionData@endlink) Targets
    ##  Returns the points indicating trimming location on the object to be trimmed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.CrayonSelectionData
    @property
    def Targets(self) -> NXOpen.GeometricUtilities.CrayonSelectionData:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.CrayonSelectionData NXOpen.GeometricUtilities.CrayonSelectionData@endlink) Targets
         Returns the points indicating trimming location on the object to be trimmed   
            
         
        """
        pass
    
## @package NXOpen.Features.DrawShapes
## Classes, Enums and Structs under NXOpen.Features.DrawShapes namespace

##  @link CurveFromStrokeDataDetectionSensitivityOption NXOpen.Features.DrawShapes.CurveFromStrokeDataDetectionSensitivityOption @endlink is an alias for @link CurveFromStrokeData.DetectionSensitivityOption NXOpen.Features.DrawShapes.CurveFromStrokeData.DetectionSensitivityOption@endlink
CurveFromStrokeDataDetectionSensitivityOption = CurveFromStrokeData.DetectionSensitivityOption


##  @link DrawCurveDataDetectionSensitivityOption NXOpen.Features.DrawShapes.DrawCurveDataDetectionSensitivityOption @endlink is an alias for @link DrawCurveData.DetectionSensitivityOption NXOpen.Features.DrawShapes.DrawCurveData.DetectionSensitivityOption@endlink
DrawCurveDataDetectionSensitivityOption = DrawCurveData.DetectionSensitivityOption


##  @link DrawCurveDataSnappingOption NXOpen.Features.DrawShapes.DrawCurveDataSnappingOption @endlink is an alias for @link DrawCurveData.SnappingOption NXOpen.Features.DrawShapes.DrawCurveData.SnappingOption@endlink
DrawCurveDataSnappingOption = DrawCurveData.SnappingOption


##  @link DrawCurveDataSnapToOptions NXOpen.Features.DrawShapes.DrawCurveDataSnapToOptions @endlink is an alias for @link DrawCurveData.SnapToOptions NXOpen.Features.DrawShapes.DrawCurveData.SnapToOptions@endlink
DrawCurveDataSnapToOptions = DrawCurveData.SnapToOptions


##  @link DrawShapeDataDrawingBaseTypes NXOpen.Features.DrawShapes.DrawShapeDataDrawingBaseTypes @endlink is an alias for @link DrawShapeData.DrawingBaseTypes NXOpen.Features.DrawShapes.DrawShapeData.DrawingBaseTypes@endlink
DrawShapeDataDrawingBaseTypes = DrawShapeData.DrawingBaseTypes


##  @link EditCurveBuilderCircleDefinitionOption NXOpen.Features.DrawShapes.EditCurveBuilderCircleDefinitionOption @endlink is an alias for @link EditCurveBuilder.CircleDefinitionOption NXOpen.Features.DrawShapes.EditCurveBuilder.CircleDefinitionOption@endlink
EditCurveBuilderCircleDefinitionOption = EditCurveBuilder.CircleDefinitionOption


## @link FilletBuilderPlacementData_Struct NXOpen.Features.DrawShapes.FilletBuilderPlacementData_Struct@endlink is an alias for @link FilletBuilder.PlacementData NXOpen.Features.DrawShapes.FilletBuilder.PlacementData@endlink.
FilletBuilderPlacementData_Struct = FilletBuilder.PlacementData


##  @link OffsetCurveDataSharpCornerTreatment NXOpen.Features.DrawShapes.OffsetCurveDataSharpCornerTreatment @endlink is an alias for @link OffsetCurveData.SharpCornerTreatment NXOpen.Features.DrawShapes.OffsetCurveData.SharpCornerTreatment@endlink
OffsetCurveDataSharpCornerTreatment = OffsetCurveData.SharpCornerTreatment


##  @link ProjectCurveBuilderProjectionDirectionType NXOpen.Features.DrawShapes.ProjectCurveBuilderProjectionDirectionType @endlink is an alias for @link ProjectCurveBuilder.ProjectionDirectionType NXOpen.Features.DrawShapes.ProjectCurveBuilder.ProjectionDirectionType@endlink
ProjectCurveBuilderProjectionDirectionType = ProjectCurveBuilder.ProjectionDirectionType


##  @link TransformDataResultOptions NXOpen.Features.DrawShapes.TransformDataResultOptions @endlink is an alias for @link TransformData.ResultOptions NXOpen.Features.DrawShapes.TransformData.ResultOptions@endlink
TransformDataResultOptions = TransformData.ResultOptions


##  @link TransformDataScalingOptions NXOpen.Features.DrawShapes.TransformDataScalingOptions @endlink is an alias for @link TransformData.ScalingOptions NXOpen.Features.DrawShapes.TransformData.ScalingOptions@endlink
TransformDataScalingOptions = TransformData.ScalingOptions


