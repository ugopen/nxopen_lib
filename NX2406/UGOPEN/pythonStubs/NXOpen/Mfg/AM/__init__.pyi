from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link Mfg::AM::AddBuildTrayBuilder Mfg::AM::AddBuildTrayBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreateAddBuildTrayBuilder  NXOpen::Mfg::AM::ApplicationManager::CreateAddBuildTrayBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AddBuildTrayBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.AddBuildTrayBuilder</ja_class> builder """


    ## Getter for property: (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) Selection
    ##  Returns the selection   
    ##     
    ##  
    ## Getter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SelectPartList
    @property
    def Selection(self) -> SelectPartList:
        """
        Getter for property: (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) Selection
         Returns the selection   
            
         
        """
        pass
    
import NXOpen
##  Represents the Additive Manufacturing application  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class ApplicationManager(NXOpen.Object): 
    """ Represents the Additive Manufacturing application """


    ##  Add New Build Tray 
    ##  @return builder (@link AddBuildTrayBuilder NXOpen.Mfg.AM.AddBuildTrayBuilder@endlink):   the Add BuildTray Builder .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def CreateAddBuildTrayBuilder() -> AddBuildTrayBuilder:
        """
         Add New Build Tray 
         @return builder (@link AddBuildTrayBuilder NXOpen.Mfg.AM.AddBuildTrayBuilder@endlink):   the Add BuildTray Builder .
        """
        pass
    
    ##  Creates a build tray in a file 
    ##  @return builder (@link BuildTray NXOpen.Mfg.AM.BuildTray@endlink):   the build tray .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink)  the part to which the build tray is added</param>
    def CreateBuildTray(part: NXOpen.Part) -> BuildTray:
        """
         Creates a build tray in a file 
         @return builder (@link BuildTray NXOpen.Mfg.AM.BuildTray@endlink):   the build tray .
        """
        pass
    
    ##  Creates a Mfg.AM.MergeSupportsBuilder 
    ##  @return builder (@link MergeSupportsBuilder NXOpen.Mfg.AM.MergeSupportsBuilder@endlink):   the merge supports builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def CreateMergeSupportsBuilder() -> MergeSupportsBuilder:
        """
         Creates a Mfg.AM.MergeSupportsBuilder 
         @return builder (@link MergeSupportsBuilder NXOpen.Mfg.AM.MergeSupportsBuilder@endlink):   the merge supports builder .
        """
        pass
    
    ##  Creates a Mfg.AM.MovePartBuilder 
    ##  @return builder (@link MovePartBuilder NXOpen.Mfg.AM.MovePartBuilder@endlink):   the move part builder .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## <param name="partToMove"> (@link Part NXOpen.Mfg.AM.Part@endlink)  @link NXOpen::Mfg::AM::Part NXOpen::Mfg::AM::Part@endlink  to be moved </param>
    def CreateMovePartBuilder(partToMove: Part) -> MovePartBuilder:
        """
         Creates a Mfg.AM.MovePartBuilder 
         @return builder (@link MovePartBuilder NXOpen.Mfg.AM.MovePartBuilder@endlink):   the move part builder .
        """
        pass
    
    ##  Creates a Mfg.AM.PatternAMPartBuilder object. 
    ##  @return builder (@link PatternAMPartBuilder NXOpen.Mfg.AM.PatternAMPartBuilder@endlink):   the pattern part builder .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="editedComponent"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreatePatternAMPartBuilder(part: NXOpen.Part, editedComponent: NXOpen.NXObject) -> PatternAMPartBuilder:
        """
         Creates a Mfg.AM.PatternAMPartBuilder object. 
         @return builder (@link PatternAMPartBuilder NXOpen.Mfg.AM.PatternAMPartBuilder@endlink):   the pattern part builder .
        """
        pass
    
    ##  Creates a Mfg.AM.RepositionPartBuilder 
    ##  @return builder (@link RepositionPartBuilder NXOpen.Mfg.AM.RepositionPartBuilder@endlink):   the reposition part builder .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateRepositionPartBuilder(part: NXOpen.Part) -> RepositionPartBuilder:
        """
         Creates a Mfg.AM.RepositionPartBuilder 
         @return builder (@link RepositionPartBuilder NXOpen.Mfg.AM.RepositionPartBuilder@endlink):   the reposition part builder .
        """
        pass
    
    ##  Creates @link NXOpen::Mfg::AM::SinterboxBuilder NXOpen::Mfg::AM::SinterboxBuilder@endlink  
    ##  @return builder (@link SinterboxBuilder NXOpen.Mfg.AM.SinterboxBuilder@endlink):   the Sinterbox Builder .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## <param name="sinterbox"> (@link Sinterbox NXOpen.Mfg.AM.Sinterbox@endlink)  the Sinterbox that is modified </param>
    def CreateSinterboxBuilder(sinterbox: Sinterbox) -> SinterboxBuilder:
        """
         Creates @link NXOpen::Mfg::AM::SinterboxBuilder NXOpen::Mfg::AM::SinterboxBuilder@endlink  
         @return builder (@link SinterboxBuilder NXOpen.Mfg.AM.SinterboxBuilder@endlink):   the Sinterbox Builder .
        """
        pass
    
    ##  Creates a Mfg.AM.SubnestingBuilder 
    ##  @return builder (@link SubnestingBuilder NXOpen.Mfg.AM.SubnestingBuilder@endlink):   the Subnesting part builder .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    def CreateSubnestingBuilder() -> SubnestingBuilder:
        """
         Creates a Mfg.AM.SubnestingBuilder 
         @return builder (@link SubnestingBuilder NXOpen.Mfg.AM.SubnestingBuilder@endlink):   the Subnesting part builder .
        """
        pass
    
    ##  Creates Builder which allows for Creating Supports(Automatic, Manual, Regions Only) 
    ##  @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    def CreateSupportBuilder() -> SupportBuilder:
        """
         Creates Builder which allows for Creating Supports(Automatic, Manual, Regions Only) 
         @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink): .
        """
        pass
    
    ##  Retrieves the 3D Nester object 
    ##  @return builder (@link Nester3D NXOpen.Mfg.AM.Nester3D@endlink):   the 3D Nester .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    def Get3DNester() -> Nester3D:
        """
         Retrieves the 3D Nester object 
         @return builder (@link Nester3D NXOpen.Mfg.AM.Nester3D@endlink):   the 3D Nester .
        """
        pass
    
    ##  Retrieves the Mfg.AM.AttributeClipboard 
    ##  @return pAttributeClipboard (@link AttributeClipboard NXOpen.Mfg.AM.AttributeClipboard@endlink):  AttributeClipboard .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetAttributeClipboard() -> AttributeClipboard:
        """
         Retrieves the Mfg.AM.AttributeClipboard 
         @return pAttributeClipboard (@link AttributeClipboard NXOpen.Mfg.AM.AttributeClipboard@endlink):  AttributeClipboard .
        """
        pass
    
    ##  Retrieves the Mfg.AM.BuildTray 
    ##  @return builder (@link BuildTray NXOpen.Mfg.AM.BuildTray@endlink):   the build tray .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink)  the part to retrieve the build tray from </param>
    def GetBuildTray(part: NXOpen.Part) -> BuildTray:
        """
         Retrieves the Mfg.AM.BuildTray 
         @return builder (@link BuildTray NXOpen.Mfg.AM.BuildTray@endlink):   the build tray .
        """
        pass
    
    ##  Creates a copy paste clipboard  
    ##  @return pClipboard (@link Clipboard NXOpen.Mfg.AM.Clipboard@endlink):  Clipboard .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetClipboard() -> Clipboard:
        """
         Creates a copy paste clipboard  
         @return pClipboard (@link Clipboard NXOpen.Mfg.AM.Clipboard@endlink):  Clipboard .
        """
        pass
    
    ##  Creates a mesh properties builder  
    ##  @return tagBuilder (@link MeshProperties NXOpen.Mfg.AM.MeshProperties@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetMeshProperties() -> MeshProperties:
        """
         Creates a mesh properties builder  
         @return tagBuilder (@link MeshProperties NXOpen.Mfg.AM.MeshProperties@endlink): .
        """
        pass
    
    ##  Gets the Root Node of Profile Library 
    ##  @return profileRoot (@link Library NXOpen.Mfg.AM.Library@endlink):  profile root .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetRootLibrary() -> Library:
        """
         Gets the Root Node of Profile Library 
         @return profileRoot (@link Library NXOpen.Mfg.AM.Library@endlink):  profile root .
        """
        pass
    
    ##  Retrieves the support builder object 
    ##  @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink):   the support builder .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## <param name="tagSupport"> (@link Support NXOpen.Mfg.AM.Support@endlink)  the support </param>
    def GetSupportBuilder(tagSupport: Support) -> SupportBuilder:
        """
         Retrieves the support builder object 
         @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink):   the support builder .
        """
        pass
    
##  Represents a @link Mfg::AM::AssemblyBuildTray Mfg::AM::AssemblyBuildTray@endlink . <br> To obtain an instance of this class use NXOpen.Mfg.AM.AssemblyBuildTrayBuilder  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class AssemblyBuildTray(Assembly): 
    """ Represents a <ja_class>Mfg.AM.AssemblyBuildTray</ja_class>."""
    pass


##  Represents a @link Mfg::AM::Assembly Mfg::AM::Assembly@endlink . <br> To obtain an instance of this class use NXOpen.Mfg.AM.AssemblyBuilder  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class Assembly(PartGroup): 
    """ Represents a <ja_class>Mfg.AM.Assembly</ja_class>."""
    pass


import NXOpen
##   attribute clipboard  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ApplicationManager NXOpen::Mfg::AM::ApplicationManager@endlink .  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class AttributeClipboard(NXOpen.NXObject): 
    """  attribute clipboard """


    ##  Copy attributes 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="target"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CopyAttributes(self, target: NXOpen.TaggedObject) -> None:
        """
         Copy attributes 
        """
        pass
    
    ##  Paste attributes 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="target"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def PasteAttributes(self, target: NXOpen.TaggedObject) -> None:
        """
         Paste attributes 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Interface for Model Build Tray objects  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::GetBuildTray  NXOpen::Mfg::AM::ApplicationManager::GetBuildTray @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class BuildTray(NXOpen.DisplayableObject): 
    """ Interface for Model Build Tray objects """


    ##  Adds a component (occurrence) to the build tray 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="part"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  the component to add to the build tray </param>
    def AddComponent(self, part: NXOpen.Assemblies.Component) -> None:
        """
         Adds a component (occurrence) to the build tray 
        """
        pass
    
    ##  Adds a part to the build tray by file name 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## <param name="buildTray"> (@link BuildTray NXOpen.Mfg.AM.BuildTray@endlink) </param>
    ## <param name="fileName"> (str)  the file name of the part to add to the build tray </param>
    @overload
    def AddPart(self, fileName: str) -> None:
        """
         Adds a part to the build tray by file name 
        """
        pass
    
    ##  Adds a part to the build tray 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## <param name="buildTray"> (@link BuildTray NXOpen.Mfg.AM.BuildTray@endlink) </param>
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink)  the part to add to the build tray </param>
    @overload
    def AddPart(self, part: NXOpen.Part) -> None:
        """
         Adds a part to the build tray 
        """
        pass
    
    ##  Clear BuildStrategy values
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def ClearBuildStrategyValues(self) -> None:
        """
         Clear BuildStrategy values
        """
        pass
    
    ##  Finds the AM part (if any) containing the given geometry 
    ##  @return part (@link Part NXOpen.Mfg.AM.Part@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="tagGeometry"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def FindPart(self, tagGeometry: NXOpen.DisplayableObject) -> Part:
        """
         Finds the AM part (if any) containing the given geometry 
         @return part (@link Part NXOpen.Mfg.AM.Part@endlink): .
        """
        pass
    
    ##  Generates 3D printer data without sending it to the printer 
    ##  @return printJob (@link PrintJob NXOpen.Mfg.AM.PrintJob@endlink):  print job .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Generate(self) -> PrintJob:
        """
         Generates 3D printer data without sending it to the printer 
         @return printJob (@link PrintJob NXOpen.Mfg.AM.PrintJob@endlink):  print job .
        """
        pass
    
    ##  Generates the 3MF output file 
    ##  @return pathName (str):  Generated 3MF file path .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Generate3MFfile(self) -> str:
        """
         Generates the 3MF output file 
         @return pathName (str):  Generated 3MF file path .
        """
        pass
    
    ##  Gets all the parts in the build tray 
    ##  @return parts (@link Part List[NXOpen.Mfg.AM.Part]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetAllParts(self) -> List[Part]:
        """
         Gets all the parts in the build tray 
         @return parts (@link Part List[NXOpen.Mfg.AM.Part]@endlink): .
        """
        pass
    
    ##  Get BuildStrategy values
    ##  @return A tuple consisting of (buildStrategyNames, buildStrategyValues). 
    ##  - buildStrategyNames is: List[str]. the list of buildStrategy names .
    ##  - buildStrategyValues is: List[str]. the list of buildStrategy values .

    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetBuildStrategyValues(self) -> Tuple[List[str], List[str]]:
        """
         Get BuildStrategy values
         @return A tuple consisting of (buildStrategyNames, buildStrategyValues). 
         - buildStrategyNames is: List[str]. the list of buildStrategy names .
         - buildStrategyValues is: List[str]. the list of buildStrategy values .

        """
        pass
    
    ##  Gets the build tray dimensions 
    ##  @return A tuple consisting of (isBox, dLength, dWidth, dDiameter, dHeight, dTrayHeight). 
    ##  - isBox is: bool.
    ##  - dLength is: float.
    ##  - dWidth is: float.
    ##  - dDiameter is: float.
    ##  - dHeight is: float.
    ##  - dTrayHeight is: float.

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetDimensions(self) -> Tuple[bool, float, float, float, float, float]:
        """
         Gets the build tray dimensions 
         @return A tuple consisting of (isBox, dLength, dWidth, dDiameter, dHeight, dTrayHeight). 
         - isBox is: bool.
         - dLength is: float.
         - dWidth is: float.
         - dDiameter is: float.
         - dHeight is: float.
         - dTrayHeight is: float.

        """
        pass
    
    ##  Returns the groups in the build tray.
    ##  @return groups (@link PartGroup List[NXOpen.Mfg.AM.PartGroup]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetGroups(self) -> List[PartGroup]:
        """
         Returns the groups in the build tray.
         @return groups (@link PartGroup List[NXOpen.Mfg.AM.PartGroup]@endlink): .
        """
        pass
    
    ##  Gets the build tray origin 
    ##  @return origin (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetOrigin(self) -> NXOpen.Point3d:
        """
         Gets the build tray origin 
         @return origin (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Create reference set for buildtray part
    ##  @return outputDirectory (str):  the output directory for the selected printer for this buildtray in NX-AM .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetOutputDirectory(self) -> str:
        """
         Create reference set for buildtray part
         @return outputDirectory (str):  the output directory for the selected printer for this buildtray in NX-AM .
        """
        pass
    
    ##  Gets the printer of the build tray 
    ##  @return status (@link Printer NXOpen.Mfg.AM.Printer@endlink):  printer .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetPrinter(self) -> Printer:
        """
         Gets the printer of the build tray 
         @return status (@link Printer NXOpen.Mfg.AM.Printer@endlink):  printer .
        """
        pass
    
    ##  Returns the assigned profile library 
    ##  @return tagProfile (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetProfile(self) -> ProfileLibrary:
        """
         Returns the assigned profile library 
         @return tagProfile (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink): .
        """
        pass
    
    ##  Groups a number of parts into a new group. If parts are already a member of a group they will be removed from that group.
    ##  @return tagNewGroup (@link PartGroup NXOpen.Mfg.AM.PartGroup@endlink):  the new group .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="children"> (@link Part List[NXOpen.Mfg.AM.Part]@endlink)  the parts to group </param>
    def Group(self, children: List[Part]) -> PartGroup:
        """
         Groups a number of parts into a new group. If parts are already a member of a group they will be removed from that group.
         @return tagNewGroup (@link PartGroup NXOpen.Mfg.AM.PartGroup@endlink):  the new group .
        """
        pass
    
    ##  Prints the build tray 
    ##  @return printJob (@link PrintJob NXOpen.Mfg.AM.PrintJob@endlink):  print job .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Print3D(self) -> PrintJob:
        """
         Prints the build tray 
         @return printJob (@link PrintJob NXOpen.Mfg.AM.PrintJob@endlink):  print job .
        """
        pass
    
    ##  Remove a component (occurrence) from the build tray 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="part"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  the component to delete from the build tray </param>
    def RemoveComponent(self, part: NXOpen.Assemblies.Component) -> None:
        """
         Remove a component (occurrence) from the build tray 
        """
        pass
    
    ##  Sets the print order by moving parts or part groups before or after anchor part
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="objectsToReorder"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  List of Parts or Part Groups</param>
    ## <param name="anchor"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  Anchor Part or Part Group </param>
    ## <param name="reorderBefore"> (bool) </param>
    def ReorderParts(self, objectsToReorder: List[NXOpen.DisplayableObject], anchor: NXOpen.DisplayableObject, reorderBefore: bool) -> None:
        """
         Sets the print order by moving parts or part groups before or after anchor part
        """
        pass
    
    ##  Sends the output files to the printer 
    ##  @return printJob (@link PrintJob NXOpen.Mfg.AM.PrintJob@endlink):  print job .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def SendToMachine(self) -> PrintJob:
        """
         Sends the output files to the printer 
         @return printJob (@link PrintJob NXOpen.Mfg.AM.PrintJob@endlink):  print job .
        """
        pass
    
    ##  Set BuildStrategy values
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="buildStrategyNames"> (List[str])  the list of buildStrategy names </param>
    ## <param name="buildStrategyValues"> (List[str])  the list of buildStrategy values </param>
    def SetBuildStrategyValues(self, buildStrategyNames: List[str], buildStrategyValues: List[str]) -> None:
        """
         Set BuildStrategy values
        """
        pass
    
    ##  Sets the given profile as the default profile on the build tray 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SetSupportProfile SetSupportProfile@endlink  instead.  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="part"> (@link Profile NXOpen.Mfg.AM.Profile@endlink) </param>
    def SetDefaultProfile(self, part: Profile) -> None:
        """
         Sets the given profile as the default profile on the build tray 
        """
        pass
    
    ##  Prints the build tray 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="status"> (@link Printer NXOpen.Mfg.AM.Printer@endlink)  printer </param>
    def SetPrinter(self, status: Printer) -> None:
        """
         Prints the build tray 
        """
        pass
    
    ##  Sets the profile library 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="supportProfile"> (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink) </param>
    def SetProfile(self, supportProfile: ProfileLibrary) -> None:
        """
         Sets the profile library 
        """
        pass
    
    ##  Sets the given profile as the default support profile on the build tray 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="tagSupportProfile"> (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) </param>
    def SetSupportProfile(self, tagSupportProfile: SupportProfile) -> None:
        """
         Sets the given profile as the default support profile on the build tray 
        """
        pass
    
    ##  Synchronize the build tray and selected objects 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def Synchronize(self) -> None:
        """
         Synchronize the build tray and selected objects 
        """
        pass
    
import NXOpen
##   CopyPaste Clipboard  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ApplicationManager NXOpen::Mfg::AM::ApplicationManager@endlink .  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Clipboard(NXOpen.NXObject): 
    """  CopyPaste Clipboard """


    ##  Empties the clipboard 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Clear(self) -> None:
        """
         Empties the clipboard 
        """
        pass
    
    ##  Copy 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="objectsToCopy"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def Copy(self, objectsToCopy: List[NXOpen.NXObject]) -> None:
        """
         Copy 
        """
        pass
    
    ##  The point of origin of the clipboard objects 
    ##  @return ptMax (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetReferencePoint(self) -> NXOpen.Point3d:
        """
         The point of origin of the clipboard objects 
         @return ptMax (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Checks if there is anything to paste 
    ##  @return bIsEmpty (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def IsEmpty(self) -> bool:
        """
         Checks if there is anything to paste 
         @return bIsEmpty (bool): .
        """
        pass
    
    ##  Paste
    ##  @return objectCopies (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="target"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def Paste(self, target: NXOpen.TaggedObject) -> List[NXOpen.NXObject]:
        """
         Paste
         @return objectCopies (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Paste Special
    ##  @return objectCopies (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="target"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="xform"> (@link NXOpen.Matrix4x4 NXOpen.Matrix4x4@endlink) </param>
    def PasteSpecial(self, target: NXOpen.TaggedObject, xform: NXOpen.Matrix4x4) -> List[NXOpen.NXObject]:
        """
         Paste Special
         @return objectCopies (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
##  Interface for Services Profile Library objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ApplicationManager NXOpen::Mfg::AM::ApplicationManager@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class Library(ProfileObject): 
    """ Interface for Services Profile Library objects """


    ##  Adds a Library 
    ##  @return newLib (@link Library NXOpen.Mfg.AM.Library@endlink):  the new library .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def AddLibrary(self) -> Library:
        """
         Adds a Library 
         @return newLib (@link Library NXOpen.Mfg.AM.Library@endlink):  the new library .
        """
        pass
    
    ##  Adds a New Build Profile 
    ##  @return newProfile (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  the new profile .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def AddNewBuildProfile(self) -> ProfileObject:
        """
         Adds a New Build Profile 
         @return newProfile (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  the new profile .
        """
        pass
    
    ##  Deprecated 
    ##  @return newProfile (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  the new profile .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link ProfileLibrary::AddSupportProfile ProfileLibrary::AddSupportProfile@endlink   <br> 

    ## License requirements: None.
    def AddNewProfile(self) -> ProfileObject:
        """
         Deprecated 
         @return newProfile (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  the new profile .
        """
        pass
    
    ##  Adds a Profile Library 
    ##  @return newProfileLib (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink):  the new profile library .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def AddProfile(self) -> ProfileLibrary:
        """
         Adds a Profile Library 
         @return newProfileLib (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink):  the new profile library .
        """
        pass
    
    ##  Adds a Profile Library 
    ##  @return newProfileLib (@link Library NXOpen.Mfg.AM.Library@endlink):  the new profile library .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link AddProfile AddProfile@endlink  instead.  <br> 

    ## License requirements: None.
    def AddProfileLibrary(self) -> Library:
        """
         Adds a Profile Library 
         @return newProfileLib (@link Library NXOpen.Mfg.AM.Library@endlink):  the new profile library .
        """
        pass
    
    ##  Adds a Support Library 
    ##  @return newSupportLib (@link Library NXOpen.Mfg.AM.Library@endlink):  the new support library .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  This method cannot be used any more. All support libraries are automatically created.  <br> 

    ## License requirements: None.
    def AddSupportLibrary(self) -> Library:
        """
         Adds a Support Library 
         @return newSupportLib (@link Library NXOpen.Mfg.AM.Library@endlink):  the new support library .
        """
        pass
    
    ##  Gets all the children Libraries  
    ##  @return libraries (@link Library List[NXOpen.Mfg.AM.Library]@endlink):  the libraries .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetChildLibraries(self) -> List[Library]:
        """
         Gets all the children Libraries  
         @return libraries (@link Library List[NXOpen.Mfg.AM.Library]@endlink):  the libraries .
        """
        pass
    
    ##  Gets the children Profiles of the Library 
    ##  @return profiles (@link ProfileObject List[NXOpen.Mfg.AM.ProfileObject]@endlink):  the profiles .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link GetProfiles GetProfiles@endlink   <br> 

    ## License requirements: None.
    def GetChildProfiles(self) -> List[ProfileObject]:
        """
         Gets the children Profiles of the Library 
         @return profiles (@link ProfileObject List[NXOpen.Mfg.AM.ProfileObject]@endlink):  the profiles .
        """
        pass
    
    ##  Returns all profiles in the library 
    ##  @return profiles (@link ProfileLibrary List[NXOpen.Mfg.AM.ProfileLibrary]@endlink):  the profiles .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetProfiles(self) -> List[ProfileLibrary]:
        """
         Returns all profiles in the library 
         @return profiles (@link ProfileLibrary List[NXOpen.Mfg.AM.ProfileLibrary]@endlink):  the profiles .
        """
        pass
    
    ##  Imports a New Profile 
    ##  @return importResult (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="mmcgFileName"> (str) </param>
    ## <param name="profileName"> (str) </param>
    def ImportNewProfile(self, mmcgFileName: str, profileName: str) -> bool:
        """
         Imports a New Profile 
         @return importResult (bool): .
        """
        pass
    
    ##  Import a profile from a file 
    ##  @return newProfileLib (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink):  the new imported profile library .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="mmcfFileName"> (str) </param>
    def ImportProfile(self, mmcfFileName: str) -> ProfileLibrary:
        """
         Import a profile from a file 
         @return newProfileLib (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink):  the new imported profile library .
        """
        pass
    
    ##  Removes a library 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="lib"> (@link Library NXOpen.Mfg.AM.Library@endlink)  the lib to remove </param>
    def RemoveLibrary(self, lib: Library) -> None:
        """
         Removes a library 
        """
        pass
    
    ##  Removes a profile 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="lib"> (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink)  the profile to remove </param>
    def RemoveProfile(self, lib: ProfileLibrary) -> None:
        """
         Removes a profile 
        """
        pass
    
import NXOpen
##  Represents a @link Mfg::AM::Support Mfg::AM::Support@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreateMergeSupportsBuilder  NXOpen::Mfg::AM::ApplicationManager::CreateMergeSupportsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MergeSupportsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.Support</ja_class> builder """


    ## Getter for property: (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) MergeSelection
    ##  Returns the merge selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectSupportList
    @property
    def MergeSelection(self) -> SelectSupportList:
        """
        Getter for property: (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) MergeSelection
         Returns the merge selection   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) TargetSelection
    ##  Returns the target support selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectSupport
    @property
    def TargetSelection(self) -> SelectSupport:
        """
        Getter for property: (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) TargetSelection
         Returns the target support selection   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a mesh properties builder  <br> To obtain an instance of this class use JAX_MFG_AM_ApplicationManager_GetMeshProperties  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MeshResolution.AngleTolerance </term> <description> 
##  
## 15.0 </description> </item> 
## 
## <item><term> 
##  
## MeshResolution.EdgeTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## MeshResolution.FaceTolerance </term> <description> 
##  
## 0.005 </description> </item> 
## 
## <item><term> 
##  
## MeshResolution.Resolution </term> <description> 
##  
## Standard </description> </item> 
## 
## <item><term> 
##  
## MeshResolution.WidthTolerance </term> <description> 
##  
## 0.3 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.2  <br> 

class MeshProperties(NXOpen.Builder): 
    """ Represents a mesh properties builder """


    ## Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) MeshResolution
    ##  Returns the mesh resolution builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.GeometricUtilities.DisplayResolutionBuilder
    @property
    def MeshResolution(self) -> NXOpen.GeometricUtilities.DisplayResolutionBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.DisplayResolutionBuilder NXOpen.GeometricUtilities.DisplayResolutionBuilder@endlink) MeshResolution
         Returns the mesh resolution builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ObjectSelection
    ##  Returns the meshed object selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ObjectSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ObjectSelection
         Returns the meshed object selection   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) PartSelection
    ##  Returns the part selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1872.0.0.  Use @link NXOpen::Mfg::AM::MeshProperties::SetObjectSelection NXOpen::Mfg::AM::MeshProperties::SetObjectSelection@endlink  instead.  <br> 

    ## @return SelectPartList
    @property
    def PartSelection(self) -> SelectPartList:
        """
        Getter for property: (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) PartSelection
         Returns the part selection   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Validate
##  Represents a @link Mfg::AM::MovePartBuilder Mfg::AM::MovePartBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreateMovePartBuilder  NXOpen::Mfg::AM::ApplicationManager::CreateMovePartBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Divisions </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## MoveType </term> <description> 
##  
## MoveOriginal </description> </item> 
## 
## <item><term> 
##  
## NumberOfCopies </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## TransformMotion.DeltaEnum </term> <description> 
##  
## ReferenceWcsWorkPart </description> </item> 
## 
## <item><term> 
##  
## TransformMotion.DeltaXc.Value </term> <description> 
##  
## 0.0 </description> </item> 
## 
## <item><term> 
##  
## TransformMotion.DeltaYc.Value </term> <description> 
##  
## 0.0 </description> </item> 
## 
## <item><term> 
##  
## TransformMotion.DeltaZc.Value </term> <description> 
##  
## 0.0 </description> </item> 
## 
## <item><term> 
##  
## TransformMotion.Option </term> <description> 
##  
## Dynamic </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class MovePartBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.MovePartBuilder</ja_class>. """


    ##  Represents move type.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Geometry</term><description> 
    ## </description> </item><item><term> 
    ## Component</term><description> 
    ## </description> </item></list>
    class MoveObject(Enum):
        """
        Members Include: <Geometry> <Component>
        """
        Geometry: int
        Component: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MovePartBuilder.MoveObject:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Indicates whether to move or copy objects 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## MoveOriginal</term><description> 
    ##  move part </description> </item><item><term> 
    ## CopyOriginal</term><description> 
    ##  copy part</description> </item></list>
    class MoveTypeOption(Enum):
        """
        Members Include: <MoveOriginal> <CopyOriginal>
        """
        MoveOriginal: int
        CopyOriginal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MovePartBuilder.MoveTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) Divisions
    ##  Returns the distance or angle divisions   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def Divisions(self) -> int:
        """
        Getter for property: (int) Divisions
         Returns the distance or angle divisions   
            
         
        """
        pass
    
    ## Setter for property: (int) Divisions

    ##  Returns the distance or angle divisions   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Divisions.setter
    def Divisions(self, distanceOrAngleDivisions: int):
        """
        Setter for property: (int) Divisions
         Returns the distance or angle divisions   
            
         
        """
        pass
    
    ## Getter for property: (@link MovePartBuilder.MoveTypeOption NXOpen.Mfg.AM.MovePartBuilder.MoveTypeOption@endlink) MoveType
    ##  Returns the move rotate result   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return MovePartBuilder.MoveTypeOption
    @property
    def MoveType(self) -> MovePartBuilder.MoveTypeOption:
        """
        Getter for property: (@link MovePartBuilder.MoveTypeOption NXOpen.Mfg.AM.MovePartBuilder.MoveTypeOption@endlink) MoveType
         Returns the move rotate result   
            
         
        """
        pass
    
    ## Setter for property: (@link MovePartBuilder.MoveTypeOption NXOpen.Mfg.AM.MovePartBuilder.MoveTypeOption@endlink) MoveType

    ##  Returns the move rotate result   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MoveType.setter
    def MoveType(self, moveType: MovePartBuilder.MoveTypeOption):
        """
        Setter for property: (@link MovePartBuilder.MoveTypeOption NXOpen.Mfg.AM.MovePartBuilder.MoveTypeOption@endlink) MoveType
         Returns the move rotate result   
            
         
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
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @NumberOfCopies.setter
    def NumberOfCopies(self, numCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of copies   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ObjectToMoveObject
    ##  Returns the objects to move-rotate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def ObjectToMoveObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ObjectToMoveObject
         Returns the objects to move-rotate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Validate.SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
    ##  Returns the selection and placement builder  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Validate.SelectionAndPlacementBuilder
    @property
    def SelectionAndPlacement(self) -> NXOpen.Validate.SelectionAndPlacementBuilder:
        """
        Getter for property: (@link NXOpen.Validate.SelectionAndPlacementBuilder NXOpen.Validate.SelectionAndPlacementBuilder@endlink) SelectionAndPlacement
         Returns the selection and placement builder  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.ModlMotion NXOpen.GeometricUtilities.ModlMotion@endlink) TransformMotion
    ##  Returns the transform   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.ModlMotion
    @property
    def TransformMotion(self) -> NXOpen.GeometricUtilities.ModlMotion:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.ModlMotion NXOpen.GeometricUtilities.ModlMotion@endlink) TransformMotion
         Returns the transform   
            
         
        """
        pass
    
import NXOpen
##  Interface for AM Nesting Dialog Builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::Get3DNester  NXOpen::Mfg::AM::ApplicationManager::Get3DNester @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Accuracy </term> <description> 
##  
## 1 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## BottomDistance </term> <description> 
##  
## 2.0 (millimeters part), 0.1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ConstraintType </term> <description> 
##  
## FixedRotation </description> </item> 
## 
## <item><term> 
##  
## InterlockingType </term> <description> 
##  
## AllowInterlocks </description> </item> 
## 
## <item><term> 
##  
## RotationAngle </term> <description> 
##  
## Degree90 </description> </item> 
## 
## <item><term> 
##  
## SolutionType </term> <description> 
##  
## OptimizeHeight </description> </item> 
## 
## <item><term> 
##  
## Spacing </term> <description> 
##  
## 5.0 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StartFromEmptyBuildtray </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## StopAfter </term> <description> 
##  
## 2 </description> </item> 
## 
## <item><term> 
##  
## TargetDensity </term> <description> 
##  
## 10.0 </description> </item> 
## 
## <item><term> 
##  
## ViewProgress </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## WallDistance </term> <description> 
##  
## 2.0 (millimeters part), 0.1 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.1  <br> 

class Nester3D(NXOpen.Builder): 
    """ Interface for AM Nesting Dialog Builder """


    ##  Interface for AM Nesting Dialog Builder 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Free</term><description> 
    ## </description> </item><item><term> 
    ## FixedZDirection</term><description> 
    ## </description> </item><item><term> 
    ## FixedFloorPlane</term><description> 
    ## </description> </item><item><term> 
    ## Rotate180</term><description> 
    ## </description> </item><item><term> 
    ## FixedBottomAndXY</term><description> 
    ## </description> </item><item><term> 
    ## FixedRotation</term><description> 
    ## </description> </item><item><term> 
    ## Fixed</term><description> 
    ## </description> </item></list>
    class Constraint(Enum):
        """
        Members Include: <Free> <FixedZDirection> <FixedFloorPlane> <Rotate180> <FixedBottomAndXY> <FixedRotation> <Fixed>
        """
        Free: int
        FixedZDirection: int
        FixedFloorPlane: int
        Rotate180: int
        FixedBottomAndXY: int
        FixedRotation: int
        Fixed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Nester3D.Constraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Interface for AM Nesting Dialog Builder 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AllowInterlocks</term><description> 
    ## </description> </item><item><term> 
    ## AvoidTunnels</term><description> 
    ## </description> </item><item><term> 
    ## AvoidAllInterlocks</term><description> 
    ## </description> </item></list>
    class Interlocking(Enum):
        """
        Members Include: <AllowInterlocks> <AvoidTunnels> <AvoidAllInterlocks>
        """
        AllowInterlocks: int
        AvoidTunnels: int
        AvoidAllInterlocks: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Nester3D.Interlocking:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Interface for AM Nesting Dialog Builder 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TwoD</term><description> 
    ## </description> </item><item><term> 
    ## ThreeD</term><description> 
    ## </description> </item></list>
    class NesterType(Enum):
        """
        Members Include: <TwoD> <ThreeD>
        """
        TwoD: int
        ThreeD: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Nester3D.NesterType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Interface for AM Nesting Dialog Builder 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Degree90</term><description> 
    ## </description> </item><item><term> 
    ## Degree45</term><description> 
    ## </description> </item><item><term> 
    ## Degree30</term><description> 
    ## </description> </item><item><term> 
    ## Degree15</term><description> 
    ## </description> </item></list>
    class RotationAngleType(Enum):
        """
        Members Include: <Degree90> <Degree45> <Degree30> <Degree15>
        """
        Degree90: int
        Degree45: int
        Degree30: int
        Degree15: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Nester3D.RotationAngleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Interface for AM Nesting Dialog Builder 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OptimizeHeight</term><description> 
    ## </description> </item><item><term> 
    ## DistributeHeight</term><description> 
    ## </description> </item><item><term> 
    ## OptimizeSliceVolume</term><description> 
    ## </description> </item><item><term> 
    ## OptimizeHeightAndSliceVolume</term><description> 
    ## </description> </item></list>
    class Solution(Enum):
        """
        Members Include: <OptimizeHeight> <DistributeHeight> <OptimizeSliceVolume> <OptimizeHeightAndSliceVolume>
        """
        OptimizeHeight: int
        DistributeHeight: int
        OptimizeSliceVolume: int
        OptimizeHeightAndSliceVolume: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Nester3D.Solution:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) Accuracy
    ##  Returns the accuracy   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def Accuracy(self) -> float:
        """
        Getter for property: (float) Accuracy
         Returns the accuracy   
            
         
        """
        pass
    
    ## Setter for property: (float) Accuracy

    ##  Returns the accuracy   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Accuracy.setter
    def Accuracy(self, accuracy: float):
        """
        Setter for property: (float) Accuracy
         Returns the accuracy   
            
         
        """
        pass
    
    ## Getter for property: (float) BottomDistance
    ##  Returns the spacing between parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return float
    @property
    def BottomDistance(self) -> float:
        """
        Getter for property: (float) BottomDistance
         Returns the spacing between parts   
            
         
        """
        pass
    
    ## Setter for property: (float) BottomDistance

    ##  Returns the spacing between parts   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @BottomDistance.setter
    def BottomDistance(self, bottomDistance: float):
        """
        Setter for property: (float) BottomDistance
         Returns the spacing between parts   
            
         
        """
        pass
    
    ## Getter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType
    ##  Returns the constraints   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Nester3D.Constraint
    @property
    def ConstraintType(self) -> Nester3D.Constraint:
        """
        Getter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType

    ##  Returns the constraints   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ConstraintType.setter
    def ConstraintType(self, constraint: Nester3D.Constraint):
        """
        Setter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    
    ## Getter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType
    ##  Returns the solution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return Nester3D.Interlocking
    @property
    def InterlockingType(self) -> Nester3D.Interlocking:
        """
        Getter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType

    ##  Returns the solution type   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @InterlockingType.setter
    def InterlockingType(self, interlockingType: Nester3D.Interlocking):
        """
        Setter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    
    ## Getter for property: (@link Nester3D.NesterType NXOpen.Mfg.AM.Nester3D.NesterType@endlink) NestingType
    ##  Returns the nesting type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return Nester3D.NesterType
    @property
    def NestingType(self) -> Nester3D.NesterType:
        """
        Getter for property: (@link Nester3D.NesterType NXOpen.Mfg.AM.Nester3D.NesterType@endlink) NestingType
         Returns the nesting type   
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.NesterType NXOpen.Mfg.AM.Nester3D.NesterType@endlink) NestingType

    ##  Returns the nesting type   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @NestingType.setter
    def NestingType(self, nestingType: Nester3D.NesterType):
        """
        Setter for property: (@link Nester3D.NesterType NXOpen.Mfg.AM.Nester3D.NesterType@endlink) NestingType
         Returns the nesting type   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) PartsToNest
    ##  Returns the parts to nest   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return SelectPartList
    @property
    def PartsToNest(self) -> SelectPartList:
        """
        Getter for property: (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) PartsToNest
         Returns the parts to nest   
            
         
        """
        pass
    
    ## Getter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle
    ##  Returns the Rotation Angle for the Parts to be nested    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return Nester3D.RotationAngleType
    @property
    def RotationAngle(self) -> Nester3D.RotationAngleType:
        """
        Getter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle

    ##  Returns the Rotation Angle for the Parts to be nested    
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: Nester3D.RotationAngleType):
        """
        Setter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    
    ## Getter for property: (@link Nester3D.Solution NXOpen.Mfg.AM.Nester3D.Solution@endlink) SolutionType
    ##  Returns the solution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return Nester3D.Solution
    @property
    def SolutionType(self) -> Nester3D.Solution:
        """
        Getter for property: (@link Nester3D.Solution NXOpen.Mfg.AM.Nester3D.Solution@endlink) SolutionType
         Returns the solution type   
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.Solution NXOpen.Mfg.AM.Nester3D.Solution@endlink) SolutionType

    ##  Returns the solution type   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @SolutionType.setter
    def SolutionType(self, solutionType: Nester3D.Solution):
        """
        Setter for property: (@link Nester3D.Solution NXOpen.Mfg.AM.Nester3D.Solution@endlink) SolutionType
         Returns the solution type   
            
         
        """
        pass
    
    ## Getter for property: (float) Spacing
    ##  Returns the spacing between parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def Spacing(self) -> float:
        """
        Getter for property: (float) Spacing
         Returns the spacing between parts   
            
         
        """
        pass
    
    ## Setter for property: (float) Spacing

    ##  Returns the spacing between parts   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @Spacing.setter
    def Spacing(self, spacing: float):
        """
        Setter for property: (float) Spacing
         Returns the spacing between parts   
            
         
        """
        pass
    
    ## Getter for property: (bool) StartFromEmptyBuildtray
    ##  Returns the StartFromEmptyBuildtray   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return bool
    @property
    def StartFromEmptyBuildtray(self) -> bool:
        """
        Getter for property: (bool) StartFromEmptyBuildtray
         Returns the StartFromEmptyBuildtray   
            
         
        """
        pass
    
    ## Setter for property: (bool) StartFromEmptyBuildtray

    ##  Returns the StartFromEmptyBuildtray   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @StartFromEmptyBuildtray.setter
    def StartFromEmptyBuildtray(self, startFromEmptyBuildtray: bool):
        """
        Setter for property: (bool) StartFromEmptyBuildtray
         Returns the StartFromEmptyBuildtray   
            
         
        """
        pass
    
    ## Getter for property: (int) StopAfter
    ##  Returns the stop after   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return int
    @property
    def StopAfter(self) -> int:
        """
        Getter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    
    ## Setter for property: (int) StopAfter

    ##  Returns the stop after   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @StopAfter.setter
    def StopAfter(self, stopAfter: int):
        """
        Setter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    
    ## Getter for property: (float) TargetDensity
    ##  Returns the targetDensity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return float
    @property
    def TargetDensity(self) -> float:
        """
        Getter for property: (float) TargetDensity
         Returns the targetDensity   
            
         
        """
        pass
    
    ## Setter for property: (float) TargetDensity

    ##  Returns the targetDensity   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @TargetDensity.setter
    def TargetDensity(self, targetDensity: float):
        """
        Setter for property: (float) TargetDensity
         Returns the targetDensity   
            
         
        """
        pass
    
    ## Getter for property: (bool) ViewProgress
    ##  Returns the view progress   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def ViewProgress(self) -> bool:
        """
        Getter for property: (bool) ViewProgress
         Returns the view progress   
            
         
        """
        pass
    
    ## Setter for property: (bool) ViewProgress

    ##  Returns the view progress   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ViewProgress.setter
    def ViewProgress(self, viewProgress: bool):
        """
        Setter for property: (bool) ViewProgress
         Returns the view progress   
            
         
        """
        pass
    
    ## Getter for property: (float) WallDistance
    ##  Returns the spacing between parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return float
    @property
    def WallDistance(self) -> float:
        """
        Getter for property: (float) WallDistance
         Returns the spacing between parts   
            
         
        """
        pass
    
    ## Setter for property: (float) WallDistance

    ##  Returns the spacing between parts   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @WallDistance.setter
    def WallDistance(self, wallDistance: float):
        """
        Setter for property: (float) WallDistance
         Returns the spacing between parts   
            
         
        """
        pass
    
    ##  Execute the Nesting 
    ##  @return nestStatus (@link NestingStatus NXOpen.Mfg.AM.NestingStatus@endlink):  Nesting Status.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    def ExecuteNesting(self) -> NestingStatus:
        """
         Execute the Nesting 
         @return nestStatus (@link NestingStatus NXOpen.Mfg.AM.NestingStatus@endlink):  Nesting Status.
        """
        pass
    
    ##  Sets the (sub) nesting box 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## <param name="builder"> (@link Nester3D NXOpen.Mfg.AM.Nester3D@endlink) </param>
    ## <param name="dLength"> (float) </param>
    ## <param name="dWidth"> (float) </param>
    ## <param name="dHeight"> (float) </param>
    @overload
    def SetNesting(self, dLength: float, dWidth: float, dHeight: float) -> None:
        """
         Sets the (sub) nesting box 
        """
        pass
    
    ##  Sets the (sub) nesting cylinder 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_mtls_nest_3d_2 ("NX Powder Bed Additive 3D Nesting") OR am_pb_mtls_nest_3d_1 ("NX Powder Bed Additive 2D Nesting") OR am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## <param name="builder"> (@link Nester3D NXOpen.Mfg.AM.Nester3D@endlink) </param>
    ## <param name="dDiameter"> (float) </param>
    ## <param name="dHeight"> (float) </param>
    @overload
    def SetNesting(self, dDiameter: float, dHeight: float) -> None:
        """
         Sets the (sub) nesting cylinder 
        """
        pass
    
import NXOpen
##  Nesting Status  
## 
##   <br>  Created in NX11.0.2  <br> 

class NestingStatus(NXOpen.TransientObject): 
    """ Nesting Status  """


    ##  Free the handle to the Nesting Status 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free the handle to the Nesting Status 
        """
        pass
    
    ##  Get the density 
    ##  @return density (float): .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    def GetDensity(self) -> float:
        """
         Get the density 
         @return density (float): .
        """
        pass
    
    ##  Get the error code 
    ##  @return errorCode (int): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetErrorCode(self) -> int:
        """
         Get the error code 
         @return errorCode (int): .
        """
        pass
    
    ##  Get the nested height 
    ##  @return nestingHeight (float): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetNestedHeight(self) -> float:
        """
         Get the nested height 
         @return nestingHeight (float): .
        """
        pass
    
    ##  Get the nested Length 
    ##  @return nestingLength (float): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetNestedLength(self) -> float:
        """
         Get the nested Length 
         @return nestingLength (float): .
        """
        pass
    
    ##  Get the nested part 
    ##  @return tagPart (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  AM Parts .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    def GetNestedParts(self) -> List[Part]:
        """
         Get the nested part 
         @return tagPart (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  AM Parts .
        """
        pass
    
    ##  Get the nested Width 
    ##  @return nestingWidth (float): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetNestedWidth(self) -> float:
        """
         Get the nested Width 
         @return nestingWidth (float): .
        """
        pass
    
    ##  Get the non nested part 
    ##  @return tagPart (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  AM Parts .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: None.
    def GetNotNestedParts(self) -> List[Part]:
        """
         Get the non nested part 
         @return tagPart (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  AM Parts .
        """
        pass
    
import NXOpen
##  Interface for Part Group objects  <br> Use @link NXOpen::Mfg::AM::BuildTray::Group NXOpen::Mfg::AM::BuildTray::Group@endlink  to create an instance of this class  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class PartGroup(NXOpen.DisplayableObject): 
    """ Interface for Part Group objects """


    ##  Adds parts to this group. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  Use @link NXOpen::Mfg::AM::PartGroup::AddObject NXOpen::Mfg::AM::PartGroup::AddObject@endlink  instead.  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="children"> (@link Part List[NXOpen.Mfg.AM.Part]@endlink)  the parts to add </param>
    def Add(self, children: List[Part]) -> None:
        """
         Adds parts to this group. 
        """
        pass
    
    ##  Adds objects to this group. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="children"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  the Objects to add </param>
    def AddObject(self, children: List[NXOpen.DisplayableObject]) -> None:
        """
         Adds objects to this group. 
        """
        pass
    
    ##  Converts the assembly group into a regular group so the members can be moved arround. If the group is not an assembly this method has no effect. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  No Replacement.  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Disassemble(self) -> None:
        """
         Converts the assembly group into a regular group so the members can be moved arround. If the group is not an assembly this method has no effect. 
        """
        pass
    
    ##  Returns the parts in this group. 
    ##  @return children (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  the member parts.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetChildren(self) -> List[Part]:
        """
         Returns the parts in this group. 
         @return children (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  the member parts.
        """
        pass
    
    ##  Gets the distance from part from the part group 
    ##  @return distanceFromPart (float): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetDistanceFromPart(self) -> float:
        """
         Gets the distance from part from the part group 
         @return distanceFromPart (float): .
        """
        pass
    
    ##  Gets the intertlocking type from the part 
    ##  @return intertlockingType (@link Part.InterlockingType NXOpen.Mfg.AM.Part.InterlockingType@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetInterlocking(self) -> Part.InterlockingType:
        """
         Gets the intertlocking type from the part 
         @return intertlockingType (@link Part.InterlockingType NXOpen.Mfg.AM.Part.InterlockingType@endlink): .
        """
        pass
    
    ##  Gets the nesting constraint type from the part 
    ##  @return nestingConstraintType (@link Part.NestingConstraintType NXOpen.Mfg.AM.Part.NestingConstraintType@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetNestingConstraint(self) -> Part.NestingConstraintType:
        """
         Gets the nesting constraint type from the part 
         @return nestingConstraintType (@link Part.NestingConstraintType NXOpen.Mfg.AM.Part.NestingConstraintType@endlink): .
        """
        pass
    
    ##  Gets the rotation angle from the part 
    ##  @return rotationAngle (@link Part.RotationAngleType NXOpen.Mfg.AM.Part.RotationAngleType@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetRotationAngle(self) -> Part.RotationAngleType:
        """
         Gets the rotation angle from the part 
         @return rotationAngle (@link Part.RotationAngleType NXOpen.Mfg.AM.Part.RotationAngleType@endlink): .
        """
        pass
    
    ##  Checks if the goup is an assembly group or not 
    ##  @return bIsAssembly (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def IsAssembly(self) -> bool:
        """
         Checks if the goup is an assembly group or not 
         @return bIsAssembly (bool): .
        """
        pass
    
    ##  Checks if the group is locked for individual position and/or orientation changes. 
    ##  @return bIsLocked (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  No Replacement.  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def IsLocked(self) -> bool:
        """
         Checks if the group is locked for individual position and/or orientation changes. 
         @return bIsLocked (bool): .
        """
        pass
    
    ##  Locks the group members for individual position and/or orientation changes. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  No Replacement.  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Lock(self) -> None:
        """
         Locks the group members for individual position and/or orientation changes. 
        """
        pass
    
    ##  Resets the group to an assembly group if possible. All assembly contraints (if any) are reapplied.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  No Replacement.  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Reassemble(self) -> None:
        """
         Resets the group to an assembly group if possible. All assembly contraints (if any) are reapplied.
        """
        pass
    
    ##  Removes the selected part from the group and adds it to the buildtray
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="children"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  the objects to remove </param>
    def Remove(self, children: List[NXOpen.DisplayableObject]) -> None:
        """
         Removes the selected part from the group and adds it to the buildtray
        """
        pass
    
    ##  Sets the print order by moving parts or part groups before or after anchor part
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="objectsToReorder"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  List of Parts or Part Groups</param>
    ## <param name="anchor"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink)  Anchor Part or Part Group </param>
    ## <param name="reorderBefore"> (bool) </param>
    def ReorderParts(self, objectsToReorder: List[NXOpen.DisplayableObject], anchor: NXOpen.DisplayableObject, reorderBefore: bool) -> None:
        """
         Sets the print order by moving parts or part groups before or after anchor part
        """
        pass
    
    ##  Sets the distance from part to the part group
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="distanceFromPart"> (float) </param>
    def SetDistanceFromPart(self, distanceFromPart: float) -> None:
        """
         Sets the distance from part to the part group
        """
        pass
    
    ##  Sets the intertlocking type on the part 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="intertlockingType"> (@link Part.InterlockingType NXOpen.Mfg.AM.Part.InterlockingType@endlink) </param>
    def SetInterlocking(self, intertlockingType: Part.InterlockingType) -> None:
        """
         Sets the intertlocking type on the part 
        """
        pass
    
    ##  Sets the nesting constraint type on the part 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="nestingConstraintType"> (@link Part.NestingConstraintType NXOpen.Mfg.AM.Part.NestingConstraintType@endlink) </param>
    def SetNestingConstraint(self, nestingConstraintType: Part.NestingConstraintType) -> None:
        """
         Sets the nesting constraint type on the part 
        """
        pass
    
    ##  Sets the rotation angle on the part 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="rotationAngle"> (@link Part.RotationAngleType NXOpen.Mfg.AM.Part.RotationAngleType@endlink) </param>
    def SetRotationAngle(self, rotationAngle: Part.RotationAngleType) -> None:
        """
         Sets the rotation angle on the part 
        """
        pass
    
    ##  Removes all parts from the group  and deletes the group. After calling this method the reference to the group has become invalid.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Ungroup(self) -> None:
        """
         Removes all parts from the group  and deletes the group. After calling this method the reference to the group has become invalid.
        """
        pass
    
    ##  Unlocks the group members for individual position and/or orientation changes. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2306.0.0.  No Replacement.  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Unlock(self) -> None:
        """
         Unlocks the group members for individual position and/or orientation changes. 
        """
        pass
    
import NXOpen
##  Interface for Model Part objects  <br> To obtain an instance of this class use JAX_MFG_AM_PART_GetRegions  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class PartRegion(NXOpen.DisplayableObject): 
    """ Interface for Model Part objects """


    ##  Clear BuildStrategy values
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def ClearBuildStrategyValues(self) -> None:
        """
         Clear BuildStrategy values
        """
        pass
    
    ##  Create support builder object 
    ##  @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink):   the support builder .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    def CreateSupportBuilder(self) -> SupportBuilder:
        """
         Create support builder object 
         @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink):   the support builder .
        """
        pass
    
    ##  Create the supports for the part region 
    ##  @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    def CreateSupports(self) -> List[Support]:
        """
         Create the supports for the part region 
         @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
        """
        pass
    
    ##  Get BuildStrategy values
    ##  @return A tuple consisting of (buildStrategyNames, buildStrategyValues). 
    ##  - buildStrategyNames is: List[str]. the list of buildStrategy names .
    ##  - buildStrategyValues is: List[str]. the list of buildStrategy values .

    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetBuildStrategyValues(self) -> Tuple[List[str], List[str]]:
        """
         Get BuildStrategy values
         @return A tuple consisting of (buildStrategyNames, buildStrategyValues). 
         - buildStrategyNames is: List[str]. the list of buildStrategy names .
         - buildStrategyValues is: List[str]. the list of buildStrategy values .

        """
        pass
    
    ##  Gets the dimensions for the part region 
    ##  @return A tuple consisting of (ptMin, ptMax). 
    ##  - ptMin is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - ptMax is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetDimensions(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the dimensions for the part region 
         @return A tuple consisting of (ptMin, ptMax). 
         - ptMin is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - ptMax is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

        """
        pass
    
    ##  Returns the geometry of the part.  Can be solid, facet or convergent objects. 
    ##  @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the geometry of the part.  Can be solid, facet or convergent objects. 
         @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Gets all the supports in the part 
    ##  @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetSupports(self) -> List[Support]:
        """
         Gets all the supports in the part 
         @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
        """
        pass
    
    ##  Removes all the supports from the part 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    def RemoveAllSupports(self) -> None:
        """
         Removes all the supports from the part 
        """
        pass
    
    ##  Removes the support from the part 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ## <param name="support"> (@link Support NXOpen.Mfg.AM.Support@endlink)  Support to be removed </param>
    def RemoveSupport(self, support: Support) -> None:
        """
         Removes the support from the part 
        """
        pass
    
    ##  Sets the print order by moving supports before or after an anchor support
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="supportsToReorder"> (@link Support List[NXOpen.Mfg.AM.Support]@endlink) </param>
    ## <param name="anchor"> (@link Support NXOpen.Mfg.AM.Support@endlink) </param>
    ## <param name="reorderBefore"> (bool) </param>
    def ReorderSupports(self, supportsToReorder: List[Support], anchor: Support, reorderBefore: bool) -> None:
        """
         Sets the print order by moving supports before or after an anchor support
        """
        pass
    
    ##  Set BuildStrategy values
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="buildStrategyNames"> (List[str])  the list of buildStrategy names </param>
    ## <param name="buildStrategyValues"> (List[str])  the list of buildStrategy values </param>
    def SetBuildStrategyValues(self, buildStrategyNames: List[str], buildStrategyValues: List[str]) -> None:
        """
         Set BuildStrategy values
        """
        pass
    
    ##  Sets the given profile as the default profile on the part region 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use SetSupportProfile  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="tagProfile"> (@link Profile NXOpen.Mfg.AM.Profile@endlink) </param>
    def SetDefaultProfile(self, tagProfile: Profile) -> None:
        """
         Sets the given profile as the default profile on the part region 
        """
        pass
    
    ##  Sets the given profile as the default profile on the part 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="tagSupportProfile"> (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) </param>
    def SetSupportProfile(self, tagSupportProfile: SupportProfile) -> None:
        """
         Sets the given profile as the default profile on the part 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
##  Interface for Model Part objects  <br> To obtain an instance of this class use JAX_MFG_AM_BUILDTRAY_GetAllParts  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Part(NXOpen.DisplayableObject): 
    """ Interface for Model Part objects """


    ##  Defines interlocking type type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ## </description> </item><item><term> 
    ## Allowinterlocks</term><description> 
    ## </description> </item><item><term> 
    ## Avoidtunnels</term><description> 
    ## </description> </item><item><term> 
    ## Avoidallinterlocks</term><description> 
    ## </description> </item></list>
    class InterlockingType(Enum):
        """
        Members Include: <Undefined> <Allowinterlocks> <Avoidtunnels> <Avoidallinterlocks>
        """
        Undefined: int
        Allowinterlocks: int
        Avoidtunnels: int
        Avoidallinterlocks: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Part.InterlockingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines nesting constraint type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ## </description> </item><item><term> 
    ## Free</term><description> 
    ## </description> </item><item><term> 
    ## FixZDirection</term><description> 
    ## </description> </item><item><term> 
    ## FixBottomPlane</term><description> 
    ## </description> </item><item><term> 
    ## Rotate180</term><description> 
    ## </description> </item><item><term> 
    ## FixBottomAndXy</term><description> 
    ## </description> </item><item><term> 
    ## FixRotation</term><description> 
    ## </description> </item><item><term> 
    ## Fixed</term><description> 
    ## </description> </item></list>
    class NestingConstraintType(Enum):
        """
        Members Include: <Undefined> <Free> <FixZDirection> <FixBottomPlane> <Rotate180> <FixBottomAndXy> <FixRotation> <Fixed>
        """
        Undefined: int
        Free: int
        FixZDirection: int
        FixBottomPlane: int
        Rotate180: int
        FixBottomAndXy: int
        FixRotation: int
        Fixed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Part.NestingConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Defines rotation angle type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ## </description> </item><item><term> 
    ## Degree90</term><description> 
    ## </description> </item><item><term> 
    ## Degree45</term><description> 
    ## </description> </item><item><term> 
    ## Degree30</term><description> 
    ## </description> </item><item><term> 
    ## Degree15</term><description> 
    ## </description> </item></list>
    class RotationAngleType(Enum):
        """
        Members Include: <Undefined> <Degree90> <Degree45> <Degree30> <Degree15>
        """
        Undefined: int
        Degree90: int
        Degree45: int
        Degree30: int
        Degree15: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Part.RotationAngleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Clear BuildStrategy values
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def ClearBuildStrategyValues(self) -> None:
        """
         Clear BuildStrategy values
        """
        pass
    
    ##  Create support builder object 
    ##  @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink):   the support builder .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    def CreateSupportBuilder(self) -> SupportBuilder:
        """
         Create support builder object 
         @return tagBuilder (@link SupportBuilder NXOpen.Mfg.AM.SupportBuilder@endlink):   the support builder .
        """
        pass
    
    ##  Create the supports for the part 
    ##  @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    def CreateSupports(self) -> List[Support]:
        """
         Create the supports for the part 
         @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
        """
        pass
    
    ##  Get BuildStrategy values
    ##  @return A tuple consisting of (buildStrategyNames, buildStrategyValues). 
    ##  - buildStrategyNames is: List[str]. the list of buildStrategy names .
    ##  - buildStrategyValues is: List[str]. the list of buildStrategy values .

    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetBuildStrategyValues(self) -> Tuple[List[str], List[str]]:
        """
         Get BuildStrategy values
         @return A tuple consisting of (buildStrategyNames, buildStrategyValues). 
         - buildStrategyNames is: List[str]. the list of buildStrategy names .
         - buildStrategyValues is: List[str]. the list of buildStrategy values .

        """
        pass
    
    ##  Returns the assembly component of the part 
    ##  @return tagComponent (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink):   the assembly component .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetComponent(self) -> NXOpen.Assemblies.Component:
        """
         Returns the assembly component of the part 
         @return tagComponent (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink):   the assembly component .
        """
        pass
    
    ##  Gets the dimensions for the part  
    ##  @return A tuple consisting of (ptMin, ptMax). 
    ##  - ptMin is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
    ##  - ptMax is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetDimensions(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
         Gets the dimensions for the part  
         @return A tuple consisting of (ptMin, ptMax). 
         - ptMin is: @link NXOpen.Point3d NXOpen.Point3d@endlink.
         - ptMax is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

        """
        pass
    
    ##  Gets the distance from the part 
    ##  @return distanceFromPart (float): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def GetDistanceFromPart(self) -> float:
        """
         Gets the distance from the part 
         @return distanceFromPart (float): .
        """
        pass
    
    ##  Returns the geometry of the part.  Can be solid, facet or convergent objects. 
    ##  @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the geometry of the part.  Can be solid, facet or convergent objects. 
         @return geometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Returns the group the part is in
    ##  @return tagGroup (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetGroup(self) -> NXOpen.DisplayableObject:
        """
         Returns the group the part is in
         @return tagGroup (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
        """
        pass
    
    ##  Gets the intertlocking type from the part 
    ##  @return intertlockingType (@link Part.InterlockingType NXOpen.Mfg.AM.Part.InterlockingType@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetInterlocking(self) -> Part.InterlockingType:
        """
         Gets the intertlocking type from the part 
         @return intertlockingType (@link Part.InterlockingType NXOpen.Mfg.AM.Part.InterlockingType@endlink): .
        """
        pass
    
    ##  Gets the nesting constraint type from the part 
    ##  @return nestingConstraintType (@link Part.NestingConstraintType NXOpen.Mfg.AM.Part.NestingConstraintType@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetNestingConstraint(self) -> Part.NestingConstraintType:
        """
         Gets the nesting constraint type from the part 
         @return nestingConstraintType (@link Part.NestingConstraintType NXOpen.Mfg.AM.Part.NestingConstraintType@endlink): .
        """
        pass
    
    ##  Returns the part regions of this part 
    ##  @return partRegions (@link PartRegion List[NXOpen.Mfg.AM.PartRegion]@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetPartRegions(self) -> List[PartRegion]:
        """
         Returns the part regions of this part 
         @return partRegions (@link PartRegion List[NXOpen.Mfg.AM.PartRegion]@endlink): .
        """
        pass
    
    ##  Returns the pattern feature of this part (if any) 
    ##  @return tagPattern (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink): .
    ## 
    ##   <br>  Created in NX1851.0.0  <br> 

    ## License requirements: None.
    def GetPattern(self) -> NXOpen.Features.Feature:
        """
         Returns the pattern feature of this part (if any) 
         @return tagPattern (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink): .
        """
        pass
    
    ##  Returns the Pattern Instances Of Part 
    ##  @return patternInstances (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    def GetPatternInstances(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the Pattern Instances Of Part 
         @return patternInstances (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Gets the rotation angle from the part 
    ##  @return rotationAngle (@link Part.RotationAngleType NXOpen.Mfg.AM.Part.RotationAngleType@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetRotationAngle(self) -> Part.RotationAngleType:
        """
         Gets the rotation angle from the part 
         @return rotationAngle (@link Part.RotationAngleType NXOpen.Mfg.AM.Part.RotationAngleType@endlink): .
        """
        pass
    
    ##  Returns the serial numbers of this part (if any) 
    ##  @return serialNumbers (@link SerialNumber List[NXOpen.Mfg.AM.SerialNumber]@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    def GetSerialNumbers(self) -> List[SerialNumber]:
        """
         Returns the serial numbers of this part (if any) 
         @return serialNumbers (@link SerialNumber List[NXOpen.Mfg.AM.SerialNumber]@endlink): .
        """
        pass
    
    ##  Gets all the supports in the part 
    ##  @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetSupports(self) -> List[Support]:
        """
         Gets all the supports in the part 
         @return supports (@link Support List[NXOpen.Mfg.AM.Support]@endlink): .
        """
        pass
    
    ##  Removes all the supports from the part 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    def RemoveAllSupports(self) -> None:
        """
         Removes all the supports from the part 
        """
        pass
    
    ##  Removes the support from the part 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ## <param name="support"> (@link Support NXOpen.Mfg.AM.Support@endlink)  Support to be removed </param>
    def RemoveSupport(self, support: Support) -> None:
        """
         Removes the support from the part 
        """
        pass
    
    ##  Set BuildStrategy values
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="buildStrategyNames"> (List[str])  the list of buildStrategy names </param>
    ## <param name="buildStrategyValues"> (List[str])  the list of buildStrategy values </param>
    def SetBuildStrategyValues(self, buildStrategyNames: List[str], buildStrategyValues: List[str]) -> None:
        """
         Set BuildStrategy values
        """
        pass
    
    ##  Sets the given profile as the default profile on the part 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SetSupportProfile SetSupportProfile@endlink   <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="tagProfile"> (@link Profile NXOpen.Mfg.AM.Profile@endlink) </param>
    def SetDefaultProfile(self, tagProfile: Profile) -> None:
        """
         Sets the given profile as the default profile on the part 
        """
        pass
    
    ##  Sets the distance from part on the part 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="distanceFromPart"> (float) </param>
    def SetDistanceFromPart(self, distanceFromPart: float) -> None:
        """
         Sets the distance from part on the part 
        """
        pass
    
    ##  Sets the intertlocking type on the part 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="intertlockingType"> (@link Part.InterlockingType NXOpen.Mfg.AM.Part.InterlockingType@endlink) </param>
    def SetInterlocking(self, intertlockingType: Part.InterlockingType) -> None:
        """
         Sets the intertlocking type on the part 
        """
        pass
    
    ##  Sets the nesting constraint type on the part 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="nestingConstraintType"> (@link Part.NestingConstraintType NXOpen.Mfg.AM.Part.NestingConstraintType@endlink) </param>
    def SetNestingConstraint(self, nestingConstraintType: Part.NestingConstraintType) -> None:
        """
         Sets the nesting constraint type on the part 
        """
        pass
    
    ##  Sets the rotation angle on the part 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="rotationAngle"> (@link Part.RotationAngleType NXOpen.Mfg.AM.Part.RotationAngleType@endlink) </param>
    def SetRotationAngle(self, rotationAngle: Part.RotationAngleType) -> None:
        """
         Sets the rotation angle on the part 
        """
        pass
    
    ##  Sets the given profile as the default profile on the part 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="tagSupportProfile"> (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) </param>
    def SetSupportProfile(self, tagSupportProfile: SupportProfile) -> None:
        """
         Sets the given profile as the default profile on the part 
        """
        pass
    
    ##  Removes the part from the group it is in
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Ungroup(self) -> None:
        """
         Removes the part from the group it is in
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a @link Mfg::AM::PatternAMPartBuilder Mfg::AM::PatternAMPartBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreatePatternAMPartBuilder  NXOpen::Mfg::AM::ApplicationManager::CreatePatternAMPartBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.XOnPathSpacing.NCopies.Value </term> <description> 
##  
## 2 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.XOnPathSpacing.SpaceType </term> <description> 
##  
## Offset </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.XPathOption </term> <description> 
##  
## Offset </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.YDirectionOption </term> <description> 
##  
## Section </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.YOnPathSpacing.NCopies.Value </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.YPathOption </term> <description> 
##  
## Offset </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.YSpacing.NCopies.Value </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.YSpacing.PitchDistance.Value </term> <description> 
##  
## 10 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.YSpacing.SpaceType </term> <description> 
##  
## Offset </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.AlongPathDefinition.YSpacing.SpanDistance.Value </term> <description> 
##  
## 100 (millimeters part), 10 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.AngularSpacing.NCopies.Value </term> <description> 
##  
## 12 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.AngularSpacing.PitchAngle.Value </term> <description> 
##  
## 30 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.AngularSpacing.PitchDistance.Value </term> <description> 
##  
## 10 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.AngularSpacing.SpaceType </term> <description> 
##  
## Offset </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.AngularSpacing.SpanAngle.Value </term> <description> 
##  
## 360 (millimeters part), 360 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.AngularSpacing.UsePitchOption </term> <description> 
##  
## Angle </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.CreateLastStaggered </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.HorizontalRef.RotationAngle.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.IncludeSeedToggle </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.RadialSpacing.NCopies.Value </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.CircularDefinition.StaggerType </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.AnglePitch.Value </term> <description> 
##  
## 30 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.CountOfInstances.Value </term> <description> 
##  
## 6 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.DirectionType </term> <description> 
##  
## Righthand </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.DistancePitch.Value </term> <description> 
##  
## 10 (millimeters part), 0.4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.HelixPitch.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.HelixSpan.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.NumberOfTurns.Value </term> <description> 
##  
## 2 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.HelixDefinition.SizeOption </term> <description> 
##  
## CountAngleDistance </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternFill.FillMargin.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternFill.FillOptions </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternFill.SimplifiedBoundaryToggle </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.AlongOrientationOption </term> <description> 
##  
## NormalToPath </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.CircularOrientationOption </term> <description> 
##  
## FollowPattern </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.FollowFaceProjDirOption </term> <description> 
##  
## PatternPlaneNormal </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.GeneralOrientationOption </term> <description> 
##  
## Fixed </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.HelixOrientationOption </term> <description> 
##  
## FollowPattern </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.LinearOrientationOption </term> <description> 
##  
## Fixed </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.MirrorOrientationOption </term> <description> 
##  
## FollowPattern </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.OrientationOption </term> <description> 
##  
## Fixed </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.PolygonOrientationOption </term> <description> 
##  
## FollowPattern </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternOrientation.SpiralOrientationOption </term> <description> 
##  
## FollowPattern </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PatternType </term> <description> 
##  
## Linear </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.NumberOfSides.Value </term> <description> 
##  
## 6 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.PolygonSizeOption </term> <description> 
##  
## Inscribed </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.PolygonSpacing.NCopies.Value </term> <description> 
##  
## 4 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.PolygonSpacing.PitchDistance.Value </term> <description> 
##  
## 25 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.PolygonSpacing.SpaceType </term> <description> 
##  
## Offset </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.PolygonSpacing.SpanAngle.Value </term> <description> 
##  
## 360 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.RadialSpacing.NCopies.Value </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.RadialSpacing.PitchDistance.Value </term> <description> 
##  
## 25 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.PolygonDefinition.RadialSpacing.SpanDistance.Value </term> <description> 
##  
## 100 (millimeters part), 4 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.RectangularDefinition.CreateLastStaggered </term> <description> 
##  
## true </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.RectangularDefinition.SimplifiedLayoutType </term> <description> 
##  
## Square </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.RectangularDefinition.StaggerType </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.RectangularDefinition.XSpacing.NCopies.Value </term> <description> 
##  
## 2 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.RectangularDefinition.YSpacing.NCopies.Value </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.SpiralDefinition.DirectionType </term> <description> 
##  
## Lefthand </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.SpiralDefinition.NumberOfTurns.Value </term> <description> 
##  
## 1 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.SpiralDefinition.RadialPitch.Value </term> <description> 
##  
## 50 (millimeters part), 2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.SpiralDefinition.SizeSpiralType </term> <description> 
##  
## NumberOfTurns </description> </item> 
## 
## <item><term> 
##  
## GeometryPatternDefinition.SpiralDefinition.TotalAngle.Value </term> <description> 
##  
## 360 (millimeters part), 360 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class PatternAMPartBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.PatternAMPartBuilder</ja_class>. """


    ##  Represents pattern type.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Component</term><description> 
    ## </description> </item><item><term> 
    ## Geometry</term><description> 
    ## </description> </item></list>
    class PatternType(Enum):
        """
        Members Include: <Component> <Geometry>
        """
        Component: int
        Geometry: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PatternAMPartBuilder.PatternType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Associative
    ##  Returns the associative option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def Associative(self) -> bool:
        """
        Getter for property: (bool) Associative
         Returns the associative option   
            
         
        """
        pass
    
    ## Setter for property: (bool) Associative

    ##  Returns the associative option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Associative.setter
    def Associative(self, associative: bool):
        """
        Setter for property: (bool) Associative
         Returns the associative option   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyThreads
    ##  Returns the copy Threads   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def CopyThreads(self) -> bool:
        """
        Getter for property: (bool) CopyThreads
         Returns the copy Threads   
            
         
        """
        pass
    
    ## Setter for property: (bool) CopyThreads

    ##  Returns the copy Threads   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @CopyThreads.setter
    def CopyThreads(self, copyThreads: bool):
        """
        Setter for property: (bool) CopyThreads
         Returns the copy Threads   
            
         
        """
        pass
    
    ## Getter for property: (bool) DynamicPosition
    ##  Returns the dynamic Position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def DynamicPosition(self) -> bool:
        """
        Getter for property: (bool) DynamicPosition
         Returns the dynamic Position   
            
         
        """
        pass
    
    ## Setter for property: (bool) DynamicPosition

    ##  Returns the dynamic Position   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DynamicPosition.setter
    def DynamicPosition(self, dynamicPosition: bool):
        """
        Setter for property: (bool) DynamicPosition
         Returns the dynamic Position   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.PatternDefinition NXOpen.GeometricUtilities.PatternDefinition@endlink) GeometryPatternDefinition
    ##  Returns the Pattern Defintion service for pattern geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.PatternDefinition
    @property
    def GeometryPatternDefinition(self) -> NXOpen.GeometricUtilities.PatternDefinition:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.PatternDefinition NXOpen.GeometricUtilities.PatternDefinition@endlink) GeometryPatternDefinition
         Returns the Pattern Defintion service for pattern geometry   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PartSelected
    ##  Returns the methods gets the selected part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def PartSelected(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PartSelected
         Returns the methods gets the selected part   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.PatternDefinition NXOpen.GeometricUtilities.PatternDefinition@endlink) PatternDefinition
    ##  Returns the Pattern Defintion service   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.PatternDefinition
    @property
    def PatternDefinition(self) -> NXOpen.GeometricUtilities.PatternDefinition:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.PatternDefinition NXOpen.GeometricUtilities.PatternDefinition@endlink) PatternDefinition
         Returns the Pattern Defintion service   
            
         
        """
        pass
    
    ## Getter for property: (@link PatternAMPartBuilder.PatternType NXOpen.Mfg.AM.PatternAMPartBuilder.PatternType@endlink) PatternOptionType
    ##  Returns the pattern type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return PatternAMPartBuilder.PatternType
    @property
    def PatternOptionType(self) -> PatternAMPartBuilder.PatternType:
        """
        Getter for property: (@link PatternAMPartBuilder.PatternType NXOpen.Mfg.AM.PatternAMPartBuilder.PatternType@endlink) PatternOptionType
         Returns the pattern type   
            
         
        """
        pass
    
    ## Setter for property: (@link PatternAMPartBuilder.PatternType NXOpen.Mfg.AM.PatternAMPartBuilder.PatternType@endlink) PatternOptionType

    ##  Returns the pattern type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @PatternOptionType.setter
    def PatternOptionType(self, patternType: PatternAMPartBuilder.PatternType):
        """
        Setter for property: (@link PatternAMPartBuilder.PatternType NXOpen.Mfg.AM.PatternAMPartBuilder.PatternType@endlink) PatternOptionType
         Returns the pattern type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder@endlink) ReferencePoint
    ##  Returns the reference point service.  
    ##   
    ##             It contains the point of reference that will be used as the origin for creating pattern based transformations.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder
    @property
    def ReferencePoint(self) -> NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder NXOpen.GeometricUtilities.PatternReferencePointServiceBuilder@endlink) ReferencePoint
         Returns the reference point service.  
          
                    It contains the point of reference that will be used as the origin for creating pattern based transformations.   
         
        """
        pass
    
import NXOpen
##  Represents the Additive Manufacturing Printer Service  <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class PrinterManager(NXOpen.Object): 
    """ Represents the Additive Manufacturing Printer Service """


    ##  Retrieves a printer by name 
    ##  @return pPrinter (@link Printer NXOpen.Mfg.AM.Printer@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## <param name="printerName"> (str) </param>
    def GetPrinter(printerName: str) -> Printer:
        """
         Retrieves a printer by name 
         @return pPrinter (@link Printer NXOpen.Mfg.AM.Printer@endlink): .
        """
        pass
    
    ##  Retrieves the available 3D printers 
    ##  @return pPrinter (@link Printer List[NXOpen.Mfg.AM.Printer]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetPrinters() -> List[Printer]:
        """
         Retrieves the available 3D printers 
         @return pPrinter (@link Printer List[NXOpen.Mfg.AM.Printer]@endlink): .
        """
        pass
    
import NXOpen
##  Printer 
## 
##   <br>  Created in NX11.0.1  <br> 

class Printer(NXOpen.TransientObject): 
    """ Printer """


    ##  Free the handle to the printer 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free the handle to the printer 
        """
        pass
    
    ##  Gets the printer build tray dimensions 
    ##  @return A tuple consisting of (isBox, dLength, dWidth, dDiameter, dHeight, dTrayHeight). 
    ##  - isBox is: bool.
    ##  - dLength is: float.
    ##  - dWidth is: float.
    ##  - dDiameter is: float.
    ##  - dHeight is: float.
    ##  - dTrayHeight is: float.

    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetDimensions(self) -> Tuple[bool, float, float, float, float, float]:
        """
         Gets the printer build tray dimensions 
         @return A tuple consisting of (isBox, dLength, dWidth, dDiameter, dHeight, dTrayHeight). 
         - isBox is: bool.
         - dLength is: float.
         - dWidth is: float.
         - dDiameter is: float.
         - dHeight is: float.
         - dTrayHeight is: float.

        """
        pass
    
    ##  Returns the printer identifier 
    ##  @return printerId (str):  .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetIdentifier(self) -> str:
        """
         Returns the printer identifier 
         @return printerId (str):  .
        """
        pass
    
    ##  Returns the printer name 
    ##  @return printerName (str):  .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetName(self) -> str:
        """
         Returns the printer name 
         @return printerName (str):  .
        """
        pass
    
    ##  Gets the printer build tray origin 
    ##  @return origin (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def GetOrigin(self) -> NXOpen.Point3d:
        """
         Gets the printer build tray origin 
         @return origin (@link NXOpen.Point3d NXOpen.Point3d@endlink): .
        """
        pass
    
    ##  Returns the printer status 
    ##  @return printerStatus (str):  .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetStatus(self) -> str:
        """
         Returns the printer status 
         @return printerStatus (str):  .
        """
        pass
    
import NXOpen
##  Print Job  
## 
##   <br>  Created in NX11.0.1  <br> 

class PrintJob(NXOpen.TransientObject): 
    """ Print Job  """


    ##  Free the handle to the print job 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free the handle to the print job 
        """
        pass
    
    ##  Returns the status message string 
    ##  @return statusMessage (str):  .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetStatusMessage(self) -> str:
        """
         Returns the status message string 
         @return statusMessage (str):  .
        """
        pass
    
import NXOpen
##  Interface for Services Profile Library objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ApplicationManager NXOpen::Mfg::AM::ApplicationManager@endlink .  <br> 
## 
##   <br>  Created in NX11.0.2  <br> 

class ProfileLibrary(Library): 
    """ Interface for Services Profile Library objects """


    ## Getter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) Active
    ##  Returns the active support profile   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SupportProfile
    @property
    def Active(self) -> SupportProfile:
        """
        Getter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) Active
         Returns the active support profile   
            
         
        """
        pass
    
    ## Setter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) Active

    ##  Returns the active support profile   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Active.setter
    def Active(self, profile: SupportProfile):
        """
        Setter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) Active
         Returns the active support profile   
            
         
        """
        pass
    
    ##  Adds a profile to the library 
    ##  @return newProfile (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink):  the new support profile .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def AddSupportProfile(self) -> SupportProfile:
        """
         Adds a profile to the library 
         @return newProfile (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink):  the new support profile .
        """
        pass
    
    ##  Remove a Library component from the Profile Library
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Profiles do not contain other profiles anymore  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pChildProfileLib"> (@link ProfileLibrary NXOpen.Mfg.AM.ProfileLibrary@endlink)  the folder to be removed </param>
    def DeleteLibraryFolder(self, pChildProfileLib: ProfileLibrary) -> None:
        """
         Remove a Library component from the Profile Library
        """
        pass
    
    ##  Remove a Profile component from the Profile Library
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link Remove Remove@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pChildProfile"> (@link Profile NXOpen.Mfg.AM.Profile@endlink)  the component to be removed </param>
    def DeleteProfile(self, pChildProfile: Profile) -> None:
        """
         Remove a Profile component from the Profile Library
        """
        pass
    
    ##  Find a profile by its recorded id
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such partfeature exists.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Name of the profile to be found </param>
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
        """
         Find a profile by its recorded id
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  Object found, or null if no such partfeature exists.
        """
        pass
    
    ##  Gets the children Profile Objects of the Profile Library 
    ##  @return profiles (@link SupportProfile List[NXOpen.Mfg.AM.SupportProfile]@endlink):  the profiles .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetSupportProfiles(self) -> List[SupportProfile]:
        """
         Gets the children Profile Objects of the Profile Library 
         @return profiles (@link SupportProfile List[NXOpen.Mfg.AM.SupportProfile]@endlink):  the profiles .
        """
        pass
    
    ##  Remove a support profile
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="profile"> (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink)  the support profile to be removed </param>
    def Remove(self, profile: SupportProfile) -> None:
        """
         Remove a support profile
        """
        pass
    
import NXOpen
##  Interface for Services Profile objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ProfileObject NXOpen::Mfg::AM::ProfileObject@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class ProfileObject(NXOpen.NXObject): 
    """ Interface for Services Profile objects """


    ##  Deletes the profile object
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def Destroy(self) -> None:
        """
         Deletes the profile object
        """
        pass
    
    ##  Get child profile object of the given name 
    ##  @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="childSupportName"> (str) </param>
    def GetChild(self, childSupportName: str) -> ProfileObject:
        """
         Get child profile object of the given name 
         @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::Mfg::AM::ProfileObject NXOpen::Mfg::AM::ProfileObject@endlink  with the given (guid) identifier as recorded in a journal.
    ##             This method will search for the profile with given GUID from the given profile object. 
    ##             The GUID used for the searching is available in the am.xml file.
    ##  @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pChildGuid"> (str) </param>
    ## <param name="recursive"> (bool) </param>
    def GetChildByGuid(self, pChildGuid: str, recursive: bool) -> ProfileObject:
        """
         Finds the @link NXOpen::Mfg::AM::ProfileObject NXOpen::Mfg::AM::ProfileObject@endlink  with the given (guid) identifier as recorded in a journal.
                    This method will search for the profile with given GUID from the given profile object. 
                    The GUID used for the searching is available in the am.xml file.
         @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink): .
        """
        pass
    
    ##  Renames the profile object
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link NXObject::SetName NXObject::SetName@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="newPropertyName"> (str) </param>
    def RenameProfileObject(self, newPropertyName: str) -> None:
        """
         Renames the profile object
        """
        pass
    
##  Interface for Services Profile Library objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::Profile NXOpen::Mfg::AM::Profile@endlink .  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class ProfileSupport(ProfileObject): 
    """ Interface for Services Profile Library objects """


    ##  Sets the default profile support within the support library. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def SetAsDefault(self) -> None:
        """
         Sets the default profile support within the support library. 
        """
        pass
    
##  Interface for Services Profile objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ProfileLibrary NXOpen::Mfg::AM::ProfileLibrary@endlink .  <br> 
## 
##   <br>  Created in NX11.0.2  <br> 
## 
##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

class Profile(ProfileObject): 
    """ Interface for Services Profile objects """


    ##  Get child profile object support of the given Profile
    ##  @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="childSupportName"> (str) </param>
    def GetChildSupport(self, childSupportName: str) -> ProfileObject:
        """
         Get child profile object support of the given Profile
         @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  .
        """
        pass
    
    ##  Get parent library of the given Profile
    ##  @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

    ## License requirements: None.
    def GetLibrary(self) -> ProfileObject:
        """
         Get parent library of the given Profile
         @return pParentLib (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  .
        """
        pass
    
    ##  Get the Profile Name
    ##  @return profileName (str):  .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

    ## License requirements: None.
    def GetName(self) -> str:
        """
         Get the Profile Name
         @return profileName (str):  .
        """
        pass
    
    ##  Gets the Profile children
    ##  @return childrenProfile (@link Profile List[NXOpen.Mfg.AM.Profile]@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

    ## License requirements: None.
    def GetProfiles(self) -> List[Profile]:
        """
         Gets the Profile children
         @return childrenProfile (@link Profile List[NXOpen.Mfg.AM.Profile]@endlink):  .
        """
        pass
    
    ##  Set the name of the Profile 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="newName"> (str) </param>
    def SetName(self, newName: str) -> None:
        """
         Set the name of the Profile 
        """
        pass
    
import NXOpen
##  Represents a @link Mfg::AM::RepositionPartBuilder Mfg::AM::RepositionPartBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreateRepositionPartBuilder  NXOpen::Mfg::AM::ApplicationManager::CreateRepositionPartBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class RepositionPartBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.RepositionPartBuilder</ja_class>. """


    ##  Represents position type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Rotate</term><description> 
    ##  rotate </description> </item><item><term> 
    ## Translate</term><description> 
    ##  translate  </description> </item><item><term> 
    ## Align</term><description> 
    ##  align </description> </item></list>
    class Method(Enum):
        """
        Members Include: <Rotate> <Translate> <Align>
        """
        Rotate: int
        Translate: int
        Align: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents rotation reference axis. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ##  XC-axis </description> </item><item><term> 
    ## Y</term><description> 
    ##  YC-axis </description> </item><item><term> 
    ## Z</term><description> 
    ##  ZC-axis </description> </item><item><term> 
    ## NegativeX</term><description> 
    ##  -XC-axis </description> </item><item><term> 
    ## NegativeY</term><description> 
    ##  -YC-axis </description> </item><item><term> 
    ## NegativeZ</term><description> 
    ##  -ZC-axis </description> </item><item><term> 
    ## Dynamic</term><description> 
    ##  Dynamic </description> </item><item><term> 
    ## Viewdirection</term><description> 
    ##  View Direction </description> </item></list>
    class RotateAxisType(Enum):
        """
        Members Include: <X> <Y> <Z> <NegativeX> <NegativeY> <NegativeZ> <Dynamic> <Viewdirection>
        """
        X: int
        Y: int
        Z: int
        NegativeX: int
        NegativeY: int
        NegativeZ: int
        Dynamic: int
        Viewdirection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.RotateAxisType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents reference point type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OneByOne</term><description> 
    ##  One by one </description> </item><item><term> 
    ## AsAGroup</term><description> 
    ##  As a group </description> </item></list>
    class TranslatePartsType(Enum):
        """
        Members Include: <OneByOne> <AsAGroup>
        """
        OneByOne: int
        AsAGroup: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.TranslatePartsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents reference object type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BuildPlate</term><description> 
    ##  Build Plate </description> </item><item><term> 
    ## BuildTrayCenter</term><description> 
    ##  Build Tray Center </description> </item><item><term> 
    ## FaceOrPlane</term><description> 
    ##  Planar object - Face or plane </description> </item></list>
    class TranslateToType(Enum):
        """
        Members Include: <BuildPlate> <BuildTrayCenter> <FaceOrPlane>
        """
        BuildPlate: int
        BuildTrayCenter: int
        FaceOrPlane: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RepositionPartBuilder.TranslateToType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Angle
    ##  Returns the angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Angle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Angle
         Returns the angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
    ##  Returns the distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
         Returns the distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) ManipulatorOffsetOrigin
    ##  Returns the offset origin point of manipulator   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def ManipulatorOffsetOrigin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) ManipulatorOffsetOrigin
         Returns the offset origin point of manipulator   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) ManipulatorOffsetOrigin

    ##  Returns the offset origin point of manipulator   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ManipulatorOffsetOrigin.setter
    def ManipulatorOffsetOrigin(self, manipulatorOrigin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) ManipulatorOffsetOrigin
         Returns the offset origin point of manipulator   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ManipulatorRotationMatrix
    ##  Returns the rotation matrix of manipulator   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Matrix3x3
    @property
    def ManipulatorRotationMatrix(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ManipulatorRotationMatrix
         Returns the rotation matrix of manipulator   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ManipulatorRotationMatrix

    ##  Returns the rotation matrix of manipulator   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ManipulatorRotationMatrix.setter
    def ManipulatorRotationMatrix(self, manipulatorMatrix: NXOpen.Matrix3x3):
        """
        Setter for property: (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) ManipulatorRotationMatrix
         Returns the rotation matrix of manipulator   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ObjectsToReposition
    ##  Returns the objects to reposition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def ObjectsToReposition(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) ObjectsToReposition
         Returns the objects to reposition   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PartFaces
    ##  Returns the part face selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def PartFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PartFaces
         Returns the part face selection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PlanarObject
    ##  Returns the planar object selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def PlanarObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PlanarObject
         Returns the planar object selection   
            
         
        """
        pass
    
    ## Getter for property: (@link RepositionPartBuilder.Method NXOpen.Mfg.AM.RepositionPartBuilder.Method@endlink) PositionMethod
    ##  Returns the position type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RepositionPartBuilder.Method
    @property
    def PositionMethod(self) -> RepositionPartBuilder.Method:
        """
        Getter for property: (@link RepositionPartBuilder.Method NXOpen.Mfg.AM.RepositionPartBuilder.Method@endlink) PositionMethod
         Returns the position type   
            
         
        """
        pass
    
    ## Setter for property: (@link RepositionPartBuilder.Method NXOpen.Mfg.AM.RepositionPartBuilder.Method@endlink) PositionMethod

    ##  Returns the position type   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @PositionMethod.setter
    def PositionMethod(self, positionMethod: RepositionPartBuilder.Method):
        """
        Setter for property: (@link RepositionPartBuilder.Method NXOpen.Mfg.AM.RepositionPartBuilder.Method@endlink) PositionMethod
         Returns the position type   
            
         
        """
        pass
    
    ## Getter for property: (@link RepositionPartBuilder.RotateAxisType NXOpen.Mfg.AM.RepositionPartBuilder.RotateAxisType@endlink) RotationAxisType
    ##  Returns the rotation axis   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RepositionPartBuilder.RotateAxisType
    @property
    def RotationAxisType(self) -> RepositionPartBuilder.RotateAxisType:
        """
        Getter for property: (@link RepositionPartBuilder.RotateAxisType NXOpen.Mfg.AM.RepositionPartBuilder.RotateAxisType@endlink) RotationAxisType
         Returns the rotation axis   
            
         
        """
        pass
    
    ## Setter for property: (@link RepositionPartBuilder.RotateAxisType NXOpen.Mfg.AM.RepositionPartBuilder.RotateAxisType@endlink) RotationAxisType

    ##  Returns the rotation axis   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @RotationAxisType.setter
    def RotationAxisType(self, rotationAxis: RepositionPartBuilder.RotateAxisType):
        """
        Setter for property: (@link RepositionPartBuilder.RotateAxisType NXOpen.Mfg.AM.RepositionPartBuilder.RotateAxisType@endlink) RotationAxisType
         Returns the rotation axis   
            
         
        """
        pass
    
    ## Getter for property: (@link RepositionPartBuilder.TranslatePartsType NXOpen.Mfg.AM.RepositionPartBuilder.TranslatePartsType@endlink) TranslatePartsOption
    ##  Returns the reference point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RepositionPartBuilder.TranslatePartsType
    @property
    def TranslatePartsOption(self) -> RepositionPartBuilder.TranslatePartsType:
        """
        Getter for property: (@link RepositionPartBuilder.TranslatePartsType NXOpen.Mfg.AM.RepositionPartBuilder.TranslatePartsType@endlink) TranslatePartsOption
         Returns the reference point   
            
         
        """
        pass
    
    ## Setter for property: (@link RepositionPartBuilder.TranslatePartsType NXOpen.Mfg.AM.RepositionPartBuilder.TranslatePartsType@endlink) TranslatePartsOption

    ##  Returns the reference point   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TranslatePartsOption.setter
    def TranslatePartsOption(self, referencePoint: RepositionPartBuilder.TranslatePartsType):
        """
        Setter for property: (@link RepositionPartBuilder.TranslatePartsType NXOpen.Mfg.AM.RepositionPartBuilder.TranslatePartsType@endlink) TranslatePartsOption
         Returns the reference point   
            
         
        """
        pass
    
    ## Getter for property: (@link RepositionPartBuilder.TranslateToType NXOpen.Mfg.AM.RepositionPartBuilder.TranslateToType@endlink) TranslateToOption
    ##  Returns the reference object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return RepositionPartBuilder.TranslateToType
    @property
    def TranslateToOption(self) -> RepositionPartBuilder.TranslateToType:
        """
        Getter for property: (@link RepositionPartBuilder.TranslateToType NXOpen.Mfg.AM.RepositionPartBuilder.TranslateToType@endlink) TranslateToOption
         Returns the reference object   
            
         
        """
        pass
    
    ## Setter for property: (@link RepositionPartBuilder.TranslateToType NXOpen.Mfg.AM.RepositionPartBuilder.TranslateToType@endlink) TranslateToOption

    ##  Returns the reference object   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @TranslateToOption.setter
    def TranslateToOption(self, referenceObject: RepositionPartBuilder.TranslateToType):
        """
        Setter for property: (@link RepositionPartBuilder.TranslateToType NXOpen.Mfg.AM.RepositionPartBuilder.TranslateToType@endlink) TranslateToOption
         Returns the reference object   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a list of objects on a selection list.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectPartList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""


    ## Getter for property: (bool) DuplicatesAllowed
    ##  Returns whether duplicate objects are allowed in the selection list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    
    ## Getter for property: (int) Size
    ##  Returns the number of objects in the list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    
    ##  Adds an object to the list
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="objectValue"> (@link Part NXOpen.Mfg.AM.Part@endlink)  object to add </param>
    @overload
    def Add(self, objectValue: Part) -> bool:
        """
         Adds an object to the list
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects with views to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Part List[NXOpen.Mfg.AM.Part]@endlink)  objects to add </param>
    ## <param name="views"> (@link NXOpen.View List[NXOpen.View]@endlink)  views for the objects </param>
    def AddWithViews(self, objects: List[Part], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="objects"> (@link Part List[NXOpen.Mfg.AM.Part]@endlink)  objects to add </param>
    @overload
    def Add(self, objects: List[Part]) -> bool:
        """
         Adds a set of objects to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the objects from a SelectionMethod to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the object with the objects view and objects point
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="selection"> (@link Part NXOpen.Mfg.AM.Part@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def Add(self, selection: Part, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Part NXOpen.Mfg.AM.Part@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link Part NXOpen.Mfg.AM.Part@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Part, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Part, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObjectList::Add NXOpen::SelectObjectList::Add@endlink .  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="selection"> (@link Part NXOpen.Mfg.AM.Part@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def Add(self, selection: Part, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Removes all items from the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    
    ##  Returns whether the specified object is already in the list or not.
    ##     
    ##  @return list_contains (bool):  true if object is in the list, false otherwise .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectValue"> (@link Part NXOpen.Mfg.AM.Part@endlink)  object to check </param>
    def Contains(self, objectValue: Part) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         @return list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    
    ##  Returns the list of objects in the selection list.
    ##     
    ##  @return objects (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetArray(self) -> List[Part]:
        """
         Returns the list of objects in the selection list.
            
         @return objects (@link Part List[NXOpen.Mfg.AM.Part]@endlink):  items in list .
        """
        pass
    
    ##  Returns the list of SelectObjects in the selection list.
    ##     
    ##  @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="objectValue"> (@link Part NXOpen.Mfg.AM.Part@endlink)  Object to remove </param>
    @overload
    def Remove(self, objectValue: Part) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified objects from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Part List[NXOpen.Mfg.AM.Part]@endlink)  Objects to remove </param>
    def RemoveArray(self, objects: List[Part]) -> bool:
        """
         Remove specified objects from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object / view was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="objectValue"> (@link Part NXOpen.Mfg.AM.Part@endlink)  Object to remove </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  with this view</param>
    @overload
    def Remove(self, objectValue: Part, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object / view was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Part NXOpen.Mfg.AM.Part@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link Part NXOpen.Mfg.AM.Part@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Part, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Part, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Removes the objects from a SelectionMethod from the list
    ##     
    ##  @return removed (bool):  True if successfully removed all objects from the list;
    ##                                     False if there was at least one object that was not a
    ##                                     member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectPartList NXOpen.Mfg.AM.SelectPartList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         @return removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    
    ##  Sets the list of objects in the selection list. This will clear any existing
    ##     items in the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Part List[NXOpen.Mfg.AM.Part]@endlink)  items to put in the list</param>
    def SetArray(self, objects: List[Part]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a list of objects on a selection list.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectSupportList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""


    ## Getter for property: (bool) DuplicatesAllowed
    ##  Returns whether duplicate objects are allowed in the selection list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def DuplicatesAllowed(self) -> bool:
        """
        Getter for property: (bool) DuplicatesAllowed
         Returns whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    
    ## Getter for property: (int) Size
    ##  Returns the number of objects in the list.  
    ##   
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Size(self) -> int:
        """
        Getter for property: (int) Size
         Returns the number of objects in the list.  
          
              
         
        """
        pass
    
    ##  Adds an object to the list
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="objectValue"> (@link Support NXOpen.Mfg.AM.Support@endlink)  object to add </param>
    @overload
    def Add(self, objectValue: Support) -> bool:
        """
         Adds an object to the list
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects with views to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Support List[NXOpen.Mfg.AM.Support]@endlink)  objects to add </param>
    ## <param name="views"> (@link NXOpen.View List[NXOpen.View]@endlink)  views for the objects </param>
    def AddWithViews(self, objects: List[Support], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds a set of objects to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="objects"> (@link Support List[NXOpen.Mfg.AM.Support]@endlink)  objects to add </param>
    @overload
    def Add(self, objects: List[Support]) -> bool:
        """
         Adds a set of objects to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the objects from a SelectionMethod to the list
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Add(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Adds the objects from a SelectionMethod to the list
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Adds the object with the objects view and objects point
    ##     
    ##  @return added (bool):  True if successfully added to list;
    ##                                   False if the object was already a member
    ##                                   of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="selection"> (@link Support NXOpen.Mfg.AM.Support@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def Add(self, selection: Support, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         @return added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Support NXOpen.Mfg.AM.Support@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link Support NXOpen.Mfg.AM.Support@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Support, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Support, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return added (bool):  True if successfully added all objects to the list;
    ##                                   False if there was at least one object that was already a
    ##                                   member of the list and duplicates are not allowed .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObjectList::Add NXOpen::SelectObjectList::Add@endlink .  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="selection"> (@link Support NXOpen.Mfg.AM.Support@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def Add(self, selection: Support, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
        """
         The object being selected with CAE set object information.
            
         @return added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    
    ##  Removes all items from the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Clear(self) -> None:
        """
         Removes all items from the list.
            
        """
        pass
    
    ##  Returns whether the specified object is already in the list or not.
    ##     
    ##  @return list_contains (bool):  true if object is in the list, false otherwise .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectValue"> (@link Support NXOpen.Mfg.AM.Support@endlink)  object to check </param>
    def Contains(self, objectValue: Support) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         @return list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    
    ##  Returns the list of objects in the selection list.
    ##     
    ##  @return objects (@link Support List[NXOpen.Mfg.AM.Support]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetArray(self) -> List[Support]:
        """
         Returns the list of objects in the selection list.
            
         @return objects (@link Support List[NXOpen.Mfg.AM.Support]@endlink):  items in list .
        """
        pass
    
    ##  Returns the list of SelectObjects in the selection list.
    ##     
    ##  @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="objectValue"> (@link Support NXOpen.Mfg.AM.Support@endlink)  Object to remove </param>
    @overload
    def Remove(self, objectValue: Support) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified objects from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Support List[NXOpen.Mfg.AM.Support]@endlink)  Objects to remove </param>
    def RemoveArray(self, objects: List[Support]) -> bool:
        """
         Remove specified objects from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object / view was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="objectValue"> (@link Support NXOpen.Mfg.AM.Support@endlink)  Object to remove </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  with this view</param>
    @overload
    def Remove(self, objectValue: Support, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object / view was not a member of the list .
        """
        pass
    
    ##  Remove specified object from list.
    ##     
    ##  @return removed (bool):  True if successfully removed from list;
    ##                                     False if the object was not a member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Support NXOpen.Mfg.AM.Support@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) first  selected object point</param>
    ## <param name="selection2"> (@link Support NXOpen.Mfg.AM.Support@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink) second  selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Support, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Support, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         Remove specified object from list.
            
         @return removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    
    ##  Removes the objects from a SelectionMethod from the list
    ##     
    ##  @return removed (bool):  True if successfully removed all objects from the list;
    ##                                     False if there was at least one object that was not a
    ##                                     member of the list .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) </param>
    ## <param name="input_selection_method"> (@link NXOpen.SelectionMethod NXOpen.SelectionMethod@endlink)  selection method containing objects to add </param>
    @overload
    def Remove(self, input_selection_method: NXOpen.SelectionMethod) -> bool:
        """
         Removes the objects from a SelectionMethod from the list
            
         @return removed (bool):  True if successfully removed all objects from the list;
                                            False if there was at least one object that was not a
                                            member of the list .
        """
        pass
    
    ##  Sets the list of objects in the selection list. This will clear any existing
    ##     items in the list.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link Support List[NXOpen.Mfg.AM.Support]@endlink)  items to put in the list</param>
    def SetArray(self, objects: List[Support]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a single object selection.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectSupport(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link Support NXOpen.Mfg.AM.Support@endlink) Value
    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return Support
    @property
    def Value(self) -> Support:
        """
        Getter for property: (@link Support NXOpen.Mfg.AM.Support@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link Support NXOpen.Mfg.AM.Support@endlink) Value

    ##  Returns the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: Support):
        """
        Setter for property: (@link Support NXOpen.Mfg.AM.Support@endlink) Value
         Returns the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link Support NXOpen.Mfg.AM.Support@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Support, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link Support NXOpen.Mfg.AM.Support@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link Support NXOpen.Mfg.AM.Support@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link Support NXOpen.Mfg.AM.Support@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Support, NXOpen.View, NXOpen.Point3d, Support, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link Support NXOpen.Mfg.AM.Support@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link Support NXOpen.Mfg.AM.Support@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link Support NXOpen.Mfg.AM.Support@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) </param>
    @overload
    def GetValue(self) -> Tuple[Support, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link Support NXOpen.Mfg.AM.Support@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) </param>
    ## <param name="selection"> (@link Support NXOpen.Mfg.AM.Support@endlink)  selected object </param>
    ## <param name="view"> (@link NXOpen.View NXOpen.View@endlink)  selected object view</param>
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  selected object point</param>
    @overload
    def SetValue(self, selection: Support, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) </param>
    ## <param name="snap_type"> (@link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink)   snap point type</param>
    ## <param name="selection1"> (@link Support NXOpen.Mfg.AM.Support@endlink)  first selected object </param>
    ## <param name="view1"> (@link NXOpen.View NXOpen.View@endlink)  first selected object view</param>
    ## <param name="point1"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  first selected object point</param>
    ## <param name="selection2"> (@link Support NXOpen.Mfg.AM.Support@endlink)  second selected object </param>
    ## <param name="view2"> (@link NXOpen.View NXOpen.View@endlink)  second selected object view</param>
    ## <param name="point2"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  second selected object point</param>
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Support, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Support, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
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
    ## <param name="select_object"> (@link SelectSupport NXOpen.Mfg.AM.SelectSupport@endlink) </param>
    ## <param name="selection"> (@link Support NXOpen.Mfg.AM.Support@endlink)  selected object </param>
    ## <param name="cae_sub_type"> (@link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink)  CAE set object sub type</param>
    ## <param name="cae_sub_id"> (int)  CAE set object sub id</param>
    @overload
    def SetValue(self, selection: Support, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
##  Interface for Model Build Tray objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::Part::GetSerialNumbers NXOpen::Mfg::AM::Part::GetSerialNumbers@endlink   <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class SerialNumber(PartRegion): 
    """ Interface for Model Build Tray objects """


    ##  Clear 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_print_mark (" NX Additive Print Mark")
    def Clear(self) -> None:
        """
         Clear 
        """
        pass
    
    ##  Generate 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_print_mark (" NX Additive Print Mark")
    def Generate(self) -> None:
        """
         Generate 
        """
        pass
    
    ##  Get Serial Number Text 
    ##  @return printMarkText (str): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    def GetText(self) -> str:
        """
         Get Serial Number Text 
         @return printMarkText (str): .
        """
        pass
    
    ##  Get Usable Label of Serial Number 
    ##  @return usageLabel (str): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: am_pb_print_mark (" NX Additive Print Mark")
    def GetUsageLabel(self) -> str:
        """
         Get Usable Label of Serial Number 
         @return usageLabel (str): .
        """
        pass
    
    ##  Set Serial Number Text 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: am_pb_print_mark (" NX Additive Print Mark")
    ## 
    ## <param name="printMarkText"> (str) </param>
    def SetText(self, printMarkText: str) -> None:
        """
         Set Serial Number Text 
        """
        pass
    
import NXOpen
##  Represents a @link Mfg::AM::SimulationSupport Mfg::AM::SimulationSupport@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::SimApplicationManager::GetSupportBuilder  NXOpen::Mfg::AM::SimApplicationManager::GetSupportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class SimSupportBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.SimulationSupport</ja_class> builder """


    ## Getter for property: (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) Supports
    ##  Returns the support selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectSupportList
    @property
    def Supports(self) -> SelectSupportList:
        """
        Getter for property: (@link SelectSupportList NXOpen.Mfg.AM.SelectSupportList@endlink) Supports
         Returns the support selection   
            
         
        """
        pass
    
    ##  Get the faces that failed during the support generation 
    ##  @return pptFailedFaces (@link NXOpen.Face List[NXOpen.Face]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def GetFailedFaces(self) -> List[NXOpen.Face]:
        """
         Get the faces that failed during the support generation 
         @return pptFailedFaces (@link NXOpen.Face List[NXOpen.Face]@endlink): .
        """
        pass
    
import NXOpen
##  Additive Manufacturing Surface Region  <br>   <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class SimulationSupport(NXOpen.NXObject): 
    """ Additive Manufacturing Surface Region """


    ##  Returns the simulation support geometry 
    ##  @return bodies (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetBodies(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the simulation support geometry 
         @return bodies (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Returns the part body for this support 
    ##  @return tagGeometry (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetPartBody(self) -> NXOpen.DisplayableObject:
        """
         Returns the part body for this support 
         @return tagGeometry (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
        """
        pass
    
    ##  Returns true if the simulation support is out of date 
    ##  @return outOfDate (bool): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def IsOutOfDate(self) -> bool:
        """
         Returns true if the simulation support is out of date 
         @return outOfDate (bool): .
        """
        pass
    
    ##  Sets the simulation support geometry 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="bodies"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink) </param>
    def SetBodies(self, bodies: List[NXOpen.DisplayableObject]) -> None:
        """
         Sets the simulation support geometry 
        """
        pass
    
import NXOpen
##  Used to create or edit a @link Mfg::AM::Sinterbox Mfg::AM::Sinterbox@endlink   <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreateSinterboxBuilder  NXOpen::Mfg::AM::ApplicationManager::CreateSinterboxBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BoundaryType </term> <description> 
##  
## PartSelection </description> </item> 
## 
## <item><term> 
##  
## EdgeBlendValue.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## LatticeType </term> <description> 
##  
## GridAndRod </description> </item> 
## 
## <item><term> 
##  
## PartOffsetDistance.Value </term> <description> 
##  
## 5 (millimeters part), 0.25 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RodDiameter.Value </term> <description> 
##  
## 1.5 (millimeters part), 0.0625 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RodLength.Value </term> <description> 
##  
## 10 (millimeters part), 2.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RodWidth.Value </term> <description> 
##  
## 1.5 (millimeters part), 0.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## ShapeType </term> <description> 
##  
## Box </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class SinterboxBuilder(NXOpen.Builder): 
    """ Used to create or edit a <ja_class>Mfg.AM.Sinterbox</ja_class> """


    ## Getter for property: (@link Sinterbox.AlignmentType NXOpen.Mfg.AM.Sinterbox.AlignmentType@endlink) AlignType
    ##  Returns the alignment of sinterbox   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return Sinterbox.AlignmentType
    @property
    def AlignType(self) -> Sinterbox.AlignmentType:
        """
        Getter for property: (@link Sinterbox.AlignmentType NXOpen.Mfg.AM.Sinterbox.AlignmentType@endlink) AlignType
         Returns the alignment of sinterbox   
            
         
        """
        pass
    
    ## Setter for property: (@link Sinterbox.AlignmentType NXOpen.Mfg.AM.Sinterbox.AlignmentType@endlink) AlignType

    ##  Returns the alignment of sinterbox   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @AlignType.setter
    def AlignType(self, alignmentType: Sinterbox.AlignmentType):
        """
        Setter for property: (@link Sinterbox.AlignmentType NXOpen.Mfg.AM.Sinterbox.AlignmentType@endlink) AlignType
         Returns the alignment of sinterbox   
            
         
        """
        pass
    
    ## Getter for property: (@link Sinterbox.Boundary NXOpen.Mfg.AM.Sinterbox.Boundary@endlink) BoundaryType
    ##  Returns the boundary type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return Sinterbox.Boundary
    @property
    def BoundaryType(self) -> Sinterbox.Boundary:
        """
        Getter for property: (@link Sinterbox.Boundary NXOpen.Mfg.AM.Sinterbox.Boundary@endlink) BoundaryType
         Returns the boundary type   
            
         
        """
        pass
    
    ## Setter for property: (@link Sinterbox.Boundary NXOpen.Mfg.AM.Sinterbox.Boundary@endlink) BoundaryType

    ##  Returns the boundary type   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @BoundaryType.setter
    def BoundaryType(self, boundary: Sinterbox.Boundary):
        """
        Setter for property: (@link Sinterbox.Boundary NXOpen.Mfg.AM.Sinterbox.Boundary@endlink) BoundaryType
         Returns the boundary type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color of sinterbox   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color of sinterbox   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color of sinterbox   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color of sinterbox   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeBlendValue
    ##  Returns the edge blend value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EdgeBlendValue(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EdgeBlendValue
         Returns the edge blend value   
            
         
        """
        pass
    
    ## Getter for property: (@link Sinterbox.Lattice NXOpen.Mfg.AM.Sinterbox.Lattice@endlink) LatticeType
    ##  Returns the lattice type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return Sinterbox.Lattice
    @property
    def LatticeType(self) -> Sinterbox.Lattice:
        """
        Getter for property: (@link Sinterbox.Lattice NXOpen.Mfg.AM.Sinterbox.Lattice@endlink) LatticeType
         Returns the lattice type   
            
         
        """
        pass
    
    ## Setter for property: (@link Sinterbox.Lattice NXOpen.Mfg.AM.Sinterbox.Lattice@endlink) LatticeType

    ##  Returns the lattice type   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application") OR nx_lattice_base (" NX Lattice Base"), am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application") OR nx_lattice_type1 (" NX Materialise Lattice")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @LatticeType.setter
    def LatticeType(self, lattice: Sinterbox.Lattice):
        """
        Setter for property: (@link Sinterbox.Lattice NXOpen.Mfg.AM.Sinterbox.Lattice@endlink) LatticeType
         Returns the lattice type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PartOffsetDistance
    ##  Returns the part offset distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PartOffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PartOffsetDistance
         Returns the part offset distance   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Parts
    ##  Returns the selection parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def Parts(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) Parts
         Returns the selection parts   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodDiameter
    ##  Returns the rod diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RodDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodDiameter
         Returns the rod diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodLength
    ##  Returns the rod length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RodLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodLength
         Returns the rod length   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodWidth
    ##  Returns the rod width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RodWidth(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RodWidth
         Returns the rod width   
            
         
        """
        pass
    
    ## Getter for property: (@link Sinterbox.Shape NXOpen.Mfg.AM.Sinterbox.Shape@endlink) ShapeType
    ##  Returns the shape type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return Sinterbox.Shape
    @property
    def ShapeType(self) -> Sinterbox.Shape:
        """
        Getter for property: (@link Sinterbox.Shape NXOpen.Mfg.AM.Sinterbox.Shape@endlink) ShapeType
         Returns the shape type   
            
         
        """
        pass
    
    ## Setter for property: (@link Sinterbox.Shape NXOpen.Mfg.AM.Sinterbox.Shape@endlink) ShapeType

    ##  Returns the shape type   
    ##     
    ##  
    ## Setter License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ShapeType.setter
    def ShapeType(self, shape: Sinterbox.Shape):
        """
        Setter for property: (@link Sinterbox.Shape NXOpen.Mfg.AM.Sinterbox.Shape@endlink) ShapeType
         Returns the shape type   
            
         
        """
        pass
    
##  Represents a @link Mfg::AM::Sinterbox Mfg::AM::Sinterbox@endlink . <br> To obtain an instance of this class use NXOpen.Mfg.AM.SinterboxBuilder  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class Sinterbox(PartGroup): 
    """ Represents a <ja_class>Mfg.AM.Sinterbox</ja_class>."""


    ##  Alignment types
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Free</term><description> 
    ## </description> </item><item><term> 
    ## BuildTray</term><description> 
    ## </description> </item></list>
    class AlignmentType(Enum):
        """
        Members Include: <Free> <BuildTray>
        """
        Free: int
        BuildTray: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.AlignmentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Boundary types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PartSelection</term><description> 
    ## </description> </item><item><term> 
    ## IndividualParts</term><description> 
    ## </description> </item></list>
    class Boundary(Enum):
        """
        Members Include: <PartSelection> <IndividualParts>
        """
        PartSelection: int
        IndividualParts: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.Boundary:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Lattice types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## GridAndRod</term><description> 
    ## </description> </item><item><term> 
    ## Standard</term><description> 
    ## </description> </item><item><term> 
    ## Voronoi</term><description> 
    ## </description> </item></list>
    class Lattice(Enum):
        """
        Members Include: <GridAndRod> <Standard> <Voronoi>
        """
        GridAndRod: int
        Standard: int
        Voronoi: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.Lattice:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  shape types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Box</term><description> 
    ## </description> </item><item><term> 
    ## Freeform</term><description> 
    ## </description> </item></list>
    class Shape(Enum):
        """
        Members Include: <Box> <Freeform>
        """
        Box: int
        Freeform: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Sinterbox.Shape:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
import NXOpen
import NXOpen.Features
##  Represents a @link Mfg::AM::Sketcher Mfg::AM::Sketcher@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::SupportBuilder::Sketcher  NXOpen::Mfg::AM::SupportBuilder::Sketcher @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CurveOnSurfaceBuilder.ArcEndOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.ArcLimits.EndLimit.LimitOption </term> <description> 
##  
## AtPoint </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.ArcMidOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.ArcThroughOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.AssociativeToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.CurveJoinMethod </term> <description> 
##  
## No </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.Degree </term> <description> 
##  
## 7 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.FitMethod </term> <description> 
##  
## DegreeAndSegments </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.IsAdvancedFit </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.IsAlignShape </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.MaximumDegree </term> <description> 
##  
## 7 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.MaximumSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.MinimumDegree </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitData.Segments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitProperties.FitOption </term> <description> 
##  
## Cubic </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitProperties.MaximumDegree </term> <description> 
##  
## 7 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveFitProperties.MaximumSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.CurveType </term> <description> 
##  
## Spline </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.LineEndOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## CurveOnSurfaceBuilder.ModeOption </term> <description> 
##  
## Projection </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.2  <br> 

class Sketcher(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.Sketcher</ja_class> builder """


    ##  the sketcher mode 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SurfaceFace</term><description> 
    ## </description> </item><item><term> 
    ## SurfaceLine</term><description> 
    ## </description> </item><item><term> 
    ## SketchFace</term><description> 
    ## </description> </item><item><term> 
    ## SketchLine</term><description> 
    ## </description> </item></list>
    class Mode(Enum):
        """
        Members Include: <SurfaceFace> <SurfaceLine> <SketchFace> <SketchLine>
        """
        SurfaceFace: int
        SurfaceLine: int
        SketchFace: int
        SketchLine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Sketcher.Mode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CloseCurve
    ##  Returns the flag indicating if curve should be closed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return bool
    @property
    def CloseCurve(self) -> bool:
        """
        Getter for property: (bool) CloseCurve
         Returns the flag indicating if curve should be closed   
            
         
        """
        pass
    
    ## Setter for property: (bool) CloseCurve

    ##  Returns the flag indicating if curve should be closed   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    @CloseCurve.setter
    def CloseCurve(self, bCloseCurve: bool):
        """
        Setter for property: (bool) CloseCurve
         Returns the flag indicating if curve should be closed   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Features.CurveOnSurfaceBuilder NXOpen.Features.CurveOnSurfaceBuilder@endlink) CurveOnSurfaceBuilder
    ##  Returns the Curve On Surface feature builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.Features.CurveOnSurfaceBuilder
    @property
    def CurveOnSurfaceBuilder(self) -> NXOpen.Features.CurveOnSurfaceBuilder:
        """
        Getter for property: (@link NXOpen.Features.CurveOnSurfaceBuilder NXOpen.Features.CurveOnSurfaceBuilder@endlink) CurveOnSurfaceBuilder
         Returns the Curve On Surface feature builder   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
    ##  Returns the sketch which holds the section curves   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Sketch
    @property
    def Sketch(self) -> NXOpen.Sketch:
        """
        Getter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
         Returns the sketch which holds the section curves   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch

    ##  Returns the sketch which holds the section curves   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Sketch.setter
    def Sketch(self, sectionSketch: NXOpen.Sketch):
        """
        Setter for property: (@link NXOpen.Sketch NXOpen.Sketch@endlink) Sketch
         Returns the sketch which holds the section curves   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SketchCollector
    ##  Returns the sketch geometry collector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SketchCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SketchCollector
         Returns the sketch geometry collector   
            
         
        """
        pass
    
    ## Getter for property: (@link Sketcher.Mode NXOpen.Mfg.AM.Sketcher.Mode@endlink) SketchMode
    ##  Returns the sketch mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return Sketcher.Mode
    @property
    def SketchMode(self) -> Sketcher.Mode:
        """
        Getter for property: (@link Sketcher.Mode NXOpen.Mfg.AM.Sketcher.Mode@endlink) SketchMode
         Returns the sketch mode   
            
         
        """
        pass
    
    ## Setter for property: (@link Sketcher.Mode NXOpen.Mfg.AM.Sketcher.Mode@endlink) SketchMode

    ##  Returns the sketch mode   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    @SketchMode.setter
    def SketchMode(self, sketchMode: Sketcher.Mode):
        """
        Setter for property: (@link Sketcher.Mode NXOpen.Mfg.AM.Sketcher.Mode@endlink) SketchMode
         Returns the sketch mode   
            
         
        """
        pass
    
    ##  Creates or extends the curve with points 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ## <param name="points"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  sketch points </param>
    def AddCurvePoints(self, points: List[NXOpen.Point]) -> None:
        """
         Creates or extends the curve with points 
        """
        pass
    
    ##  Set the faces to sketch the curve upon 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ## <param name="faces"> (@link NXOpen.Face List[NXOpen.Face]@endlink)  sketch faces </param>
    def SetSketchCanvas(self, faces: List[NXOpen.Face]) -> None:
        """
         Set the faces to sketch the curve upon 
        """
        pass
    
import NXOpen
##  Represents a @link Mfg::AM::SubnestingBuilder Mfg::AM::SubnestingBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::CreateSubnestingBuilder  NXOpen::Mfg::AM::ApplicationManager::CreateSubnestingBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConstraintType </term> <description> 
##  
## FixedRotation </description> </item> 
## 
## <item><term> 
##  
## GroupPartsAfterSubnesting </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## InterlockingType </term> <description> 
##  
## AvoidAllInterlocks </description> </item> 
## 
## <item><term> 
##  
## RotationAngle </term> <description> 
##  
## Degree90 </description> </item> 
## 
## <item><term> 
##  
## Spacing.Value </term> <description> 
##  
## 5.0 (millimeters part), 0.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## StopAfter </term> <description> 
##  
## 2 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2406.0.0  <br> 

class SubnestingBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.SubnestingBuilder</ja_class>. """


    ## Getter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType
    ##  Returns the constraints   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return Nester3D.Constraint
    @property
    def ConstraintType(self) -> Nester3D.Constraint:
        """
        Getter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType

    ##  Returns the constraints   
    ##     
    ##  
    ## Setter License requirements: am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @ConstraintType.setter
    def ConstraintType(self, constraint: Nester3D.Constraint):
        """
        Setter for property: (@link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink) ConstraintType
         Returns the constraints   
            
         
        """
        pass
    
    ## Getter for property: (bool) GroupPartsAfterSubnesting
    ##  Returns the flag to set Group after subnesting operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def GroupPartsAfterSubnesting(self) -> bool:
        """
        Getter for property: (bool) GroupPartsAfterSubnesting
         Returns the flag to set Group after subnesting operation   
            
         
        """
        pass
    
    ## Setter for property: (bool) GroupPartsAfterSubnesting

    ##  Returns the flag to set Group after subnesting operation   
    ##     
    ##  
    ## Setter License requirements: am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @GroupPartsAfterSubnesting.setter
    def GroupPartsAfterSubnesting(self, groupPartsAfterSubnesting: bool):
        """
        Setter for property: (bool) GroupPartsAfterSubnesting
         Returns the flag to set Group after subnesting operation   
            
         
        """
        pass
    
    ## Getter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType
    ##  Returns the solution type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return Nester3D.Interlocking
    @property
    def InterlockingType(self) -> Nester3D.Interlocking:
        """
        Getter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType

    ##  Returns the solution type   
    ##     
    ##  
    ## Setter License requirements: am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @InterlockingType.setter
    def InterlockingType(self, interlockingType: Nester3D.Interlocking):
        """
        Setter for property: (@link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink) InterlockingType
         Returns the solution type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PartsToSubnest
    ##  Returns the objects to reposition   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def PartsToSubnest(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PartsToSubnest
         Returns the objects to reposition   
            
         
        """
        pass
    
    ## Getter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle
    ##  Returns the Rotation Angle for the Parts to be nested    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return Nester3D.RotationAngleType
    @property
    def RotationAngle(self) -> Nester3D.RotationAngleType:
        """
        Getter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    
    ## Setter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle

    ##  Returns the Rotation Angle for the Parts to be nested    
    ##     
    ##  
    ## Setter License requirements: am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @RotationAngle.setter
    def RotationAngle(self, rotationAngle: Nester3D.RotationAngleType):
        """
        Setter for property: (@link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink) RotationAngle
         Returns the Rotation Angle for the Parts to be nested    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Spacing
    ##  Returns the spacing between parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Spacing(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Spacing
         Returns the spacing between parts   
            
         
        """
        pass
    
    ## Getter for property: (int) StopAfter
    ##  Returns the stop after   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def StopAfter(self) -> int:
        """
        Getter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    
    ## Setter for property: (int) StopAfter

    ##  Returns the stop after   
    ##     
    ##  
    ## Setter License requirements: am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @StopAfter.setter
    def StopAfter(self, stopAfter: int):
        """
        Setter for property: (int) StopAfter
         Returns the stop after   
            
         
        """
        pass
    
    ##  Execute the Subnesting 
    ##  @return nestStatus (@link NestingStatus NXOpen.Mfg.AM.NestingStatus@endlink):  Nesting Status.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: am_pb_siemens_nester (" NX Powder Bed Siemens Nester")
    def ExecuteSubnesting(self) -> NestingStatus:
        """
         Execute the Subnesting 
         @return nestStatus (@link NestingStatus NXOpen.Mfg.AM.NestingStatus@endlink):  Nesting Status.
        """
        pass
    
import NXOpen
##  Represents a @link Mfg::AM::Support Mfg::AM::Support@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Mfg::AM::ApplicationManager::GetSupportBuilder  NXOpen::Mfg::AM::ApplicationManager::GetSupportBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Mode </term> <description> 
##  
## Automatic </description> </item> 
## 
## <item><term> 
##  
## PlatformFilter </term> <description> 
##  
## KeepAll </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.ArcEndOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.ArcLimits.EndLimit.LimitOption </term> <description> 
##  
## AtPoint </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.ArcMidOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.ArcThroughOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.AssociativeToggle </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.CurveJoinMethod </term> <description> 
##  
## No </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.Degree </term> <description> 
##  
## 7 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.FitMethod </term> <description> 
##  
## DegreeAndSegments </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.IsAdvancedFit </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.IsAlignShape </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.MaximumDegree </term> <description> 
##  
## 7 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.MaximumSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.MinimumDegree </term> <description> 
##  
## 5 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitData.Segments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitProperties.FitOption </term> <description> 
##  
## Cubic </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitProperties.MaximumDegree </term> <description> 
##  
## 7 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveFitProperties.MaximumSegments </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.CurveType </term> <description> 
##  
## Spline </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.LineEndOption </term> <description> 
##  
## Point </description> </item> 
## 
## <item><term> 
##  
## Sketcher.CurveOnSurfaceBuilder.ModeOption </term> <description> 
##  
## Projection </description> </item> 
## 
## <item><term> 
##  
## SupportType </term> <description> 
##  
## Block </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX11.0.2  <br> 

class SupportBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>Mfg.AM.Support</ja_class> builder """


    ##  support creation modes 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Automatic</term><description> 
    ## </description> </item><item><term> 
    ## Manual</term><description> 
    ## </description> </item><item><term> 
    ## RegionsOnly</term><description> 
    ## </description> </item><item><term> 
    ## Duplicate</term><description> 
    ## </description> </item></list>
    class Modes(Enum):
        """
        Members Include: <Automatic> <Manual> <RegionsOnly> <Duplicate>
        """
        Automatic: int
        Manual: int
        RegionsOnly: int
        Duplicate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SupportBuilder.Modes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Platform Filter Mode 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## KeepAll</term><description> 
    ## </description> </item><item><term> 
    ## FullContactOnly</term><description> 
    ## </description> </item><item><term> 
    ## PartitialTouch</term><description> 
    ## </description> </item><item><term> 
    ## KeepPlatformFraction</term><description> 
    ## </description> </item><item><term> 
    ## AvoidInternal</term><description> 
    ## </description> </item></list>
    class PlatformFilterMode(Enum):
        """
        Members Include: <KeepAll> <FullContactOnly> <PartitialTouch> <KeepPlatformFraction> <AvoidInternal>
        """
        KeepAll: int
        FullContactOnly: int
        PartitialTouch: int
        KeepPlatformFraction: int
        AvoidInternal: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SupportBuilder.PlatformFilterMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the AM support types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Block</term><description> 
    ## </description> </item><item><term> 
    ## Line</term><description> 
    ## </description> </item><item><term> 
    ## Point</term><description> 
    ## </description> </item><item><term> 
    ## Nosupport</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item><item><term> 
    ## Volume</term><description> 
    ## </description> </item><item><term> 
    ## Web</term><description> 
    ## </description> </item><item><term> 
    ## Contour</term><description> 
    ## </description> </item><item><term> 
    ## Gusset</term><description> 
    ## </description> </item><item><term> 
    ## Combined</term><description> 
    ## </description> </item><item><term> 
    ## Tree</term><description> 
    ## </description> </item><item><term> 
    ## Hybrid</term><description> 
    ## </description> </item></list>
    class Types(Enum):
        """
        Members Include: <Block> <Line> <Point> <Nosupport> <UserDefined> <Volume> <Web> <Contour> <Gusset> <Combined> <Tree> <Hybrid>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SupportBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BodySelection
    ##  Returns the body selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def BodySelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BodySelection
         Returns the body selection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurveSelection
    ##  Returns the curve selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.ScCollector
    @property
    def CurveSelection(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) CurveSelection
         Returns the curve selection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceSelection
    ##  Returns the face selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceSelection(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceSelection
         Returns the face selection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
    ##  Returns the part (region) selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.FacetCollector
    @property
    def FacetCollector(self) -> NXOpen.FacetCollector:
        """
        Getter for property: (@link NXOpen.FacetCollector NXOpen.FacetCollector@endlink) FacetCollector
         Returns the part (region) selection   
            
         
        """
        pass
    
    ## Getter for property: (@link SupportBuilder.Modes NXOpen.Mfg.AM.SupportBuilder.Modes@endlink) Mode
    ##  Returns the support creation mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return SupportBuilder.Modes
    @property
    def Mode(self) -> SupportBuilder.Modes:
        """
        Getter for property: (@link SupportBuilder.Modes NXOpen.Mfg.AM.SupportBuilder.Modes@endlink) Mode
         Returns the support creation mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link SupportBuilder.Modes NXOpen.Mfg.AM.SupportBuilder.Modes@endlink) Mode

    ##  Returns the support creation mode.  
    ##      
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Mode.setter
    def Mode(self, mode: SupportBuilder.Modes):
        """
        Setter for property: (@link SupportBuilder.Modes NXOpen.Mfg.AM.SupportBuilder.Modes@endlink) Mode
         Returns the support creation mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) PartSelection
    ##  Returns the part (region) selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def PartSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) PartSelection
         Returns the part (region) selection   
            
         
        """
        pass
    
    ## Getter for property: (@link SupportBuilder.PlatformFilterMode NXOpen.Mfg.AM.SupportBuilder.PlatformFilterMode@endlink) PlatformFilter
    ##  Returns the platform filter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return SupportBuilder.PlatformFilterMode
    @property
    def PlatformFilter(self) -> SupportBuilder.PlatformFilterMode:
        """
        Getter for property: (@link SupportBuilder.PlatformFilterMode NXOpen.Mfg.AM.SupportBuilder.PlatformFilterMode@endlink) PlatformFilter
         Returns the platform filter   
            
         
        """
        pass
    
    ## Setter for property: (@link SupportBuilder.PlatformFilterMode NXOpen.Mfg.AM.SupportBuilder.PlatformFilterMode@endlink) PlatformFilter

    ##  Returns the platform filter   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @PlatformFilter.setter
    def PlatformFilter(self, platformFilter: SupportBuilder.PlatformFilterMode):
        """
        Setter for property: (@link SupportBuilder.PlatformFilterMode NXOpen.Mfg.AM.SupportBuilder.PlatformFilterMode@endlink) PlatformFilter
         Returns the platform filter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PointSelection
    ##  Returns the point selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def PointSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) PointSelection
         Returns the point selection   
            
         
        """
        pass
    
    ## Getter for property: (@link Sketcher NXOpen.Mfg.AM.Sketcher@endlink) Sketcher
    ##  Returns the sketcher   
    ##     
    ##  
    ## Getter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return Sketcher
    @property
    def Sketcher(self) -> Sketcher:
        """
        Getter for property: (@link Sketcher NXOpen.Mfg.AM.Sketcher@endlink) Sketcher
         Returns the sketcher   
            
         
        """
        pass
    
    ## Getter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) SupportProfile
    ##  Returns the support profile used to generate supports or a NULL_TAG if the default printer profile is used   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return SupportProfile
    @property
    def SupportProfile(self) -> SupportProfile:
        """
        Getter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) SupportProfile
         Returns the support profile used to generate supports or a NULL_TAG if the default printer profile is used   
            
         
        """
        pass
    
    ## Setter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) SupportProfile

    ##  Returns the support profile used to generate supports or a NULL_TAG if the default printer profile is used   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SupportProfile.setter
    def SupportProfile(self, tagSupportProfile: SupportProfile):
        """
        Setter for property: (@link SupportProfile NXOpen.Mfg.AM.SupportProfile@endlink) SupportProfile
         Returns the support profile used to generate supports or a NULL_TAG if the default printer profile is used   
            
         
        """
        pass
    
    ## Getter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) SupportType
    ##  Returns the type of support to create when Mode is set to Manual   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return SupportBuilder.Types
    @property
    def SupportType(self) -> SupportBuilder.Types:
        """
        Getter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) SupportType
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    
    ## Setter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) SupportType

    ##  Returns the type of support to create when Mode is set to Manual   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @SupportType.setter
    def SupportType(self, supportType: SupportBuilder.Types):
        """
        Setter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) SupportType
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    
    ## Getter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) Type
    ##  Returns the type of support to create when Mode is set to Manual   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1872.0.0.  Use @link NXOpen::Mfg::AM::SupportBuilder::SetSupportType NXOpen::Mfg::AM::SupportBuilder::SetSupportType@endlink  instead.  <br> 

    ## @return SupportBuilder.Types
    @property
    def Type(self) -> SupportBuilder.Types:
        """
        Getter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) Type
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    
    ## Setter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) Type

    ##  Returns the type of support to create when Mode is set to Manual   
    ##     
    ##  
    ## Setter License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1872.0.0.  Use @link NXOpen::Mfg::AM::SupportBuilder::SetSupportType NXOpen::Mfg::AM::SupportBuilder::SetSupportType@endlink  instead.  <br> 

    @Type.setter
    def Type(self, type: SupportBuilder.Types):
        """
        Setter for property: (@link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink) Type
         Returns the type of support to create when Mode is set to Manual   
            
         
        """
        pass
    
    ##  Get the profile support to use to create a support of a particular type. Calling this method will change the profile library when applicable 
    ##  @return tagProfile (@link ProfileSupport NXOpen.Mfg.AM.ProfileSupport@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetProfileSupport(self) -> ProfileSupport:
        """
         Get the profile support to use to create a support of a particular type. Calling this method will change the profile library when applicable 
         @return tagProfile (@link ProfileSupport NXOpen.Mfg.AM.ProfileSupport@endlink): .
        """
        pass
    
    ##  Set the profile support to use to create a support of a particular type. Calling this method will change the profile library when applicable 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ## <param name="tagProfile"> (@link ProfileSupport NXOpen.Mfg.AM.ProfileSupport@endlink) </param>
    def SetProfileSupport(self, tagProfile: ProfileSupport) -> None:
        """
         Set the profile support to use to create a support of a particular type. Calling this method will change the profile library when applicable 
        """
        pass
    
    ##  Set the surface region faces for the support to create 
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: am_pb_mtls_sg_2 ("Advanced NX Additive Support Geometry") OR am_pb_mtls_sg_1 ("Basic NX Additive Support Geometry")
    ## 
    ## <param name="faces"> (@link NXOpen.Face List[NXOpen.Face]@endlink)  surface region faces </param>
    def SetSurfaceRegion(self, faces: List[NXOpen.Face]) -> None:
        """
         Set the surface region faces for the support to create 
        """
        pass
    
##  Interface for Services Support Library objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::SupportLibrary NXOpen::Mfg::AM::SupportLibrary@endlink .  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

class SupportLibrary(Library): 
    """ Interface for Services Support Library objects """


    ##  Adds a support profile 
    ##  @return newProfileSupport (@link ProfileSupport NXOpen.Mfg.AM.ProfileSupport@endlink):  the new support profile .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link SupportProfile SupportProfile@endlink  instead.  <br> 

    ## License requirements: None.
    def AddSupportProfile(self) -> ProfileSupport:
        """
         Adds a support profile 
         @return newProfileSupport (@link ProfileSupport NXOpen.Mfg.AM.ProfileSupport@endlink):  the new support profile .
        """
        pass
    
##  Interface for Services Profile objects  <br> To obtain an instance of this class use @link NXOpen::Mfg::AM::ProfileLibrary NXOpen::Mfg::AM::ProfileLibrary@endlink .  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class SupportProfile(ProfileObject): 
    """ Interface for Services Profile objects """


    ##  Add a new profile support 
    ##  @return pProfileSupport (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="supportType"> (@link Support.Type NXOpen.Mfg.AM.Support.Type@endlink) </param>
    def AddProfile(self, supportType: Support.Type) -> ProfileObject:
        """
         Add a new profile support 
         @return pProfileSupport (@link ProfileObject NXOpen.Mfg.AM.ProfileObject@endlink):  .
        """
        pass
    
    ##  Returns the profile supports of a certain type 
    ##  @return pProfileSupports (@link ProfileObject List[NXOpen.Mfg.AM.ProfileObject]@endlink):  .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="supportType"> (@link Support.Type NXOpen.Mfg.AM.Support.Type@endlink) </param>
    def GetProfiles(self, supportType: Support.Type) -> List[ProfileObject]:
        """
         Returns the profile supports of a certain type 
         @return pProfileSupports (@link ProfileObject List[NXOpen.Mfg.AM.ProfileObject]@endlink):  .
        """
        pass
    
    ##  Sets the default support profile within the library. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def SetAsDefault(self) -> None:
        """
         Sets the default support profile within the library. 
        """
        pass
    
import NXOpen
##  Interface for Model Support objects  <br> To obtain an instance of this class use Part.CreateSupports  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class Support(NXOpen.DisplayableObject): 
    """ Interface for Model Support objects """


    ##  support types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Block</term><description> 
    ## </description> </item><item><term> 
    ## Line</term><description> 
    ## </description> </item><item><term> 
    ## Point</term><description> 
    ## </description> </item><item><term> 
    ## Volume</term><description> 
    ## </description> </item><item><term> 
    ## Web</term><description> 
    ## </description> </item><item><term> 
    ## Contour</term><description> 
    ## </description> </item><item><term> 
    ## Gusset</term><description> 
    ## </description> </item><item><term> 
    ## Combined</term><description> 
    ## </description> </item><item><term> 
    ## Tree</term><description> 
    ## </description> </item><item><term> 
    ## Hybrid</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class Type(Enum):
        """
        Members Include: <NotSet> <Block> <Line> <Point> <Volume> <Web> <Contour> <Gusset> <Combined> <Tree> <Hybrid> <UserDefined>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Support.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link Support.Type NXOpen.Mfg.AM.Support.Type@endlink) SupportType
    ##  Returns the support type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return Support.Type
    @property
    def SupportType(self) -> Support.Type:
        """
        Getter for property: (@link Support.Type NXOpen.Mfg.AM.Support.Type@endlink) SupportType
         Returns the support type   
            
         
        """
        pass
    
    ##  Returns the support geometry. Can be a solid bodies, facet bodies or convergent bodies 
    ##  @return tagGeometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetGeometries(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the support geometry. Can be a solid bodies, facet bodies or convergent bodies 
         @return tagGeometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
    ##  Returns the support geometry. Can be a solid body, facet body or convergent body 
    ##  @return tagGeometry (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use @link NXOpen::Mfg::AM::Support::GetGeometries NXOpen::Mfg::AM::Support::GetGeometries@endlink  instead.  <br> 

    ## License requirements: None.
    def GetGeometry(self) -> NXOpen.DisplayableObject:
        """
         Returns the support geometry. Can be a solid body, facet body or convergent body 
         @return tagGeometry (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink): .
        """
        pass
    
    ##  Returns the simulation support 
    ##  @return tagGeometry (@link SimulationSupport NXOpen.Mfg.AM.SimulationSupport@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetSimulationSupport(self) -> SimulationSupport:
        """
         Returns the simulation support 
         @return tagGeometry (@link SimulationSupport NXOpen.Mfg.AM.SimulationSupport@endlink): .
        """
        pass
    
    ##  Returns the surface region of the support 
    ##  @return surfaceRegion (@link SurfaceRegion NXOpen.Mfg.AM.SurfaceRegion@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetSurfaceRegion(self) -> SurfaceRegion:
        """
         Returns the surface region of the support 
         @return surfaceRegion (@link SurfaceRegion NXOpen.Mfg.AM.SurfaceRegion@endlink): .
        """
        pass
    
    ##  Regenerates Support after parameters change 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    def Regenerate(self) -> None:
        """
         Regenerates Support after parameters change 
        """
        pass
    
    ##  Sets the simulation support 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: am_pb_cam_basic ("Basic NX Powder Bed Additive Manufacturing Application")
    ## 
    ## <param name="tagGeometry"> (@link SimulationSupport NXOpen.Mfg.AM.SimulationSupport@endlink) </param>
    def SetSimulationSupport(self, tagGeometry: SimulationSupport) -> None:
        """
         Sets the simulation support 
        """
        pass
    
import NXOpen
##  Additive Manufacturing Surface Region  <br> To obtain an instance of this class use Support.GetSurfaceRegion  <br> 
## 
##   <br>  Created in NX12.0.1  <br> 

class SurfaceRegion(NXOpen.NXObject): 
    """ Additive Manufacturing Surface Region """


    ##  Returns the surface region geometry. 
    ##  @return tagGeometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetGeometry(self) -> List[NXOpen.DisplayableObject]:
        """
         Returns the surface region geometry. 
         @return tagGeometry (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink): .
        """
        pass
    
## @package NXOpen.Mfg.AM
## Classes, Enums and Structs under NXOpen.Mfg.AM namespace

##  @link MovePartBuilderMoveObject NXOpen.Mfg.AM.MovePartBuilderMoveObject @endlink is an alias for @link MovePartBuilder.MoveObject NXOpen.Mfg.AM.MovePartBuilder.MoveObject@endlink
MovePartBuilderMoveObject = MovePartBuilder.MoveObject


##  @link MovePartBuilderMoveTypeOption NXOpen.Mfg.AM.MovePartBuilderMoveTypeOption @endlink is an alias for @link MovePartBuilder.MoveTypeOption NXOpen.Mfg.AM.MovePartBuilder.MoveTypeOption@endlink
MovePartBuilderMoveTypeOption = MovePartBuilder.MoveTypeOption


##  @link Nester3DConstraint NXOpen.Mfg.AM.Nester3DConstraint @endlink is an alias for @link Nester3D.Constraint NXOpen.Mfg.AM.Nester3D.Constraint@endlink
Nester3DConstraint = Nester3D.Constraint


##  @link Nester3DInterlocking NXOpen.Mfg.AM.Nester3DInterlocking @endlink is an alias for @link Nester3D.Interlocking NXOpen.Mfg.AM.Nester3D.Interlocking@endlink
Nester3DInterlocking = Nester3D.Interlocking


##  @link Nester3DNesterType NXOpen.Mfg.AM.Nester3DNesterType @endlink is an alias for @link Nester3D.NesterType NXOpen.Mfg.AM.Nester3D.NesterType@endlink
Nester3DNesterType = Nester3D.NesterType


##  @link Nester3DRotationAngleType NXOpen.Mfg.AM.Nester3DRotationAngleType @endlink is an alias for @link Nester3D.RotationAngleType NXOpen.Mfg.AM.Nester3D.RotationAngleType@endlink
Nester3DRotationAngleType = Nester3D.RotationAngleType


##  @link Nester3DSolution NXOpen.Mfg.AM.Nester3DSolution @endlink is an alias for @link Nester3D.Solution NXOpen.Mfg.AM.Nester3D.Solution@endlink
Nester3DSolution = Nester3D.Solution


##  @link PartInterlockingType NXOpen.Mfg.AM.PartInterlockingType @endlink is an alias for @link Part.InterlockingType NXOpen.Mfg.AM.Part.InterlockingType@endlink
PartInterlockingType = Part.InterlockingType


##  @link PartNestingConstraintType NXOpen.Mfg.AM.PartNestingConstraintType @endlink is an alias for @link Part.NestingConstraintType NXOpen.Mfg.AM.Part.NestingConstraintType@endlink
PartNestingConstraintType = Part.NestingConstraintType


##  @link PartRotationAngleType NXOpen.Mfg.AM.PartRotationAngleType @endlink is an alias for @link Part.RotationAngleType NXOpen.Mfg.AM.Part.RotationAngleType@endlink
PartRotationAngleType = Part.RotationAngleType


##  @link PatternAMPartBuilderPatternType NXOpen.Mfg.AM.PatternAMPartBuilderPatternType @endlink is an alias for @link PatternAMPartBuilder.PatternType NXOpen.Mfg.AM.PatternAMPartBuilder.PatternType@endlink
PatternAMPartBuilderPatternType = PatternAMPartBuilder.PatternType


##  @link RepositionPartBuilderMethod NXOpen.Mfg.AM.RepositionPartBuilderMethod @endlink is an alias for @link RepositionPartBuilder.Method NXOpen.Mfg.AM.RepositionPartBuilder.Method@endlink
RepositionPartBuilderMethod = RepositionPartBuilder.Method


##  @link RepositionPartBuilderRotateAxisType NXOpen.Mfg.AM.RepositionPartBuilderRotateAxisType @endlink is an alias for @link RepositionPartBuilder.RotateAxisType NXOpen.Mfg.AM.RepositionPartBuilder.RotateAxisType@endlink
RepositionPartBuilderRotateAxisType = RepositionPartBuilder.RotateAxisType


##  @link RepositionPartBuilderTranslatePartsType NXOpen.Mfg.AM.RepositionPartBuilderTranslatePartsType @endlink is an alias for @link RepositionPartBuilder.TranslatePartsType NXOpen.Mfg.AM.RepositionPartBuilder.TranslatePartsType@endlink
RepositionPartBuilderTranslatePartsType = RepositionPartBuilder.TranslatePartsType


##  @link RepositionPartBuilderTranslateToType NXOpen.Mfg.AM.RepositionPartBuilderTranslateToType @endlink is an alias for @link RepositionPartBuilder.TranslateToType NXOpen.Mfg.AM.RepositionPartBuilder.TranslateToType@endlink
RepositionPartBuilderTranslateToType = RepositionPartBuilder.TranslateToType


##  @link SinterboxAlignmentType NXOpen.Mfg.AM.SinterboxAlignmentType @endlink is an alias for @link Sinterbox.AlignmentType NXOpen.Mfg.AM.Sinterbox.AlignmentType@endlink
SinterboxAlignmentType = Sinterbox.AlignmentType


##  @link SinterboxBoundary NXOpen.Mfg.AM.SinterboxBoundary @endlink is an alias for @link Sinterbox.Boundary NXOpen.Mfg.AM.Sinterbox.Boundary@endlink
SinterboxBoundary = Sinterbox.Boundary


##  @link SinterboxLattice NXOpen.Mfg.AM.SinterboxLattice @endlink is an alias for @link Sinterbox.Lattice NXOpen.Mfg.AM.Sinterbox.Lattice@endlink
SinterboxLattice = Sinterbox.Lattice


##  @link SinterboxShape NXOpen.Mfg.AM.SinterboxShape @endlink is an alias for @link Sinterbox.Shape NXOpen.Mfg.AM.Sinterbox.Shape@endlink
SinterboxShape = Sinterbox.Shape


##  @link SketcherMode NXOpen.Mfg.AM.SketcherMode @endlink is an alias for @link Sketcher.Mode NXOpen.Mfg.AM.Sketcher.Mode@endlink
SketcherMode = Sketcher.Mode


##  @link SupportBuilderModes NXOpen.Mfg.AM.SupportBuilderModes @endlink is an alias for @link SupportBuilder.Modes NXOpen.Mfg.AM.SupportBuilder.Modes@endlink
SupportBuilderModes = SupportBuilder.Modes


##  @link SupportBuilderPlatformFilterMode NXOpen.Mfg.AM.SupportBuilderPlatformFilterMode @endlink is an alias for @link SupportBuilder.PlatformFilterMode NXOpen.Mfg.AM.SupportBuilder.PlatformFilterMode@endlink
SupportBuilderPlatformFilterMode = SupportBuilder.PlatformFilterMode


##  @link SupportBuilderTypes NXOpen.Mfg.AM.SupportBuilderTypes @endlink is an alias for @link SupportBuilder.Types NXOpen.Mfg.AM.SupportBuilder.Types@endlink
SupportBuilderTypes = SupportBuilder.Types


##  @link SupportType NXOpen.Mfg.AM.SupportType @endlink is an alias for @link Support.Type NXOpen.Mfg.AM.Support.Type@endlink
SupportType = Support.Type


