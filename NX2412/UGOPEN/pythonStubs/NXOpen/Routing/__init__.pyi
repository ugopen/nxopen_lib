from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddFontBuilder(NXOpen.Builder): 
    """ Builder for creating an add font user interface dialogue """
    def SetBuilderData(self, selLine: NXOpen.Line, lineCoords: List[float], fontName: str, fontScale: float, fontLayer: int) -> None:
        """
         Takes selected line and information on the font selected which will be used to build the font 
        """
        pass
import NXOpen
class AdvanceToRsdBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Routing.AdvanceToRsdBuilder
    
        This builder takes assembly  subassembly and converts it to Routed Systems Designer structure.
    """
    class NamingMethod(Enum):
        """
        Members Include: 
         |Plugin| 
         |Incremental| 

        """
        Plugin: int
        Incremental: int
        @staticmethod
        def ValueOf(value: int) -> AdvanceToRsdBuilder.NamingMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AdvanceSpaceReservation(self) -> bool:
        """
        Getter for property: (bool) AdvanceSpaceReservation
         Returns the space reservation advancement   
            
         
        """
        pass
    @AdvanceSpaceReservation.setter
    def AdvanceSpaceReservation(self, advanceSpaceReservation: bool):
        """
        Setter for property: (bool) AdvanceSpaceReservation
         Returns the space reservation advancement   
            
         
        """
        pass
    @property
    def ComponentNamingMethod(self) -> AdvanceToRsdBuilder.NamingMethod:
        """
        Getter for property: ( AdvanceToRsdBuilder.NamingMethod NXOpen) ComponentNamingMethod
         Returns the component naming method type   
            
         
        """
        pass
    @ComponentNamingMethod.setter
    def ComponentNamingMethod(self, namingMethod: AdvanceToRsdBuilder.NamingMethod):
        """
        Setter for property: ( AdvanceToRsdBuilder.NamingMethod NXOpen) ComponentNamingMethod
         Returns the component naming method type   
            
         
        """
        pass
    @property
    def NamingPattern(self) -> NamingPatternBuilder:
        """
        Getter for property: ( NamingPatternBuilder NXOpen) NamingPattern
         Returns the naming pattern generating virtual terminals   
            
         
        """
        pass
    @NamingPattern.setter
    def NamingPattern(self, pattern: NamingPatternBuilder):
        """
        Setter for property: ( NamingPatternBuilder NXOpen) NamingPattern
         Returns the naming pattern generating virtual terminals   
            
         
        """
        pass
    @property
    def PartToAdvanceSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) PartToAdvanceSelection
         Returns the selected part to Advance   
            
         
        """
        pass
    @property
    def ReportResultToInfowindow(self) -> bool:
        """
        Getter for property: (bool) ReportResultToInfowindow
         Returns the report result to information window   
            
         
        """
        pass
    @ReportResultToInfowindow.setter
    def ReportResultToInfowindow(self, reportResultToInfowindow: bool):
        """
        Setter for property: (bool) ReportResultToInfowindow
         Returns the report result to information window   
            
         
        """
        pass
    def GenerateAndValidateNames(self) -> bool:
        """
         Generates component names via incremental or through plugin and validates them 
         Returns isValid (bool): .
        """
        pass
    def GetGeneratedNames(self) -> List[str]:
        """
         Get the generated names 
         Returns generated_names (List[str]): .
        """
        pass
import NXOpen
class AlignStockBuilder(NXOpen.Builder): 
    """ Represents a Routing.AlignStockBuilder
    Builder for aligning non-circular stocks.
        Two methods are provided to user to make stocks alignment:
            Routing Object: specify the referencing routing object and deriving the reference rotate vector from it,
            Vector to Vector: specify the to vector as reference and the from vector as the target, then align them.
    """
    class StockAlignmentMethod(Enum):
        """
        Members Include: 
         |RoutingObject| 
         |VectorToVector| 

        """
        RoutingObject: int
        VectorToVector: int
        @staticmethod
        def ValueOf(value: int) -> AlignStockBuilder.StockAlignmentMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignmentMethod(self) -> AlignStockBuilder.StockAlignmentMethod:
        """
        Getter for property: ( AlignStockBuilder.StockAlignmentMethod NXOpen) AlignmentMethod
         Returns the alignment method.  
             
         
        """
        pass
    @AlignmentMethod.setter
    def AlignmentMethod(self, alignmentMethod: AlignStockBuilder.StockAlignmentMethod):
        """
        Setter for property: ( AlignStockBuilder.StockAlignmentMethod NXOpen) AlignmentMethod
         Returns the alignment method.  
             
         
        """
        pass
    @property
    def ReferenceObject(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) ReferenceObject
         Returns the reference object.  
           The reference object could be a stock or a qualified part.  
         
        """
        pass
    @property
    def ReferenceVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ReferenceVector
         Returns  the reference vector.  
             
         
        """
        pass
    @ReferenceVector.setter
    def ReferenceVector(self, toVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ReferenceVector
         Returns  the reference vector.  
             
         
        """
        pass
    @property
    def StocksToAlign(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) StocksToAlign
         Returns  a collection of stocks to align.  
             
         
        """
        pass
    @property
    def TargetVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) TargetVector
         Returns the target vector.  
             
         
        """
        pass
    @TargetVector.setter
    def TargetVector(self, fromVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) TargetVector
         Returns the target vector.  
             
         
        """
        pass
import NXOpen
class AnchorBuilder(NXOpen.Builder): 
    """ Builder for creating  editing the Anchors. """
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point   
            
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point   
            
         
        """
        pass
    @property
    def StringName(self) -> str:
        """
        Getter for property: (str) StringName
         Returns the anchor name string   
            
         
        """
        pass
    @StringName.setter
    def StringName(self, stringName: str):
        """
        Setter for property: (str) StringName
         Returns the anchor name string   
            
         
        """
        pass
import NXOpen
class AnchorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Anchor objects. 

    Iterating this collection only returns live uncondemned objects contained in the owning part
    of the collection. Note that NXOpen.Routing.Anchor is a smart object and many smart objects are condemned as they 
    only exist to support other objects and are not displayed."""
    @overload
    def CreateAnchor(self, origin: NXOpen.Point3d) -> Anchor:
        """
         Creates a NXOpen.Routing.Anchor object. 
         Returns part_anchor ( Anchor NXOpen):  .
        """
        pass
    @overload
    def CreateAnchor(self, position: NXOpen.Point3d, point: NXOpen.Point) -> Anchor:
        """
         Creates a NXOpen.Routing.Anchor object. 
         Returns part_anchor ( Anchor NXOpen):  .
        """
        pass
import NXOpen
class Anchor(NXOpen.SmartObject): 
    """ 
        A Routing Anchor defines a position in a Qualified Routing component part.  
        In a fitting part, the anchor provides an placement point used by Place 
        Part to position the component into an assembly. In a stock profile part, 
        anchors provide an alternate position at which the cross section may be
        located with respect to the segment it is swept along.
    """
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @property
    def Position(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
    @Position.setter
    def Position(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
    def GetStock(self) -> List[Stock]:
        """
         Returns the stock(s) to which an Anchor belongs. 
         Returns stocks ( Stock List[NXOp):   .
        """
        pass
    def GetStockData(self) -> StockData:
        """
         Returns the stock data to which an Anchor belongs. 
         Returns stock_data ( StockData NXOpen):   .
        """
        pass
import NXOpen
class ArcSegmentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.ArcSegment objects. """
    pass
import NXOpen
class ArcSegment(NXOpen.Arc): 
    """ Represents a arc segment. """
    @property
    def FollowCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) FollowCurve
         Returns  the segment follow curve.  
            NULL object indicates segment has no follow curve   
         
        """
        pass
    @property
    def Guid(self) -> str:
        """
        Getter for property: (str) Guid
         Returns the Globally Unique Identifier (GUID) for this segment.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns  the length of the segment.  
             
         
        """
        pass
    def GetCorner(self) -> Corner:
        """
         Returns the corner that controls this arc segment, if any.
                    Returns  if this segment was created as a connected curve rather than
                    from a corner.
                
         Returns corner ( Corner NXOpen): .
        """
        pass
class AssemblyDefinition(ItemDefinition): 
    """
         Represents a collection of NXOpen.Routing.SingleDevice objects that are used in an assembled product.
       
       
        
       
         This class is abstract.
        
    """
    def AddSingleDeviceChild(self, device: SingleDevice) -> None:
        """
         Adds a NXOpen.Routing.SingleDevice object to the list of objects contained in the assembly. 
        """
        pass
    def GetReferencingDevice(self) -> SingleDevice:
        """
         Gets the NXOpen.Routing.SingleDevice object that has this AssemblyDefinition object as its definition. 
         Returns device ( SingleDevice NXOpen):  instance of the AssemblyDefinion .
        """
        pass
    def GetSingleDeviceChildren(self) -> List[SingleDevice]:
        """
         Gets the list of NXOpen.Routing.SingleDevice objects contained in the assembly. 
                    The returned list is empty if the assembly does not contain any objects. 
         Returns childrenOfDevice ( SingleDevice List[NXOp):  list of objects in the assembly .
        """
        pass
    def IsSingleDeviceChild(self, device: SingleDevice) -> bool:
        """
         Determines if a NXOpen.Routing.SingleDevice object is contained in the assembly 
         Returns value (bool):  TRUE if the object is in the AssemblyDefinition .
        """
        pass
    def RemoveSingleDeviceChild(self, device: SingleDevice) -> None:
        """
         Removes a NXOpen.Routing.SingleDevice from the list of objects contained in the assembly. 
        """
        pass
    def ReplaceSingleDeviceChildren(self, replacementChildren: List[SingleDevice]) -> None:
        """
         Replaces the list of NXOpen.Routing.SingleDevice objects contained in the assembly. 
                    Using  for replacementChildren is not allowed. 
        """
        pass
import NXOpen.Assemblies
class AssemblyNamePluginData(NamePluginData): 
    """ Data object created by Routing just before creating spool assemblies.
        Routing expects the plugin you write to fill in the required information for the
        new assembly name.

        For more information, see Routing.CustomManager and the
        Routing.CustomManager.SetSpoolAssemblyNamePlugin.
    """
    def GetComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the components that will go into the new assembly. 
         Returns components ( NXOpen.Assemblies.Component Li):  The Assemblies.Components that will go into the new assembly. .
        """
        pass
import NXOpen
class AssignCornerBuilder(NXOpen.Builder): 
    """ Builder class for Assign Corner which creates corner"""
    @property
    def RadiusFromBendTable(self) -> float:
        """
        Getter for property: (float) RadiusFromBendTable
         Returns the radius determined using the stock and the bend radius table.  
             
         
        """
        pass
    @RadiusFromBendTable.setter
    def RadiusFromBendTable(self, radius: float):
        """
        Setter for property: (float) RadiusFromBendTable
         Returns the radius determined using the stock and the bend radius table.  
             
         
        """
        pass
    @property
    def ReverseValue(self) -> int:
        """
        Getter for property: (int) ReverseValue
         Returns the value to store whether reverse order (for bend creation) or not  
            
         
        """
        pass
    @ReverseValue.setter
    def ReverseValue(self, num: int):
        """
        Setter for property: (int) ReverseValue
         Returns the value to store whether reverse order (for bend creation) or not  
            
         
        """
        pass
    @property
    def RouteAssignCornerCornerBlock(self) -> CornerTypeBuilder:
        """
        Getter for property: ( CornerTypeBuilder NXOpen) RouteAssignCornerCornerBlock
         Returns the route assign corner corner block   
            
         
        """
        pass
    @property
    def RouteAssignCornerEndObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) RouteAssignCornerEndObject
         Returns the route assign corner end objects.  
            Valid start objects objects are  NXOpen::Routing::ControlPoint 
                    and  NXOpen::Routing::ISegment   
         
        """
        pass
    @property
    def RouteAssignCornerRouteSelection(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteAssignCornerRouteSelection
         Returns the routing object colletor   
            
         
        """
        pass
    @property
    def RouteAssignCornerStartObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) RouteAssignCornerStartObject
         Returns the route assign corner start objects.  
            Valid start objects are  NXOpen::Routing::ControlPoint 
                    and  NXOpen::Routing::ISegment   
         
        """
        pass
    @property
    def SelectCopeStock(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectCopeStock
         Returns the user selected correct object where correct object is
                 NXOpen::Routing::Stock  and  NXOpen::Routing::ISegment .  
          
                   
         
        """
        pass
    @property
    def UBendSelection(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) UBendSelection
         Returns the routing object collector for ubend  
            
         
        """
        pass
    def GetAttributeHolder(self) -> NXOpen.NXObject:
        """
         Gets Attribute holder in builder, which is user for template attribute assignment. 
         Returns attributeHolder ( NXOpen.NXObject):  Object to hold template attributes .
        """
        pass
    def GetBendCornerAttributes(self) -> CharacteristicList:
        """
         Corner Attributes 
         Returns selectedRowAttributesCharxList ( CharacteristicList NXOpen): .
        """
        pass
    def SetBendCornerAttributes(self, selectedRowAttributesCharxList: CharacteristicList) -> None:
        """
         Corner Attributes 
        """
        pass
    def SetStockList(self, stockObjects: List[Stock]) -> None:
        """
         Set the NXOpen.Routing.Stock object list when list box
                    is updated. 
        """
        pass
import NXOpen
class AssignDiscontinuityBuilder(NXOpen.Builder): 
    """ the Builder to Assign Discontinuity for the stocks """
    class Types(Enum):
        """
        Members Include: 
         |Simple| 
         |Complex| 

        """
        Simple: int
        Complex: int
        @staticmethod
        def ValueOf(value: int) -> AssignDiscontinuityBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComplexPoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ComplexPoint
         Returns the Rcp type of the selected object    
            
         
        """
        pass
    @property
    def SegPairList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) SegPairList
         Returns the list of selected segments pairs  
            
         
        """
        pass
    @property
    def SegmentPair(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SegmentPair
         Returns the segment pairs selected for the assigning Discontinuity   
            
         
        """
        pass
    @property
    def SimplePoint(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SimplePoint
         Returns the Rcp type of the selected object    
            
         
        """
        pass
    @property
    def Type(self) -> AssignDiscontinuityBuilder.Types:
        """
        Getter for property: ( AssignDiscontinuityBuilder.Types NXOpen) Type
         Returns the type of Block  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: AssignDiscontinuityBuilder.Types):
        """
        Setter for property: ( AssignDiscontinuityBuilder.Types NXOpen) Type
         Returns the type of Block  
            
         
        """
        pass
    def SegmentPairBuilder(self) -> SegmentPairBuilder:
        """
         Creates a SegmentPairBuilder  used to create list item for AssignDiscontinuity 
         Returns builder ( SegmentPairBuilder NXOpen):  .
        """
        pass
import NXOpen
class AssignPathBuilder(NXOpen.Builder): 
    """Assigns path to a broken routing run """
    @property
    def RouteObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteObjectCollector
         Returns the route object collector   
            
         
        """
        pass
    def AddToScopedObjectSet(self, objectValue: NXOpen.NXObject, runItemType: RunItem.Type) -> None:
        """
         Add the given object to the scoped object set
        """
        pass
import NXOpen
class AssignTangencyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.AssignTangencyBuilder object.
        Provides support for NXOpen.Routing.SplinePathBuilder when assigning
        tangency constraints between adjacent splines.
    """
    class TangencySide(Enum):
        """
        Members Include: 
         |Undefined|  The tangency side is undefined.         
         |Source|  Assign tangency at source ControlPoint. 
         |Target|  Assign tangency at target ControlPoint. 

        """
        Undefined: int
        Source: int
        Target: int
        @staticmethod
        def ValueOf(value: int) -> AssignTangencyBuilder.TangencySide:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssignTangencySide(self) -> AssignTangencyBuilder.TangencySide:
        """
        Getter for property: ( AssignTangencyBuilder.TangencySide NXOpen) AssignTangencySide
         Returns the tangency side  NXOpen::Routing::AssignTangencyBuilder::TangencySide  to assign tangency  
            
         
        """
        pass
    @AssignTangencySide.setter
    def AssignTangencySide(self, tangencySide: AssignTangencyBuilder.TangencySide):
        """
        Setter for property: ( AssignTangencyBuilder.TangencySide NXOpen) AssignTangencySide
         Returns the tangency side  NXOpen::Routing::AssignTangencyBuilder::TangencySide  to assign tangency  
            
         
        """
        pass
    @property
    def SelectedTangencyGroup(self) -> TangencyGroupBuilder:
        """
        Getter for property: ( TangencyGroupBuilder NXOpen) SelectedTangencyGroup
         Returns the selected  NXOpen::Routing::TangencyGroupBuilder  to assign tangency
                    at specified side of the spline.  
          
                  
         
        """
        pass
    @SelectedTangencyGroup.setter
    def SelectedTangencyGroup(self, selectedTangencyGroup: TangencyGroupBuilder):
        """
        Setter for property: ( TangencyGroupBuilder NXOpen) SelectedTangencyGroup
         Returns the selected  NXOpen::Routing::TangencyGroupBuilder  to assign tangency
                    at specified side of the spline.  
          
                  
         
        """
        pass
    def AssignTangency(self, segments: List[NXOpen.Curve], tangencySide: AssignTangencyBuilder.TangencySide) -> None:
        """
         Assign tangency at specified side of the spline.
                    See NXOpen.Routing.AssignTangencyBuilder.TangencySide for valid
                    options.
                
        """
        pass
    def AssignTangencyAtPort(self, tangencySide: AssignTangencyBuilder.TangencySide) -> None:
        """
         Assign tangency at attached port.
                    See NXOpen.Routing.AssignTangencyBuilder.TangencySide for valid
                    options.
                
        """
        pass
    def CreateTangencyGroupBuilder(self) -> TangencyGroupBuilder:
        """
         Creates a NXOpen.Routing.TangencyGroupBuilder object. 
         Returns tangencyGroupBuilder ( TangencyGroupBuilder NXOpen): .
        """
        pass
    def RemoveTangency(self, tangencySide: AssignTangencyBuilder.TangencySide) -> None:
        """
         Remove tangency at specified side of the spline.
                    See NXOpen.Routing.AssignTangencyBuilder.TangencySide for valid
                    options.
                
        """
        pass
import NXOpen
class AssignTerminalsBuilder(NXOpen.Builder): 
    """ Builder for creatingediting terminals. """
    @property
    def NamingPattern(self) -> NamingPatternBuilder:
        """
        Getter for property: ( NamingPatternBuilder NXOpen) NamingPattern
         Returns the naming pattern generating virtual terminals   
            
         
        """
        pass
    @NamingPattern.setter
    def NamingPattern(self, pattern: NamingPatternBuilder):
        """
        Setter for property: ( NamingPatternBuilder NXOpen) NamingPattern
         Returns the naming pattern generating virtual terminals   
            
         
        """
        pass
    @property
    def TerminalList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) TerminalList
         Returns the List Containing the Terminals   
            
         
        """
        pass
    def AddPortArrays(self) -> None:
        """
         The port arrays dialog launching button
        """
        pass
    def GenerateSequence(self) -> int:
        """
         The Generate Sequence button 
         Returns errorCode (int): .
        """
        pass
import NXOpen
class AssignTerminalsItemBuilder(NXOpen.Builder): 
    """ Builder for creatingediting terminals. """
    @property
    def TerminalDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) TerminalDirection
         Returns the terminal direction   
            
         
        """
        pass
    @TerminalDirection.setter
    def TerminalDirection(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) TerminalDirection
         Returns the terminal direction   
            
         
        """
        pass
    @property
    def TerminalName(self) -> str:
        """
        Getter for property: (str) TerminalName
         Returns the terminal name   
            
         
        """
        pass
    @TerminalName.setter
    def TerminalName(self, terminalName: str):
        """
        Setter for property: (str) TerminalName
         Returns the terminal name   
            
         
        """
        pass
    @property
    def TerminalOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TerminalOrigin
         Returns the terminal origin point   
            
         
        """
        pass
    @TerminalOrigin.setter
    def TerminalOrigin(self, originPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TerminalOrigin
         Returns the terminal origin point   
            
         
        """
        pass
import NXOpen
class AttributeHolder(NXOpen.NXObject): 
    """
    Represents a NXOpen.Routing.AttributeHolder
    """
    def CopyAttributesToObject2(self, nxobject: NXOpen.NXObject) -> None:
        """
         Copies the Template Attributes of this object to a Routing Component.
                    Use this method to properly handle the journaling of copying attributes. 
        """
        pass
    def SetAttributes(self) -> None:
        """
         Sets the Template Attributes to this object 
        """
        pass
    def SetFunctionType(self, functionType: str) -> None:
        """
         Sets the function type for which Template Attributes to be applied 
        """
        pass
import NXOpen
class AttributeMembersBuilder(NXOpen.Builder): 
    """Creates attibutemembers builder object to add to the search criteria list used by FindByAttributesBuilder"""
    @property
    def AttributeName(self) -> str:
        """
        Getter for property: (str) AttributeName
         Returnsthe string containing attribute title to search for  
            
         
        """
        pass
    @AttributeName.setter
    def AttributeName(self, attributeName: str):
        """
        Setter for property: (str) AttributeName
         Returnsthe string containing attribute title to search for  
            
         
        """
        pass
    @property
    def AttributeValue(self) -> str:
        """
        Getter for property: (str) AttributeValue
         Returnsthe string containing attribute value to search for  
            
         
        """
        pass
    @AttributeValue.setter
    def AttributeValue(self, attributeValue: str):
        """
        Setter for property: (str) AttributeValue
         Returnsthe string containing attribute value to search for  
            
         
        """
        pass
import NXOpen
class BendCornerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.BendCorner objects. """
    class Type(Enum):
        """
        Members Include: 
         |RadiusRatio|  Using radius or ratio to
                                                               create a bend corner. 
         |Table|   Using a bend table to create a
                                                               bend corner. 

        """
        RadiusRatio: int
        Table: int
        @staticmethod
        def ValueOf(value: int) -> BendCornerCollection.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AssignCornerByBendRadius(self, bend_crn: ControlPoint, bend_radius: float) -> BendCorner:
        """
         This routine assigns a new bend corner to the given input bend corner object using
                    bend radius. This "assignment" can involve the removal of an existing
                    corner at this location and the creation of a new corner. 
         Returns new_crn ( BendCorner NXOpen):  The newly created Bend Corner .
        """
        pass
    def AssignCornerByBendRatio(self, bend_crn: ControlPoint, bend_ratio: float) -> BendCorner:
        """
         This routine assigns a new bend corner to the given input bend corner object using
                    bend ratio. This "assignment" can involve the removal of an existing
                    corner at this location and the creation of a new corner. 
         Returns new_crn ( BendCorner NXOpen):  The newly created Bend Corner .
        """
        pass
    def AssignCornerByBendRatioToAttribute(self, bend_crn: ControlPoint, bend_ratio_to_attribute: float, bend_attribute_name: str) -> BendCorner:
        """
         This routine assigns a new bend corner to the given input bend corner object using
                    bend ratio. This "assignment" can involve the removal of an existing
                    corner at this location and the creation of a new corner. 
         Returns new_crn ( BendCorner NXOpen):  The newly created Bend Corner .
        """
        pass
    def AssignCornerByBendTable(self, rcp: ControlPoint, bend_table: str) -> BendCorner:
        """
         This routine assigns a bend corner to the given input RCP object using
                    a bend table entry. This "assignment" can involve the removal of an existing
                    corner at this location and the creation of a new corner.  The
                    application view must be loaded before attempting to assign a
                    bend corner of this type.  
         Returns new_crn ( BendCorner NXOpen):  The newly created Bend Corner .
        """
        pass
    def CreateCorner(self, rcp: ControlPoint, bend_method: CornerTypeBuilder.BendMethods, bend_ratio: float, bend_radius: float) -> BendCorner:
        """
         Create a bend corner object at a Control Point. 
         Returns bend ( BendCorner NXOpen):  The new bend corner. .
        """
        pass
    def CreateCornerFromAttribute(self, rcp: ControlPoint, bend_method: CornerTypeBuilder.BendMethods, bend_ratio: float, bend_radius: float, bend_ratio_to_attribute: float, bend_attribute_name: str) -> BendCorner:
        """
         Create a bend corner object at a Control Point from specified attribute. 
         Returns bend ( BendCorner NXOpen):  The new bend corner. .
        """
        pass
    def GetBendAssociatedToSegment(self, segment: ISegment) -> BendCorner:
        """
         Enquire the Bend Corner that this segment represents.
                    ( can be returned, indicating that this segment does not
                    represent a Bend Corner.) 
         Returns corner ( BendCorner NXOpen):  Bend Corner that segment represents
                                              ( can be returned,indicating that
                                              segment does not represent a Bend Corner). .
        """
        pass
    def GetBendCornersFromObjects(self, objects: List[NXOpen.NXObject]) -> List[BendCorner]:
        """
         Returns all the corners connected to the given objects, if any.
                    Can find corners from NXOpen.Routing.ControlPoints,
                    NXOpen.Routing.ISegments, or NXOpen.Routing.Stock.
         Returns corners ( BendCorner List[NXOp):  .
        """
        pass
import NXOpen
class BendCorner(Corner): 
    """ 
        Computes a fillet curve between two linear segments to form a smooth
        bend transition from one segment to another.
     """
    @property
    def BendAttributeName(self) -> str:
        """
        Getter for property: (str) BendAttributeName
         Returns the bend ratio to apply when computing the bend radius   
            
         
        """
        pass
    @BendAttributeName.setter
    def BendAttributeName(self, bend_attribute_name: str):
        """
        Setter for property: (str) BendAttributeName
         Returns the bend ratio to apply when computing the bend radius   
            
         
        """
        pass
    @property
    def BendMethod(self) -> CornerTypeBuilder.BendMethods:
        """
        Getter for property: ( CornerTypeBuilder.BendMethods NXOpen) BendMethod
         Returnsthe bend method   
            
         
        """
        pass
    @BendMethod.setter
    def BendMethod(self, bend_method: CornerTypeBuilder.BendMethods):
        """
        Setter for property: ( CornerTypeBuilder.BendMethods NXOpen) BendMethod
         Returnsthe bend method   
            
         
        """
        pass
    @property
    def BendRadius(self) -> float:
        """
        Getter for property: (float) BendRadius
         Returns the bend radius of the corner.  
             
         
        """
        pass
    @BendRadius.setter
    def BendRadius(self, bend_radius: float):
        """
        Setter for property: (float) BendRadius
         Returns the bend radius of the corner.  
             
         
        """
        pass
    @property
    def BendRatio(self) -> float:
        """
        Getter for property: (float) BendRatio
         Returns the bend ratio to apply when computing the bend radius   
            
         
        """
        pass
    @BendRatio.setter
    def BendRatio(self, bend_ratio: float):
        """
        Setter for property: (float) BendRatio
         Returns the bend ratio to apply when computing the bend radius   
            
         
        """
        pass
    @property
    def BendRatioToAttribute(self) -> float:
        """
        Getter for property: (float) BendRatioToAttribute
         Returns the bend ratio to apply when computing the bend radius   
            
         
        """
        pass
    @BendRatioToAttribute.setter
    def BendRatioToAttribute(self, bend_ratio_to_attribute: float):
        """
        Setter for property: (float) BendRatioToAttribute
         Returns the bend ratio to apply when computing the bend radius   
            
         
        """
        pass
    def FindSideSegments(self) -> List[NXOpen.Curve]:
        """
         Returns the straight line segments attached to the fillet curve
                   of this bend corner.  
         Returns side_segs ( NXOpen.Curve Li):  the side segments. There will be from 0 to 2 
                                                           total side segments. .
        """
        pass
    def GetSegment(self) -> ISegment:
        """
         The bend segment following the fillet curve created for the bend. 
         Returns segment ( ISegment NXOpen):  .
        """
        pass
import NXOpen
import NXOpen.CAM
class BendReportManager(NXOpen.Object): 
    """ The Routing Bend Report Manager allows you to get a variety of bend reports. """
    class Mil98Report:
        """
         Used in the MIL-D-9898 C specification reports.
                    All values are absolute and cumulative.
                    See MIL-D-9898C for more information.
                
         BendReportManagerMil98Report_Struct NXOpen is an alias for  BendReportManager.Mil98Report NXOpen.
        """
        @property
        def C(self) -> float:
            """
            Getter for property C
            The distance before the bend, from the start of the cable                           to the beginning point of the bend.

            """
            pass
        @C.setter
        def C(self, value: float):
            """
            Getter for property C
            The distance before the bend, from the start of the cable                           to the beginning point of the bend.
            Setter for property C
            The distance before the bend, from the start of the cable                           to the beginning point of the bend.

            """
            pass
        @property
        def F(self) -> float:
            """
            Getter for property F
            The radius of the bend.

            """
            pass
        @F.setter
        def F(self, value: float):
            """
            Getter for property F
            The radius of the bend.
            Setter for property F
            The radius of the bend.

            """
            pass
        @property
        def E(self) -> float:
            """
            Getter for property E
            The turn angle, this is the angle about the Y axis, relative                           to initial position (cumulation of the B value in YBC).

            """
            pass
        @E.setter
        def E(self, value: float):
            """
            Getter for property E
            The turn angle, this is the angle about the Y axis, relative                           to initial position (cumulation of the B value in YBC).
            Setter for property E
            The turn angle, this is the angle about the Y axis, relative                           to initial position (cumulation of the B value in YBC).

            """
            pass
        @property
        def G(self) -> float:
            """
            Getter for property G
            The bend angle.

            """
            pass
        @G.setter
        def G(self, value: float):
            """
            Getter for property G
            The bend angle.
            Setter for property G
            The bend angle.

            """
            pass
        @property
        def Y(self) -> float:
            """
            Getter for property Y
            The Y value from the YBC format.

            """
            pass
        @Y.setter
        def Y(self, value: float):
            """
            Getter for property Y
            The Y value from the YBC format.
            Setter for property Y
            The Y value from the YBC format.

            """
            pass
    class SegmentInformation:
        """
         Used by all the reports to hold the information of the segments under port,
                    solid body, segment, stock, stock component, or feature representing the piece of stock.
                    Generated by calling  Routing::BendReportManager::GetSegmentInformation .
                
         BendReportManagerSegmentInformation_Struct NXOpen is an alias for  BendReportManager.SegmentInformation NXOpen.
        """
        @property
        def Stock(self) -> Stock:
            """
            Getter for property Stock
             Routing::Stock 

            """
            pass
        @Stock.setter
        def Stock(self, value: Stock):
            """
            Getter for property Stock
             Routing::Stock 
            Setter for property Stock
             Routing::Stock 

            """
            pass
        @property
        def Segment(self) -> NXOpen.CAM.NXOpen.Curve:
            """
            Getter for property Segment
            The segment itself.

            """
            pass
        @Segment.setter
        def Segment(self, value: NXOpen.CAM.NXOpen.Curve):
            """
            Getter for property Segment
            The segment itself.
            Setter for property Segment
            The segment itself.

            """
            pass
        @property
        def IsStraight(self) -> bool:
            """
            Getter for property IsStraight
            True if the  Routing::ISegment  is straight.

            """
            pass
        @IsStraight.setter
        def IsStraight(self, value: bool):
            """
            Getter for property IsStraight
            True if the  Routing::ISegment  is straight.
            Setter for property IsStraight
            True if the  Routing::ISegment  is straight.

            """
            pass
        @property
        def Length(self) -> float:
            """
            Getter for property Length
            Length of  Routing::ISegment 

            """
            pass
        @Length.setter
        def Length(self, value: float):
            """
            Getter for property Length
            Length of  Routing::ISegment 
            Setter for property Length
            Length of  Routing::ISegment 

            """
            pass
        @property
        def StartControlPoint(self) -> NXOpen.Routing.ControlPoint:
            """
            Getter for property StartControlPoint
            Start  Routing::ControlPoint .

            """
            pass
        @StartControlPoint.setter
        def StartControlPoint(self, value: NXOpen.Routing.ControlPoint):
            """
            Getter for property StartControlPoint
            Start  Routing::ControlPoint .
            Setter for property StartControlPoint
            Start  Routing::ControlPoint .

            """
            pass
        @property
        def EndControlPoint(self) -> NXOpen.Routing.ControlPoint:
            """
            Getter for property EndControlPoint
            End  Routing::ControlPoint .

            """
            pass
        @EndControlPoint.setter
        def EndControlPoint(self, value: NXOpen.Routing.ControlPoint):
            """
            Getter for property EndControlPoint
            End  Routing::ControlPoint .
            Setter for property EndControlPoint
            End  Routing::ControlPoint .

            """
            pass
        @property
        def BendCorner(self) -> BendCorner:
            """
            Getter for property BendCorner
             Routing::BendCorner 

            """
            pass
        @BendCorner.setter
        def BendCorner(self, value: BendCorner):
            """
            Getter for property BendCorner
             Routing::BendCorner 
            Setter for property BendCorner
             Routing::BendCorner 

            """
            pass
        @property
        def BendRadius(self) -> float:
            """
            Getter for property BendRadius
            Radius of the bend

            """
            pass
        @BendRadius.setter
        def BendRadius(self, value: float):
            """
            Getter for property BendRadius
            Radius of the bend
            Setter for property BendRadius
            Radius of the bend

            """
            pass
        @property
        def BendPosition(self) -> NXOpen.Point3d:
            """
            Getter for property BendPosition
            Position of the bend rcp

            """
            pass
        @BendPosition.setter
        def BendPosition(self, value: NXOpen.Point3d):
            """
            Getter for property BendPosition
            Position of the bend rcp
            Setter for property BendPosition
            Position of the bend rcp

            """
            pass
        @property
        def StartNormal(self) -> NXOpen.Vector3d:
            """
            Getter for property StartNormal
            Normal of curve at start points

            """
            pass
        @StartNormal.setter
        def StartNormal(self, value: NXOpen.Vector3d):
            """
            Getter for property StartNormal
            Normal of curve at start points
            Setter for property StartNormal
            Normal of curve at start points

            """
            pass
        @property
        def EndNormal(self) -> NXOpen.Vector3d:
            """
            Getter for property EndNormal
            Normal of curve at end points

            """
            pass
        @EndNormal.setter
        def EndNormal(self, value: NXOpen.Vector3d):
            """
            Getter for property EndNormal
            Normal of curve at end points
            Setter for property EndNormal
            Normal of curve at end points

            """
            pass
        @property
        def StartControlPointPosition(self) -> NXOpen.Point3d:
            """
            Getter for property StartControlPointPosition
            Location of start  Routing::ControlPoint                                                                                        in ABS coordinates, use this instead of the start                                                                                        Routing::ControlPoint  for S-Bends                                                                                       and bends greater than or equal to 180 degrees.

            """
            pass
        @StartControlPointPosition.setter
        def StartControlPointPosition(self, value: NXOpen.Point3d):
            """
            Getter for property StartControlPointPosition
            Location of start  Routing::ControlPoint                                                                                        in ABS coordinates, use this instead of the start                                                                                        Routing::ControlPoint  for S-Bends                                                                                       and bends greater than or equal to 180 degrees.
            Setter for property StartControlPointPosition
            Location of start  Routing::ControlPoint                                                                                        in ABS coordinates, use this instead of the start                                                                                        Routing::ControlPoint  for S-Bends                                                                                       and bends greater than or equal to 180 degrees.

            """
            pass
        @property
        def EndControlPointPosition(self) -> NXOpen.Point3d:
            """
            Getter for property EndControlPointPosition
            Location of end  Routing::ControlPoint                                                                                        in ABS coordinates, use this instead of the end                                                                                        Routing::ControlPoint  for S-Bends                                                                                       and bends greater than or equal to 180 degrees.

            """
            pass
        @EndControlPointPosition.setter
        def EndControlPointPosition(self, value: NXOpen.Point3d):
            """
            Getter for property EndControlPointPosition
            Location of end  Routing::ControlPoint                                                                                        in ABS coordinates, use this instead of the end                                                                                        Routing::ControlPoint  for S-Bends                                                                                       and bends greater than or equal to 180 degrees.
            Setter for property EndControlPointPosition
            Location of end  Routing::ControlPoint                                                                                        in ABS coordinates, use this instead of the end                                                                                        Routing::ControlPoint  for S-Bends                                                                                       and bends greater than or equal to 180 degrees.

            """
            pass
    class XyzReport:
        """
         Used in the XYZ bend reports. The first bend value is at one end point of the stock body
                    and the last bend value is at the other end point of the stock body.  The other bend
                    values are the location in work coordinates of the bend  Routing::ControlPoint s
                    associated with each bend or the location of where the bend  Routing::ControlPoint s
                    would be if they existed.
                
         BendReportManagerXyzReport_Struct NXOpen is an alias for  BendReportManager.XyzReport NXOpen.
        """
        @property
        def Xc(self) -> float:
            """
            Getter for property Xc
            X position of bend  Routing::ControlPoint  in work coordinates.

            """
            pass
        @Xc.setter
        def Xc(self, value: float):
            """
            Getter for property Xc
            X position of bend  Routing::ControlPoint  in work coordinates.
            Setter for property Xc
            X position of bend  Routing::ControlPoint  in work coordinates.

            """
            pass
        @property
        def Yc(self) -> float:
            """
            Getter for property Yc
            Y position of bend  Routing::ControlPoint  in work coordinates.

            """
            pass
        @Yc.setter
        def Yc(self, value: float):
            """
            Getter for property Yc
            Y position of bend  Routing::ControlPoint  in work coordinates.
            Setter for property Yc
            Y position of bend  Routing::ControlPoint  in work coordinates.

            """
            pass
        @property
        def Zc(self) -> float:
            """
            Getter for property Zc
            Z position of bend  Routing::ControlPoint  in work coordinates.

            """
            pass
        @Zc.setter
        def Zc(self, value: float):
            """
            Getter for property Zc
            Z position of bend  Routing::ControlPoint  in work coordinates.
            Setter for property Zc
            Z position of bend  Routing::ControlPoint  in work coordinates.

            """
            pass
        @property
        def Radius(self) -> float:
            """
            Getter for property Radius
            Radius of the bend.

            """
            pass
        @Radius.setter
        def Radius(self, value: float):
            """
            Getter for property Radius
            Radius of the bend.
            Setter for property Radius
            Radius of the bend.

            """
            pass
    class YbcReport:
        """
         Used in the YBC bend reports. The last bend value isn't actually a bend.
                    The only valid value is the Y value, which is the length after the last bend.
                    All values are relative, meaning they are calculated from the previous bend.
                    So if bend1 has B value of 90 degrees and bend2 has a B value of 90 degrees,
                    then the pipe has rotated 180 degrees about the Y axis.
                
         BendReportManagerYbcReport_Struct NXOpen is an alias for  BendReportManager.YbcReport NXOpen.
        """
        @property
        def Y(self) -> float:
            """
            Getter for property Y
            The length along the stock before the bend.

            """
            pass
        @Y.setter
        def Y(self, value: float):
            """
            Getter for property Y
            The length along the stock before the bend.
            Setter for property Y
            The length along the stock before the bend.

            """
            pass
        @property
        def B(self) -> float:
            """
            Getter for property B
            The rotation angle in degrees about the Y axis of the stock.

            """
            pass
        @B.setter
        def B(self, value: float):
            """
            Getter for property B
            The rotation angle in degrees about the Y axis of the stock.
            Setter for property B
            The rotation angle in degrees about the Y axis of the stock.

            """
            pass
        @property
        def C(self) -> float:
            """
            Getter for property C
            The rotation angle in degrees about the Z axis of the stock.

            """
            pass
        @C.setter
        def C(self, value: float):
            """
            Getter for property C
            The rotation angle in degrees about the Z axis of the stock.
            Setter for property C
            The rotation angle in degrees about the Z axis of the stock.

            """
            pass
        @property
        def Radius(self) -> float:
            """
            Getter for property Radius
            Radius of the bend.

            """
            pass
        @Radius.setter
        def Radius(self, value: float):
            """
            Getter for property Radius
            Radius of the bend.
            Setter for property Radius
            Radius of the bend.

            """
            pass
    def GenerateMil98Report(self, segmentInformation: List[BendReportManager.SegmentInformation]) -> Tuple[List[BendReportManager.Mil98Report], float]:
        """
         Generates the bend report in MIL-D-9898C specification format. 
         Returns A tuple consisting of (bends, totalLength). 
         - bends is:  BendReportManager.Mil98Report List[NXOp. The XYZ report information. .
         - totalLength is: float. Total length of the entire path of segments. .

        """
        pass
    def GenerateXyzReport(self, segmentInformation: List[BendReportManager.SegmentInformation]) -> Tuple[List[BendReportManager.XyzReport], float]:
        """
         Generates the bend report in XYZ format. 
         Returns A tuple consisting of (bends, totalLength). 
         - bends is:  BendReportManager.XyzReport List[NXOp. The XYZ report information. .
         - totalLength is: float. Total length of the entire path of segments. .

        """
        pass
    def GenerateYbcReport(self, segmentInformation: List[BendReportManager.SegmentInformation]) -> Tuple[List[BendReportManager.YbcReport], float]:
        """
         Generates the bend report in YBC format. 
         Returns A tuple consisting of (bends, totalLength). 
         - bends is:  BendReportManager.YbcReport List[NXOp. The XYZ report information. .
         - totalLength is: float. Total length of the entire path of segments. .

        """
        pass
    def GetNumberOfBends(self, segmentInformation: List[BendReportManager.SegmentInformation]) -> int:
        """
         Returns the number of bends in the segment information. 
         Returns nBends (int):  .
        """
        pass
    def GetSegmentInformation(self, stock: NXOpen.TaggedObject) -> List[BendReportManager.SegmentInformation]:
        """
         Builds up the segment information from the given ports, solid bodies, segments, stock, stock components, or features.
                    Call this first to get the segment information to end to the report methods.
                
         Returns segmentInformation ( BendReportManager.SegmentInformation List[NXOp):  Information on each segment. Send to one of the generate report methods to get a report. .
        """
        pass
    def ReverseDirection(self, segmentInformation: List[BendReportManager.SegmentInformation]) -> List[BendReportManager.SegmentInformation]:
        """
         Reverses the order of the segment information.
                    Since some of the information in the YBC and MIL98 reports are relative angles,
                    reversing the order of the segments can have a significant impact on the report.
                
         Returns reversedSegmentInformation ( BendReportManager.SegmentInformation List[NXOp):  The reversed segment order. .
        """
        pass
import NXOpen
class BranchPathNumberingBuilder(NXOpen.Builder): 
    """ Builder class for Branch Path Numbering. 
    """
    class Sequence(Enum):
        """
        Members Include: 
         |Numbers|  1, 2, 3, and so on 
         |UpperCase|  A, B, C, and so on 
         |LowerCase|  a, b, c, and so on 

        """
        Numbers: int
        UpperCase: int
        LowerCase: int
        @staticmethod
        def ValueOf(value: int) -> BranchPathNumberingBuilder.Sequence:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayOnSegments(self) -> bool:
        """
        Getter for property: (bool) DisplayOnSegments
         Returns  the toggle specified in the UI on whether to display the labels   
            
         
        """
        pass
    @DisplayOnSegments.setter
    def DisplayOnSegments(self, displayOnSegments: bool):
        """
        Setter for property: (bool) DisplayOnSegments
         Returns  the toggle specified in the UI on whether to display the labels   
            
         
        """
        pass
    @property
    def FirstBranchID(self) -> str:
        """
        Getter for property: (str) FirstBranchID
         Returns the formula specified in the UI to compute the first branch ID for the labeling sequence
                    in order to be valid, the formula must be blank OR contain the phrase "PARENT_BRANCH_ID" 
                  
            
         
        """
        pass
    @FirstBranchID.setter
    def FirstBranchID(self, firstBranchID: str):
        """
        Setter for property: (str) FirstBranchID
         Returns the formula specified in the UI to compute the first branch ID for the labeling sequence
                    in order to be valid, the formula must be blank OR contain the phrase "PARENT_BRANCH_ID" 
                  
            
         
        """
        pass
    @property
    def NextBranchID(self) -> str:
        """
        Getter for property: (str) NextBranchID
         Returns  the formula specified in the UI to compute the next branch ID for the labeling sequence
                     in order to be valid, the formula must be blank OR contain the phrase "PREVIOUS_BRANCH_ID" 
                  
            
         
        """
        pass
    @NextBranchID.setter
    def NextBranchID(self, nextBranchID: str):
        """
        Setter for property: (str) NextBranchID
         Returns  the formula specified in the UI to compute the next branch ID for the labeling sequence
                     in order to be valid, the formula must be blank OR contain the phrase "PREVIOUS_BRANCH_ID" 
                  
            
         
        """
        pass
    @property
    def Prefix(self) -> str:
        """
        Getter for property: (str) Prefix
         Returns the prefix specified in the UI for the labels   
            
         
        """
        pass
    @Prefix.setter
    def Prefix(self, prefix: str):
        """
        Setter for property: (str) Prefix
         Returns the prefix specified in the UI for the labels   
            
         
        """
        pass
    @property
    def ReassignOnSegments(self) -> bool:
        """
        Getter for property: (bool) ReassignOnSegments
         Returns the toggle specified in the UI on whether to reassign the labels    
            
         
        """
        pass
    @ReassignOnSegments.setter
    def ReassignOnSegments(self, reassignOnSegments: bool):
        """
        Setter for property: (bool) ReassignOnSegments
         Returns the toggle specified in the UI on whether to reassign the labels    
            
         
        """
        pass
    @property
    def SequenceMethod(self) -> BranchPathNumberingBuilder.Sequence:
        """
        Getter for property: ( BranchPathNumberingBuilder.Sequence NXOpen) SequenceMethod
         Returns the sequence method specified in the UI for the labels      
                    
                  
            
         
        """
        pass
    @SequenceMethod.setter
    def SequenceMethod(self, sequenceMethod: BranchPathNumberingBuilder.Sequence):
        """
        Setter for property: ( BranchPathNumberingBuilder.Sequence NXOpen) SequenceMethod
         Returns the sequence method specified in the UI for the labels      
                    
                  
            
         
        """
        pass
    @property
    def StartValueForLowerCase(self) -> str:
        """
        Getter for property: (str) StartValueForLowerCase
         Returns the start value for lower case alphabet.  
           The default value is "a" if the customer does not call this method    
         
        """
        pass
    @StartValueForLowerCase.setter
    def StartValueForLowerCase(self, startValueForLowerCase: str):
        """
        Setter for property: (str) StartValueForLowerCase
         Returns the start value for lower case alphabet.  
           The default value is "a" if the customer does not call this method    
         
        """
        pass
    @property
    def StartValueForNumbers(self) -> str:
        """
        Getter for property: (str) StartValueForNumbers
         Returns the start value for numbers.  
           The default value is "1" if the customer does not call this method    
         
        """
        pass
    @StartValueForNumbers.setter
    def StartValueForNumbers(self, startValueForNumbers: str):
        """
        Setter for property: (str) StartValueForNumbers
         Returns the start value for numbers.  
           The default value is "1" if the customer does not call this method    
         
        """
        pass
    @property
    def StartValueForUpperCase(self) -> str:
        """
        Getter for property: (str) StartValueForUpperCase
         Returns the start value for upper case alphabet.  
           The default value is "A" if the customer does not call this method    
         
        """
        pass
    @StartValueForUpperCase.setter
    def StartValueForUpperCase(self, startValueForUpperCase: str):
        """
        Setter for property: (str) StartValueForUpperCase
         Returns the start value for upper case alphabet.  
           The default value is "A" if the customer does not call this method    
         
        """
        pass
    @property
    def Suffix(self) -> str:
        """
        Getter for property: (str) Suffix
         Returns the suffix specified in the UI for the labels    
            
         
        """
        pass
    @Suffix.setter
    def Suffix(self, suffix: str):
        """
        Setter for property: (str) Suffix
         Returns the suffix specified in the UI for the labels    
            
         
        """
        pass
    def SetControlPoint(self, controlPoint: ControlPoint) -> None:
        """
         Set the control point for the start of the labeling sequence 
        """
        pass
    def SetControlPointFromSegment(self, controlPoint: ISegment) -> None:
        """
         Set the control point for the start of the labeling sequence 
        """
        pass
import NXOpen
class BuiltInPathBuilder(NXOpen.Builder): 
    """ Builder for creatingediting the Built-in Paths. """
    @property
    def Selectedpath(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Selectedpath
         Returns the selected path   
            
         
        """
        pass
import NXOpen
class BuiltInPathCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.BuiltInPath objects. """
    def CreateBuiltInPath(self, curves: List[NXOpen.Curve]) -> BuiltInPath:
        """
         Creates a NXOpen.Routing.BuiltInPath object. 
         Returns built_in_path ( BuiltInPath NXOpen):  .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class BuiltInPath(NXOpen.NXObject): 
    """ 
        The Routing BuiltInPath object stores a set of curves.  Routing will attempt to create
        segments on top of these curves whenever an instance of the part containing the 
        BuiltInPath is added to the assembly.   
     """
    def CreateSegments(self, part_occ: NXOpen.Assemblies.Component) -> List[NXOpen.Curve]:
        """
         Creates the segments in the work part to cover any curves referenced by the
                    Routing.BuiltInPath object in the component part file. 
                    
                      Finds the segments currently extracted from the part occurrence and
                      creates a new segment overy every Routing.BuiltInPath curve occurrence that doesn't
                      already have a segment.
                     
         Returns segments ( NXOpen.Curve Li):  the array of Segments referenced by the BuiltInPath includes 
                                                    previously created segments as well. .
        """
        pass
    def GetCurves(self) -> List[NXOpen.Curve]:
        """
         Returns the array of curves referenced by the Built-In-Path object.  These curves
                 are in the same part as the Built-In-Path object, and are the curves extracted into the
                 Work Part for the Routing.BuiltInPath.CreateSegments method. 
         Returns curves ( NXOpen.Curve Li):  the array of Curves referenced by the Built-In-Path .
        """
        pass
    def SetCurves(self, curves: List[NXOpen.Curve]) -> None:
        """
         Sets the array of curves referenced by the Built-In-Path object.  These curves
                 are in the same part as the Built-In-Path object, and are the curves extracted into the
                 Work Part for the Routing.BuiltInPath.CreateSegments method. 
        """
        pass
import NXOpen
class BulkReplacementBuilder(NXOpen.Builder): 
    """ Builder class for Bulk Replacement which manages replacement operations on Routing objects """
    @property
    def ReferenceObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ReferenceObject
         Returns the reference object used to extract characteristics for Bulk Replacement   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteObjectCollector
         Returns the Routing object collector   
            
         
        """
        pass
    def ClearAttributeForAllObjects(self, attributeIdType: RoutingAttributeIdentifierType, attributeId: str) -> None:
        """
         The attribute value clear method for all objects 
        """
        pass
    def ClearAttributeForObject(self, objectTag: NXOpen.NXObject, attributeIdType: RoutingAttributeIdentifierType, attributeId: str) -> None:
        """
         The object attribute value clear method 
        """
        pass
    def CopySearchResultsToObject(self, fromObjectTag: NXOpen.NXObject, toObjectTag: NXOpen.NXObject) -> None:
        """
         The method that copies the search results from one object to another 
        """
        pass
    def GetAttributeForObject(self, objectTag: NXOpen.NXObject, attributeIdType: RoutingAttributeIdentifierType, attributeId: str) -> str:
        """
         The object attribute value method getter 
         Returns value (str):  The value of the attribute .
        """
        pass
    def GetPartLayer(self) -> int:
        """
         The method that gets the layer used for newly replaced objects 
         Returns layer (int):  The number of the layer .
        """
        pass
    def GetPartLibraryValuesForAttributeForObject(self, objectTag: NXOpen.NXObject, attributeIdType: RoutingAttributeIdentifierType, attributeId: str) -> List[str]:
        """
         The method gets the part library values for a given attribute for the specified object 
         Returns values (List[str]):  The values retrieved from all the part library for the attribute .
        """
        pass
    def GetPartReferenceSet(self) -> str:
        """
         The method that gets the reference set used for newly replaced objects 
         Returns referenceSetName (str):  The name of the reference set .
        """
        pass
    def GetReplacementMethodForObject(self, objectTag: NXOpen.NXObject) -> RoutingBulkReplacementBuilderReplacementMethodType:
        """
         The replacement method getter 
         Returns method ( RoutingBulkReplacementBuilderReplacementMethodType NXOpen):  The replacement method currently set for this object .
        """
        pass
    def GetReplacementObjectIdentifierForObject(self, objectTag: NXOpen.NXObject) -> str:
        """
         The replacement object identifier getter 
         Returns objectIdentifier (str):  The object identifier for which is currently set as the replacement object .
        """
        pass
    def GetReplacementObjectIdentifiersFromSearchResultsForObject(self, objectTag: NXOpen.NXObject) -> List[str]:
        """
         The possible replacement object identifiers method getter 
         Returns objectIdentifiers (List[str]):  array of object identifiers which are possible replacement objects .
        """
        pass
    def GetRetainReasonForObject(self, objectTag: NXOpen.NXObject) -> RoutingBulkReplacementBuilderRetainReasonType:
        """
         The retain reason getter 
         Returns reason ( RoutingBulkReplacementBuilderRetainReasonType NXOpen):  The retain reason currently set for this object .
        """
        pass
    def GetSelectedObjectValuesForAttribute(self, attributeIdType: RoutingAttributeIdentifierType, attributeId: str) -> List[str]:
        """
         The method that retrieves all the values for a given attribute from all the objects 
         Returns values (List[str]):  The values retrieved from all the objects for the attribute .
        """
        pass
    def GetValueForAttributeFromReferenceObject(self, attributeIdType: RoutingAttributeIdentifierType, attributeId: str) -> str:
        """
         The method that returns the value of an attribute from the reference object 
         Returns value (str):  The value of the attribute from the reference object .
        """
        pass
    def SearchForReplacementForObject(self, objectTag: NXOpen.NXObject) -> None:
        """
         The method that initiates a search for the replacement object 
        """
        pass
    def SearchForReplacementForObjectOnAttributes(self, objectTag: NXOpen.NXObject, attributeIdTypes: List[RoutingAttributeIdentifierType], attributeIds: List[str]) -> None:
        """
         The method that initiates a search for the replacement object using on the passed in attributes as criteria 
        """
        pass
    def SetAttributeForAllObjects(self, attributeIdType: RoutingAttributeIdentifierType, attributeId: str, value: str) -> None:
        """
         The attribute value setter for all objects 
        """
        pass
    def SetAttributeForObject(self, objectTag: NXOpen.NXObject, attributeIdType: RoutingAttributeIdentifierType, attributeId: str, value: str) -> None:
        """
         The object attribute value method setter 
        """
        pass
    def SetAttributeValueForObjectFromReferenceObject(self, objectTag: NXOpen.NXObject, attributeIdType: RoutingAttributeIdentifierType, attributeId: str) -> None:
        """
         The method that sets the attribute value from the reference object on the specified object 
        """
        pass
    def SetPartLayer(self, layer: int) -> None:
        """
         The method that sets the layer used for newly replaced objects 
        """
        pass
    def SetPartReferenceSet(self, referenceSetName: str) -> None:
        """
         The method that sets the reference set used for newly replaced objects 
        """
        pass
    def SetReplacementClassificationObjectForObject(self, objectTag: NXOpen.NXObject, classificationClassId: str, classificationInstanceId: str) -> None:
        """
         The replacement object method setter 
        """
        pass
    def SetReplacementMethodForAllObjects(self, method: RoutingBulkReplacementBuilderReplacementMethodType) -> None:
        """
         The replacement method setter for all objects 
        """
        pass
    def SetReplacementMethodForObject(self, objectTag: NXOpen.NXObject, method: RoutingBulkReplacementBuilderReplacementMethodType) -> None:
        """
         The replacement method setter 
        """
        pass
    def SetReplacementObjectIdentifierForObject(self, objectTag: NXOpen.NXObject, objectIdentifier: str) -> None:
        """
         The replacement object identifier method setter 
        """
        pass
    def SetReplacementObjectPartNumberForObject(self, objectTag: NXOpen.NXObject, partNumber: str) -> None:
        """
         The replacement object part number method setter 
        """
        pass
    def SetReplacementPartSpecificationForObject(self, objectTag: NXOpen.NXObject, partSpecification: str) -> None:
        """
         The replacement part specification method setter 
        """
        pass
    def SetSequenceOfObjectReplacement(self, objects: List[NXOpen.NXObject]) -> None:
        """
         The method that sets the sequence of object replacement 
        """
        pass
import NXOpen
class CablewayNetwork(NXOpen.NXObject): 
    """ The Routing CablewayNetwork object stores a set of curves. """
    def GetCurveEndPoints(self) -> List[NXOpen.Point]:
        """
         Returns the array of points automatically created at the ends of the curves
                    when qualifying a Cableway Network. 
         Returns points ( NXOpen.Point Li):  the array of automatically created points. .
        """
        pass
    def GetCurves(self) -> List[NXOpen.Curve]:
        """
         Returns the array of curves referenced by the Cableway Network object.  These curves
                 are in the same part as the Cableway Network object. 
         Returns curves ( NXOpen.Curve Li):  the array of Curves referenced by the Cableway Network .
        """
        pass
    def SetCurves(self, curves: List[NXOpen.Curve]) -> None:
        """
         Sets the array of curves referenced by the Cableway Network object.  These curves
                 are in the same part as the Cableway Network object. 
        """
        pass
import NXOpen
class CharacteristicList(NXOpen.TransientObject): 
    """
         Contains a list of characteristics.
         A characteristics is a name-value pair where the value can be an integer, real or string.

    """
    class CharacteristicInformation:
        """
         Contains the type and name of a characteristic 
         CharacteristicListCharacteristicInformation_Struct NXOpen is an alias for  CharacteristicList.CharacteristicInformation NXOpen.
        """
        @property
        def Type(self) -> NXOpen.NXObject.AttributeType:
            """
            Getter for property Type
            characteristic type

            """
            pass
        @Type.setter
        def Type(self, value: NXOpen.NXObject.AttributeType):
            """
            Getter for property Type
            characteristic type
            Setter for property Type
            characteristic type

            """
            pass
        @property
        def Name(self) -> str:
            """
            Getter for property Name
            characteristic name

            """
            pass
        @Name.setter
        def Name(self, value: str):
            """
            Getter for property Name
            characteristic name
            Setter for property Name
            characteristic name

            """
            pass
    def DeleteCharacteristic(self, name: str, type: NXOpen.NXObject.AttributeType) -> None:
        """
         Removes a characteristic from the characteristic list.  
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object. 
        """
        pass
    def GetCharacteristicTitlesByType(self, type: NXOpen.NXObject.AttributeType) -> List[CharacteristicList.CharacteristicInformation]:
        """
         Returns the titles of all characteristics that have the specified type. 
         Returns titles ( CharacteristicList.CharacteristicInformation List[NXOp):  The list of characteristic names. .
        """
        pass
    def GetIntegerCharacteristic(self, name: str) -> int:
        """
         Gets the value of an integer characteristic. 
         Returns value (int):  The integer value of the characteristic. .
        """
        pass
    def GetRealCharacteristic(self, name: str) -> float:
        """
         Gets the value of a real characteristic. 
         Returns value (float):  The real value of the characteristic .
        """
        pass
    def GetStringCharacteristic(self, name: str) -> str:
        """
         Gets the value of a string characteristic 
         Returns value (str):  The string value of the characteristic .
        """
        pass
    @overload
    def SetCharacteristic(self, name: str, value: int) -> None:
        """
         Sets the value of an integer characteristic associated with the input name.
                    The method adds a new characteristic to the list if one does not exist already or converts
                    the type of an existing characteristic to integer if necessary. 
        """
        pass
    @overload
    def SetCharacteristic(self, name: str, value: float) -> None:
        """
         Sets the value of an real characteristic associated with the input name.
                    The method adds a new characteristic to the list if one doesn't exist already or converts
                    the type of an existing characteristic to real if necessary. 
        """
        pass
    @overload
    def SetCharacteristic(self, name: str, value: str) -> None:
        """
         Sets the value of an string characteristic.
                    The method adds a new characteristic to the list if one does not exist already or converts
                    the type of an existing characteristic to string if necessary. 
        """
        pass
    @overload
    def SetCharacteristic(self, name: str, value: str, type: NXOpen.NXObject.AttributeType) -> None:
        """
         Sets the value of a string or reference characteristic.
                    The method adds a new characteristic to the list if one does not exist already or converts
                    the type of an existing characteristic to string or reference if necessary. 
        """
        pass
import NXOpen
class ChoosePartPluginData(NXOpen.TaggedObject): 
    """ Data object created by Routing for use by the Choose Part plugin called by the Place Part command.
        Routing sends this object to any registered Choose Part plugin.

        It is the Choose Part plugin's responsibility to prompt the user to choose a part and then
        fill in the information about the part by calling the methods on this object.

        For more information, see Routing.CustomManager and the
        Routing.CustomManager.SetChoosePartPlugin
    """
    def SetCharacteristics(self, characteristics: CharacteristicList) -> None:
        """
         Sets the characteristics of the part choosen by the user. 
        """
        pass
    def SetMemberName(self, memberName: str) -> None:
        """
         Sets the Member Name of the part choosen by the user.
                    The unique name of each member in a part family. Routing uses Part Name and Member Name
                    together to find the correct .prt file or Teamcenter Item ID in a part family.
                
        """
        pass
    def SetPartName(self, partName: str) -> None:
        """
         Sets the Part Name of the part choosen by the user.
                    The Part Name is the key Routing uses to find the .prt file in native mode on disk or
                    to find the proper item ID in Teamcenter. The Part Name must exactly match the .prt
                    file name or the Item ID in order for Routing to place the part.
                
        """
        pass
    def SetPartNumber(self, partNumber: str) -> None:
        """
         Sets the Part Number of the part choosen by the user.
                    The Part Number is an attribute that Routing displays in the Reuse Library.
                    Part Number does not have to match the .prt file name or the Item ID in Teamcenter,
                    but it often does. Part Name and Part Number are often the same.
                
        """
        pass
import NXOpen
class ClockPartBuilder(NXOpen.Builder): 
    """ Builder class for clock part object """
    @property
    def PortSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) PortSelection
         Returns the user selected  NXOpen::Routing::Port   for rotation of compoent   
            
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle applied to the component for rotation   
            
         
        """
        pass
    def DragByTransform(self, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
         Drag the selected objects by the given translation and rotation.  Only
                    call after invoking the Routing.ClockPartBuilder.StartDrag
                    method.  After finished dragging, call 
                    Routing.ClockPartBuilder.StopDrag.
        """
        pass
    def InitializeFromPort(self, port: Port) -> None:
        """
         Initializes (or resets) the builder based off of the input line segment.  
        """
        pass
    def SetLockEngagement(self, lockEngagement: bool) -> None:
        """
        Set EngagementLock of builder attribute
        """
        pass
    def SetLockRotation(self, lockRotation: bool) -> None:
        """
        Set RotationLock of builder attribute
        """
        pass
    def StartDrag(self) -> None:
        """
         Begin a drag operation.  
        """
        pass
    def StopDrag(self) -> None:
        """
         End a drag operation.  
        """
        pass
    def SuppressPortConstraint(self, portTag: Port, suppress: bool) -> None:
        """
         Suppress the constraind applied to the selected  NXOpen.Routing.Port  
        """
        pass
    def UpdateRotationAngle(self, angle: float) -> None:
        """
         Suppress the constraind applied to the selected  NXOpen.Routing.Port  
        """
        pass
import NXOpen
class CompareRunsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.CompareRunsBuilder, used to compare runs in the work 
        part to the ones in another part, or to runs defined in xml files gathered in a folder 
        (native mode) or on an item revision (managed mode).
    """
    class CompareTypes(Enum):
        """
        Members Include: 
         |Xml| 
         |Part| 

        """
        Xml: int
        Part: int
        @staticmethod
        def ValueOf(value: int) -> CompareRunsBuilder.CompareTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CompareTypesEnum(self) -> CompareRunsBuilder.CompareTypes:
        """
        Getter for property: ( CompareRunsBuilder.CompareTypes NXOpen) CompareTypesEnum
         Returns the Compare type: part or xml   
            
         
        """
        pass
    @CompareTypesEnum.setter
    def CompareTypesEnum(self, compareTypesEnum: CompareRunsBuilder.CompareTypes):
        """
        Setter for property: ( CompareRunsBuilder.CompareTypes NXOpen) CompareTypesEnum
         Returns the Compare type: part or xml   
            
         
        """
        pass
    @property
    def FilterString(self) -> str:
        """
        Getter for property: (str) FilterString
         Returns the filter used to limit which runs are compared among those in the folder or on the item revision   
            
         
        """
        pass
    @FilterString.setter
    def FilterString(self, filterString: str):
        """
        Setter for property: (str) FilterString
         Returns the filter used to limit which runs are compared among those in the folder or on the item revision   
            
         
        """
        pass
    @property
    def InputPathString(self) -> str:
        """
        Getter for property: (str) InputPathString
         Returns the full path input to the compare runs algorithm.  
            Can be a folder or an item revision for xml comparisons, or a part.  
         
        """
        pass
    @InputPathString.setter
    def InputPathString(self, filename: str):
        """
        Setter for property: (str) InputPathString
         Returns the full path input to the compare runs algorithm.  
            Can be a folder or an item revision for xml comparisons, or a part.  
         
        """
        pass
    @property
    def ReportDiscrepancies(self) -> bool:
        """
        Getter for property: (bool) ReportDiscrepancies
         Returns the option to report discrepancies down to attribute level.  
             
         
        """
        pass
    @ReportDiscrepancies.setter
    def ReportDiscrepancies(self, reportDiscrepancies: bool):
        """
        Setter for property: (bool) ReportDiscrepancies
         Returns the option to report discrepancies down to attribute level.  
             
         
        """
        pass
import NXOpen
class ComponentNamePluginData(NamePluginData): 
    """ Data object created by Routing just before creating stock or cut elbow components.
        Routing expects the plugin you write to fill in the required information for the
        component name.

        For more information, see Routing.CustomManager and the
        Routing.CustomManager.SetStockComponentNamePlugin or
        Routing.CustomManager.SetCutElbowComponentNamePlugin.
    """
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the name Routing will use for the component in the NX assembly.  
             
         
        """
        pass
    @ComponentName.setter
    def ComponentName(self, componentName: str):
        """
        Setter for property: (str) ComponentName
         Returns the name Routing will use for the component in the NX assembly.  
             
         
        """
        pass
    @property
    def RenameComponentPartFlag(self) -> bool:
        """
        Getter for property: (bool) RenameComponentPartFlag
         Returns the flag that tells Routing to use the information in this data object to
                    rename the stock's or cut elbow's part.  
             
         
        """
        pass
    @RenameComponentPartFlag.setter
    def RenameComponentPartFlag(self, shouldRenamePart: bool):
        """
        Setter for property: (bool) RenameComponentPartFlag
         Returns the flag that tells Routing to use the information in this data object to
                    rename the stock's or cut elbow's part.  
             
         
        """
        pass
    @property
    def TemplateObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) TemplateObject
         Returns the stock or the elbow's template part for which Routing needs to create a new component.  
             
         
        """
        pass
class ComponentName(Enum):
    """
    Members Include: 
     |Temporary|  Component name is temporary, it has not been renamed. 
     |Permanent|  Component has been renamed by the user. 

    """
    Temporary: int
    Permanent: int
    @staticmethod
    def ValueOf(value: int) -> ComponentName:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ConnectedCurvesBuilder(NXOpen.Builder): 
    """ Builder for creating automatically creating segments on end-to-end connected
        curves. """
    @property
    def AllowArcs(self) -> bool:
        """
        Getter for property: (bool) AllowArcs
         Returns the flag that allows traversal of arcs when finding connected
                    curves.  
           If False, the traversal will stop when it hits an arc curve.  In addition
                    the curve selection list will not allow arcs to be added to the list.
                      
         
        """
        pass
    @AllowArcs.setter
    def AllowArcs(self, allowArcs: bool):
        """
        Setter for property: (bool) AllowArcs
         Returns the flag that allows traversal of arcs when finding connected
                    curves.  
           If False, the traversal will stop when it hits an arc curve.  In addition
                    the curve selection list will not allow arcs to be added to the list.
                      
         
        """
        pass
    @property
    def AllowLines(self) -> bool:
        """
        Getter for property: (bool) AllowLines
         Returns the flag that allows traversal of lines when finding connected
                    curves.  
           If False, the traversal will stop when it hits a line curve.  In addition
                    the curve selection list will not allow lines to be added to the list.
                      
         
        """
        pass
    @AllowLines.setter
    def AllowLines(self, allowLines: bool):
        """
        Setter for property: (bool) AllowLines
         Returns the flag that allows traversal of lines when finding connected
                    curves.  
           If False, the traversal will stop when it hits a line curve.  In addition
                    the curve selection list will not allow lines to be added to the list.
                      
         
        """
        pass
    @property
    def AllowOccs(self) -> bool:
        """
        Getter for property: (bool) AllowOccs
         Returns the flag that allows traversal of curve occurrences when finding connected
                    curves.  
           If False, the traversal will stop when it hits a curve occurrence.  In 
                    addition the curve selection list will not allow curve occurrences to be added 
                    to the list.
                      
         
        """
        pass
    @AllowOccs.setter
    def AllowOccs(self, allowOccs: bool):
        """
        Setter for property: (bool) AllowOccs
         Returns the flag that allows traversal of curve occurrences when finding connected
                    curves.  
           If False, the traversal will stop when it hits a curve occurrence.  In 
                    addition the curve selection list will not allow curve occurrences to be added 
                    to the list.
                      
         
        """
        pass
    @property
    def AllowSplines(self) -> bool:
        """
        Getter for property: (bool) AllowSplines
         Returns the flag that allows traversal of splines when finding connected
                    curves.  
           If False, the traversal will stop when it hits an spline curve.  In addition
                    the curve selection list will not allow splines to be added to the list.
                      
         
        """
        pass
    @AllowSplines.setter
    def AllowSplines(self, allowSplines: bool):
        """
        Setter for property: (bool) AllowSplines
         Returns the flag that allows traversal of splines when finding connected
                    curves.  
           If False, the traversal will stop when it hits an spline curve.  In addition
                    the curve selection list will not allow splines to be added to the list.
                      
         
        """
        pass
    @property
    def CurveSelection(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: ( NXOpen.SelectCurveList) CurveSelection
         Returns the list of selected curves.  
             
         
        """
        pass
    def ChainSelectedCurves(self) -> List[NXOpen.Curve]:
        """
         Finds all curves attached end-to-end with the current list of selected
                    curves.  The returned list of curves includes the selected curves. 
         Returns curves ( NXOpen.Curve Li):  .
        """
        pass
class ConnectivityDefinition(RouteObject): 
    """ 
        
        The base class for various connection objects.
        
        
        Reference subclasses for more information.  
        See NX Open Routing help for detailed information on the Connection data model.
        This is an abstract class.
        
    """
    @property
    def ImplementedBy(self) -> RouteObject:
        """
        Getter for property: ( RouteObject NXOpen) ImplementedBy
         Returns the  NXOpen::Routing::RouteObject  implementing a connection.  
            Is typically a  NXOpen::Routing::Electrical::WireDevice ,  NXOpen::Routing::Electrical::CableDevice ,
                     NXOpen::Routing::Electrical::ShieldDevice 
                  
         
        """
        pass
import NXOpen
class ConnectPathBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.ConnectPathBuilder. 
        Routing.ConnectPathBuilderis used to control the connecting of 
        Routing.ControlPoints within the distance tolerance specified.
        This eliminates duplicate Routing.ControlPoints such that only one 
        Routing.ControlPoint remains.  The Routing.Segments that were defined 
        by the duplicate Routing.ControlPoints are now defined by the remaining 
        Routing.ControlPoint.  Routing.ConnectPath is the reverse operation to 
        Routing.DiscontinuityCorner. """
    @property
    def Selection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Selection
         Returns the Routing.  
          ControlPoints that are selected.   
         
        """
        pass
    @property
    def Tolerance(self) -> float:
        """
        Getter for property: (float) Tolerance
         Returns the 3D distance within which Routing.  
          ControlPoints will be considered duplicates 
                    and some will be merged away so that only one Routing.ControlPoint remains.   
         
        """
        pass
    @Tolerance.setter
    def Tolerance(self, tolerance: float):
        """
        Setter for property: (float) Tolerance
         Returns the 3D distance within which Routing.  
          ControlPoints will be considered duplicates 
                    and some will be merged away so that only one Routing.ControlPoint remains.   
         
        """
        pass
import NXOpen
class ControlPointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.ControlPoint objects. 

    Iterating this collection only returns live uncondemned objects contained in the owning part
    of the collection. Note that NXOpen.Routing.ControlPoint is a smart object and many smart objects are condemned as they 
    only exist to support other objects and are not displayed."""
    class CheckExisting(Enum):
        """
        Members Include: 
         |DontSearch|  Don't search for an exising object, 
                                                                    always create a new object. 
         |Search|  Search for an existing object, don't 
                                                                    create a new object if one exists at the 
                                                                    correct location. 

        """
        DontSearch: int
        Search: int
        @staticmethod
        def ValueOf(value: int) -> ControlPointCollection.CheckExisting:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FoundExisting(Enum):
        """
        Members Include: 
         |BrandNew|  Object is a new object. 
         |Existing|  Object existed already. 

        """
        BrandNew: int
        Existing: int
        @staticmethod
        def ValueOf(value: int) -> ControlPointCollection.FoundExisting:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @overload
    def CreateControlPoint(self, position: NXOpen.Point3d, check_existing: ControlPointCollection.CheckExisting) -> Tuple[ControlPoint, ControlPointCollection.FoundExisting]:
        """
         Creates a dumb NXOpen.Routing.ControlPoint object.  The NXOpen.Routing.ControlPoint's 
                    position is not associative to any other object.  
         Returns A tuple consisting of (controlpoint, found_existing). 
         - controlpoint is:  ControlPoint NXOpen. .
         - found_existing is:  ControlPointCollection.FoundExisting NXOpen. Returned NXOpen.Routing.ControlPoint is
                                                                an existing control point. .

        """
        pass
    @overload
    def CreateControlPoint(self, port: Port, check_existing: ControlPointCollection.CheckExisting) -> Tuple[ControlPoint, ControlPointCollection.FoundExisting]:
        """
         Creates a smart NXOpen.Routing.ControlPoint object.  The NXOpen.Routing.ControlPoint's 
                    position is associative to the input NXOpen.Routing.Port.  
         Returns A tuple consisting of (controlpoint, found_existing). 
         - controlpoint is:  ControlPoint NXOpen. .
         - found_existing is:  ControlPointCollection.FoundExisting NXOpen. Returned NXOpen.Routing.ControlPoint is
                                                                an existing control point. .

        """
        pass
    @overload
    def CreateControlPoint(self, objectValue: NXOpen.TaggedObject, object_parm: float, check_existing: ControlPointCollection.CheckExisting) -> Tuple[ControlPoint, ControlPointCollection.FoundExisting]:
        """
         Creates a NXOpen.Routing.ControlPoint at the given object and normalized parameter.
                    Supports curves [includes segments], ports and circular edges.  
         Returns A tuple consisting of (controlpoint, found_existing). 
         - controlpoint is:  ControlPoint NXOpen. .
         - found_existing is:  ControlPointCollection.FoundExisting NXOpen. Returned NXOpen.Routing.ControlPoint is
                                                                an existing control point. .

        """
        pass
    @overload
    def CreateControlPoint(self, point: NXOpen.Point, check_existing: ControlPointCollection.CheckExisting) -> Tuple[ControlPoint, ControlPointCollection.FoundExisting]:
        """
         Creates a smart NXOpen.Routing.ControlPoint object.  The NXOpen.Routing.ControlPoint's 
                    position is associative to the input NXOpen.Point.  
         Returns A tuple consisting of (controlpoint, found_existing). 
         - controlpoint is:  ControlPoint NXOpen. .
         - found_existing is:  ControlPointCollection.FoundExisting NXOpen. Returned NXOpen.Routing.ControlPoint is
                                                                an existing control point. .

        """
        pass
    @overload
    def CreateControlPoint(self, conic: NXOpen.IBaseCurve, check_existing: ControlPointCollection.CheckExisting) -> Tuple[ControlPoint, ControlPointCollection.FoundExisting]:
        """
         Creates a smart NXOpen.Routing.ControlPoint object.  The NXOpen.Routing.ControlPoint's 
                    position is associative to a NXOpen.Point that is defined at the center
                    of a NXOpen.IBaseCurve object.  
         Returns A tuple consisting of (controlpoint, found_existing). 
         - controlpoint is:  ControlPoint NXOpen. .
         - found_existing is:  ControlPointCollection.FoundExisting NXOpen. Returned NXOpen.Routing.ControlPoint is
                                                                an existing control point. .

        """
        pass
    @overload
    def CreateControlPoint(self, start_object: IRoutePosition, offset: NXOpen.Vector3d, check_existing: ControlPointCollection.CheckExisting) -> Tuple[ControlPoint, ControlPointCollection.FoundExisting]:
        """
         Creates a dumb NXOpen.Routing.ControlPoint object.  The NXOpen.Routing.ControlPoint's 
                    position is not associative to any other object.  The position of the object is located at
                    the XC, YC, ZC offset (using the work coordinate system) from the input 
                    NXOpen.Routing.IRoutePosition  object.  
         Returns A tuple consisting of (controlpoint, found_existing). 
         - controlpoint is:  ControlPoint NXOpen. .
         - found_existing is:  ControlPointCollection.FoundExisting NXOpen. Returned NXOpen.Routing.ControlPoint is
                                                                an existing control point. .

        """
        pass
    @overload
    def CreateControlPoint(self, cp_occ: ControlPoint, check_existing: ControlPointCollection.CheckExisting) -> Tuple[ControlPoint, ControlPointCollection.FoundExisting]:
        """
         Creates a smart NXOpen.Routing.ControlPoint object.  The NXOpen.Routing.ControlPoint's 
                    position is smart point that is associative to a NXOpen.Point that is associative
                    to a NXOpen.Routing.ControlPoint occurrence. 
         Returns A tuple consisting of (controlpoint, found_existing). 
         - controlpoint is:  ControlPoint NXOpen. .
         - found_existing is:  ControlPointCollection.FoundExisting NXOpen. Returned NXOpen.Routing.ControlPoint is
                                                                an existing control point. .

        """
        pass
    def FindControlPoint(self, position: NXOpen.Point3d, tolerance: float) -> ControlPoint:
        """
         Finds an existing NXOpen.Routing.ControlPoint at the given ABS coordinates within
                    the given tolerance. 
         Returns controlpoint ( ControlPoint NXOpen):  .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Positioning
class ControlPoint(NXOpen.SmartObject): 
    """ 
        Routing Control Points define a position in space, and are used to determine connections
        from segments to segments, and segments to ports.
    """
    class DefinedStatus(Enum):
        """
        Members Include: 
         |System|  Created automatically by the application. 
         |User|  Created by the user. 

        """
        System: int
        User: int
        @staticmethod
        def ValueOf(value: int) -> ControlPoint.DefinedStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Guid(self) -> str:
        """
        Getter for property: (str) Guid
         Returns the Globally Unique Identifier (GUID) for this control point.  
             
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @property
    def Position(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
    @Position.setter
    def Position(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
    def AssignDefaultElbow(self) -> NXOpen.Assemblies.Component:
        """
         Places the default elbow at this object.  
                 
                    Finds the default elbow by searching through the default elbow part
                    table (see NXOpen.Preferences.RoutingPart using the destination
                    characteristics assigned to the stock on this object.
                 
                    Uses the ALLOW_DEFAULT_ELBOW_PLACEMENT plugin to determine if an elbow can be 
                    placed at this object.
                
         Returns placed_elbow ( NXOpen.Assemblies.Component):  the placed elbow component,  if
                                                        placement fails. .
        """
        pass
    def FindConnectedControlPoints(self) -> List[ControlPoint]:
        """
         Returns all the control points from different stock components that are connected to the given control point. 
         Returns equivalentControlPoints ( ControlPoint List[NXOp):  The equivalent control points from other stock components. .
        """
        pass
    def GenerateNewGuid(self) -> None:
        """
         Generates a new Globally Unique Identifier (GUID) on this segment. 
        """
        pass
    def GetDefiningObject(self) -> NXOpen.NXObject:
        """
         Returns defining object for this NXOpen.Routing.ControlPoint. 
         Returns object ( NXOpen.NXObject):  Object defining control point. .
        """
        pass
    def GetIsUserDefined(self) -> ControlPoint.DefinedStatus:
        """
         Returns whether this object is defined by a user or 
                    automatically by the Routing Application. 
         Returns user_defined ( ControlPoint.DefinedStatus NXOpen):  .
        """
        pass
    def GetRcpSegments(self) -> List[ISegment]:
        """
         Returns all segments whose start or end Control Point is this Control Point. 
         Returns segments ( ISegment List[NXOp):  .
        """
        pass
    def IsLockedToObject(self, objectValue: NXOpen.NXObject) -> bool:
        """
          Returns whether or not a touch constraint exists between the 
                     control point and the input object.  
                     This control point must not be an occurrence, the input object may
                     be an occurrence.
                 
         Returns is_locked (bool):  Whether or not the 
                                                                    control point is 
                                                                    constrained to the object. .
        """
        pass
    def LockToObject(self, objectValue: NXOpen.NXObject) -> NXOpen.Positioning.Constraint:
        """
         Ensures that a touch constraint exists between this 
                    control point and the input object.  Creates a constraint if one 
                    doesn't exist already.
                    This control point must not be an occurrence, the input object may
                    be an occurrence.
                    See NXOpen.Positioning.Constraint for a description of 
                    touch constraints.
                    Do not attempt to lock control points to NXOpen.Routing.ISegment
                    or NXOpen.Routing.Stock objects, this will result in 
                    unpredictable behavior.
                
         Returns constraint ( NXOpen.Positioning.Constraint):  The new or existing touch constraint. .
        """
        pass
    def RemoveCorner(self) -> None:
        """
         Remove the assigned corner. 
        """
        pass
    def UnlockFromObject(self, objectValue: NXOpen.NXObject) -> None:
        """
          Removes the touch constraint that exists between the 
                     control point and the input object.  This control point must not be 
                     an occurrence, the input object may be an occurrence.
                     Call NXOpen.Update.DoUpdate afterward to ensure that
                     the constraint is fully deleted.
                 
        """
        pass
class ConvertEccentricLinearToLinear(Enum):
    """
    Members Include: 
     |NotConverted|  Is not converted Eccentric linear to linear 
     |Converted|  Is converted Eccentric linear to linear 

    """
    NotConverted: int
    Converted: int
    @staticmethod
    def ValueOf(value: int) -> ConvertEccentricLinearToLinear:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class ConvertLinearToEccentricLinear(Enum):
    """
    Members Include: 
     |NotConverted|  Is not converted linear to Eccentric linear 
     |Converted|  Is converted linear to Eccentric linear 

    """
    NotConverted: int
    Converted: int
    @staticmethod
    def ValueOf(value: int) -> ConvertLinearToEccentricLinear:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CopeCornerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.CopeCorner objects. """
    def AssignCopeCorner(self, rcp: ControlPoint, cope_stocks: List[Stock]) -> CopeCorner:
        """
         Assigns a cope corner to the given control point.  The input stocks must
                    cover segments that are attached at the input control point.  There
                    must be at least two input stocks. 
         Returns new_crn ( CopeCorner NXOpen):  The newly created Cope Corner .
        """
        pass
import NXOpen.Features
class CopeCorner(Corner): 
    """ 
        The cope corner is a corner that trims stocks at a junction.  Each stock in the cope 
        trims in successive order to all of the previous stocks.  The first stock in the
        cope is not trimmed. 
     """
    def GetCopeStocks(self) -> List[Stock]:
        """
         Returns the ordered list of stocks coped at this corner. 
         Returns cope_stocks ( Stock List[NXOp):  .
        """
        pass
    def GetFeatures(self) -> List[NXOpen.Features.Feature]:
        """
         Returns the list of ROUTE_COPE features created to trim stocks. 
         Returns features ( NXOpen.Features.Feature Li):  .
        """
        pass
    def GetStockCopeFeature(self, stock: Stock) -> NXOpen.Features.Feature:
        """
         Get ROUTE_COPE feature applied the given stock at the cope corner 
         Returns feature ( NXOpen.Features.Feature):  Cope feature at the given stock. .
        """
        pass
    def SetCopeStocks(self, cope_stocks: List[Stock]) -> None:
        """
         Set the ordered list of stocks to cope.  The stocks must follow
                   segments which are attached the control point of this cope.  
        """
        pass
import NXOpen
class CornerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Corner objects. """
    def GetRcpCornerInfo(self, rcp: ControlPoint) -> Tuple[Corner, Corner.Type]:
        """
         Gets the corner information given a NXOpen.Routing.ControlPoint. 
         Returns A tuple consisting of (corner, corner_type). 
         - corner is:  Corner NXOpen. NXOpen.Routing.Corner associated
                                                                 with this RCP .
         - corner_type is:  Corner.Type NXOpen. Type of corner.

        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CornerTypeBuilder(NXOpen.TaggedObject): 
    """ Contains setting for corner creation. Type of bend to be created and the method to
        create the corner. 
    
    """
    class BendMethods(Enum):
        """
        Members Include: 
         |Radius|  Radius method allows corner creation with the specified radius value  
         |RatioToDiameter|  Ratio to diameter method 
         |BendRadiusTable|  Bend table method creates bend from specified bend table
         |InnerRadius|  Inner Radius method allows corner creation with the specified inner radius value  
         |RatioToAttribute| 

        """
        Radius: int
        RatioToDiameter: int
        BendRadiusTable: int
        InnerRadius: int
        RatioToAttribute: int
        @staticmethod
        def ValueOf(value: int) -> CornerTypeBuilder.BendMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |NotSet|  
         |Miter|  
         |Bend|  
         |SBend|  
         |SElbow|  
         |UBend|  
         |UElbow|  
         |Cope|  
         |MiteredBend| 

        """
        NotSet: int
        Miter: int
        Bend: int
        SBend: int
        SElbow: int
        UBend: int
        UElbow: int
        Cope: int
        MiteredBend: int
        @staticmethod
        def ValueOf(value: int) -> CornerTypeBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def RouteCornerBendMethods(self) -> CornerTypeBuilder.BendMethods:
        """
        Getter for property: ( CornerTypeBuilder.BendMethods NXOpen) RouteCornerBendMethods
         Returns the route corner bend options   
            
         
        """
        pass
    @RouteCornerBendMethods.setter
    def RouteCornerBendMethods(self, routeCornerBendMethods: CornerTypeBuilder.BendMethods):
        """
        Setter for property: ( CornerTypeBuilder.BendMethods NXOpen) RouteCornerBendMethods
         Returns the route corner bend options   
            
         
        """
        pass
    @property
    def RouteCornerNumberOfMiters(self) -> int:
        """
        Getter for property: (int) RouteCornerNumberOfMiters
         Returns the number of miter in mitered bend corner  
            
         
        """
        pass
    @RouteCornerNumberOfMiters.setter
    def RouteCornerNumberOfMiters(self, routeCornerNumberOfMiter: int):
        """
        Setter for property: (int) RouteCornerNumberOfMiters
         Returns the number of miter in mitered bend corner  
            
         
        """
        pass
    @property
    def RouteCornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RouteCornerRadius
         Returns the route corner radius   
            
         
        """
        pass
    @property
    def RouteCornerRatioToAttribute(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RouteCornerRatioToAttribute
         Returns the route corner ratio to attribute   
            
         
        """
        pass
    @property
    def RouteCornerRatioToAttributeName(self) -> str:
        """
        Getter for property: (str) RouteCornerRatioToAttributeName
         Returns the route corner ratio to attribute   
            
         
        """
        pass
    @RouteCornerRatioToAttributeName.setter
    def RouteCornerRatioToAttributeName(self, routeCornerRatioToAttributeName: str):
        """
        Setter for property: (str) RouteCornerRatioToAttributeName
         Returns the route corner ratio to attribute   
            
         
        """
        pass
    @property
    def RouteCornerRatioToDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RouteCornerRatioToDiameter
         Returns the route corner ratio to diameter   
            
         
        """
        pass
    @property
    def RouteCornerRequireLinearSolution(self) -> bool:
        """
        Getter for property: (bool) RouteCornerRequireLinearSolution
         Returns the route corner require linear solution   
            
         
        """
        pass
    @RouteCornerRequireLinearSolution.setter
    def RouteCornerRequireLinearSolution(self, routeCornerRequireLinearSolution: bool):
        """
        Setter for property: (bool) RouteCornerRequireLinearSolution
         Returns the route corner require linear solution   
            
         
        """
        pass
    @property
    def RouteCornerTypeOptions(self) -> CornerTypeBuilder.Type:
        """
        Getter for property: ( CornerTypeBuilder.Type NXOpen) RouteCornerTypeOptions
         Returns the route corner type options   
            
         
        """
        pass
    @RouteCornerTypeOptions.setter
    def RouteCornerTypeOptions(self, routeCornerTypeOptions: CornerTypeBuilder.Type):
        """
        Setter for property: ( CornerTypeBuilder.Type NXOpen) RouteCornerTypeOptions
         Returns the route corner type options   
            
         
        """
        pass
    def GetElbowAppliedCharx(self) -> CharacteristicList:
        """
         Returns the  applied charx of elbow part
         Returns elbowPart ( CharacteristicList NXOpen):  Characteristic list used to find the appropriate .
        """
        pass
    def GetElbowPart(self) -> CharacteristicList:
        """
         Returns the created elbow part
         Returns elbowPart ( CharacteristicList NXOpen):  Characteristic list used to find the appropriate .
        """
        pass
    def RouteCornerAlternateSolution(self) -> None:
        """
         Route alternate solution
        """
        pass
    def RouteCornerBendRadiusInfo(self) -> None:
        """
         Bend corner info 
        """
        pass
    def RouteCornerSpecifyElbow(self) -> None:
        """
         Route specify elbow 
        """
        pass
    def SetElbowAppliedCharx(self, elbowPart: CharacteristicList) -> None:
        """
         Sets the applied charx for elbow creation
        """
        pass
    def SetElbowPart(self, elbowPart: CharacteristicList) -> None:
        """
         Sets the elbow part to be used for elbow creation
        """
        pass
import NXOpen
class Corner(NXOpen.NXObject): 
    """ 
        The Routing Corner is the abstract parent class of all other corner objects. The
        corner object defines some behavior associated with segments and stocks that
        are connected at a single routing control point.
     """
    class Type(Enum):
        """
        Members Include: 
         |Bend|  Bend corner 
         |Miter|  Miter corner. 
         |Cope|  Cope corner. 
         |Discontinuity|  Discontinuity corner. 
         |NotSet|  No corner. 

        """
        Bend: int
        Miter: int
        Cope: int
        Discontinuity: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> Corner.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Rcp(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) Rcp
         Returns the corner ControlPoint referenced by the Corner object.  
             
         
        """
        pass
    @Rcp.setter
    def Rcp(self, rcp: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) Rcp
         Returns the corner ControlPoint referenced by the Corner object.  
             
         
        """
        pass
    def GetStocks(self) -> List[Stock]:
        """
         Returns the stocks that are assigned to segments affected by
                  this corner object.  
         Returns stocks ( Stock List[NXOp): .
        """
        pass
import NXOpen
class CreateFabricationBuilder(NXOpen.Builder): 
    """ Builder class to fabricate subassembly from standard parts, path segments, stock, and other routing objects within the current routing assembly """
    @property
    def RouteSelectionStock(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteSelectionStock
         Returns the route selection stock for selecting routing objects  
            
         
        """
        pass
class CreationMethod(Enum):
    """
    Members Include: 
     |Unknown| 
     |EntireSegments|  
     |Interval|  
     |PointToPoint|  
     |PointAndLength|  

    """
    Unknown: int
    EntireSegments: int
    Interval: int
    PointToPoint: int
    PointAndLength: int
    @staticmethod
    def ValueOf(value: int) -> CreationMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CrossSectionBuilder(NXOpen.Builder): 
    """ Builder for qualifying a Simple  Detail Cross Section """
    @property
    def CurveSelection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) CurveSelection
         Returns the curve selection   
            
         
        """
        pass
    @property
    def Offset01(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset01
         Returns the offset01   
            
         
        """
        pass
    @Offset01.setter
    def Offset01(self, offset01: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) Offset01
         Returns the offset01   
            
         
        """
        pass
    @property
    def Offset02(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset02
         Returns the offset02   
            
         
        """
        pass
    @Offset02.setter
    def Offset02(self, offset02: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) Offset02
         Returns the offset02   
            
         
        """
        pass
    @property
    def SpecifyOffset(self) -> bool:
        """
        Getter for property: (bool) SpecifyOffset
         Returns the specify offset toggle   
            
         
        """
        pass
    @SpecifyOffset.setter
    def SpecifyOffset(self, specifyOffset: bool):
        """
        Setter for property: (bool) SpecifyOffset
         Returns the specify offset toggle   
            
         
        """
        pass
    @property
    def StockStyle(self) -> StockStyle:
        """
        Getter for property: ( StockStyle NXOpen) StockStyle
         Returns the stock style   
            
         
        """
        pass
    @StockStyle.setter
    def StockStyle(self, stockStyle: StockStyle):
        """
        Setter for property: ( StockStyle NXOpen) StockStyle
         Returns the stock style   
            
         
        """
        pass
import NXOpen
class CrossSectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.CrossSection objects.  """
    def CreateCrossSection(self, cross_curves: List[NXOpen.Curve], offset: NXOpen.Expression, second_offset: NXOpen.Expression, style: StockStyle) -> CrossSection:
        """
         Creates a new NXOpen.Routing.CrossSection object.  This object
                  defines a profile for sweeping NXOpen.Routing.Stock objects. In
                  order to build stocks using this cross section, the cross section must be
                  contained in a NXOpen.Routing.StockData object.
                 
         Returns cross ( CrossSection NXOpen): .
        """
        pass
import NXOpen
class CrossSection(NXOpen.NXObject): 
    """ A NXOpen.Routing.CrossSection defines a profile to sweep for NXOpen.Routing.Stock objects. 
        The profile is a set of curves centered around the origin, and in the XY plane.  An offset may be
        specified that forms a second profile that consists of curves offset by the specified offset from
        the profile curves (which forms a hollow stock body, such as a pipe).  
      """
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset expression applied to the profile when generating a Sweep.  
            This forms
                    a second set of profile curves that are offset outwards (for positive offsets, inwards for negative
                    offsets) from the profile curves of the  NXOpen::Routing::CrossSection .  A value of
                    0.0 or a NULL expression indicates no offset.   
         
        """
        pass
    @Offset.setter
    def Offset(self, expression: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) Offset
         Returns the offset expression applied to the profile when generating a Sweep.  
            This forms
                    a second set of profile curves that are offset outwards (for positive offsets, inwards for negative
                    offsets) from the profile curves of the  NXOpen::Routing::CrossSection .  A value of
                    0.0 or a NULL expression indicates no offset.   
         
        """
        pass
    @property
    def SecondOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondOffset
         Returns the offset expression applied to the profile when generating a Sweep.  
            This forms
                    a second set of profile curves that are offset outwards (for positive offsets, inwards for negative
                    offsets) from the profile curves of the  NXOpen::Routing::CrossSection .  A value of
                    0.0 or a NULL expression indicates no offset.   
         
        """
        pass
    @SecondOffset.setter
    def SecondOffset(self, second_offset: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) SecondOffset
         Returns the offset expression applied to the profile when generating a Sweep.  
            This forms
                    a second set of profile curves that are offset outwards (for positive offsets, inwards for negative
                    offsets) from the profile curves of the  NXOpen::Routing::CrossSection .  A value of
                    0.0 or a NULL expression indicates no offset.   
         
        """
        pass
    @property
    def Style(self) -> StockStyle:
        """
        Getter for property: ( StockStyle NXOpen) Style
         Returns the style of the profile.  
            See  NXOpen::Routing::StockData  for information on styles   
         
        """
        pass
    @Style.setter
    def Style(self, style: StockStyle):
        """
        Setter for property: ( StockStyle NXOpen) Style
         Returns the style of the profile.  
            See  NXOpen::Routing::StockData  for information on styles   
         
        """
        pass
    def GetCrossCurves(self) -> List[NXOpen.Curve]:
        """
         Returns the curves that define the profile for the NXOpen.Routing.CrossSection object. 
         Returns curves ( NXOpen.Curve Li):  The curves that define the profile. .
        """
        pass
    def GetMaximumRadius(self) -> float:
        """
         Returns the maximum radius of the profile.  
         Returns radius (float):  The radius of the circle that encircles all profile curves in
                                                         the NXOpen.Routing.CrossSection .
        """
        pass
    def GetStockData(self) -> StockData:
        """
         Returns the NXOpen.Routing.StockData that owns this NXOpen.Routing.CrossSection. 
         Returns stock_data ( StockData NXOpen):  The NXOpen.Routing.StockData that owns the 
                                                          NXOpen.Routing.CrossSection object. .
        """
        pass
    def SetCrossCurves(self, curves: List[NXOpen.Curve]) -> None:
        """
         Sets the curves that define the profile for the NXOpen.Routing.CrossSection object. The
                    curves must form a single closed loop.  
        """
        pass
import NXOpen
class CustomManager(NXOpen.Object): 
    """ The Routing Custom Manager allows you to customize Routing by setting session wide Routing
        preferences and by adding plugins, callbacks, and design rules. """
    class Application(Enum):
        """
        Members Include: 
         |Electrical|  
         |Mechanical|  

        """
        Electrical: int
        Mechanical: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.Application:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CallbackReason(Enum):
        """
        Members Include: 
         |Unknown|  Used only for validation. 
         |PlacePart|  Called after the Place Part command. 
         |MovePart|  Called after the Move Part command. 
         |RemovePart|  Called after the Remove Part command. 
         |MovePath|  Called after the Move Path command. 
         |CopyPath|  Called after the Copy Path command. 
         |DeletePath|  Called after the Delete Path command. 
         |TransformPath|  Called after the Transform Path command. 
         |OffsetPath|  Called after the Offset Path command. 
         |AssignStock|  Called after the Assign Stock command. 
         |WireRouteManual|  Called after the Manual Route command. 
         |WireRouteAuto|  Called after the AutoRoute command. 
         |WireCompManual|  Called after the Manual Assign command. 
         |WireCompAuto|  Called after the AutoAssign command. 
         |WireUnroute|  Called after the Unroute command. 
         |WireUncomp|  Called after the Unassign Component command. 
         |WireTerminals|  Called after the Model Terminals command. 
         |ChoosePart|  Called after the Choose Part command. 
         |CreateConnection|  Called after the Create Connection command. 
         |EditConnection|  Called after the Edit Connection command. 
         |UnassignStock|  Called after the Remove Stock command. 
         |CreateRun|  Called after the Create Run command. 
         |RunPreDelete|  Called before deleting a run. 
         |ReplaceStock|  Called after the Replace Stock command. 
         |CreatePortConnection|  Called after the creating a connection between two ports. 
         |WireCompProxy|  Called after the Assign Proxy command. 
         |ReplacePart|  Called after the Replace Part command. 
         |BrokenConnection|  Called after a port-to-port connection is broken. 
         |EditReplacePart|  Unused. 
         |AttrDiscrepancy|  Called after the Place Part and Replace Part commands. 
         |AttributeCopyReplacePart|  Called after the Replace Part command. 
         |StockComponentCreated|  Called after a stock component is created. 
         |Count|  The number of callback reasons. 

        """
        Unknown: int
        PlacePart: int
        MovePart: int
        RemovePart: int
        MovePath: int
        CopyPath: int
        DeletePath: int
        TransformPath: int
        OffsetPath: int
        AssignStock: int
        WireRouteManual: int
        WireRouteAuto: int
        WireCompManual: int
        WireCompAuto: int
        WireUnroute: int
        WireUncomp: int
        WireTerminals: int
        ChoosePart: int
        CreateConnection: int
        EditConnection: int
        UnassignStock: int
        CreateRun: int
        RunPreDelete: int
        ReplaceStock: int
        CreatePortConnection: int
        WireCompProxy: int
        ReplacePart: int
        BrokenConnection: int
        EditReplacePart: int
        AttrDiscrepancy: int
        AttributeCopyReplacePart: int
        StockComponentCreated: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.CallbackReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DesignRuleReason(Enum):
        """
        Members Include: 
         |Unknown|  Used only for validation. 
         |CreatePath|  Called after the Create Path command. 
         |HealPath|  Called after the Heal Path command. 
         |AssignCorner|  Called after the Assign Corner command. 
         |AssignStock|  Called after the Assign Stock command. 
         |RemoveStock|  Called after the Remove Stockcommand. 
         |StockStyle|  Called after the Stock Style command. 
         |PlacePart|  Called after the Place Part command. 
         |CreateFabrication|  Called after the Create Fabrication command. 
         |QualifyPart|  Called after the Qualify Part command. 
         |MovePath|  Called after the Move Path command. 
         |CopyPath|  Called after the Copy Path command. 
         |DeletePath|  Called after the Delete Path command. 
         |SubdivideSegment|  Called after the Subdivide Segment command. 
         |SimplifyPath|  Called after the Simplify Path command. 
         |RemovePart|  Called after the Remove Part command. 
         |MovePart|  Called after the Move Part command. 
         |EditCharacteristic|  Called after the Edit Characteristics command. 
         |Interactive|  The design rule is called for an interactive check instead of after a particular command. 
         |Batch|  Unused 
         |OrientStock|  Called after the Orient Stock command. 
         |UnifyPath|  Called after the Unify Path command. 
         |TransformPath|  Called after the Transform Path command. 
         |OffsetPath|  Called after the Offset Path command. 
         |AutoRoutePinLevel|  Called after the AutoRoute command using pin level routing. 
         |ManualRoutePinLevel|  Called after the Manual Route command using pin level routing. 
         |AutoRouteComponentLevel|  Called after the AutoRoute command using component level routing. 
         |ManualRouteComponentLevel|  Called after the Manual Route command using component level routing. 
         |Import|  Called after the Import command from the Routing Electrical application's navigators. 
         |SpaceReservation|  Called after the Space Reservation command. 
         |PartialAutoRoute|  Called after the Partial AutoRoute command. 
         |PartialManualRoute|  Called after the Partial Manual Route command. 
         |WindCatcher|  Called after the Wind Catcher command. 
         |CreatePlatform|  Called after the Create Platform command. 
         |EditPlacePart|  Called after the Edit Place Part command. 
         |BulkReplacement|  Called after the Bulk Replacement command. 
         |ReparentParts|  Called after the Reparent Parts command. 
         |CablewayValidation|  Called before the Cableway Export command. 
         |EditTemplateParameters|  Called before the Edit Template Parameters command. 
         |Spline|  Called after the Spline command. 
         |EditPoint|  Called after the Edit Point command. 
         |Endform|  Called after the Place, edit and delete command. 
         |PlaceElbows|  Called after the Place elbows command. 
         |EditCutElbow|  Called after the Edit Cut Elbow command. 
         |Insulation|  Called after the Insulation command. 
         |ConnectComponents|  Called after the Connect Components command. 
         |DisconnectComponents|  Called after the Disconnect Components command. 
         |DerivedPath|  Called after the Derived Path command. 
         |SplitStock|  Called after the Split Stock command. 
         |MergeStock|  Called after the Merge Stock command. 
         |EditPosition|  Called after the Edit Position Method command. 
         |PlaceSplice|  Called after the Place Splice command. 
         |ConnectionCompatibility|  Connection compatibility design rule reason. 
         |SlopePath|  Called after the Slope Path command. 
         |Count|  The number of design rule reasons. 

        """
        Unknown: int
        CreatePath: int
        HealPath: int
        AssignCorner: int
        AssignStock: int
        RemoveStock: int
        StockStyle: int
        PlacePart: int
        CreateFabrication: int
        QualifyPart: int
        MovePath: int
        CopyPath: int
        DeletePath: int
        SubdivideSegment: int
        SimplifyPath: int
        RemovePart: int
        MovePart: int
        EditCharacteristic: int
        Interactive: int
        Batch: int
        OrientStock: int
        UnifyPath: int
        TransformPath: int
        OffsetPath: int
        AutoRoutePinLevel: int
        ManualRoutePinLevel: int
        AutoRouteComponentLevel: int
        ManualRouteComponentLevel: int
        Import: int
        SpaceReservation: int
        PartialAutoRoute: int
        PartialManualRoute: int
        WindCatcher: int
        CreatePlatform: int
        EditPlacePart: int
        BulkReplacement: int
        ReparentParts: int
        CablewayValidation: int
        EditTemplateParameters: int
        Spline: int
        EditPoint: int
        Endform: int
        PlaceElbows: int
        EditCutElbow: int
        Insulation: int
        ConnectComponents: int
        DisconnectComponents: int
        DerivedPath: int
        SplitStock: int
        MergeStock: int
        EditPosition: int
        PlaceSplice: int
        ConnectionCompatibility: int
        SlopePath: int
        Count: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.DesignRuleReason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DuctSizeCalculatorDisplayNoteFlag(Enum):
        """
        Members Include: 
         |AddNote| 
         |RemoveNote| 

        """
        AddNote: int
        RemoveNote: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.DuctSizeCalculatorDisplayNoteFlag:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DuctSizeCalculatorDuctShape(Enum):
        """
        Members Include: 
         |Rectangular| 
         |Circular| 
         |FlatOval| 

        """
        Rectangular: int
        Circular: int
        FlatOval: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.DuctSizeCalculatorDuctShape:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NavigatorType(Enum):
        """
        Members Include: 
         |Component|  The objects were selected in the component navigator.  
         |Connection|  The objects were selected in the connection navigator. 

        """
        Component: int
        Connection: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.NavigatorType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PipingComponentFileOptions(Enum):
        """
        Members Include: 
         |AskToOverwriteFile|  Prompt the user of the plugin if it is OK to overwrite the piping component file.  
         |NeverOverwriteFile|  Never overwrite any existing piping component file. Throw an error if the file exists. 
         |AlwaysOverwriteFile|  Always overwrite any existing piping component file. 

        """
        AskToOverwriteFile: int
        NeverOverwriteFile: int
        AlwaysOverwriteFile: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.PipingComponentFileOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectionType(Enum):
        """
        Members Include: 
         |Deselected|  The objects were deselected. 
         |Selected|  The objects were selected.   

        """
        Deselected: int
        Selected: int
        @staticmethod
        def ValueOf(value: int) -> CustomManager.SelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    Callback = Callable[[List[NXOpen.NXObject]], None]
    def AddCallback(self, reason: CustomManager.CallbackReason, callbackMethod: CustomManager.Callback) -> int:
        """
         Adds the callback with the given reason.
                    NOTE: You can register more than one callback with the same reason. 
         Returns callbackMethodId (int):  A unique identifier for your callback. .
        """
        pass
    DesignRule = Callable[[CustomManager.DesignRuleReason, List[NXOpen.NXObject]], None]
    def AddDesignRule(self, reason: CustomManager.DesignRuleReason, name: str, description: str, designRuleMethod: CustomManager.DesignRule) -> int:
        """
         Adds the design rule with the given reason.
                    NOTE: You can register more than one design rule with the same reason. 
         Returns designRuleMethodId (int):  A unique identifier for your design rule. .
        """
        pass
    ApplicationEnterPlugin = Callable[[CustomManager.Application], None]
    ApplicationExitPlugin = Callable[[CustomManager.Application], None]
    AutoroutePlugin = Callable[[List[NXOpen.Routing.Electrical.Connection]], None]
    BomPlugin = Callable[[], None]
    BundlePlugin = Callable[[List[StockData]], None]
    ChoosePartPlugin = Callable[[ChoosePartPluginData], None]
    ComponentNamePlugin = Callable[[ComponentNamePluginData], None]
    def CreateViolationForReason(self, designRuleName: str, reason: CustomManager.DesignRuleReason, shortDescription: str, longDescription: str, objects: List[NXOpen.NXObject]) -> DesignRuleViolation:
        """
         Creates a new violation for a design rule reason. 
         Returns violation ( DesignRuleViolation NXOpen):  The newly created violation object. .
        """
        pass
    def DeleteViolationsOfRuleOnObject(self, designRuleName: str, nxObject: NXOpen.NXObject) -> None:
        """
         Finds the violation of a design rule attached to the given object and deletes it.
                    Useful when the given object no longer violates this rule.
                    This method calls update after deleting the violations. 
        """
        pass
    def DeleteViolationsOnObjectForReason(self, reason: CustomManager.DesignRuleReason, nxObject: NXOpen.NXObject) -> None:
        """
         Finds the violation of a design rule reason attached to the given object and deletes it.
                    Useful when the given object no longer violates this rule.
                    This method calls update after deleting the violations. 
        """
        pass
    DisciplineChangedPlugin = Callable[[str, str], None]
    DuctSizeCalculatorCreateStockPlugin = Callable[[List[NXOpen.Curve], CustomManager.DuctSizeCalculatorDuctShape, float, float, float], None]
    DuctSizeCalculatorDisplayNotePlugin = Callable[[NXOpen.Curve, CustomManager.DuctSizeCalculatorDisplayNoteFlag], None]
    FilterBlankingPlugin = Callable[[NXOpen.NXObject, str, str, str], None]
    GeneratePLMXMLFileNamePluginForBulkExport = Callable[[str, str, str], None]
    GenerateStockComponentNameplugin = Callable[[Stock], None]
    def GetCallbacksRegisteredForReason(self, reason: CustomManager.CallbackReason) -> List[int]:
        """
         Returns the callbacks, if any, registered for the given reason. 
         Returns registeredCallbackIds (List[int]):  The callback identifiers, if any, registered with this reason. .
        """
        pass
    def GetDesignRulesRegisteredForReason(self, reason: CustomManager.DesignRuleReason) -> List[int]:
        """
         Returns the design rules, if any, registered for the given reason. 
         Returns registeredDesignRuleIds (List[int]):  The design rule identifiers, if any, registered with this reason. .
        """
        pass
    def GetViolationsForReason(self, reason: CustomManager.DesignRuleReason) -> List[DesignRuleViolation]:
        """
         Returns any violations recorded against a design rule reason. 
         Returns violations ( DesignRuleViolation List[NXOp):  The violations for this reason. .
        """
        pass
    def GetViolationsOfRule(self, designRuleName: str) -> List[DesignRuleViolation]:
        """
         Returns any violations recorded against a design rule. 
         Returns violations ( DesignRuleViolation List[NXOp):  The violations for this reason. .
        """
        pass
    ImportExportPlugin = Callable[[str], None]
    NavigatorObjectSelectedPlugin = Callable[[CustomManager.NavigatorType, CustomManager.SelectionType, List[NXOpen.NXObject]], None]
    PipingComponentFilePlugin = Callable[[str, List[NXOpen.Assemblies.Component], CustomManager.PipingComponentFileOptions], None]
    PlmxmlObjectNamePlugin = Callable[[], None]
    def RemoveAllCallbacks(self) -> None:
        """
         Removes all the registered callbacks, except those configured in the Application View (APV) file. 
        """
        pass
    def RemoveAllCallbacksForReason(self, reason: CustomManager.CallbackReason) -> None:
        """
         Removes all the callbacks registered for a particular reason. 
        """
        pass
    def RemoveAllDesignRules(self) -> None:
        """
         Removes all the registered design rules, except those configured in the Application View (APV) file. 
        """
        pass
    def RemoveAllDesignRulesForReason(self, reason: CustomManager.DesignRuleReason) -> None:
        """
         Removes all the design rules registered for a particular reason. 
        """
        pass
    def RemoveAllPlugins(self) -> None:
        """
         Removes all the registered plugins, except those configured in the Application View (APV) file. 
        """
        pass
    def RemoveApplicationEnterPlugin(self) -> None:
        """
         Removes any registered application enter plugin. 
        """
        pass
    def RemoveApplicationExitPlugin(self) -> None:
        """
         Removes any registered application exit plugin. 
        """
        pass
    def RemoveAutoRoutePlugin(self) -> None:
        """
         Removes any registered autoroute plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveBomPlugin(self) -> None:
        """
         Removes any registered bill of materials plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveBundlePlugin(self) -> None:
        """
         Removes any registered bundle plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveCallback(self, callbackMethodId: int) -> None:
        """
         Removes the registered callback. 
        """
        pass
    def RemoveChoosePartPlugin(self) -> None:
        """
         Removes any registered choose part plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveCmpPostExportPlugin(self) -> None:
        """
         Removes any registered post-export CMP plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveCmpPreImportPlugin(self) -> None:
        """
         Removes any registered pre-import CMP plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveCutElbowComponentNamePlugin(self) -> None:
        """
         Removes any registered cut elbow component name plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveDesignRule(self, designRuleMethodId: int) -> None:
        """
         Removes the registered design rule. 
        """
        pass
    def RemoveDisciplineChangedPlugin(self) -> None:
        """
         Removes any registered discipline changed plugin. 
        """
        pass
    def RemoveDuctSizeCalculatorCreateStockPlugin(self) -> None:
        """
         Removes any registered create stock plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveDuctSizeCalculatorDisplayNotePlugin(self) -> None:
        """
         Removes any registered display note plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveFilterBlankingPlugin(self) -> None:
        """
         Removes any registered filter blanking plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveGeneratePLMXMLFileNamePluginForBulkExport(self) -> None:
        """
         Removes any registered plugin for generating PLMXML file for bulk export 
        """
        pass
    def RemoveGenerateStockComponentNamePlugin(self) -> None:
        """
         Removes any registered generate stock component name plugin. 
        """
        pass
    def RemoveHrnPostExportPlugin(self) -> None:
        """
         Removes any registered post-export HRN plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveHrnPreImportPlugin(self) -> None:
        """
         Removes any registered pre-import HRN plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveManualRoutePlugin(self) -> None:
        """
         Removes any registered manual route plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveNavigatorObjectSelectedPlugin(self) -> None:
        """
         Removes any registered navigator object selected plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemovePipingComponentFilePlugin(self) -> None:
        """
         Removes any registered piping component file plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemovePlmXmlPostExportPlugin(self) -> None:
        """
         Removes any registered post-export PLMXML plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemovePlmXmlPreImportPlugin(self) -> None:
        """
         Removes any registered pre-import PLMXML plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemovePlmXmlRouteNodeNamePlugin(self) -> None:
        """
         Removes any registered Route Node name plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemovePlmXmlRouteSectionNamePlugin(self) -> None:
        """
         Removes any registered Route Section name plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveSortConnectionsPlugin(self) -> None:
        """
         Removes any registered sort connections plugin. 
        """
        pass
    def RemoveSpecificationChangedPlugin(self) -> None:
        """
         Removes any registered specification changed plugin. 
        """
        pass
    def RemoveStockComponentLockedPlugin(self) -> None:
        """
         Removes any registered stock component locked plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveStockComponentNamePlugin(self) -> None:
        """
         Removes any registered stock component name plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveTemporaryStockComponentNamePlugin(self) -> None:
        """
         Removes any registered stock component name plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveUnifyPathPlugin(self) -> None:
        """
         Removes any registered unify path plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveUnroutePlugin(self) -> None:
        """
         Removes any registered unroute plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveValidateFormboardPlugin(self) -> None:
        """
         Removes any registered validate formboard plugin, except one configured in the Application View (APV) file. 
        """
        pass
    def RemoveWrappedOverstockLengthCalculationPlugin(self) -> None:
        """
         Removes any registered wrapped overstock length calculation plugin,
                    except one configured in the Application View (APV) file. 
        """
        pass
    def SetApplicationEnterPlugin(self, applicationEnterPlugin: CustomManager.ApplicationEnterPlugin) -> None:
        """
         Sets the plugin Routing will call when entering a Routing application.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetApplicationExitPlugin(self, applicationExitPlugin: CustomManager.ApplicationExitPlugin) -> None:
        """
         Sets the plugin Routing will call when exiting a Routing application.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetAutoRoutePlugin(self, autoRoutePlugin: CustomManager.AutoroutePlugin) -> None:
        """
         Sets the plugin Routing will instead of the internal automatic routing of
                    connections along a path.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetBomPlugin(self, bomPlugin: CustomManager.BomPlugin) -> None:
        """
         Sets the plugin called just after Routing creates a bill of materials.
                    The intent is that the plugin can then add stocks to Teamcenter's Product Structure.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetBundlePlugin(self, bundlePlugin: CustomManager.BundlePlugin) -> None:
        """
         Sets the plugin Routing will call to determine the bundle diameter for each
                    bundle in a harness.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetChoosePartPlugin(self, choosePartPlugin: CustomManager.ChoosePartPlugin) -> None:
        """
         Sets the choose part plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetCmpPostExportPlugin(self, cmpPostExportPlugin: CustomManager.ImportExportPlugin) -> None:
        """
         Sets the plugin called just after Routing exports an CMP file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetCmpPreImportPlugin(self, cmpPreImportPlugin: CustomManager.ImportExportPlugin) -> None:
        """
         Sets the plugin called before importing an CMP file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetCutElbowComponentNamePlugin(self, cutElbowComponentNamePlugin: CustomManager.ComponentNamePlugin) -> None:
        """
         Sets the cut elbow component name plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetDisciplineChangedPlugin(self, disciplineChangedPlugin: CustomManager.DisciplineChangedPlugin) -> None:
        """
         Sets the plugin Routing will call when the discipline is changed.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetDuctSizeCalculatorCreateStockPlugin(self, createStockPlugin: CustomManager.DuctSizeCalculatorCreateStockPlugin) -> None:
        """
         Sets the plugin Routing will use to create stock for the Duct Size Calculator command.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetDuctSizeCalculatorDisplayNotePlugin(self, displayNotePlugin: CustomManager.DuctSizeCalculatorDisplayNotePlugin) -> None:
        """
         Sets the plugin Routing will use to display a note on the segments selected in the Duct Size Calculator.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetFilterBlankingPlugin(self, filterBlankingPlugin: CustomManager.FilterBlankingPlugin) -> None:
        """
         Sets the plugin called by Routing to determine if a segment or component needs to be blanked.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetGeneratePLMXMLFileNamePluginForBulkExport(self, partName: CustomManager.GeneratePLMXMLFileNamePluginForBulkExport) -> None:
        """
         Sets the plugin Routing will call to get the name for PLMXML file
                    while exporting the PLMXML files when Wiring Preference Export Route List in Bulk is toggled ON.
                
        """
        pass
    def SetGenerateStockComponentNamePlugin(self, generateStockComponentNamePlugin: CustomManager.GenerateStockComponentNameplugin) -> None:
        """
         Sets the plugin Routing will call to get the name for stock
                     while creating new stock part during Advance process.
                     Will throw an error if one is already registered.
                
        """
        pass
    def SetHrnPostExportPlugin(self, hrnPostExportPlugin: CustomManager.ImportExportPlugin) -> None:
        """
         Sets the plugin called just after Routing exports an HRN file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetHrnPreImportPlugin(self, hrnPreImportPlugin: CustomManager.ImportExportPlugin) -> None:
        """
         Sets the plugin called before importing an HRN file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetManualRoutePlugin(self, manualRoutePlugin: CustomManager.AutoroutePlugin) -> None:
        """
         Sets the plugin Routing will instead of the internal manual routing of
                    connections along a path. This uses the same plugin prototype as the autoroute plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetNavigatorObjectSelectedPlugin(self, navigatorObjectSelectedPlugin: CustomManager.NavigatorObjectSelectedPlugin) -> None:
        """
         Sets the plugin Routing will call whenever an object on the Component or
                    Connection Navigator is selected or deselected.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetPipingComponentFilePlugin(self, pipingComponentFilePlugin: CustomManager.PipingComponentFilePlugin) -> None:
        """
         Sets the plugin Routing will use for the Unify Path command.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetPlmXmlPostExportPlugin(self, plmXmlPostExportPlugin: CustomManager.ImportExportPlugin) -> None:
        """
         Sets the plugin called just after Routing exports an PLMXML file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetPlmXmlPreImportPlugin(self, plmXmlPreImportPlugin: CustomManager.ImportExportPlugin) -> None:
        """
         Sets the plugin called before importing an PLMXML file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetPlmXmlRouteNodeNamePlugin(self, plmXmlRouteNodeNamePlugin: CustomManager.PlmxmlObjectNamePlugin) -> None:
        """
         Sets the plugin Routing will call to get the name of the next Route Node for the PLMXML file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetPlmXmlRouteSectionNamePlugin(self, plmXmlRouteSectionNamePlugin: CustomManager.PlmxmlObjectNamePlugin) -> None:
        """
         Sets the plugin Routing will call to get the name of the next Route Section for the PLMXML file.
                    Will throw an error if one is already registered.
                
        """
        pass
    SortConnectionsPlugin = Callable[[NXOpen.Routing.Electrical.SortConnectionsPluginData], None]
    def SetSortConnectionsPlugin(self, sortConnectionsPlugin: CustomManager.SortConnectionsPlugin) -> None:
        """
         Sets the plugin Routing will call to sort the connections about to be routed.
                    Will throw an error if one is already registered.
                
        """
        pass
    SpecificationChangedPlugin = Callable[[str, str], None]
    def SetSpecificationChangedPlugin(self, specificationChangedPlugin: CustomManager.SpecificationChangedPlugin) -> None:
        """
         Sets the plugin Routing will call when the specification is changed.
                    Will throw an error if one is already registered.
                
        """
        pass
    StockComponentLockedPlugin = Callable[[Stock], None]
    def SetStockComponentLockedPlugin(self, stockComponentLockedPlugin: CustomManager.StockComponentLockedPlugin) -> None:
        """
         Sets the plugin Routing will call to see if a stock component is modifiable.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetStockComponentNamePlugin(self, stockComponentNamePlugin: CustomManager.ComponentNamePlugin) -> None:
        """
         Sets the stock component name plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetTemporaryStockComponentNamePlugin(self, stockComponentNamePlugin: CustomManager.ComponentNamePlugin) -> None:
        """
         Sets the temporary stock component name plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    UnifyPathPlugin = Callable[[List[NXOpen.NXObject]], None]
    def SetUnifyPathPlugin(self, unifyPathPlugin: CustomManager.UnifyPathPlugin) -> None:
        """
         Sets the plugin Routing will use for the Unify Path command.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetUnroutePlugin(self, unroutePlugin: CustomManager.AutoroutePlugin) -> None:
        """
         Sets the plugin Routing will instead of the internal unroute method.
                    This uses the same plugin prototype as the autoroute plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    ValidateFormboardPlugin = Callable[[List[NXOpen.Routing.Electrical.HarnessDevice]], None]
    def SetValidateFormboardPlugin(self, validateFormboardPlugin: CustomManager.ValidateFormboardPlugin) -> None:
        """
         Sets the plugin Routing will call to validate the harnesses on a formboard.
                    Will throw an error if one is already registered.
                
        """
        pass
    WrappedOverstockLengthCalculationPlugin = Callable[[Overstock], None]
    def SetWrappedOverstockLengthCalculationPlugin(self, lengthCalculationPlugin: CustomManager.WrappedOverstockLengthCalculationPlugin) -> None:
        """
         Sets the plugin called by Routing to calculate the length of a wrapped overstock.
                    Will throw an error if one is already registered.
                
        """
        pass
import NXOpen
class DefineRunBuilder(NXOpen.Builder): 
    """ Builder Class for DefineRun Object """
    @property
    def FromItemsList(self) -> RunItemsBuilderList:
        """
        Getter for property: ( RunItemsBuilderList NXOpen) FromItemsList
         Returns the FROM items list of the run.  
          
                     The list consists of  NXOpen::Routing::DefineRunBuilder   objects.   
         
        """
        pass
    @property
    def MemberItems(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) MemberItems
         Returns  the MEMBER items of the run.  
             
         
        """
        pass
    @property
    def RunIdentifier(self) -> str:
        """
        Getter for property: (str) RunIdentifier
         Returns the run identifier   
            
         
        """
        pass
    @RunIdentifier.setter
    def RunIdentifier(self, runIdentifier: str):
        """
        Setter for property: (str) RunIdentifier
         Returns the run identifier   
            
         
        """
        pass
    @property
    def RunType(self) -> str:
        """
        Getter for property: (str) RunType
         Returns the run type   
            
         
        """
        pass
    @RunType.setter
    def RunType(self, runType: str):
        """
        Setter for property: (str) RunType
         Returns the run type   
            
         
        """
        pass
    @property
    def SpecificationOption(self) -> str:
        """
        Getter for property: (str) SpecificationOption
         Returns the specification of the run.  
             
         
        """
        pass
    @SpecificationOption.setter
    def SpecificationOption(self, specificationOption: str):
        """
        Setter for property: (str) SpecificationOption
         Returns the specification of the run.  
             
         
        """
        pass
    @property
    def ToItemsList(self) -> RunItemsBuilderList:
        """
        Getter for property: ( RunItemsBuilderList NXOpen) ToItemsList
         Returns the TO items list of the run .  
          
                The list consists of  NXOpen::Routing::DefineRunBuilder   objects.   
         
        """
        pass
    def AddMemberItems(self, memberItem: NXOpen.TaggedObject) -> None:
        """
         Append a member item  to the list in the builder for DefineRun 
        """
        pass
    def CreateRunItemsBuilder(self) -> RunItemsBuilder:
        """
         Creates a RunItems  used to create list item for DefineRun 
         Returns runItemsBuilder ( RunItemsBuilder NXOpen):   runItems builder.
        """
        pass
    def RemoveMemberItems(self, memberItems: List[NXOpen.TaggedObject]) -> None:
        """
         Remove a member item  from the list in the builder for DefineRun 
        """
        pass
    def UnifyPath(self) -> None:
        """
         UnifyPath of the run.
        """
        pass
import NXOpen
class DefiningPoint(NXOpen.TransientObject): 
    """  Represents a NXOpen.Routing.DefiningPoint object. 
         This class is used by the NXOpen.Routing.SplineData object to
               represent a defining point of an NX Routing spline segment. 
         The class provides interfaces to specify a point's position and optional extension
               direction and magnitudes. 
         Use the NXOpen.Routing.SplineData.GetDefiningPoints method
               to get the point and extension data for a spline.  """
    @property
    def BackwardExtension(self) -> float:
        """
        Getter for property: (float) BackwardExtension
         Returns the backward extension of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    @BackwardExtension.setter
    def BackwardExtension(self, backwardExtension: float):
        """
        Setter for property: (float) BackwardExtension
         Returns the backward extension of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    @property
    def Direction(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) Direction
         Returns the extension direction of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) Direction
         Returns the extension direction of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    @property
    def ForwardExtension(self) -> float:
        """
        Getter for property: (float) ForwardExtension
         Returns the forward extension of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    @ForwardExtension.setter
    def ForwardExtension(self, forwardExtension: float):
        """
        Setter for property: (float) ForwardExtension
         Returns the forward extension of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    @property
    def Position(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Position
         Returns the position of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    @Position.setter
    def Position(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Position
         Returns the position of the  NXOpen::Routing::DefiningPoint .  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the NXOpen.Routing.DefiningPoint object. 
        """
        pass
    def IsConstrained(self) -> bool:
        """
         Does the NXOpen.Routing.DefiningPoint have any
                    NXOpen.Positioning.Constraint that determines its location?
                    If so, you cannot change the position of this point. 
         Returns isConstrained (bool): .
        """
        pass
import NXOpen
class DeleteFontsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Routing.DeleteFontsBuilder
    """
    @property
    def ObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) ObjectCollector
         Returns the routing object collector   
            
         
        """
        pass
import NXOpen
class DeleteGapsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Routing.DeleteGapsBuilder
    """
    @property
    def ObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) ObjectCollector
         Returns the routing object collector   
            
         
        """
        pass
import NXOpen
class DeleteObjectsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Routing.DeleteObjectsBuilder
    """
    @property
    def ObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) ObjectCollector
         Returns the routing object collector   
            
         
        """
        pass
import NXOpen
class DesignRuleCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.DesignRule objects. """
    pass
import NXOpen
class DesignRuleManager(NXOpen.Object): 
    """ Represents NXOpen.Routing.DesignRuleManager object """
    def ClearConcurrent() -> None:
        """
         Remove all objects from the concurrent check list 
        """
        pass
    def ExpandConcurrent() -> None:
        """
         Expand the current list of objects on the concurrent check list to include 'dependents' 
        """
        pass
    def GetConcurrentObjects() -> List[NXOpen.NXObject]:
        """
          Inquire the list of objects to be checked at the next concurrent check. 
         Returns objects ( NXOpen.NXObject Li):   .
        """
        pass
    def GetObjectViolations(nxObject: NXOpen.NXObject) -> List[DesignRuleViolation]:
        """
         Returns the violations, if any, on the given object. 
         Returns violations ( DesignRuleViolation List[NXOp):  .
        """
        pass
    def LogConcurrent(object_to_log: NXOpen.NXObject) -> None:
        """
         Add an object to be checked during the next concurrent design rule check 
        """
        pass
    def UnlogConcurrent(object_to_unlog: NXOpen.NXObject) -> None:
        """
         Remove an object from the list of objects to be checked at the next design rule check. 
        """
        pass
import NXOpen
class DesignRuleOverride(NXOpen.NXObject): 
    """ Represents Routing DesignRuleOverride object """
    @property
    def Reason(self) -> str:
        """
        Getter for property: (str) Reason
         Returns the reason of the design rule override is returned   
            
         
        """
        pass
    @Reason.setter
    def Reason(self, reason: str):
        """
        Setter for property: (str) Reason
         Returns the reason of the design rule override is returned   
            
         
        """
        pass
    @property
    def TimeStamp(self) -> int:
        """
        Getter for property: (int) TimeStamp
         Returns the date and time the override was created or updated.  
          
                   The time stamp is number of seconds since the UNIX epoch (midnight GMT, 1 January 1970).
                   
         
        """
        pass
    @TimeStamp.setter
    def TimeStamp(self, timeStamp: int):
        """
        Setter for property: (int) TimeStamp
         Returns the date and time the override was created or updated.  
          
                   The time stamp is number of seconds since the UNIX epoch (midnight GMT, 1 January 1970).
                   
         
        """
        pass
    @property
    def User(self) -> str:
        """
        Getter for property: (str) User
         Returns the user of the design rule override is returned   
            
         
        """
        pass
    @User.setter
    def User(self, user: str):
        """
        Setter for property: (str) User
         Returns the user of the design rule override is returned   
            
         
        """
        pass
    def GetViolation(self) -> DesignRuleViolation:
        """
         Returns the violation of this override. 
         Returns violation ( DesignRuleViolation NXOpen): .
        """
        pass
import NXOpen
class DesignRuleViolationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.DesignRuleViolation objects. """
    class Mode(Enum):
        """
        Members Include: 
         |Concurrent|  Executes design rules on all concurrently logged objects.
                                                        Use LogConcurrent method on NXOpen.Routing.RouteManager
                                                        to concurrently logged objects and GetConcurrent method to get all the
                                                        concurrent objects 
         |Interactive|  Execute design rules during next interactive check 
         |Batch|  Unused. 

        """
        Concurrent: int
        Interactive: int
        Batch: int
        @staticmethod
        def ValueOf(value: int) -> DesignRuleViolationCollection.Mode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Reason(Enum):
        """
        Members Include: 
         |Unknown|  
         |CreatePath|  
         |HealPath|  
         |AssignCorner|  
         |AssignStock|  
         |RemoveStock|  
         |StockStyle|  
         |PlacePart|  
         |CreateFab|  
         |QualifyPart|  
         |MovePath|  
         |CopyPath|  
         |DeletePath|  
         |SubdivideSeg|  
         |SimplifyPath|  
         |RemovePart|  
         |MovePart|  
         |EditCharx|  
         |Interactive|  
         |Batch|  
         |OrientStock|  
         |UnifyPath|  
         |TransformPath|  
         |OffsetPath|  
         |AutoRoutePin|  
         |ManualRoutePin|  
         |AutoRouteComp|  
         |ManualRouteComp|  
         |Import|  
         |PartialAutoRouteComp|  
         |EditPlacePart|  
         |BulkReplacement|  

        """
        Unknown: int
        CreatePath: int
        HealPath: int
        AssignCorner: int
        AssignStock: int
        RemoveStock: int
        StockStyle: int
        PlacePart: int
        CreateFab: int
        QualifyPart: int
        MovePath: int
        CopyPath: int
        DeletePath: int
        SubdivideSeg: int
        SimplifyPath: int
        RemovePart: int
        MovePart: int
        EditCharx: int
        Interactive: int
        Batch: int
        OrientStock: int
        UnifyPath: int
        TransformPath: int
        OffsetPath: int
        AutoRoutePin: int
        ManualRoutePin: int
        AutoRouteComp: int
        ManualRouteComp: int
        Import: int
        PartialAutoRouteComp: int
        EditPlacePart: int
        BulkReplacement: int
        @staticmethod
        def ValueOf(value: int) -> DesignRuleViolationCollection.Reason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def ReasonExecuteRule(self, mode: DesignRuleViolationCollection.Mode, reason: DesignRuleViolationCollection.Reason, objs: List[NXOpen.NXObject]) -> List[DesignRuleViolation]:
        """
         Executes design rules and returns all the violations of the rule 
         Returns violations ( DesignRuleViolation List[NXOp):  Violations .
        """
        pass
import NXOpen
class DesignRuleViolationLocationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.DesignRuleViolationLocation objects. """
    class DeleteOption(Enum):
        """
        Members Include: 
         |DoDelete|  
         |DontDelete|  Set this option only if you do not want to delete violation location objects

        """
        DoDelete: int
        DontDelete: int
        @staticmethod
        def ValueOf(value: int) -> DesignRuleViolationLocationCollection.DeleteOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CreateDesignRuleViolationLocation(self, delete_location_objects: DesignRuleViolationLocationCollection.DeleteOption, location_objects: List[NXOpen.NXObject]) -> DesignRuleViolationLocation:
        """
         Creates a NXOpen.Routing.DesignRuleViolationLocation object. 
         Returns design_rule_violation_location ( DesignRuleViolationLocation NXOpen):  .
        """
        pass
import NXOpen
class DesignRuleViolationLocation(NXOpen.NXObject): 
    """ Represents NXOpen.Routing.DesignRuleViolationLocation object """
    @property
    def DeleteLocationObjects(self) -> DesignRuleViolationLocationCollection.DeleteOption:
        """
        Getter for property: ( DesignRuleViolationLocationCollection.DeleteOption NXOpen) DeleteLocationObjects
         Returns the function returns delete location objects, 
                    which is an option for deletion of violation location objects.  
             
         
        """
        pass
    @DeleteLocationObjects.setter
    def DeleteLocationObjects(self, delete_location_objects: DesignRuleViolationLocationCollection.DeleteOption):
        """
        Setter for property: ( DesignRuleViolationLocationCollection.DeleteOption NXOpen) DeleteLocationObjects
         Returns the function returns delete location objects, 
                    which is an option for deletion of violation location objects.  
             
         
        """
        pass
    def GetLocationObjects(self) -> List[NXOpen.NXObject]:
        """
         This function returns an array of all Objects at a violation location along with its count. 
         Returns location_objects ( NXOpen.NXObject Li):  Location objects  array.  .
        """
        pass
    def SetLocationObjects(self, location_objects: List[NXOpen.NXObject]) -> None:
        """
          
        """
        pass
import NXOpen
class DesignRuleViolationViewer(NXOpen.Builder): 
    """ This class can be used to set the violation id, update text for overridding the violation and 
        update the user name used to override the violation. """
    class FilterOption(Enum):
        """
        Members Include: 
         |AllViolations|  will show all violations 
         |SkipOverrides|  will not show overridden violations 
         |OverridesOnly|  will show only overridden violations 

        """
        AllViolations: int
        SkipOverrides: int
        OverridesOnly: int
        @staticmethod
        def ValueOf(value: int) -> DesignRuleViolationViewer.FilterOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OverrideOption(Enum):
        """
        Members Include: 
         |Yes|  this shows that current violation is overridden violations 
         |No|  this shows that current violation is not overridden. 

        """
        Yes: int
        No: int
        @staticmethod
        def ValueOf(value: int) -> DesignRuleViolationViewer.OverrideOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DialogViolationId(self) -> int:
        """
        Getter for property: (int) DialogViolationId
         Returns the dialog design rule violation Id   
            
         
        """
        pass
    @DialogViolationId.setter
    def DialogViolationId(self, dialogViolationID: int):
        """
        Setter for property: (int) DialogViolationId
         Returns the dialog design rule violation Id   
            
         
        """
        pass
    @property
    def FilterOptionValue(self) -> DesignRuleViolationViewer.FilterOption:
        """
        Getter for property: ( DesignRuleViolationViewer.FilterOption NXOpen) FilterOptionValue
         Returns the value for filter option of route Design Rule Violation    
            
         
        """
        pass
    @FilterOptionValue.setter
    def FilterOptionValue(self, filter_option_value: DesignRuleViolationViewer.FilterOption):
        """
        Setter for property: ( DesignRuleViolationViewer.FilterOption NXOpen) FilterOptionValue
         Returns the value for filter option of route Design Rule Violation    
            
         
        """
        pass
    @property
    def NavigateViolationLocationOption(self) -> bool:
        """
        Getter for property: (bool) NavigateViolationLocationOption
         Returns the state of Violation Location toggle option, 
                    if true: Navigate Violation Locations of current violation
                    if false: Navigate Violations.  
              
         
        """
        pass
    @NavigateViolationLocationOption.setter
    def NavigateViolationLocationOption(self, navigateViolationLocationOption: bool):
        """
        Setter for property: (bool) NavigateViolationLocationOption
         Returns the state of Violation Location toggle option, 
                    if true: Navigate Violation Locations of current violation
                    if false: Navigate Violations.  
              
         
        """
        pass
    @property
    def OverrideOptionValue(self) -> DesignRuleViolationViewer.OverrideOption:
        """
        Getter for property: ( DesignRuleViolationViewer.OverrideOption NXOpen) OverrideOptionValue
         Returns the value for design Rule Violation override option
                    if Yes: violation is overridden
                    if No:  violation is not overridden   
            
         
        """
        pass
    @OverrideOptionValue.setter
    def OverrideOptionValue(self, override_option_value: DesignRuleViolationViewer.OverrideOption):
        """
        Setter for property: ( DesignRuleViolationViewer.OverrideOption NXOpen) OverrideOptionValue
         Returns the value for design Rule Violation override option
                    if Yes: violation is overridden
                    if No:  violation is not overridden   
            
         
        """
        pass
    @property
    def Username(self) -> str:
        """
        Getter for property: (str) Username
         Returns the username who has overridden design Rule violation   
            
         
        """
        pass
    @Username.setter
    def Username(self, username: str):
        """
        Setter for property: (str) Username
         Returns the username who has overridden design Rule violation   
            
         
        """
        pass
    def GetOverrideText(self) -> List[str]:
        """
         Returns the text written as a reason for overriding the violation 
         Returns overrideText (List[str]): .
        """
        pass
    def SetOverrideText(self, overrideText: List[str]) -> None:
        """
         Sets the text for reason of overriding the violation 
        """
        pass
import NXOpen
class DesignRuleViolation(NXOpen.NXObject): 
    """ Represents NXOpen.Routing.DesignRuleViolation object """
    class BlankOption(Enum):
        """
        Members Include: 
         |Blank|   
         |Unblank|  

        """
        Blank: int
        Unblank: int
        @staticmethod
        def ValueOf(value: int) -> DesignRuleViolation.BlankOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LongDescription(self) -> str:
        """
        Getter for property: (str) LongDescription
         Returns the long description of the design rule violation is returned   
            
         
        """
        pass
    @LongDescription.setter
    def LongDescription(self, long_description: str):
        """
        Setter for property: (str) LongDescription
         Returns the long description of the design rule violation is returned   
            
         
        """
        pass
    @property
    def Override(self) -> DesignRuleOverride:
        """
        Getter for property: ( DesignRuleOverride NXOpen) Override
         Returns the override object for the violation is inquired   
            
         
        """
        pass
    @Override.setter
    def Override(self, overrideTag: DesignRuleOverride):
        """
        Setter for property: ( DesignRuleOverride NXOpen) Override
         Returns the override object for the violation is inquired   
            
         
        """
        pass
    @property
    def ShortDescription(self) -> str:
        """
        Getter for property: (str) ShortDescription
         Returns the short description of the design rule violation is returned   
            
         
        """
        pass
    @ShortDescription.setter
    def ShortDescription(self, short_description: str):
        """
        Setter for property: (str) ShortDescription
         Returns the short description of the design rule violation is returned   
            
         
        """
        pass
    @property
    def TimeStamp(self) -> int:
        """
        Getter for property: (int) TimeStamp
         Returns the date and time the violation was created or updated.  
          
                   The time stamp is number of seconds since the UNIX epoch (midnight GMT, 1 January 1970).
                   
         
        """
        pass
    @TimeStamp.setter
    def TimeStamp(self, time_stamp: int):
        """
        Setter for property: (int) TimeStamp
         Returns the date and time the violation was created or updated.  
          
                   The time stamp is number of seconds since the UNIX epoch (midnight GMT, 1 January 1970).
                   
         
        """
        pass
    def AddObjects(self, objects: List[DesignRuleViolation]) -> None:
        """
         Add an object in violation to the violation 
        """
        pass
    def AddViolationLocations(self, locationObjects: List[DesignRuleViolationLocation]) -> None:
        """
         This will add given number of violation location objects. 
        """
        pass
    def BlankLocationObjectsOfViolation(self, blank_option: DesignRuleViolation.BlankOption) -> None:
        """
         This function will blank location objects of given violation. 
        """
        pass
    def DeleteRuleOverride(self, deleteObject: DesignRuleOverride) -> None:
        """
         Override object will be deleted 
        """
        pass
    def GetLocations(self) -> List[DesignRuleViolationLocation]:
        """
         This will give all violation location objects stored in calling violation object. 
         Returns locationObjectList ( DesignRuleViolationLocation List[NXOp):  Array of NXOpen.Routing.DesignRuleViolationLocation object. .
        """
        pass
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Get the array of objects in violation 
         Returns objects ( NXOpen.NXObject Li):  Caller frees the array .
        """
        pass
    def GetOwningDesignRule(self) -> DesignRule:
        """
         Returns the Design Rule that owns this violation. 
         Returns owningDesignRule ( DesignRule NXOpen):  .
        """
        pass
    def IsRuleOverridden(self) -> bool:
        """
         Violation is overridden or not is inquired 
         Returns value (bool):   .
        """
        pass
    def RemoveViolationOverride(self) -> None:
        """
         Removes violation override from given violation object. 
        """
        pass
    def SetLocations(self, violationLocations: List[DesignRuleViolationLocation]) -> None:
        """
         Adds locations for violations of this design rule. 
        """
        pass
    def SetObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Sets the array of objects in violation 
        """
        pass
    def SetViolationOverride(self, user: str, reason: str, timestamp: int) -> None:
        """
         Sets the violation override 
        """
        pass
import NXOpen
class DesignRule(NXOpen.NXObject): 
    """ Represents NXOpen.Routing.DesignRule object """
    @property
    def Application(self) -> str:
        """
        Getter for property: (str) Application
         Returns the application to which this design rule belongs.  
             
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the description of this design rule.  
             
         
        """
        pass
    @property
    def Drname(self) -> str:
        """
        Getter for property: (str) Drname
         Returns the name of this design rule.  
             
         
        """
        pass
    def ClearViolationOnObject(self, objectToCheck: NXOpen.NXObject) -> None:
        """
         Finds the violation of this rule attached to the given object and deletes it.
                    Useful when the given object no longer violates this rule.
                    Call NXOpen.Update.DoUpdate after clearing violations. 
        """
        pass
    def CreateViolation(self, shortDescription: str, longDescription: str, objects: List[NXOpen.NXObject]) -> DesignRuleViolation:
        """
         Creates a new violation for this design rule. 
         Returns violation ( DesignRuleViolation NXOpen):   .
        """
        pass
    def GetViolations(self) -> List[DesignRuleViolation]:
        """
         Returns any violations recorded against this design rule. 
         Returns violations ( DesignRuleViolation List[NXOp): .
        """
        pass
class DeviceRelationship(ObjectRelationship): 
    """
         Represents a relationship between NXOpen.Routing.SingleDevice objects.
       
       
         ObjectRelationship is the abstract base class for NXOpen.Routing.InterfaceTerminalRelationshipBase
         and NXOpen.Routing.DeviceRelationship.
        
    """
    class RelationType(Enum):
        """
        Members Include: 
         |AssociatedEquipment|  the related single devices are attached to the relating single device 

        """
        AssociatedEquipment: int
        @staticmethod
        def ValueOf(value: int) -> DeviceRelationship.RelationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def RelationshipType(self) -> DeviceRelationship.RelationType:
        """
        Getter for property: ( DeviceRelationship.RelationType NXOpen) RelationshipType
         Returns  the type of the relationship.  
             
         
        """
        pass
    @RelationshipType.setter
    def RelationshipType(self, relationship_type: DeviceRelationship.RelationType):
        """
        Setter for property: ( DeviceRelationship.RelationType NXOpen) RelationshipType
         Returns  the type of the relationship.  
             
         
        """
        pass
    def AddRelatedSingleDevice(self, related_device: SingleDevice) -> None:
        """
         Adds a NXOpen.Routing.SingleDevice to the collection of related NXOpen.Routing.SingleDevice objects. 
        """
        pass
    def GetRelatedSingleDevices(self) -> List[SingleDevice]:
        """
         Returns the list of related NXOpen.Routing.SingleDevice objects.  The objects in the list are related to the relating NXOpen.Routing.SingleDevice object. 
         Returns related_devices ( SingleDevice List[NXOp):  Set of NXOpen.Routing.SingleDevice objects that are related to the Relating SingleDevice .
        """
        pass
    def GetRelatingSingleDevice(self) -> SingleDevice:
        """
          Returns the one NXOpen.Routing.SingleDevice to which the other NXOpen.Routing.SingleDevice objects are related. 
         Returns relating_device ( SingleDevice NXOpen):  .
        """
        pass
    def RemoveRelatedSingleDevice(self, related_device: SingleDevice) -> None:
        """
         Removes a NXOpen.Routing.SingleDevice from the collection of related NXOpen.Routing.SingleDevice objects. 
        """
        pass
    def ReplaceRelatedSingleDevices(self, related_devices: List[SingleDevice]) -> None:
        """
         Replaces the collection of related NXOpen.Routing.SingleDevice objects. 
        """
        pass
    def SetRelatingSingleDevice(self, relating_device: SingleDevice) -> None:
        """
         Sets the one Relating NXOpen.Routing.SingleDevice. 
        """
        pass
import NXOpen
class DiscontinuityCornerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.DiscontinuityCorner objects. """
    def AreSegmentsDisconnected(self, segment1: SplineSegment, segment2: SplineSegment, rcp: ControlPoint) -> bool:
        """
         Checks whether segment1 and segment2 are disconnected at a control point
                    due to a discontinuity corner. 
         Returns seg_disc (bool):  TRUE: If the two segments are disconnected. 
                                                          FALSE: Otherwise . .
        """
        pass
    def Create(self, rcp: ControlPoint, first_segment: ISegment, second_segment: ISegment) -> DiscontinuityCorner:
        """
         Creates a discontinuity corner object at the given 
                    NXOpen.Routing.ControlPoint.  There must be two input 
                    NXOpen.Routing.ISegment objects, and they both must
                    reference the input NXOpen.Routing.ControlPoint object.
                    
         Returns disc_crn ( DiscontinuityCorner NXOpen):  The new disc corner object. .
        """
        pass
    def GetDiscontinuityCorners(self, rcp: ControlPoint) -> List[DiscontinuityCorner]:
        """
         Return the discontinuity corners assigned to the input control point.  There
                    may be more than one discontinuity corner assigned to input control point.
                    This may occur for example when four segments form a cross, the control
                    point at the center may have two discontinuity corners assigned.  One corner
                    will force stock to split when crossing the horizontal segments, the 
                    other will cause stock to split when crossing the vertical segments. 
         Returns discs ( DiscontinuityCorner List[NXOp):  Corner objects pointing to the rcp. .
        """
        pass
class DiscontinuityCorner(Corner): 
    """ 
        A discontinuity corner is a corner that forces Routing.Stock objects
        to split as they cover the segments attached to the discontinuity corner.  
        The discontinuity specifies over which two segments (at a junction of 2 or more segments)
        that the break should occur.
     """
    @property
    def FirstSegment(self) -> ISegment:
        """
        Getter for property: ( ISegment NXOpen) FirstSegment
         Returns the first segment of a discontinuity corner, segment must be
                 attached to the  Routing::ControlPoint  that
                 defines this corner.  
              
         
        """
        pass
    @FirstSegment.setter
    def FirstSegment(self, segment: ISegment):
        """
        Setter for property: ( ISegment NXOpen) FirstSegment
         Returns the first segment of a discontinuity corner, segment must be
                 attached to the  Routing::ControlPoint  that
                 defines this corner.  
              
         
        """
        pass
    @property
    def SecondSegment(self) -> ISegment:
        """
        Getter for property: ( ISegment NXOpen) SecondSegment
         Returns the second segment of a discontinuity corner, segment must be
                 attached to the  Routing::ControlPoint  that
                 defines this corner.  
              
         
        """
        pass
    @SecondSegment.setter
    def SecondSegment(self, segment: ISegment):
        """
        Setter for property: ( ISegment NXOpen) SecondSegment
         Returns the second segment of a discontinuity corner, segment must be
                 attached to the  Routing::ControlPoint  that
                 defines this corner.  
              
         
        """
        pass
    def Remove(self) -> None:
        """
         Removes (deletes) the input discontinuity corner.
        """
        pass
import NXOpen
class DivisionsBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Routing.DivisionsBuilder

        Builder for creatingediting splits at an end of a duct.
        Takes an end face of a rectangular stock and splits it into a pair of
        divisions based on the specified absolute flow percentage for each division.
    """
    class SplitDirectionType(Enum):
        """
        Members Include: 
         |SplitVertically|  Creates a vertical split 
         |SplitHorizontally|  Creates a horizontal split 

        """
        SplitVertically: int
        SplitHorizontally: int
        @staticmethod
        def ValueOf(value: int) -> DivisionsBuilder.SplitDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LeftChildFlow(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LeftChildFlow
         Returns the value of percent absolute or relative flow in left (first) child division   
            
         
        """
        pass
    @property
    def RightChildFlow(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RightChildFlow
         Returns the value of percent absolute or relative flow in right (second) child division   
            
         
        """
        pass
    @property
    def SelectedPort(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectedPort
         Returns the  NXOpen::Routing::Port   to identify the cross-section that is to be split   
            
         
        """
        pass
    @property
    def SplitDirection(self) -> DivisionsBuilder.SplitDirectionType:
        """
        Getter for property: ( DivisionsBuilder.SplitDirectionType NXOpen) SplitDirection
         Returns the direction of split, either vertical or horizontal   
            
         
        """
        pass
    @SplitDirection.setter
    def SplitDirection(self, splitDirection: DivisionsBuilder.SplitDirectionType):
        """
        Setter for property: ( DivisionsBuilder.SplitDirectionType NXOpen) SplitDirection
         Returns the direction of split, either vertical or horizontal   
            
         
        """
        pass
    def CreateDivisions(self) -> Division:
        """
         Creates two new divisions by splitting the parent division. 
         Returns division ( Division NXOpen): .
        """
        pass
    def GetDivision(self) -> Division:
        """
         Gets the division object, if any, associated with the division builder 
         Returns division ( Division NXOpen): .
        """
        pass
import NXOpen
class Division(NXOpen.NXObject): 
    """ Represents NXOpen.Routing.Division """
    class SplitDirectionType(Enum):
        """
        Members Include: 
         |SplitVertically|  Creates a vertical split 
         |SplitHorizontally|  Creates a horizontal split 

        """
        SplitVertically: int
        SplitHorizontally: int
        @staticmethod
        def ValueOf(value: int) -> Division.SplitDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SplitDirection(self) -> Division.SplitDirectionType:
        """
        Getter for property: ( Division.SplitDirectionType NXOpen) SplitDirection
         Returns the direction of split, either vertical or horizontal   
            
         
        """
        pass
    @SplitDirection.setter
    def SplitDirection(self, splitDirection: Division.SplitDirectionType):
        """
        Setter for property: ( Division.SplitDirectionType NXOpen) SplitDirection
         Returns the direction of split, either vertical or horizontal   
            
         
        """
        pass
    def CreateSplitterCurve(self) -> None:
        """
         Creates splitting Curve. 
        """
        pass
    def DeleteAllChildren(self) -> None:
        """
         Deletes all children divisions of the input division and the splitter curves
                    that were used to create the children divisions. In case the input division
                    is the root division or the immediate child of the root division then the
                    root division and the boundary curves are also deleted. 
        """
        pass
    def UpdateFlow(self, leftChildFlow: float, rightChildFlow: float, isAbsoluteFlow: bool) -> None:
        """
         Update the Flow. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class DuctReinforcementBuilder(NXOpen.Builder): 
    """
        Builder for creatingediting duct reinforcements. Rules can be defined based on which the type of
        reinforcement to be placed on the input duct will be determined.
        See NXOpen.Routing.DuctReinforcement for Duct Reinforcement
        class documentation.
    """
    class ReinforcementTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Inside| 
         |Outside| 

        """
        NotSet: int
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> DuctReinforcementBuilder.ReinforcementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IntervalExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IntervalExpression
         Returns the distance between each set of reinforcement stocks going perpendicular to axis of the duct   
            
         
        """
        pass
    @property
    def MinimumClearance(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) MinimumClearance
         Returns the minimum clearance value for duct reinforcement
                    It defines the minimum distance from the beginning and end of the path to place the 
                    first and last piece of reinforcement stock.  
             
         
        """
        pass
    @property
    def NumberOfPairs(self) -> int:
        """
        Getter for property: (int) NumberOfPairs
         Returns the number of pairs of outside reinforcements going parallel to axis of the duct   
            
         
        """
        pass
    @NumberOfPairs.setter
    def NumberOfPairs(self, numberOfPairs: int):
        """
        Setter for property: (int) NumberOfPairs
         Returns the number of pairs of outside reinforcements going parallel to axis of the duct   
            
         
        """
        pass
    @property
    def ParallelReinforcement(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) ParallelReinforcement
         Returns the stock settings for parallel reinforcements   
            
         
        """
        pass
    @ParallelReinforcement.setter
    def ParallelReinforcement(self, parallelStockBuilder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) ParallelReinforcement
         Returns the stock settings for parallel reinforcements   
            
         
        """
        pass
    @property
    def ParentDuct(self) -> SelectStock:
        """
        Getter for property: ( SelectStock NXOpen) ParentDuct
         Returns the duct that is to be reinforced.  
             
         
        """
        pass
    @property
    def PathCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) PathCurve
         Returns the path curve that is used to specify perpendicular reinforcement defining points.  
            
         
        """
        pass
    @property
    def PerpendicularReinforcement(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) PerpendicularReinforcement
         Returns the stock settings for perpendicular reinforcements   
            
         
        """
        pass
    @PerpendicularReinforcement.setter
    def PerpendicularReinforcement(self, perpendicularStockBuilder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) PerpendicularReinforcement
         Returns the stock settings for perpendicular reinforcements   
            
         
        """
        pass
    @property
    def ReinforcementType(self) -> DuctReinforcementBuilder.ReinforcementTypes:
        """
        Getter for property: ( DuctReinforcementBuilder.ReinforcementTypes NXOpen) ReinforcementType
         Returns the type of reinforcement   
            
         
        """
        pass
    @ReinforcementType.setter
    def ReinforcementType(self, reinforcementType: DuctReinforcementBuilder.ReinforcementTypes):
        """
        Setter for property: ( DuctReinforcementBuilder.ReinforcementTypes NXOpen) ReinforcementType
         Returns the type of reinforcement   
            
         
        """
        pass
    @property
    def SpacingExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpacingExpression
         Returns the distance between each pair of reinforcement   
            
         
        """
        pass
    def UpdatePathCurve(self) -> None:
        """
         The path curve that is used to specify perpendicular reinforcement defining points.
        """
        pass
import NXOpen.Features
class DuctReinforcement(NXOpen.Features.BodyFeature): 
    """ Represents a Duct Reinforcement feature used for creatingediting reinforcements 
        on the inside or outside of rectangular HVAC ducts.
        Use the NXOpen.Routing.DuctReinforcementBuilder class to create a Duct Reinforcement feature. """
    pass
import NXOpen
class DuctSizeCalculatorBuilder(NXOpen.Builder): 
    """ Builder to perform calculations of the duct which is to be used in the HVAC applications. The duct has some flow attributes and has dimentions."""
    class DuctShapeType(Enum):
        """
        Members Include: 
         |Rectangular| 
         |Circular| 
         |FlatOval| 

        """
        Rectangular: int
        Circular: int
        FlatOval: int
        @staticmethod
        def ValueOf(value: int) -> DuctSizeCalculatorBuilder.DuctShapeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DuctAreaExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DuctAreaExp
         Returns the duct area   
            
         
        """
        pass
    @property
    def DuctAspectRatioExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DuctAspectRatioExp
         Returns the Aspect ratio of the duct dimentions   
            
         
        """
        pass
    @property
    def DuctDiameterExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DuctDiameterExp
         Returns the duct diameter   
            
         
        """
        pass
    @property
    def DuctEqvalentDiameterExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DuctEqvalentDiameterExp
         Returns the duct equivalent diameter   
            
         
        """
        pass
    @property
    def DuctHeightExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DuctHeightExp
         Returns the duct height   
            
         
        """
        pass
    @property
    def DuctShape(self) -> DuctSizeCalculatorBuilder.DuctShapeType:
        """
        Getter for property: ( DuctSizeCalculatorBuilder.DuctShapeType NXOpen) DuctShape
         Returns the shape of the duct   
            
         
        """
        pass
    @DuctShape.setter
    def DuctShape(self, ductShape: DuctSizeCalculatorBuilder.DuctShapeType):
        """
        Setter for property: ( DuctSizeCalculatorBuilder.DuctShapeType NXOpen) DuctShape
         Returns the shape of the duct   
            
         
        """
        pass
    @property
    def DuctWidthExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DuctWidthExp
         Returns the duct width   
            
         
        """
        pass
    @property
    def IsCreateSpaceReservationEnabled(self) -> bool:
        """
        Getter for property: (bool) IsCreateSpaceReservationEnabled
         Returns the status of the create space reservation toggle; whether the toggle is on  or off.  
             
         
        """
        pass
    @IsCreateSpaceReservationEnabled.setter
    def IsCreateSpaceReservationEnabled(self, isCreateSpaceReservation: bool):
        """
        Setter for property: (bool) IsCreateSpaceReservationEnabled
         Returns the status of the create space reservation toggle; whether the toggle is on  or off.  
             
         
        """
        pass
    @property
    def IsDisplayFlowParamsEnabled(self) -> bool:
        """
        Getter for property: (bool) IsDisplayFlowParamsEnabled
         Returns the ON or OFF status of the Display flow parameters over Segments toggle   
            
         
        """
        pass
    @IsDisplayFlowParamsEnabled.setter
    def IsDisplayFlowParamsEnabled(self, isDispFlowParams: bool):
        """
        Setter for property: (bool) IsDisplayFlowParamsEnabled
         Returns the ON or OFF status of the Display flow parameters over Segments toggle   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteObjectCollector
         Returns the route object collector  Stores the routing segments for which calculations are to be done   
            
         
        """
        pass
    @property
    def VelocityExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VelocityExp
         Returns the velocity component Flow parameter for the duct.  
            
         
        """
        pass
    @property
    def VolumeFlowRateExp(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VolumeFlowRateExp
         Returns the volume flow rate associated with the duct.  
           This is a flow parameter   
         
        """
        pass
class Eccentric(Enum):
    """
    Members Include: 
     |NotEccentricSeg|  Is not a eccentric segment 
     |EccentricSeg|  Is a eccentric segment 

    """
    NotEccentricSeg: int
    EccentricSeg: int
    @staticmethod
    def ValueOf(value: int) -> Eccentric:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class EditBendAngleBuilder(NXOpen.Builder): 
    """ 
    """
    def CommitCurrentEdit(self) -> None:
        """
         Commits the current edit operation. 
        """
        pass
    def GetSelectedBendData(self) -> Tuple[float, NXOpen.Vector3d, NXOpen.Point3d, NXOpen.Vector3d]:
        """
         Returns information about the angle being changed. 
         Returns A tuple consisting of (angle, anchorSegDir, rcpPos, planeNormal). 
         - angle is: float. Teh angle between the two segments .
         - anchorSegDir is:  NXOpen.Vector3d. The anchor Segment .
         - rcpPos is:  NXOpen.Point3d. The position of the bend rcp .
         - planeNormal is:  NXOpen.Vector3d. The normal of the plane the arc lies in. .

        """
        pass
    def SetMoveAttachedFlag(self, moveAttached: bool) -> None:
        """
         Move all attached geometry as a rigid set. 
        """
        pass
    def SetRCP(self, bendRcp: NXOpen.TaggedObject) -> None:
        """
         Set the Bend RCP to edit. 
        """
        pass
    def SwapAnchorSegment(self) -> None:
        """
         Swap the free and anchor segments. 
        """
        pass
    def UpdateAngle(self, angle: float) -> None:
        """
         Set the vector the defines the new bend angle. 
        """
        pass
import NXOpen
class EditCharacteristicsBuilder(NXOpen.Builder): 
    """ Builder to edit required and optional characteristics of Routing.Stock
        or Assemblies.Component as defined in the application view file. """
    @property
    def ReferenceObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ReferenceObject
         Returns the reference object to obtain the characteristic values   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteObjectCollector
         Returns the routing objects to edit characteristics.  
           The objects should be either 
                     Routing::Stock  or  Assemblies::Component    
         
        """
        pass
    @property
    def RoutingLevel(self) -> str:
        """
        Getter for property: (str) RoutingLevel
         Returns the Routing Level associated with selected objects.  
             
         
        """
        pass
    @RoutingLevel.setter
    def RoutingLevel(self, routeLevel: str):
        """
        Setter for property: (str) RoutingLevel
         Returns the Routing Level associated with selected objects.  
             
         
        """
        pass
    def ApplyReferenceObjectCharx(self, refObject: NXOpen.NXObject) -> None:
        """
         Apply characteristics of the reference object to the selected objects. 
        """
        pass
    def ClearValues(self) -> None:
        """
         Clear the characteristic values of the selected objects. 
        """
        pass
    def GetOptionalCharacteristicsToEdit(self) -> CharacteristicList:
        """
         Returns the editable Routing.CharacteristicList 
                    that contains optional characteristics common to all the selected objects. 
         Returns charxToEdit ( CharacteristicList NXOpen): The characteristics to edit.
        """
        pass
    def GetRequiredCharacteristicsToEdit(self) -> CharacteristicList:
        """
         Returns the editable Routing.CharacteristicList 
                    that contains required characteristics common to all the selected objects. 
         Returns charxToEdit ( CharacteristicList NXOpen): The characteristics to edit.
        """
        pass
    def ResetValues(self) -> None:
        """
         Reset the characteristic values of the selected objects. 
        """
        pass
import NXOpen
class EditLineSegmentBuilder(NXOpen.Builder): 
    """ 
        Builder for the "Edit Line Segment" operation.  Sets (and locks or unlocks)
        the length of NXOpen.Routing.LineSegment objects.  Also moves geometry
        attached to the line segment to ensure that the attached geometry has the correct
        shape after an edit. 
    """
    @property
    def ConvertEccentricSegment(self) -> bool:
        """
        Getter for property: (bool) ConvertEccentricSegment
         Returns the conversion flag.  
            Forces the commit method to convert line segment to eccentric line segment if set to true.  Otherwise 
                 convert it to vice versa   
         
        """
        pass
    @ConvertEccentricSegment.setter
    def ConvertEccentricSegment(self, convertEccentricSegment: bool):
        """
        Setter for property: (bool) ConvertEccentricSegment
         Returns the conversion flag.  
            Forces the commit method to convert line segment to eccentric line segment if set to true.  Otherwise 
                 convert it to vice versa   
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length expression.  
            This data from this expression is copied to (or from)
                    the distance constraint applied to the ends of the line segment.    
         
        """
        pass
    @property
    def LineSelection(self) -> SelectLineSegment:
        """
        Getter for property: ( SelectLineSegment NXOpen) LineSelection
         Returns the line selection.  
            Stores the line segment selected by the user.   
         
        """
        pass
    @property
    def LockLength(self) -> bool:
        """
        Getter for property: (bool) LockLength
         Returns the lock length flag.  
            Forces the commit method to lock the length to the 
                    specified value if set to true.  Otherwise the length of the line segment 
                    is unconstrained after the commit method is invoked.   
         
        """
        pass
    @LockLength.setter
    def LockLength(self, lockLength: bool):
        """
        Setter for property: (bool) LockLength
         Returns the lock length flag.  
            Forces the commit method to lock the length to the 
                    specified value if set to true.  Otherwise the length of the line segment 
                    is unconstrained after the commit method is invoked.   
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction flag.  
            Flips the direction that the extends towards (or
                    shrinks along).  This flips the origin of the line as well as the direction.   
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverse: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction flag.  
            Flips the direction that the extends towards (or
                    shrinks along).  This flips the origin of the line as well as the direction.   
         
        """
        pass
    def AddLineToSetOfAllEditedSegments(self) -> None:
        """
         Adds the current line segment to the set of all line segments that have been edited
                    by the user. 
        """
        pass
    def DetachActiveRcp(self) -> None:
        """
         Detaches the line segment, stored in builder, at its active end RCP.
                    By reversing the direction of line segment, user could make other end RCP as active 
                    RCP. 
        """
        pass
    def DragLineLength(self) -> None:
        """
         Updates the line length based on the expression stored in this builder.  The line is
                    not fully updated only partially updated (i.e. solid bodies build on the line do not
                    update).    This method assumes the difference between the new length value and the
                    previous length value is very small (e.g. a drag operation). 
        """
        pass
    def GetActiveRcpPositon(self) -> NXOpen.Point3d:
        """
         Determines the active RCP for the line selected by the user.
                    This is end RCP other than the start point of line segment.
                    This RCP could be dragged along the segment.
         Returns activeRcpPosition ( NXOpen.Point3d):  End point other
                                                                                          than the start point 
                                                                                          of line segment. .
        """
        pass
    def GetOrientation(self) -> Tuple[bool, NXOpen.Point3d, NXOpen.Vector3d]:
        """
         Determines the orientation information for the line selected by the user.  Returns
                    false if there is no line currently stored in the builder.  
         Returns A tuple consisting of (is_valid, start_point, direction). 
         - is_valid is: bool. True if there
                                                                                            is a line 
                                                                                            associated with
                                                                                            this builder. .
         - start_point is:  NXOpen.Point3d. The start 
                                                                                        of the line. .
         - direction is:  NXOpen.Vector3d. The direction 
                                                                                        of the line 
                                                                                        (unit vector).

        """
        pass
    def InitializeFromLine(self, line: LineSegment) -> None:
        """
         Initializes (or resets) the builder based off of the input line segment.  
        """
        pass
    def ModifiedLineLength(self) -> None:
        """
         Updates the line length based on the expression stored in this builder.  The line is
                    not fully updated only partially updated (i.e. solid bodies build on the line do not
                    update).   This method doesn't assume anything about the new value.  This method
                    updates the line incrementally from the original length to the new length
                    as this usually results in better looking geometry. 
        """
        pass
    def RestartDrag(self) -> None:
        """
         Restart a line drag operation. This routine should only be called if 
                NXOpen.Routing.EditLineSegmentBuilder.StopDrag. was previously
                called to stop a line drag operation. 
        """
        pass
    def StopDrag(self) -> None:
        """
         Stop the drag operation if it has begun. This will commit the drag and update the assembly.
                    This will not remove the segment from the builder and dragging can be restarted by calling
                    NXOpen.Routing.EditLineSegmentBuilder.RestartDrag. 
        """
        pass
import NXOpen
class EditPlacePartBuilder(NXOpen.Builder): 
    """ 
    """
    @property
    def SelectedPart(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectedPart
         Returns the target body to edit part placement   
            
         
        """
        pass
    def FinalizePlacementForScrewSeat(self, startPointId: NXOpen.TaggedObject, endPointId: NXOpen.TaggedObject, alignStartPoint: NXOpen.Point3d, alignEndPoint: NXOpen.Point3d, length: NXOpen.Expression, angle: NXOpen.Expression, alignVector: NXOpen.Vector3d, screwSeatInstance: NXOpen.TaggedObject, target: NXOpen.TaggedObject) -> None:
        """
         Places a screw measurement holder seat part onto a target object by locating and constraining by the given parameters. 
        """
        pass
    def GetScrewSeatAngle(self) -> NXOpen.Expression:
        """
         Gets the angle expression to be used for screw seat placement along a placed object. 
         Returns angleExp ( NXOpen.Expression):  The angle used for screw seat placement on placed routing object. .
        """
        pass
    def GetScrewSeatLength(self) -> NXOpen.Expression:
        """
         Gets the length expression to be used for screw seat placement along a placed object. 
         Returns lengthExp ( NXOpen.Expression):  The length used for screw seat placement on placed routing object. .
        """
        pass
import NXOpen
class ElbowSnapSettings(NXOpen.Builder): 
    """ Helper object used the by NXOpen.Routing.LinearPathBuilder builder. 
        Determines whether or not elbow snapping should occur in the "Create Linear Path"
        UI, and if so, what the angle tolerance should be.
    """
    @property
    def AngleTolerance(self) -> float:
        """
        Getter for property: (float) AngleTolerance
         Returns the tolerance within which to search for elbow angles.  
             
         
        """
        pass
    @AngleTolerance.setter
    def AngleTolerance(self, tolerance: float):
        """
        Setter for property: (float) AngleTolerance
         Returns the tolerance within which to search for elbow angles.  
             
         
        """
        pass
    @property
    def SnapToElbowAngles(self) -> bool:
        """
        Getter for property: (bool) SnapToElbowAngles
         Returns whether or not to snap control points to the nearest valid elbow angle.  
             
         
        """
        pass
    @SnapToElbowAngles.setter
    def SnapToElbowAngles(self, do_snap: bool):
        """
        Setter for property: (bool) SnapToElbowAngles
         Returns whether or not to snap control points to the nearest valid elbow angle.  
             
         
        """
        pass
import NXOpen
class EndFormBuilder(NXOpen.Builder): 
    """ Builder for creating End Form.
        Create Stock: Takes a set of segments or stocks and places the selected endform
        to the end of of it. 
    """
    @property
    def RouteControlPointList(self) -> RouteObjectCollectorList:
        """
        Getter for property: ( RouteObjectCollectorList NXOpen) RouteControlPointList
         Returns the RouteControlPoint list   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteObjectCollector
         Returns the route object collector for placing end form   
            
         
        """
        pass
    def CreateRouteControlPointListItem(self) -> RouteObjectCollector:
        """
         Create a RouteControlPoint list item. 
         Returns listitem ( RouteObjectCollector NXOpen): .
        """
        pass
    def EditEndForm(self) -> None:
        """
         Edit EndForm 
        """
        pass
    def PlaceEndForm(self) -> None:
        """
         Place EndForm 
        """
        pass
    def RemoveEndForm(self) -> None:
        """
         Remove EndForm 
        """
        pass
    def SpecifyEndForm(self, jaCharx: CharacteristicList) -> None:
        """
         Specify EndForm 
        """
        pass
import NXOpen
class ExtractPort(Port): 
    """ Routing ExtractPort object is an extract of Port class """
    def GetPrototypePort(self) -> Port:
        """
         Retrieves the prototype of the extract port.
         Returns prototype ( Port NXOpen):  Prototype port from which the extract port was created.
        """
        pass
    def GetStockOffsetPoint(self) -> NXOpen.Point:
        """
         Retrieves the stock offset point. Stock offset point exists only if
                    ExtractPort is a stock offset port If the source of an extracted port
                    is loaded, but other objects from the source part are not loaded -
                    routine loads all objects of required classes from the source part.
         Returns sop ( NXOpen.Point):  Stock offset Point if it exists .
        """
        pass
import NXOpen.Features
class FeaturePort(NXOpen.Features.Feature): 
    """ NXOpen.Routing.FeaturePort is a NXOpen.Features.Feature associated
        with NXOpen.Routing.Port. """
    pass
import NXOpen
class FillerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Stock objects.  """
    def CreateStock(self, stock_data: StockData, anchor: Anchor, cross_section: CrossSection, segments: List[ISegment]) -> List[Stock]:
        """
         Creates a NXOpen.Routing.Filler stock object. 
         Returns stocks ( Stock List[NXOp):  The resulting array of newly created NXOpen.Routing.Stock
                                                    objects. .
        """
        pass
import NXOpen
class FillerStockBuilder(NXOpen.Builder): 
    """ Creates Filler stock on selected Segments. """
    @property
    def RemoveExistingStock(self) -> bool:
        """
        Getter for property: (bool) RemoveExistingStock
         Returns the remove existing stock flag.  
           If set to TRUE the existing stock
                    on the path will be removed when assigning new stock.  
         
        """
        pass
    @RemoveExistingStock.setter
    def RemoveExistingStock(self, removeStock: bool):
        """
        Setter for property: (bool) RemoveExistingStock
         Returns the remove existing stock flag.  
           If set to TRUE the existing stock
                    on the path will be removed when assigning new stock.  
         
        """
        pass
    @property
    def RouteSelection(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteSelection
         Returns the route selection which allows selection of routing objects  
            
         
        """
        pass
    @property
    def StockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for creating filler stock.  
             
         
        """
        pass
    @StockSettings.setter
    def StockSettings(self, stockBuilder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for creating filler stock.  
             
         
        """
        pass
class Filler(Stock): 
    """ Represents a Filler """
    pass
import NXOpen
class FindByAttributesBuilder(NXOpen.Builder): 
    """ Find runsobjects with specified attribute name and attribute value criteria,
        highlight the corresponding nodes in the run navigator and the graphics area"""
    @property
    def AttribList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) AttribList
         Returnsthe attribute list containing search criteria  
            
         
        """
        pass
    @property
    def AttributeName(self) -> str:
        """
        Getter for property: (str) AttributeName
         Returnsthe string containing attribute title to search for  
            
         
        """
        pass
    @AttributeName.setter
    def AttributeName(self, attributeName: str):
        """
        Setter for property: (str) AttributeName
         Returnsthe string containing attribute title to search for  
            
         
        """
        pass
    @property
    def AttributeValue(self) -> str:
        """
        Getter for property: (str) AttributeValue
         Returnsthe string containing attribute value to search for  
            
         
        """
        pass
    @AttributeValue.setter
    def AttributeValue(self, attributeValue: str):
        """
        Setter for property: (str) AttributeValue
         Returnsthe string containing attribute value to search for  
            
         
        """
        pass
    def AttributeMembersBuilder(self) -> AttributeMembersBuilder:
        """
         Creates an AttributeMembersBuilder object used to create list item
         Returns builder ( AttributeMembersBuilder NXOpen):  .
        """
        pass
    def HighlightRunNavItems(self, objects: List[NXOpen.NXObject], highLight: bool) -> None:
        """
         HighlightUnhighlight the search results for FindByAttributes
        """
        pass
import NXOpen
import NXOpen.Assemblies
class FittingOverstockBuilder(NXOpen.Builder): 
    """ Builder for creating or editing NXOpen.Routing.FittingOverstock objects. """
    class TrimMethod(Enum):
        """
        Members Include: 
         |TrimPlane|  Single Trim Plane 
         |BetweenPlanes|  Double Trim Planes 

        """
        TrimPlane: int
        BetweenPlanes: int
        @staticmethod
        def ValueOf(value: int) -> FittingOverstockBuilder.TrimMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |EntirePart|  Entire Part 
         |EntireFace|  Entire Face 
         |PartialFace|  Partial Face 

        """
        EntirePart: int
        EntireFace: int
        PartialFace: int
        @staticmethod
        def ValueOf(value: int) -> FittingOverstockBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FaceTrimMethod(self) -> FittingOverstockBuilder.TrimMethod:
        """
        Getter for property: ( FittingOverstockBuilder.TrimMethod NXOpen) FaceTrimMethod
         Returns the  NXOpen::Routing::FittingOverstockBuilder::TrimMethod   
            
         
        """
        pass
    @FaceTrimMethod.setter
    def FaceTrimMethod(self, faceTrimMethod: FittingOverstockBuilder.TrimMethod):
        """
        Setter for property: ( FittingOverstockBuilder.TrimMethod NXOpen) FaceTrimMethod
         Returns the  NXOpen::Routing::FittingOverstockBuilder::TrimMethod   
            
         
        """
        pass
    @property
    def Faces(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) Faces
         Returns the faces to apply overstock to.  
            
         
        """
        pass
    @property
    def FirstPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) FirstPlane
         Returns the first trimming plane   
            
         
        """
        pass
    @FirstPlane.setter
    def FirstPlane(self, firstPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) FirstPlane
         Returns the first trimming plane   
            
         
        """
        pass
    @property
    def OverstockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) OverstockSettings
         Returns the stock settings for overstock assignment.  
             
         
        """
        pass
    @OverstockSettings.setter
    def OverstockSettings(self, stockBuilder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) OverstockSettings
         Returns the stock settings for overstock assignment.  
             
         
        """
        pass
    @property
    def RoutingParts(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) RoutingParts
         Returns the qualifed routing parts to apply overstock to.  
             
         
        """
        pass
    @property
    def SecondPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SecondPlane
         Returns the second trimming plane   
            
         
        """
        pass
    @SecondPlane.setter
    def SecondPlane(self, secondPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SecondPlane
         Returns the second trimming plane   
            
         
        """
        pass
    @property
    def Type(self) -> FittingOverstockBuilder.Types:
        """
        Getter for property: ( FittingOverstockBuilder.Types NXOpen) Type
         Returns the type  
            
         
        """
        pass
    @Type.setter
    def Type(self, type: FittingOverstockBuilder.Types):
        """
        Setter for property: ( FittingOverstockBuilder.Types NXOpen) Type
         Returns the type  
            
         
        """
        pass
import NXOpen
class FittingOverstockCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.FittingOverstock objects. """
    pass
import NXOpen
import NXOpen.Assemblies
class FittingOverstock(NXOpen.NXObject): 
    """ The NXOpen.Routing.FittingOverstock object represents overstock
        applied over the faces of the routing parts."""
    def GetComponent(self) -> NXOpen.Assemblies.Component:
        """
         Returns the NXOpen.Assemblies.Component created and controlled by the fitting overstock for a
                   fitting overstock as Components stock.  Only returns a component if the fitting overstock type is
                   Routing.StockUse.StockAsComponent. 
         Returns component ( NXOpen.Assemblies.Component): .
        """
        pass
    def GetStockData(self) -> StockData:
        """
         Gets the NXOpen.Routing.StockData. 
         Returns stockData ( StockData NXOpen):  .
        """
        pass
    def RenameFittingOverstockComponent(self, partName: str) -> None:
        """
         Renames the FittingOverstock component part with given name
        """
        pass
import NXOpen
class FittingPortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.FittingPort objects. """
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float) -> FittingPort:
        """
         Creates a FittingPort with a rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d) -> FittingPort:
        """
         Creates a FittingPort with no rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, axis: NXOpen.Axis, allowMultipleConnections: bool) -> FittingPort:
        """
         Creates a FittingPort with a rotation vector on an axis 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, derivationObject: NXOpen.Axis, allowMultipleConnections: bool) -> FittingPort:
        """
         Creates a FittingPort with no rotation vector on an axis 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, point: NXOpen.Point) -> FittingPort:
        """
         Creates a FittingPort with a rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, point: NXOpen.Point) -> FittingPort:
        """
         Creates a FittingPort with no rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, axis: NXOpen.Axis) -> FittingPort:
        """
         Creates a FittingPort with a rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, derivationObject: NXOpen.Axis) -> FittingPort:
        """
         Creates a FittingPort with no rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, allowMultipleConnections: bool) -> FittingPort:
        """
         Creates a FittingPort with a rotation vector at an absolute location 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, allowMultipleConnections: bool) -> FittingPort:
        """
         Creates a FittingPort with no rotation vector at an absolute location 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, point: NXOpen.Point, allowMultipleConnections: bool) -> FittingPort:
        """
         Creates a FittingPort with a rotation vector at a point 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    @overload
    def CreateFittingPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, point: NXOpen.Point, allowMultipleConnections: bool) -> FittingPort:
        """
         Creates a FittingPort with no rotation vector at a point 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    def CreateFromAxis(self, axis: NXOpen.Axis) -> FittingPort:
        """
         Creates a fitting port based on an existing axis. 
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
    def CreateFromCsys(self, csys: NXOpen.CartesianCoordinateSystem, createRotationVector: Port.CreateRotationVector) -> FittingPort:
        """
         Creates a fitting port based on an existing Cartesian Coordinate System.
                    The port aligns with the Z axis of the Coordinate System. The port's rotation vector, if any,
                    aligns with the Y direction of the Coordinate System.
                
         Returns fittingPort ( FittingPort NXOpen):  .
        """
        pass
import NXOpen
class FittingPort(Port): 
    """ Represents a Routing Fitting Port ObjectNXOpen.Routing.FittingPort.
        These objects are ones to which segments are routed to or from when
        creating a routing path.
      """
    @property
    def Axis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @Axis.setter
    def Axis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @property
    def CutbackLengthObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @CutbackLengthObject.setter
    def CutbackLengthObject(self, cutback_length: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @property
    def EngagementObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @EngagementObject.setter
    def EngagementObject(self, engagement: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @property
    def ForwardExtensionObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @ForwardExtensionObject.setter
    def ForwardExtensionObject(self, forward_extension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
import NXOpen
class FixturePortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.FixturePort objects. """
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float) -> FixturePort:
        """
         Creates a FixturePort with a rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d) -> FixturePort:
        """
         Creates a FixturePort with no rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, axis: NXOpen.Axis, allowMultipleConnections: bool) -> FixturePort:
        """
         Creates a FixturePort with a rotation vector on an axis 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, derivationObject: NXOpen.Axis, allowMultipleConnections: bool) -> FixturePort:
        """
         Creates a FixturePort with no rotation vector on an axis 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, point: NXOpen.Point) -> FixturePort:
        """
         Creates a FixturePort with a rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, point: NXOpen.Point) -> FixturePort:
        """
         Creates a FixturePort with no rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, axis: NXOpen.Axis) -> FixturePort:
        """
         Creates a FixturePort with a rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, derivationObject: NXOpen.Axis) -> FixturePort:
        """
         Creates a FixturePort with no rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, allowMultipleConnections: bool) -> FixturePort:
        """
         Creates a FixturePort with a rotation vector at an absolute location 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, allowMultipleConnections: bool) -> FixturePort:
        """
         Creates a FixturePort with no rotation vector at an absolute location 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, point: NXOpen.Point, allowMultipleConnections: bool) -> FixturePort:
        """
         Creates a FixturePort with a rotation vector at a point 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    @overload
    def CreateFixturePort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, point: NXOpen.Point, allowMultipleConnections: bool) -> FixturePort:
        """
         Creates a FixturePort with no rotation vector at a point 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    def CreateFromAxis(self, axis: NXOpen.Axis) -> FixturePort:
        """
         Creates a fixture port based on an existing axis. 
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
    def CreateFromCsys(self, csys: NXOpen.CartesianCoordinateSystem, createRotationVector: Port.CreateRotationVector) -> FixturePort:
        """
         Creates a fixture port based on an existing Cartesian Coordinate System.
                    The port aligns with the Z axis of the Coordinate System. The port's rotation vector, if any,
                    aligns with the Y direction of the Coordinate System.
                
         Returns fixturePort ( FixturePort NXOpen):  .
        """
        pass
import NXOpen
class FixturePort(Port): 
    """  NXOpen.Routing.FixturePort objects are objects that
      segments are routed through when creating a routing path. """
    @property
    def Axis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @Axis.setter
    def Axis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @property
    def CutbackLengthObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @CutbackLengthObject.setter
    def CutbackLengthObject(self, cutback_length: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @property
    def EngagementObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @EngagementObject.setter
    def EngagementObject(self, engagement: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @property
    def ForwardExtensionObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @ForwardExtensionObject.setter
    def ForwardExtensionObject(self, forward_extension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
class Flip(Enum):
    """
    Members Include: 
     |NotFlipped|   Profile is not flipped. 
     |Flipped|   Profile is flipped. 

    """
    NotFlipped: int
    Flipped: int
    @staticmethod
    def ValueOf(value: int) -> Flip:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class FormboardPlacementCoordinateSystemBuilder(NXOpen.Builder): 
    """ Builder for CreatingEditing the Formboard Placement Coordinate Systems."""
    class Method(Enum):
        """
        Members Include: 
         |Specify|  Specify Csys. 
         |Select|  Select Csys. 

        """
        Specify: int
        Select: int
        @staticmethod
        def ValueOf(value: int) -> FormboardPlacementCoordinateSystemBuilder.Method:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def QualifyMethod(self) -> FormboardPlacementCoordinateSystemBuilder.Method:
        """
        Getter for property: ( FormboardPlacementCoordinateSystemBuilder.Method NXOpen) QualifyMethod
         Returns the Qualify Method enum   
            
         
        """
        pass
    @QualifyMethod.setter
    def QualifyMethod(self, qualifyGroup: FormboardPlacementCoordinateSystemBuilder.Method):
        """
        Setter for property: ( FormboardPlacementCoordinateSystemBuilder.Method NXOpen) QualifyMethod
         Returns the Qualify Method enum   
            
         
        """
        pass
    @property
    def SelectedCSYS(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedCSYS
         Returns the selected csys   
            
         
        """
        pass
    @property
    def SpecifiedCSYS(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) SpecifiedCSYS
         Returns the specified csys   
            
         
        """
        pass
    @SpecifiedCSYS.setter
    def SpecifiedCSYS(self, specifiedCSYS: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) SpecifiedCSYS
         Returns the specified csys   
            
         
        """
        pass
import NXOpen
class GapArcSegment(NXOpen.Arc): 
    """ Represents a gap arc segment. """
    @property
    def FollowCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) FollowCurve
         Returns  the segment follow curve.  
            NULL object indicates segment has no follow curve   
         
        """
        pass
    @property
    def Guid(self) -> str:
        """
        Getter for property: (str) Guid
         Returns the Globally Unique Identifier (GUID) for this segment.  
             
         
        """
        pass
    @property
    def IsArcOpensDown(self) -> bool:
        """
        Getter for property: (bool) IsArcOpensDown
         Returns the arc orientation.  
           If true, arc opens downwards false, arc opens upwards   
         
        """
        pass
    @IsArcOpensDown.setter
    def IsArcOpensDown(self, arcOpensDown: bool):
        """
        Setter for property: (bool) IsArcOpensDown
         Returns the arc orientation.  
           If true, arc opens downwards false, arc opens upwards   
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns  the length of the segment.  
             
         
        """
        pass
import NXOpen
class GapDisplayBuilder(NXOpen.Builder): 
    """ Builder for creating a gap arc object on a line segment. """
    def CreateBuilder(self, selLine: NXOpen.Line, crossLine: NXOpen.Line, gapWidth: float, gapStartPoint: NXOpen.Point3d, gapEndPoint: NXOpen.Point3d, bridgeOverGap: bool, arcOrientation: bool) -> None:
        """
         Takes selected line, gap start and end points, and gap 
                type settings in to initialise builder data.
        """
        pass
    def SetBuilderData(self, selLine: NXOpen.Line, crossLine: NXOpen.Line, gapWidth: float, gapStartPoint: NXOpen.Point3d, gapEndPoint: NXOpen.Point3d, bridgeOverGap: bool, arcOrientation: bool) -> None:
        """
         Takes selected line, gap start and end points, and gap 
                type settings in to set builder data.
        """
        pass
import NXOpen
class HandrailBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Routing.HandrailBuilder
        Creates a handrail from a selected point. The handrail is created by
        optionally placing a post depending on the post type followed by placing
        the rails across the route control points corresponding to the posts.
    """
    class PostTypes(Enum):
        """
        Members Include: 
         |Start| 
         |Intermediate| 
         |NotSet| 
         |End| 

        """
        Start: int
        Intermediate: int
        NotSet: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> HandrailBuilder.PostTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoCloseOption(self) -> bool:
        """
        Getter for property: (bool) AutoCloseOption
         Returns an option to automatically close the handrail   
            
         
        """
        pass
    @AutoCloseOption.setter
    def AutoCloseOption(self, autoClose: bool):
        """
        Setter for property: (bool) AutoCloseOption
         Returns an option to automatically close the handrail   
            
         
        """
        pass
    @property
    def HasHorizontalRails(self) -> bool:
        """
        Getter for property: (bool) HasHorizontalRails
         Returns an option to create horizontal rail stock   
            
         
        """
        pass
    @HasHorizontalRails.setter
    def HasHorizontalRails(self, railOption: bool):
        """
        Setter for property: (bool) HasHorizontalRails
         Returns an option to create horizontal rail stock   
            
         
        """
        pass
    @property
    def PostType(self) -> HandrailBuilder.PostTypes:
        """
        Getter for property: ( HandrailBuilder.PostTypes NXOpen) PostType
         Returns the type of post: Start, Intermediate, None, End   
            
         
        """
        pass
    @PostType.setter
    def PostType(self, postType: HandrailBuilder.PostTypes):
        """
        Setter for property: ( HandrailBuilder.PostTypes NXOpen) PostType
         Returns the type of post: Start, Intermediate, None, End   
            
         
        """
        pass
    def PlaceHandrail(self, postLocation: NXOpen.Point3d) -> None:
        """
         Creates a handrail post, horizontal railings assembly components and places them in the appropriate orientation. 
        """
        pass
    def ReverseLastPost(self) -> None:
        """
         Reverses the orientation of the last placed post 
        """
        pass
    def SetHandrailPartCharx(self, partCharx: CharacteristicList) -> None:
        """
         Sets the handrail part characteristics 
        """
        pass
class HealMethod(Enum):
    """
    Members Include: 
     |Direct|  
     |Intersect|  
     |Xyz|  
     |Xzy|  
     |Yxz|  
     |Yzx|  
     |Zxy|  
     |Zyx|  
     |Max|  

    """
    Direct: int
    Intersect: int
    Xyz: int
    Xzy: int
    Yxz: int
    Yzx: int
    Zxy: int
    Zyx: int
    Max: int
    @staticmethod
    def ValueOf(value: int) -> HealMethod:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class HealPath(NXOpen.TransientObject): 
    """ Represents a NXOpen.Routing.HealPath object which holds the data used in the creation of the heal path spline. """
    @property
    def ReverseEnd(self) -> bool:
        """
        Getter for property: (bool) ReverseEnd
         Returns the reverse end end.  
            Reverse the direction tha tthe end of the heal path takes
                    when the path is healed.   
         
        """
        pass
    @property
    def ReverseStart(self) -> bool:
        """
        Getter for property: (bool) ReverseStart
         Returns the reverse start end.  
            Reverse the direction that the start of the heal path
                    takes when the path is healed.   
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory. After this method is called,
                it is illegal to use the object. 
        """
        pass
    def GetAllData(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d, NXOpen.Vector3d, NXOpen.Vector3d, float, float, float, float, bool, bool, HealMethod, SplineOptions]:
        """
         Get all the data associated with the heal path creation. 
         Returns A tuple consisting of (start_point, end_point, start_vector, end_vector, start_parms, end_parms, start_extension, end_extension, reverse_start, reverse_end, heal_method, spline_options). 
         - start_point is:  NXOpen.Point3d. .
         - end_point is:  NXOpen.Point3d. .
         - start_vector is:  NXOpen.Vector3d. .
         - end_vector is:  NXOpen.Vector3d. .
         - start_parms is: float. .
         - end_parms is: float. .
         - start_extension is: float. .
         - end_extension is: float. .
         - reverse_start is: bool. .
         - reverse_end is: bool. .
         - heal_method is:  HealMethod NXOpen. .
         - spline_options is:  SplineOptions NXOpen. .

        """
        pass
    def GetEndExtension(self) -> float:
        """
         Get end extension. 
         Returns end_extension (float):  .
        """
        pass
    def GetEndParms(self) -> float:
        """
         Get end parameters. 
         Returns end_parms (float):  .
        """
        pass
    def GetEndPoint(self) -> NXOpen.Point3d:
        """
         Get the end point. Queries from end object if input is origin. 
         Returns end_point ( NXOpen.Point3d):  .
        """
        pass
    def GetEndVector(self) -> NXOpen.Vector3d:
        """
         Get the end vector. Queries from end object if input is zero vector. 
         Returns end_vector ( NXOpen.Vector3d):  .
        """
        pass
    def GetHealMethod(self) -> HealMethod:
        """
         Get heal method. 
         Returns heal_method ( HealMethod NXOpen):  .
        """
        pass
    def GetSplineOptions(self) -> SplineOptions:
        """
         Get spline options (by poleby points). 
         Returns spline_options ( SplineOptions NXOpen):  .
        """
        pass
    def GetStartExtension(self) -> float:
        """
         Get start extension. 
         Returns start_extension (float):  .
        """
        pass
    def GetStartParms(self) -> float:
        """
         Get start parameters. 
         Returns start_parms (float):  .
        """
        pass
    def GetStartPoint(self) -> NXOpen.Point3d:
        """
         Get the start point. Queries from start object if input is origin. 
         Returns start_point ( NXOpen.Point3d):  .
        """
        pass
    def GetStartVector(self) -> NXOpen.Vector3d:
        """
         Get the start vector. Queries from start object if input is zero vector. 
         Returns start_vector ( NXOpen.Vector3d):  .
        """
        pass
    def SetAllData(self, start_point: NXOpen.Point3d, end_point: NXOpen.Point3d, start_vector: NXOpen.Vector3d, end_vector: NXOpen.Vector3d, start_parm: float, end_parm: float, start_extension: float, end_extension: float, reverse_start: bool, reverse_end: bool, heal_method: HealMethod, spline_options: SplineOptions) -> None:
        """
         Set all the data associated with the heal path creation. 
        """
        pass
    def SetEndExtension(self, end_extension: float) -> None:
        """
         Set end extension. 
        """
        pass
    def SetEndParms(self, end_parms: float) -> None:
        """
         Set end parameters. 
        """
        pass
    def SetEndPoint(self, end_point: NXOpen.Point3d) -> None:
        """
         Set the end point. 
        """
        pass
    def SetEndVector(self, end_vector: NXOpen.Vector3d) -> None:
        """
         Set the end vector. 
        """
        pass
    def SetHealMethod(self, heal_method: HealMethod) -> None:
        """
         Set heal method. 
        """
        pass
    def SetReverseEnd(self, reverse: bool) -> None:
        """
         Sets the reverse end end.  Reverse the direction tha tthe end of the heal path takes
                    when the path is healed. 
        """
        pass
    def SetReverseStart(self, reverse: bool) -> None:
        """
         Sets the reverse start end.  Reverse the direction that the start of the heal path
                    takes when the path is healed. 
        """
        pass
    def SetSplineOptions(self, spline_options: SplineOptions) -> None:
        """
         Set spline options. 
        """
        pass
    def SetStartExtension(self, start_extension: float) -> None:
        """
         Set start extension. 
        """
        pass
    def SetStartParms(self, start_parms: float) -> None:
        """
         Set start parameters. 
        """
        pass
    def SetStartPoint(self, start_point: NXOpen.Point3d) -> None:
        """
         Set the start point. 
        """
        pass
    def SetStartVector(self, start_vector: NXOpen.Vector3d) -> None:
        """
         Set the start vector. 
        """
        pass
import NXOpen
class IAxisPort(IRoutePosition): 
    """ Interface class for all routing objects that specify a direction """
    @property
    @abstractmethod
    def Axis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @Axis.setter
    def Axis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @property
    @abstractmethod
    def CutbackLengthObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @CutbackLengthObject.setter
    def CutbackLengthObject(self, cutback_length: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @property
    @abstractmethod
    def EngagementObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @EngagementObject.setter
    def EngagementObject(self, engagement: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @property
    @abstractmethod
    def ForwardExtensionObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @ForwardExtensionObject.setter
    def ForwardExtensionObject(self, forward_extension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @abstractmethod
    def SetAlignVector(self, vector: NXOpen.Vector3d) -> None:
        """
         Sets the align vector of Port 
        """
        pass
    @abstractmethod
    def SetCutbackLength(self, cutback_length: float) -> None:
        """
         Sets the cutback length of a port, i.e. the length along the wire from
                    the port where individual wires leave a bundle to attach to pins
                  
        """
        pass
    @abstractmethod
    def SetEngagement(self, engagement: float) -> None:
        """
         The engagment distance of a NXOpen.Routing.IAxisPort, i.e. the distance 
                    behind the port that another fitting or stock may engage
                  
        """
        pass
    @abstractmethod
    def SetForwardExtension(self, forward_extension: float) -> None:
        """
         Sets the forward extension value of a port, i.e. the minimum length that
                    a segment must remain straight coming out of a NXOpen.Routing.Port
                  
        """
        pass
    @abstractmethod
    def SetRotationObject(self, rotation_object: NXOpen.DisplayableObject) -> None:
        """
         Sets the object used to derive the rotation vector of Port 
        """
        pass
    @abstractmethod
    def SetRotationVector(self, vector: NXOpen.Vector3d) -> None:
        """
         Sets the rotation vector of Port 
        """
        pass
import NXOpen
class ICharacteristic(NXOpen.INXObject): 
    """ Interface for querying and setting characteristic (UG attribute values) on various
        routing objects.  These methods should be used instead of the attribute methods on
        the NXObject object in order to support extra functionality 
        such as synonym characteristics available in the Routing application.  """
    @abstractmethod
    def DeleteCharacterstics(self, values: CharacteristicList) -> None:
        """
         Removes the input list of characteristics from this object. 
        """
        pass
    @abstractmethod
    def GetCharacteristics(self) -> CharacteristicList:
        """
         Get all of the characteristics values on the this object. 
         Returns values ( CharacteristicList NXOpen):  .
        """
        pass
    @abstractmethod
    def GetDestinationCharacteristics(self) -> CharacteristicList:
        """
           Returns the destination characteristics from the input object.
                      Retrieves the description of which destination characteristics to read
                      from the application view and then reads those destination 
                      characteristics from the object
                      
                          Ports: Reads characteristics from the port.
                          RCPs: Attempts to find a port at the RCP, reads characteristics from
                                      the port if it exists, otherwise reads from the
                                      stock associated with the rcp.
                          Segments: Reads characteristics from the stock associated with the segment.
                          Components: Reads characteristics directly from the component.
                          Stock: Reads characteristics from the stock or from the stock's data.
                      
                
         Returns values ( CharacteristicList NXOpen):  .
        """
        pass
    @abstractmethod
    def GetIntegerCharacteristic(self, name: str) -> int:
        """
         Get the value of an integer characteristic associated with the input name. 
         Returns value (int):  .
        """
        pass
    @abstractmethod
    def GetRealCharacteristic(self, name: str) -> float:
        """
         Get the value of a real characteristic associated with the input name. 
         Returns value (float):  .
        """
        pass
    @abstractmethod
    def GetStringCharacteristic(self, name: str) -> str:
        """
         Get the value of a string characteristic associated with the input name. 
         Returns value (str):  .
        """
        pass
    @abstractmethod
    @overload
    def SetCharacteristic(self, name: str, value: int) -> None:
        """
         Set the value of an integer characteristic associated with the input name,
                    adds a new characteristic to the list if one doesn't exist already. Converts
                    the type of an existing characteristic with the same name to integer if it's 
                    type is not integer. 
        """
        pass
    @abstractmethod
    @overload
    def SetCharacteristic2(self, title: str, value: int) -> None:
        """
         Sets or creates an integer type attribute associated with the input title. 
                creating a new attribute if one doesn't exist already. 
                If the method is called on a stock Assemblies.Component, the 
                method will create or edit a part attribute on the stock part. For legacy parts 
                where the attribute is on the stock component, the attribute will be moved 
                to the stock part. 
                If the method is called on a non-stock Assemblies.Component, 
                the method will create or edit an attribute on the corresponding instance. For 
                legacy parts where the attribute is on the component, the attribute will be moved 
                to the corresponding instance. 
                If the method is called on any non-component object, the method will 
                access or create an attribute on the object itself. 
        """
        pass
    @abstractmethod
    @overload
    def SetCharacteristic2(self, title: str, value: float) -> None:
        """
         Sets or creates a double type attribute associated with the input title. 
                creating a new attribute if one doesn't exist already. 
                If the method is called on a stock Assemblies.Component, the 
                method will create or edit a part attribute on the stock part. For legacy parts 
                where the attribute is on the stock component, the attribute will be moved 
                to the stock part. 
                If the method is called on a non-stock Assemblies.Component, 
                the method will create or edit an attribute on the corresponding instance. For 
                legacy parts where the attribute is on the component, the attribute will be moved 
                to the corresponding instance. 
                If the method is called on any non-component object, the method will 
                access or create an attribute on the object itself. 
        """
        pass
    @abstractmethod
    @overload
    def SetCharacteristic2(self, title: str, value: str) -> None:
        """
         Sets or creates a string type type attribute associated with the input title. 
                creating a new attribute if one doesn't exist already. 
                If the method is called on a stock Assemblies.Component, the 
                method will create or edit a part attribute on the stock part. For legacy parts 
                where the attribute is on the stock component, the attribute will be moved 
                to the stock part. 
                If the method is called on a non-stock Assemblies.Component, 
                the method will create or edit an attribute on the corresponding instance. For 
                legacy parts where the attribute is on the component, the attribute will be moved 
                to the corresponding instance. 
                If the method is called on any non-component object, the method will 
                access or create an attribute on the object itself. 
        """
        pass
    @abstractmethod
    @overload
    def SetCharacteristic(self, name: str, value: float) -> None:
        """
         Set the value of an real characteristic associated with the input name,
                    adds a new characteristic to the list if one doesn't exist already. Converts
                    the type of an existing characteristic with the same name to real if it's 
                    type is not real. 
        """
        pass
    @abstractmethod
    @overload
    def SetCharacteristic(self, name: str, value: str) -> None:
        """
         Set the value of an string characteristic associated with the input name,
                    adds a new characteristic to the list if one doesn't exist already. Converts
                    the type of an existing characteristic with the same name to string if it's 
                    type is not string. 
        """
        pass
    @abstractmethod
    def SetCharacteristics(self, values: CharacteristicList) -> None:
        """
         Set all of the characteristics values on this object. 
        """
        pass
    @abstractmethod
    def SetCharacteristics2(self, values: CharacteristicList) -> None:
        """
         Sets all attributes associated with the titles from the input list, 
                creating new attributes for the ones that don't exist already. 
                If the method is called on a stock Assemblies.Component, the 
                method will create or edit part attributes on the stock part. For legacy parts 
                where the attributes are on the stock component, the attributes will be moved 
                to the stock part. 
                If the method is called on a non-stock Assemblies.Component, 
                the method will create or edit attributes on the corresponding instance. For 
                legacy parts where the attribute is on the component, the attributes will be moved 
                to the corresponding instance. 
                If the method is called on any non-component object, the method will 
                access or create attributes on the object itself. 
        """
        pass
import NXOpen
class InfoObjectsBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Routing.InfoObjectsBuilder
    """
    @property
    def ObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) ObjectCollector
         Returns the routing object collector   
            
         
        """
        pass
import NXOpen
class InstanceNameLookupBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.InstanceNameLookupBuilder. 
        Routing.InstanceNameLookupBuilder is used to look up the matching part to place
        based on the criteria defined in the INSTANCE_NAME_LOOKUP node and the ship 
        identifier specified in the customer defaults."""
    @property
    def InstanceNameCombo(self) -> str:
        """
        Getter for property: (str) InstanceNameCombo
         Returns the instance name   
            
         
        """
        pass
    @InstanceNameCombo.setter
    def InstanceNameCombo(self, instanceNameCombo: str):
        """
        Setter for property: (str) InstanceNameCombo
         Returns the instance name   
            
         
        """
        pass
import NXOpen
class IntegrateRunsBuilder(NXOpen.Builder): 
    """ Builder Class for Integrate Runs Object """
    class Button(Enum):
        """
        Members Include: 
         |FromItems|  Set as FromItem for selected node in tree list
         |ToItems|  Set as ToItem for selected node in tree list
         |MemberItems|  Set as MemberItem for selected node in tree list
         |Unknown|  unknown button ID 

        """
        FromItems: int
        ToItems: int
        MemberItems: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> IntegrateRunsBuilder.Button:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Enum(Enum):
        """
        Members Include: 
         |FirstRun| 
         |SecondRun| 

        """
        FirstRun: int
        SecondRun: int
        @staticmethod
        def ValueOf(value: int) -> IntegrateRunsBuilder.Enum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FirstRun(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) FirstRun
         Returns the first run   
            
         
        """
        pass
    @property
    def RunAttributes(self) -> IntegrateRunsBuilder.Enum:
        """
        Getter for property: ( IntegrateRunsBuilder.Enum NXOpen) RunAttributes
         Returns the run attributes   
            
         
        """
        pass
    @RunAttributes.setter
    def RunAttributes(self, runAttributes: IntegrateRunsBuilder.Enum):
        """
        Setter for property: ( IntegrateRunsBuilder.Enum NXOpen) RunAttributes
         Returns the run attributes   
            
         
        """
        pass
    @property
    def RunName(self) -> str:
        """
        Getter for property: (str) RunName
         Returns the user mentioned run name for Integrated Run  
            
         
        """
        pass
    @RunName.setter
    def RunName(self, runName: str):
        """
        Setter for property: (str) RunName
         Returns the user mentioned run name for Integrated Run  
            
         
        """
        pass
    @property
    def SecondRun(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SecondRun
         Returns the second run   
            
         
        """
        pass
    def ModifyItemsButton(self, objects: List[NXOpen.NXObject], buttonType: IntegrateRunsBuilder.Button) -> None:
        """
         Updates the selected nodes in Specify FromTo item tree list to FromToMember item based on buttonType 
        """
        pass
class InterfaceTerminalBase(RouteObject): 
    """ 
        The NXOpen.Routing.InterfaceTerminalBase corresponds to an abstract class for
        a prototype NXOpen.Routing.Port.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    @property
    def Port(self) -> Port:
        """
        Getter for property: ( Port NXOpen) Port
         Returns a physical port representing a prototype  NXOpen::Routing::Port  on
                    a connector piece part or subassembly.  
          
                    Depricated in NX5.
                  
         
        """
        pass
    def GetPorts(self) -> List[Port]:
        """
         Get the physical NXOpen.Routing.Ports associated with the terminal.
                    
                    The physical NXOpen.Routing.Port corresponds to a port occurrence.
                    
                
         Returns ports ( Port List[NXOp):   .
        """
        pass
class InterfaceTerminalRelationshipBase(ObjectRelationship): 
    """ 
        The abstract class NXOpen.Routing.InterfaceTerminalRelationshipBase relates many
        NXOpen.Routing.Ports to one NXOpen.Routing.Port.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    class RelationType(Enum):
        """
        Members Include: 
         |Decomposition|  

        """
        Decomposition: int
        @staticmethod
        def ValueOf(value: int) -> InterfaceTerminalRelationshipBase.RelationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def RelationshipType(self) -> InterfaceTerminalRelationshipBase.RelationType:
        """
        Getter for property: ( InterfaceTerminalRelationshipBase.RelationType NXOpen) RelationshipType
         Returns the type of the  NXOpen::Routing::InterfaceTerminalRelationshipBase  object.  
          
                      
                    Interface Terminal Relationship can be of following types:
                     NXOpen::Routing::InterfaceTerminalRelationshipBase::RelationTypeDecomposition 
                      
                  
         
        """
        pass
    @RelationshipType.setter
    def RelationshipType(self, relationship_type: InterfaceTerminalRelationshipBase.RelationType):
        """
        Setter for property: ( InterfaceTerminalRelationshipBase.RelationType NXOpen) RelationshipType
         Returns the type of the  NXOpen::Routing::InterfaceTerminalRelationshipBase  object.  
          
                      
                    Interface Terminal Relationship can be of following types:
                     NXOpen::Routing::InterfaceTerminalRelationshipBase::RelationTypeDecomposition 
                      
                  
         
        """
        pass
    def AddRelatedInterfaceTerminal(self, related_interface_terminal: InterfaceTerminalShadow) -> None:
        """
         Adds a NXOpen.Routing.Port to the NXOpen.Routing.InterfaceTerminalRelationshipBase object
                    with a relationship of related.
                
        """
        pass
    def GetRelatedInterfaceTerminals(self) -> List[InterfaceTerminalShadow]:
        """
         Gets the list of NXOpen.Routing.Ports in the NXOpen.Routing.InterfaceTerminalRelationshipBase
                    object with a relationship of related.
                    
                    A NXOpen.Routing.InterfaceTerminalRelationshipBase object can have one or more related NXOpen.Routing.Ports
                    associated with a single relating NXOpen.Routing.Port.
                    
                
         Returns related_interface_terminals ( InterfaceTerminalShadow List[NXOp):  .
        """
        pass
    def GetRelatingInterfaceTerminal(self) -> InterfaceTerminalShadow:
        """
         Gets the NXOpen.Routing.Port in the NXOpen.Routing.InterfaceTerminalRelationshipBase
                    with a relationship of relating.
                    
                    A NXOpen.Routing.InterfaceTerminalRelationshipBase object can have only one relating NXOpen.Routing.Port
                    associated with one or more related NXOpen.Routing.Ports.
                    
                
         Returns relating_interface_terminal ( InterfaceTerminalShadow NXOpen):  .
        """
        pass
    def RemoveRelatedInterfaceTerminal(self, related_interface_terminal: InterfaceTerminalShadow) -> None:
        """
         Removes a related NXOpen.Routing.Port from the list of related terminals in the
                    NXOpen.Routing.InterfaceTerminalRelationshipBase object.
                
        """
        pass
    def ReplaceRelatedInterfaceTerminals(self, related_interface_terminals: List[InterfaceTerminalShadow]) -> None:
        """
         Replaces the existing related NXOpen.Routing.Ports in the NXOpen.Routing.InterfaceTerminalRelationshipBase
                    object with input ones.
                    
                    Removes all the related NXOpen.Routing.Ports in a relationship and replaces them with the set
                    of input NXOpen.Routing.Ports.
                    
                
        """
        pass
    def SetRelatingInterfaceTerminal(self, relating_interface_terminal: InterfaceTerminalShadow) -> None:
        """
          
        """
        pass
import NXOpen
class InterfaceTerminalRelationshipCollection(NXOpen.TaggedObjectCollection): 
    """
        Represents a collection of NXOpen.Routing.InterfaceTerminalRelationshipShadow objects.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    @overload
    def CreateElectricalInterfaceTerminalRelationship(self) -> InterfaceTerminalRelationshipShadow:
        """
         Creates and returns a NXOpen.Routing.InterfaceTerminalRelationshipShadow object
                    under electrical data root object.
                
         Returns interface_terminal_relationship ( InterfaceTerminalRelationshipShadow NXOpen):  .
        """
        pass
    @overload
    def CreateElectricalInterfaceTerminalRelationship(self, guid: str) -> InterfaceTerminalRelationshipShadow:
        """
         Creates and returns a NXOpen.Routing.InterfaceTerminalRelationshipShadow object
                    under electrical data root object.
                
         Returns interface_terminal_relationship ( InterfaceTerminalRelationshipShadow NXOpen):  .
        """
        pass
    @overload
    def CreateMechanicalInterfaceTerminalRelationship(self) -> InterfaceTerminalRelationshipShadow:
        """
         Creates and returns a NXOpen.Routing.InterfaceTerminalRelationshipShadow object
                    under mechanical data root object.
                
         Returns interface_terminal_relationship ( InterfaceTerminalRelationshipShadow NXOpen):  .
        """
        pass
    @overload
    def CreateMechanicalInterfaceTerminalRelationship(self, guid: str) -> InterfaceTerminalRelationshipShadow:
        """
         Creates and returns a NXOpen.Routing.InterfaceTerminalRelationshipShadow object
                    under mechanical data root object.
                
         Returns interface_terminal_relationship ( InterfaceTerminalRelationshipShadow NXOpen):  .
        """
        pass
class InterfaceTerminalRelationshipShadow(InterfaceTerminalRelationshipBase): 
    """ 
        Represents an assembly shadow of
        NXOpen.Routing.InterfaceTerminalRelationshipBase.
        
        
        Shadow objects stand in for the source objects when source parts are unavailable or unloaded.
        
        
        NXOpen.Routing.InterfaceTerminalRelationshipShadow carries the same GUID as the
        source NXOpen.Routing.InterfaceTerminalRelationshipBase and syncs with the source
        anytime necessary or possible.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    pass
class InterfaceTerminalShadow(InterfaceTerminalBase): 
    """ Represents the defining data for a physical NXOpen.Routing.Port.

        
        NXOpen.Routing.InterfaceTerminalShadow is an assembly shadow of NXOpen.Routing.InterfaceTerminalBase.  
        Component assignment associates the physical NX NXOpen.Routing.Port to the logical port defined by this
        NXOpen.Routing.InterfaceTerminalShadow.
               
        
        NXOpen.Routing.InterfaceTerminalShadow objects reside in the work part (in assembly context) and
        carries the same GUID as the source NXOpen.Routing.Port.  It syncs with the source anytime necessary or possible.
        
        
        Shadow objects are like extracted objects and stand in for the source objects, when source parts are
        unavailable or unloaded.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    pass
class Interior(Enum):
    """
    Members Include: 
     |NotInteriorToPart|  Is not interior to any part 
     |InteriorToPart|  Is interior to some part 

    """
    NotInteriorToPart: int
    InteriorToPart: int
    @staticmethod
    def ValueOf(value: int) -> Interior:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class IPath(NXOpen.INXObject): 
    """ The Routing IPath object is a list of segments in a route. It also
        contains the beginning and ending control point for the path.
     """
    @property
    @abstractmethod
    def ControlPointEnd(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointEnd.setter
    def ControlPointEnd(self, end: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @property
    @abstractmethod
    def ControlPointStart(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointStart.setter
    def ControlPointStart(self, start: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    @abstractmethod
    def AddSegmentsToList(self, objs: List[ISegment]) -> None:
        """
         Adds segment(s) to an IPath object. 
        """
        pass
    @abstractmethod
    def DelSegmentsFromList(self, objs: List[ISegment]) -> None:
        """
         Removes segment(s) from the IPath object. 
        """
        pass
    @abstractmethod
    def GetSegmentList(self) -> List[ISegment]:
        """
         Returns the list of all of the segments contained in the IPath 
         Returns objs ( ISegment List[NXOp):  list of all of the segments in this IPath object .
        """
        pass
import NXOpen
class IRoutePosition(ICharacteristic): 
    """ 
        Interface class for all routing objects that specify a single (possibly associative) location
        in space.
     """
    @property
    @abstractmethod
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @property
    @abstractmethod
    def Position(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
    @Position.setter
    def Position(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
import NXOpen
class ISegmentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Routing.ISegment objects. """
    pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing.Electrical
class ISegment(ICharacteristic): 
    """ Interface class for all routing segments [LineArcSpline] """
    @property
    @abstractmethod
    def FollowCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) FollowCurve
         Returns  the segment follow curve.  
            NULL object indicates segment has no follow curve   
         
        """
        pass
    @property
    @abstractmethod
    def Guid(self) -> str:
        """
        Getter for property: (str) Guid
         Returns the Globally Unique Identifier (GUID) for this segment.  
             
         
        """
        pass
    @property
    @abstractmethod
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns  the length of the segment.  
             
         
        """
        pass
    @abstractmethod
    def ConvertEccentricLinearToLinear(self) -> ConvertEccentricLinearToLinear:
        """
         Is line segment eccentric converted to line segment? 
         Returns is_converted ( ConvertEccentricLinearToLinear NXOpen):  Is line segment eccentric converted to line segment? .
        """
        pass
    @abstractmethod
    def ConvertLinearToEccentricLinear(self) -> ConvertLinearToEccentricLinear:
        """
         Is line segment converted to eccentric line segment? 
         Returns is_converted ( ConvertLinearToEccentricLinear NXOpen):  Is line segment converted to eccentric line segment? .
        """
        pass
    @abstractmethod
    def GenerateNewGuid(self) -> None:
        """
         Generates a new Globally Unique Identifier (GUID) on this segment. 
        """
        pass
    @abstractmethod
    def GetCableDevices(self) -> List[NXOpen.Routing.Electrical.CableDevice]:
        """
         Returns NXOpen.Routing.Electrical.CableDevice objects
                       from NXOpen.Routing.ISegment. 
         Returns cableDevices ( NXOpen.Routing.Electrical.CableDevice Li):  Array of cable devices. .
        """
        pass
    @abstractmethod
    def GetCablewaysLayoutViews(self) -> List[NXOpen.Routing.Electrical.CablewaysLayoutView]:
        """
         Returns NXOpen.Routing.Electrical.CablewaysLayoutView objects
                    from the NXOpen.Routing.ISegment. 
         Returns views ( NXOpen.Routing.Electrical.CablewaysLayoutView Li):  Array of cableways layout views. .
        """
        pass
    @abstractmethod
    def GetConnections(self) -> List[NXOpen.Routing.Electrical.Connection]:
        """
         Returns the electrical connections routed on this segment, if any. 
         Returns connections ( NXOpen.Routing.Electrical.Connection Li):  .
        """
        pass
    @abstractmethod
    def GetEndPoints(self) -> Tuple[NXOpen.Point3d, NXOpen.Point3d]:
        """
          Get the current location of the segment ends in ABS coordinates.  This value is
                     overridden by the coordinates of the end RCPs associated with this segment. 
         Returns A tuple consisting of (start_point, end_point). 
         - start_point is:  NXOpen.Point3d. Location of end 0 in ABS coordinates .
         - end_point is:  NXOpen.Point3d. Location of end 1 in ABS coordinates .

        """
        pass
    @abstractmethod
    def GetEndRcps(self) -> Tuple[ControlPoint, ControlPoint]:
        """
          Return of segment end control points.
                     The NXOpen.Routing.ControlPoint defines an end of a segment 
         Returns A tuple consisting of (start_rcp, end_rcp). 
         - start_rcp is:  ControlPoint NXOpen. RCP defining start of segment .
         - end_rcp is:  ControlPoint NXOpen. RCP defining end of segment .

        """
        pass
    @abstractmethod
    def GetIsEccentricSegment(self) -> Eccentric:
        """
         Is given segment a eccentric segment? 
         Returns is_eccentric ( Eccentric NXOpen):  Is segment a eccentric segment? .
        """
        pass
    @abstractmethod
    def GetIsSegmentInterior(self) -> Interior:
        """
         Query if a segment is interior to any part 
         Returns is_interior ( Interior NXOpen):  Is segment interior? .
        """
        pass
    @abstractmethod
    def GetIsTerminalSegment(self) -> Terminal:
        """
         Is given segment a terminal segment? 
         Returns is_terminal ( Terminal NXOpen):  Is segment a terminal segment? .
        """
        pass
    @abstractmethod
    def GetSegmentAllStocks(self) -> List[Stock]:
        """
         Returns NXOpen.Routing.Stock as well as NXOpen.Routing.Overstock
                    objects from the NXOpen.Routing.ISegment. 
         Returns stocks ( Stock List[NXOp):  Array of stocksoverstocks. .
        """
        pass
    @abstractmethod
    def GetSegmentStock(self) -> List[Stock]:
        """
         Returns all stocks that directly reference this segment as part of the path defining the stock. 
         Returns stocks ( Stock List[NXOp):  .
        """
        pass
    @abstractmethod
    def GetWires(self) -> List[Wire]:
        """
         Returns the electrical wires routed on this segment, if any. 
         Returns wires ( Wire List[NXOp):  .
        """
        pass
    @abstractmethod
    def IsSegmentFromBuiltInPath(self) -> bool:
        """
         Was this segment generated by placing a Built-In Path component? 
         Returns isSegmentFromBuiltInPath (bool):  .
        """
        pass
    @abstractmethod
    def SetEndPoints(self, start_point: NXOpen.Point3d, end_point: NXOpen.Point3d) -> None:
        """
          Set the current location of the segment ends in ABS coordinates.  This value is
                     overridden by the coordinates of the end RCPs associated with this segment. 
        """
        pass
    @abstractmethod
    def SetEndRcps(self, start_rcp: ControlPoint, end_rcp: ControlPoint) -> None:
        """
         
        """
        pass
    @abstractmethod
    def SetIsTerminalSegment(self, is_terminal: Terminal) -> None:
        """
         Set given segment to be a terminal segment? 
        """
        pass
    @abstractmethod
    def SetSegmentInteriorPart(self, interior_part: NXOpen.Assemblies.Component) -> None:
        """
         Set a segment to be interior to supplied part 
        """
        pass
import NXOpen
class ItemDefinition(RouteObject): 
    """ NXOpen.Routing.ItemDefinition object corresponds to DDID in AP212 and to a piece
        part or routing stock in NX.
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    @property
    def DefiningNxObject(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) DefiningNxObject
         Returns the NX object associated with the item definition object.  
          
                      
                    NX part object defining the item definition can be a piece part, a group of displayable
                    entities or a routing stock.
                      
                  
         
        """
        pass
import NXOpen
class LinearPathBuilder(NXOpen.Builder): 
    """ Builder for creating routing linear paths.   These paths can include
        constrained line segments,  bend corners and elbows.  This fuctionality
        can only be used with the Assemblies Positioning functionality.  The
        work part must have been converted to use Assemblies Positioning
        using the Convert Mating Conditions tool.


        To create a control point (and it's associated segment) first create
        a preview control point, then define the control point using either
        a smart point (Routing.LinearPathBuilder.SetControlPointDefiningPoint), 
        or some other object 
        (Routing.LinearPathBuilder.SetControlPointDefiningObject).  

    """
    @property
    def ElbowSnapSettings(self) -> ElbowSnapSettings:
        """
        Getter for property: ( ElbowSnapSettings NXOpen) ElbowSnapSettings
         Returns the elbow snapping settings for determining location of control points
                    as the user drags their mouse.  
            Only useful in the UI.    
         
        """
        pass
    @ElbowSnapSettings.setter
    def ElbowSnapSettings(self, snap_settings: ElbowSnapSettings):
        """
        Setter for property: ( ElbowSnapSettings NXOpen) ElbowSnapSettings
         Returns the elbow snapping settings for determining location of control points
                    as the user drags their mouse.  
            Only useful in the UI.    
         
        """
        pass
    @property
    def LinearPathSettings(self) -> LinearPathSettings:
        """
        Getter for property: ( LinearPathSettings NXOpen) LinearPathSettings
         Returns the settings that determine what constraints to apply to the new path.  
             
         
        """
        pass
    @LinearPathSettings.setter
    def LinearPathSettings(self, settings_builder: LinearPathSettings):
        """
        Setter for property: ( LinearPathSettings NXOpen) LinearPathSettings
         Returns the settings that determine what constraints to apply to the new path.  
             
         
        """
        pass
    @property
    def PathStockBuilder(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) PathStockBuilder
         Returns the builder for assigning stock to the new path.  
            
         
        """
        pass
    @PathStockBuilder.setter
    def PathStockBuilder(self, stock_builder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) PathStockBuilder
         Returns the builder for assigning stock to the new path.  
            
         
        """
        pass
    def AddPreviewControlPoint(self, location: NXOpen.Point3d) -> ControlPoint:
        """
         Add a new control point to the path.  This control point is considered
                    to be a preview control point to show what the path will look like
                    interactively.   This control point will be deleted when the commit
                    method is invoked unless the rcp has been fully defined.
                    
         Returns preview_rcp ( ControlPoint NXOpen):  Preview control point, 
                                                                            will be  if there
                                                                            is already a control 
                                                                            point at the given location.
        """
        pass
    def GetLastControlPoint(self) -> ControlPoint:
        """
         Returns the last control point in the path. 
         Returns last_rcp ( ControlPoint NXOpen):  .
        """
        pass
    def GetParentSegmentOfEccentricSegment(self) -> ISegment:
        """
         Parent segment
         Returns parentSegment ( ISegment NXOpen):  .
        """
        pass
    def RemoveLastNonPreviewControlPoint(self) -> None:
        """
         Removes the last fully-defined control point in the path.  Also removes any 
                    preview control points. 
        """
        pass
    def SetControlPointDefiningObject(self, preview_rcp: ControlPoint, position: NXOpen.Point3d, objectValue: NXOpen.NXObject) -> None:
        """
         Fully defines a preview control point.  The preview control point's location is
                    set to the given position, and the control point is constrained to the
                    given object (depending on the linear path settings).  
                    A control point may only be defined once.
        """
        pass
    def SetControlPointDefiningPoint(self, preview_rcp: ControlPoint, point: NXOpen.Point) -> None:
        """
         Fully defines a preview control point using the given point.  The control
                    point is not made associative directly to the input point.  The control point
                    is made associative (depending on the linear path settings) to the
                    objects that the input point is associative to. 
                    
                    A control point may only be defined once.
        """
        pass
    def SetIsEccentricModeSelected(self, isEccentricModeSelected: bool) -> None:
        """
         Set the boolean value specifies that Eccentric mode selected or not
        """
        pass
    def SetIsNewControlPointRequired(self, isNewControlPointRequired: bool) -> None:
        """
         Set the boolean value specifies that new control point required or not
        """
        pass
    def SetParentSegmentOfEccentricSegment(self, parentSegment: ISegment) -> None:
        """
         
        """
        pass
    def SettingChanged(self) -> None:
        """
         Notifies the builder that some routing preferences have changed, and that the
                    builder (and it's associated builders) must update their values to refelect those
                    changes. 
        """
        pass
import NXOpen
class LinearPathSettings(NXOpen.Builder): 
    """ Helper object used the by Routing.LinearPathBuilder builder. 
        Determines various settings to be applied when the path is created.
    """
    @property
    def AllowCutElbow(self) -> bool:
        """
        Getter for property: (bool) AllowCutElbow
         Returns  a flag indicating whether or not to allow cut elbow placement   
            
         
        """
        pass
    @AllowCutElbow.setter
    def AllowCutElbow(self, assign: bool):
        """
        Setter for property: (bool) AllowCutElbow
         Returns  a flag indicating whether or not to allow cut elbow placement   
            
         
        """
        pass
    @property
    def AssignDefaultCorner(self) -> bool:
        """
        Getter for property: (bool) AssignDefaultCorner
         Returns the preference to assign the current default corner to new segments.  
             
         
        """
        pass
    @AssignDefaultCorner.setter
    def AssignDefaultCorner(self, assign: bool):
        """
        Setter for property: (bool) AssignDefaultCorner
         Returns the preference to assign the current default corner to new segments.  
             
         
        """
        pass
    @property
    def AssignDefaultElbow(self) -> bool:
        """
        Getter for property: (bool) AssignDefaultElbow
         Returns the preference to find and assign a default elbow to new segments.  
             
         
        """
        pass
    @AssignDefaultElbow.setter
    def AssignDefaultElbow(self, assign: bool):
        """
        Setter for property: (bool) AssignDefaultElbow
         Returns the preference to find and assign a default elbow to new segments.  
             
         
        """
        pass
    @property
    def LockAngle(self) -> bool:
        """
        Getter for property: (bool) LockAngle
         Returns the preference to determine if the angle between segments should
                        be constrained.  
              
         
        """
        pass
    @LockAngle.setter
    def LockAngle(self, lock: bool):
        """
        Setter for property: (bool) LockAngle
         Returns the preference to determine if the angle between segments should
                        be constrained.  
              
         
        """
        pass
    @property
    def LockLength(self) -> bool:
        """
        Getter for property: (bool) LockLength
         Returns the preference to determine if the length of new segments should
                     be constrained.  
             
         
        """
        pass
    @LockLength.setter
    def LockLength(self, lock: bool):
        """
        Setter for property: (bool) LockLength
         Returns the preference to determine if the length of new segments should
                     be constrained.  
             
         
        """
        pass
    @property
    def LockToSelectedObject(self) -> bool:
        """
        Getter for property: (bool) LockToSelectedObject
         Returns the preference to determine if the new segments and control points
                        should be constrained to the objects selected by the user.  
             
         
        """
        pass
    @LockToSelectedObject.setter
    def LockToSelectedObject(self, lock: bool):
        """
        Setter for property: (bool) LockToSelectedObject
         Returns the preference to determine if the new segments and control points
                        should be constrained to the objects selected by the user.  
             
         
        """
        pass
import NXOpen
class LineSegmentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.LineSegment objects. """
    pass
import NXOpen
import NXOpen.Positioning
class LineSegment(NXOpen.Line): 
    """ Represents a line segment. """
    @property
    def FollowCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) FollowCurve
         Returns  the segment follow curve.  
            NULL object indicates segment has no follow curve   
         
        """
        pass
    @property
    def Guid(self) -> str:
        """
        Getter for property: (str) Guid
         Returns the Globally Unique Identifier (GUID) for this segment.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns  the length of the segment.  
             
         
        """
        pass
    def IsAngleLocked(self, objectValue: NXOpen.NXObject) -> bool:
        """
          Returns whether or not an angle, parallel or perpendicular constraint exists
                     that constrains the angle between this segment and the other input object.
                     Both line segments must not be occurrences.
                 
         Returns angle_locked (bool):  Whether or not the angle is locked. .
        """
        pass
    def IsLengthLocked(self) -> bool:
        """
          Returns whether or not a distance constraint exists that constrains the
                     distance between the two end control points of this line segment.
                 
         Returns length_locked (bool):  Whether or not the length is locked. .
        """
        pass
    def LockAngle(self, objectValue: NXOpen.NXObject, logical_cons_only: bool) -> NXOpen.Positioning.Constraint:
        """
          Adds a constraint to maintain the angle of this line segment with respect
                 to another object.  It does this by ensuring that there is an angle, perpendicular
                 or parallel constraint between this line segment and the other object.  This line
                 segment must not be an occurrence, the other object may be an occurrence.
                 See NXOpen.Positioning.Constraint for a description of angle, parallel
                 and perpendicular constraints.
                 
         Returns angle_constraint ( NXOpen.Positioning.Constraint):  The new or existing angle constraint. .
        """
        pass
    def LockLength(self) -> NXOpen.Positioning.Constraint:
        """
          Adds a constraint to maintain the length of this line segment.  It does this
                 by ensuring that there is a distance constraint between the two end
                 NXOpen.Routing.ControlPoint objects of this line segment.  See
                 NXOpen.Positioning.Constraint for a description of distance
                 constraints.
                 
         Returns distance_constraint ( NXOpen.Positioning.Constraint):   The new or existing distance constraint between the end control points. .
        """
        pass
    def UnlockAngle(self, objectValue: NXOpen.NXObject) -> None:
        """
          Removes the angle, parallel or perpendicular constraint that constrains
                     the angle between this line segment and the input object.  This line
                     segment must not be an occurrence.
                     Call NXOpen.Update.DoUpdate afterwards to ensure that
                     the constraint is fully deleted.
                 
        """
        pass
    def UnlockLength(self) -> None:
        """
          Removes the distance constraint that constrains the distance between
                     the two end control points of this line segment.
                     Call NXOpen.Update.DoUpdate afterwards to ensure that
                     the constraint is fully deleted.
                 
        """
        pass
class LogicalConnection(ConnectivityDefinition): 
    """ 
        Represents a connection between mutiple From and To Routing.LogicalTerminal.
        
        
        Use Routing.Electrical.Connection to constrain 
        a connection to one From and To Routing.LogicalTerminal
        This is an abstract class and is for future use.
        See NX Open Routing help for detailed information on the Connection data model
        
     """
    def AddFromTerminal(self, from_terminal: LogicalTerminal) -> bool:
        """
         Add Routing.LogicalTerminal to the From Terminals collection.
                    Ordering is not important within variable length array. 
         Returns result (bool):  Successfully added Routing.LogicalTerminal?.
        """
        pass
    def AddToTerminal(self, to_terminal: LogicalTerminal) -> bool:
        """
         Add Routing.LogicalTerminal to end of the To Terminals collection.
                    Ordering is not important within variable length array. 
         Returns result (bool):  Successful addition of Routing.LogicalTerminal?. .
        """
        pass
    def GetFromTerminals(self) -> List[LogicalTerminal]:
        """
         Get all From Terminals from the logical connection 
         Returns from_terminals ( LogicalTerminal List[NXOp):  Collection of Routing.LogicalTerminal.
        """
        pass
    def GetToTerminals(self) -> List[LogicalTerminal]:
        """
         Get all To Terminals from the logical connection
         Returns to_terminals ( LogicalTerminal List[NXOp):  Collection of Routing.LogicalTerminal.
        """
        pass
    def RemoveFromTerminal(self, from_terminal: LogicalTerminal) -> bool:
        """
         Remove a Routing.LogicalTerminal from the From Terminals collection.
                    Ordering is not important within the variable length array. 
         Returns result (bool):  Successful removal of Routing.LogicalTerminal?.
        """
        pass
    def RemoveToTerminal(self, to_terminal: LogicalTerminal) -> bool:
        """
         Remove a Routing.LogicalTerminal from the To Terminals collection.
                    Ordering is not important within the variable length array. 
         Returns result (bool):  Successful removal of Routing.LogicalTerminal? .
        """
        pass
    def ReplaceFromTerminals(self, from_terminals: List[LogicalTerminal]) -> None:
        """
         Replace the existing From Terminals for the logical connection with
                     collection of Routing.LogicalTerminal terminals 
        """
        pass
    def ReplaceToTerminals(self, to_terminals: List[LogicalTerminal]) -> None:
        """
         Replace the existing To Terminals for the logical connection with
                    collection of Routing.LogicalTerminal terminals 
        """
        pass
class LogicalTerminal(RouteObject): 
    """ 
        Assembly instance of a NXOpen.Routing.InterfaceTerminalBase.
        
        
        NXOpen.Routing.LogicalTerminal corresponds to NX
        occurrences of NXOpen.Routing.MultiPorts,
        NXOpen.Routing.TerminalPorts or
        NXOpen.Routing.FittingPorts.  Multiple ports can be
        associated to a single
        NXOpen.Routing.LogicalTerminal.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    @property
    def InterfaceTerminalShadow(self) -> InterfaceTerminalShadow:
        """
        Getter for property: ( InterfaceTerminalShadow NXOpen) InterfaceTerminalShadow
         Returns the  NXOpen::Routing::InterfaceTerminalShadow  corresponding to  NXOpen::Routing::Port  in piece part.  
          
                  
         
        """
        pass
    @property
    def Port(self) -> Port:
        """
        Getter for property: ( Port NXOpen) Port
         Returns the physical  NXOpen::Routing::Port  associated with the terminal.  
          
                      
                    The physical  NXOpen::Routing::Port  corresponds to a port occurrence.
                      
                  
         
        """
        pass
    def AddPort(self, port: Port) -> None:
        """
         Add a physical NXOpen.Routing.Port to the
                    terminal.  If , nothing is added.
                    
                    The physical NXOpen.Routing.Port corresponds to a port occurrence.
                    
                
        """
        pass
    def ClearAllPorts(self) -> None:
        """
         Clears the NXOpen.Routing.Port of all
                    NXOpen.Routing.Ports.
                
        """
        pass
    def GetParentConnector(self) -> SingleDevice:
        """
         The physical connector associated with the NXOpen.Routing.Port.
                    
                    Assumes that a NXOpen.Routing.Port cannot be associated to more than one physical connector at any time.
                    
                
         Returns connector ( SingleDevice NXOpen):  .
        """
        pass
    def GetPorts(self) -> List[Port]:
        """
         Get the physical NXOpen.Routing.Ports associated with the terminal.
                    
                    The physical NXOpen.Routing.Port corresponds to a port occurrence.
                    
                    Depricated in NX4.
                
         Returns ports ( Port List[NXOp):   .
        """
        pass
    def RemovePort(self, port: Port) -> None:
        """
         Remove a physical NXOpen.Routing.Port from the
                    terminal.  If the NXOpen.Routing.Port is not
                    associated to the NXOpen.Routing.LogicalTerminal
                    or is , nothing is done.
                    
                    The physical NXOpen.Routing.Port corresponds to a port occurrence.
                    
                
        """
        pass
import NXOpen
class ManualRouteBuilder(NXOpen.Builder): 
    """ """
    @property
    def PointList(self) -> NXOpen.PointList:
        """
        Getter for property: ( NXOpen.PointList) PointList
         Returns the point list   
            
         
        """
        pass
    def CreateValidPointsOnPaths(self, pointLocs: List[NXOpen.Point3d]) -> Tuple[List[Path], List[NXOpen.Point]]:
        """
         This function will get all the paths stored in NXOpen.Routing.ManualRouteBuilder and 
                    will create point for any location which lies on any of the paths. Newly created points will be returned
                    as result. It will also return the filter paths found using given locations. 
         Returns A tuple consisting of (filterPaths, validPoints). 
         - filterPaths is:  Path List[NXOp.
         - validPoints is:  NXOpen.Point Li.

        """
        pass
    def CyclePaths(self) -> None:
        """
         Cycle paths through filter paths array to enable user select path for routing. 
        """
        pass
    def FindPaths(self) -> None:
        """
         Call this immediately after creating the Manual Route Builder to find all the possible paths. 
        """
        pass
    def FindPathsFromMultiplePoints(self, points: List[NXOpen.Point]) -> Tuple[List[Path], bool]:
        """
         This function returns all possible paths which are passing through all the given points. 
         Returns A tuple consisting of (paths, foundPath). 
         - paths is:  Path List[NXOp.
         - foundPath is: bool.

        """
        pass
    def GetFilterPaths(self) -> List[Path]:
        """
         This function gets filter paths from builder. These paths are those which passes through selected points
                    in point list.
         Returns filterPaths ( Path List[NXOp): .
        """
        pass
    def GetHighlightPath(self) -> Path:
        """
         This function returns currently highlighted path stored in builder 
         Returns path ( Path NXOpen): .
        """
        pass
    def GetPaths(self) -> List[Path]:
        """
         This function returns all possible paths for stockDevice stored in builder. 
         Returns paths ( Path List[NXOp): .
        """
        pass
    def SetFilterPaths(self, filterPaths: List[Path]) -> None:
        """
          
        """
        pass
    def SetHighlightPath(self, path: Path) -> None:
        """
         This function sets highlight path amongst all paths, and this highlight path only
                     will be used for routing the stock device 
        """
        pass
    def UpdateFilterPaths(self, point: NXOpen.Point) -> bool:
        """
         This function updates the filter paths in builder, using the given selected point. 
                    It checks all the filter paths stored in builder, and finds paths passing through given point.
                    Then it updates filter paths accordingly in builder. 
         Returns foundPath (bool): .
        """
        pass
import NXOpen
class MergeStocksBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.MergeStocksBuilder
        Builder for merging routing stocks ( including space reservation stocks ). """
    @property
    def CandidateStockCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) CandidateStockCollector
         Returns a collector object that holds candidate stocks to be merged with target stock.  
            
         
        """
        pass
    @property
    def TargetStockCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) TargetStockCollector
         Returnsa collector object that holds target stock for merge operation.  
           Candidate stocks will be merged with this stock , if possible   
         
        """
        pass
class Method(Enum):
    """
    Members Include: 
     |EntireSegments|  Cover all given segments 
     |Interval|  Cover the given segments intermittently 
     |PointToPoint|  Cover the given segments from one point to another 
     |PointAndLength|  Cover the given segments a point for a length 

    """
    EntireSegments: int
    Interval: int
    PointToPoint: int
    PointAndLength: int
    @staticmethod
    def ValueOf(value: int) -> Method:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class MiterCornerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.MiterCorner objects. """
    def AssignCorner(self, rcp: ControlPoint) -> MiterCorner:
        """
         Assigns a new miter corner to the given control point. 
         Returns new_crn ( MiterCorner NXOpen):  The newly created Miter Corner .
        """
        pass
    def GetMitersAssociatedToStock(self, stock: Stock) -> List[MiterCorner]:
        """
         Return miter corners referenced by the given NXOpen.Routing.Stock. 
         Returns miter_crn ( MiterCorner List[NXOp):  .
        """
        pass
class MiterCorner(Corner): 
    """ 
        This class defines a mitered corner.  That is a corner where the stock is extended and
        trimmed to form a flush connection at an angle.  When stock is updated, the stock solid
        body is extended and then trimmed to the miter plain.  The miter plane is defined as
        the plane that is perpendicular to the plane formed by the two linear segments
        that meet at the corner, and bisecting the angle between the two linear segments.
     """
    def GetSegments(self) -> List[ISegment]:
        """
         Gets the segments of the miter corner object. 
         Returns segments ( ISegment List[NXOp):  .
        """
        pass
import NXOpen
class MiteredBendCornerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.MiteredBendCorner objects. """
    def CreateCorner(self, rcp: ControlPoint, bend_radius: float, number_of_miters: int) -> MiteredBendCorner:
        """
         Create a mitered bend corner object at a Control Point. 
         Returns bend ( MiteredBendCorner NXOpen):  The new mitered bend corner. .
        """
        pass
    def GetBendAssociatedToSegment(self, segment: ISegment) -> BendCorner:
        """
         Enquire the Mitered Bend Corner that this segment represents.
                     ( can be returned, indicating that this segment does not
                     represent a Bend Corner.) 
         Returns corner ( BendCorner NXOpen):  Bend Corner that segment represents 
                                                 ( can be returned,indicating that 
                                                  segment does not represent a Bend Corner). .
        """
        pass
import NXOpen
class MiteredBendCorner(Corner): 
    """ 
        Computes a fillet curve between two linear segments to form a smooth
        bend transition from one segment to another that represents a mitered bend.
        A mitered bend is also known as "shrimp bend" or "corrugated bend".
     """
    @property
    def BendRadius(self) -> float:
        """
        Getter for property: (float) BendRadius
         Returns the bend radius of the corner.  
             
         
        """
        pass
    @BendRadius.setter
    def BendRadius(self, bend_radius: float):
        """
        Setter for property: (float) BendRadius
         Returns the bend radius of the corner.  
             
         
        """
        pass
    @property
    def NumberOfMiters(self) -> int:
        """
        Getter for property: (int) NumberOfMiters
         Returns the number of miters in the corner.  
             
         
        """
        pass
    @NumberOfMiters.setter
    def NumberOfMiters(self, number_of_miters: int):
        """
        Setter for property: (int) NumberOfMiters
         Returns the number of miters in the corner.  
             
         
        """
        pass
    def FindSideSegments(self) -> List[NXOpen.Curve]:
        """
         Returns the straight line segments attached to the fillet curve
                    of this bend corner.  
         Returns side_segs ( NXOpen.Curve Li):  the side segments. There will be from 0 to 2 
                                                       total side segments. .
        """
        pass
    def GetSegment(self) -> ISegment:
        """
         The bend segment following the fillet curve created for mitered bend. 
         Returns segment ( ISegment NXOpen):  .
        """
        pass
import NXOpen
class ModelTerminalsBuilder(NXOpen.Builder): 
    """ The Builder to ModelUnModel the Terminals """
    class CutBackLocationOption(Enum):
        """
        Members Include: 
         |FromCharacteristic|  FromCharacteristic 
         |UniformValue|  UniformValue 
         |IndividualCutbacks|  IndividualValue 

        """
        FromCharacteristic: int
        UniformValue: int
        IndividualCutbacks: int
        @staticmethod
        def ValueOf(value: int) -> ModelTerminalsBuilder.CutBackLocationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ExtensionValueOption(Enum):
        """
        Members Include: 
         |FromCharacteristic|  FromCharacteristic 
         |UniformValue|  UniformValue 
         |IndividualExtensions|  IndividualValue 

        """
        FromCharacteristic: int
        UniformValue: int
        IndividualExtensions: int
        @staticmethod
        def ValueOf(value: int) -> ModelTerminalsBuilder.ExtensionValueOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CutbackOption(self) -> ModelTerminalsBuilder.CutBackLocationOption:
        """
        Getter for property: ( ModelTerminalsBuilder.CutBackLocationOption NXOpen) CutbackOption
         Returns the cutback option   
            
         
        """
        pass
    @CutbackOption.setter
    def CutbackOption(self, cutbackOption: ModelTerminalsBuilder.CutBackLocationOption):
        """
        Setter for property: ( ModelTerminalsBuilder.CutBackLocationOption NXOpen) CutbackOption
         Returns the cutback option   
            
         
        """
        pass
    @property
    def ExtensionOption(self) -> ModelTerminalsBuilder.ExtensionValueOption:
        """
        Getter for property: ( ModelTerminalsBuilder.ExtensionValueOption NXOpen) ExtensionOption
         Returns the extension option   
            
         
        """
        pass
    @ExtensionOption.setter
    def ExtensionOption(self, extensionOption: ModelTerminalsBuilder.ExtensionValueOption):
        """
        Setter for property: ( ModelTerminalsBuilder.ExtensionValueOption NXOpen) ExtensionOption
         Returns the extension option   
            
         
        """
        pass
    @property
    def List(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) List
         Returns the list containing the terminals and their properties.  
            
         
        """
        pass
    @property
    def MultiPort(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) MultiPort
         Returns the  NXOpen::Routing::MultiPort  of the selected object  
            
         
        """
        pass
    @MultiPort.setter
    def MultiPort(self, port: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) MultiPort
         Returns the  NXOpen::Routing::MultiPort  of the selected object  
            
         
        """
        pass
    @property
    def PortSelection(self) -> SelectPort:
        """
        Getter for property: ( SelectPort NXOpen) PortSelection
         Returns the port selection   
            
         
        """
        pass
    @property
    def PreviewToggle(self) -> bool:
        """
        Getter for property: (bool) PreviewToggle
         Returns the preview   
            
         
        """
        pass
    @PreviewToggle.setter
    def PreviewToggle(self, preview: bool):
        """
        Setter for property: (bool) PreviewToggle
         Returns the preview   
            
         
        """
        pass
    def Model(self) -> None:
        """
          Model the selected Terminals  
        """
        pass
    def ModelAll(self) -> None:
        """
         Model all the terminals 
        """
        pass
    def UnModel(self) -> None:
        """
         Unmodel the selected terminals 
        """
        pass
    def UnModelAll(self) -> None:
        """
         Unmodel all of the terminals 
        """
        pass
import NXOpen
class MultiPortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.MultiPort objects. """
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, rotation_vector: NXOpen.Vector3d, rotation_object: NXOpen.DisplayableObject, clock_angle: float) -> MultiPort:
        """
         Creates a MultiPort with a rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d) -> MultiPort:
        """
         Creates a MultiPort with no rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, rotation_vector: NXOpen.Vector3d, rotation_object: NXOpen.DisplayableObject, clock_angle: float, axis: NXOpen.Axis, allowMultipleConnections: bool) -> MultiPort:
        """
         Creates a MultiPort with a rotation vector on an axis 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, derivation_object: NXOpen.Axis, allowMultipleConnections: bool) -> MultiPort:
        """
         Creates a MultiPort with no rotation vector on an axis 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, rotation_vector: NXOpen.Vector3d, rotation_object: NXOpen.DisplayableObject, clock_angle: float, point: NXOpen.Point) -> MultiPort:
        """
         Creates a MultiPort with a rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, point: NXOpen.Point) -> MultiPort:
        """
         Creates a MultiPort with no rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, rotation_vector: NXOpen.Vector3d, rotation_object: NXOpen.DisplayableObject, clock_angle: float, axis: NXOpen.Axis) -> MultiPort:
        """
         Creates a MultiPort with a rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, derivation_object: NXOpen.Axis) -> MultiPort:
        """
         Creates a MultiPort with no rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, rotation_vector: NXOpen.Vector3d, rotation_object: NXOpen.DisplayableObject, clock_angle: float, allowMultipleConnections: bool) -> MultiPort:
        """
         Creates a MultiPort with a rotation vector at an absolute location 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, allowMultipleConnections: bool) -> MultiPort:
        """
         Creates a MultiPort with no rotation vector at an absolute location 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, rotation_vector: NXOpen.Vector3d, rotation_object: NXOpen.DisplayableObject, clock_angle: float, point: NXOpen.Point, allowMultipleConnections: bool) -> MultiPort:
        """
         Creates a MultiPort with a rotation vector at a point 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
    @overload
    def CreateMultiPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, point: NXOpen.Point, allowMultipleConnections: bool) -> MultiPort:
        """
         Creates a MultiPort with no rotation vector at a point 
         Returns multi_port ( MultiPort NXOpen):  .
        """
        pass
import NXOpen
class MultiPort(Port): 
    """ Represents a NXOpen.Routing.MultiPort.
        These objects are ones to which segments are routed to or from when
        creating a routing path.
      """
    @property
    def Axis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @Axis.setter
    def Axis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @property
    def CutbackLengthObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @CutbackLengthObject.setter
    def CutbackLengthObject(self, cutback_length: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @property
    def EngagementObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @EngagementObject.setter
    def EngagementObject(self, engagement: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @property
    def ForwardExtensionObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @ForwardExtensionObject.setter
    def ForwardExtensionObject(self, forward_extension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    def AddTerminalPorts(self, terminal_ports: List[TerminalPort]) -> None:
        """
         Adds terminal ports to this NXOpen.Routing.MultiPort.  
        """
        pass
    def AddVirtualPorts(self, virtual_ports: List[str]) -> None:
        """
         Adds new virtual ports to this NXOpen.Routing.MultiPort 
        """
        pass
    def GetTerminalPorts(self) -> List[TerminalPort]:
        """
         Gets the terminal ports that are associated with this NXOpen.Routing.MultiPort 
         Returns terminal_ports ( TerminalPort List[NXOp):  Terminal Ports associated with this Multi Port .
        """
        pass
    def GetVirtualPorts(self) -> List[str]:
        """
         Gets the virtual ports that are associated with this NXOpen.Routing.MultiPort 
         Returns virtual_ports (List[str]):  Virtual Port names associated with this Multi Port .
        """
        pass
    def RemoveTerminalPorts(self, terminal_ports: List[TerminalPort]) -> None:
        """
         Removes terminal ports from this NXOpen.Routing.MultiPort.  
        """
        pass
    def RemoveVirtualPorts(self, virtual_ports: List[str]) -> None:
        """
         Removes virtual ports from this NXOpen.Routing.MultiPort.  
        """
        pass
    def SetVirtualPorts(self, virtual_ports: List[str]) -> None:
        """
         Sets the virtual ports that are associated with this NXOpen.Routing.MultiPort 
        """
        pass
import NXOpen
class NamePluginData(NXOpen.TaggedObject): 
    """ An abstract data object used by both the component name and assembly name plugins.

        For more information, see Routing.ComponentNamePluginData and
        Routing.AssemblyNamePluginData.
    """
    @property
    def ManagedModeFolderName(self) -> str:
        """
        Getter for property: (str) ManagedModeFolderName
         Returns the folder in which to show the component part in managed mode.  
             
         
        """
        pass
    @ManagedModeFolderName.setter
    def ManagedModeFolderName(self, folderName: str):
        """
        Setter for property: (str) ManagedModeFolderName
         Returns the folder in which to show the component part in managed mode.  
             
         
        """
        pass
    @property
    def ManagedModeItemDescription(self) -> str:
        """
        Getter for property: (str) ManagedModeItemDescription
         Returns the item description for the component part when in managed mode.  
             
         
        """
        pass
    @ManagedModeItemDescription.setter
    def ManagedModeItemDescription(self, itemDescription: str):
        """
        Setter for property: (str) ManagedModeItemDescription
         Returns the item description for the component part when in managed mode.  
             
         
        """
        pass
    @property
    def ManagedModeItemName(self) -> str:
        """
        Getter for property: (str) ManagedModeItemName
         Returns the item name and part name (DB_PART_NAME) for the component part when in managed mode.  
             
         
        """
        pass
    @ManagedModeItemName.setter
    def ManagedModeItemName(self, itemName: str):
        """
        Setter for property: (str) ManagedModeItemName
         Returns the item name and part name (DB_PART_NAME) for the component part when in managed mode.  
             
         
        """
        pass
    @property
    def ManagedModeItemRevision(self) -> str:
        """
        Getter for property: (str) ManagedModeItemRevision
         Returns the item revision for the component part when in managed mode.  
             
         
        """
        pass
    @ManagedModeItemRevision.setter
    def ManagedModeItemRevision(self, itemRevision: str):
        """
        Setter for property: (str) ManagedModeItemRevision
         Returns the item revision for the component part when in managed mode.  
             
         
        """
        pass
    @property
    def ManagedModeItemType(self) -> str:
        """
        Getter for property: (str) ManagedModeItemType
         Returns the item type for the component part when in managed mode.  
             
         
        """
        pass
    @ManagedModeItemType.setter
    def ManagedModeItemType(self, itemType: str):
        """
        Setter for property: (str) ManagedModeItemType
         Returns the item type for the component part when in managed mode.  
             
         
        """
        pass
    @property
    def NativeFileName(self) -> str:
        """
        Getter for property: (str) NativeFileName
         Returns the the name for the component part when in native mode and
                    the part number (DB_PART_NO) in managed mode.  
             
         
        """
        pass
    @NativeFileName.setter
    def NativeFileName(self, fileName: str):
        """
        Setter for property: (str) NativeFileName
         Returns the the name for the component part when in native mode and
                    the part number (DB_PART_NO) in managed mode.  
             
         
        """
        pass
    @property
    def NativePath(self) -> str:
        """
        Getter for property: (str) NativePath
         Returns the path under which to place the component part when in native mode.  
          
                    An empty string means use the current directory.
                    This may be a relative path from the current directory or an absolute path.
                  
         
        """
        pass
    @NativePath.setter
    def NativePath(self, nativePath: str):
        """
        Setter for property: (str) NativePath
         Returns the path under which to place the component part when in native mode.  
          
                    An empty string means use the current directory.
                    This may be a relative path from the current directory or an absolute path.
                  
         
        """
        pass
import NXOpen
class NamingPatternBuilder(NXOpen.Builder): 
    """ Builder for selecting a naming pattern for terminal arrays. """
    class PatternTypes(Enum):
        """
        Members Include: 
         |Number| 
         |UpperChar| 
         |LowerChar| 

        """
        Number: int
        UpperChar: int
        LowerChar: int
        @staticmethod
        def ValueOf(value: int) -> NamingPatternBuilder.PatternTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndString(self) -> str:
        """
        Getter for property: (str) EndString
         Returns the end string   
            
         
        """
        pass
    @EndString.setter
    def EndString(self, endString: str):
        """
        Setter for property: (str) EndString
         Returns the end string   
            
         
        """
        pass
    @property
    def PatternType(self) -> NamingPatternBuilder.PatternTypes:
        """
        Getter for property: ( NamingPatternBuilder.PatternTypes NXOpen) PatternType
         Returns the pattern type   
            
         
        """
        pass
    @PatternType.setter
    def PatternType(self, patternType: NamingPatternBuilder.PatternTypes):
        """
        Setter for property: ( NamingPatternBuilder.PatternTypes NXOpen) PatternType
         Returns the pattern type   
            
         
        """
        pass
    @property
    def Prefix(self) -> str:
        """
        Getter for property: (str) Prefix
         Returns the prefix   
            
         
        """
        pass
    @Prefix.setter
    def Prefix(self, prefix: str):
        """
        Setter for property: (str) Prefix
         Returns the prefix   
            
         
        """
        pass
    @property
    def StartString(self) -> str:
        """
        Getter for property: (str) StartString
         Returns the start string   
            
         
        """
        pass
    @StartString.setter
    def StartString(self, startString: str):
        """
        Setter for property: (str) StartString
         Returns the start string   
            
         
        """
        pass
    @property
    def Suffix(self) -> str:
        """
        Getter for property: (str) Suffix
         Returns the suffix   
            
         
        """
        pass
    @Suffix.setter
    def Suffix(self, suffix: str):
        """
        Setter for property: (str) Suffix
         Returns the suffix   
            
         
        """
        pass
class ObjectRelationship(RootObject): 
    """
         Represents a relationship between Routing objects.
       
       
         ObjectRelationship is the abstract base class for NXOpen.Routing.InterfaceTerminalRelationshipBase
         and NXOpen.Routing.DeviceRelationship.  This class is reserved for future use.
        
    """
    pass
import NXOpen
class OffsetPathCollection(NXOpen.TaggedObjectCollection): 
    """ The Routing OffsetPath object is a list of segments in a route. It also
        contains the beginning and ending control point for the path.
     """
    class BendType(Enum):
        """
        Members Include: 
         |MaintainRadius|  Maintain Radius 
         |MaintainCenter|  Maintain Center 
         |MaximumBendTypes|   

        """
        MaintainRadius: int
        MaintainCenter: int
        MaximumBendTypes: int
        @staticmethod
        def ValueOf(value: int) -> OffsetPathCollection.BendType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def ConvertOffsetPaths(self, master_offset_path: OffsetPath) -> None:
        """
         Converts an offset path into NXOpen.Positioning.Constraint 
                    objects applied to the copied routing objects.  Converts the input
                    master offset path as well as all of the children offset paths of
                    the input master offset path.
                    
                    The NXOpen.Routing.OffsetPath is incompatible with segments 
                    created using the NXOpen.Routing.SegmentManager.CreateConstrainedSegment
                    or to any segments that have NXOpen.Positioning.Constraint objects
                    applied to them.  This routine makes the path parallel and associative to
                    each other using constraints rather than the NXOpen.Routing.OffsetPath
                    objects.  The converted offset path objects are logged for delete, the next
                    call to NXOpen.Update.DoUpdate will delete the offset path
                    objects.
                
        """
        pass
    def CreateCircularOffsetPath(self, segments: List[ISegment], allStock: bool, specStocks: List[Stock], maintain_stock: bool, copy_bend_corners: bool, maintain: OffsetPathCollection.BendType, use_minimum_bend_ratio: bool, minimum_bend_ratio: float, minimum_bend_radius: float, delete_all_duplicates: bool, create_associative_paths: bool, pattern_x_vector: NXOpen.Vector3d, pattern_y_vector: NXOpen.Vector3d, pattern_axis_end_point: NXOpen.Point3d, pattern_start_angle: float, radial_offset: float, n_paths: int, total_angle: float) -> Tuple[OffsetPath, List[OffsetPath]]:
        """
         Creates a circular offset path. 
         Returns A tuple consisting of (master_offset_path, slave_paths_created). 
         - master_offset_path is:  OffsetPath NXOpen. The created master offset path .
         - slave_paths_created is:  OffsetPath List[NXOp. The created slave offset paths .

        """
        pass
    def CreateRectangularOffsetPath(self, segments: List[ISegment], allStock: bool, specStocks: List[Stock], maintain_stock: bool, copy_bend_corners: bool, maintain: OffsetPathCollection.BendType, use_minimum_bend_ratio: bool, minimum_bend_ratio: float, minimum_bend_radius: float, delete_all_duplicates: bool, create_associative_paths: bool, pattern_x_vector: NXOpen.Vector3d, pattern_y_vector: NXOpen.Vector3d, pattern_axis_end_point: NXOpen.Point3d, pattern_start_angle: float, row_offset: float, column_offset: float, n_rows: int, n_columns: int, master_row: int, master_column: int) -> Tuple[OffsetPath, List[OffsetPath]]:
        """
         Creates a rectangular offset path.
         Returns A tuple consisting of (master_offset_path, slave_paths_created). 
         - master_offset_path is:  OffsetPath NXOpen. The created master offset path .
         - slave_paths_created is:  OffsetPath List[NXOp. The created slave offset paths .

        """
        pass
import NXOpen
class OffsetPath(NXOpen.NXObject): 
    """ The Routing OffsetPath object is the set of information needed to define an offset route.
     """
    @property
    def BendRadius(self) -> float:
        """
        Getter for property: (float) BendRadius
         Returns the bend radius for an offset object.  
             
         
        """
        pass
    @BendRadius.setter
    def BendRadius(self, radius: float):
        """
        Setter for property: (float) BendRadius
         Returns the bend radius for an offset object.  
             
         
        """
        pass
    @property
    def BendRatio(self) -> float:
        """
        Getter for property: (float) BendRatio
         Returns the bend ratio for an offset object.  
             
         
        """
        pass
    @BendRatio.setter
    def BendRatio(self, ratio: float):
        """
        Setter for property: (float) BendRatio
         Returns the bend ratio for an offset object.  
             
         
        """
        pass
    @property
    def ControlPointEnd(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointEnd.setter
    def ControlPointEnd(self, end: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @property
    def ControlPointStart(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointStart.setter
    def ControlPointStart(self, start: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    @property
    def CopyCornerFlag(self) -> bool:
        """
        Getter for property: (bool) CopyCornerFlag
         Returns the copy corner flag for an offset object.  
             
         
        """
        pass
    @CopyCornerFlag.setter
    def CopyCornerFlag(self, copy_corner: bool):
        """
        Setter for property: (bool) CopyCornerFlag
         Returns the copy corner flag for an offset object.  
             
         
        """
        pass
    @property
    def IsMaster(self) -> bool:
        """
        Getter for property: (bool) IsMaster
         Returns the isMaster state for this offset object.  
             
         
        """
        pass
    @IsMaster.setter
    def IsMaster(self, is_master: bool):
        """
        Setter for property: (bool) IsMaster
         Returns the isMaster state for this offset object.  
             
         
        """
        pass
    @property
    def IsSlave(self) -> bool:
        """
        Getter for property: (bool) IsSlave
         Returns the isSlave state for this offset object.  
             
         
        """
        pass
    @IsSlave.setter
    def IsSlave(self, is_slave: bool):
        """
        Setter for property: (bool) IsSlave
         Returns the isSlave state for this offset object.  
             
         
        """
        pass
    @property
    def MaintainStockFlag(self) -> bool:
        """
        Getter for property: (bool) MaintainStockFlag
         Returns the use maintain stock flag for an offset object.  
             
         
        """
        pass
    @MaintainStockFlag.setter
    def MaintainStockFlag(self, maintain_stock: bool):
        """
        Setter for property: (bool) MaintainStockFlag
         Returns the use maintain stock flag for an offset object.  
             
         
        """
        pass
    @property
    def OffsetVector(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) OffsetVector
         Returns the vector for an offset object.  
             
         
        """
        pass
    @OffsetVector.setter
    def OffsetVector(self, vector: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) OffsetVector
         Returns the vector for an offset object.  
             
         
        """
        pass
    @property
    def UseBendRatio(self) -> bool:
        """
        Getter for property: (bool) UseBendRatio
         Returns the use bend ratio flag for an offset object.  
             
         
        """
        pass
    @UseBendRatio.setter
    def UseBendRatio(self, ratio_state: bool):
        """
        Setter for property: (bool) UseBendRatio
         Returns the use bend ratio flag for an offset object.  
             
         
        """
        pass
    def GetMasterPath(self) -> IPath:
        """
         The master path object for this offset object. 
         Returns master_path ( IPath NXOpen):  master path for this offset object .
        """
        pass
    def GetOffsetPathSegments(self) -> List[ISegment]:
        """
         The path segments for an offset object. 
         Returns segments ( ISegment List[NXOp):  segment list for the offset object .
        """
        pass
    def GetOffsetPaths(self) -> List[IPath]:
        """
         Returns the list of all of the offset paths for a master path 
         Returns slave_paths ( IPath List[NXOp):  list of all of the offset paths in this master object .
        """
        pass
    def GetOffsetReferenceAxes(self) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, NXOpen.Vector3d]:
        """
         The reference axes for an offset object. 
         Returns A tuple consisting of (orgin, x_vector, y_vector). 
         - orgin is:  NXOpen.Point3d. origin for the offset object           .
         - x_vector is:  NXOpen.Vector3d. X reference axes for the offset object .
         - y_vector is:  NXOpen.Vector3d. Y reference axes for the offset object .

        """
        pass
    def RemovePathAssociativityFromParent(self) -> None:
        """
         Breaks the associativity of a child ( slave ) path to its parent ( master ) path. 
        """
        pass
    def RemovePathAssociativityToImmediateChildren(self) -> None:
        """
         Breaks the associativity of a parent ( master ) path to 
                    its immediate children ( slave ) paths. 
        """
        pass
    def SetMasterPath(self, master_path: IPath) -> None:
        """
         The master path object for this offset object. 
        """
        pass
    def SetOffsetPathSegments(self, segments: List[ISegment]) -> None:
        """
         The path segments for an offset object. 
        """
        pass
    def SetOffsetReferenceAxes(self, orgin: NXOpen.Point3d, x_vector: NXOpen.Vector3d, y_vector: NXOpen.Vector3d) -> None:
        """
         The reference axes for an offset object. 
        """
        pass
class Operation(Enum):
    """
    Members Include: 
     |Create|  Create overstock 
     |Edit|  Edit existing overstock 

    """
    Create: int
    Edit: int
    @staticmethod
    def ValueOf(value: int) -> Operation:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class OverstockApplicationCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.OverstockApplication objects. """
    @overload
    def ConvertOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], overstock_part: CharacteristicList, req_opt_charx_list: CharacteristicList, wrap_value: NXOpen.Expression, overstocks: List[Overstock]) -> OverstockApplication:
        """
         Converts an existing NXOpen.Routing.Overstock to
                    Routing.Method.EntireSegments overstock.
                
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    @overload
    def ConvertOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], start_offset: NXOpen.Expression, end_offset: NXOpen.Expression, piece_length: NXOpen.Expression, gap: NXOpen.Expression, number_of_pieces: NXOpen.Expression, start_point: NXOpen.Point, overstock_part: CharacteristicList, req_opt_charx_list: CharacteristicList, wrap_value: NXOpen.Expression, overstocks: List[Overstock]) -> OverstockApplication:
        """
         Converts an existing NXOpen.Routing.Overstock to
                    Routing.Method.Interval overstock.
                
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    @overload
    def ConvertOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], start_point: NXOpen.Point, end_point: NXOpen.Point, overstock_part: CharacteristicList, req_opt_charx_list: CharacteristicList, wrap_value: NXOpen.Expression, overstocks: List[Overstock]) -> OverstockApplication:
        """
         Converts an existing NXOpen.Routing.Overstock to
                    Routing.Method.PointToPoint overstock. 
                
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    @overload
    def ConvertOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], defining_point: NXOpen.Point, defining_direction: PointDefinition, piece_length: NXOpen.Expression, overstock_part: CharacteristicList, req_opt_charx_list: CharacteristicList, wrap_value: NXOpen.Expression, overstocks: List[Overstock]) -> OverstockApplication:
        """
         Converts an existing NXOpen.Routing.Overstock to
                    Routing.Method.PointAndLength overstock. 
                
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    @overload
    def CreateOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], overstock_part: CharacteristicList, stock_wrap_type: WrapApplicationType, wrap_value: NXOpen.Expression) -> OverstockApplication:
        """
         Creates the Routing.Method.EntireSegments
                    overstock. Specify the type of overstock to create (for example fixed cross section,
                    wrapped, sleeved, or flagged) in the overstock part characteristic list using
                    the "OVERSTOCK_TYPE" characteristic. Spot wrapping is not allowed for entire segments. 
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    @overload
    def CreateOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], start_offset: NXOpen.Expression, end_offset: NXOpen.Expression, piece_length: NXOpen.Expression, gap: NXOpen.Expression, number_of_pieces: NXOpen.Expression, start_point: NXOpen.Point, overstock_part: CharacteristicList, stock_wrap_type: WrapApplicationType, wrap_value: NXOpen.Expression) -> OverstockApplication:
        """
         Creates an NXOpen.Routing.OverstockApplication using the Interval method of application.
                    Specify the type of overstock to create (for example fixed cross section,
                    wrapped, sleeved, or flagged) in the overstock part characteristic list using
                    the "OVERSTOCK_TYPE" characteristic. 
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    @overload
    def CreateOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], start_point: NXOpen.Point, end_point: NXOpen.Point, overstock_part: CharacteristicList, stock_type: WrapApplicationType, wrap_value: NXOpen.Expression) -> OverstockApplication:
        """
         Creates an NXOpen.Routing.OverstockApplication using the
                    Point to Point method of application. Specify the type of overstock to create (for example fixed cross section,
                    wrapped, sleeved, or flagged) in the overstock part characteristic list using
                    the "OVERSTOCK_TYPE" characteristic.  
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    @overload
    def CreateOverstockApplication(self, start_control_point: ControlPoint, segments: List[ISegment], stocks: List[Stock], defining_point: NXOpen.Point, defining_direction: PointDefinition, piece_length: NXOpen.Expression, overstock_part: CharacteristicList, stock_wrap_type: WrapApplicationType, wrap_value: NXOpen.Expression) -> OverstockApplication:
        """
         Creates the Routing.Method.PointAndLength
                    overstock by the Point and Length method. Specify the type of overstock to create (for example fixed cross section,
                    wrapped, sleeved, or flagged) in the overstock part characteristic list using
                    the "OVERSTOCK_TYPE" characteristic. 
         Returns overstock_application ( OverstockApplication NXOpen):  .
        """
        pass
    def ReplaceOverstockApplication(self, charxMap: CharacteristicList, overstock: Overstock) -> None:
        """
         Replace current selected overstock NXOpen.Routing.Overstock with 
                    the chosen overstock. It is only used by UI. 
                
        """
        pass
import NXOpen
class OverstockApplication(NXOpen.NXObject): 
    """ Represents a collection of NXOpen.Routing.OverstockApplication objects. """
    @property
    def Definition(self) -> Method:
        """
        Getter for property: ( Method NXOpen) Definition
         Returns  the method used to define the overstock application.  
             
         
        """
        pass
    @property
    def EndOfPath(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) EndOfPath
         Returns  the end control point of the path over which the overstock is applied.  
             
         
        """
        pass
    @property
    def EndPointOfOverstock(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPointOfOverstock
         Returns  the end point of overstock on the path.  
            Used in the  NXOpen::Routing::Method::PointToPoint  definition method.   
         
        """
        pass
    @property
    def MidPointOfOverstock(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) MidPointOfOverstock
         Returns  the mid point of overstock on the path.  
            Used in  NXOpen::Routing::Method::PointAndLength  definition
                     method.   
         
        """
        pass
    @property
    def StartOfPath(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) StartOfPath
         Returns  the start control point of the path over which the overstock is applied.  
             
         
        """
        pass
    @property
    def StartPointOfOverstock(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPointOfOverstock
         Returns  the start point of overstock on the path.  
            Used in
                      NXOpen::Routing::Method::Interval , 
                      NXOpen::Routing::Method::PointToPoint , and 
                      NXOpen::Routing::Method::PointAndLength 
                     definition methods.   
         
        """
        pass
    def GetCoveredStocks(self) -> List[Stock]:
        """
         Gets the NXOpen.Routing.Stock and
                    NXOpen.Routing.OverstockApplication that this
                    NXOpen.Routing.OverstockApplication covers. 
         Returns covered_stocks ( Stock List[NXOp):  Covered stocks.  .
        """
        pass
    def GetCrossSections(self) -> List[NXOpen.Curve]:
        """
         Gets the cross sections controlled by this object.  These
                    cross sections could be used for a custom bundling algorithm.  
         Returns cross_sections ( NXOpen.Curve Li):  Cross sections.  .
        """
        pass
    def GetEndParameter(self) -> float:
        """
         Returns the end offset. Only useful for the
                    NXOpen.Routing.Method.Interval,
                    NXOpen.Routing.Method.PointToPoint, and
                    NXOpen.Routing.Method.PointAndLength
                    methods.
                    The offset is always returned as a percentage from 0 to 1 along the path of all the
                    segments this overstock covers from the start of the segment.
                
         Returns end_offset (float): .
        """
        pass
    def GetOverstocks(self) -> List[Overstock]:
        """
         Returns NXOpen.Routing.Overstock objects covering this NXOpen.Routing.OverstockApplication. 
         Returns overstocks ( Overstock List[NXOp):  .
        """
        pass
    def GetSegments(self) -> List[ISegment]:
        """
          Returns the set of segments over which the overstock is applied. 
         Returns segments ( ISegment List[NXOp):  the contiguous set of segments this overstock
                                                                                      application is covering.  .
        """
        pass
    def GetStartParameter(self) -> float:
        """
         Returns the start offset. Only useful the for 
                    NXOpen.Routing.Method.Interval, 
                    NXOpen.Routing.Method.PointToPoint, and 
                    NXOpen.Routing.Method.PointAndLength
                    methods.
                    The offset is always returned as a percentage from 0 to 1 along the path of all the
                    segments this overstock covers from the start of the segment.
                
         Returns start_offset (float): .
        """
        pass
    def SetCoveredStocks(self, covered_stocks: List[Stock]) -> None:
        """
         Sets the NXOpen.Routing.Stock and
                    NXOpen.Routing.OverstockApplication that this
                    NXOpen.Routing.OverstockApplication covers. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class OverstockBuilder(NXOpen.Builder): 
    """ Builder for creatingediting overstocks.
        Create Overstock: This builder takes a set of segments and overstock and assign the 
        the overstock on the segments depending on the applicatio method and parameters
        chosen by the user.
        Edit Overstock: This builder takes in the selected overstock to edit as input and 
        redefines the overstock with the modified(by the user) parameters.
    """
    class ApplicationType(Enum):
        """
        Members Include: 
         |EntireSegments|  Entire Segments 
         |Interval|  Interval 
         |PointToPoint|  Point To Point 
         |PointAndLength|  Point And Length 

        """
        EntireSegments: int
        Interval: int
        PointToPoint: int
        PointAndLength: int
        @staticmethod
        def ValueOf(value: int) -> OverstockBuilder.ApplicationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PointType(Enum):
        """
        Members Include: 
         |Start|  Start 
         |Middle|  Middle 
         |End|  End 

        """
        Start: int
        Middle: int
        End: int
        @staticmethod
        def ValueOf(value: int) -> OverstockBuilder.PointType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WrapType(Enum):
        """
        Members Include: 
         |OverlapSpiral|  Overlap Spiral 
         |Spot|  Spot 
         |StripedSpiral|  Striped Spiral 
         |Unknown| 

        """
        OverlapSpiral: int
        Spot: int
        StripedSpiral: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> OverstockBuilder.WrapType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ApplicationMethod(self) -> OverstockBuilder.ApplicationType:
        """
        Getter for property: ( OverstockBuilder.ApplicationType NXOpen) ApplicationMethod
         Returns the application method for overstock assignment.  
           It defines the way in 
                    which to create piggyback segment for overstock.   
         
        """
        pass
    @ApplicationMethod.setter
    def ApplicationMethod(self, applicationMethod: OverstockBuilder.ApplicationType):
        """
        Setter for property: ( OverstockBuilder.ApplicationType NXOpen) ApplicationMethod
         Returns the application method for overstock assignment.  
           It defines the way in 
                    which to create piggyback segment for overstock.   
         
        """
        pass
    @property
    def DefiningPoint(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) DefiningPoint
         Returns the defining point for   NXOpen::Routing::OverstockBuilder::ApplicationTypePointAndLength   method.  
            
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance over which the pieces of overstock can possibly range for
                     NXOpen::Routing::OverstockBuilder::ApplicationTypeInterval 
                    method.  
            
         
        """
        pass
    @property
    def DistanceLock(self) -> bool:
        """
        Getter for property: (bool) DistanceLock
         Returns the distance lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @DistanceLock.setter
    def DistanceLock(self, distanceLock: bool):
        """
        Setter for property: (bool) DistanceLock
         Returns the distance lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @property
    def EndOffset(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndOffset
         Returns the end offset value for  NXOpen::Routing::OverstockBuilder::ApplicationTypeInterval 
                    method.  
           It defins the MINIMUM distance from the end of the path to place 
                    the last piece of overstock.   
         
        """
        pass
    @property
    def EndOffsetLock(self) -> bool:
        """
        Getter for property: (bool) EndOffsetLock
         Returns the end offset lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @EndOffsetLock.setter
    def EndOffsetLock(self, endOffsetLock: bool):
        """
        Setter for property: (bool) EndOffsetLock
         Returns the end offset lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @property
    def EndPoint(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndPoint
         Returns the end point that defines the end of the overstock for 
                     NXOpen::Routing::OverstockBuilder::ApplicationTypePointToPoint 
                    method.  
             
         
        """
        pass
    @property
    def FlipStock(self) -> bool:
        """
        Getter for property: (bool) FlipStock
         Returns the stock flip flag   
            
         
        """
        pass
    @FlipStock.setter
    def FlipStock(self, flipStock: bool):
        """
        Setter for property: (bool) FlipStock
         Returns the stock flip flag   
            
         
        """
        pass
    @property
    def Gap(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Gap
         Returns the gap from the end of one piece of overstock to the start of the next piece
                    of overstock for  NXOpen::Routing::OverstockBuilder::ApplicationTypeInterval  method.  
             
         
        """
        pass
    @property
    def GapDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GapDistance
         Returns the gap distance if the  NXOpen::Routing::OverstockBuilder::WrapType 
                    is  NXOpen::Routing::OverstockBuilder::WrapTypeStripedSpiral    
            
         
        """
        pass
    @property
    def GapLock(self) -> bool:
        """
        Getter for property: (bool) GapLock
         Returns the gap lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @GapLock.setter
    def GapLock(self, gapLock: bool):
        """
        Setter for property: (bool) GapLock
         Returns the gap lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @property
    def IntervalPieceLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IntervalPieceLength
         Returns the length of the overstock pieces for  NXOpen::Routing::OverstockBuilder::ApplicationTypeInterval 
                    method.  
           If the overstock type is Wrapped, and the wrap method is set to Spot,
                    the Piece Length is always the width of the overstock and is locked.   
         
        """
        pass
    @property
    def NumberOfPieces(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfPieces
         Returns the number of pieces of overstock to place along the path for 
                     NXOpen::Routing::OverstockBuilder::ApplicationTypeInterval 
                    method.  
             
         
        """
        pass
    @property
    def NumberOfPiecesLock(self) -> bool:
        """
        Getter for property: (bool) NumberOfPiecesLock
         Returns the number of pieces lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @NumberOfPiecesLock.setter
    def NumberOfPiecesLock(self, numberOfPiecesLock: bool):
        """
        Setter for property: (bool) NumberOfPiecesLock
         Returns the number of pieces lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @property
    def NumberOfWraps(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfWraps
         Returns the number of wraps if the  NXOpen::Routing::OverstockBuilder::WrapType 
                    is  NXOpen::Routing::OverstockBuilder::WrapTypeSpot    
            
         
        """
        pass
    @property
    def OverlapPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OverlapPercentage
         Returns the percentage overlap if the  NXOpen::Routing::OverstockBuilder::WrapType 
                    is  NXOpen::Routing::OverstockBuilder::WrapTypeOverlapSpiral    
            
         
        """
        pass
    @property
    def PathCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) PathCurve
         Returns the path curve that is used to specify overstock defining points.  
             
         
        """
        pass
    @property
    def PieceLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PieceLength
         Returns the length over which overstock piece to be assigned for 
                     NXOpen::Routing::OverstockBuilder::ApplicationTypePointAndLength  method.  
            
         
        """
        pass
    @property
    def PieceLengthLock(self) -> bool:
        """
        Getter for property: (bool) PieceLengthLock
         Returns the piece length lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @PieceLengthLock.setter
    def PieceLengthLock(self, pieceLengthLock: bool):
        """
        Setter for property: (bool) PieceLengthLock
         Returns the piece length lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path.   
         
        """
        pass
    @property
    def PointDefines(self) -> OverstockBuilder.PointType:
        """
        Getter for property: ( OverstockBuilder.PointType NXOpen) PointDefines
         Returns the defining point location which can be any of  NXOpen::Routing::OverstockBuilder::PointType 
                    for   NXOpen::Routing::OverstockBuilder::ApplicationTypePointAndLength   method.  
            
         
        """
        pass
    @PointDefines.setter
    def PointDefines(self, pointDefines: OverstockBuilder.PointType):
        """
        Setter for property: ( OverstockBuilder.PointType NXOpen) PointDefines
         Returns the defining point location which can be any of  NXOpen::Routing::OverstockBuilder::PointType 
                    for   NXOpen::Routing::OverstockBuilder::ApplicationTypePointAndLength   method.  
            
         
        """
        pass
    @property
    def RotationValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationValue
         Returns the rotation value.  
           Determines the rotation angle of the overstock.   
         
        """
        pass
    @property
    def SegmentCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SegmentCollector
         Returns the routing object collector to collect the segments to assign overstock to.  
            
         
        """
        pass
    @property
    def StartOffset(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartOffset
         Returns the start offset value for  NXOpen::Routing::OverstockBuilder::ApplicationTypeInterval 
                    method.  
           It defines the distance from the beginning of the path to place the 
                    first piece of overstock.   
         
        """
        pass
    @property
    def StartOffsetLock(self) -> bool:
        """
        Getter for property: (bool) StartOffsetLock
         Returns the start offset lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path   
         
        """
        pass
    @StartOffsetLock.setter
    def StartOffsetLock(self, startOffsetLock: bool):
        """
        Setter for property: (bool) StartOffsetLock
         Returns the start offset lock state.  
           If TRUE, changing the parameters will change other
                    unlocked parameters to fit overstock along the selected path   
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartPoint
         Returns the start point that defines the start of the overstock for 
                     NXOpen::Routing::OverstockBuilder::ApplicationTypePointToPoint 
                    method.  
             
         
        """
        pass
    @property
    def StockAnchor(self) -> str:
        """
        Getter for property: (str) StockAnchor
         Returns the  NXOpen::Routing::Anchor  name associated with the overstock.  
             
         
        """
        pass
    @StockAnchor.setter
    def StockAnchor(self, anchorName: str):
        """
        Setter for property: (str) StockAnchor
         Returns the  NXOpen::Routing::Anchor  name associated with the overstock.  
             
         
        """
        pass
    @property
    def StockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for overstock assignment.  
             
         
        """
        pass
    @StockSettings.setter
    def StockSettings(self, stockBuilder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for overstock assignment.  
             
         
        """
        pass
    @property
    def SwapProfile(self) -> bool:
        """
        Getter for property: (bool) SwapProfile
         Returns the profile swap flag.  
           Determines whether the profile should be
                    at the path start or end.  
         
        """
        pass
    @SwapProfile.setter
    def SwapProfile(self, swapProfile: bool):
        """
        Setter for property: (bool) SwapProfile
         Returns the profile swap flag.  
           Determines whether the profile should be
                    at the path start or end.  
         
        """
        pass
    @property
    def SwitchStartEnd(self) -> bool:
        """
        Getter for property: (bool) SwitchStartEnd
         Returns the path direction that defines the start of overstock assignment.  
             
         
        """
        pass
    @SwitchStartEnd.setter
    def SwitchStartEnd(self, switchStartEnd: bool):
        """
        Setter for property: (bool) SwitchStartEnd
         Returns the path direction that defines the start of overstock assignment.  
             
         
        """
        pass
    @property
    def WrapMethod(self) -> OverstockBuilder.WrapType:
        """
        Getter for property: ( OverstockBuilder.WrapType NXOpen) WrapMethod
         Returns the  NXOpen::Routing::OverstockBuilder::WrapType  for Wrapped overstock.  
             
         
        """
        pass
    @WrapMethod.setter
    def WrapMethod(self, wrapMethod: OverstockBuilder.WrapType):
        """
        Setter for property: ( OverstockBuilder.WrapType NXOpen) WrapMethod
         Returns the  NXOpen::Routing::OverstockBuilder::WrapType  for Wrapped overstock.  
             
         
        """
        pass
    def GetCoveredStocks(self) -> List[Stock]:
        """
         Returns the stocks to be covered by the overstock. 
         Returns stocks ( Stock List[NXOp):  .
        """
        pass
    def GetNumberOfLayers(self) -> NXOpen.Expression:
        """
         Returns the number of layers in case of wrapped overstock. 
         Returns numberOfLayers ( NXOpen.Expression): .
        """
        pass
    def IsOverlapDefinedByNumberOfLayers(self) -> bool:
        """
         Returns if wrapped overstock is defined by number of layers  
         Returns isOverlapDefinedByNumberOfLayers (bool): .
        """
        pass
    def SetCoveredStocks(self, stocks: List[Stock]) -> None:
        """
         Sets the stocks to be covered by the overstock. 
        """
        pass
    def SetNumberOfLayers(self, numberOfLayers: NXOpen.Expression) -> None:
        """
         Sets the number of layers in case of wrapped overstock. 
        """
        pass
    def SetOverlapDefinedByNumberOfLayers(self, isOverlapDefinedByNumberOfLayers: bool) -> None:
        """
         Sets wrapped overstock is to be defined by number of layers
        """
        pass
    def UpdatePathCurve(self) -> None:
        """
         Update the path curve that is used to specify overstock defining points
                    when any segment is selected or deselected.
        """
        pass
import NXOpen
class OverstockFacesBuilder(NXOpen.Builder): 
    """ Builder for qualifying faces for overstock application over fittings.
        These faces will be used to apply overstock automatically without explicit
        face selection during overstock application over fittings. """
    @property
    def Faces(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: ( NXOpen.SelectFaceList) Faces
         Returns the faces qualified for overstock application.  
             
         
        """
        pass
import NXOpen
class Overstock(Stock): 
    """ Represents an NXOpen.Routing.Overstock object. """
    @property
    def Application(self) -> OverstockApplication:
        """
        Getter for property: ( OverstockApplication NXOpen) Application
         Returns  the  NXOpen::Routing::OverstockApplication  that defines how this
                     overstock is applied to the segments.  
          
                  
         
        """
        pass
    def GetCoveredStocks(self) -> List[Stock]:
        """
         Get the stocks covering this NXOpen.Routing.Overstock. 
         Returns covered_stocks ( Stock List[NXOp):  .
        """
        pass
    def GetGapDistance(self) -> NXOpen.Scalar:
        """
         Get the gap distance for this NXOpen.Routing.Overstock. 
         Returns gap_distance ( NXOpen.Scalar):  .
        """
        pass
    def GetNumberOfWraps(self) -> NXOpen.Scalar:
        """
         Returns the number of wraps for this NXOpen.Routing.Overstock. 
         Returns number_of_wraps ( NXOpen.Scalar):  .
        """
        pass
    def GetOverstockCreationMethod(self) -> CreationMethod:
        """
         Returns the creation method of this NXOpen.Routing.Overstock. 
         Returns creation_method ( CreationMethod NXOpen):  .
        """
        pass
    def GetOverstockSegments(self) -> List[NXOpen.Curve]:
        """
         Returns the segments over which this NXOpen.Routing.Overstock is applied. 
         Returns segments ( NXOpen.Curve Li):  .
        """
        pass
    def GetOverstockType(self) -> Type:
        """
         Returns the type of overstock. Possible types are wrapped, sleeved, flagged and
                    an overstock with fixed cross section. 
         Returns type ( Type NXOpen):  .
        """
        pass
    def GetPercentageOverlap(self) -> NXOpen.Scalar:
        """
         Get the overlap percentage of this NXOpen.Routing.Overstock. 
         Returns percentage_overlap ( NXOpen.Scalar):  .
        """
        pass
    def GetThickness(self) -> NXOpen.Scalar:
        """
         Get the thickness of this NXOpen.Routing.Overstock. 
         Returns thickness ( NXOpen.Scalar):  .
        """
        pass
    def GetWidth(self) -> NXOpen.Scalar:
        """
         Get the width of this NXOpen.Routing.Overstock. 
         Returns width ( NXOpen.Scalar):  .
        """
        pass
class PartDefinitionBase(ItemDefinition): 
    """
        
        The abstract class NXOpen.Routing.PartDefinitionBase contains
        information defining a logical part.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    pass
class PartDefinitionShadow(ItemDefinition): 
    """
        
        NXOpen.Routing.PartDefinitionShadow contains the defining data for a
        logical part, such as an connector.
        NXOpen.Routing.PartDefinitionShadows contains a list of
        NXOpen.Routing.InterfaceTerminalShadows.  Component assignment
        associates the physical NX component to the logical component defined by this
        NXOpen.Routing.PartDefinitionShadow.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
    """
    def GetInterfaceTerminalShadows(self) -> List[InterfaceTerminalShadow]:
        """
         Returns the
                    NXOpen.Routing.PartDefinitionShadow's associated
                    NXOpen.Routing.InterfaceTerminalShadows.
                
         Returns shadowValues ( InterfaceTerminalShadow List[NXOp):  The NXOpen.Routing.InterfaceTerminalShadows
                                                            for this NXOpen.Routing.PartDefinitionShadow .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class PathStockBuilder(NXOpen.Builder): 
    """ Assigns stocks to segments based of users critiera and the current
        default stock.  """
    class AssignMethod(Enum):
        """
        Members Include: 
         |NotSet|  No Stock. 
         |DefaultStock|  Default Stock. 
         |FromStartObject|  Finds a stock based off of the
                                                                       default stock and the object
                                                                       selected by the user. 
         |DiameterValue|  User specified diameter, creates round
                                                                       space reservation stock. 
         |Rectangular|  User specified values, creates rectangular
                                                                       space reservation stock. 
         |FlatOval|  User specified values, creates flat_oval 
                                                                           space reservation stock. 
         |SpecifiedStock|  Stock selected from Specify Item dialog 
         |FromParts|  Find stocks from the part table
                                                                       of parts selected by the user.

        """
        NotSet: int
        DefaultStock: int
        FromStartObject: int
        DiameterValue: int
        Rectangular: int
        FlatOval: int
        SpecifiedStock: int
        FromParts: int
        @staticmethod
        def ValueOf(value: int) -> PathStockBuilder.AssignMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AssignStockType(Enum):
        """
        Members Include: 
         |Stock|  Default stock type.             
         |Overstock|  Overstock stock type.           
         |Filler|  Filler stock type.              
         |SpaceReservation|  Space Reservation stock type.   

        """
        Stock: int
        Overstock: int
        Filler: int
        SpaceReservation: int
        @staticmethod
        def ValueOf(value: int) -> PathStockBuilder.AssignStockType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssignStockMethod(self) -> PathStockBuilder.AssignMethod:
        """
        Getter for property: ( PathStockBuilder.AssignMethod NXOpen) AssignStockMethod
         Returns the method to determine which stock to assign.  
             
         
        """
        pass
    @AssignStockMethod.setter
    def AssignStockMethod(self, method: PathStockBuilder.AssignMethod):
        """
        Setter for property: ( PathStockBuilder.AssignMethod NXOpen) AssignStockMethod
         Returns the method to determine which stock to assign.  
             
         
        """
        pass
    @property
    def DiameterValue(self) -> float:
        """
        Getter for property: (float) DiameterValue
         Returns the diameter value to use for the 
                     Routing::PathStockBuilder::AssignMethodDiameterValue  
                    method of stock assignment.  
              
         
        """
        pass
    @DiameterValue.setter
    def DiameterValue(self, val: float):
        """
        Setter for property: (float) DiameterValue
         Returns the diameter value to use for the 
                     Routing::PathStockBuilder::AssignMethodDiameterValue  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def FlatOvalHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatOvalHeight
         Returns the height value to use for the   
                    Routing::PathStockBuilder::AssignMethodFlatOval  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def FlatOvalRotation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatOvalRotation
         Returns the Width value to use for the   
                    Routing::PathStockBuilder::AssignMethodFlatOval  
                    method of stock assignment      
            
         
        """
        pass
    @property
    def FlatOvalWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatOvalWidth
         Returns the Width value to use for the   
                    Routing::PathStockBuilder::AssignMethodFlatOval  
                    method of stock assignment      
            
         
        """
        pass
    @property
    def RectangularHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangularHeight
         Returns the height value to use for the   
                    Routing::PathStockBuilder::AssignMethodRectangular  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def RectangularRotation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangularRotation
         Returns the Width value to use for the   
                    Routing::PathStockBuilder::AssignMethodRectangular  
                    method of stock assignment      
            
         
        """
        pass
    @property
    def RectangularWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangularWidth
         Returns the Width value to use for the   
                    Routing::PathStockBuilder::AssignMethodRectangular  
                    method of stock assignment      
            
         
        """
        pass
    @property
    def StartObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) StartObject
         Returns the start object to use for the 
                     Routing::PathStockBuilder::AssignMethodFromStartObject  
                    method of stock assignment.  
              
         
        """
        pass
    @StartObject.setter
    def StartObject(self, start_object: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) StartObject
         Returns the start object to use for the 
                     Routing::PathStockBuilder::AssignMethodFromStartObject  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def StockRotation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StockRotation
         Returns the stock rotation value    
            
         
        """
        pass
    @property
    def StockType(self) -> PathStockBuilder.AssignStockType:
        """
        Getter for property: ( PathStockBuilder.AssignStockType NXOpen) StockType
         Returns the type of stock being assigned.  
             
         
        """
        pass
    @StockType.setter
    def StockType(self, stock_type: PathStockBuilder.AssignStockType):
        """
        Setter for property: ( PathStockBuilder.AssignStockType NXOpen) StockType
         Returns the type of stock being assigned.  
             
         
        """
        pass
    def AssignStock(self, segments: List[ISegment]) -> None:
        """
         Assigns stock using the method defined by this stock builder object.  
        """
        pass
    def DefaultOrientationAlignmentEnabled(self) -> bool:
        """
         Get the flag if non-circular stock default alignment is enabled 
         Returns suggestRotationAngle (bool): .
        """
        pass
    def EnableDefaultOrientationAlignment(self, suggestRotationAngle: bool) -> None:
        """
         Set the flag if it is to enable non-circular stock default alignment or not 
        """
        pass
    def GetFlatOvalDimensions(self) -> Tuple[float, float]:
        """
         Get the FlatOval height and width value to use for the FlatOval space reservation assignment 
         Returns A tuple consisting of (height, width). 
         - height is: float.
         - width is: float. .

        """
        pass
    def GetParts(self) -> List[NXOpen.Assemblies.Component]:
        """
         Get the parts to use for the  
                    Routing.PathStockBuilder.AssignMethod.FromParts 
                    method of stock assignment 
         Returns parts ( NXOpen.Assemblies.Component Li):  Part table parts to get
                                                                                                           stock characteristics. .
        """
        pass
    def GetRectangularDimensions(self) -> Tuple[float, float]:
        """
         Get the rectangular height and width value to use for the rectangular space reservation assignment 
         Returns A tuple consisting of (height, width). 
         - height is: float.
         - width is: float. .

        """
        pass
    @overload
    def GetSpecifiedStock(self) -> CharacteristicList:
        """
         Returns the specified stock to use for the 
                    Routing.PathStockBuilder.AssignMethod.SpecifiedStock 
                    method of stock assignment. 
         Returns stockPart ( CharacteristicList NXOpen):  Characteristic list used to find the appropriate 
                                                                        Routing.StockData for building the stock.  
                                                                        See Routing.StockDataCollection.CreateStockData. .
        """
        pass
    @overload
    def GetSpecifiedStock(self) -> Tuple[CharacteristicList, CharacteristicList]:
        """
         Returns the specified stock and applied characteristics to use for the 
                    Routing.PathStockBuilder.AssignMethod.SpecifiedStock 
                    method of stock assignment. 
         Returns A tuple consisting of (stockPart, appliedCharx). 
         - stockPart is:  CharacteristicList NXOpen. Characteristic list used to find the appropriate 
                                                                        Routing.StockData for building the stock.  
                                                                        See Routing.StockDataCollection.CreateStockData. .
         - appliedCharx is:  CharacteristicList NXOpen. Applied characteristics for the specified stock. .

        """
        pass
    def IsRotationOverriden(self) -> bool:
        """
         Get the rotation value overwritten flag 
         Returns overridenRotation (bool): .
        """
        pass
    def OverrideRotation(self, overrideRotation: bool) -> None:
        """
         Set the rotation value overwritten flag 
        """
        pass
    def SetFlatOvalDimensions(self, height: float, width: float) -> None:
        """
         Set the FlatOval height and width value for the FlatOval space reservation assignment 
        """
        pass
    def SetParts(self, parts: List[NXOpen.Assemblies.Component]) -> None:
        """
         Set the parts to use for the  
                    Routing.PathStockBuilder.AssignMethod.FromParts 
                    method of stock assignment 
        """
        pass
    def SetRectangularDimensions(self, height: float, width: float) -> None:
        """
         Set the rectangular height and width value for the rectangular space reservation assignment 
        """
        pass
    def SetSelectedStock(self, stock: Stock) -> None:
        """
         Set the selected stock 
        """
        pass
    @overload
    def SetSpecifiedStock(self, stockPart: CharacteristicList) -> None:
        """
         Sets the specified stock to use for the 
                    Routing.PathStockBuilder.AssignMethod.SpecifiedStock 
                    method of stock assignment. 
        """
        pass
    @overload
    def SetSpecifiedStock(self, stockPart: CharacteristicList, appliedCharx: CharacteristicList) -> None:
        """
         Sets the specified stock and applied characteristics to use for the 
                    Routing.PathStockBuilder.AssignMethod.SpecifiedStock 
                    method of stock assignment. 
        """
        pass
    def SettingsChanged(self) -> None:
        """
         Notify the builder that the Routing preferred stock has been modified.  This updates
                    the builder so that it now uses the new preferred stock do determine which stock to
                    assign.  
        """
        pass
    def UpdateExistingStock(self, existingStock: Stock) -> None:
        """
         Updates an existing routing stock with settings stored in the builder.
        """
        pass
import NXOpen
class Path(NXOpen.NXObject): 
    """ The Routing Path object is the set of ordered continuous segments.  """
    @property
    def ControlPointEnd(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointEnd.setter
    def ControlPointEnd(self, end: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @property
    def ControlPointStart(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointStart.setter
    def ControlPointStart(self, start: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    def GetLength(self) -> float:
        """
         Returns the combined length of all the segments in this path. 
         Returns length (float):  The combined length of all the segments in this path. .
        """
        pass
import NXOpen
class PlaceElbowsBuilder(NXOpen.Builder): 
    """ Class PlaceElbowsBuilder """
    @property
    def AttributeHolder(self) -> AttributeHolder:
        """
        Getter for property: ( AttributeHolder NXOpen) AttributeHolder
         Returns the attribute holder for elbow placement   
            
         
        """
        pass
    @property
    def SelectRoutingObjects(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SelectRoutingObjects
         Returns the route object collector builder for placing elbows   
            
         
        """
        pass
    def PlaceMultipleElbows(self, jaCharx: CharacteristicList, refSet: str, layer: int, layerOption: int, overstockFlag: bool, optionalCharx: CharacteristicList, requiredCharx: CharacteristicList) -> None:
        """
         Place Multiple Elbows 
        """
        pass
    def SetAttributeHolder(self, attributeHolder: AttributeHolder) -> None:
        """
         Set the Attribute Holder 
        """
        pass
import NXOpen
class PlacementSolutionsBuilder(NXOpen.Builder): 
    """ 
    
    """
    @overload
    def ApplyConstraintsAndClear(self) -> None:
        """
         Commit the solution and apply constraints if needed.  
        """
        pass
    @overload
    def ApplyConstraintsAndClear(self, lockEngagement: bool, lockRotation: bool) -> None:
        """
         Commit the solution and apply constraints if needed.  
        """
        pass
    @overload
    def ApplyConstraintsAndClear(self, lockEngagement: bool, lockRotation: bool, fixPart: bool) -> None:
        """
         Commit the solution and apply constraints if needed.  
        """
        pass
    def ApplyPortRotation(self, angle: float) -> None:
        """
         Applies a rotation to the component about the axis of the port being used for placement. 
        """
        pass
    def FirstSolution(self) -> None:
        """
         Cycle to the first solution. 
        """
        pass
    def GetConsiderPorts(self) -> bool:
        """
         Returns false if the first placement solution maintains the origin and orientation of the original component. 
         Returns considerPorts (bool):  Are ports to be considered when finding the first placement solution? .
        """
        pass
    def GetLookForAdditionalPlacementSolutions(self) -> bool:
        """
         Is Place Part looking for additional placement solutions? Used for Maintain Origin and Orientation replacement. 
         Returns lookForAdditionalPlacementSolutions (bool):  Are additional placement solutions to be found? .
        """
        pass
    def GetNumberOfSolutions(self) -> int:
        """
         Returns the total number of solutions based on the placement object. 
         Returns nSolutions (int): .
        """
        pass
    def GetOnlyPrimaryPlacementSolutions(self) -> bool:
        """
         Is Place Part only considering the primary placement solutions? 
         Returns onlyPrimaryPlacementSolutions (bool):  Are only the primary placement solutions to be found? .
        """
        pass
    def GetSolutionIndex(self) -> int:
        """
         Returns the current index of the solution. For example, index 1 of 10 solutions. 
         Returns solutionIndex (int): .
        """
        pass
    def GetSolutionPort(self) -> Port:
        """
         If Routing.PlacementSolutionsBuilder.SetConsiderPorts is set to true, 
                    returns the port used by the current placement solution. Otherwise returns . 
         Returns port ( Port NXOpen):  The port used in the current placement solution. .
        """
        pass
    def InitializePlacementData(self, part: NXOpen.TaggedObject, placementPos: NXOpen.Point3d, partToPlace: NXOpen.TaggedObject) -> None:
        """
         Initialize Placement Data
        """
        pass
    def NextSolution(self) -> None:
        """
         Cycle to the next solution. 
        """
        pass
    def PreviousSolution(self) -> None:
        """
         Cycle to the previous solution 
        """
        pass
    def SetConsiderPorts(self, considerPorts: bool) -> None:
        """
         Set to false to include a placement solution maintaining the origin and orientation of the component being replaced.
                    This solution, where ports are not considered in the calculation, will be the first solution. 
        """
        pass
    def SetLookForAdditionalPlacementSolutions(self, lookForAdditionalPlacementSolutions: bool) -> None:
        """
         Set to true to look for additional placement solutions. Used for Maintain Origin and Orientation replacement. 
        """
        pass
    def SetOnlyPrimaryPlacementSolutions(self, onlyPrimaryPlacementSolutions: bool) -> None:
        """
         True tells Place Part to only consider the primary placement solutions. 
        """
        pass
import NXOpen
class PlacePartBuilder(NXOpen.Builder): 
    """ 
    """
    def AddPlacedOccurrence(self, occTag: NXOpen.TaggedObject) -> None:
        """
         Sets a post placed occurrence. 
        """
        pass
    def FinalizePlacement(self, optionalCharx: CharacteristicList, requiredCharx: CharacteristicList, name: str, layerOption: int, layer: int, dfaultOStock: bool) -> None:
        """
         Complete the placement operation. 
        """
        pass
    def GetActiveRefSet(self) -> str:
        """
         Get the reference set for the loaded part. 
         Returns refSet (str): .
        """
        pass
    def GetAddPartToActiveRunFlag(self) -> bool:
        """
         Determines whether part being placed has to be added in active run or not. 
         Returns addPartToActiveRun (bool): .
        """
        pass
    def GetAttributeHolder(self) -> AttributeHolder:
        """
         Gets Attribute holder in builder, which is user for template attribute assignment. 
         Returns attributeHolder ( AttributeHolder NXOpen):  Object to hold template attributes .
        """
        pass
    def GetLoadedPartInfo(self) -> Tuple[NXOpen.TaggedObject, NXOpen.TaggedObject]:
        """
         Get information about the parts being placed.  
         Returns A tuple consisting of (loadedPart, loadedInst). 
         - loadedPart is:  NXOpen.TaggedObject. The PART object of the loaded part. .
         - loadedInst is:  NXOpen.TaggedObject. The Instance object of the loaded part. .

        """
        pass
    def GetNumberOfPlacedOccurrences(self) -> int:
        """
         Gets the count of placed occurrences.  
         Returns occCount (int):  The total number of occs. .
        """
        pass
    def GetPlacedOccurrence(self, index: int) -> NXOpen.TaggedObject:
        """
         Gets placed occurrences.  
         Returns occTag ( NXOpen.TaggedObject):  The placed occurrence. .
        """
        pass
    def GetScrewSeatAlignmentVector(self) -> NXOpen.Vector3d:
        """
         Gets the alignment vector, primary axis direction for a stock, reducer, elbow, etc. along the part the screw seat is placed to align the screw seat. Optional, otherwise an arbitrary vector will be constructed. 
         Returns alignVector ( NXOpen.Vector3d):  The alignment vector along the part on which screw seat is placed. .
        """
        pass
    def GetScrewSeatAngle(self) -> NXOpen.Expression:
        """
         Gets the angle expression to be used for screw seat placement along a placed object. 
         Returns angleExp ( NXOpen.Expression):  The angle used for screw seat placement on placed routing object. .
        """
        pass
    def GetScrewSeatEnd(self) -> NXOpen.Point3d:
        """
         Gets the point from builder, used in final placement of screw seat. This point is used for creating 
                segemnts  constraints when finally placing the screw seat. 
         Returns point ( NXOpen.Point3d):  This is the internal point used in determining final position of screw seat placement.  .
        """
        pass
    def GetScrewSeatIntersectionPoint(self) -> NXOpen.Point3d:
        """
         Gets information about the final screw seat position.  
         Returns intersectionPoint ( NXOpen.Point3d):  The final position of screw seat placement. .
        """
        pass
    def GetScrewSeatLength(self) -> NXOpen.Expression:
        """
         Gets the length expression to be used for screw seat placement along a placed object. 
         Returns lengthExp ( NXOpen.Expression):  The length used for screw seat placement on placed routing object. .
        """
        pass
    @overload
    def LoadPart(self, partNumber: str) -> None:
        """
         Load a part given the input part number. 
        """
        pass
    @overload
    def LoadPart(self) -> None:
        """
         Load the specified part. 
        """
        pass
    def ReplaceLoadedInstance(self, partInst: NXOpen.TaggedObject) -> None:
        """
         Replace the builder's part instance with a new instance.
                    This is used when the assemblies absolute positioning method is used. It will create
                    it's own part instance and we need make sure the builder has the new one. 
        """
        pass
    def SetActiveLayer(self, layerOption: int, layer: int) -> None:
        """
         Set the layer for the loaded part. 
        """
        pass
    def SetActiveRefSet(self, refSet: str) -> None:
        """
         Set the reference set to use for the loaded part. 
        """
        pass
    def SetAddPartToActiveRunFlag(self, addPartToActiveRun: bool) -> None:
        """
         Set a flag which tells the builder whether the part being placed will be added in active run or not. 
        """
        pass
    def SetAttributeHolder(self, attributeHolder: AttributeHolder) -> None:
        """
         Sets Attribute holder in builder, which is user for template attribute assignment. 
        """
        pass
    def SetConsiderPorts(self, considerPorts: bool) -> None:
        """
         Set a flag which will inform the placement solutions builder to consider ports when computing placement solutions during a replace part operation.
                    Setting this to false implies that the first placement solution computed is to maintain the origin and orientation of the part being replaced.
                    Setting this to true  implies that the first placement solution computed is to maintain the location of the original part's ports. 
        """
        pass
    def SetItemSelection(self, itemSelectionMethod: int, selectedPartOcc: NXOpen.TaggedObject) -> None:
        """
         Set a flag which tells the builder from where the part being placed was selected and the tag of the selected part. 
        """
        pass
    def SetLoadedPartInfo(self, loadedPart: NXOpen.TaggedObject, loadedInst: NXOpen.TaggedObject) -> None:
        """
         Get information about the parts being placed.  
        """
        pass
    def SetPlacePartOperation(self, replacePart: bool) -> None:
        """
         Set a flag which tells the builder whether the part being placed is replacing
                    an existing part in the assembly. 
        """
        pass
    def SetScrewSeatAlignmentVector(self, alignVector: NXOpen.Vector3d) -> None:
        """
         Sets the alignment vector, primary axis direction for a stock, reducer, elbow, etc. along the part the screw seat is placed to align the screw seat. Optional, otherwise an arbitrary vector will be constructed. 
        """
        pass
    def SetScrewSeatEnd(self, point: NXOpen.Point3d) -> None:
        """
         Sets a point in builder, which is required for final placement of screw seat.
                This point is used for creating segments  constraints when finally placing the screw seat. 
        """
        pass
    def SetScrewSeatIntersectionPoint(self, intersectionPoint: NXOpen.Point3d) -> None:
        """
         Sets the final position of screw seat. This is required in builder when doing
                finalize placement after (OKApply) . 
        """
        pass
    def SetScrewSeatPlacement(self, startLocation: NXOpen.TaggedObject, endLocation: NXOpen.TaggedObject, startPoint: NXOpen.Point3d, endPoint: NXOpen.Point3d, length: NXOpen.Expression, angle: NXOpen.Expression) -> None:
        """
         Sets the input parameters to be used for measurement holder screw seats. 
        """
        pass
    def UnloadPart(self) -> None:
        """
         Update the loaded part with a new placement location and object.  
        """
        pass
    def UpdatePlacementObj(self, placementObj: NXOpen.TaggedObject, placementPos: NXOpen.Point3d) -> None:
        """
         Update the loaded part with a new placement location and object.  
        """
        pass
    def UpdateRoutingTemplateAttributes(self) -> None:
        """
         Updates the Routing Template Attributes to AttributeHolder 
        """
        pass
import NXOpen
class PlatformCreatorBuilder(NXOpen.Builder): 
    """ Builder for creating platform.
        Create platform: Takes platform outer boundaries sketch, platform plate boundaries sketch, platform plates,
        stocks for external and internal frames. Grate orientation symbol display is optional."""
    class ReferenceType(Enum):
        """
        Members Include: 
         |Horizontal| 
         |Vertical| 

        """
        Horizontal: int
        Vertical: int
        @staticmethod
        def ValueOf(value: int) -> PlatformCreatorBuilder.ReferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ExternalFrameAnchorName(self) -> str:
        """
        Getter for property: (str) ExternalFrameAnchorName
         Returns the external frame stock anchor   
            
         
        """
        pass
    @ExternalFrameAnchorName.setter
    def ExternalFrameAnchorName(self, anchorName: str):
        """
        Setter for property: (str) ExternalFrameAnchorName
         Returns the external frame stock anchor   
            
         
        """
        pass
    @property
    def ExternalStockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) ExternalStockSettings
         Returns the external frame stock settings for stock assignment.  
             
         
        """
        pass
    @property
    def GrateOrientationReference(self) -> PlatformCreatorBuilder.ReferenceType:
        """
        Getter for property: ( PlatformCreatorBuilder.ReferenceType NXOpen) GrateOrientationReference
         Returns the grate orientation reference   
            
         
        """
        pass
    @GrateOrientationReference.setter
    def GrateOrientationReference(self, grateOrientationReference: PlatformCreatorBuilder.ReferenceType):
        """
        Setter for property: ( PlatformCreatorBuilder.ReferenceType NXOpen) GrateOrientationReference
         Returns the grate orientation reference   
            
         
        """
        pass
    @property
    def GrateOrientationSymbolDisplay(self) -> bool:
        """
        Getter for property: (bool) GrateOrientationSymbolDisplay
         Returns the grate orientation symbol display   
            
         
        """
        pass
    @GrateOrientationSymbolDisplay.setter
    def GrateOrientationSymbolDisplay(self, grateOrientationSymbolDisplay: bool):
        """
        Setter for property: (bool) GrateOrientationSymbolDisplay
         Returns the grate orientation symbol display   
            
         
        """
        pass
    @property
    def GrateOrientationSymbolRefSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) GrateOrientationSymbolRefSelection
         Returns the grate orientation symbol ref selection   
            
         
        """
        pass
    @property
    def InternalFrameAnchorName(self) -> str:
        """
        Getter for property: (str) InternalFrameAnchorName
         Returns the internal frame stock anchor   
            
         
        """
        pass
    @InternalFrameAnchorName.setter
    def InternalFrameAnchorName(self, anchorName: str):
        """
        Setter for property: (str) InternalFrameAnchorName
         Returns the internal frame stock anchor   
            
         
        """
        pass
    @property
    def InternalStockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) InternalStockSettings
         Returns the internal stock settings for stock assignment.  
             
         
        """
        pass
    @property
    def PlateBoundariesSelection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) PlateBoundariesSelection
         Returns the platform part boundaries section   
            
         
        """
        pass
    @property
    def SelectOuterBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectOuterBoundary
         Returns the platform outer boundary section   
            
         
        """
        pass
    @property
    def ThickenDirection(self) -> bool:
        """
        Getter for property: (bool) ThickenDirection
         Returns the thicken direction   
            
         
        """
        pass
    @ThickenDirection.setter
    def ThickenDirection(self, thickenDirection: bool):
        """
        Setter for property: (bool) ThickenDirection
         Returns the thicken direction   
            
         
        """
        pass
    @property
    def UseSameStock(self) -> bool:
        """
        Getter for property: (bool) UseSameStock
         Returns the internal frame use same stock option   
            
         
        """
        pass
    @UseSameStock.setter
    def UseSameStock(self, internalFrameFlipStock: bool):
        """
        Setter for property: (bool) UseSameStock
         Returns the internal frame use same stock option   
            
         
        """
        pass
    def GetPlateAppliedCharx(self) -> CharacteristicList:
        """
         Gets the plate charx which is used for platform plate
         Returns appliedCharx ( CharacteristicList NXOpen): .
        """
        pass
    def GetPlatePart(self) -> CharacteristicList:
        """
         Gets the plate part which data is used for platform plate 
         Returns platePart ( CharacteristicList NXOpen): .
        """
        pass
    def SetPlateAppliedCharx(self, appliedCharx: CharacteristicList) -> None:
        """
         Sets the  plate charx which is used for platform plate
        """
        pass
    def SetPlatePart(self, platePart: CharacteristicList) -> None:
        """
         Sets the plate part which data is used for plaform plate
        """
        pass
    def SpecifyPlate(self) -> None:
        """
         The specify plate button callback 
        """
        pass
import NXOpen.Features
class PlatformFeature(NXOpen.Features.BodyFeature): 
    """ Represents a Platform feature.
        Use the NXOpen.Routing.PlatformCreatorBuilder class to create a Platform feature. """
    pass
import NXOpen
class Platform(NXOpen.NXObject): 
    """ NXOpen.Routing.Platform objects are automatically created and updated by
        NXOpen.Routing.Platform objects. """
    pass
class PointDefinition(Enum):
    """
    Members Include: 
     |Start|  The point defines the start of the overstock application. 
     |Middle|  The point defines the middle of the overstock application. 
     |End|  The point defines the end of the overstock application. 

    """
    Start: int
    Middle: int
    End: int
    @staticmethod
    def ValueOf(value: int) -> PointDefinition:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class PortArrayListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PortArrayListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PortArrayListItemBuilder) -> None:
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
    def Erase(self, obj: PortArrayListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PortArrayListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PortArrayListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PortArrayListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PortArrayListItemBuilder NXOpen):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PortArrayListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PortArrayListItemBuilder List[NXOp):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PortArrayListItemBuilder) -> None:
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
    def SetContents(self, objects: List[PortArrayListItemBuilder]) -> None:
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
    def Swap(self, object1: PortArrayListItemBuilder, object2: PortArrayListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Features
class PortArrayListItemBuilder(NXOpen.Builder): 
    """ Builder for selecting a pattern and initial positions in terminal arrays builder. """
    @property
    def MasterInstance(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) MasterInstance
         Returns the initial position   
            
         
        """
        pass
    @MasterInstance.setter
    def MasterInstance(self, masterInstance: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) MasterInstance
         Returns the initial position   
            
         
        """
        pass
    @property
    def PatternFeature(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) PatternFeature
         Returns the pattern feature   
            
         
        """
        pass
    @property
    def StartingLocation(self) -> NXOpen.Features.SelectFeature:
        """
        Getter for property: ( NXOpen.Features.SelectFeature) StartingLocation
         Returns the starting position for naming circular arrays   
            
         
        """
        pass
import NXOpen
class PortArraysBuilder(NXOpen.Builder): 
    """ Builder for creating terminal arrays in multiports. """
    class ArrayTypes(Enum):
        """
        Members Include: 
         |Rectangular| 
         |Circular| 

        """
        Rectangular: int
        Circular: int
        @staticmethod
        def ValueOf(value: int) -> PortArraysBuilder.ArrayTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class NamingMethods(Enum):
        """
        Members Include: 
         |Clockwise| 
         |Counterclockwise| 
         |Across| 
         |Continuous| 
         |RowCol| 

        """
        Clockwise: int
        Counterclockwise: int
        Across: int
        Continuous: int
        RowCol: int
        @staticmethod
        def ValueOf(value: int) -> PortArraysBuilder.NamingMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StartingCorners(Enum):
        """
        Members Include: 
         |BottomLeft| 
         |BottomRight| 
         |UpperLeft| 
         |UpperRight| 

        """
        BottomLeft: int
        BottomRight: int
        UpperLeft: int
        UpperRight: int
        @staticmethod
        def ValueOf(value: int) -> PortArraysBuilder.StartingCorners:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StartingDirections(Enum):
        """
        Members Include: 
         |Horizontal| 
         |Vertical| 

        """
        Horizontal: int
        Vertical: int
        @staticmethod
        def ValueOf(value: int) -> PortArraysBuilder.StartingDirections:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrayPatternList(self) -> PortArrayListItemBuilderList:
        """
        Getter for property: ( PortArrayListItemBuilderList NXOpen) ArrayPatternList
         Returns the array pattern list   
            
         
        """
        pass
    @property
    def ArrayType(self) -> PortArraysBuilder.ArrayTypes:
        """
        Getter for property: ( PortArraysBuilder.ArrayTypes NXOpen) ArrayType
         Returns the array type   
            
         
        """
        pass
    @ArrayType.setter
    def ArrayType(self, arrayType: PortArraysBuilder.ArrayTypes):
        """
        Setter for property: ( PortArraysBuilder.ArrayTypes NXOpen) ArrayType
         Returns the array type   
            
         
        """
        pass
    @property
    def NamingMethod(self) -> PortArraysBuilder.NamingMethods:
        """
        Getter for property: ( PortArraysBuilder.NamingMethods NXOpen) NamingMethod
         Returns the naming method   
            
         
        """
        pass
    @NamingMethod.setter
    def NamingMethod(self, namingMethod: PortArraysBuilder.NamingMethods):
        """
        Setter for property: ( PortArraysBuilder.NamingMethods NXOpen) NamingMethod
         Returns the naming method   
            
         
        """
        pass
    @property
    def PatternCol(self) -> NamingPatternBuilder:
        """
        Getter for property: ( NamingPatternBuilder NXOpen) PatternCol
         Returns the naming pattern for the columns of ColumnRow rectangular terminal port arrays   
            
         
        """
        pass
    @PatternCol.setter
    def PatternCol(self, patternCol: NamingPatternBuilder):
        """
        Setter for property: ( NamingPatternBuilder NXOpen) PatternCol
         Returns the naming pattern for the columns of ColumnRow rectangular terminal port arrays   
            
         
        """
        pass
    @property
    def PatternRow(self) -> NamingPatternBuilder:
        """
        Getter for property: ( NamingPatternBuilder NXOpen) PatternRow
         Returns the naming pattern for the rows of ColumnRow rectangular terminal port arrays   
            
         
        """
        pass
    @PatternRow.setter
    def PatternRow(self, patternRow: NamingPatternBuilder):
        """
        Setter for property: ( NamingPatternBuilder NXOpen) PatternRow
         Returns the naming pattern for the rows of ColumnRow rectangular terminal port arrays   
            
         
        """
        pass
    @property
    def ReuseSuppressedNames(self) -> bool:
        """
        Getter for property: (bool) ReuseSuppressedNames
         Returns the reuse suppressed names   
            
         
        """
        pass
    @ReuseSuppressedNames.setter
    def ReuseSuppressedNames(self, reuseSuppressedNames: bool):
        """
        Setter for property: (bool) ReuseSuppressedNames
         Returns the reuse suppressed names   
            
         
        """
        pass
    @property
    def StartingCorner(self) -> PortArraysBuilder.StartingCorners:
        """
        Getter for property: ( PortArraysBuilder.StartingCorners NXOpen) StartingCorner
         Returns the starting corner   
            
         
        """
        pass
    @StartingCorner.setter
    def StartingCorner(self, startingCorner: PortArraysBuilder.StartingCorners):
        """
        Setter for property: ( PortArraysBuilder.StartingCorners NXOpen) StartingCorner
         Returns the starting corner   
            
         
        """
        pass
    @property
    def StartingDirection(self) -> PortArraysBuilder.StartingDirections:
        """
        Getter for property: ( PortArraysBuilder.StartingDirections NXOpen) StartingDirection
         Returns the starting direction   
            
         
        """
        pass
    @StartingDirection.setter
    def StartingDirection(self, startingDirection: PortArraysBuilder.StartingDirections):
        """
        Setter for property: ( PortArraysBuilder.StartingDirections NXOpen) StartingDirection
         Returns the starting direction   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class PortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Port objects. 

    Iterating this collection only returns live uncondemned objects contained in the owning part
    of the collection. Note that NXOpen.Routing.Port is a smart object and many smart objects are condemned as they
    only exist to support other objects and are not displayed."""
    def ConvertToFeatures(self) -> None:
        """
         Cycles through all the NXOpen.Routing.Port objects and creates
                    a NXOpen.Routing.FeaturePort object for NXOpen.Routing.FittingPort object,
                    NXOpen.Routing.FixturePort object, NXOpen.Routing.MultiPort object, and
                    NXOpen.Routing.TerminalPort object.  
        """
        pass
    @overload
    def CreateExtractPort(self, port: Port) -> ExtractPort:
        """
         Creates a NXOpen.Routing.ExtractPort.  Default
                    allows multiple connections to this port. 
         Returns extract ( ExtractPort NXOpen):  Extracted Port .
        """
        pass
    @overload
    def CreateExtractPort(self, port: Port, allowMultipleConnections: bool) -> ExtractPort:
        """
         Creates a NXOpen.Routing.ExtractPort.  
         Returns extract ( ExtractPort NXOpen):  Extracted Port .
        """
        pass
    def FindPortFromPoint(self, point: NXOpen.Point) -> Port:
        """
         Finds the Routing.Port used to create the given Point.
                    Returns  if the point was not created from a port.
                
         Returns port ( Port NXOpen):  The port used to create the point, if any. .
        """
        pass
    def GetComponentPorts(self, component: NXOpen.Assemblies.Component) -> List[Port]:
        """
         Given a component, returns the port occurrences that belong to it.
                    Returns  otherwise. 
         Returns ports ( Port List[NXOp): .
        """
        pass
    def GetObjectPorts(self, entity: NXOpen.NXObject) -> List[Port]:
        """
         Given any NXObject, returns any port occurrences that
                    belong to it. Returns  otherwise.
                    The type of ports returned depends on the type of object given.
                    If given a NXOpen.Routing.ISegment, if there is stock on the segment,
                    returns the ports from stock. If there is no stock, returns any fitting ports at the segment ends.
                    If given a NXOpen.Routing.Stock, returns the ports at ends of stock.
                    If given a NXOpen.Routing.Port, returns itself.
                    if given a NXOpen.Routing.ControlPoint, returns any fitting ports at the Control Point.
                    If given a part, returns any ports in the part.
                
         Returns ports ( Port List[NXOp): .
        """
        pass
    def GroupWavePortsInWork(self, component: NXOpen.Assemblies.Component) -> NXOpen.Group:
        """
         Creates or outputs existing group with the wave ports in the work part from the identified component 
         Returns prototype ( NXOpen.Group):  The group containing the wave link ports from the passed in component .
        """
        pass
    def UpdatePortObjectLocations(self) -> None:
        """
         Ensures that all NXOpen.Routing.Port objects have the correct locations based on their associated ports.
                
        """
        pass
import NXOpen
class PortConnectionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.PortConnection objects. """
    class PortsStatus(Enum):
        """
        Members Include: 
         |CanConnect|  The Ports can be connected
                                                                            using Port Connection object. 
         |CannotConnect|  The Ports cannot be connected
                                                                            using Port Connection object. 

        """
        CanConnect: int
        CannotConnect: int
        @staticmethod
        def ValueOf(value: int) -> PortConnectionCollection.PortsStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CanPortsConnect(self, port_1: Port, port_2: Port) -> PortConnectionCollection.PortsStatus:
        """
         Determines if the two ports can be connected using a NXOpen.Routing.PortConnection object. 
         Returns can_ports_connect ( PortConnectionCollection.PortsStatus NXOpen):  .
        """
        pass
    def CreatePortConnection(self, port_1: Port, port_2: Port) -> PortConnection:
        """
         Creates a NXOpen.Routing.PortConnection object. 
         Returns port_connection ( PortConnection NXOpen):  .
        """
        pass
    def GetConnectionFromPort(self, port: Port) -> PortConnection:
        """
         Returns the NXOpen.Routing.PortConnection the given part participates in, if any. 
         Returns portConnection ( PortConnection NXOpen):  .
        """
        pass
import NXOpen
class PortConnection(NXOpen.NXObject): 
    """ The Routing PortConnection object is used by Routing to position ports
        while placing parts.
     """
    class OverriddenValidity(Enum):
        """
        Members Include: 
         |NotSet|  The port connection validity has not been overridden 
         |Valid|  The port connection validity has been overridden to be valid 
         |Invalid|  The port connection validity has been overridden to be invalid 

        """
        NotSet: int
        Valid: int
        Invalid: int
        @staticmethod
        def ValueOf(value: int) -> PortConnection.OverriddenValidity:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def ArePortsAligned(self) -> bool:
        """
         Returns whether the ports in the port connection are aligned correctly.  Both direction and rotation are evaluated. 
         Returns alignment (bool):  validity of the current connection. .
        """
        pass
    def ForceValid(self, reason: str) -> None:
        """
         Force the connection to be valid regardless of the port alignment or the overridden value. 
                    The user's login name and the date and time are recorded automatically along
                    with the given reason. 
        """
        pass
    def GetEngagement(self) -> float:
        """
         Returns the engagement distance between the two ports connected by a Port Connection object. 
         Returns engagement (float):  engagement distance between the ports connected by the
                                                         Port Connection object .
        """
        pass
    def GetOverriddenValidity(self) -> PortConnection.OverriddenValidity:
        """
         Returns the overridden validity value of the port connection. 
         Returns overridden_validity ( PortConnection.OverriddenValidity NXOpen):  overridden validity value. .
        """
        pass
    def GetOverrideReason(self) -> str:
        """
         Gets the reason why a port connection's validity was overridden. 
         Returns reason (str):  The reason why this connection's validity was overridden. .
        """
        pass
    def GetPorts(self) -> Tuple[Port, Port]:
        """
         Returns the two ports connected by a Port Connection object. 
         Returns A tuple consisting of (port_1, port_2). 
         - port_1 is:  Port NXOpen. first Port connected by the
                                                                           Port Connection object .
         - port_2 is:  Port NXOpen. second Port connected by the
                                                                           Port Connection object .

        """
        pass
    def IsForcedValid(self) -> bool:
        """
         Returns whether the connection is forced to be valid. 
         Returns forced_valid (bool):  validity of the current connection. .
        """
        pass
    def IsValid(self) -> bool:
        """
         Returns whether the connection is valid. Validity is initially determined by the alignment of the ports
                    but can be overridden by OverrideValidity or ForceValid 
         Returns validity (bool):  validity of the current connection. .
        """
        pass
    def OverrideValidity(self, overridden_validity: PortConnection.OverriddenValidity) -> None:
        """
         Overrides the validity of the port connection.  By default, the validity is determined by
                    evaluating the alignment of the connected ports. 
        """
        pass
    def RemoveForcedValidity(self) -> None:
        """
         Removes the forced validity setting on the connection.  Validity will now be determined based on the alignment or
                    on the overridden validity setting. 
        """
        pass
    def SetEngagement(self, engagement: float) -> None:
        """
         Sets the engagement distance between the two ports connected by a Port Connection object. 
        """
        pass
    def SetOverrideReason(self, reason: str) -> None:
        """
         Sets the reason why a port connection's validity was overridden. 
        """
        pass
    def SetPorts(self, port_1: Port, port_2: Port) -> None:
        """
         Sets the link between the two ports connected by the Port Connection object. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
import NXOpen.Positioning
class Port(NXOpen.SmartObject): 
    """ Routing Port Object is a parent class for FixturePort, ExtractPort, FittingPort,
        Multiport, StockPort and TerminalPort"""
    class CreateRotationVector(Enum):
        """
        Members Include: 
         |No|  Do not create the rotation vector on the port created from a coordinate system. 
         |Yes|  Create the rotation vector on the port created from a coordinate system. 

        """
        No: int
        Yes: int
        @staticmethod
        def ValueOf(value: int) -> Port.CreateRotationVector:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlowDirectionType(Enum):
        """
        Members Include: 
         |RouteFlowEither|  
         |RouteFlowIn|  
         |RouteFlowOut|  
         |FlowNone|  

        """
        RouteFlowEither: int
        RouteFlowIn: int
        RouteFlowOut: int
        FlowNone: int
        @staticmethod
        def ValueOf(value: int) -> Port.FlowDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PortType(Enum):
        """
        Members Include: 
         |UnknownPort|  Unknown Port      
         |FittingPort|  Fitting Port      
         |FixturePort|  Fixture Port      
         |MultiPort|  Multi Port        
         |TerminalPort|  Terminal Port     
         |StockPort|  Stock Port        
         |StockOffsetPort|  Stock Offset Port 

        """
        UnknownPort: int
        FittingPort: int
        FixturePort: int
        MultiPort: int
        TerminalPort: int
        StockPort: int
        StockOffsetPort: int
        @staticmethod
        def ValueOf(value: int) -> Port.PortType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowMultipleConnections(self) -> bool:
        """
        Getter for property: (bool) AllowMultipleConnections
         Returns the Allow Multiple Connections property for a  NXOpen::Routing::Port .  
          
                    The property controls the number of connections that can be routed to this
                     NXOpen::Routing::Port .  Although this can be specified in the
                    Mechanical application, the Electrical application is where this property is most
                    used.
                    
         
        """
        pass
    @AllowMultipleConnections.setter
    def AllowMultipleConnections(self, allow_multiple_connections: bool):
        """
        Setter for property: (bool) AllowMultipleConnections
         Returns the Allow Multiple Connections property for a  NXOpen::Routing::Port .  
          
                    The property controls the number of connections that can be routed to this
                     NXOpen::Routing::Port .  Although this can be specified in the
                    Mechanical application, the Electrical application is where this property is most
                    used.
                    
         
        """
        pass
    @property
    def BackwardExtension(self) -> float:
        """
        Getter for property: (float) BackwardExtension
         Returns the backward extension value for a port (i.  
          e. the minimum length that
                   a segment must remain straight going into the back of a  NXOpen::Routing::Port )   
         
        """
        pass
    @BackwardExtension.setter
    def BackwardExtension(self, extension: float):
        """
        Setter for property: (float) BackwardExtension
         Returns the backward extension value for a port (i.  
          e. the minimum length that
                   a segment must remain straight going into the back of a  NXOpen::Routing::Port )   
         
        """
        pass
    @property
    def BackwardExtensionObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BackwardExtensionObject
         Returns the backward extension object for a port.  
             
         
        """
        pass
    @BackwardExtensionObject.setter
    def BackwardExtensionObject(self, backwardExtension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) BackwardExtensionObject
         Returns the backward extension object for a port.  
             
         
        """
        pass
    @property
    def ClockIncrementObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ClockIncrementObject
         Returns the clock angle increment expression of a
                    NXOpen::Routing::Port , i.  
          e. an expression
                   representing the minimum angle for clocking the
                    NXOpen::Routing::Port .   
         
        """
        pass
    @ClockIncrementObject.setter
    def ClockIncrementObject(self, increment: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ClockIncrementObject
         Returns the clock angle increment expression of a
                    NXOpen::Routing::Port , i.  
          e. an expression
                   representing the minimum angle for clocking the
                    NXOpen::Routing::Port .   
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the  NXOpen::Point  that specifies the location of the
                     NXOpen::Routing::IRoutePosition  object.  
            A NULL object indicates that this
                    object is not associated to any point.    
         
        """
        pass
    @property
    def Position(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
    @Position.setter
    def Position(self, position: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Position
         Returns  the current location of the object in ABS coordinates.  
            This value is
                      overridden by the coordinates of the point associated with this object.   
         
        """
        pass
    def AskFeature(self) -> FeaturePort:
        """
         Ask NXOpen.Routing.FeaturePort object associated with
                   NXOpen.Routing.Port. Returns  if the port was created
                   in preNX6 release and not converted to NXOpen.Routing.FeaturePort
                   or the port is a WAVE-linked port.
                   To convert NXOpen.Routing.Port object to NXOpen.Routing.FeaturePort object
                   use Routing.PortCollection.ConvertToFeatures. 
         Returns feature ( FeaturePort NXOpen):  .
        """
        pass
    def AskWaveFeature(self) -> NXOpen.Features.WaveRouting:
        """
         Ask NXOpen.Features.WaveRouting object associated with this
                   NXOpen.Routing.Port. Returns  if the port is not
                   WAVE-linked.
                
         Returns feature ( NXOpen.Features.WaveRouting):  .
        """
        pass
    def Connect(self) -> PortConnection:
        """
         Finds another NXOpen.Routing.Port to connect this port to.  Builds a
                    NXOpen.Routing.PortConnection object if a connectable port is found.  See
                    Routing.PortConnectionCollection.CanPortsConnect. Does nothing if
                    this port already has a NXOpen.Routing.PortConnection object referencing it. 
         Returns connection ( PortConnection NXOpen):  .
        """
        pass
    def Disconnect(self) -> None:
        """
         Deletes any NXOpen.Routing.PortConnection objects that reference this port. 
        """
        pass
    def FindPortIntegerCharacteristic(self, name: str) -> int:
        """
         Searches for an integer characteristics on the port, then on the ports component
                    and prototype port if the port is an occurrence.   
         Returns value (int):  .
        """
        pass
    def FindPortRealCharacteristic(self, name: str) -> float:
        """
         Searches for a real characteristics on the port, then on the ports component
                    and prototype port if the port is an occurrence.   
         Returns value (float):  .
        """
        pass
    def FindPortStringCharacteristic(self, name: str) -> str:
        """
         Searches for a string characteristics on the port, then on the ports component
                    and prototype port if the port is an occurrence.   
         Returns value (str):  .
        """
        pass
    def GetAlignmentVector(self) -> NXOpen.Vector3d:
        """
         Retrieves the alignment vector of Port 
         Returns vector ( NXOpen.Vector3d):  Vector direction in absolute co-ordinate system .
        """
        pass
    def GetClockIncrement(self) -> float:
        """
         The clock angle increment value of NXOpen.Routing.Port 
         Returns increment (float):  Clock increment value in degrees .
        """
        pass
    def GetComponent(self) -> NXOpen.Assemblies.Component:
        """
         If this port is an occurrence, returns the component part to which it belongs.
                    Returns  otherwise. 
         Returns component ( NXOpen.Assemblies.Component):  .
        """
        pass
    def GetConnectedPorts(self) -> Tuple[Port, Port]:
        """
         If port is connected to another port, returns both connected ports.
                    Returns  otherwise. 
         Returns A tuple consisting of (connectedPort1, connectedPort2). 
         - connectedPort1 is:  Port NXOpen. .
         - connectedPort2 is:  Port NXOpen. .

        """
        pass
    def GetControlPoint(self) -> ControlPoint:
        """
         Returns the Routing.ControlPoint to which this port is constrained, if any.
                    Returns  otherwise. 
         Returns controlPoint ( ControlPoint NXOpen):  .
        """
        pass
    def GetCutbackLength(self) -> float:
        """
         Returns the cutback length of a port, i.e. the length along the wire from
                   the port where individual wires leave a bundle to attach to pins 
         Returns cutbackLength (float):  Cutback length .
        """
        pass
    def GetEngagement(self) -> float:
        """
         Returns the engagement distance of a port, i.e. the distance
                   behind the port that another fitting or stock may engage 
         Returns engagement (float):  Engagement distance .
        """
        pass
    def GetEngagementPosition(self) -> NXOpen.Point3d:
        """
         Returns the position of the port taking into account the engagement distance. 
         Returns position ( NXOpen.Point3d):  Location of engagement position in ABS coordinates .
        """
        pass
    def GetFlowDirection(self) -> Port.FlowDirectionType:
        """
         Get the value of flow direction of NXOpen.Routing.Port 
         Returns flow_direction ( Port.FlowDirectionType NXOpen):  .
        """
        pass
    def GetForwardExtension(self) -> float:
        """
         Returns the forward extension value for a port i.e. the minimum length that
                   a segment must remain straight coming out of a NXOpen.Routing.Port 
         Returns extension (float):  Port extension .
        """
        pass
    def GetForwardExtensionObject(self) -> NXOpen.Expression:
        """
         Returns the forward extension object for a port. 
         Returns forwardExtension ( NXOpen.Expression):  Forward Extension Expression. .
        """
        pass
    def GetOccurrence(self) -> NXOpen.NXObject:
        """
         Returns the occurrence of the given port.
                    If the given port is a port extract, uses the port extract data to find the source
                    occurrence.  Only establishes an occurrence if the extract xform and the source
                    (prototype) port are loaded.  Returns a  otherwise.
                    Given any other port, tries to find an occurrence under the work occurrence.
                
         Returns portOccurrence ( NXOpen.NXObject): .
        """
        pass
    def GetPortConnection(self) -> PortConnection:
        """
         If port is connected to another port, returns the Port Connection that links them.
                    Returns  otherwise. 
         Returns portConnection ( PortConnection NXOpen): .
        """
        pass
    def GetPortType(self) -> Port.PortType:
        """
         Get the type of Port 
         Returns type ( Port.PortType NXOpen):  Port Type .
        """
        pass
    def GetReferenceCharacteristic(self, name: str) -> str:
        """
         Gets a reference characteristic from the port. 
         Returns value (str):  .
        """
        pass
    def GetRotationObject(self) -> NXOpen.DisplayableObject:
        """
         Retrieves the object used to derive the rotation vector of Port 
         Returns rotationObject ( NXOpen.DisplayableObject):  Object used to derive the rotation vector .
        """
        pass
    def GetRotationVector(self) -> NXOpen.Vector3d:
        """
         Retrieves the rotation vector of Port 
         Returns vector ( NXOpen.Vector3d):  Vector direction in absolute co-ordinate system .
        """
        pass
    def GetSegment(self) -> ISegment:
        """
         Return the segment the port position and alignment are derived from
                    Returns  if the port is not derived from segment 
         Returns segment ( ISegment NXOpen):  ISegment from which the port is derived .
        """
        pass
    def GetStockOfPort(self) -> Stock:
        """
         For a Routing.StockPort, returns the Routing.Stock
                    to which this port is attached, if any. Returns  otherwise for all other types of ports. 
         Returns stock ( Stock NXOpen):  .
        """
        pass
    def IsEngagementLocked(self, portToCheck: Port) -> bool:
        """
        Checks to see if ports are engaged.
         Returns engagementLocked (bool):  .
        """
        pass
    def IsRotationLocked(self, portToCheck: Port) -> bool:
        """
        Checks if ports have their rotation vectors locked. 
         Returns rotationLocked (bool):  .
        """
        pass
    def LockEngagement(self, portToLock: Port) -> List[NXOpen.Positioning.Constraint]:
        """
        Locks the port engagement using dcm3 constraints
         Returns newConstraints ( NXOpen.Positioning.Constraint Li):  Newly created port constraints .
        """
        pass
    def LockRotation(self, portToLock: Port) -> List[NXOpen.Positioning.Constraint]:
        """
        Locks the port rotation vector using dcm3 constraints
         Returns newConstraints ( NXOpen.Positioning.Constraint Li):  Newly created port constraints .
        """
        pass
    def ReorderFeature(self) -> None:
        """
         Reorders the NXOpen.Routing.FeaturePort object associated with
                   NXOpen.Routing.Port after all of the features on which the
                   port feature depends. Does nothing if the port was created
                   in preNX6 release and not converted to NXOpen.Routing.FeaturePort.
                   To convert NXOpen.Routing.Port object to NXOpen.Routing.FeaturePort object
                   use Routing.PortCollection.ConvertToFeatures. 
        """
        pass
    def SetClockIncrement(self, increment: float) -> None:
        """
         The clock angle increment value of NXOpen.Routing.Port 
        """
        pass
    def SetFlowDirection(self, flow_direction: Port.FlowDirectionType) -> None:
        """
         Set the flow direction value of NXOpen.Routing.Port 
        """
        pass
    def SetReferenceCharacteristic(self, name: str, value: str) -> None:
        """
         Sets a reference characteristics on the port. 
        """
        pass
    def UnlockEngagement(self, portToUnlock: Port) -> None:
        """
        Unlocks the port engagement
        """
        pass
    def UnlockRotation(self, portToUnlock: Port) -> None:
        """
        Unlocks the port rotation
        """
        pass
class ProfileFrom(Enum):
    """
    Members Include: 
     |Start|   Profile is at the start of the first segment. 
     |End|   Profile is at the end of the last segment. 

    """
    Start: int
    End: int
    @staticmethod
    def ValueOf(value: int) -> ProfileFrom:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class ProxyPortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.ProxyPort objects. """
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float) -> ProxyPort:
        """
         Creates a ProxyPort with a rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d) -> ProxyPort:
        """
         Creates a ProxyPort with no rotation vector at an absolute location.  Default
                    allows multiple connections to this port. 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, axis: NXOpen.Axis, allowMultipleConnections: bool) -> ProxyPort:
        """
         Creates a ProxyPort with a rotation vector on an axis 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, derivationObject: NXOpen.Axis, allowMultipleConnections: bool) -> ProxyPort:
        """
         Creates a ProxyPort with no rotation vector on an axis 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, point: NXOpen.Point) -> ProxyPort:
        """
         Creates a ProxyPort with a rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, point: NXOpen.Point) -> ProxyPort:
        """
         Creates a ProxyPort with no rotation vector at a point.  Default
                    allows multiple connections to this port. 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, axis: NXOpen.Axis) -> ProxyPort:
        """
         Creates a ProxyPort with a rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, derivationObject: NXOpen.Axis) -> ProxyPort:
        """
         Creates a ProxyPort with no rotation vector on an axis.  Default
                    allows multiple connections to this port. 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, allowMultipleConnections: bool) -> ProxyPort:
        """
         Creates a ProxyPort with a rotation vector at an absolute location 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, allowMultipleConnections: bool) -> ProxyPort:
        """
         Creates a ProxyPort with no rotation vector at an absolute location 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, rotationVector: NXOpen.Vector3d, rotationObject: NXOpen.DisplayableObject, clockAngle: float, point: NXOpen.Point, allowMultipleConnections: bool) -> ProxyPort:
        """
         Creates a ProxyPort with a rotation vector at a point 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
    @overload
    def CreateProxyPort(self, origin: NXOpen.Point3d, alignmentVector: NXOpen.Vector3d, point: NXOpen.Point, allowMultipleConnections: bool) -> ProxyPort:
        """
         Creates a ProxyPort with no rotation vector at a point 
         Returns proxyPort ( ProxyPort NXOpen):  .
        """
        pass
import NXOpen
class ProxyPort(Port): 
    """ A NXOpen.Routing.ProxyPort is a port that represents a connector in
     another design zone, but not present in this design zone. NXOpen.Routing.ProxyPort
     can be assigned to a connector using the NXOpen.Routing.Electrical.ConnectorDevice
     class method NXOpen.Routing.Electrical.ConnectorDevice.ProxyAssignConnector """
    @property
    def Axis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @Axis.setter
    def Axis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @property
    def CutbackLengthObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @CutbackLengthObject.setter
    def CutbackLengthObject(self, cutback_length: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @property
    def EngagementObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @EngagementObject.setter
    def EngagementObject(self, engagement: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @property
    def ForwardExtensionObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @ForwardExtensionObject.setter
    def ForwardExtensionObject(self, forward_extension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
import NXOpen
class QualifyPortBuilder(NXOpen.Builder): 
    """ Builder for creatingediting ports. """
    class CreatePortType(Enum):
        """
        Members Include: 
         |Fitting|  Fitting Port. 
         |Fixture|  Fixture Port. 
         |Multi|  Multi Port. 

        """
        Fitting: int
        Fixture: int
        Multi: int
        @staticmethod
        def ValueOf(value: int) -> QualifyPortBuilder.CreatePortType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositioningMethodType(Enum):
        """
        Members Include: 
         |PointAndVector|  Point and Vector. 
         |MidpointOnFace|  Midpoint on Face. 
         |BetweenTwoLines|  Between Two Lines. 

        """
        PointAndVector: int
        MidpointOnFace: int
        BetweenTwoLines: int
        @staticmethod
        def ValueOf(value: int) -> QualifyPortBuilder.PositioningMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AlignVector
         Returns the align vector   
            
         
        """
        pass
    @AlignVector.setter
    def AlignVector(self, alignVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AlignVector
         Returns the align vector   
            
         
        """
        pass
    @property
    def AlignVectorUserDefined(self) -> bool:
        """
        Getter for property: (bool) AlignVectorUserDefined
         Returns the align vector user defined   
            
         
        """
        pass
    @AlignVectorUserDefined.setter
    def AlignVectorUserDefined(self, alignVectorUserDefined: bool):
        """
        Setter for property: (bool) AlignVectorUserDefined
         Returns the align vector user defined   
            
         
        """
        pass
    @property
    def AllowMultiConnections(self) -> bool:
        """
        Getter for property: (bool) AllowMultiConnections
         Returns the allow multiple connections   
            
         
        """
        pass
    @AllowMultiConnections.setter
    def AllowMultiConnections(self, multiConnections: bool):
        """
        Setter for property: (bool) AllowMultiConnections
         Returns the allow multiple connections   
            
         
        """
        pass
    @property
    def AllowPortEngagement(self) -> bool:
        """
        Getter for property: (bool) AllowPortEngagement
         Returns the allow port engagement   
            
         
        """
        pass
    @AllowPortEngagement.setter
    def AllowPortEngagement(self, allowPortEngagement: bool):
        """
        Setter for property: (bool) AllowPortEngagement
         Returns the allow port engagement   
            
         
        """
        pass
    @property
    def BackExtension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BackExtension
         Returns the back extension   
            
         
        """
        pass
    @BackExtension.setter
    def BackExtension(self, backExtension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) BackExtension
         Returns the back extension   
            
         
        """
        pass
    @property
    def ClockingAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ClockingAngle
         Returns the clocking angle   
            
         
        """
        pass
    @property
    def CutbackLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutbackLength
         Returns the cutback length   
            
         
        """
        pass
    @CutbackLength.setter
    def CutbackLength(self, cutbackLength: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) CutbackLength
         Returns the cutback length   
            
         
        """
        pass
    @property
    def Face(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) Face
         Returns the face for positioning method Midpoint on Face   
            
         
        """
        pass
    @property
    def FlowDirection(self) -> Port.FlowDirectionType:
        """
        Getter for property: ( Port.FlowDirectionType NXOpen) FlowDirection
         Returns the flow direction   
            
         
        """
        pass
    @FlowDirection.setter
    def FlowDirection(self, flowDirection: Port.FlowDirectionType):
        """
        Setter for property: ( Port.FlowDirectionType NXOpen) FlowDirection
         Returns the flow direction   
            
         
        """
        pass
    @property
    def LengthAddition(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthAddition
         Returns the length addition   
            
         
        """
        pass
    @LengthAddition.setter
    def LengthAddition(self, lengthAddition: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) LengthAddition
         Returns the length addition   
            
         
        """
        pass
    @property
    def Line1(self) -> NXOpen.SelectICurve:
        """
        Getter for property: ( NXOpen.SelectICurve) Line1
         Returns the first line for positioning method Between Two Lines   
            
         
        """
        pass
    @property
    def Line2(self) -> NXOpen.SelectICurve:
        """
        Getter for property: ( NXOpen.SelectICurve) Line2
         Returns the second line for positioning method Between Two Lines   
            
         
        """
        pass
    @property
    def OffsetExpression(self) -> str:
        """
        Getter for property: (str) OffsetExpression
         Returns the offset expression   
            
         
        """
        pass
    @OffsetExpression.setter
    def OffsetExpression(self, offsetExpression: str):
        """
        Setter for property: (str) OffsetExpression
         Returns the offset expression   
            
         
        """
        pass
    @property
    def OffsetVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) OffsetVector
         Returns the offset vector   
            
         
        """
        pass
    @OffsetVector.setter
    def OffsetVector(self, offsetVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) OffsetVector
         Returns the offset vector   
            
         
        """
        pass
    @property
    def OffsetVectorUserDefined(self) -> bool:
        """
        Getter for property: (bool) OffsetVectorUserDefined
         Returns the offset vector user defined   
            
         
        """
        pass
    @OffsetVectorUserDefined.setter
    def OffsetVectorUserDefined(self, offsetVectorUserDefined: bool):
        """
        Setter for property: (bool) OffsetVectorUserDefined
         Returns the offset vector user defined   
            
         
        """
        pass
    @property
    def OriginPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) OriginPoint
         Returns the origin point   
            
         
        """
        pass
    @OriginPoint.setter
    def OriginPoint(self, originPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) OriginPoint
         Returns the origin point   
            
         
        """
        pass
    @property
    def PortEngagement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PortEngagement
         Returns the port engagement   
            
         
        """
        pass
    @PortEngagement.setter
    def PortEngagement(self, portEngagement: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) PortEngagement
         Returns the port engagement   
            
         
        """
        pass
    @property
    def PortExtension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PortExtension
         Returns the port extension   
            
         
        """
        pass
    @PortExtension.setter
    def PortExtension(self, portExtension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) PortExtension
         Returns the port extension   
            
         
        """
        pass
    @property
    def PortNameString(self) -> str:
        """
        Getter for property: (str) PortNameString
         Returns the port name string   
            
         
        """
        pass
    @PortNameString.setter
    def PortNameString(self, portNameString: str):
        """
        Setter for property: (str) PortNameString
         Returns the port name string   
            
         
        """
        pass
    @property
    def PortType(self) -> QualifyPortBuilder.CreatePortType:
        """
        Getter for property: ( QualifyPortBuilder.CreatePortType NXOpen) PortType
         Returns the port type   
            
         
        """
        pass
    @PortType.setter
    def PortType(self, portType: QualifyPortBuilder.CreatePortType):
        """
        Setter for property: ( QualifyPortBuilder.CreatePortType NXOpen) PortType
         Returns the port type   
            
         
        """
        pass
    @property
    def PositioningMethod(self) -> QualifyPortBuilder.PositioningMethodType:
        """
        Getter for property: ( QualifyPortBuilder.PositioningMethodType NXOpen) PositioningMethod
         Returns the positioning method type   
            
         
        """
        pass
    @PositioningMethod.setter
    def PositioningMethod(self, positioningMethod: QualifyPortBuilder.PositioningMethodType):
        """
        Setter for property: ( QualifyPortBuilder.PositioningMethodType NXOpen) PositioningMethod
         Returns the positioning method type   
            
         
        """
        pass
    @property
    def ReverseVector(self) -> bool:
        """
        Getter for property: (bool) ReverseVector
         Returns the reverse vector   
            
         
        """
        pass
    @ReverseVector.setter
    def ReverseVector(self, reverseVector: bool):
        """
        Setter for property: (bool) ReverseVector
         Returns the reverse vector   
            
         
        """
        pass
    @property
    def RotationVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) RotationVector
         Returns the rotation vector   
            
         
        """
        pass
    @RotationVector.setter
    def RotationVector(self, rotationVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) RotationVector
         Returns the rotation vector   
            
         
        """
        pass
    @property
    def SpoolDelimiter(self) -> bool:
        """
        Getter for property: (bool) SpoolDelimiter
         Returns the spool delimiter   
            
         
        """
        pass
    @SpoolDelimiter.setter
    def SpoolDelimiter(self, spoolDelimiter: bool):
        """
        Setter for property: (bool) SpoolDelimiter
         Returns the spool delimiter   
            
         
        """
        pass
    @property
    def StockOffset(self) -> bool:
        """
        Getter for property: (bool) StockOffset
         Returns the stock offset   
            
         
        """
        pass
    @StockOffset.setter
    def StockOffset(self, stockOffset: bool):
        """
        Setter for property: (bool) StockOffset
         Returns the stock offset   
            
         
        """
        pass
import NXOpen
class QuickPathBuilder(NXOpen.Builder): 
    """ 
        Builder for creating a path between user selected points.

        After invoking the commit method, invoke the 
        NXOpen.Routing.QuickPathBuilder.PathErrors method to find
        out which sections between points contained errors.  
    """
    @property
    def PathErrors(self) -> NXOpen.ErrorList:
        """
        Getter for property: ( NXOpen.ErrorList) PathErrors
         Returns the errors associated with this path.  
           The list will be NULL if the
                    commit method has not been invoked yet. 
                  
         
        """
        pass
    @property
    def PathSettings(self) -> LinearPathSettings:
        """
        Getter for property: ( LinearPathSettings NXOpen) PathSettings
         Returns the linear path settings for this path.  
              
         
        """
        pass
    @property
    def PointList(self) -> NXOpen.PointList:
        """
        Getter for property: ( NXOpen.PointList) PointList
         Returns the list of path points.  
              
         
        """
        pass
    @property
    def RouteSegment(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) RouteSegment
         Returns the routing segment managed by the builder, if it exists.  
             
         
        """
        pass
    @property
    def StockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for this path.  
              
         
        """
        pass
    def SetListOfPointsToDraw(self, index: int, point: NXOpen.Point3d) -> None:
        """
         Save a point or extension point to the list of all points to draw on the screen.  
        """
        pass
    def SetListOfPointsToDrawCount(self, count: int) -> None:
        """
         Set the number of elements in the list of all points to draw on the screen.  
        """
        pass
import NXOpen
class RemoveDiscontinuityBuilder(NXOpen.Builder): 
    """ Builder class for remove discontinuity object """
    @property
    def DiscontinuityCorner(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) DiscontinuityCorner
         Returns the selected  NXOpen::Routing::RouteObjectCollector  which contains
                    discontinuity corner   
            
         
        """
        pass
import NXOpen
class ReuseLibrary(NXOpen.Object): 
    """ Represents a NXOpen.Routing.ReuseLibrary """
    class PartType(Enum):
        """
        Members Include: 
         |Gasket|  Gasket Post Placement Type 
         |Bolt|  Bolt Post Placement Type 
         |Stud|  Stud Post Placement Type 
         |Nut|  Nut Post Placement Type 
         |Washer|  Washer Post Placement Type 
         |Weldring|  Weld Ring Post Placement Type 
         |Ringjoint|  Ring Joint Post Placement Type 
         |Unknown|  Unknown Type 

        """
        Gasket: int
        Bolt: int
        Stud: int
        Nut: int
        Washer: int
        Weldring: int
        Ringjoint: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> ReuseLibrary.PartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ReportInBom(Enum):
        """
        Members Include: 
         |DoNotReport|  Do not report in the Bill of Materials 
         |Report|  Report in the Bill of Materials 

        """
        DoNotReport: int
        Report: int
        @staticmethod
        def ValueOf(value: int) -> ReuseLibrary.ReportInBom:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddNewSpecification(self, specName: str) -> None:
        """
         Adds a new empty specification to the library. The input name can be used
                    to configure the specification once it has been added. 
        """
        pass
    def DeleteSpecification(self, specName: str) -> None:
        """
         Delete a Specification from the reuse library. 
        """
        pass
    def GetMatchingParts(self, startingIdentifier: str, searchCriteria: CharacteristicList) -> List[CharacteristicList]:
        """
         Query the reuse library for all parts that match the given search criteria. The search will include
                    the given node and all of its children. 
         Returns searchResults ( CharacteristicList List[NXOp):  Search Results .
        """
        pass
    def GetPartInformationAtNode(self, nodeIdentifier: str) -> List[CharacteristicList]:
        """
         Given a node identifier, this routine will return all parts associated with that node.
         Returns parts ( CharacteristicList List[NXOp):  An array of parts. .
        """
        pass
    def PartLibraryGetChildNodes(self, nodeIdentifier: str) -> Tuple[List[str], List[str]]:
        """
         Given an identifier, this routine returns it's child identifiers. 
         Returns A tuple consisting of (childIdentifiers, names). 
         - childIdentifiers is: List[str]. The child node identifiers. .
         - names is: List[str]. The discipline start node identifiers.

        """
        pass
    def PartLibraryGetDisciplineRoots(self) -> Tuple[List[str], List[str]]:
        """
         Returns the identifiers which represent the start nodes for the current discipline. 
         Returns A tuple consisting of (identifiers, names). 
         - identifiers is: List[str]. The discipline start node identifiers.
         - names is: List[str]. The discipline start node identifiers.

        """
        pass
    def PartLibraryGetPartsAtNode(self, nodeIdentifier: str) -> CharacteristicList:
        """
         Given a node identifier, this routine will return all parts associated with that node.
         Returns charxToEdit ( CharacteristicList NXOpen):  An array of parts. .
        """
        pass
    def Reload(self) -> None:
        """
         Reloads all of the nodes of the Routing Reuse Library based on the current discipline. 
        """
        pass
    def ReloadSpecification(self, specName: str) -> None:
        """
         Reload a Specification into the reuse library. 
        """
        pass
    def ReloadSpecifications(self, forceReload: bool) -> None:
        """
         Reload Specifications into the reuse library. 
        """
        pass
    def SpecificationInitializeManager(self, specName: str, isEditFlag: bool) -> None:
        """
         Initializes the specification builder. isEditFlag needs to set true to edit the existing specification. 
        """
        pass
    def SpecificationsAddConnectionCompatibility(self, specName: str, connectionTypeOne: str, connectionTypeTwo: str) -> None:
        """
         Adds a connection compatibility to the specification. 
        """
        pass
    def SpecificationsAddGenericPostPlacement(self, specName: str, placedPartIdentifier: str, postPlacementIdentifier: str, searchAttributes: List[str]) -> None:
        """
         Add a generic post placmeent rule. 
        """
        pass
    def SpecificationsClearGenericPostPlacements(self, specificationName: str) -> None:
        """
         Clear the generic post placement specification. 
        """
        pass
    def SpecificationsDefinePostPlacementRules(self, specName: str, partType: ReuseLibrary.PartType, startingIdentifier: str, searchAttributes: List[str]) -> None:
        """
         Defines Post Placement rules. 
        """
        pass
    def SpecificationsDestroyManager(self) -> None:
        """
         Clear Specification Manager. 
        """
        pass
    def SpecificationsGetAttributeRelationships(self, specName: str, nodeIdentifier: str) -> Tuple[CharacteristicList, int]:
        """
         Gets the attribute relationships at a given library node. 
         Returns A tuple consisting of (attributeFilter, numFilters). 
         - attributeFilter is:  CharacteristicList NXOpen. Attribute filters. .
         - numFilters is: int.

        """
        pass
    def SpecificationsGetBranchTable(self, specName: str) -> Tuple[List[float], List[float]]:
        """
         Gets the branch compatibilities for the input specification. Compatibilities can be identified by indexing into
                    the NPSValues and NPS_BRANCHValues arrays. Index 0 in each array is a compatibility and so on. 
         Returns A tuple consisting of (npsValues, npsBranchValues). 
         - npsValues is: List[float]. The NPS Values. .
         - npsBranchValues is: List[float]. The NPS_BRANCH values. .

        """
        pass
    def SpecificationsGetConnectionCompatibilities(self, specName: str) -> Tuple[List[str], List[str]]:
        """
         Get the list of connection compatibilities from the specificaiton. 
         Returns A tuple consisting of (connectionTypesOne, connectionTypesTwo). 
         - connectionTypesOne is: List[str]. Values for the first CONNECTION_TYPE attribute. .
         - connectionTypesTwo is: List[str]. Values for the second CONNECTION_TYPE attribute. .

        """
        pass
    def SpecificationsGetConnectionPostPlacement(self, specName: str, connectionTypeOne: str, connectionTypeTwo: str) -> Tuple[bool, bool, bool, bool, bool, bool, bool]:
        """
         Get post placement options for a given connection. 
         Returns A tuple consisting of (gasket, bolt, stud, nut, washers, weldRing, ringJoints). 
         - gasket is: bool. Whether or not to place Gaskets for this connection. .
         - bolt is: bool. Whether or not to place Bolts for this connection. .
         - stud is: bool. Whether or not to place Studs for this connection. .
         - nut is: bool. Whether or not to place Nuts for this connection. .
         - washers is: bool. Whether or not to place Washers for this connection. .
         - weldRing is: bool. Whether or not to place Weld Rings for this connection. .
         - ringJoints is: bool.

        """
        pass
    def SpecificationsGetCurrent(self) -> str:
        """
         Returns the name of the current specification. 
         Returns currentSpec (str):  The name of the current specification. .
        """
        pass
    def SpecificationsGetDescription(self, specName: str) -> str:
        """
         Gets the description of a specification.  
         Returns description (str):  Specification description. .
        """
        pass
    def SpecificationsGetDisciplineSpecifications(self) -> List[str]:
        """
         Returns the names of all of the specifications that are defined for the current discipline. 
         Returns specs (List[str]):  Specification names. .
        """
        pass
    def SpecificationsGetGeneralConnectionOptions(self, specName: str) -> Tuple[bool, bool, float, float, float]:
        """
         Gets the general connection options. 
         Returns A tuple consisting of (modelGaskets, modelWeldGaps, additionalBoltLength, additionalStudLength, weldGapValue). 
         - modelGaskets is: bool. Whether or not to model Gaskets .
         - modelWeldGaps is: bool. Whether or not to model Weld Gaps .
         - additionalBoltLength is: float. Additional length for bolts. .
         - additionalStudLength is: float. Additional length for studs.
         - weldGapValue is: float.

        """
        pass
    def SpecificationsGetGenericPostPlacementSearchAttributes(self, specName: str, placedPartIdentifier: str, postPlacementIdentifier: str) -> List[str]:
        """
         Get the generic post placement search attributes. 
         Returns searchAttributes (List[str]):  Attribute search titles. .
        """
        pass
    def SpecificationsGetGenericPostPlacements(self, specName: str) -> Tuple[List[str], List[str]]:
        """
         Gets the defined generic post placement rules. 
         Returns A tuple consisting of (placedPartIdentifier, postPlacementIdentifier). 
         - placedPartIdentifier is: List[str]. The list of placed part node identifiers .
         - postPlacementIdentifier is: List[str]. The list of post placement node identifiers. .

        """
        pass
    def SpecificationsGetPostPlacementRules(self, specName: str, partType: ReuseLibrary.PartType) -> Tuple[str, List[str]]:
        """
         Gets post placement rules. 
         Returns A tuple consisting of (startingIdentifier, searchAttributes). 
         - startingIdentifier is: str. Library node to begin searching from. .
         - searchAttributes is: List[str]. Search Attribute Titles. .

        """
        pass
    def SpecificationsGetReportInBom(self, specName: str) -> Tuple[bool, bool, bool, bool, bool, bool, bool, bool]:
        """
         Gets the Report in BOM flags. 
         Returns A tuple consisting of (gasket, bolt, stud, nut, washers, weldRing, ringJoints, weldGap). 
         - gasket is: bool. Report Gaskets .
         - bolt is: bool. Report Bolts .
         - stud is: bool. Report Studs.
         - nut is: bool. Report Nuts.
         - washers is: bool. Report Washers.
         - weldRing is: bool. Report Weld Rings.
         - ringJoints is: bool. Report Ring Joints.
         - weldGap is: bool.

        """
        pass
    def SpecificationsRemoveAttribute(self, specificationName: str, connectionTypeOne: str) -> None:
        """
         Removes the attribute of given connection type in conncetion compatibility table of a specification 
        """
        pass
    def SpecificationsRemoveAttributeRelationships(self, specificationName: str, index: int) -> None:
        """
         Remove the attribute relationships for a specification at a given index. 
        """
        pass
    def SpecificationsRemoveBranchCompatibility(self, specName: str, nps: float, npsBranch: float) -> None:
        """
         Removes a branch compatibility 
        """
        pass
    def SpecificationsRemoveConnectionCompatibility(self, specName: str, connectionTypeOne: str, connectionTypeTwo: str) -> None:
        """
         Removes a connection compatibility from the specification. 
        """
        pass
    def SpecificationsRemoveGenericPostPlacement(self, specName: str, placedPartIdentifier: str, postPlacementIdentifier: str) -> None:
        """
         Remove a generic post placement option.
        """
        pass
    def SpecificationsSetAdditionalConnectionOptions(self, specName: str, modelGaskets: bool, additionalBoltLength: float, additionalStudLength: float) -> None:
        """
         Sets the Additional Connection Options. 
        """
        pass
    def SpecificationsSetAttributeRelationships(self, specName: str, nodeIdentifier: str, attributeFilter: CharacteristicList) -> None:
        """
         Sets the attribute relationships for a specification. 
        """
        pass
    def SpecificationsSetBranchCompatibility(self, specName: str, nps: float, npsBranch: float) -> None:
        """
         Sets a branch compatibility. 
        """
        pass
    def SpecificationsSetConnectionPostPlacement(self, specName: str, connectionTypeOne: str, connectionTypeTwo: str, gasket: bool, bolt: bool, stud: bool, nut: bool, washers: bool, weldRing: bool, ringJoints: bool) -> None:
        """
         Set Connection post placement rules on a valid connection. 
        """
        pass
    def SpecificationsSetDescription(self, specName: str, description: str) -> None:
        """
         Sets the description text for a specification. 
        """
        pass
    def SpecificationsSetDiscipline(self, specificationName: str, discipline: str) -> None:
        """
         Set the discipline for a specification 
        """
        pass
    def SpecificationsSetPostPlacementReportInBom(self, specName: str, gasket: bool, bolt: bool, stud: bool, nut: bool, washers: bool, ringJoints: bool) -> None:
        """
         Sets the post placement report in BOM flags. 
        """
        pass
    def SpecificationsTogglePostPlacementOption(self, specificationName: str, connectionTypeOne: str, connectionTypeTwo: str, partType: ReuseLibrary.PartType) -> None:
        """
         Toggles the post placement option of given connection type of a specification 
        """
        pass
    def SpecificationsUpdateAttributeRelationship(self, specificationName: str, nodeIdentifier: str, index: int, title: str, value: str) -> None:
        """
         Update the attribute relationship for a specification at a given index. 
        """
        pass
import NXOpen
class RootObject(NXOpen.NXObject): 
    """
        
        The NXOpen.Routing.RootObject is the parent
        class of all other Routing logical objects.  Every child inherits the Global Object
        Identifier (GUID) attribute and methods from NXOpen.Routing.RootObject.
        
        
        See NX Routing help for the Connectivity data model documentation.
        
     """
    @property
    def Guid(self) -> str:
        """
        Getter for property: (str) Guid
         Returns the object's Global Unique Identifier (GUID).  
             
         
        """
        pass
    @Guid.setter
    def Guid(self, guid: str):
        """
        Setter for property: (str) Guid
         Returns the object's Global Unique Identifier (GUID).  
             
         
        """
        pass
import NXOpen
class RouteLogicalAssociationCollection(NXOpen.TaggedObjectCollection): 
    """ Collection class for RouteLogicalAssociation object """
    def CreateLogicalAssociation(self, name: str, control: NXOpen.NXObject, targets: List[NXOpen.NXObject], include_stocks: bool) -> RouteLogicalAssociation:
        """
         Creates a NXOpen.Routing.RouteLogicalAssociation 
         Returns lao ( RouteLogicalAssociation NXOpen):  Logical Association .
        """
        pass
    def GetLogicalAssociations(self) -> List[RouteLogicalAssociation]:
        """
         Returns NXOpen.Routing.RouteLogicalAssociation of this part. 
         Returns logical_associations ( RouteLogicalAssociation List[NXOp):  .
        """
        pass
    def PerformLogicalAssociation(self, logical_associations: List[RouteLogicalAssociation]) -> None:
        """
         Performs the blankingsuppressing of objects in NXOpen.Routing.RouteLogicalAssociation. 
        """
        pass
import NXOpen
class RouteLogicalAssociation(NXOpen.NXObject): 
    """ RouteLogicalAssociation object associates non-electrical components to 
        electrical components. Logical Associations have control objects and 
        target objects.  Meeting control object's condition applies actions to 
        target objects. Example: Control object is a NXOpen.Routing.ISegment
        and the target object is a clip or clamp which supports the harness. When
        the segment is routed (i.e. condition on control object is satisfied), 
        the action is to suppress the target (clip or clamp) """
    def AddTarget(self, target: NXOpen.NXObject) -> None:
        """
         Adds target to Logical Assocition 
        """
        pass
    def EnableLogicalAssociation(self, enable: bool) -> None:
        """
         Set Logical Association to enabled state or disabled state.                 
                   True sets LAO to enabled state, False sets LAO to disabled state.
                  
        """
        pass
    def GetControl(self) -> NXOpen.NXObject:
        """
         Retrieves the control for LogicalAssocition 
         Returns control ( NXOpen.NXObject):  Control .
        """
        pass
    def GetRoutedCondition(self) -> bool:
        """
         Get the routed condition of a logical association object.  
                   The routed condition evaluates the state of the control object.
                   True if condition is ROUTED, False if UNROUTED 
                  
         Returns condition (bool):   .
        """
        pass
    def GetTargets(self) -> List[NXOpen.NXObject]:
        """
         Get all the targets LogicalAssocition 
         Returns targets ( NXOpen.NXObject Li):  Targets of current logical association  .
        """
        pass
    def Perform(self) -> None:
        """
         Performs the specified action (suppress or unsuppress) on the 
                    RouteLogicalAssociation Object 
        """
        pass
    def Remove(self) -> None:
        """
         Removes the RouteLogicalAssociation object 
        """
        pass
    def RemoveTarget(self, target: NXOpen.NXObject) -> None:
        """
         Removes the target from Logical Assocition 
        """
        pass
    def SetControl(self, control: NXOpen.NXObject) -> None:
        """
         Sets the control for LogicalAssocition 
        """
        pass
    def SetRoutedCondition(self, condition: bool) -> None:
        """
         Set the routed condition of a logical association object 
                   The routed condition evaluates the state of the control object.
                   True if condition is ROUTED, False if UNROUTED 
                  
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Formboard
import NXOpen.Routing.Electrical
class RouteManager(NXOpen.Object): 
    """ Manages various Routing collections and methods for use in the current work part.
        
        See the NX Routing help for detailed information on the Connection data model.
        
    """
    class BomBlankLines(Enum):
        """
        Members Include: 
         |Off|  
         |On|  

        """
        Off: int
        On: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.BomBlankLines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BomFabrication(Enum):
        """
        Members Include: 
         |Off|  
         |On|  

        """
        Off: int
        On: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.BomFabrication:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BomLevel(Enum):
        """
        Members Include: 
         |Summery|  
         |Itemized|  

        """
        Summery: int
        Itemized: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.BomLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BomStockLength(Enum):
        """
        Members Include: 
         |SingleSum|  
         |ListEach|  

        """
        SingleSum: int
        ListEach: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.BomStockLength:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColumnStatus(Enum):
        """
        Members Include: 
         |NotHidden|  Column is displayed in Specify Item. 
         |Hidden|  Column is not displayed in Specify Item. 

        """
        NotHidden: int
        Hidden: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.ColumnStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FindObjectType(Enum):
        """
        Members Include: 
         |Harness|   
         |Cable|   
         |Shield|   
         |Connector|   
         |Device|   
         |Connection|   
         |Wire|   
         |Unknown|   

        """
        Harness: int
        Cable: int
        Shield: int
        Connector: int
        Device: int
        Connection: int
        Wire: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.FindObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FixPosition(Enum):
        """
        Members Include: 
         |Off|  
         |On|  

        """
        Off: int
        On: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.FixPosition:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImportMode(Enum):
        """
        Members Include: 
         |Update|  Update existing objects with data from the imported objects. 
         |Merge|  Update existing objects with data from the imported objects. 
         |Append|  Create the imported objects as new objects. 
         |Derivative|  Create the imported harnesses as derivatives harnesses 

        """
        Update: int
        Merge: int
        Append: int
        Derivative: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.ImportMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JsonInformation(Enum):
        """
        Members Include: 
         |Splice|  
         |Clocking|  
         |Twist|  
         |All|  

        """
        Splice: int
        Clocking: int
        Twist: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.JsonInformation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PartType(Enum):
        """
        Members Include: 
         |Part|   
         |Stock|   
         |Fabrication|   
         |StockComponent|   
         |WireComponent|   
         |Overstock|   
         |Logical|   
         |TemplateAssy|   
         |Connector|   
         |Splice|   
         |Device|   
         |Filler|   
         |Unknown|   

        """
        Part: int
        Stock: int
        Fabrication: int
        StockComponent: int
        WireComponent: int
        Overstock: int
        Logical: int
        TemplateAssy: int
        Connector: int
        Splice: int
        Device: int
        Filler: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.PartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RootType(Enum):
        """
        Members Include: 
         |Top|  Top of entire part table. 
         |Stock|  Top node for selecting stocks.
         |Wire|  Top node for selecting wires. 
         |Part|  Top node for selecting parts. 

        """
        Top: int
        Stock: int
        Wire: int
        Part: int
        @staticmethod
        def ValueOf(value: int) -> RouteManager.RootType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SearchCriteria:
        """
         Fill in this information with as much as you know about the object you want to find. 
         RouteManagerSearchCriteria_Struct NXOpen is an alias for  RouteManager.SearchCriteria NXOpen.
        """
        @property
        def ObjectType(self) -> RouteManager.FindObjectType:
            """
            Getter for property ObjectType
            Required.

            """
            pass
        @ObjectType.setter
        def ObjectType(self, value: RouteManager.FindObjectType):
            """
            Getter for property ObjectType
            Required.
            Setter for property ObjectType
            Required.

            """
            pass
        @property
        def OwningHarness(self) -> NXOpen.Routing.Electrical.HarnessDevice:
            """
            Getter for property OwningHarness
            Optional.

            """
            pass
        @OwningHarness.setter
        def OwningHarness(self, value: NXOpen.Routing.Electrical.HarnessDevice):
            """
            Getter for property OwningHarness
            Optional.
            Setter for property OwningHarness
            Optional.

            """
            pass
        @property
        def ApplicationName(self) -> str:
            """
            Getter for property ApplicationName
            Optional.

            """
            pass
        @ApplicationName.setter
        def ApplicationName(self, value: str):
            """
            Getter for property ApplicationName
            Optional.
            Setter for property ApplicationName
            Optional.

            """
            pass
        @property
        def UniqueID(self) -> str:
            """
            Getter for property UniqueID
            Optional.

            """
            pass
        @UniqueID.setter
        def UniqueID(self, value: str):
            """
            Getter for property UniqueID
            Optional.
            Setter for property UniqueID
            Optional.

            """
            pass
    @property
    def DownDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DownDirection
         Returns the down direction for the part used by Routing.  
             
         
        """
        pass
    @DownDirection.setter
    def DownDirection(self, down_direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DownDirection
         Returns the down direction for the part used by Routing.  
             
         
        """
        pass
    @property
    def PartTypeFlag(self) -> RouteManager.PartType:
        """
        Getter for property: ( RouteManager.PartType NXOpen) PartTypeFlag
         Returns the type for the part used by Routing.  
             
         
        """
        pass
    @PartTypeFlag.setter
    def PartTypeFlag(self, type: RouteManager.PartType):
        """
        Setter for property: ( RouteManager.PartType NXOpen) PartTypeFlag
         Returns the type for the part used by Routing.  
             
         
        """
        pass
    @property
    def BuiltInPaths() -> BuiltInPathCollection:
        """
         BuiltInPath collection 
        """
        pass
    @property
    def CablewayNetworks() -> CablewayNetworkCollection:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    @property
    def ControlPoints() -> ControlPointCollection:
        """
         ControlPoint collection 
        """
        pass
    @property
    def Ports() -> PortCollection:
        """
         Port Collection 
        """
        pass
    @property
    def PortConnections() -> PortConnectionCollection:
        """
         PortConnection Collection 
        """
        pass
    @property
    def FixturePorts() -> FixturePortCollection:
        """
         FixturePort Collection 
        """
        pass
    @property
    def FittingPorts() -> FittingPortCollection:
        """
         FittingPort Collection 
        """
        pass
    @property
    def MultiPorts() -> MultiPortCollection:
        """
         MultiPort Collection 
        """
        pass
    @property
    def TerminalPorts() -> TerminalPortCollection:
        """
         TerminalPort Collection 
        """
        pass
    @property
    def ProxyPorts() -> ProxyPortCollection:
        """
         ProxyPort Collection 
        """
        pass
    @property
    def StockOffsetPorts() -> StockOffsetPortCollection:
        """
         Stock Offset Port Collection. 
        """
        pass
    @property
    def OffsetPaths() -> OffsetPathCollection:
        """
         OffsetPath Collection 
        """
        pass
    @property
    def Runs() -> RunCollection:
        """
         Run Collection 
        """
        pass
    @property
    def RoutingSystems() -> RoutingSystemCollection:
        """
         RoutingSystem Collection 
        """
        pass
    @property
    def RouteLogicalAssociations() -> RouteLogicalAssociationCollection:
        """
         RouteLogicalAssociation Collection 
        """
        pass
    @property
    def Corners() -> CornerCollection:
        """
         Corner collection 
        """
        pass
    @property
    def BendCorners() -> BendCornerCollection:
        """
         BendCorner collection 
        """
        pass
    @property
    def CopeCorners() -> CopeCornerCollection:
        """
         CopeCorner collection 
        """
        pass
    @property
    def DiscontinuityCorners() -> DiscontinuityCornerCollection:
        """
         DiscontinuityCorner collection 
        """
        pass
    @property
    def MiterCorners() -> MiterCornerCollection:
        """
         MiterCorner collection 
        """
        pass
    @property
    def SBendCorners() -> SBendCornerCollection:
        """
         SBendCorner collection 
        """
        pass
    @property
    def MiteredBendCorners() -> MiteredBendCornerCollection:
        """
         MiteredBendCorner collection 
        """
        pass
    @property
    def RoutePartDescriptors() -> RoutePartDescriptorCollection:
        """
         RoutePartDescriptor collection 
        """
        pass
    @property
    def Anchors() -> AnchorCollection:
        """
         Anchor collection 
        """
        pass
    @property
    def Stocks() -> StockCollection:
        """
         Stock collection 
        """
        pass
    @property
    def StockDatas() -> StockDataCollection:
        """
         StockData collection 
        """
        pass
    @property
    def CrossSections() -> CrossSectionCollection:
        """
         CrossSection collection 
        """
        pass
    @property
    def Wires() -> WireCollection:
        """
         Wire Collection 
        """
        pass
    @property
    def OverstockApplications() -> OverstockApplicationCollection:
        """
         OverstockApplication collection 
        """
        pass
    @property
    def Fillers() -> FillerCollection:
        """
         Filler stock Application collection 
        """
        pass
    @property
    def CableConnections() -> NXOpen.Routing.Electrical.CableConnectionCollection:
        """
         CableConnection collection 
        """
        pass
    @property
    def NonPathConnections() -> NXOpen.Routing.Electrical.NonPathConnectionCollection:
        """
         NonPathConnection collection 
        """
        pass
    @property
    def ConnectorDevices() -> NXOpen.Routing.Electrical.ConnectorDeviceCollection:
        """
         ConnectorDevice collection 
        """
        pass
    @property
    def HarnessDevices() -> NXOpen.Routing.Electrical.HarnessDeviceCollection:
        """
         HarnessDevice collection 
        """
        pass
    @property
    def DerivativeDevices() -> NXOpen.Routing.Electrical.DerivativeDeviceCollection:
        """
         DerivativeDevice collection 
        """
        pass
    @property
    def SystemDevices() -> NXOpen.Routing.Electrical.SystemDeviceCollection:
        """
         SystemDevice collection 
        """
        pass
    @property
    def ElectricalStockDevice() -> NXOpen.Routing.Electrical.ElectricalStockDeviceCollection:
        """
         ElectricalStockDevice collection 
        """
        pass
    @property
    def PathConnections() -> NXOpen.Routing.Electrical.PathConnectionCollection:
        """
         PathConnection collection 
        """
        pass
    @property
    def InterfaceTerminalRelationships() -> InterfaceTerminalRelationshipCollection:
        """
         InterfaceTerminalRelationship collection 
        """
        pass
    @property
    def JumperConnections() -> NXOpen.Routing.Electrical.JumperConnectionCollection:
        """
         JumperConnection collection 
        """
        pass
    @property
    def ElectricalDeviceRelationships() -> NXOpen.Routing.Electrical.ElectricalDeviceRelationshipCollection:
        """
         ElectricalDeviceRelationship Connection collection 
        """
        pass
    @property
    def DesignRules() -> DesignRuleCollection:
        """
         RoutingDesignRule collection 
        """
        pass
    @property
    def DesignRulesViolation() -> DesignRuleViolationCollection:
        """
         RoutingDesignRuleViolation collection 
        """
        pass
    @property
    def DesignRuleViolationLocation() -> DesignRuleViolationLocationCollection:
        """
         RoutingDesignRuleViolationLocation collection 
        """
        pass
    @property
    def ElectricalConnections() -> NXOpen.Routing.Electrical.ConnectionCollection:
        """
         Routing Electrical Connection collection 
        """
        pass
    @property
    def ElectricalFormats() -> NXOpen.Routing.Electrical.ElectricalFormatCollection:
        """
         Routing Electrical Format collection 
        """
        pass
    @property
    def ElectricalNavigatorFilters() -> NXOpen.Routing.Electrical.ElectricalNavigatorFilterCollection:
        """
         Routing Electrical Filter collection 
        """
        pass
    @property
    def FormboardManager() -> NXOpen.Formboard.FormboardManager:
        """
         Collection for managing Formboard data. 
        """
        pass
    @property
    def CablewaysLayoutViews() -> NXOpen.Routing.Electrical.CablewaysLayoutViewCollection:
        """
         Collection for managing Cableways Layout Views. 
        """
        pass
    @property
    def FittingOverstock() -> FittingOverstockCollection:
        """
         Routing FittingOverstock collection 
        """
        pass
    @property
    def SplicePoints() -> NXOpen.Routing.Electrical.SplicePointCollection:
        """
         Splice Point Collection 
        """
        pass
    @property
    def ReuseLibrary() -> ReuseLibrary:
        """
         Returns the  NXOpen::Routing::ReuseLibrary  object
        """
        pass
    @property
    def BendReportManager() -> BendReportManager:
        """
         Bend Report Manager 
        """
        pass
    def AssembleConnectionsImportedFromSubAssemblies(self) -> None:
        """
         Copies the connections, connectors and devices from the design elements of
                    study to the part containing object_in_part and assembles them. 
        """
        pass
    @overload
    def BuildFabrication(self, filename: str, objects: List[NXOpen.NXObject], charx_data: CharacteristicList) -> NXOpen.Part:
        """
         Creates a Routing fabrication, a sub-assembly made of
                    NXOpen.Assemblies.Components and
                    NXOpen.Routing.Stock from the assembly in which
                    the Routing Fabrication is created.
         Returns fab_part_obj ( NXOpen.Part): .
        """
        pass
    def BuildFabricationWithFileNewBuilder(self, builder: NXOpen.FileNew, objects: List[NXOpen.NXObject], optional_charx_data: CharacteristicList, required_charx_data: CharacteristicList) -> NXOpen.Part:
        """
        Create a Routing fabrication sub-assembly made of
                NXOpen.Assemblies.Components and
                NXOpen.Routing.Stock from the assembly in which
                the Routing Fabrication is created with help of FileNewBuilder.
         Returns fab_part_obj ( NXOpen.Part): .
        """
        pass
    @overload
    def BuildFabrication(self, filename: str, objects: List[NXOpen.NXObject], optional_charx_data: CharacteristicList, required_charx_data: CharacteristicList) -> NXOpen.Part:
        """
         Creates a Routing fabrication, a sub-assembly made of
                    NXOpen.Assemblies.Components and
                    NXOpen.Routing.Stock from the assembly in which
                    the Routing Fabrication is created.
         Returns fab_part_obj ( NXOpen.Part): .
        """
        pass
    @overload
    def CheckDesignRules(self, mode: DesignRuleViolationCollection.Mode, reason: DesignRuleViolationCollection.Reason, objects: List[NXOpen.NXObject]) -> List[DesignRuleViolation]:
        """
         Executes the Routing Design Rules against the work part 
         Returns violations ( DesignRuleViolation List[NXOp):  The violations generated by the check.  May be empty. .
        """
        pass
    @overload
    def CheckDesignRules(self, mode: DesignRuleViolationCollection.Mode, reason: CustomManager.DesignRuleReason, objects: List[NXOpen.NXObject]) -> List[DesignRuleViolation]:
        """
         Executes the Routing Design Rules against the work part 
         Returns violations ( DesignRuleViolation List[NXOp):  The violations generated by the check.  May be empty. .
        """
        pass
    def ComponentHasBIPGeometry(self, bipComponent: NXOpen.Assemblies.Component) -> bool:
        """
         Determines whether or not a built-in path component has proper work part geometry.
         Returns hasBipGeom (bool): .
        """
        pass
    def ConnectPartPorts(self, component: NXOpen.Assemblies.Component) -> None:
        """
         Connects ports present in this NXOpen.Assemblies.Component. 
        """
        pass
    def ConvertSplineSegments(self) -> Tuple[List[ISegment], List[float], List[float]]:
        """
         Converts all of the spline segments in this part from the pre-NX9 data model
                    to the NX9 data model.
                
         Returns A tuple consisting of (splineSegments, originalSplineLengths, newSplineLengths). 
         - splineSegments is:  ISegment List[NXOp. The converted spline segments.
         - originalSplineLengths is: List[float]. The length of each spline segment before converting.
         - newSplineLengths is: List[float]. The new length of each spline segment after converting.

        """
        pass
    def CopyOverstock(self) -> str:
        """
         Copy the overstock from subassembly to parent assembly.
                    This functionality, gets the segments which are WAVE-linked from the subassembly
                    to the parent assembly. It finds the overstock alloted to these segments in subassembly
                    and recreate them over WAVE-linked segment at the parent assembly level. 
         Returns msg (str):  .
        """
        pass
    def CreateAddFontBuilder(self) -> AddFontBuilder:
        """
         Creates a  NXOpen.Routing.AddFontBuilder for creating user-defined line fonts
                    to use with line segments.  
         Returns builder ( AddFontBuilder NXOpen):  .
        """
        pass
    def CreateAdvanceToRsdBuilder(self) -> AdvanceToRsdBuilder:
        """
         Creates a AdvanceToRsd builder.  See the documentation in the
                    NXOpen.Routing.AdvanceToRsdBuilder class for a description of the builder.  
         Returns builder ( AdvanceToRsdBuilder NXOpen): .
        """
        pass
    def CreateAlignStockBuilder(self) -> AlignStockBuilder:
        """
         Creates a NXOpen.Routing.AlignStockBuilder for aligning Routing Stocks.
                Provide a tool to align non-circular stocks to routing objects.
         Returns builder ( AlignStockBuilder NXOpen): .
        """
        pass
    def CreateAnchorBuilder(self, anchorObject: Anchor) -> AnchorBuilder:
        """
         Creates a NXOpen.Routing.AnchorBuilder that is used to qualify Anchor. 
         Returns builder ( AnchorBuilder NXOpen): .
        """
        pass
    @overload
    def CreateAssignCornerBuilder(self) -> AssignCornerBuilder:
        """
         Creates a NXOpen.Routing.AssignCornerBuilder which creates corner
         Returns builder ( AssignCornerBuilder NXOpen):  .
        """
        pass
    @overload
    def CreateAssignCornerBuilder(self, selectedObject: NXOpen.NXObject) -> AssignCornerBuilder:
        """
         Creates a NXOpen.Routing.AssignCornerBuilder which creates corner
         Returns builder ( AssignCornerBuilder NXOpen):  .
        """
        pass
    def CreateAssignDiscontinuityBuilder(self, selectedPoint: NXOpen.NXObject) -> AssignDiscontinuityBuilder:
        """
         Creates a NXOpen.Routing.AssignDiscontinuityBuilder 
         Returns builder ( AssignDiscontinuityBuilder NXOpen):  .
        """
        pass
    def CreateAssignPathBuilder(self, run: Run) -> AssignPathBuilder:
        """
         Creates a NXOpen.Routing.AssignPathBuilder 
         Returns builder ( AssignPathBuilder NXOpen): .
        """
        pass
    def CreateAssignProxyBuilder(self, objects: List[NXOpen.NXObject]) -> NXOpen.Routing.Electrical.AssignProxyBuilder:
        """
         Creates a proxy port assigned to a connector. See the documentation in the
                    NXOpen.Routing.Electrical.AssignProxyBuilder class for a description of
                    the builder. 
         Returns builder ( NXOpen.Routing.Electrical.AssignProxyBuilder): .
        """
        pass
    def CreateAssignTerminalsBuilder(self, port: Port) -> AssignTerminalsBuilder:
        """
         Creates a NXOpen.Routing.AssignTerminalsBuilder that is used to assign terminals to multiports
                
         Returns builder ( AssignTerminalsBuilder NXOpen): .
        """
        pass
    def CreateAssignTerminalsItemBuilder(self, port: Port) -> AssignTerminalsItemBuilder:
        """
         Creates a NXOpen.Routing.AssignTerminalsItemBuilder that is used to specify attributes 
                of a terminal ports like terminal name, terminal direction and terminal origin.
         Returns builder ( AssignTerminalsItemBuilder NXOpen): .
        """
        pass
    def CreateAttributeHolder(self) -> AttributeHolder:
        """
         Creates a NXOpen.Routing.AttributeHolder to set Template Attributes and
                    then copying Template Attributes to Routing Objects.
         Returns attributeHolder ( AttributeHolder NXOpen):  .
        """
        pass
    def CreateBom(self, level: RouteManager.BomLevel, length: RouteManager.BomStockLength, fab_numbering: RouteManager.BomFabrication, blank_lines: RouteManager.BomBlankLines, format_file_part: NXOpen.Part) -> None:
        """
         Creates Bill of Material (BOM). BOM generates a table with the relevant
                    information regarding the existing routing objects present in the NX window.
                    Various options are available on the BOM dialog to control the generated output.
                    These options are the inputs to this function. 
        """
        pass
    def CreateBranchPathNumberingBuilder(self) -> BranchPathNumberingBuilder:
        """
         Creates a NXOpen.Routing.BranchPathNumberingBuilder for labeling branches. 
         Returns builder ( BranchPathNumberingBuilder NXOpen):  .
        """
        pass
    def CreateBuiltInPathBuilder(self, bipObject: BuiltInPath) -> BuiltInPathBuilder:
        """
         Creates a NXOpen.Routing.BuiltInPathBuilder that is used to qualify Built-in Path. 
         Returns builder ( BuiltInPathBuilder NXOpen): .
        """
        pass
    def CreateCablewaysBuilder(self) -> NXOpen.Routing.Electrical.CablewaysBuilder:
        """
         Creates NXOpen.Routing.Electrical.CablewaysBuilder. 
         Returns builder ( NXOpen.Routing.Electrical.CablewaysBuilder):  .
        """
        pass
    def CreateCablewaysBuilderWithObjects(self, objects: List[NXOpen.NXObject]) -> NXOpen.Routing.Electrical.CablewaysBuilder:
        """
         Creates NXOpen.Routing.Electrical.CablewaysBuilder. 
         Returns builder ( NXOpen.Routing.Electrical.CablewaysBuilder):  .
        """
        pass
    def CreateCablewaysLayoutBuilder(self) -> NXOpen.Routing.Electrical.CablewaysLayoutBuilder:
        """
         Creates NXOpen.Routing.Electrical.CablewaysBuilder. 
         Returns builder ( NXOpen.Routing.Electrical.CablewaysLayoutBuilder):  .
        """
        pass
    def CreateClockPartBuilder(self, selectedPort: NXOpen.NXObject) -> ClockPartBuilder:
        """
         Creates a NXOpen.Routing.ClockPartBuilder. for the rotation of
                    component. 
         Returns builder ( ClockPartBuilder NXOpen):  .
        """
        pass
    def CreateCompareRunsBuilder(self, run: Run) -> CompareRunsBuilder:
        """
         Creates a NXOpen.Routing.CompareRunsBuilder to compare runs in the working part
                    to another part or an xml definition. 
         Returns builder ( CompareRunsBuilder NXOpen):  .
        """
        pass
    def CreateConnectPathBuilder(self) -> ConnectPathBuilder:
        """
         Creates a NXOpen.Routing.ConnectPathBuilder which connects path
         Returns builder ( ConnectPathBuilder NXOpen):  .
        """
        pass
    def CreateConnectedCurvesBuilder(self) -> ConnectedCurvesBuilder:
        """
         Creates a  NXOpen.Routing.ConnectedCurvesBuilder for building segments
                  on end-to-end connected curves. 
         Returns builder ( ConnectedCurvesBuilder NXOpen):  .
        """
        pass
    def CreateConnectionPostPlacementUdo(self, udoType: ReuseLibrary.PartType, numberOfItems: int, reportInBOM: ReuseLibrary.ReportInBom, udoCharx: CharacteristicList, connectionsToLink: List[PortConnection]) -> None:
        """
         Creates a user defined object (UDO) linked to one or two connections.
                    This UDO is used in connection post placement to represent items of a given type on the bill of materials (BOM).
                
        """
        pass
    def CreateCrossSectionBuilder(self, crossSectionObject: CrossSection) -> CrossSectionBuilder:
        """
         Creates a NXOpen.Routing.CrossSectionBuilder that is used to qualify Cross Section. 
         Returns builder ( CrossSectionBuilder NXOpen): .
        """
        pass
    def CreateDefineRunBuilder(self, selectedRun: Run) -> DefineRunBuilder:
        """
         Creates a NXOpen.Routing.DefineRunBuilder  that can
                    create or edit a run.
         Returns builder ( DefineRunBuilder NXOpen): .
        """
        pass
    def CreateDeleteFontsBuilder(self, objects: List[NXOpen.NXObject]) -> DeleteFontsBuilder:
        """
         Creates a  NXOpen.Routing.DeleteFontsBuilder for deleting routing line fonts from segments.  
         Returns builder ( DeleteFontsBuilder NXOpen):  .
        """
        pass
    def CreateDeleteGapsBuilder(self, objects: List[NXOpen.NXObject]) -> DeleteGapsBuilder:
        """
         Creates a  NXOpen.Routing.DeleteGapsBuilder for deleting routing objects.  
         Returns builder ( DeleteGapsBuilder NXOpen):  .
        """
        pass
    def CreateDeleteObjectsBuilder(self, objects: List[NXOpen.NXObject]) -> DeleteObjectsBuilder:
        """
         Creates a  NXOpen.Routing.DeleteObjectsBuilder for deleting routing objects.  
         Returns builder ( DeleteObjectsBuilder NXOpen):  .
        """
        pass
    @overload
    def CreateDesignRuleViolationViewer(self, violations: List[NXOpen.NXObject]) -> DesignRuleViolationViewer:
        """
         Creates a NXOpen.Routing.DesignRuleViolationViewer to display the given violations
                    in the Design Rule Violation Browser just like the Browse Violations command.
                
         Returns viewer ( DesignRuleViolationViewer NXOpen):  .
        """
        pass
    @overload
    def CreateDesignRuleViolationViewer(self) -> DesignRuleViolationViewer:
        """
         Runs all the registered Design Rules just like the Interactive Check command.
                    Then creates a NXOpen.Routing.DesignRuleViolationViewer to display any violations
                    found in the Design Rule Violation Browser.
                
         Returns viewer ( DesignRuleViolationViewer NXOpen):  .
        """
        pass
    def CreateDivisionsBuilder(self, selectedPort: NXOpen.NXObject, isAbsoluteFlow: bool) -> DivisionsBuilder:
        """
         Creates a Divisions builder.  See the documentation in the
                    NXOpen.Routing.DivisionsBuilder class for a description of
                    the builder. 
         Returns builder ( DivisionsBuilder NXOpen):  .
        """
        pass
    def CreateDuctReinforcementBuilderForStock(self, ductReinforcement: NXOpen.NXObject) -> DuctReinforcementBuilder:
        """
         Creates an HVAC Duct Reinforcement Builder. See the documentation in the
                    NXOpen.Routing.DuctReinforcementBuilder class for a description of the builder. 
         Returns builder ( DuctReinforcementBuilder NXOpen): .
        """
        pass
    def CreateDuctSizeCalculatorBuilder(self, objects: List[NXOpen.NXObject]) -> DuctSizeCalculatorBuilder:
        """
         Creates a Duct size calculator builder. See the documentation in the
                NXOpen.Routing.DuctSizeCalculatorBuilder for a description of the builder 
         Returns builder ( DuctSizeCalculatorBuilder NXOpen):  .
        """
        pass
    def CreateEditBendAngleBuilder(self, bendRcp: NXOpen.NXObject) -> EditBendAngleBuilder:
        """
         Creates an Edit Bend Angle builder.  See the documentation in the
                    NXOpen.Routing.EditBendAngleBuilder class for a description of
                    the builder. 
         Returns builder ( EditBendAngleBuilder NXOpen):  .
        """
        pass
    def CreateEditCharacteristicsBuilder(self, objects: List[NXOpen.NXObject]) -> EditCharacteristicsBuilder:
        """
         Creates a NXOpen.Routing.EditCharacteristicsBuilder that edits
                    the Required and Optional NXOpen.Routing.CharacteristicList
                    (UG attribute values) of NXOpen.Routing.Stock or
                    NXOpen.Assemblies.Component. 
         Returns builder ( EditCharacteristicsBuilder NXOpen):  .
        """
        pass
    def CreateEditLineSegmentBuilder(self, line: LineSegment) -> EditLineSegmentBuilder:
        """
         Creates a  NXOpen.Routing.EditLineSegmentBuilder for editing and locking
                    the length of line segments.  
         Returns builder ( EditLineSegmentBuilder NXOpen):  .
        """
        pass
    def CreateEditPlacePartBuilder(self, partOcc: NXOpen.Assemblies.Component) -> EditPlacePartBuilder:
        """
         Creates a Routing.EditPlacePartBuilder that is used to edit the location of a previously placed
                    routing part in an assembly. 
         Returns builder ( EditPlacePartBuilder NXOpen):  .
        """
        pass
    def CreateElbowSnapSettings(self) -> ElbowSnapSettings:
        """
         Creates a snap elbow settings object, this object is only useful for
                   NXOpen.Routing.LinearPathBuilder object. 
         Returns builder ( ElbowSnapSettings NXOpen):  .
        """
        pass
    def CreateFabricationBuilder(self, objects: List[NXOpen.NXObject]) -> CreateFabricationBuilder:
        """
         Creates a NXOpen.Routing.CreateFabricationBuilder which fabricate subassembly from standard parts, path segments, stock, and other routing objects within the current routing assembly 
         Returns builder ( CreateFabricationBuilder NXOpen): .
        """
        pass
    def CreateFillerStockBuilder(self, objects: List[NXOpen.NXObject]) -> FillerStockBuilder:
        """
         Creates a NXOpen.Routing.FillerStockBuilder 
         Returns builder ( FillerStockBuilder NXOpen):  .
        """
        pass
    def CreateFindByAttributesBuilder(self) -> FindByAttributesBuilder:
        """
         Creates a NXOpen.Routing.FindByAttributesBuilder 
         Returns builder ( FindByAttributesBuilder NXOpen): .
        """
        pass
    def CreateFittingOverstockBuilder(self, overstock: FittingOverstock) -> FittingOverstockBuilder:
        """
         Creates a NXOpen.Routing.FittingOverstockBuilder that applies
                    or edits overstock on fittings.
         Returns builder ( FittingOverstockBuilder NXOpen):  .
        """
        pass
    def CreateFormboardPlacementCoordinateSystemBuilder(self, csysObject: NXOpen.CoordinateSystem) -> FormboardPlacementCoordinateSystemBuilder:
        """
         Creates a NXOpen.Routing.FormboardPlacementCoordinateSystemBuilder that is used to qualify Formboard Placements. 
         Returns builder ( FormboardPlacementCoordinateSystemBuilder NXOpen): .
        """
        pass
    def CreateGapDisplayBuilder(self) -> GapDisplayBuilder:
        """
         Creates a  NXOpen.Routing.GapDisplayBuilder for creating gaps
                    and bridges across line segments.  
         Returns builder ( GapDisplayBuilder NXOpen):  .
        """
        pass
    def CreateHandrailBuilder(self) -> HandrailBuilder:
        """
         Creates a NXOpen.Routing.HandrailBuilder object. 
         Returns builder ( HandrailBuilder NXOpen):  .
        """
        pass
    def CreateInfoObjectsBuilder(self, objects: List[NXOpen.NXObject]) -> InfoObjectsBuilder:
        """
         Creates a  NXOpen.Routing.InfoObjectsBuilder for deleting routing objects.  
         Returns builder ( InfoObjectsBuilder NXOpen):  .
        """
        pass
    def CreateInstanceNameLookupBuilder(self) -> InstanceNameLookupBuilder:
        """
         Creates a NXOpen.Routing.InstanceNameLookupBuilder which is used to look up the
                matching part to place based on the criteria defined in the INSTANCE_NAME_LOOKUP node and the ship
                identifier specified in the customer defaults. 
         Returns builder ( InstanceNameLookupBuilder NXOpen): .
        """
        pass
    def CreateLinearPathBuilder(self) -> LinearPathBuilder:
        """
         Creates a linear path builder for building a path consisting of
                    lines, arcs (bends) and elbows.  
         Returns builder ( LinearPathBuilder NXOpen):  .
        """
        pass
    def CreateLinearPathSettings(self) -> LinearPathSettings:
        """
         Creates a linear path settings object which stores preferences to
                    apply when creating linear paths using a NXOpen.Routing.LinearPathBuilder.
                    
         Returns builder ( LinearPathSettings NXOpen):  .
        """
        pass
    def CreateManualRouteBuilder(self, routeLevel: NXOpen.Routing.Electrical.ElectricalStockDevice.RouteLevel, elecStockDevice: NXOpen.Routing.Electrical.ElectricalStockDevice) -> ManualRouteBuilder:
        """
         Creates a NXOpen.Routing.ManualRouteBuilder that can create or edit stock transition.
         Returns builder ( ManualRouteBuilder NXOpen):  .
        """
        pass
    def CreateMergeStocksBuilder(self) -> MergeStocksBuilder:
        """
         Creates a NXOpen.Routing.MergeStocksBuilder for merging Routing Stocks.
                    Stocks are mergeable if they are C1 continuous and have mergeable attributes.
         Returns builder ( MergeStocksBuilder NXOpen): .
        """
        pass
    def CreateNamingPatternBuilder(self) -> NamingPatternBuilder:
        """
         Creates a NXOpen.Routing.NamingPatternBuilder that is used to create a sequence of port names 
                This class allows to specify the naming sequence for terminal ports whether alphabetical or 
                numerical or alpha-numeric pattern.
                
         Returns builder ( NamingPatternBuilder NXOpen): .
        """
        pass
    def CreateNewDownDirection(self) -> NXOpen.Direction:
        """
         Creates a new down direction object based on the direction for the part used by Routing. 
         Returns new_down_direction ( NXOpen.Direction):  .
        """
        pass
    def CreateOverstockBuilder(self, overstock: Overstock) -> OverstockBuilder:
        """
         Creates a NXOpen.Routing.OverstockBuilder that can
                    create or edit overstock.
         Returns builder ( OverstockBuilder NXOpen):  .
        """
        pass
    def CreateOverstockFacesBuilder(self) -> OverstockFacesBuilder:
        """
         Creates a NXOpen.Routing.OverstockFacesBuilder to qualify faces
                    of fittings for overstock application
         Returns builder ( OverstockFacesBuilder NXOpen):  .
        """
        pass
    def CreatePathArrangementBuilder(self) -> NXOpen.Routing.Electrical.PathArrangementBuilder:
        """
         Creates a Routing.Electrical.PathArrangementBuilder 
         Returns builder ( NXOpen.Routing.Electrical.PathArrangementBuilder): .
        """
        pass
    def CreatePathStockBuilder(self) -> PathStockBuilder:
        """
         Creates a path stock builder.  This builder can be used for assigning stock
                    to new path segments based off of the current default stock and the
                    settings in this builder. 
         Returns builder ( PathStockBuilder NXOpen):  .
        """
        pass
    def CreatePlacePartBuilder(self, nodeIdentifier: str, filteredPtbRowIndex: int, placementPos: NXOpen.Point3d, placementObj: NXOpen.TaggedObject) -> PlacePartBuilder:
        """
         Creates a NXOpen.Routing.PlacePartBuilder that is used to place
                    a routing part into an assembly. 
         Returns builder ( PlacePartBuilder NXOpen):  .
        """
        pass
    def CreatePlacePartBuilderFS(self, nodeIdentifier: str, fileSelectCharx: CharacteristicList, placementPos: NXOpen.Point3d, placementObj: NXOpen.TaggedObject, replacePartOp: bool) -> PlacePartBuilder:
        """
         Creates a NXOpen.Routing.PlacePartBuilder that is used to place
                    a routing part into an assembly. 
         Returns builder ( PlacePartBuilder NXOpen):  .
        """
        pass
    def CreatePlacePartBuilderPTS(self, ptsPart: NXOpen.TaggedObject, ptsInstance: NXOpen.TaggedObject, placementPos: NXOpen.Point3d, placementObj: NXOpen.TaggedObject) -> PlacePartBuilder:
        """
         Creates a NXOpen.Routing.PlacePartBuilder that is used to place
                    a routing part into an assembly. 
         Returns builder ( PlacePartBuilder NXOpen):  .
        """
        pass
    def CreatePlacementSolutionsBuilder(self) -> PlacementSolutionsBuilder:
        """
         Creates a placement solutions builder used to position a part that has been placed in the assembly. 
         Returns builder ( PlacementSolutionsBuilder NXOpen):  .
        """
        pass
    @overload
    def CreatePlatformCreatorBuilder(self) -> PlatformCreatorBuilder:
        """
         Creates a NXOpen.Routing.PlatformCreatorBuilder which creates accessways platform 
         Returns builder ( PlatformCreatorBuilder NXOpen):  .
        """
        pass
    @overload
    def CreatePlatformCreatorBuilder(self, platformFeature: PlatformFeature) -> PlatformCreatorBuilder:
        """
         Creates an Platform builder. See the documentation in the
                    NXOpen.Routing.PlatformCreatorBuilder class for a description of the builder. 
         Returns builder ( PlatformCreatorBuilder NXOpen): .
        """
        pass
    def CreatePortArrayListItemBuilder(self) -> PortArrayListItemBuilder:
        """
         Creates a NXOpen.Routing.PortArrayListItemBuilder 
                This class allows to specify the pattern feature, select the initial position and select the starting pattern instance for creating 
                Terminal Port arrays for circular or rectangular pattern for multiports.
                
         Returns builder ( PortArrayListItemBuilder NXOpen): .
        """
        pass
    def CreatePortArraysBuilder(self, port: Port) -> PortArraysBuilder:
        """
         Creates a NXOpen.Routing.PortArraysBuilder
                This class allows to create terminal port arrays for circular or rectangular pattern for multi-ports.
                
         Returns builder ( PortArraysBuilder NXOpen): .
        """
        pass
    def CreateQualifyPortBuilder(self, port: Port) -> QualifyPortBuilder:
        """
         Creates a NXOpen.Routing.QualifyPortBuilder that is used to create ports. 
         Returns builder ( QualifyPortBuilder NXOpen): .
        """
        pass
    def CreateQuickPathBuilder(self) -> QuickPathBuilder:
        """
         Creates a Quick Path builder.  See the documentation in the
                    NXOpen.Routing.QuickPathBuilder class for a description of
                    the builder.  
         Returns builder ( QuickPathBuilder NXOpen):  .
        """
        pass
    def CreateRemoveDiscontinuityBuilder(self, objects: List[NXOpen.NXObject]) -> RemoveDiscontinuityBuilder:
        """
         Creates a NXOpen.Routing.RemoveDiscontinuityBuilder which removes
                    selected discontinuity corners 
         Returns builder ( RemoveDiscontinuityBuilder NXOpen):  .
        """
        pass
    def CreateRouteSweptFoldBuilder(self, selectedStock: NXOpen.NXObject, editFoldObj: NXOpen.NXObject) -> RouteSweptFoldBuilder:
        """
         Creates a NXOpen.Routing.RouteSweptFoldBuilder.   
         Returns builder ( RouteSweptFoldBuilder NXOpen):  .
        """
        pass
    def CreateRouteSweptTwistBuilder(self, objects: NXOpen.NXObject) -> RouteSweptTwistBuilder:
        """
         Creates a NXOpen.Routing.RouteSweptTwistBuilder 
         Returns builder ( RouteSweptTwistBuilder NXOpen):  .
        """
        pass
    def CreateRoutingEndFormBuilder(self) -> EndFormBuilder:
        """
         Creates a NXOpen.Routing.EndFormBuilder that is used to place End Form. 
         Returns builder ( EndFormBuilder NXOpen): .
        """
        pass
    def CreateRoutingPlaceElbowsBuilder(self) -> PlaceElbowsBuilder:
        """
         Creates a NXOpen.Routing.PlaceElbowsBuilder that is used to place multiple elbows. 
         Returns builder ( PlaceElbowsBuilder NXOpen): .
        """
        pass
    def CreateRoutingPlacePartBuilder(self, partCharx: CharacteristicList, placementPos: NXOpen.Point3d, placementObj: NXOpen.TaggedObject) -> PlacePartBuilder:
        """
         Creates a NXOpen.Routing.PlacePartBuilder that is used to place
                    a routing part into an assembly. 
         Returns builder ( PlacePartBuilder NXOpen):  .
        """
        pass
    def CreateRunItem(self, referenceID: str, itemType: RunItem.Type, attributes: CharacteristicList) -> RunItem:
        """
         Creates a new NXOpen.Routing.RunItem.
                    Use Routing.RunCollection.CreateRun to create a new run with this new item.
                    Use NXOpen.Routing.Run.Edit to add this new item to an existing run. 
         Returns runItem ( RunItem NXOpen): .
        """
        pass
    def CreateSimplifyPathBuilder(self, segments: List[ISegment]) -> SimplifyPathBuilder:
        """
         Creates a  NXOpen.Routing.SimplifyPathBuilder that combines the
                    collinear segments by merging RCPs. 
         Returns builder ( SimplifyPathBuilder NXOpen):  .
        """
        pass
    def CreateSimplifyPathBuilder2(self, workOcc: NXOpen.Assemblies.Component, segments: List[ISegment]) -> SimplifyPathBuilder:
        """
         Creates a  NXOpen.Routing.SimplifyPathBuilder that combines the
                    collinear segments by merging RCPs in the Routed System Designer applications. 
         Returns builder ( SimplifyPathBuilder NXOpen):  .
        """
        pass
    def CreateSpaceReservationBuilder(self, objects: List[NXOpen.NXObject]) -> SpaceReservationBuilder:
        """
         Creates a Space Reservation builder.  See the documentation in the
                    NXOpen.Routing.SpaceReservationBuilder class for a description of
                    the builder.  
         Returns builder ( SpaceReservationBuilder NXOpen):  .
        """
        pass
    def CreateSplicePositionBuilder(self, splicePoint: NXOpen.Point) -> NXOpen.Routing.Electrical.SplicePositionBuilder:
        """
         Creates a NXOpen.Routing.Electrical.SplicePositionBuilder 
                This class allows to create or reposition the splices in NX.
                
         Returns builder ( NXOpen.Routing.Electrical.SplicePositionBuilder): .
        """
        pass
    def CreateSplinePathBuilder(self, spline: NXOpen.Curve) -> SplinePathBuilder:
        """
         Creates a NXOpen.Routing.SplinePathBuilder which creates
                    D-Cubed constrained splines. 
         Returns builder ( SplinePathBuilder NXOpen):  .
        """
        pass
    def CreateSplitDuctBuilder(self) -> SplitDuctBuilder:
        """
         Creates a Split Duct builder.  See the documentation in the
                    NXOpen.Routing.SplitDuctBuilder class for a description of
                    the builder. 
         Returns builder ( SplitDuctBuilder NXOpen):  .
        """
        pass
    def CreateStockBrowserBuilder(self) -> StockBrowserBuilder:
        """
         Creates a NXOpen.Routing.StockBrowserBuilder which finds and filters stock
         Returns builder ( StockBrowserBuilder NXOpen):  .
        """
        pass
    def CreateStockBuilder(self, objects: List[NXOpen.NXObject]) -> StockBuilder:
        """
         Creates a NXOpen.Routing.StockBuilder that can create or edit stock.
         Returns builder ( StockBuilder NXOpen):  .
        """
        pass
    def CreateStockColorBuilder(self) -> StockColorBuilder:
        """
         Creates a NXOpen.Routing.StockColorBuilder which assigns color to the face of stocks
                    having rectangular cross sections
                
         Returns builder ( StockColorBuilder NXOpen):  .
        """
        pass
    def CreateStockDataRefreshBuilder(self) -> StockDataRefreshBuilder:
        """
         Creates a NXOpen.Routing.StockDataRefreshBuilder for refreshing Routing Stock Data definitions. 
         Returns builder ( StockDataRefreshBuilder NXOpen): .
        """
        pass
    def CreateStockOffsetPointBuilder(self, point_or_rcp: NXOpen.NXObject) -> StockOffsetPointBuilder:
        """
         Creates a builder than can create or edit stock offset points.  This builder
                    can convert a normal dumb point to stock offset point as well as convert
                    a stock offset point to a normal point. 
         Returns builder ( StockOffsetPointBuilder NXOpen):  .
        """
        pass
    def CreateStockPartConverterBuilder(self) -> StockPartConverterBuilder:
        """
         Creates a NXOpen.Routing.StockPartConverterBuilder 
         Returns builder ( StockPartConverterBuilder NXOpen): .
        """
        pass
    def CreateStockStyleBuilder(self, objects: List[NXOpen.NXObject]) -> StockStyleBuilder:
        """
         Creates a NXOpen.Routing.StockStyleBuilder which assigns style to stock
         Returns builder ( StockStyleBuilder NXOpen):  .
        """
        pass
    def CreateStockTransitionBuilder(self, objects: List[NXOpen.NXObject]) -> StockTransitionBuilder:
        """
         Creates a NXOpen.Routing.StockTransitionBuilder that can create or edit stock transition.
         Returns builder ( StockTransitionBuilder NXOpen):  .
        """
        pass
    def CreateSubdivideSegmentBuilder(self, segment: NXOpen.NXObject, pickPoint: NXOpen.Point3d) -> SubdivideSegmentBuilder:
        """
         Creates a NXOpen.Routing.SubdivideSegmentBuilder that can
                    subdivide a segment into multiple segments
                
         Returns builder ( SubdivideSegmentBuilder NXOpen):  .
        """
        pass
    def CreateTransformPathBuilder(self, objs: List[NXOpen.NXObject]) -> TransformPathBuilder:
        """
         Creates a builder that can transform a path. 
         Returns builder ( TransformPathBuilder NXOpen):  .
        """
        pass
    def CreateUnifyPathBuilder(self, objects: List[NXOpen.NXObject]) -> UnifyPathBuilder:
        """
         Creates a NXOpen.Routing.UnifyPathBuilder which replaces given stocks
                    and fittings based on the new NXOpen.Routing.CharacteristicList.
                    Useful for unifying all of the stocks and components (e.g. elbows and tees) in
                    a path to the same characteristics. 
         Returns builder ( UnifyPathBuilder NXOpen):  .
        """
        pass
    def CreateWatertightFittingsBuilder(self) -> WatertightFittingsBuilder:
        """
         Creates a NXOpen.Routing.WatertightFittingsBuilder that
                    creates Watertight Fittings.
         Returns builder ( WatertightFittingsBuilder NXOpen): .
        """
        pass
    def CreateWindCatcherBuilder(self, windCatcher: WindCatcher) -> WindCatcherBuilder:
        """
         Creates an HVAC Wind Catcher builder. See the documentation in the
                    NXOpen.Routing.WindCatcherBuilder class for a description of the builder. 
         Returns builder ( WindCatcherBuilder NXOpen): .
        """
        pass
    def DeleteBundleSolids(self) -> None:
        """
                Removes the bundle solids that were imported from Capital
                
        """
        pass
    def DeletePath(self, objects: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Deletes the given Routing Control Points (RCP), segments, curves, and components.
                    Useful for deleting all of the objects along a path.
                    
                    Given a Routing Control Point (RCP):
                        
                        Log input RCP to delete.
                        If a side bend RCP, log bend segments to update.
                        If a bend corner RCP, log bend corner, bend arc and bend segment RCPs to delete.
                        
                    Given a Segment
                        
                        Log segment, associated bend corner, bend RCP and bend arc to delete.
                        
                    Given an Instances
                        
                        Delete component instances from the assembly.
                        
                    Given any other objects
                        
                        Log to delete.
                        
                    
                    NOTE: Does not delete occurrence or segments with other dependencies.
                
         Returns surviving_objects ( NXOpen.NXObject Li):  Objects from the given list of objects that survived. .
        """
        pass
    def DeselectAllObjectsInNavigators(self) -> None:
        """
         Deselects all objects in both the Component and Connection Navigators. 
        """
        pass
    def DesignateFormboardPlacementCSys(self, csys: NXOpen.CoordinateSystem) -> None:
        """
         Designates the passed in Coordinate System as a Formboard Placement Coordinate System for the part 
        """
        pass
    def DisQualifyModuleAssemblyPart(self) -> None:
        """
         Removes Qualification from module assembly part
        """
        pass
    def EraseNetlistHistory(self) -> None:
        """
         Erases the Netlist content history from the work part 
        """
        pass
    def ExportHx2ml(self, hx2ml_filename: str) -> None:
        """
         Exports all of the NX Routing electrical information from the currently open part
                    to the given file.
                    Returns an error if
                    
                        Unable to write to the file
                        There is no Routing electrical information in the part
                        There is no part file open
                    
                
        """
        pass
    def ExportJson(self, infoType: RouteManager.JsonInformation, jsonFileName: str) -> None:
        """
         Exports NX Routing electrical information related to specified input 
                    from the currently open part to the JSON file.
                 
        """
        pass
    def ExportJsonFromHarnessDevice(self, harnessDeviceTag: NXOpen.Routing.Electrical.HarnessDevice, infoType: RouteManager.JsonInformation, jsonFileName: str) -> None:
        """
         Exports NX Routing electrical information from input harness device to the JSON file.
                    If harnessDeviceTag is NULL Tag, then unused topology will exported to JSON file.
        """
        pass
    def ExportLegacyComponentFile(self, export_filename: str, exportFormatName: str) -> None:
        """
         Exports all of the NX Routing electrical information from the currently open part
                    to the given XML or legacy component file.
                    Returns an error if
                    
                        Unable to write to the file
                        There is no Routing electrical information in the part
                        There is no part file open
                    
                
        """
        pass
    def ExportLegacyHarnessFile(self, export_filename: str, exportFormatName: str) -> None:
        """
         Exports all of the NX Routing electrical information from the currently open part
                    to the given XML or legacy harness file.
                    Returns an error if
                    
                        Unable to write to the file
                        There is no Routing electrical information in the part
                        There is no part file open
                    
                
        """
        pass
    def ExportPlmxml(self, plmxml_filename: str) -> None:
        """
         Exports all of the NX Routing electrical information from the currently open part
                    to the given file.
                    Returns an error if
                    
                        Unable to write to the file
                        There is no Routing electrical information in the part
                        There is no part file open
                    
                
        """
        pass
    def ExportSpliceObjects(self, jsonFilename: str) -> None:
        """
         Exports the splice objects in part to a JSON file if customer default 'Export PLMXML Unused Topology' is turned on.
        """
        pass
    def ExportZipFile(self, zipFilename: str) -> None:
        """
         Exports NX Routing electrical information through Zip file created by PLMXML and JSON File (if generated). 
        """
        pass
    def FindRoutingControlPoint(self, guid: str) -> ControlPoint:
        """
         Returns the Routing.ControlPoint, if any, that matches the given globally unique identifier (GUID). 
         Returns controlPoints ( ControlPoint NXOpen): .
        """
        pass
    def FindRoutingObject(self, searchCriteria: RouteManager.SearchCriteria) -> RootObject:
        """
         Returns the Routing object, if any, that matches the given search criteria. 
         Returns objectFound ( RootObject NXOpen): .
        """
        pass
    def FindRoutingSegments(self, guid: str) -> List[ISegment]:
        """
         Returns the Routing.ISegments, if any, that match the given globally unique identifier (GUID). 
         Returns segments ( ISegment List[NXOp): .
        """
        pass
    def GenerateCablewaysLayoutData(self, segment: NXOpen.Curve, xform: NXOpen.Xform, width: float, height: float, gridFactor: int) -> Tuple[List[NXOpen.Point], List[NXOpen.Routing.Electrical.CableDevice]]:
        """
         Generates the cableways layout data (cable center points) using the
                    default bin-packing algorithm. 
         Returns A tuple consisting of (points, cables). 
         - points is:  NXOpen.Point Li.
         - cables is:  NXOpen.Routing.Electrical.CableDevice Li.

        """
        pass
    def GetAllBIPComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
         Returns all of the Built-in path components in the current part 
         Returns components ( NXOpen.Assemblies.Component Li): .
        """
        pass
    def GetConcurrent(self) -> List[NXOpen.NXObject]:
        """
         Gets objects logged for concurrent design rule check. 
         Returns objects ( NXOpen.NXObject Li):  .
        """
        pass
    def GetLengthTolerance(self) -> float:
        """
         Returns the default length tolerance for the current root part. 
         Returns tolerance (float):  Length tolerance value used by Routing in units
                                                        of the current root part. .
        """
        pass
    def GetReferencingRuns(self, objectValue: NXOpen.NXObject) -> List[Run]:
        """
         This function returns objects of type NXOpen.Routing.Run referring to given input object. Generally input object
                    for this function may be NXOpen.Routing.ISegment, NXOpen.Routing.Port,
                    NXOpen.Routing.ControlPoint, NXOpen.Features.Feature,  NXOpen.Body and
                    NXOpen.Assemblies.Component. It will not give error if any other input is passed. In that case
                    output array will be empty.
                
         Returns runs ( Run List[NXOp):  .
        """
        pass
    def GetSelectedObjectsInNavigators(self) -> List[RootObject]:
        """
         Returns all of the objects selected in the Component and Connection Navigators. 
         Returns selectedObjects ( RootObject List[NXOp): .
        """
        pass
    def GetStockFromBody(self, body: NXOpen.Body) -> Stock:
        """
         Returns the Routing.Stock, if any, that was used to create the given solid body. 
         Returns stock ( Stock NXOpen): .
        """
        pass
    def HasAllReferencingStockComponentsLoaded(self, objectToValidate: NXOpen.TaggedObject) -> bool:
        """
         Checks whether all the stock components referenced by the given Routing object are loaded or not.
         Returns areAllStockComponentsLoaded (bool):  Are all the referencing stock components loaded or not. .
        """
        pass
    def HighLightPathandBundleSolids(self, controlPoint1: ControlPoint, controlPoint2: ControlPoint, bundleId: str) -> None:
        """
                Highlights the path and bundle solids between Routing Control Points for specified bundle.
                
        """
        pass
    def ImportFromCapital(self) -> None:
        """
         
                Imports the data from the context diagram selected in the Capital navigator into the given part when Connect to Capital is enabled in Customer Defaults.
                
        """
        pass
    def ImportHx2ml(self, hx2ml_filename: str, import_operation: RouteManager.ImportMode) -> None:
        """
         Imports NX Routing electrical information from the given HX2ML file
                    into the current work part.
                    Returns an error if
                    
                        Unable to read the file
                        There is no part file open
                        An import mode other than Upate or derivative is used.
                    
                
        """
        pass
    def ImportLegacyComponentFile(self, import_filename: str, import_operation: RouteManager.ImportMode, import_format_name: str) -> None:
        """
         Imports NX Routing electrical information from the given
                    XML or legacy component file into the current work part.
                    Returns an error if
                    
                        Unable to read the file
                        There is no part file open
                    
                
        """
        pass
    def ImportLegacyHarnessFile(self, import_filename: str, import_operation: RouteManager.ImportMode, import_format_name: str) -> None:
        """
         Imports NX Routing electrical information from the given
                    XML or legacy harness file into the current work part.
                    Returns an error if
                    
                        Unable to read the file
                        There is no part file open
                    
                
        """
        pass
    def ImportPartListFormatFile(self, file_name: str) -> NXOpen.Part:
        """
         Loads the part list format (template) file. Part list is based on this
                    format and using this Bill of Material (BOM) is generated. 
         Returns part ( NXOpen.Part):  Template part. .
        """
        pass
    def ImportPlmxml(self, plmxml_filename: str, import_operation: RouteManager.ImportMode) -> None:
        """
         Imports NX Routing electrical information from the given PLM XML file
                    into the current work part.
                    Returns an error if
                    
                        Unable to read the file
                        There is no part file open
                    
                
        """
        pass
    def ImportRunsManaged(self, itemPartNumber: str, itemRevision: str) -> None:
        """
         Builds runs from all XML files defined on the provided Item Revision from Teamcenter. 
        """
        pass
    def ImportRunsNative(self, path: str) -> None:
        """
         Builds runs from all XML files contained in the provided folder path. 
        """
        pass
    def ImportZipFile(self, zipFilename: str, importOperation: RouteManager.ImportMode) -> None:
        """
         Imports the Routing electrical information from Zip file.
                    Zip file must contain plmxml file. JSON file is optional. No other file should be present in Zip file.
        """
        pass
    def InsertIntoStock(self, component: NXOpen.Assemblies.Component) -> None:
        """
         Connects the input component to the stocks and other components in the work part.
                    
                        Subdivides segments intersected by ports of the part
                        and marked interior if the segment is "inside" of the part.  Segments are considered
                        inside if all of the end NXOpen.Routing.ControlPoint objects of the
                        segments are inside the bounding box of the component.  Interior segments are
                        not displayable.
                    
                    
                        All stocks are split at the new interior segments.  The interior stocks are
                        hidden and do not show up in the bill of materials.
                    
                    
                        In addition this routine adds fixture ports of the input component to fixed
                        length splines that are intersected by the ports.
                    
                 
        """
        pass
    def IntegrateRunsBuilder(self, first_run: Run, second_run: Run) -> IntegrateRunsBuilder:
        """
        Creates a NXOpen.Routing.IntegrateRunsBuilder  that can
                    Integrate two runs.
         Returns builder ( IntegrateRunsBuilder NXOpen):  .
        """
        pass
    def IsComponentNavigatorOpen(self) -> bool:
        """
         Is the Component Navigator open? 
         Returns isOpen (bool): .
        """
        pass
    def IsConnectionNavigatorOpen(self) -> bool:
        """
         Is the Connection Navigator open? 
         Returns isOpen (bool): .
        """
        pass
    def IsDirectIntegrationwithCapitalEnabled(self) -> bool:
        """
         
                If Connect to Capital customer default is turned on, return true else return false.
                
         Returns isConnected (bool): .
        """
        pass
    def IsRoutingPart(self) -> bool:
        """
         Checks if the given part is a Routing part  
         Returns isRoutingPart (bool): .
        """
        pass
    def IsStockComponent(self, inputComponent: NXOpen.Assemblies.Component) -> bool:
        """
         Identifies if input component is Stock as Component or not.
                    This method returns truefalse
                    true  = The input component is Stock as Component
                    false = The input component Fitting Component.
         Returns isStockComponent (bool): .
        """
        pass
    def LiftFromStock(self, component: NXOpen.Assemblies.Component) -> None:
        """
         Disconnects the input component from stocks and components in the work part.
                    
                        This the opposite of NXOpen.Routing.RouteManager.InsertIntoStock.
                        Interior segments are marked as non-interior, and any subdivisions performed by
                        NXOpen.Routing.RouteManager.InsertIntoStock are reversed to
                        the previous state.
                    
                    
                        Interior stocks are marked as non-interior and merge with the existing stocks
                        that were connected to the component.
                    
                 
        """
        pass
    def LoadPart(self, part_entry: CharacteristicList) -> NXOpen.Part:
        """
         Loads a part based on the input NXOpen.Routing.CharacteristicList.
                    This object can be created on the fly, or returned from a search through the part library using
                   the Preferences.RoutingPartLibrary.MatchCriteria or
                   Preferences.RoutingPartLibrary.MatchCriteriaWithFilter methods.
                  
         Returns part ( NXOpen.Part):  .
        """
        pass
    def LogConcurrent(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Logs objects to be checked during the next concurrent design rule check. 
        """
        pass
    def MergeDuplicateRcps(self, tolerance: float, rcps: List[ControlPoint]) -> bool:
        """
         Finds the duplicate Routing Control Points (RCPs) within given tolerance and
                    merges them. Call NXOpen.Update.DoUpdate afterwards to ensure that
                    the duplicates are deleted.
         Returns merge (bool):  If RCPs are merged returns TRUE else FALSE .
        """
        pass
    def ModelConnectionPostPlacementGasket(self, placedPart: NXOpen.Assemblies.Component, connection: PortConnection, reportInBOM: ReuseLibrary.ReportInBom, gasketCharx: CharacteristicList) -> Tuple[PortConnection, PortConnection]:
        """
         Places a gasket part based on the gasketCharx NXOpen.Routing.CharacteristicList .
                    The gasket is returned from a search through the reuse part library.
                
         Returns A tuple consisting of (connectionOne, connectionTwo). 
         - connectionOne is:  PortConnection NXOpen. One of the new gasket flange connections .
         - connectionTwo is:  PortConnection NXOpen. The other new gasket flange connection .

        """
        pass
    def ModelConnectionPostPlacementGasketBetweenFlanges(self, placedPart: NXOpen.Assemblies.Component, connection: PortConnection, reportInBOM: ReuseLibrary.ReportInBom, gasketCharx: CharacteristicList) -> Tuple[PortConnection, PortConnection, NXOpen.Assemblies.Component]:
        """
         Places a gasket part based on the gasketCharx NXOpen.Routing.CharacteristicList .
                    The gasket is returned from a search through the reuse part library.
                    This overload allows the caller to recover the modeled gasket.
                
         Returns A tuple consisting of (connectionOne, connectionTwo, modeledGasket). 
         - connectionOne is:  PortConnection NXOpen. One of the new gasket flange connections .
         - connectionTwo is:  PortConnection NXOpen. The other new gasket flange connection .
         - modeledGasket is:  NXOpen.Assemblies.Component. The gasket created .

        """
        pass
    def ModelConnectionPostPlacementWeldGap(self, placedPart: NXOpen.Assemblies.Component, connection: PortConnection, gapValue: float) -> None:
        """
         Places a weld gap by adding a weld gap characteristic to one of the part occurrences connected.
                
        """
        pass
    def ModelTerminalsBuilder(self) -> ModelTerminalsBuilder:
        """
         Creates a NXOpen.Routing.ModelTerminalsBuilder which Models Terminal
         Returns builder ( ModelTerminalsBuilder NXOpen):  .
        """
        pass
    def OpenComponentNavigator(self) -> None:
        """
         Opens the Component Navigator. 
        """
        pass
    def OpenConnectionNavigator(self) -> None:
        """
         Opens the Connection Navigator. 
        """
        pass
    def PlaceCutElbow(self, load_charx: CharacteristicList, apply_charx: CharacteristicList, rcp: ControlPoint) -> None:
        """
         Places a cut elbow at the given Routing Control Point (RCP). 
        """
        pass
    def PlacePostPlacementParts(self, placedPart: NXOpen.Assemblies.Component, postPartCharx: CharacteristicList) -> List[NXOpen.Assemblies.Component]:
        """
         Places post placement parts based on the postPartCharxNXOpen.Routing.CharacteristicList on the placedPart object.
                    The postPartCharx object can be created on the fly, or returned from a search through the part library using
                    the Preferences.RoutingPartLibrary.MatchCriteria or
                    Preferences.RoutingPartLibrary.MatchCriteriaWithFilter methods.
                    The postPartCharx should be empty to search for post placement part using post placement rules
                    of current specification. The first part from the search will be used for post placement if the
                    search based on post placement rules returns more than one part.
                  
         Returns postParts ( NXOpen.Assemblies.Component Li):  .
        """
        pass
    def PromoteBIPGeometry(self, bipComponent: NXOpen.Assemblies.Component) -> None:
        """
         Finds all Built-In Path components which do not have referencing built-in path updaters and creates them.
                    This may also involve creating the workpart geometry for the Built-in path if needed. 
        """
        pass
    def QualifyModuleAssemblyPart(self) -> None:
        """
         Qualifies a module assembly part
        """
        pass
    def RecreateStockComponents(self) -> str:
        """
         Regenerates the stock components in the assembly. This command will fully load the assembly and if any stock components
                    are found to be missing, it will recreate those components. Since parts can get opened and deleted it invokes
                    full update to restore sanity of the model. 
         Returns msg (str): .
        """
        pass
    def RemoveComponents(self, components: List[NXOpen.Assemblies.Component]) -> None:
        """
         Removes the NXOpen.Assemblies.Component objects from the assembly
                    and updates the routing path data. 
        """
        pass
    def RemoveFormboardPlacementCSysDesignation(self) -> None:
        """
         Removes the designation of any Formboard Placement Coordinate System for the part 
        """
        pass
    def RemoveIdentifierFromNonRoutingParts(self) -> None:
        """
         Removes routing identifier if the given part is a non-routing part. 
        """
        pass
    @overload
    def ReplaceComponents(self, old_occ: NXOpen.Assemblies.Component, new_occ: NXOpen.Assemblies.Component, refset_name: str) -> None:
        """
         Replaces old component with new component, and relinks ports if possible. Copies the characteristics on the old component
                    onto the new component. 
        """
        pass
    @overload
    def ReplaceComponents(self, old_occ: NXOpen.Assemblies.Component, new_occ: NXOpen.Assemblies.Component, refset_name: str, fixPosition: RouteManager.FixPosition) -> None:
        """
         Replaces old component with new component, and relinks ports if possible. Copies the characteristics on the old component
                    onto the new component. The parameter fixPosition can allow a fix constraint to be applied to the new component
                    in order to prevent it from moving during the replace component operation. 
        """
        pass
    def RepositionPartOccurrence(self, part_occ: NXOpen.Assemblies.Component, position: NXOpen.Point3d, transform: NXOpen.Matrix3x3) -> None:
        """
         Repositions part component given position and transformation 
        """
        pass
    def RouteReplacePart(self, old_occ: NXOpen.Assemblies.Component, new_part: NXOpen.Part, comp_name: str, refset: str, occ_layer: int) -> NXOpen.Assemblies.Component:
        """
         Replace part 
         Returns new_instance ( NXOpen.Assemblies.Component):   .
        """
        pass
    def SelectObjectInNavigator(self, objectToSelect: RootObject) -> None:
        """
         Highlights the given object in the Component or Connection Navigator.
                    Once selected, all the other connected devices highlight, too. For example,
                    selecting an assigned connector highlights the connector in the Component Navigator,
                    the assemblies component if one is assigned, the connections that use it, etc.
                    Selecting a connection highlights the connectors it uses and the path it takes, if routed.
                    Throws an error if the Routing Electrical application or the navigator is
                    not initialized. To initialize the navigators, you simply have to open them
                    once.
                
        """
        pass
    def SelectObjectsInNavigator(self, objectsToSelect: List[RootObject]) -> None:
        """
         Highlights the given objects in the Component or Connection Navigator.
                    Once selected, all the other connected devices highlight, too. For example,
                    selecting an assigned connector highlights the connector in the Component Navigator,
                    the assemblies component if one is assigned, the connections that use it, etc.
                    Selecting a connection highlights the connectors it uses and the path it takes, if routed.
                    Throws an error if the Routing Electrical application or the navigator is
                    not initialized. To initialize the navigators, you simply have to open them
                    once.
                
        """
        pass
    def SplitRunBuilder(self, run: Run) -> SplitRunBuilder:
        """
         Creates a NXOpen.Routing.SplitRunBuilder  that can
                    split a run.
         Returns builder ( SplitRunBuilder NXOpen):  .
        """
        pass
    def TerminalPortBuilder(self) -> TerminalPortBuilder:
        """
         Creates a NXOpen.Routing.TerminalPortBuilder 
         Returns builder ( TerminalPortBuilder NXOpen):  .
        """
        pass
    def TransformObjects(self, all_stock: bool, specified_stocks: List[Stock], objects: List[NXOpen.NXObject], position: NXOpen.Point3d, transform: NXOpen.Matrix3x3, copy_operation: bool) -> List[NXOpen.NXObject]:
        """
         Transforms routing objects. The transformation can be a Move or a Copy.
                     objects should not be passed for transformation.  
         Returns copy_objects ( NXOpen.NXObject Li):  Objects surviving the operation (the
                                                                                        copied objects for a copy, the moved objects
                                                                                        for a move). Can contain  entries .
        """
        pass
    def UnifyPath(self, input_object: NXOpen.TaggedObject, new_charx_list: CharacteristicList) -> None:
        """
         Changes the given stock or component to a new object that matches the given characteristics.
                    Useful for unifying all of the stocks and components (e.g. elbows and tees) in
                    a path to the same characteristics.
                
        """
        pass
    def UnlinkContextDiagram(self) -> None:
        """
         
                Unlinks the work part from any previously selected context diagram in Capital.
                
        """
        pass
    def ViewNetlistHistory(self) -> None:
        """
         Prints the Netlist content history to the Listing Window 
        """
        pass
import NXOpen
class RouteObjectCollectorList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[RouteObjectCollector]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: RouteObjectCollector) -> None:
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
    def Erase(self, obj: RouteObjectCollector) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: RouteObjectCollector, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: RouteObjectCollector) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> RouteObjectCollector:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( RouteObjectCollector NXOpen):  object found at input index .
        """
        pass
    def GetContents(self) -> List[RouteObjectCollector]:
        """
         Gets the contents of the entire list 
         Returns objects ( RouteObjectCollector List[NXOp):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: RouteObjectCollector) -> None:
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
    def SetContents(self, objects: List[RouteObjectCollector]) -> None:
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
    def Swap(self, object1: RouteObjectCollector, object2: RouteObjectCollector) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class RouteObjectCollector(NXOpen.TaggedObject): 
    """ Represents a NXOpen.Routing.RouteObjectCollector class
        to create objects for getting routing objects.
    """
    @property
    def RoutingObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) RoutingObjects
         Returns the selected routing object list   
            
         
        """
        pass
class RouteObject(RootObject): 
    """ 
            The Top level routing data model object.
        
        
        Provides each routing data model object with a unique identifier. 
        See NX Open Routing help for detailed information on the Connection data model.
        
     """
    pass
import NXOpen
class RoutePartDescriptorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.RoutePartDescriptor objects. """
    def CreatePartDescriptor(self, descriptor_source_type: RoutePartDescriptor.SourceType, descriptor_charx_type: RoutePartDescriptor.CharxType, title: str, expression: str) -> RoutePartDescriptor:
        """
         Creates a NXOpen.Routing.RoutePartDescriptor object. 
         Returns descriptor ( RoutePartDescriptor NXOpen):  .
        """
        pass
    def CreatePartDescriptorWithUnit(self, descriptor_source_type: RoutePartDescriptor.SourceType, descriptor_charx_type: RoutePartDescriptor.CharxType, title: str, expression: str, unit: str, locked: bool) -> RoutePartDescriptor:
        """
         Overload which Creates a NXOpen.Routing.RoutePartDescriptor object. 
         Returns descriptor ( RoutePartDescriptor NXOpen): .
        """
        pass
import NXOpen
class RoutePartDescriptor(NXOpen.TaggedObject): 
    """ Represents a part descriptor chrx. """
    class CharxType(Enum):
        """
        Members Include: 
         |Int|   
         |Real|   
         |Sting|   
         |Any|   
         |Ref|   
         |AnyRef|   

        """
        Int: int
        Real: int
        Sting: int
        Any: int
        Ref: int
        AnyRef: int
        @staticmethod
        def ValueOf(value: int) -> RoutePartDescriptor.CharxType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SourceType(Enum):
        """
        Members Include: 
         |Null|   
         |PartAttribute|   
         |Expression|   
         |DumbCopy|   

        """
        Null: int
        PartAttribute: int
        Expression: int
        DumbCopy: int
        @staticmethod
        def ValueOf(value: int) -> RoutePartDescriptor.SourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DescriptorCharxType(self) -> RoutePartDescriptor.CharxType:
        """
        Getter for property: ( RoutePartDescriptor.CharxType NXOpen) DescriptorCharxType
         Returns the charx type for the part descriptor used by Routing.  
             
         
        """
        pass
    @DescriptorCharxType.setter
    def DescriptorCharxType(self, type: RoutePartDescriptor.CharxType):
        """
        Setter for property: ( RoutePartDescriptor.CharxType NXOpen) DescriptorCharxType
         Returns the charx type for the part descriptor used by Routing.  
             
         
        """
        pass
    @property
    def DescriptorSourceType(self) -> RoutePartDescriptor.SourceType:
        """
        Getter for property: ( RoutePartDescriptor.SourceType NXOpen) DescriptorSourceType
         Returns the descriptor type for the part descriptor used by Routing.  
             
         
        """
        pass
    @DescriptorSourceType.setter
    def DescriptorSourceType(self, type: RoutePartDescriptor.SourceType):
        """
        Setter for property: ( RoutePartDescriptor.SourceType NXOpen) DescriptorSourceType
         Returns the descriptor type for the part descriptor used by Routing.  
             
         
        """
        pass
    @property
    def Expression(self) -> str:
        """
        Getter for property: (str) Expression
         Returns the expression for the part descriptor used by Routing.  
             
         
        """
        pass
    @Expression.setter
    def Expression(self, expression: str):
        """
        Setter for property: (str) Expression
         Returns the expression for the part descriptor used by Routing.  
             
         
        """
        pass
    @property
    def Locked(self) -> bool:
        """
        Getter for property: (bool) Locked
         Returns the accessor for islocked variable   
            
         
        """
        pass
    @Locked.setter
    def Locked(self, locked: bool):
        """
        Setter for property: (bool) Locked
         Returns the accessor for islocked variable   
            
         
        """
        pass
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the title for the part descriptor used by Routing.  
             
         
        """
        pass
    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
         Returns the title for the part descriptor used by Routing.  
             
         
        """
        pass
    @property
    def Unit(self) -> str:
        """
        Getter for property: (str) Unit
         Returns the unit for the part descriptor used by Routing.  
             
         
        """
        pass
    @Unit.setter
    def Unit(self, unit: str):
        """
        Setter for property: (str) Unit
         Returns the unit for the part descriptor used by Routing.  
             
         
        """
        pass
import NXOpen
class RouteSegmentFontElement(NXOpen.NXObject): 
    """ Represents a route segment font element. """
    pass
import NXOpen
class RouteSegmentFont(NXOpen.NXObject): 
    """ Represents a route segment font. """
    @property
    def Segment(self) -> NXOpen.Line:
        """
        Getter for property: ( NXOpen.Line) Segment
         Returns   
            
         
        """
        pass
    @Segment.setter
    def Segment(self, segTag: NXOpen.Line):
        """
        Setter for property: ( NXOpen.Line) Segment
         Returns   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class RouteSweptFoldBuilder(NXOpen.Builder): 
    """ Represents a Rout Swept Fold Builder """
    @property
    def BendAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendAngle
         Returns the bend angle   
            
         
        """
        pass
    @property
    def BendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BendRadius
         Returns the bend radius   
            
         
        """
        pass
    @property
    def FoldLocation(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) FoldLocation
         Returns the fold location   
            
         
        """
        pass
    @property
    def FoldRotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FoldRotationAngle
         Returns the fold rotation angle   
            
         
        """
        pass
    @property
    def FoldStartRotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FoldStartRotationAngle
         Returns the fold start rotation angle   
            
         
        """
        pass
    @property
    def LengthAdjustment(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LengthAdjustment
         Returns the length adjustment   
            
         
        """
        pass
    @property
    def ReverseBendAngle(self) -> bool:
        """
        Getter for property: (bool) ReverseBendAngle
         Returns the reverse bend angle   
            
         
        """
        pass
    @ReverseBendAngle.setter
    def ReverseBendAngle(self, reverseBendAngle: bool):
        """
        Setter for property: (bool) ReverseBendAngle
         Returns the reverse bend angle   
            
         
        """
        pass
    @property
    def ReverseFixedSegment(self) -> bool:
        """
        Getter for property: (bool) ReverseFixedSegment
         Returns the reverse fixed segment   
            
         
        """
        pass
    @ReverseFixedSegment.setter
    def ReverseFixedSegment(self, reverseFixedSegment: bool):
        """
        Setter for property: (bool) ReverseFixedSegment
         Returns the reverse fixed segment   
            
         
        """
        pass
    @property
    def ReverseFoldRotationAngle(self) -> bool:
        """
        Getter for property: (bool) ReverseFoldRotationAngle
         Returns the reverse fold rotation angle   
            
         
        """
        pass
    @ReverseFoldRotationAngle.setter
    def ReverseFoldRotationAngle(self, reverseFoldRotationAngle: bool):
        """
        Setter for property: (bool) ReverseFoldRotationAngle
         Returns the reverse fold rotation angle   
            
         
        """
        pass
    @property
    def Spline(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) Spline
         Returns the spline stored in the builder.  
             
         
        """
        pass
    @property
    def StockSelection(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) StockSelection
         Returns the stock selection.  
           This will be the solid body  
         
        """
        pass
    def SetStock(self, stock: Stock) -> None:
        """
         Sets the value of stock, stock width and stock thickness to the builder. This will set the stock only if it has rectangular cross section. 
                    After setting the stock it will create and set the spline for the builder. It will also set the spline curves for the builder
                    if the stock has more than one segments. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class RouteSweptTwistBuilder(NXOpen.Builder): 
    """ """
    @property
    def Spine(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) Spine
         Returns the spine   
            
         
        """
        pass
    @property
    def Stock(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Stock
         Returns the stock   
            
         
        """
        pass
    @property
    def TwistPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TwistPoint
         Returns the twist point   
            
         
        """
        pass
    @TwistPoint.setter
    def TwistPoint(self, twistPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TwistPoint
         Returns the twist point   
            
         
        """
        pass
    @property
    def TwistPointList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) TwistPointList
         Returns the twist point list   
            
         
        """
        pass
    def AskExistingTwistData(self) -> Tuple[List[float], List[float]]:
        """
         The twist data i.e locations and angles 
         Returns A tuple consisting of (locations, angles). 
         - locations is: List[float]. Number of locations .
         - angles is: List[float]. Number of angles .

        """
        pass
    def CreateSpine(self) -> None:
        """
         Creates a new spine 
        """
        pass
    def CreateSpinePoint(self) -> NXOpen.GeometricUtilities.OnPathDimWithValueBuilder:
        """
         Creates a new spine point 
         Returns dimWithValueBuilder ( NXOpen.GeometricUtilities.OnPathDimWithValueBuilder):  OnPathDimWithValueBuilder Object .
        """
        pass
class RoutingAttributeIdentifierType(Enum):
    """
    Members Include: 
     |String|  A simple string identifier 
     |Classification|  An identifier for a Teamcenter classification attribute 

    """
    String: int
    Classification: int
    @staticmethod
    def ValueOf(value: int) -> RoutingAttributeIdentifierType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class RoutingBulkReplacementBuilderLibrarySelectSourceType(Enum):
    """
    Members Include: 
     |Unspecified|  Library select source is not specified 
     |Classification|  Library select source is a classification object 
     |SpecificPart|  Library select source is a specific part 

    """
    Unspecified: int
    Classification: int
    SpecificPart: int
    @staticmethod
    def ValueOf(value: int) -> RoutingBulkReplacementBuilderLibrarySelectSourceType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class RoutingBulkReplacementBuilderReplacementMethodType(Enum):
    """
    Members Include: 
     |AttributeValues|  Search for a replacement object using attribute values 
     |LibrarySelect|  Select a replacement object from the part library 
     |Retain|  Keep the original object, no replacement is performed 
     |NotSet|  Replacement method not set yet 

    """
    AttributeValues: int
    LibrarySelect: int
    Retain: int
    NotSet: int
    @staticmethod
    def ValueOf(value: int) -> RoutingBulkReplacementBuilderReplacementMethodType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class RoutingBulkReplacementBuilderRetainReasonType(Enum):
    """
    Members Include: 
     |Unspecified|  Retain reason is not specified  
     |Explicit|  Retain reason is the user explicitly marked it retain 
     |BlockUnify|  Retain reason is because of the presence of the NX_BLOCK_UNIFY attribute 
     |NonClassification|  Retain reason is the object did not originate from classification and is not supported 
     |Equipment|  Retain reason is the object is equipment and is not supported 
     |NonPartLibrary|  Retain reason is the object did not originate from the Routing part library and is not supported 
     |ReferenceStock|  Retain reason is the object is reference stock 
     |UnloadedConnectedComponents|  Retain reason is the object is connected to unloaded components 
     |SpaceReservationNotSupported|  Retain reason is the object is a space reservation which is not supported yet 
     |PtsPartNotSupported|  Retain reason is the object is a PTS part which is not supported 
     |FtsStockNotSupported|  Retain reason is the object is a FTS stock which is not supported 
     |ConnectedToDerivedObject|  Retain reason is the object is connected to a derived object or component which is not supported 
     |NonLibraryTemplatePartNotSupoorted|  Retain reason is the object is template part which doesnt have library representation 
     |ModuleAssembly|  Retain reason is the object is a Module Assembly which is not supported 
     |PtsPartWithWaveLinksNotSupported|  Retain reason is the object is a PTS part having wave links which is not supported 
     |FtsStockConnectedWithWaveLinksNotSupported|  Retain reason is the object is a FTS stock connected with wave links which is not supported 
     |PatternComponent|  Retain reason is the object is a Pattern component which is not supported 
     |FlexPart|  Retain reason is that the partOcc contains flex definition 

    """
    Unspecified: int
    Explicit: int
    BlockUnify: int
    NonClassification: int
    Equipment: int
    NonPartLibrary: int
    ReferenceStock: int
    UnloadedConnectedComponents: int
    SpaceReservationNotSupported: int
    PtsPartNotSupported: int
    FtsStockNotSupported: int
    ConnectedToDerivedObject: int
    NonLibraryTemplatePartNotSupoorted: int
    ModuleAssembly: int
    PtsPartWithWaveLinksNotSupported: int
    FtsStockConnectedWithWaveLinksNotSupported: int
    PatternComponent: int
    FlexPart: int
    @staticmethod
    def ValueOf(value: int) -> RoutingBulkReplacementBuilderRetainReasonType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class RoutingMeasureDistanceBuilder(NXOpen.MeasureDistanceBuilder): 
    """ Represents a NXOpen.Routing.RoutingMeasureDistanceBuilder """
    @property
    def RoutingSelection(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RoutingSelection
         Returns the  NXOpen::Routing::RouteObjectCollector    
            
         
        """
        pass
    @RoutingSelection.setter
    def RoutingSelection(self, selectionBuilder: RouteObjectCollector):
        """
        Setter for property: ( RouteObjectCollector NXOpen) RoutingSelection
         Returns the  NXOpen::Routing::RouteObjectCollector    
            
         
        """
        pass
    def GetRoutingObjects(self) -> List[NXOpen.NXObject]:
        """
         The routing objects used for path length 
         Returns routingObjects ( NXOpen.NXObject Li):  the routing objects used for path length .
        """
        pass
    def SetRoutingObjects(self, routingObjects: List[NXOpen.NXObject]) -> None:
        """
         The routing objects used for path length 
        """
        pass
import NXOpen
class RoutingSystemCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.RoutingSystem objects. """
    def CreateRouting(self, name: str) -> RoutingSystem:
        """
         Creates a NXOpen.Routing.RoutingSystem object. 
         Returns routing ( RoutingSystem NXOpen):  .
        """
        pass
import NXOpen
class RoutingSystem(NXOpen.NXObject): 
    """ Routing object is a collection of NXOpen.Routing.Run objects. """
    def AddRuns(self, runs: List[Run]) -> None:
        """
         Adds NXOpen.Routing.Run objects to a RoutingSystem 
        """
        pass
    def GetId(self) -> str:
        """
         Returns name of routing. 
         Returns name (str):  Name of given routing .
        """
        pass
    def GetRuns(self) -> List[Run]:
        """
         Retrieves all NXOpen.Routing.Run objects in RoutingSystem 
         Returns runs ( Run List[NXOp):  Runs belonging to the RoutingSytem .
        """
        pass
    def RemoveRuns(self, runs: List[Run]) -> None:
        """
         Removes NXOpen.Routing.Run objects from a RoutingSystem. Only removes
                    Run from the RoutingSystem, does not remove the Run definition 
        """
        pass
    def SetId(self, name: str) -> None:
        """
         Sets name of routing. 
        """
        pass
import NXOpen
class RunCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Run objects. """
    @overload
    def CreateRun(self, run_id: str, run_type: str, fromValue: List[NXOpen.NXObject], to: List[NXOpen.NXObject], member: List[NXOpen.NXObject]) -> Run:
        """
         Creates a fully defined NXOpen.Routing.Run object whose "From" item(s),
                    "To" item(s), and "Member" item(s) are assigned to components in the assembly. 
         Returns run ( Run NXOpen):  .
        """
        pass
    @overload
    def CreateRun(self, run_id: str, run_type: str, attributes: CharacteristicList, from_items: List[RunItem], to_items: List[RunItem], member_items: List[RunItem]) -> Run:
        """
         Creates a NXOpen.Routing.Run with items that are not assigned to components in the assembly. 
         Returns run ( Run NXOpen):  .
        """
        pass
    @overload
    def CreateRun(self, run_id: str, run_type: str, attributes: CharacteristicList) -> Run:
        """
         Creates an empty NXOpen.Routing.Run using just a unique Run identifier and a type. 
         Returns run ( Run NXOpen):  .
        """
        pass
    def FindPath(self, source: List[NXOpen.NXObject], target: List[NXOpen.NXObject]) -> List[NXOpen.NXObject]:
        """
         Find a run path connecting all input From items to the To items. 
         Returns members ( NXOpen.NXObject Li):  Array of member items. Must be NXOpen.Assemblies.Component,
                                                        NXOpen.Routing.ISegment or Routing.Stock .
        """
        pass
import NXOpen
class RunItemsBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[RunItemsBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: RunItemsBuilder) -> None:
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
    def Erase(self, obj: RunItemsBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: RunItemsBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: RunItemsBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> RunItemsBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( RunItemsBuilder NXOpen):  object found at input index .
        """
        pass
    def GetContents(self) -> List[RunItemsBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( RunItemsBuilder List[NXOp):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: RunItemsBuilder) -> None:
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
    def SetContents(self, objects: List[RunItemsBuilder]) -> None:
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
    def Swap(self, object1: RunItemsBuilder, object2: RunItemsBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class RunItemsBuilder(NXOpen.Builder): 
    """ The builder for creating the list item of RunItems """
    @property
    def CurrentSelectedPort(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) CurrentSelectedPort
         Returns the ports of FROMTO item of the run.  
             
         
        """
        pass
    @CurrentSelectedPort.setter
    def CurrentSelectedPort(self, selectedPort: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) CurrentSelectedPort
         Returns the ports of FROMTO item of the run.  
             
         
        """
        pass
    @property
    def RunItems(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) RunItems
         Returns the list item of run FromTo item   
            
         
        """
        pass
    @property
    def VirtualReferenceId(self) -> str:
        """
        Getter for property: (str) VirtualReferenceId
         Returns the virtual reference Id for FROMTO items of a run.  
             
         
        """
        pass
    @VirtualReferenceId.setter
    def VirtualReferenceId(self, virtualRefIdFrom: str):
        """
        Setter for property: (str) VirtualReferenceId
         Returns the virtual reference Id for FROMTO items of a run.  
             
         
        """
        pass
    def GetVirtualStubItem(self, virtualReferenceId: str) -> NXOpen.TaggedObject:
        """
         A virtual stub item to be used as FromTo item. 
         Returns virtualStubItem ( NXOpen.TaggedObject): .
        """
        pass
    def SetSelectedItemData(self, scopedObject: NXOpen.TaggedObject, referenceId: str, portName: str, availablePorts: List[NXOpen.TaggedObject]) -> None:
        """
         The selected items data of the run 
        """
        pass
import NXOpen
class RunItem(NXOpen.TransientObject): 
    """ Routing Run Item object references components which comprise a piping run. """
    class Type(Enum):
        """
        Members Include: 
         |From|  A "From" item type.  
         |To|  A "To" item type     
         |Member|  A "Member" item type 

        """
        From: int
        To: int
        Member: int
        @staticmethod
        def ValueOf(value: int) -> RunItem.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Attributes(self) -> CharacteristicList:
        """
        Getter for property: ( CharacteristicList NXOpen) Attributes
         Returns the attributes on the Run Item.  
             
         
        """
        pass
    @Attributes.setter
    def Attributes(self, attributes: CharacteristicList):
        """
        Setter for property: ( CharacteristicList NXOpen) Attributes
         Returns the attributes on the Run Item.  
             
         
        """
        pass
    @property
    def ItemType(self) -> RunItem.Type:
        """
        Getter for property: ( RunItem.Type NXOpen) ItemType
         Returns the Run Item type such as "From", "To", or "Member" item.  
             
         
        """
        pass
    @ItemType.setter
    def ItemType(self, itemType: RunItem.Type):
        """
        Setter for property: ( RunItem.Type NXOpen) ItemType
         Returns the Run Item type such as "From", "To", or "Member" item.  
             
         
        """
        pass
    @property
    def ReferenceId(self) -> str:
        """
        Getter for property: (str) ReferenceId
         Returns the unique reference identifier for this Run Item.  
             
         
        """
        pass
    @ReferenceId.setter
    def ReferenceId(self, reference_id: str):
        """
        Setter for property: (str) ReferenceId
         Returns the unique reference identifier for this Run Item.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Free resources associated with this instance of Run Item class.
                After calling this method, it is illegal to use the object.  In .NET,
                this method is automatically called when the object is deleted by the
                garbage collector. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class Run(NXOpen.NXObject): 
    """ Routing Run object references components and stocks which comprise a piping run. """
    class CompareStatus(Enum):
        """
        Members Include: 
         |NotSet|  Run has no compare status. Compare operation is not invoked yet 
         |Ok|  No missing, extra or discrepancy items 
         |MissingRun|  Entire run is missing 
         |ExtraRun|  Entire run is extra 
         |MissingItem|  Item or items are missing from the run 
         |ExtraItem|  Extra item or items present in the run 
         |Discrepancy|  Items have characteristics discrepancies 

        """
        NotSet: int
        Ok: int
        MissingRun: int
        ExtraRun: int
        MissingItem: int
        ExtraItem: int
        Discrepancy: int
        @staticmethod
        def ValueOf(value: int) -> Run.CompareStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlipStatus(Enum):
        """
        Members Include: 
         |Success|  Component is flipped. 
         |NotTwoPorts|  Given component ports are not equal to two ports.  
         |UnequalConstraints|  Each ports has different number of constraints. 
         |PortPositionMismatch|  Ports are not collinear and opposite or perpendicular. 
         |FlowTypeMismatch|  Ports are defined with ambiguous flow types. 
         |FollowsFlow|  Ports correctly aligned with flow. No flipping done. 
         |RunFlowNotDefined|  Flow is not defined on Run. Component can't be flipped. 
         |CannotFlip|  Run is deleted or there are no segments attached to component. Component cannot be flipped. 

        """
        Success: int
        NotTwoPorts: int
        UnequalConstraints: int
        PortPositionMismatch: int
        FlowTypeMismatch: int
        FollowsFlow: int
        RunFlowNotDefined: int
        CannotFlip: int
        @staticmethod
        def ValueOf(value: int) -> Run.FlipStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Status(Enum):
        """
        Members Include: 
         |Valid|  Run is valid. All items are connected and all segments have
                                                        stocks assigned on them 
         |Broken|  Run is broken. All items are not connected end to end 
         |Incomplete|  Run is incomplete. Some segments do not have stock assigned on them

        """
        Valid: int
        Broken: int
        Incomplete: int
        @staticmethod
        def ValueOf(value: int) -> Run.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def DeleteRunPath(self) -> None:
        """
         This will delete the Run path and member items in a run 
        """
        pass
    def DetectRunSpools(self) -> List[NXOpen.ObjectList]:
        """
         This will detect spools in a run 
         Returns sets ( NXOpen.ObjectList Li):  .
        """
        pass
    @overload
    def Edit(self, run_id: str, run_type: str, fromValue: List[NXOpen.NXObject], to: List[NXOpen.NXObject], member: List[NXOpen.NXObject]) -> Run.Status:
        """
         Edits an existing run with new items. NOTE: Removes any existing items in the run and adds these new items 
         Returns status ( Run.Status NXOpen):  Valid, broken or incomplete run .
        """
        pass
    @overload
    def Edit(self, run_id: str, run_type: str, from_items: List[RunItem], to_items: List[RunItem], member_items: List[RunItem]) -> None:
        """
         Edits an existing run with new run item data. NOTE: Removes any existing items in the run and adds these new items. 
        """
        pass
    def FlipComponent(self, component: NXOpen.Assemblies.Component) -> Run.FlipStatus:
        """
         Flips a component that is part of a run by rotating the component so that it's input and output ports reverse. 
         Returns flipStatus ( Run.FlipStatus NXOpen):  Flip Component status .
        """
        pass
    def GetActiveStatus(self) -> bool:
        """
         Get status of Run, Active or Inactive 
         Returns isActive (bool):   .
        """
        pass
    def GetCharacteristics(self) -> CharacteristicList:
        """
         Get all of the characteristics values on the this object. 
         Returns values ( CharacteristicList NXOpen):  .
        """
        pass
    def GetCharacteristicsWithId(self) -> CharacteristicList:
        """
         Get all of the characteristics values on the this object, including RunId. 
         Returns values ( CharacteristicList NXOpen):  .
        """
        pass
    def GetFromItemData(self) -> List[RunItem]:
        """
         Retrieves the data of the "From" items of a run 
         Returns from_items ( RunItem List[NXOp):  Array of data for the "From" items. .
        """
        pass
    def GetFromItems(self) -> List[NXOpen.NXObject]:
        """
         Retrieves the from items of a run. From items are extracted ports or run 
         Returns items ( NXOpen.NXObject Li):  All from items of the run .
        """
        pass
    def GetMemberItemData(self) -> List[RunItem]:
        """
         Retrieves the data of the "Member" items of a run 
         Returns member_items ( RunItem List[NXOp):  Array of data for the "Member" items. .
        """
        pass
    def GetMembers(self) -> List[NXOpen.NXObject]:
        """
         Retrieves the member items of a run. Member items are part occurrence of ports, stocks,
                    or segments. 
         Returns items ( NXOpen.NXObject Li):  All member items of the run .
        """
        pass
    def GetRoutingSystem(self) -> RoutingSystem:
        """
         Ask the NXOpen.Routing.RoutingSystem run belongs to 
         Returns routing ( RoutingSystem NXOpen):  RoutingSystem run belongs to .
        """
        pass
    def GetRunCompareStatus(self) -> Run.CompareStatus:
        """
         Ask the compare status of run 
         Returns status ( Run.CompareStatus NXOpen):  Run compare status .
        """
        pass
    def GetRunId(self) -> str:
        """
         Retrieves the run_id of run 
         Returns run_id (str):  Run id of run .
        """
        pass
    def GetRunStatus(self) -> Run.Status:
        """
         Ask the status of run 
         Returns status ( Run.Status NXOpen):  Valid, broken or incomplete run .
        """
        pass
    def GetRunType(self) -> str:
        """
         Retrieves the run type of run 
         Returns run_type (str):  Run type of run .
        """
        pass
    def GetToItemData(self) -> List[RunItem]:
        """
         Retrieves the data of the "To" items of a run 
         Returns to_items ( RunItem List[NXOp):  Array of data for the "To" items. .
        """
        pass
    def GetToItems(self) -> List[NXOpen.NXObject]:
        """
         Retrieves the to items of a run. To items are extracted ports or run
         Returns items ( NXOpen.NXObject Li):  All to items of the run .
        """
        pass
    def MakeActive(self) -> None:
        """
         Set a Run as Active. All the newly created segments and parts through Linear Path, Spline Path,
                    Heal Path and parts placed through Place Part will be added as members to the Active Run.
                    The specification of the Run will be set as Active Specification.
                    The previous active run will be made Inactive. Use NXOpen.Routing.Run.MakeInactive to make a Run as Inactive.
        """
        pass
    def MakeInactive(self) -> None:
        """
         Set a Run as Inactive and the Active Specification will be changed to Default Specification of the
                    discipline, if no discipline is being used then the Active Specification will be set to None.
                    Use NXOpen.Routing.Run.MakeActive to make a Run as Active. 
        """
        pass
    def RunSegmentGetFlowDirection(self, segment: ISegment) -> int:
        """
         Get flow direction of a run segment 
         Returns flow_state (int): .
        """
        pass
    def RunSegmentReverseFlowDirection(self, segment: ISegment) -> None:
        """
         Reverse flow direction of a run segment 
        """
        pass
    def RunSegmentSetFlowDirection(self, segment: ISegment, flow_state: int) -> None:
        """
         Set flow direction of a run segment 
        """
        pass
    def SetCharacteristics(self, values: CharacteristicList) -> None:
        """
         Set all of the characteristics values on this object. 
        """
        pass
import NXOpen
class SBendCornerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.SBendCorner objects. """
    def ComputeSBend(self, start_pnt: NXOpen.Point3d, end_pnt: NXOpen.Point3d, line_vec1: NXOpen.Vector3d, line_vec2: NXOpen.Vector3d, radius: float, sbend_type: int) -> Tuple[bool, NXOpen.Spline]:
        """
         Compute a S-Bend curve given input.  
         Returns A tuple consisting of (is_sbend, bend_curve). 
         - is_sbend is: bool. TURE: if S-Bend is possible;  
                                                               FALSE: otherwise. .
         - bend_curve is:  NXOpen.Spline. S-Bend spline when a valid solution exists;  
                                                                otherwise. .

        """
        pass
    def ComputeSBendData(self, start_pnt: NXOpen.Point3d, end_pnt: NXOpen.Point3d, line_vec1: NXOpen.Vector3d, line_vec2: NXOpen.Vector3d, radius: float, sbend_type: int) -> Tuple[bool, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d, NXOpen.Point3d]:
        """
         Compute a S-Bend parameters given input. 
         Returns A tuple consisting of (is_sbend, extension_pt1, extension_pt2, arc1_start_pt, arc1_end_pt, arc2_start_pt, arc2_end_pt). 
         - is_sbend is: bool. TURE: if S-Bend is possible;  
                                                           FALSE: otherwise. .
         - extension_pt1 is:  NXOpen.Point3d. Location of 1st extension point where
                                                           bend fillets could be assigned. Value is
                                                           not valid when no S-Bend is possible.
         - extension_pt2 is:  NXOpen.Point3d. Location of 2nd extension point where
                                                           bend fillets could be assigned.
         - arc1_start_pt is:  NXOpen.Point3d. Point where the first bend arc starts. 
                                                           Only computed if not . .
         - arc1_end_pt is:  NXOpen.Point3d. Point where the first bend arc ends. 
                                                           Only computed if not . .
         - arc2_start_pt is:  NXOpen.Point3d. Point where the second bend arc starts. 
                                                                       Only computed if not . .
         - arc2_end_pt is:  NXOpen.Point3d. Point where the second bend arc ends. 
                                                           Only computed if not . .

        """
        pass
    def CreateCornerByBendRadius(self, start_rcp: ControlPoint, end_rcp: ControlPoint, bend_radius: float, sbend_type: int) -> SBendCorner:
        """
         Creates a S-Bend corner between the start rcp and end rcp using a 
                    bend radius. 
         Returns sbend ( SBendCorner NXOpen):  The newly created S-Bend Corner .
        """
        pass
    def CreateCornerByBendRatio(self, start_rcp: ControlPoint, end_rcp: ControlPoint, bend_ratio: float, sbend_type: int) -> SBendCorner:
        """
         Creates a S-Bend corner between the start rcp and end rcp using a 
                    bend ratio. 
         Returns sbend ( SBendCorner NXOpen):  The newly created S-Bend Corner .
        """
        pass
    def CreateCornerBySegBendRadius(self, start_rcp: ControlPoint, end_rcp: ControlPoint, segment: SplineSegment, sbend_type: int, bend_radius: float) -> SBendCorner:
        """
         Creates a S-Bend corner between the start rcp and end rcp using a 
                    NXOpen.Routing.SplineSegment and a bend radius. 
         Returns sbend ( SBendCorner NXOpen):  The newly created S-Bend corner object. .
        """
        pass
    def CreateCornerBySegBendRatio(self, start_rcp: ControlPoint, end_rcp: ControlPoint, segment: SplineSegment, sbend_type: int, bend_ratio: float) -> SBendCorner:
        """
         Creates a S-Bend corner between the start rcp and end rcp using a 
                    NXOpen.Routing.SplineSegment and a bend ratio. 
         Returns sbend ( SBendCorner NXOpen):  The newly created S-Bend corner object. .
        """
        pass
    def EditCornerByBendRadius(self, start_rcp: ControlPoint, end_rcp: ControlPoint, bend_radius: float, sbend_type: int, sbend: SBendCorner) -> None:
        """
         Edits a selected S-Bend corner between the start rcp and end rcp using a 
                    bend radius. 
        """
        pass
    def EditCornerByBendRatio(self, start_rcp: ControlPoint, end_rcp: ControlPoint, bend_ratio: float, sbend_type: int, sbend: SBendCorner) -> None:
        """
         Edits a S-Bend corner between the start rcp and end rcp using a 
                    bend ratio. 
        """
        pass
    def GetRcpSBendRadius(self, rcp: ControlPoint) -> float:
        """
         Gets the S-Bend radius of a rcp associated S-Bend corner. 
         Returns bend_radius (float):  The bend radius.
        """
        pass
    def GetSBendAssociatedToRcp(self, rcp: ControlPoint) -> List[SBendCorner]:
        """
         Given a control point, get S-Bend corners pointing to it 
         Returns sbends ( SBendCorner List[NXOp):  Corner objects pointing to the rcp. .
        """
        pass
    def GetSBendAssociatedToSegment(self, segment: SplineSegment) -> SBendCorner:
        """
         Enquire the S-Bend Corner that this segment represents.
                     ( can be returned, indicating that this segment does not
                     represent a S-Bend Corner.) 
         Returns corner ( SBendCorner NXOpen):  S-Bend Corner that segment represents 
                                                           ( can be returned,indicating that 
                                                           segment does not represent a S-Bend Corner). .
        """
        pass
    def GetSegmentSBendRadius(self, segment: SplineSegment) -> float:
        """
         Gets the bend radius of a segment associated S-Bend corner. 
         Returns bend_radius (float):  The bend radius. .
        """
        pass
    def IsRcpAssociatedToSBend(self, rcp: ControlPoint) -> bool:
        """
         Determines if the rcp is associated to an S-Bend corner. 
         Returns is_sbend_rcp (bool):  true - The control point is a rcp for
                                                                   a S-Bend corner.
                                                           false - Otherwise .
        """
        pass
import NXOpen
class SBendCorner(NXOpen.NXObject): 
    """ 
    The Routing SBendCorner defines a S-Bend. There are 5 possible S-bend types. 

The UI input is two work part line segment-ending RCPs, each of which
implicitly provides a 3D point and vector.  An S-bend heals the
separation between the two segments with a C1 continuous spline segment.


To disambiguate among 5 S-bend types (see below), the user may need to
further indicate whether the S-bend starts bending immediately at the
end of one or both of the 2 input segments.  Some arrangements of 2
segments do not require further user input to disambiguate among the
possible S-bend types.


The direction vectors of the 2 input segments must either be 
perpendicular (types 1,2,3) or parallel (types 4,5).


The closest distance between the (infinite) lines containing the input
segments must be less that twice the bend radius.  If this condition
does not hold, then 2 right angle bends could connect the 2 input
segments, i.e., an S-bend is unnecessary.


Every S-bend has two bends, whose radii are always equal.  Except for
type 2 and 3, the bend angles are equal and in the range
[ Pi4, Pi2 ].


S-bends never cause a cutback of an input segment, although type 1,2,4
S-bends may add a straight line extension to one of the segment ends
before the bending starts.  Type 1 S-bends may add a straight line
extension to both segment ends.


INPUT
 
     R bend radius, which the user supplies, e.g., from a bend table.
     P1 Work part X,Y,Z of segment 1's end.
     Vec1 Tangent at P1, pointing toward the open end of the segment.
     P2, Vec2 Similar to segment 1 above...
  


    For computation solving purposes, the above input becomes a bend
    radius, height, width, and possibly a depth.


 OUTPUT bend angle(s):
 
 a (alpha)   (all S-bend types)
 g (gamma)   (Type 3 only)
 Extension lengths, if any.



Bend angles are computed at the centers of the bend arcs


S-bends fall into two categories:



    End tangents are perpendicular.

        Three types are possible.  In the 3D diagrams below:
        

            The constructor line, AB, is the perpendicular distance
            between the lines that the segments define.
            
                Height (H):  length of A-B
                Depth  (D):  length of A-P1
                Width  (W):  length of B-P2
            
            The A-B, A-P1, B-P2 vectors are mutually perpendicular.
        
        Features.SewBuilder.Type 1:  does not have a middle straight line portion.
        
        
                                   
                                  seg1
                           P1  
                             
                           
                         
                       
                     
                    
                   :
             A     :
              |     :
              |      ,
              |       ,  ---- bends meet (no straight segment)
              |        :
              |         :
              |          `-,
              |             ``-,_
              +------------------`-------------
             B                      P2   seg2
             

            The bend from segment 2 lies in the plane A,B,P2.  The bend
            from segment 1 is always 90 degrees, and thus terminates
            somewhere in the plane A,B,P2.  The bend from segment 1 always
            starts on an extension of segment 1 that is a distance R from
            A.

            Segment 2 may also have to extend toward B before its bend
            starts.

            Geometrically, the height is the sum of the vertical
            components of bend 1 and bend 2.
            

        Type 2:  middle straight line portion
        
                                   
                                  seg1
                           P1  
                             
                           
                         
                       
                     
                    
                   :
             A     :
              |     :
              |      \
              |       \ ---- straight segment
              |        \
              |         \ ----- bend ends
              |          `-,
              |             ``-,_
              +------------------`-------------
             B                      P2   seg2
        
            Similar to Type 1:
           The bend from segment 2 lies in the plane A,B,P2.

                 The bend from segment 1 is always 90 degrees, and thus
                terminates somewhere in the plane A,B,P2.

                 The bend from segment 1 always starts on an extension of
                segment 1 that is a distance R from A.

             Unlike Type 1:
                 Segment 2's bend always starts at P2, i.e., segment 2
                never has an extension.
                
                
        Type 3:  middle straight line portion.  user chooses between Type 2-3.
        
                                   
                                  seg1
                           P1  
                             
                           
                          '
                         '
                        : ---- segment 1's bend ends
                        |
                        |
             A          |
              |          | --- straight segment
              |          |
              |          |
              |          |
              |          |
              |           \ ---- segment 2's bend ends
              |            `-,_
              +----------------`-------------
             B                    P2   seg2

             The bend radius isn't big enough to span the height so a
            middle straight line segment is necessary.

             Neither segment can have an extension, i.e., the bends start
            at P1 and P2.  Unlike in Type 2, segment 2's bend does not lie
            in the plane A,B,P2, i.e., both bends immediately start
            bending toward each other.
            
        
        

         End tangents are parallel, i.e., bend lies entirely within a
        plane.  This category falls into two types.
        
        
        Type 4:  no middle straight line portion
        
              seg1       P1
            -------------.
                           `.
                             :  --- where bends meet
                              `,
                               `------------------
                       A          E2        P2   seg2

             The height, H, is length (A-P1), where A is the projection of
            P1 onto the line that seg2 defines.

             Because both bend angles are the same, the bends meet at half
            the height H2.
        
        
        Type 5:  middle straight line portion
        
              seg1       P1
            -------------.
                           `.
                             \
                              \ --- middle straight line segment
                               \
                                `.
                                 `-------------
                       A          P2      seg2

             The height, H, is length (A-P1), where A is the projection of
            P1 onto the line that seg2 defines.  The width, W, is the A-P2
            length.
          
          
          
          

     Support Information: 
    ===============================
     
      o  An extension as described above is the distance leading up to the 
         bend arc. 
    
     """
    def GetSBendData(self) -> Tuple[bool, int, ControlPoint, ControlPoint, SplineSegment, float]:
        """
         Returns the data for the S-Bend object 
         Returns A tuple consisting of (use_bend_ratio, sbend_type, start_rcp, end_rcp, segment, radius_or_ratio). 
         - use_bend_ratio is: bool. TRUE:  if bend ratio is used;
                                                                 FALSE: otherwise. .
         - sbend_type is: int. S-Bend type .
         - start_rcp is:  ControlPoint NXOpen. S-Bend start Control point .
         - end_rcp is:  ControlPoint NXOpen. S-Bend end Control point .
         - segment is:  SplineSegment NXOpen. S-Bend segment.
         - radius_or_ratio is: float. Bend radius or bend_ratio. .

        """
        pass
    def GetSBendRadius(self) -> float:
        """
         Gets the S-Bend radius of a S-Bend corner. 
         Returns bend_radius (float):  .
        """
        pass
    def GetSBendStocks(self) -> List[Stock]:
        """
         Returns an array of stocks for the S-Bend object 
         Returns stock ( Stock List[NXOp):  Stock objects of the S-Bend corner. .
        """
        pass
    def GetSegment(self) -> SplineSegment:
        """
         Gets the segment being used to represent the S-Bend. 
         Returns segment ( SplineSegment NXOpen):  .
        """
        pass
    def SetSBendData(self, sbend_type: int, start_rcp: ControlPoint, end_rcp: ControlPoint, segment: SplineSegment, radius_or_ratio: float, use_bend_ratio: bool) -> None:
        """
         Set the data for the S-Bend object 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class SegmentManager(NXOpen.Object): 
    """ Contains the type of the routing part as well as the Collection objects for creatingiterating
        over routing objects.
    """
    class SubdivideSpacing(Enum):
        """
        Members Include: 
         |ScreenPoint|  Screen Point 
         |EqualArcLength|  Equal Arc Length 
         |EqualParameter|  Equal Parameter 
         |IncrementalArcLength|  Incremental Arc Length 
         |GeometricRatio|  Geometric Progression Ratio 
         |ChordalTolerance|  Chordal Tolerance 
         |NumberOfOptions|  Number of Options 

        """
        ScreenPoint: int
        EqualArcLength: int
        EqualParameter: int
        IncrementalArcLength: int
        GeometricRatio: int
        ChordalTolerance: int
        NumberOfOptions: int
        @staticmethod
        def ValueOf(value: int) -> SegmentManager.SubdivideSpacing:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SubdivideOption:
        """
         Contains subdivide segment method information.  This structure is used by
                     NXOpen::Routing::SegmentManager::Subdivide . 
         SegmentManagerSubdivideOption_Struct NXOpen is an alias for  SegmentManager.SubdivideOption NXOpen.
        """
        @property
        def SpacingOption(self) -> SegmentManager.SubdivideSpacing:
            """
            Getter for property SpacingOption
            Spacing Option

            """
            pass
        @SpacingOption.setter
        def SpacingOption(self, value: SegmentManager.SubdivideSpacing):
            """
            Getter for property SpacingOption
            Spacing Option
            Setter for property SpacingOption
            Spacing Option

            """
            pass
        @property
        def StartPercent(self) -> float:
            """
            Getter for property StartPercent
            Start Percentage; 0 \
            """
            pass
        @StartPercent.setter
        def StartPercent(self, value: float):
            """
            Getter for property StartPercent
            Start Percentage; 0 \
            """
            pass
        @property
        def EndPercent(self) -> float:
            """
            Getter for property EndPercent
            End Percentage; start_percent \
            """
            pass
        @EndPercent.setter
        def EndPercent(self, value: float):
            """
            Getter for property EndPercent
            End Percentage; start_percent \
            """
            pass
        @property
        def ScreenPointPercentage(self) -> float:
            """
            Getter for property ScreenPointPercentage
            Screen Point Percentage

            """
            pass
        @ScreenPointPercentage.setter
        def ScreenPointPercentage(self, value: float):
            """
            Getter for property ScreenPointPercentage
            Screen Point Percentage
            Setter for property ScreenPointPercentage
            Screen Point Percentage

            """
            pass
        @property
        def Direction(self) -> int:
            """
            Getter for property Direction
            Direction; If direction = 1, normal curve direction                                                                             else if direction = -1, reverse the sense of curve direction

            """
            pass
        @Direction.setter
        def Direction(self, value: int):
            """
            Getter for property Direction
            Direction; If direction = 1, normal curve direction                                                                             else if direction = -1, reverse the sense of curve direction
            Setter for property Direction
            Direction; If direction = 1, normal curve direction                                                                             else if direction = -1, reverse the sense of curve direction

            """
            pass
        @property
        def NumberOfSegments(self) -> int:
            """
            Getter for property NumberOfSegments
            Number of Segments

            """
            pass
        @NumberOfSegments.setter
        def NumberOfSegments(self, value: int):
            """
            Getter for property NumberOfSegments
            Number of Segments
            Setter for property NumberOfSegments
            Number of Segments

            """
            pass
        @property
        def GeometricRatio(self) -> float:
            """
            Getter for property GeometricRatio
            Geometric Progression Ratio

            """
            pass
        @GeometricRatio.setter
        def GeometricRatio(self, value: float):
            """
            Getter for property GeometricRatio
            Geometric Progression Ratio
            Setter for property GeometricRatio
            Geometric Progression Ratio

            """
            pass
        @property
        def IncrementalArcLength(self) -> float:
            """
            Getter for property IncrementalArcLength
            Incremental Arc Length

            """
            pass
        @IncrementalArcLength.setter
        def IncrementalArcLength(self, value: float):
            """
            Getter for property IncrementalArcLength
            Incremental Arc Length
            Setter for property IncrementalArcLength
            Incremental Arc Length

            """
            pass
        @property
        def ChordalTolerance(self) -> float:
            """
            Getter for property ChordalTolerance
            Chordal Tolerance

            """
            pass
        @ChordalTolerance.setter
        def ChordalTolerance(self, value: float):
            """
            Getter for property ChordalTolerance
            Chordal Tolerance
            Setter for property ChordalTolerance
            Chordal Tolerance

            """
            pass
        @property
        def Dcm3CreateTangency(self) -> bool:
            """
            Getter for property Dcm3CreateTangency
            Create Tangency at subdivision point when subdividing splines

            """
            pass
        @Dcm3CreateTangency.setter
        def Dcm3CreateTangency(self, value: bool):
            """
            Getter for property Dcm3CreateTangency
            Create Tangency at subdivision point when subdividing splines
            Setter for property Dcm3CreateTangency
            Create Tangency at subdivision point when subdividing splines

            """
            pass
        @property
        def Dcm3AddPoints(self) -> bool:
            """
            Getter for property Dcm3AddPoints
            Add Points to subdivided splines to maintain shape

            """
            pass
        @Dcm3AddPoints.setter
        def Dcm3AddPoints(self, value: bool):
            """
            Getter for property Dcm3AddPoints
            Add Points to subdivided splines to maintain shape
            Setter for property Dcm3AddPoints
            Add Points to subdivided splines to maintain shape

            """
            pass
        @property
        def Dcm3AddFixConstraint(self) -> bool:
            """
            Getter for property Dcm3AddFixConstraint
            """
            pass
        @Dcm3AddFixConstraint.setter
        def Dcm3AddFixConstraint(self, value: bool):
            """
            Getter for property Dcm3AddFixConstraintSetter for property Dcm3AddFixConstraint
            """
            pass
    @property
    def Segments() -> ISegmentCollection:
        """
         All Segment types collection 
        """
        pass
    @property
    def LineSegments() -> LineSegmentCollection:
        """
         Line Segment collection 
        """
        pass
    @property
    def ArcSegments() -> ArcSegmentCollection:
        """
         Arc Segment collection 
        """
        pass
    @property
    def SplineSegments() -> SplineSegmentCollection:
        """
         Spline Segment collection 
        """
        pass
    def AreSegmentsTangent(self, segment1: ISegment, segment2: ISegment, controlPoint: ControlPoint) -> bool:
        """
         Tests whether two segments are tangent to one another where they both are connected at
                    the given Control Point. 
         Returns areSegmentsTangent (bool):  Are the two segments tangent? .
        """
        pass
    def CreateConstrainedSegment(self, start_rcp: ControlPoint, end_rcp: ControlPoint) -> ISegment:
        """
         Creates a constrained line NXOpen.Routing.ISegment object
                     with input NXOpen.Routing.ControlPoint as ends.
                     Only use this method when building segments in a part that
                     use NXOpen.Positioning.Constraint objects to constraint components
                     and geometry.  This is a new method for creating segments in NX5 and
                     should be used instead of NXOpen.Routing.SegmentManager.CreateSegment
                     for all line segments.
                    
         Returns new_segment ( ISegment NXOpen):  Created segment .
        """
        pass
    def CreateHealPath(self) -> HealPath:
        """
         Creates a new empty NXOpen.Routing.HealPath object that can be
                    used as an input to NXOpen.Routing.SegmentManager.CreateHealSpline.
                 
         Returns heal_path ( HealPath NXOpen):  .
        """
        pass
    def CreateHealSpline(self, start_object: NXOpen.DisplayableObject, end_object: NXOpen.DisplayableObject, heal_path: HealPath) -> ISegment:
        """
         Creates a spline NXOpen.Routing.ISegment object
                    with input NXOpen.Routing.ControlPoint as ends.
                    
         Returns new_segment ( ISegment NXOpen):  Created segment .
        """
        pass
    @overload
    def CreateSegment(self, follow_curve: NXOpen.Curve, start_rcp: ControlPoint, end_rcp: ControlPoint, user_defined: UserDefined) -> ISegment:
        """
         Creates a NXOpen.Routing.ISegment object following a curve. 
         Returns new_segment ( ISegment NXOpen):  Created segment .
        """
        pass
    @overload
    def CreateSegment(self, start_rcp: ControlPoint, end_rcp: ControlPoint) -> ISegment:
        """
         Creates a line NXOpen.Routing.ISegment object with input
                    NXOpen.Routing.ControlPoint as ends. 
         Returns new_segment ( ISegment NXOpen):  Created segment .
        """
        pass
    @overload
    def CreateSplineData(self, splineSegment: ISegment) -> SplineData:
        """
          Creates a NXOpen.Routing.SplineData object. 
                 This class provides the ability to query and edit Routing Spline Segments. 
                 The NXOpen.Routing.SplineData provides access to an array of
                       NXOpen.Routing.DefiningPoint objects which identify the
                       positions and optional directions and forwardbackward magnitudes for extensions.  
         Returns splineData ( SplineData NXOpen):  a new NXOpen.Routing.SplineData object .
        """
        pass
    @overload
    def CreateSplineData(self, positions: List[NXOpen.Point3d]) -> SplineData:
        """
          Create a new NXOpen.Routing.SplineData object. 
                 This class provides the ability to create, query and edit Routing Spline Segments from an array of positions. 
                 The NXOpen.Routing.SplineData provides access to an array of
                       NXOpen.Routing.DefiningPoint objects which identify the
                       positions and optional directions and forwardbackward magnitudes for extensions.  
         Returns splineData ( SplineData NXOpen):  a new NXOpen.Routing.SplineData object .
        """
        pass
    def GetShortestPathBetweenControlPoints(self, controlPoint1: ControlPoint, controlPoint2: ControlPoint) -> List[ISegment]:
        """
         Returns the shortest connected segments (i.e. the path) linking the two NXOpen.Routing.ControlPoints, if any. 
         Returns segments ( ISegment List[NXOp):  .
        """
        pass
    def ModelTerminals(self, multi_port: Port, cut_back_length: float, extension_string: str, override_charx: bool, terminal_ports: List[Port]) -> None:
        """
         Models spline paths to to specified terminals. Updates connection list to reflect
                    changes to wire lengths of referencing connections. 
        """
        pass
    def ProcessBuiltInPaths(self, part_occ: NXOpen.Assemblies.Component) -> None:
        """
         Create segments of NXOpen.Routing.BuiltInPath objects present in this
                    NXOpen.Assemblies.Component object. 
        """
        pass
    def SetFollowCurve(self, segment: ISegment, follow_curve: NXOpen.Curve) -> ISegment:
        """
         Set segment follow curve.  Segment can change type to mirror the type of the follow curve being set. 
         Returns modified_segment ( ISegment NXOpen):  Segment can possibly change types.
                                                            Use the returned segment object pointer instead
                                                            of any older pointers after calling this function.
                                                            For example: A LineSegment can become a SplineSegment after
                                                            calling this function if new follow curve is a spline. .
        """
        pass
    def SimplifySegments(self, segments: List[ISegment], do_update: bool) -> List[ISegment]:
        """
         Combine segments that are collinear and whose intermediate RCPs do not branch 
         Returns new_segments ( ISegment List[NXOp):  resulting segments .
        """
        pass
    def Subdivide(self, segment: ISegment, subdivide_option: SegmentManager.SubdivideOption) -> List[ISegment]:
        """
         Subdivide a routing path segment 
         Returns subdivide_segments ( ISegment List[NXOp):  resulting segments .
        """
        pass
    def UnmodelTerminals(self, multi_port: Port, terminal_ports: List[Port]) -> None:
        """
         Un-model terminals and update connection list routes for specified terminal ports. 
        """
        pass
import NXOpen
class SegmentPairBuilder(NXOpen.Builder): 
    """ The builder for creating the list item of SegmentPairs """
    @property
    def PairSegment(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) PairSegment
         Returns the list item of Segment Pairs   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectControlPoint(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[ControlPoint, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  ControlPoint NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, ControlPoint, NXOpen.View, NXOpen.Point3d, ControlPoint, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  ControlPoint NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  ControlPoint NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[ControlPoint, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  ControlPoint NXOpen. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: ControlPoint, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: ControlPoint, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: ControlPoint, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: ControlPoint, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectISegment(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> ISegment:
        """
        Getter for property: ( ISegment NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: ISegment):
        """
        Setter for property: ( ISegment NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[ISegment, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  ISegment NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, ISegment, NXOpen.View, NXOpen.Point3d, ISegment, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  ISegment NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  ISegment NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[ISegment, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  ISegment NXOpen. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: ISegment, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: ISegment, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: ISegment, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: ISegment, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectLineSegment(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> LineSegment:
        """
        Getter for property: ( LineSegment NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: LineSegment):
        """
        Setter for property: ( LineSegment NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[LineSegment, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  LineSegment NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, LineSegment, NXOpen.View, NXOpen.Point3d, LineSegment, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  LineSegment NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  LineSegment NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[LineSegment, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  LineSegment NXOpen. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: LineSegment, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: LineSegment, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: LineSegment, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: LineSegment, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectPortList(NXOpen.TaggedObject): 
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
    def Add(self, objectValue: Port) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[Port], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[Port]) -> bool:
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
    def Add(self, selection: Port, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Port, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Port, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: Port, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
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
    def Contains(self, objectValue: Port) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[Port]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( Port List[NXOp):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: Port) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[Port]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: Port, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Port, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Port, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def SetArray(self, objects: List[Port]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectPort(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Port:
        """
        Getter for property: ( Port NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Port):
        """
        Setter for property: ( Port NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Port, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Port NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Port, NXOpen.View, NXOpen.Point3d, Port, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Port NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Port NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[Port, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  Port NXOpen. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: Port, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Port, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Port, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: Port, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectRun(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Run:
        """
        Getter for property: ( Run NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Run):
        """
        Setter for property: ( Run NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Run, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Run NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Run, NXOpen.View, NXOpen.Point3d, Run, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Run NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Run NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[Run, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  Run NXOpen. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: Run, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Run, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Run, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: Run, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectStock(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Stock:
        """
        Getter for property: ( Stock NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Stock):
        """
        Setter for property: ( Stock NXOpen) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Stock, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Stock NXOpen. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Stock, NXOpen.View, NXOpen.Point3d, Stock, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Stock NXOpen. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Stock NXOpen. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[Stock, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  Stock NXOpen. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: Stock, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Stock, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Stock, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: Stock, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
class SimplifyPathBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Routing.SimplifyPathBuilder for Simplify Path operation.
    Merges collinear segments (with no follow curves) together.  Also merges segments that 
    share a follow curve.
    """
    @property
    def SegmentCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SegmentCollector
         Returns the routing object collector that collects the segments to simplify.  
            
         
        """
        pass
import NXOpen
class SingleDevice(RouteObject): 
    """
        The Routing SingleDevice corresponds to an abstract instance of NXOpen.Routing.ItemDefinition.
    """
    class DeleteObjectResult(Enum):
        """
        Members Include: 
         |Ok|  Single Device deleted successfully. 
         |StillRouted|  Routed connections will not be deleted.
                                                                                 Unroute before deleting. 
         |StillAssigned|  Assigned components will not be deleted.
                                                                                   Unassign before deleting. 
         |CantDeleteUnknown|  Unknown error occurred while deleting.
                                                                                       Please report this as an Incident Report. 

        """
        Ok: int
        StillRouted: int
        StillAssigned: int
        CantDeleteUnknown: int
        @staticmethod
        def ValueOf(value: int) -> SingleDevice.DeleteObjectResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def NxEquivalent(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) NxEquivalent
         Returns the NX equivalent object.  
           
                    The NX Equivalent of a  Routing::Electrical::ConnectorDevice  is an  Assemblies::Component .
                    The NX Equivalent of a  Routing::Electrical::ElectricalStockDevice  is a  Routing::Wire .
                    The NX Equivalent of a  Routing::Electrical::HarnessDevice  is also a  Routing::Wire .
                    The NX Equivalent of a  Routing::StockDevice  is a  Routing::Stock .
                  
         
        """
        pass
    @NxEquivalent.setter
    def NxEquivalent(self, route_nx_equivalent: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) NxEquivalent
         Returns the NX equivalent object.  
           
                    The NX Equivalent of a  Routing::Electrical::ConnectorDevice  is an  Assemblies::Component .
                    The NX Equivalent of a  Routing::Electrical::ElectricalStockDevice  is a  Routing::Wire .
                    The NX Equivalent of a  Routing::Electrical::HarnessDevice  is also a  Routing::Wire .
                    The NX Equivalent of a  Routing::StockDevice  is a  Routing::Stock .
                  
         
        """
        pass
    @property
    def PartName(self) -> str:
        """
        Getter for property: (str) PartName
         Returns the part name   
            
         
        """
        pass
    @PartName.setter
    def PartName(self, route_part_name: str):
        """
        Setter for property: (str) PartName
         Returns the part name   
            
         
        """
        pass
    @property
    def PartNumber(self) -> str:
        """
        Getter for property: (str) PartNumber
         Returns the part number   
            
         
        """
        pass
    @PartNumber.setter
    def PartNumber(self, route_part_number: str):
        """
        Setter for property: (str) PartNumber
         Returns the part number   
            
         
        """
        pass
    def GetImplementedConnections(self) -> List[LogicalConnection]:
        """
         Gets connections implemented on single device.
         Returns route_implemented_connections ( LogicalConnection List[NXOp):  .
        """
        pass
    def GetItemDefinition(self) -> ItemDefinition:
        """
         Get item definition. 
         Returns route_item_definition ( ItemDefinition NXOpen):  .
        """
        pass
    def GetReferencingDeviceRelshps(self) -> List[DeviceRelationship]:
        """
         Gets referencing device relationships. 
         Returns route_device_relshps ( DeviceRelationship List[NXOp):  .
        """
        pass
    def GetRelatedSingleDevices(self) -> List[SingleDevice]:
        """
         Assuming this single device to be the relating single device in a
                NXOpen.Routing.DeviceRelationship, get associated related single devices. 
         Returns related_single_devices ( SingleDevice List[NXOp):  .
        """
        pass
    def GetRelatingSingleDevice(self) -> SingleDevice:
        """
         Assuming this single device to be the related single device in a
                NXOpen.Routing.DeviceRelationship, get associated relating single device. 
         Returns relating_single_device ( SingleDevice NXOpen):  .
        """
        pass
    def ManuallyDelete(self) -> SingleDevice.DeleteObjectResult:
        """
         Deletes the single device. 
         Returns elec_delete_object_result ( SingleDevice.DeleteObjectResult NXOpen):  .
        """
        pass
import NXOpen
class SpaceReservationBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Routing.SpaceReservationBuilder
    
        This builder takes one or more segments and creates space reservation stock on it.
    """
    @property
    def GridTopologyEligibilityFlag(self) -> bool:
        """
        Getter for property: (bool) GridTopologyEligibilityFlag
         Returns the grid topology eligibility flag.  
           When this flag is set, a non circular space reservation will produce bend faces in the bend regions instead of merged faces.
                    This flag has no effect on space reservation.   
         
        """
        pass
    @GridTopologyEligibilityFlag.setter
    def GridTopologyEligibilityFlag(self, gridOptionEligible: bool):
        """
        Setter for property: (bool) GridTopologyEligibilityFlag
         Returns the grid topology eligibility flag.  
           When this flag is set, a non circular space reservation will produce bend faces in the bend regions instead of merged faces.
                    This flag has no effect on space reservation.   
         
        """
        pass
    @property
    def SegmentCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SegmentCollector
         Returns the routing segment collector   
            
         
        """
        pass
    @property
    def StockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for creating space reservation stock   
            
         
        """
        pass
import NXOpen
class SplineData(NXOpen.TransientObject): 
    """  Represents a transient NXOpen.Routing.SplineData object. 
         This class provides the ability to create or edit Routing Spline Segments. 
         To create an instance of this class, call NXOpen.Routing.SegmentManager.CreateSplineData
               or NXOpen.Routing.SplineSegment.SplineData. 
         For example, to change an existing spline, first get the spline's data by calling
               NXOpen.Routing.SegmentManager.CreateSplineData with the spline
               you want to update. Then call NXOpen.Routing.SplineData.GetDefiningPoints
               to get the defining points. You can change the point's position, extension direction,
               or extension values using the NXOpen.Routing.DefiningPoint methods. 
         To create a new spline, create a new NXOpen.Routing.SplineData
               object by calling NXOpen.Routing.SplineSegment.SplineData. Then
               add points and extensions using the NXOpen.Routing.DefiningPoint methods.  """
    @property
    def NumDefiningPoints(self) -> int:
        """
        Getter for property: (int) NumDefiningPoints
         Returns the number of  NXOpen::Routing::DefiningPoint  objects.  
             
         
        """
        pass
    def CommitChanges(self) -> ISegment:
        """
         Commit the NXOpen.Routing.SplineData changes. 
         Returns splineSegment ( ISegment NXOpen):  the resultant spline segment. .
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the NXOpen.Routing.SplineData object. 
        """
        pass
    def GetBackwardExtension(self, index: int) -> float:
        """
         Get the backward extension of the NXOpen.Routing.DefiningPoint at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
         Returns backwardExtension (float):  The backward extension at the index. .
        """
        pass
    def GetDefiningPoint(self, index: int) -> DefiningPoint:
        """
         Get the NXOpen.Routing.DefiningPoint object at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
         Returns definingPoint ( DefiningPoint NXOpen):   .
        """
        pass
    def GetDefiningPoints(self) -> List[DefiningPoint]:
        """
         Get the NXOpen.Routing.DefiningPoint objects. 
         Returns definingPoints ( DefiningPoint List[NXOp):   .
        """
        pass
    def GetDirection(self, index: int) -> NXOpen.Vector3d:
        """
         Get the extension direction of the NXOpen.Routing.DefiningPoint object at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
         Returns direction ( NXOpen.Vector3d):  The direction at the index. .
        """
        pass
    def GetForwardExtension(self, index: int) -> float:
        """
         Get the forward extension of the NXOpen.Routing.DefiningPoint at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
         Returns forwardExtension (float):  the forward extension at the index. .
        """
        pass
    def GetPosition(self, index: int) -> NXOpen.Point3d:
        """
         Get the position of the NXOpen.Routing.DefiningPoint object at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
         Returns position ( NXOpen.Point3d):  The position at the index. .
        """
        pass
    def InsertPositionAfter(self, index: int, position: NXOpen.Point3d) -> int:
        """
         Insert a position after the NXOpen.Routing.DefiningPoint object at the index.
                     The index should be a positive integer less than the number of defining points returned
                           by NXOpen.Routing.SplineData.NumDefiningPoints. 
                     If the insertion of the position is successful, the number of defining points will
                           be incremented and increments the index of all of the positions greater than the
                           index of the inserted position.  
         Returns numDefiningPoints (int):  The resultant number of defining points. .
        """
        pass
    def InsertPositionBefore(self, index: int, position: NXOpen.Point3d) -> int:
        """
         Insert a position before the NXOpen.Routing.DefiningPoint object at the index.
                     The index should be a positive integer less than the number of defining points returned
                           by NXOpen.Routing.SplineData.NumDefiningPoints. 
                     If the insertion of the position is successful, the number of defining points will
                           be incremented and increments the index of all of the positions greater than the
                           index of the inserted position.  
         Returns numDefiningPoints (int):  The resultant number of defining points. .
        """
        pass
    def IsConstrained(self, index: int) -> bool:
        """
         Does the NXOpen.Routing.DefiningPoint have any
                    NXOpen.Positioning.Constraint that determines its location?
                    If so, you cannot change the position of this point. 
         Returns isConstrained (bool): .
        """
        pass
    def RemoveExtension(self, index: int) -> None:
        """
         Remove an extension on the NXOpen.Routing.DefiningPoint at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
        """
        pass
    def RemovePosition(self, index: int) -> int:
        """
         Remove a position of the NXOpen.Routing.DefiningPoint object at the index.
                     The index should be a positive integer less than the number of defining points returned
                           by NXOpen.Routing.SplineData.NumDefiningPoints. 
                     If the removal of the position is successful, the number of defining points will
                           be decremented and decrements the index of all the positions greater than the
                           index of the point removed.  
         Returns numDefiningPoints (int):  The resultant number of defining points. .
        """
        pass
    def SetBackwardExtension(self, index: int, backwardExtension: float) -> None:
        """
         Set the backward extension of the NXOpen.Routing.DefiningPoint at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
        """
        pass
    def SetDefiningPoint(self, index: int, definingPoint: DefiningPoint) -> None:
        """
         Set the NXOpen.Routing.DefiningPoint object at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
        """
        pass
    def SetDefiningPoints(self, definingPoints: List[DefiningPoint]) -> None:
        """
         Set the NXOpen.Routing.DefiningPoint objects. 
        """
        pass
    def SetDirection(self, index: int, direction: NXOpen.Vector3d) -> None:
        """
         Set the extension direction of the NXOpen.Routing.DefiningPoint object at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
        """
        pass
    def SetForwardExtension(self, index: int, forwardExtension: float) -> None:
        """
         Set the forward extension of the NXOpen.Routing.DefiningPoint at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
        """
        pass
    def SetPosition(self, index: int, position: NXOpen.Point3d) -> None:
        """
         Set the position of the NXOpen.Routing.DefiningPoint object at the index.
                    The index should be a positive integer less than the number of defining points returned
                    by NXOpen.Routing.SplineData.NumDefiningPoints. 
        """
        pass
class SplineOptions(Enum):
    """
    Members Include: 
     |ByPoints|  
     |ByPoles|  

    """
    ByPoints: int
    ByPoles: int
    @staticmethod
    def ValueOf(value: int) -> SplineOptions:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class SplinePathBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.SplinePathBuilder object.
        The builder allows for creating and editing D-Cubed constrained splines, adding extensions,
        adding stock offset points, adding stock, locking length, adding slack, and locking to other
        D-Cubed constrained objects.
    """
    class DefiningPointMethod(Enum):
        """
        Members Include: 
         |CreatePoint| 
         |UseExisting| 

        """
        CreatePoint: int
        UseExisting: int
        @staticmethod
        def ValueOf(value: int) -> SplinePathBuilder.DefiningPointMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefiningTypes(Enum):
        """
        Members Include: 
         |Unsupported|  The defining type is unsupported. 
         |Interpolation|  The defining type represents a C1-continuous, interpolation spline. 
         |Parametric|  The defining type represents a G1-continuous, parametric curve. 
         |Bezier|  The defining type represents a G1-continuous, piecewise cubic Bezier. 
         |BezierSlack|  The defining type represents a G1-continuous, piecewise cubic Bezier with pseudo gravity slack. 
         |BezierMaxCurvature|  The defining type represents a G1-continuous, piecewise cubic Bezier with bounded maximum curvature. 
         |BezierMaxCurvatureSlacked|  The defining type represents a G1-continuous, piecewise cubic Bezier with bounded maximum curvature with pseudo gravity slack. 

        """
        Unsupported: int
        Interpolation: int
        Parametric: int
        Bezier: int
        BezierSlack: int
        BezierMaxCurvature: int
        BezierMaxCurvatureSlacked: int
        @staticmethod
        def ValueOf(value: int) -> SplinePathBuilder.DefiningTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DragMode(Enum):
        """
        Members Include: 
         |Active|  The drag network is active 
         |Inactive|  The drag network is inactive 

        """
        Active: int
        Inactive: int
        @staticmethod
        def ValueOf(value: int) -> SplinePathBuilder.DragMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplinePathAttributeOptions(Enum):
        """
        Members Include: 
         |Radius|  A radius method option for spline user attribute  
         |RatioToDiameter|  A ratio to diameter method option for spline user attribute. 

        """
        Radius: int
        RatioToDiameter: int
        @staticmethod
        def ValueOf(value: int) -> SplinePathBuilder.SplinePathAttributeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplinePathRadiusSource(Enum):
        """
        Members Include: 
         |Expression|  Specify radius by value. 
         |RatioToDiameter|  Specify radius by ratio to stock.
         |Attribute|  Specify radius by attribute. 

        """
        Expression: int
        RatioToDiameter: int
        Attribute: int
        @staticmethod
        def ValueOf(value: int) -> SplinePathBuilder.SplinePathRadiusSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplinePathSlackType(Enum):
        """
        Members Include: 
         |PercentLength|  The length of the spline is increased by a percentage of the spline length. 
         |AdditionalLength|  The length of the spline is increased by an additional length. 
         |LockLength|  The length of the spline is slacking to a specified and locked length. 
         |TotalPercentage|  Slack value is ratio of extra length. Non-end defining points relaxed down 
         |TotalAdditional|  Slack value is extra length. Non-end defining points relaxed down 
         |Undefined|  Slack length is undefined. 

        """
        PercentLength: int
        AdditionalLength: int
        LockLength: int
        TotalPercentage: int
        TotalAdditional: int
        Undefined: int
        @staticmethod
        def ValueOf(value: int) -> SplinePathBuilder.SplinePathSlackType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundedCurvature(self) -> bool:
        """
        Getter for property: (bool) BoundedCurvature
         Returns whether the spline maximum bounded radius value should be used.  
             
         
        """
        pass
    @BoundedCurvature.setter
    def BoundedCurvature(self, useBoundedCurvature: bool):
        """
        Setter for property: (bool) BoundedCurvature
         Returns whether the spline maximum bounded radius value should be used.  
             
         
        """
        pass
    @property
    def BoundedCurvatureRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoundedCurvatureRadius
         Returns the minimum radius allowed for this spline.  
             
         
        """
        pass
    @property
    def BoundedCurvatureRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BoundedCurvatureRatio
         Returns the minimum radius allowed for this spline as a ratio to diameter.  
             
         
        """
        pass
    @property
    def DefiningType(self) -> SplinePathBuilder.DefiningTypes:
        """
        Getter for property: ( SplinePathBuilder.DefiningTypes NXOpen) DefiningType
         Returns the type which specifies the shape of the spline.  
          
                See  NXOpen::Routing::SplinePathBuilder::DefiningTypes  for valid options   
         
        """
        pass
    @DefiningType.setter
    def DefiningType(self, definingType: SplinePathBuilder.DefiningTypes):
        """
        Setter for property: ( SplinePathBuilder.DefiningTypes NXOpen) DefiningType
         Returns the type which specifies the shape of the spline.  
          
                See  NXOpen::Routing::SplinePathBuilder::DefiningTypes  for valid options   
         
        """
        pass
    @property
    def MinimumCheckingAllowableRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumCheckingAllowableRatio
         Returns the minimum ratio allowed for this spline  
            
         
        """
        pass
    @property
    def MinimumCheckingAllowableValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumCheckingAllowableValue
         Returns the minimum radius allowed for this spline.  
             
         
        """
        pass
    @property
    def MinimumCheckingMethod(self) -> SplinePathBuilder.SplinePathAttributeOptions:
        """
        Getter for property: ( SplinePathBuilder.SplinePathAttributeOptions NXOpen) MinimumCheckingMethod
         Returns the minimum checking method for this spline.  
          
                See  NXOpen::Routing::SplinePathBuilder::SplinePathAttributeOptions  for valid
                options   
         
        """
        pass
    @MinimumCheckingMethod.setter
    def MinimumCheckingMethod(self, routeCheckingMethod: SplinePathBuilder.SplinePathAttributeOptions):
        """
        Setter for property: ( SplinePathBuilder.SplinePathAttributeOptions NXOpen) MinimumCheckingMethod
         Returns the minimum checking method for this spline.  
          
                See  NXOpen::Routing::SplinePathBuilder::SplinePathAttributeOptions  for valid
                options   
         
        """
        pass
    @property
    def MinimumRadius(self) -> float:
        """
        Getter for property: (float) MinimumRadius
         Returns the actual minimum radius of the curve itself.  
             
         
        """
        pass
    @property
    def RadiusSource(self) -> SplinePathBuilder.SplinePathRadiusSource:
        """
        Getter for property: ( SplinePathBuilder.SplinePathRadiusSource NXOpen) RadiusSource
         Returns the driving expression, value, or attribute of the bounded radius.  
             
         
        """
        pass
    @RadiusSource.setter
    def RadiusSource(self, source: SplinePathBuilder.SplinePathRadiusSource):
        """
        Setter for property: ( SplinePathBuilder.SplinePathRadiusSource NXOpen) RadiusSource
         Returns the driving expression, value, or attribute of the bounded radius.  
             
         
        """
        pass
    @property
    def ShowSplineMinimumRadius(self) -> bool:
        """
        Getter for property: (bool) ShowSplineMinimumRadius
         Returns whether the spline minimum radius value should be displayed or not.  
             
         
        """
        pass
    @ShowSplineMinimumRadius.setter
    def ShowSplineMinimumRadius(self, allowDisplay: bool):
        """
        Setter for property: (bool) ShowSplineMinimumRadius
         Returns whether the spline minimum radius value should be displayed or not.  
             
         
        """
        pass
    @property
    def UseMinimumCheckingValue(self) -> bool:
        """
        Getter for property: (bool) UseMinimumCheckingValue
         Returns whether the spline minimum radius value should be checked or not on this spline.  
            
         
        """
        pass
    @UseMinimumCheckingValue.setter
    def UseMinimumCheckingValue(self, useMinRadius: bool):
        """
        Setter for property: (bool) UseMinimumCheckingValue
         Returns whether the spline minimum radius value should be checked or not on this spline.  
            
         
        """
        pass
    def AddDefiningPointAtAbsoluteCoords(self, point: NXOpen.Point3d) -> None:
        """
         Adds a point to the spline.
                    The point will be the new endpoint of the spline.
                
        """
        pass
    def AddDefiningPointToSpline(self, point: NXOpen.Point, createNewPoint: bool) -> int:
        """
         Adds a defining point to the current spline or creates the first point of the new
                    spline.
                
         Returns index (int):  Returns the index the point was added along the spline.
                                                                                                 For example, if 3 points exist on the spline and the new point
                                                                                                 was added between points 0 and 1 this variable would be set to 1.
                                                                                             .
        """
        pass
    def AddSlackToSpline(self, slackType: SplinePathBuilder.SplinePathSlackType, slackValue: NXOpen.Expression, slackDirection: NXOpen.Direction) -> None:
        """
         
        """
        pass
    def AskDefiningData(self) -> List[NXOpen.Point]:
        """
         When a spline is selected for editing, the builder will analyze the spline
                    and gather all of the defining data. The dialog will use this function
                    to retrieve the defining data from the builder to populate its fields.
         Returns points ( NXOpen.Point Li):  Defining points of the spline. .
        """
        pass
    @overload
    def AssignExtension(self, pointIndex: int, direction: NXOpen.Direction, forwardLength: NXOpen.Expression, backwardLength: NXOpen.Expression) -> None:
        """
         Assigns an extension to the point at pointIndex. 
        """
        pass
    @overload
    def AssignExtension(self, pointIndex: int, direction: NXOpen.Direction, forwardLength: NXOpen.Expression, backwardLength: NXOpen.Expression, forceDeleteOnZeroExpression: bool) -> None:
        """
         Assigns an extension to the point at pointIndex. 
        """
        pass
    def AssignHealPathExtension(self, pointIndex: int, direction: NXOpen.Direction, forwardLength: NXOpen.Expression, backwardLength: NXOpen.Expression) -> None:
        """
         Assigns an extension to the point at pointIndex for Heal Path. 
        """
        pass
    def AssignTangentExtensionForPointAtIndex(self, index: int, forwardLength: NXOpen.Expression, backwardLength: NXOpen.Expression) -> Tuple[NXOpen.Vector3d, NXOpen.Vector3d, NXOpen.Direction]:
        """
         Assigns the extension direction and expressions tangent to the spline path at the given
                point index. 
         Returns A tuple consisting of (tangent, normal, extensionDir). 
         - tangent is:  NXOpen.Vector3d. Extension direction. .
         - normal is:  NXOpen.Vector3d. Curve normal. .
         - extensionDir is:  NXOpen.Direction. Direction object. .

        """
        pass
    def CommitDrag(self, definingPoint: NXOpen.Point) -> None:
        """
         Clears the current drag network. 
        """
        pass
    def CreateAssignTangencyBuilder(self) -> AssignTangencyBuilder:
        """
         Creates a NXOpen.Routing.AssignTangencyBuilder object. 
         Returns assignTangencyBuilder ( AssignTangencyBuilder NXOpen): .
        """
        pass
    def CreateHealPathConstraints(self, startObject: NXOpen.NXObject, endObject: NXOpen.NXObject) -> None:
        """
         Creates constraints between the start and end objects passed in to the spline.  These
                    constraints can include touch  align to the RCP and parallel to the spline extension.
        """
        pass
    def DeleteDefiningPointAtIndex(self, index: int) -> None:
        """
         Deletes a defining point from the spline. 
        """
        pass
    def DetachPoint(self, index: int) -> None:
        """
         Detaches the point at the selected index from all objects its attached to using a Touch
                constraint. 
        """
        pass
    def GetAssignTangencyBuilder(self) -> AssignTangencyBuilder:
        """
         Get a NXOpen.Routing.AssignTangencyBuilder object. 
         Returns assignTangencyBuilder ( AssignTangencyBuilder NXOpen): .
        """
        pass
    def GetDefiningPointPositions(self) -> List[float]:
        """
         Gets the positions of the defining points as an array of doubles.
                    Each point's XYZ coordinates are represented by three doubles.
                    X1, Y1, Z1, X2, Y2, Z2, X3, Y3, Z3, ...   
                
         Returns pointPositions (List[float]):  array of doubles representing the defining points. .
        """
        pass
    def GetDefiningPointPositionsAsPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets the positions of the defining points as an array of Point3d coordinates. 
         Returns pointPositions ( NXOpen.Point3d Li):  array of points representing the defining points. .
        """
        pass
    def GetExtensionDataForPointAtIndex(self, index: int) -> Tuple[NXOpen.Expression, NXOpen.Expression, NXOpen.Vector3d]:
        """
         Get the extension expressions at the given index. 
         Returns A tuple consisting of (forwardLength, backwardLength, extDirection). 
         - forwardLength is:  NXOpen.Expression. Forward extension length. .
         - backwardLength is:  NXOpen.Expression. Backward extension length. .
         - extDirection is:  NXOpen.Vector3d. Extension direction. .

        """
        pass
    def GetLargestDiameterStock(self) -> Stock:
        """
         Returns the stock with the largest on the current segment.
         Returns largestDia ( Stock NXOpen):  The stock with the largest diameter. .
        """
        pass
    def GetLockedSplineMinimumLength(self) -> float:
        """
         Returns the minimum length of the spline.  The minimum length is the straight line
                distance between all defining points, including extensions. 
         Returns length (float):  The minimum length of the spline. .
        """
        pass
    def GetOffsetData(self, index: int) -> Tuple[int, NXOpen.Point, NXOpen.Direction, str]:
        """
         Returns the Stock Offset data associated with a given point. Output can be NULL if the
                associated point is not a stock offset point. 
         Returns A tuple consisting of (method, basePoint, offDir, exp). 
         - method is: int. The type of offset object.
                                                                                                 0 = Not Offset,
                                                                                                 1 = Stock Offset Point,
                                                                                                 2 = Stock Offset Surface. .
         - basePoint is:  NXOpen.Point. The base point frim the offset object. .
         - offDir is:  NXOpen.Direction. The offset direction. .
         - exp is: str. The expression defining the offset distance. .

        """
        pass
    def GetRouteSegment(self) -> NXOpen.Curve:
        """
         Gets the routing segment managed by the builder, if it exists. 
         Returns segment ( NXOpen.Curve):  Visible Routing BCurve Segment. .
        """
        pass
    def GetSplineLength(self) -> float:
        """
         Gets the current length of the spline. 
         Returns length (float):  The length of the current spline. .
        """
        pass
    def GetSplineLengthNoShaping(self) -> float:
        """
         Gets the current length of the spline without shaping applied. 
         Returns length (float):  The length of the current spline without shaping. .
        """
        pass
    def GetStartAndEndRcp(self) -> Tuple[ControlPoint, ControlPoint]:
        """
         Gets the RCPs managed by the builder, if they exist. 
         Returns A tuple consisting of (endRcp, startRcp). 
         - endRcp is:  ControlPoint NXOpen. The target ControlPoint. .
         - startRcp is:  ControlPoint NXOpen. The source ControlPoint. .

        """
        pass
    def InitializeDrag(self, index: int) -> None:
        """
         Initialize the D-Cubed dragging functionality for the point at index. 
        """
        pass
    def IsLengthLocked(self) -> Tuple[NXOpen.Expression, bool, NXOpen.Direction]:
        """
         Is the spline length locked? 
         Returns A tuple consisting of (length, isLocked, slackDirection). 
         - length is:  NXOpen.Expression. The locked length of the spline. .
         - isLocked is: bool. Is the spline length locked? .
         - slackDirection is:  NXOpen.Direction. The direction to apply slack. .

        """
        pass
    def IsSplineSlacked(self) -> Tuple[bool, SplinePathBuilder.SplinePathSlackType, NXOpen.Expression, NXOpen.Direction]:
        """
         
         Returns A tuple consisting of (slacked, slackType, slackValue, downDir). 
         - slacked is: bool. Is slack applied to the spline? .
         - slackType is:  SplinePathBuilder.SplinePathSlackType NXOpen. The type of slack. .
         - slackValue is:  NXOpen.Expression. The added amount of slack. .
         - downDir is:  NXOpen.Direction. The slack direction. .

        """
        pass
    def LockSplineLengthNoShaping(self, length: NXOpen.Expression) -> None:
        """
         Locks the length of the current spline. 
        """
        pass
    def LockSplineLengthWithShaping(self, length: NXOpen.Expression, slackDirection: NXOpen.Direction) -> None:
        """
         Locks the length of the current spline. 
        """
        pass
    def LockSplineLengthWithShapingFixedPoints(self, length: NXOpen.Expression, slackDirection: NXOpen.Direction) -> None:
        """
         Locks the length of the current spline and fixes the interior points of the spline. 
        """
        pass
    def RemoveAllShaping(self) -> None:
        """
         Removes all shaping applied to the spline (Lock length, slacking). 
        """
        pass
    def RemoveLengthConstraint(self) -> None:
        """
         Removes the spline length constraint that makes the spline a locked length spline. 
        """
        pass
    def SetAddPointsOnSubdivideFlag(self, addPoints: bool) -> None:
        """
         Sets whether or not additional points will be added to a spline which is created as the
                    result of a subdivide.
                    If true, new points will be added to maintain a shape similar to the original curve.
                
        """
        pass
    def SetCreateTangencyFlag(self, createTangency: bool) -> None:
        """
         Sets whether or not additional the newly created spline will be made tangent to
                    connecting splines.
                
        """
        pass
    def SetDefaultPortExtensionLength(self, value: float) -> None:
        """
         Sets the default port extension length to be used when creating or editing points at port
                locations that do not already have an extension . 
        """
        pass
    def SetLockToSelectedFlag(self, lockSelected: bool) -> None:
        """
         Sets whether the spline will attempt to lock points to selected object.
                    This flag is only checked when adding a point to a spline by passing in a smart point to
                    derive a new dumb spline point from.
                    If the smart point is derived from a Port, ControlPoint, or other Routing Object, the
                    new spline defining point will lock to that object.
                    This flag is also checked during commit, where endpoint associativity is applied.
                
        """
        pass
    def SetSplineLength(self, length: NXOpen.Expression) -> None:
        """
         Sets the length of the current spline without permanently locking the spline to that length. 
        """
        pass
    def SetStockBoundedDiameter(self, value: float) -> None:
        """
         Sets the driving diameter of the current stock for the ratio-to-diameter bounded curvature. 
        """
        pass
    def ShapeByAdditionalLengthMovingPoints(self, length: NXOpen.Expression, slackType: SplinePathBuilder.SplinePathSlackType, slackDirection: NXOpen.Direction) -> None:
        """
         Adds slack to the spline without locking the length.
                    This will move the interior defining points of the spline in the slack direction
                    until the given length is reached.
                
        """
        pass
    def UpdateDefiningPoint(self, index: int, point: NXOpen.Point, inDrag: bool, translation: NXOpen.Vector3d) -> None:
        """
         Updates the position of a point on the spline.  
        """
        pass
    def UpdateDefiningPointPositionAtIndex(self, index: int, point: NXOpen.Point, inDrag: bool) -> None:
        """
         Updates the position of a point on the spline.  
        """
        pass
    def UpdateExtensionDirectionAtIndex(self, index: int, direction: NXOpen.Vector3d) -> None:
        """
         Update the extension orientation at the point index. 
        """
        pass
    def UpdateExtensionDirectionForPointAtIndex(self, index: int, deltaTrans: NXOpen.Vector3d, orientation: NXOpen.Matrix3x3, inDrag: bool) -> None:
        """
         Update the extension orientation at the point index. 
        """
        pass
import NXOpen
class SplineSegmentCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.SplineSegment objects. """
    pass
import NXOpen
class SplineSegment(NXOpen.Spline): 
    """ Represents a spline segment. """
    @property
    def FollowCurve(self) -> NXOpen.Curve:
        """
        Getter for property: ( NXOpen.Curve) FollowCurve
         Returns  the segment follow curve.  
            NULL object indicates segment has no follow curve   
         
        """
        pass
    @property
    def Guid(self) -> str:
        """
        Getter for property: (str) Guid
         Returns the Globally Unique Identifier (GUID) for this segment.  
             
         
        """
        pass
    @property
    def IsFlexibleParametricSplineSegment(self) -> bool:
        """
        Getter for property: (bool) IsFlexibleParametricSplineSegment
         Returns a boolean value that indicates whether the spline has been
                    converted to the new flexible parametric spline in NX9.  
             
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns  the length of the segment.  
             
         
        """
        pass
    @property
    def SplineData(self) -> SplineData:
        """
        Getter for property: ( SplineData NXOpen) SplineData
         Returns the  NXOpen::Routing::SplineData  object.  
          
                   This class provides the ability to query and edit a Routing Spline Segment.   
                   The  NXOpen::Routing::SplineData  provides access to the
                        NXOpen::Routing::DefiningPoint  objects which represent the
                       positions and optional directions and forwardbackward magnitudes for extensions.      
         
        """
        pass
import NXOpen
class SplitDuctBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Routing.SplitDuctBuilder
        
        Builder for creatingediting splits at an end of a duct.
        Takes an end face of a rectangular stock and splits it into a pair of
        divisions based on the specified absolute flow percentage for each division.
    """
    class FlowTypes(Enum):
        """
        Members Include: 
         |AbsoluteFlow|  Absolute flow 
         |RelativeFlow|  Relative flow 

        """
        AbsoluteFlow: int
        RelativeFlow: int
        @staticmethod
        def ValueOf(value: int) -> SplitDuctBuilder.FlowTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DivisionsList(self) -> NXOpen.TaggedObjectList:
        """
        Getter for property: ( NXOpen.TaggedObjectList) DivisionsList
         Returns the divisions list   
            
         
        """
        pass
    @property
    def FlowType(self) -> SplitDuctBuilder.FlowTypes:
        """
        Getter for property: ( SplitDuctBuilder.FlowTypes NXOpen) FlowType
         Returns the type of flow to be displayed in the list flow column   
            
         
        """
        pass
    @FlowType.setter
    def FlowType(self, flowType: SplitDuctBuilder.FlowTypes):
        """
        Setter for property: ( SplitDuctBuilder.FlowTypes NXOpen) FlowType
         Returns the type of flow to be displayed in the list flow column   
            
         
        """
        pass
    def AddDivisionsBuilderToList(self, selectedPort: Port) -> None:
        """
         Creates divisions builders for all the divisions, if any, associated with
                    the cross-section to which the input port belongs and adds them to the list
                    of divisions.
                
        """
        pass
    def CreateNewDivisionsListItem(self, selectedPort: Port, isAbsoluteFlow: bool) -> DivisionsBuilder:
        """
         Creates a new item for the divisions list in Split Duct dialog 
         Returns divisionsBuilder ( DivisionsBuilder NXOpen): .
        """
        pass
import NXOpen
class SplitRunBuilder(NXOpen.Builder): 
    """ Builder Class for Split Run Object """
    @property
    def NameToFrom(self) -> bool:
        """
        Getter for property: (bool) NameToFrom
         Returns the new run name to From section or not  
            
         
        """
        pass
    @NameToFrom.setter
    def NameToFrom(self, nameToFrom: bool):
        """
        Setter for property: (bool) NameToFrom
         Returns the new run name to From section or not  
            
         
        """
        pass
    @property
    def RunName(self) -> str:
        """
        Getter for property: (str) RunName
         Returns the user mentioned run name after split  
            
         
        """
        pass
    @RunName.setter
    def RunName(self, runName: str):
        """
        Setter for property: (str) RunName
         Returns the user mentioned run name after split  
            
         
        """
        pass
    @property
    def RunObject(self) -> SelectRun:
        """
        Getter for property: ( SelectRun NXOpen) RunObject
         Returns the user selected Run for Split   
            
         
        """
        pass
    @property
    def SplitObject(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SplitObject
         Returns the user selected split object   
            
         
        """
        pass
    def GetAttributeHolder(self) -> NXOpen.NXObject:
        """
         Gets Attribute holder in builder. 
         Returns attributeHolder ( NXOpen.NXObject):  Object to hold template attributes .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.GeometricUtilities
class StockBlockBuilder(NXOpen.TaggedObject): 
    """ Assigns stocks to segments based on user's criteria and the current default stock.  """
    class AssignStockSubType(Enum):
        """
        Members Include: 
         |Stock|  Default stock subtype.             
         |SpaceReservation|  Space Reservation stock subtype.   

        """
        Stock: int
        SpaceReservation: int
        @staticmethod
        def ValueOf(value: int) -> StockBlockBuilder.AssignStockSubType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AssignStockType(Enum):
        """
        Members Include: 
         |Stock|  Default stock type.             
         |Overstock|  Overstock stock type.           

        """
        Stock: int
        Overstock: int
        @staticmethod
        def ValueOf(value: int) -> StockBlockBuilder.AssignStockType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpaceReservationMethod(Enum):
        """
        Members Include: 
         |NotSet|  No Stock. 
         |FromStartObject|  Finds a stock based off of the
                                                                                                                default stock and the object selected by the user. 
         |Circular|  User specified diameter, creates round
                                                                                                                space reservation stock. 
         |Rectangular|  User specified values, creates rectangular
                                                                                                                space reservation stock. 
         |FlatOval|  User specified values, creates flat_oval 
                                                                                                                space reservation stock. 
         |SpecifiedSpaceReservation|  sp selected from Specify Item dialog 

        """
        NotSet: int
        FromStartObject: int
        Circular: int
        Rectangular: int
        FlatOval: int
        SpecifiedSpaceReservation: int
        @staticmethod
        def ValueOf(value: int) -> StockBlockBuilder.SpaceReservationMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpaceReservationSelectionSource(Enum):
        """
        Members Include: 
         |NotSpecified|  Space Reservation not specified 
         |ClassficationObject|  SpaceReservation selected from classification 
         |PTBLibrary|  SpaceReservation selected from part table library 
         |Session|  SpaceReservation selected from NX session 

        """
        NotSpecified: int
        ClassficationObject: int
        PTBLibrary: int
        Session: int
        @staticmethod
        def ValueOf(value: int) -> StockBlockBuilder.SpaceReservationSelectionSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StockMethod(Enum):
        """
        Members Include: 
         |NotSet|  No Stock. 
         |SpecifiedStock|  Stock selected from Specify Item dialog 

        """
        NotSet: int
        SpecifiedStock: int
        @staticmethod
        def ValueOf(value: int) -> StockBlockBuilder.StockMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StockSelectionSource(Enum):
        """
        Members Include: 
         |NotSpecified|  Stock not specified 
         |ClassficationObject|  Stock selected from classification 
         |PTBLibrary|  Stock selected from part table library 
         |Database|  stock selected from database or disk 
         |Session|  stock selected from NX session 

        """
        NotSpecified: int
        ClassficationObject: int
        PTBLibrary: int
        Database: int
        Session: int
        @staticmethod
        def ValueOf(value: int) -> StockBlockBuilder.StockSelectionSource:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns the diameter value to use for the 
                     NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodCircular  
                    method of stock assignment.  
              
         
        """
        pass
    @Diameter.setter
    def Diameter(self, diameter: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) Diameter
         Returns the diameter value to use for the 
                     NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodCircular  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def FlatOvalHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatOvalHeight
         Returns the height value to use for the   
                    NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodFlatOval  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def FlatOvalWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlatOvalWidth
         Returns the Width value to use for the   
                    NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodFlatOval  
                    method of stock assignment      
            
         
        """
        pass
    @property
    def RectangularHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangularHeight
         Returns the height value to use for the   
                    NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodRectangular  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def RectangularWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RectangularWidth
         Returns the Width value to use for the   
                    NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodRectangular  
                    method of stock assignment      
            
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle   
            
         
        """
        pass
    @property
    def SpaceReservationMethodType(self) -> StockBlockBuilder.SpaceReservationMethod:
        """
        Getter for property: ( StockBlockBuilder.SpaceReservationMethod NXOpen) SpaceReservationMethodType
         Returns the method to determine which space reservation to assign.  
             
         
        """
        pass
    @SpaceReservationMethodType.setter
    def SpaceReservationMethodType(self, method: StockBlockBuilder.SpaceReservationMethod):
        """
        Setter for property: ( StockBlockBuilder.SpaceReservationMethod NXOpen) SpaceReservationMethodType
         Returns the method to determine which space reservation to assign.  
             
         
        """
        pass
    @property
    def StartObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) StartObject
         Returns the start object to use for the 
                     NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodFromStartObject  
                    method of stock assignment.  
              
         
        """
        pass
    @StartObject.setter
    def StartObject(self, start_object: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) StartObject
         Returns the start object to use for the 
                     NXOpen::Routing::StockBlockBuilder::SpaceReservationMethodFromStartObject  
                    method of stock assignment.  
              
         
        """
        pass
    @property
    def StockMethodType(self) -> StockBlockBuilder.StockMethod:
        """
        Getter for property: ( StockBlockBuilder.StockMethod NXOpen) StockMethodType
         Returns the method to determine which stock to assign.  
             
         
        """
        pass
    @StockMethodType.setter
    def StockMethodType(self, method: StockBlockBuilder.StockMethod):
        """
        Setter for property: ( StockBlockBuilder.StockMethod NXOpen) StockMethodType
         Returns the method to determine which stock to assign.  
             
         
        """
        pass
    @property
    def StockSubType(self) -> StockBlockBuilder.AssignStockSubType:
        """
        Getter for property: ( StockBlockBuilder.AssignStockSubType NXOpen) StockSubType
         Returns the type of stock being assigned.  
             
         
        """
        pass
    @StockSubType.setter
    def StockSubType(self, stock_type: StockBlockBuilder.AssignStockSubType):
        """
        Setter for property: ( StockBlockBuilder.AssignStockSubType NXOpen) StockSubType
         Returns the type of stock being assigned.  
             
         
        """
        pass
    @property
    def StockType(self) -> StockBlockBuilder.AssignStockType:
        """
        Getter for property: ( StockBlockBuilder.AssignStockType NXOpen) StockType
         Returns the type of stock being assigned.  
             
         
        """
        pass
    @StockType.setter
    def StockType(self, stock_type: StockBlockBuilder.AssignStockType):
        """
        Setter for property: ( StockBlockBuilder.AssignStockType NXOpen) StockType
         Returns the type of stock being assigned.  
             
         
        """
        pass
    def GetClassificationObjectIdentifierForSpaceReservation(self) -> str:
        """
         Get the identifier of the classification object associated with the space reservation part to place 
                     NOTE: Client should NOT free the returned string 
         Returns classificationObjectId (str):  .
        """
        pass
    def GetClassificationObjectIdentifierForStock(self) -> str:
        """
         Get the identifier of the classification object associated with the stock part to place 
                    NOTE: Client should NOT free the returned string 
         Returns classificationObjectId (str):  .
        """
        pass
    def GetFileSpecificationOfSpaceReservationToPlace(self) -> str:
        """
         Get the file specification of the space reservation part to place 
                    NOTE: Client should NOT free the returned string 
         Returns filename (str):  .
        """
        pass
    def GetFileSpecificationOfStockToPlace(self) -> str:
        """
         Get the file specification of the stock part to place 
                    NOTE: Client should NOT free the returned string 
         Returns filename (str):  .
        """
        pass
    def GetLibraryDefinedAttributeHolderForSpaceReservation(self) -> AttributeHolder:
        """
         Gets the attribute holder for library defined attributes on space reservation to be applied 
         Returns libraryDefinedAttributeHolder ( AttributeHolder NXOpen): .
        """
        pass
    def GetLibraryDefinedAttributeHolderForStock(self) -> AttributeHolder:
        """
         Gets the attribute holder for library defined attributes on stock to be applied 
         Returns libraryDefinedAttributeHolder ( AttributeHolder NXOpen): .
        """
        pass
    def ResetAttributesOnLibraryDefinedAttributeHolder(self) -> None:
        """
         Resets the attribute holder for library defined attributes for stock and space reservation attribute holders
                    This API is recommended to be used before assigning attributes onto builder so as to ensure stockspace reservation apply operation to function correctly 
        """
        pass
    def SetClassificationObjectIdentifierForSpaceReservation(self, classificationObjectId: str) -> None:
        """
         Sets the identifier of the classification object associated with the space reservation part to place 
        """
        pass
    def SetClassificationObjectIdentifierForStock(self, classificationObjectId: str) -> None:
        """
         Sets the identifier of the classification object associated with the stock part to place 
        """
        pass
    def SetComponentSelectedInSession(self, component: NXOpen.Assemblies.Component) -> None:
        """
         Sets stock component selected in NX session while applying stock 
        """
        pass
    def SetFileSpecificationOfSpaceReservationToPlace(self, filename: str) -> None:
        """
         Sets the file specification of the space reservation part to place 
        """
        pass
    def SetFileSpecificationOfStockToPlace(self, filename: str) -> None:
        """
         Sets the file specification of the stock part to place 
        """
        pass
    def SetPartNumberIdentifierForSpaceReservation(self, partNumberId: str) -> None:
        """
         Sets the part number identifier of the attributeHolder object associated with the stock part to create 
        """
        pass
    def SetPartNumberIdentifierForStock(self, partNumberId: str) -> None:
        """
         Sets the identifier of the attributeHolder object associated with the stock part to create 
        """
        pass
    def SetSegmentAndRotationAngle(self, segment: ISegment, formula: str) -> None:
        """
         Sets the segment and angle to control orientation of stock allocation.
        """
        pass
    def SetSpaceReservationSelectionSource(self, stockSelectionSource: StockBlockBuilder.SpaceReservationSelectionSource) -> None:
        """
         Sets the source of space reservation to assign 
        """
        pass
    def SetStockObjectSelectedInSession(self, component: NXOpen.NXObject) -> None:
        """
         Sets stock object selected in NX session while applying stock 
        """
        pass
    def SetStockSelectionSource(self, stockSelectionSource: StockBlockBuilder.StockSelectionSource) -> None:
        """
         Sets the source of stock to assign 
        """
        pass
import NXOpen
class StockBrowserBuilder(NXOpen.Builder): 
    """ Builder class for stock browser . """
    class TypeFilter(Enum):
        """
        Members Include: 
         |All|  All Stocks 
         |Stock|  Stock 
         |OverStock|  Overstock 
         |FillerStock|  Filler Stock 
         |SpaceReservation|  Space Reservation 
         |FittingOverstock| 

        """
        All: int
        Stock: int
        OverStock: int
        FillerStock: int
        SpaceReservation: int
        FittingOverstock: int
        @staticmethod
        def ValueOf(value: int) -> StockBrowserBuilder.TypeFilter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FilterType(self) -> StockBrowserBuilder.TypeFilter:
        """
        Getter for property: ( StockBrowserBuilder.TypeFilter NXOpen) FilterType
         Returns the stock type filter which defines the type of stock  
            
         
        """
        pass
    @FilterType.setter
    def FilterType(self, stockTypeFilter: StockBrowserBuilder.TypeFilter):
        """
        Setter for property: ( StockBrowserBuilder.TypeFilter NXOpen) FilterType
         Returns the stock type filter which defines the type of stock  
            
         
        """
        pass
    @property
    def NameFilter(self) -> str:
        """
        Getter for property: (str) NameFilter
         Returns the stock name filter which defines filter to name stock   
            
         
        """
        pass
    @NameFilter.setter
    def NameFilter(self, stockNameFilter: str):
        """
        Setter for property: (str) NameFilter
         Returns the stock name filter which defines filter to name stock   
            
         
        """
        pass
    def DeleteStocks(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Deletes the given Routing.Stock or Routing.FittingOverstock 
        """
        pass
    def GetSortedList(self) -> List[NXOpen.NXObject]:
        """
         Get the filtered stock object list 
         Returns objects ( NXOpen.NXObject Li):  Filtered Routing Stocks .
        """
        pass
    def SetSortedList(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Set the filtered stock object list when filter type is changed.
        """
        pass
import NXOpen
class StockBuilder(NXOpen.Builder): 
    """ Builder for creatingediting stocks.
        Create Stock: Takes a set of segments and assign the selected the stock
        to the segments. The stock style and orientation settings are optional.
        Edit Stock: Takes in the selected stock to edit as input and redefines
        the stock with the new settings.
    """
    class StockStyleType(Enum):
        """
        Members Include: 
         |Centerline|  Centreline     
         |SimpleSolid|  Simple Solid   
         |DetailedSolid|  Detailed Solid 

        """
        Centerline: int
        SimpleSolid: int
        DetailedSolid: int
        @staticmethod
        def ValueOf(value: int) -> StockBuilder.StockStyleType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FlipStock(self) -> bool:
        """
        Getter for property: (bool) FlipStock
         Returns the stock flip flag   
            
         
        """
        pass
    @FlipStock.setter
    def FlipStock(self, flipStock: bool):
        """
        Setter for property: (bool) FlipStock
         Returns the stock flip flag   
            
         
        """
        pass
    @property
    def GridTopologyEligibilityFlag(self) -> bool:
        """
        Getter for property: (bool) GridTopologyEligibilityFlag
         Returns the grid topology eligibility flag.  
           When this flag is set, a non circular stock will produce bend faces in the bend regions instead of merged faces.
                    This flag has no effect on circular stock.   
         
        """
        pass
    @GridTopologyEligibilityFlag.setter
    def GridTopologyEligibilityFlag(self, gridOptionEligible: bool):
        """
        Setter for property: (bool) GridTopologyEligibilityFlag
         Returns the grid topology eligibility flag.  
           When this flag is set, a non circular stock will produce bend faces in the bend regions instead of merged faces.
                    This flag has no effect on circular stock.   
         
        """
        pass
    @property
    def RemoveExistingStock(self) -> bool:
        """
        Getter for property: (bool) RemoveExistingStock
         Returns the remove existing stock flag.  
           If set to TRUE the existing stock
                    on the path will be removed when assigning new stock.  
         
        """
        pass
    @RemoveExistingStock.setter
    def RemoveExistingStock(self, removeStock: bool):
        """
        Setter for property: (bool) RemoveExistingStock
         Returns the remove existing stock flag.  
           If set to TRUE the existing stock
                    on the path will be removed when assigning new stock.  
         
        """
        pass
    @property
    def RotationValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationValue
         Returns the rotation value.  
           Determines the rotation angle of the stock.   
         
        """
        pass
    @property
    def SegmentCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SegmentCollector
         Returns the routing object collector that collects segments to assign stock to.  
             
         
        """
        pass
    @property
    def StockAnchor(self) -> str:
        """
        Getter for property: (str) StockAnchor
         Returns the  NXOpen::Routing::Anchor  name associated with the stock.  
             
         
        """
        pass
    @StockAnchor.setter
    def StockAnchor(self, anchorName: str):
        """
        Setter for property: (str) StockAnchor
         Returns the  NXOpen::Routing::Anchor  name associated with the stock.  
             
         
        """
        pass
    @property
    def StockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for stock assignment.  
             
         
        """
        pass
    @StockSettings.setter
    def StockSettings(self, stockBuilder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for stock assignment.  
             
         
        """
        pass
    @property
    def StockStyle(self) -> StockBuilder.StockStyleType:
        """
        Getter for property: ( StockBuilder.StockStyleType NXOpen) StockStyle
         Returns the stock style of the stock to assign   
            
         
        """
        pass
    @StockStyle.setter
    def StockStyle(self, stockStyle: StockBuilder.StockStyleType):
        """
        Setter for property: ( StockBuilder.StockStyleType NXOpen) StockStyle
         Returns the stock style of the stock to assign   
            
         
        """
        pass
    @property
    def SwapProfile(self) -> bool:
        """
        Getter for property: (bool) SwapProfile
         Returns the profile swap flag.  
           Determines whether the profile should be
                    at the path start or end.  
         
        """
        pass
    @SwapProfile.setter
    def SwapProfile(self, swapProfile: bool):
        """
        Setter for property: (bool) SwapProfile
         Returns the profile swap flag.  
           Determines whether the profile should be
                    at the path start or end.  
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class StockCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.Stock objects.  """
    @overload
    def AddStock(self, stock_part: CharacteristicList, data_charx: CharacteristicList, segments: List[ISegment], route_level: str) -> None:
        """
         Creates stock on the given segments. The segments do not need to be in order, and don't
                necessarily have to form a single path. 
        """
        pass
    @overload
    def AddStock(self, stock_part: CharacteristicList, data_charx: CharacteristicList, segments: List[ISegment], route_level: str) -> List[Stock]:
        """
         Creates stock NXOpen.Routing.Stock on the given segments. The segments do not need to be in order, and don't
                necessarily have to form a single path. Returns created stock and number of stock 
         Returns stocks ( Stock List[NXOp):  Array of stocks created .
        """
        pass
    @overload
    def AddStock(self, stock_part: CharacteristicList, data_charx: CharacteristicList, segments: List[ISegment], route_level: str, is_space_reservation: bool) -> List[Stock]:
        """
         Creates normal or space reservation stock on the given segments. The segments do not need to be in order,
                 and don't necessarily have to form a single path.
         Returns stocks ( Stock List[NXOp):  Array of stocks created .
        """
        pass
    @overload
    def AddStock(self, stock_part: CharacteristicList, data_charx: CharacteristicList, segments: List[ISegment], route_level: str, is_space_reservation: bool, anchor_name: str) -> List[Stock]:
        """
         Creates normal or space reservation stock on the given segments. The segments do not need to be in order,
                 and don't necessarily have to form a single path.
         Returns stocks ( Stock List[NXOp):  Array of stocks created .
        """
        pass
    def ConvertToStockAsComponents(self, convertSpaceReservartion: bool, nameType: ComponentName) -> None:
        """
          Converts a part file from Legacy Stock into Stock as Components.
                    Converts all stocks whose use is NXOpen.Routing.StockUse.LegacyStock into NXOpen.Routing.StockUse.StockAsComponent
                    stocks by creating components for each stock.  After calling this routine, all new stocks in this part will have components associated with them.  
        """
        pass
    def CreateStock(self, stock_data: StockData, anchor: Anchor, cross_section: CrossSection, segments: List[ISegment]) -> List[Stock]:
        """
         Creates a NXOpen.Routing.Stock object. 
         Returns stocks ( Stock List[NXOp):  The resulting array of newly created NXOpen.Routing.Stock
                                                    objects. .
        """
        pass
    def GetComponentStock(self, component: NXOpen.Assemblies.Component) -> Stock:
        """
         Returns the NXOpen.Routing.Stock that controls the given component.
                    Only returns a NXOpen.Routing.Stock if the input component is a component created
                    by a Stock as Components stock object. 
         Returns stock ( Stock NXOpen):  Returns  if the input component is not controlled
                                                    by a NXOpen.Routing.Stock .
        """
        pass
    def GetStockFromObject(self, objectValue: NXOpen.NXObject) -> Stock:
        """
         Returns the stock assigned to the Segment or attached to the
                    Stock Port or the stock associated with the Stock Solid feature. The
                    input may be a Port of a stock, a Segment, Stock Solid feature tag or a
                    Curve used to define the segment that is assigned the stock. If no
                    stock is assigned to the segment, returns .
                
         Returns stock ( Stock NXOpen): .
        """
        pass
    def RemoveAllFillerStocks(self, segments: List[ISegment]) -> None:
        """
         Removes all filler stocks from the input set of segments. 
        """
        pass
    def RemoveStock(self, segments: List[ISegment]) -> None:
        """
         Removes all stocks (excluding flexed stocks) from the input set of segments. 
        """
        pass
    def ResetReferenceStock(self) -> None:
        """
         Resets the reference NXOpen.Routing.Stock information to . The information
                    attributes are rotation, twist, negate, flip, port and anchor. They determine the default
                    creation options for the new stock. This information is used during path creation. 
        """
        pass
    def SetAttachedStockLength(self, part_occ: NXOpen.Assemblies.Component) -> None:
        """
         Set the length of the NXOpen.Routing.Stock to which a
                    NXOpen.Assemblies.Component object is attached. 
        """
        pass
    def SetReferenceStockFromObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Sets the reference NXOpen.Routing.Stock information based
                    on the NXOpen.Routing.Stock associated with this object. 
        """
        pass
    def UpdateBundleStockForFiller(self, segments: List[ISegment]) -> None:
        """
         Update the bundle stock if the NXOpen.Routing.Filler stock is created underneath it. 
        """
        pass
import NXOpen
class StockColorBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Routing.StockColorBuilder. This is used 
    to assign color to the face of stocks having rectangular cross section.
    """
    @property
    def RouteStockPickColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) RouteStockPickColor
         Returns the route stock pick color   
            
         
        """
        pass
    @RouteStockPickColor.setter
    def RouteStockPickColor(self, routeStockPickColor: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) RouteStockPickColor
         Returns the route stock pick color   
            
         
        """
        pass
    @property
    def RouteStockSelectStockFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) RouteStockSelectStockFace
         Returns the route stock select stock face   
            
         
        """
        pass
import NXOpen
class StockDataCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.StockData objects.  """
    @overload
    def CreateStockData(self, values: CharacteristicList) -> StockData:
        """
          Creates (or finds an existing NXOpen.Routing.StockData) object in the work
                  part that has the characteristics specified by the input list of characteristic values.  Creates
                  the stock by copying the stock defined in the qualified part to the work part. The qualified stock
                  part is specified by the PART_NAME or MEMBER_NAME in the list.  If there is no PART_NAME or MEMBER_NAME
                  a stock data, the OD or WIDTHHEIGHT values are used to generate either a circular or rectangular
                  stock data.  
                  
                    Use this routine to create stock data's in the work part in order to create stocks.  Use
                    Routing.RouteManager.PartTypeFlag to create a qualified
                    stock data part.  
                    
                    Example Use:
                    
                        values = theSession.Preferences.RoutingApplicationView.PartPreferences.PartLibrary.CreateCriteria ( );
                        values.SetCharacteristic ( "OD", 10.0 );
                        stock_data = workPart.RouteManager.StockDataCollection.CreateStockData ( values );
                        stocks = workPart.RouteManager.StockCollection.CreateStock ( stock_data, anchor, cross_section, segments );
                        workPart.RouteManager.SetPartTypeFlag( Routing.RouteManager.PartType.Stock );
                    
                  
                  
         Returns stock_data ( StockData NXOpen):  .
        """
        pass
    @overload
    def CreateStockData(self) -> StockData:
        """
         Creates a new stock data in the work part.  The new stock data contains all of the 
                 NXOpen.Routing.CrossSection and NXOpen.Routing.Anchor objects
                 in the work part.  After calling this routine call Routing.RouteManager.PartTypeFlag
                 to NXOpen.Routing.RouteManager.PartType.Stock, 
                 NXOpen.Routing.RouteManager.PartType.Overstock, or
                 NXOpen.Routing.RouteManager.PartType.Filler to properly qualify this
                 as a stock definition part.
                 
         Returns stock_data ( StockData NXOpen):  .
        """
        pass
    def LoadStockData(self, part_name: str, member_name: str, stock_style: StockStyle) -> Tuple[StockData, Anchor, CrossSection]:
        """
         Loads the NXOpen.Routing.StockData into the current part.
                    The NXOpen.Routing.StockData can be used to assign 
                    NXOpen.Routing.Stock to NXOpen.Routing.ISegments
                    using NXOpen.Routing.PathStockBuilder.
                    Once the stock has been "loaded", several calls to
                    NXOpen.Routing.PathStockBuilder may be made (for various segments)
                    without the need to "load" another.
                    The Assembly Search Directory list, specified via the load_options.def
                    file or interactively through the File --Options--Load Options dialog,
                    is used to locate the part file for the stock.
                
         Returns A tuple consisting of (stock_data, anchor, cross_section). 
         - stock_data is:  StockData NXOpen. The loaded NXOpen.Routing.StockData. .
         - anchor is:  Anchor NXOpen. The NXOpen.Routing.Anchor of the stock data. .
         - cross_section is:  CrossSection NXOpen. The NXOpen.Routing.CrossSection of the stock data. .

        """
        pass
    def RemoveUnusedStockData(self) -> None:
        """
         Logs for deletion any NXOpen.Routing.StockData objects in the
                 input part not referenced by any NXOpen.Routing.Stock, 
                 NXOpen.Routing.Wire and NXOpen.Routing.CrossSection
                 not referenced by any NXOpen.Routing.StockData.
                
        """
        pass
import NXOpen
class StockDataRefreshBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.StockDataRefreshBuilder
        Builder for updatingreloading routing stock data definitions. """
    class RefreshStatus(Enum):
        """
        Members Include: 
         |Ok|  Refresh successful 
         |StockDataTagInvalid|  NULL stock definition encountered 
         |StockDataMissingSearchAttributes|  No attributes used for searching library found 
         |StockPartNotFoundInReuseLibrary|  Cannot find stock under the stock or overstock root nodes in the Reuse Library 
         |MultipleStocksFoundInReuseLibrary|  More than one stock found - cannot resolve ambiguity 
         |StockPartNotRequired|  Stock part name not found indicating there is no stock part 
         |StockPartNotFoundForLoading|  Problem loading the stock part 
         |CannotFullyLoadStockPart|  Unable to fully load the stock part 
         |StockDataNotFoundInLoadedPart|  Unable to find a stock definition in the loaded stock part 
         |StockConversionError|  Error converting units of loaded stock part to that of stock definition being refreshed 
         |ErrorRefreshUndone|  Error encountered after partial update of stock definition; UNDO was performed to return to original state 

        """
        Ok: int
        StockDataTagInvalid: int
        StockDataMissingSearchAttributes: int
        StockPartNotFoundInReuseLibrary: int
        MultipleStocksFoundInReuseLibrary: int
        StockPartNotRequired: int
        StockPartNotFoundForLoading: int
        CannotFullyLoadStockPart: int
        StockDataNotFoundInLoadedPart: int
        StockConversionError: int
        ErrorRefreshUndone: int
        @staticmethod
        def ValueOf(value: int) -> StockDataRefreshBuilder.RefreshStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Status(self) -> StockDataRefreshBuilder.RefreshStatus:
        """
        Getter for property: ( StockDataRefreshBuilder.RefreshStatus NXOpen) Status
         Returns   
            
         
        """
        pass
    @property
    def StockData(self) -> StockData:
        """
        Getter for property: ( StockData NXOpen) StockData
         Returns   
            
         
        """
        pass
    @StockData.setter
    def StockData(self, stockData: StockData):
        """
        Setter for property: ( StockData NXOpen) StockData
         Returns   
            
         
        """
        pass
    def RefreshStockData(self, stockData: StockData) -> StockDataRefreshBuilder.RefreshStatus:
        """
         Update the Stock Data Definition
                    Requires an update to be applied after call. 
         Returns status ( StockDataRefreshBuilder.RefreshStatus NXOpen): .
        """
        pass
class StockDataType(Enum):
    """
    Members Include: 
     |NotBundled|  Not generated (or used ) by bundling. 
     |Bundled|  Generated (or used ) by bundling. 

    """
    NotBundled: int
    Bundled: int
    @staticmethod
    def ValueOf(value: int) -> StockDataType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class StockData(NXOpen.NXObject): 
    """ A NXOpen.Routing.StockData contains the various profiles, characteristic information, 
        NXOpen.Routing.Anchor and other attributes that define NXOpen.Routing.Stock 
        objects. Each NXOpen.Routing.Stock has exactly one NXOpen.Routing.StockData
        associated with it.  All NXOpen.Routing.CrossSection and NXOpen.Routing.Anchor
        objects used in a NXOpen.Routing.Stock object must come from the 
        NXOpen.Routing.StockData associated with that NXOpen.Routing.Stock object.
      """
    def GetAnchors(self) -> List[Anchor]:
        """
         Gets the list of NXOpen.Routing.Anchor objects associated with this
                    NXOpen.Routing.StockData.  There should be no more than one NXOpen.Routing.Anchor
                    with the same name. 
         Returns anchors ( Anchor List[NXOp):  The list of NXOpen.Routing.Anchor objects.   .
        """
        pass
    def GetBundledStockDatas(self) -> List[StockData]:
        """
         Returns all of the NXOpen.Routing.StockData that were used to build this object 
                   by the bundling algorithm.  Only returns valid output if 
                   NXOpen.Routing.StockData.GetIsBundled returns 
                   Routing.StockDataType.Bundled.
                   
         Returns stock_datas ( StockData List[NXOp):  .
        """
        pass
    def GetCrossSections(self) -> List[CrossSection]:
        """
         Gets the list of NXOpen.Routing.CrossSection objects associated with this
                    NXOpen.Routing.StockData.  There should be no more than one 
                    NXOpen.Routing.CrossSection of any particular NXOpen.Routing.StockStyle 
                    (and no NXOpen.Routing.CrossSection with a style of 
                    NXOpen.Routing.StockStyle.None). 
         Returns cross_sections ( CrossSection List[NXOp):  The list of NXOpen.Routing.CrossSection objects.   .
        """
        pass
    def GetIsBundled(self) -> StockDataType:
        """
         Returns whether or not the NXOpen.Routing.StockData is used in
                    the bundling of wires or not.  
         Returns is_bundled ( StockDataType NXOpen):  .
        """
        pass
    def GetNamedAnchor(self, anchor_name: str) -> Anchor:
        """
         Returns the NXOpen.Routing.Anchor which is part of the 
                     Routing.StockData, given the anchors name. 
         Returns anchor ( Anchor NXOpen):  .
        """
        pass
    def GetStocks(self) -> List[Stock]:
        """
         Returns all of the NXOpen.Routing.Stock objects that use this 
                  NXOpen.Routing.StockData object. 
         Returns stocks ( Stock List[NXOp):  .
        """
        pass
    def GetStyledCross(self, stock_style: StockStyle) -> CrossSection:
        """
         Returns the NXOpen.Routing.CrossSection which is part of the 
                    Routing.StockData, given the cross section style. 
         Returns cross_section ( CrossSection NXOpen):  .
        """
        pass
    def SetAnchors(self, anchors: List[Anchor]) -> None:
        """
         Sets the list of NXOpen.Routing.Anchor objects associated with this
                    NXOpen.Routing.StockData.  There should be no more than one NXOpen.Routing.Anchor
                    with the same name. 
        """
        pass
    def SetCrossSections(self, cross_sections: List[CrossSection]) -> None:
        """
         Sets the list of NXOpen.Routing.CrossSection objects associated with this
                    NXOpen.Routing.StockData.  There should be no more than one NXOpen.Routing.CrossSection
                    of any particular NXOpen.Routing.StockStyle (and no NXOpen.Routing.CrossSection 
                    with a style of NXOpen.Routing.StockStyle.None). 
        """
        pass
class StockDefinition(ItemDefinition): 
    """ Represents Routing StockDefinition object """
    @property
    def OuterDiameter(self) -> float:
        """
        Getter for property: (float) OuterDiameter
         Returns the outer diameter   
            
         
        """
        pass
    @OuterDiameter.setter
    def OuterDiameter(self, diameter: float):
        """
        Setter for property: (float) OuterDiameter
         Returns the outer diameter   
            
         
        """
        pass
import NXOpen
class StockDevice(SingleDevice): 
    """ 
        The Routing StockDevice corresponds to a generic stock instance 
        of Routing.SingleDevice.
    """
    @property
    def StockDefinition(self) -> StockDefinition:
        """
        Getter for property: ( StockDefinition NXOpen) StockDefinition
         Returns the stock definition.  
             
         
        """
        pass
    @StockDefinition.setter
    def StockDefinition(self, route_stock_definition: StockDefinition):
        """
        Setter for property: ( StockDefinition NXOpen) StockDefinition
         Returns the stock definition.  
             
         
        """
        pass
    @property
    def StockLength(self) -> float:
        """
        Getter for property: (float) StockLength
         Returns the stock length.  
             
         
        """
        pass
    @StockLength.setter
    def StockLength(self, stock_length: float):
        """
        Setter for property: (float) StockLength
         Returns the stock length.  
             
         
        """
        pass
    def LogStockDeviceWiresforConcurrency(self, partTag: NXOpen.Part) -> None:
        """
         Log stock device's wire and its segment for concurrency 
        """
        pass
import NXOpen
class StockOffsetPointBuilder(NXOpen.Builder): 
    """ Applies Assemblies Constraints to a selected NXOpen.Point or 
        NXOpen.Routing.ControlPoint to mimic the updatemove behavior of
        the input smart NXOpen.Point.    The smart point may be a Routing
        stock offset point (see NXOpen.PointCollection.CreateStockOffsetPoint) or
        any of the points created using the NXOpen.PointCollection class.  
    """
    class PointType(Enum):
        """
        Members Include: 
         |Normal|  Normal smart point. 
         |StockOffset|  Routing stock offset point. 

        """
        Normal: int
        StockOffset: int
        @staticmethod
        def ValueOf(value: int) -> StockOffsetPointBuilder.PointType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ConstraintPoint
         Returns the point that defines the location of the selected point.  
            On commit, this
                    point is used for determining the set of Assemblies Constraints to apply to the
                    selected point (or Routing control point).  The input point itself is not used
                    after the commit method.    
         
        """
        pass
    @ConstraintPoint.setter
    def ConstraintPoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ConstraintPoint
         Returns the point that defines the location of the selected point.  
            On commit, this
                    point is used for determining the set of Assemblies Constraints to apply to the
                    selected point (or Routing control point).  The input point itself is not used
                    after the commit method.    
         
        """
        pass
    @property
    def PointSelection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) PointSelection
         Returns the point selection.  
            Stores the point or Routing control point selected by the user.   
         
        """
        pass
    def GetPointData(self) -> Tuple[StockOffsetPointBuilder.PointType, NXOpen.Point, NXOpen.Direction, str]:
        """
         Gets the stock offset data from the currently selected point or routing
                    control point. 
         Returns A tuple consisting of (point_type, base_point, offset_dir, offset_expression). 
         - point_type is:  StockOffsetPointBuilder.PointType NXOpen. Type of point currently defined. .
         - base_point is:  NXOpen.Point. Base point for stock offset points,  for
        Routing.StockOffsetPointBuilder.PointType.Normal points. .
         - offset_dir is:  NXOpen.Direction. Offset direction for stock offset points,  for
        Routing.StockOffsetPointBuilder.PointType.Normal points. .
         - offset_expression is: str. Offset expression for stock offset points,  for
        Routing.StockOffsetPointBuilder.PointType.Normal points. .

        """
        pass
    def GetStockOffsetPointObject(self) -> NXOpen.TaggedObject:
        """
         Gets the object on which a Stock Offset Point was based.
                    Returns  if the point is not a Stock Offset Point or if the 
                    Stock Offset Point was not offset from another object. 
         Returns offsetObject ( NXOpen.TaggedObject): .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class StockOffsetPortCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of NXOpen.Routing.StockOffsetPort objects. """
    def CreateStockOffsetPort(self, partOccurrence: NXOpen.Assemblies.Component, portPrototype: Port) -> StockOffsetPort:
        """
         Creates a NXOpen.Routing.StockOffsetPort in the work part from the
                    stock offset port in the given part occurrence. Returns the existing stock offset
                    port in the work part if one already exists. 
         Returns stockOffsetPort ( StockOffsetPort NXOpen):  The stock offset port in the work part. .
        """
        pass
class StockOffsetPort(Port): 
    """ NXOpen.Routing.StockOffsetPort class handles the relationship
        between a component part's port occurrence and the dumb offset port in
        the work part. The dumb port offsets based on expressions that use
        the stock diameter. """
    def GetMaxPathStockDiameter(self) -> float:
        """
         Returns the diameter of all the stock on the path at this NXOpen.Routing.StockOffsetPort.
                NOTE: This value may change in the next update cycle. 
         Returns diameter (float): .
        """
        pass
    def GetOffsetPort(self) -> Port:
        """
         Returns the NXOpen.Routing.StockOffsetPort in the work part that was created from the original port occurrence. 
         Returns offsetPort ( Port NXOpen): .
        """
        pass
    def GetPortOccurrence(self) -> Port:
        """
         Returns the original port occurrence from which the dumb port was extracted.
                    Returns  if the occurrence is not available because it is not loaded, or not in the current reference set, etc. 
         Returns portOccurrence ( Port NXOpen): .
        """
        pass
import NXOpen
class StockPartConverterBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.StockPartConverterBuilder
        Builder for Part Conversion of the stocks.
        This also provides an option to Recreate stock components during part conversion."""
    class PartOption(Enum):
        """
        Members Include: 
         |WorkPart|  Upgrades stocks from the work part only 
         |WorkPartWithLoadedChildren|  Upgraded stocks from work part as well loaded children parts 

        """
        WorkPart: int
        WorkPartWithLoadedChildren: int
        @staticmethod
        def ValueOf(value: int) -> StockPartConverterBuilder.PartOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConvertWorkPartAndLoadedChildrenOption(self) -> StockPartConverterBuilder.PartOption:
        """
        Getter for property: ( StockPartConverterBuilder.PartOption NXOpen) ConvertWorkPartAndLoadedChildrenOption
         Returns the convert workpart and loaded children option.  
           Returns if the stocks from only the work part or from the work part and loaded children have to be converted during part conversion.  
         
        """
        pass
    @ConvertWorkPartAndLoadedChildrenOption.setter
    def ConvertWorkPartAndLoadedChildrenOption(self, conversionOption: StockPartConverterBuilder.PartOption):
        """
        Setter for property: ( StockPartConverterBuilder.PartOption NXOpen) ConvertWorkPartAndLoadedChildrenOption
         Returns the convert workpart and loaded children option.  
           Returns if the stocks from only the work part or from the work part and loaded children have to be converted during part conversion.  
         
        """
        pass
    @property
    def RecreateStockComponentsOption(self) -> bool:
        """
        Getter for property: (bool) RecreateStockComponentsOption
         Returns the recreate StockComponents option.  
           Returns true if the stock components have to be recreated during part conversion.  
         
        """
        pass
    @RecreateStockComponentsOption.setter
    def RecreateStockComponentsOption(self, recreateStockComponentsOption: bool):
        """
        Setter for property: (bool) RecreateStockComponentsOption
         Returns the recreate StockComponents option.  
           Returns true if the stock components have to be recreated during part conversion.  
         
        """
        pass
class StockPort(Port): 
    """ NXOpen.Routing.StockPort objects are automatically created and updated by
      NXOpen.Routing.Stock objects. """
    def GetExtractPort(self) -> ExtractPort:
        """
         For Stock As Components, returns the NXOpen.Routing.ExtractPort
                    of this NXOpen.Routing.StockPort using the NXOpen.Routing.StockPort's
                    occurrence in the work part. Returns  if the given NXOpen.Routing.StockPort
                    does not have a port occurrence in the work part. 
         Returns extract_port ( ExtractPort NXOpen):  Extract port that represents the occurrence of
                                                                                        the NXOpen.Routing.StockPort in the work part. .
        """
        pass
    def GetStock(self) -> Stock:
        """
         Gets the NXOpen.Routing.Stock that owns this object.  
         Returns stock ( Stock NXOpen):  .
        """
        pass
import NXOpen
class StockStyleBuilder(NXOpen.Builder): 
    """ Builder class to assigns style to the selected stock . """
    class StockStyle(Enum):
        """
        Members Include: 
         |Centerline|  
         |SimpleSolid|  
         |DetailedSolid|  

        """
        Centerline: int
        SimpleSolid: int
        DetailedSolid: int
        @staticmethod
        def ValueOf(value: int) -> StockStyleBuilder.StockStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnumStockStyle(self) -> StockStyleBuilder.StockStyle:
        """
        Getter for property: ( StockStyleBuilder.StockStyle NXOpen) EnumStockStyle
         Returns the enum for setting stock style   
            
         
        """
        pass
    @EnumStockStyle.setter
    def EnumStockStyle(self, enumStockStyle: StockStyleBuilder.StockStyle):
        """
        Setter for property: ( StockStyleBuilder.StockStyle NXOpen) EnumStockStyle
         Returns the enum for setting stock style   
            
         
        """
        pass
    @property
    def RouteSelectionStock(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteSelectionStock
         Returns the route selection stock for selecting routing objects  
            
         
        """
        pass
class StockStyle(Enum):
    """
    Members Include: 
     |NotSet|  No profile. 
     |Simple|  Simple profile. 
     |Detailed|  Detailed profile. 

    """
    NotSet: int
    Simple: int
    Detailed: int
    @staticmethod
    def ValueOf(value: int) -> StockStyle:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class StockTransitionBuilder(NXOpen.Builder): 
    """ 
        Builder for creatingediting stockTransition. 
        
        Create StockTransition: Takes a set of segments and assign characteristics of the selected stock
        to the segments.
        
         
        Edit Stock: Takes in the selected stockTransition to edit as input and redefines
        the stockTransition with the new settings.
        
    """
    @property
    def EndProfileOriginCurve(self) -> NXOpen.SelectCurve:
        """
        Getter for property: ( NXOpen.SelectCurve) EndProfileOriginCurve
         Returns the origin curve of end profile   
            
         
        """
        pass
    @property
    def EndProfileOriginCurveDirection(self) -> bool:
        """
        Getter for property: (bool) EndProfileOriginCurveDirection
         Returns the direction of origin curve of end profile   
            
         
        """
        pass
    @EndProfileOriginCurveDirection.setter
    def EndProfileOriginCurveDirection(self, endProfileOriginCurveDirection: bool):
        """
        Setter for property: (bool) EndProfileOriginCurveDirection
         Returns the direction of origin curve of end profile   
            
         
        """
        pass
    @property
    def SegmentCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) SegmentCollector
         Returns the segment collector   
            
         
        """
        pass
    @property
    def StartProfileOriginCurve(self) -> NXOpen.SelectCurve:
        """
        Getter for property: ( NXOpen.SelectCurve) StartProfileOriginCurve
         Returns the origin curve of start profile   
            
         
        """
        pass
    @property
    def StartProfileOriginCurveDirection(self) -> bool:
        """
        Getter for property: (bool) StartProfileOriginCurveDirection
         Returns the direction of origin curve of start profile   
            
         
        """
        pass
    @StartProfileOriginCurveDirection.setter
    def StartProfileOriginCurveDirection(self, startProfileOriginCurveDirection: bool):
        """
        Setter for property: (bool) StartProfileOriginCurveDirection
         Returns the direction of origin curve of start profile   
            
         
        """
        pass
    @property
    def StockSettings(self) -> PathStockBuilder:
        """
        Getter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for stock assignment.  
             
         
        """
        pass
    @StockSettings.setter
    def StockSettings(self, pathStockBuilder: PathStockBuilder):
        """
        Setter for property: ( PathStockBuilder NXOpen) StockSettings
         Returns the stock settings for stock assignment.  
             
         
        """
        pass
    def SetStockTransitionProperties(self) -> None:
        """
         
        """
        pass
class StockTransition(Stock): 
    """ Represents NXOpen.Routing.StockTransition object. NXOpen.Routing.StockTransition covers C1 continuous NXOpen.Routing.ISegment 
    in between two stocks. It acts as transition from NXOpen.Routing.CrossSection of one NXOpen.Routing.Stock to another. 
    When two different NXOpen.Routing.Stock are connected with set of segments, then a stockTransition can be used to cover
    it in such a way that NXOpen.Routing.CrossSection at each end of this segments matches with the stock at that location.
    These segments can be a routing path, or just a collection of segments.
    NXOpen.Routing.Stock covers segments, and NXOpen.Routing.StockTransition inherits
    that behavior.  However, NXOpen.Routing.StockTransition refers to two end NXOpen.Routing.Stock and the NXOpen.Routing.CrossSection
    of NXOpen.Routing.StockTransition object varies from one end to another.   """
    pass
class StockType(Enum):
    """
    Members Include: 
     |Unknown|  Unknown overstock type 
     |FixedCrossSection|  Fixed cross section, e.g., conduit 
     |Wrapped|  Wrapped, e.g., electrical tape 
     |Sleeved|  Sleeved, e.g., woven nylon 
     |Flagged|  Flagged, e.g., paper flag 

    """
    Unknown: int
    FixedCrossSection: int
    Wrapped: int
    Sleeved: int
    Flagged: int
    @staticmethod
    def ValueOf(value: int) -> StockType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
class StockUse(Enum):
    """
    Members Include: 
     |LegacyStock|  Normal Legacy Stock. 
     |Bundled|  Legacy Stock that was generated by the bundling algorithm 
     |StockAsComponent|  Stock as Component stock in the work part. 
     |StockInComponent|  Stock as Component stock in the component part. User
                                                                should not modify this stock.  
     |Deformed|  Stock has been deformed using the "Deform Component"
                                                                functionality.  User should not modify this stock. 

    """
    LegacyStock: int
    Bundled: int
    StockAsComponent: int
    StockInComponent: int
    Deformed: int
    @staticmethod
    def ValueOf(value: int) -> StockUse:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Features
import NXOpen.Routing.Electrical
class Stock(NXOpen.NXObject): 
    """

            The NXOpen.Routing.Stock object represents a material (such as as pipe or tube)
            that covers a path of segments.  The material is defined in the NXOpen.Routing.StockData
            object.  NXOpen.Routing.Stock consists of a NXOpen.Routing.StockData
            object, as well as references to at most one of the NXOpen.Routing.CrossSection and
            NXOpen.Routing.Anchor objects that are associated with that
            NXOpen.Routing.StockData.

        
            A NXOpen.Routing.Stock object may exist in one of two modes ; Legacy Stock or
            Stock as Components Stock.  Legacy Stock is modeled as a sweep feature in the work part.  Stock
            as Components Stock is modeled as a child component (of the work part) that contains a sweep
            feature.  Legacy Stock and Stock as Components stock cannot exist in the same part file with
            the exception of Bundled stock.
        
            Stock as Components Stock creates a component file, and creates a copy of itself inside of
            that part file.  Segments, anchors, and all other necessary information are copied into
            the component part file.  The stock inside of the component file should not be edited or
            modified as it is completely controlled by the Stock as Component Stock in the work part.
        
        
            NXOpen.Routing.Stock object that have automatically been generated by the bundling
            algorithm used for routing wires are Bundled stock.  Bundled stocks are always created as
            Legacy Stocks (even in parts containing Stock as Component stocks).  Any NXOpen.Routing.StockData
             object that defines a bundled stock has a type of Routing.StockDataType.Bundled
            .  Editing the segments or the stock data of a Bundled stock may result in undefined
            behavior.
        
            With the exception of stock style, there are no functional differences between the two
            stock types.  Stock as Components Stock always uses the NXOpen.Routing.StockStyle.Detailed
            style (if available, otherwise it uses the NXOpen.Routing.StockStyle.Simple style) and
            the stock's style cannot be changed.
        
     """
    @property
    def Diameter(self) -> float:
        """
        Getter for property: (float) Diameter
         Returns the diameter of this stock.  
             
         
        """
        pass
    @property
    def NegateOffsetsFlag(self) -> bool:
        """
        Getter for property: (bool) NegateOffsetsFlag
         Returns the negate offsets flag of this  NXOpen::Routing::Stock .  
             
         
        """
        pass
    @NegateOffsetsFlag.setter
    def NegateOffsetsFlag(self, offset_flag: bool):
        """
        Setter for property: (bool) NegateOffsetsFlag
         Returns the negate offsets flag of this  NXOpen::Routing::Stock .  
             
         
        """
        pass
    def AddSegments(self, segments: List[NXOpen.Curve]) -> None:
        """
         Adds new segments to this object.  If the new segments (added to the old segments) do not form
                   a single continuous path, the NXOpen.Routing.Stock will split so that there is a
                   copy of this object on each continuous path formed by the input segments. 
        """
        pass
    def AlignStock(self, vector: NXOpen.Vector3d) -> None:
        """
         Align stock to new rotation vector. 
        """
        pass
    def ColorBodies(self) -> None:
        """
         Colors the solid bodies of the stock based on the COLOR characteristic specified in the
                    NXOpen.Routing.StockData of the stock.  The color string can contain
                    the name of a color, a hex string specifying the RGB values, a comma separated list of RGB integer values and
                    a simple integer specifying the color index directly. 
        """
        pass
    def ConnectStockComponentWithAssemblyPath(self) -> bool:
        """
          If the stock components are disconnected from the path in the assembly this method will connect them again with the path.  
         Returns wasDisconnected (bool):  True if stock component was disconnected from the assembly path and connection has been restored. False otherwise. .
        """
        pass
    def FixCrossSectionInvalidities(self) -> bool:
        """
         If the stock has cross section invalidities this function corrects those. If the invalidity is fixed, the stock needs needs to be logged for update and update should 
                    be triggered. 
         Returns invalidityFoundAndFixed (bool):  Return true if the invalidity was found and fixed. .
        """
        pass
    def GetAnchor(self) -> Anchor:
        """
         Gets the NXOpen.Routing.Anchor that currently modifies the profile for the stock.  
         Returns anchor ( Anchor NXOpen):  Returns  if this object isn't using an NXOpen.Routing.Anchor
                                               .
        """
        pass
    def GetBodies(self) -> List[NXOpen.Body]:
        """
         Returns the solid bodies, if any, that are created and controlled by this object.  For
                  Stock as Components stock, the bodies exist in a separate part file.  For Legacy Stock
                  the bodies exist in the same part as the input object.  
         Returns bodies ( NXOpen.Body Li):  .
        """
        pass
    def GetBodySegmentMap(self, feature: NXOpen.Features.Feature) -> Tuple[NXOpen.Body, List[NXOpen.Curve], List[NXOpen.Curve]]:
        """
         Given stock and a feature of the stock, returns solid body, stock segments and path segments that produced the body.
                    Path segments are the visible segments over which the stock is created. Stock segments may be same as the 
                    path segments or those may be hidden segments created for the stock. In case of NXOpen.Routing.Overstock
                    stockSegments are hidden and path segments are visible. There may be many stock segments created on a single path segment in
                    that case. 
                    Usage: 1. Query features for a stock. If an overstock is applied on a path with a sharp corner, it may have created multiple features.
                           2.Call this method for every feature in a loop. 
         Returns A tuple consisting of (body, stockSegments, pathSegments). 
         - body is:  NXOpen.Body. Solid body of the stock sweep. .
         - stockSegments is:  NXOpen.Curve Li. Stock segments. Hidden segments in case of overstocks. .
         - pathSegments is:  NXOpen.Curve Li. Path segments. Same as stock segments for stock but visible path segments for overstock. .

        """
        pass
    def GetComponent(self) -> NXOpen.Assemblies.Component:
        """
         Returns the NXOpen.Assemblies.Component created and controlled by the stock for a
                   Stock as Components stock.  Only returns a component if the stock type is
                   Routing.StockUse.StockAsComponent. 
         Returns component ( NXOpen.Assemblies.Component):  .
        """
        pass
    def GetConnections(self) -> List[NXOpen.Routing.Electrical.Connection]:
        """
         Returns the electrical connections this stock represents, if any. 
         Returns connections ( NXOpen.Routing.Electrical.Connection Li):  .
        """
        pass
    def GetCrossSection(self) -> CrossSection:
        """
         Gets the NXOpen.Routing.CrossSection that currently defines the profile for the stock.  
         Returns cross_section ( CrossSection NXOpen):  Returns  if this object is using stock style 
                                                     Routing.StockStyle.None .
        """
        pass
    def GetFeatures(self) -> List[NXOpen.Features.Feature]:
        """
         Returns the sweep features that are created and controlled by this object.  For
                  Stock as Components stock, the features exist in a separate part file.  For Legacy Stock
                  the features exist in the same part as the input object.  
         Returns features ( NXOpen.Features.Feature Li):  Sweep features.  .
        """
        pass
    def GetFlippedStatus(self) -> Flip:
        """
         Gets whether or not the profile is flipped. 
         Returns flipped ( Flip NXOpen):   .
        """
        pass
    def GetHarnessDevice(self) -> NXOpen.Routing.Electrical.HarnessDevice:
        """
         For Routing Electrical application only, returns the Routing.Electrical.HarnessDevice
                    that owns the wire or wires that make up a stock bundle.
                    Will return  if this stock is not a wire, cable, or shield bundle.
                
         Returns harnessDevice ( NXOpen.Routing.Electrical.HarnessDevice):  .
        """
        pass
    def GetNameStatus(self) -> ComponentName:
        """
         Returns whether or not the component associated with a Stock as Components Stock has a
                    permanent or temporary name. 
         Returns status ( ComponentName NXOpen):  .
        """
        pass
    def GetOriginalLength(self) -> float:
        """
         Returns the original length for a stock that has been deformed (it's use is
                  Routing.StockUse.Deformed).  This is the length of the original stock
                  in the component part at the time that the deformed stock was created. 
         Returns length (float):  The original length in units of the original part file. .
        """
        pass
    def GetPorts(self) -> Tuple[StockPort, StockPort]:
        """
         Returns the NXOpen.Routing.StockPort at each end of the stock. 
         Returns A tuple consisting of (start_port, end_port). 
         - start_port is:  StockPort NXOpen. Port at the start of the first segment. .
         - end_port is:  StockPort NXOpen. Port at the end of the last segment. .

        """
        pass
    def GetProfileEnd(self) -> ProfileFrom:
        """
         Gets the end that defines profile.  
         Returns profile_end ( ProfileFrom NXOpen):   .
        """
        pass
    def GetRotationAngle(self) -> float:
        """
         Gets the rotation angle applied to the profile.  
         Returns rotation_angle (float):  The angle in radians. .
        """
        pass
    def GetRotationVector(self) -> NXOpen.Vector3d:
        """
         Returns the rotation vector showing how the stock is rotated from it's "up" direction.
                    Only useful for non-circular stocks.
                
         Returns anchorSegDir ( NXOpen.Vector3d): .
        """
        pass
    def GetSegments(self) -> List[NXOpen.Curve]:
        """
         Gets the segments that the NXOpen.Routing.Stock object is placed on top of. 
         Returns segments ( NXOpen.Curve Li):   .
        """
        pass
    def GetStockData(self) -> StockData:
        """
         Gets the NXOpen.Routing.StockData.  
         Returns stock_data ( StockData NXOpen):  .
        """
        pass
    def GetStockStyle(self) -> StockStyle:
        """
         Gets the NXOpen.Routing.StockStyle of the NXOpen.Routing.Stock. 
         Returns style ( StockStyle NXOpen):  .
        """
        pass
    def GetStockUse(self) -> StockUse:
        """
         Returns the use of the stock. 
         Returns use ( StockUse NXOpen):  .
        """
        pass
    def GetTwistAngle(self) -> float:
        """
         Gets the twist angle applied to the profile.  
         Returns twist_angle (float):  The angle in radians. .
        """
        pass
    def GetWires(self) -> List[Wire]:
        """
         Returns the electrical wires this stock represents, if any. 
         Returns wires ( Wire List[NXOp):  .
        """
        pass
    def Highlight(self) -> None:
        """
         Highlights the bodies of the stock, if any. If the stock is in centerline mode, there
                    are no bodies to highlight. 
        """
        pass
    def IsSpaceReservation(self) -> bool:
        """
         Is this stock a Space Reservation stock?.
                
         Returns isSpaceReservation (bool):  .
        """
        pass
    def IsStockEqual(self, otherStock: Stock) -> bool:
        """
         Tests whether two stock objects are equivalent.  Two stock objects are
                    equivalent if they reference the same stock data, the same anchor, and
                    all characteristic values are equal. 
         Returns isEqual (bool):  Is this stock the same as the given stock? .
        """
        pass
    def RemoveSegments(self, segments: List[NXOpen.Curve]) -> None:
        """
         Removes segments from this object.  If the segments of this object (after removing the input
                   segments) do not form a single continuous path, the NXOpen.Routing.Stock will split so
                   that there is a copy of this object on each continuous path.   This object will delete itself inside of
                   update if all segments are removed. 
        """
        pass
    def RenameStockComponent(self, partName: str) -> None:
        """
         Renames the stock component part with given name
        """
        pass
    def SetAnchor(self, anchor: Anchor) -> None:
        """
         Sets the NXOpen.Routing.Anchor. The given object must be one of the
                    NXOpen.Routing.Anchor objects referenced by the NXOpen.Routing.StockData
                    object that defines this NXOpen.Routing.Stock object. 
        """
        pass
    def SetCrossSection(self, cross_section: CrossSection) -> None:
        """
         Sets the NXOpen.Routing.CrossSection. The given object must be one of the
                    NXOpen.Routing.CrossSection objects referenced by the NXOpen.Routing.StockData
                    object that defines this NXOpen.Routing.Stock object.  NXOpen.Routing.Stock.SetStockStyle
                     should be used (when possible) instead of this routine.  
        """
        pass
    def SetFlippedStatus(self, flipped: Flip) -> None:
        """
         Sets whether or not the profile is flipped. See the user help documentation on
                    Orient Stock for more information.
        """
        pass
    def SetProfileEnd(self, profile_end: ProfileFrom) -> None:
        """
         Sets the end that defines profile.  See the user help documentation on
                    Orient Stock for more information.
        """
        pass
    def SetRotationAngle(self, rotation_angle: float) -> None:
        """
         Sets the rotation angle applied to the profile.  See the user help documentation on
                    Orient Stock for more information.  
        """
        pass
    def SetStockData(self, stock_data: StockData) -> None:
        """
         Sets the NXOpen.Routing.StockData. After setting the StockData, the
                    caller must also make sure to set the CrossSection and Anchor so that the NXOpen.Routing.Stock
                    object only references objects associated with this NXOpen.Routing.StockData object.
        """
        pass
    def SetStockStyle(self, style: StockStyle) -> None:
        """
         Sets the NXOpen.Routing.StockStyle of the NXOpen.Routing.Stock. This may
                    cause update to fire, and can be a time-consuming operation as it may require the building of a
                    new sweep feature.  When style is set to NXOpen.Routing.StockStyle.None this routine
                    deletes the stock sweep feature.  Only call on Legacy Stocks. 
        """
        pass
    def SetTwistAngle(self, twist_angle: float) -> None:
        """
         Sets the twist angle applied to the profile.  See the user help documentation on
                    Orient Stock for more information.  
        """
        pass
    def SyncComponentAttrs(self, is_new_part: bool) -> None:
        """
         Set the characteristics of the given stock's
                    component so that it has the same characteristics as the NXOpen.Routing.Stock and its stock data. 
        """
        pass
    def Unhighlight(self) -> None:
        """
         Unhighlights the bodies of the stock, if any. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SubdivideSegmentBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.Routing.SubdivideSegmentBuilder. This is used 
    to subidivide a given segment into two or more segments based on one of the three
    spacing methods.
    """
    class EqualSegmentsMethod(Enum):
        """
        Members Include: 
         |EqualArcLength|  Equal Arc Length 
         |EqualParameter|  Equal Parameter 

        """
        EqualArcLength: int
        EqualParameter: int
        @staticmethod
        def ValueOf(value: int) -> SubdivideSegmentBuilder.EqualSegmentsMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Types(Enum):
        """
        Members Include: 
         |AtPoint|  At Point 
         |EqualSegments|  Equal Segments 
         |ArcLengthSegments|  Arc Length Segments 

        """
        AtPoint: int
        EqualSegments: int
        ArcLengthSegments: int
        @staticmethod
        def ValueOf(value: int) -> SubdivideSegmentBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EqualSegmentsOption(self) -> SubdivideSegmentBuilder.EqualSegmentsMethod:
        """
        Getter for property: ( SubdivideSegmentBuilder.EqualSegmentsMethod NXOpen) EqualSegmentsOption
         Returns the equal segments option as  NXOpen::Routing::SubdivideSegmentBuilder::EqualSegmentsMethod   
            
         
        """
        pass
    @EqualSegmentsOption.setter
    def EqualSegmentsOption(self, equalSegmentsOption: SubdivideSegmentBuilder.EqualSegmentsMethod):
        """
        Setter for property: ( SubdivideSegmentBuilder.EqualSegmentsMethod NXOpen) EqualSegmentsOption
         Returns the equal segments option as  NXOpen::Routing::SubdivideSegmentBuilder::EqualSegmentsMethod   
            
         
        """
        pass
    @property
    def ReverseSubdividePoint(self) -> bool:
        """
        Getter for property: (bool) ReverseSubdividePoint
         Returns the direction of the start of segment to subdivide.  
           The distance of the subdivision 
                    point on the segment is measured from this end.
                  
         
        """
        pass
    @ReverseSubdividePoint.setter
    def ReverseSubdividePoint(self, reverseSubdividePoint: bool):
        """
        Setter for property: (bool) ReverseSubdividePoint
         Returns the direction of the start of segment to subdivide.  
           The distance of the subdivision 
                    point on the segment is measured from this end.
                  
         
        """
        pass
    @property
    def Segment(self) -> SelectISegment:
        """
        Getter for property: ( SelectISegment NXOpen) Segment
         Returns the segment to subdivide   
            
         
        """
        pass
    @property
    def SubdivideArcLength(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) SubdivideArcLength
         Returns the arc length of each resulting segment from subdivision, if  NXOpen::Routing::SubdivideSegmentBuilder::Types  is 
                     NXOpen::Routing::SubdivideSegmentBuilder::TypesArcLengthSegments 
                  
            
         
        """
        pass
    @property
    def SubdivideEndPercentage(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) SubdivideEndPercentage
         Returns the end location of subdivision on the segment as percentage, if
                     NXOpen::Routing::SubdivideSegmentBuilder::Types  is  NXOpen::Routing::SubdivideSegmentBuilder::TypesEqualSegments 
                    or  NXOpen::Routing::SubdivideSegmentBuilder::TypesArcLengthSegments 
                  
            
         
        """
        pass
    @property
    def SubdivideNumSegments(self) -> int:
        """
        Getter for property: (int) SubdivideNumSegments
         Returns the number of subdivisions to do on the given segment, if  NXOpen::Routing::SubdivideSegmentBuilder::Types  
                    is  NXOpen::Routing::SubdivideSegmentBuilder::TypesEqualSegments 
                    or  NXOpen::Routing::SubdivideSegmentBuilder::TypesArcLengthSegments 
                  
            
         
        """
        pass
    @SubdivideNumSegments.setter
    def SubdivideNumSegments(self, subdivideNumSegments: int):
        """
        Setter for property: (int) SubdivideNumSegments
         Returns the number of subdivisions to do on the given segment, if  NXOpen::Routing::SubdivideSegmentBuilder::Types  
                    is  NXOpen::Routing::SubdivideSegmentBuilder::TypesEqualSegments 
                    or  NXOpen::Routing::SubdivideSegmentBuilder::TypesArcLengthSegments 
                  
            
         
        """
        pass
    @property
    def SubdividePoint(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) SubdividePoint
         Returns the location of the subdivision point on segment as arclength or %arclength or point, if
                     NXOpen::Routing::SubdivideSegmentBuilder::Types  is  NXOpen::Routing::SubdivideSegmentBuilder::TypesAtPoint 
                  
            
         
        """
        pass
    @property
    def SubdivideStartPercentage(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) SubdivideStartPercentage
         Returns the start location of subdivision on the segment as percentage, if
                     NXOpen::Routing::SubdivideSegmentBuilder::Types  is  NXOpen::Routing::SubdivideSegmentBuilder::TypesEqualSegments 
                    or  NXOpen::Routing::SubdivideSegmentBuilder::TypesArcLengthSegments 
                  
            
         
        """
        pass
    @property
    def Type(self) -> SubdivideSegmentBuilder.Types:
        """
        Getter for property: ( SubdivideSegmentBuilder.Types NXOpen) Type
         Returns the spacing method as  NXOpen::Routing::SubdivideSegmentBuilder::Types    
            
         
        """
        pass
    @Type.setter
    def Type(self, type: SubdivideSegmentBuilder.Types):
        """
        Setter for property: ( SubdivideSegmentBuilder.Types NXOpen) Type
         Returns the spacing method as  NXOpen::Routing::SubdivideSegmentBuilder::Types    
            
         
        """
        pass
    @overload
    def GetSplineSettings(self) -> Tuple[bool, bool]:
        """
         Gets the current subdivide spline settings. 
         Returns A tuple consisting of (createTangency, createPoints). 
         - createTangency is: bool. Creates tangency at the point where the spline is subdivided by adding parallel extensions.
         - createPoints is: bool. Add points to the new segments to maintain shape after subdivision.

        """
        pass
    @overload
    def GetSplineSettings(self) -> Tuple[bool, bool, bool]:
        """
         Gets the current subdivide spline settings. 
         Returns A tuple consisting of (createTangency, createPoints, addFixConstraint). 
         - createTangency is: bool. Creates tangency at the point where the spline is subdivided by adding parallel extensions.
         - createPoints is: bool. Add points to the new segments to maintain shape after subdivision.
         - addFixConstraint is: bool. Adds a fix constraint at newly created subdivision locations.

        """
        pass
    @overload
    def SetSplineSettings(self, createTangency: bool, addPoints: bool) -> None:
        """
         Sets options for subdividing splines.
        """
        pass
    @overload
    def SetSplineSettings(self, createTangency: bool, addPoints: bool, addFixConstraint: bool) -> None:
        """
         Sets options for subdividing splines.
        """
        pass
import NXOpen
class TangencyGroupBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Routing.TangencyGroupBuilder
    Assign tangency for segments connected with current editing spline.
    """
    @property
    def SegmentList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SegmentList
         Returns the segment current editing.  
             
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TerminalPortBuilder(NXOpen.Builder): 
    """ Builder for creating the Terminal List Item for the Create Terminals dialog. """
    @property
    def IndividualCutBack(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) IndividualCutBack
         Returns the cutback length for the terminal port   
            
         
        """
        pass
    @property
    def IndividualExtenstion(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) IndividualExtenstion
         Returns  the extension value for the terminal port   
            
         
        """
        pass
    @property
    def Modeled(self) -> bool:
        """
        Getter for property: (bool) Modeled
         Returns the flag for the terminal that says if it is Modeled or not   
            
         
        """
        pass
    @Modeled.setter
    def Modeled(self, modeled: bool):
        """
        Setter for property: (bool) Modeled
         Returns the flag for the terminal that says if it is Modeled or not   
            
         
        """
        pass
    @property
    def TerminalPort(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) TerminalPort
         Returns the  NXOpen::Routing::TerminalPort    
            
         
        """
        pass
    @TerminalPort.setter
    def TerminalPort(self, port: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) TerminalPort
         Returns the  NXOpen::Routing::TerminalPort    
            
         
        """
        pass
import NXOpen
class TerminalPortCollection(NXOpen.TaggedObjectCollection): 
    """
        
        The collection of all NXOpen.Routing.TerminalPorts.  The
        NXOpen.Routing.TerminalPortCollection creates and enumerates
        NXOpen.Routing.TerminalPort.
        
    """
    @overload
    def CreateTerminalPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, multi_port: MultiPort, pin_identifier: str) -> TerminalPort:
        """
                   Creates a NXOpen.Routing.TerminalPort with no
                   rotation vector at an absolute location.
                
         Returns terminal_port ( TerminalPort NXOpen):  newly created NXOpen.Routing.TerminalPort.
        """
        pass
    @overload
    def CreateTerminalPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, point: NXOpen.Point, multi_port: MultiPort, pin_identifier: str) -> TerminalPort:
        """
         Creates a NXOpen.Routing.TerminalPort with no
                    rotation vector at an existing point.  Default allows multiple
                    connections to this port.
                
         Returns terminal_port ( TerminalPort NXOpen):  newly created NXOpen.Routing.TerminalPort .
        """
        pass
    @overload
    def CreateTerminalPort(self, origin: NXOpen.Point3d, alignment_vector: NXOpen.Vector3d, derivation_object: NXOpen.Axis, multi_port: MultiPort, pin_identifier: str) -> TerminalPort:
        """
                    Creates a NXOpen.Routing.TerminalPort with no rotation vector on an
                    axis.  Default allows multiple connections to this port.
                
         Returns terminal_port ( TerminalPort NXOpen):  newly created NXOpen.Routing.TerminalPort .
        """
        pass
import NXOpen
class TerminalPort(Port): 
    """
        
        A NXOpen.Routing.TerminalPort models the pins on an electrical
        connector.  NXOpen.Routing.TerminalPorts are a
        NXOpen.Routing.MultiPort's children.
        
      """
    @property
    def Axis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @Axis.setter
    def Axis(self, axis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) Axis
         Returns  the axis that defines the port  
            
         
        """
        pass
    @property
    def CutbackLengthObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @CutbackLengthObject.setter
    def CutbackLengthObject(self, cutback_length: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) CutbackLengthObject
         Returns the cutback length object of a port, i.  
          e. an expression representing the length
                    along the wire from the port where individual wires leave a bundle to attach to pins
                    
         
        """
        pass
    @property
    def EngagementObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @EngagementObject.setter
    def EngagementObject(self, engagement: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) EngagementObject
         Returns the engagement object of a port, i.  
          e. an expression representing the
                    distance behind the port that another fitting or stock may engage
                    
         
        """
        pass
    @property
    def ForwardExtensionObject(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @ForwardExtensionObject.setter
    def ForwardExtensionObject(self, forward_extension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ForwardExtensionObject
         Returns the forward extension object of a port, i.  
          e. an expression representing the minimum
                    length that a segment must remain straight coming out of a  NXOpen::Routing::Port 
                    
         
        """
        pass
    @property
    def MultiPort(self) -> MultiPort:
        """
        Getter for property: ( MultiPort NXOpen) MultiPort
         Returns the parent  NXOpen::Routing::MultiPort  of the
                     NXOpen::Routing::TerminalPort 
                  
            
         
        """
        pass
    @property
    def PinIdentifier(self) -> str:
        """
        Getter for property: (str) PinIdentifier
         Returns the pin identifier (name) of the  NXOpen::Routing::TerminalPort    
            
         
        """
        pass
    @PinIdentifier.setter
    def PinIdentifier(self, pin_identifier: str):
        """
        Setter for property: (str) PinIdentifier
         Returns the pin identifier (name) of the  NXOpen::Routing::TerminalPort    
            
         
        """
        pass
class Terminal(Enum):
    """
    Members Include: 
     |NotTerminalSeg|  Is not a terminal segment 
     |TerminalSeg|  Is a terminal segment 

    """
    NotTerminalSeg: int
    TerminalSeg: int
    @staticmethod
    def ValueOf(value: int) -> Terminal:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TransformPathBuilder(NXOpen.Builder): 
    """
        Builder for the "Transform Path" operation.  Allows the user to perform
        either a "Transform" or "Copy" of Routing objects.
    """
    class CopyAttributes(Enum):
        """
        Members Include: 
         |Defaults|  Copy Attributes as per defaults. 
         |UserSpecified|  Copy Attributes as per user defined. 

        """
        Defaults: int
        UserSpecified: int
        @staticmethod
        def ValueOf(value: int) -> TransformPathBuilder.CopyAttributes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransformOption(Enum):
        """
        Members Include: 
         |MoveOriginal|  Move the selected entities. 
         |CopyOriginal|  Copy the selected entities. 

        """
        MoveOriginal: int
        CopyOriginal: int
        @staticmethod
        def ValueOf(value: int) -> TransformPathBuilder.TransformOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AcrossAssemblies(self) -> bool:
        """
        Getter for property: (bool) AcrossAssemblies
         Returns the flag that indicates whether or not to transform.  
           across the assemblies   
         
        """
        pass
    @AcrossAssemblies.setter
    def AcrossAssemblies(self, across_assemblies: bool):
        """
        Setter for property: (bool) AcrossAssemblies
         Returns the flag that indicates whether or not to transform.  
           across the assemblies   
         
        """
        pass
    @property
    def AttributeReferenceSelection(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) AttributeReferenceSelection
         Returns the selection which is used to choose the object from which source object attributes
                    should be copied when copying attributes during a Transform Path operation.  
          
                  
         
        """
        pass
    @property
    def CheckForDuplicates(self) -> bool:
        """
        Getter for property: (bool) CheckForDuplicates
         Returns the flag that indicates whether or not to check for duplicate segments after the copy or transform.  
          
                    It applies only to segments and not to control points.   
         
        """
        pass
    @CheckForDuplicates.setter
    def CheckForDuplicates(self, check_for_dups: bool):
        """
        Setter for property: (bool) CheckForDuplicates
         Returns the flag that indicates whether or not to check for duplicate segments after the copy or transform.  
          
                    It applies only to segments and not to control points.   
         
        """
        pass
    @property
    def CopyConnectedParts(self) -> bool:
        """
        Getter for property: (bool) CopyConnectedParts
         Returns the method indicates whether connected parts get copied or not.  
             
         
        """
        pass
    @CopyConnectedParts.setter
    def CopyConnectedParts(self, copy_connected_parts: bool):
        """
        Setter for property: (bool) CopyConnectedParts
         Returns the method indicates whether connected parts get copied or not.  
             
         
        """
        pass
    @property
    def MoveOrCopyOption(self) -> TransformPathBuilder.TransformOption:
        """
        Getter for property: ( TransformPathBuilder.TransformOption NXOpen) MoveOrCopyOption
         Returns the operation to perform during the commit method.  
              
         
        """
        pass
    @MoveOrCopyOption.setter
    def MoveOrCopyOption(self, move_option: TransformPathBuilder.TransformOption):
        """
        Setter for property: ( TransformPathBuilder.TransformOption NXOpen) MoveOrCopyOption
         Returns the operation to perform during the commit method.  
              
         
        """
        pass
    @property
    def MoveWithExtensionSegments(self) -> bool:
        """
        Getter for property: (bool) MoveWithExtensionSegments
         Returns a message stating whether or not to move the selected segments with extension segments.  
             
         
        """
        pass
    @MoveWithExtensionSegments.setter
    def MoveWithExtensionSegments(self, move_with_ext_seg: bool):
        """
        Setter for property: (bool) MoveWithExtensionSegments
         Returns a message stating whether or not to move the selected segments with extension segments.  
             
         
        """
        pass
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of copies to create in the commit method for the option
                     Routing::TransformPathBuilder::TransformOptionCopyOriginal .  
             
         
        """
        pass
    @NumberOfCopies.setter
    def NumberOfCopies(self, number_of_copies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of copies to create in the commit method for the option
                     Routing::TransformPathBuilder::TransformOptionCopyOriginal .  
             
         
        """
        pass
    @property
    def PathSelection(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) PathSelection
         Returns the path selection.  
            Stores the objects to be transformed or copied.   
         
        """
        pass
    @property
    def Transform(self) -> NXOpen.GeometricUtilities.ModlMotion:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ModlMotion) Transform
         Returns the motion or transform.  
            The transformation to apply to the selected or
                    copied objects.   
         
        """
        pass
    def AddConnectedPartsInBuilder(self) -> None:
        """
         Add object in transform object list of builder as per list updated by
                     Routing.TransformPathBuilder.UpdateConnectedPartList
        """
        pass
    def AttachSelectedPath(self) -> None:
        """
         Attaches the selected path back to the path it was originally
                    attached to before the call to Routing.TransformPathBuilder.DetachSelectedPath
                
        """
        pass
    def DestroyAllPreviewObjects(self) -> None:
        """
         Destroys all preview objects associated with this operation.  Caller must
                   call update to complete the deletion of the preview objects. 
        """
        pass
    def DetachSelectedPath(self) -> None:
        """
         Detaches the selected path ends from the connected routing segments.
                    The detached path can be attached back to the previously connected routing
                    segments by using Routing.TransformPathBuilder.AttachSelectedPath
                  
        """
        pass
    def DragByTransform(self, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
         Drag the selected objects by the given translation and rotation.  Only
                    call after invoking the Routing.TransformPathBuilder.StartDrag
                    method.  After finished dragging, call
                    Routing.TransformPathBuilder.StopDrag.
        """
        pass
    def GetCopiedAttributes(self) -> CharacteristicList:
        """
         Get attributes to be copied. 
         Returns charx_data ( CharacteristicList NXOpen): .
        """
        pass
    def GetIthSetOfObjects(self, ith: int) -> List[NXOpen.NXObject]:
        """
         Gets the set of objects created for the "ith" copy during the
                    commit method.  The 0th element is the original set of objects
                    to copy.  
         Returns objects ( NXOpen.NXObject Li):  Copied objects. .
        """
        pass
    def GetOmittedAttributes(self) -> CharacteristicList:
        """
         Get attributes to be omitted. 
         Returns charx_data ( CharacteristicList NXOpen): .
        """
        pass
    def RemoveConnectedPartsInBuilder(self) -> None:
        """
         Remove object from transform object list of builder as per list updated by
                     Routing.TransformPathBuilder.UpdateConnectedPartList
        """
        pass
    def SetCollisionObject(self, objectValue: NXOpen.NXObject) -> None:
        """
         Sets collision object during the preview 
        """
        pass
    def SetCopiedAttributes(self, charx_data: CharacteristicList) -> None:
        """
         Set attributes to be copied. 
        """
        pass
    def SetCopyTransform(self, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
         Sets the transform to use for the copy operation. 
        """
        pass
    def SetOmittedAttributes(self, charx_data: CharacteristicList) -> None:
        """
         Set attributes to be omitted. 
        """
        pass
    def StartDrag(self) -> None:
        """
         Begin a drag operation.  
        """
        pass
    def StopDrag(self) -> None:
        """
         End a drag operation.  
        """
        pass
    def UpdateConnectedPartList(self, selectedObject: List[NXOpen.NXObject], deselectedObject: List[NXOpen.NXObject]) -> None:
        """
         Update connected part list in builder as per selection or deselection of object 
        """
        pass
    def UpdateSelObjectsVector(self) -> None:
        """
         Adds selected objects into vector during selection 
        """
        pass
class Type(Enum):
    """
    Members Include: 
     |Unknown| 
     |FixedCrossSection|  
     |Wrapped|  
     |Sleeved|  
     |Flagged|  

    """
    Unknown: int
    FixedCrossSection: int
    Wrapped: int
    Sleeved: int
    Flagged: int
    @staticmethod
    def ValueOf(value: int) -> Type:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class UnifyPathBuilder(NXOpen.Builder): 
    """ Builder to unify Routing.Stock and Assemblies.Component
        based on specified characteristic values.
        The builder takes a set of objects and replaces them with new objects that matches
        the given characterstics."""
    @property
    def ReferenceObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ReferenceObject
         Returns the reference object used to extract characteristics to unify.  
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) RouteObjectCollector
         Returns the routing object collector to select objects to unify.  
            
         
        """
        pass
    def GetUnifyCharacteristics(self) -> CharacteristicList:
        """
         Returns Routing.CharacteristicList to be used to find
                    matching Routing.Stock and Assemblies.Component
                    to replace. 
         Returns unifyCharx ( CharacteristicList NXOpen): The characteristics to use in finding a replacement for the given object.
        """
        pass
    def SetUnifyCharacteristics(self, charxType: NXOpen.NXObject.AttributeType, charxName: str, charxValue: str) -> None:
        """
         Sets the characteristics to be applied
        """
        pass
class UserDefined(Enum):
    """
    Members Include: 
     |NotUserDefined|  System generated segment.
                                                                  System manages simplification and some update behavior. 
     |UserDefined|  User defined generated segment. 

    """
    NotUserDefined: int
    UserDefined: int
    @staticmethod
    def ValueOf(value: int) -> UserDefined:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class WatertightFittingsBuilder(NXOpen.Builder): 
    """  Represents a NXOpen.Routing.WatertightFittingsBuilder  """
    @property
    def Filename(self) -> str:
        """
        Getter for property: (str) Filename
         Returns the name of new part file containing watertight fittings assembly which includes the full path.  
             
         
        """
        pass
    @Filename.setter
    def Filename(self, fileName: str):
        """
        Setter for property: (str) Filename
         Returns the name of new part file containing watertight fittings assembly which includes the full path.  
             
         
        """
        pass
    @property
    def FittingMembers(self) -> RouteObjectCollector:
        """
        Getter for property: ( RouteObjectCollector NXOpen) FittingMembers
         Returns the Routing Object Collector builder that stores selected routing members     
            
         
        """
        pass
    @property
    def FlangeDirection(self) -> bool:
        """
        Getter for property: (bool) FlangeDirection
         Returns the direction of flange thickness   
            
         
        """
        pass
    @FlangeDirection.setter
    def FlangeDirection(self, flangeDirection: bool):
        """
        Setter for property: (bool) FlangeDirection
         Returns the direction of flange thickness   
            
         
        """
        pass
    @property
    def FlangeOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlangeOffset
         Returns the offset value for flange creation   
            
         
        """
        pass
    @property
    def FlangeSketch(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) FlangeSketch
         Returns the section used for creating penetration extrude.  
             
         
        """
        pass
    @property
    def FlangeThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlangeThickness
         Returns the thickness value for flange creation   
            
         
        """
        pass
    def GetOptionalAttributes(self) -> CharacteristicList:
        """
         Get optional attributes for Watertight Fittings. 
         Returns charx_data ( CharacteristicList NXOpen): .
        """
        pass
    def GetRequiredAttributes(self) -> CharacteristicList:
        """
         Get required attributes for Watertight Fittings. 
         Returns charx_data ( CharacteristicList NXOpen): .
        """
        pass
    def SetFilenameFromFilenewbuilder(self, fileNewBuilder: NXOpen.FileNew) -> None:
        """
         Sets the file name on  Watertight Fittings from file new builder
                
        """
        pass
    def SetOptionalAttributes(self, charx_data: CharacteristicList) -> None:
        """
         Set optional attributes for Watertight Fittings. 
        """
        pass
    def SetRequiredAttributes(self, charx_data: CharacteristicList) -> None:
        """
         Set required attributes for Watertight Fittings. 
        """
        pass
import NXOpen
class WindCatcherBuilder(NXOpen.Builder): 
    """ Builder class for Wind Catcher feature. See NXOpen.Routing.WindCatcher
        for the Wind Catcher class documentation.
    """
    class WindCatcherType(Enum):
        """
        Members Include: 
         |Arc|  
         |Triangle|  

        """
        Arc: int
        Triangle: int
        @staticmethod
        def ValueOf(value: int) -> WindCatcherBuilder.WindCatcherType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EndAngleExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndAngleExpression
         Returns the angle in degrees between the wind direction vector and the open face of the Wind Catcher.  
          
                  
         
        """
        pass
    @property
    def ParentDuct(self) -> Stock:
        """
        Getter for property: ( Stock NXOpen) ParentDuct
         Returns the duct from which the Wind Catcher derives the wind direction.  
             
         
        """
        pass
    @ParentDuct.setter
    def ParentDuct(self, parentDuct: Stock):
        """
        Setter for property: ( Stock NXOpen) ParentDuct
         Returns the duct from which the Wind Catcher derives the wind direction.  
             
         
        """
        pass
    @property
    def ReverseWindDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseWindDirection
         Returns the flag that indicates whether the wind direction is reversed from its normal direction.  
          
                  The normal direction for the wind either matches the flow direction, if the parent stock
                  is part of a Run, or matches the parent stock's segment direction from the start control point
                  to the end control point.
                  
         
        """
        pass
    @ReverseWindDirection.setter
    def ReverseWindDirection(self, windDirection: bool):
        """
        Setter for property: (bool) ReverseWindDirection
         Returns the flag that indicates whether the wind direction is reversed from its normal direction.  
          
                  The normal direction for the wind either matches the flow direction, if the parent stock
                  is part of a Run, or matches the parent stock's segment direction from the start control point
                  to the end control point.
                  
         
        """
        pass
    @property
    def TrimToParentDuct(self) -> bool:
        """
        Getter for property: (bool) TrimToParentDuct
         Returns the flag that indicates whether the Wind Catcher's duct should be trimmed back to the top of the parent duct.  
             
         
        """
        pass
    @TrimToParentDuct.setter
    def TrimToParentDuct(self, trim: bool):
        """
        Setter for property: (bool) TrimToParentDuct
         Returns the flag that indicates whether the Wind Catcher's duct should be trimmed back to the top of the parent duct.  
             
         
        """
        pass
    @property
    def Type(self) -> WindCatcherBuilder.WindCatcherType:
        """
        Getter for property: ( WindCatcherBuilder.WindCatcherType NXOpen) Type
         Returns the type of Wind Catcher.  
             
         
        """
        pass
    @Type.setter
    def Type(self, windCatcherType: WindCatcherBuilder.WindCatcherType):
        """
        Setter for property: ( WindCatcherBuilder.WindCatcherType NXOpen) Type
         Returns the type of Wind Catcher.  
             
         
        """
        pass
    @property
    def WindCatcherDuct(self) -> Stock:
        """
        Getter for property: ( Stock NXOpen) WindCatcherDuct
         Returns the duct on which the Wind Catcher attaches.  
             
         
        """
        pass
    @WindCatcherDuct.setter
    def WindCatcherDuct(self, windCatcherDuct: Stock):
        """
        Setter for property: ( Stock NXOpen) WindCatcherDuct
         Returns the duct on which the Wind Catcher attaches.  
             
         
        """
        pass
    def GetClosestParentDuctSegment(self) -> LineSegment:
        """
         Returns the linear segment under the Parent Duct that is closest to the Wind Catcher. 
         Returns segment ( LineSegment NXOpen): .
        """
        pass
import NXOpen.Features
class WindCatcher(NXOpen.Features.BodyFeature): 
    """ Represents a Wind Catcher feature.
        Use the NXOpen.Routing.WindCatcherBuilder class to create a Wind Catcher feature. """
    pass
import NXOpen
class WireCollection(NXOpen.TaggedObjectCollection): 
    """ The Routing Wire object is a list of segments in a route and some
        stock.  It also contains the beginning and ending control point
        for the path.
     """
    def CreateWire(self, startControlPoint: ControlPoint, endControlPoint: ControlPoint, segments: List[ISegment], stockData: StockData, stocks: List[Stock], lengthOfWire: float) -> Wire:
        """
         Creates a wire object. 
         Returns wire ( Wire NXOpen):  .
        """
        pass
import NXOpen
class Wire(NXOpen.NXObject): 
    """ The Routing Wire object is the set of information needed to define
        a wire that implements a connection.  """
    @property
    def ControlPointEnd(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointEnd.setter
    def ControlPointEnd(self, end: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointEnd
         Returns the end ControlPoint for an IPath object.  
             
         
        """
        pass
    @property
    def ControlPointStart(self) -> ControlPoint:
        """
        Getter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    @ControlPointStart.setter
    def ControlPointStart(self, start: ControlPoint):
        """
        Setter for property: ( ControlPoint NXOpen) ControlPointStart
         Returns the start ControlPoint for an IPath object.  
             
         
        """
        pass
    def GetSegments(self) -> List[ISegment]:
        """
         Returns the segments for the wire. 
         Returns segments ( ISegment List[NXOp):  .
        """
        pass
    def GetStock(self) -> List[Stock]:
        """
         Returns the stocks for the wire. 
         Returns stocks ( Stock List[NXOp):  .
        """
        pass
class WrapApplicationType(Enum):
    """
    Members Include: 
     |Unknown|  Unknown wrap application 
     |Spot|  Spot wrap application, i.e., 100% overlap 
     |Overlapped|  Overlapping spiral wrap application, e.g., [0-100)% overlap 
     |Gapped|  Barber pole spiral wrap application, e.g., no overlap 

    """
    Unknown: int
    Spot: int
    Overlapped: int
    Gapped: int
    @staticmethod
    def ValueOf(value: int) -> WrapApplicationType:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
