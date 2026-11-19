from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents an object to manage Composites objects active states  <br> To obtain an instance of this class, refer to @link NXOpen::Composites::Manager  NXOpen::Composites::Manager @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ActivationManager(NXOpen.Object): 
    """ Represents an object to manage Composites objects active states """


    ##  Activate the indicated objects 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="objectTags"> (@link ICanBeDeactivated List[NXOpen.Composites.ICanBeDeactivated]@endlink) </param>
    def ActivateObjects(objectTags: List[ICanBeDeactivated]) -> None:
        """
         Activate the indicated objects 
        """
        pass
    
    ##  Deactivate the indicated objects 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="objectTags"> (@link ICanBeDeactivated List[NXOpen.Composites.ICanBeDeactivated]@endlink) </param>
    def DeactivateObjects(objectTags: List[ICanBeDeactivated]) -> None:
        """
         Deactivate the indicated objects 
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Creates or edits a @link Composites::PlyPiece Composites::PlyPiece@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateAddPlyPieceBuilder  NXOpen::Composites::Manager::CreateAddPlyPieceBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class AddPlyPieceBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.PlyPiece</ja_class> object.
    """


    ## Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion
    ##  Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::PlyPiece Composites::PlyPiece@endlink   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Features.Feature
    @property
    def BoundaryRegion(self) -> NXOpen.Features.Feature:
        """
        Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion
         Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::PlyPiece Composites::PlyPiece@endlink   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion

    ##  Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::PlyPiece Composites::PlyPiece@endlink   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoundaryRegion.setter
    def BoundaryRegion(self, region: NXOpen.Features.Feature):
        """
        Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion
         Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::PlyPiece Composites::PlyPiece@endlink   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectPly NXOpen.Composites.SelectPly@endlink) Ply
    ##  Returns the @link Composites::Ply Composites::Ply@endlink  to be spliced.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return SelectPly
    @property
    def Ply(self) -> SelectPly:
        """
        Getter for property: (@link SelectPly NXOpen.Composites.SelectPly@endlink) Ply
         Returns the @link Composites::Ply Composites::Ply@endlink  to be spliced.  
             
         
        """
        pass
    
##  Represents a single piece/layer of material to be deposited during manufacturing, defined using a splicing process  <br> Ply pieces are created with a splicing operation, e.g. @link Composites::AddPlyPieceBuilder Composites::AddPlyPieceBuilder@endlink .  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class AutomatedPlyPiece(Base): 
    """ Represents a single piece/layer of material to be deposited during manufacturing, defined using a splicing process """
    pass


import NXOpen
##  validator for a base composites data object.  <br> This is a test class.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class BaseObjectValidator(NXOpen.TaggedObject): 
    """ validator for a base composites data object. """
    pass


import NXOpen
##  Represents a base object, which other composite objects inherit functionality from  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Base(NXOpen.DisplayableObject): 
    """ Represents a base object, which other composite objects inherit functionality from """


    ##  Overrides the default function for setting an object's name, respecting the case of the provided name 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## 
    ## <param name="desiredName"> (str) </param>
    def SetName(self, desiredName: str) -> None:
        """
         Overrides the default function for setting an object's name, respecting the case of the provided name 
        """
        pass
    
import NXOpen
##  Represents a full-definition of a composite part, consisting of one or more @link Composites::Laminate Composites::Laminate@endlink  <br> CompositeParts cannot be manually created.  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class CompositePart(Base): 
    """ Represents a full-definition of a composite part, consisting of one or more <ja_class>Composites.Laminate</ja_class>"""


    ##  Insert options for resequencing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Before</term><description> 
    ## </description> </item><item><term> 
    ## After</term><description> 
    ## </description> </item></list>
    class ResequenceInsertOption(Enum):
        """
        Members Include: <Before> <After>
        """
        Before: int
        After: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CompositePart.ResequenceInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
    ##  Returns the center of mass of the @link Composites::CompositePart Composites::CompositePart@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
         Returns the center of mass of the @link Composites::CompositePart Composites::CompositePart@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Mass
    ##  Returns the mass of the @link Composites::CompositePart Composites::CompositePart@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the @link Composites::CompositePart Composites::CompositePart@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
    ##  Returns the moment of inertia of the @link Composites::CompositePart Composites::CompositePart@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
         Returns the moment of inertia of the @link Composites::CompositePart Composites::CompositePart@endlink .  
             
         
        """
        pass
    
    ##  The ordered list of cores of the @link Composites::CompositePart Composites::CompositePart@endlink . 
    ##  @return orderedCores (@link CrossSection List[NXOpen.Composites.CrossSection]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def GetOrderedCores(self) -> List[CrossSection]:
        """
         The ordered list of cores of the @link Composites::CompositePart Composites::CompositePart@endlink . 
         @return orderedCores (@link CrossSection List[NXOpen.Composites.CrossSection]@endlink): .
        """
        pass
    
    ##  The ordered list of laminates of the @link Composites::CompositePart Composites::CompositePart@endlink . 
    ##  @return orderedLaminates (@link Laminate List[NXOpen.Composites.Laminate]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def GetOrderedLaminates(self) -> List[Laminate]:
        """
         The ordered list of laminates of the @link Composites::CompositePart Composites::CompositePart@endlink . 
         @return orderedLaminates (@link Laminate List[NXOpen.Composites.Laminate]@endlink): .
        """
        pass
    
    ##  The ordered list of laminates and cores of the @link Composites::CompositePart Composites::CompositePart@endlink . 
    ##  @return orderedLaminatesAndCores (@link Base List[NXOpen.Composites.Base]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def GetOrderedLaminatesAndCores(self) -> List[Base]:
        """
         The ordered list of laminates and cores of the @link Composites::CompositePart Composites::CompositePart@endlink . 
         @return orderedLaminatesAndCores (@link Base List[NXOpen.Composites.Base]@endlink): .
        """
        pass
    
    ##  Resequences the given children before or after the provided target child. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## 
    ## <param name="children_to_resequence"> (@link Base List[NXOpen.Composites.Base]@endlink) </param>
    ## <param name="target_child"> (@link Base NXOpen.Composites.Base@endlink) </param>
    ## <param name="insert_option"> (@link CompositePart.ResequenceInsertOption NXOpen.Composites.CompositePart.ResequenceInsertOption@endlink) </param>
    def ResequenceChildren(self, children_to_resequence: List[Base], target_child: Base, insert_option: CompositePart.ResequenceInsertOption) -> None:
        """
         Resequences the given children before or after the provided target child. 
        """
        pass
    
import NXOpen
##  validator for the base composites data model in a part.  <br> This is a test class.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class CompositesCollectionValidator(NXOpen.TaggedObject): 
    """ validator for the base composites data model in a part. """


    ##  option of which edges to output in producibility 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EdgesFromFrontOfList</term><description> 
    ## </description> </item><item><term> 
    ## EdgesFromEndOfList</term><description> 
    ## </description> </item><item><term> 
    ## OutputAllEdges</term><description> 
    ## </description> </item></list>
    class EdgeOptionValue(Enum):
        """
        Members Include: <EdgesFromFrontOfList> <EdgesFromEndOfList> <OutputAllEdges>
        """
        EdgesFromFrontOfList: int
        EdgesFromEndOfList: int
        OutputAllEdges: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CompositesCollectionValidator.EdgeOptionValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  option of which nodes to output in producibility 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NodesFromFrontOfList</term><description> 
    ## </description> </item><item><term> 
    ## NodesFromEndOfList</term><description> 
    ## </description> </item><item><term> 
    ## OutputAllNodes</term><description> 
    ## </description> </item></list>
    class NodeOptionValue(Enum):
        """
        Members Include: <NodesFromFrontOfList> <NodesFromEndOfList> <OutputAllNodes>
        """
        NodesFromFrontOfList: int
        NodesFromEndOfList: int
        OutputAllNodes: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CompositesCollectionValidator.NodeOptionValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) OutputCompositeParts
    ##  Returns the flag controlling whether composite parts are included in the composites collection validation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def OutputCompositeParts(self) -> bool:
        """
        Getter for property: (bool) OutputCompositeParts
         Returns the flag controlling whether composite parts are included in the composites collection validation  
            
         
        """
        pass
    
    ## Setter for property: (bool) OutputCompositeParts

    ##  Returns the flag controlling whether composite parts are included in the composites collection validation  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @OutputCompositeParts.setter
    def OutputCompositeParts(self, outputCompositeParts: bool):
        """
        Setter for property: (bool) OutputCompositeParts
         Returns the flag controlling whether composite parts are included in the composites collection validation  
            
         
        """
        pass
    
    ## Getter for property: (bool) OutputDetailedObjectStatus
    ##  Returns the flag controlling whether detailed object status is included in the composites collection validation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def OutputDetailedObjectStatus(self) -> bool:
        """
        Getter for property: (bool) OutputDetailedObjectStatus
         Returns the flag controlling whether detailed object status is included in the composites collection validation  
            
         
        """
        pass
    
    ## Setter for property: (bool) OutputDetailedObjectStatus

    ##  Returns the flag controlling whether detailed object status is included in the composites collection validation  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @OutputDetailedObjectStatus.setter
    def OutputDetailedObjectStatus(self, outputDetailedObjectStatus: bool):
        """
        Setter for property: (bool) OutputDetailedObjectStatus
         Returns the flag controlling whether detailed object status is included in the composites collection validation  
            
         
        """
        pass
    
    ## Getter for property: (bool) OutputMassProperties
    ##  Returns the flag controlling whether to export the Mass Properties  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def OutputMassProperties(self) -> bool:
        """
        Getter for property: (bool) OutputMassProperties
         Returns the flag controlling whether to export the Mass Properties  
            
         
        """
        pass
    
    ## Setter for property: (bool) OutputMassProperties

    ##  Returns the flag controlling whether to export the Mass Properties  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OutputMassProperties.setter
    def OutputMassProperties(self, outputMassProperties: bool):
        """
        Setter for property: (bool) OutputMassProperties
         Returns the flag controlling whether to export the Mass Properties  
            
         
        """
        pass
    
    ## Getter for property: (bool) OutputRosettes
    ##  Returns the flag controlling whether rosettes are included in the composites collection validation  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def OutputRosettes(self) -> bool:
        """
        Getter for property: (bool) OutputRosettes
         Returns the flag controlling whether rosettes are included in the composites collection validation  
            
         
        """
        pass
    
    ## Setter for property: (bool) OutputRosettes

    ##  Returns the flag controlling whether rosettes are included in the composites collection validation  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @OutputRosettes.setter
    def OutputRosettes(self, outputRosettes: bool):
        """
        Setter for property: (bool) OutputRosettes
         Returns the flag controlling whether rosettes are included in the composites collection validation  
            
         
        """
        pass
    
import NXOpen
## 
##     Creates or edits a @link Composites::Core Composites::Core@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateCoreBuilder  NXOpen::Composites::Manager::CreateCoreBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class CoreBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.Core</ja_class> object.
    """


    ## Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) Solid
    ##  Returns the solid defining the shape of the @link Composites::Core Composites::Core@endlink   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Body
    @property
    def Solid(self) -> NXOpen.Body:
        """
        Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) Solid
         Returns the solid defining the shape of the @link Composites::Core Composites::Core@endlink   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) Solid

    ##  Returns the solid defining the shape of the @link Composites::Core Composites::Core@endlink   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Solid.setter
    def Solid(self, solid: NXOpen.Body):
        """
        Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) Solid
         Returns the solid defining the shape of the @link Composites::Core Composites::Core@endlink   
            
         
        """
        pass
    
import NXOpen
##  Represents a solid piece of material to be placed within a composite part  <br> To create or edit an instance of this class, use @link NXOpen::Composites::CoreBuilder  NXOpen::Composites::CoreBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Core(Base): 
    """ Represents a solid piece of material to be placed within a composite part """


    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
    ##  Returns the center of mass of the @link Composites::Core Composites::Core@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
         Returns the center of mass of the @link Composites::Core Composites::Core@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Density
    ##  Returns the density of the @link Composites::Core Composites::Core@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the density of the @link Composites::Core Composites::Core@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Mass
    ##  Returns the mass of the @link Composites::Core Composites::Core@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the @link Composites::Core Composites::Core@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
    ##  Returns the moment of inertia of the @link Composites::Core Composites::Core@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
         Returns the moment of inertia of the @link Composites::Core Composites::Core@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Volume
    ##  Returns the volume of the @link Composites::Core Composites::Core@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Volume(self) -> float:
        """
        Getter for property: (float) Volume
         Returns the volume of the @link Composites::Core Composites::Core@endlink .  
             
         
        """
        pass
    
import NXOpen
## 
##     Creates or edits a @link Composites::CrossSection Composites::CrossSection@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateCrossSectionBuilder  NXOpen::Composites::Manager::CreateCrossSectionBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## PlyScale </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class CrossSectionBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.CrossSection</ja_class> object.
    """


    ## Getter for property: (float) EndLimit
    ##  Returns the end limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Cross section will be trimmed by this limit.  
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def EndLimit(self) -> float:
        """
        Getter for property: (float) EndLimit
         Returns the end limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
    
    ## Setter for property: (float) EndLimit

    ##  Returns the end limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Cross section will be trimmed by this limit.  
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EndLimit.setter
    def EndLimit(self, endLimit: float):
        """
        Setter for property: (float) EndLimit
         Returns the end limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneSelect
    ##  Returns the plane to intersect composite objects of the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Results will be drawn in this @link Plane Plane@endlink .  
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Plane
    @property
    def PlaneSelect(self) -> NXOpen.Plane:
        """
        Getter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneSelect
         Returns the plane to intersect composite objects of the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Results will be drawn in this @link Plane Plane@endlink .  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneSelect

    ##  Returns the plane to intersect composite objects of the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Results will be drawn in this @link Plane Plane@endlink .  
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PlaneSelect.setter
    def PlaneSelect(self, planeSelect: NXOpen.Plane):
        """
        Setter for property: (@link NXOpen.Plane NXOpen.Plane@endlink) PlaneSelect
         Returns the plane to intersect composite objects of the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Results will be drawn in this @link Plane Plane@endlink .  
         
        """
        pass
    
    ## Getter for property: (float) PlyScale
    ##  Returns the scale for ply height in the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Each ply thickness will be multiplied by this value.  
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def PlyScale(self) -> float:
        """
        Getter for property: (float) PlyScale
         Returns the scale for ply height in the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Each ply thickness will be multiplied by this value.  
         
        """
        pass
    
    ## Setter for property: (float) PlyScale

    ##  Returns the scale for ply height in the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Each ply thickness will be multiplied by this value.  
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PlyScale.setter
    def PlyScale(self, plyScale: float):
        """
        Setter for property: (float) PlyScale
         Returns the scale for ply height in the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Each ply thickness will be multiplied by this value.  
         
        """
        pass
    
    ## Getter for property: (float) StartLimit
    ##  Returns the start limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Cross section will be trimmed by this limit.  
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def StartLimit(self) -> float:
        """
        Getter for property: (float) StartLimit
         Returns the start limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
    
    ## Setter for property: (float) StartLimit

    ##  Returns the start limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
    ##    Cross section will be trimmed by this limit.  
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @StartLimit.setter
    def StartLimit(self, startLimit: float):
        """
        Setter for property: (float) StartLimit
         Returns the start limit of the @link Composites::CrossSection Composites::CrossSection@endlink .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
    
##  Represents a composites planar cross section to visualize composite part geometry <br> To create or edit an instance of this class, use @link NXOpen::Composites::CrossSectionBuilder  NXOpen::Composites::CrossSectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class CrossSection(Base): 
    """ Represents a composites planar cross section to visualize composite part geometry"""
    pass


import NXOpen
## 
##     Creates or edits a @link Composites::Dart Composites::Dart@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateDartBuilder  NXOpen::Composites::Manager::CreateDartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DartBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.Dart</ja_class> object.
    """


    ## Getter for property: (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) Ply
    ##  Returns the @link Composites::IPly Composites::IPly@endlink  to be darted.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return SelectIPly
    @property
    def Ply(self) -> SelectIPly:
        """
        Getter for property: (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) Ply
         Returns the @link Composites::IPly Composites::IPly@endlink  to be darted.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section
    ##  Returns the section defining the single, open curve to cut into 
    ##         the @link Composites::Ply Composites::Ply@endlink 's surface   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section
         Returns the section defining the single, open curve to cut into 
                the @link Composites::Ply Composites::Ply@endlink 's surface   
            
         
        """
        pass
    
##  Represents an open curve to cut into a @link Composites::Ply Composites::Ply@endlink  boundary to alleviate material deformation in the @link Composites::Ply Composites::Ply@endlink 's producibility results  <br> To create or edit an instance of this class, use @link NXOpen::Composites::DartBuilder  NXOpen::Composites::DartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Dart(Base): 
    """ Represents an open curve to cut into a <ja_class>Composites.Ply</ja_class> boundary to alleviate material deformation in the <ja_class>Composites.Ply</ja_class>'s producibility results """
    pass


import NXOpen
## 
##     Creates or edits a @link Composites::DesignStation Composites::DesignStation@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateDesignStationBuilder  NXOpen::Composites::Manager::CreateDesignStationBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DesignStationBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.DesignStation</ja_class> object.
    """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##  Returns the @link Point Point@endlink  specifying where the @link Composites::DesignStation Composites::DesignStation@endlink  is calculated   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the @link Point Point@endlink  specifying where the @link Composites::DesignStation Composites::DesignStation@endlink  is calculated   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##  Returns the @link Point Point@endlink  specifying where the @link Composites::DesignStation Composites::DesignStation@endlink  is calculated   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Point.setter
    def Point(self, pointTag: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the @link Point Point@endlink  specifying where the @link Composites::DesignStation Composites::DesignStation@endlink  is calculated   
            
         
        """
        pass
    
##  Represents a definition of a Design Station to perform a virtual core sample on a composite part.  <br> Design Stations are created with a @link Composites::DesignStationBuilder Composites::DesignStationBuilder@endlink .  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DesignStation(Base): 
    """ Represents a definition of a Design Station to perform a virtual core sample on a composite part. """
    pass


import NXOpen
## 
##     Creates Flat Pattern to DXF Builder object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateFlatPatternToDXFBuilder  NXOpen::Composites::Manager::CreateFlatPatternToDXFBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

class FlatPatternToDxfBuilder(NXOpen.Builder): 
    """
    Creates Flat Pattern to DXF Builder object.
    """


    ## Getter for property: (str) DXFVersion
    ##  Returns the DXF Version of the DXF output.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    ## @return str
    @property
    def DXFVersion(self) -> str:
        """
        Getter for property: (str) DXFVersion
         Returns the DXF Version of the DXF output.  
             
         
        """
        pass
    
    ## Setter for property: (str) DXFVersion

    ##  Returns the DXF Version of the DXF output.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    @DXFVersion.setter
    def DXFVersion(self, dxfVersion: str):
        """
        Setter for property: (str) DXFVersion
         Returns the DXF Version of the DXF output.  
             
         
        """
        pass
    
    ## Getter for property: (str) ExportDirectory
    ##  Returns the file directory of the DXF output.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    ## @return str
    @property
    def ExportDirectory(self) -> str:
        """
        Getter for property: (str) ExportDirectory
         Returns the file directory of the DXF output.  
             
         
        """
        pass
    
    ## Setter for property: (str) ExportDirectory

    ##  Returns the file directory of the DXF output.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    @ExportDirectory.setter
    def ExportDirectory(self, exportDirectory: str):
        """
        Setter for property: (str) ExportDirectory
         Returns the file directory of the DXF output.  
             
         
        """
        pass
    
    ## Getter for property: (str) ExportFileName
    ##  Returns the file name of the DXF output.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    ## @return str
    @property
    def ExportFileName(self) -> str:
        """
        Getter for property: (str) ExportFileName
         Returns the file name of the DXF output.  
             
         
        """
        pass
    
    ## Setter for property: (str) ExportFileName

    ##  Returns the file name of the DXF output.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    @ExportFileName.setter
    def ExportFileName(self, exportFileName: str):
        """
        Setter for property: (str) ExportFileName
         Returns the file name of the DXF output.  
             
         
        """
        pass
    
    ## Getter for property: (@link IPly NXOpen.Composites.IPly@endlink) Ply
    ##  Returns the @link Composites::IPly Composites::IPly@endlink  to output flat pattern results for.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    ## @return IPly
    @property
    def Ply(self) -> IPly:
        """
        Getter for property: (@link IPly NXOpen.Composites.IPly@endlink) Ply
         Returns the @link Composites::IPly Composites::IPly@endlink  to output flat pattern results for.  
             
         
        """
        pass
    
    ## Setter for property: (@link IPly NXOpen.Composites.IPly@endlink) Ply

    ##  Returns the @link Composites::IPly Composites::IPly@endlink  to output flat pattern results for.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    @Ply.setter
    def Ply(self, plyTag: IPly):
        """
        Setter for property: (@link IPly NXOpen.Composites.IPly@endlink) Ply
         Returns the @link Composites::IPly Composites::IPly@endlink  to output flat pattern results for.  
             
         
        """
        pass
    
##  Represents a flat area of material to be draped onto a @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  to create a @link Composites::Ply Composites::Ply@endlink   <br> Flat Pattern objects are created from a @link Composites::Producibility Composites::Producibility@endlink .  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class FlatPattern(Base): 
    """ Represents a flat area of material to be draped onto a <ja_class>Composites.Features.LayupSurface</ja_class> to create a <ja_class>Composites.Ply</ja_class> """
    pass


import NXOpen
##  Interface for Composites objects that can be used with the @link Composites::ActivationManager Composites::ActivationManager@endlink  
## 
##   <br>  Created in NX2206.0.0  <br> 

class ICanBeDeactivated(NXOpen.INXObject): 
    """ Interface for Composites objects that can be used with the <ja_class>Composites.ActivationManager</ja_class> """
    pass


import NXOpen
##  Interface for Composites objects that can be used with the @link Composites::UpdateManager Composites::UpdateManager@endlink  
## 
##   <br>  Created in NX2306.0.0  <br> 

class ICanBeUpdated(NXOpen.INXObject): 
    """ Interface for Composites objects that can be used with the <ja_class>Composites.UpdateManager</ja_class> """
    pass


##  Interface for Composites objects that are the result of splicing operations
## 
##   <br>  Created in NX2406.0.0  <br> 

class IPlyPiece(IPly): 
    """ Interface for Composites objects that are the result of splicing operations"""
    pass


import NXOpen
##  Interface for Composites objects that can be used with the @link Composites::Ply Composites::Ply@endlink  and @link Composites::PlyPiece Composites::PlyPiece@endlink  objects
## 
##   <br>  Created in NX2312.0.0  <br> 

class IPly(NXOpen.INXObject): 
    """ Interface for Composites objects that can be used with the <ja_class>Composites.Ply</ja_class> and <ja_class>Composites.PlyPiece</ja_class> objects"""


    ## Getter for property: (float) Area
    ##  Returns the area of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    @abstractmethod
    def Area(self) -> float:
        """
        Getter for property: (float) Area
         Returns the area of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
    ##  Returns the center of mass of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    @abstractmethod
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
         Returns the center of mass of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) CuredThickness
    ##  Returns the cured thickness of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    @abstractmethod
    def CuredThickness(self) -> float:
        """
        Getter for property: (float) CuredThickness
         Returns the cured thickness of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Density
    ##  Returns the density of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    @abstractmethod
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the density of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Mass
    ##  Returns the mass of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    @abstractmethod
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
    ##  Returns the moment of inertia of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    @abstractmethod
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
         Returns the moment of inertia of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Perimeter
    ##  Returns the perimeter of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    @abstractmethod
    def Perimeter(self) -> float:
        """
        Getter for property: (float) Perimeter
         Returns the perimeter of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ##  Hide the ply's rosette-mapped orientation display 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    @abstractmethod
    def HideRosetteMappedOrientationDisplay(self) -> None:
        """
         Hide the ply's rosette-mapped orientation display 
        """
        pass
    
    ##  Show the ply's rosette-mapped orientation display 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    @abstractmethod
    def ShowRosetteMappedOrientationDisplay(self) -> None:
        """
         Show the ply's rosette-mapped orientation display 
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Creates or edits a @link Composites::Laminate Composites::Laminate@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateLaminateBuilder  NXOpen::Composites::Manager::CreateLaminateBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class LaminateBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.Laminate</ja_class> object.
    """


    ## Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) LayupSurface
    ##  Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  forming the surface upon which this laminate is defined    
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Features.Feature
    @property
    def LayupSurface(self) -> NXOpen.Features.Feature:
        """
        Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) LayupSurface
         Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  forming the surface upon which this laminate is defined    
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) LayupSurface

    ##  Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  forming the surface upon which this laminate is defined    
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @LayupSurface.setter
    def LayupSurface(self, frec: NXOpen.Features.Feature):
        """
        Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) LayupSurface
         Returns the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  forming the surface upon which this laminate is defined    
            
         
        """
        pass
    
    ## Getter for property: (@link Rosette NXOpen.Composites.Rosette@endlink) Rosette
    ##  Returns the @link Composites::Rosette Composites::Rosette@endlink  defining the @link Composites::Laminate Composites::Laminate@endlink 's coordinate system, providing an orientation reference for the @link Composites::Laminate Composites::Laminate@endlink 's child objects   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return Rosette
    @property
    def Rosette(self) -> Rosette:
        """
        Getter for property: (@link Rosette NXOpen.Composites.Rosette@endlink) Rosette
         Returns the @link Composites::Rosette Composites::Rosette@endlink  defining the @link Composites::Laminate Composites::Laminate@endlink 's coordinate system, providing an orientation reference for the @link Composites::Laminate Composites::Laminate@endlink 's child objects   
            
         
        """
        pass
    
    ## Setter for property: (@link Rosette NXOpen.Composites.Rosette@endlink) Rosette

    ##  Returns the @link Composites::Rosette Composites::Rosette@endlink  defining the @link Composites::Laminate Composites::Laminate@endlink 's coordinate system, providing an orientation reference for the @link Composites::Laminate Composites::Laminate@endlink 's child objects   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Rosette.setter
    def Rosette(self, rosette: Rosette):
        """
        Setter for property: (@link Rosette NXOpen.Composites.Rosette@endlink) Rosette
         Returns the @link Composites::Rosette Composites::Rosette@endlink  defining the @link Composites::Laminate Composites::Laminate@endlink 's coordinate system, providing an orientation reference for the @link Composites::Laminate Composites::Laminate@endlink 's child objects   
            
         
        """
        pass
    
import NXOpen
##  Represents a sequenced collection of composite objects to be manufactured on a layup surface  <br> Laminates are created with a @link Composites::LaminateBuilder Composites::LaminateBuilder@endlink .  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Laminate(Base): 
    """ Represents a sequenced collection of composite objects to be manufactured on a layup surface """


    ##  Insert options for resequencing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Before</term><description> 
    ## </description> </item><item><term> 
    ## After</term><description> 
    ## </description> </item></list>
    class ResequenceInsertOption(Enum):
        """
        Members Include: <Before> <After>
        """
        Before: int
        After: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Laminate.ResequenceInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
    ##  Returns the center of mass of the @link Composites::Laminate Composites::Laminate@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
         Returns the center of mass of the @link Composites::Laminate Composites::Laminate@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Mass
    ##  Returns the mass of the @link Composites::Laminate Composites::Laminate@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the @link Composites::Laminate Composites::Laminate@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
    ##  Returns the moment of inertia of the @link Composites::Laminate Composites::Laminate@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
         Returns the moment of inertia of the @link Composites::Laminate Composites::Laminate@endlink .  
             
         
        """
        pass
    
    ##  The ordered list of immediate child plies of the @link Composites::Laminate Composites::Laminate@endlink . These 
    ##         plies may be superceded by other objects in the final design 
    ##  @return orderedPlies (@link IPly List[NXOpen.Composites.IPly]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def GetOrderedImmediateChildPlies(self) -> List[IPly]:
        """
         The ordered list of immediate child plies of the @link Composites::Laminate Composites::Laminate@endlink . These 
                plies may be superceded by other objects in the final design 
         @return orderedPlies (@link IPly List[NXOpen.Composites.IPly]@endlink): .
        """
        pass
    
    ##  The ordered list of 'final' plies of the @link Composites::Laminate Composites::Laminate@endlink . These plies define the laminate
    ##         as it is intended to be manufactured. 
    ##  @return orderedPlies (@link IPly List[NXOpen.Composites.IPly]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def GetOrderedPlies(self) -> List[IPly]:
        """
         The ordered list of 'final' plies of the @link Composites::Laminate Composites::Laminate@endlink . These plies define the laminate
                as it is intended to be manufactured. 
         @return orderedPlies (@link IPly List[NXOpen.Composites.IPly]@endlink): .
        """
        pass
    
    ##  Resequences the given plies before or after the provided target ply. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## 
    ## <param name="plies_to_resequence"> (@link Ply List[NXOpen.Composites.Ply]@endlink) </param>
    ## <param name="target_ply"> (@link Ply NXOpen.Composites.Ply@endlink) </param>
    ## <param name="insert_option"> (@link Laminate.ResequenceInsertOption NXOpen.Composites.Laminate.ResequenceInsertOption@endlink) </param>
    def ResequencePlies(self, plies_to_resequence: List[Ply], target_ply: Ply, insert_option: Laminate.ResequenceInsertOption) -> None:
        """
         Resequences the given plies before or after the provided target ply. 
        """
        pass
    
import NXOpen
## 
##     Creates a laser projection file based on the current Composites definition
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class LaserProjectionExportBase(NXOpen.Builder): 
    """
    Creates a laser projection file based on the current Composites definition
    """


    ## Getter for property: (str) ExportFileName
    ##  Returns the base file name of the output file(s).  
    ##      
    ##  
    ## Getter License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ExportFileName(self) -> str:
        """
        Getter for property: (str) ExportFileName
         Returns the base file name of the output file(s).  
             
         
        """
        pass
    
    ## Setter for property: (str) ExportFileName

    ##  Returns the base file name of the output file(s).  
    ##      
    ##  
    ## Setter License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ExportFileName.setter
    def ExportFileName(self, exportFileName: str):
        """
        Setter for property: (str) ExportFileName
         Returns the base file name of the output file(s).  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) ReferenceCoordinateSystem
    ##  Returns the reference coordinate system for the laser projection system.  
    ##      
    ##  
    ## Getter License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.CartesianCoordinateSystem
    @property
    def ReferenceCoordinateSystem(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) ReferenceCoordinateSystem
         Returns the reference coordinate system for the laser projection system.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) ReferenceCoordinateSystem

    ##  Returns the reference coordinate system for the laser projection system.  
    ##      
    ##  
    ## Setter License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ReferenceCoordinateSystem.setter
    def ReferenceCoordinateSystem(self, referenceCsys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: (@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) ReferenceCoordinateSystem
         Returns the reference coordinate system for the laser projection system.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) ReferencePointsSelect
    ##  Returns the selection list containing reference points to output.  
    ##      
    ##  
    ## Getter License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def ReferencePointsSelect(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) ReferencePointsSelect
         Returns the selection list containing reference points to output.  
             
         
        """
        pass
    
    ##  Disable inserting additional points for long output boundary segments
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites_laser (" Export Laser Projection Data")
    def DisableMaximumStepLengthEnforcement(self) -> None:
        """
         Disable inserting additional points for long output boundary segments
        """
        pass
    
    ##  Enforce a maximum step length between consecutive points output for each output boundary
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ## <param name="maximumStepLength"> (float) </param>
    def EnableMaximumStepLengthEnforcement(self, maximumStepLength: float) -> None:
        """
         Enforce a maximum step length between consecutive points output for each output boundary
        """
        pass
    
    ##  Sets the export to use the Aligned Vision format 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def UseAlignedVisionOutputFormat(self) -> None:
        """
         Sets the export to use the Aligned Vision format 
        """
        pass
    
    ##  Sets the export to use the FARO BuildIT format 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def UseFAROOutputFormat(self) -> None:
        """
         Sets the export to use the FARO BuildIT format 
        """
        pass
    
    ##  Sets the export to use the LAP format 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def UseLAPOutputFormat(self) -> None:
        """
         Sets the export to use the LAP format 
        """
        pass
    
    ##  Sets the export to use the SL (Seiffert Lasertechnik) format 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def UseSLOutputFormat(self) -> None:
        """
         Sets the export to use the SL (Seiffert Lasertechnik) format 
        """
        pass
    
    ##  Sets the export to use the Virtek .ply format 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def UseVirtekPlyFormat(self) -> None:
        """
         Sets the export to use the Virtek .ply format 
        """
        pass
    
    ##  Sets the export to use the generic Composites Laser XML format 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def UseXMLOutputFormat(self) -> None:
        """
         Sets the export to use the generic Composites Laser XML format 
        """
        pass
    
## 
##     Creates a laser projection file based on the current Composites definition
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateLaserProjectionExport  NXOpen::Composites::Manager::CreateLaserProjectionExport @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class LaserProjectionExport(LaserProjectionExportBase): 
    """
    Creates a laser projection file based on the current Composites definition
    """


    ## Getter for property: (str) ExportDirectory
    ##  Returns the file directory to create the output file(s)   
    ##     
    ##  
    ## Getter License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ExportDirectory(self) -> str:
        """
        Getter for property: (str) ExportDirectory
         Returns the file directory to create the output file(s)   
            
         
        """
        pass
    
    ## Setter for property: (str) ExportDirectory

    ##  Returns the file directory to create the output file(s)   
    ##     
    ##  
    ## Setter License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ExportDirectory.setter
    def ExportDirectory(self, exportDirectory: str):
        """
        Setter for property: (str) ExportDirectory
         Returns the file directory to create the output file(s)   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Manages builders and common functionality of the Composites application  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Manages builders and common functionality of the Composites application """


    ##  Returns the @link Composites::ActivationManager Composites::ActivationManager@endlink  belonging to this manager 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @link ActivationManager NXOpen.Composites.ActivationManager@endlink
    @property
    def ActivationManager() -> ActivationManager:
        """
         Returns the @link Composites::ActivationManager Composites::ActivationManager@endlink  belonging to this manager 
        """
        pass
    
    ##  Returns the @link Composites::UpdateManager Composites::UpdateManager@endlink  belonging to this manager 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @link UpdateManager NXOpen.Composites.UpdateManager@endlink
    @property
    def UpdateManager() -> UpdateManager:
        """
         Returns the @link Composites::UpdateManager Composites::UpdateManager@endlink  belonging to this manager 
        """
        pass
    
    ##  Creates a @link Composites::AddPlyPieceBuilder Composites::AddPlyPieceBuilder@endlink  to define a ply piece for a spliced @link Composites::Ply Composites::Ply@endlink 
    ##  @return exportObject (@link AddPlyPieceBuilder NXOpen.Composites.AddPlyPieceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="plyPiece"> (@link PlyPiece NXOpen.Composites.PlyPiece@endlink) </param>
    def CreateAddPlyPieceBuilder(part: NXOpen.Part, plyPiece: PlyPiece) -> AddPlyPieceBuilder:
        """
         Creates a @link Composites::AddPlyPieceBuilder Composites::AddPlyPieceBuilder@endlink  to define a ply piece for a spliced @link Composites::Ply Composites::Ply@endlink 
         @return exportObject (@link AddPlyPieceBuilder NXOpen.Composites.AddPlyPieceBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::CoreBuilder Composites::CoreBuilder@endlink  to create or edit a @link Composites::Core Composites::Core@endlink  object 
    ##  @return builder (@link CoreBuilder NXOpen.Composites.CoreBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="core"> (@link Core NXOpen.Composites.Core@endlink) </param>
    def CreateCoreBuilder(part: NXOpen.Part, core: Core) -> CoreBuilder:
        """
         Creates a @link Composites::CoreBuilder Composites::CoreBuilder@endlink  to create or edit a @link Composites::Core Composites::Core@endlink  object 
         @return builder (@link CoreBuilder NXOpen.Composites.CoreBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::CrossSectionBuilder Composites::CrossSectionBuilder@endlink  to create or edit a @link Composites::CrossSection Composites::CrossSection@endlink  object 
    ##  @return builder (@link CrossSectionBuilder NXOpen.Composites.CrossSectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="crossSection"> (@link CrossSection NXOpen.Composites.CrossSection@endlink) </param>
    def CreateCrossSectionBuilder(part: NXOpen.Part, crossSection: CrossSection) -> CrossSectionBuilder:
        """
         Creates a @link Composites::CrossSectionBuilder Composites::CrossSectionBuilder@endlink  to create or edit a @link Composites::CrossSection Composites::CrossSection@endlink  object 
         @return builder (@link CrossSectionBuilder NXOpen.Composites.CrossSectionBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::DartBuilder Composites::DartBuilder@endlink  to create or edit a @link Composites::Dart Composites::Dart@endlink  object 
    ##  @return builder (@link DartBuilder NXOpen.Composites.DartBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="dart"> (@link Dart NXOpen.Composites.Dart@endlink) </param>
    def CreateDartBuilder(part: NXOpen.Part, dart: Dart) -> DartBuilder:
        """
         Creates a @link Composites::DartBuilder Composites::DartBuilder@endlink  to create or edit a @link Composites::Dart Composites::Dart@endlink  object 
         @return builder (@link DartBuilder NXOpen.Composites.DartBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::DesignStationBuilder Composites::DesignStationBuilder@endlink  to create or edit a @link Composites::DesignStation Composites::DesignStation@endlink  object 
    ##  @return builder (@link DesignStationBuilder NXOpen.Composites.DesignStationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="designStation"> (@link DesignStation NXOpen.Composites.DesignStation@endlink) </param>
    def CreateDesignStationBuilder(part: NXOpen.Part, designStation: DesignStation) -> DesignStationBuilder:
        """
         Creates a @link Composites::DesignStationBuilder Composites::DesignStationBuilder@endlink  to create or edit a @link Composites::DesignStation Composites::DesignStation@endlink  object 
         @return builder (@link DesignStationBuilder NXOpen.Composites.DesignStationBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::FlatPatternToDxfBuilder Composites::FlatPatternToDxfBuilder@endlink  to output flat patterns to a DXF file 
    ##  @return builder (@link FlatPatternToDxfBuilder NXOpen.Composites.FlatPatternToDxfBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  instead  <br> 

    ## License requirements: dxfdwg ("DxF/DWG Translator"), nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateFlatPatternToDXFBuilder(part: NXOpen.Part) -> FlatPatternToDxfBuilder:
        """
         Creates a @link Composites::FlatPatternToDxfBuilder Composites::FlatPatternToDxfBuilder@endlink  to output flat patterns to a DXF file 
         @return builder (@link FlatPatternToDxfBuilder NXOpen.Composites.FlatPatternToDxfBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::LaminateBuilder Composites::LaminateBuilder@endlink  to create or edit a @link Composites::Laminate Composites::Laminate@endlink  object 
    ##  @return builder (@link LaminateBuilder NXOpen.Composites.LaminateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="laminate"> (@link Laminate NXOpen.Composites.Laminate@endlink) </param>
    def CreateLaminateBuilder(part: NXOpen.Part, laminate: Laminate) -> LaminateBuilder:
        """
         Creates a @link Composites::LaminateBuilder Composites::LaminateBuilder@endlink  to create or edit a @link Composites::Laminate Composites::Laminate@endlink  object 
         @return builder (@link LaminateBuilder NXOpen.Composites.LaminateBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::LaserProjectionExport Composites::LaserProjectionExport@endlink  to generate files for a laser projection system 
    ##  @return exportObject (@link LaserProjectionExport NXOpen.Composites.LaserProjectionExport@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateLaserProjectionExport(part: NXOpen.Part) -> LaserProjectionExport:
        """
         Creates a @link Composites::LaserProjectionExport Composites::LaserProjectionExport@endlink  to generate files for a laser projection system 
         @return exportObject (@link LaserProjectionExport NXOpen.Composites.LaserProjectionExport@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::PlmLaserProjectionExport Composites::PlmLaserProjectionExport@endlink  to publish files for a laser projection system as datasets in Teamcenter 
    ##  @return exportObject (@link PlmLaserProjectionExport NXOpen.Composites.PlmLaserProjectionExport@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_composites_laser (" Export Laser Projection Data")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePlmLaserProjectionExport(part: NXOpen.Part) -> PlmLaserProjectionExport:
        """
         Creates a @link Composites::PlmLaserProjectionExport Composites::PlmLaserProjectionExport@endlink  to publish files for a laser projection system as datasets in Teamcenter 
         @return exportObject (@link PlmLaserProjectionExport NXOpen.Composites.PlmLaserProjectionExport@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::PlmPlyFlatPatternToDxfBuilder Composites::PlmPlyFlatPatternToDxfBuilder@endlink  to publish flat patterns DXF files as datasets in Teamcenter 
    ##  @return builder (@link PlmPlyFlatPatternToDxfBuilder NXOpen.Composites.PlmPlyFlatPatternToDxfBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: dxfdwg ("DxF/DWG Translator"), nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePlmPlyFlatPatternToDXFBuilder(part: NXOpen.Part) -> PlmPlyFlatPatternToDxfBuilder:
        """
         Creates a @link Composites::PlmPlyFlatPatternToDxfBuilder Composites::PlmPlyFlatPatternToDxfBuilder@endlink  to publish flat patterns DXF files as datasets in Teamcenter 
         @return builder (@link PlmPlyFlatPatternToDxfBuilder NXOpen.Composites.PlmPlyFlatPatternToDxfBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::PlyBuilder Composites::PlyBuilder@endlink  to create or edit a @link Composites::Ply Composites::Ply@endlink  object 
    ##  @return builder (@link PlyBuilder NXOpen.Composites.PlyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="ply"> (@link Ply NXOpen.Composites.Ply@endlink) </param>
    def CreatePlyBuilder(part: NXOpen.Part, ply: Ply) -> PlyBuilder:
        """
         Creates a @link Composites::PlyBuilder Composites::PlyBuilder@endlink  to create or edit a @link Composites::Ply Composites::Ply@endlink  object 
         @return builder (@link PlyBuilder NXOpen.Composites.PlyBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  to output multiple flat patterns to a DXF file 
    ##  @return builder (@link PlyFlatPatternToDxfBuilder NXOpen.Composites.PlyFlatPatternToDxfBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: dxfdwg ("DxF/DWG Translator"), nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePlyFlatPatternToDXFBuilder(part: NXOpen.Part) -> PlyFlatPatternToDxfBuilder:
        """
         Creates a @link Composites::PlyFlatPatternToDxfBuilder Composites::PlyFlatPatternToDxfBuilder@endlink  to output multiple flat patterns to a DXF file 
         @return builder (@link PlyFlatPatternToDxfBuilder NXOpen.Composites.PlyFlatPatternToDxfBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::PlyPMIBuilder Composites::PlyPMIBuilder@endlink  to create an annotation on a @link Composites::Ply Composites::Ply@endlink  object 
    ##  @return exportObject (@link PlyPMIBuilder NXOpen.Composites.PlyPMIBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="annotation"> (@link NXOpen.Annotations.SimpleDraftingAid NXOpen.Annotations.SimpleDraftingAid@endlink) </param>
    def CreatePlyPMIBuilder(part: NXOpen.Part, annotation: NXOpen.Annotations.SimpleDraftingAid) -> PlyPMIBuilder:
        """
         Creates a @link Composites::PlyPMIBuilder Composites::PlyPMIBuilder@endlink  to create an annotation on a @link Composites::Ply Composites::Ply@endlink  object 
         @return exportObject (@link PlyPMIBuilder NXOpen.Composites.PlyPMIBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::PreferencesBuilder Composites::PreferencesBuilder@endlink  to create or edit a @link Composites::Preferences Composites::Preferences@endlink  object.
    ##             The @link Composites::Preferences Composites::Preferences@endlink  object is one per part file. 
    ##  @return builder (@link PreferencesBuilder NXOpen.Composites.PreferencesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePreferencesBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates a @link Composites::PreferencesBuilder Composites::PreferencesBuilder@endlink  to create or edit a @link Composites::Preferences Composites::Preferences@endlink  object.
                    The @link Composites::Preferences Composites::Preferences@endlink  object is one per part file. 
         @return builder (@link PreferencesBuilder NXOpen.Composites.PreferencesBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::ProducibilityBuilder Composites::ProducibilityBuilder@endlink  to create or edit a @link Composites::Producibility Composites::Producibility@endlink  object
    ##  @return builder (@link ProducibilityBuilder NXOpen.Composites.ProducibilityBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="producibility"> (@link Producibility NXOpen.Composites.Producibility@endlink) </param>
    def CreateProducibilityBuilder(part: NXOpen.Part, producibility: Producibility) -> ProducibilityBuilder:
        """
         Creates a @link Composites::ProducibilityBuilder Composites::ProducibilityBuilder@endlink  to create or edit a @link Composites::Producibility Composites::Producibility@endlink  object
         @return builder (@link ProducibilityBuilder NXOpen.Composites.ProducibilityBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link Composites::RosetteBuilder Composites::RosetteBuilder@endlink  to create or edit a @link Composites::Rosette Composites::Rosette@endlink  object 
    ##  @return builder (@link RosetteBuilder NXOpen.Composites.RosetteBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="rosette"> (@link Rosette NXOpen.Composites.Rosette@endlink) </param>
    def CreateRosetteBuilder(part: NXOpen.Part, rosette: Rosette) -> RosetteBuilder:
        """
         Creates a @link Composites::RosetteBuilder Composites::RosetteBuilder@endlink  to create or edit a @link Composites::Rosette Composites::Rosette@endlink  object 
         @return builder (@link RosetteBuilder NXOpen.Composites.RosetteBuilder@endlink): .
        """
        pass
    
    ##  Gets the @link Composites::CompositePart Composites::CompositePart@endlink  in the part file if it exists 
    ##  @return compositePart (@link CompositePart NXOpen.Composites.CompositePart@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def GetCompositePart(part: NXOpen.Part) -> CompositePart:
        """
         Gets the @link Composites::CompositePart Composites::CompositePart@endlink  in the part file if it exists 
         @return compositePart (@link CompositePart NXOpen.Composites.CompositePart@endlink): .
        """
        pass
    
## 
##     Creates a laser projection file based on the current Composites definition and publishes it as a dataset in Teamcenter
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreatePlmLaserProjectionExport  NXOpen::Composites::Manager::CreatePlmLaserProjectionExport @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PlmLaserProjectionExport(LaserProjectionExportBase): 
    """
    Creates a laser projection file based on the current Composites definition and publishes it as a dataset in Teamcenter
    """
    pass


## 
##     Creates DXF Flat Pattern Plm Builder object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreatePlmPlyFlatPatternToDXFBuilder  NXOpen::Composites::Manager::CreatePlmPlyFlatPatternToDXFBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PlmPlyFlatPatternToDxfBuilder(PlyFlatPatternToDxfBuilderBase): 
    """
    Creates DXF Flat Pattern Plm Builder object.
    """
    pass


import NXOpen
import NXOpen.Features
## 
##     Creates or edits a @link Composites::Ply Composites::Ply@endlink  object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreatePlyBuilder  NXOpen::Composites::Manager::CreatePlyBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class PlyBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.Ply</ja_class> object.
    """


    ## Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion
    ##  Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::Ply Composites::Ply@endlink   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Features.Feature
    @property
    def BoundaryRegion(self) -> NXOpen.Features.Feature:
        """
        Getter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion
         Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::Ply Composites::Ply@endlink   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion

    ##  Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::Ply Composites::Ply@endlink   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoundaryRegion.setter
    def BoundaryRegion(self, region: NXOpen.Features.Feature):
        """
        Setter for property: (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) BoundaryRegion
         Returns the selected @link Composites::Features::Region Composites::Features::Region@endlink , defining the extents of the @link Composites::Ply Composites::Ply@endlink   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
    ##  Returns a material string   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns a material string   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material

    ##  Returns a material string   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) Material
         Returns a material string   
            
         
        """
        pass
    
    ## Getter for property: (str) OrientationString
    ##  Returns the @link Composites::Ply Composites::Ply@endlink 's orientation.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def OrientationString(self) -> str:
        """
        Getter for property: (str) OrientationString
         Returns the @link Composites::Ply Composites::Ply@endlink 's orientation.  
             
         
        """
        pass
    
    ## Setter for property: (str) OrientationString

    ##  Returns the @link Composites::Ply Composites::Ply@endlink 's orientation.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OrientationString.setter
    def OrientationString(self, orientationString: str):
        """
        Setter for property: (str) OrientationString
         Returns the @link Composites::Ply Composites::Ply@endlink 's orientation.  
             
         
        """
        pass
    
    ## Getter for property: (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) ParentLaminate
    ##  Returns the list containing the single selected parent @link Composites::Laminate Composites::Laminate@endlink .  
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectLaminate
    @property
    def ParentLaminate(self) -> SelectLaminate:
        """
        Getter for property: (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) ParentLaminate
         Returns the list containing the single selected parent @link Composites::Laminate Composites::Laminate@endlink .  
            
         
        """
        pass
    
import NXOpen
## 
##     Creates Flat Pattern to DXF Builder object.
##      <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PlyFlatPatternToDxfBuilderBase(NXOpen.Builder): 
    """
    Creates Flat Pattern to DXF Builder object.
    """


    ##  Determines the version of DXF file 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## VersionR12</term><description> 
    ## </description> </item><item><term> 
    ## VersionR13</term><description> 
    ## </description> </item><item><term> 
    ## VersionR14</term><description> 
    ## </description> </item><item><term> 
    ## Version2000</term><description> 
    ## </description> </item><item><term> 
    ## Version2004</term><description> 
    ## </description> </item><item><term> 
    ## Version2005</term><description> 
    ## </description> </item><item><term> 
    ## Version2007</term><description> 
    ## </description> </item><item><term> 
    ## VersionsFrom2010To2012</term><description> 
    ## </description> </item><item><term> 
    ## VersionsFrom2013To2017</term><description> 
    ## </description> </item><item><term> 
    ## VersionsFrom2018To2022</term><description> 
    ## </description> </item></list>
    class Dxf(Enum):
        """
        Members Include: <VersionR12> <VersionR13> <VersionR14> <Version2000> <Version2004> <Version2005> <Version2007> <VersionsFrom2010To2012> <VersionsFrom2013To2017> <VersionsFrom2018To2022>
        """
        VersionR12: int
        VersionR13: int
        VersionR14: int
        Version2000: int
        Version2004: int
        Version2005: int
        Version2007: int
        VersionsFrom2010To2012: int
        VersionsFrom2013To2017: int
        VersionsFrom2018To2022: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlyFlatPatternToDxfBuilderBase.Dxf:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PlyFlatPatternToDxfBuilderBase.Dxf NXOpen.Composites.PlyFlatPatternToDxfBuilderBase.Dxf@endlink) DXFVersion
    ##  Returns the DXF Version of the DXF output.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return PlyFlatPatternToDxfBuilderBase.Dxf
    @property
    def DXFVersion(self) -> PlyFlatPatternToDxfBuilderBase.Dxf:
        """
        Getter for property: (@link PlyFlatPatternToDxfBuilderBase.Dxf NXOpen.Composites.PlyFlatPatternToDxfBuilderBase.Dxf@endlink) DXFVersion
         Returns the DXF Version of the DXF output.  
             
         
        """
        pass
    
    ## Setter for property: (@link PlyFlatPatternToDxfBuilderBase.Dxf NXOpen.Composites.PlyFlatPatternToDxfBuilderBase.Dxf@endlink) DXFVersion

    ##  Returns the DXF Version of the DXF output.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DXFVersion.setter
    def DXFVersion(self, dxfVersion: PlyFlatPatternToDxfBuilderBase.Dxf):
        """
        Setter for property: (@link PlyFlatPatternToDxfBuilderBase.Dxf NXOpen.Composites.PlyFlatPatternToDxfBuilderBase.Dxf@endlink) DXFVersion
         Returns the DXF Version of the DXF output.  
             
         
        """
        pass
    
    ##  Adds a collection of @link Composites::IPly Composites::IPly@endlink  to output flat pattern results for. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## 
    ## <param name="iPlies"> (@link IPly List[NXOpen.Composites.IPly]@endlink) </param>
    def AddPlies(self, iPlies: List[IPly]) -> None:
        """
         Adds a collection of @link Composites::IPly Composites::IPly@endlink  to output flat pattern results for. 
        """
        pass
    
## 
##     Creates Flat Pattern to DXF Builder object.
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreatePlyFlatPatternToDXFBuilder  NXOpen::Composites::Manager::CreatePlyFlatPatternToDXFBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PlyFlatPatternToDxfBuilder(PlyFlatPatternToDxfBuilderBase): 
    """
    Creates Flat Pattern to DXF Builder object.
    """


    ## Getter for property: (str) ExportDirectory
    ##  Returns the file directory of the DXF output.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def ExportDirectory(self) -> str:
        """
        Getter for property: (str) ExportDirectory
         Returns the file directory of the DXF output.  
             
         
        """
        pass
    
    ## Setter for property: (str) ExportDirectory

    ##  Returns the file directory of the DXF output.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ExportDirectory.setter
    def ExportDirectory(self, exportDirectory: str):
        """
        Setter for property: (str) ExportDirectory
         Returns the file directory of the DXF output.  
             
         
        """
        pass
    
##  Represents a single piece/layer of material to be deposited during manufacturing  <br> Ply pieces are created with a splicing operation, e.g. @link Composites::AddPlyPieceBuilder Composites::AddPlyPieceBuilder@endlink .  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PlyPiece(Base): 
    """ Represents a single piece/layer of material to be deposited during manufacturing """
    pass


import NXOpen.Annotations
##  Creates or edits Composites @link NXOpen::Annotations::SimpleDraftingAid NXOpen::Annotations::SimpleDraftingAid@endlink  objects  <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreatePlyPMIBuilder  NXOpen::Composites::Manager::CreatePlyPMIBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class PlyPMIBuilder(NXOpen.Annotations.PmiNoteBuilder): 
    """ Creates or edits Composites <ja_class>NXOpen.Annotations.SimpleDraftingAid</ja_class> objects """
    pass


import NXOpen
##  Represents a single piece/layer of material to be deposited during manufacturing  <br> Plies are created with a @link Composites::PlyBuilder Composites::PlyBuilder@endlink .  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Ply(Base): 
    """ Represents a single piece/layer of material to be deposited during manufacturing """


    ##  Insert options for resequencing 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Before</term><description> 
    ## </description> </item><item><term> 
    ## After</term><description> 
    ## </description> </item></list>
    class ResequenceInsertOption(Enum):
        """
        Members Include: <Before> <After>
        """
        Before: int
        After: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Ply.ResequenceInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) Area
    ##  Returns the area of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Area(self) -> float:
        """
        Getter for property: (float) Area
         Returns the area of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
    ##  Returns the center of mass of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) CenterOfMass
         Returns the center of mass of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) CuredThickness
    ##  Returns the cured thickness of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def CuredThickness(self) -> float:
        """
        Getter for property: (float) CuredThickness
         Returns the cured thickness of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Density
    ##  Returns the density of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the density of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Mass
    ##  Returns the mass of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
    ##  Returns the moment of inertia of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) MomentOfInertia
         Returns the moment of inertia of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (float) Perimeter
    ##  Returns the perimeter of the @link Composites::IPly Composites::IPly@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def Perimeter(self) -> float:
        """
        Getter for property: (float) Perimeter
         Returns the perimeter of the @link Composites::IPly Composites::IPly@endlink .  
             
         
        """
        pass
    
    ##  The ordered list of @link Composites::IPlyPiece Composites::IPlyPiece@endlink  objects that this
    ##         @link Composites::Ply Composites::Ply@endlink  is broken up into 
    ##  @return orderedPlyPieces (@link IPlyPiece List[NXOpen.Composites.IPlyPiece]@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def GetOrderedIPlyPieces(self) -> List[IPlyPiece]:
        """
         The ordered list of @link Composites::IPlyPiece Composites::IPlyPiece@endlink  objects that this
                @link Composites::Ply Composites::Ply@endlink  is broken up into 
         @return orderedPlyPieces (@link IPlyPiece List[NXOpen.Composites.IPlyPiece]@endlink): .
        """
        pass
    
    ##  The ordered list of @link Composites::PlyPiece Composites::PlyPiece@endlink  objects that  this
    ##         @link Composites::Ply Composites::Ply@endlink  is broken up into 
    ##  @return orderedPlyPieces (@link PlyPiece List[NXOpen.Composites.PlyPiece]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use GetOrderedIPlyPieces instead  <br> 

    ## License requirements: nx_composites (" Composites")
    def GetOrderedPlyPieces(self) -> List[PlyPiece]:
        """
         The ordered list of @link Composites::PlyPiece Composites::PlyPiece@endlink  objects that  this
                @link Composites::Ply Composites::Ply@endlink  is broken up into 
         @return orderedPlyPieces (@link PlyPiece List[NXOpen.Composites.PlyPiece]@endlink): .
        """
        pass
    
    ##  Resequences the given @link Composites::IPlyPiece Composites::IPlyPiece@endlink  objects before or after the provided target @link Composites::IPlyPiece Composites::IPlyPiece@endlink . 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## 
    ## <param name="pieces_to_resequence"> (@link IPlyPiece List[NXOpen.Composites.IPlyPiece]@endlink) </param>
    ## <param name="target_ply_piece"> (@link IPlyPiece NXOpen.Composites.IPlyPiece@endlink) </param>
    ## <param name="insert_option"> (@link Ply.ResequenceInsertOption NXOpen.Composites.Ply.ResequenceInsertOption@endlink) </param>
    def ResequenceIPlyPieces(self, pieces_to_resequence: List[IPlyPiece], target_ply_piece: IPlyPiece, insert_option: Ply.ResequenceInsertOption) -> None:
        """
         Resequences the given @link Composites::IPlyPiece Composites::IPlyPiece@endlink  objects before or after the provided target @link Composites::IPlyPiece Composites::IPlyPiece@endlink . 
        """
        pass
    
    ##  Resequences the given ply pieces before or after the provided target ply piece. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2406.0.0.  Use ResequenceIPlyPieces instead  <br> 

    ## License requirements: nx_composites (" Composites")
    ## 
    ## <param name="pieces_to_resequence"> (@link PlyPiece List[NXOpen.Composites.PlyPiece]@endlink) </param>
    ## <param name="target_ply_piece"> (@link PlyPiece NXOpen.Composites.PlyPiece@endlink) </param>
    ## <param name="insert_option"> (@link Ply.ResequenceInsertOption NXOpen.Composites.Ply.ResequenceInsertOption@endlink) </param>
    def ResequencePlyPieces(self, pieces_to_resequence: List[PlyPiece], target_ply_piece: PlyPiece, insert_option: Ply.ResequenceInsertOption) -> None:
        """
         Resequences the given ply pieces before or after the provided target ply piece. 
        """
        pass
    
import NXOpen
## 
##     Creates or edits a @link Composites::Preferences Composites::Preferences@endlink  object
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreatePreferencesBuilder  NXOpen::Composites::Manager::CreatePreferencesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.Preferences</ja_class> object
    """


    ## Getter for property: (int) NegativeBiasDirectionColor
    ##  Returns the color of the primary direction   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def NegativeBiasDirectionColor(self) -> int:
        """
        Getter for property: (int) NegativeBiasDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    
    ## Setter for property: (int) NegativeBiasDirectionColor

    ##  Returns the color of the primary direction   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @NegativeBiasDirectionColor.setter
    def NegativeBiasDirectionColor(self, negativeBiasDirectionColor: int):
        """
        Setter for property: (int) NegativeBiasDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    
    ## Getter for property: (int) OtherDirectionColor
    ##  Returns the color of the primary direction   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def OtherDirectionColor(self) -> int:
        """
        Getter for property: (int) OtherDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    
    ## Setter for property: (int) OtherDirectionColor

    ##  Returns the color of the primary direction   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OtherDirectionColor.setter
    def OtherDirectionColor(self, otherDirectionColor: int):
        """
        Setter for property: (int) OtherDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) PlyLineWidth
    ##  Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Ply   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def PlyLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) PlyLineWidth
         Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Ply   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) PlyLineWidth

    ##  Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Ply   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PlyLineWidth.setter
    def PlyLineWidth(self, plyLineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) PlyLineWidth
         Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Ply   
            
         
        """
        pass
    
    ## Getter for property: (int) PositiveBiasDirectionColor
    ##  Returns the color of the positive bias direction   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def PositiveBiasDirectionColor(self) -> int:
        """
        Getter for property: (int) PositiveBiasDirectionColor
         Returns the color of the positive bias direction   
            
         
        """
        pass
    
    ## Setter for property: (int) PositiveBiasDirectionColor

    ##  Returns the color of the positive bias direction   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PositiveBiasDirectionColor.setter
    def PositiveBiasDirectionColor(self, positiveBiasDirectionColor: int):
        """
        Setter for property: (int) PositiveBiasDirectionColor
         Returns the color of the positive bias direction   
            
         
        """
        pass
    
    ## Getter for property: (int) PrimaryDirectionColor
    ##  Returns the color of the primary direction   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def PrimaryDirectionColor(self) -> int:
        """
        Getter for property: (int) PrimaryDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    
    ## Setter for property: (int) PrimaryDirectionColor

    ##  Returns the color of the primary direction   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PrimaryDirectionColor.setter
    def PrimaryDirectionColor(self, primaryDirectionColor: int):
        """
        Setter for property: (int) PrimaryDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) ProducibilityLineWidth
    ##  Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Producibility   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def ProducibilityLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) ProducibilityLineWidth
         Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Producibility   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) ProducibilityLineWidth

    ##  Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Producibility   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ProducibilityLineWidth.setter
    def ProducibilityLineWidth(self, producibilityLineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) ProducibilityLineWidth
         Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Producibility   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) RosetteLineWidth
    ##  Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Rosette   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.DisplayableObject.ObjectWidth
    @property
    def RosetteLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) RosetteLineWidth
         Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Rosette   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) RosetteLineWidth

    ##  Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Rosette   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RosetteLineWidth.setter
    def RosetteLineWidth(self, rosetteLineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: (@link NXOpen.DisplayableObject.ObjectWidth NXOpen.DisplayableObject.ObjectWidth@endlink) RosetteLineWidth
         Returns the @link DisplayableObject::ObjectWidth DisplayableObject::ObjectWidth@endlink  defining line width for Rosette   
            
         
        """
        pass
    
    ## Getter for property: (int) SecondaryDirectionColor
    ##  Returns the color of the secondary direction   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return int
    @property
    def SecondaryDirectionColor(self) -> int:
        """
        Getter for property: (int) SecondaryDirectionColor
         Returns the color of the secondary direction   
            
         
        """
        pass
    
    ## Setter for property: (int) SecondaryDirectionColor

    ##  Returns the color of the secondary direction   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SecondaryDirectionColor.setter
    def SecondaryDirectionColor(self, secondaryDirectionColor: int):
        """
        Setter for property: (int) SecondaryDirectionColor
         Returns the color of the secondary direction   
            
         
        """
        pass
    
##  Represents the Composites Preferences.  <br> Preferences are created with a @link Composites::PreferencesBuilder Composites::PreferencesBuilder@endlink .  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Preferences(Base): 
    """ Represents the Composites Preferences. """
    pass


import NXOpen
## 
##     Creates or edits a @link Composites::Producibility Composites::Producibility@endlink  object
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateProducibilityBuilder  NXOpen::Composites::Manager::CreateProducibilityBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ProducibilityBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.Producibility</ja_class> object
    """


    ## Getter for property: (float) CellSize
    ##  Returns the cell size of the @link Composites::Producibility Composites::Producibility@endlink  simulation.  
    ##    A smaller value creates denser results.   
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return float
    @property
    def CellSize(self) -> float:
        """
        Getter for property: (float) CellSize
         Returns the cell size of the @link Composites::Producibility Composites::Producibility@endlink  simulation.  
           A smaller value creates denser results.   
         
        """
        pass
    
    ## Setter for property: (float) CellSize

    ##  Returns the cell size of the @link Composites::Producibility Composites::Producibility@endlink  simulation.  
    ##    A smaller value creates denser results.   
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CellSize.setter
    def CellSize(self, cellSize: float):
        """
        Setter for property: (float) CellSize
         Returns the cell size of the @link Composites::Producibility Composites::Producibility@endlink  simulation.  
           A smaller value creates denser results.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
    ##  Returns the starting @link Point Point@endlink  of the @link Composites::Producibility Composites::Producibility@endlink .  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
         Returns the starting @link Point Point@endlink  of the @link Composites::Producibility Composites::Producibility@endlink .  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin

    ##  Returns the starting @link Point Point@endlink  of the @link Composites::Producibility Composites::Producibility@endlink .  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Origin.setter
    def Origin(self, originPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Origin
         Returns the starting @link Point Point@endlink  of the @link Composites::Producibility Composites::Producibility@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) OverrideCurveSection
    ##  Returns the geometry defining the desired primary fiber direction for the @link Composites::Producibility Composites::Producibility@endlink  simulation.  
    ##     This overrides any direction defined on the @link Composites::IPly Composites::IPly@endlink .   
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def OverrideCurveSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) OverrideCurveSection
         Returns the geometry defining the desired primary fiber direction for the @link Composites::Producibility Composites::Producibility@endlink  simulation.  
            This overrides any direction defined on the @link Composites::IPly Composites::IPly@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) Ply
    ##  Returns the @link Composites::IPly Composites::IPly@endlink  on which the @link Composites::Producibility Composites::Producibility@endlink  is run.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return SelectIPly
    @property
    def Ply(self) -> SelectIPly:
        """
        Getter for property: (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) Ply
         Returns the @link Composites::IPly Composites::IPly@endlink  on which the @link Composites::Producibility Composites::Producibility@endlink  is run.  
             
         
        """
        pass
    
    ##  Clears the current producibility simulation results, forcing a resimulation on commit 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def ClearResults(self) -> None:
        """
         Clears the current producibility simulation results, forcing a resimulation on commit 
        """
        pass
    
    ##  Sets the constraint propagation type to use a geodesic curve 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def SetConstraintPropagationTypeGeodesic(self) -> None:
        """
         Sets the constraint propagation type to use a geodesic curve 
        """
        pass
    
    ##  Sets the constraint propagation type to use the standard type. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def SetConstraintPropagationTypeStandard(self) -> None:
        """
         Sets the constraint propagation type to use the standard type. 
        """
        pass
    
    ##  Sets the constraint propagation type to use a user-specified curve 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def SetConstraintPropagationTypeToCurve(self) -> None:
        """
         Sets the constraint propagation type to use a user-specified curve 
        """
        pass
    
##  Represents a simulation showing the effects of draping a @link Composites::Ply Composites::Ply@endlink  onto a @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink   <br> Producibility Objects are created with a @link Composites::ProducibilityBuilder Composites::ProducibilityBuilder@endlink .  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Producibility(Base): 
    """ Represents a simulation showing the effects of draping a <ja_class>Composites.Ply</ja_class> onto a <ja_class>Composites.Features.LayupSurface</ja_class> """


    ##  Generate/update the @link Composites::FlatPattern Composites::FlatPattern@endlink  calculated from the draping simulation results
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    def PublishFlatPattern(self) -> None:
        """
         Generate/update the @link Composites::FlatPattern Composites::FlatPattern@endlink  calculated from the draping simulation results
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Creates or edits a @link Composites::Rosette Composites::Rosette@endlink  object
##      <br> To create a new instance of this class, use @link NXOpen::Composites::Manager::CreateRosetteBuilder  NXOpen::Composites::Manager::CreateRosetteBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class RosetteBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.Rosette</ja_class> object
    """


    ##  the information required for creating a standard-mapping rosette. 
    ## @link RosetteBuilderStandardRosetteInfo_Struct NXOpen.Composites.RosetteBuilderStandardRosetteInfo_Struct@endlink is an alias for @link RosetteBuilder.StandardRosetteInfo NXOpen.Composites.RosetteBuilder.StandardRosetteInfo@endlink.
    class StandardRosetteInfo:
        """
         the information required for creating a standard-mapping rosette. 
        @link RosetteBuilderStandardRosetteInfo_Struct NXOpen.Composites.RosetteBuilderStandardRosetteInfo_Struct@endlink is an alias for @link RosetteBuilder.StandardRosetteInfo NXOpen.Composites.RosetteBuilder.StandardRosetteInfo@endlink.
        """
        ## Getter for property :(@link NXOpen.Features.NXOpen.Point NXOpen.Features.NXOpen.Point@endlink) OriginPoint
        ## the @link Point Point@endlink  defining the point at which the standard-mapping rosette's zero direction is defined.
        ## @return @link NXOpen.Features.NXOpen.Point NXOpen.Features.NXOpen.Point@endlink
        @property
        def OriginPoint(self) -> NXOpen.Features.NXOpen.Point:
            """
            Getter for property OriginPoint
            the @link Point Point@endlink  defining the point at which the standard-mapping rosette's zero direction is defined.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Features.NXOpen.Point NXOpen.Features.NXOpen.Point@endlink) OriginPoint
        @OriginPoint.setter
        def OriginPoint(self, value: NXOpen.Features.NXOpen.Point):
            """
            Getter for property OriginPoint
            the @link Point Point@endlink  defining the point at which the standard-mapping rosette's zero direction is defined.
            Setter for property OriginPoint
            the @link Point Point@endlink  defining the point at which the standard-mapping rosette's zero direction is defined.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Features.NXOpen.Direction NXOpen.Features.NXOpen.Direction@endlink) ZeroDirection
        ## the @link Direction Direction@endlink  defining the zero direction of a standard-mapping rosette.
        ## @return @link NXOpen.Features.NXOpen.Direction NXOpen.Features.NXOpen.Direction@endlink
        @property
        def ZeroDirection(self) -> NXOpen.Features.NXOpen.Direction:
            """
            Getter for property ZeroDirection
            the @link Direction Direction@endlink  defining the zero direction of a standard-mapping rosette.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Features.NXOpen.Direction NXOpen.Features.NXOpen.Direction@endlink) ZeroDirection
        @ZeroDirection.setter
        def ZeroDirection(self, value: NXOpen.Features.NXOpen.Direction):
            """
            Getter for property ZeroDirection
            the @link Direction Direction@endlink  defining the zero direction of a standard-mapping rosette.
            Setter for property ZeroDirection
            the @link Direction Direction@endlink  defining the zero direction of a standard-mapping rosette.

            """
            pass
        
        ## Getter for property :(@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) LayupSurface
        ## the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  defining the surface the standard-mapping rosette's origin must lie on.
        ## @return @link NXOpen.Features.Feature NXOpen.Features.Feature@endlink
        @property
        def LayupSurface(self) -> NXOpen.Features.Feature:
            """
            Getter for property LayupSurface
            the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  defining the surface the standard-mapping rosette's origin must lie on.

            """
            pass
        
        ## Setter for property :(@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink) LayupSurface
        @LayupSurface.setter
        def LayupSurface(self, value: NXOpen.Features.Feature):
            """
            Getter for property LayupSurface
            the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  defining the surface the standard-mapping rosette's origin must lie on.
            Setter for property LayupSurface
            the @link Composites::Features::LayupSurface Composites::Features::LayupSurface@endlink  defining the surface the standard-mapping rosette's origin must lie on.

            """
            pass
        
    
    
    ##  the information required for creating a translational-mapping rosette. 
    ## @link RosetteBuilderTranslationalRosetteInfo_Struct NXOpen.Composites.RosetteBuilderTranslationalRosetteInfo_Struct@endlink is an alias for @link RosetteBuilder.TranslationalRosetteInfo NXOpen.Composites.RosetteBuilder.TranslationalRosetteInfo@endlink.
    class TranslationalRosetteInfo:
        """
         the information required for creating a translational-mapping rosette. 
        @link RosetteBuilderTranslationalRosetteInfo_Struct NXOpen.Composites.RosetteBuilderTranslationalRosetteInfo_Struct@endlink is an alias for @link RosetteBuilder.TranslationalRosetteInfo NXOpen.Composites.RosetteBuilder.TranslationalRosetteInfo@endlink.
        """
        ## Getter for property :(@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) ReferenceCsys
        ## the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location for translational-mapping rosette.
        ## @return @link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink
        @property
        def ReferenceCsys(self) -> NXOpen.CartesianCoordinateSystem:
            """
            Getter for property ReferenceCsys
            the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location for translational-mapping rosette.

            """
            pass
        
        ## Setter for property :(@link NXOpen.CartesianCoordinateSystem NXOpen.CartesianCoordinateSystem@endlink) ReferenceCsys
        @ReferenceCsys.setter
        def ReferenceCsys(self, value: NXOpen.CartesianCoordinateSystem):
            """
            Getter for property ReferenceCsys
            the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location for translational-mapping rosette.
            Setter for property ReferenceCsys
            the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location for translational-mapping rosette.

            """
            pass
        
    
    
    ## Getter for property: (@link RosetteBuilder.StandardRosetteInfo NXOpen.Composites.RosetteBuilder.StandardRosetteInfo@endlink) StandardRosetteData
    ##  Returns the @link Composites::RosetteBuilder::StandardRosetteInfo Composites::RosetteBuilder::StandardRosetteInfo@endlink  defining the data required for the standard-mapping rosette.  
    ##      
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return RosetteBuilder.StandardRosetteInfo
    @property
    def StandardRosetteData(self) -> RosetteBuilder.StandardRosetteInfo:
        """
        Getter for property: (@link RosetteBuilder.StandardRosetteInfo NXOpen.Composites.RosetteBuilder.StandardRosetteInfo@endlink) StandardRosetteData
         Returns the @link Composites::RosetteBuilder::StandardRosetteInfo Composites::RosetteBuilder::StandardRosetteInfo@endlink  defining the data required for the standard-mapping rosette.  
             
         
        """
        pass
    
    ## Setter for property: (@link RosetteBuilder.StandardRosetteInfo NXOpen.Composites.RosetteBuilder.StandardRosetteInfo@endlink) StandardRosetteData

    ##  Returns the @link Composites::RosetteBuilder::StandardRosetteInfo Composites::RosetteBuilder::StandardRosetteInfo@endlink  defining the data required for the standard-mapping rosette.  
    ##      
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @StandardRosetteData.setter
    def StandardRosetteData(self, standardRosetteData: RosetteBuilder.StandardRosetteInfo):
        """
        Setter for property: (@link RosetteBuilder.StandardRosetteInfo NXOpen.Composites.RosetteBuilder.StandardRosetteInfo@endlink) StandardRosetteData
         Returns the @link Composites::RosetteBuilder::StandardRosetteInfo Composites::RosetteBuilder::StandardRosetteInfo@endlink  defining the data required for the standard-mapping rosette.  
             
         
        """
        pass
    
    ## Getter for property: (@link RosetteBuilder.TranslationalRosetteInfo NXOpen.Composites.RosetteBuilder.TranslationalRosetteInfo@endlink) TranslationalRosetteData
    ##  Returns the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return RosetteBuilder.TranslationalRosetteInfo
    @property
    def TranslationalRosetteData(self) -> RosetteBuilder.TranslationalRosetteInfo:
        """
        Getter for property: (@link RosetteBuilder.TranslationalRosetteInfo NXOpen.Composites.RosetteBuilder.TranslationalRosetteInfo@endlink) TranslationalRosetteData
         Returns the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location   
            
         
        """
        pass
    
    ## Setter for property: (@link RosetteBuilder.TranslationalRosetteInfo NXOpen.Composites.RosetteBuilder.TranslationalRosetteInfo@endlink) TranslationalRosetteData

    ##  Returns the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location   
    ##     
    ##  
    ## Setter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @TranslationalRosetteData.setter
    def TranslationalRosetteData(self, translationalRosetteData: RosetteBuilder.TranslationalRosetteInfo):
        """
        Setter for property: (@link RosetteBuilder.TranslationalRosetteInfo NXOpen.Composites.RosetteBuilder.TranslationalRosetteInfo@endlink) TranslationalRosetteData
         Returns the @link CartesianCoordinateSystem CartesianCoordinateSystem@endlink  defining the orientations at a single location   
            
         
        """
        pass
    
##  Represents a coordinate system and mapping scheme to define reference orientations at various locations  <br> Rosettes are created with a @link Composites::RosetteBuilder Composites::RosetteBuilder@endlink .  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Rosette(Base): 
    """ Represents a coordinate system and mapping scheme to define reference orientations at various locations """
    pass


import NXOpen
import NXOpen.GeometricUtilities
##  Represents a single object selection.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectIPly(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link IPly NXOpen.Composites.IPly@endlink) Value
    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return IPly
    @property
    def Value(self) -> IPly:
        """
        Getter for property: (@link IPly NXOpen.Composites.IPly@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link IPly NXOpen.Composites.IPly@endlink) Value

    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: IPly):
        """
        Setter for property: (@link IPly NXOpen.Composites.IPly@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link IPly NXOpen.Composites.IPly@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[IPly, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link IPly NXOpen.Composites.IPly@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link IPly NXOpen.Composites.IPly@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link IPly NXOpen.Composites.IPly@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, IPly, NXOpen.View, NXOpen.Point3d, IPly, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link IPly NXOpen.Composites.IPly@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link IPly NXOpen.Composites.IPly@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link IPly NXOpen.Composites.IPly@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[IPly, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link IPly NXOpen.Composites.IPly@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) </param>
    ## <param name="selection"> (@link IPly NXOpen.Composites.IPly@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def SetValue(self, selection: IPly, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link IPly NXOpen.Composites.IPly@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  first selected object point</param>
    ## <param name="selection2"> (@link IPly NXOpen.Composites.IPly@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink)  second selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: IPly, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: IPly, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
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
    ## <param name="select_object"> (@link SelectIPly NXOpen.Composites.SelectIPly@endlink) </param>
    ## <param name="selection"> (@link IPly NXOpen.Composites.IPly@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def SetValue(self, selection: IPly, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a single object selection.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectLaminate(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link Laminate NXOpen.Composites.Laminate@endlink) Value
    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return Laminate
    @property
    def Value(self) -> Laminate:
        """
        Getter for property: (@link Laminate NXOpen.Composites.Laminate@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link Laminate NXOpen.Composites.Laminate@endlink) Value

    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: Laminate):
        """
        Setter for property: (@link Laminate NXOpen.Composites.Laminate@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link Laminate NXOpen.Composites.Laminate@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Laminate, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link Laminate NXOpen.Composites.Laminate@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link Laminate NXOpen.Composites.Laminate@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link Laminate NXOpen.Composites.Laminate@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Laminate, NXOpen.View, NXOpen.Point3d, Laminate, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link Laminate NXOpen.Composites.Laminate@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link Laminate NXOpen.Composites.Laminate@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link Laminate NXOpen.Composites.Laminate@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Laminate, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link Laminate NXOpen.Composites.Laminate@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) </param>
    ## <param name="selection"> (@link Laminate NXOpen.Composites.Laminate@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def SetValue(self, selection: Laminate, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Laminate NXOpen.Composites.Laminate@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  first selected object point</param>
    ## <param name="selection2"> (@link Laminate NXOpen.Composites.Laminate@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink)  second selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Laminate, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Laminate, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
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
    ## <param name="select_object"> (@link SelectLaminate NXOpen.Composites.SelectLaminate@endlink) </param>
    ## <param name="selection"> (@link Laminate NXOpen.Composites.Laminate@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def SetValue(self, selection: Laminate, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a single object selection.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectPly(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link Ply NXOpen.Composites.Ply@endlink) Value
    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return Ply
    @property
    def Value(self) -> Ply:
        """
        Getter for property: (@link Ply NXOpen.Composites.Ply@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link Ply NXOpen.Composites.Ply@endlink) Value

    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: Ply):
        """
        Setter for property: (@link Ply NXOpen.Composites.Ply@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link Ply NXOpen.Composites.Ply@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPly NXOpen.Composites.SelectPly@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Ply, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link Ply NXOpen.Composites.Ply@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link Ply NXOpen.Composites.Ply@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link Ply NXOpen.Composites.Ply@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPly NXOpen.Composites.SelectPly@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Ply, NXOpen.View, NXOpen.Point3d, Ply, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link Ply NXOpen.Composites.Ply@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link Ply NXOpen.Composites.Ply@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link Ply NXOpen.Composites.Ply@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPly NXOpen.Composites.SelectPly@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Ply, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link Ply NXOpen.Composites.Ply@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPly NXOpen.Composites.SelectPly@endlink) </param>
    ## <param name="selection"> (@link Ply NXOpen.Composites.Ply@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def SetValue(self, selection: Ply, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectPly NXOpen.Composites.SelectPly@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Ply NXOpen.Composites.Ply@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  first selected object point</param>
    ## <param name="selection2"> (@link Ply NXOpen.Composites.Ply@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink)  second selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Ply, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Ply, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
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
    ## <param name="select_object"> (@link SelectPly NXOpen.Composites.SelectPly@endlink) </param>
    ## <param name="selection"> (@link Ply NXOpen.Composites.Ply@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def SetValue(self, selection: Ply, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class SpliceCurveBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="objects"> (@link SpliceCurveBuilder List[NXOpen.Composites.SpliceCurveBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[SpliceCurveBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: SpliceCurveBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="obj"> (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: SpliceCurveBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="obj"> (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: SpliceCurveBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: SpliceCurveBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> SpliceCurveBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link SpliceCurveBuilder List[NXOpen.Composites.SpliceCurveBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[SpliceCurveBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link SpliceCurveBuilder List[NXOpen.Composites.SpliceCurveBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: SpliceCurveBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link SpliceCurveBuilder List[NXOpen.Composites.SpliceCurveBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[SpliceCurveBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SpliceCurveBuilderList NXOpen.Composites.SpliceCurveBuilderList@endlink) </param>
    ## <param name="object1"> (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link SpliceCurveBuilder NXOpen.Composites.SpliceCurveBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: SpliceCurveBuilder, object2: SpliceCurveBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
## 
##     Creates or edits a @link Composites::SpliceCurve Composites::SpliceCurve@endlink  object.
##      <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class SpliceCurveBuilder(NXOpen.Builder): 
    """
    Creates or edits a <ja_class>Composites.SpliceCurve</ja_class> object.
    """


    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section
    ##  Returns the section defining the base geometry of @link Composites::SpliceCurve Composites::SpliceCurve@endlink   
    ##     
    ##  
    ## Getter License requirements: nx_composites (" Composites")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) Section
         Returns the section defining the base geometry of @link Composites::SpliceCurve Composites::SpliceCurve@endlink   
            
         
        """
        pass
    
##  A curve used within a splice operation  <br> Splice curves are created by @link Composites::SpliceCurveBuilder Composites::SpliceCurveBuilder@endlink .  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class SpliceCurve(Base): 
    """ A curve used within a splice operation """
    pass


import NXOpen
##  Represents an object to update Composites objects  <br> To obtain an instance of this class, refer to @link NXOpen::Composites::Manager  NXOpen::Composites::Manager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class UpdateManager(NXOpen.Object): 
    """ Represents an object to update Composites objects """


    ##  Update the indicated objects 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_composites (" Composites")
    ## <param name="objectTags"> (@link ICanBeUpdated List[NXOpen.Composites.ICanBeUpdated]@endlink) </param>
    def UpdateObjects(objectTags: List[ICanBeUpdated]) -> None:
        """
         Update the indicated objects 
        """
        pass
    
## @package NXOpen.Composites
## Classes, Enums and Structs under NXOpen.Composites namespace

##  @link CompositePartResequenceInsertOption NXOpen.Composites.CompositePartResequenceInsertOption @endlink is an alias for @link CompositePart.ResequenceInsertOption NXOpen.Composites.CompositePart.ResequenceInsertOption@endlink
CompositePartResequenceInsertOption = CompositePart.ResequenceInsertOption


##  @link CompositesCollectionValidatorEdgeOptionValue NXOpen.Composites.CompositesCollectionValidatorEdgeOptionValue @endlink is an alias for @link CompositesCollectionValidator.EdgeOptionValue NXOpen.Composites.CompositesCollectionValidator.EdgeOptionValue@endlink
CompositesCollectionValidatorEdgeOptionValue = CompositesCollectionValidator.EdgeOptionValue


##  @link CompositesCollectionValidatorNodeOptionValue NXOpen.Composites.CompositesCollectionValidatorNodeOptionValue @endlink is an alias for @link CompositesCollectionValidator.NodeOptionValue NXOpen.Composites.CompositesCollectionValidator.NodeOptionValue@endlink
CompositesCollectionValidatorNodeOptionValue = CompositesCollectionValidator.NodeOptionValue


##  @link LaminateResequenceInsertOption NXOpen.Composites.LaminateResequenceInsertOption @endlink is an alias for @link Laminate.ResequenceInsertOption NXOpen.Composites.Laminate.ResequenceInsertOption@endlink
LaminateResequenceInsertOption = Laminate.ResequenceInsertOption


##  @link PlyFlatPatternToDxfBuilderBaseDxf NXOpen.Composites.PlyFlatPatternToDxfBuilderBaseDxf @endlink is an alias for @link PlyFlatPatternToDxfBuilderBase.Dxf NXOpen.Composites.PlyFlatPatternToDxfBuilderBase.Dxf@endlink
PlyFlatPatternToDxfBuilderBaseDxf = PlyFlatPatternToDxfBuilderBase.Dxf


##  @link PlyResequenceInsertOption NXOpen.Composites.PlyResequenceInsertOption @endlink is an alias for @link Ply.ResequenceInsertOption NXOpen.Composites.Ply.ResequenceInsertOption@endlink
PlyResequenceInsertOption = Ply.ResequenceInsertOption


## @link RosetteBuilderStandardRosetteInfo_Struct NXOpen.Composites.RosetteBuilderStandardRosetteInfo_Struct@endlink is an alias for @link RosetteBuilder.StandardRosetteInfo NXOpen.Composites.RosetteBuilder.StandardRosetteInfo@endlink.
RosetteBuilderStandardRosetteInfo_Struct = RosetteBuilder.StandardRosetteInfo


## @link RosetteBuilderTranslationalRosetteInfo_Struct NXOpen.Composites.RosetteBuilderTranslationalRosetteInfo_Struct@endlink is an alias for @link RosetteBuilder.TranslationalRosetteInfo NXOpen.Composites.RosetteBuilder.TranslationalRosetteInfo@endlink.
RosetteBuilderTranslationalRosetteInfo_Struct = RosetteBuilder.TranslationalRosetteInfo


