from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddToWeldmentBuilder(NXOpen.Builder): 
    """
        Represents a builder which is used to create Structure Design Add To Weldment.
        """
    @property
    def ConsolidatedComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ConsolidatedComponents
         Returns the consolidated components to add to new weldment.  
             
         
        """
        pass
    @property
    def WeldmentName(self) -> str:
        """
        Getter for property: (str) WeldmentName
         Returns the weldment name   
            
         
        """
        pass
    @WeldmentName.setter
    def WeldmentName(self, weldmentName: str):
        """
        Setter for property: (str) WeldmentName
         Returns the weldment name   
            
         
        """
        pass
import NXOpen
class AssignWeldingAttributesBuilder(NXOpen.Builder): 
    """ Used to assign welding attributes to Structure Design member edges """
    @property
    def SelectionButtWeldingEdges(self) -> NXOpen.SelectEdgeList:
        """
        Getter for property: ( NXOpen.SelectEdgeList) SelectionButtWeldingEdges
         Returns the selection butt welding edges   
            
         
        """
        pass
    @property
    def SelectionCorners(self) -> SelectCornerList:
        """
        Getter for property: ( SelectCornerList NXOpen.Features) SelectionCorners
         Returns the selection corners   
            
         
        """
        pass
    @property
    def SelectionEdgesToBeClear(self) -> NXOpen.SelectEdgeList:
        """
        Getter for property: ( NXOpen.SelectEdgeList) SelectionEdgesToBeClear
         Returns the selection edges to be clear   
            
         
        """
        pass
    @property
    def SelectionFilletWeldingEdges(self) -> NXOpen.SelectEdgeList:
        """
        Getter for property: ( NXOpen.SelectEdgeList) SelectionFilletWeldingEdges
         Returns the selection fillet welding edges   
            
         
        """
        pass
class BeamCurveBuilder(FeatureParmsBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design BeamCurve feature.
        """
    pass
import NXOpen.Features
class BeamCurve(NXOpen.Features.BodyFeature): 
    """ Represents a structure design beam curve feature. """
    pass
import NXOpen
class BeamPreparationBuilder(FeatureParmsBuilder): 
    """
    Represents a builder which is used to create or edit a Structure Design BeamPreparation feature.
    """
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the name used for the created component file.  
            
         
        """
        pass
    @ComponentName.setter
    def ComponentName(self, componentName: str):
        """
        Setter for property: (str) ComponentName
         Returns the name used for the created component file.  
            
         
        """
        pass
    @property
    def NonStructureBodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) NonStructureBodies
         Returns the non-structure bodies to add to preparation model.  
             
         
        """
        pass
    @property
    def ShowBodies(self) -> bool:
        """
        Getter for property: (bool) ShowBodies
         Returns the flag to indicate whether to show bodies or not.  
             
         
        """
        pass
    @ShowBodies.setter
    def ShowBodies(self, showBodies: bool):
        """
        Setter for property: (bool) ShowBodies
         Returns the flag to indicate whether to show bodies or not.  
             
         
        """
        pass
    @property
    def StructureComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) StructureComponents
         Returns the structure components to beam.  
             
         
        """
        pass
import NXOpen.Features
class BeamPreparation(NXOpen.Features.BodyFeature): 
    """ Represents a structure design beam preparation feature. """
    pass
import NXOpen
class BoltedConnectionBuilder(FeatureParmsBuilder): 
    """
        Represents a Features.StructureDesign.BoltedConnection builder
        """
    class BeamColumnConnectionSubTypes(Enum):
        """
        Members Include: 
         |End|  The connection sub type of two connected members with bolted plate attached to one member end. 
         |LPlate|  The connection sub type of two othogonal connected members with L shape bolted plate attached. 
         |FlatPlate|  The connection sub type of two othogonal connected members with flate shape bolted plate attached. 

        """
        End: int
        LPlate: int
        FlatPlate: int
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.BeamColumnConnectionSubTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConnectionTypes(Enum):
        """
        Members Include: 
         |Splice|  The splice connection type. 
         |BeamColumn|  The beam column connection type. 
         |GussetPlate| 

        """
        Splice: int
        BeamColumn: int
        GussetPlate: int
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.ConnectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GussetPlateConnectionSubTypes(Enum):
        """
        Members Include: 
         |CornerPlate|  The connection sub type of two othogonal members connect with diagonal member at the corner with bolted plate. 
         |FlatPlate|  The connection sub type of one member connect with mulit diagonal members with bolted plate. 
         |LappedPlate|  The connection sub type of one member connect with mulit diagonal members with bolted plate lapped. 

        """
        CornerPlate: int
        FlatPlate: int
        LappedPlate: int
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.GussetPlateConnectionSubTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MountingTypes(Enum):
        """
        Members Include: 
         |Middle| 
         |FlushUp| 
         |FlushDown| 

        """
        Middle: int
        FlushUp: int
        FlushDown: int
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.MountingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpliceConnectionSubTypes(Enum):
        """
        Members Include: 
         |End|  The connection sub type of two splice connected members with bolted plate attached between the two member end. 
         |Flange|  The connection sub type of two splice connected members with bolted plate attached to flange faces. 
         |Web|  The connection sub type of two splice connected members with bolted plate attached to web faces. 

        """
        End: int
        Flange: int
        Web: int
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.SpliceConnectionSubTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddFasteners(self) -> bool:
        """
        Getter for property: (bool) AddFasteners
         Returns the flag to indicate whether to add fasteners or not.  
             
         
        """
        pass
    @AddFasteners.setter
    def AddFasteners(self, addFasteners: bool):
        """
        Setter for property: (bool) AddFasteners
         Returns the flag to indicate whether to add fasteners or not.  
             
         
        """
        pass
    @property
    def BeamColumnConnectionSubType(self) -> BoltedConnectionBuilder.BeamColumnConnectionSubTypes:
        """
        Getter for property: ( BoltedConnectionBuilder.BeamColumnConnectionSubTypes NXOpen.Features) BeamColumnConnectionSubType
         Returns an option to indicate the sub type of beam column bolted connection.  
             
         
        """
        pass
    @BeamColumnConnectionSubType.setter
    def BeamColumnConnectionSubType(self, subTypeOption: BoltedConnectionBuilder.BeamColumnConnectionSubTypes):
        """
        Setter for property: ( BoltedConnectionBuilder.BeamColumnConnectionSubTypes NXOpen.Features) BeamColumnConnectionSubType
         Returns an option to indicate the sub type of beam column bolted connection.  
             
         
        """
        pass
    @property
    def BodyOne(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodyOne
         Returns the first input body   
            
         
        """
        pass
    @property
    def BodyTwo(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodyTwo
         Returns the second input body   
            
         
        """
        pass
    @property
    def BoltedConnectionName(self) -> str:
        """
        Getter for property: (str) BoltedConnectionName
         Returns the bolted connection name   
            
         
        """
        pass
    @BoltedConnectionName.setter
    def BoltedConnectionName(self, strName: str):
        """
        Setter for property: (str) BoltedConnectionName
         Returns the bolted connection name   
            
         
        """
        pass
    @property
    def BraceFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BraceFaces
         Returns the brace faces   
            
         
        """
        pass
    @property
    def ConfigurationName(self) -> str:
        """
        Getter for property: (str) ConfigurationName
         Returns the fasteners configuration name  
            
         
        """
        pass
    @ConfigurationName.setter
    def ConfigurationName(self, strName: str):
        """
        Setter for property: (str) ConfigurationName
         Returns the fasteners configuration name  
            
         
        """
        pass
    @property
    def ConnectionType(self) -> BoltedConnectionBuilder.ConnectionTypes:
        """
        Getter for property: ( BoltedConnectionBuilder.ConnectionTypes NXOpen.Features) ConnectionType
         Returns an option to indicate the connection type of bolted connection.  
             
         
        """
        pass
    @ConnectionType.setter
    def ConnectionType(self, connectionTypeOption: BoltedConnectionBuilder.ConnectionTypes):
        """
        Setter for property: ( BoltedConnectionBuilder.ConnectionTypes NXOpen.Features) ConnectionType
         Returns an option to indicate the connection type of bolted connection.  
             
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def DisableRule(self) -> bool:
        """
        Getter for property: (bool) DisableRule
         Returns the flag to indicate whether to disable rule or not.  
             
         
        """
        pass
    @DisableRule.setter
    def DisableRule(self, disableRule: bool):
        """
        Setter for property: (bool) DisableRule
         Returns the flag to indicate whether to disable rule or not.  
             
         
        """
        pass
    @property
    def DrillThrough(self) -> bool:
        """
        Getter for property: (bool) DrillThrough
         Returns the flag to indicate whether to apply hole through or not.  
             
         
        """
        pass
    @DrillThrough.setter
    def DrillThrough(self, drillThrough: bool):
        """
        Setter for property: (bool) DrillThrough
         Returns the flag to indicate whether to apply hole through or not.  
             
         
        """
        pass
    @property
    def FaceOne(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceOne
         Returns the first input face   
            
         
        """
        pass
    @property
    def FaceTwo(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceTwo
         Returns the second input face   
            
         
        """
        pass
    @property
    def GussetPlateConnectionSubType(self) -> BoltedConnectionBuilder.GussetPlateConnectionSubTypes:
        """
        Getter for property: ( BoltedConnectionBuilder.GussetPlateConnectionSubTypes NXOpen.Features) GussetPlateConnectionSubType
         Returns an option to indicate the sub type of gusset plate bolted connection.  
             
         
        """
        pass
    @GussetPlateConnectionSubType.setter
    def GussetPlateConnectionSubType(self, subTypeOption: BoltedConnectionBuilder.GussetPlateConnectionSubTypes):
        """
        Setter for property: ( BoltedConnectionBuilder.GussetPlateConnectionSubTypes NXOpen.Features) GussetPlateConnectionSubType
         Returns an option to indicate the sub type of gusset plate bolted connection.  
             
         
        """
        pass
    @property
    def MountingType(self) -> BoltedConnectionBuilder.MountingTypes:
        """
        Getter for property: ( BoltedConnectionBuilder.MountingTypes NXOpen.Features) MountingType
         Returns the mountingType   
            
         
        """
        pass
    @MountingType.setter
    def MountingType(self, mountingType: BoltedConnectionBuilder.MountingTypes):
        """
        Setter for property: ( BoltedConnectionBuilder.MountingTypes NXOpen.Features) MountingType
         Returns the mountingType   
            
         
        """
        pass
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngle
         Returns the rotate angle   
            
         
        """
        pass
    @property
    def SpliceConnectionSubType(self) -> BoltedConnectionBuilder.SpliceConnectionSubTypes:
        """
        Getter for property: ( BoltedConnectionBuilder.SpliceConnectionSubTypes NXOpen.Features) SpliceConnectionSubType
         Returns an option to indicate the sub type of splice bolted connection.  
             
         
        """
        pass
    @SpliceConnectionSubType.setter
    def SpliceConnectionSubType(self, subTypeOption: BoltedConnectionBuilder.SpliceConnectionSubTypes):
        """
        Setter for property: ( BoltedConnectionBuilder.SpliceConnectionSubTypes NXOpen.Features) SpliceConnectionSubType
         Returns an option to indicate the sub type of splice bolted connection.  
             
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data.  
            
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the x offset   
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the y offset   
            
         
        """
        pass
    def ExecuteRule(self) -> bool:
        """
         Executes the rule to update the bolted plate stock data. 
         Returns executeRuleOk (bool): .
        """
        pass
    def GetGussetConnectionBuilders(self) -> List[GussetConnectionBuilder]:
        """
         Get gusset connection builders. 
         Returns gussetConnectionBuilders ( GussetConnectionBuilder List[NXOpen.Featur): .
        """
        pass
    def UpdateStockSectionTypes(self, sectionModified: bool) -> None:
        """
         Update stock section types by user input. 
        """
        pass
import NXOpen.Features
class BoltedConnection(NXOpen.Features.BodyFeature): 
    """ Represents a bolted connection feature """
    pass
import NXOpen.Features.ShipDesign
class ComponentDrawingBuilder(NXOpen.Features.ShipDesign.SubAssemblyDrawingBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design Component Drawing.
        """
    class DrawingTypeOption(Enum):
        """
        Members Include: 
         |Assembly| 
         |Connection| 
         |Member| 
         |SpecialComponent| 
         |Weldment| 

        """
        Assembly: int
        Connection: int
        Member: int
        SpecialComponent: int
        Weldment: int
        @staticmethod
        def ValueOf(value: int) -> ComponentDrawingBuilder.DrawingTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CreatePartsList(self) -> bool:
        """
        Getter for property: (bool) CreatePartsList
         Returns the flag to indicate whether to create a parts list or not.  
             
         
        """
        pass
    @CreatePartsList.setter
    def CreatePartsList(self, createPartsList: bool):
        """
        Setter for property: (bool) CreatePartsList
         Returns the flag to indicate whether to create a parts list or not.  
             
         
        """
        pass
    @property
    def DrawingType(self) -> ComponentDrawingBuilder.DrawingTypeOption:
        """
        Getter for property: ( ComponentDrawingBuilder.DrawingTypeOption NXOpen.Features) DrawingType
         Returns the drawing type.  
             
         
        """
        pass
    @DrawingType.setter
    def DrawingType(self, drawingType: ComponentDrawingBuilder.DrawingTypeOption):
        """
        Setter for property: ( ComponentDrawingBuilder.DrawingTypeOption NXOpen.Features) DrawingType
         Returns the drawing type.  
             
         
        """
        pass
    @property
    def ShowBalloons(self) -> bool:
        """
        Getter for property: (bool) ShowBalloons
         Returns the flag to indicate whether to show balloons or not.  
             
         
        """
        pass
    @ShowBalloons.setter
    def ShowBalloons(self, showBalloons: bool):
        """
        Setter for property: (bool) ShowBalloons
         Returns the flag to indicate whether to show balloons or not.  
             
         
        """
        pass
import NXOpen
class ConsolidateBuilder(NXOpen.Builder): 
    """ This class contains the factory method for consolidate builders. """
    @property
    def Container(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) Container
         Returns
                         the part under which are added newly created consolidation parts.  
          
                      
         
        """
        pass
    @Container.setter
    def Container(self, container: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) Container
         Returns
                         the part under which are added newly created consolidation parts.  
          
                      
         
        """
        pass
    @property
    def ExternalComponents(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) ExternalComponents
         Returns the selected external components to consolidate   
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the component part name under the consolidate list.  
            
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the component part name under the consolidate list.  
            
         
        """
        pass
    @property
    def Structures(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Structures
         Returns the selected structures to consolidate   
            
         
        """
        pass
    def CreateConsolidatedStructure(self) -> NXOpen.Part:
        """
         Create consolidated structure 
         Returns consolidatedStructure ( NXOpen.Part): .
        """
        pass
import NXOpen
class ContainerBuilder(NXOpen.Builder): 
    """ Used to specify the "container" part for the Structure Design application """
    @property
    def SelectStructure(self) -> NXOpen.Part:
        """
        Getter for property: ( NXOpen.Part) SelectStructure
         Returns
                        the part to which are added newly created Structure Design objects
                      
            
         
        """
        pass
    @SelectStructure.setter
    def SelectStructure(self, selectStructure: NXOpen.Part):
        """
        Setter for property: ( NXOpen.Part) SelectStructure
         Returns
                        the part to which are added newly created Structure Design objects
                      
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class ContextAttributeBuilder(NXOpen.TaggedObject): 
    """
            NXOpen.Features.StructureDesign.ContextAttributeBuilderobject.
        """
    @property
    def ContextAttribute(self) -> str:
        """
        Getter for property: (str) ContextAttribute
         Returns
                        the Context Attribute value.  
           This is the value of the SAW_SUB_NAME part
                        attribute added to the newly created  named objects.
                      
         
        """
        pass
    @ContextAttribute.setter
    def ContextAttribute(self, contextAttribute: str):
        """
        Setter for property: (str) ContextAttribute
         Returns
                        the Context Attribute value.  
           This is the value of the SAW_SUB_NAME part
                        attribute added to the newly created  named objects.
                      
         
        """
        pass
import NXOpen
class CornerNodeBuilder(NXOpen.NXObject): 
    """ The object containing the information about the end corner to be modified.
     """
    @property
    def EndCorner(self) -> MemberBuilder.EndCornerTypes:
        """
        Getter for property: ( MemberBuilder.EndCornerTypes NXOpen.Features) EndCorner
         Returns the setting of the end corner.  
             
         
        """
        pass
    @EndCorner.setter
    def EndCorner(self, endCorner: MemberBuilder.EndCornerTypes):
        """
        Setter for property: ( MemberBuilder.EndCornerTypes NXOpen.Features) EndCorner
         Returns the setting of the end corner.  
             
         
        """
        pass
import NXOpen
class Corner(NXOpen.DisplayableObject): 
    """ Represents a Corner object """
    pass
import NXOpen
import NXOpen.ShipDesign
class CreateStructureBuilder(NXOpen.Builder): 
    """
    Used to create structre structure in the Structure Design application.
    Up direction information and catalog information are stored as user attributes on created structure part.
    """
    class PartTypes(Enum):
        """
        Members Include: 
         |Structure| 
         |Design| 

        """
        Structure: int
        Design: int
        @staticmethod
        def ValueOf(value: int) -> CreateStructureBuilder.PartTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Catalog(self) -> str:
        """
        Getter for property: (str) Catalog
         Returns the catalog to use for the stock definitions.  
             
         
        """
        pass
    @Catalog.setter
    def Catalog(self, catalog: str):
        """
        Setter for property: (str) Catalog
         Returns the catalog to use for the stock definitions.  
             
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    @property
    def DesignName(self) -> str:
        """
        Getter for property: (str) DesignName
         Returns the name used for the created design component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    @DesignName.setter
    def DesignName(self, designName: str):
        """
        Setter for property: (str) DesignName
         Returns the name used for the created design component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    @property
    def Reference(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Reference
         Returns  the reference objects used to evaluate the structure member orientation.  
             
         
        """
        pass
    @property
    def ReferenceOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ReferenceOrientation
         Returns the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    @ReferenceOrientation.setter
    def ReferenceOrientation(self, refOrientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ReferenceOrientation
         Returns the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    @property
    def StructreRootNode(self) -> NXOpen.ShipDesign.NavigatorNode:
        """
        Getter for property: ( NXOpen.ShipDesign.NavigatorNode) StructreRootNode
         Returns the structure root node for structure node creation in navigator.  
           Structure node will be created under the structure root node.   
         
        """
        pass
    @StructreRootNode.setter
    def StructreRootNode(self, tgStructureRootNode: NXOpen.ShipDesign.NavigatorNode):
        """
        Setter for property: ( NXOpen.ShipDesign.NavigatorNode) StructreRootNode
         Returns the structure root node for structure node creation in navigator.  
           Structure node will be created under the structure root node.   
         
        """
        pass
    @property
    def UpOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) UpOrientation
         Returns the direction which is considered up in the Structure Design application.  
             
         
        """
        pass
    @UpOrientation.setter
    def UpOrientation(self, upOrientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) UpOrientation
         Returns the direction which is considered up in the Structure Design application.  
             
         
        """
        pass
    def CreateStructure(self) -> NXOpen.Part:
        """
         Create structure part 
         Returns structure ( NXOpen.Part): .
        """
        pass
import NXOpen
class DrawingsBuilder(NXOpen.Builder): 
    """
        Represents a builder which is used to create or edit a Structure Design Drawings feature.
        """
    class TargetAssemblyOption(Enum):
        """
        Members Include: 
         |Consolidated| 
         |Structure| 
         |Root| 

        """
        Consolidated: int
        Structure: int
        Root: int
        @staticmethod
        def ValueOf(value: int) -> DrawingsBuilder.TargetAssemblyOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssemblyBalloonsToggle(self) -> bool:
        """
        Getter for property: (bool) AssemblyBalloonsToggle
         Returns the flag to indicate whether to create assembly drawing balloons or not.  
             
         
        """
        pass
    @AssemblyBalloonsToggle.setter
    def AssemblyBalloonsToggle(self, assemblyBalloonsToggle: bool):
        """
        Setter for property: (bool) AssemblyBalloonsToggle
         Returns the flag to indicate whether to create assembly drawing balloons or not.  
             
         
        """
        pass
    @property
    def AssemblyConsolidatedList(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) AssemblyConsolidatedList
         Returns the assembly components to draw.  
             
         
        """
        pass
    @property
    def AssemblyPartsListToggle(self) -> bool:
        """
        Getter for property: (bool) AssemblyPartsListToggle
         Returns the flag to indicate whether to create an assembly drawing parts list or not.  
             
         
        """
        pass
    @AssemblyPartsListToggle.setter
    def AssemblyPartsListToggle(self, assemblyPartsListToggle: bool):
        """
        Setter for property: (bool) AssemblyPartsListToggle
         Returns the flag to indicate whether to create an assembly drawing parts list or not.  
             
         
        """
        pass
    @property
    def AssemblyTemplateName(self) -> str:
        """
        Getter for property: (str) AssemblyTemplateName
         Returns the assembly drawing template   
            
         
        """
        pass
    @AssemblyTemplateName.setter
    def AssemblyTemplateName(self, assemblyTemplateName: str):
        """
        Setter for property: (str) AssemblyTemplateName
         Returns the assembly drawing template   
            
         
        """
        pass
    @property
    def AssemblyToggle(self) -> bool:
        """
        Getter for property: (bool) AssemblyToggle
         Returns the flag to indicate whether to create an assembly drawing or not.  
             
         
        """
        pass
    @AssemblyToggle.setter
    def AssemblyToggle(self, assemblyToggle: bool):
        """
        Setter for property: (bool) AssemblyToggle
         Returns the flag to indicate whether to create an assembly drawing or not.  
             
         
        """
        pass
    @property
    def ConnectionBalloonsToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectionBalloonsToggle
         Returns the flag to indicate whether to create connection drawing balloons or not.  
             
         
        """
        pass
    @ConnectionBalloonsToggle.setter
    def ConnectionBalloonsToggle(self, connectionBalloonsToggle: bool):
        """
        Setter for property: (bool) ConnectionBalloonsToggle
         Returns the flag to indicate whether to create connection drawing balloons or not.  
             
         
        """
        pass
    @property
    def ConnectionPartsListToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectionPartsListToggle
         Returns the flag to indicate whether to create connection drawing parts lists or not.  
             
         
        """
        pass
    @ConnectionPartsListToggle.setter
    def ConnectionPartsListToggle(self, connectionPartsListToggle: bool):
        """
        Setter for property: (bool) ConnectionPartsListToggle
         Returns the flag to indicate whether to create connection drawing parts lists or not.  
             
         
        """
        pass
    @property
    def ConnectionTemplateName(self) -> str:
        """
        Getter for property: (str) ConnectionTemplateName
         Returns the connection drawing template   
            
         
        """
        pass
    @ConnectionTemplateName.setter
    def ConnectionTemplateName(self, connectionTemplateName: str):
        """
        Setter for property: (str) ConnectionTemplateName
         Returns the connection drawing template   
            
         
        """
        pass
    @property
    def ConnectionToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectionToggle
         Returns the flag to indicate whether to create connection drawings or not.  
             
         
        """
        pass
    @ConnectionToggle.setter
    def ConnectionToggle(self, connectionToggle: bool):
        """
        Setter for property: (bool) ConnectionToggle
         Returns the flag to indicate whether to create connection drawings or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyBack(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyBack
         Returns the flag to indicate whether to create an assembly back view or not.  
             
         
        """
        pass
    @CreateAssemblyBack.setter
    def CreateAssemblyBack(self, createAssemblyBack: bool):
        """
        Setter for property: (bool) CreateAssemblyBack
         Returns the flag to indicate whether to create an assembly back view or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyBottom(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyBottom
         Returns the flag to indicate whether to create an assembly bottom view or not.  
             
         
        """
        pass
    @CreateAssemblyBottom.setter
    def CreateAssemblyBottom(self, createAssemblyBottom: bool):
        """
        Setter for property: (bool) CreateAssemblyBottom
         Returns the flag to indicate whether to create an assembly bottom view or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyFront(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyFront
         Returns the flag to indicate whether to create an assembly front view or not.  
             
         
        """
        pass
    @CreateAssemblyFront.setter
    def CreateAssemblyFront(self, createAssemblyFront: bool):
        """
        Setter for property: (bool) CreateAssemblyFront
         Returns the flag to indicate whether to create an assembly front view or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyIsometric
         Returns the flag to indicate whether to create an assembly isometric view or not.  
             
         
        """
        pass
    @CreateAssemblyIsometric.setter
    def CreateAssemblyIsometric(self, createAssemblyIsometric: bool):
        """
        Setter for property: (bool) CreateAssemblyIsometric
         Returns the flag to indicate whether to create an assembly isometric view or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyLeft(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyLeft
         Returns the flag to indicate whether to create an assembly left view or not.  
             
         
        """
        pass
    @CreateAssemblyLeft.setter
    def CreateAssemblyLeft(self, createAssemblyLeft: bool):
        """
        Setter for property: (bool) CreateAssemblyLeft
         Returns the flag to indicate whether to create an assembly left view or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyRight(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyRight
         Returns the flag to indicate whether to create an assembly right view or not.  
             
         
        """
        pass
    @CreateAssemblyRight.setter
    def CreateAssemblyRight(self, createAssemblyRight: bool):
        """
        Setter for property: (bool) CreateAssemblyRight
         Returns the flag to indicate whether to create an assembly right view or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyTop(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyTop
         Returns the flag to indicate whether to create an assembly top view or not.  
             
         
        """
        pass
    @CreateAssemblyTop.setter
    def CreateAssemblyTop(self, createAssemblyTop: bool):
        """
        Setter for property: (bool) CreateAssemblyTop
         Returns the flag to indicate whether to create an assembly top view or not.  
             
         
        """
        pass
    @property
    def CreateAssemblyTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyTrimetric
         Returns the flag to indicate whether to create an assembly trimetric view or not.  
             
         
        """
        pass
    @CreateAssemblyTrimetric.setter
    def CreateAssemblyTrimetric(self, createAssemblyTrimetric: bool):
        """
        Setter for property: (bool) CreateAssemblyTrimetric
         Returns the flag to indicate whether to create an assembly trimetric view or not.  
             
         
        """
        pass
    @property
    def CreateConnectionBack(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionBack
         Returns the flag to indicate whether to create connection back views or not.  
             
         
        """
        pass
    @CreateConnectionBack.setter
    def CreateConnectionBack(self, createConnectionBack: bool):
        """
        Setter for property: (bool) CreateConnectionBack
         Returns the flag to indicate whether to create connection back views or not.  
             
         
        """
        pass
    @property
    def CreateConnectionBottom(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionBottom
         Returns the flag to indicate whether to create connection bottom views or not.  
             
         
        """
        pass
    @CreateConnectionBottom.setter
    def CreateConnectionBottom(self, createConnectionBottom: bool):
        """
        Setter for property: (bool) CreateConnectionBottom
         Returns the flag to indicate whether to create connection bottom views or not.  
             
         
        """
        pass
    @property
    def CreateConnectionFront(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionFront
         Returns the flag to indicate whether to create connection front views or not.  
             
         
        """
        pass
    @CreateConnectionFront.setter
    def CreateConnectionFront(self, createConnectionFront: bool):
        """
        Setter for property: (bool) CreateConnectionFront
         Returns the flag to indicate whether to create connection front views or not.  
             
         
        """
        pass
    @property
    def CreateConnectionIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionIsometric
         Returns the flag to indicate whether to create connection isometric views or not.  
             
         
        """
        pass
    @CreateConnectionIsometric.setter
    def CreateConnectionIsometric(self, createConnectionIsometric: bool):
        """
        Setter for property: (bool) CreateConnectionIsometric
         Returns the flag to indicate whether to create connection isometric views or not.  
             
         
        """
        pass
    @property
    def CreateConnectionLeft(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionLeft
         Returns the flag to indicate whether to create connection left views or not.  
             
         
        """
        pass
    @CreateConnectionLeft.setter
    def CreateConnectionLeft(self, createConnectionLeft: bool):
        """
        Setter for property: (bool) CreateConnectionLeft
         Returns the flag to indicate whether to create connection left views or not.  
             
         
        """
        pass
    @property
    def CreateConnectionRight(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionRight
         Returns the flag to indicate whether to create connection right views or not.  
             
         
        """
        pass
    @CreateConnectionRight.setter
    def CreateConnectionRight(self, createConnectionRight: bool):
        """
        Setter for property: (bool) CreateConnectionRight
         Returns the flag to indicate whether to create connection right views or not.  
             
         
        """
        pass
    @property
    def CreateConnectionTop(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionTop
         Returns the flag to indicate whether to create connection top views or not.  
             
         
        """
        pass
    @CreateConnectionTop.setter
    def CreateConnectionTop(self, createConnectionTop: bool):
        """
        Setter for property: (bool) CreateConnectionTop
         Returns the flag to indicate whether to create connection top views or not.  
             
         
        """
        pass
    @property
    def CreateConnectionTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionTrimetric
         Returns the flag to indicate whether to create connection trimetric views or not.  
             
         
        """
        pass
    @CreateConnectionTrimetric.setter
    def CreateConnectionTrimetric(self, createConnectionTrimetric: bool):
        """
        Setter for property: (bool) CreateConnectionTrimetric
         Returns the flag to indicate whether to create connection trimetric views or not.  
             
         
        """
        pass
    @property
    def CreateMemberBack(self) -> bool:
        """
        Getter for property: (bool) CreateMemberBack
         Returns the flag to indicate whether to create member back views or not.  
             
         
        """
        pass
    @CreateMemberBack.setter
    def CreateMemberBack(self, createMemberBack: bool):
        """
        Setter for property: (bool) CreateMemberBack
         Returns the flag to indicate whether to create member back views or not.  
             
         
        """
        pass
    @property
    def CreateMemberBottom(self) -> bool:
        """
        Getter for property: (bool) CreateMemberBottom
         Returns the flag to indicate whether to create member bottom views or not.  
             
         
        """
        pass
    @CreateMemberBottom.setter
    def CreateMemberBottom(self, createMemberBottom: bool):
        """
        Setter for property: (bool) CreateMemberBottom
         Returns the flag to indicate whether to create member bottom views or not.  
             
         
        """
        pass
    @property
    def CreateMemberFront(self) -> bool:
        """
        Getter for property: (bool) CreateMemberFront
         Returns the flag to indicate whether to create member front views or not.  
             
         
        """
        pass
    @CreateMemberFront.setter
    def CreateMemberFront(self, createMemberFront: bool):
        """
        Setter for property: (bool) CreateMemberFront
         Returns the flag to indicate whether to create member front views or not.  
             
         
        """
        pass
    @property
    def CreateMemberIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateMemberIsometric
         Returns the flag to indicate whether to create member isometric views or not.  
             
         
        """
        pass
    @CreateMemberIsometric.setter
    def CreateMemberIsometric(self, createMemberIsometric: bool):
        """
        Setter for property: (bool) CreateMemberIsometric
         Returns the flag to indicate whether to create member isometric views or not.  
             
         
        """
        pass
    @property
    def CreateMemberLeft(self) -> bool:
        """
        Getter for property: (bool) CreateMemberLeft
         Returns the flag to indicate whether to create member left views or not.  
             
         
        """
        pass
    @CreateMemberLeft.setter
    def CreateMemberLeft(self, createMemberLeft: bool):
        """
        Setter for property: (bool) CreateMemberLeft
         Returns the flag to indicate whether to create member left views or not.  
             
         
        """
        pass
    @property
    def CreateMemberRight(self) -> bool:
        """
        Getter for property: (bool) CreateMemberRight
         Returns the flag to indicate whether to create member right views or not.  
             
         
        """
        pass
    @CreateMemberRight.setter
    def CreateMemberRight(self, createMemberRight: bool):
        """
        Setter for property: (bool) CreateMemberRight
         Returns the flag to indicate whether to create member right views or not.  
             
         
        """
        pass
    @property
    def CreateMemberTop(self) -> bool:
        """
        Getter for property: (bool) CreateMemberTop
         Returns the flag to indicate whether to create member top views or not.  
             
         
        """
        pass
    @CreateMemberTop.setter
    def CreateMemberTop(self, createMemberTop: bool):
        """
        Setter for property: (bool) CreateMemberTop
         Returns the flag to indicate whether to create member top views or not.  
             
         
        """
        pass
    @property
    def CreateMemberTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateMemberTrimetric
         Returns the flag to indicate whether to create member trimetric views or not.  
             
         
        """
        pass
    @CreateMemberTrimetric.setter
    def CreateMemberTrimetric(self, createMemberTrimetric: bool):
        """
        Setter for property: (bool) CreateMemberTrimetric
         Returns the flag to indicate whether to create member trimetric views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompBack(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompBack
         Returns the flag to indicate whether to create special component back views or not.  
             
         
        """
        pass
    @CreateSpecialCompBack.setter
    def CreateSpecialCompBack(self, createSpecialCompBack: bool):
        """
        Setter for property: (bool) CreateSpecialCompBack
         Returns the flag to indicate whether to create special component back views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompBottom(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompBottom
         Returns the flag to indicate whether to create special component bottom views or not.  
             
         
        """
        pass
    @CreateSpecialCompBottom.setter
    def CreateSpecialCompBottom(self, createSpecialCompBottom: bool):
        """
        Setter for property: (bool) CreateSpecialCompBottom
         Returns the flag to indicate whether to create special component bottom views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompFront(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompFront
         Returns the flag to indicate whether to create special component front views or not.  
             
         
        """
        pass
    @CreateSpecialCompFront.setter
    def CreateSpecialCompFront(self, createSpecialCompFront: bool):
        """
        Setter for property: (bool) CreateSpecialCompFront
         Returns the flag to indicate whether to create special component front views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompIsometric
         Returns the flag to indicate whether to create special component isometric views or not.  
             
         
        """
        pass
    @CreateSpecialCompIsometric.setter
    def CreateSpecialCompIsometric(self, createSpecialCompIsometric: bool):
        """
        Setter for property: (bool) CreateSpecialCompIsometric
         Returns the flag to indicate whether to create special component isometric views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompLeft(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompLeft
         Returns the flag to indicate whether to create special component left views or not.  
             
         
        """
        pass
    @CreateSpecialCompLeft.setter
    def CreateSpecialCompLeft(self, createSpecialCompLeft: bool):
        """
        Setter for property: (bool) CreateSpecialCompLeft
         Returns the flag to indicate whether to create special component left views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompRight(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompRight
         Returns the flag to indicate whether to create special component right views or not.  
             
         
        """
        pass
    @CreateSpecialCompRight.setter
    def CreateSpecialCompRight(self, createSpecialCompRight: bool):
        """
        Setter for property: (bool) CreateSpecialCompRight
         Returns the flag to indicate whether to create special component right views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompTop(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompTop
         Returns the flag to indicate whether to create special component top views or not.  
             
         
        """
        pass
    @CreateSpecialCompTop.setter
    def CreateSpecialCompTop(self, createSpecialCompTop: bool):
        """
        Setter for property: (bool) CreateSpecialCompTop
         Returns the flag to indicate whether to create special component top views or not.  
             
         
        """
        pass
    @property
    def CreateSpecialCompTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompTrimetric
         Returns the flag to indicate whether to create special component trimetric views or not.  
             
         
        """
        pass
    @CreateSpecialCompTrimetric.setter
    def CreateSpecialCompTrimetric(self, createSpecialCompTrimetric: bool):
        """
        Setter for property: (bool) CreateSpecialCompTrimetric
         Returns the flag to indicate whether to create special component trimetric views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentBack(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentBack
         Returns the flag to indicate whether to create weldment back views or not.  
             
         
        """
        pass
    @CreateWeldmentBack.setter
    def CreateWeldmentBack(self, createWeldmentBack: bool):
        """
        Setter for property: (bool) CreateWeldmentBack
         Returns the flag to indicate whether to create weldment back views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentBottom(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentBottom
         Returns the flag to indicate whether to create weldment bottom views or not.  
             
         
        """
        pass
    @CreateWeldmentBottom.setter
    def CreateWeldmentBottom(self, createWeldmentBottom: bool):
        """
        Setter for property: (bool) CreateWeldmentBottom
         Returns the flag to indicate whether to create weldment bottom views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentFront(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentFront
         Returns the flag to indicate whether to create weldment front views or not.  
             
         
        """
        pass
    @CreateWeldmentFront.setter
    def CreateWeldmentFront(self, createWeldmentFront: bool):
        """
        Setter for property: (bool) CreateWeldmentFront
         Returns the flag to indicate whether to create weldment front views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentIsometric
         Returns the flag to indicate whether to create weldment isometric views or not.  
             
         
        """
        pass
    @CreateWeldmentIsometric.setter
    def CreateWeldmentIsometric(self, createWeldmentIsometric: bool):
        """
        Setter for property: (bool) CreateWeldmentIsometric
         Returns the flag to indicate whether to create weldment isometric views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentLeft(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentLeft
         Returns the flag to indicate whether to create weldment left views or not.  
             
         
        """
        pass
    @CreateWeldmentLeft.setter
    def CreateWeldmentLeft(self, createWeldmentLeft: bool):
        """
        Setter for property: (bool) CreateWeldmentLeft
         Returns the flag to indicate whether to create weldment left views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentRight(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentRight
         Returns the flag to indicate whether to create weldment right views or not.  
             
         
        """
        pass
    @CreateWeldmentRight.setter
    def CreateWeldmentRight(self, createWeldmentRight: bool):
        """
        Setter for property: (bool) CreateWeldmentRight
         Returns the flag to indicate whether to create weldment right views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentTop(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentTop
         Returns the flag to indicate whether to create weldment top views or not.  
             
         
        """
        pass
    @CreateWeldmentTop.setter
    def CreateWeldmentTop(self, createWeldmentTop: bool):
        """
        Setter for property: (bool) CreateWeldmentTop
         Returns the flag to indicate whether to create weldment top views or not.  
             
         
        """
        pass
    @property
    def CreateWeldmentTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentTrimetric
         Returns the flag to indicate whether to create weldment trimetric views or not.  
             
         
        """
        pass
    @CreateWeldmentTrimetric.setter
    def CreateWeldmentTrimetric(self, createWeldmentTrimetric: bool):
        """
        Setter for property: (bool) CreateWeldmentTrimetric
         Returns the flag to indicate whether to create weldment trimetric views or not.  
             
         
        """
        pass
    @property
    def MemberTemplateName(self) -> str:
        """
        Getter for property: (str) MemberTemplateName
         Returns the member drawing template   
            
         
        """
        pass
    @MemberTemplateName.setter
    def MemberTemplateName(self, memberTemplateName: str):
        """
        Setter for property: (str) MemberTemplateName
         Returns the member drawing template   
            
         
        """
        pass
    @property
    def MemberToggle(self) -> bool:
        """
        Getter for property: (bool) MemberToggle
         Returns the flag to indicate whether to create member drawings or not.  
             
         
        """
        pass
    @MemberToggle.setter
    def MemberToggle(self, memberToggle: bool):
        """
        Setter for property: (bool) MemberToggle
         Returns the flag to indicate whether to create member drawings or not.  
             
         
        """
        pass
    @property
    def SpecialCompIncludeWeldToggle(self) -> bool:
        """
        Getter for property: (bool) SpecialCompIncludeWeldToggle
         Returns the flag to indicate whether to include special components present in weldments or not.  
             
         
        """
        pass
    @SpecialCompIncludeWeldToggle.setter
    def SpecialCompIncludeWeldToggle(self, specialCompIncludeWeldToggle: bool):
        """
        Setter for property: (bool) SpecialCompIncludeWeldToggle
         Returns the flag to indicate whether to include special components present in weldments or not.  
             
         
        """
        pass
    @property
    def SpecialCompTemplateName(self) -> str:
        """
        Getter for property: (str) SpecialCompTemplateName
         Returns the special component drawing template   
            
         
        """
        pass
    @SpecialCompTemplateName.setter
    def SpecialCompTemplateName(self, specialCompTemplateName: str):
        """
        Setter for property: (str) SpecialCompTemplateName
         Returns the special component drawing template   
            
         
        """
        pass
    @property
    def SpecialCompToggle(self) -> bool:
        """
        Getter for property: (bool) SpecialCompToggle
         Returns the flag to indicate whether to create special component drawings or not.  
             
         
        """
        pass
    @SpecialCompToggle.setter
    def SpecialCompToggle(self, specialCompToggle: bool):
        """
        Setter for property: (bool) SpecialCompToggle
         Returns the flag to indicate whether to create special component drawings or not.  
             
         
        """
        pass
    @property
    def TargetAssembly(self) -> DrawingsBuilder.TargetAssemblyOption:
        """
        Getter for property: ( DrawingsBuilder.TargetAssemblyOption NXOpen.Features) TargetAssembly
         Returns the target assembly.  
             
         
        """
        pass
    @TargetAssembly.setter
    def TargetAssembly(self, targetAssembly: DrawingsBuilder.TargetAssemblyOption):
        """
        Setter for property: ( DrawingsBuilder.TargetAssemblyOption NXOpen.Features) TargetAssembly
         Returns the target assembly.  
             
         
        """
        pass
    @property
    def WeldmentBalloonsToggle(self) -> bool:
        """
        Getter for property: (bool) WeldmentBalloonsToggle
         Returns the flag to indicate whether to create weldment drawing balloons or not.  
             
         
        """
        pass
    @WeldmentBalloonsToggle.setter
    def WeldmentBalloonsToggle(self, weldmentBalloonsToggle: bool):
        """
        Setter for property: (bool) WeldmentBalloonsToggle
         Returns the flag to indicate whether to create weldment drawing balloons or not.  
             
         
        """
        pass
    @property
    def WeldmentPartsListToggle(self) -> bool:
        """
        Getter for property: (bool) WeldmentPartsListToggle
         Returns the flag to indicate whether to create weldment parts list or not.  
             
         
        """
        pass
    @WeldmentPartsListToggle.setter
    def WeldmentPartsListToggle(self, weldmentPartsListToggle: bool):
        """
        Setter for property: (bool) WeldmentPartsListToggle
         Returns the flag to indicate whether to create weldment parts list or not.  
             
         
        """
        pass
    @property
    def WeldmentTemplateName(self) -> str:
        """
        Getter for property: (str) WeldmentTemplateName
         Returns the weldment drawing template   
            
         
        """
        pass
    @WeldmentTemplateName.setter
    def WeldmentTemplateName(self, weldmentTemplateName: str):
        """
        Setter for property: (str) WeldmentTemplateName
         Returns the weldment drawing template   
            
         
        """
        pass
    @property
    def WeldmentToggle(self) -> bool:
        """
        Getter for property: (bool) WeldmentToggle
         Returns the flag to indicate whether to create weldment drawings or not.  
             
         
        """
        pass
    @WeldmentToggle.setter
    def WeldmentToggle(self, weldmentToggle: bool):
        """
        Setter for property: (bool) WeldmentToggle
         Returns the flag to indicate whether to create weldment drawings or not.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
class EditCornerBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Features.StructureDesign.EditCornerBuilder which is used 
    edit the corners of multiple members in the Structure Design application. Only corners at one
    connected end of the member can be modified. 
    """
    @property
    def Corner(self) -> SelectCorner:
        """
        Getter for property: ( SelectCorner NXOpen.Features) Corner
         Returns the select corner   
            
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the member.  
            
         
        """
        pass
    def AddMemberReferenceObjects(self, iMemberIndex: int, tRefObj: List[NXOpen.NXObject]) -> None:
        """
         Add butt member reference object
        """
        pass
    def AddReferenceMemberFaceInformation(self, iMemberIndex: int, iRefMemberIndex: int, facePoint: NXOpen.Point3d, faceNormal: NXOpen.Vector3d) -> None:
        """
         Add reference member face information
        """
        pass
    def AskMembers(self) -> List[NXOpen.Body]:
        """
         Gets related member bodies
         Returns members ( NXOpen.Body Li): .
        """
        pass
    def ClearReferenceMemberFaceInformation(self, iMemberIndex: int) -> None:
        """
         Clears reference member faces
        """
        pass
    def ClearReferencedMemberInformation(self, iMemberIndex: int) -> None:
        """
         Clears referenced member information
        """
        pass
    def CreateCorners(self, body: NXOpen.Body, endPoint: NXOpen.Point3d) -> List[CornerNodeBuilder]:
        """
         Create the corners for the input body and adjacent members. 
         Returns corners ( CornerNodeBuilder List[NXOpen.Featur):  The corners being processed. .
        """
        pass
    def GetCorners(self) -> List[CornerNodeBuilder]:
        """
         Output the corner nodes being processed. 
         Returns corners ( CornerNodeBuilder List[NXOpen.Featur):  The corners being processed. .
        """
        pass
    def GetStockDataByMember(self, iMemberIndex: int) -> FeatureSpreadsheetBuilder:
        """
         Gets the stock data used for current selected member.
         Returns stockData ( FeatureSpreadsheetBuilder NXOpen.Features): .
        """
        pass
    def RemoveCorners(self, corners: List[CornerNodeBuilder]) -> None:
        """
         Remove the corner nodes from processing. 
        """
        pass
    def ResetStockData(self) -> None:
        """
         Resets the stock data
        """
        pass
    def SetCopeMemberIndex(self, iMemberIndex: int, iRefCopeMemberIndex: int) -> None:
        """
         Sets cope member index
        """
        pass
    def SetCopeMemberIndexArray(self, iMemberIndex: int, refCopeMemberIndexArray: List[int]) -> None:
        """
         Sets cope member index array
        """
        pass
    def SetCornerObject(self, corner: Corner) -> None:
        """
         Set the corner object 
        """
        pass
    def SetCurrentStockData(self, stockData: FeatureSpreadsheetBuilder) -> None:
        """
         Sets current stock data
        """
        pass
    def SetCutback(self, iMemberIndex: int, usCutback: str) -> None:
        """
         Sets cutback
        """
        pass
    def SetEndCorner(self, iNodeIndex: int, endCorner: MemberBuilder.EndCornerTypes) -> None:
        """
         Set the corner type for the corner node
        """
        pass
    def SetInitialStockData(self, bInitial: bool) -> None:
        """
         Sets the flag to indicate the cope stock data is initial values
        """
        pass
    def SetMemberIndex(self, iNodeIndex: int, iMemberIndex: int) -> None:
        """
         Set the member index for the corner node
        """
        pass
    def SetParamtersChanged(self, bChanged: bool) -> None:
        """
         Sets member end parameters changed
        """
        pass
    def UpdateAllCopeStockData(self) -> None:
        """
         Update all the cope stock data of the conner
        """
        pass
    def UpdateCopeMemberStockData(self, iMemberIndex: int, bOnlyUpdateSize: bool) -> None:
        """
         Update the stock data for memeber 
        """
        pass
    def UpdateStockData(self, bOnlyUpdateSize: bool) -> None:
        """
         Update the stock data with the member
        """
        pass
import NXOpen
import NXOpen.Features
class EditStockBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a Features.StructureDesign.EditStockBuilder which is used
        to change the stock of multiple Structure Design members at the same time.
        """
    class AlignMemberSelectionType(Enum):
        """
        Members Include: 
         |FacePlane| 
         |CurveEdge| 

        """
        FacePlane: int
        CurveEdge: int
        @staticmethod
        def ValueOf(value: int) -> EditStockBuilder.AlignMemberSelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlternateOrigin(self) -> int:
        """
        Getter for property: (int) AlternateOrigin
         Returns the index number of the alternate sketch origin to use.  
             
         
        """
        pass
    @AlternateOrigin.setter
    def AlternateOrigin(self, alternateOrigin: int):
        """
        Setter for property: (int) AlternateOrigin
         Returns the index number of the alternate sketch origin to use.  
             
         
        """
        pass
    @property
    def EnableTransform(self) -> bool:
        """
        Getter for property: (bool) EnableTransform
         Returns the flag to enable transform.  
             
         
        """
        pass
    @EnableTransform.setter
    def EnableTransform(self, bEnableTransform: bool):
        """
        Setter for property: (bool) EnableTransform
         Returns the flag to enable transform.  
             
         
        """
        pass
    @property
    def EndLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndLimit
         Returns the end limit.  
            
         
        """
        pass
    @property
    def InheritStock(self) -> InheritStockBuilder:
        """
        Getter for property: ( InheritStockBuilder NXOpen.Features) InheritStock
         Returns the inherit stock object for member.  
            
         
        """
        pass
    @property
    def Member(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Member
         Returns the selection object to allow for selection of a member's body.  
             
         
        """
        pass
    @property
    def MemberCurveEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MemberCurveEdge
         Returns the member curve edge   
            
         
        """
        pass
    @property
    def MemberFacePlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MemberFacePlane
         Returns the member face plane   
            
         
        """
        pass
    @property
    def ReferenceCurveEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReferenceCurveEdge
         Returns the reference curve edge   
            
         
        """
        pass
    @property
    def ReferenceFacePlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReferenceFacePlane
         Returns the reference face plane   
            
         
        """
        pass
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngle
         Returns the rotate angle period  
            
         
        """
        pass
    @property
    def SelectionType(self) -> EditStockBuilder.AlignMemberSelectionType:
        """
        Getter for property: ( EditStockBuilder.AlignMemberSelectionType NXOpen.Features) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @SelectionType.setter
    def SelectionType(self, selectionType: EditStockBuilder.AlignMemberSelectionType):
        """
        Setter for property: ( EditStockBuilder.AlignMemberSelectionType NXOpen.Features) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @property
    def StartLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartLimit
         Returns the start limit.  
            
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the member.  
            
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the x offset.  
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the y offset.  
            
         
        """
        pass
    def FlipX(self) -> None:
        """
         Rotate the sketch 180 degrees around the X axis. 
        """
        pass
    def FlipY(self) -> None:
        """
         Rotate the sketch 180 degrees around the Y axis. 
        """
        pass
    def UpdateStockInformation(self, member: NXOpen.NXObject) -> None:
        """
         Update the stock data settings using the stock of the input member body. 
        """
        pass
import NXOpen
class EditStructureBuilder(NXOpen.Builder): 
    """
        Represents a Features.StructureDesign.EditStructureBuilder which is used to edit structure in the Structure Design application.
        Up direction information and catalog information are stored as user attributes on created frame part.
        """
    @property
    def Catalog(self) -> str:
        """
        Getter for property: (str) Catalog
         Returns the catalog to use for the stock definitions.  
             
         
        """
        pass
    @Catalog.setter
    def Catalog(self, catalog: str):
        """
        Setter for property: (str) Catalog
         Returns the catalog to use for the stock definitions.  
             
         
        """
        pass
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
         Returns the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
         Returns the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    @property
    def Reference(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Reference
         Returns the selected references   
            
         
        """
        pass
    @property
    def ReferenceOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ReferenceOrientation
         Returns the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    @ReferenceOrientation.setter
    def ReferenceOrientation(self, refOrientation: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ReferenceOrientation
         Returns the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    @property
    def Structure(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) Structure
         Returns the selected structures   
            
         
        """
        pass
    def UpdateReferenceInfomation(self, selStructure: NXOpen.NXObject) -> None:
        """
         Updates the stock data settings using the stock of the input member body. 
        """
        pass
import NXOpen
import NXOpen.Features
class EndcapBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Features.StructureDesign.Endcap builder
    """
    class CornerTreatmentTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Chamfer| 
         |Fillet| 

        """
        NotSet: int
        Chamfer: int
        Fillet: int
        @staticmethod
        def ValueOf(value: int) -> EndcapBuilder.CornerTreatmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlacementTypes(Enum):
        """
        Members Include: 
         |Inside| 
         |Outside| 

        """
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> EndcapBuilder.PlacementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Chamfer(self) -> bool:
        """
        Getter for property: (bool) Chamfer
         Returns the chamfer   
            
         
        """
        pass
    @Chamfer.setter
    def Chamfer(self, chamfer: bool):
        """
        Setter for property: (bool) Chamfer
         Returns the chamfer   
            
         
        """
        pass
    @property
    def ChamferLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChamferLength
         Returns the chamferLength   
            
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance   
            
         
        """
        pass
    @property
    def EndCapName(self) -> str:
        """
        Getter for property: (str) EndCapName
         Returns the end cap name   
            
         
        """
        pass
    @EndCapName.setter
    def EndCapName(self, endCapName: str):
        """
        Setter for property: (str) EndCapName
         Returns the end cap name   
            
         
        """
        pass
    @property
    def EnumCornerTreatmentType(self) -> EndcapBuilder.CornerTreatmentTypes:
        """
        Getter for property: ( EndcapBuilder.CornerTreatmentTypes NXOpen.Features) EnumCornerTreatmentType
         Returns the end cap corner treatment type   
            
         
        """
        pass
    @EnumCornerTreatmentType.setter
    def EnumCornerTreatmentType(self, enumCornerTreatmentType: EndcapBuilder.CornerTreatmentTypes):
        """
        Setter for property: ( EndcapBuilder.CornerTreatmentTypes NXOpen.Features) EnumCornerTreatmentType
         Returns the end cap corner treatment type   
            
         
        """
        pass
    @property
    def Member(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Member
         Returns the member   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset between end cap and inside face of member  
            
         
        """
        pass
    @property
    def OffsetRatio(self) -> float:
        """
        Getter for property: (float) OffsetRatio
         Returns the offset ratio   
            
         
        """
        pass
    @OffsetRatio.setter
    def OffsetRatio(self, offsetRatio: float):
        """
        Setter for property: (float) OffsetRatio
         Returns the offset ratio   
            
         
        """
        pass
    @property
    def PlacementType(self) -> EndcapBuilder.PlacementTypes:
        """
        Getter for property: ( EndcapBuilder.PlacementTypes NXOpen.Features) PlacementType
         Returns the placement type   
            
         
        """
        pass
    @PlacementType.setter
    def PlacementType(self, placementType: EndcapBuilder.PlacementTypes):
        """
        Setter for property: ( EndcapBuilder.PlacementTypes NXOpen.Features) PlacementType
         Returns the placement type   
            
         
        """
        pass
    @property
    def PreserveOverallLength(self) -> bool:
        """
        Getter for property: (bool) PreserveOverallLength
         Returns the preserveOverallLength   
            
         
        """
        pass
    @PreserveOverallLength.setter
    def PreserveOverallLength(self, preserveOverallLength: bool):
        """
        Setter for property: (bool) PreserveOverallLength
         Returns the preserveOverallLength   
            
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns the thickness   
            
         
        """
        pass
import NXOpen.Features
class Endcap(NXOpen.Features.BodyFeature): 
    """ Represents a endcap feature """
    pass
import NXOpen
class ExportDSTVBuilder(NXOpen.Builder): 
    """
          This is to create a NXOpen.Features.StructureDesign.ExportDSTVBuilder which is used to export DSTV
         """
    class ActionTypes(Enum):
        """
        Members Include: 
         |CreateNew|  Creating dataset action type. 
         |OverwriteExisting|  Overwriting dataset action type. 
         |ExportToFolder|  Exporting to folder action type. 

        """
        CreateNew: int
        OverwriteExisting: int
        ExportToFolder: int
        @staticmethod
        def ValueOf(value: int) -> ExportDSTVBuilder.ActionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionType(self) -> ExportDSTVBuilder.ActionTypes:
        """
        Getter for property: ( ExportDSTVBuilder.ActionTypes NXOpen.Features) ActionType
         Returns the option to indicate how to save DSTV file.  
             
         
        """
        pass
    @ActionType.setter
    def ActionType(self, actionTypeOption: ExportDSTVBuilder.ActionTypes):
        """
        Setter for property: ( ExportDSTVBuilder.ActionTypes NXOpen.Features) ActionType
         Returns the option to indicate how to save DSTV file.  
             
         
        """
        pass
    @property
    def ExportFileFolder(self) -> str:
        """
        Getter for property: (str) ExportFileFolder
         Returns the DSTV file folder.  
             
         
        """
        pass
    @ExportFileFolder.setter
    def ExportFileFolder(self, fileFolder: str):
        """
        Setter for property: (str) ExportFileFolder
         Returns the DSTV file folder.  
             
         
        """
        pass
    @property
    def ExportFileName(self) -> str:
        """
        Getter for property: (str) ExportFileName
         Returns the DSTV file name prefix.  
             
         
        """
        pass
    @ExportFileName.setter
    def ExportFileName(self, filenName: str):
        """
        Setter for property: (str) ExportFileName
         Returns the DSTV file name prefix.  
             
         
        """
        pass
    @property
    def ProjectName(self) -> str:
        """
        Getter for property: (str) ProjectName
         Returns the project name.  
             
         
        """
        pass
    @ProjectName.setter
    def ProjectName(self, projectName: str):
        """
        Setter for property: (str) ProjectName
         Returns the project name.  
             
         
        """
        pass
    @property
    def SelectStructureParts(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectStructureParts
         Returns the selected structures or members to export   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class ExtendMemberBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a Features.StructureDesign.ExtendMember builder
        """
    @property
    def Plane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @Plane.setter
    def Plane(self, plane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) Plane
         Returns the plane   
            
         
        """
        pass
    @property
    def SelectBoundary(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectBoundary
         Returns the trim and extension boundary   
            
         
        """
        pass
    @property
    def SelectEndFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectEndFaces
         Returns the member end faces   
            
         
        """
        pass
    def Preview(self) -> None:
        """
         Preview bodies of the feature, for code coverage 
        """
        pass
import NXOpen.Features
class ExtendMember(NXOpen.Features.BodyFeature): 
    """ Represents a extend member feature """
    pass
import NXOpen.Features
class FeatureParmsBuilder(NXOpen.Features.FeatureBuilder): 
    """
    This class is used to create or edit the information shared among all Structure Design features.
    """
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
         Returns the tolerance, in degrees, used to determine when angles are zero.  
             
         
        """
        pass
    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: float):
        """
        Setter for property: (float) AngularTolerance
         Returns the tolerance, in degrees, used to determine when angles are zero.  
             
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the tolerance used to determine when distances are considered zero.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the tolerance used to determine when distances are considered zero.  
             
         
        """
        pass
import NXOpen.Features.ShipDesign
class FeatureSpreadsheetBuilder(NXOpen.Features.ShipDesign.SteelFeatureSpreadsheetBuilder): 
    """
        Represents a NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder builder. 
        """
    pass
import NXOpen
class Frame3DBuilder(FeatureParmsBuilder): 
    """
    Represents a builder which is used to create or edit a Structure Design Frame3D feature.
    """
    class OperationTypes(Enum):
        """
        Members Include: 
         |Creation| 
         |Edit| 
         |HandleOnly| 

        """
        Creation: int
        Edit: int
        HandleOnly: int
        @staticmethod
        def ValueOf(value: int) -> Frame3DBuilder.OperationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def InPreview(self) -> bool:
        """
        Getter for property: (bool) InPreview
         Returns the preview mode.  
             
         
        """
        pass
    @InPreview.setter
    def InPreview(self, isInPreview: bool):
        """
        Setter for property: (bool) InPreview
         Returns the preview mode.  
             
         
        """
        pass
    def AddOriginOffset(self, offset: NXOpen.Vector3d) -> None:
        """
         Adds a starting point offset from the selected objects for the next operation. 
        """
        pass
    def AndPointToBuilder(self, pointTag: NXOpen.Point) -> None:
        """
         Adds point to builder. 
        """
        pass
    def CreateFrameCurve(self, startPoint: NXOpen.Point3d, endPoint: NXOpen.Point3d) -> None:
        """
         Creates a frame curve. 
        """
        pass
    def CreateTempFramePoint(self, existingPointTag: NXOpen.Point) -> NXOpen.Point:
        """
         Creates a temporary frame point from a snapped point to operate with. 
         Returns tempPointTag ( NXOpen.Point): .
        """
        pass
    def DeleteObjects(self, objectTags: List[NXOpen.TaggedObject]) -> None:
        """
         Deletes objects belonging to the active frame. 
        """
        pass
    def ExecuteDragByRayOperation(self, selectedObjectTags: List[NXOpen.TaggedObject], newOrigin: NXOpen.Point3d, axisDir: NXOpen.Vector3d, snapPoint: NXOpen.Point3d, snapDistance: float, individualMode: bool, breakMode: bool) -> None:
        """
         Executes drag by ray operation for selected objects. 
        """
        pass
    def ExecuteDrawByRayOperation(self, selectedObjectTags: List[NXOpen.TaggedObject], newOrigin: NXOpen.Point3d, axisDir: NXOpen.Vector3d, snapPoint: NXOpen.Point3d, snapDistance: float, individualMode: bool) -> None:
        """
         Executes draw by ray operation for selected objects. 
        """
        pass
    def ExecuteLinearDragOperation(self, selectedObjectTags: List[NXOpen.TaggedObject], dragDir: NXOpen.Vector3d, dragDistance: float, snapPoint: NXOpen.Point3d, snapDistance: float, individualMode: bool, breakMode: bool) -> None:
        """
         Executes linear drag operation for selected objects. 
        """
        pass
    def ExecuteLinearDrawOperation(self, selectedObjectTags: List[NXOpen.TaggedObject], dragDir: NXOpen.Vector3d, dragDistance: float, snapPoint: NXOpen.Point3d, snapDistance: float, individualMode: bool) -> None:
        """
         Executes linear draw operation for selected objects. 
        """
        pass
    def ExecutePlanarDragOperation(self, selectedObjectTags: List[NXOpen.TaggedObject], planeLocation: NXOpen.Point3d, planeNormal: NXOpen.Vector3d, snapPoint: NXOpen.Point3d, snapDistance: float, individualMode: bool, breakMode: bool) -> None:
        """
         Executes planar drag operation for selected objects. 
        """
        pass
    def ExecutePlanarDrawOperation(self, selectedObjectTags: List[NXOpen.TaggedObject], planeLocation: NXOpen.Point3d, planeNormal: NXOpen.Vector3d, snapPoint: NXOpen.Point3d, snapDistance: float, individualMode: bool) -> None:
        """
         Executes planar draw operation for selected objects. 
        """
        pass
import NXOpen.Features
class Frame3D(NXOpen.Features.CurveFeature): 
    """ Represents a frame 3d feature. """
    pass
import NXOpen
import NXOpen.Features
class GrabTabBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a Features.StructureDesign.GrabTab builder """
    class AnchorPoints(Enum):
        """
        Members Include: 
         |Left| 
         |Center| 
         |Right| 

        """
        Left: int
        Center: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> GrabTabBuilder.AnchorPoints:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlaceDirections(Enum):
        """
        Members Include: 
         |Horizontal| 
         |Vertical| 

        """
        Horizontal: int
        Vertical: int
        @staticmethod
        def ValueOf(value: int) -> GrabTabBuilder.PlaceDirections:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnchorPoint(self) -> GrabTabBuilder.AnchorPoints:
        """
        Getter for property: ( GrabTabBuilder.AnchorPoints NXOpen.Features) AnchorPoint
         Returns the anchor point   
            
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: GrabTabBuilder.AnchorPoints):
        """
        Setter for property: ( GrabTabBuilder.AnchorPoints NXOpen.Features) AnchorPoint
         Returns the anchor point   
            
         
        """
        pass
    @property
    def Attachment(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Attachment
         Returns the placement face  
            
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def GrabTabName(self) -> str:
        """
        Getter for property: (str) GrabTabName
         Returns the grab tab name   
            
         
        """
        pass
    @GrabTabName.setter
    def GrabTabName(self, grabTabName: str):
        """
        Setter for property: (str) GrabTabName
         Returns the grab tab name   
            
         
        """
        pass
    @property
    def OrientVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) OrientVector
         Returns the orientation vector.  
             
         
        """
        pass
    @OrientVector.setter
    def OrientVector(self, orientVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) OrientVector
         Returns the orientation vector.  
             
         
        """
        pass
    @property
    def PlaceDirection(self) -> GrabTabBuilder.PlaceDirections:
        """
        Getter for property: ( GrabTabBuilder.PlaceDirections NXOpen.Features) PlaceDirection
         Returns the placement direction   
            
         
        """
        pass
    @PlaceDirection.setter
    def PlaceDirection(self, placementDirection: GrabTabBuilder.PlaceDirections):
        """
        Setter for property: ( GrabTabBuilder.PlaceDirections NXOpen.Features) PlaceDirection
         Returns the placement direction   
            
         
        """
        pass
    @property
    def Reference1(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Reference1
         Returns the select reference 1   
            
         
        """
        pass
    @property
    def Reference1Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Reference1Offset
         Returns the x offset.  
             
         
        """
        pass
    @property
    def Reference1ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) Reference1ReverseFlange
         Returns the flag to specify whether the x offset direction is reversed or not.  
             
         
        """
        pass
    @Reference1ReverseFlange.setter
    def Reference1ReverseFlange(self, reference1ReverseFlange: bool):
        """
        Setter for property: (bool) Reference1ReverseFlange
         Returns the flag to specify whether the x offset direction is reversed or not.  
             
         
        """
        pass
    @property
    def Reference2(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Reference2
         Returns the select reference 2   
            
         
        """
        pass
    @property
    def Reference2Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Reference2Offset
         Returns the y offset.  
             
         
        """
        pass
    @property
    def Reference2ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) Reference2ReverseFlange
         Returns the flag to specify whether the y offset direction is reversed or not.  
             
         
        """
        pass
    @Reference2ReverseFlange.setter
    def Reference2ReverseFlange(self, reference2ReverseFlange: bool):
        """
        Setter for property: (bool) Reference2ReverseFlange
         Returns the flag to specify whether the y offset direction is reversed or not.  
             
         
        """
        pass
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngle
         Returns the rotate angle   
            
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the member.  
            
         
        """
        pass
import NXOpen.Features
class GrabTab(NXOpen.Features.BodyFeature): 
    """ Represents a grab tab feature """
    pass
import NXOpen
import NXOpen.Features
class GussetBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design Gusset feature.
        """
    class AlignmentTypes(Enum):
        """
        Members Include: 
         |GussetPlate| 
         |LappedPlate| 

        """
        GussetPlate: int
        LappedPlate: int
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.AlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositionTypes(Enum):
        """
        Members Include: 
         |Offset| 
         |Center| 
         |AlignToEdge| 

        """
        Offset: int
        Center: int
        AlignToEdge: int
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.PositionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessTypes(Enum):
        """
        Members Include: 
         |BothSides| 
         |InnerSide| 
         |OuterSide| 

        """
        BothSides: int
        InnerSide: int
        OuterSide: int
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.ThicknessTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddAlignment(self) -> bool:
        """
        Getter for property: (bool) AddAlignment
         Returns the flag to indicate whether to use alignment object to position the gussets or not.  
            
         
        """
        pass
    @AddAlignment.setter
    def AddAlignment(self, addAlignment: bool):
        """
        Setter for property: (bool) AddAlignment
         Returns the flag to indicate whether to use alignment object to position the gussets or not.  
            
         
        """
        pass
    @property
    def Alignment(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Alignment
         Returns the alignment object used for positioning multiple gussets.  
             
         
        """
        pass
    @property
    def AlignmentType(self) -> GussetBuilder.AlignmentTypes:
        """
        Getter for property: ( GussetBuilder.AlignmentTypes NXOpen.Features) AlignmentType
         Returns the alignment type to be used to locate gusset   
            
         
        """
        pass
    @AlignmentType.setter
    def AlignmentType(self, alignmentType: GussetBuilder.AlignmentTypes):
        """
        Setter for property: ( GussetBuilder.AlignmentTypes NXOpen.Features) AlignmentType
         Returns the alignment type to be used to locate gusset   
            
         
        """
        pass
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
         Returns    the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        
                            gusset placement orign and orientation evaluation
                            gusset geometry construction
                        
                    
                      
         
        """
        pass
    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: float):
        """
        Setter for property: (float) AngularTolerance
         Returns    the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        
                            gusset placement orign and orientation evaluation
                            gusset geometry construction
                        
                    
                      
         
        """
        pass
    @property
    def AttachmentOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AttachmentOffset
         Returns  the lapped offset distance in the attachment face.  
            
         
        """
        pass
    @property
    def AttachmentPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) AttachmentPointNormal
         Returns the pick point normal on attachment face.  
             
         
        """
        pass
    @AttachmentPointNormal.setter
    def AttachmentPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) AttachmentPointNormal
         Returns the pick point normal on attachment face.  
             
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def Counts(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Counts
         Returns the number of gussets created   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns    the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        
                            gusset placement orign and orientation evaluation
                            gusset geometry construction
                        
                    
                      
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns    the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        
                            gusset placement orign and orientation evaluation
                            gusset geometry construction
                        
                    
                      
         
        """
        pass
    @property
    def FirstFaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FirstFaceSelect
         Returns the firstface to be used at locate gusset  
            
         
        """
        pass
    @property
    def FlangeData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) FlangeData
         Returns the stock data used to define the stock information of the gusset.  
            
         
        """
        pass
    @property
    def GussetName(self) -> str:
        """
        Getter for property: (str) GussetName
         Returns the gusset name   
            
         
        """
        pass
    @GussetName.setter
    def GussetName(self, gussetName: str):
        """
        Setter for property: (str) GussetName
         Returns the gusset name   
            
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns  the offset to the alignment plane in gusset plate type.  
            
         
        """
        pass
    @property
    def OrientVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) OrientVector
         Returns the specify line to help locate gusset when one face is curved surface and the other is plane.  
             
         
        """
        pass
    @OrientVector.setter
    def OrientVector(self, orientVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) OrientVector
         Returns the specify line to help locate gusset when one face is curved surface and the other is plane.  
             
         
        """
        pass
    @property
    def PickPointOnAttachment(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PickPointOnAttachment
         Returns    the pick point on attachment face.  
            
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                      
                    It is only used when  NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType 
                    is set to  Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment .   
                   
         
        """
        pass
    @PickPointOnAttachment.setter
    def PickPointOnAttachment(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PickPointOnAttachment
         Returns    the pick point on attachment face.  
            
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                      
                    It is only used when  NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType 
                    is set to  Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment .   
                   
         
        """
        pass
    @property
    def PickPointOnReinforcement(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PickPointOnReinforcement
         Returns    the pick point on reinforcement face.  
            
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                   
         
        """
        pass
    @PickPointOnReinforcement.setter
    def PickPointOnReinforcement(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PickPointOnReinforcement
         Returns    the pick point on reinforcement face.  
            
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                   
         
        """
        pass
    @property
    def PitchAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PitchAngle
         Returns the angle   
            
         
        """
        pass
    @property
    def PositionType(self) -> GussetBuilder.PositionTypes:
        """
        Getter for property: ( GussetBuilder.PositionTypes NXOpen.Features) PositionType
         Returns the position to be used to locate origin   
            
         
        """
        pass
    @PositionType.setter
    def PositionType(self, positionType: GussetBuilder.PositionTypes):
        """
        Setter for property: ( GussetBuilder.PositionTypes NXOpen.Features) PositionType
         Returns the position to be used to locate origin   
            
         
        """
        pass
    @property
    def ReinforcementOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReinforcementOffset
         Returns  the lapped offset distance in the reinforcement face.  
            
         
        """
        pass
    @property
    def ReinforcementPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) ReinforcementPointNormal
         Returns the pick point normal on reinforcement face.  
             
         
        """
        pass
    @ReinforcementPointNormal.setter
    def ReinforcementPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) ReinforcementPointNormal
         Returns the pick point normal on reinforcement face.  
             
         
        """
        pass
    @property
    def ReverseAlignEdge(self) -> bool:
        """
        Getter for property: (bool) ReverseAlignEdge
         Returns the flag to specify whether the gusset align edge direction is reversed or not.  
             
         
        """
        pass
    @ReverseAlignEdge.setter
    def ReverseAlignEdge(self, reverseAlignEdge: bool):
        """
        Setter for property: (bool) ReverseAlignEdge
         Returns the flag to specify whether the gusset align edge direction is reversed or not.  
             
         
        """
        pass
    @property
    def ReverseAttachmentOffsetFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseAttachmentOffsetFlange
         Returns the flag to indicate whether the lapped offset direction in attachment face is reversed or not.  
             
         
        """
        pass
    @ReverseAttachmentOffsetFlange.setter
    def ReverseAttachmentOffsetFlange(self, reverseAttachmentOffsetFlange: bool):
        """
        Setter for property: (bool) ReverseAttachmentOffsetFlange
         Returns the flag to indicate whether the lapped offset direction in attachment face is reversed or not.  
             
         
        """
        pass
    @property
    def ReverseFirstFace(self) -> bool:
        """
        Getter for property: (bool) ReverseFirstFace
         Returns the flag to specify whether the gusset first face is reversed or not.  
             
         
        """
        pass
    @ReverseFirstFace.setter
    def ReverseFirstFace(self, reverseFirstFace: bool):
        """
        Setter for property: (bool) ReverseFirstFace
         Returns the flag to specify whether the gusset first face is reversed or not.  
             
         
        """
        pass
    @property
    def ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseFlange
         Returns the flag to specify whether the gusset offset distance direction is reversed or not.  
             
         
        """
        pass
    @ReverseFlange.setter
    def ReverseFlange(self, reverseFlange: bool):
        """
        Setter for property: (bool) ReverseFlange
         Returns the flag to specify whether the gusset offset distance direction is reversed or not.  
             
         
        """
        pass
    @property
    def ReverseReinforcementOffsetFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseReinforcementOffsetFlange
         Returns the flag to indicate whether the lapped offset direction in reinforcement face is reversed or not.  
             
         
        """
        pass
    @ReverseReinforcementOffsetFlange.setter
    def ReverseReinforcementOffsetFlange(self, reverseReinforcementOffsetFlange: bool):
        """
        Setter for property: (bool) ReverseReinforcementOffsetFlange
         Returns the flag to indicate whether the lapped offset direction in reinforcement face is reversed or not.  
             
         
        """
        pass
    @property
    def ReverseSecondFace(self) -> bool:
        """
        Getter for property: (bool) ReverseSecondFace
         Returns the flag to specify whether the gusset second face is reversed or not.  
             
         
        """
        pass
    @ReverseSecondFace.setter
    def ReverseSecondFace(self, reverseSecondFace: bool):
        """
        Setter for property: (bool) ReverseSecondFace
         Returns the flag to specify whether the gusset second face is reversed or not.  
             
         
        """
        pass
    @property
    def SecondFaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SecondFaceSelect
         Returns  the second face to be used at locate gusset  
            
         
        """
        pass
    @property
    def ThicknessType(self) -> GussetBuilder.ThicknessTypes:
        """
        Getter for property: ( GussetBuilder.ThicknessTypes NXOpen.Features) ThicknessType
         Returns the direction to be used at thicken sketch   
            
         
        """
        pass
    @ThicknessType.setter
    def ThicknessType(self, thicknessType: GussetBuilder.ThicknessTypes):
        """
        Setter for property: ( GussetBuilder.ThicknessTypes NXOpen.Features) ThicknessType
         Returns the direction to be used at thicken sketch   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class GussetConnectionBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a Structure Design Gusset Connection builder.
        """
    class JaBoltedConnectionBuilderGussetconnectionreferenceface(Enum):
        """
        Members Include: 
         |AnchorFace| 
         |AttachmentFace| 

        """
        AnchorFace: int
        AttachmentFace: int
        @staticmethod
        def ValueOf(value: int) -> GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BraceFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BraceFace
         Returns the brace member face   
            
         
        """
        pass
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Clearance
         Returns the clearance value.  
            
         
        """
        pass
    @property
    def Disabled(self) -> bool:
        """
        Getter for property: (bool) Disabled
         Returns the flag to indicate whether current builder is disabled.  
             
         
        """
        pass
    @Disabled.setter
    def Disabled(self, disabled: bool):
        """
        Setter for property: (bool) Disabled
         Returns the flag to indicate whether current builder is disabled.  
             
         
        """
        pass
    @property
    def LappedPlateAttachedMember(self) -> bool:
        """
        Getter for property: (bool) LappedPlateAttachedMember
         Returns the flag to indicate whether the current brace member is attached by a lapped plate.  
             
         
        """
        pass
    @LappedPlateAttachedMember.setter
    def LappedPlateAttachedMember(self, lappedPlateAttachedMember: bool):
        """
        Setter for property: (bool) LappedPlateAttachedMember
         Returns the flag to indicate whether the current brace member is attached by a lapped plate.  
             
         
        """
        pass
    @property
    def Modified(self) -> bool:
        """
        Getter for property: (bool) Modified
         Returns the flag to indicate whether current builder is modified.  
             
         
        """
        pass
    @Modified.setter
    def Modified(self, modified: bool):
        """
        Setter for property: (bool) Modified
         Returns the flag to indicate whether current builder is modified.  
             
         
        """
        pass
    @property
    def PreviewGenerator(self) -> BoltedConnectionBuilder:
        """
        Getter for property: ( BoltedConnectionBuilder NXOpen.Features) PreviewGenerator
         Returns the preview generator.  
            
         
        """
        pass
    @PreviewGenerator.setter
    def PreviewGenerator(self, previewGenerator: BoltedConnectionBuilder):
        """
        Setter for property: ( BoltedConnectionBuilder NXOpen.Features) PreviewGenerator
         Returns the preview generator.  
            
         
        """
        pass
    @property
    def ReferenceFace(self) -> GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface:
        """
        Getter for property: ( GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features) ReferenceFace
         Returns the clearance face.  
            
         
        """
        pass
    @ReferenceFace.setter
    def ReferenceFace(self, referenceFace: GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface):
        """
        Setter for property: ( GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features) ReferenceFace
         Returns the clearance face.  
            
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data.  
            
         
        """
        pass
    def CloneDataToSelectedBuilders(self, selectedBuilders: List[GussetConnectionBuilder]) -> None:
        """
         Clones current builder data to the selected gusset connection builders. 
        """
        pass
    def ResetFromParms(self) -> None:
        """
         Reset builder data from parms. 
        """
        pass
    def UpdateStockSectionTypes(self, sectionModified: bool) -> None:
        """
         Update stock section types by user input. 
        """
        pass
import NXOpen.Features
class Gusset(NXOpen.Features.BodyFeature): 
    """ Represents a gusset feature """
    pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class HandrailBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Features.StructureDesign.Handrail builder
    """
    class CornerTypes(Enum):
        """
        Members Include: 
         |NotSet|  leave it as it is 
         |Bend|  bend the corner 

        """
        NotSet: int
        Bend: int
        @staticmethod
        def ValueOf(value: int) -> HandrailBuilder.CornerTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HandrailTypes(Enum):
        """
        Members Include: 
         |Linear|  create linear type handrail 
         |Curved|  create curved type handrail 

        """
        Linear: int
        Curved: int
        @staticmethod
        def ValueOf(value: int) -> HandrailBuilder.HandrailTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StanchionPositionTypes(Enum):
        """
        Members Include: 
         |Gap|  Place stanchions by stanchion gap 
         |Datum|  Place stanchions on the intersection of datum and curve 

        """
        Gap: int
        Datum: int
        @staticmethod
        def ValueOf(value: int) -> HandrailBuilder.StanchionPositionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BMergePaths(self) -> bool:
        """
        Getter for property: (bool) BMergePaths
         Returns the b merge paths   
            
         
        """
        pass
    @BMergePaths.setter
    def BMergePaths(self, bMergePaths: bool):
        """
        Setter for property: (bool) BMergePaths
         Returns the b merge paths   
            
         
        """
        pass
    @property
    def BPreserveLen(self) -> bool:
        """
        Getter for property: (bool) BPreserveLen
         Returns the b preserve len   
            
         
        """
        pass
    @BPreserveLen.setter
    def BPreserveLen(self, bPreserveLen: bool):
        """
        Setter for property: (bool) BPreserveLen
         Returns the b preserve len   
            
         
        """
        pass
    @property
    def BRevStanchionDir(self) -> bool:
        """
        Getter for property: (bool) BRevStanchionDir
         Returns the b rev stanchion dir   
            
         
        """
        pass
    @BRevStanchionDir.setter
    def BRevStanchionDir(self, bRevStanchionDir: bool):
        """
        Setter for property: (bool) BRevStanchionDir
         Returns the b rev stanchion dir   
            
         
        """
        pass
    @property
    def BReversePaths(self) -> bool:
        """
        Getter for property: (bool) BReversePaths
         Returns the b reverse paths   
            
         
        """
        pass
    @BReversePaths.setter
    def BReversePaths(self, bReversePaths: bool):
        """
        Setter for property: (bool) BReversePaths
         Returns the b reverse paths   
            
         
        """
        pass
    @property
    def CornerRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CornerRadius
         Returns the corner radius   
            
         
        """
        pass
    @property
    def CornerType(self) -> HandrailBuilder.CornerTypes:
        """
        Getter for property: ( HandrailBuilder.CornerTypes NXOpen.Features) CornerType
         Returns the corner type enum   
            
         
        """
        pass
    @CornerType.setter
    def CornerType(self, cornerType: HandrailBuilder.CornerTypes):
        """
        Setter for property: ( HandrailBuilder.CornerTypes NXOpen.Features) CornerType
         Returns the corner type enum   
            
         
        """
        pass
    @property
    def DatumOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DatumOffset
         Returns the datum offset   
            
         
        """
        pass
    @property
    def EndLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndLimit
         Returns the end offset   
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the handrail.   
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the handrail.   
         
        """
        pass
    @property
    def HandrailType(self) -> HandrailBuilder.HandrailTypes:
        """
        Getter for property: ( HandrailBuilder.HandrailTypes NXOpen.Features) HandrailType
         Returns the handrail type enum   
            
         
        """
        pass
    @HandrailType.setter
    def HandrailType(self, handrailType: HandrailBuilder.HandrailTypes):
        """
        Setter for property: ( HandrailBuilder.HandrailTypes NXOpen.Features) HandrailType
         Returns the handrail type enum   
            
         
        """
        pass
    @property
    def PlaceDatums(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) PlaceDatums
         Returns the datums, which is used to place the mid stanchions of handrail   
            
         
        """
        pass
    @property
    def SelectedCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectedCurves
         Returns the selected curves   
            
         
        """
        pass
    @property
    def StanchionPositionType(self) -> HandrailBuilder.StanchionPositionTypes:
        """
        Getter for property: ( HandrailBuilder.StanchionPositionTypes NXOpen.Features) StanchionPositionType
         Returns the stanchion position type enum   
            
         
        """
        pass
    @StanchionPositionType.setter
    def StanchionPositionType(self, stanchionPositionType: HandrailBuilder.StanchionPositionTypes):
        """
        Setter for property: ( HandrailBuilder.StanchionPositionTypes NXOpen.Features) StanchionPositionType
         Returns the stanchion position type enum   
            
         
        """
        pass
    @property
    def StartLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartLimit
         Returns the start limit   
            
         
        """
        pass
    @property
    def StartPointOnLoop(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) StartPointOnLoop
         Returns the start point on loop.  
             
         
        """
        pass
    @StartPointOnLoop.setter
    def StartPointOnLoop(self, startPointOnLoop: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) StartPointOnLoop
         Returns the start point on loop.  
             
         
        """
        pass
    @property
    def StartPointOnLoopDim(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) StartPointOnLoopDim
         Returns the start point on loop.  
             
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the handrail.  
            
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the x offset   
            
         
        """
        pass
    @property
    def YOffset(self) -> HandrailYOffsetBuilder:
        """
        Getter for property: ( HandrailYOffsetBuilder NXOpen.Features) YOffset
         Returns the boundary offset   
            
         
        """
        pass
    def ApplyBendAtCorner(self) -> None:
        """
        Applyies bend at corner.
        """
        pass
    def ApplyPathXOffset(self) -> None:
        """
        Applyies x offset to path.
        """
        pass
    def ReorderPathsBeforeLimit(self) -> None:
        """
        Reorder paths before applying limits.
        """
        pass
    def SpecifyStartPointOnClosedLoop(self) -> None:
        """
        Specify start point on closed loop.
        """
        pass
    def UpdateSegmentsData(self) -> None:
        """
        Update handrail segments data
        """
        pass
import NXOpen
class HandrailYOffsetBuilder(NXOpen.Builder): 
    """ 
        Represents a HandrailYOffset builder for Structure Design. 
        
        
        This builder is used to create HandrailYOffset Data in Structure Design.
        
    """
    @property
    def YOffsetList(self) -> HandrailYOffsetListItemBuilderList:
        """
        Getter for property: ( HandrailYOffsetListItemBuilderList NXOpen.Features) YOffsetList
         Returns the handrail y offset list   
            
         
        """
        pass
    def CreateHandrailYOffsetListItemBuilder(self) -> HandrailYOffsetListItemBuilder:
        """
         The handrail y offset item creation function
         Returns yOffsetListItemBuilder ( HandrailYOffsetListItemBuilder NXOpen.Features): .
        """
        pass
import NXOpen
class HandrailYOffsetListItemBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[HandrailYOffsetListItemBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: HandrailYOffsetListItemBuilder) -> None:
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
    def Erase(self, obj: HandrailYOffsetListItemBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: HandrailYOffsetListItemBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: HandrailYOffsetListItemBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> HandrailYOffsetListItemBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( HandrailYOffsetListItemBuilder NXOpen.Features):  object found at input index .
        """
        pass
    def GetContents(self) -> List[HandrailYOffsetListItemBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( HandrailYOffsetListItemBuilder List[NXOpen.Featur):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: HandrailYOffsetListItemBuilder) -> None:
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
    def SetContents(self, objects: List[HandrailYOffsetListItemBuilder]) -> None:
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
    def Swap(self, object1: HandrailYOffsetListItemBuilder, object2: HandrailYOffsetListItemBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class HandrailYOffsetListItemBuilder(NXOpen.TaggedObject): 
    """ Handrail y offset list item builder """
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the rail.  
            
         
        """
        pass
    @property
    def XOffsetDimension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffsetDimension
         Returns the horizontal x offset dimension   
            
         
        """
        pass
    @property
    def YOffsetDimension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffsetDimension
         Returns the vertical y offset dimension   
            
         
        """
        pass
    def DeleteBuilder(self) -> None:
        """
         Delete builder.
        """
        pass
import NXOpen.Features
class Handrail(NXOpen.Features.BodyFeature): 
    """ Represents a handrail feature """
    pass
import NXOpen
import NXOpen.Features
class HaunchBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design Haunch feature.
        """
    class PlacementMethods(Enum):
        """
        Members Include: 
         |OnEdge| 
         |OnFace| 

        """
        OnEdge: int
        OnFace: int
        @staticmethod
        def ValueOf(value: int) -> HaunchBuilder.PlacementMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignmentType(self) -> GussetBuilder.AlignmentTypes:
        """
        Getter for property: ( GussetBuilder.AlignmentTypes NXOpen.Features) AlignmentType
         Returns the alignment type to be used to locate haunch   
            
         
        """
        pass
    @AlignmentType.setter
    def AlignmentType(self, alignmentType: GussetBuilder.AlignmentTypes):
        """
        Setter for property: ( GussetBuilder.AlignmentTypes NXOpen.Features) AlignmentType
         Returns the alignment type to be used to locate haunch   
            
         
        """
        pass
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
         Returns    the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        
                            haunch placement orign and orientation evaluation
                            haunch geometry construction
                        
                    
                      
         
        """
        pass
    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: float):
        """
        Setter for property: (float) AngularTolerance
         Returns    the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        
                            haunch placement orign and orientation evaluation
                            haunch geometry construction
                        
                    
                      
         
        """
        pass
    @property
    def AttachmentFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) AttachmentFace
         Returns  the attachment face to be used at locate haunch  
            
         
        """
        pass
    @property
    def AttachmentPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) AttachmentPointNormal
         Returns the pick point normal on attachment face.  
             
         
        """
        pass
    @AttachmentPointNormal.setter
    def AttachmentPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) AttachmentPointNormal
         Returns the pick point normal on attachment face.  
             
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the context attribute builder   
            
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns    the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        
                            haunch placement orign and orientation evaluation
                            haunch geometry construction
                        
                    
                      
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns    the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        
                            haunch placement orign and orientation evaluation
                            haunch geometry construction
                        
                    
                      
         
        """
        pass
    @property
    def FaceOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FaceOffset
         Returns the stiffening plate offset.  
            
         
        """
        pass
    @property
    def GussetData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) GussetData
         Returns the stock data used to define the stock information of the haunch.  
            
         
        """
        pass
    @property
    def HaunchName(self) -> str:
        """
        Getter for property: (str) HaunchName
         Returns the haunch name   
            
         
        """
        pass
    @HaunchName.setter
    def HaunchName(self, haunchName: str):
        """
        Setter for property: (str) HaunchName
         Returns the haunch name   
            
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns  the offset to the alignment plane in haunch plate type.  
            
         
        """
        pass
    @property
    def OrientVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) OrientVector
         Returns the orientation vector   
            
         
        """
        pass
    @OrientVector.setter
    def OrientVector(self, orientVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) OrientVector
         Returns the orientation vector   
            
         
        """
        pass
    @property
    def PickPointOnAttachment(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PickPointOnAttachment
         Returns    the pick point on attachment face.  
            
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                      
                    It is only used when  NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType 
                    is set to  Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment .   
                   
         
        """
        pass
    @PickPointOnAttachment.setter
    def PickPointOnAttachment(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PickPointOnAttachment
         Returns    the pick point on attachment face.  
            
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                      
                    It is only used when  NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType 
                    is set to  Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment .   
                   
         
        """
        pass
    @property
    def PickPointOnReinforcement(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) PickPointOnReinforcement
         Returns    the pick point on reinforcement face.  
            
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                   
         
        """
        pass
    @PickPointOnReinforcement.setter
    def PickPointOnReinforcement(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) PickPointOnReinforcement
         Returns    the pick point on reinforcement face.  
            
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                       It is optional. If there are multiple candidate locations and this is not set, a random location is chosen.  
                   
         
        """
        pass
    @property
    def PositionType(self) -> GussetBuilder.PositionTypes:
        """
        Getter for property: ( GussetBuilder.PositionTypes NXOpen.Features) PositionType
         Returns the position to be used to locate origin   
            
         
        """
        pass
    @PositionType.setter
    def PositionType(self, positionType: GussetBuilder.PositionTypes):
        """
        Setter for property: ( GussetBuilder.PositionTypes NXOpen.Features) PositionType
         Returns the position to be used to locate origin   
            
         
        """
        pass
    @property
    def ReinforcementFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReinforcementFace
         Returns the reinforcement face to be used at locate haunch  
            
         
        """
        pass
    @property
    def ReinforcementPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: ( NXOpen.Vector3d) ReinforcementPointNormal
         Returns the pick point normal on reinforcement face.  
             
         
        """
        pass
    @ReinforcementPointNormal.setter
    def ReinforcementPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: ( NXOpen.Vector3d) ReinforcementPointNormal
         Returns the pick point normal on reinforcement face.  
             
         
        """
        pass
    @property
    def ReverseAlignEdge(self) -> bool:
        """
        Getter for property: (bool) ReverseAlignEdge
         Returns the flag to specify whether the haunch align edge direction is reversed or not.  
             
         
        """
        pass
    @ReverseAlignEdge.setter
    def ReverseAlignEdge(self, reverseAlignEdge: bool):
        """
        Setter for property: (bool) ReverseAlignEdge
         Returns the flag to specify whether the haunch align edge direction is reversed or not.  
             
         
        """
        pass
    @property
    def ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseFlange
         Returns the flag to specify whether the haunch offset distance direction is reversed or not.  
             
         
        """
        pass
    @ReverseFlange.setter
    def ReverseFlange(self, reverseFlange: bool):
        """
        Setter for property: (bool) ReverseFlange
         Returns the flag to specify whether the haunch offset distance direction is reversed or not.  
             
         
        """
        pass
    @property
    def ReverseStiffeningOnFace(self) -> bool:
        """
        Getter for property: (bool) ReverseStiffeningOnFace
         Returns the flag to specify whether the haunch stiffening face is reversed or not.  
             
         
        """
        pass
    @ReverseStiffeningOnFace.setter
    def ReverseStiffeningOnFace(self, reverse: bool):
        """
        Setter for property: (bool) ReverseStiffeningOnFace
         Returns the flag to specify whether the haunch stiffening face is reversed or not.  
             
         
        """
        pass
    @property
    def StiffeningPlateData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StiffeningPlateData
         Returns the stock data used to define the stock information of the stiffening plate.  
            
         
        """
        pass
    @property
    def StiffeningPlatePlacementMethod(self) -> HaunchBuilder.PlacementMethods:
        """
        Getter for property: ( HaunchBuilder.PlacementMethods NXOpen.Features) StiffeningPlatePlacementMethod
         Returns the stiffening plate placement method type    
            
         
        """
        pass
    @StiffeningPlatePlacementMethod.setter
    def StiffeningPlatePlacementMethod(self, placementMethod: HaunchBuilder.PlacementMethods):
        """
        Setter for property: ( HaunchBuilder.PlacementMethods NXOpen.Features) StiffeningPlatePlacementMethod
         Returns the stiffening plate placement method type    
            
         
        """
        pass
    @property
    def ThicknessType(self) -> GussetBuilder.ThicknessTypes:
        """
        Getter for property: ( GussetBuilder.ThicknessTypes NXOpen.Features) ThicknessType
         Returns the direction to be used to thicken the gusset plate   
            
         
        """
        pass
    @ThicknessType.setter
    def ThicknessType(self, thicknessType: GussetBuilder.ThicknessTypes):
        """
        Setter for property: ( GussetBuilder.ThicknessTypes NXOpen.Features) ThicknessType
         Returns the direction to be used to thicken the gusset plate   
            
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the x offset.  
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the y offset.  
            
         
        """
        pass
import NXOpen.Features
class Haunch(NXOpen.Features.BodyFeature): 
    """ Represents a haunch feature """
    pass
import NXOpen
class IFrame(NXOpen.INXObject): 
    """ Represents a frame feature. """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class InheritStockBuilder(NXOpen.TaggedObject): 
    """
        NXOpen.Features.StructureDesign.InheritStockBuilderobject.
    """
    class StockObjectTypes(Enum):
        """
        Members Include: 
         |Member| 
         |EndCap| 
         |Gusset| 
         |GrabTab| 
         |Stiffener| 
         |BoltedConnection| 

        """
        Member: int
        EndCap: int
        Gusset: int
        GrabTab: int
        Stiffener: int
        BoltedConnection: int
        @staticmethod
        def ValueOf(value: int) -> InheritStockBuilder.StockObjectTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def UpdateStockInformation(self, stockObject: NXOpen.NXObject, stockBuilder: FeatureSpreadsheetBuilder) -> None:
        """
         Update the stock data settings using the stock of the input stock object. 
        """
        pass
import NXOpen
class LibraryBuilder(NXOpen.Builder): 
    """
        Represents a Features.StructureDesign.LibraryBuilder which is used to select the library for structure designer object creation.
        """
    @property
    def Catalog(self) -> str:
        """
        Getter for property: (str) Catalog
         Returns the catalog to use for the stock definitions.  
             
         
        """
        pass
    @Catalog.setter
    def Catalog(self, catalog: str):
        """
        Setter for property: (str) Catalog
         Returns the catalog to use for the stock definitions.  
             
         
        """
        pass
    @property
    def ProjectNumber(self) -> str:
        """
        Getter for property: (str) ProjectNumber
         Returns  the project number used as the filter on the library content.  
             
         
        """
        pass
    @ProjectNumber.setter
    def ProjectNumber(self, projectNumber: str):
        """
        Setter for property: (str) ProjectNumber
         Returns  the project number used as the filter on the library content.  
             
         
        """
        pass
import NXOpen
class MemberBuilder(FeatureParmsBuilder): 
    """
    Represents a builder which is used to create or edit a Structure Design Member feature.
    """
    class AlignMemberSelectionType(Enum):
        """
        Members Include: 
         |FacePlane| 
         |CurveEdge| 

        """
        FacePlane: int
        CurveEdge: int
        @staticmethod
        def ValueOf(value: int) -> MemberBuilder.AlignMemberSelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class EndCornerTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Miter| 
         |Butt| 
         |Cope| 
         |MatchedCope| 
         |SmartExtend| 

        """
        NotSet: int
        Miter: int
        Butt: int
        Cope: int
        MatchedCope: int
        SmartExtend: int
        @staticmethod
        def ValueOf(value: int) -> MemberBuilder.EndCornerTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlternateOrigin(self) -> int:
        """
        Getter for property: (int) AlternateOrigin
         Returns the index number of the alternate sketch origin to use.  
           This number is retrieved
                from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".  
         
        """
        pass
    @AlternateOrigin.setter
    def AlternateOrigin(self, alternateOrigin: int):
        """
        Setter for property: (int) AlternateOrigin
         Returns the index number of the alternate sketch origin to use.  
           This number is retrieved
                from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".  
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def EnableMergeColinearPath(self) -> bool:
        """
        Getter for property: (bool) EnableMergeColinearPath
         Returns the flag to enable auto merge colinear path.  
             
         
        """
        pass
    @EnableMergeColinearPath.setter
    def EnableMergeColinearPath(self, bEnableMergeColinearPath: bool):
        """
        Setter for property: (bool) EnableMergeColinearPath
         Returns the flag to enable auto merge colinear path.  
             
         
        """
        pass
    @property
    def EndCornerEnd(self) -> MemberBuilder.EndCornerTypes:
        """
        Getter for property: ( MemberBuilder.EndCornerTypes NXOpen.Features) EndCornerEnd
         Returns the corner to be used at the end of the member.  
             
         
        """
        pass
    @EndCornerEnd.setter
    def EndCornerEnd(self, endCornerEnd: MemberBuilder.EndCornerTypes):
        """
        Setter for property: ( MemberBuilder.EndCornerTypes NXOpen.Features) EndCornerEnd
         Returns the corner to be used at the end of the member.  
             
         
        """
        pass
    @property
    def EndCornerStart(self) -> MemberBuilder.EndCornerTypes:
        """
        Getter for property: ( MemberBuilder.EndCornerTypes NXOpen.Features) EndCornerStart
         Returns the corner to be used at the start of the member.  
             
         
        """
        pass
    @EndCornerStart.setter
    def EndCornerStart(self, endCornerStart: MemberBuilder.EndCornerTypes):
        """
        Setter for property: ( MemberBuilder.EndCornerTypes NXOpen.Features) EndCornerStart
         Returns the corner to be used at the start of the member.  
             
         
        """
        pass
    @property
    def EndLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndLimit
         Returns the end limit.  
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the member.   
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the member.   
         
        """
        pass
    @property
    def InheritStock(self) -> InheritStockBuilder:
        """
        Getter for property: ( InheritStockBuilder NXOpen.Features) InheritStock
         Returns the inherit stock object for member.  
            
         
        """
        pass
    @property
    def MemberCurveEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MemberCurveEdge
         Returns the member curve edge   
            
         
        """
        pass
    @property
    def MemberFacePlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MemberFacePlane
         Returns the member face plane   
            
         
        """
        pass
    @property
    def MemberPathEnd(self) -> MemberPathBuilder:
        """
        Getter for property: ( MemberPathBuilder NXOpen.Features) MemberPathEnd
         Returns the path end data for member.  
            
         
        """
        pass
    @property
    def MemberPathStart(self) -> MemberPathBuilder:
        """
        Getter for property: ( MemberPathBuilder NXOpen.Features) MemberPathStart
         Returns the path start data for member.  
            
         
        """
        pass
    @property
    def PathGeometry(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) PathGeometry
         Returns the path geometry.  
             
         
        """
        pass
    @property
    def ReferenceCurveEdge(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReferenceCurveEdge
         Returns the reference curve edge   
            
         
        """
        pass
    @property
    def ReferenceFacePlane(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) ReferenceFacePlane
         Returns the reference face plane   
            
         
        """
        pass
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngle
         Returns the rotate angle.  
            
         
        """
        pass
    @property
    def SelectionType(self) -> MemberBuilder.AlignMemberSelectionType:
        """
        Getter for property: ( MemberBuilder.AlignMemberSelectionType NXOpen.Features) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @SelectionType.setter
    def SelectionType(self, selectionType: MemberBuilder.AlignMemberSelectionType):
        """
        Setter for property: ( MemberBuilder.AlignMemberSelectionType NXOpen.Features) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @property
    def StartLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartLimit
         Returns the start limit.  
            
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the member.  
            
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the x offset.  
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the y offset.  
            
         
        """
        pass
    def CleanAfterEditingCorner(self, corner: Corner) -> None:
        """
         Clean created bodies after the editing of preview corner 
        """
        pass
    def ClearAllAdjustedPath(self) -> None:
        """
         Clears all adjusted paths.
        """
        pass
    def ClearAllCombinedCurveMap(self) -> None:
        """
         Clears all combined curve maps.
        """
        pass
    def ClearCombinedCurveMap(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Clear combined curve map
        """
        pass
    def CreatePreviewBodies(self) -> int:
        """
         Create preview bodies 
         Returns errorCode (int): .
        """
        pass
    def DeletePreviewCorners(self) -> None:
        """
         Delete preview corners
        """
        pass
    def DestroyPreviewBodies(self) -> None:
        """
         Destroy preview bodies
        """
        pass
    def DestroyPreviewBodyMap(self) -> None:
        """
         Destroy preview body map
        """
        pass
    def EvaluateStructurePositionInformation(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Enaluates structure curves or edges position information 
        """
        pass
    def FlipX(self) -> None:
        """
         Rotate the sketch 180 degrees around the X axis. 
        """
        pass
    def FlipY(self) -> None:
        """
         Rotate the sketch 180 degrees around the Y axis. 
        """
        pass
    def GetEditingPreviewCorner(self) -> Corner:
        """
         Gets the editing previewcorner. 
         Returns corner ( Corner NXOpen.Features):  The editing preview corner. .
        """
        pass
    def MakeLinkOnFlyCurveConsistent(self, inputCurve: NXOpen.NXObject) -> None:
        """
         Make link on fly curve's direction consistent with source curve or edge.
        """
        pass
    def MakePathGeometryConsistent(self) -> None:
        """
         Make path geometry's direction consistent with input curve or edge.
        """
        pass
    def PrepareBeforeEditingCorner(self, corner: Corner) -> None:
        """
         Prepare for editing the preview corner 
        """
        pass
    def SetEditingPreviewCorner(self, corner: Corner) -> None:
        """
         Sets the editing preview corner
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class MemberPathBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder which is used to create or edit a Structure Design Member Path.
    """
    class MemberPathMethod(Enum):
        """
        Members Include: 
         |Members| 
         |Csys| 
         |Point| 

        """
        Members: int
        Csys: int
        Point: int
        @staticmethod
        def ValueOf(value: int) -> MemberPathBuilder.MemberPathMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def CoordSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) CoordSystem
         Returns the coord system   
            
         
        """
        pass
    @CoordSystem.setter
    def CoordSystem(self, coordSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) CoordSystem
         Returns the coord system   
            
         
        """
        pass
    @property
    def PathMethod(self) -> MemberPathBuilder.MemberPathMethod:
        """
        Getter for property: ( MemberPathBuilder.MemberPathMethod NXOpen.Features) PathMethod
         Returns the path method   
            
         
        """
        pass
    @PathMethod.setter
    def PathMethod(self, pathMethod: MemberPathBuilder.MemberPathMethod):
        """
        Setter for property: ( MemberPathBuilder.MemberPathMethod NXOpen.Features) PathMethod
         Returns the path method   
            
         
        """
        pass
    @property
    def PathOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PathOffset
         Returns the exp face path offset   
            
         
        """
        pass
    @property
    def PathPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PathPoint
         Returns the path point   
            
         
        """
        pass
    @PathPoint.setter
    def PathPoint(self, pathPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PathPoint
         Returns the path point   
            
         
        """
        pass
    @property
    def SelectFirstMember(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectFirstMember
         Returns the select first face   
            
         
        """
        pass
    @property
    def SelectSecondMember(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectSecondMember
         Returns the select second face   
            
         
        """
        pass
import NXOpen.Features
class Member(NXOpen.Features.BodyFeature): 
    """ Represents a structure design member feature. """
    pass
import NXOpen
class MoveToContainerBuilder(NXOpen.Builder): 
    """
            This class is used to move components into sub-assmebly.
        """
    class MoveModes(Enum):
        """
        Members Include: 
         |Move|  The move only mode. 
         |Copy|  The move and copy mode. 

        """
        Move: int
        Copy: int
        @staticmethod
        def ValueOf(value: int) -> MoveToContainerBuilder.MoveModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MoveMode(self) -> MoveToContainerBuilder.MoveModes:
        """
        Getter for property: ( MoveToContainerBuilder.MoveModes NXOpen.Features) MoveMode
         Returns the option mode  
            
         
        """
        pass
    @MoveMode.setter
    def MoveMode(self, moveMode: MoveToContainerBuilder.MoveModes):
        """
        Setter for property: ( MoveToContainerBuilder.MoveModes NXOpen.Features) MoveMode
         Returns the option mode  
            
         
        """
        pass
    @property
    def SelectComponent(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectComponent
         Returns the select component to be moved to container  
            
         
        """
        pass
    @property
    def SelectContainer(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectContainer
         Returns the container to move to  
            
         
        """
        pass
import NXOpen
class NavigatorNodeBuilder(NXOpen.Builder): 
    """
        Represents a builder which is used to create Structure Design Navigator Node.
        """
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
         Returns the component name   
            
         
        """
        pass
    @ComponentName.setter
    def ComponentName(self, assemblyTemplateName: str):
        """
        Setter for property: (str) ComponentName
         Returns the component name   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class PadBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Features.StructureDesign.Pad builder
    """
    class PositionTypes(Enum):
        """
        Members Include: 
         |Center| 
         |AlignToEdge| 

        """
        Center: int
        AlignToEdge: int
        @staticmethod
        def ValueOf(value: int) -> PadBuilder.PositionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessDirections(Enum):
        """
        Members Include: 
         |AttachToEnd| 
         |TrimBack| 
         |TrimHalfThickness| 

        """
        AttachToEnd: int
        TrimBack: int
        TrimHalfThickness: int
        @staticmethod
        def ValueOf(value: int) -> PadBuilder.ThicknessDirections:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Attachment(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) Attachment
         Returns the selected attachment   
            
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def MemberEndFace(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) MemberEndFace
         Returns the selected member end face   
            
         
        """
        pass
    @property
    def PadName(self) -> str:
        """
        Getter for property: (str) PadName
         Returns the pad name   
            
         
        """
        pass
    @PadName.setter
    def PadName(self, padName: str):
        """
        Setter for property: (str) PadName
         Returns the pad name   
            
         
        """
        pass
    @property
    def PositionType(self) -> PadBuilder.PositionTypes:
        """
        Getter for property: ( PadBuilder.PositionTypes NXOpen.Features) PositionType
         Returns the position type   
            
         
        """
        pass
    @PositionType.setter
    def PositionType(self, positionType: PadBuilder.PositionTypes):
        """
        Setter for property: ( PadBuilder.PositionTypes NXOpen.Features) PositionType
         Returns the position type   
            
         
        """
        pass
    @property
    def ReverseXOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseXOffsetDirection
         Returns the reverse x offset direction   
            
         
        """
        pass
    @ReverseXOffsetDirection.setter
    def ReverseXOffsetDirection(self, reverseXOffsetDirection: bool):
        """
        Setter for property: (bool) ReverseXOffsetDirection
         Returns the reverse x offset direction   
            
         
        """
        pass
    @property
    def ReverseYOffsetDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseYOffsetDirection
         Returns the reverse y offset direction   
            
         
        """
        pass
    @ReverseYOffsetDirection.setter
    def ReverseYOffsetDirection(self, reverseYOffsetDirection: bool):
        """
        Setter for property: (bool) ReverseYOffsetDirection
         Returns the reverse y offset direction   
            
         
        """
        pass
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngle
         Returns the rotate angle   
            
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the Pad.  
            
         
        """
        pass
    @property
    def ThicknessDirection(self) -> PadBuilder.ThicknessDirections:
        """
        Getter for property: ( PadBuilder.ThicknessDirections NXOpen.Features) ThicknessDirection
         Returns the thickness direction   
            
         
        """
        pass
    @ThicknessDirection.setter
    def ThicknessDirection(self, thicknessDirection: PadBuilder.ThicknessDirections):
        """
        Setter for property: ( PadBuilder.ThicknessDirections NXOpen.Features) ThicknessDirection
         Returns the thickness direction   
            
         
        """
        pass
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffset
         Returns the x offset   
            
         
        """
        pass
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffset
         Returns the y offset   
            
         
        """
        pass
    def MatchMemberSize(self) -> bool:
        """
         Executes the rule to update the pad stock data. 
         Returns success (bool): .
        """
        pass
    def MatchMemberType(self) -> bool:
        """
         Executes the rule to update the pad stock data. 
         Returns success (bool): .
        """
        pass
    def SetMatched(self, matched: bool) -> None:
        """
         The flag whether has matched the rules 
        """
        pass
    def SetMemberType(self, memberType: str) -> None:
        """
         The member type 
        """
        pass
import NXOpen.Features
class Pad(NXOpen.Features.BodyFeature): 
    """ Represents a pad feature """
    pass
import NXOpen
class PatternSettingsBuilder(NXOpen.Builder): 
    """
        Represents a Features.StructureDesign.PatternSettingsBuilder which is used to manager settings 
        determining if structure designer object need to be automatically patterned at creation when dependant source has been patterned.
        """
    @property
    def AutoPatternEndCap(self) -> bool:
        """
        Getter for property: (bool) AutoPatternEndCap
         Returns the flag to indicate whether to automatically pattern the end cap feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternEndCap.setter
    def AutoPatternEndCap(self, autoPatternEndCap: bool):
        """
        Setter for property: (bool) AutoPatternEndCap
         Returns the flag to indicate whether to automatically pattern the end cap feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @property
    def AutoPatternGrabTab(self) -> bool:
        """
        Getter for property: (bool) AutoPatternGrabTab
         Returns the flag to indicate whether to automatically pattern the grab tab feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternGrabTab.setter
    def AutoPatternGrabTab(self, autoPatternGrabTab: bool):
        """
        Setter for property: (bool) AutoPatternGrabTab
         Returns the flag to indicate whether to automatically pattern the grab tab feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @property
    def AutoPatternGusset(self) -> bool:
        """
        Getter for property: (bool) AutoPatternGusset
         Returns the flag to indicate whether to automatically pattern the gusset feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternGusset.setter
    def AutoPatternGusset(self, autoPatternGusset: bool):
        """
        Setter for property: (bool) AutoPatternGusset
         Returns the flag to indicate whether to automatically pattern the gusset feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @property
    def AutoPatternHaunch(self) -> bool:
        """
        Getter for property: (bool) AutoPatternHaunch
         Returns the flag to indicate whether to automatically pattern the haunch feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternHaunch.setter
    def AutoPatternHaunch(self, autoPatternHaunch: bool):
        """
        Setter for property: (bool) AutoPatternHaunch
         Returns the flag to indicate whether to automatically pattern the haunch feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @property
    def AutoPatternMountingFeet(self) -> bool:
        """
        Getter for property: (bool) AutoPatternMountingFeet
         Returns the flag to indicate whether to automatically pattern the mounting feet feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternMountingFeet.setter
    def AutoPatternMountingFeet(self, autoPatternMountingFeet: bool):
        """
        Setter for property: (bool) AutoPatternMountingFeet
         Returns the flag to indicate whether to automatically pattern the mounting feet feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @property
    def AutoPatternPad(self) -> bool:
        """
        Getter for property: (bool) AutoPatternPad
         Returns the flag to indicate whether to automatically pattern the pad feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternPad.setter
    def AutoPatternPad(self, autoPatternPad: bool):
        """
        Setter for property: (bool) AutoPatternPad
         Returns the flag to indicate whether to automatically pattern the pad feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @property
    def AutoPatternPlate(self) -> bool:
        """
        Getter for property: (bool) AutoPatternPlate
         Returns the flag to indicate whether to automatically pattern the plate feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternPlate.setter
    def AutoPatternPlate(self, autoPatternPlate: bool):
        """
        Setter for property: (bool) AutoPatternPlate
         Returns the flag to indicate whether to automatically pattern the plate feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @property
    def AutoPatternStiffener(self) -> bool:
        """
        Getter for property: (bool) AutoPatternStiffener
         Returns the flag to indicate whether to automatically pattern the stiffener feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    @AutoPatternStiffener.setter
    def AutoPatternStiffener(self, autoPatternStiffener: bool):
        """
        Setter for property: (bool) AutoPatternStiffener
         Returns the flag to indicate whether to automatically pattern the stiffener feature at creation when dependent source has been patterned.  
             
         
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class PlateBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a NXOpen.Features.StructureDesign.Plate builder. This builder is used to
        create and edit structure design plate feature. The plate feature can be created from construction curves, 
        boundary faces or planes. 
        """
    class OffsetOptions(Enum):
        """
        Members Include: 
         |All| 
         |InsideOnly| 
         |OutsideOnly| 

        """
        All: int
        InsideOnly: int
        OutsideOnly: int
        @staticmethod
        def ValueOf(value: int) -> PlateBuilder.OffsetOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def CurveBoundary(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurveBoundary
         Returns the curve boundary, which can be a single region or multiple regions.  
           
                    In case of multiple regions, it creates multiple plates.   
         
        """
        pass
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
         Returns the distance tolerance.  
             
         
        """
        pass
    @property
    def FacePlaneBoundary(self) -> NXOpen.ExpressionCollectorSetList:
        """
        Getter for property: ( NXOpen.ExpressionCollectorSetList) FacePlaneBoundary
         Returns the selected faceplane boundary.  
             
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                    property is only used during creation of the member.   
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                    property is only used during creation of the member.   
         
        """
        pass
    @property
    def MergeRegions(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) MergeRegions
         Returns the multiple regions to merge together as plate body.  
             
         
        """
        pass
    @property
    def MoldFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) MoldFace
         Returns the mold face, which is used to create the plate body and define the plate placement.  
             
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns  the plate offset value .  
            
         
        """
        pass
    @property
    def OffsetOption(self) -> PlateBuilder.OffsetOptions:
        """
        Getter for property: ( PlateBuilder.OffsetOptions NXOpen.Features) OffsetOption
         Returns the offset option, which defines the plate side faces to be offset.  
             
         
        """
        pass
    @OffsetOption.setter
    def OffsetOption(self, offsetOption: PlateBuilder.OffsetOptions):
        """
        Setter for property: ( PlateBuilder.OffsetOptions NXOpen.Features) OffsetOption
         Returns the offset option, which defines the plate side faces to be offset.  
             
         
        """
        pass
    @property
    def PlateStock(self) -> PlateStockBuilder:
        """
        Getter for property: ( PlateStockBuilder NXOpen.Features) PlateStock
         Returns the plate stock builder, which defines the plate material, grade, thickness, mass density, thicken option and opposite thickness.  
              
         
        """
        pass
    @property
    def ProjectDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: ( NXOpen.GeometricUtilities.ProjectionOptions) ProjectDirection
         Returns the project direction, which is used to project the boundary curves to the plate mold face.  
             
         
        """
        pass
    @property
    def RegionPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) RegionPoint
         Returns the region point, which is used to identify the plate region.  
             
         
        """
        pass
    @RegionPoint.setter
    def RegionPoint(self, regionPoint: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) RegionPoint
         Returns the region point, which is used to identify the plate region.  
             
         
        """
        pass
    @property
    def Regions(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Regions
         Returns the regions to create plates  
            
         
        """
        pass
    def AddMergeRegionPoint(self, regionPoint: NXOpen.Point3d) -> None:
        """
         Adds a merge region point. If there are multiple region points, do a loop to add one by one. 
        """
        pass
    def AddRegionPoint(self, regionPoint: NXOpen.Point3d) -> None:
        """
         Adds a region point. If there are multiple region points, do a loop to add one by one. 
        """
        pass
    def ClearRegions(self) -> None:
        """
         Clears the selected regions and merged regions. 
        """
        pass
    def CreateRegions(self) -> List[NXOpen.Body]:
        """
         Creates regions to output the selected plates. 
         Returns regionBodies ( NXOpen.Body Li):  Region Bodies .
        """
        pass
    def DeleteRegions(self) -> None:
        """
         Deletes regions 
        """
        pass
    def GetMultipleRegionPoints(self) -> List[NXOpen.Point3d]:
        """
         Gets multiple region points. 
         Returns region_points ( NXOpen.Point3d Li): .
        """
        pass
    def MapRegionToRegionPoint(self, plateRegionString: str, regionPoint: NXOpen.Point3d) -> None:
        """
          Maps the user selected plate region to a region point. 
        """
        pass
    def RemoveAllMergedRegionPoints(self) -> None:
        """
         Removes all merged region points. 
        """
        pass
    def RemoveAllRegionPoints(self) -> None:
        """
         Removes all region points. 
        """
        pass
    def RemoveMergeRegionPoint(self, regionPoint: NXOpen.Point3d) -> None:
        """
         Removes a merge region point. 
        """
        pass
    def RemoveRegionPoint(self, regionPoint: NXOpen.Point3d, bMerge: bool) -> None:
        """
         Removes a region point. Plate will find the region body by the input region point and remove the cached region point.
        """
        pass
    def SetPreviewEnabled(self, enabled: bool) -> None:
        """
         Sets the status of the preview enabling status. 
        """
        pass
import NXOpen
class PlateStockBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.Features.StructureDesign.PlateStockBuilder builder. 
        """
    class ThicknessDirs(Enum):
        """
        Members Include: 
         |Up| 
         |Down| 
         |Both| 

        """
        Up: int
        Down: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> PlateStockBuilder.ThicknessDirs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OppositeThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OppositeThickness
         Returns the opposite thickness.  
             
         
        """
        pass
    @property
    def ThicknessDirection(self) -> PlateStockBuilder.ThicknessDirs:
        """
        Getter for property: ( PlateStockBuilder.ThicknessDirs NXOpen.Features) ThicknessDirection
         Returns the thickness direction   
            
         
        """
        pass
    @ThicknessDirection.setter
    def ThicknessDirection(self, thickness: PlateStockBuilder.ThicknessDirs):
        """
        Setter for property: ( PlateStockBuilder.ThicknessDirs NXOpen.Features) ThicknessDirection
         Returns the thickness direction   
            
         
        """
        pass
    def UpdateSpreadsheetData(self, paramNames: List[str], paramValues: List[str]) -> None:
        """
         It is used to update spreadsheet data. 
        """
        pass
import NXOpen.Features
class Plate(NXOpen.Features.BodyFeature): 
    """ Represents a structure plate feature """
    pass
import NXOpen
import NXOpen.Features
class PlatformBuilder(NXOpen.Features.FeatureBuilder): 
    """
     Represents a NXOpen.Features.StructureDesign.Platform builder. This builder is used to
     create and edit structure design platform feature. The platform feature can be created from construction curves.
     """
    class LegMemberCreation(Enum):
        """
        Members Include: 
         |NotSet| 
         |OnCorner| 

        """
        NotSet: int
        OnCorner: int
        @staticmethod
        def ValueOf(value: int) -> PlatformBuilder.LegMemberCreation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlateDividingOption(Enum):
        """
        Members Include: 
         |Automatically| 
         |Manually| 

        """
        Automatically: int
        Manually: int
        @staticmethod
        def ValueOf(value: int) -> PlatformBuilder.PlateDividingOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlateHandlingMethod(Enum):
        """
        Members Include: 
         |NotSet| 
         |Chamfer| 
         |Hole| 

        """
        NotSet: int
        Chamfer: int
        Hole: int
        @staticmethod
        def ValueOf(value: int) -> PlatformBuilder.PlateHandlingMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplitMemberKeepOption(Enum):
        """
        Members Include: 
         |KeepLongest| 
         |KeepShortest| 

        """
        KeepLongest: int
        KeepShortest: int
        @staticmethod
        def ValueOf(value: int) -> PlatformBuilder.SplitMemberKeepOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BottomFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BottomFace
         Returns the bottom face   
            
         
        """
        pass
    @property
    def BoundaryCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BoundaryCurve
         Returns the boundary curve   
            
         
        """
        pass
    @property
    def ConnectionCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ConnectionCurve
         Returns the connection curve   
            
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def DividingCurve(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) DividingCurve
         Returns the dividing curve   
            
         
        """
        pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the platform.   
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the platform.   
         
        """
        pass
    @property
    def LegMemberCreationType(self) -> PlatformBuilder.LegMemberCreation:
        """
        Getter for property: ( PlatformBuilder.LegMemberCreation NXOpen.Features) LegMemberCreationType
         Returns the leg member creation option   
            
         
        """
        pass
    @LegMemberCreationType.setter
    def LegMemberCreationType(self, type: PlatformBuilder.LegMemberCreation):
        """
        Setter for property: ( PlatformBuilder.LegMemberCreation NXOpen.Features) LegMemberCreationType
         Returns the leg member creation option   
            
         
        """
        pass
    @property
    def MaxPlateLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxPlateLength
         Returns the max plate length.  
            
         
        """
        pass
    @property
    def MaxPlateWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxPlateWidth
         Returns the max plate width.  
            
         
        """
        pass
    @property
    def MemberSplitOption(self) -> PlatformBuilder.SplitMemberKeepOption:
        """
        Getter for property: ( PlatformBuilder.SplitMemberKeepOption NXOpen.Features) MemberSplitOption
         Returns the member split option   
            
         
        """
        pass
    @MemberSplitOption.setter
    def MemberSplitOption(self, memberSplitOption: PlatformBuilder.SplitMemberKeepOption):
        """
        Setter for property: ( PlatformBuilder.SplitMemberKeepOption NXOpen.Features) MemberSplitOption
         Returns the member split option   
            
         
        """
        pass
    @property
    def MemberStockDataLeg(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) MemberStockDataLeg
         Returns the stock data used to define the stock information of the leg member.  
            
         
        """
        pass
    @property
    def MemberStockDataPrimary(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) MemberStockDataPrimary
         Returns the stock data used to define the stock information of the primary member.  
            
         
        """
        pass
    @property
    def MemberStockDataSupporting(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) MemberStockDataSupporting
         Returns the stock data used to define the stock information of the supporting member.  
            
         
        """
        pass
    @property
    def PlateChamferOffsetX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlateChamferOffsetX
         Returns the plate chamfer offset in X direction  
            
         
        """
        pass
    @property
    def PlateChamferOffsetY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlateChamferOffsetY
         Returns the plate chamfer offset in Y direction  
            
         
        """
        pass
    @property
    def PlateDividingMethod(self) -> PlatformBuilder.PlateDividingOption:
        """
        Getter for property: ( PlatformBuilder.PlateDividingOption NXOpen.Features) PlateDividingMethod
         Returns the plate dividing method   
            
         
        """
        pass
    @PlateDividingMethod.setter
    def PlateDividingMethod(self, plateDividingMethod: PlatformBuilder.PlateDividingOption):
        """
        Setter for property: ( PlatformBuilder.PlateDividingOption NXOpen.Features) PlateDividingMethod
         Returns the plate dividing method   
            
         
        """
        pass
    @property
    def PlateHandlingType(self) -> PlatformBuilder.PlateHandlingMethod:
        """
        Getter for property: ( PlatformBuilder.PlateHandlingMethod NXOpen.Features) PlateHandlingType
         Returns the plate handling type   
            
         
        """
        pass
    @PlateHandlingType.setter
    def PlateHandlingType(self, type: PlatformBuilder.PlateHandlingMethod):
        """
        Setter for property: ( PlatformBuilder.PlateHandlingMethod NXOpen.Features) PlateHandlingType
         Returns the plate handling type   
            
         
        """
        pass
    @property
    def PlateHoleOffsetX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlateHoleOffsetX
         Returns the plate hole offset in X direction  
            
         
        """
        pass
    @property
    def PlateHoleOffsetY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlateHoleOffsetY
         Returns the plate hole offset in Y direction  
            
         
        """
        pass
    @property
    def PlateHoleSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlateHoleSize
         Returns the plate hole size   
            
         
        """
        pass
    @property
    def PlateOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PlateOffset
         Returns the plate offset   
            
         
        """
        pass
    @property
    def PlateStock(self) -> PlateStockBuilder:
        """
        Getter for property: ( PlateStockBuilder NXOpen.Features) PlateStock
         Returns the plate stock builder, which defines the plate material, grade, thickness, mass density, thicken option and opposite thickness.  
              
         
        """
        pass
    @property
    def RotateAngleLeg(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngleLeg
         Returns the rotate angle.  
            
         
        """
        pass
    @property
    def RotateAnglePrimary(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAnglePrimary
         Returns the rotate angle.  
            
         
        """
        pass
    @property
    def RotateAngleSupporting(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotateAngleSupporting
         Returns the rotate angle.  
            
         
        """
        pass
    @property
    def XOffsetLeg(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffsetLeg
         Returns the x offset.  
            
         
        """
        pass
    @property
    def XOffsetPrimary(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffsetPrimary
         Returns the x offset.  
            
         
        """
        pass
    @property
    def XOffsetSupporting(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XOffsetSupporting
         Returns the x offset.  
            
         
        """
        pass
    @property
    def YOffsetLeg(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffsetLeg
         Returns the y offset.  
            
         
        """
        pass
    @property
    def YOffsetPrimary(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffsetPrimary
         Returns the y offset.  
            
         
        """
        pass
    @property
    def YOffsetSupporting(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YOffsetSupporting
         Returns the y offset.  
            
         
        """
        pass
    def AddStartPoint(self, startPoint: NXOpen.Point3d) -> None:
        """
         Adds the selected plate dividing start point 
        """
        pass
    def FlipXLeg(self) -> None:
        """
         Rotate the sketch 180 degrees around the X axis. 
        """
        pass
    def FlipXPrimary(self) -> None:
        """
         Rotate the sketch 180 degrees around the X axis. 
        """
        pass
    def FlipXSupporting(self) -> None:
        """
         Rotate the sketch 180 degrees around the X axis. 
        """
        pass
    def FlipYLeg(self) -> None:
        """
         Rotate the sketch 180 degrees around the Y axis. 
        """
        pass
    def FlipYPrimary(self) -> None:
        """
         Rotate the sketch 180 degrees around the Y axis. 
        """
        pass
    def FlipYSupporting(self) -> None:
        """
         Rotate the sketch 180 degrees around the Y axis. 
        """
        pass
    def ProcessBoundaryCurves(self) -> None:
        """
         Processes the selected boundary curves 
        """
        pass
    def ProcessConnectionCurves(self) -> None:
        """
         Processes the selected connection curves 
        """
        pass
    def RemoveStartPoint(self, startPoint: NXOpen.Point3d) -> None:
        """
         Removes the selected plate dividing start point
        """
        pass
    def SetLegMemberUpdate(self, bUpdate: bool) -> None:
        """
         Sets the flag if the leg member need to update in platform editing
        """
        pass
    def SetPlateUpdate(self, bUpdate: bool) -> None:
        """
         Sets the flag if the plate need to update in platform editing
        """
        pass
    def SetPrimaryMemberUpdate(self, bUpdate: bool) -> None:
        """
         Sets the flag if the primary member need to update in platform editing
        """
        pass
    def SetSupportingMemberUpdate(self, bUpdate: bool) -> None:
        """
         Sets the flag if the supporting member need to update in platform editing
        """
        pass
import NXOpen
import NXOpen.Features
class PlatformSettingsBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a Structure Design PlatformSettings builder.
        """
    @property
    def MaxPlateLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxPlateLength
         Returns the max plate length.  
            
         
        """
        pass
    @property
    def MaxPlateWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxPlateWidth
         Returns the max plate width.  
            
         
        """
        pass
import NXOpen.Features
class Platform(NXOpen.Features.BodyFeature): 
    """ Represents a plateforms feature """
    pass
class RailBuilder(MemberBuilder): 
    """
        Represents a Features.StructureDesign.Rail builder
        """
    pass
class Rail(Member): 
    """ Represents a structure design rail feature. """
    pass
import NXOpen
import NXOpen.Features
class RuleBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a Structure Design Rule builder.
        """
    class ButtOptions(Enum):
        """
        Members Include: 
         |ButtShortest| 
         |ButtLongest| 

        """
        ButtShortest: int
        ButtLongest: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.ButtOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CopeOptions(Enum):
        """
        Members Include: 
         |CopeShortest| 
         |CopeLongest| 

        """
        CopeShortest: int
        CopeLongest: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.CopeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CornerTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Miter| 
         |Butt| 
         |Cope| 
         |MatchedCope| 

        """
        NotSet: int
        Miter: int
        Butt: int
        Cope: int
        MatchedCope: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.CornerTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CustomConfigs(Enum):
        """
        Members Include: 
         |Choose| 
         |NotSet| 

        """
        Choose: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.CustomConfigs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefaultConfigs(Enum):
        """
        Members Include: 
         |Choose| 
         |NotSet| 

        """
        Choose: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.DefaultConfigs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefaultGroup1Configs(Enum):
        """
        Members Include: 
         |Choose| 
         |NotSet| 

        """
        Choose: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.DefaultGroup1Configs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefaultGroup2Configs(Enum):
        """
        Members Include: 
         |Choose| 
         |NotSet| 

        """
        Choose: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.DefaultGroup2Configs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DefaultGroup3Configs(Enum):
        """
        Members Include: 
         |Choose| 
         |NotSet| 

        """
        Choose: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.DefaultGroup3Configs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Placements(Enum):
        """
        Members Include: 
         |Inside| 
         |Center| 
         |Outside| 

        """
        Inside: int
        Center: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.Placements:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ButtOption(self) -> RuleBuilder.ButtOptions:
        """
        Getter for property: ( RuleBuilder.ButtOptions NXOpen.Features) ButtOption
         Returns the butt option   
            
         
        """
        pass
    @ButtOption.setter
    def ButtOption(self, buttOption: RuleBuilder.ButtOptions):
        """
        Setter for property: ( RuleBuilder.ButtOptions NXOpen.Features) ButtOption
         Returns the butt option   
            
         
        """
        pass
    @property
    def CopeOption(self) -> RuleBuilder.CopeOptions:
        """
        Getter for property: ( RuleBuilder.CopeOptions NXOpen.Features) CopeOption
         Returns the cope option   
            
         
        """
        pass
    @CopeOption.setter
    def CopeOption(self, copeOption: RuleBuilder.CopeOptions):
        """
        Setter for property: ( RuleBuilder.CopeOptions NXOpen.Features) CopeOption
         Returns the cope option   
            
         
        """
        pass
    @property
    def CustomGroupController(self) -> RuleBuilder.CustomConfigs:
        """
        Getter for property: ( RuleBuilder.CustomConfigs NXOpen.Features) CustomGroupController
         Returns the custom config   
            
         
        """
        pass
    @CustomGroupController.setter
    def CustomGroupController(self, customConfig: RuleBuilder.CustomConfigs):
        """
        Setter for property: ( RuleBuilder.CustomConfigs NXOpen.Features) CustomGroupController
         Returns the custom config   
            
         
        """
        pass
    @property
    def Cutback(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Cutback
         Returns the cutback value.  
            
         
        """
        pass
    @property
    def DefaultGroup1Controller(self) -> RuleBuilder.DefaultGroup1Configs:
        """
        Getter for property: ( RuleBuilder.DefaultGroup1Configs NXOpen.Features) DefaultGroup1Controller
         Returns the default group1 config   
            
         
        """
        pass
    @DefaultGroup1Controller.setter
    def DefaultGroup1Controller(self, defaultGroup1Config: RuleBuilder.DefaultGroup1Configs):
        """
        Setter for property: ( RuleBuilder.DefaultGroup1Configs NXOpen.Features) DefaultGroup1Controller
         Returns the default group1 config   
            
         
        """
        pass
    @property
    def DefaultGroup2Controller(self) -> RuleBuilder.DefaultGroup2Configs:
        """
        Getter for property: ( RuleBuilder.DefaultGroup2Configs NXOpen.Features) DefaultGroup2Controller
         Returns the default group2 config   
            
         
        """
        pass
    @DefaultGroup2Controller.setter
    def DefaultGroup2Controller(self, defaultGroup2Config: RuleBuilder.DefaultGroup2Configs):
        """
        Setter for property: ( RuleBuilder.DefaultGroup2Configs NXOpen.Features) DefaultGroup2Controller
         Returns the default group2 config   
            
         
        """
        pass
    @property
    def DefaultGroup3Controller(self) -> RuleBuilder.DefaultGroup3Configs:
        """
        Getter for property: ( RuleBuilder.DefaultGroup3Configs NXOpen.Features) DefaultGroup3Controller
         Returns the default group3 config   
            
         
        """
        pass
    @DefaultGroup3Controller.setter
    def DefaultGroup3Controller(self, defaultGroup3Config: RuleBuilder.DefaultGroup3Configs):
        """
        Setter for property: ( RuleBuilder.DefaultGroup3Configs NXOpen.Features) DefaultGroup3Controller
         Returns the default group3 config   
            
         
        """
        pass
    @property
    def DefaultGroupController(self) -> RuleBuilder.DefaultConfigs:
        """
        Getter for property: ( RuleBuilder.DefaultConfigs NXOpen.Features) DefaultGroupController
         Returns the default group config   
            
         
        """
        pass
    @DefaultGroupController.setter
    def DefaultGroupController(self, defaultConfig: RuleBuilder.DefaultConfigs):
        """
        Setter for property: ( RuleBuilder.DefaultConfigs NXOpen.Features) DefaultGroupController
         Returns the default group config   
            
         
        """
        pass
    @property
    def HorizontalCornerType(self) -> RuleBuilder.CornerTypes:
        """
        Getter for property: ( RuleBuilder.CornerTypes NXOpen.Features) HorizontalCornerType
         Returns the horizontal corner type   
            
         
        """
        pass
    @HorizontalCornerType.setter
    def HorizontalCornerType(self, horizontalCornerType: RuleBuilder.CornerTypes):
        """
        Setter for property: ( RuleBuilder.CornerTypes NXOpen.Features) HorizontalCornerType
         Returns the horizontal corner type   
            
         
        """
        pass
    @property
    def InnerCornerType(self) -> RuleBuilder.CornerTypes:
        """
        Getter for property: ( RuleBuilder.CornerTypes NXOpen.Features) InnerCornerType
         Returns the inner corner type   
            
         
        """
        pass
    @InnerCornerType.setter
    def InnerCornerType(self, innerCornerType: RuleBuilder.CornerTypes):
        """
        Setter for property: ( RuleBuilder.CornerTypes NXOpen.Features) InnerCornerType
         Returns the inner corner type   
            
         
        """
        pass
    @property
    def Placement(self) -> RuleBuilder.Placements:
        """
        Getter for property: ( RuleBuilder.Placements NXOpen.Features) Placement
         Returns the placement   
            
         
        """
        pass
    @Placement.setter
    def Placement(self, placement: RuleBuilder.Placements):
        """
        Setter for property: ( RuleBuilder.Placements NXOpen.Features) Placement
         Returns the placement   
            
         
        """
        pass
    @property
    def VerticalCornerType(self) -> RuleBuilder.CornerTypes:
        """
        Getter for property: ( RuleBuilder.CornerTypes NXOpen.Features) VerticalCornerType
         Returns the vertical corner type   
            
         
        """
        pass
    @VerticalCornerType.setter
    def VerticalCornerType(self, verticalCornerType: RuleBuilder.CornerTypes):
        """
        Setter for property: ( RuleBuilder.CornerTypes NXOpen.Features) VerticalCornerType
         Returns the vertical corner type   
            
         
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectCornerList(NXOpen.TaggedObject): 
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
    def Add(self, objectValue: Corner) -> bool:
        """
         Adds an object to the list
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    def AddWithViews(self, objects: List[Corner], views: List[NXOpen.View]) -> bool:
        """
         Adds a set of objects with views to the list
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, objects: List[Corner]) -> bool:
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
    def Add(self, selection: Corner, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
        """
         Adds the object with the objects view and objects point
            
         Returns added (bool):  True if successfully added to list;
                                          False if the object was already a member
                                          of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Corner, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Corner, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
        """
         The object being selected with the objects view and objects point and snap information.
            
         Returns added (bool):  True if successfully added all objects to the list;
                                          False if there was at least one object that was already a
                                          member of the list and duplicates are not allowed .
        """
        pass
    @overload
    def Add(self, selection: Corner, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
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
    def Contains(self, objectValue: Corner) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         Returns list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    def GetArray(self) -> List[Corner]:
        """
         Returns the list of objects in the selection list.
            
         Returns objects ( Corner List[NXOpen.Featur):  items in list .
        """
        pass
    def GetSelectObjectArray(self) -> List[NXOpen.SelectObject]:
        """
         Returns the list of SelectObjects in the selection list.
            
         Returns objects ( NXOpen.SelectObject Li):  items in list .
        """
        pass
    @overload
    def Remove(self, objectValue: Corner) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    def RemoveArray(self, objects: List[Corner]) -> bool:
        """
         Remove specified objects from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object was not a member of the list .
        """
        pass
    @overload
    def Remove(self, objectValue: Corner, view: NXOpen.View) -> bool:
        """
         Remove specified object from list.
            
         Returns removed (bool):  True if successfully removed from list;
                                            False if the object  view was not a member of the list .
        """
        pass
    @overload
    def Remove(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Corner, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Corner, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    def SetArray(self, objects: List[Corner]) -> None:
        """
         Sets the list of objects in the selection list. This will clear any existing
            items in the list.
            
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class SelectCorner(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""
    @property
    def Value(self) -> Corner:
        """
        Getter for property: ( Corner NXOpen.Features) Value
         Returns the object being selected
              
            
         
        """
        pass
    @Value.setter
    def Value(self, selection: Corner):
        """
        Setter for property: ( Corner NXOpen.Features) Value
         Returns the object being selected
              
            
         
        """
        pass
    @overload
    def GetValue(self) -> Tuple[Corner, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         Returns A tuple consisting of (selection, view, point). 
         - selection is:  Corner NXOpen.Features. selected object .
         - view is:  NXOpen.View. selected object view.
         - point is:  NXOpen.Point3d. selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[NXOpen.InferSnapType.SnapType, Corner, NXOpen.View, NXOpen.Point3d, Corner, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         Returns A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is:  NXOpen.InferSnapType.SnapType.  snap point type.
         - selection1 is:  Corner NXOpen.Features. first selected object .
         - view1 is:  NXOpen.View. first selected object view.
         - point1 is:  NXOpen.Point3d. first selected object point.
         - selection2 is:  Corner NXOpen.Features. second selected object .
         - view2 is:  NXOpen.View. second selected object view.
         - point2 is:  NXOpen.Point3d. second selected object point.

        """
        pass
    @overload
    def GetValue(self) -> Tuple[Corner, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         Returns A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is:  Corner NXOpen.Features. selected object .
         - cae_sub_type is:  NXOpen.CaeObjectType.CaeSubType. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    @overload
    def SetValue(self, selection: Corner, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    @overload
    def SetValue(self, snap_type: NXOpen.InferSnapType.SnapType, selection1: Corner, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Corner, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
        """
         The object being selected with the objects view and objects point and snap information.
            
        """
        pass
    @overload
    def SetValue(self, selection: Corner, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
import NXOpen
class SplitRailBuilder(NXOpen.Builder): 
    """
    Represents a Features.StructureDesign.SplitRailBuilder builder
    """
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset distance in the Z direction   
            
         
        """
        pass
    @property
    def SelectRailPart(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectRailPart
         Returns the select rail part   
            
         
        """
        pass
    @property
    def SelectStanchionPart(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) SelectStanchionPart
         Returns the select stanchion part   
            
         
        """
        pass
import NXOpen
import NXOpen.Features
class StiffenerBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a Features.StructureDesign.Stiffener builder
    """
    class AttachmentSides(Enum):
        """
        Members Include: 
         |Left| 
         |Right| 
         |Both| 

        """
        Left: int
        Right: int
        Both: int
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.AttachmentSides:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FillTypes(Enum):
        """
        Members Include: 
         |UppperHalf| 
         |LowerHalf| 
         |Full| 
         |MatchedCope| 

        """
        UppperHalf: int
        LowerHalf: int
        Full: int
        MatchedCope: int
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.FillTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HeightTypes(Enum):
        """
        Members Include: 
         |Default| 
         |Input| 

        """
        Default: int
        Input: int
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.HeightTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessDirs(Enum):
        """
        Members Include: 
         |Upper| 
         |Lower| 
         |Center| 

        """
        Upper: int
        Lower: int
        Center: int
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.ThicknessDirs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Alignment(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Alignment
         Returns the alignment   
            
         
        """
        pass
    @property
    def AttachmentSide(self) -> StiffenerBuilder.AttachmentSides:
        """
        Getter for property: ( StiffenerBuilder.AttachmentSides NXOpen.Features) AttachmentSide
         Returns the fill type to be used to Stiffener   
            
         
        """
        pass
    @AttachmentSide.setter
    def AttachmentSide(self, attachmentSide: StiffenerBuilder.AttachmentSides):
        """
        Setter for property: ( StiffenerBuilder.AttachmentSides NXOpen.Features) AttachmentSide
         Returns the fill type to be used to Stiffener   
            
         
        """
        pass
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: ( ContextAttributeBuilder NXOpen.Features) ContextAttribute
         Returns the structure design comp   
            
         
        """
        pass
    @property
    def DepthOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DepthOffset
         Returns the depth offset   
            
         
        """
        pass
    @property
    def FillType(self) -> StiffenerBuilder.FillTypes:
        """
        Getter for property: ( StiffenerBuilder.FillTypes NXOpen.Features) FillType
         Returns the fill type to be used to Stiffener   
            
         
        """
        pass
    @FillType.setter
    def FillType(self, fillType: StiffenerBuilder.FillTypes):
        """
        Setter for property: ( StiffenerBuilder.FillTypes NXOpen.Features) FillType
         Returns the fill type to be used to Stiffener   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height   
            
         
        """
        pass
    @property
    def HeightType(self) -> StiffenerBuilder.HeightTypes:
        """
        Getter for property: ( StiffenerBuilder.HeightTypes NXOpen.Features) HeightType
         Returns the height value type to be used to Stiffener   
            
         
        """
        pass
    @HeightType.setter
    def HeightType(self, fillType: StiffenerBuilder.HeightTypes):
        """
        Setter for property: ( StiffenerBuilder.HeightTypes NXOpen.Features) HeightType
         Returns the height value type to be used to Stiffener   
            
         
        """
        pass
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetDistance
         Returns the offset distance to the referenced object to adjust stiffener location.  
             
         
        """
        pass
    @property
    def ReverseOffset(self) -> bool:
        """
        Getter for property: (bool) ReverseOffset
         Returns the flag to specify whether the stiffener offset distance direction is reversed or not.  
             
         
        """
        pass
    @ReverseOffset.setter
    def ReverseOffset(self, reverseOffset: bool):
        """
        Setter for property: (bool) ReverseOffset
         Returns the flag to specify whether the stiffener offset distance direction is reversed or not.  
             
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectObject
         Returns the attachment   
            
         
        """
        pass
    @property
    def StiffenerName(self) -> str:
        """
        Getter for property: (str) StiffenerName
         Returns the stiffener name   
            
         
        """
        pass
    @StiffenerName.setter
    def StiffenerName(self, stiffenerName: str):
        """
        Setter for property: (str) StiffenerName
         Returns the stiffener name   
            
         
        """
        pass
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: ( FeatureSpreadsheetBuilder NXOpen.Features) StockData
         Returns the stock data used to define the stock information of the Stiffener.  
            
         
        """
        pass
    @property
    def ThicknessDir(self) -> StiffenerBuilder.ThicknessDirs:
        """
        Getter for property: ( StiffenerBuilder.ThicknessDirs NXOpen.Features) ThicknessDir
         Returns the fill type to be used to Stiffener   
            
         
        """
        pass
    @ThicknessDir.setter
    def ThicknessDir(self, fillType: StiffenerBuilder.ThicknessDirs):
        """
        Setter for property: ( StiffenerBuilder.ThicknessDirs NXOpen.Features) ThicknessDir
         Returns the fill type to be used to Stiffener   
            
         
        """
        pass
import NXOpen.Features
class Stiffener(NXOpen.Features.BodyFeature): 
    """ Represents a Stiffener feature """
    pass
import NXOpen
class SuperFrameBuilder(FeatureParmsBuilder): 
    """
    Represents a builder which is used to create or edit a Structure Design SuperFrame feature.
    """
    class BaseTypes(Enum):
        """
        Members Include: 
         |NotSet| 
         |Corners| 
         |Transform| 

        """
        NotSet: int
        Corners: int
        Transform: int
        @staticmethod
        def ValueOf(value: int) -> SuperFrameBuilder.BaseTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InputModes(Enum):
        """
        Members Include: 
         |Coordinates| 
         |Parameters| 

        """
        Coordinates: int
        Parameters: int
        @staticmethod
        def ValueOf(value: int) -> SuperFrameBuilder.InputModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransformTypes(Enum):
        """
        Members Include: 
         |Move| 
         |Copy| 
         |Split| 
         |Delete| 
         |NotSet| 

        """
        Move: int
        Copy: int
        Split: int
        Delete: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> SuperFrameBuilder.TransformTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BoundaryCurve
         Returns the tool curves selected to split   
            
         
        """
        pass
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Height
         Returns the height dimension   
            
         
        """
        pass
    @property
    def InputMode0(self) -> SuperFrameBuilder.InputModes:
        """
        Getter for property: ( SuperFrameBuilder.InputModes NXOpen.Features) InputMode0
         Returns the first point input mode  
            
         
        """
        pass
    @InputMode0.setter
    def InputMode0(self, mode0: SuperFrameBuilder.InputModes):
        """
        Setter for property: ( SuperFrameBuilder.InputModes NXOpen.Features) InputMode0
         Returns the first point input mode  
            
         
        """
        pass
    @property
    def InputMode1(self) -> SuperFrameBuilder.InputModes:
        """
        Getter for property: ( SuperFrameBuilder.InputModes NXOpen.Features) InputMode1
         Returns the second point input mode  
            
         
        """
        pass
    @InputMode1.setter
    def InputMode1(self, mode1: SuperFrameBuilder.InputModes):
        """
        Setter for property: ( SuperFrameBuilder.InputModes NXOpen.Features) InputMode1
         Returns the second point input mode  
            
         
        """
        pass
    @property
    def InputMode2(self) -> SuperFrameBuilder.InputModes:
        """
        Getter for property: ( SuperFrameBuilder.InputModes NXOpen.Features) InputMode2
         Returns the third point input mode  
            
         
        """
        pass
    @InputMode2.setter
    def InputMode2(self, mode2: SuperFrameBuilder.InputModes):
        """
        Setter for property: ( SuperFrameBuilder.InputModes NXOpen.Features) InputMode2
         Returns the third point input mode  
            
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns the length dimension   
            
         
        """
        pass
    @property
    def Point0(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point0
         Returns the first point   
            
         
        """
        pass
    @Point0.setter
    def Point0(self, point0: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point0
         Returns the first point   
            
         
        """
        pass
    @property
    def Point0X(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Point0X
         Returns the first point x coordinate   
            
         
        """
        pass
    @property
    def Point0Y(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Point0Y
         Returns the first point y coordinate   
            
         
        """
        pass
    @property
    def Point0Z(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Point0Z
         Returns the first point z coordinate   
            
         
        """
        pass
    @property
    def Point1(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point1
         Returns the second point   
            
         
        """
        pass
    @Point1.setter
    def Point1(self, point1: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point1
         Returns the second point   
            
         
        """
        pass
    @property
    def Point1X(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Point1X
         Returns the second point x coordinate   
            
         
        """
        pass
    @property
    def Point1Y(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Point1Y
         Returns the second point y coordinate   
            
         
        """
        pass
    @property
    def Point2(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point2
         Returns the third point   
            
         
        """
        pass
    @Point2.setter
    def Point2(self, point2: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point2
         Returns the third point   
            
         
        """
        pass
    @property
    def Point2Z(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Point2Z
         Returns the third point z coordinate   
            
         
        """
        pass
    @property
    def SplitCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SplitCurve
         Returns the curves selected to be split   
            
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns the width dimension   
            
         
        """
        pass
    def AddAction(self, sourceCurves: List[NXOpen.Curve], actionType: SuperFrameBuilder.TransformTypes, actionDirection: NXOpen.Vector3d, actionDistance: float) -> None:
        """
         Adds action to lists. 
        """
        pass
    def CopyCurve(self, curveTag: NXOpen.Curve) -> NXOpen.Curve:
        """
         Creates a copy of the curve. 
         Returns copiedCurveTag ( NXOpen.Curve): .
        """
        pass
    def CreateCurves(self) -> None:
        """
         Creates the frame curves. 
        """
        pass
    def DeleteCurve(self, curveTag: NXOpen.Curve) -> None:
        """
         Deletes the curve. 
        """
        pass
    def ReparentAndDeleteCurve(self, curveTag: NXOpen.Curve) -> None:
        """
         Deletes the curve and reparents dependent curves. 
        """
        pass
    def UndoAction(self) -> None:
        """
         Removes last action from lists. 
        """
        pass
    def UpdateCurve(self, curveTag: NXOpen.Curve, startPoint: NXOpen.Point3d, endPoint: NXOpen.Point3d) -> None:
        """
         Changes the curve's start and end points. 
        """
        pass
import NXOpen.Features
class SuperFrame(NXOpen.Features.BodyFeature): 
    """ Represents a structure design super frame feature. """
    pass
