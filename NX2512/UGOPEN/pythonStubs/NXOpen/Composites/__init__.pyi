from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ActivationManager(NXOpen.Object): 
    """ Represents an object to manage Composites objects active states """
    def ActivateObjects(objectTags: List[ICanBeDeactivated]) -> None:
        """
         Activate the indicated objects 
        """
        pass
    def DeactivateObjects(objectTags: List[ICanBeDeactivated]) -> None:
        """
         Deactivate the indicated objects 
        """
        pass
import NXOpen
import NXOpen.Features
class AddPlyPieceBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.PlyPiece object.
    """
    @property
    def BoundaryRegion(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) BoundaryRegion
         Returns the selected  Composites::Features::Region , defining the extents of the  Composites::PlyPiece   
            
         
        """
        pass
    @BoundaryRegion.setter
    def BoundaryRegion(self, region: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) BoundaryRegion
         Returns the selected  Composites::Features::Region , defining the extents of the  Composites::PlyPiece   
            
         
        """
        pass
    @property
    def Ply(self) -> SelectPly:
        """
        Getter for property: ( SelectPly NXOpen.C) Ply
         Returns the  Composites::Ply  to be spliced.  
             
         
        """
        pass
import NXOpen.Annotations
class AutoCrossSectionPMIBuilder(NXOpen.Annotations.DraftingNoteBuilder): 
    """ Creates or edits Composites NXOpen.Composites.AutoCrossSectionPMI objects """
    @property
    def AssociatedObjects(self) -> NXOpen.Annotations.AssociatedObjectsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.AssociatedObjectsBuilder) AssociatedObjects
         Returns the  NXOpen::Annotations::AssociatedObjectsBuilder  for the annotation   
            
         
        """
        pass
import NXOpen.Annotations
class AutoCrossSectionPMI(NXOpen.Annotations.Label): 
    """ A label referencing an item within a NXOpen.Composites.CrossSection object"""
    pass
class AutomatedPlyPiece(Base): 
    """ Represents a single piecelayer of material to be deposited during manufacturing, defined using a splicing process """
    pass
import NXOpen
class BaseObjectValidator(NXOpen.TaggedObject): 
    """ validator for a base composites data object. """
    pass
import NXOpen
class Base(NXOpen.DisplayableObject): 
    """ Represents a base object, which other composite objects inherit functionality from """
    def SetName(self, desiredName: str) -> None:
        """
         Overrides the default function for setting an object's name, respecting the case of the provided name 
        """
        pass
import NXOpen
class CompositePart(Base): 
    """ Represents a full-definition of a composite part, consisting of one or more Composites.Laminate"""
    class ResequenceInsertOption(Enum):
        """
        Members Include: 
         |Before| 
         |After| 

        """
        Before: int
        After: int
        @staticmethod
        def ValueOf(value: int) -> CompositePart.ResequenceInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CenterOfMass
         Returns the center of mass of the  Composites::CompositePart .  
             
         
        """
        pass
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the  Composites::CompositePart .  
             
         
        """
        pass
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) MomentOfInertia
         Returns the moment of inertia of the  Composites::CompositePart .  
             
         
        """
        pass
    def GetOrderedCores(self) -> List[CrossSection]:
        """
         The ordered list of cores of the Composites.CompositePart. 
         Returns orderedCores ( CrossSection List[NXOpen): .
        """
        pass
    def GetOrderedLaminates(self) -> List[Laminate]:
        """
         The ordered list of laminates of the Composites.CompositePart. 
         Returns orderedLaminates ( Laminate List[NXOpen): .
        """
        pass
    def GetOrderedLaminatesAndCores(self) -> List[Base]:
        """
         The ordered list of laminates and cores of the Composites.CompositePart. 
         Returns orderedLaminatesAndCores ( Base List[NXOpen): .
        """
        pass
    def ResequenceChildren(self, children_to_resequence: List[Base], target_child: Base, insert_option: CompositePart.ResequenceInsertOption) -> None:
        """
         Resequences the given children before or after the provided target child. 
        """
        pass
import NXOpen
class CompositesCollectionValidator(NXOpen.TaggedObject): 
    """ validator for the base composites data model in a part. """
    class EdgeOptionValue(Enum):
        """
        Members Include: 
         |EdgesFromFrontOfList| 
         |EdgesFromEndOfList| 
         |OutputAllEdges| 

        """
        EdgesFromFrontOfList: int
        EdgesFromEndOfList: int
        OutputAllEdges: int
        @staticmethod
        def ValueOf(value: int) -> CompositesCollectionValidator.EdgeOptionValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NodeOptionValue(Enum):
        """
        Members Include: 
         |NodesFromFrontOfList| 
         |NodesFromEndOfList| 
         |OutputAllNodes| 

        """
        NodesFromFrontOfList: int
        NodesFromEndOfList: int
        OutputAllNodes: int
        @staticmethod
        def ValueOf(value: int) -> CompositesCollectionValidator.NodeOptionValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OutputCompositeParts(self) -> bool:
        """
        Getter for property: (bool) OutputCompositeParts
         Returns the flag controlling whether composite parts are included in the composites collection validation  
            
         
        """
        pass
    @OutputCompositeParts.setter
    def OutputCompositeParts(self, outputCompositeParts: bool):
        """
        Setter for property: (bool) OutputCompositeParts
         Returns the flag controlling whether composite parts are included in the composites collection validation  
            
         
        """
        pass
    @property
    def OutputDetailedObjectStatus(self) -> bool:
        """
        Getter for property: (bool) OutputDetailedObjectStatus
         Returns the flag controlling whether detailed object status is included in the composites collection validation  
            
         
        """
        pass
    @OutputDetailedObjectStatus.setter
    def OutputDetailedObjectStatus(self, outputDetailedObjectStatus: bool):
        """
        Setter for property: (bool) OutputDetailedObjectStatus
         Returns the flag controlling whether detailed object status is included in the composites collection validation  
            
         
        """
        pass
    @property
    def OutputMassProperties(self) -> bool:
        """
        Getter for property: (bool) OutputMassProperties
         Returns the flag controlling whether to export the Mass Properties  
            
         
        """
        pass
    @OutputMassProperties.setter
    def OutputMassProperties(self, outputMassProperties: bool):
        """
        Setter for property: (bool) OutputMassProperties
         Returns the flag controlling whether to export the Mass Properties  
            
         
        """
        pass
    @property
    def OutputRosettes(self) -> bool:
        """
        Getter for property: (bool) OutputRosettes
         Returns the flag controlling whether rosettes are included in the composites collection validation  
            
         
        """
        pass
    @OutputRosettes.setter
    def OutputRosettes(self, outputRosettes: bool):
        """
        Setter for property: (bool) OutputRosettes
         Returns the flag controlling whether rosettes are included in the composites collection validation  
            
         
        """
        pass
import NXOpen.Annotations
class CompositeSectionPMISettingsBuilder(NXOpen.Annotations.BaseApplicationStyleBuilder): 
    """
    Controls and edits a Composite Section PMI label's settings.
    """
    @property
    def CompositeSectionNamePrefix(self) -> str:
        """
        Getter for property: (str) CompositeSectionNamePrefix
         Returns the prefix added to the composite section name displayed in the created PMI label   
            
         
        """
        pass
    @CompositeSectionNamePrefix.setter
    def CompositeSectionNamePrefix(self, prefix: str):
        """
        Setter for property: (str) CompositeSectionNamePrefix
         Returns the prefix added to the composite section name displayed in the created PMI label   
            
         
        """
        pass
    @property
    def CompositeSectionNameSuffix(self) -> str:
        """
        Getter for property: (str) CompositeSectionNameSuffix
         Returns the suffix added to the composite section name displayed in the created PMI label   
            
         
        """
        pass
    @CompositeSectionNameSuffix.setter
    def CompositeSectionNameSuffix(self, prefix: str):
        """
        Setter for property: (str) CompositeSectionNameSuffix
         Returns the suffix added to the composite section name displayed in the created PMI label   
            
         
        """
        pass
import NXOpen
class CoreBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.Core object.
    """
    @property
    def Solid(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) Solid
         Returns the solid defining the shape of the  Composites::Core   
            
         
        """
        pass
    @Solid.setter
    def Solid(self, solid: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) Solid
         Returns the solid defining the shape of the  Composites::Core   
            
         
        """
        pass
import NXOpen
class Core(Base): 
    """ Represents a solid piece of material to be placed within a composite part """
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CenterOfMass
         Returns the center of mass of the  Composites::Core .  
             
         
        """
        pass
    @property
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the density of the  Composites::Core .  
             
         
        """
        pass
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the  Composites::Core .  
             
         
        """
        pass
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) MomentOfInertia
         Returns the moment of inertia of the  Composites::Core .  
             
         
        """
        pass
    @property
    def Sequence(self) -> float:
        """
        Getter for property: (float) Sequence
         Returns the stacking sequence number of the  Composites::Core .  
             
         
        """
        pass
    @property
    def Volume(self) -> float:
        """
        Getter for property: (float) Volume
         Returns the volume of the  Composites::Core .  
             
         
        """
        pass
import NXOpen
class CrossSectionBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.CrossSection object.
    """
    @property
    def EndLimit(self) -> float:
        """
        Getter for property: (float) EndLimit
         Returns the end limit of the  Composites::CrossSection .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
    @EndLimit.setter
    def EndLimit(self, endLimit: float):
        """
        Setter for property: (float) EndLimit
         Returns the end limit of the  Composites::CrossSection .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
    @property
    def PlaneSelect(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) PlaneSelect
         Returns the plane to intersect composite objects of the  Composites::CrossSection .  
           Results will be drawn in this  Plane .  
         
        """
        pass
    @PlaneSelect.setter
    def PlaneSelect(self, planeSelect: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) PlaneSelect
         Returns the plane to intersect composite objects of the  Composites::CrossSection .  
           Results will be drawn in this  Plane .  
         
        """
        pass
    @property
    def PlyScale(self) -> float:
        """
        Getter for property: (float) PlyScale
         Returns the scale for ply height in the  Composites::CrossSection .  
           Each ply thickness will be multiplied by this value.  
         
        """
        pass
    @PlyScale.setter
    def PlyScale(self, plyScale: float):
        """
        Setter for property: (float) PlyScale
         Returns the scale for ply height in the  Composites::CrossSection .  
           Each ply thickness will be multiplied by this value.  
         
        """
        pass
    @property
    def StartLimit(self) -> float:
        """
        Getter for property: (float) StartLimit
         Returns the start limit of the  Composites::CrossSection .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
    @StartLimit.setter
    def StartLimit(self, startLimit: float):
        """
        Setter for property: (float) StartLimit
         Returns the start limit of the  Composites::CrossSection .  
           Cross section will be trimmed by this limit.  
         
        """
        pass
import NXOpen.Annotations
class CrossSectionPMIBuilder(NXOpen.Annotations.DraftingNoteBuilder): 
    """ Creates or edits Composites NXOpen.Composites.CrossSectionPMI objects """
    @property
    def AssociatedObjects(self) -> NXOpen.Annotations.AssociatedObjectsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.AssociatedObjectsBuilder) AssociatedObjects
         Returns the  NXOpen::Annotations::AssociatedObjectsBuilder  for the annotation   
            
         
        """
        pass
import NXOpen.Annotations
class CrossSectionPMI(NXOpen.Annotations.Label): 
    """ A label referencing an item within a NXOpen.Composites.CrossSection object"""
    pass
class CrossSection(Base): 
    """ Represents a composites planar composite cross section to visualize composite part geometry"""
    pass
import NXOpen
class CustomStaggerProfile(NXOpen.NXObject): 
    """ A stagger profile with an array of user-defined indices """
    pass
import NXOpen
class DartBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.Dart object.
    """
    @property
    def Ply(self) -> SelectIPly:
        """
        Getter for property: ( SelectIPly NXOpen.C) Ply
         Returns the  Composites::IPly  to be darted.  
             
         
        """
        pass
    @property
    def Section(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) Section
         Returns the section defining the single, open curve to cut into 
                the  Composites::Ply 's surface   
            
         
        """
        pass
class Dart(Base): 
    """ Represents an open curve to cut into a Composites.Ply boundary to alleviate material deformation in the Composites.Ply's producibility results """
    pass
import NXOpen
class DesignStationBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.DesignStation object.
    """
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the  Point  specifying where the  Composites::DesignStation  is calculated   
            
         
        """
        pass
    @Point.setter
    def Point(self, pointTag: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the  Point  specifying where the  Composites::DesignStation  is calculated   
            
         
        """
        pass
import NXOpen.Annotations
class DesignStationPMIBuilder(NXOpen.Annotations.DraftingNoteBuilder): 
    """ Creates or edits Composites NXOpen.Composites.DesignStationPMI objects """
    @property
    def AssociatedObjects(self) -> NXOpen.Annotations.AssociatedObjectsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.AssociatedObjectsBuilder) AssociatedObjects
         Returns the  NXOpen::Annotations::AssociatedObjectsBuilder  for the annotation   
            
         
        """
        pass
import NXOpen.Annotations
class DesignStationPMISettingsBuilder(NXOpen.Annotations.BaseApplicationStyleBuilder): 
    """
    Controls and edits a Design Station PMI label's settings.
    """
    @property
    def DesignStationComponentCountPrefix(self) -> str:
        """
        Getter for property: (str) DesignStationComponentCountPrefix
         Returns the prefix added to the design station component count displayed in the created PMI label   
            
         
        """
        pass
    @DesignStationComponentCountPrefix.setter
    def DesignStationComponentCountPrefix(self, prefix: str):
        """
        Setter for property: (str) DesignStationComponentCountPrefix
         Returns the prefix added to the design station component count displayed in the created PMI label   
            
         
        """
        pass
    @property
    def DesignStationComponentCountSuffix(self) -> str:
        """
        Getter for property: (str) DesignStationComponentCountSuffix
         Returns the suffix added to the design station component count displayed in the created PMI label   
            
         
        """
        pass
    @DesignStationComponentCountSuffix.setter
    def DesignStationComponentCountSuffix(self, prefix: str):
        """
        Setter for property: (str) DesignStationComponentCountSuffix
         Returns the suffix added to the design station component count displayed in the created PMI label   
            
         
        """
        pass
    @property
    def DesignStationNamePrefix(self) -> str:
        """
        Getter for property: (str) DesignStationNamePrefix
         Returns the prefix added to the design station name displayed in the created PMI label   
            
         
        """
        pass
    @DesignStationNamePrefix.setter
    def DesignStationNamePrefix(self, prefix: str):
        """
        Setter for property: (str) DesignStationNamePrefix
         Returns the prefix added to the design station name displayed in the created PMI label   
            
         
        """
        pass
    @property
    def DesignStationNameSuffix(self) -> str:
        """
        Getter for property: (str) DesignStationNameSuffix
         Returns the suffix added to the design station name displayed in the created PMI label   
            
         
        """
        pass
    @DesignStationNameSuffix.setter
    def DesignStationNameSuffix(self, prefix: str):
        """
        Setter for property: (str) DesignStationNameSuffix
         Returns the suffix added to the design station name displayed in the created PMI label   
            
         
        """
        pass
    @property
    def DesignStationTotalThicknessPrefix(self) -> str:
        """
        Getter for property: (str) DesignStationTotalThicknessPrefix
         Returns the prefix added to the design station total thickness displayed in the created PMI label   
            
         
        """
        pass
    @DesignStationTotalThicknessPrefix.setter
    def DesignStationTotalThicknessPrefix(self, prefix: str):
        """
        Setter for property: (str) DesignStationTotalThicknessPrefix
         Returns the prefix added to the design station total thickness displayed in the created PMI label   
            
         
        """
        pass
    @property
    def DesignStationTotalThicknessSuffix(self) -> str:
        """
        Getter for property: (str) DesignStationTotalThicknessSuffix
         Returns the suffix added to the design station total thickness displayed in the created PMI label   
            
         
        """
        pass
    @DesignStationTotalThicknessSuffix.setter
    def DesignStationTotalThicknessSuffix(self, prefix: str):
        """
        Setter for property: (str) DesignStationTotalThicknessSuffix
         Returns the suffix added to the design station total thickness displayed in the created PMI label   
            
         
        """
        pass
    @property
    def IncludeDesignStationComponentCount(self) -> bool:
        """
        Getter for property: (bool) IncludeDesignStationComponentCount
         Returns the flag controlling whether to include the design station component count in the created PMI label   
            
         
        """
        pass
    @IncludeDesignStationComponentCount.setter
    def IncludeDesignStationComponentCount(self, include: bool):
        """
        Setter for property: (bool) IncludeDesignStationComponentCount
         Returns the flag controlling whether to include the design station component count in the created PMI label   
            
         
        """
        pass
    @property
    def IncludeDesignStationName(self) -> bool:
        """
        Getter for property: (bool) IncludeDesignStationName
         Returns the flag controlling whether to include the design station name in the created PMI label   
            
         
        """
        pass
    @IncludeDesignStationName.setter
    def IncludeDesignStationName(self, include: bool):
        """
        Setter for property: (bool) IncludeDesignStationName
         Returns the flag controlling whether to include the design station name in the created PMI label   
            
         
        """
        pass
    @property
    def IncludeDesignStationTotalThickness(self) -> bool:
        """
        Getter for property: (bool) IncludeDesignStationTotalThickness
         Returns the flag controlling whether to include the design station total thickness in the created PMI label   
            
         
        """
        pass
    @IncludeDesignStationTotalThickness.setter
    def IncludeDesignStationTotalThickness(self, include: bool):
        """
        Setter for property: (bool) IncludeDesignStationTotalThickness
         Returns the flag controlling whether to include the design station total thickness in the created PMI label   
            
         
        """
        pass
import NXOpen.Annotations
class DesignStationPMI(NXOpen.Annotations.Label): 
    """ A label referencing a NXOpen.Composites.DesignStation object"""
    pass
class DesignStation(Base): 
    """ Represents a definition of a Design Station to perform a virtual core sample on a composite part. """
    pass
class FlatPattern(Base): 
    """ Represents a flat area of material to be draped onto a Composites.Features.LayupSurface to create a Composites.Ply """
    pass
import NXOpen.Annotations
class GeneralPMISettingsBuilder(NXOpen.Annotations.BaseApplicationStyleBuilder): 
    """
    Controls and edits a Composites PMI label's settings.
    """
    @property
    def NumberOfDecimalPlaces(self) -> int:
        """
        Getter for property: (int) NumberOfDecimalPlaces
         Returns the number of decimals to include in the created PMI label   
            
         
        """
        pass
    @NumberOfDecimalPlaces.setter
    def NumberOfDecimalPlaces(self, numberOfDecimalPlaces: int):
        """
        Setter for property: (int) NumberOfDecimalPlaces
         Returns the number of decimals to include in the created PMI label   
            
         
        """
        pass
import NXOpen
class HDF5ExportBuilder(NXOpen.Builder): 
    """
    Creates HDF5 Export Builder Object.
    """
    @property
    def ExportFileName(self) -> str:
        """
        Getter for property: (str) ExportFileName
         Returns the name of the export file   
            
         
        """
        pass
    @ExportFileName.setter
    def ExportFileName(self, exportFileName: str):
        """
        Setter for property: (str) ExportFileName
         Returns the name of the export file   
            
         
        """
        pass
    @property
    def PlySelection(self) -> SelectIPlyList:
        """
        Getter for property: ( SelectIPlyList NXOpen.C) PlySelection
         Returns the list of  Composites::IPly  to export   
            
         
        """
        pass
    def SetFiberOrientationToUseProducibilityResult(self) -> None:
        """
         Sets the HDF5 export to use fiber orientations from the ply producibility results 
        """
        pass
    def SetFiberOrientationToUseRosetteMapping(self) -> None:
        """
         Sets the HDF5 export to use fiber orientations from the mapped rosette directions 
        """
        pass
import NXOpen
class Hdf5ExportValidator(NXOpen.TaggedObject): 
    """ validator for an HDF5 Export File from NX Composites. """
    pass
import NXOpen
class ICanBeDeactivated(NXOpen.INXObject): 
    """ Interface for Composites objects that can be used with the Composites.ActivationManager """
    pass
import NXOpen
class ICanBeUpdated(NXOpen.INXObject): 
    """ Interface for Composites objects that can be used with the Composites.UpdateManager """
    pass
import NXOpen
class IObjectCanSetSequence(NXOpen.INXObject): 
    """ Interface for Composites objects that can be used with the Composites.SequenceSetter """
    pass
class IPlyPiece(IPly): 
    """ Interface for Composites objects that are the result of splicing operations"""
    pass
import NXOpen
class IPly(NXOpen.INXObject): 
    """ Interface for Composites objects that can be used with the Composites.Ply and Composites.PlyPiece objects"""
    @property
    @abstractmethod
    def Area(self) -> float:
        """
        Getter for property: (float) Area
         Returns the area of the  Composites::IPly .  
             
         
        """
        pass
    @property
    @abstractmethod
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CenterOfMass
         Returns the center of mass of the  Composites::IPly .  
             
         
        """
        pass
    @property
    @abstractmethod
    def CuredThickness(self) -> float:
        """
        Getter for property: (float) CuredThickness
         Returns the cured thickness of the  Composites::IPly .  
             
         
        """
        pass
    @property
    @abstractmethod
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the density of the  Composites::IPly .  
             
         
        """
        pass
    @property
    @abstractmethod
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the  Composites::IPly .  
             
         
        """
        pass
    @property
    @abstractmethod
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) MomentOfInertia
         Returns the moment of inertia of the  Composites::IPly .  
             
         
        """
        pass
    @property
    @abstractmethod
    def Perimeter(self) -> float:
        """
        Getter for property: (float) Perimeter
         Returns the perimeter of the  Composites::IPly .  
             
         
        """
        pass
    @property
    @abstractmethod
    def Sequence(self) -> float:
        """
        Getter for property: (float) Sequence
         Returns the stacking sequence number of  Composites::IPly .  
             
         
        """
        pass
    @abstractmethod
    def GetOrderedPlyPieces(self) -> List[IPlyPiece]:
        """
         The ordered list of Composites.IPlyPiece objects that this
                Composites.IPly is broken up into 
         Returns orderedPlyPieces ( IPlyPiece List[NXOpen): .
        """
        pass
    @abstractmethod
    def HideRosetteMappedOrientationDisplay(self) -> None:
        """
         Hide the ply's rosette-mapped orientation display 
        """
        pass
    @abstractmethod
    def PerformResequenceOfIPlyPieces(self, pieces_to_resequence: List[IPlyPiece], target_ply_piece: IPlyPiece, insert_option: PlyResequenceOption) -> None:
        """
         Resequences the given Composites.IPlyPiece objects before or after the provided target Composites.IPlyPiece. 
        """
        pass
    @abstractmethod
    def ShowRosetteMappedOrientationDisplay(self) -> None:
        """
         Show the ply's rosette-mapped orientation display 
        """
        pass
import NXOpen
import NXOpen.Features
class LaminateBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.Laminate object.
    """
    @property
    def LayupSurface(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) LayupSurface
         Returns the  Composites::Features::LayupSurface  forming the surface upon which this laminate is defined    
            
         
        """
        pass
    @LayupSurface.setter
    def LayupSurface(self, frec: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) LayupSurface
         Returns the  Composites::Features::LayupSurface  forming the surface upon which this laminate is defined    
            
         
        """
        pass
    @property
    def Rosette(self) -> Rosette:
        """
        Getter for property: ( Rosette NXOpen.C) Rosette
         Returns the  Composites::Rosette  defining the  Composites::Laminate 's coordinate system, providing an orientation reference for the  Composites::Laminate 's child objects   
            
         
        """
        pass
    @Rosette.setter
    def Rosette(self, rosette: Rosette):
        """
        Setter for property: ( Rosette NXOpen.C) Rosette
         Returns the  Composites::Rosette  defining the  Composites::Laminate 's coordinate system, providing an orientation reference for the  Composites::Laminate 's child objects   
            
         
        """
        pass
import NXOpen
class LaminateOffsetSurfaceBuilder(NXOpen.Builder): 
    """ Creates a non-associative convergent body to represent the inner mold line surface for a Composites.Laminate. """
    @property
    def ChordTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChordTolerance
         Returns the maxiumum deviation of a triangle edge to the surface.  
            Only used when source is set to laminate mesh.   
         
        """
        pass
    @property
    def FacetMaximumSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FacetMaximumSize
         Returns the maxiumum length of any triangle facet edge.  
            Only used when source is set to laminate mesh.   
         
        """
        pass
    @property
    def GridControlFactor(self) -> float:
        """
        Getter for property: (float) GridControlFactor
         Returns the multiplier to refine the grid size.  
             
         
        """
        pass
    @GridControlFactor.setter
    def GridControlFactor(self, factor: float):
        """
        Setter for property: (float) GridControlFactor
         Returns the multiplier to refine the grid size.  
             
         
        """
        pass
    @property
    def InputConvergentBody(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) InputConvergentBody
         Returns the convergent body being used, if the input source is set to use a convergent body.  
             
         
        """
        pass
    @property
    def LaminateSelect(self) -> SelectLaminate:
        """
        Getter for property: ( SelectLaminate NXOpen.C) LaminateSelect
         Returns the  Composites::Laminate  to use as the basis for the offset surface.  
             
         
        """
        pass
    @property
    def RampRatio(self) -> float:
        """
        Getter for property: (float) RampRatio
         Returns the ratio of the thickness of the material to the surface distance the ramp travels.  
             
         
        """
        pass
    @RampRatio.setter
    def RampRatio(self, rampRatio: float):
        """
        Setter for property: (float) RampRatio
         Returns the ratio of the thickness of the material to the surface distance the ramp travels.  
             
         
        """
        pass
    @property
    def RemeshChordTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RemeshChordTolerance
         Returns the maxiumum length of any triangle facet edge when remeshing the final result.  
            Only used when remesh result is selected.   
         
        """
        pass
    @property
    def RemeshFacetMaximumSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RemeshFacetMaximumSize
         Returns the maxiumum length of any triangle facet edge when remeshing the final result.  
            Only used when remesh result is selected.   
         
        """
        pass
    @property
    def UseRemeshResults(self) -> bool:
        """
        Getter for property: (bool) UseRemeshResults
         Returns the flag which determines if the builder will remesh the final result of the offset.  
             
         
        """
        pass
    @UseRemeshResults.setter
    def UseRemeshResults(self, flag: bool):
        """
        Setter for property: (bool) UseRemeshResults
         Returns the flag which determines if the builder will remesh the final result of the offset.  
             
         
        """
        pass
    def SetInputToUseConvergentBody(self) -> None:
        """
         Sets the builder to use a selected convergent body as the input mesh. 
        """
        pass
    def SetInputToUseLaminateMesh(self) -> None:
        """
         Sets the builder to create a mesh from the selected Composites.Laminate to use as the input mesh.  
        """
        pass
import NXOpen
class LaminateOffsetSurfaceManager(NXOpen.Object): 
    """ Manages laminate surface offset functionality of the Composites application """
    def CreateLaminateOffsetSurfaceBuilder(part: NXOpen.Part) -> LaminateOffsetSurfaceBuilder:
        """
         Creates a Composites.LaminateOffsetSurfaceBuilder to create a non-associative convergent body to represent the inner mold line surface for a Composites.Laminate. 
         Returns builderObject ( LaminateOffsetSurfaceBuilder NXOpen.C): .
        """
        pass
import NXOpen
class Laminate(Base): 
    """ Represents a sequenced collection of composite objects to be manufactured on a layup surface """
    class ResequenceInsertOption(Enum):
        """
        Members Include: 
         |Before| 
         |After| 

        """
        Before: int
        After: int
        @staticmethod
        def ValueOf(value: int) -> Laminate.ResequenceInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CenterOfMass
         Returns the center of mass of the  Composites::Laminate .  
             
         
        """
        pass
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the  Composites::Laminate .  
             
         
        """
        pass
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) MomentOfInertia
         Returns the moment of inertia of the  Composites::Laminate .  
             
         
        """
        pass
    def GetOrderedImmediateChildPlies(self) -> List[IPly]:
        """
         The ordered list of immediate child plies of the Composites.Laminate. These 
                plies may be superceded by other objects in the final design 
         Returns orderedPlies ( IPly List[NXOpen): .
        """
        pass
    def GetOrderedPlies(self) -> List[IPly]:
        """
         The ordered list of 'final' plies of the Composites.Laminate. These plies define the laminate
                as it is intended to be manufactured. 
         Returns orderedPlies ( IPly List[NXOpen): .
        """
        pass
    def ResequenceChildPlies(self, pliesToResequence: List[IPly], targetPly: IPly, insertOption: Laminate.ResequenceInsertOption) -> None:
        """
         Resequences the given plies before or after the provided target ply. 
        """
        pass
    def ResequencePlies(self, plies_to_resequence: List[Ply], target_ply: Ply, insert_option: Laminate.ResequenceInsertOption) -> None:
        """
         Resequences the given plies before or after the provided target ply. 
        """
        pass
import NXOpen
class LaserProjectionExportBase(NXOpen.Builder): 
    """
    Creates a laser projection file based on the current Composites definition
    """
    @property
    def ExportFileName(self) -> str:
        """
        Getter for property: (str) ExportFileName
         Returns the base file name of the output file(s).  
             
         
        """
        pass
    @ExportFileName.setter
    def ExportFileName(self, exportFileName: str):
        """
        Setter for property: (str) ExportFileName
         Returns the base file name of the output file(s).  
             
         
        """
        pass
    @property
    def ReferenceCoordinateSystem(self) -> NXOpen.CartesianCoordinateSystem:
        """
        Getter for property: ( NXOpen.CartesianCoordinateSystem) ReferenceCoordinateSystem
         Returns the reference coordinate system for the laser projection system.  
             
         
        """
        pass
    @ReferenceCoordinateSystem.setter
    def ReferenceCoordinateSystem(self, referenceCsys: NXOpen.CartesianCoordinateSystem):
        """
        Setter for property: ( NXOpen.CartesianCoordinateSystem) ReferenceCoordinateSystem
         Returns the reference coordinate system for the laser projection system.  
             
         
        """
        pass
    @property
    def ReferencePointsSelect(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) ReferencePointsSelect
         Returns the selection list containing reference points to output.  
             
         
        """
        pass
    def DisableMaximumStepLengthEnforcement(self) -> None:
        """
         Disable inserting additional points for long output boundary segments
        """
        pass
    def EnableMaximumStepLengthEnforcement(self, maximumStepLength: float) -> None:
        """
         Enforce a maximum step length between consecutive points output for each output boundary
        """
        pass
    def UseAlignedVisionOutputFormat(self) -> None:
        """
         Sets the export to use the Aligned Vision format 
        """
        pass
    def UseFAROOutputFormat(self) -> None:
        """
         Sets the export to use the FARO BuildIT format 
        """
        pass
    def UseLAPOutputFormat(self) -> None:
        """
         Sets the export to use the LAP format 
        """
        pass
    def UseSLOutputFormat(self) -> None:
        """
         Sets the export to use the SL (Seiffert Lasertechnik) format 
        """
        pass
    def UseVirtekPlyFormat(self) -> None:
        """
         Sets the export to use the Virtek .ply format 
        """
        pass
    def UseXMLOutputFormat(self) -> None:
        """
         Sets the export to use the generic Composites Laser XML format 
        """
        pass
class LaserProjectionExport(LaserProjectionExportBase): 
    """
    Creates a laser projection file based on the current Composites definition
    """
    @property
    def ExportDirectory(self) -> str:
        """
        Getter for property: (str) ExportDirectory
         Returns the file directory to create the output file(s)   
            
         
        """
        pass
    @ExportDirectory.setter
    def ExportDirectory(self, exportDirectory: str):
        """
        Setter for property: (str) ExportDirectory
         Returns the file directory to create the output file(s)   
            
         
        """
        pass
import NXOpen
class LinearAscendingStaggerProfile(NXOpen.NXObject): 
    """ A stagger profile with increasing consecutive indices """
    pass
import NXOpen
class Manager(NXOpen.Object): 
    """ Manages builders and common functionality of the Composites application """
    @property
    def ActivationManager() -> ActivationManager:
        """
         Returns the  Composites::ActivationManager  belonging to this manager 
        """
        pass
    @property
    def UpdateManager() -> UpdateManager:
        """
         Returns the  Composites::UpdateManager  belonging to this manager 
        """
        pass
    def CreateAddPlyPieceBuilder(part: NXOpen.Part, plyPiece: PlyPiece) -> AddPlyPieceBuilder:
        """
         Creates a Composites.AddPlyPieceBuilder to define a ply piece for a spliced Composites.Ply
         Returns exportObject ( AddPlyPieceBuilder NXOpen.C): .
        """
        pass
    def CreateCoreBuilder(part: NXOpen.Part, core: Core) -> CoreBuilder:
        """
         Creates a Composites.CoreBuilder to create or edit a Composites.Core object 
         Returns builder ( CoreBuilder NXOpen.C): .
        """
        pass
    def CreateCrossSectionBuilder(part: NXOpen.Part, crossSection: CrossSection) -> CrossSectionBuilder:
        """
         Creates a Composites.CrossSectionBuilder to create or edit a Composites.CrossSection object 
         Returns builder ( CrossSectionBuilder NXOpen.C): .
        """
        pass
    def CreateDartBuilder(part: NXOpen.Part, dart: Dart) -> DartBuilder:
        """
         Creates a Composites.DartBuilder to create or edit a Composites.Dart object 
         Returns builder ( DartBuilder NXOpen.C): .
        """
        pass
    def CreateDesignStationBuilder(part: NXOpen.Part, designStation: DesignStation) -> DesignStationBuilder:
        """
         Creates a Composites.DesignStationBuilder to create or edit a Composites.DesignStation object 
         Returns builder ( DesignStationBuilder NXOpen.C): .
        """
        pass
    def CreateHDF5ExportBuilder(part: NXOpen.Part) -> HDF5ExportBuilder:
        """
         Creates a Composites.HDF5ExportBuilder to output composite object data to an HDF5 file for communication with CAE
         Returns builder ( HDF5ExportBuilder NXOpen.C): .
        """
        pass
    def CreateLaminateBuilder(part: NXOpen.Part, laminate: Laminate) -> LaminateBuilder:
        """
         Creates a Composites.LaminateBuilder to create or edit a Composites.Laminate object 
         Returns builder ( LaminateBuilder NXOpen.C): .
        """
        pass
    def CreateLaserProjectionExport(part: NXOpen.Part) -> LaserProjectionExport:
        """
         Creates a Composites.LaserProjectionExport to generate files for a laser projection system 
         Returns exportObject ( LaserProjectionExport NXOpen.C): .
        """
        pass
    def CreateNoSpliceRegionBuilder(part: NXOpen.Part, noSpliceRegion: NoSpliceRegion) -> NoSpliceRegionBuilder:
        """
         Creates a Composites.NoSpliceRegionBuilder to create or edit a Composites.NoSpliceRegion object 
         Returns builder ( NoSpliceRegionBuilder NXOpen.C): .
        """
        pass
    def CreatePlmLaserProjectionExport(part: NXOpen.Part) -> PlmLaserProjectionExport:
        """
         Creates a Composites.PlmLaserProjectionExport to publish files for a laser projection system as datasets in Teamcenter 
         Returns exportObject ( PlmLaserProjectionExport NXOpen.C): .
        """
        pass
    def CreatePlmPlyFlatPatternToDXFBuilder(part: NXOpen.Part) -> PlmPlyFlatPatternToDxfBuilder:
        """
         Creates a Composites.PlmPlyFlatPatternToDxfBuilder to publish flat patterns DXF files as datasets in Teamcenter 
         Returns builder ( PlmPlyFlatPatternToDxfBuilder NXOpen.C): .
        """
        pass
    def CreatePlyBuilder(part: NXOpen.Part, ply: Ply) -> PlyBuilder:
        """
         Creates a Composites.PlyBuilder to create or edit a Composites.Ply object 
         Returns builder ( PlyBuilder NXOpen.C): .
        """
        pass
    def CreatePlyFlatPatternToDXFBuilder(part: NXOpen.Part) -> PlyFlatPatternToDxfBuilder:
        """
         Creates a Composites.PlyFlatPatternToDxfBuilder to output multiple flat patterns to a DXF file 
         Returns builder ( PlyFlatPatternToDxfBuilder NXOpen.C): .
        """
        pass
    def CreatePlyPMIBuilder(part: NXOpen.Part, annotation: PlyPMI) -> PlyPMIBuilder:
        """
         Creates a Composites.PlyPMIBuilder to create an annotation on a Composites.Ply object 
         Returns exportObject ( PlyPMIBuilder NXOpen.C): .
        """
        pass
    def CreatePreferencesBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates a Composites.PreferencesBuilder to create or edit a Composites.Preferences object.
                    The Composites.Preferences object is one per part file. 
         Returns builder ( PreferencesBuilder NXOpen.C): .
        """
        pass
    def CreateProducibilityBuilder(part: NXOpen.Part, producibility: Producibility) -> ProducibilityBuilder:
        """
         Creates a Composites.ProducibilityBuilder to create or edit a Composites.Producibility object
         Returns builder ( ProducibilityBuilder NXOpen.C): .
        """
        pass
    def CreateRosetteBuilder(part: NXOpen.Part, rosette: Rosette) -> RosetteBuilder:
        """
         Creates a Composites.RosetteBuilder to create or edit a Composites.Rosette object 
         Returns builder ( RosetteBuilder NXOpen.C): .
        """
        pass
    def CreateRuleBasedSpliceBuilder(part: NXOpen.Part, splice: RuleBasedSplice) -> RuleBasedSpliceBuilder:
        """
         Creates a Composites.RuleBasedSpliceBuilder to define one or more spliced Composites.Ply objects using a rule
         Returns buildre ( RuleBasedSpliceBuilder NXOpen.C): .
        """
        pass
    def CreateSequenceSetter(part: NXOpen.Part) -> SequenceSetter:
        """
         Creates a Composites.SequenceSetter to add a sequence value to one or more object
         Returns builder ( SequenceSetter NXOpen.C): .
        """
        pass
    def CreateStaggerProfileBuilder(part: NXOpen.Part) -> StaggerProfileBuilder:
        """
         Creates a Composites.StaggerProfileBuilder to create a stagger profile object 
         Returns builder ( StaggerProfileBuilder NXOpen.C): .
        """
        pass
    def GetCompositePart(part: NXOpen.Part) -> CompositePart:
        """
         Gets the Composites.CompositePart in the part file if it exists 
         Returns compositePart ( CompositePart NXOpen.C): .
        """
        pass
import NXOpen
class MaterialSpecificationBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[MaterialSpecificationBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: MaterialSpecificationBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
               not change, but the item at this index is set to NULL.
            
        """
        pass
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    @overload
    def Erase(self, obj: MaterialSpecificationBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: MaterialSpecificationBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: MaterialSpecificationBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> MaterialSpecificationBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( MaterialSpecificationBuilder NXOpen.C):  object found at input index .
        """
        pass
    def GetContents(self) -> List[MaterialSpecificationBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( MaterialSpecificationBuilder List[NXOpen):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: MaterialSpecificationBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    def SetContents(self, objects: List[MaterialSpecificationBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    @overload
    def Swap(self, object1: MaterialSpecificationBuilder, object2: MaterialSpecificationBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
class MaterialWidthLines(Base): 
    """ Represents a set of curves spaced by material width, often used for splicing. """
    pass
import NXOpen
import NXOpen.Features
class NoSpliceRegionBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.NoSpliceRegion object.
    """
    @property
    def BoundaryRegion(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) BoundaryRegion
         Returns the selected  Composites::Features::Region , defining the extents of the  Composites::NoSpliceRegion   
            
         
        """
        pass
    @BoundaryRegion.setter
    def BoundaryRegion(self, region: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) BoundaryRegion
         Returns the selected  Composites::Features::Region , defining the extents of the  Composites::NoSpliceRegion   
            
         
        """
        pass
    @property
    def ParentLaminate(self) -> SelectLaminate:
        """
        Getter for property: ( SelectLaminate NXOpen.C) ParentLaminate
         Returns the list containing the single selected parent  Composites::Laminate .  
            
         
        """
        pass
class NoSpliceRegion(Base): 
    """ Represents an area of the part where splicing is not allowed. """
    pass
class PlmLaserProjectionExport(LaserProjectionExportBase): 
    """
    Creates a laser projection file based on the current Composites definition and publishes it as a dataset in Teamcenter
    """
    pass
class PlmPlyFlatPatternToDxfBuilder(PlyFlatPatternToDxfBuilderBase): 
    """
    Creates DXF Flat Pattern Plm Builder object.
    """
    pass
import NXOpen
import NXOpen.Features
class PlyBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.Ply object.
    """
    @property
    def BoundaryRegion(self) -> NXOpen.Features.Feature:
        """
        Getter for property: ( NXOpen.Features.Feature) BoundaryRegion
         Returns the selected  Composites::Features::Region , defining the extents of the  Composites::Ply   
            
         
        """
        pass
    @BoundaryRegion.setter
    def BoundaryRegion(self, region: NXOpen.Features.Feature):
        """
        Setter for property: ( NXOpen.Features.Feature) BoundaryRegion
         Returns the selected  Composites::Features::Region , defining the extents of the  Composites::Ply   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: ( NXOpen.PhysicalMaterial) Material
         Returns a material string   
            
         
        """
        pass
    @Material.setter
    def Material(self, material: NXOpen.PhysicalMaterial):
        """
        Setter for property: ( NXOpen.PhysicalMaterial) Material
         Returns a material string   
            
         
        """
        pass
    @property
    def OrientationString(self) -> str:
        """
        Getter for property: (str) OrientationString
         Returns the  Composites::Ply 's orientation.  
             
         
        """
        pass
    @OrientationString.setter
    def OrientationString(self, orientationString: str):
        """
        Setter for property: (str) OrientationString
         Returns the  Composites::Ply 's orientation.  
             
         
        """
        pass
    @property
    def ParentLaminate(self) -> SelectLaminate:
        """
        Getter for property: ( SelectLaminate NXOpen.C) ParentLaminate
         Returns the list containing the single selected parent  Composites::Laminate .  
            
         
        """
        pass
import NXOpen
class PlyFlatPatternToDxfBuilderBase(NXOpen.Builder): 
    """
    Creates Flat Pattern to DXF Builder object.
    """
    class Dxf(Enum):
        """
        Members Include: 
         |VersionR12| 
         |VersionR13| 
         |VersionR14| 
         |Version2000| 
         |Version2004| 
         |Version2005| 
         |Version2007| 
         |VersionsFrom2010To2012| 
         |VersionsFrom2013To2017| 
         |VersionsFrom2018To2022| 

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
        @staticmethod
        def ValueOf(value: int) -> PlyFlatPatternToDxfBuilderBase.Dxf:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DXFVersion(self) -> PlyFlatPatternToDxfBuilderBase.Dxf:
        """
        Getter for property: ( PlyFlatPatternToDxfBuilderBase.Dxf NXOpen.C) DXFVersion
         Returns the DXF Version of the DXF output.  
             
         
        """
        pass
    @DXFVersion.setter
    def DXFVersion(self, dxfVersion: PlyFlatPatternToDxfBuilderBase.Dxf):
        """
        Setter for property: ( PlyFlatPatternToDxfBuilderBase.Dxf NXOpen.C) DXFVersion
         Returns the DXF Version of the DXF output.  
             
         
        """
        pass
    def AddPlies(self, iPlies: List[IPly]) -> None:
        """
         Adds a collection of Composites.IPly to output flat pattern results for. 
        """
        pass
class PlyFlatPatternToDxfBuilder(PlyFlatPatternToDxfBuilderBase): 
    """
    Creates Flat Pattern to DXF Builder object.
    """
    @property
    def ExportDirectory(self) -> str:
        """
        Getter for property: (str) ExportDirectory
         Returns the file directory of the DXF output.  
             
         
        """
        pass
    @ExportDirectory.setter
    def ExportDirectory(self, exportDirectory: str):
        """
        Setter for property: (str) ExportDirectory
         Returns the file directory of the DXF output.  
             
         
        """
        pass
class PlyPiece(Base): 
    """ Represents a single piecelayer of material to be deposited during manufacturing """
    pass
import NXOpen.Annotations
class PlyPMIBuilder(NXOpen.Annotations.PmiNoteBuilder): 
    """ Creates or edits Composites NXOpen.Composites.PlyPMI objects """
    pass
import NXOpen.Annotations
class PlyPMI(NXOpen.Annotations.Label): 
    """ A label referencing a NXOpen.Composites.Ply object"""
    pass
class PlyResequenceOption(Enum):
    """
    Members Include: 
     |Before| 
     |After| 

    """
    Before: int
    After: int
    @staticmethod
    def ValueOf(value: int) -> PlyResequenceOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class Ply(Base): 
    """ Represents a single piecelayer of material to be deposited during manufacturing """
    class ResequenceInsertOption(Enum):
        """
        Members Include: 
         |Before| 
         |After| 

        """
        Before: int
        After: int
        @staticmethod
        def ValueOf(value: int) -> Ply.ResequenceInsertOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Area(self) -> float:
        """
        Getter for property: (float) Area
         Returns the area of the  Composites::IPly .  
             
         
        """
        pass
    @property
    def CenterOfMass(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) CenterOfMass
         Returns the center of mass of the  Composites::IPly .  
             
         
        """
        pass
    @property
    def CuredThickness(self) -> float:
        """
        Getter for property: (float) CuredThickness
         Returns the cured thickness of the  Composites::IPly .  
             
         
        """
        pass
    @property
    def Density(self) -> float:
        """
        Getter for property: (float) Density
         Returns the density of the  Composites::IPly .  
             
         
        """
        pass
    @property
    def Mass(self) -> float:
        """
        Getter for property: (float) Mass
         Returns the mass of the  Composites::IPly .  
             
         
        """
        pass
    @property
    def MomentOfInertia(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) MomentOfInertia
         Returns the moment of inertia of the  Composites::IPly .  
             
         
        """
        pass
    @property
    def Perimeter(self) -> float:
        """
        Getter for property: (float) Perimeter
         Returns the perimeter of the  Composites::IPly .  
             
         
        """
        pass
    @property
    def Sequence(self) -> float:
        """
        Getter for property: (float) Sequence
         Returns the stacking sequence number of  Composites::IPly .  
             
         
        """
        pass
    def GetOrderedIPlyPieces(self) -> List[IPlyPiece]:
        """
         The ordered list of Composites.IPlyPiece objects that this
                Composites.Ply is broken up into 
         Returns orderedPlyPieces ( IPlyPiece List[NXOpen): .
        """
        pass
    def ResequenceIPlyPieces(self, pieces_to_resequence: List[IPlyPiece], target_ply_piece: IPlyPiece, insert_option: Ply.ResequenceInsertOption) -> None:
        """
         Resequences the given Composites.IPlyPiece objects before or after the provided target Composites.IPlyPiece. 
        """
        pass
import NXOpen
class PMIManager(NXOpen.Object): 
    """ Manages PMI builders and functionality for the Composites application """
    def CreateAutoCrossSectionPMICoreCreationBuilder(part: NXOpen.Part, crossSection: CrossSection, core: Core, indicationPoint: NXOpen.Point3d) -> AutoCrossSectionPMIBuilder:
        """
         Creates a Composites.AutoCrossSectionPMIBuilder to create a Composites.AutoCrossSectionPMI for a core object
         Returns exportObject ( AutoCrossSectionPMIBuilder NXOpen.C): .
        """
        pass
    def CreateAutoCrossSectionPMIEditBuilder(part: NXOpen.Part, annotation: AutoCrossSectionPMI) -> AutoCrossSectionPMIBuilder:
        """
         Creates a Composites.AutoCrossSectionPMIBuilder to edit a Composites.AutoCrossSectionPMI
         Returns exportObject ( AutoCrossSectionPMIBuilder NXOpen.C): .
        """
        pass
    def CreateAutoCrossSectionPMIPlyEndCreationBuilder(part: NXOpen.Part, crossSection: CrossSection, ply: IPly, indicationPoint: NXOpen.Point3d) -> AutoCrossSectionPMIBuilder:
        """
         Creates a Composites.AutoCrossSectionPMIBuilder to create a Composites.AutoCrossSectionPMI at the start of end of a ply
         Returns exportObject ( AutoCrossSectionPMIBuilder NXOpen.C): .
        """
        pass
    def CreateAutoCrossSectionPMIPlyStartCreationBuilder(part: NXOpen.Part, crossSection: CrossSection, ply: IPly, indicationPoint: NXOpen.Point3d) -> AutoCrossSectionPMIBuilder:
        """
         Creates a Composites.AutoCrossSectionPMIBuilder to create a Composites.AutoCrossSectionPMI at the start of a ply
         Returns exportObject ( AutoCrossSectionPMIBuilder NXOpen.C): .
        """
        pass
    def CreateCrossSectionPMIBuilder(part: NXOpen.Part, annotation: CrossSectionPMI) -> CrossSectionPMIBuilder:
        """
         Creates a Composites.CrossSectionPMIBuilder to create an annotation on a Composites.CrossSection object 
         Returns exportObject ( CrossSectionPMIBuilder NXOpen.C): .
        """
        pass
    def CreateDesignStationPMIBuilder(part: NXOpen.Part, annotation: DesignStationPMI) -> DesignStationPMIBuilder:
        """
         Creates a Composites.DesignStationPMIBuilder to create an annotation on a Composites.DesignStation object 
         Returns exportObject ( DesignStationPMIBuilder NXOpen.C): .
        """
        pass
import NXOpen
class PreferencesBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.Preferences object
    """
    @property
    def MaterialWidthExceededTolerance(self) -> float:
        """
        Getter for property: (float) MaterialWidthExceededTolerance
         Returns the producibility material width tolerance used to determine whether the material width is exceeded   
            
         
        """
        pass
    @MaterialWidthExceededTolerance.setter
    def MaterialWidthExceededTolerance(self, materialWidthTolerance: float):
        """
        Setter for property: (float) MaterialWidthExceededTolerance
         Returns the producibility material width tolerance used to determine whether the material width is exceeded   
            
         
        """
        pass
    @property
    def NegativeBiasDirectionColor(self) -> int:
        """
        Getter for property: (int) NegativeBiasDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    @NegativeBiasDirectionColor.setter
    def NegativeBiasDirectionColor(self, negativeBiasDirectionColor: int):
        """
        Setter for property: (int) NegativeBiasDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    @property
    def OtherDirectionColor(self) -> int:
        """
        Getter for property: (int) OtherDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    @OtherDirectionColor.setter
    def OtherDirectionColor(self, otherDirectionColor: int):
        """
        Setter for property: (int) OtherDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    @property
    def PlyLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) PlyLineWidth
         Returns the  DisplayableObject::ObjectWidth  defining line width for Ply   
            
         
        """
        pass
    @PlyLineWidth.setter
    def PlyLineWidth(self, plyLineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) PlyLineWidth
         Returns the  DisplayableObject::ObjectWidth  defining line width for Ply   
            
         
        """
        pass
    @property
    def PositiveBiasDirectionColor(self) -> int:
        """
        Getter for property: (int) PositiveBiasDirectionColor
         Returns the color of the positive bias direction   
            
         
        """
        pass
    @PositiveBiasDirectionColor.setter
    def PositiveBiasDirectionColor(self, positiveBiasDirectionColor: int):
        """
        Setter for property: (int) PositiveBiasDirectionColor
         Returns the color of the positive bias direction   
            
         
        """
        pass
    @property
    def PrimaryDirectionColor(self) -> int:
        """
        Getter for property: (int) PrimaryDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    @PrimaryDirectionColor.setter
    def PrimaryDirectionColor(self, primaryDirectionColor: int):
        """
        Setter for property: (int) PrimaryDirectionColor
         Returns the color of the primary direction   
            
         
        """
        pass
    @property
    def ProducibilityDefaultCellSize(self) -> float:
        """
        Getter for property: (float) ProducibilityDefaultCellSize
         Returns the producibility default cell size   
            
         
        """
        pass
    @ProducibilityDefaultCellSize.setter
    def ProducibilityDefaultCellSize(self, cellSize: float):
        """
        Setter for property: (float) ProducibilityDefaultCellSize
         Returns the producibility default cell size   
            
         
        """
        pass
    @property
    def ProducibilityLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) ProducibilityLineWidth
         Returns the  DisplayableObject::ObjectWidth  defining line width for Producibility   
            
         
        """
        pass
    @ProducibilityLineWidth.setter
    def ProducibilityLineWidth(self, producibilityLineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) ProducibilityLineWidth
         Returns the  DisplayableObject::ObjectWidth  defining line width for Producibility   
            
         
        """
        pass
    @property
    def RosetteLineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) RosetteLineWidth
         Returns the  DisplayableObject::ObjectWidth  defining line width for Rosette   
            
         
        """
        pass
    @RosetteLineWidth.setter
    def RosetteLineWidth(self, rosetteLineWidth: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) RosetteLineWidth
         Returns the  DisplayableObject::ObjectWidth  defining line width for Rosette   
            
         
        """
        pass
    @property
    def SecondaryDirectionColor(self) -> int:
        """
        Getter for property: (int) SecondaryDirectionColor
         Returns the color of the secondary direction   
            
         
        """
        pass
    @SecondaryDirectionColor.setter
    def SecondaryDirectionColor(self, secondaryDirectionColor: int):
        """
        Setter for property: (int) SecondaryDirectionColor
         Returns the color of the secondary direction   
            
         
        """
        pass
class Preferences(Base): 
    """ Represents the Composites Preferences. """
    pass
import NXOpen
class ProducibilityBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.Producibility object
    """
    @property
    def CellSize(self) -> float:
        """
        Getter for property: (float) CellSize
         Returns the cell size of the  Composites::Producibility  simulation.  
           A smaller value creates denser results.   
         
        """
        pass
    @CellSize.setter
    def CellSize(self, cellSize: float):
        """
        Setter for property: (float) CellSize
         Returns the cell size of the  Composites::Producibility  simulation.  
           A smaller value creates denser results.   
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Origin
         Returns the starting  Point  of the  Composites::Producibility .  
             
         
        """
        pass
    @Origin.setter
    def Origin(self, originPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Origin
         Returns the starting  Point  of the  Composites::Producibility .  
             
         
        """
        pass
    @property
    def OverrideCurveSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) OverrideCurveSection
         Returns the geometry defining the desired primary fiber direction for the  Composites::Producibility  simulation.  
            This overrides any direction defined on the  Composites::IPly .   
         
        """
        pass
    @property
    def Ply(self) -> SelectIPly:
        """
        Getter for property: ( SelectIPly NXOpen.C) Ply
         Returns the  Composites::IPly  on which the  Composites::Producibility  is run.  
             
         
        """
        pass
    def ClearResults(self) -> None:
        """
         Clears the current producibility simulation results, forcing a resimulation on commit 
        """
        pass
    def SetConstraintPropagationTypeGeodesic(self) -> None:
        """
         Sets the constraint propagation type to use a geodesic curve 
        """
        pass
    def SetConstraintPropagationTypeStandard(self) -> None:
        """
         Sets the constraint propagation type to use the standard type. 
        """
        pass
    def SetConstraintPropagationTypeToCurve(self) -> None:
        """
         Sets the constraint propagation type to use a user-specified curve 
        """
        pass
class Producibility(Base): 
    """ Represents a simulation showing the effects of draping a Composites.Ply onto a Composites.Features.LayupSurface """
    def PublishFlatPattern(self) -> None:
        """
         Generateupdate the Composites.FlatPattern calculated from the draping simulation results
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class RosetteBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.Rosette object
    """
    class StandardRosetteInfo:
        """
         the information required for creating a standard-mapping rosette. 
         RosetteBuilderStandardRosetteInfo_Struct NXOpen.C is an alias for  RosetteBuilder.StandardRosetteInfo NXOpen.C.
        """
        @property
        def OriginPoint(self) -> NXOpen.GeometricUtilities.NXOpen.Point:
            """
            Getter for property OriginPoint
            the  Point  defining the point at which the standard-mapping rosette's zero direction is defined.

            """
            pass
        @OriginPoint.setter
        def OriginPoint(self, value: NXOpen.GeometricUtilities.NXOpen.Point):
            """
            Getter for property OriginPoint
            the  Point  defining the point at which the standard-mapping rosette's zero direction is defined.
            Setter for property OriginPoint
            the  Point  defining the point at which the standard-mapping rosette's zero direction is defined.

            """
            pass
        @property
        def ZeroDirection(self) -> NXOpen.GeometricUtilities.NXOpen.Direction:
            """
            Getter for property ZeroDirection
            the  Direction  defining the zero direction of a standard-mapping rosette.

            """
            pass
        @ZeroDirection.setter
        def ZeroDirection(self, value: NXOpen.GeometricUtilities.NXOpen.Direction):
            """
            Getter for property ZeroDirection
            the  Direction  defining the zero direction of a standard-mapping rosette.
            Setter for property ZeroDirection
            the  Direction  defining the zero direction of a standard-mapping rosette.

            """
            pass
        @property
        def LayupSurface(self) -> NXOpen.Features.Feature:
            """
            Getter for property LayupSurface
            the  Composites::Features::LayupSurface  defining the surface the standard-mapping rosette's origin must lie on.

            """
            pass
        @LayupSurface.setter
        def LayupSurface(self, value: NXOpen.Features.Feature):
            """
            Getter for property LayupSurface
            the  Composites::Features::LayupSurface  defining the surface the standard-mapping rosette's origin must lie on.
            Setter for property LayupSurface
            the  Composites::Features::LayupSurface  defining the surface the standard-mapping rosette's origin must lie on.

            """
            pass
    class TranslationalRosetteInfo:
        """
         the information required for creating a translational-mapping rosette. 
         RosetteBuilderTranslationalRosetteInfo_Struct NXOpen.C is an alias for  RosetteBuilder.TranslationalRosetteInfo NXOpen.C.
        """
        @property
        def ReferenceCsys(self) -> NXOpen.CartesianCoordinateSystem:
            """
            Getter for property ReferenceCsys
            the  CartesianCoordinateSystem  defining the orientations at a single location for translational-mapping rosette.

            """
            pass
        @ReferenceCsys.setter
        def ReferenceCsys(self, value: NXOpen.CartesianCoordinateSystem):
            """
            Getter for property ReferenceCsys
            the  CartesianCoordinateSystem  defining the orientations at a single location for translational-mapping rosette.
            Setter for property ReferenceCsys
            the  CartesianCoordinateSystem  defining the orientations at a single location for translational-mapping rosette.

            """
            pass
    @property
    def StandardRosetteData(self) -> RosetteBuilder.StandardRosetteInfo:
        """
        Getter for property: ( RosetteBuilder.StandardRosetteInfo NXOpen.C) StandardRosetteData
         Returns the  Composites::RosetteBuilder::StandardRosetteInfo  defining the data required for the standard-mapping rosette.  
             
         
        """
        pass
    @StandardRosetteData.setter
    def StandardRosetteData(self, standardRosetteData: RosetteBuilder.StandardRosetteInfo):
        """
        Setter for property: ( RosetteBuilder.StandardRosetteInfo NXOpen.C) StandardRosetteData
         Returns the  Composites::RosetteBuilder::StandardRosetteInfo  defining the data required for the standard-mapping rosette.  
             
         
        """
        pass
    @property
    def TranslationalRosetteData(self) -> RosetteBuilder.TranslationalRosetteInfo:
        """
        Getter for property: ( RosetteBuilder.TranslationalRosetteInfo NXOpen.C) TranslationalRosetteData
         Returns the  CartesianCoordinateSystem  defining the orientations at a single location   
            
         
        """
        pass
    @TranslationalRosetteData.setter
    def TranslationalRosetteData(self, translationalRosetteData: RosetteBuilder.TranslationalRosetteInfo):
        """
        Setter for property: ( RosetteBuilder.TranslationalRosetteInfo NXOpen.C) TranslationalRosetteData
         Returns the  CartesianCoordinateSystem  defining the orientations at a single location   
            
         
        """
        pass
class Rosette(Base): 
    """ Represents a coordinate system and mapping scheme to define reference orientations at various locations """
    pass
import NXOpen
class RuleBasedSpliceBuilder(NXOpen.Builder): 
    """
    Creates or edits a Composites.RuleBasedSplice object.
    """
    @property
    def RuleInstance(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) RuleInstance
         Returns the rule instance   
            
         
        """
        pass
    @RuleInstance.setter
    def RuleInstance(self, data: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) RuleInstance
         Returns the rule instance   
            
         
        """
        pass
class RuleBasedSplice(Base): 
    """ Represents the operation to divide one or more Composites.Ply objects into one or more Composites.AutomatedPlyPiece objects using a rule"""
    pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectIPlyList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    @overload
    def Add(self, objectValue: IPly) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[IPly], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[IPly]) -> bool:
        """
         Adds a set of objects to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: IPly, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: IPly, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: IPly, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    def Contains(self, objectValue: IPly) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[IPly]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( IPly List[NXOpen):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: IPly) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[IPly]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: IPly, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: IPly, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: IPly, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         Returns removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    def SetArray(self, objects: List[IPly]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectIPly(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> IPly:
        """
        Getter for property: ( IPly NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: IPly):
        """
        Setter for property: ( IPly NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[IPly, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  IPly NXOpen.C. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, IPly, NXOpen.View, NXOpen.Point3d, IPly, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  IPly NXOpen.C. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  IPly NXOpen.C. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def SetValue(self, selection: IPly, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: IPly, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: IPly, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectLaminate(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Laminate:
        """
        Getter for property: ( Laminate NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Laminate):
        """
        Setter for property: ( Laminate NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Laminate, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Laminate NXOpen.C. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Laminate, NXOpen.View, NXOpen.Point3d, Laminate, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Laminate NXOpen.C. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Laminate NXOpen.C. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def SetValue(self, selection: Laminate, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Laminate, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Laminate, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectPly(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Ply:
        """
        Getter for property: ( Ply NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Ply):
        """
        Setter for property: ( Ply NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Ply, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Ply NXOpen.C. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Ply, NXOpen.View, NXOpen.Point3d, Ply, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Ply NXOpen.C. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Ply NXOpen.C. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def SetValue(self, selection: Ply, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Ply, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Ply, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectProducibility(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Producibility:
        """
        Getter for property: ( Producibility NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Producibility):
        """
        Setter for property: ( Producibility NXOpen.C) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Producibility, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Producibility NXOpen.C. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Producibility, NXOpen.View, NXOpen.Point3d, Producibility, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Producibility NXOpen.C. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Producibility NXOpen.C. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def SetValue(self, selection: Producibility, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Producibility, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Producibility, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
import NXOpen
class SequenceSetter(NXOpen.Builder): 
    """ Sets a new sequence on one or more objects """
    def SetSequence(self, objTag: IObjectCanSetSequence, sequence: float) -> None:
        """
         Define a new sequence value to apply to the provided object. 
        """
        pass
import NXOpen
class StaggerProfileBuilder(NXOpen.Builder): 
    """ Creates a stagger profile object """
    def GetCustomStaggerIndicies(self) -> List[int]:
        """
         Gets the custom stagger indicies for this stagger profile 
         Returns indicies (List[int]): .
        """
        pass
    def SetCustomStaggerIndicies(self, indicies: List[int]) -> None:
        """
         Sets the custom stagger indicies for this stagger profile 
        """
        pass
import NXOpen
class UpdateManager(NXOpen.Object): 
    """ Represents an object to update Composites objects """
    def UpdateObjects(objectTags: List[ICanBeUpdated]) -> None:
        """
         Update the indicated objects 
        """
        pass
