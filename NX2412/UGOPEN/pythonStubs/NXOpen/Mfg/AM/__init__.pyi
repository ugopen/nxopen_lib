from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddBuildTrayBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.AddBuildTrayBuilder builder """
    @property
    def Selection(self) -> SelectPartList:
        """
        Getter for property: ( SelectPartList NXOpen) Selection
         Returns the selection   
            
         
        """
        pass
import NXOpen
class ApplicationManager(NXOpen.Object): 
    """ Represents the Additive Manufacturing application """
    def CreateAddBuildTrayBuilder() -> AddBuildTrayBuilder:
        """
         Add New Build Tray 
         Returns builder ( AddBuildTrayBuilder NXOpen):   the Add BuildTray Builder .
        """
        pass
    def CreateBuildTray(part: NXOpen.Part) -> BuildTray:
        """
         Creates a build tray in a file 
         Returns builder ( BuildTray NXOpen):   the build tray .
        """
        pass
    def CreateMergeSupportsBuilder() -> MergeSupportsBuilder:
        """
         Creates a Mfg.AM.MergeSupportsBuilder 
         Returns builder ( MergeSupportsBuilder NXOpen):   the merge supports builder .
        """
        pass
    def CreateMovePartBuilder(partToMove: Part) -> MovePartBuilder:
        """
         Creates a Mfg.AM.MovePartBuilder 
         Returns builder ( MovePartBuilder NXOpen):   the move part builder .
        """
        pass
    def CreateNoBuildZoneBuilder() -> NoBuildZoneBuilder:
        """
         Creates a Mfg.AM.NoBuildZoneBuilder 
         Returns builder ( NoBuildZoneBuilder NXOpen):   the print zone builder .
        """
        pass
    def CreatePatternAMPartBuilder(part: NXOpen.Part, editedComponent: NXOpen.NXObject) -> PatternAMPartBuilder:
        """
         Creates a Mfg.AM.PatternAMPartBuilder object. 
         Returns builder ( PatternAMPartBuilder NXOpen):   the pattern part builder .
        """
        pass
    def CreateRepositionPartBuilder(part: NXOpen.Part) -> RepositionPartBuilder:
        """
         Creates a Mfg.AM.RepositionPartBuilder 
         Returns builder ( RepositionPartBuilder NXOpen):   the reposition part builder .
        """
        pass
    def CreateSinterboxBuilder(sinterbox: Sinterbox) -> SinterboxBuilder:
        """
         Creates NXOpen.Mfg.AM.SinterboxBuilder 
         Returns builder ( SinterboxBuilder NXOpen):   the Sinterbox Builder .
        """
        pass
    def CreateSubnestingBuilder() -> SubnestingBuilder:
        """
         Creates a Mfg.AM.SubnestingBuilder 
         Returns builder ( SubnestingBuilder NXOpen):   the Subnesting part builder .
        """
        pass
    def CreateSupportBuilder() -> SupportBuilder:
        """
         Creates Builder which allows for Creating Supports(Automatic, Manual, Regions Only) 
         Returns tagBuilder ( SupportBuilder NXOpen): .
        """
        pass
    def Get3DNester() -> Nester3D:
        """
         Retrieves the 3D Nester object 
         Returns builder ( Nester3D NXOpen):   the 3D Nester .
        """
        pass
    def GetAttributeClipboard() -> AttributeClipboard:
        """
         Retrieves the Mfg.AM.AttributeClipboard 
         Returns pAttributeClipboard ( AttributeClipboard NXOpen):  AttributeClipboard .
        """
        pass
    def GetBuildTray(part: NXOpen.Part) -> BuildTray:
        """
         Retrieves the Mfg.AM.BuildTray 
         Returns builder ( BuildTray NXOpen):   the build tray .
        """
        pass
    def GetClipboard() -> Clipboard:
        """
         Creates a copy paste clipboard  
         Returns pClipboard ( Clipboard NXOpen):  Clipboard .
        """
        pass
    def GetMeshProperties() -> MeshProperties:
        """
         Creates a mesh properties builder  
         Returns tagBuilder ( MeshProperties NXOpen): .
        """
        pass
    def GetRootLibrary() -> Library:
        """
         Gets the Root Node of Profile Library 
         Returns profileRoot ( Library NXOpen):  profile root .
        """
        pass
    def GetSupportBuilder(tagSupport: Support) -> SupportBuilder:
        """
         Retrieves the support builder object 
         Returns tagBuilder ( SupportBuilder NXOpen):   the support builder .
        """
        pass
class AssemblyBuildTray(Assembly): 
    """ Represents a Mfg.AM.AssemblyBuildTray."""
    pass
class Assembly(PartGroup): 
    """ Represents a Mfg.AM.Assembly."""
    pass
import NXOpen
class AttributeClipboard(NXOpen.NXObject): 
    """  attribute clipboard """
    def CopyAttributes(self, target: NXOpen.TaggedObject) -> None:
        """
         Copy attributes 
        """
        pass
    def PasteAttributes(self, target: NXOpen.TaggedObject) -> None:
        """
         Paste attributes 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class BuildTray(NXOpen.DisplayableObject): 
    """ Interface for Model Build Tray objects """
    def AddComponent(self, part: NXOpen.Assemblies.Component) -> None:
        """
         Adds a component (occurrence) to the build tray 
        """
        pass
    @overload
    def AddPart(self, fileName: str) -> None:
        """
         Adds a part to the build tray by file name 
        """
        pass
    @overload
    def AddPart(self, part: NXOpen.Part) -> None:
        """
         Adds a part to the build tray 
        """
        pass
    def ClearBuildStrategyValues(self) -> None:
        """
         Clear BuildStrategy values
        """
        pass
    def FindPart(self, tagGeometry: NXOpen.DisplayableObject) -> Part:
        """
         Finds the AM part (if any) containing the given geometry 
         Returns part ( Part NXOpen): .
        """
        pass
    def Generate(self) -> PrintJob:
        """
         Generates 3D printer data without sending it to the printer 
         Returns printJob ( PrintJob NXOpen):  print job .
        """
        pass
    def Generate3MFfile(self) -> str:
        """
         Generates the 3MF output file 
         Returns pathName (str):  Generated 3MF file path .
        """
        pass
    def GenerateAllPrintMarks(self) -> None:
        """
         Generate all print marks 
        """
        pass
    def GetAllParts(self) -> List[Part]:
        """
         Gets all the parts in the build tray 
         Returns parts ( Part List[NXOp): .
        """
        pass
    def GetBuildStrategyValues(self) -> Tuple[List[str], List[str]]:
        """
         Get BuildStrategy values
         Returns A tuple consisting of (buildStrategyNames, buildStrategyValues). 
         - buildStrategyNames is: List[str]. the list of buildStrategy names .
         - buildStrategyValues is: List[str]. the list of buildStrategy values .

        """
        pass
    def GetDimensions(self) -> Tuple[bool, float, float, float, float, float]:
        """
         Gets the build tray dimensions 
         Returns A tuple consisting of (isBox, dLength, dWidth, dDiameter, dHeight, dTrayHeight). 
         - isBox is: bool.
         - dLength is: float.
         - dWidth is: float.
         - dDiameter is: float.
         - dHeight is: float.
         - dTrayHeight is: float.

        """
        pass
    def GetGroups(self) -> List[PartGroup]:
        """
         Returns the groups in the build tray.
         Returns groups ( PartGroup List[NXOp): .
        """
        pass
    def GetOrigin(self) -> NXOpen.Point3d:
        """
         Gets the build tray origin 
         Returns origin ( NXOpen.Point3d): .
        """
        pass
    def GetOutputDirectory(self) -> str:
        """
         Create reference set for buildtray part
         Returns outputDirectory (str):  the output directory for the selected printer for this buildtray in NX-AM .
        """
        pass
    def GetPrinter(self) -> Printer:
        """
         Gets the printer of the build tray 
         Returns status ( Printer NXOpen):  printer .
        """
        pass
    def GetProfile(self) -> ProfileLibrary:
        """
         Returns the assigned profile library 
         Returns tagProfile ( ProfileLibrary NXOpen): .
        """
        pass
    def Group(self, children: List[Part]) -> PartGroup:
        """
         Groups a number of parts into a new group. If parts are already a member of a group they will be removed from that group.
         Returns tagNewGroup ( PartGroup NXOpen):  the new group .
        """
        pass
    def Print3D(self) -> PrintJob:
        """
         Prints the build tray 
         Returns printJob ( PrintJob NXOpen):  print job .
        """
        pass
    def RemoveComponent(self, part: NXOpen.Assemblies.Component) -> None:
        """
         Remove a component (occurrence) from the build tray 
        """
        pass
    def ReorderParts(self, objectsToReorder: List[NXOpen.DisplayableObject], anchor: NXOpen.DisplayableObject, reorderBefore: bool) -> None:
        """
         Sets the print order by moving parts or part groups before or after anchor part
        """
        pass
    def SendToMachine(self) -> PrintJob:
        """
         Sends the output files to the printer 
         Returns printJob ( PrintJob NXOpen):  print job .
        """
        pass
    def SetBuildStrategyValues(self, buildStrategyNames: List[str], buildStrategyValues: List[str]) -> None:
        """
         Set BuildStrategy values
        """
        pass
    def SetDefaultProfile(self, part: Profile) -> None:
        """
         Sets the given profile as the default profile on the build tray 
        """
        pass
    def SetPrinter(self, status: Printer) -> None:
        """
         Prints the build tray 
        """
        pass
    def SetProfile(self, supportProfile: ProfileLibrary) -> None:
        """
         Sets the profile library 
        """
        pass
    def SetSupportProfile(self, tagSupportProfile: SupportProfile) -> None:
        """
         Sets the given profile as the default support profile on the build tray 
        """
        pass
    def Synchronize(self) -> None:
        """
         Synchronize the build tray and selected objects 
        """
        pass
import NXOpen
class Clipboard(NXOpen.NXObject): 
    """  CopyPaste Clipboard """
    def Clear(self) -> None:
        """
         Empties the clipboard 
        """
        pass
    def Copy(self, objectsToCopy: List[NXOpen.NXObject]) -> None:
        """
         Copy 
        """
        pass
    def GetReferencePoint(self) -> NXOpen.Point3d:
        """
         The point of origin of the clipboard objects 
         Returns ptMax ( NXOpen.Point3d): .
        """
        pass
    def IsEmpty(self) -> bool:
        """
         Checks if there is anything to paste 
         Returns bIsEmpty (bool): .
        """
        pass
    def Paste(self, target: NXOpen.TaggedObject) -> List[NXOpen.NXObject]:
        """
         Paste
         Returns objectCopies ( NXOpen.NXObject Li): .
        """
        pass
    def PasteSpecial(self, target: NXOpen.TaggedObject, xform: NXOpen.Matrix4x4) -> List[NXOpen.NXObject]:
        """
         Paste Special
         Returns objectCopies ( NXOpen.NXObject Li): .
        """
        pass
class Library(ProfileObject): 
    """ Interface for Services Profile Library objects """
    def AddLibrary(self) -> Library:
        """
         Adds a Library 
         Returns newLib ( Library NXOpen):  the new library .
        """
        pass
    def AddNewBuildProfile(self) -> ProfileObject:
        """
         Adds a New Build Profile 
         Returns newProfile ( ProfileObject NXOpen):  the new profile .
        """
        pass
    def AddNewProfile(self) -> ProfileObject:
        """
         Deprecated 
         Returns newProfile ( ProfileObject NXOpen):  the new profile .
        """
        pass
    def AddProfile(self) -> ProfileLibrary:
        """
         Adds a Profile Library 
         Returns newProfileLib ( ProfileLibrary NXOpen):  the new profile library .
        """
        pass
    def AddProfileLibrary(self) -> Library:
        """
         Adds a Profile Library 
         Returns newProfileLib ( Library NXOpen):  the new profile library .
        """
        pass
    def AddSupportLibrary(self) -> Library:
        """
         Adds a Support Library 
         Returns newSupportLib ( Library NXOpen):  the new support library .
        """
        pass
    def GetChildLibraries(self) -> List[Library]:
        """
         Gets all the children Libraries  
         Returns libraries ( Library List[NXOp):  the libraries .
        """
        pass
    def GetChildProfiles(self) -> List[ProfileObject]:
        """
         Gets the children Profiles of the Library 
         Returns profiles ( ProfileObject List[NXOp):  the profiles .
        """
        pass
    def GetProfiles(self) -> List[ProfileLibrary]:
        """
         Returns all profiles in the library 
         Returns profiles ( ProfileLibrary List[NXOp):  the profiles .
        """
        pass
    def ImportNewProfile(self, mmcgFileName: str, profileName: str) -> bool:
        """
         Imports a New Profile 
         Returns importResult (bool): .
        """
        pass
    def ImportProfile(self, mmcfFileName: str) -> ProfileLibrary:
        """
         Import a profile from a file 
         Returns newProfileLib ( ProfileLibrary NXOpen):  the new imported profile library .
        """
        pass
    def RemoveLibrary(self, lib: Library) -> None:
        """
         Removes a library 
        """
        pass
    def RemoveProfile(self, lib: ProfileLibrary) -> None:
        """
         Removes a profile 
        """
        pass
import NXOpen
class ManifoldChecker(NXOpen.Object): 
    """ Interface for manifold checker """
    def GetMeshStatus(selectedObj: NXOpen.TaggedObject) -> MeshStatus:
        """
         Get mesh status of selected object 
         Returns meshStatus ( MeshStatus NXOpen):  Mesh Status.
        """
        pass
import NXOpen
class MergeSupportsBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.Support builder """
    @property
    def MergeSelection(self) -> SelectSupportList:
        """
        Getter for property: ( SelectSupportList NXOpen) MergeSelection
         Returns the merge selection   
            
         
        """
        pass
    @property
    def TargetSelection(self) -> SelectSupport:
        """
        Getter for property: ( SelectSupport NXOpen) TargetSelection
         Returns the target support selection   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class MeshProperties(NXOpen.Builder): 
    """ Represents a mesh properties builder """
    @property
    def MeshResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.DisplayResolutionBuilder) MeshResolution
         Returns the mesh resolution builder   
            
         
        """
        pass
    @property
    def ObjectSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ObjectSelection
         Returns the meshed object selection   
            
         
        """
        pass
    @property
    def PartSelection(self) -> SelectPartList:
        """
        Getter for property: ( SelectPartList NXOpen) PartSelection
         Returns the part selection   
            
         
        """
        pass
import NXOpen
class MeshStatus(NXOpen.TaggedObject): 
    """ Represents a Mfg.AM.MeshStatus."""
    class Type(Enum):
        """
        Members Include: 
         |Unchecked| 
         |Busy| 
         |Error| 
         |Warning| 
         |Ok| 
         |Sheet| 

        """
        Unchecked: int
        Busy: int
        Error: int
        Warning: int
        Ok: int
        Sheet: int
        @staticmethod
        def ValueOf(value: int) -> MeshStatus.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetMessage(self) -> str:
        """
         Get the mesh status message of the given object 
         Returns statusMessage (str): .
        """
        pass
    def GetStatusType(self) -> MeshStatus.Type:
        """
         Get the mesh status of the given object 
         Returns status ( MeshStatus.Type NXOpen): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Validate
class MovePartBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.MovePartBuilder. """
    class MoveObject(Enum):
        """
        Members Include: 
         |Geometry| 
         |Component| 

        """
        Geometry: int
        Component: int
        @staticmethod
        def ValueOf(value: int) -> MovePartBuilder.MoveObject:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MoveTypeOption(Enum):
        """
        Members Include: 
         |MoveOriginal|  move part 
         |CopyOriginal|  copy part

        """
        MoveOriginal: int
        CopyOriginal: int
        @staticmethod
        def ValueOf(value: int) -> MovePartBuilder.MoveTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Divisions(self) -> int:
        """
        Getter for property: (int) Divisions
         Returns the distance or angle divisions   
            
         
        """
        pass
    @Divisions.setter
    def Divisions(self, distanceOrAngleDivisions: int):
        """
        Setter for property: (int) Divisions
         Returns the distance or angle divisions   
            
         
        """
        pass
    @property
    def MoveType(self) -> MovePartBuilder.MoveTypeOption:
        """
        Getter for property: ( MovePartBuilder.MoveTypeOption NXOpen) MoveType
         Returns the move rotate result   
            
         
        """
        pass
    @MoveType.setter
    def MoveType(self, moveType: MovePartBuilder.MoveTypeOption):
        """
        Setter for property: ( MovePartBuilder.MoveTypeOption NXOpen) MoveType
         Returns the move rotate result   
            
         
        """
        pass
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    @NumberOfCopies.setter
    def NumberOfCopies(self, numCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    @property
    def ObjectToMoveObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ObjectToMoveObject
         Returns the objects to move-rotate   
            
         
        """
        pass
    @property
    def SelectionAndPlacement(self) -> NXOpen.Validate.SelectionAndPlacementBuilder:
        """
        Getter for property: ( NXOpen.Validate.SelectionAndPlacementBuilder) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    @property
    def TransformMotion(self) -> NXOpen.GeometricUtilities.ModlMotion:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ModlMotion) TransformMotion
         Returns the transform   
            
         
        """
        pass
import NXOpen
class Nester3D(NXOpen.Builder): 
    """ Interface for AM Nesting Dialog Builder """
    class Constraint(Enum):
        """
        Members Include: 
         |Free| 
         |FixedZDirection| 
         |FixedFloorPlane| 
         |Rotate180| 
         |FixedBottomAndXY| 
         |FixedRotation| 
         |Fixed| 

        """
        Free: int
        FixedZDirection: int
        FixedFloorPlane: int
        Rotate180: int
        FixedBottomAndXY: int
        FixedRotation: int
        Fixed: int
        @staticmethod
        def ValueOf(value: int) -> Nester3D.Constraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Interlocking(Enum):
        """
        Members Include: 
         |AllowInterlocks| 
         |AvoidTunnels| 
         |AvoidAllInterlocks| 

        """
        AllowInterlocks: int
        AvoidTunnels: int
        AvoidAllInterlocks: int
        @staticmethod
        def ValueOf(value: int) -> Nester3D.Interlocking:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NesterType(Enum):
        """
        Members Include: 
         |TwoD| 
         |ThreeD| 

        """
        TwoD: int
        ThreeD: int
        @staticmethod
        def ValueOf(value: int) -> Nester3D.NesterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RotationAngleType(Enum):
        """
        Members Include: 
         |Degree90| 
         |Degree45| 
         |Degree30| 
         |Degree15| 

        """
        Degree90: int
        Degree45: int
        Degree30: int
        Degree15: int
        @staticmethod
        def ValueOf(value: int) -> Nester3D.RotationAngleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Solution(Enum):
        """
        Members Include: 
         |OptimizeHeight| 
         |DistributeHeight| 
         |OptimizeSliceVolume| 
         |OptimizeHeightAndSliceVolume| 

        """
        OptimizeHeight: int
        DistributeHeight: int
        OptimizeSliceVolume: int
        OptimizeHeightAndSliceVolume: int
        @staticmethod
        def ValueOf(value: int) -> Nester3D.Solution:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Accuracy(self) -> float:
        """
        Getter for property: (float) Accuracy
         Returns the accuracy   
            
         
        """
        pass
    @Accuracy.setter
    def Accuracy(self, accuracy: float):
        """
        Setter for property: (float) Accuracy
         Returns the accuracy   
            
         
        """
        pass
    @property
    def BottomDistance(self) -> float:
        """
        Getter for property: (float) BottomDistance
         Returns the spacing between parts   
            
         
        """
        pass
    @BottomDistance.setter
    def BottomDistance(self, bottomDistance: float):
        """
        Setter for property: (float) BottomDistance
         Returns the spacing between parts   
            
         
        """
        pass
    @property
    def ConstraintType(self) -> Nester3D.Constraint:
        """
        Getter for property: ( Nester3D.Constraint NXOpen) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraint: Nester3D.Constraint):
        """
        Setter for property: ( Nester3D.Constraint NXOpen) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    @property
    def InterlockingType(self) -> Nester3D.Interlocking:
        """
        Getter for property: ( Nester3D.Interlocking NXOpen) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    @InterlockingType.setter
    def InterlockingType(self, interlockingType: Nester3D.Interlocking):
        """
        Setter for property: ( Nester3D.Interlocking NXOpen) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    @property
    def NestingType(self) -> Nester3D.NesterType:
        """
        Getter for property: ( Nester3D.NesterType NXOpen) NestingType
         Returns the nesting type   
            
         
        """
        pass
    @NestingType.setter
    def NestingType(self, nestingType: Nester3D.NesterType):
        """
        Setter for property: ( Nester3D.NesterType NXOpen) NestingType
         Returns the nesting type   
            
         
        """
        pass
    @property
    def PartsToNest(self) -> SelectPartList:
        """
        Getter for property: ( SelectPartList NXOpen) PartsToNest
         Returns the parts to nest   
            
         
        """
        pass
    @property
    def RotationAngle(self) -> Nester3D.RotationAngleType:
        """
        Getter for property: ( Nester3D.RotationAngleType NXOpen) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: Nester3D.RotationAngleType):
        """
        Setter for property: ( Nester3D.RotationAngleType NXOpen) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    @property
    def SolutionType(self) -> Nester3D.Solution:
        """
        Getter for property: ( Nester3D.Solution NXOpen) SolutionType
         Returns the solution type   
            
         
        """
        pass
    @SolutionType.setter
    def SolutionType(self, solutionType: Nester3D.Solution):
        """
        Setter for property: ( Nester3D.Solution NXOpen) SolutionType
         Returns the solution type   
            
         
        """
        pass
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns the spacing between parts   
            
         
        """
        pass
    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns the spacing between parts   
            
         
        """
        pass
    @property
    def StartFromEmptyBuildtray(self) -> bool:
        """
        Getter for property: (bool) StartFromEmptyBuildtray
         Returns the StartFromEmptyBuildtray   
            
         
        """
        pass
    @StartFromEmptyBuildtray.setter
    def StartFromEmptyBuildtray(self, startFromEmptyBuildtray: bool):
        """
        Setter for property: (bool) StartFromEmptyBuildtray
         Returns the StartFromEmptyBuildtray   
            
         
        """
        pass
    @property
    def StopAfter(self) -> int:
        """
        Getter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    @StopAfter.setter
    def StopAfter(self, stopAfter: int):
        """
        Setter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    @property
    def TargetDensity(self) -> float:
        """
        Getter for property: (float) TargetDensity
         Returns the targetDensity   
            
         
        """
        pass
    @TargetDensity.setter
    def TargetDensity(self, targetDensity: float):
        """
        Setter for property: (float) TargetDensity
         Returns the targetDensity   
            
         
        """
        pass
    @property
    def ViewProgress(self) -> bool:
        """
        Getter for property: (bool) ViewProgress
         Returns the view progress   
            
         
        """
        pass
    @ViewProgress.setter
    def ViewProgress(self, viewProgress: bool):
        """
        Setter for property: (bool) ViewProgress
         Returns the view progress   
            
         
        """
        pass
    @property
    def WallDistance(self) -> float:
        """
        Getter for property: (float) WallDistance
         Returns the spacing between parts   
            
         
        """
        pass
    @WallDistance.setter
    def WallDistance(self, wallDistance: float):
        """
        Setter for property: (float) WallDistance
         Returns the spacing between parts   
            
         
        """
        pass
    def ExecuteNesting(self) -> NestingStatus:
        """
         Execute the Nesting 
         Returns nestStatus ( NestingStatus NXOpen):  Nesting Status.
        """
        pass
    @overload
    def SetNesting(self, dLength: float, dWidth: float, dHeight: float) -> None:
        """
         Sets the (sub) nesting box 
        """
        pass
    @overload
    def SetNesting(self, dDiameter: float, dHeight: float) -> None:
        """
         Sets the (sub) nesting cylinder 
        """
        pass
import NXOpen
class NestingStatus(NXOpen.TransientObject): 
    """ Nesting Status  """
    def Dispose(self) -> None:
        """
         Free the handle to the Nesting Status 
        """
        pass
    def GetDensity(self) -> float:
        """
         Get the density 
         Returns density (float): .
        """
        pass
    def GetErrorCode(self) -> int:
        """
         Get the error code 
         Returns errorCode (int): .
        """
        pass
    def GetNestedHeight(self) -> float:
        """
         Get the nested height 
         Returns nestingHeight (float): .
        """
        pass
    def GetNestedLength(self) -> float:
        """
         Get the nested Length 
         Returns nestingLength (float): .
        """
        pass
    def GetNestedParts(self) -> List[Part]:
        """
         Get the nested part 
         Returns tagPart ( Part List[NXOp):  AM Parts .
        """
        pass
    def GetNestedWidth(self) -> float:
        """
         Get the nested Width 
         Returns nestingWidth (float): .
        """
        pass
    def GetNotNestedParts(self) -> List[Part]:
        """
         Get the non nested part 
         Returns tagPart ( Part List[NXOp):  AM Parts .
        """
        pass
import NXOpen
class NoBuildZoneBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.NoBuildZoneBuilder. """
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedObjects
         Returns the selected objects   
            
         
        """
        pass
import NXOpen
class PartGroup(NXOpen.DisplayableObject): 
    """ Interface for Part Group objects """
    def Add(self, children: List[Part]) -> None:
        """
         Adds parts to this group. 
        """
        pass
    def AddObject(self, children: List[NXOpen.DisplayableObject]) -> None:
        """
         Adds objects to this group. 
        """
        pass
    def Disassemble(self) -> None:
        """
         Converts the assembly group into a regular group so the members can be moved arround. If the group is not an assembly this method has no effect. 
        """
        pass
    def GetChildren(self) -> List[Part]:
        """
         Returns the parts in this group. 
         Returns children ( Part List[NXOp):  the member parts.
        """
        pass
    def GetDistanceFromPart(self) -> float:
        """
         Gets the distance from part from the part group 
         Returns distanceFromPart (float): .
        """
        pass
    def GetInterlocking(self) -> Part.InterlockingType:
        """
         Gets the intertlocking type from the part 
         Returns intertlockingType ( Part.InterlockingType NXOpen): .
        """
        pass
    def GetNestingConstraint(self) -> Part.NestingConstraintType:
        """
         Gets the nesting constraint type from the part 
         Returns nestingConstraintType ( Part.NestingConstraintType NXOpen): .
        """
        pass
    def GetRotationAngle(self) -> Part.RotationAngleType:
        """
         Gets the rotation angle from the part 
         Returns rotationAngle ( Part.RotationAngleType NXOpen): .
        """
        pass
    def IsAssembly(self) -> bool:
        """
         Checks if the goup is an assembly group or not 
         Returns bIsAssembly (bool): .
        """
        pass
    def IsLocked(self) -> bool:
        """
         Checks if the group is locked for individual position andor orientation changes. 
         Returns bIsLocked (bool): .
        """
        pass
    def Lock(self) -> None:
        """
         Locks the group members for individual position andor orientation changes. 
        """
        pass
    def Reassemble(self) -> None:
        """
         Resets the group to an assembly group if possible. All assembly contraints (if any) are reapplied.
        """
        pass
    def Remove(self, children: List[NXOpen.DisplayableObject]) -> None:
        """
         Removes the selected part from the group and adds it to the buildtray
        """
        pass
    def ReorderParts(self, objectsToReorder: List[NXOpen.DisplayableObject], anchor: NXOpen.DisplayableObject, reorderBefore: bool) -> None:
        """
         Sets the print order by moving parts or part groups before or after anchor part
        """
        pass
    def SetDistanceFromPart(self, distanceFromPart: float) -> None:
        """
         Sets the distance from part to the part group
        """
        pass
    def SetInterlocking(self, intertlockingType: Part.InterlockingType) -> None:
        """
         Sets the intertlocking type on the part 
        """
        pass
    def SetNestingConstraint(self, nestingConstraintType: Part.NestingConstraintType) -> None:
        """
         Sets the nesting constraint type on the part 
        """
        pass
    def SetRotationAngle(self, rotationAngle: Part.RotationAngleType) -> None:
        """
         Sets the rotation angle on the part 
        """
        pass
    def Ungroup(self) -> None:
        """
         Removes all parts from the group  and deletes the group. After calling this method the reference to the group has become invalid.
        """
        pass
    def Unlock(self) -> None:
        """
         Unlocks the group members for individual position andor orientation changes. 
        """
        pass
import NXOpen
class PartRegion(NXOpen.DisplayableObject): 
    """ Interface for Model Part objects """
    def ClearBuildStrategyValues(self) -> None:
        """
         Clear BuildStrategy values
        """
        pass
    def CreateSupportBuilder(self) -> SupportBuilder:
        """
         Create support builder object 
         Returns tagBuilder ( SupportBuilder NXOpen):   the support builder .
        """
        pass
    def CreateSupports(self) -> List[Support]:
        """
         Create the supports for the part region 
         Returns supports ( Support List[NXOp): .
        """
        pass
    def GetBuildStrategyValues(self) -> Tuple[List[str], List[str]]:
        """
         Get BuildStrategy values
         Returns A tuple consisting of (buildStrategyNames, buildStrategyValues). 
         - buildStrategyNames is: List[str]. the list of buildStrategy names .
         - buildStrategyValues is: List[str]. the list of buildStrategy values .

        """
        pass
    def GetDimensions(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the dimensions for the part region 
         Returns A tuple consisting of (ptMin, ptMax). 
         - ptMin is:  NXOpen.Point3d.
         - ptMax is:  NXOpen.Point3d.

        """
        pass
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the geometry of the part.  Can be solid, facet or convergent objects. 
         Returns geometry ( NXOpen.DisplayableObject Li): .
        """
        pass
    def GetSupports(self) -> List[Support]:
        """
         Gets all the supports in the part 
         Returns supports ( Support List[NXOp): .
        """
        pass
    def RemoveAllSupports(self) -> None:
        """
         Removes all the supports from the part 
        """
        pass
    def RemoveSupport(self, support: Support) -> None:
        """
         Removes the support from the part 
        """
        pass
    def ReorderSupports(self, supportsToReorder: List[Support], anchor: Support, reorderBefore: bool) -> None:
        """
         Sets the print order by moving supports before or after an anchor support
        """
        pass
    def SetBuildStrategyValues(self, buildStrategyNames: List[str], buildStrategyValues: List[str]) -> None:
        """
         Set BuildStrategy values
        """
        pass
    def SetDefaultProfile(self, tagProfile: Profile) -> None:
        """
         Sets the given profile as the default profile on the part region 
        """
        pass
    def SetSupportProfile(self, tagSupportProfile: SupportProfile) -> None:
        """
         Sets the given profile as the default profile on the part 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
class Part(NXOpen.DisplayableObject): 
    """ Interface for Model Part objects """
    class InterlockingType(Enum):
        """
        Members Include: 
         |Undefined| 
         |Allowinterlocks| 
         |Avoidtunnels| 
         |Avoidallinterlocks| 

        """
        Undefined: int
        Allowinterlocks: int
        Avoidtunnels: int
        Avoidallinterlocks: int
        @staticmethod
        def ValueOf(value: int) -> Part.InterlockingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NestingConstraintType(Enum):
        """
        Members Include: 
         |Undefined| 
         |Free| 
         |FixZDirection| 
         |FixBottomPlane| 
         |Rotate180| 
         |FixBottomAndXy| 
         |FixRotation| 
         |Fixed| 

        """
        Undefined: int
        Free: int
        FixZDirection: int
        FixBottomPlane: int
        Rotate180: int
        FixBottomAndXy: int
        FixRotation: int
        Fixed: int
        @staticmethod
        def ValueOf(value: int) -> Part.NestingConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RotationAngleType(Enum):
        """
        Members Include: 
         |Undefined| 
         |Degree90| 
         |Degree45| 
         |Degree30| 
         |Degree15| 

        """
        Undefined: int
        Degree90: int
        Degree45: int
        Degree30: int
        Degree15: int
        @staticmethod
        def ValueOf(value: int) -> Part.RotationAngleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def ClearBuildStrategyValues(self) -> None:
        """
         Clear BuildStrategy values
        """
        pass
    def CreateSupportBuilder(self) -> SupportBuilder:
        """
         Create support builder object 
         Returns tagBuilder ( SupportBuilder NXOpen):   the support builder .
        """
        pass
    def CreateSupports(self) -> List[Support]:
        """
         Create the supports for the part 
         Returns supports ( Support List[NXOp): .
        """
        pass
    def GetBuildStrategyValues(self) -> Tuple[List[str], List[str]]:
        """
         Get BuildStrategy values
         Returns A tuple consisting of (buildStrategyNames, buildStrategyValues). 
         - buildStrategyNames is: List[str]. the list of buildStrategy names .
         - buildStrategyValues is: List[str]. the list of buildStrategy values .

        """
        pass
    def GetComponent(self) -> NXOpen.Assemblies.Component:
        """
         Returns the assembly component of the part 
         Returns tagComponent ( NXOpen.Assemblies.Component):   the assembly component .
        """
        pass
    def GetDimensions(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the dimensions for the part  
         Returns A tuple consisting of (ptMin, ptMax). 
         - ptMin is:  NXOpen.Point3d.
         - ptMax is:  NXOpen.Point3d.

        """
        pass
    def GetDistanceFromPart(self) -> float:
        """
         Gets the distance from the part 
         Returns distanceFromPart (float): .
        """
        pass
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the geometry of the part.  Can be solid, facet or convergent objects. 
         Returns geometry ( NXOpen.DisplayableObject Li): .
        """
        pass
    def GetGroup(self) -> NXOpen.DisplayableObject:
        """
         Returns the group the part is in
         Returns tagGroup ( NXOpen.DisplayableObject): .
        """
        pass
    def GetInterlocking(self) -> Part.InterlockingType:
        """
         Gets the intertlocking type from the part 
         Returns intertlockingType ( Part.InterlockingType NXOpen): .
        """
        pass
    def GetNestingConstraint(self) -> Part.NestingConstraintType:
        """
         Gets the nesting constraint type from the part 
         Returns nestingConstraintType ( Part.NestingConstraintType NXOpen): .
        """
        pass
    def GetPartRegions(self) -> List[PartRegion]:
        """
         Returns the part regions of this part 
         Returns partRegions ( PartRegion List[NXOp): .
        """
        pass
    def GetPattern(self) -> NXOpen.Features.Feature:
        """
         Returns the pattern feature of this part (if any) 
         Returns tagPattern ( NXOpen.Features.Feature): .
        """
        pass
    def GetPatternInstances(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the Pattern Instances Of Part 
         Returns patternInstances ( NXOpen.DisplayableObject Li): .
        """
        pass
    def GetRotationAngle(self) -> Part.RotationAngleType:
        """
         Gets the rotation angle from the part 
         Returns rotationAngle ( Part.RotationAngleType NXOpen): .
        """
        pass
    def GetSerialNumbers(self) -> List[SerialNumber]:
        """
         Returns the serial numbers of this part (if any) 
         Returns serialNumbers ( SerialNumber List[NXOp): .
        """
        pass
    def GetSupports(self) -> List[Support]:
        """
         Gets all the supports in the part 
         Returns supports ( Support List[NXOp): .
        """
        pass
    def RemoveAllSupports(self) -> None:
        """
         Removes all the supports from the part 
        """
        pass
    def RemoveSupport(self, support: Support) -> None:
        """
         Removes the support from the part 
        """
        pass
    def SetBuildStrategyValues(self, buildStrategyNames: List[str], buildStrategyValues: List[str]) -> None:
        """
         Set BuildStrategy values
        """
        pass
    def SetDefaultProfile(self, tagProfile: Profile) -> None:
        """
         Sets the given profile as the default profile on the part 
        """
        pass
    def SetDistanceFromPart(self, distanceFromPart: float) -> None:
        """
         Sets the distance from part on the part 
        """
        pass
    def SetInterlocking(self, intertlockingType: Part.InterlockingType) -> None:
        """
         Sets the intertlocking type on the part 
        """
        pass
    def SetNestingConstraint(self, nestingConstraintType: Part.NestingConstraintType) -> None:
        """
         Sets the nesting constraint type on the part 
        """
        pass
    def SetRotationAngle(self, rotationAngle: Part.RotationAngleType) -> None:
        """
         Sets the rotation angle on the part 
        """
        pass
    def SetSupportProfile(self, tagSupportProfile: SupportProfile) -> None:
        """
         Sets the given profile as the default profile on the part 
        """
        pass
    def Ungroup(self) -> None:
        """
         Removes the part from the group it is in
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PatternAMPartBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.PatternAMPartBuilder. """
    class PatternType(Enum):
        """
        Members Include: 
         |Component| 
         |Geometry| 

        """
        Component: int
        Geometry: int
        @staticmethod
        def ValueOf(value: int) -> PatternAMPartBuilder.PatternType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative option   
            
         
        """
        pass
    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative option   
            
         
        """
        pass
    @property
    def CopyThreads(self) -> bool:
        """
        Getter for property: (bool) CopyThreads
         Returns the copy Threads   
            
         
        """
        pass
    @CopyThreads.setter
    def CopyThreads(self, copyThreads: bool):
        """
        Setter for property: (bool) CopyThreads
         Returns the copy Threads   
            
         
        """
        pass
    @property
    def DynamicPosition(self) -> bool:
        """
        Getter for property: (bool) DynamicPosition
         Returns the dynamic Position   
            
         
        """
        pass
    @DynamicPosition.setter
    def DynamicPosition(self, dynamicPosition: bool):
        """
        Setter for property: (bool) DynamicPosition
         Returns the dynamic Position   
            
         
        """
        pass
    @property
    def GeometryPatternDefinition(self) -> NXOpen.GeometricUtilities.PatternDefinition:
        """
        Getter for property: ( NXOpen.GeometricUtilities.PatternDefinition) GeometryPatternDefinition
         Returns the Pattern Defintion service for pattern geometry   
            
         
        """
        pass
    @property
    def PartSelected(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PartSelected
         Returns the methods gets the selected part   
            
         
        """
        pass
    @property
    def PatternDefinition(self) -> NXOpen.GeometricUtilities.PatternDefinition:
        """
        Getter for property: ( NXOpen.GeometricUtilities.PatternDefinition) PatternDefinition
         Returns the Pattern Defintion service   
            
         
        """
        pass
    @property
    def PatternOptionType(self) -> PatternAMPartBuilder.PatternType:
        """
        Getter for property: ( PatternAMPartBuilder.PatternType NXOpen) PatternOptionType
         Returns the pattern type   
            
         
        """
        pass
    @PatternOptionType.setter
    def PatternOptionType(self, patternType: PatternAMPartBuilder.PatternType):
        """
        Setter for property: ( PatternAMPartBuilder.PatternType NXOpen) PatternOptionType
         Returns the pattern type   
            
         
        """
        pass
    @property
    def ReferencePoint(self) -> NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder) ReferencePoint
         Returns the reference point service.  
          
                    It contains the point of reference that will be used as the origin for creating pattern based transformations.   
         
        """
        pass
import NXOpen
class PrinterManager(NXOpen.Object): 
    """ Represents the Additive Manufacturing Printer Service """
    def GetPrinter(printerName: str) -> Printer:
        """
         Retrieves a printer by name 
         Returns pPrinter ( Printer NXOpen): .
        """
        pass
    def GetPrinters() -> List[Printer]:
        """
         Retrieves the available 3D printers 
         Returns pPrinter ( Printer List[NXOp): .
        """
        pass
import NXOpen
class Printer(NXOpen.TransientObject): 
    """ Printer """
    def Dispose(self) -> None:
        """
         Free the handle to the printer 
        """
        pass
    def GetDimensions(self) -> Tuple[bool, float, float, float, float, float]:
        """
         Gets the printer build tray dimensions 
         Returns A tuple consisting of (isBox, dLength, dWidth, dDiameter, dHeight, dTrayHeight). 
         - isBox is: bool.
         - dLength is: float.
         - dWidth is: float.
         - dDiameter is: float.
         - dHeight is: float.
         - dTrayHeight is: float.

        """
        pass
    def GetIdentifier(self) -> str:
        """
         Returns the printer identifier 
         Returns printerId (str):  .
        """
        pass
    def GetName(self) -> str:
        """
         Returns the printer name 
         Returns printerName (str):  .
        """
        pass
    def GetOrigin(self) -> NXOpen.Point3d:
        """
         Gets the printer build tray origin 
         Returns origin ( NXOpen.Point3d): .
        """
        pass
    def GetStatus(self) -> str:
        """
         Returns the printer status 
         Returns printerStatus (str):  .
        """
        pass
import NXOpen
class PrintJob(NXOpen.TransientObject): 
    """ Print Job  """
    def Dispose(self) -> None:
        """
         Free the handle to the print job 
        """
        pass
    def GetStatusMessage(self) -> str:
        """
         Returns the status message string 
         Returns statusMessage (str):  .
        """
        pass
import NXOpen
class ProfileLibrary(Library): 
    """ Interface for Services Profile Library objects """
    @property
    def Active(self) -> SupportProfile:
        """
        Getter for property: ( SupportProfile NXOpen) Active
         Returns the active support profile   
            
         
        """
        pass
    @Active.setter
    def Active(self, profile: SupportProfile):
        """
        Setter for property: ( SupportProfile NXOpen) Active
         Returns the active support profile   
            
         
        """
        pass
    def AddSupportProfile(self) -> SupportProfile:
        """
         Adds a profile to the library 
         Returns newProfile ( SupportProfile NXOpen):  the new support profile .
        """
        pass
    def DeleteLibraryFolder(self, pChildProfileLib: ProfileLibrary) -> None:
        """
         Remove a Library component from the Profile Library
        """
        pass
    def DeleteProfile(self, pChildProfile: Profile) -> None:
        """
         Remove a Profile component from the Profile Library
        """
        pass
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Find a profile by its recorded id
         Returns found ( NXOpen.INXObject):  Object found, or null if no such partfeature exists.
        """
        pass
    def GetSupportProfiles(self) -> List[SupportProfile]:
        """
         Gets the children Profile Objects of the Profile Library 
         Returns profiles ( SupportProfile List[NXOp):  the profiles .
        """
        pass
    def Remove(self, profile: SupportProfile) -> None:
        """
         Remove a support profile
        """
        pass
import NXOpen
class ProfileObject(NXOpen.NXObject): 
    """ Interface for Services Profile objects """
    def Destroy(self) -> None:
        """
         Deletes the profile object
        """
        pass
    def GetChild(self, childSupportName: str) -> ProfileObject:
        """
         Get child profile object of the given name 
         Returns pParentLib ( ProfileObject NXOpen): .
        """
        pass
    def GetChildByGuid(self, pChildGuid: str, recursive: bool) -> ProfileObject:
        """
         Finds the NXOpen.Mfg.AM.ProfileObject with the given (guid) identifier as recorded in a journal.
                    This method will search for the profile with given GUID from the given profile object. 
                    The GUID used for the searching is available in the am.xml file.
         Returns pParentLib ( ProfileObject NXOpen): .
        """
        pass
    def RenameProfileObject(self, newPropertyName: str) -> None:
        """
         Renames the profile object
        """
        pass
class ProfileSupport(ProfileObject): 
    """ Interface for Services Profile Library objects """
    def SetAsDefault(self) -> None:
        """
         Sets the default profile support within the support library. 
        """
        pass
class Profile(ProfileObject): 
    """ Interface for Services Profile objects """
    def GetChildSupport(self, childSupportName: str) -> ProfileObject:
        """
         Get child profile object support of the given Profile
         Returns pParentLib ( ProfileObject NXOpen):  .
        """
        pass
    def GetLibrary(self) -> ProfileObject:
        """
         Get parent library of the given Profile
         Returns pParentLib ( ProfileObject NXOpen):  .
        """
        pass
    def GetName(self) -> str:
        """
         Get the Profile Name
         Returns profileName (str):  .
        """
        pass
    def GetProfiles(self) -> List[Profile]:
        """
         Gets the Profile children
         Returns childrenProfile ( Profile List[NXOp):  .
        """
        pass
    def SetName(self, newName: str) -> None:
        """
         Set the name of the Profile 
        """
        pass
import NXOpen
class RepositionPartBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.RepositionPartBuilder. """
    class Method(Enum):
        """
        Members Include: 
         |Rotate|  rotate 
         |Translate|  translate  
         |Align|  align 

        """
        Rotate: int
        Translate: int
        Align: int
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RotateAxisType(Enum):
        """
        Members Include: 
         |X|  XC-axis 
         |Y|  YC-axis 
         |Z|  ZC-axis 
         |NegativeX|  -XC-axis 
         |NegativeY|  -YC-axis 
         |NegativeZ|  -ZC-axis 
         |Dynamic|  Dynamic 
         |Viewdirection|  View Direction 

        """
        X: int
        Y: int
        Z: int
        NegativeX: int
        NegativeY: int
        NegativeZ: int
        Dynamic: int
        Viewdirection: int
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.RotateAxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TranslatePartsType(Enum):
        """
        Members Include: 
         |OneByOne|  One by one 
         |AsAGroup|  As a group 

        """
        OneByOne: int
        AsAGroup: int
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.TranslatePartsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TranslateToType(Enum):
        """
        Members Include: 
         |BuildPlate|  Build Plate 
         |BuildTrayCenter|  Build Tray Center 
         |FaceOrPlane|  Planar object - Face or plane 

        """
        BuildPlate: int
        BuildTrayCenter: int
        FaceOrPlane: int
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.TranslateToType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Angle
         Returns the angle   
            
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance   
            
         
        """
        pass
    @property
    def ManipulatorOffsetOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) ManipulatorOffsetOrigin
         Returns the offset origin point of manipulator   
            
         
        """
        pass
    @ManipulatorOffsetOrigin.setter
    def ManipulatorOffsetOrigin(self, manipulatorOrigin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) ManipulatorOffsetOrigin
         Returns the offset origin point of manipulator   
            
         
        """
        pass
    @property
    def ManipulatorRotationMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) ManipulatorRotationMatrix
         Returns the rotation matrix of manipulator   
            
         
        """
        pass
    @ManipulatorRotationMatrix.setter
    def ManipulatorRotationMatrix(self, manipulatorMatrix: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) ManipulatorRotationMatrix
         Returns the rotation matrix of manipulator   
            
         
        """
        pass
    @property
    def ObjectsToReposition(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) ObjectsToReposition
         Returns the objects to reposition   
            
         
        """
        pass
    @property
    def PartFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PartFaces
         Returns the part face selection   
            
         
        """
        pass
    @property
    def PlanarObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PlanarObject
         Returns the planar object selection   
            
         
        """
        pass
    @property
    def PositionMethod(self) -> RepositionPartBuilder.Method:
        """
        Getter for property: ( RepositionPartBuilder.Method NXOpen) PositionMethod
         Returns the position type   
            
         
        """
        pass
    @PositionMethod.setter
    def PositionMethod(self, positionMethod: RepositionPartBuilder.Method):
        """
        Setter for property: ( RepositionPartBuilder.Method NXOpen) PositionMethod
         Returns the position type   
            
         
        """
        pass
    @property
    def RotationAxisType(self) -> RepositionPartBuilder.RotateAxisType:
        """
        Getter for property: ( RepositionPartBuilder.RotateAxisType NXOpen) RotationAxisType
         Returns the rotation axis   
            
         
        """
        pass
    @RotationAxisType.setter
    def RotationAxisType(self, rotationAxis: RepositionPartBuilder.RotateAxisType):
        """
        Setter for property: ( RepositionPartBuilder.RotateAxisType NXOpen) RotationAxisType
         Returns the rotation axis   
            
         
        """
        pass
    @property
    def TranslatePartsOption(self) -> RepositionPartBuilder.TranslatePartsType:
        """
        Getter for property: ( RepositionPartBuilder.TranslatePartsType NXOpen) TranslatePartsOption
         Returns the reference point   
            
         
        """
        pass
    @TranslatePartsOption.setter
    def TranslatePartsOption(self, referencePoint: RepositionPartBuilder.TranslatePartsType):
        """
        Setter for property: ( RepositionPartBuilder.TranslatePartsType NXOpen) TranslatePartsOption
         Returns the reference point   
            
         
        """
        pass
    @property
    def TranslateToOption(self) -> RepositionPartBuilder.TranslateToType:
        """
        Getter for property: ( RepositionPartBuilder.TranslateToType NXOpen) TranslateToOption
         Returns the reference object   
            
         
        """
        pass
    @TranslateToOption.setter
    def TranslateToOption(self, referenceObject: RepositionPartBuilder.TranslateToType):
        """
        Setter for property: ( RepositionPartBuilder.TranslateToType NXOpen) TranslateToOption
         Returns the reference object   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectPartList(NXOpen.TaggedObject): 
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
    def Add(self, objectValue: Part) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[Part], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[Part]) -> bool:
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
    def Add(self, selection: Part, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Part, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Part, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: Part, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
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
    def Contains(self, objectValue: Part) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[Part]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( Part List[NXOp):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: Part) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[Part]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: Part, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Part, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Part, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def SetArray(self, objects: List[Part]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectSupportList(NXOpen.TaggedObject): 
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
    def Add(self, objectValue: Support) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[Support], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[Support]) -> bool:
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
    def Add(self, selection: Support, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Support, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Support, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: Support, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
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
    def Contains(self, objectValue: Support) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[Support]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( Support List[NXOp):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: Support) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[Support]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: Support, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Support, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Support, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def SetArray(self, objects: List[Support]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectSupport(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Support:
        """
        Getter for property: ( Support NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Support):
        """
        Setter for property: ( Support NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Support, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Support NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Support, NXOpen.View, NXOpen.Point3d, Support, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Support NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Support NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[Support, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  Support NXOpen. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: Support, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Support, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Support, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: Support, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
class SerialNumber(PartRegion): 
    """ Interface for Model Build Tray objects """
    def Clear(self) -> None:
        """
         Clear 
        """
        pass
    def Generate(self) -> None:
        """
         Generate 
        """
        pass
    def GetText(self) -> str:
        """
         Get Serial Number Text 
         Returns printMarkText (str): .
        """
        pass
    def GetUsageLabel(self) -> str:
        """
         Get Usable Label of Serial Number 
         Returns usageLabel (str): .
        """
        pass
    def SetText(self, printMarkText: str) -> None:
        """
         Set Serial Number Text 
        """
        pass
import NXOpen
class SimSupportBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.SimulationSupport builder """
    @property
    def Supports(self) -> SelectSupportList:
        """
        Getter for property: ( SelectSupportList NXOpen) Supports
         Returns the support selection   
            
         
        """
        pass
    def GetFailedFaces(self) -> List[NXOpen.Face]:
        """
         Get the faces that failed during the support generation 
         Returns pptFailedFaces ( NXOpen.Face Li): .
        """
        pass
import NXOpen
class SimulationSupport(NXOpen.NXObject): 
    """ Additive Manufacturing Surface Region """
    def GetBodies(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the simulation support geometry 
         Returns bodies ( NXOpen.DisplayableObject Li): .
        """
        pass
    def GetPartBody(self) -> NXOpen.DisplayableObject:
        """
         Returns the part body for this support 
         Returns tagGeometry ( NXOpen.DisplayableObject): .
        """
        pass
    def IsOutOfDate(self) -> bool:
        """
         Returns true if the simulation support is out of date 
         Returns outOfDate (bool): .
        """
        pass
    def SetBodies(self, bodies: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the simulation support geometry 
        """
        pass
import NXOpen
class SinterboxBuilder(NXOpen.Builder): 
    """ Used to create or edit a Mfg.AM.Sinterbox """
    @property
    def AlignType(self) -> Sinterbox.AlignmentType:
        """
        Getter for property: ( Sinterbox.AlignmentType NXOpen) AlignType
         Returns the alignment of sinterbox   
            
         
        """
        pass
    @AlignType.setter
    def AlignType(self, alignmentType: Sinterbox.AlignmentType):
        """
        Setter for property: ( Sinterbox.AlignmentType NXOpen) AlignType
         Returns the alignment of sinterbox   
            
         
        """
        pass
    @property
    def BoundaryType(self) -> Sinterbox.Boundary:
        """
        Getter for property: ( Sinterbox.Boundary NXOpen) BoundaryType
         Returns the boundary type   
            
         
        """
        pass
    @BoundaryType.setter
    def BoundaryType(self, boundary: Sinterbox.Boundary):
        """
        Setter for property: ( Sinterbox.Boundary NXOpen) BoundaryType
         Returns the boundary type   
            
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color of sinterbox   
            
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color of sinterbox   
            
         
        """
        pass
    @property
    def EdgeBlendValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EdgeBlendValue
         Returns the edge blend value   
            
         
        """
        pass
    @property
    def LatticeType(self) -> Sinterbox.Lattice:
        """
        Getter for property: ( Sinterbox.Lattice NXOpen) LatticeType
         Returns the lattice type   
            
         
        """
        pass
    @LatticeType.setter
    def LatticeType(self, lattice: Sinterbox.Lattice):
        """
        Setter for property: ( Sinterbox.Lattice NXOpen) LatticeType
         Returns the lattice type   
            
         
        """
        pass
    @property
    def PartOffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PartOffsetDistance
         Returns the part offset distance   
            
         
        """
        pass
    @property
    def Parts(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) Parts
         Returns the selection parts   
            
         
        """
        pass
    @property
    def RodDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RodDiameter
         Returns the rod diameter   
            
         
        """
        pass
    @property
    def RodLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RodLength
         Returns the rod length   
            
         
        """
        pass
    @property
    def RodWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RodWidth
         Returns the rod width   
            
         
        """
        pass
    @property
    def ShapeType(self) -> Sinterbox.Shape:
        """
        Getter for property: ( Sinterbox.Shape NXOpen) ShapeType
         Returns the shape type   
            
         
        """
        pass
    @ShapeType.setter
    def ShapeType(self, shape: Sinterbox.Shape):
        """
        Setter for property: ( Sinterbox.Shape NXOpen) ShapeType
         Returns the shape type   
            
         
        """
        pass
class Sinterbox(PartGroup): 
    """ Represents a Mfg.AM.Sinterbox."""
    class AlignmentType(Enum):
        """
        Members Include: 
         |Free| 
         |BuildTray| 

        """
        Free: int
        BuildTray: int
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.AlignmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Boundary(Enum):
        """
        Members Include: 
         |PartSelection| 
         |IndividualParts| 

        """
        PartSelection: int
        IndividualParts: int
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.Boundary:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Lattice(Enum):
        """
        Members Include: 
         |GridAndRod| 
         |Standard| 
         |Voronoi| 

        """
        GridAndRod: int
        Standard: int
        Voronoi: int
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.Lattice:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Shape(Enum):
        """
        Members Include: 
         |Box| 
         |Freeform| 

        """
        Box: int
        Freeform: int
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.Shape:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetBuildStrategyValues(self) -> Tuple[List[str], List[str]]:
        """
         Get BuildStrategy values
         Returns A tuple consisting of (buildStrategyNames, buildStrategyValues). 
         - buildStrategyNames is: List[str]. the list of buildStrategy names .
         - buildStrategyValues is: List[str]. the list of buildStrategy values .

        """
        pass
    def SetBuildStrategyValues(self, buildStrategyNames: List[str], buildStrategyValues: List[str]) -> None:
        """
         Set BuildStrategy values
        """
        pass
import NXOpen
import NXOpen.Features
class Sketcher(NXOpen.Builder): 
    """ Represents a Mfg.AM.Sketcher builder """
    class Mode(Enum):
        """
        Members Include: 
         |SurfaceFace| 
         |SurfaceLine| 
         |SketchFace| 
         |SketchLine| 

        """
        SurfaceFace: int
        SurfaceLine: int
        SketchFace: int
        SketchLine: int
        @staticmethod
        def ValueOf(value: int) -> Sketcher.Mode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CloseCurve(self) -> bool:
        """
        Getter for property: (bool) CloseCurve
         Returns the flag indicating if curve should be closed   
            
         
        """
        pass
    @CloseCurve.setter
    def CloseCurve(self, bCloseCurve: bool):
        """
        Setter for property: (bool) CloseCurve
         Returns the flag indicating if curve should be closed   
            
         
        """
        pass
    @property
    def CurveOnSurfaceBuilder(self) -> NXOpen.Features.CurveOnSurfaceBuilder:
        """
        Getter for property: ( NXOpen.Features.CurveOnSurfaceBuilder) CurveOnSurfaceBuilder
         Returns the Curve On Surface feature builder   
            
         
        """
        pass
    @property
    def Sketch(self) -> NXOpen.Sketch:
        """
        Getter for property: ( NXOpen.Sketch) Sketch
         Returns the sketch which holds the section curves   
            
         
        """
        pass
    @Sketch.setter
    def Sketch(self, sectionSketch: NXOpen.Sketch):
        """
        Setter for property: ( NXOpen.Sketch) Sketch
         Returns the sketch which holds the section curves   
            
         
        """
        pass
    @property
    def SketchCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SketchCollector
         Returns the sketch geometry collector   
            
         
        """
        pass
    @property
    def SketchMode(self) -> Sketcher.Mode:
        """
        Getter for property: ( Sketcher.Mode NXOpen) SketchMode
         Returns the sketch mode   
            
         
        """
        pass
    @SketchMode.setter
    def SketchMode(self, sketchMode: Sketcher.Mode):
        """
        Setter for property: ( Sketcher.Mode NXOpen) SketchMode
         Returns the sketch mode   
            
         
        """
        pass
    def AddCurvePoints(self, points: List[NXOpen.Point]) -> None:
        """
         Creates or extends the curve with points 
        """
        pass
    def SetSketchCanvas(self, faces: List[NXOpen.Face]) -> None:
        """
         Set the faces to sketch the curve upon 
        """
        pass
import NXOpen
class SubnestingBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.SubnestingBuilder. """
    @property
    def ConstraintType(self) -> Nester3D.Constraint:
        """
        Getter for property: ( Nester3D.Constraint NXOpen) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraint: Nester3D.Constraint):
        """
        Setter for property: ( Nester3D.Constraint NXOpen) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    @property
    def GroupPartsAfterSubnesting(self) -> bool:
        """
        Getter for property: (bool) GroupPartsAfterSubnesting
         Returns the flag to set Group after subnesting operation   
            
         
        """
        pass
    @GroupPartsAfterSubnesting.setter
    def GroupPartsAfterSubnesting(self, groupPartsAfterSubnesting: bool):
        """
        Setter for property: (bool) GroupPartsAfterSubnesting
         Returns the flag to set Group after subnesting operation   
            
         
        """
        pass
    @property
    def InterlockingType(self) -> Nester3D.Interlocking:
        """
        Getter for property: ( Nester3D.Interlocking NXOpen) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    @InterlockingType.setter
    def InterlockingType(self, interlockingType: Nester3D.Interlocking):
        """
        Setter for property: ( Nester3D.Interlocking NXOpen) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    @property
    def PartsToSubnest(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PartsToSubnest
         Returns the objects to reposition   
            
         
        """
        pass
    @property
    def RotationAngle(self) -> Nester3D.RotationAngleType:
        """
        Getter for property: ( Nester3D.RotationAngleType NXOpen) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: Nester3D.RotationAngleType):
        """
        Setter for property: ( Nester3D.RotationAngleType NXOpen) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    @property
    def Spacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Spacing
         Returns the spacing between parts   
            
         
        """
        pass
    @property
    def StopAfter(self) -> int:
        """
        Getter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    @StopAfter.setter
    def StopAfter(self, stopAfter: int):
        """
        Setter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    def ExecuteSubnesting(self) -> NestingStatus:
        """
         Execute the Subnesting 
         Returns nestStatus ( NestingStatus NXOpen):  Nesting Status.
        """
        pass
import NXOpen
class SupportBuilder(NXOpen.Builder): 
    """ Represents a Mfg.AM.Support builder """
    class Modes(Enum):
        """
        Members Include: 
         |Automatic| 
         |Manual| 
         |RegionsOnly| 
         |Duplicate| 

        """
        Automatic: int
        Manual: int
        RegionsOnly: int
        Duplicate: int
        @staticmethod
        def ValueOf(value: int) -> SupportBuilder.Modes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlatformFilterMode(Enum):
        """
        Members Include: 
         |KeepAll| 
         |FullContactOnly| 
         |PartitialTouch| 
         |KeepPlatformFraction| 
         |AvoidInternal| 

        """
        KeepAll: int
        FullContactOnly: int
        PartitialTouch: int
        KeepPlatformFraction: int
        AvoidInternal: int
        @staticmethod
        def ValueOf(value: int) -> SupportBuilder.PlatformFilterMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |Block| 
         |Line| 
         |Point| 
         |Nosupport| 
         |UserDefined| 
         |Volume| 
         |Web| 
         |Contour| 
         |Gusset| 
         |Combined| 
         |Tree| 
         |Hybrid| 

        """
        Block: int
        Line: int
        Point: int
        Nosupport: int
        UserDefined: int
        Volume: int
        Web: int
        Contour: int
        Gusset: int
        Combined: int
        Tree: int
        Hybrid: int
        @staticmethod
        def ValueOf(value: int) -> SupportBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BodySelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) BodySelection
         Returns the body selection   
            
         
        """
        pass
    @property
    def CurveSelection(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) CurveSelection
         Returns the curve selection   
            
         
        """
        pass
    @property
    def FaceSelection(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceSelection
         Returns the face selection   
            
         
        """
        pass
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: ( NXOpen.FacetCollector) FacetCollector
         Returns the part (region) selection   
            
         
        """
        pass
    @property
    def Mode(self) -> SupportBuilder.Modes:
        """
        Getter for property: ( SupportBuilder.Modes NXOpen) Mode
         Returns the support creation mode.  
             
         
        """
        pass
    @Mode.setter
    def Mode(self, mode: SupportBuilder.Modes):
        """
        Setter for property: ( SupportBuilder.Modes NXOpen) Mode
         Returns the support creation mode.  
             
         
        """
        pass
    @property
    def PartSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) PartSelection
         Returns the part (region) selection   
            
         
        """
        pass
    @property
    def PlatformFilter(self) -> SupportBuilder.PlatformFilterMode:
        """
        Getter for property: ( SupportBuilder.PlatformFilterMode NXOpen) PlatformFilter
         Returns the platform filter   
            
         
        """
        pass
    @PlatformFilter.setter
    def PlatformFilter(self, platformFilter: SupportBuilder.PlatformFilterMode):
        """
        Setter for property: ( SupportBuilder.PlatformFilterMode NXOpen) PlatformFilter
         Returns the platform filter   
            
         
        """
        pass
    @property
    def PointSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PointSelection
         Returns the point selection   
            
         
        """
        pass
    @property
    def Sketcher(self) -> Sketcher:
        """
        Getter for property: ( Sketcher NXOpen) Sketcher
         Returns the sketcher   
            
         
        """
        pass
    @property
    def SupportProfile(self) -> SupportProfile:
        """
        Getter for property: ( SupportProfile NXOpen) SupportProfile
         Returns the support profile used to generate supports or a NULL_TAG if the default printer profile is used   
            
         
        """
        pass
    @SupportProfile.setter
    def SupportProfile(self, tagSupportProfile: SupportProfile):
        """
        Setter for property: ( SupportProfile NXOpen) SupportProfile
         Returns the support profile used to generate supports or a NULL_TAG if the default printer profile is used   
            
         
        """
        pass
    @property
    def SupportType(self) -> SupportBuilder.Types:
        """
        Getter for property: ( SupportBuilder.Types NXOpen) SupportType
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    @SupportType.setter
    def SupportType(self, supportType: SupportBuilder.Types):
        """
        Setter for property: ( SupportBuilder.Types NXOpen) SupportType
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    @property
    def Type(self) -> SupportBuilder.Types:
        """
        Getter for property: ( SupportBuilder.Types NXOpen) Type
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SupportBuilder.Types):
        """
        Setter for property: ( SupportBuilder.Types NXOpen) Type
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    def GetProfileSupport(self) -> ProfileSupport:
        """
         Get the profile support to use to create a support of a particular type. Calling this method will change the profile library when applicable 
         Returns tagProfile ( ProfileSupport NXOpen): .
        """
        pass
    def SetProfileSupport(self, tagProfile: ProfileSupport) -> None:
        """
         Set the profile support to use to create a support of a particular type. Calling this method will change the profile library when applicable 
        """
        pass
    def SetSurfaceRegion(self, faces: List[NXOpen.Face]) -> None:
        """
         Set the surface region faces for the support to create 
        """
        pass
class SupportLibrary(Library): 
    """ Interface for Services Support Library objects """
    def AddSupportProfile(self) -> ProfileSupport:
        """
         Adds a support profile 
         Returns newProfileSupport ( ProfileSupport NXOpen):  the new support profile .
        """
        pass
class SupportProfile(ProfileObject): 
    """ Interface for Services Profile objects """
    def AddProfile(self, supportType: Support.Type) -> ProfileObject:
        """
         Add a new profile support 
         Returns pProfileSupport ( ProfileObject NXOpen):  .
        """
        pass
    def GetProfiles(self, supportType: Support.Type) -> List[ProfileObject]:
        """
         Returns the profile supports of a certain type 
         Returns pProfileSupports ( ProfileObject List[NXOp):  .
        """
        pass
    def SetAsDefault(self) -> None:
        """
         Sets the default support profile within the library. 
        """
        pass
import NXOpen
class Support(NXOpen.DisplayableObject): 
    """ Interface for Model Support objects """
    class Type(Enum):
        """
        Members Include: 
         |NotSet| 
         |Block| 
         |Line| 
         |Point| 
         |Volume| 
         |Web| 
         |Contour| 
         |Gusset| 
         |Combined| 
         |Tree| 
         |Hybrid| 
         |UserDefined| 

        """
        NotSet: int
        Block: int
        Line: int
        Point: int
        Volume: int
        Web: int
        Contour: int
        Gusset: int
        Combined: int
        Tree: int
        Hybrid: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> Support.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SupportType(self) -> Support.Type:
        """
        Getter for property: ( Support.Type NXOpen) SupportType
         Returns the support type   
            
         
        """
        pass
    def GetGeometries(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the support geometry. Can be a solid bodies, facet bodies or convergent bodies 
         Returns tagGeometry ( NXOpen.DisplayableObject Li): .
        """
        pass
    def GetGeometry(self) -> NXOpen.DisplayableObject:
        """
         Returns the support geometry. Can be a solid body, facet body or convergent body 
         Returns tagGeometry ( NXOpen.DisplayableObject): .
        """
        pass
    def GetSimulationSupport(self) -> SimulationSupport:
        """
         Returns the simulation support 
         Returns tagGeometry ( SimulationSupport NXOpen): .
        """
        pass
    def GetSurfaceRegion(self) -> SurfaceRegion:
        """
         Returns the surface region of the support 
         Returns surfaceRegion ( SurfaceRegion NXOpen): .
        """
        pass
    def Regenerate(self) -> None:
        """
         Regenerates Support after parameters change 
        """
        pass
    def SetSimulationSupport(self, tagGeometry: SimulationSupport) -> None:
        """
         Sets the simulation support 
        """
        pass
import NXOpen
class SurfaceRegion(NXOpen.NXObject): 
    """ Additive Manufacturing Surface Region """
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the surface region geometry. 
         Returns tagGeometry ( NXOpen.DisplayableObject Li): .
        """
        pass
