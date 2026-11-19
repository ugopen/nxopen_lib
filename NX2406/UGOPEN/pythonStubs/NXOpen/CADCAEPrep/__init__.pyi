from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
##  Bar sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionBar(IBeamSection): 
    """ Bar sections. """


    ## Getter for property: (float) H
    ##  Returns the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    
    ## Getter for property: (float) W
    ##  Returns the width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    def Edit(self, width: float, height: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  Box sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionBox(IBeamSection): 
    """ Box sections. """


    ## Getter for property: (float) H
    ##  Returns the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    
    ## Getter for property: (float) Tss
    ##  Returns the thickness sides   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tss(self) -> float:
        """
        Getter for property: (float) Tss
         Returns the thickness sides   
            
         
        """
        pass
    
    ## Getter for property: (float) Ttb
    ##  Returns the thickness top-bottom   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Ttb(self) -> float:
        """
        Getter for property: (float) Ttb
         Returns the thickness top-bottom   
            
         
        """
        pass
    
    ## Getter for property: (float) W
    ##  Returns the width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    ## <param name="thicknessTopBottom"> (float) </param>
    ## <param name="thicknessSides"> (float) </param>
    def Edit(self, width: float, height: float, thicknessTopBottom: float, thicknessSides: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  Chan sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionChan(IBeamSection): 
    """ Chan sections. """


    ## Getter for property: (float) H
    ##  Returns the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    
    ## Getter for property: (float) Tf
    ##  Returns the flange thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tf(self) -> float:
        """
        Getter for property: (float) Tf
         Returns the flange thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) Tw
    ##  Returns the web thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tw(self) -> float:
        """
        Getter for property: (float) Tw
         Returns the web thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) W
    ##  Returns the width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    ## <param name="webThickness"> (float) </param>
    ## <param name="flangeThickness"> (float) </param>
    def Edit(self, width: float, height: float, webThickness: float, flangeThickness: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  Hexa sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionHexa(IBeamSection): 
    """ Hexa sections. """


    ## Getter for property: (float) H
    ##  Returns the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    
    ## Getter for property: (float) W
    ##  Returns the overall width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the overall width   
            
         
        """
        pass
    
    ## Getter for property: (float) Ws
    ##  Returns the side width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Ws(self) -> float:
        """
        Getter for property: (float) Ws
         Returns the side width   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sideWidth"> (float) </param>
    ## <param name="overallWidth"> (float) </param>
    ## <param name="height"> (float) </param>
    def Edit(self, sideWidth: float, overallWidth: float, height: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  I sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionI(IBeamSection): 
    """ I sections. """


    ## Getter for property: (float) H
    ##  Returns the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    
    ## Getter for property: (float) Tbf
    ##  Returns the bottom flange thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tbf(self) -> float:
        """
        Getter for property: (float) Tbf
         Returns the bottom flange thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) Ttf
    ##  Returns the top flange thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Ttf(self) -> float:
        """
        Getter for property: (float) Ttf
         Returns the top flange thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) Tw
    ##  Returns the web thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tw(self) -> float:
        """
        Getter for property: (float) Tw
         Returns the web thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) Wbf
    ##  Returns the bottom flange width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Wbf(self) -> float:
        """
        Getter for property: (float) Wbf
         Returns the bottom flange width   
            
         
        """
        pass
    
    ## Getter for property: (float) Wtf
    ##  Returns the top flange width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Wtf(self) -> float:
        """
        Getter for property: (float) Wtf
         Returns the top flange width   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="height"> (float) </param>
    ## <param name="widthBottomFlange"> (float) </param>
    ## <param name="widthTopFlange"> (float) </param>
    ## <param name="thicknessWeb"> (float) </param>
    ## <param name="thicknessBottomFlange"> (float) </param>
    ## <param name="thicknessTopFlange"> (float) </param>
    def Edit(self, height: float, widthBottomFlange: float, widthTopFlange: float, thicknessWeb: float, thicknessBottomFlange: float, thicknessTopFlange: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  L sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionL(IBeamSection): 
    """ L sections. """


    ## Getter for property: (float) Lh
    ##  Returns the horizontal length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Lh(self) -> float:
        """
        Getter for property: (float) Lh
         Returns the horizontal length   
            
         
        """
        pass
    
    ## Getter for property: (float) Lv
    ##  Returns the vertical length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Lv(self) -> float:
        """
        Getter for property: (float) Lv
         Returns the vertical length   
            
         
        """
        pass
    
    ## Getter for property: (float) Th
    ##  Returns the horizontal thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Th(self) -> float:
        """
        Getter for property: (float) Th
         Returns the horizontal thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) Tv
    ##  Returns the vertical thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tv(self) -> float:
        """
        Getter for property: (float) Tv
         Returns the vertical thickness   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lengthVertical"> (float) </param>
    ## <param name="lengthHorizontal"> (float) </param>
    ## <param name="thicknessHorizontal"> (float) </param>
    ## <param name="thicknessVertical"> (float) </param>
    def Edit(self, lengthVertical: float, lengthHorizontal: float, thicknessHorizontal: float, thicknessVertical: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  Rod sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionRod(IBeamSection): 
    """ Rod sections. """


    ## Getter for property: (float) R
    ##  Returns the radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def R(self) -> float:
        """
        Getter for property: (float) R
         Returns the radius   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="radius"> (float) </param>
    def Edit(self, radius: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
import NXOpen
##  Sketch sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionSketch(IBeamSection): 
    """ Sketch sections. """


    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OriginBoundingBoxCenterOffset
    ##  Returns the offset between the origin and the center of the bounding box   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Point2d
    @property
    def OriginBoundingBoxCenterOffset(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OriginBoundingBoxCenterOffset
         Returns the offset between the origin and the center of the bounding box   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
    ##  Returns the sketch   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Sketch
    @property
    def Sketch(self) -> NXOpen.Sketch:
        """
        Getter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
         Returns the sketch   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sketch"> (@link NXOpen.Sketch NXOpen.Sketch@endlink) </param>
    def Edit(self, sketch: NXOpen.Sketch) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  Tube sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionTube(IBeamSection): 
    """ Tube sections. """


    ## Getter for property: (float) Ri
    ##  Returns the inside radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Ri(self) -> float:
        """
        Getter for property: (float) Ri
         Returns the inside radius   
            
         
        """
        pass
    
    ## Getter for property: (float) Ro
    ##  Returns the outside radius   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Ro(self) -> float:
        """
        Getter for property: (float) Ro
         Returns the outside radius   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="radiusOutside"> (float) </param>
    ## <param name="radiusInside"> (float) </param>
    def Edit(self, radiusOutside: float, radiusInside: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
##  T sections.  <br> Use specific creator in <ja>CADCAEPrep.IdealizedBeamManager</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamSectionT(IBeamSection): 
    """ T sections. """


    ## Getter for property: (float) H
    ##  Returns the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def H(self) -> float:
        """
        Getter for property: (float) H
         Returns the height   
            
         
        """
        pass
    
    ## Getter for property: (float) Tf
    ##  Returns the flange thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tf(self) -> float:
        """
        Getter for property: (float) Tf
         Returns the flange thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) Tw
    ##  Returns the web thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def Tw(self) -> float:
        """
        Getter for property: (float) Tw
         Returns the web thickness   
            
         
        """
        pass
    
    ## Getter for property: (float) W
    ##  Returns the width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def W(self) -> float:
        """
        Getter for property: (float) W
         Returns the width   
            
         
        """
        pass
    
    ##  Edit the section parameters 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    ## <param name="flangeThickness"> (float) </param>
    ## <param name="webThickness"> (float) </param>
    def Edit(self, width: float, height: float, flangeThickness: float, webThickness: float) -> None:
        """
         Edit the section parameters 
        """
        pass
    
import NXOpen
##  Represents a collection of IBeamSections  <br> Use @link CADCAEPrep::IdealizedBeamManager::IBeamSectionCollection CADCAEPrep::IdealizedBeamManager::IBeamSectionCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IBeamSectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of IBeamSections """
    pass


import NXOpen
##  Base abstract class for beam sections.  <br>   <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IBeamSection(NXOpen.NXObject): 
    """ Base abstract class for beam sections. """


    ##  the section type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ## </description> </item><item><term> 
    ## Sketch</term><description> 
    ## </description> </item><item><term> 
    ## Rod</term><description> 
    ## </description> </item><item><term> 
    ## Tube</term><description> 
    ## </description> </item><item><term> 
    ## Hexa</term><description> 
    ## </description> </item><item><term> 
    ## Bar</term><description> 
    ## </description> </item><item><term> 
    ## Box</term><description> 
    ## </description> </item><item><term> 
    ## T</term><description> 
    ## </description> </item><item><term> 
    ## L</term><description> 
    ## </description> </item><item><term> 
    ## I</term><description> 
    ## </description> </item><item><term> 
    ## Chan</term><description> 
    ## </description> </item></list>
    class Sectiontype(Enum):
        """
        Members Include: <Unknown> <Sketch> <Rod> <Tube> <Hexa> <Bar> <Box> <T> <L> <I> <Chan>
        """
        Unknown: int
        Sketch: int
        Rod: int
        Tube: int
        Hexa: int
        Bar: int
        Box: int
        T: int
        L: int
        I: int
        Chan: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> IBeamSection.Sectiontype:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Name
    ##  Returns the section name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the section name   
            
         
        """
        pass
    
    ## Getter for property: (@link IBeamSection.Sectiontype NXOpen.CADCAEPrep.IBeamSection.Sectiontype@endlink) Type
    ##  Returns the section type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return IBeamSection.Sectiontype
    @property
    def Type(self) -> IBeamSection.Sectiontype:
        """
        Getter for property: (@link IBeamSection.Sectiontype NXOpen.CADCAEPrep.IBeamSection.Sectiontype@endlink) Type
         Returns the section type   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of IdealizedBeams  <br> Use @link CADCAEPrep::IdealizedBeamManager::IdealizedBeamCollection CADCAEPrep::IdealizedBeamManager::IdealizedBeamCollection@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IdealizedBeamCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of IdealizedBeams """
    pass


import NXOpen
##  The object containing the information about the IdealizedBeamManager to be modified. <br> Use @link Part::IdealizedBeamManager Part::IdealizedBeamManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IdealizedBeamManager(NXOpen.Object): 
    """ The object containing the information about the IdealizedBeamManager to be modified."""


    ##  Returns the @link NXOpen::CADCAEPrep::IBeamSectionCollection NXOpen::CADCAEPrep::IBeamSectionCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @link IBeamSectionCollection NXOpen.CADCAEPrep.IBeamSectionCollection@endlink
    @property
    def IBeamSectionCollection() -> IBeamSectionCollection:
        """
         Returns the @link NXOpen::CADCAEPrep::IBeamSectionCollection NXOpen::CADCAEPrep::IBeamSectionCollection@endlink  belonging to this 
        """
        pass
    
    ##  Returns the @link NXOpen::CADCAEPrep::IdealizedBeamCollection NXOpen::CADCAEPrep::IdealizedBeamCollection@endlink  belonging to this 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @link IdealizedBeamCollection NXOpen.CADCAEPrep.IdealizedBeamCollection@endlink
    @property
    def IdealizedBeamCollection() -> IdealizedBeamCollection:
        """
         Returns the @link NXOpen::CADCAEPrep::IdealizedBeamCollection NXOpen::CADCAEPrep::IdealizedBeamCollection@endlink  belonging to this 
        """
        pass
    
    ##  Add a beam section Bar 
    ##  @return section (@link BeamSectionBar NXOpen.CADCAEPrep.BeamSectionBar@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    def AddBeamSectionBar(self, sectionName: str, width: float, height: float) -> BeamSectionBar:
        """
         Add a beam section Bar 
         @return section (@link BeamSectionBar NXOpen.CADCAEPrep.BeamSectionBar@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section Box
    ##  @return section (@link BeamSectionBox NXOpen.CADCAEPrep.BeamSectionBox@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    ## <param name="thicknessTopBottom"> (float) </param>
    ## <param name="thicknessSides"> (float) </param>
    def AddBeamSectionBox(self, sectionName: str, width: float, height: float, thicknessTopBottom: float, thicknessSides: float) -> BeamSectionBox:
        """
         Add a beam section Box
         @return section (@link BeamSectionBox NXOpen.CADCAEPrep.BeamSectionBox@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section Chan
    ##  @return section (@link BeamSectionChan NXOpen.CADCAEPrep.BeamSectionChan@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    ## <param name="flangeThickness"> (float) </param>
    ## <param name="webThickness"> (float) </param>
    def AddBeamSectionChan(self, sectionName: str, width: float, height: float, flangeThickness: float, webThickness: float) -> BeamSectionChan:
        """
         Add a beam section Chan
         @return section (@link BeamSectionChan NXOpen.CADCAEPrep.BeamSectionChan@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section Hexa
    ##  @return section (@link BeamSectionHexa NXOpen.CADCAEPrep.BeamSectionHexa@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="sideWidth"> (float) </param>
    ## <param name="overallWidth"> (float) </param>
    ## <param name="height"> (float) </param>
    def AddBeamSectionHexa(self, sectionName: str, sideWidth: float, overallWidth: float, height: float) -> BeamSectionHexa:
        """
         Add a beam section Hexa
         @return section (@link BeamSectionHexa NXOpen.CADCAEPrep.BeamSectionHexa@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section I 
    ##  @return section (@link BeamSectionI NXOpen.CADCAEPrep.BeamSectionI@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="height"> (float) </param>
    ## <param name="widthBottomFlange"> (float) </param>
    ## <param name="widthTopFlange"> (float) </param>
    ## <param name="thicknessWeb"> (float) </param>
    ## <param name="thicknessBottomFlange"> (float) </param>
    ## <param name="thicknessTopFlange"> (float) </param>
    def AddBeamSectionI(self, sectionName: str, height: float, widthBottomFlange: float, widthTopFlange: float, thicknessWeb: float, thicknessBottomFlange: float, thicknessTopFlange: float) -> BeamSectionI:
        """
         Add a beam section I 
         @return section (@link BeamSectionI NXOpen.CADCAEPrep.BeamSectionI@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section L 
    ##  @return section (@link BeamSectionL NXOpen.CADCAEPrep.BeamSectionL@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="lengthVertical"> (float) </param>
    ## <param name="lengthHorizontal"> (float) </param>
    ## <param name="thicknessVertical"> (float) </param>
    ## <param name="thicknessHorizontal"> (float) </param>
    def AddBeamSectionL(self, sectionName: str, lengthVertical: float, lengthHorizontal: float, thicknessVertical: float, thicknessHorizontal: float) -> BeamSectionL:
        """
         Add a beam section L 
         @return section (@link BeamSectionL NXOpen.CADCAEPrep.BeamSectionL@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section Rod
    ##  @return section (@link BeamSectionRod NXOpen.CADCAEPrep.BeamSectionRod@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="radius"> (float) </param>
    def AddBeamSectionRod(self, sectionName: str, radius: float) -> BeamSectionRod:
        """
         Add a beam section Rod
         @return section (@link BeamSectionRod NXOpen.CADCAEPrep.BeamSectionRod@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section Sketch 
    ##  @return section (@link BeamSectionSketch NXOpen.CADCAEPrep.BeamSectionSketch@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="sketchTag"> (@link NXOpen.Sketch NXOpen.Sketch@endlink) </param>
    def AddBeamSectionSketch(self, sectionName: str, sketchTag: NXOpen.Sketch) -> BeamSectionSketch:
        """
         Add a beam section Sketch 
         @return section (@link BeamSectionSketch NXOpen.CADCAEPrep.BeamSectionSketch@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section T
    ##  @return section (@link BeamSectionT NXOpen.CADCAEPrep.BeamSectionT@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="width"> (float) </param>
    ## <param name="height"> (float) </param>
    ## <param name="flangeThickness"> (float) </param>
    ## <param name="webThickness"> (float) </param>
    def AddBeamSectionT(self, sectionName: str, width: float, height: float, flangeThickness: float, webThickness: float) -> BeamSectionT:
        """
         Add a beam section T
         @return section (@link BeamSectionT NXOpen.CADCAEPrep.BeamSectionT@endlink):  the new section .
        """
        pass
    
    ##  Add a beam section Tube 
    ##  @return section (@link BeamSectionTube NXOpen.CADCAEPrep.BeamSectionTube@endlink):  the new section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    ## <param name="radiusOutside"> (float) </param>
    ## <param name="radiusInside"> (float) </param>
    def AddBeamSectionTube(self, sectionName: str, radiusOutside: float, radiusInside: float) -> BeamSectionTube:
        """
         Add a beam section Tube 
         @return section (@link BeamSectionTube NXOpen.CADCAEPrep.BeamSectionTube@endlink):  the new section .
        """
        pass
    
    ##  Add an idealized beam 
    ##  @return idealizedBeam (@link IdealizedBeam NXOpen.CADCAEPrep.IdealizedBeam@endlink):  the new idealized beam .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  the associated curve  </param>
    def AddIdealizedBeam(self, curve: NXOpen.Curve) -> IdealizedBeam:
        """
         Add an idealized beam 
         @return idealizedBeam (@link IdealizedBeam NXOpen.CADCAEPrep.IdealizedBeam@endlink):  the new idealized beam .
        """
        pass
    
    ##  Get idealized beam from curve 
    ##  @return ibeam (@link IdealizedBeam NXOpen.CADCAEPrep.IdealizedBeam@endlink):  the idealized beam .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="curve"> (@link NXOpen.Curve NXOpen.Curve@endlink)  the curve</param>
    def GetIdealizedBeam(self, curve: NXOpen.Curve) -> IdealizedBeam:
        """
         Get idealized beam from curve 
         @return ibeam (@link IdealizedBeam NXOpen.CADCAEPrep.IdealizedBeam@endlink):  the idealized beam .
        """
        pass
    
    ##  Get section by name 
    ##  @return section (@link IBeamSection NXOpen.CADCAEPrep.IBeamSection@endlink):  the section .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionName"> (str) </param>
    def GetSection(self, sectionName: str) -> IBeamSection:
        """
         Get section by name 
         @return section (@link IBeamSection NXOpen.CADCAEPrep.IBeamSection@endlink):  the section .
        """
        pass
    
import NXOpen
##  The object containing the information about the IdealizedBeam to be modified. <br>   <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IdealizedBeam(NXOpen.NXObject): 
    """ The object containing the information about the IdealizedBeam to be modified."""


    ## Getter for property: (@link NXOpen.Curve NXOpen.Curve@endlink) Curve
    ##  Returns the associated curve    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Curve
    @property
    def Curve(self) -> NXOpen.Curve:
        """
        Getter for property: (@link NXOpen.Curve NXOpen.Curve@endlink) Curve
         Returns the associated curve    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns the physical material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the physical material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns the physical material   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns the physical material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) MaterialBody
    ##  Returns the associated body used to infer the material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Body
    @property
    def MaterialBody(self) -> NXOpen.Body:
        """
        Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) MaterialBody
         Returns the associated body used to infer the material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) MaterialBody

    ##  Returns the associated body used to infer the material   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MaterialBody.setter
    def MaterialBody(self, body: NXOpen.Body):
        """
        Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) MaterialBody
         Returns the associated body used to infer the material   
            
         
        """
        pass
    
    ## Getter for property: (str) MeshCollectorPrefix
    ##  Returns the mesh collector prefix.  
    ##    
    ##                 The mesh collector prefix will be used to create the name of the mesh collector.
    ##                 If several idealized beams share the same mesh collector prefix, all the resulting meshes will be put in the same collector.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def MeshCollectorPrefix(self) -> str:
        """
        Getter for property: (str) MeshCollectorPrefix
         Returns the mesh collector prefix.  
           
                        The mesh collector prefix will be used to create the name of the mesh collector.
                        If several idealized beams share the same mesh collector prefix, all the resulting meshes will be put in the same collector.
                      
         
        """
        pass
    
    ## Setter for property: (str) MeshCollectorPrefix

    ##  Returns the mesh collector prefix.  
    ##    
    ##                 The mesh collector prefix will be used to create the name of the mesh collector.
    ##                 If several idealized beams share the same mesh collector prefix, all the resulting meshes will be put in the same collector.
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MeshCollectorPrefix.setter
    def MeshCollectorPrefix(self, meshCollectorPrefix: str):
        """
        Setter for property: (str) MeshCollectorPrefix
         Returns the mesh collector prefix.  
           
                        The mesh collector prefix will be used to create the name of the mesh collector.
                        If several idealized beams share the same mesh collector prefix, all the resulting meshes will be put in the same collector.
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetEnd
    ##  Returns the OffsetEnd: 
    ##                 Offset from the center of the bounding box to the curve end point, in the cross-section CSYS.  
    ##   
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Point2d
    @property
    def OffsetEnd(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetEnd
         Returns the OffsetEnd: 
                        Offset from the center of the bounding box to the curve end point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetEnd

    ##  Returns the OffsetEnd: 
    ##                 Offset from the center of the bounding box to the curve end point, in the cross-section CSYS.  
    ##   
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OffsetEnd.setter
    def OffsetEnd(self, offsetEnd: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetEnd
         Returns the OffsetEnd: 
                        Offset from the center of the bounding box to the curve end point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetStart
    ##  Returns the OffsetStart: 
    ##                 Offset from the center of the bounding box to the curve start point, in the cross-section CSYS.  
    ##   
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Point2d
    @property
    def OffsetStart(self) -> NXOpen.Point2d:
        """
        Getter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetStart
         Returns the OffsetStart: 
                        Offset from the center of the bounding box to the curve start point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetStart

    ##  Returns the OffsetStart: 
    ##                 Offset from the center of the bounding box to the curve start point, in the cross-section CSYS.  
    ##   
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OffsetStart.setter
    def OffsetStart(self, offsetStart: NXOpen.Point2d):
        """
        Setter for property: (@link NXOpen.Point2d NXOpen.Point2d@endlink) OffsetStart
         Returns the OffsetStart: 
                        Offset from the center of the bounding box to the curve start point, in the cross-section CSYS.  
          
                      
         
        """
        pass
    
    ## Getter for property: (@link IBeamSection NXOpen.CADCAEPrep.IBeamSection@endlink) Section
    ##  Returns the section   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return IBeamSection
    @property
    def Section(self) -> IBeamSection:
        """
        Getter for property: (@link IBeamSection NXOpen.CADCAEPrep.IBeamSection@endlink) Section
         Returns the section   
            
         
        """
        pass
    
    ## Setter for property: (@link IBeamSection NXOpen.CADCAEPrep.IBeamSection@endlink) Section

    ##  Returns the section   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Section.setter
    def Section(self, section: IBeamSection):
        """
        Setter for property: (@link IBeamSection NXOpen.CADCAEPrep.IBeamSection@endlink) Section
         Returns the section   
            
         
        """
        pass
    
    ## Getter for property: (float) XOffsetEnd
    ##  Returns the XOffsetEnd:
    ##                 the offset along the curve on end point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
    ##   
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def XOffsetEnd(self) -> float:
        """
        Getter for property: (float) XOffsetEnd
         Returns the XOffsetEnd:
                        the offset along the curve on end point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    
    ## Setter for property: (float) XOffsetEnd

    ##  Returns the XOffsetEnd:
    ##                 the offset along the curve on end point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
    ##   
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @XOffsetEnd.setter
    def XOffsetEnd(self, xOffsetEnd: float):
        """
        Setter for property: (float) XOffsetEnd
         Returns the XOffsetEnd:
                        the offset along the curve on end point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    
    ## Getter for property: (float) XOffsetStart
    ##  Returns the XOffsetStart:
    ##                 the offset along the curve on start point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
    ##   
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def XOffsetStart(self) -> float:
        """
        Getter for property: (float) XOffsetStart
         Returns the XOffsetStart:
                        the offset along the curve on start point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    
    ## Setter for property: (float) XOffsetStart

    ##  Returns the XOffsetStart:
    ##                 the offset along the curve on start point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
    ##   
    ##               
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @XOffsetStart.setter
    def XOffsetStart(self, xOffsetStart: float):
        """
        Setter for property: (float) XOffsetStart
         Returns the XOffsetStart:
                        the offset along the curve on start point side; Positive means inside the curve, negative means outside the curve (along the tangent).  
          
                      
         
        """
        pass
    
    ##  The orientation by vector:
    ##                  The section orientation is determined by the 3d vector parameter OrienVect that corresponds to either the Y axis or Z axis depending on the OrientAxis parameter.
    ##                  The coordinate system of the section is determined as follows:
    ##                     Its X axis correspond to the tagent to the curve
    ##                     Its Y or Z axis direction is given by the projection of OrientVect onto the Y,Z plane. As a consequence OrientVect should not be parallel to X.
    ##                     OrientAxis (ether Y or Z): indicates if the OrientVect is the Y or Z axis
    ##                     IOrientation::FlipY (boolean): flips the section around the Y axis
    ##                     IOrientation::FlipZ (boolean): flips the section around the Z axis             
    ##  @return A tuple consisting of (orientVect, orientAxis, flipY, flipZ). 
    ##  - orientVect is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.
    ##  - orientAxis is: @link OrientationByVector.OrientAxis NXOpen.CADCAEPrep.OrientationByVector.OrientAxis@endlink.
    ##  - flipY is: bool.
    ##  - flipZ is: bool.

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetOrientationByVector(self) -> Tuple[NXOpen.Vector3d, OrientationByVector.OrientAxis, bool, bool]:
        """
         The orientation by vector:
                         The section orientation is determined by the 3d vector parameter OrienVect that corresponds to either the Y axis or Z axis depending on the OrientAxis parameter.
                         The coordinate system of the section is determined as follows:
                            Its X axis correspond to the tagent to the curve
                            Its Y or Z axis direction is given by the projection of OrientVect onto the Y,Z plane. As a consequence OrientVect should not be parallel to X.
                            OrientAxis (ether Y or Z): indicates if the OrientVect is the Y or Z axis
                            IOrientation::FlipY (boolean): flips the section around the Y axis
                            IOrientation::FlipZ (boolean): flips the section around the Z axis             
         @return A tuple consisting of (orientVect, orientAxis, flipY, flipZ). 
         - orientVect is: @link NXOpen.Vector3d NXOpen.Vector3d@endlink.
         - orientAxis is: @link OrientationByVector.OrientAxis NXOpen.CADCAEPrep.OrientationByVector.OrientAxis@endlink.
         - flipY is: bool.
         - flipZ is: bool.

        """
        pass
    
    ##  Set the orientation by vector 
    ##                  The section orientation is determined by the 3d vector parameter OrienVect that corresponds to either the Y axis or Z axis depending on the OrientAxis parameter.
    ##                  The coordinate system of the section is determined as follows:
    ##                     Its X axis correspond to the tagent to the curve
    ##                     Its Y or Z axis direction is given by the projection of OrientVect onto the Y,Z plane. As a consequence OrientVect should not be parallel to X.
    ##                     OrientAxis (ether Y or Z): indicates if the OrientVect is the Y or Z axis
    ##                     IOrientation::FlipY (boolean): flips the section around the Y axis
    ##                     IOrientation::FlipZ (boolean): flips the section around the Z axis             
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="orientVect"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="orientAxis"> (@link OrientationByVector.OrientAxis NXOpen.CADCAEPrep.OrientationByVector.OrientAxis@endlink) </param>
    ## <param name="flipY"> (bool) </param>
    ## <param name="flipZ"> (bool) </param>
    def SetOrientationByVector(self, orientVect: NXOpen.Vector3d, orientAxis: OrientationByVector.OrientAxis, flipY: bool, flipZ: bool) -> None:
        """
         Set the orientation by vector 
                         The section orientation is determined by the 3d vector parameter OrienVect that corresponds to either the Y axis or Z axis depending on the OrientAxis parameter.
                         The coordinate system of the section is determined as follows:
                            Its X axis correspond to the tagent to the curve
                            Its Y or Z axis direction is given by the projection of OrientVect onto the Y,Z plane. As a consequence OrientVect should not be parallel to X.
                            OrientAxis (ether Y or Z): indicates if the OrientVect is the Y or Z axis
                            IOrientation::FlipY (boolean): flips the section around the Y axis
                            IOrientation::FlipZ (boolean): flips the section around the Z axis             
        """
        pass
    
import NXOpen
##  The object containing the information about the IOrientation.  <br> No instance of this base class, use specific children class getters in <ja>CADCAEPrep.IdealizedBeam</ja>  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class IOrientation(NXOpen.NXObject): 
    """ The object containing the information about the IOrientation. """
    pass


##  The object containing the information about the OrientationByVector. <br> Use @link CADCAEPrep::IdealizedBeam::GetOrientationByVector CADCAEPrep::IdealizedBeam::GetOrientationByVector@endlink  to get the properties of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class OrientationByVector(IOrientation): 
    """ The object containing the information about the OrientationByVector."""


    ##  the Orient Axis type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Y</term><description> 
    ##  Orient Axis along Y </description> </item><item><term> 
    ## Z</term><description> 
    ##  Orient Axis along Z </description> </item></list>
    class OrientAxis(Enum):
        """
        Members Include: <Y> <Z>
        """
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OrientationByVector.OrientAxis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
## @package NXOpen.CADCAEPrep
## Classes, Enums and Structs under NXOpen.CADCAEPrep namespace

##  @link IBeamSectionSectiontype NXOpen.CADCAEPrep.IBeamSectionSectiontype @endlink is an alias for @link IBeamSection.Sectiontype NXOpen.CADCAEPrep.IBeamSection.Sectiontype@endlink
IBeamSectionSectiontype = IBeamSection.Sectiontype


##  @link OrientationByVectorOrientAxis NXOpen.CADCAEPrep.OrientationByVectorOrientAxis @endlink is an alias for @link OrientationByVector.OrientAxis NXOpen.CADCAEPrep.OrientationByVector.OrientAxis@endlink
OrientationByVectorOrientAxis = OrientationByVector.OrientAxis


