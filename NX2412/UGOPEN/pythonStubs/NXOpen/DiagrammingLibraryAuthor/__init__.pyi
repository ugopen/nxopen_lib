from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
class AllowedAttachmentTypes(Enum):
    """
    Members Include: 
     |NotSet|  none. 
     |ToConnection|  allow attach to connection. 
     |ToNode|  allow attach to node. 

    """
    NotSet: int
    ToConnection: int
    ToNode: int
    @staticmethod
    def ValueOf(value: int) -> AllowedAttachmentTypes:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AllowedSides(Enum):
    """
    Members Include: 
     |NotSet| 
     |Top| 
     |Bottom| 
     |Left| 
     |Right| 

    """
    NotSet: int
    Top: int
    Bottom: int
    Left: int
    Right: int
    @staticmethod
    def ValueOf(value: int) -> AllowedSides:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class AttachingPolicy(Enum):
    """
    Members Include: 
     |DynamicNode| 
     |DynamicPort| 

    """
    DynamicNode: int
    DynamicPort: int
    @staticmethod
    def ValueOf(value: int) -> AttachingPolicy:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class AttributeHolder(NXOpen.NXObject): 
    """  Represents a NXOpen.DiagrammingLibraryAuthor.AttributeHolder.  """
    pass
import NXOpen
class EquipmentData(NXOpen.TransientObject): 
    """ Defines an object represent Equipment data.
     Equipment data contains the equipment class name and the id of equipment instances. 
     These information is used to retrieve equipment from library and link to or unlink from symbol.
    """
    def Dispose(self) -> None:
        """
         Frees resources associated with the instance.
        """
        pass
import NXOpen
class LineTypeAuthoringBuilder(NXOpen.Builder): 
    """  Represents a LineTypeAuthoringBuilder.  
        Calling Builder.Commit on this builder will only return . """
    @property
    def Discipline(self) -> str:
        """
        Getter for property: (str) Discipline
         Returns the discipline of the object.  
             
         
        """
        pass
    @Discipline.setter
    def Discipline(self, discipline: str):
        """
        Setter for property: (str) Discipline
         Returns the discipline of the object.  
             
         
        """
        pass
    @property
    def LineTypes(self) -> LineTypeBuilderList:
        """
        Getter for property: ( LineTypeBuilderList NXOpen.Diagramm) LineTypes
         Returns the list of line types.  
             
         
        """
        pass
    @property
    def OutputFolder(self) -> str:
        """
        Getter for property: (str) OutputFolder
         Returns the output folder for generated files.  
             
         
        """
        pass
    @OutputFolder.setter
    def OutputFolder(self, outputFolder: str):
        """
        Setter for property: (str) OutputFolder
         Returns the output folder for generated files.  
             
         
        """
        pass
    def CreateLineType(self) -> LineTypeBuilder:
        """
         Creates a new line type 
         Returns lineType ( LineTypeBuilder NXOpen.Diagramm): .
        """
        pass
import NXOpen
class LineTypeBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[LineTypeBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: LineTypeBuilder) -> None:
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
    def Erase(self, obj: LineTypeBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: LineTypeBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: LineTypeBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> LineTypeBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( LineTypeBuilder NXOpen.Diagramm):  object found at input index .
        """
        pass
    def GetContents(self) -> List[LineTypeBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( LineTypeBuilder List[NXOpen.Diagra):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: LineTypeBuilder) -> None:
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
    def SetContents(self, objects: List[LineTypeBuilder]) -> None:
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
    def Swap(self, object1: LineTypeBuilder, object2: LineTypeBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class LineTypeBuilder(NXOpen.TaggedObject): 
    """  Represents a LineTypeBuilder.  """
    @property
    def LineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) LineColor
         Returns the line color.  
             
         
        """
        pass
    @LineColor.setter
    def LineColor(self, colorId: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) LineColor
         Returns the line color.  
             
         
        """
        pass
    @property
    def LineFont(self) -> NXOpen.DisplayableObject.ObjectFont:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font.  
             
         
        """
        pass
    @LineFont.setter
    def LineFont(self, font: NXOpen.DisplayableObject.ObjectFont):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectFont) LineFont
         Returns the line font.  
             
         
        """
        pass
    @property
    def LineTypeName(self) -> str:
        """
        Getter for property: (str) LineTypeName
         Returns the name of the line type.  
           It should be unique.   
         
        """
        pass
    @LineTypeName.setter
    def LineTypeName(self, name: str):
        """
        Setter for property: (str) LineTypeName
         Returns the name of the line type.  
           It should be unique.   
         
        """
        pass
    @property
    def LineTypePriority(self) -> int:
        """
        Getter for property: (int) LineTypePriority
         Returns the priority of the line type.  
           It should be greater than or equal to 0.   
         
        """
        pass
    @LineTypePriority.setter
    def LineTypePriority(self, priority: int):
        """
        Setter for property: (int) LineTypePriority
         Returns the priority of the line type.  
           It should be greater than or equal to 0.   
         
        """
        pass
    @property
    def LineWidth(self) -> NXOpen.DisplayableObject.ObjectWidth:
        """
        Getter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @LineWidth.setter
    def LineWidth(self, width: NXOpen.DisplayableObject.ObjectWidth):
        """
        Setter for property: ( NXOpen.DisplayableObject.ObjectWidth) LineWidth
         Returns the line width.  
             
         
        """
        pass
    @property
    def ObjectId(self) -> str:
        """
        Getter for property: (str) ObjectId
         Returns the object Id of the line type.  
             
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PipeStockBuilder(NXOpen.TaggedObject): 
    """  Represents a PipeStockBuilder.  """
    def CreatePipeStock(self, instanceId: str, partId: str, partName: str, numberName: str) -> AttributeHolder:
        """
         Creates a new pipe stock 
         Returns pipeStockObject ( AttributeHolder NXOpen.Diagramm):  the pipe stock object .
        """
        pass
    def DeletePipeStock(self, pipeStockObject: AttributeHolder) -> None:
        """
         Deletes the pipe stock which is new created 
        """
        pass
    def GetPipeStockObjects(self) -> List[AttributeHolder]:
        """
         Gets the pipe stock objects which have user attributes of the pipe stock. 
         Returns pipeStockObjects ( AttributeHolder List[NXOpen.Diagra):  the pipe stock objects .
        """
        pass
    def SelectFolder(self, classId: str) -> None:
        """
         Selects the pipe stock folder by the class ID 
        """
        pass
    def SelectPipeStock(self, symbolId: str) -> None:
        """
         Selects one pipe stock by the symbol ID 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PortDataBuilder(NXOpen.TaggedObject): 
    """  Represents a PortDataBuilder.  """
    @property
    def NozzleBottom(self) -> bool:
        """
        Getter for property: (bool) NozzleBottom
         Returns the nozzle in the bottom edge.  
             
         
        """
        pass
    @NozzleBottom.setter
    def NozzleBottom(self, nozzleBottom: bool):
        """
        Setter for property: (bool) NozzleBottom
         Returns the nozzle in the bottom edge.  
             
         
        """
        pass
    @property
    def NozzleLeft(self) -> bool:
        """
        Getter for property: (bool) NozzleLeft
         Returns the nozzle in the left edge.  
             
         
        """
        pass
    @NozzleLeft.setter
    def NozzleLeft(self, nozzleLeft: bool):
        """
        Setter for property: (bool) NozzleLeft
         Returns the nozzle in the left edge.  
             
         
        """
        pass
    @property
    def NozzleRight(self) -> bool:
        """
        Getter for property: (bool) NozzleRight
         Returns the nozzle in the right edge.  
             
         
        """
        pass
    @NozzleRight.setter
    def NozzleRight(self, nozzleRight: bool):
        """
        Setter for property: (bool) NozzleRight
         Returns the nozzle in the right edge.  
             
         
        """
        pass
    @property
    def NozzleTop(self) -> bool:
        """
        Getter for property: (bool) NozzleTop
         Returns the nozzle in the top edge   
            
         
        """
        pass
    @NozzleTop.setter
    def NozzleTop(self, nozzleTop: bool):
        """
        Setter for property: (bool) NozzleTop
         Returns the nozzle in the top edge   
            
         
        """
        pass
    def CreatePort(self) -> AttributeHolder:
        """
         Creates a new port 
         Returns portObject ( AttributeHolder NXOpen.Diagramm):  the port object .
        """
        pass
    def DeletePort(self, portObject: AttributeHolder) -> None:
        """
         Deletes the port which is new created 
        """
        pass
    def GetConnectionDirection(self, portObject: AttributeHolder) -> NXOpen.Point2d:
        """
         Gets the connection direction 
         Returns connectionDirection ( NXOpen.Point2d):  the connection direction .
        """
        pass
    def GetPointLocation(self, portObject: AttributeHolder) -> NXOpen.Point2d:
        """
         Gets the port location 
         Returns portLocation ( NXOpen.Point2d):  the port location .
        """
        pass
    def GetPortObjects(self) -> List[AttributeHolder]:
        """
         Gets the port objects which have user attributes of the port. 
         Returns portObjects ( AttributeHolder List[NXOpen.Diagra):  the port objects .
        """
        pass
    def SetConnectionDirection(self, portObject: AttributeHolder, connectionDirection: NXOpen.Point2d) -> None:
        """
         Sets the connection direction  
        """
        pass
    def SetPointLocation(self, portObject: AttributeHolder, portLocation: NXOpen.Point2d) -> None:
        """
         Sets the port location 
        """
        pass
class PortType(Enum):
    """
    Members Include: 
     |Single| 
     |Multiple| 

    """
    Single: int
    Multiple: int
    @staticmethod
    def ValueOf(value: int) -> PortType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Gateway
import NXOpen.GeometricUtilities
import NXOpen.Tooling
class Symbol2DBuilder(NXOpen.TaggedObject): 
    """  Represents a Symbol2DBuilder.  """
    @property
    def AnchorPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) AnchorPoint
         Returns the anchor point   
            
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) AnchorPoint
         Returns the anchor point   
            
         
        """
        pass
    @property
    def DraftingSymbol(self) -> NXOpen.Tooling.SelectReuseLibraryItemBuilder:
        """
        Getter for property: ( NXOpen.Tooling.SelectReuseLibraryItemBuilder) DraftingSymbol
         Returns the 2D symbol sub-builder.  
             
         
        """
        pass
    @property
    def EnableScale(self) -> bool:
        """
        Getter for property: (bool) EnableScale
         Returns the scaling   
            
         
        """
        pass
    @EnableScale.setter
    def EnableScale(self, enableScale: bool):
        """
        Setter for property: (bool) EnableScale
         Returns the scaling   
            
         
        """
        pass
    @property
    def Image(self) -> NXOpen.Gateway.ImageCaptureBuilder:
        """
        Getter for property: ( NXOpen.Gateway.ImageCaptureBuilder) Image
         Returns the image capture builder   
            
         
        """
        pass
    @Image.setter
    def Image(self, imageCaptureBuilder: NXOpen.Gateway.ImageCaptureBuilder):
        """
        Setter for property: ( NXOpen.Gateway.ImageCaptureBuilder) Image
         Returns the image capture builder   
            
         
        """
        pass
    @property
    def IsInline(self) -> bool:
        """
        Getter for property: (bool) IsInline
         Returns the inline   
            
         
        """
        pass
    @IsInline.setter
    def IsInline(self, isInline: bool):
        """
        Setter for property: (bool) IsInline
         Returns the inline   
            
         
        """
        pass
    @property
    def PortData(self) -> PortDataBuilder:
        """
        Getter for property: ( PortDataBuilder NXOpen.Diagramm) PortData
         Returns the port data sub-builder.  
             
         
        """
        pass
    @property
    def PrefixLetters(self) -> str:
        """
        Getter for property: (str) PrefixLetters
         Returns the prefix   
            
         
        """
        pass
    @PrefixLetters.setter
    def PrefixLetters(self, prefixLetters: str):
        """
        Setter for property: (str) PrefixLetters
         Returns the prefix   
            
         
        """
        pass
    @property
    def TagLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) TagLocation
         Returns the tag location   
            
         
        """
        pass
    @TagLocation.setter
    def TagLocation(self, tagLocation: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) TagLocation
         Returns the tag location   
            
         
        """
        pass
    def CreateFromSymbol(self, symbolId: str) -> None:
        """
         Creates a new symbol from another symbol 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class Symbol3DBuilder(NXOpen.TaggedObject): 
    """  Represents a Symbol3DBuilder.  """
    @property
    def PortMappingData(self) -> NXOpen.ITableEditorDataProvider:
        """
        Getter for property: ( NXOpen.ITableEditorDataProvider) PortMappingData
         Returns the data provider of the port mapping table.  
             
         
        """
        pass
import NXOpen
class SymbolBuilder(NXOpen.Builder): 
    """  Represents a SymbolBuilder.  
        Calling Builder.Commit on this builder will only return . """
    @property
    def ActiveVariantId(self) -> int:
        """
        Getter for property: (int) ActiveVariantId
         Returns the active variant in symbol  
            
         
        """
        pass
    @ActiveVariantId.setter
    def ActiveVariantId(self, variantId: int):
        """
        Setter for property: (int) ActiveVariantId
         Returns the active variant in symbol  
            
         
        """
        pass
    @property
    def AnchorPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) AnchorPoint
         Returns the anchor location point  
            
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) AnchorPoint
         Returns the anchor location point  
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the symbol description  
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the symbol description  
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the symbol name  
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the symbol name  
            
         
        """
        pass
    @property
    def Standard(self) -> str:
        """
        Getter for property: (str) Standard
         Returns the symbol standard  
            
         
        """
        pass
    @Standard.setter
    def Standard(self, standard: str):
        """
        Setter for property: (str) Standard
         Returns the symbol standard  
            
         
        """
        pass
    @property
    def TagLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) TagLocation
         Returns the tag location point  
            
         
        """
        pass
    @TagLocation.setter
    def TagLocation(self, tagLocation: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) TagLocation
         Returns the tag location point  
            
         
        """
        pass
    @property
    def TagPrefix(self) -> str:
        """
        Getter for property: (str) TagPrefix
         Returns the tag prefix name  
            
         
        """
        pass
    @TagPrefix.setter
    def TagPrefix(self, tagPrefix: str):
        """
        Setter for property: (str) TagPrefix
         Returns the tag prefix name  
            
         
        """
        pass
    @property
    def Unit(self) -> str:
        """
        Getter for property: (str) Unit
         Returns the symbol unit  
            
         
        """
        pass
    @Unit.setter
    def Unit(self, unit: str):
        """
        Setter for property: (str) Unit
         Returns the symbol unit  
            
         
        """
        pass
    def GetSymbolPort(self, portId: str) -> NXOpen.NXObject:
        """
         Gets symbol port 
         Returns portObject ( NXOpen.NXObject): .
        """
        pass
    def GetSymbolVariant(self, variantId: int) -> NXOpen.NXObject:
        """
         Gets symbol variant 
         Returns variantObject ( NXOpen.NXObject): .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SymbolConnectionPointBuilder(NXOpen.TaggedObject): 
    """  Represents a SymbolConnectionPointBuilder.  
        Calling Builder.Commit on this builder will only return . """
    @property
    def ConnectionDirection(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) ConnectionDirection
         Returns the connection direction   
            
         
        """
        pass
    @ConnectionDirection.setter
    def ConnectionDirection(self, connectionDirection: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) ConnectionDirection
         Returns the connection direction   
            
         
        """
        pass
    @property
    def Location(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) Location
         Returns the port location point  
            
         
        """
        pass
    @Location.setter
    def Location(self, portLocation: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) Location
         Returns the port location point  
            
         
        """
        pass
    def GetPortType(self) -> PortType:
        """
         Get port type 
         Returns type ( PortType NXOpen.Diagramm): .
        """
        pass
    def SetPortType(self, type: PortType) -> None:
        """
         Set port type 
        """
        pass
import NXOpen
class SymbolDesignerManager(NXOpen.Object): 
    """ Represents an object that manages Symbol Designer application specific interfaces.
     """
    def CreateEquipmentData(equipmentClass: str, equipmentIds: List[str]) -> EquipmentData:
        """
         Creates a DiagrammingLibraryAuthor.EquipmentData. 
         Returns equipmentData ( EquipmentData NXOpen.Diagramm): .
        """
        pass
    def CreateLineTypeAuthoringBuilder(part: NXOpen.Part) -> LineTypeAuthoringBuilder:
        """
         Creates a NXOpen.DiagrammingLibraryAuthor.LineTypeAuthoringBuilder. 
         Returns builder ( LineTypeAuthoringBuilder NXOpen.Diagramm): .
        """
        pass
    def CreateSymbolBuilder(part: NXOpen.Part) -> SymbolBuilder:
        """
         Creates a NXOpen.DiagrammingLibraryAuthor.SymbolBuilder. 
         Returns builder ( SymbolBuilder NXOpen.Diagramm): .
        """
        pass
    def CreateSymbolPart(symbolName: str) -> NXOpen.Part:
        """
         Create a symbol part. 
         Returns symbolPart ( NXOpen.Part): .
        """
        pass
    def CreateSymbolPortBuilder(part: NXOpen.Part, portID: str) -> SymbolPortBuilder:
        """
         Creates a NXOpen.DiagrammingLibraryAuthor.SymbolPortBuilder. 
         Returns builder ( SymbolPortBuilder NXOpen.Diagramm): .
        """
        pass
    def CreateSymbolSaveBuilder(part: NXOpen.Part) -> SymbolSaveBuilder:
        """
         Creates a NXOpen.DiagrammingLibraryAuthor.SymbolSaveBuilder. 
         Returns builder ( SymbolSaveBuilder NXOpen.Diagramm): .
        """
        pass
    def CreateSymbolVariantBuilder(part: NXOpen.Part, variantID: int) -> SymbolVariantBuilder:
        """
         Creates a NXOpen.DiagrammingLibraryAuthor.SymbolVariantBuilder. 
         Returns builder ( SymbolVariantBuilder NXOpen.Diagramm): .
        """
        pass
    def LinkEquipment(part: NXOpen.Part, equipmentData: EquipmentData) -> None:
        """
         Links equipment to the symbol part. 
        """
        pass
    def OpenSymbolPart(partSpec: str) -> NXOpen.Part:
        """
         Open symbol in Symbol Designer environment. 
         Returns symbolPart ( NXOpen.Part): .
        """
        pass
    def UnlinkAllEquipment(part: NXOpen.Part) -> None:
        """
         Unlink all equipment from the symbol part. 
        """
        pass
    def UnlinkEquipment(part: NXOpen.Part, equipmentData: EquipmentData) -> None:
        """
         Unlink equipment from the symbol part. 
        """
        pass
import NXOpen
class SymbolPortBuilder(NXOpen.Builder): 
    """  Represents a SymbolPortBuilder.  
        Calling Builder.Commit on this builder will only return . """
    @property
    def ConnectionPoint(self) -> SymbolConnectionPointBuilder:
        """
        Getter for property: ( SymbolConnectionPointBuilder NXOpen.Diagramm) ConnectionPoint
         Returns the symbol connection point sub-builder.  
             
         
        """
        pass
    def GetAllowedAttachmentTypes(self) -> AllowedAttachmentTypes:
        """
         Get allowed attachment types. 
         Returns types ( AllowedAttachmentTypes NXOpen.Diagramm): .
        """
        pass
    def GetDirection(self) -> str:
        """
         Get port direction
         Returns portDirection (str):  the port direction .
        """
        pass
    def GetNumberAllowedConnections(self) -> int:
        """
         Get number allowed connections on port. 
         Returns num (int): .
        """
        pass
    def GetPortID(self) -> str:
        """
         Get port id
         Returns portID (str):  the port id .
        """
        pass
    def GetPortObject(self) -> AttributeHolder:
        """
         Gets the port objects which have user attributes of the port. 
         Returns portObject ( AttributeHolder NXOpen.Diagramm):  the port objects .
        """
        pass
    def SetAllowedAttachmentTypes(self, types: AllowedAttachmentTypes) -> None:
        """
         Set allowed attachment types. 
        """
        pass
    def SetDirection(self, portDirection: str) -> None:
        """
         Set port direction 
        """
        pass
    def SetNumberAllowedConnections(self, num: int) -> None:
        """
         Set number allowed connections on port. 
        """
        pass
    def SetPortID(self, portID: str) -> None:
        """
         Set port id 
        """
        pass
import NXOpen
class SymbolSaveBuilder(NXOpen.Builder): 
    """  Represents a SymbolSaveBuilder.  
        Calling Builder.Commit on this builder will only return . """
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the symbol file name   
            
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the symbol file name   
            
         
        """
        pass
    @property
    def FolderPath(self) -> str:
        """
        Getter for property: (str) FolderPath
         Returns the folder path to save symbol   
            
         
        """
        pass
    @FolderPath.setter
    def FolderPath(self, path: str):
        """
        Setter for property: (str) FolderPath
         Returns the folder path to save symbol   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the symbol name   
            
         
        """
        pass
    @Name.setter
    def Name(self, symbolName: str):
        """
        Setter for property: (str) Name
         Returns the symbol name   
            
         
        """
        pass
    @property
    def SaveAsMode(self) -> bool:
        """
        Getter for property: (bool) SaveAsMode
         Returns the flag that indicates if save-as mode is used.  
             
         
        """
        pass
    @SaveAsMode.setter
    def SaveAsMode(self, isSaveAs: bool):
        """
        Setter for property: (bool) SaveAsMode
         Returns the flag that indicates if save-as mode is used.  
             
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Gets the symbol description 
         Returns text (List[str]): .
        """
        pass
    def SetDescription(self, text: List[str]) -> None:
        """
         Sets the symbol description 
        """
        pass
import NXOpen
class SymbolVariantBuilder(NXOpen.Builder): 
    """  Represents a SymbolVariantBuilder.  
        Calling Builder.Commit on this builder will only return . """
    @property
    def AllowedSides(self) -> int:
        """
        Getter for property: (int) AllowedSides
         Returns the allowed sides on symbol   
            
         
        """
        pass
    @AllowedSides.setter
    def AllowedSides(self, val: int):
        """
        Setter for property: (int) AllowedSides
         Returns the allowed sides on symbol   
            
         
        """
        pass
    @property
    def AnchorPoint(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) AnchorPoint
         Returns the anchor location point  
            
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) AnchorPoint
         Returns the anchor location point  
            
         
        """
        pass
    @property
    def AttachingPolicy(self) -> AttachingPolicy:
        """
        Getter for property: ( AttachingPolicy NXOpen.Diagramm) AttachingPolicy
         Returns the attaching policy   
            
         
        """
        pass
    @AttachingPolicy.setter
    def AttachingPolicy(self, val: AttachingPolicy):
        """
        Setter for property: ( AttachingPolicy NXOpen.Diagramm) AttachingPolicy
         Returns the attaching policy   
            
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the variant description  
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the variant description  
            
         
        """
        pass
    @property
    def TagLocation(self) -> NXOpen.Point2d:
        """
        Getter for property: ( NXOpen.Point2d) TagLocation
         Returns the tag location point  
            
         
        """
        pass
    @TagLocation.setter
    def TagLocation(self, tagLocation: NXOpen.Point2d):
        """
        Setter for property: ( NXOpen.Point2d) TagLocation
         Returns the tag location point  
            
         
        """
        pass
    @property
    def VariantName(self) -> str:
        """
        Getter for property: (str) VariantName
         Returns the variant name  
            
         
        """
        pass
    @VariantName.setter
    def VariantName(self, variantName: str):
        """
        Setter for property: (str) VariantName
         Returns the variant name  
            
         
        """
        pass
    def SetPreviewImage(self, imageFile: str) -> None:
        """
         Set preview image 
        """
        pass
