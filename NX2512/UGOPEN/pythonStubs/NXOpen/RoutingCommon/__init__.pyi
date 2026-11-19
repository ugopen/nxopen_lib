from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class AssignCornerBuilder(NXOpen.Builder): 
    """ Builder class for Assign Corner which creates corner"""
    @property
    def ControlPointSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) ControlPointSelection
         Returns the routing control points collector   
            
         
        """
        pass
    @property
    def CornerSettings(self) -> CornerBuilder:
        """
        Getter for property: ( CornerBuilder NXOpen.Ro) CornerSettings
         Returns the corner block   
            
         
        """
        pass
    def CycleSolution(self) -> None:
        """
         Reverse the direction which the overlap stock will be trimmed. 
        """
        pass
    def GetBendCornerAttributes(self) -> List[NXOpen.NXObject.AttributeInformation]:
        """
         Gets the corner attributes that came from the bend radius table. 
         Returns attributes ( NXOpen.NXObject.AttributeInformation Li):  .
        """
        pass
    def GetCreatedComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
         Components created during Assign Corner operation. 
         Returns components ( NXOpen.Assemblies.Component Li):  Components created during Assign Corner operation. .
        """
        pass
    def RemoveBendCornerAttributes(self, corners: List[NXOpen.Routing.Corner]) -> None:
        """
         Removes the corner attributes that came from the bend radius table. 
        """
        pass
    def SetBendCornerAttributes(self, attributes: List[NXOpen.NXObject.AttributeInformation]) -> None:
        """
         Sets the corner attributes that came from the bend radius table. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class BaseCornerTypeBuilder(NXOpen.TaggedObject): 
    """ Builder class for Base Corner Types """
    pass
import NXOpen
class BendCornerTypeBuilder(BaseCornerTypeBuilder): 
    """ Contains setting for corner creation. Type of bend to be created and the method to
        create the corner. 
    
    """
    class BendMethod(Enum):
        """
        Members Include: 
         |Radius|  Radius method allows corner creation with the specified radius value  
         |RatioToDiameter|  Ratio to diameter method 
         |RatioToAttribute|  Ratio to attribute method 
         |BendRadiusTable|  Bend table method creates bend from specified bend table
         |InnerRadius|  Inner Radius method allows corner creation with the specified inner radius value  

        """
        Radius: int
        RatioToDiameter: int
        RatioToAttribute: int
        BendRadiusTable: int
        InnerRadius: int
        @staticmethod
        def ValueOf(value: int) -> BendCornerTypeBuilder.BendMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Method(self) -> BendCornerTypeBuilder.BendMethod:
        """
        Getter for property: ( BendCornerTypeBuilder.BendMethod NXOpen.Ro) Method
         Returns the bend corner methods   
            
         
        """
        pass
    @Method.setter
    def Method(self, routeCornerBendMethods: BendCornerTypeBuilder.BendMethod):
        """
        Setter for property: ( BendCornerTypeBuilder.BendMethod NXOpen.Ro) Method
         Returns the bend corner methods   
            
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the bend corner radius   
            
         
        """
        pass
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
    def RatioToAttributeName(self) -> str:
        """
        Getter for property: (str) RatioToAttributeName
         Returns the bend corner ratio to attribute name   
            
         
        """
        pass
    @RatioToAttributeName.setter
    def RatioToAttributeName(self, bendRatioToAttributeName: str):
        """
        Setter for property: (str) RatioToAttributeName
         Returns the bend corner ratio to attribute name   
            
         
        """
        pass
    @property
    def RatioToAttributeValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RatioToAttributeValue
         Returns the bend corner ratio to attribute   
            
         
        """
        pass
    @property
    def RatioToDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RatioToDiameter
         Returns the bend corner ratio to diameter   
            
         
        """
        pass
    @property
    def StockPartNumberFromBendTable(self) -> str:
        """
        Getter for property: (str) StockPartNumberFromBendTable
         Returns the stock name  determined using the stock and the bend radius table.  
             
         
        """
        pass
    @StockPartNumberFromBendTable.setter
    def StockPartNumberFromBendTable(self, stockPartNumber: str):
        """
        Setter for property: (str) StockPartNumberFromBendTable
         Returns the stock name  determined using the stock and the bend radius table.  
             
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class BuilderFactory(NXOpen.Object): 
    """ Represents an NXOpen.RoutingCommon.BuilderFactory object.  Use this object 
        to create specific routing builders.
    """
    def CreateAssignCornerBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> AssignCornerBuilder:
        """
          Creates a NXOpen.RoutingCommon.AssignCornerBuilder object. 
         Returns builder ( AssignCornerBuilder NXOpen.Ro): .
        """
        pass
    def CreateCablewayPatternBlockBuilder(part: NXOpen.Part) -> CablewayPatternBlockBuilder:
        """
          Creates a NXOpen.RoutingCommon.CablewayPatternBlockBuilder object. 
         Returns builder ( CablewayPatternBlockBuilder NXOpen.Ro): .
        """
        pass
    def CreateConnectBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, components: List[NXOpen.Assemblies.Component]) -> ConnectBuilder:
        """
          Creates a NXOpen.RoutingCommon.ConnectBuilder object. 
         Returns builder ( ConnectBuilder NXOpen.Ro): .
        """
        pass
    def CreateConnectOutletStockBuilder(part: NXOpen.Part) -> ConnectOutletStockBuilder:
        """
          Creates a NXOpen.RoutingCommon.ConnectOutletStockBuilder object. 
         Returns builder ( ConnectOutletStockBuilder NXOpen.Ro): .
        """
        pass
    def CreateDeleteBuilder(part: NXOpen.Part) -> DeleteBuilder:
        """
          Creates a NXOpen.RoutingCommon.DeleteBuilder object. 
                     This API is for delete routing objects. 
         Returns builder ( DeleteBuilder NXOpen.Ro): .
        """
        pass
    def CreateDisconnectBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> DisconnectBuilder:
        """
          Create a NXOpen.RoutingCommon.DisconnectBuilder object. 
         Returns builder ( DisconnectBuilder NXOpen.Ro): .
        """
        pass
    def CreateEditPlacementBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> EditPlacementBuilder:
        """
          Creates a NXOpen.RoutingCommon.EditPlacementBuilder object. 
         Returns builder ( EditPlacementBuilder NXOpen.Ro): .
        """
        pass
    def CreateEditPointBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> EditPointBuilder:
        """
          Create a NXOpen.RoutingCommon.EditPointBuilder object. 
         Returns builder ( EditPointBuilder NXOpen.Ro): .
        """
        pass
    def CreateEditTemplateParametersBuilder(part: NXOpen.Part) -> EditTemplateParametersBuilder:
        """
          Creates a NXOpen.RoutingCommon.EditTemplateParametersBuilder object. 
         Returns builder ( EditTemplateParametersBuilder NXOpen.Ro): .
        """
        pass
    def CreateInsulationBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, insulationPartOccurrence: NXOpen.Assemblies.Component) -> InsulationBuilder:
        """
          Create a NXOpen.RoutingCommon.InsulationBuilder object. 
         Returns builder ( InsulationBuilder NXOpen.Ro): .
        """
        pass
    def CreateLibraryRefreshBuilder(part: NXOpen.Part) -> LibraryRefreshBuilder:
        """
          Creates a NXOpen.RoutingCommon.LibraryRefreshBuilder object. 
         Returns builder ( LibraryRefreshBuilder NXOpen.Ro): .
        """
        pass
    def CreateManageInlineBehaviorBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> ManageInlineBehaviorBuilder:
        """
          Creates a NXOpen.RoutingCommon.ManageInlineBehaviorBuilder object. 
         Returns builder ( ManageInlineBehaviorBuilder NXOpen.Ro): .
        """
        pass
    def CreateMergeBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> MergeBuilder:
        """
          Creates a NXOpen.RoutingCommon.MergeBuilder object. 
         Returns builder ( MergeBuilder NXOpen.Ro): .
        """
        pass
    def CreateMovePathBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> MovePathBuilder:
        """
          Create a NXOpen.RoutingCommon.MovePathBuilder object. 
         Returns builder ( MovePathBuilder NXOpen.Ro): .
        """
        pass
    def CreateOffsetOutletStockBuilder(part: NXOpen.Part) -> OffsetOutletStockBuilder:
        """
          Creates a NXOpen.RoutingCommon.OffsetOutletStockBuilder object. 
         Returns builder ( OffsetOutletStockBuilder NXOpen.Ro): .
        """
        pass
    def CreatePartPlacementBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> PartPlacementBuilder:
        """
          Creates a NXOpen.RoutingCommon.PartPlacementBuilder object. 
         Returns builder ( PartPlacementBuilder NXOpen.Ro): .
        """
        pass
    def CreatePathBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component) -> CreatePathBuilder:
        """
          Create a NXOpen.RoutingCommon.CreatePathBuilder object. 
         Returns builder ( CreatePathBuilder NXOpen.Ro): .
        """
        pass
    def CreateReparentPartsBuilder(part: NXOpen.Part) -> ReparentPartsBuilder:
        """
          Create a NXOpen.RoutingCommon.ReparentPartsBuilder object. 
         Returns builder ( ReparentPartsBuilder NXOpen.Ro): .
        """
        pass
    def CreateSecondaryPlacementBuilder(part: NXOpen.Part, parentBuilderTag: NXOpen.Builder) -> SecondaryPlacementBuilder:
        """
          Creates a NXOpen.RoutingCommon.SecondaryPlacementBuilder object.
                     This API is for creating secondary placement builder and it is common for both create path and place part. 
                     When it is called for place part, parentBuilderTag would be the PartPlacementBuilder.
                     When it is called for Create Path, parentBuilderTag is used just for data transfer from create path builder to
                     secondary placement builder. 
         Returns builder ( SecondaryPlacementBuilder NXOpen.Ro): .
        """
        pass
    def CreateSimplifyCurvesBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, segments: List[NXOpen.Routing.ISegment]) -> SimplifyCurvesBuilder:
        """
          Create a NXOpen.RoutingCommon.SimplifyCurvesBuilder object. 
         Returns builder ( SimplifyCurvesBuilder NXOpen.Ro):  .
        """
        pass
    def CreateSplitBuilder(part: NXOpen.Part, controlPoints: List[NXOpen.Routing.ControlPoint]) -> SplitBuilder:
        """
          Creates a NXOpen.RoutingCommon.SplitBuilder object. 
         Returns builder ( SplitBuilder NXOpen.Ro): .
        """
        pass
    def CreateStockBuilder(part: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, segmentsOrStocks: List[NXOpen.NXObject]) -> StockBuilder:
        """
          Creates a NXOpen.RoutingCommon.StockBuilder object. 
         Returns builder ( StockBuilder NXOpen.Ro): .
        """
        pass
    def CreateSubdivideCurveBuilder(part: NXOpen.Part, segment: NXOpen.NXObject, pickPoint: NXOpen.Point3d) -> SubdivideCurveBuilder:
        """
          Create a NXOpen.RoutingCommon.SubdivideCurveBuilder object. 
         Returns builder ( SubdivideCurveBuilder NXOpen.Ro):  .
        """
        pass
    def CreateTransferBuilder(part: NXOpen.Part, components: List[NXOpen.Assemblies.Component]) -> TransferBuilder:
        """
         Creates a NXOpen.RoutingCommon.TransferBuilder object 
         Returns builder ( TransferBuilder NXOpen.Ro): .
        """
        pass
    def CreateTransformBlockBuilder(part: NXOpen.Part) -> TransformBlockBuilder:
        """
          Create a NXOpen.RoutingCommon.TransformBlockBuilder object. 
         Returns builder ( TransformBlockBuilder NXOpen.Ro): .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class CablewayPatternBlockBuilder(NXOpen.Builder): 
    """ Builder class for Cableway Pattern Block command. """
    class CablewayPatternMethod(Enum):
        """
        Members Include: 
         |NotSet|  No Pattern. 
         |SpecifiedPattern|  Pattern selected from Specify Item dialog 
         |SpecifiedStock|  Stock selected from Specify Item dialog 
         |SpecifiedSpaceReservation|  Space Reservation selected from Specify Item dialog 

        """
        NotSet: int
        SpecifiedPattern: int
        SpecifiedStock: int
        SpecifiedSpaceReservation: int
        @staticmethod
        def ValueOf(value: int) -> CablewayPatternBlockBuilder.CablewayPatternMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PatternMethod(Enum):
        """
        Members Include: 
         |NotSet|  No Pattern. 
         |SpecifiedPattern|  Pattern selected from Specify Item dialog 
         |SpecifiedCablewayTray|  Cableway Tray selected from Specify Item dialog 
         |SpecifiedSpaceReservation|  Space Reservation selected from Specify Item dialog 

        """
        NotSet: int
        SpecifiedPattern: int
        SpecifiedCablewayTray: int
        SpecifiedSpaceReservation: int
        @staticmethod
        def ValueOf(value: int) -> CablewayPatternBlockBuilder.PatternMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CablewayPatternMethodType(self) -> CablewayPatternBlockBuilder.CablewayPatternMethod:
        """
        Getter for property: ( CablewayPatternBlockBuilder.CablewayPatternMethod NXOpen.Ro) CablewayPatternMethodType
         Returns the method to determine which pattern to assign.  
             
         
        """
        pass
    @CablewayPatternMethodType.setter
    def CablewayPatternMethodType(self, method: CablewayPatternBlockBuilder.CablewayPatternMethod):
        """
        Setter for property: ( CablewayPatternBlockBuilder.CablewayPatternMethod NXOpen.Ro) CablewayPatternMethodType
         Returns the method to determine which pattern to assign.  
             
         
        """
        pass
    @property
    def CablewayPatternPartNumber(self) -> str:
        """
        Getter for property: (str) CablewayPatternPartNumber
         Returns   
            
         
        """
        pass
    @property
    def PatternMethodType(self) -> CablewayPatternBlockBuilder.PatternMethod:
        """
        Getter for property: ( CablewayPatternBlockBuilder.PatternMethod NXOpen.Ro) PatternMethodType
         Returns the method to determine which pattern to assign.  
             
         
        """
        pass
    @PatternMethodType.setter
    def PatternMethodType(self, method: CablewayPatternBlockBuilder.PatternMethod):
        """
        Setter for property: ( CablewayPatternBlockBuilder.PatternMethod NXOpen.Ro) PatternMethodType
         Returns the method to determine which pattern to assign.  
             
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle   
            
         
        """
        pass
    def Flip(self) -> None:
        """
         The button to handle the flip state 
        """
        pass
    def GetAttributeHolder(self) -> NXOpen.Routing.AttributeHolder:
        """
         Gets the attribute holder for library defined attributes on cableway pattern to be applied 
         Returns libraryDefinedAttributeHolder ( NXOpen.Routing.AttributeHolder): .
        """
        pass
    def ResetAttributeHolder(self) -> None:
        """
         Resets the attribute holder for library defined attributes for cableway pattern attribute holder
                    This API is recommended to be used before assigning attributes onto builder so as to ensure cableway pattern apply operation to function correctly 
        """
        pass
    def SetEtpComponents(self, etpComponents: List[NXOpen.Assemblies.Component]) -> None:
        """
         
        """
        pass
    def SetEtpSegments(self, etpSegments: List[NXOpen.Routing.ISegment]) -> None:
        """
         Sets the etp segments to which the pattern will be applied
        """
        pass
    def SetFlip(self, flip: bool) -> None:
        """
         
        """
        pass
    def SetScreenSelectedComponent(self, component: NXOpen.Assemblies.Component) -> None:
        """
         Sets the screen-selected component that is used for creating a cableway pattern. 
        """
        pass
    def SetSegmentAndRotationAngleForPattern(self, segment: NXOpen.Routing.ISegment, formula: str) -> None:
        """
         Sets the segment and angle to control orientation of pattern allocation.
        """
        pass
    def SetSegmentAndRotationAngleForStandaloneSpaceReservation(self, segment: NXOpen.Routing.ISegment, formula: str) -> None:
        """
         Sets the segment and angle to control orientation of standalone space reservation allocation.
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ConnectBuilder(NXOpen.Builder): 
    """ the Builder for Connect Path """
    @property
    def ComponentsCollector(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) ComponentsCollector
         Returns the selected components    
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ConnectOutletStockBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.ConnectOutletStockBuilder. """
    @property
    def HeaderCollector(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) HeaderCollector
         Returns the header components    
            
         
        """
        pass
    @property
    def OutletCollector(self) -> NXOpen.Assemblies.SelectComponentList:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponentList) OutletCollector
         Returns the outlet components    
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class CornerBuilder(NXOpen.TaggedObject): 
    """ Builder class for Corner Block """
    class Type(Enum):
        """
        Members Include: 
         |NotSet|  None, no corner created  
         |Bend|  allows corner creation with the specified bend type 
         |Miter|  allows miter corner creation 
         |Overlap|  allows overlap corner creation 
         |Elbow|  allows elbow corner creation 

        """
        NotSet: int
        Bend: int
        Miter: int
        Overlap: int
        Elbow: int
        @staticmethod
        def ValueOf(value: int) -> CornerBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BendCornerSettings(self) -> BendCornerTypeBuilder:
        """
        Getter for property: ( BendCornerTypeBuilder NXOpen.Ro) BendCornerSettings
         Returns the bend corner block   
            
         
        """
        pass
    @property
    def CornerType(self) -> CornerBuilder.Type:
        """
        Getter for property: ( CornerBuilder.Type NXOpen.Ro) CornerType
         Returns the corner types   
            
         
        """
        pass
    @CornerType.setter
    def CornerType(self, cornerType: CornerBuilder.Type):
        """
        Setter for property: ( CornerBuilder.Type NXOpen.Ro) CornerType
         Returns the corner types   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class CreatePathBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.CreatePathBuilder. Allows the user to create 
        routing path.
    """
    @property
    def CablewayPatternSettings(self) -> CablewayPatternBlockBuilder:
        """
        Getter for property: ( CablewayPatternBlockBuilder NXOpen.Ro) CablewayPatternSettings
         Returns the cableway pattern block    
            
         
        """
        pass
    @property
    def CornerSettings(self) -> CornerBuilder:
        """
        Getter for property: ( CornerBuilder NXOpen.Ro) CornerSettings
         Returns the builder to assign corners to the routing path.  
            
         
        """
        pass
    @property
    def ElbowCornerOptionBuilder(self) -> ElbowCornerOptionBuilder:
        """
        Getter for property: ( ElbowCornerOptionBuilder NXOpen.Ro) ElbowCornerOptionBuilder
         Returns the elbow corner option builder on this builder   
            
         
        """
        pass
    @property
    def ElectricalTopologyPath(self) -> bool:
        """
        Getter for property: (bool) ElectricalTopologyPath
         Returns the toggle to set the electrical topology path    
            
         
        """
        pass
    @ElectricalTopologyPath.setter
    def ElectricalTopologyPath(self, electricalTopologyPath: bool):
        """
        Setter for property: (bool) ElectricalTopologyPath
         Returns the toggle to set the electrical topology path    
            
         
        """
        pass
    @property
    def PathStockBuilder(self) -> StockBuilder:
        """
        Getter for property: ( StockBuilder NXOpen.Ro) PathStockBuilder
         Returns the builder for creating stock.  
            
         
        """
        pass
    @property
    def PathTransitionListManagerBuilder(self) -> PathTransitionListManagerBuilder:
        """
        Getter for property: ( PathTransitionListManagerBuilder NXOpen.Ro) PathTransitionListManagerBuilder
         Returns the builder for managing path transitions that make up the path.  
            
         
        """
        pass
    @property
    def StockSettings(self) -> NXOpen.Routing.StockBlockBuilder:
        """
        Getter for property: ( NXOpen.Routing.StockBlockBuilder) StockSettings
         Returns the builder for assigning stock to the new path.  
            
         
        """
        pass
    def CreatePathTransitionManagerBuilder(self, workPart: NXOpen.Part, workOcc: NXOpen.Assemblies.Component, displayPart: NXOpen.Part) -> PathTransitionListManagerBuilder:
        """
         Creates a NXOpen.RoutingCommon.PathTransitionListManagerBuilder object. 
         Returns transitionManagerBuilder ( PathTransitionListManagerBuilder NXOpen.Ro): .
        """
        pass
    def GetBendCornerAttributes(self) -> List[NXOpen.NXObject.AttributeInformation]:
        """
         Gets the corner attributes that came from the bend radius table. 
         Returns attributes ( NXOpen.NXObject.AttributeInformation Li):  .
        """
        pass
    def GetCreateOutletAtFirstPoint(self) -> bool:
        """
         Gets create outlet at first point from builder  
         Returns createOutletAtFirstPoint (bool): .
        """
        pass
    def GetCreateOutletAtLastPoint(self) -> bool:
        """
         Gets create outlet at last point from builder  
         Returns createOutletAtLastPoint (bool): .
        """
        pass
    def GetHeaderApplyDeflector(self) -> bool:
        """
         Gets header stock apply deflector from builder  
         Returns applyHeaderDeflector (bool): .
        """
        pass
    def GetLogicalConnection(self) -> NXOpen.TaggedObject:
        """
         Gets logical connection from builder 
         Returns connection ( NXOpen.TaggedObject): .
        """
        pass
    def RemoveBendCornerAttributes(self, corners: List[NXOpen.Routing.Corner]) -> None:
        """
         Removes the corner attributes that came from the bend radius table. 
        """
        pass
    def SetBendCornerAttributes(self, attributes: List[NXOpen.NXObject.AttributeInformation]) -> None:
        """
         Sets the corner attributes that came from the bend radius table. 
        """
        pass
    def SetCreateOutletAtFirstPoint(self, createOutletAtFirstPoint: bool) -> None:
        """
         Sets create outlet at first point on builder 
        """
        pass
    def SetCreateOutletAtLastPoint(self, createOutletAtLastPoint: bool) -> None:
        """
         Sets create outlet at last point on builder 
        """
        pass
    def SetElbowCornerOptionBuilder(self, elbowCornerOptionBuilder: ElbowCornerOptionBuilder) -> None:
        """
         Sets the elbow corner option builder on the create path builder 
        """
        pass
    def SetHeaderApplyDeflector(self, applyHeaderDeflector: bool) -> None:
        """
         Sets header stock apply deflector from builder 
        """
        pass
    def SetLogicalConnection(self, connection: NXOpen.TaggedObject) -> None:
        """
         Sets logical connection on builder 
        """
        pass
    def SetTemplateAttributes(self) -> None:
        """
         Updates the feature template attributes .
        """
        pass
import NXOpen
import NXOpen.Routing
class CustomManager(NXOpen.Object): 
    """ The Routing Custom Manager allows you to customize the Routed System Designer (RSD)
        applications by adding plugins and design rules. """
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
    DesignRule = Callable[[NXOpen.Routing.CustomManager.DesignRuleReason, List[NXOpen.NXObject]], None]
    def AddDesignRule(self, reason: NXOpen.Routing.CustomManager.DesignRuleReason, name: str, description: str, designRuleMethod: CustomManager.DesignRule) -> int:
        """
         Adds the design rule with the given reason.
                    NOTE: You can register more than one design rule with the same reason. 
         Returns designRuleMethodId (int):  A unique identifier for your design rule. .
        """
        pass
    CablewayAreaNamePlugin = Callable[[NXOpen.Assemblies.Component], None]
    CablewayDeviceIdentifierPlugin = Callable[[NXOpen.Assemblies.Component], None]
    CablewayPostExportPlugin = Callable[[str], None]
    CablewayPreExportPlugin = Callable[[str], None]
    CablewayUniqueNodeNamePlugin = Callable[[str, NXOpen.Assemblies.Component, NXOpen.NXObject], None]
    CablewayUniqueSegmentNamePlugin = Callable[[str, NXOpen.Assemblies.Component, NXOpen.NXObject], None]
    CablewayXmlFileNamePlugin = Callable[[], None]
    ComponentNamePlugin = Callable[[NXOpen.Routing.ComponentNamePluginData], None]
    def CreateViolationForReason(self, designRuleName: str, reason: NXOpen.Routing.CustomManager.DesignRuleReason, shortDescription: str, longDescription: str, objects: List[NXOpen.NXObject]) -> NXOpen.Routing.DesignRuleViolation:
        """
         Creates a new violation for a design rule reason. 
         Returns violation ( NXOpen.Routing.DesignRuleViolation):  The newly created violation object. .
        """
        pass
    def DeleteViolationsOfRuleOnObject(self, designRuleName: str, nxObject: NXOpen.NXObject) -> None:
        """
         Finds the violation of a design rule attached to the given object and deletes it.
                    Useful when the given object no longer violates this rule.
                    This method calls update after deleting the violations. 
        """
        pass
    def DeleteViolationsOnObjectForReason(self, reason: NXOpen.Routing.CustomManager.DesignRuleReason, nxObject: NXOpen.NXObject) -> None:
        """
         Finds the violation of a design rule reason attached to the given object and deletes it.
                    Useful when the given object no longer violates this rule.
                    This method calls update after deleting the violations. 
        """
        pass
    def GetDesignRulesRegisteredForReason(self, reason: NXOpen.Routing.CustomManager.DesignRuleReason) -> List[int]:
        """
         Returns the design rules, if any, registered for the given reason. 
         Returns registeredDesignRuleIds (List[int]):  The design rule identifiers, if any, registered with this reason. .
        """
        pass
    def GetViolationsForReason(self, reason: NXOpen.Routing.CustomManager.DesignRuleReason) -> List[NXOpen.Routing.DesignRuleViolation]:
        """
         Returns any violations recorded against a design rule reason. 
         Returns violations ( NXOpen.Routing.DesignRuleViolation Li):  The violations for this reason. .
        """
        pass
    def GetViolationsOfRule(self, designRuleName: str) -> List[NXOpen.Routing.DesignRuleViolation]:
        """
         Returns any violations recorded against a design rule. 
         Returns violations ( NXOpen.Routing.DesignRuleViolation Li):  The violations for this reason. .
        """
        pass
    RSDApplicationEnterPlugin = Callable[[CustomManager.Application], None]
    RSDApplicationExitPlugin = Callable[[CustomManager.Application], None]
    def RemoveAllDesignRules(self) -> None:
        """
         Removes all the registered design rules, except those configured in the Application View file. 
        """
        pass
    def RemoveAllDesignRulesForReason(self, reason: NXOpen.Routing.CustomManager.DesignRuleReason) -> None:
        """
         Removes all the design rules registered for a particular reason. 
        """
        pass
    def RemoveAllPlugins(self) -> None:
        """
         Removes all the registered plugins. 
        """
        pass
    def RemoveCablewayAreaNamePlugin(self) -> None:
        """
         Removes any registered Cableway area name plugin. 
        """
        pass
    def RemoveCablewayDeviceIdentifierPlugin(self) -> None:
        """
         Removes any registered Cableway device identifier plugin. 
        """
        pass
    def RemoveCablewayPostExportPlugin(self) -> None:
        """
         Removes any registered Cableway post-export plugin. 
        """
        pass
    def RemoveCablewayPreExportPlugin(self) -> None:
        """
         Removes any registered Cableway pre-export plugin. 
        """
        pass
    def RemoveCablewayUniqueNodeNamePlugin(self) -> None:
        """
         Removes any registered Cableway node unique name plugin. 
        """
        pass
    def RemoveCablewayUniqueSegmentNamePlugin(self) -> None:
        """
         Removes any registered Cableway segment unique name plugin. 
        """
        pass
    def RemoveCablewayXmlFileNamePlugin(self) -> None:
        """
         Removes any registered Cableway XML file name plugin. 
        """
        pass
    def RemoveDesignRule(self, designRuleMethodId: int) -> None:
        """
         Removes the registered design rule. 
        """
        pass
    def RemoveRSDApplicationEnterPlugin(self) -> None:
        """
         Removes any registered application enter plugin. 
        """
        pass
    def RemoveRSDApplicationExitPlugin(self) -> None:
        """
         Removes any registered application exit plugin. 
        """
        pass
    def RemoveSpoolAssemblyNamePlugin(self) -> None:
        """
         Removes any registered spool assembly name plugin. 
        """
        pass
    def RemoveSpoolNamePlugin(self) -> None:
        """
         Removes any registered spool name plugin. 
        """
        pass
    def RemoveWiringComponentNamePlugin(self) -> None:
        """
         Removes any registered wiring component name plugin, except one configured in the Application View file. 
        """
        pass
    def SetCablewayAreaNamePlugin(self, cablewayAreaNamePlugin: CustomManager.CablewayAreaNamePlugin) -> None:
        """
         Sets the plugin Routing will call to determine the area name. 
        """
        pass
    def SetCablewayDeviceIdentifierPlugin(self, cablewayDeviceIdentifierPlugin: CustomManager.CablewayDeviceIdentifierPlugin) -> None:
        """
         Sets the plugin Routing will call to determine if a device component should be
                    included in the Cableway Export. 
        """
        pass
    def SetCablewayPostExportPlugin(self, cablewayPostExportPlugin: CustomManager.CablewayPostExportPlugin) -> None:
        """
         Sets the plugin Routing will call after Cableway post-export. 
        """
        pass
    def SetCablewayPreExportPlugin(self, cablewayPreExportPlugin: CustomManager.CablewayPreExportPlugin) -> None:
        """
         Sets the plugin Routing will call after Cableway pre-export. 
        """
        pass
    def SetCablewayUniqueNodeNamePlugin(self, uniqueNodeNamePlugin: CustomManager.CablewayUniqueNodeNamePlugin) -> None:
        """
         Sets the plugin Routing will call during Cableway Export to get a new, unique name for
                    the node in the XML file that represents the given Routing.ControlPoint.
                    Note: It is this plugin's responsibility to ensure uniqueness. Routing will not
                    check the returned value to make sure it is unique.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetCablewayUniqueSegmentNamePlugin(self, uniqueSegmentNamePlugin: CustomManager.CablewayUniqueSegmentNamePlugin) -> None:
        """
         Sets the plugin Routing will call during Cableway Export to get a new, unique name for
                    the segment in the XML file that represents the given Routing.ISegment.
                    Note: It is this plugin's responsibility to ensure uniqueness. Routing will not
                    check the returned value to make sure it is unique.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetCablewayXmlFileNamePlugin(self, xmlFileNamePlugin: CustomManager.CablewayXmlFileNamePlugin) -> None:
        """
         Sets the plugin Routing will call before Cableway Export to get the name to use for
                    the Cableway XML file.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetRSDApplicationEnterPlugin(self, applicationEnterPlugin: CustomManager.RSDApplicationEnterPlugin) -> None:
        """
         Sets the plugin Routing will call when entering a Routed System Designer (RSD) application.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetRSDApplicationExitPlugin(self, applicationExitPlugin: CustomManager.RSDApplicationExitPlugin) -> None:
        """
         Sets the plugin Routing will call when exiting a Routed System Designer (RSD) application.
                    Will throw an error if one is already registered.
                
        """
        pass
    SpoolAssemblyNamePlugin = Callable[[List[NXOpen.Assemblies.Component], NXOpen.Routing.AssemblyNamePluginData], None]
    def SetSpoolAssemblyNamePlugin(self, assemblyNamePlugin: CustomManager.SpoolAssemblyNamePlugin) -> None:
        """
         Sets the spool assembly name plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    SpoolNamePlugin = Callable[[NXOpen.Part, List[NXOpen.Assemblies.Component]], None]
    def SetSpoolNamePlugin(self, spoolNamePlugin: CustomManager.SpoolNamePlugin) -> None:
        """
         Sets the spool name plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
    def SetWiringComponentNamePlugin(self, wiringComponentNamePlugin: CustomManager.ComponentNamePlugin) -> None:
        """
         Sets the wiring component name plugin.
                    Will throw an error if one is already registered.
                
        """
        pass
import NXOpen
import NXOpen.Routing
class DeleteBuilder(NXOpen.Builder): 
    """ Builder class for Delete which manages delete operations on Routing objects """
    class DeleteMethod(Enum):
        """
        Members Include: 
         |NotExtended|  Leave a gap where the part or package has been deleted. The elements connected to the ports (rts or part) will have no changes 
         |Extended|  Fill the gap left by the deleted part or package by extending the existing rts until they are connected. 
         |MergedAndSimplified|  Fill the gap left by the deleted part or package by extending the existing rts until they are connected and then, merge them when possible. 

        """
        NotExtended: int
        Extended: int
        MergedAndSimplified: int
        @staticmethod
        def ValueOf(value: int) -> DeleteBuilder.DeleteMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Method(self) -> DeleteBuilder.DeleteMethod:
        """
        Getter for property: ( DeleteBuilder.DeleteMethod NXOpen.Ro) Method
         Returns the Method type   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: DeleteBuilder.DeleteMethod):
        """
        Setter for property: ( DeleteBuilder.DeleteMethod NXOpen.Ro) Method
         Returns the Method type   
            
         
        """
        pass
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the Routing object collector   
            
         
        """
        pass
import NXOpen
class DerivedPathBuilder(NXOpen.Builder): 
    """ Builder for creating Routing segments derived from selected modeling curves. """
    class AssociativityType(Enum):
        """
        Members Include: 
         |Associative|  Make the Routing segments associative to the selected curves. 
         |Copy|  Make the Routing segments copies of the selected curves. 

        """
        Associative: int
        Copy: int
        @staticmethod
        def ValueOf(value: int) -> DerivedPathBuilder.AssociativityType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectedCurveStatus(Enum):
        """
        Members Include: 
         |Visible|  Leave the selected curves visible. 
         |Hidden|  Hide (blank) the selected curves. 

        """
        Visible: int
        Hidden: int
        @staticmethod
        def ValueOf(value: int) -> DerivedPathBuilder.SelectedCurveStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Associativity(self) -> DerivedPathBuilder.AssociativityType:
        """
        Getter for property: ( DerivedPathBuilder.AssociativityType NXOpen.Ro) Associativity
         Returns the associativity of the Routing segments created from the selected curves.  
             
         
        """
        pass
    @Associativity.setter
    def Associativity(self, associativity: DerivedPathBuilder.AssociativityType):
        """
        Setter for property: ( DerivedPathBuilder.AssociativityType NXOpen.Ro) Associativity
         Returns the associativity of the Routing segments created from the selected curves.  
             
         
        """
        pass
    @property
    def CurveSelection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurveSelection
         Returns the section containing the selected curves.  
             
         
        """
        pass
    @property
    def NumberOfPoints(self) -> int:
        """
        Getter for property: (int) NumberOfPoints
         Returns the number of points to use to approximate unassociative splines.  
             
         
        """
        pass
    @NumberOfPoints.setter
    def NumberOfPoints(self, nPoints: int):
        """
        Setter for property: (int) NumberOfPoints
         Returns the number of points to use to approximate unassociative splines.  
             
         
        """
        pass
    @property
    def SelectedCurveVisibility(self) -> DerivedPathBuilder.SelectedCurveStatus:
        """
        Getter for property: ( DerivedPathBuilder.SelectedCurveStatus NXOpen.Ro) SelectedCurveVisibility
         Returns the visible status of the selected curves.  
             
         
        """
        pass
    @SelectedCurveVisibility.setter
    def SelectedCurveVisibility(self, status: DerivedPathBuilder.SelectedCurveStatus):
        """
        Setter for property: ( DerivedPathBuilder.SelectedCurveStatus NXOpen.Ro) SelectedCurveVisibility
         Returns the visible status of the selected curves.  
             
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class DisconnectBuilder(NXOpen.Builder): 
    """ Builder for disconnecting routing objects.
        Disconnect: Takes a set of routing objects and remove the connections between them.
    """
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the route object collector   
            
         
        """
        pass
    def LogConnection(self, component1: NXOpen.Assemblies.Component, component2: NXOpen.Assemblies.Component) -> None:
        """
         The two connected components logging to connection list 
        """
        pass
    def UnlogConnection(self, component1: NXOpen.Assemblies.Component, component2: NXOpen.Assemblies.Component) -> None:
        """
         The two connected components unlogging from connection list 
        """
        pass
import NXOpen
class EditPlacementBuilder(NXOpen.Builder): 
    """ the Builder to Edit Placement """
    @property
    def PartPlacementBuilder(self) -> PartPlacementBuilder:
        """
        Getter for property: ( PartPlacementBuilder NXOpen.Ro) PartPlacementBuilder
         Returns the  NXOpen::RoutingCommon::PartPlacementBuilder    
            
         
        """
        pass
import NXOpen
import NXOpen.Routing
class EditPointBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.EditPointBuilder. """
    class Editsegmenttype(Enum):
        """
        Members Include: 
         |NotSet|  Move Point Motion 
         |Length|  Edit length type in Edit Segment Motion 
         |Angle|  Edit angle type in Edit Segment Motion 

        """
        NotSet: int
        Length: int
        Angle: int
        @staticmethod
        def ValueOf(value: int) -> EditPointBuilder.Editsegmenttype:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Motiontype(Enum):
        """
        Members Include: 
         |MovePoint|  Move Point Motion 
         |EditSegment|  Edit Segment Motion 

        """
        MovePoint: int
        EditSegment: int
        @staticmethod
        def ValueOf(value: int) -> EditPointBuilder.Motiontype:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActiveEditSegmentType(self) -> EditPointBuilder.Editsegmenttype:
        """
        Getter for property: ( EditPointBuilder.Editsegmenttype NXOpen.Ro) ActiveEditSegmentType
         Returns the edit segment type setting             
                    Allows you to specify the type of edit in edit segment motion.  
          
                  
         
        """
        pass
    @ActiveEditSegmentType.setter
    def ActiveEditSegmentType(self, editSegmentType: EditPointBuilder.Editsegmenttype):
        """
        Setter for property: ( EditPointBuilder.Editsegmenttype NXOpen.Ro) ActiveEditSegmentType
         Returns the edit segment type setting             
                    Allows you to specify the type of edit in edit segment motion.  
          
                  
         
        """
        pass
    @property
    def ActiveMotionType(self) -> EditPointBuilder.Motiontype:
        """
        Getter for property: ( EditPointBuilder.Motiontype NXOpen.Ro) ActiveMotionType
         Returns the motion type setting.  
          
                    Allows you to specify the type of edit point motion to be applied. 
                  
         
        """
        pass
    @ActiveMotionType.setter
    def ActiveMotionType(self, motionType: EditPointBuilder.Motiontype):
        """
        Setter for property: ( EditPointBuilder.Motiontype NXOpen.Ro) ActiveMotionType
         Returns the motion type setting.  
          
                    Allows you to specify the type of edit point motion to be applied. 
                  
         
        """
        pass
    @property
    def BendAngle(self) -> float:
        """
        Getter for property: (float) BendAngle
         Returns the bend angle setting.  
          
                    Allows you to specify new angle for a segment connected at the RCP or Port being edited. Reference
                    for angle measurement is the other segment connected at the RCP or Port being edited.
                    Is applicable only when there are two segments connected at RCP or Port being edited. 
                  
         
        """
        pass
    @BendAngle.setter
    def BendAngle(self, bendAngle: float):
        """
        Setter for property: (float) BendAngle
         Returns the bend angle setting.  
          
                    Allows you to specify new angle for a segment connected at the RCP or Port being edited. Reference
                    for angle measurement is the other segment connected at the RCP or Port being edited.
                    Is applicable only when there are two segments connected at RCP or Port being edited. 
                  
         
        """
        pass
    @property
    def MaintainAngle(self) -> bool:
        """
        Getter for property: (bool) MaintainAngle
         Returns the maintain angle setting.  
          
                    Allows you to specify if the angles between segments connected at the RCP or Port being edited must be fixed
                    during transformation. 
                  
         
        """
        pass
    @MaintainAngle.setter
    def MaintainAngle(self, maintainAngle: bool):
        """
        Setter for property: (bool) MaintainAngle
         Returns the maintain angle setting.  
          
                    Allows you to specify if the angles between segments connected at the RCP or Port being edited must be fixed
                    during transformation. 
                  
         
        """
        pass
    @property
    def MaintainLength(self) -> bool:
        """
        Getter for property: (bool) MaintainLength
         Returns the maintain length setting.  
          
                    Allows you to specify if the lengths of segments connected at the RCP or Port being edited must be fixed
                    during transformation. 
                  
         
        """
        pass
    @MaintainLength.setter
    def MaintainLength(self, maintainLength: bool):
        """
        Setter for property: (bool) MaintainLength
         Returns the maintain length setting.  
          
                    Allows you to specify if the lengths of segments connected at the RCP or Port being edited must be fixed
                    during transformation. 
                  
         
        """
        pass
    @property
    def PointSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) PointSelection
         Returns the routing objects that are being edited.  
           The object can be a Routing Control Point 
                    or routing port or one of their occurrences. 
                  
         
        """
        pass
    @property
    def Segment(self) -> NXOpen.Routing.ISegment:
        """
        Getter for property: ( NXOpen.Routing.ISegment) Segment
         Returns the segment setting.  
          
                    Allows you to specify a segment connected at the RCP or Port being edited.
                  
         
        """
        pass
    @Segment.setter
    def Segment(self, segment: NXOpen.Routing.ISegment):
        """
        Setter for property: ( NXOpen.Routing.ISegment) Segment
         Returns the segment setting.  
          
                    Allows you to specify a segment connected at the RCP or Port being edited.
                  
         
        """
        pass
    @property
    def SegmentLength(self) -> float:
        """
        Getter for property: (float) SegmentLength
         Returns the segment length setting.  
          
                    Allows you to specify new length for a segment connected at the RCP or Port being edited. 
                    New length is applied on the segment by moving the RCP or Port being edited. 
                  
         
        """
        pass
    @SegmentLength.setter
    def SegmentLength(self, segmentLength: float):
        """
        Setter for property: (float) SegmentLength
         Returns the segment length setting.  
          
                    Allows you to specify new length for a segment connected at the RCP or Port being edited. 
                    New length is applied on the segment by moving the RCP or Port being edited. 
                  
         
        """
        pass
    @property
    def TransformTool(self) -> TransformBlockBuilder:
        """
        Getter for property: ( TransformBlockBuilder NXOpen.Ro) TransformTool
         Returns the transform tool.  
          
                    Allows you to access the transform block object.
                  
         
        """
        pass
    def DragObjects(self) -> None:
        """
         Perform a drag operation.  
                    
                    Solves the constraint network applying the transform required to move the routing object to a new position.
                
        """
        pass
    def ResetDrag(self) -> None:
        """
         Reset a drag operation 
                    
                    Resets the position of routing objects in constraint network back to their initial position.  
                
        """
        pass
    def StartDrag(self) -> None:
        """
         Begin a drag operation.  
                    
                    Creates a constraint network of routing objects connected to the routing object that is being edited.
                
        """
        pass
    def StopDrag(self) -> None:
        """
         End a drag operation 
                    
                    Applies the transforms obtained from solving the constraint network on routing objects. 
                
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class EditTemplateParametersBuilder(NXOpen.Builder): 
    """ the Builder to Edit Template Parameters Template """
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the objects that have been selected for editing.  
          
                    The selection is limited to routing components.
                  
         
        """
        pass
    def ResetExpressionValue(self, part: NXOpen.Part, expressionName: str) -> None:
        """
                    Resets the current set value of an expression to its original unchanged value.
                
        """
        pass
    def SetExpressionValue(self, part: NXOpen.Part, expressionName: str, value: str) -> None:
        """
                    Updates the value for a specified expression on a Part, to be set on commit.
                
        """
        pass
    def SetReferenceObject(self, part: NXOpen.Assemblies.Component) -> None:
        """
                    Sets the active reference object.
                
        """
        pass
    def SetValueFromReferenceObject(self, part: NXOpen.Part, expressionName: str) -> None:
        """
                    Updates the value for a specified expression on a part to match the attibute value on the reference object.
                
        """
        pass
import NXOpen
import NXOpen.Display
class ElbowCornerOptionBuilder(NXOpen.Builder): 
    """ Contains settings for elbow placement """
    class ReferenceSetType(Enum):
        """
        Members Include: 
         |Model|  Use model 
         |EntirePart|  Entire part 
         |Empty|  Empty reference set 

        """
        Model: int
        EntirePart: int
        Empty: int
        @staticmethod
        def ValueOf(value: int) -> ElbowCornerOptionBuilder.ReferenceSetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LayerSettings(self) -> NXOpen.Display.LayerSettingsBuilder:
        """
        Getter for property: ( NXOpen.Display.LayerSettingsBuilder) LayerSettings
         Returns the value of the reference set on the builder   
            
         
        """
        pass
    def GetAllowCutElbows(self) -> bool:
        """
         Gets the value of the allow cut elbows option 
         Returns allowCutElbows (bool): .
        """
        pass
    def GetReferenceSet(self) -> ElbowCornerOptionBuilder.ReferenceSetType:
        """
         Gets the value of the reference set on the builder 
         Returns referenceSet ( ElbowCornerOptionBuilder.ReferenceSetType NXOpen.Ro): .
        """
        pass
    def SetAllowCutElbows(self, allowCutElbows: bool) -> None:
        """
         Sets the value of the allow cut elbows option 
        """
        pass
    def SetReferenceSet(self, referenceSet: ElbowCornerOptionBuilder.ReferenceSetType) -> None:
        """
         Sets the value of the reference set on the builder 
        """
        pass
    def SetReuseNode(self, nodeIdentifier: str) -> None:
        """
         Sets the reuse node on the builder 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class InsulationBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.InsulationBuilder. """
    class ApplicationType(Enum):
        """
        Members Include: 
         |EntireSegments|  Entire Segments 
         |Offsets|  offsets 
         |PointAndLength|  Point And Length 

        """
        EntireSegments: int
        Offsets: int
        PointAndLength: int
        @staticmethod
        def ValueOf(value: int) -> InsulationBuilder.ApplicationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OffsetMethodType(Enum):
        """
        Members Include: 
         |FromBothEnds| 
         |FromOneEnd| 

        """
        FromBothEnds: int
        FromOneEnd: int
        @staticmethod
        def ValueOf(value: int) -> InsulationBuilder.OffsetMethodType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class WrapType(Enum):
        """
        Members Include: 
         |NoWarp|  No wrapping 
         |OverlapSpiral|  Overlap Spiral 
         |StripedSpiral|  Striped Spiral 

        """
        NoWarp: int
        OverlapSpiral: int
        StripedSpiral: int
        @staticmethod
        def ValueOf(value: int) -> InsulationBuilder.WrapType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddInsulationOnFittings(self) -> bool:
        """
        Getter for property: (bool) AddInsulationOnFittings
         Returns the value for whether insulation be added on fitting parts or not   
            
         
        """
        pass
    @AddInsulationOnFittings.setter
    def AddInsulationOnFittings(self, addInsulationOnFittings: bool):
        """
        Setter for property: (bool) AddInsulationOnFittings
         Returns the value for whether insulation be added on fitting parts or not   
            
         
        """
        pass
    @property
    def ApplicationMethod(self) -> InsulationBuilder.ApplicationType:
        """
        Getter for property: ( InsulationBuilder.ApplicationType NXOpen.Ro) ApplicationMethod
         Returns the application method for insulation assignment.  
           It defines the way in 
                    which to create piggyback segment for insulation.   
         
        """
        pass
    @ApplicationMethod.setter
    def ApplicationMethod(self, applicationMethod: InsulationBuilder.ApplicationType):
        """
        Setter for property: ( InsulationBuilder.ApplicationType NXOpen.Ro) ApplicationMethod
         Returns the application method for insulation assignment.  
           It defines the way in 
                    which to create piggyback segment for insulation.   
         
        """
        pass
    @property
    def EndOffsetPoint(self) -> PathDimensionBuilder:
        """
        Getter for property: ( PathDimensionBuilder NXOpen.Ro) EndOffsetPoint
         Returns the end offset point that defines the end of the insulation for   
            
         
        """
        pass
    @property
    def EndPoint(self) -> PathDimensionBuilder:
        """
        Getter for property: ( PathDimensionBuilder NXOpen.Ro) EndPoint
         Returns the end point that defines the end of the insulation for   
            
         
        """
        pass
    @property
    def GapDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GapDistance
         Returns the gap distance if the  NXOpen::RoutingCommon::InsulationBuilder::WrapType 
                    is  NXOpen::RoutingCommon::InsulationBuilder::WrapTypeStripedSpiral    
            
         
        """
        pass
    @property
    def InsulationPartOccurrenceSelection(self) -> NXOpen.Assemblies.SelectComponent:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponent) InsulationPartOccurrenceSelection
         Returns the insulation component to edit.  
             
         
        """
        pass
    @property
    def OffsetMethod(self) -> InsulationBuilder.OffsetMethodType:
        """
        Getter for property: ( InsulationBuilder.OffsetMethodType NXOpen.Ro) OffsetMethod
         Returns the offsets method    
            
         
        """
        pass
    @OffsetMethod.setter
    def OffsetMethod(self, offsetMethod: InsulationBuilder.OffsetMethodType):
        """
        Setter for property: ( InsulationBuilder.OffsetMethodType NXOpen.Ro) OffsetMethod
         Returns the offsets method    
            
         
        """
        pass
    @property
    def OverlapPercentage(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OverlapPercentage
         Returns the percentage overlap if the  NXOpen::RoutingCommon::InsulationBuilder::WrapType 
                    is  NXOpen::RoutingCommon::InsulationBuilder::WrapTypeOverlapSpiral    
            
         
        """
        pass
    @property
    def SegmentCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SegmentCollector
         Returns the routing object collector to collect the segments to assign Insulation to.  
            
         
        """
        pass
    @property
    def StartOffsetPoint(self) -> PathDimensionBuilder:
        """
        Getter for property: ( PathDimensionBuilder NXOpen.Ro) StartOffsetPoint
         Returns the start offset point that defines the start of the insulation for   
            
         
        """
        pass
    @property
    def StartPoint(self) -> PathDimensionBuilder:
        """
        Getter for property: ( PathDimensionBuilder NXOpen.Ro) StartPoint
         Returns the start point that defines the start of the insulation for   
            
         
        """
        pass
    @property
    def StockSettings(self) -> NXOpen.Routing.StockBlockBuilder:
        """
        Getter for property: ( NXOpen.Routing.StockBlockBuilder) StockSettings
         Returns the stock settings for Insulation assignment.  
             
         
        """
        pass
    @property
    def SwitchStartEnd(self) -> bool:
        """
        Getter for property: (bool) SwitchStartEnd
         Returns the direction of the path   
            
         
        """
        pass
    @SwitchStartEnd.setter
    def SwitchStartEnd(self, switchStartEnd: bool):
        """
        Setter for property: (bool) SwitchStartEnd
         Returns the direction of the path   
            
         
        """
        pass
    @property
    def WrapMethod(self) -> InsulationBuilder.WrapType:
        """
        Getter for property: ( InsulationBuilder.WrapType NXOpen.Ro) WrapMethod
         Returns the  NXOpen::RoutingCommon::InsulationBuilder::WrapType  for Wrapped Insulation.  
             
         
        """
        pass
    @WrapMethod.setter
    def WrapMethod(self, wrapMethod: InsulationBuilder.WrapType):
        """
        Setter for property: ( InsulationBuilder.WrapType NXOpen.Ro) WrapMethod
         Returns the  NXOpen::RoutingCommon::InsulationBuilder::WrapType  for Wrapped Insulation.  
             
         
        """
        pass
    def CreateScalarPoint(self, partToCreatePointIn: NXOpen.Part, pointLocation: List[float]) -> NXOpen.TaggedObject:
        """
         Create point in the given part at given location 
         Returns point ( NXOpen.TaggedObject): .
        """
        pass
    def GetOrderedPath(self) -> List[NXOpen.TaggedObject]:
        """
         The ordered path for offset method 
         Returns orderedPath ( NXOpen.TaggedObject Li): .
        """
        pass
    def SuggestWrapMethodBasedOnStockSettings(self) -> InsulationBuilder.WrapType:
        """
         Returns the suggestion for NXOpen.RoutingCommon.InsulationBuilder.WrapType based on
                    Routing.StockBlockBuilder 
         Returns wrapMethod ( InsulationBuilder.WrapType NXOpen.Ro): .
        """
        pass
    def UpdatePath(self) -> None:
        """
         Updates paths for start point, end point, start offset point, end offset point 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class InsulationService(NXOpen.Object): 
    """ Represents a NXOpen.RoutingCommon.InsulationService object.
        Uses the RoutingCommon.RoutingManager.InsulationService to obtain
        an instance of this class.
     """
    def GetAllInsulatedObjectsInContainer(container: NXOpen.Assemblies.Component) -> List[NXOpen.NXObject]:
        """
         Get all insulation occurrences in current container 
         Returns insulatedObjects ( NXOpen.NXObject Li): .
        """
        pass
    def GetAssociatedInsulationComponents(coveredComponent: NXOpen.Assemblies.Component) -> List[NXOpen.Assemblies.Component]:
        """
         Gets the associated insulation components for the passed in component 
         Returns insulationComps ( NXOpen.Assemblies.Component Li): .
        """
        pass
import NXOpen
class LibraryRefreshBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.RoutingCommon.LibraryRefreshBuilder Builder for Refresh Library
        Refresh Libary: Refreshes the attributes and geometry of selected stocks and insulation. 
        Additional capability allows user to refresh attributes of fittings.
    """
    class JaRoutingcommonRefreshLibraryBuilderRefreshStatus(Enum):
        """
        Members Include: 
         |RefreshSuccessful|  Component definition refresh successful 
         |RefreshFailed|  Component definition refresh failed 
         |RefreshFailedMultipleDefinitionsFound|  Multiple matches for same component definition were found in the Reuse Library. Refresh Failed. 
         |RefreshFailedNoDefinitionFound|  Component not found in Reuse Library. Refresh Failed. 
         |RefreshFailedComponentNotLoaded|  Component not loaded. Refresh Failed. 
         |RefreshFailedRefrenceComponent|  Refrence stock and inuslation cannot be refreshed. Refresh Failed. 

        """
        RefreshSuccessful: int
        RefreshFailed: int
        RefreshFailedMultipleDefinitionsFound: int
        RefreshFailedNoDefinitionFound: int
        RefreshFailedComponentNotLoaded: int
        RefreshFailedRefrenceComponent: int
        @staticmethod
        def ValueOf(value: int) -> LibraryRefreshBuilder.JaRoutingcommonRefreshLibraryBuilderRefreshStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def RefreshPart(self, occurrence: NXOpen.NXObject) -> LibraryRefreshBuilder.JaRoutingcommonRefreshLibraryBuilderRefreshStatus:
        """
         Refreshes a single occurrence of stock, fitting or insulation.
         Returns reason ( LibraryRefreshBuilder.JaRoutingcommonRefreshLibraryBuilderRefreshStatus NXOpen.Ro):  The resulting status of refresh for the occurrence .
        """
        pass
    def SetComponentsToRefresh(self, componentStrings: List[str]) -> None:
        """
         Set the list of occurrences for fittings, stock and insulation
                to be refreshed.
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ManageInlineBehaviorBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.ManageInlineBehaviorBuilder. """
    def GetInlineBehavior(self) -> bool:
        """
         Returns true if current model element revision as inline design element. 
         Returns isInline (bool): .
        """
        pass
    def SetComponent(self, component: NXOpen.Assemblies.Component) -> None:
        """
         Sets NXOpen.Assemblies.Component of Routing Reuse type. Raises an error if passed
                    other type of object. 
        """
        pass
    def SetComponents(self, components: List[NXOpen.TaggedObject]) -> None:
        """
         Sets all components selected from UI to Builder. 
        """
        pass
    def SetInlineBehavior(self, isInline: bool) -> None:
        """
         Sets true to mark current model element revision as inline design element(which moves along with connected
                    routing design elements), false for non-inline design element (which has its own position and drives connected
                    routing design elements. Its position is never driven by inline design elements). 
                    Client should call update after this as model element revision has been logged to change. 
        """
        pass
import NXOpen
import NXOpen.Routing
class MergeBuilder(NXOpen.Builder): 
    """ the Builder to Merge Component """
    @property
    def CandidateStockComponentCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) CandidateStockComponentCollector
         Returns the routing component collector that collects candidate stock component to merge with target component   
            
         
        """
        pass
    @property
    def SimplifyPath(self) -> bool:
        """
        Getter for property: (bool) SimplifyPath
         Returns the simplify path setting   
            
         
        """
        pass
    @SimplifyPath.setter
    def SimplifyPath(self, simplifyPath: bool):
        """
        Setter for property: (bool) SimplifyPath
         Returns the simplify path setting   
            
         
        """
        pass
    @property
    def TargetStockComponentCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) TargetStockComponentCollector
         Returns the routing component collector that collects target stock component   
            
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.GeometricUtilities
import NXOpen.Routing
class MovePathBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.MovePathBuilder. Allows the user to perform 
        transform of routing objects.  If run from a non-interactive session it will return .
    """
    class CopyMode(Enum):
        """
        Members Include: 
         |NoCopy| 
         |CopyToWorkPart| 
         |CopyToTarget| 

        """
        NoCopy: int
        CopyToWorkPart: int
        CopyToTarget: int
        @staticmethod
        def ValueOf(value: int) -> MovePathBuilder.CopyMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DetachTypes(Enum):
        """
        Members Include: 
         |AlwaysMaintainConnections| 
         |DetachSelectedObjects| 

        """
        AlwaysMaintainConnections: int
        DetachSelectedObjects: int
        @staticmethod
        def ValueOf(value: int) -> MovePathBuilder.DetachTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MoveType(Enum):
        """
        Members Include: 
         |Move|  Default Move subtype.             
         |PortToPort|  Port to Port subtype.   

        """
        Move: int
        PortToPort: int
        @staticmethod
        def ValueOf(value: int) -> MovePathBuilder.MoveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CopyModeType(self) -> MovePathBuilder.CopyMode:
        """
        Getter for property: ( MovePathBuilder.CopyMode NXOpen.Ro) CopyModeType
         Returns the copy mode.  
            
         
        """
        pass
    @CopyModeType.setter
    def CopyModeType(self, copyMode: MovePathBuilder.CopyMode):
        """
        Setter for property: ( MovePathBuilder.CopyMode NXOpen.Ro) CopyModeType
         Returns the copy mode.  
            
         
        """
        pass
    @property
    def DetachType(self) -> MovePathBuilder.DetachTypes:
        """
        Getter for property: ( MovePathBuilder.DetachTypes NXOpen.Ro) DetachType
         Returns the detach type setting.  
           
                    Allows the user to specify acceptable detach types for objects that prevent the transformation of the 
                    selected objects.
                  
         
        """
        pass
    @DetachType.setter
    def DetachType(self, detachType: MovePathBuilder.DetachTypes):
        """
        Setter for property: ( MovePathBuilder.DetachTypes NXOpen.Ro) DetachType
         Returns the detach type setting.  
           
                    Allows the user to specify acceptable detach types for objects that prevent the transformation of the 
                    selected objects.
                  
         
        """
        pass
    @property
    def EndObject(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) EndObject
         Returns the end object to where the selected objects has to be moved.  
          
                The object can be port or routing control point.
                  
         
        """
        pass
    @property
    def MaintainLength(self) -> bool:
        """
        Getter for property: (bool) MaintainLength
         Returns the maintain length setting.  
           
                
                    This keeps the length of the selected segments constant through the transform operation. The adjacent 
                    segments will be modified and reconnected to the end of the moving segments as required. 
                    If this option is turned off, the segments that are moved may extend or trim back to connect to adjacent segments. 
                  
         
        """
        pass
    @MaintainLength.setter
    def MaintainLength(self, maintainLength: bool):
        """
        Setter for property: (bool) MaintainLength
         Returns the maintain length setting.  
           
                
                    This keeps the length of the selected segments constant through the transform operation. The adjacent 
                    segments will be modified and reconnected to the end of the moving segments as required. 
                    If this option is turned off, the segments that are moved may extend or trim back to connect to adjacent segments. 
                  
         
        """
        pass
    @property
    def Motion(self) -> NXOpen.GeometricUtilities.ModlMotion:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ModlMotion) Motion
         Returns the transformation to apply to the selected routing objects.  
             
         
        """
        pass
    @property
    def MoveSubType(self) -> MovePathBuilder.MoveType:
        """
        Getter for property: ( MovePathBuilder.MoveType NXOpen.Ro) MoveSubType
         Returns the type of move operation, either move or port to port method   
            
         
        """
        pass
    @MoveSubType.setter
    def MoveSubType(self, move_type: MovePathBuilder.MoveType):
        """
        Setter for property: ( MovePathBuilder.MoveType NXOpen.Ro) MoveSubType
         Returns the type of move operation, either move or port to port method   
            
         
        """
        pass
    @property
    def NumberOfCopies(self) -> int:
        """
        Getter for property: (int) NumberOfCopies
         Returns the number of times to copy the selected objects   
            
         
        """
        pass
    @NumberOfCopies.setter
    def NumberOfCopies(self, numberOfCopies: int):
        """
        Setter for property: (int) NumberOfCopies
         Returns the number of times to copy the selected objects   
            
         
        """
        pass
    @property
    def PathSelection(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) PathSelection
         Returns the objects that make up the path that needs to be transformed.  
          
                    The objects can be segments, routing control points and routing components that have properties that 
                    make them suitable to be moved by the routing application.
                  
         
        """
        pass
    @property
    def Preview(self) -> bool:
        """
        Getter for property: (bool) Preview
         Returns the preview setting   
            
         
        """
        pass
    @Preview.setter
    def Preview(self, preview: bool):
        """
        Setter for property: (bool) Preview
         Returns the preview setting   
            
         
        """
        pass
    @property
    def RotationAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationAngle
         Returns the rotation angle, units as per customer defaults.  
            
         
        """
        pass
    @property
    def StartObject(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) StartObject
         Returns the start object from where the selected objects has to be moved.  
          
                The object can be port or routing control point.
                  
         
        """
        pass
    @property
    def TargetAssembly(self) -> NXOpen.Assemblies.SelectComponent:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponent) TargetAssembly
         Returns the target assembly.  
             
         
        """
        pass
    def DragObjects(self) -> None:
        """
         Perform a drag operation.  
        """
        pass
    def ResetDrag(self) -> None:
        """
         Reset a drag operation 
        """
        pass
    def StartDrag(self) -> None:
        """
         Begin a drag operation.  
        """
        pass
    def StopDrag(self) -> None:
        """
         End a drag operation 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class OffsetOutletStockBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.OffsetOutletStockBuilder. """
    class OutletSelectionType(Enum):
        """
        Members Include: 
         |AlignFaces|  Entire Face 
         |OffsetRoutePath|  Entire Part 

        """
        AlignFaces: int
        OffsetRoutePath: int
        @staticmethod
        def ValueOf(value: int) -> OffsetOutletStockBuilder.OutletSelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def HeaderFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) HeaderFace
         Returns the header face selection   
            
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns the Offset Distance   
            
         
        """
        pass
    @property
    def OutletComponent(self) -> NXOpen.Assemblies.SelectComponent:
        """
        Getter for property: ( NXOpen.Assemblies.SelectComponent) OutletComponent
         Returns the select outlet comp   
            
         
        """
        pass
    @property
    def OutletFace(self) -> NXOpen.SelectFace:
        """
        Getter for property: ( NXOpen.SelectFace) OutletFace
         Returns the outlet face slection   
            
         
        """
        pass
    @property
    def Type(self) -> OffsetOutletStockBuilder.OutletSelectionType:
        """
        Getter for property: ( OffsetOutletStockBuilder.OutletSelectionType NXOpen.Ro) Type
         Returns a return  NXOpen::RoutingCommon::OffsetOutletStockBuilder::OutletSelectionType   method.  
             
         
        """
        pass
    @Type.setter
    def Type(self, type: OffsetOutletStockBuilder.OutletSelectionType):
        """
        Setter for property: ( OffsetOutletStockBuilder.OutletSelectionType NXOpen.Ro) Type
         Returns a return  NXOpen::RoutingCommon::OffsetOutletStockBuilder::OutletSelectionType   method.  
             
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.PDM
import NXOpen.Placement
import NXOpen.Routing
class PartPlacementBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.PartPlacementBuilder. """
    class FlowSense(Enum):
        """
        Members Include: 
         |Undefined| 
         |FavouringFlow| 
         |AganistFlow| 

        """
        Undefined: int
        FavouringFlow: int
        AganistFlow: int
        @staticmethod
        def ValueOf(value: int) -> PartPlacementBuilder.FlowSense:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlacementValidationStatus(Enum):
        """
        Members Include: 
         |Success|  part placement is successful as expected 
         |PartNotConnectedToRout|  after placement connection should have been built with routing system but it was not 

        """
        Success: int
        PartNotConnectedToRout: int
        @staticmethod
        def ValueOf(value: int) -> PartPlacementBuilder.PlacementValidationStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositionAsType(Enum):
        """
        Members Include: 
         |Routing|  position as inline routing fitting 
         |Equipment|  position as equipment   

        """
        Routing: int
        Equipment: int
        @staticmethod
        def ValueOf(value: int) -> PartPlacementBuilder.PositionAsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RebuildPathOption(Enum):
        """
        Members Include: 
         |NotSet| 
         |BulkReplacement| 
         |Automatic| 

        """
        NotSet: int
        BulkReplacement: int
        Automatic: int
        @staticmethod
        def ValueOf(value: int) -> PartPlacementBuilder.RebuildPathOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplatePartHandlingOption(Enum):
        """
        Members Include: 
         |Instantiate| 
         |Clone| 

        """
        Instantiate: int
        Clone: int
        @staticmethod
        def ValueOf(value: int) -> PartPlacementBuilder.TemplatePartHandlingOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowOverrideOfLocationSpecification(self) -> bool:
        """
        Getter for property: (bool) AllowOverrideOfLocationSpecification
         Returns the check, whether to determine specification from location customer default should be overridden or not.  
             
         
        """
        pass
    @AllowOverrideOfLocationSpecification.setter
    def AllowOverrideOfLocationSpecification(self, overrideLocationBasedSpec: bool):
        """
        Setter for property: (bool) AllowOverrideOfLocationSpecification
         Returns the check, whether to determine specification from location customer default should be overridden or not.  
             
         
        """
        pass
    @property
    def ComponentsToEditCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) ComponentsToEditCollector
         Returns the  NXOpen::Routing::RouteObjectCollector  that collects components to edit   
            
         
        """
        pass
    @property
    def LogicalDesignObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) LogicalDesignObject
         Returns the mapping logical design object   
            
         
        """
        pass
    @LogicalDesignObject.setter
    def LogicalDesignObject(self, logicalDesignObject: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) LogicalDesignObject
         Returns the mapping logical design object   
            
         
        """
        pass
    @property
    def MergeAndSimplify(self) -> bool:
        """
        Getter for property: (bool) MergeAndSimplify
         Returns  
                Flag to decide whether to merge and simplify stock components or not.  
          
                 
         
                
                A flag that determines whether to merge and simplify stock components or not. This flag only has an effect in edit mode.
                  
         
        """
        pass
    @MergeAndSimplify.setter
    def MergeAndSimplify(self, mergeAndSimplify: bool):
        """
        Setter for property: (bool) MergeAndSimplify
         Returns  
                Flag to decide whether to merge and simplify stock components or not.  
          
                 
         
                
                A flag that determines whether to merge and simplify stock components or not. This flag only has an effect in edit mode.
                  
         
        """
        pass
    @property
    def RebuildPathOptions(self) -> PartPlacementBuilder.RebuildPathOption:
        """
        Getter for property: ( PartPlacementBuilder.RebuildPathOption NXOpen.Ro) RebuildPathOptions
         Returns the rebuild path options    
            
         
        """
        pass
    @RebuildPathOptions.setter
    def RebuildPathOptions(self, rebuildPathOptions: PartPlacementBuilder.RebuildPathOption):
        """
        Setter for property: ( PartPlacementBuilder.RebuildPathOption NXOpen.Ro) RebuildPathOptions
         Returns the rebuild path options    
            
         
        """
        pass
    @property
    def SubdivideSegmentForFixturePartPlacementFlag(self) -> bool:
        """
        Getter for property: (bool) SubdivideSegmentForFixturePartPlacementFlag
         Returns  
                the subdivide segment for fixture part placement flag
                 
          
          
         
                
                A flag that determines whether to add a routing control point at the location of the placed part's fixture port. This flag only has an effect when the solution locates a fixture port on a routing path.
                  
         
        """
        pass
    @SubdivideSegmentForFixturePartPlacementFlag.setter
    def SubdivideSegmentForFixturePartPlacementFlag(self, subdivideSegment: bool):
        """
        Setter for property: (bool) SubdivideSegmentForFixturePartPlacementFlag
         Returns  
                the subdivide segment for fixture part placement flag
                 
          
          
         
                
                A flag that determines whether to add a routing control point at the location of the placed part's fixture port. This flag only has an effect when the solution locates a fixture port on a routing path.
                  
         
        """
        pass
    @property
    def SystemPartTag(self) -> str:
        """
        Getter for property: (str) SystemPartTag
         Returns the system part tag   
            
         
        """
        pass
    @SystemPartTag.setter
    def SystemPartTag(self, systemPartTag: str):
        """
        Setter for property: (str) SystemPartTag
         Returns the system part tag   
            
         
        """
        pass
    def ApplySecondaryPlacementParts(self) -> List[NXOpen.Assemblies.Component]:
        """
         Process the post placement parts (ex. placement of flange after the valve and do geometry operations like split stock, etc).
                    This method will also prepare data needed to build connectivity (connectivity will be built in final commit).
         Returns secondaryPlacementComponents ( NXOpen.Assemblies.Component Li): .
        """
        pass
    def AutoAssignAttributes(self) -> None:
        """
         Auto assign the auto assignable attributes of all PDM.LogicalObjects that were created during part placement operation. 
        """
        pass
    def CacheInterfaceNodesFromOtherAssembly(self, targetObject: NXOpen.TaggedObject) -> None:
        """
         Caches interface nodes from other assemblies on builder.
                This API infers interface nodes within design in context scenarios when the Create Interpart Link option is disabled
        """
        pass
    def CleanUpPlacementEngineRelatedData(self) -> None:
        """
         Clean up placement engine related data
        """
        pass
    def CommitThisPlacement(self) -> PartPlacementBuilder.PlacementValidationStatus:
        """
         Commits the current placement operation. 
         Returns placementValidationStatus ( PartPlacementBuilder.PlacementValidationStatus NXOpen.Ro): .
        """
        pass
    def CopyAttributesToPartToPlace(self, sourcePartOccurrence: NXOpen.Assemblies.Component) -> None:
        """
         Copies user defined attributes from given component to the component to place. 
                The attributes attributes are copied from instance to instance and component to component. 
                Attributes will be copied only if the given component and the component to place are of same part. 
        """
        pass
    def CreatePartOccurrenceToPlace(self, referenceSet: str, layer: int) -> NXOpen.Assemblies.Component:
        """
         Creates the Assemblies.Component for part to place with given reference set and layer.
                    The created component will be used to generate placement solutions. Error will be raised if part to place is not loaded. 
         Returns partOccurrence ( NXOpen.Assemblies.Component):  created part occurrence .
        """
        pass
    def DesignateComponentForPlacementSolutionComputation(self, partOccurrence: NXOpen.Assemblies.Component) -> None:
        """
         Designates the component to be used for placement solution computation.
                When relocating a flange-valve-flange unit, typically the intent is to relocate the valve. Flanges just follow the valve to its new location.
                In such case, user should designate valve as the component to be used for placement solution computation.
                If user does not designate any component, placement solutions will be computed on all components which may result in a large number of solutions to choose from.
                
        """
        pass
    def GetAngleOfOutletFittingOnStock(self) -> float:
        """
         Gets the angle of outlet fitting on stock surface. 
         Returns angleOfOutletFittingOnStock (float): .
        """
        pass
    def GetErrorCodeForPlacementSolution(self, placementSolution: NXOpen.Placement.PlacementSolution) -> int:
        """
         Returns the error code for a placement solution. A non-zero error code may suggest whether there
                will be any design rule validation due to the given placement solution. 
         Returns errorCode (int): .
        """
        pass
    def GetFilteredPlacementSolutions(self) -> List[NXOpen.Placement.PlacementSolution]:
        """
         Filters placement solutions based existing filtration flags in builder ex. primary. 
         Returns placementSolutions ( NXOpen.Placement.PlacementSolution Li): .
        """
        pass
    def GetLibraryDefinedAttributeHolder(self) -> NXOpen.Routing.AttributeHolder:
        """
         Gets the attribute holder for library defined attributes on placed part instance 
         Returns libraryDefinedAttributeHolder ( NXOpen.Routing.AttributeHolder): .
        """
        pass
    def GetLogicalObjects(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Returns the PDM.LogicalObjects that were created during part placement operation. 
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetLogicalObjectsHavingUnassignedRequiredAttributes(self) -> List[NXOpen.PDM.LogicalObject]:
        """
         Returns the PDM.LogicalObjects having unassigned non-auto-assignable required attributes. 
         Returns logicalObjects ( NXOpen.PDM.LogicalObject Li): .
        """
        pass
    def GetOutletFittingPlacementLocation(self) -> float:
        """
         Gets the segment percentage from source control point where outlet fitting is placed. 
         Returns perOnSegFromSourceControlPt (float): .
        """
        pass
    def InitializePlacementEngineBuilder(self) -> NXOpen.Placement.PlacementEngineBuilder:
        """
         Initializes the Placement Engine builder with input already present in the Part Placement Builder.  
         Returns placementEngineBuilder ( NXOpen.Placement.PlacementEngineBuilder): .
        """
        pass
    def LoadPart(self) -> NXOpen.BasePart:
        """
         Loads the BasePart to place.  
         Returns part ( NXOpen.BasePart):  loaded part .
        """
        pass
    def PerformOperationsAfterPlacement(self) -> None:
        """
         Process any operations after placement for example cutting an elbow
        """
        pass
    def PrepareDataForConnectivity(self) -> None:
        """
         Prepare data to build connectivity for all placed parts. 
                    Things like computation of new stock DE (resultant of splitting) will happen here. 
                
        """
        pass
    def ProcessComponentsForEdit(self) -> None:
        """
         Processes the Assemblies.Components to edit their placement 
        """
        pass
    def ProcessPlacedPart(self) -> None:
        """
         Processes the placed part. This might split the target stock geometry. 
                This method will also prepare data needed to build connectivity (connectivity will be built in final commit).
        """
        pass
    def ProcessPostPlaceParts(self) -> List[NXOpen.Assemblies.Component]:
        """
         Process the post placement parts (ex. placement of flange after the valve and do geometry operations like split stock, etc).
                    This method will also prepare data needed to build connectivity (connectivity will be built in final commit).
         Returns postPlaceComponents ( NXOpen.Assemblies.Component Li): .
        """
        pass
    def ResetAttributesOnLibraryDefinedAttributeHolder(self) -> None:
        """
         Resets the attribute holder for library defined attributes for part to be placed
                    This API is recommended to be used before assigning attributes onto builder so as to ensure part placement to function correctly 
        """
        pass
    def RotatePlaceableObjectByAngle(self, rotationAngle: float) -> None:
        """
         Rotates the fitting by the specified angle along the plane perpendicular to the vector defined by the engaged port. 
        """
        pass
    def SetAngleOfOutletFittingOnStock(self, angleOfOutletFittingOnStock: float) -> None:
        """
         Sets the angle of outlet fitting on stock surface.
        """
        pass
    def SetClassificationObjectIdentifier(self, classificationObjectId: str) -> None:
        """
         Sets the identifier of the classification object associated with the part to place 
        """
        pass
    def SetExistingPartBeingPlaced(self, isExistingPartBeingPlaced: bool) -> None:
        """
         Sets whether placement is performed by selecting an existing part from the assembly. 
        """
        pass
    def SetFileSpecificationOfPartToPlace(self, filename: str) -> None:
        """
         Sets the file specification of the part to place 
        """
        pass
    def SetFlowDirectionAtPlacementLocation(self, flowDirectionAtPlacementLoc: NXOpen.Vector3d) -> None:
        """
         Sets flow direction at placement location on builder.
        """
        pass
    def SetFlowSenseAtPlacementLocation(self, flowSenseAtPlacementLoc: PartPlacementBuilder.FlowSense) -> None:
        """
         Sets flow sense at placement location on builder.
        """
        pass
    def SetLinkedCompositeCurve(self, targetObject: NXOpen.TaggedObject) -> None:
        """
         Sets linked composite curve on builder.
        """
        pass
    def SetOutletFittingPlacementLocation(self, perOnSegFromSourceControlPt: float) -> None:
        """
         Sets the segment percentage from source control point where outlet fitting will be placed. 
        """
        pass
    def SetPositionAsOption(self, positioningType: PartPlacementBuilder.PositionAsType) -> None:
        """
         Sets the positioning option NXOpen.RoutingCommon.PartPlacementBuilder.PositionAsType on the builder. 
        """
        pass
    def SetPrimarySolutionsFlag(self, showPrimarySolutions: bool) -> None:
        """
         Sets the primary solutions flag on builder. 
        """
        pass
    def SetReferenceObjectForPlacement(self, referenceObject: NXOpen.TaggedObject, referencePositionPoint: NXOpen.Point3d) -> None:
        """
         Sets the reference object and reference location for placement.  
        """
        pass
    def SetSpecificationMatchingOnTargetAndIncomingParts(self, specificationMatchingOnTargetAndIncomingParts: bool) -> None:
        """
         Set the flag if target and incoming parts having same specification or not 
        """
        pass
    def SetTemplatePartHandlingOption(self, templatePartOption: PartPlacementBuilder.TemplatePartHandlingOption) -> None:
        """
         Sets the template part handling option NXOpen.RoutingCommon.PartPlacementBuilder.TemplatePartHandlingOption on the builder. 
        """
        pass
    def TranslatePart(self, referenceObject: NXOpen.TaggedObject, newLocationOfReferenceObject: NXOpen.Point3d) -> None:
        """
         Translates the entire part with the given object (typically a port) as a reference such that
                    the reference object is at the specified location at the end of translation.
                    The specified location should be such a way that atleast one port will always lie on the
                    selected segment else it will throw error.
        """
        pass
    def UpdateLayer(self, layerNumber: int) -> None:
        """
         Updates the layer for the Design Elements created during part placement operation. 
        """
        pass
    def UpdateReferenceSet(self, referenseSetName: str) -> None:
        """
         Updates the reference set for the Design Elements created during part placement operation. 
        """
        pass
    def UpdateSpecificationAttributeOnParts(self) -> None:
        """
         Updates the specification attribute on the parts. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PathDimensionBuilder(NXOpen.GeometricUtilities.OnPathDimensionBuilder): 
    """ Represents NXOpen.RoutingCommon.PathDimensionBuilder. """
    def GetOrderedPathCurves(self) -> List[NXOpen.Curve]:
        """
         Gets the ordered paths 
         Returns pathCurves ( NXOpen.Curve Li): .
        """
        pass
    def GetValueAsLength(self) -> float:
        """
         Gets the value of expression always as length. If percent has been used, this will covert the value in percentage to length. 
         Returns valueAsLength (float): .
        """
        pass
    def SetOrderedPathCurves(self, pathCurves: List[NXOpen.Curve]) -> None:
        """
         Sets the ordered paths 
        """
        pass
    def UpdateExpression(self) -> None:
        """
         Updates the expression 
        """
        pass
import NXOpen
class PathTransitionBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PathTransitionBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PathTransitionBuilder) -> None:
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
    def Erase(self, obj: PathTransitionBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PathTransitionBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PathTransitionBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PathTransitionBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PathTransitionBuilder NXOpen.Ro):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PathTransitionBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PathTransitionBuilder List[NXOpen.):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PathTransitionBuilder) -> None:
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
    def SetContents(self, objects: List[PathTransitionBuilder]) -> None:
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
    def Swap(self, object1: PathTransitionBuilder, object2: PathTransitionBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class PathTransitionBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.PathTransitionBuilder. Allows the user to create 
        a routing path transition.
    """
    class HealOrientation(Enum):
        """
        Members Include: 
         |Wcs| 
         |Absolute| 
         |Start| 
         |End| 
         |NewCsys| 

        """
        Wcs: int
        Absolute: int
        Start: int
        End: int
        NewCsys: int
        @staticmethod
        def ValueOf(value: int) -> PathTransitionBuilder.HealOrientation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TraversalOrder(Enum):
        """
        Members Include: 
         |Xyz| 
         |Xzy| 
         |Yzx| 
         |Yxz| 
         |Zxy| 
         |Zyx| 
         |Invalid| 

        """
        Xyz: int
        Xzy: int
        Yzx: int
        Yxz: int
        Zxy: int
        Zyx: int
        Invalid: int
        @staticmethod
        def ValueOf(value: int) -> PathTransitionBuilder.TraversalOrder:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Direct| 
         |Heal| 
         |Intersect| 

        """
        Direct: int
        Heal: int
        Intersect: int
        @staticmethod
        def ValueOf(value: int) -> PathTransitionBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddExtensionToggle(self) -> bool:
        """
        Getter for property: (bool) AddExtensionToggle
         Returns the toggle to set forwardbackward extensions for this transition.  
             
         
        """
        pass
    @AddExtensionToggle.setter
    def AddExtensionToggle(self, extensionToggle: bool):
        """
        Setter for property: (bool) AddExtensionToggle
         Returns the toggle to set forwardbackward extensions for this transition.  
             
         
        """
        pass
    @property
    def BackwardExtension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BackwardExtension
         Returns the backward extension length for this transition.  
             
         
        """
        pass
    @BackwardExtension.setter
    def BackwardExtension(self, backwardExtension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) BackwardExtension
         Returns the backward extension length for this transition.  
             
         
        """
        pass
    @property
    def BoxOrientation(self) -> PathTransitionBuilder.HealOrientation:
        """
        Getter for property: ( PathTransitionBuilder.HealOrientation NXOpen.Ro) BoxOrientation
         Returns the box orientation for heal transition traversal order.  
             
         
        """
        pass
    @BoxOrientation.setter
    def BoxOrientation(self, boxOrientation: PathTransitionBuilder.HealOrientation):
        """
        Setter for property: ( PathTransitionBuilder.HealOrientation NXOpen.Ro) BoxOrientation
         Returns the box orientation for heal transition traversal order.  
             
         
        """
        pass
    @property
    def ConnectedObject(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) ConnectedObject
         Returns the object that the end point of this path transition connects to.  
           If the transition
                    connects to a port or a routing control point, it is required to set that object as the connected object to
                    build connectivity.   
         
        """
        pass
    @ConnectedObject.setter
    def ConnectedObject(self, connectedObject: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) ConnectedObject
         Returns the object that the end point of this path transition connects to.  
           If the transition
                    connects to a port or a routing control point, it is required to set that object as the connected object to
                    build connectivity.   
         
        """
        pass
    @property
    def EndPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPoint
         Returns the end point that defines the end of the path transition.  
             
         
        """
        pass
    @EndPoint.setter
    def EndPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPoint
         Returns the end point that defines the end of the path transition.  
             
         
        """
        pass
    @property
    def ExtensionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ExtensionVector
         Returns the direction for extension segments.  
             
         
        """
        pass
    @ExtensionVector.setter
    def ExtensionVector(self, extensionVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ExtensionVector
         Returns the direction for extension segments.  
             
         
        """
        pass
    @property
    def ForwardExtension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForwardExtension
         Returns the forward extension length for this transition.  
             
         
        """
        pass
    @ForwardExtension.setter
    def ForwardExtension(self, forwardExtension: NXOpen.Expression):
        """
        Setter for property: ( NXOpen.Expression) ForwardExtension
         Returns the forward extension length for this transition.  
             
         
        """
        pass
    @property
    def HealSolutionCsys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) HealSolutionCsys
         Returns the user-defined coordinate system for the heal box orientation.  
             
         
        """
        pass
    @HealSolutionCsys.setter
    def HealSolutionCsys(self, coordinateSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) HealSolutionCsys
         Returns the user-defined coordinate system for the heal box orientation.  
             
         
        """
        pass
    @property
    def HealTraversalOrder(self) -> PathTransitionBuilder.TraversalOrder:
        """
        Getter for property: ( PathTransitionBuilder.TraversalOrder NXOpen.Ro) HealTraversalOrder
         Returns the heal transition traversal order the path takes to reach the transition end point.  
             
         
        """
        pass
    @HealTraversalOrder.setter
    def HealTraversalOrder(self, healTraversalOrder: PathTransitionBuilder.TraversalOrder):
        """
        Setter for property: ( PathTransitionBuilder.TraversalOrder NXOpen.Ro) HealTraversalOrder
         Returns the heal transition traversal order the path takes to reach the transition end point.  
             
         
        """
        pass
    @property
    def PathForwardThroughExtensionVector(self) -> bool:
        """
        Getter for property: (bool) PathForwardThroughExtensionVector
         Returns the toggle setting to define whether the path passes forward through the extension vector, or backward.  
             
         
        """
        pass
    @PathForwardThroughExtensionVector.setter
    def PathForwardThroughExtensionVector(self, isPathForwardThroughExtensionVector: bool):
        """
        Setter for property: (bool) PathForwardThroughExtensionVector
         Returns the toggle setting to define whether the path passes forward through the extension vector, or backward.  
             
         
        """
        pass
    @property
    def TransitionType(self) -> PathTransitionBuilder.Type:
        """
        Getter for property: ( PathTransitionBuilder.Type NXOpen.Ro) TransitionType
         Returns the type of transition the path takes to reach the transition end point.  
             
         
        """
        pass
    @TransitionType.setter
    def TransitionType(self, transitionType: PathTransitionBuilder.Type):
        """
        Setter for property: ( PathTransitionBuilder.Type NXOpen.Ro) TransitionType
         Returns the type of transition the path takes to reach the transition end point.  
             
         
        """
        pass
import NXOpen
class PathTransitionListManagerBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.PathTransitionListManagerBuilder. 
        Allows the user to create a routing path defined by path points and transitions.
    """
    @property
    def InterPartSelection(self) -> bool:
        """
        Getter for property: (bool) InterPartSelection
         Returns the associative inter part selection setting.  
             
         
        """
        pass
    @InterPartSelection.setter
    def InterPartSelection(self, interPartSelection: bool):
        """
        Setter for property: (bool) InterPartSelection
         Returns the associative inter part selection setting.  
             
         
        """
        pass
    @property
    def PathTransitionBuilderList(self) -> PathTransitionBuilderList:
        """
        Getter for property: ( PathTransitionBuilderList NXOpen.Ro) PathTransitionBuilderList
         Returns the list of path transition builders that describe the path.  
             
         
        """
        pass
    def CacheInterfaceNodesFromOtherAssembly(self, targetObject: NXOpen.TaggedObject) -> None:
        """
         Caches interface nodes from other assemblies on builder.
                This API infers interface nodes within design in context scenarios when the Create Interpart Link option is disabled
        """
        pass
    def CreatePathTransitionBuilder(self, part: NXOpen.Part) -> PathTransitionBuilder:
        """
         Creates a NXOpen.RoutingCommon.PathTransitionBuilder object. 
         Returns transitionBuilder ( PathTransitionBuilder NXOpen.Ro): .
        """
        pass
    def SetLinkedCompositeCurve(self, targetObject: NXOpen.TaggedObject) -> None:
        """
         Sets linked composite curve on builder.
        """
        pass
import NXOpen
import NXOpen.Routing
class ReparentPartsBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.RoutingCommon.ReparentPartsBuilder builder. 
     """
    class StockActionType(Enum):
        """
        Members Include: 
         |CreateNew| 
         |TransferExisting| 

        """
        CreateNew: int
        TransferExisting: int
        @staticmethod
        def ValueOf(value: int) -> ReparentPartsBuilder.StockActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionType(self) -> ReparentPartsBuilder.StockActionType:
        """
        Getter for property: ( ReparentPartsBuilder.StockActionType NXOpen.Ro) ActionType
         Returns the type of action being assigned on selected stock.  
             
         
        """
        pass
    @ActionType.setter
    def ActionType(self, actionType: ReparentPartsBuilder.StockActionType):
        """
        Setter for property: ( ReparentPartsBuilder.StockActionType NXOpen.Ro) ActionType
         Returns the type of action being assigned on selected stock.  
             
         
        """
        pass
    @property
    def AllowSelectionOfLiveStock(self) -> bool:
        """
        Getter for property: (bool) AllowSelectionOfLiveStock
         Returns the value for whether allow selection of live stock   
            
         
        """
        pass
    @AllowSelectionOfLiveStock.setter
    def AllowSelectionOfLiveStock(self, allowSelectionOfLiveStock: bool):
        """
        Setter for property: (bool) AllowSelectionOfLiveStock
         Returns the value for whether allow selection of live stock   
            
         
        """
        pass
    @property
    def SelectedParts(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SelectedParts
         Returns the selected parts to be assigned to new parents are returned.  
              
         
        """
        pass
    def ShowStockSummary(self) -> None:
        """
         Perform the operation to show stock information of list of stocks in current work part 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class RoutingManager(NXOpen.Object): 
    """ Represents an NXOpen.RoutingCommon.RoutingManager object.  """
    class AppType(Enum):
        """
        Members Include: 
         |NotSet|  Not currently in any of the routing applications. 
         |RsdMechanical| In RSD Mechanical  
         |RsdElectrical| In RSd Electrical  

        """
        NotSet: int
        RsdMechanical: int
        RsdElectrical: int
        @staticmethod
        def ValueOf(value: int) -> RoutingManager.AppType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConnectionType(Enum):
        """
        Members Include: 
         |Unknown|  Connection type is unknown. 
         |Butt|  Butt weld  
         |Fillet|  Fillet weld  
         |Threaded|  Threaded  

        """
        Unknown: int
        Butt: int
        Fillet: int
        Threaded: int
        @staticmethod
        def ValueOf(value: int) -> RoutingManager.ConnectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BuilderFactory() -> BuilderFactory:
        """
          Returns a  NXOpen::RoutingCommon::BuilderFactory  object.  Use this object
                     to create specific routing builders.
                
        """
        pass
    @property
    def InsulationService() -> InsulationService:
        """
          Returns a  NXOpen::RoutingCommon::InsulationService  object.  Use this object
                     for specific Routing  Insulation service
                
        """
        pass
    @property
    def OverlapCornerCollection() -> OverlapCornerCollection:
        """
         This is an internal API and can be changed at any time 
        """
        pass
    def ConditionAssemblyForTraditionalRouting(part: NXOpen.Part) -> bool:
        """
         Modifies given Routed System Designer Assembly so that it can be used in Traditional Routing Applications. 
                This operation will succeed only if the given assembly does not have any stock or insulation component.
                Inline fitting components will be processed. 
         Returns success (bool): .
        """
        pass
    def CreateStockComponent(part: NXOpen.Part, stockPartNumber: str, points: List[NXOpen.Point3d]) -> NXOpen.Assemblies.Component:
        """
          Creates the stocks by using provided points in a stock component. 
         Returns stockComponent ( NXOpen.Assemblies.Component):  Created stock component .
        """
        pass
    def CreateWiringComponent(part: NXOpen.Part, componentName: str) -> NXOpen.Assemblies.Component:
        """
         Creates wiring component in the given part.
                   The operation also sets wiring component into part data manager.
                   It does not check if there is existing wiring component in workpart
                   before creating a new wiring component 
         Returns wiringComponent ( NXOpen.Assemblies.Component):  Created wiring component .
        """
        pass
    def GetPortsConnectingPartOccurrencesForPipeJoin(partOccurrence1: NXOpen.Assemblies.Component, partOccurrence2: NXOpen.Assemblies.Component) -> Tuple[List[NXOpen.Routing.Port], float, RoutingManager.ConnectionType]:
        """
          Returns the ports connected to two part occurrences, if any, the engagement value of the ports or zero if no engagement and connection type 
         Returns A tuple consisting of (ports, engagement, connectionType). 
         - ports is:  NXOpen.Routing.Port Li. .
         - engagement is: float.
         - connectionType is:  RoutingManager.ConnectionType NXOpen.Ro.

        """
        pass
    def GetSavedDisciplineAndSpecificationFromThePart(part: NXOpen.Part) -> Tuple[str, str]:
        """
         Returns saved discipline and specification from the given part. Only Routed System Assembly part can 
                    have discipline and specification saved in it. 
         Returns A tuple consisting of (discipline, specification). 
         - discipline is: str. Name of the discipline .
         - specification is: str. Name of the specification .

        """
        pass
    def InitializeRoutedSystemDesigner(appType: RoutingManager.AppType) -> None:
        """
         Enters RSD application by setting application type and loading the required Application View file 
        """
        pass
    def IsInsulationComponentPart(part: NXOpen.BasePart) -> bool:
        """
         Checks if the part is a insulation component part
         Returns isInsulationComponent (bool):  Returns true if the part is a Routed System Designer part. .
        """
        pass
    def IsReusableComponentPart(part: NXOpen.BasePart) -> bool:
        """
         Checks if the part is a reusable component part  
         Returns isReusableComponentPart (bool):  Returns true if the part is a routed system designer part. .
        """
        pass
    def IsRouteSystemAssembly(part: NXOpen.Part) -> bool:
        """
         Checks if the part is a route system assembly  
         Returns isRouteSytemAssembly (bool):  Returns true if the part is a routed system designer part. .
        """
        pass
    def IsStockComponentPart(part: NXOpen.BasePart) -> bool:
        """
         Checks if the part is a stock component part 
         Returns isStockComponent (bool):  Returns true if the part is a Routed System Designer part. .
        """
        pass
    def LoadData(part: NXOpen.Part) -> bool:
        """
          Loads Routing data under the work part so that Routing operations can be performed. 
         Returns dataLoaded (bool):  Returns true if the Routing data under the work part was loaded by this method. .
        """
        pass
    def MakeComponentReusable(component: NXOpen.Assemblies.Component) -> bool:
        """
         Makes a component a reusable component for Routed System Designer provided the component is not already a Routed System Designer component. 
                It is recommended to check NXOpen.RoutingCommon.RoutingManager.IsReusableComponentPart before calling this API 
         Returns madeComponentReusable (bool):  Returns true if the component was made reusable. It can return false even in cases where the component was already reusable. .
        """
        pass
    def PerformDetachOperationOnPort(port: NXOpen.Routing.Port) -> bool:
        """
         Performs Detach Operation on port
         Returns isDetachPerformed (bool):  Returns true if the detach operation is performed. .
        """
        pass
    def PerformDetachOperationOnRcp(rcp: NXOpen.Routing.ControlPoint) -> bool:
        """
         Performs Detach Operation on rcp 
         Returns isDetachPerformed (bool):  Returns true if the detach operation is performed. .
        """
        pass
    def RestoreDisciplineAndSpecificationFromThePart(part: NXOpen.Part) -> Tuple[bool, bool]:
        """
         Sets saved discipline and specification from the given part as active. Only Routed System Assembly part can
                    have discipline and specification saved in it. If saved discipline or specification is no longer valid, the method
                    returns failure status. 
         Returns A tuple consisting of (disciplineSuccess, specificationSuccess). 
         - disciplineSuccess is: bool.
         - specificationSuccess is: bool.

        """
        pass
    def StoreReuseLibraryDisciplineWithinPart(part: NXOpen.Part, discipline: str) -> bool:
        """
         Stores given discipline within the routing assembly part so that the same discipline can be restored upon reopening the assembly.
                    Only in Routed System Assembly part, RoutingManager.IsRouteSystemAssembly, discipline can be saved.
                    If discipline is not found in application view, it is considered invalid. Invalid discipline is not saved.
         Returns success (bool): .
        """
        pass
    def StoreReuseLibrarySpecificationWithinPart(part: NXOpen.Part, specification: str) -> bool:
        """
         Stores given specification within the routing assembly part so that the same specification can be restored upon reopening the assembly.
                    Only in Routed System Assembly part, RoutingManager.IsRouteSystemAssembly, specification can be saved.
                    If specification is not found in current discipline, it is considered invalid. Invalid specification is not saved.
         Returns success (bool): .
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class SecondaryPlacementBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.SecondaryPlacementBuilder. Allows the user to  select secondary parts.
    """
    class PartType(Enum):
        """
        Members Include: 
         |Part|  The secondary part type is Part, for example, a flange. 
         |Gasket|  The secondary part type is Gasket. 
         |Bolt|  The secondary part type is Bolt. 
         |Stud|  The secondary part type is Stud. 
         |Nut|  The secondary part type is Nut. 
         |Washer|  The secondary part type is Washer. 

        """
        Part: int
        Gasket: int
        Bolt: int
        Stud: int
        Nut: int
        Washer: int
        @staticmethod
        def ValueOf(value: int) -> SecondaryPlacementBuilder.PartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CleanUpSecondaryPartOccurrencesAtGivenPort(self, portOfPrimaryPart: NXOpen.TaggedObject, deleteOnlyGaskets: bool) -> None:
        """
         Removes the secondary parts for the given primary port, deleteOnlyGaskets true would remove only gaskets
                deleteOnlyGaskets false would remove both the secondary part and gasket for the given port.
        """
        pass
    def ClearLibraryDefinedAttributeHolder(self) -> None:
        """
         Clears all the attributes in library defined attribute holder for secondary part to be placed.
                    This API is recommended to be used before assigning attributes onto builder so as to ensure that secondary part placement function correctly. 
        """
        pass
    def ClearPartNumberAndPartName(self, partType: SecondaryPlacementBuilder.PartType, portOfPrimaryPart: NXOpen.TaggedObject) -> None:
        """
         Clears the part number and part name for a given secondary part type at a given primary port. 
        """
        pass
    def CreateMechanicalJoins(self) -> None:
        """
         Creates mechanical joins associated with secondary parts. 
        """
        pass
    def GetLibraryDefinedAttributeHolder(self) -> NXOpen.Routing.AttributeHolder:
        """
         Gets the library defined attribute holder for secondary part instance 
         Returns secondaryPartLibraryDefinedAttributeHolder ( NXOpen.Routing.AttributeHolder): .
        """
        pass
    def PlaceGasket(self, portOfPrimaryPart: NXOpen.Routing.Port, onlyUpdateLocation: bool) -> NXOpen.Assemblies.Component:
        """
         Cleans old gasket part occurrence if it exists at the primary port location and creates new part occurrence at the primary port location .
                The value of onlyUpdateLocation should be true when updating the location of the existing gasket part occurrence to the primary port location.
                The partOccurrenceTag gives the tag of a newly created gasket part occurrence or tag of an existing gasket part occurrence whose location is updated 
                when the value of onlyUpdateLocation is passed as true.
         Returns partOccurrenceTag ( NXOpen.Assemblies.Component): .
        """
        pass
    def PlacePart(self, portOfPrimaryPart: NXOpen.Routing.Port, onlyUpdateLocation: bool) -> NXOpen.Assemblies.Component:
        """
         Cleans old part occurrence if it exists at the primary port location and creates new part occurrence at the primary port location .
                The value of onlyUpdateLocation should be true when updating the location of the existing part occurrence to the primary port location.
                The partOccurrenceTag gives the tag of a newly created part occurrence or tag of an existing part occurrence whose location is updated 
                when the value of onlyUpdateLocation is passed as true. 
         Returns partOccurrenceTag ( NXOpen.Assemblies.Component): .
        """
        pass
    def PrepareSecondaryPlacementDataForPorts(self, primaryPorts: List[NXOpen.TaggedObject], primaryPartOccurence: NXOpen.TaggedObject) -> None:
        """
         Prepares initial secondary placement data on the builder for the given primary ports 
        """
        pass
    def RemoveAllSecondaryParts(self) -> None:
        """
         Removes all previously placed secondary parts. 
        """
        pass
    def RepositionAllSecondaryParts(self) -> None:
        """
         Repositions all previously placed secondary parts. 
        """
        pass
    def ResetTransformForAllParts(self) -> None:
        """
         Resets the linear and rotation transform for all parts to the initial placement solution transform. 
        """
        pass
    def ResizePtsPart(self, portOfPrimaryPart: NXOpen.Routing.Port, isGasket: bool) -> None:
        """
         Resizes secondary part which is placed on the given primary part port. Secondary part is resized as per the matching
                PTS (product template studio) attributes from primary placement part. Set isGasket to true if the gasket needs resizing,
                otherwise, set it to false for part (e.g., flange)
        """
        pass
    def SetClassificationObjectIdentifier(self, classificationObjectIdentifier: str) -> None:
        """
         Sets the identifier of the classification object associated with the secondary part to be placed. 
                    This also updates the secondary part library defined attribute holder from corresponding classification object. 
        """
        pass
    def SetPartNumberAndPartName(self, partType: SecondaryPlacementBuilder.PartType, portOfPrimaryPart: NXOpen.TaggedObject, partNumber: str) -> None:
        """
         Sets the part number and part name for a given secondary part type at a given primary port. 
        """
        pass
import NXOpen
import NXOpen.Routing
class SimplifyCurvesBuilder(NXOpen.Builder): 
    """
     Simplify Curves class for Linear and Spline segments.
    """
    @property
    def SegmentCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SegmentCollector
         Returns the routing object collector that collects the segments to simplify.  
            
         
        """
        pass
    def GetSimplifiedCurves(self) -> List[NXOpen.Curve]:
        """
         The result of simplify path
         Returns simplifiedCurves ( NXOpen.Curve Li):  .
        """
        pass
import NXOpen
class SplinePointBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SplinePointBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SplinePointBuilder) -> None:
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
    def Erase(self, obj: SplinePointBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SplinePointBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SplinePointBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SplinePointBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SplinePointBuilder NXOpen.Ro):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SplinePointBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( SplinePointBuilder List[NXOpen.):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SplinePointBuilder) -> None:
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
    def SetContents(self, objects: List[SplinePointBuilder]) -> None:
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
    def Swap(self, object1: SplinePointBuilder, object2: SplinePointBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.Routing
class SplitBuilder(NXOpen.Builder): 
    """ the Builder to Assign Discontinuity for the stocks """
    @property
    def ControlPointCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) ControlPointCollector
         Returns the Rcp type of the selected object    
            
         
        """
        pass
    def GetCreatedComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
         Components created during Split operation. 
         Returns components ( NXOpen.Assemblies.Component Li):  Components created during Split operation. .
        """
        pass
import NXOpen
import NXOpen.Routing
class StockBuilder(NXOpen.Builder): 
    """ Builder for creatingediting stocks.
        Create Stock: Takes a set of segments and assign the selected the stock
        to the segments. The stock style and orientation settings are optional.
        Edit Stock: Takes in the selected stock to edit as input and redefines
        the stock with the new settings.
    """
    @property
    def IsNonCircular(self) -> bool:
        """
        Getter for property: (bool) IsNonCircular
         Returns whether non circular mode or not.  
             
         
        """
        pass
    @IsNonCircular.setter
    def IsNonCircular(self, isNonCircular: bool):
        """
        Setter for property: (bool) IsNonCircular
         Returns whether non circular mode or not.  
             
         
        """
        pass
    @property
    def SegmentCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SegmentCollector
         Returns the routing object collector that collects segments to assign stock to.  
             
         
        """
        pass
    @property
    def StockSettings(self) -> NXOpen.Routing.StockBlockBuilder:
        """
        Getter for property: ( NXOpen.Routing.StockBlockBuilder) StockSettings
         Returns the path stock settings required to assign stock   
            
         
        """
        pass
    def SetTemplateAttributes(self) -> None:
        """
         Updates the feature template attributes .
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
import NXOpen.Routing
class SubdivideCurveBuilder(NXOpen.Builder): 
    """
       Subdivide Curve class for Linear and Spline segments.
      """
    class Types(Enum):
        """
        Members Include: 
         |AtPoint| 
         |EqualSegments| 
         |ArcLengthSegments| 

        """
        AtPoint: int
        EqualSegments: int
        ArcLengthSegments: int
        @staticmethod
        def ValueOf(value: int) -> SubdivideCurveBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArcLength(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) ArcLength
         Returns the arc length   
            
         
        """
        pass
    @property
    def CreateTangencySetting(self) -> bool:
        """
        Getter for property: (bool) CreateTangencySetting
         Returns the tangency toggle   
            
         
        """
        pass
    @CreateTangencySetting.setter
    def CreateTangencySetting(self, createTangency: bool):
        """
        Setter for property: (bool) CreateTangencySetting
         Returns the tangency toggle   
            
         
        """
        pass
    @property
    def EndPercentage(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) EndPercentage
         Returns the end percentage   
            
         
        """
        pass
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments equal segments   
            
         
        """
        pass
    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments equal segments   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction   
            
         
        """
        pass
    @property
    def SelectedSegment(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) SelectedSegment
         Returns the segment select   
            
         
        """
        pass
    @property
    def StartPercentage(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartPercentage
         Returns the start percentage   
            
         
        """
        pass
    @property
    def SubdivideAtPoint(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) SubdivideAtPoint
         Returns the subdivide at point   
            
         
        """
        pass
    @property
    def Type(self) -> SubdivideCurveBuilder.Types:
        """
        Getter for property: ( SubdivideCurveBuilder.Types NXOpen.Ro) Type
         Returns the subdivide type   
            
         
        """
        pass
    @Type.setter
    def Type(self, subdivideType: SubdivideCurveBuilder.Types):
        """
        Setter for property: ( SubdivideCurveBuilder.Types NXOpen.Ro) Type
         Returns the subdivide type   
            
         
        """
        pass
    def GetSubdividedCurves(self) -> List[NXOpen.Curve]:
        """
         The result of subdivide path
         Returns subdividedCurves ( NXOpen.Curve Li):  .
        """
        pass
import NXOpen
import NXOpen.Routing
class TransferBuilder(NXOpen.Builder): 
    """ Builder for transfer routing objects.
        Transfer: Takes a set of routing objects and Transfers them into current work part.
    """
    @property
    def RouteObjectCollector(self) -> NXOpen.Routing.RouteObjectCollector:
        """
        Getter for property: ( NXOpen.Routing.RouteObjectCollector) RouteObjectCollector
         Returns the route object collector   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class TransformBlockBuilder(NXOpen.Builder): 
    """ Represents NXOpen.RoutingCommon.TransformBlockBuilder. """
    class Transformtype(Enum):
        """
        Members Include: 
         |NotSet| 
         |OrientXpress|  OrientXpress allows you to move a point constrained to a coordinate axis or plane in wcs. 
         |Vector|  Vector allows you to move a point constrained to a specified direction. 
         |View|  View allows you to move a point constrained to a plane, normal to the view. 
         |Manipulator|  Manipulator allows you to move a point dynamically to any location in wcs. 
         |Plane|  Plane allows you to move a point constrained to a specified plane. 

        """
        NotSet: int
        OrientXpress: int
        Vector: int
        View: int
        Manipulator: int
        Plane: int
        @staticmethod
        def ValueOf(value: int) -> TransformBlockBuilder.Transformtype:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActiveTransformType(self) -> TransformBlockBuilder.Transformtype:
        """
        Getter for property: ( TransformBlockBuilder.Transformtype NXOpen.Ro) ActiveTransformType
         Returns the transform type setting.  
          
                    Allows you to specify the type of tool to be used for transform. 
                  
         
        """
        pass
    @ActiveTransformType.setter
    def ActiveTransformType(self, transformType: TransformBlockBuilder.Transformtype):
        """
        Setter for property: ( TransformBlockBuilder.Transformtype NXOpen.Ro) ActiveTransformType
         Returns the transform type setting.  
          
                    Allows you to specify the type of tool to be used for transform. 
                  
         
        """
        pass
    @property
    def ConstrainedPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ConstrainedPoint
         Returns the constrained point setting.  
          
                    Allows you to specify the constrained point. 
                  
         
        """
        pass
    @ConstrainedPoint.setter
    def ConstrainedPoint(self, constrainedPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ConstrainedPoint
         Returns the constrained point setting.  
          
                    Allows you to specify the constrained point. 
                  
         
        """
        pass
    @property
    def InitialOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) InitialOrientation
         Returns the initial orientation setting.  
          
                    Allows you to specify initial orientation for the transform tools. 
                  
         
        """
        pass
    @InitialOrientation.setter
    def InitialOrientation(self, initialOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) InitialOrientation
         Returns the initial orientation setting.  
          
                    Allows you to specify initial orientation for the transform tools. 
                  
         
        """
        pass
    @property
    def InitialPosition(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) InitialPosition
         Returns the initial position setting.  
          
                    Allows you to specify start point for the transform tool. 
                  
         
        """
        pass
    @InitialPosition.setter
    def InitialPosition(self, initialPosition: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) InitialPosition
         Returns the initial position setting.  
          
                    Allows you to specify start point for the transform tool. 
                  
         
        """
        pass
    @property
    def OrientExpress(self) -> NXOpen.GeometricUtilities.OrientXpressBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OrientXpressBuilder) OrientExpress
         Returns the orient express setting.  
          
                    Allows you to access the orient express object. 
                  
         
        """
        pass
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane setting.  
          
                    Allows you to specify the constraint plane. 
                  
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane setting.  
          
                    Allows you to specify the constraint plane. 
                  
         
        """
        pass
    @property
    def TempOrientation(self) -> NXOpen.Matrix3x3:
        """
        Getter for property: ( NXOpen.Matrix3x3) TempOrientation
         Returns the temp orientation setting.  
          
                    Allows you to specify final orientation for the transform tools. 
                  
         
        """
        pass
    @TempOrientation.setter
    def TempOrientation(self, tempOrientation: NXOpen.Matrix3x3):
        """
        Setter for property: ( NXOpen.Matrix3x3) TempOrientation
         Returns the temp orientation setting.  
          
                    Allows you to specify final orientation for the transform tools. 
                  
         
        """
        pass
    @property
    def TempPosition(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) TempPosition
         Returns the temp position setting.  
          
                    Allows you to specify final position for the transform tool. 
                  
         
        """
        pass
    @TempPosition.setter
    def TempPosition(self, tempPosition: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) TempPosition
         Returns the temp position setting.  
          
                    Allows you to specify final position for the transform tool. 
                  
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the vector setting.  
          
                    Allows you to specify the constraint direction. 
                  
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the vector setting.  
          
                    Allows you to specify the constraint direction. 
                  
         
        """
        pass
