from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link NXOpen::Appearance::AppearanceDesignatorBuilder NXOpen::Appearance::AppearanceDesignatorBuilder@endlink 
##         The AppearanceDesignatorBuilder used to manipulate specific appearance designator
##         for appearance management.
##      <br> To create a new instance of this class, use @link NXOpen::Appearance::AppearanceManager::CreateAppearanceDesignatorBuilder  NXOpen::Appearance::AppearanceManager::CreateAppearanceDesignatorBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class AppearanceDesignatorBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Appearance.AppearanceDesignatorBuilder</ja_class>
        The AppearanceDesignatorBuilder used to manipulate specific appearance designator
        for appearance management.
    """


    ## Getter for property: (str) DesignatorDescription
    ##  Returns the designator description   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def DesignatorDescription(self) -> str:
        """
        Getter for property: (str) DesignatorDescription
         Returns the designator description   
            
         
        """
        pass
    
    ## Setter for property: (str) DesignatorDescription

    ##  Returns the designator description   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DesignatorDescription.setter
    def DesignatorDescription(self, designatorDescription: str):
        """
        Setter for property: (str) DesignatorDescription
         Returns the designator description   
            
         
        """
        pass
    
    ## Getter for property: (str) DesignatorName
    ##  Returns the designator name   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def DesignatorName(self) -> str:
        """
        Getter for property: (str) DesignatorName
         Returns the designator name   
            
         
        """
        pass
    
    ## Setter for property: (str) DesignatorName

    ##  Returns the designator name   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DesignatorName.setter
    def DesignatorName(self, designatorName: str):
        """
        Setter for property: (str) DesignatorName
         Returns the designator name   
            
         
        """
        pass
    
    ## Getter for property: (str) ParentAppearanceArea
    ##  Returns the appearance area   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def ParentAppearanceArea(self) -> str:
        """
        Getter for property: (str) ParentAppearanceArea
         Returns the appearance area   
            
         
        """
        pass
    
    ## Setter for property: (str) ParentAppearanceArea

    ##  Returns the appearance area   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ParentAppearanceArea.setter
    def ParentAppearanceArea(self, parentAppearanceArea: str):
        """
        Setter for property: (str) ParentAppearanceArea
         Returns the appearance area   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectionList
    ##  Returns the selection list   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectionList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectionList
         Returns the selection list   
            
         
        """
        pass
    
    ##  This function will remove conflicted face material
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="conflictDesignatorTag"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="conflictAppMat"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    ## <param name="conflictEntities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink) </param>
    def RemoveConflictedFaceMaterial(self, conflictDesignatorTag: List[NXOpen.TaggedObject], conflictAppMat: List[NXOpen.TaggedObject], conflictEntities: List[NXOpen.TaggedObject]) -> None:
        """
         This function will remove conflicted face material
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::Appearance::AppearanceEditTexture NXOpen::Appearance::AppearanceEditTexture@endlink 
##         The AppearanceEditTexture used to manipulate texture space of appearance material
##         for appearance designator.
## 
##      <br> To create a new instance of this class, use @link NXOpen::Appearance::AppearanceManager::CreateAppearanceEditTextureBuilder  NXOpen::Appearance::AppearanceManager::CreateAppearanceEditTextureBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AppearanceEditTexture(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Appearance.AppearanceEditTexture</ja_class>
        The AppearanceEditTexture used to manipulate texture space of appearance material
        for appearance designator.

    """


    ##  AnchorTypes 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TopLeft</term><description> 
    ## </description> </item><item><term> 
    ## Center</term><description> 
    ## </description> </item><item><term> 
    ## BottomLeft</term><description> 
    ## </description> </item><item><term> 
    ## TopMiddle</term><description> 
    ## </description> </item><item><term> 
    ## TopRight</term><description> 
    ## </description> </item><item><term> 
    ## LeftMiddle</term><description> 
    ## </description> </item><item><term> 
    ## RightMiddle</term><description> 
    ## </description> </item><item><term> 
    ## BottomMiddle</term><description> 
    ## </description> </item><item><term> 
    ## BottomRight</term><description> 
    ## </description> </item></list>
    class AnchorTypes(Enum):
        """
        Members Include: <TopLeft> <Center> <BottomLeft> <TopMiddle> <TopRight> <LeftMiddle> <RightMiddle> <BottomMiddle> <BottomRight>
        """
        TopLeft: int
        Center: int
        BottomLeft: int
        TopMiddle: int
        TopRight: int
        LeftMiddle: int
        RightMiddle: int
        BottomMiddle: int
        BottomRight: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.AnchorTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  DecalMappingProjections 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Planar</term><description> 
    ## </description> </item><item><term> 
    ## Cylindrical</term><description> 
    ## </description> </item><item><term> 
    ## Spherical</term><description> 
    ## </description> </item><item><term> 
    ## Uv</term><description> 
    ## </description> </item></list>
    class DecalProjectionsType(Enum):
        """
        Members Include: <Planar> <Cylindrical> <Spherical> <Uv>
        """
        Planar: int
        Cylindrical: int
        Spherical: int
        Uv: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.DecalProjectionsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  BaseMaterialMappingProjections 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Uv</term><description> 
    ## </description> </item><item><term> 
    ## Planar</term><description> 
    ## </description> </item><item><term> 
    ## Box</term><description> 
    ## </description> </item><item><term> 
    ## Spherical</term><description> 
    ## </description> </item><item><term> 
    ## Cylindrical</term><description> 
    ## </description> </item></list>
    class MaterialProjectionsType(Enum):
        """
        Members Include: <Uv> <Planar> <Box> <Spherical> <Cylindrical>
        """
        Uv: int
        Planar: int
        Box: int
        Spherical: int
        Cylindrical: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.MaterialProjectionsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Scaling 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ToFace</term><description> 
    ## </description> </item><item><term> 
    ## ToImageSize</term><description> 
    ## </description> </item><item><term> 
    ## ToUniformScale</term><description> 
    ## </description> </item><item><term> 
    ## ToNonUniformScale</term><description> 
    ## </description> </item></list>
    class Scaling(Enum):
        """
        Members Include: <ToFace> <ToImageSize> <ToUniformScale> <ToNonUniformScale>
        """
        ToFace: int
        ToImageSize: int
        ToUniformScale: int
        ToNonUniformScale: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.Scaling:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AppearanceEditTexture.AnchorTypes NXOpen.Appearance.AppearanceEditTexture.AnchorTypes@endlink) AnchorType
    ##  Returns the anchor type   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AppearanceEditTexture.AnchorTypes
    @property
    def AnchorType(self) -> AppearanceEditTexture.AnchorTypes:
        """
        Getter for property: (@link AppearanceEditTexture.AnchorTypes NXOpen.Appearance.AppearanceEditTexture.AnchorTypes@endlink) AnchorType
         Returns the anchor type   
            
         
        """
        pass
    
    ## Setter for property: (@link AppearanceEditTexture.AnchorTypes NXOpen.Appearance.AppearanceEditTexture.AnchorTypes@endlink) AnchorType

    ##  Returns the anchor type   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AnchorType.setter
    def AnchorType(self, anchorType: AppearanceEditTexture.AnchorTypes):
        """
        Setter for property: (@link AppearanceEditTexture.AnchorTypes NXOpen.Appearance.AppearanceEditTexture.AnchorTypes@endlink) AnchorType
         Returns the anchor type   
            
         
        """
        pass
    
    ## Getter for property: (float) AspectRatio
    ##  Returns the decal aspect ratio   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def AspectRatio(self) -> float:
        """
        Getter for property: (float) AspectRatio
         Returns the decal aspect ratio   
            
         
        """
        pass
    
    ## Setter for property: (float) AspectRatio

    ##  Returns the decal aspect ratio   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AspectRatio.setter
    def AspectRatio(self, aspect_ratio: float):
        """
        Setter for property: (float) AspectRatio
         Returns the decal aspect ratio   
            
         
        """
        pass
    
    ## Getter for property: (int) MappingProjection
    ##  Returns the mapping projection   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def MappingProjection(self) -> int:
        """
        Getter for property: (int) MappingProjection
         Returns the mapping projection   
            
         
        """
        pass
    
    ## Setter for property: (int) MappingProjection

    ##  Returns the mapping projection   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MappingProjection.setter
    def MappingProjection(self, mappingProjection: int):
        """
        Setter for property: (int) MappingProjection
         Returns the mapping projection   
            
         
        """
        pass
    
    ## Getter for property: (float) Scale
    ##  Returns the decal scale  
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the decal scale  
            
         
        """
        pass
    
    ## Setter for property: (float) Scale

    ##  Returns the decal scale  
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the decal scale  
            
         
        """
        pass
    
    ## Getter for property: (str) StudioMaterialName
    ##  Returns the studio material name   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def StudioMaterialName(self) -> str:
        """
        Getter for property: (str) StudioMaterialName
         Returns the studio material name   
            
         
        """
        pass
    
    ## Setter for property: (str) StudioMaterialName

    ##  Returns the studio material name   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @StudioMaterialName.setter
    def StudioMaterialName(self, studioMaterialName: str):
        """
        Setter for property: (str) StudioMaterialName
         Returns the studio material name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureNormalVector
    ##  Returns the texture normal vector   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def TextureNormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureNormalVector
         Returns the texture normal vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureNormalVector

    ##  Returns the texture normal vector   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TextureNormalVector.setter
    def TextureNormalVector(self, textureNormalVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureNormalVector
         Returns the texture normal vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextureOrigin
    ##  Returns the texture origin   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def TextureOrigin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextureOrigin
         Returns the texture origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextureOrigin

    ##  Returns the texture origin   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TextureOrigin.setter
    def TextureOrigin(self, textureOrigin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TextureOrigin
         Returns the texture origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureUpVector
    ##  Returns the texture up vector   
    ##     
    ##  
    ## Getter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def TextureUpVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureUpVector
         Returns the texture up vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureUpVector

    ##  Returns the texture up vector   
    ##     
    ##  
    ## Setter License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TextureUpVector.setter
    def TextureUpVector(self, textureUpVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) TextureUpVector
         Returns the texture up vector   
            
         
        """
        pass
    
import NXOpen
##  Represents an object that manages Appearance application specific objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class AppearanceManager(NXOpen.Object): 
    """ Represents an object that manages Appearance application specific objects. """


    ##  Creates a @link NXOpen::Appearance::AppearanceDesignatorBuilder NXOpen::Appearance::AppearanceDesignatorBuilder@endlink  object 
    ##  @return builder (@link AppearanceDesignatorBuilder NXOpen.Appearance.AppearanceDesignatorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="schemeName"> (str) </param>
    def CreateAppearanceDesignatorBuilder(self, schemeName: str) -> AppearanceDesignatorBuilder:
        """
         Creates a @link NXOpen::Appearance::AppearanceDesignatorBuilder NXOpen::Appearance::AppearanceDesignatorBuilder@endlink  object 
         @return builder (@link AppearanceDesignatorBuilder NXOpen.Appearance.AppearanceDesignatorBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Appearance::AppearanceEditTexture NXOpen::Appearance::AppearanceEditTexture@endlink  object 
    ##  @return builder (@link AppearanceEditTexture NXOpen.Appearance.AppearanceEditTexture@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="designatorName"> (str) </param>
    ## <param name="schemeName"> (str) </param>
    def CreateAppearanceEditTextureBuilder(self, designatorName: str, schemeName: str) -> AppearanceEditTexture:
        """
         Creates a @link NXOpen::Appearance::AppearanceEditTexture NXOpen::Appearance::AppearanceEditTexture@endlink  object 
         @return builder (@link AppearanceEditTexture NXOpen.Appearance.AppearanceEditTexture@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::Appearance::AppearanceSchemeBuilder NXOpen::Appearance::AppearanceSchemeBuilder@endlink  
    ##  @return builder (@link AppearanceSchemeBuilder NXOpen.Appearance.AppearanceSchemeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def CreateAppearanceSchemeBuilder(self) -> AppearanceSchemeBuilder:
        """
         Creates a @link NXOpen::Appearance::AppearanceSchemeBuilder NXOpen::Appearance::AppearanceSchemeBuilder@endlink  
         @return builder (@link AppearanceSchemeBuilder NXOpen.Appearance.AppearanceSchemeBuilder@endlink): .
        """
        pass
    
    ##  This function will set the input product assembly which has the appearance data
    ##  @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    ## 
    ## <param name="productAssembly"> (str) </param>
    def SetProductAssembly(self, productAssembly: str) -> NXOpen.ErrorList:
        """
         This function will set the input product assembly which has the appearance data
         @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
    ##  This function will do full unload of appearance schemes present in session 
    ##  @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def UnloadAllAppearanceData(self) -> NXOpen.ErrorList:
        """
         This function will do full unload of appearance schemes present in session 
         @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
import NXOpen
##  Represents a builder class that creates the new Appearance Scheme
##      <br> To create a new instance of this class, use @link NXOpen::Appearance::AppearanceManager::CreateAppearanceSchemeBuilder  NXOpen::Appearance::AppearanceManager::CreateAppearanceSchemeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AppearanceSchemeBuilder(NXOpen.Builder): 
    """ Represents a builder class that creates the new Appearance Scheme
    """


    ##  This enum is used to specify the action for appearance scheme. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## New</term><description> 
    ## </description> </item><item><term> 
    ## Copy</term><description> 
    ## </description> </item><item><term> 
    ## Rename</term><description> 
    ## </description> </item></list>
    class Action(Enum):
        """
        Members Include: <New> <Copy> <Rename>
        """
        New: int
        Copy: int
        Rename: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AppearanceSchemeBuilder.Action:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This function returns errors/warning list occurred during builder commit.
    ##         
    ##  @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def GetErrorWarningList(self) -> NXOpen.ErrorList:
        """
         This function returns errors/warning list occurred during builder commit.
                
         @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
        """
        pass
    
    ##  This function returns the newly created Appearance Scheme if the operation is successful.
    ##             Otherwise it will return null.
    ##         
    ##  @return appearanceScheme (@link Scheme NXOpen.Appearance.Scheme@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def GetNewAppearanceScheme(self) -> Scheme:
        """
         This function returns the newly created Appearance Scheme if the operation is successful.
                    Otherwise it will return null.
                
         @return appearanceScheme (@link Scheme NXOpen.Appearance.Scheme@endlink): .
        """
        pass
    
    ##  This function sets the Appearance Area on the Appearance Scheme.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="appearanceArea"> (@link Area NXOpen.Appearance.Area@endlink) </param>
    def SetAppearanceArea(self, appearanceArea: Area) -> None:
        """
         This function sets the Appearance Area on the Appearance Scheme.
                
        """
        pass
    
    ##  This function sets the Current Appearance Scheme, which is referred in Copy and Rename action.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="appearanceScheme"> (@link Scheme NXOpen.Appearance.Scheme@endlink) </param>
    def SetCurrentAppearanceScheme(self, appearanceScheme: Scheme) -> None:
        """
         This function sets the Current Appearance Scheme, which is referred in Copy and Rename action.
                
        """
        pass
    
    ##  This function sets the user action (from the enum JA_APPEARANCE_SCHEME_BUILDER_Action) to perform on the Appearance Scheme.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="actionType"> (@link AppearanceSchemeBuilder.Action NXOpen.Appearance.AppearanceSchemeBuilder.Action@endlink) </param>
    def SetSchemeActionType(self, actionType: AppearanceSchemeBuilder.Action) -> None:
        """
         This function sets the user action (from the enum JA_APPEARANCE_SCHEME_BUILDER_Action) to perform on the Appearance Scheme.
                
        """
        pass
    
    ##  This function sets new name on the Appearance Scheme.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="schemeName"> (str) </param>
    def SetSchemeName(self, schemeName: str) -> None:
        """
         This function sets new name on the Appearance Scheme.
                
        """
        pass
    
import NXOpen
##  Contains various Appearance utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AppearanceUtils(NXOpen.Object): 
    """ Contains various Appearance utility methods """


    ##  This function will set the given scheme as an active scheme in Appearance context.
    ##             Note: This function will also set the provided area as the current work appearance area.
    ##         
    ##  @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    ## <param name="areaName"> (str)  Appearance area name from which the given scheme is set active.</param>
    ## <param name="schemeName"> (str)  Scheme name which is to be set active. </param>
    def ApplyAppearanceScheme(areaName: str, schemeName: str) -> NXOpen.ErrorList:
        """
         This function will set the given scheme as an active scheme in Appearance context.
                    Note: This function will also set the provided area as the current work appearance area.
                
         @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
    ##  This function will delete the given scheme from the given area.
    ##             Note: This function will also set the first scheme as default appearance scheme.
    ##         
    ##  @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="parentAppAreaName"> (str)  Name of the Parent Appearance Area. </param>
    ## <param name="schemeName"> (str)  Name of the scheme to delete. </param>
    def DeleteAppearanceScheme(parentAppAreaName: str, schemeName: str) -> NXOpen.ErrorList:
        """
         This function will delete the given scheme from the given area.
                    Note: This function will also set the first scheme as default appearance scheme.
                
         @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
    ##  This function will get the Appearance Manager instance if already created else returns by creating one. 
    ##  @return appearanceManager (@link DataManager NXOpen.Appearance.DataManager@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetAppearanceManager() -> DataManager:
        """
         This function will get the Appearance Manager instance if already created else returns by creating one. 
         @return appearanceManager (@link DataManager NXOpen.Appearance.DataManager@endlink): .
        """
        pass
    
    ##  This function will get the parent appearance area of given designator object.
    ##  @return appearanceArea (@link Area NXOpen.Appearance.Area@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="designator"> (@link Designator NXOpen.Appearance.Designator@endlink) </param>
    def GetParentAppearanceArea(designator: Designator) -> Area:
        """
         This function will get the parent appearance area of given designator object.
         @return appearanceArea (@link Area NXOpen.Appearance.Area@endlink): .
        """
        pass
    
    ##  Constructs a new VisualMaterialUsageInstance object
    ##  @return data (@link VisualMaterialUsage NXOpen.Appearance.VisualMaterialUsage@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetVisualMaterialUsage() -> VisualMaterialUsage:
        """
         Constructs a new VisualMaterialUsageInstance object
         @return data (@link VisualMaterialUsage NXOpen.Appearance.VisualMaterialUsage@endlink): .
        """
        pass
    
    ##  This function will remove the given designator from the given area.
    ##             Note: This function will also set the provided area as a current work appearance area.
    ##         
    ##  @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="parentAppAreaName"> (str)  Name of the parent appearance area from which the designator is being removed. </param>
    ## <param name="designatorName"> (str)  Name of the designator which is to be removed. </param>
    def RemoveAppearanceDesignator(parentAppAreaName: str, designatorName: str) -> NXOpen.ErrorList:
        """
         This function will remove the given designator from the given area.
                    Note: This function will also set the provided area as a current work appearance area.
                
         @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
    ##  This function will remove input geometry entities from designator and update display.
    ##             Note: This function will also set the provided area as a current work appearance area.
    ##         
    ##  @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="parentAppAreaName"> (str)  Name of the Parent Appearance Area. </param>
    ## <param name="designatorName"> (str)  Designator name for which the associated geometries are to be removed.</param>
    ## <param name="geometricEntities"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  List of geometric entities to be removed from designator </param>
    def RemoveGeometricEntities(parentAppAreaName: str, designatorName: str, geometricEntities: List[NXOpen.TaggedObject]) -> NXOpen.ErrorList:
        """
         This function will remove input geometry entities from designator and update display.
                    Note: This function will also set the provided area as a current work appearance area.
                
         @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
    ##  This function will remove the applied visual material from the given designator.
    ##              Note: This function will also set the provided area as a current work appearance area.
    ##         
    ##  @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="parentAppAreaName"> (str)  Name of the parent appearance area of the designator from which visual material will be removed. </param>
    ## <param name="designatorName"> (str)  Name of the designator from which visual material will be removed. </param>
    def RemoveVisualMaterialOnDesignator(parentAppAreaName: str, designatorName: str) -> NXOpen.ErrorList:
        """
         This function will remove the applied visual material from the given designator.
                     Note: This function will also set the provided area as a current work appearance area.
                
         @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
    ##  This function will set the 'description' for the Designator object.
    ##             Note: This function will also set the provided area as a current work appearance area.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="parentAppAreaName"> (str)  Parent appearance area name under which this designator description change is expected.</param>
    ## <param name="designatorName"> (str)  Designator name for which the designator description change is expected.</param>
    ## <param name="newDesignatorDescription"> (str)  New designator description </param>
    def SetDesignatorDescription(parentAppAreaName: str, designatorName: str, newDesignatorDescription: str) -> None:
        """
         This function will set the 'description' for the Designator object.
                    Note: This function will also set the provided area as a current work appearance area.
                
        """
        pass
    
    ##  This function will set the 'name' for the Designator object.
    ##             Note: This function will also set the provided area as a current work appearance area.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="parentAppAreaName"> (str)  Parent appearance area name under which this designator name change is expected.</param>
    ## <param name="currentDesignatorName"> (str)  Designator name for which the designator name change is expected.</param>
    ## <param name="newDesignatorName"> (str)  New designator name </param>
    def SetDesignatorName(parentAppAreaName: str, currentDesignatorName: str, newDesignatorName: str) -> None:
        """
         This function will set the 'name' for the Designator object.
                    Note: This function will also set the provided area as a current work appearance area.
                
        """
        pass
    
    ##  This function will set the Visual Material on the given Designator for the active Scheme in the Appearance context.
    ##             Note: This function will also set the provided area as a current work appearance area.
    ##         
    ##  @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## <param name="parentAppAreaName"> (str)  Name of the parent appearance area of the designator on which we are going to change the material. </param>
    ## <param name="designatorName"> (str)  Name of the designator for which new visual material is to be set </param>
    ## <param name="visualMaterialName"> (str)  Name of the material.</param>
    ## <param name="materialSource"> (int)  Source of the material.</param>
    def SetVisualMaterialForDesignator(parentAppAreaName: str, designatorName: str, visualMaterialName: str, materialSource: int) -> NXOpen.ErrorList:
        """
         This function will set the Visual Material on the given Designator for the active Scheme in the Appearance context.
                    Note: This function will also set the provided area as a current work appearance area.
                
         @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
import NXOpen
## 
##         Represents the Appearance Area class in NX data model. This class holds the set of Appearance Designators.
## 
##         ( Appearance Schemes are assigned to an Appearance Area. Appearance Schemes have Visual Materials mapped
##         through Appearance Designators.)
##      <br> Use @link NXOpen::Appearance::DataManager::GetCurrentWorkAppearanceArea NXOpen::Appearance::DataManager::GetCurrentWorkAppearanceArea@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Area(NXOpen.NXObject): 
    """
        Represents the Appearance Area class in NX data model. This class holds the set of Appearance Designators.

        ( Appearance Schemes are assigned to an Appearance Area. Appearance Schemes have Visual Materials mapped
        through Appearance Designators.)
    """


    ##  This function will fetch the active appearance scheme in appearance context. 
    ##  @return defaultScheme (@link Scheme NXOpen.Appearance.Scheme@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetActiveAppearanceScheme(self) -> Scheme:
        """
         This function will fetch the active appearance scheme in appearance context. 
         @return defaultScheme (@link Scheme NXOpen.Appearance.Scheme@endlink): .
        """
        pass
    
    ##  Returns the array of Appearance Designators under the current Appearance Area.
    ##  @return designators (@link Designator List[NXOpen.Appearance.Designator]@endlink):  Array of Appearance Designators.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def GetAllAppearanceDesignators(self) -> List[Designator]:
        """
         Returns the array of Appearance Designators under the current Appearance Area.
         @return designators (@link Designator List[NXOpen.Appearance.Designator]@endlink):  Array of Appearance Designators.
        """
        pass
    
    ##  This function will get the designator object of the input designator name
    ##  @return designatorObj (@link Designator NXOpen.Appearance.Designator@endlink):  Designator object will be returned.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="designatorName"> (str) </param>
    def GetDesignator(self, designatorName: str) -> Designator:
        """
         This function will get the designator object of the input designator name
         @return designatorObj (@link Designator NXOpen.Appearance.Designator@endlink):  Designator object will be returned.
        """
        pass
    
    ##  This function will get the scheme object of the input scheme name.
    ##  @return defaultScheme (@link Scheme NXOpen.Appearance.Scheme@endlink):  Scheme object will be returned.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    ## 
    ## <param name="schemeName"> (str) </param>
    def GetScheme(self, schemeName: str) -> Scheme:
        """
         This function will get the scheme object of the input scheme name.
         @return defaultScheme (@link Scheme NXOpen.Appearance.Scheme@endlink):  Scheme object will be returned.
        """
        pass
    
import NXOpen
import NXOpen.PDM
## 
##         Represents the NX Appearance Manager class in the NX runtime data model. 
##         In the session, this class holds all the information like the Product Assembly
##         having the Appearance data, the loaded Appearance Areas for the assembly,
##         and operation APIs for Load, Unload, and Save of the Appearance data
##      <br> Use @link NXOpen::Appearance::AppearanceUtils::GetAppearanceManager NXOpen::Appearance::AppearanceUtils::GetAppearanceManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class DataManager(NXOpen.NXObject): 
    """
        Represents the NX Appearance Manager class in the NX runtime data model. 
        In the session, this class holds all the information like the Product Assembly
        having the Appearance data, the loaded Appearance Areas for the assembly,
        and operation APIs for Load, Unload, and Save of the Appearance data
    """


    ##  This function will get the all the loaded appearance areas. The manager holds the reference to the
    ##             loaded Appearance Product Breakdown which will be used to get the appearance areas.
    ##         
    ##  @return appearanceAreas (@link Area List[NXOpen.Appearance.Area]@endlink):  Array of loaded Appearance Areas .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def GetAllLoadedAppearanceAreas(self) -> List[Area]:
        """
         This function will get the all the loaded appearance areas. The manager holds the reference to the
                    loaded Appearance Product Breakdown which will be used to get the appearance areas.
                
         @return appearanceAreas (@link Area List[NXOpen.Appearance.Area]@endlink):  Array of loaded Appearance Areas .
        """
        pass
    
    ##  This function will get the Appearance Area object of given Appearance Area name.
    ##  @return appArea (@link Area NXOpen.Appearance.Area@endlink):  Appearance Area to be returned.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="appearanceAreaName"> (str) </param>
    def GetAppearanceArea(self, appearanceAreaName: str) -> Area:
        """
         This function will get the Appearance Area object of given Appearance Area name.
         @return appArea (@link Area NXOpen.Appearance.Area@endlink):  Appearance Area to be returned.
        """
        pass
    
    ##  This function will get the current work appearance area 
    ##  @return appearanceArea (@link Area NXOpen.Appearance.Area@endlink):  Appearance Area object which will returned.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetCurrentWorkAppearanceArea(self) -> Area:
        """
         This function will get the current work appearance area 
         @return appearanceArea (@link Area NXOpen.Appearance.Area@endlink):  Appearance Area object which will returned.
        """
        pass
    
    ##  This function will get the loaded assembly having appearance data in the context of product assembly. 
    ##  @return loadedAssembly (str): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetLoadedAssembly(self) -> str:
        """
         This function will get the loaded assembly having appearance data in the context of product assembly. 
         @return loadedAssembly (str): .
        """
        pass
    
    ##  This function will get the Product assembly having Appearance data. 
    ##  @return productAssembly (str): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetProductAssembly(self) -> str:
        """
         This function will get the Product assembly having Appearance data. 
         @return productAssembly (str): .
        """
        pass
    
    ##  This function will check for modifications in an Appearance Scheme and save them.
    ##         
    ##  @return pdmOperationErrors (@link NXOpen.PDM.OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered during Appearance Save .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def SaveAppearanceScheme(self) -> NXOpen.PDM.OperationErrors:
        """
         This function will check for modifications in an Appearance Scheme and save them.
                
         @return pdmOperationErrors (@link NXOpen.PDM.OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered during Appearance Save .
        """
        pass
    
    ##  This function will set the current work appearance area 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    ## 
    ## <param name="appearanceArea"> (@link Area NXOpen.Appearance.Area@endlink)  Appearance Area object which will set as current work appearance area.</param>
    def SetCurrentWorkAppearanceArea(self, appearanceArea: Area) -> None:
        """
         This function will set the current work appearance area 
        """
        pass
    
    ##  This function will do unload of appearance schemes for input part.
    ##             The Appearance Data specific to given part will be unloaded keeping other Appearance 
    ##             Data intact.
    ##             NOTE: Calling this function for all the Parts in the session, will not result in unload of all the Appearance Data.
    ##         
    ##  @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    ## 
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink)  Unload appearance data for input part </param>
    def UnloadAppearanceData(self, part: NXOpen.Part) -> NXOpen.ErrorList:
        """
         This function will do unload of appearance schemes for input part.
                    The Appearance Data specific to given part will be unloaded keeping other Appearance 
                    Data intact.
                    NOTE: Calling this function for all the Parts in the session, will not result in unload of all the Appearance Data.
                
         @return error_list (@link NXOpen.ErrorList NXOpen.ErrorList@endlink):  Any errors that occurred. .
        """
        pass
    
import NXOpen
## 
##         This is Appearance Designator class in NX data model. Using this object the visual
##         material is mapped to different geometric entities. This object is contained by some
##         appearance area
##      <br> Use @link NXOpen::Appearance::AppearanceDesignatorBuilder NXOpen::Appearance::AppearanceDesignatorBuilder@endlink  to create the instances of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Designator(NXOpen.NXObject): 
    """
        This is Appearance Designator class in NX data model. Using this object the visual
        material is mapped to different geometric entities. This object is contained by some
        appearance area
    """


    ## This function clears all the geometric entities associated with the input Appearance Designator 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def ClearGeometricEntites(self) -> None:
        """
        This function clears all the geometric entities associated with the input Appearance Designator 
        """
        pass
    
import NXOpen
## 
##         This is Appearance Scheme class in NX data model. This class holds information about the 
##         visual material mapping for the Designator. Each scheme is assigned to some Appearance Area
##         which holds the Designators.
##      <br> Use @link NXOpen::Appearance::AppearanceSchemeBuilder NXOpen::Appearance::AppearanceSchemeBuilder@endlink  to create the instance of this class.  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class Scheme(NXOpen.NXObject): 
    """
        This is Appearance Scheme class in NX data model. This class holds information about the 
        visual material mapping for the Designator. Each scheme is assigned to some Appearance Area
        which holds the Designators.
    """


    ##  Returns the Designator objects under the scheme.
    ##  @return designators (@link Designator List[NXOpen.Appearance.Designator]@endlink):  List of Appearance Designators in the Scheme.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    def GetAppearanceDesignators(self) -> List[Designator]:
        """
         Returns the Designator objects under the scheme.
         @return designators (@link Designator List[NXOpen.Appearance.Designator]@endlink):  List of Appearance Designators in the Scheme.
        """
        pass
    
    ##  This function gets the scheme description. 
    ##  @return schemeDescription (str): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetSchemeDescription(self) -> str:
        """
         This function gets the scheme description. 
         @return schemeDescription (str): .
        """
        pass
    
    ##  This function gets the scheme name. 
    ##  @return schemeName (str): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: studio_visualize ("STUDIO VISUALIZE")
    def GetSchemeName(self) -> str:
        """
         This function gets the scheme name. 
         @return schemeName (str): .
        """
        pass
    
    ##  This function will get visual material data for the input designator under scheme.
    ##             Note: This function allocates memory for visualMaterialData,
    ##             its callers responsiblity to release visualMaterialData memory.
    ##         
    ##  @return visualMaterialData (@link VisualMaterialUsage NXOpen.Appearance.VisualMaterialUsage@endlink):  Visual material data returned for input designator.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: appearance_mgmt (" AppearanceManagement Author for Native mode") OR appearance_mgmt_mgd (" AppearanceManagement Author for Managed mode")
    ## 
    ## <param name="designator"> (@link Designator NXOpen.Appearance.Designator@endlink)  Designator object to get visual material data</param>
    def GetVisualMaterialForDesignator(self, designator: Designator) -> VisualMaterialUsage:
        """
         This function will get visual material data for the input designator under scheme.
                    Note: This function allocates memory for visualMaterialData,
                    its callers responsiblity to release visualMaterialData memory.
                
         @return visualMaterialData (@link VisualMaterialUsage NXOpen.Appearance.VisualMaterialUsage@endlink):  Visual material data returned for input designator.
        """
        pass
    
import NXOpen
##  Represents Operation Errors to be returned in TCIN related operations 
## 
##   <br>  Created in NX1953.0.0  <br> 

class VisualMaterialUsage(NXOpen.TransientObject): 
    """ Represents Operation Errors to be returned in TCIN related operations """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
## @package NXOpen.Appearance
## Classes, Enums and Structs under NXOpen.Appearance namespace

##  @link AppearanceEditTextureAnchorTypes NXOpen.Appearance.AppearanceEditTextureAnchorTypes @endlink is an alias for @link AppearanceEditTexture.AnchorTypes NXOpen.Appearance.AppearanceEditTexture.AnchorTypes@endlink
AppearanceEditTextureAnchorTypes = AppearanceEditTexture.AnchorTypes


##  @link AppearanceEditTextureDecalProjectionsType NXOpen.Appearance.AppearanceEditTextureDecalProjectionsType @endlink is an alias for @link AppearanceEditTexture.DecalProjectionsType NXOpen.Appearance.AppearanceEditTexture.DecalProjectionsType@endlink
AppearanceEditTextureDecalProjectionsType = AppearanceEditTexture.DecalProjectionsType


##  @link AppearanceEditTextureMaterialProjectionsType NXOpen.Appearance.AppearanceEditTextureMaterialProjectionsType @endlink is an alias for @link AppearanceEditTexture.MaterialProjectionsType NXOpen.Appearance.AppearanceEditTexture.MaterialProjectionsType@endlink
AppearanceEditTextureMaterialProjectionsType = AppearanceEditTexture.MaterialProjectionsType


##  @link AppearanceEditTextureScaling NXOpen.Appearance.AppearanceEditTextureScaling @endlink is an alias for @link AppearanceEditTexture.Scaling NXOpen.Appearance.AppearanceEditTexture.Scaling@endlink
AppearanceEditTextureScaling = AppearanceEditTexture.Scaling


##  @link AppearanceSchemeBuilderAction NXOpen.Appearance.AppearanceSchemeBuilderAction @endlink is an alias for @link AppearanceSchemeBuilder.Action NXOpen.Appearance.AppearanceSchemeBuilder.Action@endlink
AppearanceSchemeBuilderAction = AppearanceSchemeBuilder.Action


