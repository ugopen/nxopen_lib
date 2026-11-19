from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AppearanceDesignatorBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Appearance.AppearanceDesignatorBuilder
        The AppearanceDesignatorBuilder used to manipulate specific appearance designator
        for appearance management.
    """
    @property
    def DesignatorDescription(self) -> str:
        """
        Getter for property: (str) DesignatorDescription
         Returns the designator description   
            
         
        """
        pass
    @DesignatorDescription.setter
    def DesignatorDescription(self, designatorDescription: str):
        """
        Setter for property: (str) DesignatorDescription
         Returns the designator description   
            
         
        """
        pass
    @property
    def DesignatorName(self) -> str:
        """
        Getter for property: (str) DesignatorName
         Returns the designator name   
            
         
        """
        pass
    @DesignatorName.setter
    def DesignatorName(self, designatorName: str):
        """
        Setter for property: (str) DesignatorName
         Returns the designator name   
            
         
        """
        pass
    @property
    def ParentAppearanceArea(self) -> str:
        """
        Getter for property: (str) ParentAppearanceArea
         Returns the appearance area   
            
         
        """
        pass
    @ParentAppearanceArea.setter
    def ParentAppearanceArea(self, parentAppearanceArea: str):
        """
        Setter for property: (str) ParentAppearanceArea
         Returns the appearance area   
            
         
        """
        pass
    @property
    def SelectionList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectionList
         Returns the selection list   
            
         
        """
        pass
    def RemoveConflictedFaceMaterial(self, conflictDesignatorTag: List[NXOpen.TaggedObject], conflictAppMat: List[NXOpen.TaggedObject], conflictEntities: List[NXOpen.TaggedObject]) -> None:
        """
         This function will remove conflicted face material
        """
        pass
import NXOpen
class AppearanceEditTexture(NXOpen.Builder): 
    """ Represents a NXOpen.Appearance.AppearanceEditTexture
        The AppearanceEditTexture used to manipulate texture space of appearance material
        for appearance designator.

    """
    class AnchorTypes(Enum):
        """
        Members Include: 
         |TopLeft| 
         |Center| 
         |BottomLeft| 
         |TopMiddle| 
         |TopRight| 
         |LeftMiddle| 
         |RightMiddle| 
         |BottomMiddle| 
         |BottomRight| 

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
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.AnchorTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DecalProjectionsType(Enum):
        """
        Members Include: 
         |Planar| 
         |Cylindrical| 
         |Spherical| 
         |Uv| 

        """
        Planar: int
        Cylindrical: int
        Spherical: int
        Uv: int
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.DecalProjectionsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialProjectionsType(Enum):
        """
        Members Include: 
         |Uv| 
         |Planar| 
         |Box| 
         |Spherical| 
         |Cylindrical| 

        """
        Uv: int
        Planar: int
        Box: int
        Spherical: int
        Cylindrical: int
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.MaterialProjectionsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Scaling(Enum):
        """
        Members Include: 
         |ToFace| 
         |ToImageSize| 
         |ToUniformScale| 
         |ToNonUniformScale| 

        """
        ToFace: int
        ToImageSize: int
        ToUniformScale: int
        ToNonUniformScale: int
        @staticmethod
        def ValueOf(value: int) -> AppearanceEditTexture.Scaling:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorType(self) -> AppearanceEditTexture.AnchorTypes:
        """
        Getter for property: ( AppearanceEditTexture.AnchorTypes NXOpen.A) AnchorType
         Returns the anchor type   
            
         
        """
        pass
    @AnchorType.setter
    def AnchorType(self, anchorType: AppearanceEditTexture.AnchorTypes):
        """
        Setter for property: ( AppearanceEditTexture.AnchorTypes NXOpen.A) AnchorType
         Returns the anchor type   
            
         
        """
        pass
    @property
    def AspectRatio(self) -> float:
        """
        Getter for property: (float) AspectRatio
         Returns the decal aspect ratio   
            
         
        """
        pass
    @AspectRatio.setter
    def AspectRatio(self, aspect_ratio: float):
        """
        Setter for property: (float) AspectRatio
         Returns the decal aspect ratio   
            
         
        """
        pass
    @property
    def MappingProjection(self) -> int:
        """
        Getter for property: (int) MappingProjection
         Returns the mapping projection   
            
         
        """
        pass
    @MappingProjection.setter
    def MappingProjection(self, mappingProjection: int):
        """
        Setter for property: (int) MappingProjection
         Returns the mapping projection   
            
         
        """
        pass
    @property
    def Scale(self) -> float:
        """
        Getter for property: (float) Scale
         Returns the decal scale  
            
         
        """
        pass
    @Scale.setter
    def Scale(self, scale: float):
        """
        Setter for property: (float) Scale
         Returns the decal scale  
            
         
        """
        pass
    @property
    def StudioMaterialName(self) -> str:
        """
        Getter for property: (str) StudioMaterialName
         Returns the studio material name   
            
         
        """
        pass
    @StudioMaterialName.setter
    def StudioMaterialName(self, studioMaterialName: str):
        """
        Setter for property: (str) StudioMaterialName
         Returns the studio material name   
            
         
        """
        pass
    @property
    def TextureNormalVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) TextureNormalVector
         Returns the texture normal vector   
            
         
        """
        pass
    @TextureNormalVector.setter
    def TextureNormalVector(self, textureNormalVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) TextureNormalVector
         Returns the texture normal vector   
            
         
        """
        pass
    @property
    def TextureOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TextureOrigin
         Returns the texture origin   
            
         
        """
        pass
    @TextureOrigin.setter
    def TextureOrigin(self, textureOrigin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TextureOrigin
         Returns the texture origin   
            
         
        """
        pass
    @property
    def TextureUpVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) TextureUpVector
         Returns the texture up vector   
            
         
        """
        pass
    @TextureUpVector.setter
    def TextureUpVector(self, textureUpVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) TextureUpVector
         Returns the texture up vector   
            
         
        """
        pass
import NXOpen
class AppearanceManager(NXOpen.Object): 
    """ Represents an object that manages Appearance application specific objects. """
    def CreateAppearanceDesignatorBuilder(self, schemeName: str) -> AppearanceDesignatorBuilder:
        """
         Creates a NXOpen.Appearance.AppearanceDesignatorBuilder object 
         Returns builder ( AppearanceDesignatorBuilder NXOpen.A): .
        """
        pass
    def CreateAppearanceEditTextureBuilder(self, designatorName: str, schemeName: str) -> AppearanceEditTexture:
        """
         Creates a NXOpen.Appearance.AppearanceEditTexture object 
         Returns builder ( AppearanceEditTexture NXOpen.A): .
        """
        pass
    def CreateAppearanceSchemeBuilder(self) -> AppearanceSchemeBuilder:
        """
         Creates a NXOpen.Appearance.AppearanceSchemeBuilder 
         Returns builder ( AppearanceSchemeBuilder NXOpen.A): .
        """
        pass
    def SetProductAssembly(self, productAssembly: str) -> NXOpen.ErrorList:
        """
         This function will set the input product assembly which has the appearance data
         Returns errorList ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
    def UnloadAllAppearanceData(self) -> NXOpen.ErrorList:
        """
         This function will do full unload of appearance schemes present in session 
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
import NXOpen
class AppearanceSchemeBuilder(NXOpen.Builder): 
    """ Represents a builder class that creates the new Appearance Scheme
    """
    class Action(Enum):
        """
        Members Include: 
         |New| 
         |Copy| 
         |Rename| 

        """
        New: int
        Copy: int
        Rename: int
        @staticmethod
        def ValueOf(value: int) -> AppearanceSchemeBuilder.Action:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetErrorWarningList(self) -> NXOpen.ErrorList:
        """
         This function returns errorswarning list occurred during builder commit.
                
         Returns errorList ( NXOpen.ErrorList): .
        """
        pass
    def GetNewAppearanceScheme(self) -> Scheme:
        """
         This function returns the newly created Appearance Scheme if the operation is successful.
                    Otherwise it will return null.
                
         Returns appearanceScheme ( Scheme NXOpen.A): .
        """
        pass
    def SetAppearanceArea(self, appearanceArea: Area) -> None:
        """
         This function sets the Appearance Area on the Appearance Scheme.
                
        """
        pass
    def SetCurrentAppearanceScheme(self, appearanceScheme: Scheme) -> None:
        """
         This function sets the Current Appearance Scheme, which is referred in Copy and Rename action.
                
        """
        pass
    def SetSchemeActionType(self, actionType: AppearanceSchemeBuilder.Action) -> None:
        """
         This function sets the user action (from the enum JA_APPEARANCE_SCHEME_BUILDER_Action) to perform on the Appearance Scheme.
                
        """
        pass
    def SetSchemeName(self, schemeName: str) -> None:
        """
         This function sets new name on the Appearance Scheme.
                
        """
        pass
import NXOpen
class AppearanceUtils(NXOpen.Object): 
    """ Contains various Appearance utility methods """
    def ApplyAppearanceScheme(areaName: str, schemeName: str) -> NXOpen.ErrorList:
        """
         This function will set the given scheme as an active scheme in Appearance context.
                    Note: This function will also set the provided area as the current work appearance area.
                
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
    def DeleteAppearanceScheme(parentAppAreaName: str, schemeName: str) -> NXOpen.ErrorList:
        """
         This function will delete the given scheme from the given area.
                    Note: This function will also set the first scheme as default appearance scheme.
                
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
    def GetAppearanceManager() -> DataManager:
        """
         This function will get the Appearance Manager instance if already created else returns by creating one. 
         Returns appearanceManager ( DataManager NXOpen.A): .
        """
        pass
    def GetParentAppearanceArea(designator: Designator) -> Area:
        """
         This function will get the parent appearance area of given designator object.
         Returns appearanceArea ( Area NXOpen.A): .
        """
        pass
    def GetVisualMaterialUsage() -> VisualMaterialUsage:
        """
         Constructs a new VisualMaterialUsageInstance object
         Returns data ( VisualMaterialUsage NXOpen.A): .
        """
        pass
    def RemoveAppearanceDesignator(parentAppAreaName: str, designatorName: str) -> NXOpen.ErrorList:
        """
         This function will remove the given designator from the given area.
                    Note: This function will also set the provided area as a current work appearance area.
                
         Returns errorList ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
    def RemoveGeometricEntities(parentAppAreaName: str, designatorName: str, geometricEntities: List[NXOpen.TaggedObject]) -> NXOpen.ErrorList:
        """
         This function will remove input geometry entities from designator and update display.
                    Note: This function will also set the provided area as a current work appearance area.
                
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
    def RemoveVisualMaterialOnDesignator(parentAppAreaName: str, designatorName: str) -> NXOpen.ErrorList:
        """
         This function will remove the applied visual material from the given designator.
                     Note: This function will also set the provided area as a current work appearance area.
                
         Returns errorList ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
    def SetDesignatorDescription(parentAppAreaName: str, designatorName: str, newDesignatorDescription: str) -> None:
        """
         This function will set the 'description' for the Designator object.
                    Note: This function will also set the provided area as a current work appearance area.
                
        """
        pass
    def SetDesignatorName(parentAppAreaName: str, currentDesignatorName: str, newDesignatorName: str) -> None:
        """
         This function will set the 'name' for the Designator object.
                    Note: This function will also set the provided area as a current work appearance area.
                
        """
        pass
    def SetVisualMaterialForDesignator(parentAppAreaName: str, designatorName: str, visualMaterialName: str, materialSource: int) -> NXOpen.ErrorList:
        """
         This function will set the Visual Material on the given Designator for the active Scheme in the Appearance context.
                    Note: This function will also set the provided area as a current work appearance area.
                
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
import NXOpen
class Area(NXOpen.NXObject): 
    """
        Represents the Appearance Area class in NX data model. This class holds the set of Appearance Designators.

        ( Appearance Schemes are assigned to an Appearance Area. Appearance Schemes have Visual Materials mapped
        through Appearance Designators.)
    """
    def GetActiveAppearanceScheme(self) -> Scheme:
        """
         This function will fetch the active appearance scheme in appearance context. 
         Returns defaultScheme ( Scheme NXOpen.A): .
        """
        pass
    def GetAllAppearanceDesignators(self) -> List[Designator]:
        """
         Returns the array of Appearance Designators under the current Appearance Area.
         Returns designators ( Designator List[NXOpen):  Array of Appearance Designators.
        """
        pass
    def GetDesignator(self, designatorName: str) -> Designator:
        """
         This function will get the designator object of the input designator name
         Returns designatorObj ( Designator NXOpen.A):  Designator object will be returned.
        """
        pass
    def GetScheme(self, schemeName: str) -> Scheme:
        """
         This function will get the scheme object of the input scheme name.
         Returns defaultScheme ( Scheme NXOpen.A):  Scheme object will be returned.
        """
        pass
import NXOpen
import NXOpen.PDM
class DataManager(NXOpen.NXObject): 
    """
        Represents the NX Appearance Manager class in the NX runtime data model. 
        In the session, this class holds all the information like the Product Assembly
        having the Appearance data, the loaded Appearance Areas for the assembly,
        and operation APIs for Load, Unload, and Save of the Appearance data
    """
    def GetAllLoadedAppearanceAreas(self) -> List[Area]:
        """
         This function will get the all the loaded appearance areas. The manager holds the reference to the
                    loaded Appearance Product Breakdown which will be used to get the appearance areas.
                
         Returns appearanceAreas ( Area List[NXOpen):  Array of loaded Appearance Areas .
        """
        pass
    def GetAppearanceArea(self, appearanceAreaName: str) -> Area:
        """
         This function will get the Appearance Area object of given Appearance Area name.
         Returns appArea ( Area NXOpen.A):  Appearance Area to be returned.
        """
        pass
    def GetCurrentWorkAppearanceArea(self) -> Area:
        """
         This function will get the current work appearance area 
         Returns appearanceArea ( Area NXOpen.A):  Appearance Area object which will returned.
        """
        pass
    def GetLoadedAssembly(self) -> str:
        """
         This function will get the loaded assembly having appearance data in the context of product assembly. 
         Returns loadedAssembly (str): .
        """
        pass
    def GetProductAssembly(self) -> str:
        """
         This function will get the Product assembly having Appearance data. 
         Returns productAssembly (str): .
        """
        pass
    def SaveAppearanceScheme(self) -> NXOpen.PDM.OperationErrors:
        """
         This function will check for modifications in an Appearance Scheme and save them.
                
         Returns pdmOperationErrors ( NXOpen.PDM.OperationErrors):  Errors encountered during Appearance Save .
        """
        pass
    def SetCurrentWorkAppearanceArea(self, appearanceArea: Area) -> None:
        """
         This function will set the current work appearance area 
        """
        pass
    def UnloadAppearanceData(self, part: NXOpen.Part) -> NXOpen.ErrorList:
        """
         This function will do unload of appearance schemes for input part.
                    The Appearance Data specific to given part will be unloaded keeping other Appearance 
                    Data intact.
                    NOTE: Calling this function for all the Parts in the session, will not result in unload of all the Appearance Data.
                
         Returns error_list ( NXOpen.ErrorList):  Any errors that occurred. .
        """
        pass
import NXOpen
class Designator(NXOpen.NXObject): 
    """
        This is Appearance Designator class in NX data model. Using this object the visual
        material is mapped to different geometric entities. This object is contained by some
        appearance area
    """
    def ClearGeometricEntites(self) -> None:
        """
        This function clears all the geometric entities associated with the input Appearance Designator 
        """
        pass
import NXOpen
class Scheme(NXOpen.NXObject): 
    """
        This is Appearance Scheme class in NX data model. This class holds information about the 
        visual material mapping for the Designator. Each scheme is assigned to some Appearance Area
        which holds the Designators.
    """
    def GetAppearanceDesignators(self) -> List[Designator]:
        """
         Returns the Designator objects under the scheme.
         Returns designators ( Designator List[NXOpen):  List of Appearance Designators in the Scheme.
        """
        pass
    def GetSchemeDescription(self) -> str:
        """
         This function gets the scheme description. 
         Returns schemeDescription (str): .
        """
        pass
    def GetSchemeName(self) -> str:
        """
         This function gets the scheme name. 
         Returns schemeName (str): .
        """
        pass
    def GetVisualMaterialForDesignator(self, designator: Designator) -> VisualMaterialUsage:
        """
         This function will get visual material data for the input designator under scheme.
                    Note: This function allocates memory for visualMaterialData,
                    its callers responsiblity to release visualMaterialData memory.
                
         Returns visualMaterialData ( VisualMaterialUsage NXOpen.A):  Visual material data returned for input designator.
        """
        pass
import NXOpen
class VisualMaterialUsage(NXOpen.TransientObject): 
    """ Represents Operation Errors to be returned in TCIN related operations """
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
