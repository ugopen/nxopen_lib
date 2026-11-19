from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
## 
##         Represents a builder which is used to create Structure Design Add To Weldment.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignAddToWeldmentBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignAddToWeldmentBuilder @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class AddToWeldmentBuilder(NXOpen.Builder): 
    """
        Represents a builder which is used to create Structure Design Add To Weldment.
        """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ConsolidatedComponents
    ##   the consolidated components to add to new weldment.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def ConsolidatedComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) ConsolidatedComponents
          the consolidated components to add to new weldment.  
             
         
        """
        pass
    
    ## Getter for property: (str) WeldmentName
    ##   the weldment name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def WeldmentName(self) -> str:
        """
        Getter for property: (str) WeldmentName
          the weldment name   
            
         
        """
        pass
    
    ## Setter for property: (str) WeldmentName

    ##   the weldment name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @WeldmentName.setter
    def WeldmentName(self, weldmentName: str):
        """
        Setter for property: (str) WeldmentName
          the weldment name   
            
         
        """
        pass
    
import NXOpen
##  Used to assign welding attributes to Structure Design member edges  <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignAssignWeldingAttributesBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignAssignWeldingAttributesBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AssignWeldingAttributesBuilder(NXOpen.Builder): 
    """ Used to assign welding attributes to Structure Design member edges """


    ## Getter for property: (@link NXOpen.SelectEdgeList NXOpen.SelectEdgeList@endlink) SelectionButtWeldingEdges
    ##   the selection butt welding edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectEdgeList
    @property
    def SelectionButtWeldingEdges(self) -> NXOpen.SelectEdgeList:
        """
        Getter for property: (@link NXOpen.SelectEdgeList NXOpen.SelectEdgeList@endlink) SelectionButtWeldingEdges
          the selection butt welding edges   
            
         
        """
        pass
    
    ## Getter for property: (@link SelectCornerList NXOpen.Features.StructureDesign.SelectCornerList@endlink) SelectionCorners
    ##   the selection corners   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectCornerList
    @property
    def SelectionCorners(self) -> SelectCornerList:
        """
        Getter for property: (@link SelectCornerList NXOpen.Features.StructureDesign.SelectCornerList@endlink) SelectionCorners
          the selection corners   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectEdgeList NXOpen.SelectEdgeList@endlink) SelectionEdgesToBeClear
    ##   the selection edges to be clear   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectEdgeList
    @property
    def SelectionEdgesToBeClear(self) -> NXOpen.SelectEdgeList:
        """
        Getter for property: (@link NXOpen.SelectEdgeList NXOpen.SelectEdgeList@endlink) SelectionEdgesToBeClear
          the selection edges to be clear   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectEdgeList NXOpen.SelectEdgeList@endlink) SelectionFilletWeldingEdges
    ##   the selection fillet welding edges   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectEdgeList
    @property
    def SelectionFilletWeldingEdges(self) -> NXOpen.SelectEdgeList:
        """
        Getter for property: (@link NXOpen.SelectEdgeList NXOpen.SelectEdgeList@endlink) SelectionFilletWeldingEdges
          the selection fillet welding edges   
            
         
        """
        pass
    
## 
##         Represents a builder which is used to create or edit a Structure Design BeamCurve feature.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignBeamCurveBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignBeamCurveBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamCurveBuilder(FeatureParmsBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design BeamCurve feature.
        """
    pass


import NXOpen.Features
##  Represents a structure design beam curve feature.  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::BeamCurveBuilder  NXOpen::Features::StructureDesign::BeamCurveBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamCurve(NXOpen.Features.BodyFeature): 
    """ Represents a structure design beam curve feature. """
    pass


import NXOpen
## 
##     Represents a builder which is used to create or edit a Structure Design BeamPreparation feature.
##      <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignBeamPreparationBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignBeamPreparationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamPreparationBuilder(FeatureParmsBuilder): 
    """
    Represents a builder which is used to create or edit a Structure Design BeamPreparation feature.
    """


    ## Getter for property: (str) ComponentName
    ##   the name used for the created component file.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
          the name used for the created component file.  
            
         
        """
        pass
    
    ## Setter for property: (str) ComponentName

    ##   the name used for the created component file.  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ComponentName.setter
    def ComponentName(self, componentName: str):
        """
        Setter for property: (str) ComponentName
          the name used for the created component file.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) NonStructureBodies
    ##   the non-structure bodies to add to preparation model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def NonStructureBodies(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) NonStructureBodies
          the non-structure bodies to add to preparation model.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowBodies
    ##   the flag to indicate whether to show bodies or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def ShowBodies(self) -> bool:
        """
        Getter for property: (bool) ShowBodies
          the flag to indicate whether to show bodies or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowBodies

    ##   the flag to indicate whether to show bodies or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ShowBodies.setter
    def ShowBodies(self, showBodies: bool):
        """
        Setter for property: (bool) ShowBodies
          the flag to indicate whether to show bodies or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) StructureComponents
    ##   the structure components to beam.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def StructureComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) StructureComponents
          the structure components to beam.  
             
         
        """
        pass
    
import NXOpen.Features
##  Represents a structure design beam preparation feature.  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::BeamPreparationBuilder  NXOpen::Features::StructureDesign::BeamPreparationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class BeamPreparation(NXOpen.Features.BodyFeature): 
    """ Represents a structure design beam preparation feature. """
    pass


import NXOpen
## 
##         Represents a @link Features::StructureDesign::BoltedConnection Features::StructureDesign::BoltedConnection@endlink  builder
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignBoltedConnectionBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignBoltedConnectionBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AddFasteners </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## RotateAngle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## XOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## YOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1980.0.0  <br> 

class BoltedConnectionBuilder(FeatureParmsBuilder): 
    """
        Represents a <ja_class>Features.StructureDesign.BoltedConnection</ja_class> builder
        """


    ##  Settings to indicate the sub type of beam column bolted connection. 
    ##  The connection sub type of two connected members with bolted plate attached to one member end. 
    class BeamColumnConnectionSubTypes(Enum):
        """
        Members Include: <End> <LPlate> <FlatPlate>
        """
        End: int
        LPlate: int
        FlatPlate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.BeamColumnConnectionSubTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Settings to indicate the connection type of bolted connection. 
    ##  The splice connection type. 
    class ConnectionTypes(Enum):
        """
        Members Include: <Splice> <BeamColumn> <GussetPlate>
        """
        Splice: int
        BeamColumn: int
        GussetPlate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.ConnectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Settings to indicate the sub type of gusset plate bolted connection. 
    ##  The connection sub type of two othogonal members connect with diagonal member at the corner with bolted plate. 
    class GussetPlateConnectionSubTypes(Enum):
        """
        Members Include: <CornerPlate> <FlatPlate> <LappedPlate>
        """
        CornerPlate: int
        FlatPlate: int
        LappedPlate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.GussetPlateConnectionSubTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Settings to indicate the mounting type of bolted connection
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Middle</term><description> 
    ## </description> </item><item><term> 
    ## FlushUp</term><description> 
    ## </description> </item><item><term> 
    ## FlushDown</term><description> 
    ## </description> </item></list>
    class MountingTypes(Enum):
        """
        Members Include: <Middle> <FlushUp> <FlushDown>
        """
        Middle: int
        FlushUp: int
        FlushDown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.MountingTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Settings to indicate the sub type of splice bolted connection. 
    ##  The connection sub type of two splice connected members with bolted plate attached between the two member end. 
    class SpliceConnectionSubTypes(Enum):
        """
        Members Include: <End> <Flange> <Web>
        """
        End: int
        Flange: int
        Web: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BoltedConnectionBuilder.SpliceConnectionSubTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AddFasteners
    ##   the flag to indicate whether to add fasteners or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def AddFasteners(self) -> bool:
        """
        Getter for property: (bool) AddFasteners
          the flag to indicate whether to add fasteners or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AddFasteners

    ##   the flag to indicate whether to add fasteners or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @AddFasteners.setter
    def AddFasteners(self, addFasteners: bool):
        """
        Setter for property: (bool) AddFasteners
          the flag to indicate whether to add fasteners or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoltedConnectionBuilder.BeamColumnConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.BeamColumnConnectionSubTypes@endlink) BeamColumnConnectionSubType
    ##   an option to indicate the sub type of beam column bolted connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return BoltedConnectionBuilder.BeamColumnConnectionSubTypes
    @property
    def BeamColumnConnectionSubType(self) -> BoltedConnectionBuilder.BeamColumnConnectionSubTypes:
        """
        Getter for property: (@link BoltedConnectionBuilder.BeamColumnConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.BeamColumnConnectionSubTypes@endlink) BeamColumnConnectionSubType
          an option to indicate the sub type of beam column bolted connection.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoltedConnectionBuilder.BeamColumnConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.BeamColumnConnectionSubTypes@endlink) BeamColumnConnectionSubType

    ##   an option to indicate the sub type of beam column bolted connection.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @BeamColumnConnectionSubType.setter
    def BeamColumnConnectionSubType(self, subTypeOption: BoltedConnectionBuilder.BeamColumnConnectionSubTypes):
        """
        Setter for property: (@link BoltedConnectionBuilder.BeamColumnConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.BeamColumnConnectionSubTypes@endlink) BeamColumnConnectionSubType
          an option to indicate the sub type of beam column bolted connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyOne
    ##   the first input body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodyOne(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyOne
          the first input body   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyTwo
    ##   the second input body   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BodyTwo(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BodyTwo
          the second input body   
            
         
        """
        pass
    
    ## Getter for property: (str) BoltedConnectionName
    ##   the bolted connection name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def BoltedConnectionName(self) -> str:
        """
        Getter for property: (str) BoltedConnectionName
          the bolted connection name   
            
         
        """
        pass
    
    ## Setter for property: (str) BoltedConnectionName

    ##   the bolted connection name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @BoltedConnectionName.setter
    def BoltedConnectionName(self, strName: str):
        """
        Setter for property: (str) BoltedConnectionName
          the bolted connection name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BraceFaces
    ##   the brace faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BraceFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BraceFaces
          the brace faces   
            
         
        """
        pass
    
    ## Getter for property: (str) ConfigurationName
    ##   the fasteners configuration name  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def ConfigurationName(self) -> str:
        """
        Getter for property: (str) ConfigurationName
          the fasteners configuration name  
            
         
        """
        pass
    
    ## Setter for property: (str) ConfigurationName

    ##   the fasteners configuration name  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConfigurationName.setter
    def ConfigurationName(self, strName: str):
        """
        Setter for property: (str) ConfigurationName
          the fasteners configuration name  
            
         
        """
        pass
    
    ## Getter for property: (@link BoltedConnectionBuilder.ConnectionTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.ConnectionTypes@endlink) ConnectionType
    ##   an option to indicate the connection type of bolted connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return BoltedConnectionBuilder.ConnectionTypes
    @property
    def ConnectionType(self) -> BoltedConnectionBuilder.ConnectionTypes:
        """
        Getter for property: (@link BoltedConnectionBuilder.ConnectionTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.ConnectionTypes@endlink) ConnectionType
          an option to indicate the connection type of bolted connection.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoltedConnectionBuilder.ConnectionTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.ConnectionTypes@endlink) ConnectionType

    ##   an option to indicate the connection type of bolted connection.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ConnectionType.setter
    def ConnectionType(self, connectionTypeOption: BoltedConnectionBuilder.ConnectionTypes):
        """
        Setter for property: (@link BoltedConnectionBuilder.ConnectionTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.ConnectionTypes@endlink) ConnectionType
          an option to indicate the connection type of bolted connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the structure design comp   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the structure design comp   
            
         
        """
        pass
    
    ## Getter for property: (bool) DisableRule
    ##   the flag to indicate whether to disable rule or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def DisableRule(self) -> bool:
        """
        Getter for property: (bool) DisableRule
          the flag to indicate whether to disable rule or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) DisableRule

    ##   the flag to indicate whether to disable rule or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DisableRule.setter
    def DisableRule(self, disableRule: bool):
        """
        Setter for property: (bool) DisableRule
          the flag to indicate whether to disable rule or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) DrillThrough
    ##   the flag to indicate whether to apply hole through or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def DrillThrough(self) -> bool:
        """
        Getter for property: (bool) DrillThrough
          the flag to indicate whether to apply hole through or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) DrillThrough

    ##   the flag to indicate whether to apply hole through or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DrillThrough.setter
    def DrillThrough(self, drillThrough: bool):
        """
        Setter for property: (bool) DrillThrough
          the flag to indicate whether to apply hole through or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceOne
    ##   the first input face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceOne(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceOne
          the first input face   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceTwo
    ##   the second input face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FaceTwo(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FaceTwo
          the second input face   
            
         
        """
        pass
    
    ## Getter for property: (@link BoltedConnectionBuilder.GussetPlateConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.GussetPlateConnectionSubTypes@endlink) GussetPlateConnectionSubType
    ##   an option to indicate the sub type of gusset plate bolted connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return BoltedConnectionBuilder.GussetPlateConnectionSubTypes
    @property
    def GussetPlateConnectionSubType(self) -> BoltedConnectionBuilder.GussetPlateConnectionSubTypes:
        """
        Getter for property: (@link BoltedConnectionBuilder.GussetPlateConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.GussetPlateConnectionSubTypes@endlink) GussetPlateConnectionSubType
          an option to indicate the sub type of gusset plate bolted connection.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoltedConnectionBuilder.GussetPlateConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.GussetPlateConnectionSubTypes@endlink) GussetPlateConnectionSubType

    ##   an option to indicate the sub type of gusset plate bolted connection.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @GussetPlateConnectionSubType.setter
    def GussetPlateConnectionSubType(self, subTypeOption: BoltedConnectionBuilder.GussetPlateConnectionSubTypes):
        """
        Setter for property: (@link BoltedConnectionBuilder.GussetPlateConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.GussetPlateConnectionSubTypes@endlink) GussetPlateConnectionSubType
          an option to indicate the sub type of gusset plate bolted connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoltedConnectionBuilder.MountingTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.MountingTypes@endlink) MountingType
    ##   the mountingType   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return BoltedConnectionBuilder.MountingTypes
    @property
    def MountingType(self) -> BoltedConnectionBuilder.MountingTypes:
        """
        Getter for property: (@link BoltedConnectionBuilder.MountingTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.MountingTypes@endlink) MountingType
          the mountingType   
            
         
        """
        pass
    
    ## Setter for property: (@link BoltedConnectionBuilder.MountingTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.MountingTypes@endlink) MountingType

    ##   the mountingType   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MountingType.setter
    def MountingType(self, mountingType: BoltedConnectionBuilder.MountingTypes):
        """
        Setter for property: (@link BoltedConnectionBuilder.MountingTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.MountingTypes@endlink) MountingType
          the mountingType   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
    ##   the rotate angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
          the rotate angle   
            
         
        """
        pass
    
    ## Getter for property: (@link BoltedConnectionBuilder.SpliceConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.SpliceConnectionSubTypes@endlink) SpliceConnectionSubType
    ##   an option to indicate the sub type of splice bolted connection.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return BoltedConnectionBuilder.SpliceConnectionSubTypes
    @property
    def SpliceConnectionSubType(self) -> BoltedConnectionBuilder.SpliceConnectionSubTypes:
        """
        Getter for property: (@link BoltedConnectionBuilder.SpliceConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.SpliceConnectionSubTypes@endlink) SpliceConnectionSubType
          an option to indicate the sub type of splice bolted connection.  
             
         
        """
        pass
    
    ## Setter for property: (@link BoltedConnectionBuilder.SpliceConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.SpliceConnectionSubTypes@endlink) SpliceConnectionSubType

    ##   an option to indicate the sub type of splice bolted connection.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @SpliceConnectionSubType.setter
    def SpliceConnectionSubType(self, subTypeOption: BoltedConnectionBuilder.SpliceConnectionSubTypes):
        """
        Setter for property: (@link BoltedConnectionBuilder.SpliceConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.SpliceConnectionSubTypes@endlink) SpliceConnectionSubType
          an option to indicate the sub type of splice bolted connection.  
             
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
    ##   the stock data.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
          the stock data.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
    ##   the x offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
          the x offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
    ##   the y offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
          the y offset   
            
         
        """
        pass
    
    ##  Executes the rule to update the bolted plate stock data. 
    ##  @return executeRuleOk (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def ExecuteRule(builder: BoltedConnectionBuilder) -> bool:
        """
         Executes the rule to update the bolted plate stock data. 
         @return executeRuleOk (bool): .
        """
        pass
    
    ##  Get gusset connection builders. 
    ##  @return gussetConnectionBuilders (@link GussetConnectionBuilder List[NXOpen.Features.StructureDesign.GussetConnectionBuilder]@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def GetGussetConnectionBuilders(builder: BoltedConnectionBuilder) -> List[GussetConnectionBuilder]:
        """
         Get gusset connection builders. 
         @return gussetConnectionBuilders (@link GussetConnectionBuilder List[NXOpen.Features.StructureDesign.GussetConnectionBuilder]@endlink): .
        """
        pass
    
    ##  Update stock section types by user input. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sectionModified"> (bool) </param>
    def UpdateStockSectionTypes(builder: BoltedConnectionBuilder, sectionModified: bool) -> None:
        """
         Update stock section types by user input. 
        """
        pass
    
import NXOpen.Features
##  Represents a bolted connection feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::BoltedConnectionBuilder  NXOpen::Features::StructureDesign::BoltedConnectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class BoltedConnection(NXOpen.Features.BodyFeature): 
    """ Represents a bolted connection feature """
    pass


import NXOpen.Features.ShipDesign
## 
##         Represents a builder which is used to create or edit a Structure Design Component Drawing.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignComponentDrawingBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignComponentDrawingBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ComponentDrawingBuilder(NXOpen.Features.ShipDesign.SubAssemblyDrawingBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design Component Drawing.
        """


    ##  the drawing type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Assembly</term><description> 
    ## </description> </item><item><term> 
    ## Connection</term><description> 
    ## </description> </item><item><term> 
    ## Member</term><description> 
    ## </description> </item><item><term> 
    ## SpecialComponent</term><description> 
    ## </description> </item><item><term> 
    ## Weldment</term><description> 
    ## </description> </item></list>
    class DrawingTypeOption(Enum):
        """
        Members Include: <Assembly> <Connection> <Member> <SpecialComponent> <Weldment>
        """
        Assembly: int
        Connection: int
        Member: int
        SpecialComponent: int
        Weldment: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ComponentDrawingBuilder.DrawingTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) CreatePartsList
    ##   the flag to indicate whether to create a parts list or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def CreatePartsList(self) -> bool:
        """
        Getter for property: (bool) CreatePartsList
          the flag to indicate whether to create a parts list or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreatePartsList

    ##   the flag to indicate whether to create a parts list or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreatePartsList.setter
    def CreatePartsList(self, createPartsList: bool):
        """
        Setter for property: (bool) CreatePartsList
          the flag to indicate whether to create a parts list or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link ComponentDrawingBuilder.DrawingTypeOption NXOpen.Features.StructureDesign.ComponentDrawingBuilder.DrawingTypeOption@endlink) DrawingType
    ##   the drawing type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ComponentDrawingBuilder.DrawingTypeOption
    @property
    def DrawingType(self) -> ComponentDrawingBuilder.DrawingTypeOption:
        """
        Getter for property: (@link ComponentDrawingBuilder.DrawingTypeOption NXOpen.Features.StructureDesign.ComponentDrawingBuilder.DrawingTypeOption@endlink) DrawingType
          the drawing type.  
             
         
        """
        pass
    
    ## Setter for property: (@link ComponentDrawingBuilder.DrawingTypeOption NXOpen.Features.StructureDesign.ComponentDrawingBuilder.DrawingTypeOption@endlink) DrawingType

    ##   the drawing type.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DrawingType.setter
    def DrawingType(self, drawingType: ComponentDrawingBuilder.DrawingTypeOption):
        """
        Setter for property: (@link ComponentDrawingBuilder.DrawingTypeOption NXOpen.Features.StructureDesign.ComponentDrawingBuilder.DrawingTypeOption@endlink) DrawingType
          the drawing type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowBalloons
    ##   the flag to indicate whether to show balloons or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ShowBalloons(self) -> bool:
        """
        Getter for property: (bool) ShowBalloons
          the flag to indicate whether to show balloons or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowBalloons

    ##   the flag to indicate whether to show balloons or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ShowBalloons.setter
    def ShowBalloons(self, showBalloons: bool):
        """
        Setter for property: (bool) ShowBalloons
          the flag to indicate whether to show balloons or not.  
             
         
        """
        pass
    
import NXOpen
##  This class contains the factory method for consolidate builders.  <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignConsolidateBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignConsolidateBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ConsolidateBuilder(NXOpen.Builder): 
    """ This class contains the factory method for consolidate builders. """


    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) Container
    ##  
    ##                  the part under which are added newly created consolidation parts.  
    ##   
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Part
    @property
    def Container(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) Container
         
                         the part under which are added newly created consolidation parts.  
          
                      
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) Container

    ##  
    ##                  the part under which are added newly created consolidation parts.  
    ##   
    ##               
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Container.setter
    def Container(self, container: NXOpen.Part):
        """
        Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) Container
         
                         the part under which are added newly created consolidation parts.  
          
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ExternalComponents
    ##   the selected external components to consolidate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def ExternalComponents(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) ExternalComponents
          the selected external components to consolidate   
            
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##   the component part name under the consolidate list.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the component part name under the consolidate list.  
            
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the component part name under the consolidate list.  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
          the component part name under the consolidate list.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Structures
    ##   the selected structures to consolidate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Structures(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Structures
          the selected structures to consolidate   
            
         
        """
        pass
    
import NXOpen
##  Used to specify the "container" part for the Structure Design application  <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignContainerBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignContainerBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ContainerBuilder(NXOpen.Builder): 
    """ Used to specify the "container" part for the Structure Design application """


    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) SelectStructure
    ##  
    ##                 the part to which are added newly created Structure Design objects
    ##               
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Part
    @property
    def SelectStructure(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) SelectStructure
         
                        the part to which are added newly created Structure Design objects
                      
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) SelectStructure

    ##  
    ##                 the part to which are added newly created Structure Design objects
    ##               
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SelectStructure.setter
    def SelectStructure(self, selectStructure: NXOpen.Part):
        """
        Setter for property: (@link NXOpen.Part NXOpen.Part@endlink) SelectStructure
         
                        the part to which are added newly created Structure Design objects
                      
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##             @link NXOpen::Features::StructureDesign::ContextAttributeBuilder NXOpen::Features::StructureDesign::ContextAttributeBuilder@endlink object.
##          <br> This is an abstract class and cannot be instantiated  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ContextAttributeBuilder(NXOpen.TaggedObject): 
    """
            <ja_class>NXOpen.Features.StructureDesign.ContextAttributeBuilder</ja_class>object.
        """


    ## Getter for property: (str) ContextAttribute
    ##  
    ##                 the Context Attribute value.  
    ##    This is the value of the SAW_SUB_NAME part
    ##                 attribute added to the newly created / named objects.
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ContextAttribute(self) -> str:
        """
        Getter for property: (str) ContextAttribute
         
                        the Context Attribute value.  
           This is the value of the SAW_SUB_NAME part
                        attribute added to the newly created / named objects.
                      
         
        """
        pass
    
    ## Setter for property: (str) ContextAttribute

    ##  
    ##                 the Context Attribute value.  
    ##    This is the value of the SAW_SUB_NAME part
    ##                 attribute added to the newly created / named objects.
    ##               
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ContextAttribute.setter
    def ContextAttribute(self, contextAttribute: str):
        """
        Setter for property: (str) ContextAttribute
         
                        the Context Attribute value.  
           This is the value of the SAW_SUB_NAME part
                        attribute added to the newly created / named objects.
                      
         
        """
        pass
    
import NXOpen
##  The object containing the information about the end corner to be modified.
##      
## 
##   <br>  Created in NX1926.0.0  <br> 

class CornerNodeBuilder(NXOpen.NXObject): 
    """ The object containing the information about the end corner to be modified.
     """


    ## Getter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCorner
    ##   the setting of the end corner.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return MemberBuilder.EndCornerTypes
    @property
    def EndCorner(self) -> MemberBuilder.EndCornerTypes:
        """
        Getter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCorner
          the setting of the end corner.  
             
         
        """
        pass
    
    ## Setter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCorner

    ##   the setting of the end corner.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EndCorner.setter
    def EndCorner(self, endCorner: MemberBuilder.EndCornerTypes):
        """
        Setter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCorner
          the setting of the end corner.  
             
         
        """
        pass
    
import NXOpen
##  Represents a Corner object  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::EditCornerBuilder  NXOpen::Features::StructureDesign::EditCornerBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Corner(NXOpen.DisplayableObject): 
    """ Represents a Corner object """
    pass


import NXOpen
import NXOpen.ShipDesign
## 
##     Used to create structre structure in the Structure Design application.
##     Up direction information and catalog information are stored as user attributes on created structure part.
##      <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignCreateStructureBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignCreateStructureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Description </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1899.0.0  <br> 

class CreateStructureBuilder(NXOpen.Builder): 
    """
    Used to create structre structure in the Structure Design application.
    Up direction information and catalog information are stored as user attributes on created structure part.
    """


    ##  the part types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Structure</term><description> 
    ## </description> </item><item><term> 
    ## Design</term><description> 
    ## </description> </item></list>
    class PartTypes(Enum):
        """
        Members Include: <Structure> <Design>
        """
        Structure: int
        Design: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CreateStructureBuilder.PartTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Catalog
    ##   the catalog to use for the stock definitions.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Catalog(self) -> str:
        """
        Getter for property: (str) Catalog
          the catalog to use for the stock definitions.  
             
         
        """
        pass
    
    ## Setter for property: (str) Catalog

    ##   the catalog to use for the stock definitions.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Catalog.setter
    def Catalog(self, catalog: str):
        """
        Setter for property: (str) Catalog
          the catalog to use for the stock definitions.  
             
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the discription that would be assigned to the structure Teamcenter item.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the discription that would be assigned to the structure Teamcenter item.  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    
    ## Getter for property: (str) DesignName
    ##   the name used for the created design component file.  
    ##    If a duplicated name is found, an index number will be appended to the name. 
    ##         This property is only used during creation of structure design structure.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def DesignName(self) -> str:
        """
        Getter for property: (str) DesignName
          the name used for the created design component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    
    ## Setter for property: (str) DesignName

    ##   the name used for the created design component file.  
    ##    If a duplicated name is found, an index number will be appended to the name. 
    ##         This property is only used during creation of structure design structure.   
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DesignName.setter
    def DesignName(self, designName: str):
        """
        Setter for property: (str) DesignName
          the name used for the created design component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##   the name used for the created component file.  
    ##    If a duplicated name is found, an index number will be appended to the name. 
    ##         This property is only used during creation of structure design structure.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the name used for the created component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the name used for the created component file.  
    ##    If a duplicated name is found, an index number will be appended to the name. 
    ##         This property is only used during creation of structure design structure.   
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
          the name used for the created component file.  
           If a duplicated name is found, an index number will be appended to the name. 
                This property is only used during creation of structure design structure.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Reference
    ##    the reference objects used to evaluate the structure member orientation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Reference(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Reference
           the reference objects used to evaluate the structure member orientation.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation
    ##   the reference direction which used to determin structure member's orientation in the Structure Design application.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ReferenceOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation
          the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation

    ##   the reference direction which used to determin structure member's orientation in the Structure Design application.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ReferenceOrientation.setter
    def ReferenceOrientation(self, refOrientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation
          the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ShipDesign.NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) StructreRootNode
    ##   the structure root node for structure node creation in navigator.  
    ##    Structure node will be created under the structure root node.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.ShipDesign.NavigatorNode
    @property
    def StructreRootNode(self) -> NXOpen.ShipDesign.NavigatorNode:
        """
        Getter for property: (@link NXOpen.ShipDesign.NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) StructreRootNode
          the structure root node for structure node creation in navigator.  
           Structure node will be created under the structure root node.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.ShipDesign.NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) StructreRootNode

    ##   the structure root node for structure node creation in navigator.  
    ##    Structure node will be created under the structure root node.   
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @StructreRootNode.setter
    def StructreRootNode(self, tgStructureRootNode: NXOpen.ShipDesign.NavigatorNode):
        """
        Setter for property: (@link NXOpen.ShipDesign.NavigatorNode NXOpen.ShipDesign.NavigatorNode@endlink) StructreRootNode
          the structure root node for structure node creation in navigator.  
           Structure node will be created under the structure root node.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UpOrientation
    ##   the direction which is considered up in the Structure Design application.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def UpOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UpOrientation
          the direction which is considered up in the Structure Design application.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UpOrientation

    ##   the direction which is considered up in the Structure Design application.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @UpOrientation.setter
    def UpOrientation(self, upOrientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) UpOrientation
          the direction which is considered up in the Structure Design application.  
             
         
        """
        pass
    
import NXOpen
## 
##         Represents a builder which is used to create or edit a Structure Design Drawings feature.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignDrawingsBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignDrawingsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class DrawingsBuilder(NXOpen.Builder): 
    """
        Represents a builder which is used to create or edit a Structure Design Drawings feature.
        """


    ##  the target assembly. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Consolidated</term><description> 
    ## </description> </item><item><term> 
    ## Structure</term><description> 
    ## </description> </item><item><term> 
    ## Root</term><description> 
    ## </description> </item></list>
    class TargetAssemblyOption(Enum):
        """
        Members Include: <Consolidated> <Structure> <Root>
        """
        Consolidated: int
        Structure: int
        Root: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DrawingsBuilder.TargetAssemblyOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AssemblyBalloonsToggle
    ##   the flag to indicate whether to create assembly drawing balloons or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def AssemblyBalloonsToggle(self) -> bool:
        """
        Getter for property: (bool) AssemblyBalloonsToggle
          the flag to indicate whether to create assembly drawing balloons or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AssemblyBalloonsToggle

    ##   the flag to indicate whether to create assembly drawing balloons or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AssemblyBalloonsToggle.setter
    def AssemblyBalloonsToggle(self, assemblyBalloonsToggle: bool):
        """
        Setter for property: (bool) AssemblyBalloonsToggle
          the flag to indicate whether to create assembly drawing balloons or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) AssemblyConsolidatedList
    ##   the assembly components to draw.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def AssemblyConsolidatedList(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) AssemblyConsolidatedList
          the assembly components to draw.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AssemblyPartsListToggle
    ##   the flag to indicate whether to create an assembly drawing parts list or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AssemblyPartsListToggle(self) -> bool:
        """
        Getter for property: (bool) AssemblyPartsListToggle
          the flag to indicate whether to create an assembly drawing parts list or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AssemblyPartsListToggle

    ##   the flag to indicate whether to create an assembly drawing parts list or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AssemblyPartsListToggle.setter
    def AssemblyPartsListToggle(self, assemblyPartsListToggle: bool):
        """
        Setter for property: (bool) AssemblyPartsListToggle
          the flag to indicate whether to create an assembly drawing parts list or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) AssemblyTemplateName
    ##   the assembly drawing template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def AssemblyTemplateName(self) -> str:
        """
        Getter for property: (str) AssemblyTemplateName
          the assembly drawing template   
            
         
        """
        pass
    
    ## Setter for property: (str) AssemblyTemplateName

    ##   the assembly drawing template   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AssemblyTemplateName.setter
    def AssemblyTemplateName(self, assemblyTemplateName: str):
        """
        Setter for property: (str) AssemblyTemplateName
          the assembly drawing template   
            
         
        """
        pass
    
    ## Getter for property: (bool) AssemblyToggle
    ##   the flag to indicate whether to create an assembly drawing or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def AssemblyToggle(self) -> bool:
        """
        Getter for property: (bool) AssemblyToggle
          the flag to indicate whether to create an assembly drawing or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AssemblyToggle

    ##   the flag to indicate whether to create an assembly drawing or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AssemblyToggle.setter
    def AssemblyToggle(self, assemblyToggle: bool):
        """
        Setter for property: (bool) AssemblyToggle
          the flag to indicate whether to create an assembly drawing or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ConnectionBalloonsToggle
    ##   the flag to indicate whether to create connection drawing balloons or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ConnectionBalloonsToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectionBalloonsToggle
          the flag to indicate whether to create connection drawing balloons or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ConnectionBalloonsToggle

    ##   the flag to indicate whether to create connection drawing balloons or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ConnectionBalloonsToggle.setter
    def ConnectionBalloonsToggle(self, connectionBalloonsToggle: bool):
        """
        Setter for property: (bool) ConnectionBalloonsToggle
          the flag to indicate whether to create connection drawing balloons or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ConnectionPartsListToggle
    ##   the flag to indicate whether to create connection drawing parts lists or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ConnectionPartsListToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectionPartsListToggle
          the flag to indicate whether to create connection drawing parts lists or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ConnectionPartsListToggle

    ##   the flag to indicate whether to create connection drawing parts lists or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ConnectionPartsListToggle.setter
    def ConnectionPartsListToggle(self, connectionPartsListToggle: bool):
        """
        Setter for property: (bool) ConnectionPartsListToggle
          the flag to indicate whether to create connection drawing parts lists or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) ConnectionTemplateName
    ##   the connection drawing template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ConnectionTemplateName(self) -> str:
        """
        Getter for property: (str) ConnectionTemplateName
          the connection drawing template   
            
         
        """
        pass
    
    ## Setter for property: (str) ConnectionTemplateName

    ##   the connection drawing template   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ConnectionTemplateName.setter
    def ConnectionTemplateName(self, connectionTemplateName: str):
        """
        Setter for property: (str) ConnectionTemplateName
          the connection drawing template   
            
         
        """
        pass
    
    ## Getter for property: (bool) ConnectionToggle
    ##   the flag to indicate whether to create connection drawings or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ConnectionToggle(self) -> bool:
        """
        Getter for property: (bool) ConnectionToggle
          the flag to indicate whether to create connection drawings or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ConnectionToggle

    ##   the flag to indicate whether to create connection drawings or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ConnectionToggle.setter
    def ConnectionToggle(self, connectionToggle: bool):
        """
        Setter for property: (bool) ConnectionToggle
          the flag to indicate whether to create connection drawings or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyBack
    ##   the flag to indicate whether to create an assembly back view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyBack(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyBack
          the flag to indicate whether to create an assembly back view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyBack

    ##   the flag to indicate whether to create an assembly back view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyBack.setter
    def CreateAssemblyBack(self, createAssemblyBack: bool):
        """
        Setter for property: (bool) CreateAssemblyBack
          the flag to indicate whether to create an assembly back view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyBottom
    ##   the flag to indicate whether to create an assembly bottom view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyBottom(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyBottom
          the flag to indicate whether to create an assembly bottom view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyBottom

    ##   the flag to indicate whether to create an assembly bottom view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyBottom.setter
    def CreateAssemblyBottom(self, createAssemblyBottom: bool):
        """
        Setter for property: (bool) CreateAssemblyBottom
          the flag to indicate whether to create an assembly bottom view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyFront
    ##   the flag to indicate whether to create an assembly front view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyFront(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyFront
          the flag to indicate whether to create an assembly front view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyFront

    ##   the flag to indicate whether to create an assembly front view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyFront.setter
    def CreateAssemblyFront(self, createAssemblyFront: bool):
        """
        Setter for property: (bool) CreateAssemblyFront
          the flag to indicate whether to create an assembly front view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyIsometric
    ##   the flag to indicate whether to create an assembly isometric view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyIsometric
          the flag to indicate whether to create an assembly isometric view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyIsometric

    ##   the flag to indicate whether to create an assembly isometric view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyIsometric.setter
    def CreateAssemblyIsometric(self, createAssemblyIsometric: bool):
        """
        Setter for property: (bool) CreateAssemblyIsometric
          the flag to indicate whether to create an assembly isometric view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyLeft
    ##   the flag to indicate whether to create an assembly left view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyLeft(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyLeft
          the flag to indicate whether to create an assembly left view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyLeft

    ##   the flag to indicate whether to create an assembly left view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyLeft.setter
    def CreateAssemblyLeft(self, createAssemblyLeft: bool):
        """
        Setter for property: (bool) CreateAssemblyLeft
          the flag to indicate whether to create an assembly left view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyRight
    ##   the flag to indicate whether to create an assembly right view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyRight(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyRight
          the flag to indicate whether to create an assembly right view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyRight

    ##   the flag to indicate whether to create an assembly right view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyRight.setter
    def CreateAssemblyRight(self, createAssemblyRight: bool):
        """
        Setter for property: (bool) CreateAssemblyRight
          the flag to indicate whether to create an assembly right view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyTop
    ##   the flag to indicate whether to create an assembly top view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyTop(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyTop
          the flag to indicate whether to create an assembly top view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyTop

    ##   the flag to indicate whether to create an assembly top view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyTop.setter
    def CreateAssemblyTop(self, createAssemblyTop: bool):
        """
        Setter for property: (bool) CreateAssemblyTop
          the flag to indicate whether to create an assembly top view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateAssemblyTrimetric
    ##   the flag to indicate whether to create an assembly trimetric view or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateAssemblyTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateAssemblyTrimetric
          the flag to indicate whether to create an assembly trimetric view or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateAssemblyTrimetric

    ##   the flag to indicate whether to create an assembly trimetric view or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateAssemblyTrimetric.setter
    def CreateAssemblyTrimetric(self, createAssemblyTrimetric: bool):
        """
        Setter for property: (bool) CreateAssemblyTrimetric
          the flag to indicate whether to create an assembly trimetric view or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionBack
    ##   the flag to indicate whether to create connection back views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionBack(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionBack
          the flag to indicate whether to create connection back views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionBack

    ##   the flag to indicate whether to create connection back views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionBack.setter
    def CreateConnectionBack(self, createConnectionBack: bool):
        """
        Setter for property: (bool) CreateConnectionBack
          the flag to indicate whether to create connection back views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionBottom
    ##   the flag to indicate whether to create connection bottom views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionBottom(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionBottom
          the flag to indicate whether to create connection bottom views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionBottom

    ##   the flag to indicate whether to create connection bottom views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionBottom.setter
    def CreateConnectionBottom(self, createConnectionBottom: bool):
        """
        Setter for property: (bool) CreateConnectionBottom
          the flag to indicate whether to create connection bottom views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionFront
    ##   the flag to indicate whether to create connection front views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionFront(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionFront
          the flag to indicate whether to create connection front views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionFront

    ##   the flag to indicate whether to create connection front views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionFront.setter
    def CreateConnectionFront(self, createConnectionFront: bool):
        """
        Setter for property: (bool) CreateConnectionFront
          the flag to indicate whether to create connection front views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionIsometric
    ##   the flag to indicate whether to create connection isometric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionIsometric
          the flag to indicate whether to create connection isometric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionIsometric

    ##   the flag to indicate whether to create connection isometric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionIsometric.setter
    def CreateConnectionIsometric(self, createConnectionIsometric: bool):
        """
        Setter for property: (bool) CreateConnectionIsometric
          the flag to indicate whether to create connection isometric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionLeft
    ##   the flag to indicate whether to create connection left views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionLeft(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionLeft
          the flag to indicate whether to create connection left views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionLeft

    ##   the flag to indicate whether to create connection left views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionLeft.setter
    def CreateConnectionLeft(self, createConnectionLeft: bool):
        """
        Setter for property: (bool) CreateConnectionLeft
          the flag to indicate whether to create connection left views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionRight
    ##   the flag to indicate whether to create connection right views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionRight(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionRight
          the flag to indicate whether to create connection right views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionRight

    ##   the flag to indicate whether to create connection right views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionRight.setter
    def CreateConnectionRight(self, createConnectionRight: bool):
        """
        Setter for property: (bool) CreateConnectionRight
          the flag to indicate whether to create connection right views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionTop
    ##   the flag to indicate whether to create connection top views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionTop(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionTop
          the flag to indicate whether to create connection top views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionTop

    ##   the flag to indicate whether to create connection top views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionTop.setter
    def CreateConnectionTop(self, createConnectionTop: bool):
        """
        Setter for property: (bool) CreateConnectionTop
          the flag to indicate whether to create connection top views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateConnectionTrimetric
    ##   the flag to indicate whether to create connection trimetric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateConnectionTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateConnectionTrimetric
          the flag to indicate whether to create connection trimetric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateConnectionTrimetric

    ##   the flag to indicate whether to create connection trimetric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateConnectionTrimetric.setter
    def CreateConnectionTrimetric(self, createConnectionTrimetric: bool):
        """
        Setter for property: (bool) CreateConnectionTrimetric
          the flag to indicate whether to create connection trimetric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberBack
    ##   the flag to indicate whether to create member back views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberBack(self) -> bool:
        """
        Getter for property: (bool) CreateMemberBack
          the flag to indicate whether to create member back views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberBack

    ##   the flag to indicate whether to create member back views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberBack.setter
    def CreateMemberBack(self, createMemberBack: bool):
        """
        Setter for property: (bool) CreateMemberBack
          the flag to indicate whether to create member back views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberBottom
    ##   the flag to indicate whether to create member bottom views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberBottom(self) -> bool:
        """
        Getter for property: (bool) CreateMemberBottom
          the flag to indicate whether to create member bottom views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberBottom

    ##   the flag to indicate whether to create member bottom views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberBottom.setter
    def CreateMemberBottom(self, createMemberBottom: bool):
        """
        Setter for property: (bool) CreateMemberBottom
          the flag to indicate whether to create member bottom views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberFront
    ##   the flag to indicate whether to create member front views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberFront(self) -> bool:
        """
        Getter for property: (bool) CreateMemberFront
          the flag to indicate whether to create member front views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberFront

    ##   the flag to indicate whether to create member front views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberFront.setter
    def CreateMemberFront(self, createMemberFront: bool):
        """
        Setter for property: (bool) CreateMemberFront
          the flag to indicate whether to create member front views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberIsometric
    ##   the flag to indicate whether to create member isometric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateMemberIsometric
          the flag to indicate whether to create member isometric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberIsometric

    ##   the flag to indicate whether to create member isometric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberIsometric.setter
    def CreateMemberIsometric(self, createMemberIsometric: bool):
        """
        Setter for property: (bool) CreateMemberIsometric
          the flag to indicate whether to create member isometric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberLeft
    ##   the flag to indicate whether to create member left views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberLeft(self) -> bool:
        """
        Getter for property: (bool) CreateMemberLeft
          the flag to indicate whether to create member left views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberLeft

    ##   the flag to indicate whether to create member left views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberLeft.setter
    def CreateMemberLeft(self, createMemberLeft: bool):
        """
        Setter for property: (bool) CreateMemberLeft
          the flag to indicate whether to create member left views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberRight
    ##   the flag to indicate whether to create member right views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberRight(self) -> bool:
        """
        Getter for property: (bool) CreateMemberRight
          the flag to indicate whether to create member right views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberRight

    ##   the flag to indicate whether to create member right views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberRight.setter
    def CreateMemberRight(self, createMemberRight: bool):
        """
        Setter for property: (bool) CreateMemberRight
          the flag to indicate whether to create member right views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberTop
    ##   the flag to indicate whether to create member top views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberTop(self) -> bool:
        """
        Getter for property: (bool) CreateMemberTop
          the flag to indicate whether to create member top views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberTop

    ##   the flag to indicate whether to create member top views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberTop.setter
    def CreateMemberTop(self, createMemberTop: bool):
        """
        Setter for property: (bool) CreateMemberTop
          the flag to indicate whether to create member top views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateMemberTrimetric
    ##   the flag to indicate whether to create member trimetric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateMemberTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateMemberTrimetric
          the flag to indicate whether to create member trimetric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateMemberTrimetric

    ##   the flag to indicate whether to create member trimetric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateMemberTrimetric.setter
    def CreateMemberTrimetric(self, createMemberTrimetric: bool):
        """
        Setter for property: (bool) CreateMemberTrimetric
          the flag to indicate whether to create member trimetric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompBack
    ##   the flag to indicate whether to create special component back views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompBack(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompBack
          the flag to indicate whether to create special component back views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompBack

    ##   the flag to indicate whether to create special component back views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompBack.setter
    def CreateSpecialCompBack(self, createSpecialCompBack: bool):
        """
        Setter for property: (bool) CreateSpecialCompBack
          the flag to indicate whether to create special component back views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompBottom
    ##   the flag to indicate whether to create special component bottom views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompBottom(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompBottom
          the flag to indicate whether to create special component bottom views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompBottom

    ##   the flag to indicate whether to create special component bottom views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompBottom.setter
    def CreateSpecialCompBottom(self, createSpecialCompBottom: bool):
        """
        Setter for property: (bool) CreateSpecialCompBottom
          the flag to indicate whether to create special component bottom views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompFront
    ##   the flag to indicate whether to create special component front views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompFront(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompFront
          the flag to indicate whether to create special component front views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompFront

    ##   the flag to indicate whether to create special component front views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompFront.setter
    def CreateSpecialCompFront(self, createSpecialCompFront: bool):
        """
        Setter for property: (bool) CreateSpecialCompFront
          the flag to indicate whether to create special component front views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompIsometric
    ##   the flag to indicate whether to create special component isometric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompIsometric
          the flag to indicate whether to create special component isometric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompIsometric

    ##   the flag to indicate whether to create special component isometric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompIsometric.setter
    def CreateSpecialCompIsometric(self, createSpecialCompIsometric: bool):
        """
        Setter for property: (bool) CreateSpecialCompIsometric
          the flag to indicate whether to create special component isometric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompLeft
    ##   the flag to indicate whether to create special component left views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompLeft(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompLeft
          the flag to indicate whether to create special component left views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompLeft

    ##   the flag to indicate whether to create special component left views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompLeft.setter
    def CreateSpecialCompLeft(self, createSpecialCompLeft: bool):
        """
        Setter for property: (bool) CreateSpecialCompLeft
          the flag to indicate whether to create special component left views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompRight
    ##   the flag to indicate whether to create special component right views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompRight(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompRight
          the flag to indicate whether to create special component right views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompRight

    ##   the flag to indicate whether to create special component right views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompRight.setter
    def CreateSpecialCompRight(self, createSpecialCompRight: bool):
        """
        Setter for property: (bool) CreateSpecialCompRight
          the flag to indicate whether to create special component right views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompTop
    ##   the flag to indicate whether to create special component top views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompTop(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompTop
          the flag to indicate whether to create special component top views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompTop

    ##   the flag to indicate whether to create special component top views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompTop.setter
    def CreateSpecialCompTop(self, createSpecialCompTop: bool):
        """
        Setter for property: (bool) CreateSpecialCompTop
          the flag to indicate whether to create special component top views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateSpecialCompTrimetric
    ##   the flag to indicate whether to create special component trimetric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateSpecialCompTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateSpecialCompTrimetric
          the flag to indicate whether to create special component trimetric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateSpecialCompTrimetric

    ##   the flag to indicate whether to create special component trimetric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateSpecialCompTrimetric.setter
    def CreateSpecialCompTrimetric(self, createSpecialCompTrimetric: bool):
        """
        Setter for property: (bool) CreateSpecialCompTrimetric
          the flag to indicate whether to create special component trimetric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentBack
    ##   the flag to indicate whether to create weldment back views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentBack(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentBack
          the flag to indicate whether to create weldment back views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentBack

    ##   the flag to indicate whether to create weldment back views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentBack.setter
    def CreateWeldmentBack(self, createWeldmentBack: bool):
        """
        Setter for property: (bool) CreateWeldmentBack
          the flag to indicate whether to create weldment back views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentBottom
    ##   the flag to indicate whether to create weldment bottom views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentBottom(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentBottom
          the flag to indicate whether to create weldment bottom views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentBottom

    ##   the flag to indicate whether to create weldment bottom views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentBottom.setter
    def CreateWeldmentBottom(self, createWeldmentBottom: bool):
        """
        Setter for property: (bool) CreateWeldmentBottom
          the flag to indicate whether to create weldment bottom views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentFront
    ##   the flag to indicate whether to create weldment front views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentFront(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentFront
          the flag to indicate whether to create weldment front views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentFront

    ##   the flag to indicate whether to create weldment front views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentFront.setter
    def CreateWeldmentFront(self, createWeldmentFront: bool):
        """
        Setter for property: (bool) CreateWeldmentFront
          the flag to indicate whether to create weldment front views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentIsometric
    ##   the flag to indicate whether to create weldment isometric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentIsometric(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentIsometric
          the flag to indicate whether to create weldment isometric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentIsometric

    ##   the flag to indicate whether to create weldment isometric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentIsometric.setter
    def CreateWeldmentIsometric(self, createWeldmentIsometric: bool):
        """
        Setter for property: (bool) CreateWeldmentIsometric
          the flag to indicate whether to create weldment isometric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentLeft
    ##   the flag to indicate whether to create weldment left views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentLeft(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentLeft
          the flag to indicate whether to create weldment left views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentLeft

    ##   the flag to indicate whether to create weldment left views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentLeft.setter
    def CreateWeldmentLeft(self, createWeldmentLeft: bool):
        """
        Setter for property: (bool) CreateWeldmentLeft
          the flag to indicate whether to create weldment left views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentRight
    ##   the flag to indicate whether to create weldment right views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentRight(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentRight
          the flag to indicate whether to create weldment right views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentRight

    ##   the flag to indicate whether to create weldment right views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentRight.setter
    def CreateWeldmentRight(self, createWeldmentRight: bool):
        """
        Setter for property: (bool) CreateWeldmentRight
          the flag to indicate whether to create weldment right views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentTop
    ##   the flag to indicate whether to create weldment top views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentTop(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentTop
          the flag to indicate whether to create weldment top views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentTop

    ##   the flag to indicate whether to create weldment top views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentTop.setter
    def CreateWeldmentTop(self, createWeldmentTop: bool):
        """
        Setter for property: (bool) CreateWeldmentTop
          the flag to indicate whether to create weldment top views or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CreateWeldmentTrimetric
    ##   the flag to indicate whether to create weldment trimetric views or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def CreateWeldmentTrimetric(self) -> bool:
        """
        Getter for property: (bool) CreateWeldmentTrimetric
          the flag to indicate whether to create weldment trimetric views or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CreateWeldmentTrimetric

    ##   the flag to indicate whether to create weldment trimetric views or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CreateWeldmentTrimetric.setter
    def CreateWeldmentTrimetric(self, createWeldmentTrimetric: bool):
        """
        Setter for property: (bool) CreateWeldmentTrimetric
          the flag to indicate whether to create weldment trimetric views or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) MemberTemplateName
    ##   the member drawing template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def MemberTemplateName(self) -> str:
        """
        Getter for property: (str) MemberTemplateName
          the member drawing template   
            
         
        """
        pass
    
    ## Setter for property: (str) MemberTemplateName

    ##   the member drawing template   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MemberTemplateName.setter
    def MemberTemplateName(self, memberTemplateName: str):
        """
        Setter for property: (str) MemberTemplateName
          the member drawing template   
            
         
        """
        pass
    
    ## Getter for property: (bool) MemberToggle
    ##   the flag to indicate whether to create member drawings or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def MemberToggle(self) -> bool:
        """
        Getter for property: (bool) MemberToggle
          the flag to indicate whether to create member drawings or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MemberToggle

    ##   the flag to indicate whether to create member drawings or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @MemberToggle.setter
    def MemberToggle(self, memberToggle: bool):
        """
        Setter for property: (bool) MemberToggle
          the flag to indicate whether to create member drawings or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SpecialCompIncludeWeldToggle
    ##   the flag to indicate whether to include special components present in weldments or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def SpecialCompIncludeWeldToggle(self) -> bool:
        """
        Getter for property: (bool) SpecialCompIncludeWeldToggle
          the flag to indicate whether to include special components present in weldments or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SpecialCompIncludeWeldToggle

    ##   the flag to indicate whether to include special components present in weldments or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SpecialCompIncludeWeldToggle.setter
    def SpecialCompIncludeWeldToggle(self, specialCompIncludeWeldToggle: bool):
        """
        Setter for property: (bool) SpecialCompIncludeWeldToggle
          the flag to indicate whether to include special components present in weldments or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) SpecialCompTemplateName
    ##   the special component drawing template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def SpecialCompTemplateName(self) -> str:
        """
        Getter for property: (str) SpecialCompTemplateName
          the special component drawing template   
            
         
        """
        pass
    
    ## Setter for property: (str) SpecialCompTemplateName

    ##   the special component drawing template   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SpecialCompTemplateName.setter
    def SpecialCompTemplateName(self, specialCompTemplateName: str):
        """
        Setter for property: (str) SpecialCompTemplateName
          the special component drawing template   
            
         
        """
        pass
    
    ## Getter for property: (bool) SpecialCompToggle
    ##   the flag to indicate whether to create special component drawings or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def SpecialCompToggle(self) -> bool:
        """
        Getter for property: (bool) SpecialCompToggle
          the flag to indicate whether to create special component drawings or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SpecialCompToggle

    ##   the flag to indicate whether to create special component drawings or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SpecialCompToggle.setter
    def SpecialCompToggle(self, specialCompToggle: bool):
        """
        Setter for property: (bool) SpecialCompToggle
          the flag to indicate whether to create special component drawings or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link DrawingsBuilder.TargetAssemblyOption NXOpen.Features.StructureDesign.DrawingsBuilder.TargetAssemblyOption@endlink) TargetAssembly
    ##   the target assembly.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return DrawingsBuilder.TargetAssemblyOption
    @property
    def TargetAssembly(self) -> DrawingsBuilder.TargetAssemblyOption:
        """
        Getter for property: (@link DrawingsBuilder.TargetAssemblyOption NXOpen.Features.StructureDesign.DrawingsBuilder.TargetAssemblyOption@endlink) TargetAssembly
          the target assembly.  
             
         
        """
        pass
    
    ## Setter for property: (@link DrawingsBuilder.TargetAssemblyOption NXOpen.Features.StructureDesign.DrawingsBuilder.TargetAssemblyOption@endlink) TargetAssembly

    ##   the target assembly.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @TargetAssembly.setter
    def TargetAssembly(self, targetAssembly: DrawingsBuilder.TargetAssemblyOption):
        """
        Setter for property: (@link DrawingsBuilder.TargetAssemblyOption NXOpen.Features.StructureDesign.DrawingsBuilder.TargetAssemblyOption@endlink) TargetAssembly
          the target assembly.  
             
         
        """
        pass
    
    ## Getter for property: (bool) WeldmentBalloonsToggle
    ##   the flag to indicate whether to create weldment drawing balloons or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def WeldmentBalloonsToggle(self) -> bool:
        """
        Getter for property: (bool) WeldmentBalloonsToggle
          the flag to indicate whether to create weldment drawing balloons or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) WeldmentBalloonsToggle

    ##   the flag to indicate whether to create weldment drawing balloons or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @WeldmentBalloonsToggle.setter
    def WeldmentBalloonsToggle(self, weldmentBalloonsToggle: bool):
        """
        Setter for property: (bool) WeldmentBalloonsToggle
          the flag to indicate whether to create weldment drawing balloons or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) WeldmentPartsListToggle
    ##   the flag to indicate whether to create weldment parts list or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def WeldmentPartsListToggle(self) -> bool:
        """
        Getter for property: (bool) WeldmentPartsListToggle
          the flag to indicate whether to create weldment parts list or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) WeldmentPartsListToggle

    ##   the flag to indicate whether to create weldment parts list or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @WeldmentPartsListToggle.setter
    def WeldmentPartsListToggle(self, weldmentPartsListToggle: bool):
        """
        Setter for property: (bool) WeldmentPartsListToggle
          the flag to indicate whether to create weldment parts list or not.  
             
         
        """
        pass
    
    ## Getter for property: (str) WeldmentTemplateName
    ##   the weldment drawing template   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def WeldmentTemplateName(self) -> str:
        """
        Getter for property: (str) WeldmentTemplateName
          the weldment drawing template   
            
         
        """
        pass
    
    ## Setter for property: (str) WeldmentTemplateName

    ##   the weldment drawing template   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @WeldmentTemplateName.setter
    def WeldmentTemplateName(self, weldmentTemplateName: str):
        """
        Setter for property: (str) WeldmentTemplateName
          the weldment drawing template   
            
         
        """
        pass
    
    ## Getter for property: (bool) WeldmentToggle
    ##   the flag to indicate whether to create weldment drawings or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def WeldmentToggle(self) -> bool:
        """
        Getter for property: (bool) WeldmentToggle
          the flag to indicate whether to create weldment drawings or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) WeldmentToggle

    ##   the flag to indicate whether to create weldment drawings or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @WeldmentToggle.setter
    def WeldmentToggle(self, weldmentToggle: bool):
        """
        Setter for property: (bool) WeldmentToggle
          the flag to indicate whether to create weldment drawings or not.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Represents a @link Features::StructureDesign::EditCornerBuilder Features::StructureDesign::EditCornerBuilder@endlink  which is used 
##     edit the corners of multiple members in the Structure Design application. Only corners at one
##     connected end of the member can be modified. 
##      <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignEditCornerBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignEditCornerBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class EditCornerBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>Features.StructureDesign.EditCornerBuilder</ja_class> which is used 
    edit the corners of multiple members in the Structure Design application. Only corners at one
    connected end of the member can be modified. 
    """


    ## Getter for property: (@link SelectCorner NXOpen.Features.StructureDesign.SelectCorner@endlink) Corner
    ##   the select corner   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SelectCorner
    @property
    def Corner(self) -> SelectCorner:
        """
        Getter for property: (@link SelectCorner NXOpen.Features.StructureDesign.SelectCorner@endlink) Corner
          the select corner   
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
    ##   the stock data used to define the stock information of the member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
          the stock data used to define the stock information of the member.  
            
         
        """
        pass
    
    ##  Add butt member reference object
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ##  face or plane
    def AddMemberReferenceObjects(builder: EditCornerBuilder, iMemberIndex: int, tRefObj: List[NXOpen.NXObject]) -> None:
        """
         Add butt member reference object
        """
        pass
    
    ##  Add reference member face information
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    ## <param name="iRefMemberIndex"> (int) </param>
    ## <param name="facePoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="faceNormal"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    def AddReferenceMemberFaceInformation(builder: EditCornerBuilder, iMemberIndex: int, iRefMemberIndex: int, facePoint: NXOpen.Point3d, faceNormal: NXOpen.Vector3d) -> None:
        """
         Add reference member face information
        """
        pass
    
    ##  Gets related member bodies
    ##  @return members (@link NXOpen.Body List[NXOpen.Body]@endlink): .
    ## 
    ##   <br>  Created in NX2306.7000.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def AskMembers(builder: EditCornerBuilder) -> List[NXOpen.Body]:
        """
         Gets related member bodies
         @return members (@link NXOpen.Body List[NXOpen.Body]@endlink): .
        """
        pass
    
    ##  Clears reference member faces
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    def ClearReferenceMemberFaceInformation(builder: EditCornerBuilder, iMemberIndex: int) -> None:
        """
         Clears reference member faces
        """
        pass
    
    ##  Clears referenced member information
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    def ClearReferencedMemberInformation(builder: EditCornerBuilder, iMemberIndex: int) -> None:
        """
         Clears referenced member information
        """
        pass
    
    ##  Create the corners for the input body and adjacent members. 
    ##  @return corners (@link CornerNodeBuilder List[NXOpen.Features.StructureDesign.CornerNodeBuilder]@endlink):  The corners being processed. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Member's body in which to create a corner for, and also for adjacent corners. 
    def CreateCorners(builder: EditCornerBuilder, body: NXOpen.Body, endPoint: NXOpen.Point3d) -> List[CornerNodeBuilder]:
        """
         Create the corners for the input body and adjacent members. 
         @return corners (@link CornerNodeBuilder List[NXOpen.Features.StructureDesign.CornerNodeBuilder]@endlink):  The corners being processed. .
        """
        pass
    
    ##  Output the corner nodes being processed. 
    ##  @return corners (@link CornerNodeBuilder List[NXOpen.Features.StructureDesign.CornerNodeBuilder]@endlink):  The corners being processed. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCorners(builder: EditCornerBuilder) -> List[CornerNodeBuilder]:
        """
         Output the corner nodes being processed. 
         @return corners (@link CornerNodeBuilder List[NXOpen.Features.StructureDesign.CornerNodeBuilder]@endlink):  The corners being processed. .
        """
        pass
    
    ##  Gets the stock data used for current selected member.
    ##  @return stockData (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    def GetStockDataByMember(builder: EditCornerBuilder, iMemberIndex: int) -> FeatureSpreadsheetBuilder:
        """
         Gets the stock data used for current selected member.
         @return stockData (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink): .
        """
        pass
    
    ##  Remove the corner nodes from processing. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The corners being processed. 
    def RemoveCorners(builder: EditCornerBuilder, corners: List[CornerNodeBuilder]) -> None:
        """
         Remove the corner nodes from processing. 
        """
        pass
    
    ##  Resets the stock data
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def ResetStockData(builder: EditCornerBuilder) -> None:
        """
         Resets the stock data
        """
        pass
    
    ##  Sets cope member index
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    ## <param name="iRefCopeMemberIndex"> (int) </param>
    def SetCopeMemberIndex(builder: EditCornerBuilder, iMemberIndex: int, iRefCopeMemberIndex: int) -> None:
        """
         Sets cope member index
        """
        pass
    
    ##  Sets cope member index array
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    ## <param name="refCopeMemberIndexArray"> (List[int]) </param>
    def SetCopeMemberIndexArray(builder: EditCornerBuilder, iMemberIndex: int, refCopeMemberIndexArray: List[int]) -> None:
        """
         Sets cope member index array
        """
        pass
    
    ##  Set the corner object 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ##  The corner being processed. 
    def SetCornerObject(builder: EditCornerBuilder, corner: Corner) -> None:
        """
         Set the corner object 
        """
        pass
    
    ##  Sets current stock data
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="stockData"> (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) </param>
    def SetCurrentStockData(builder: EditCornerBuilder, stockData: FeatureSpreadsheetBuilder) -> None:
        """
         Sets current stock data
        """
        pass
    
    ##  Sets cutback
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    ## <param name="usCutback"> (str) </param>
    def SetCutback(builder: EditCornerBuilder, iMemberIndex: int, usCutback: str) -> None:
        """
         Sets cutback
        """
        pass
    
    ##  Set the corner type for the corner node
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iNodeIndex"> (int) </param>
    ## <param name="endCorner"> (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) </param>
    def SetEndCorner(builder: EditCornerBuilder, iNodeIndex: int, endCorner: MemberBuilder.EndCornerTypes) -> None:
        """
         Set the corner type for the corner node
        """
        pass
    
    ##  Sets the flag to indicate the cope stock data is initial values
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="bInitial"> (bool) </param>
    def SetInitialStockData(builder: EditCornerBuilder, bInitial: bool) -> None:
        """
         Sets the flag to indicate the cope stock data is initial values
        """
        pass
    
    ##  Set the member index for the corner node
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iNodeIndex"> (int) </param>
    ## <param name="iMemberIndex"> (int) </param>
    def SetMemberIndex(builder: EditCornerBuilder, iNodeIndex: int, iMemberIndex: int) -> None:
        """
         Set the member index for the corner node
        """
        pass
    
    ##  Sets member end parameters changed
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="bChanged"> (bool) </param>
    def SetParamtersChanged(builder: EditCornerBuilder, bChanged: bool) -> None:
        """
         Sets member end parameters changed
        """
        pass
    
    ##  Update all the cope stock data of the conner
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def UpdateAllCopeStockData(builder: EditCornerBuilder) -> None:
        """
         Update all the cope stock data of the conner
        """
        pass
    
    ##  Update the stock data for memeber 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="iMemberIndex"> (int) </param>
    ## <param name="bOnlyUpdateSize"> (bool) </param>
    def UpdateCopeMemberStockData(builder: EditCornerBuilder, iMemberIndex: int, bOnlyUpdateSize: bool) -> None:
        """
         Update the stock data for memeber 
        """
        pass
    
    ##  Update the stock data with the member
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="bOnlyUpdateSize"> (bool) </param>
    def UpdateStockData(builder: EditCornerBuilder, bOnlyUpdateSize: bool) -> None:
        """
         Update the stock data with the member
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##         Represents a @link Features::StructureDesign::EditStockBuilder Features::StructureDesign::EditStockBuilder@endlink  which is used
##         to change the stock of multiple Structure Design members at the same time.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignEditStockBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignEditStockBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EndLimit.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RotateAngle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## StartLimit.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## XOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## YOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class EditStockBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a <ja_class>Features.StructureDesign.EditStockBuilder</ja_class> which is used
        to change the stock of multiple Structure Design members at the same time.
        """


    ## Getter for property: (int) AlternateOrigin
    ##   the index number of the alternate sketch origin to use.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def AlternateOrigin(self) -> int:
        """
        Getter for property: (int) AlternateOrigin
          the index number of the alternate sketch origin to use.  
             
         
        """
        pass
    
    ## Setter for property: (int) AlternateOrigin

    ##   the index number of the alternate sketch origin to use.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AlternateOrigin.setter
    def AlternateOrigin(self, alternateOrigin: int):
        """
        Setter for property: (int) AlternateOrigin
          the index number of the alternate sketch origin to use.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EnableTransform
    ##   the flag to enable transform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def EnableTransform(self) -> bool:
        """
        Getter for property: (bool) EnableTransform
          the flag to enable transform.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EnableTransform

    ##   the flag to enable transform.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @EnableTransform.setter
    def EnableTransform(self, bEnableTransform: bool):
        """
        Setter for property: (bool) EnableTransform
          the flag to enable transform.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndLimit
    ##   the end limit.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndLimit
          the end limit.  
            
         
        """
        pass
    
    ## Getter for property: (@link InheritStockBuilder NXOpen.Features.StructureDesign.InheritStockBuilder@endlink) InheritStock
    ##   the inherit stock object for member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return InheritStockBuilder
    @property
    def InheritStock(self) -> InheritStockBuilder:
        """
        Getter for property: (@link InheritStockBuilder NXOpen.Features.StructureDesign.InheritStockBuilder@endlink) InheritStock
          the inherit stock object for member.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Member
    ##   the selection object to allow for selection of a member's body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Member(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Member
          the selection object to allow for selection of a member's body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
    ##   the rotate angle period  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
          the rotate angle period  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartLimit
    ##   the start limit.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartLimit
          the start limit.  
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
    ##   the stock data used to define the stock information of the member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
          the stock data used to define the stock information of the member.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
    ##   the x offset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
          the x offset.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
    ##   the y offset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
          the y offset.  
            
         
        """
        pass
    
    ##  Rotate the sketch 180 degrees around the X axis. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def FlipX(builder: EditStockBuilder) -> None:
        """
         Rotate the sketch 180 degrees around the X axis. 
        """
        pass
    
    ##  Rotate the sketch 180 degrees around the Y axis. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def FlipY(builder: EditStockBuilder) -> None:
        """
         Rotate the sketch 180 degrees around the Y axis. 
        """
        pass
    
    ##  Update the stock data settings using the stock of the input member body. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="member"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def UpdateStockInformation(builder: EditStockBuilder, member: NXOpen.NXObject) -> None:
        """
         Update the stock data settings using the stock of the input member body. 
        """
        pass
    
import NXOpen
## 
##         Represents a @link Features::StructureDesign::EditStructureBuilder Features::StructureDesign::EditStructureBuilder@endlink  which is used to edit structure in the Structure Design application.
##         Up direction information and catalog information are stored as user attributes on created frame part.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignEditStructureBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignEditStructureBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Description </term> <description> 
##  
## None </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class EditStructureBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>Features.StructureDesign.EditStructureBuilder</ja_class> which is used to edit structure in the Structure Design application.
        Up direction information and catalog information are stored as user attributes on created frame part.
        """


    ## Getter for property: (str) Catalog
    ##   the catalog to use for the stock definitions.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def Catalog(self) -> str:
        """
        Getter for property: (str) Catalog
          the catalog to use for the stock definitions.  
             
         
        """
        pass
    
    ## Setter for property: (str) Catalog

    ##   the catalog to use for the stock definitions.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Catalog.setter
    def Catalog(self, catalog: str):
        """
        Setter for property: (str) Catalog
          the catalog to use for the stock definitions.  
             
         
        """
        pass
    
    ## Getter for property: (str) Description
    ##   the discription that would be assigned to the structure Teamcenter item.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return str
    @property
    def Description(self) -> str:
        """
        Getter for property: (str) Description
          the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    
    ## Setter for property: (str) Description

    ##   the discription that would be assigned to the structure Teamcenter item.  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Description.setter
    def Description(self, description: str):
        """
        Setter for property: (str) Description
          the discription that would be assigned to the structure Teamcenter item.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Reference
    ##   the selected references   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Reference(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Reference
          the selected references   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation
    ##   the reference direction which used to determin structure member's orientation in the Structure Design application.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ReferenceOrientation(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation
          the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation

    ##   the reference direction which used to determin structure member's orientation in the Structure Design application.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ReferenceOrientation.setter
    def ReferenceOrientation(self, refOrientation: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ReferenceOrientation
          the reference direction which used to determin structure member's orientation in the Structure Design application.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) Structure
    ##   the selected structures   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def Structure(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) Structure
          the selected structures   
            
         
        """
        pass
    
    ##  Updates the stock data settings using the stock of the input member body. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="selStructure"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def UpdateReferenceInfomation(builder: EditStructureBuilder, selStructure: NXOpen.NXObject) -> None:
        """
         Updates the stock data settings using the stock of the input member body. 
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Represents a @link Features::StructureDesign::Endcap Features::StructureDesign::Endcap@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignEndcapBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignEndcapBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Chamfer </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ChamferLength.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Offset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OffsetRatio </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## PlacementType </term> <description> 
##  
## Inside </description> </item> 
## 
## <item><term> 
##  
## PreserveOverallLength </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## Thickness.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class EndcapBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>Features.StructureDesign.Endcap</ja_class> builder
    """


    ##  Corner Treatment Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Chamfer</term><description> 
    ## </description> </item><item><term> 
    ## Fillet</term><description> 
    ## </description> </item></list>
    class CornerTreatmentTypes(Enum):
        """
        Members Include: <NotSet> <Chamfer> <Fillet>
        """
        NotSet: int
        Chamfer: int
        Fillet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EndcapBuilder.CornerTreatmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Placement Type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inside</term><description> 
    ## </description> </item><item><term> 
    ## Outside</term><description> 
    ## </description> </item></list>
    class PlacementTypes(Enum):
        """
        Members Include: <Inside> <Outside>
        """
        Inside: int
        Outside: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> EndcapBuilder.PlacementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Chamfer
    ##   the chamfer   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def Chamfer(self) -> bool:
        """
        Getter for property: (bool) Chamfer
          the chamfer   
            
         
        """
        pass
    
    ## Setter for property: (bool) Chamfer

    ##   the chamfer   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Chamfer.setter
    def Chamfer(self, chamfer: bool):
        """
        Setter for property: (bool) Chamfer
          the chamfer   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChamferLength
    ##   the chamferLength   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ChamferLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ChamferLength
          the chamferLength   
            
         
        """
        pass
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the structure design comp   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the structure design comp   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##   the distance tolerance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
          the distance tolerance   
            
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##   the distance tolerance   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
          the distance tolerance   
            
         
        """
        pass
    
    ## Getter for property: (str) EndCapName
    ##   the end cap name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def EndCapName(self) -> str:
        """
        Getter for property: (str) EndCapName
          the end cap name   
            
         
        """
        pass
    
    ## Setter for property: (str) EndCapName

    ##   the end cap name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EndCapName.setter
    def EndCapName(self, endCapName: str):
        """
        Setter for property: (str) EndCapName
          the end cap name   
            
         
        """
        pass
    
    ## Getter for property: (@link EndcapBuilder.CornerTreatmentTypes NXOpen.Features.StructureDesign.EndcapBuilder.CornerTreatmentTypes@endlink) EnumCornerTreatmentType
    ##   the end cap corner treatment type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return EndcapBuilder.CornerTreatmentTypes
    @property
    def EnumCornerTreatmentType(self) -> EndcapBuilder.CornerTreatmentTypes:
        """
        Getter for property: (@link EndcapBuilder.CornerTreatmentTypes NXOpen.Features.StructureDesign.EndcapBuilder.CornerTreatmentTypes@endlink) EnumCornerTreatmentType
          the end cap corner treatment type   
            
         
        """
        pass
    
    ## Setter for property: (@link EndcapBuilder.CornerTreatmentTypes NXOpen.Features.StructureDesign.EndcapBuilder.CornerTreatmentTypes@endlink) EnumCornerTreatmentType

    ##   the end cap corner treatment type   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnumCornerTreatmentType.setter
    def EnumCornerTreatmentType(self, enumCornerTreatmentType: EndcapBuilder.CornerTreatmentTypes):
        """
        Setter for property: (@link EndcapBuilder.CornerTreatmentTypes NXOpen.Features.StructureDesign.EndcapBuilder.CornerTreatmentTypes@endlink) EnumCornerTreatmentType
          the end cap corner treatment type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Member
    ##   the member   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Member(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Member
          the member   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##   the offset between end cap and inside face of member  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
          the offset between end cap and inside face of member  
            
         
        """
        pass
    
    ## Getter for property: (float) OffsetRatio
    ##   the offset ratio   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def OffsetRatio(self) -> float:
        """
        Getter for property: (float) OffsetRatio
          the offset ratio   
            
         
        """
        pass
    
    ## Setter for property: (float) OffsetRatio

    ##   the offset ratio   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OffsetRatio.setter
    def OffsetRatio(self, offsetRatio: float):
        """
        Setter for property: (float) OffsetRatio
          the offset ratio   
            
         
        """
        pass
    
    ## Getter for property: (@link EndcapBuilder.PlacementTypes NXOpen.Features.StructureDesign.EndcapBuilder.PlacementTypes@endlink) PlacementType
    ##   the placement type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return EndcapBuilder.PlacementTypes
    @property
    def PlacementType(self) -> EndcapBuilder.PlacementTypes:
        """
        Getter for property: (@link EndcapBuilder.PlacementTypes NXOpen.Features.StructureDesign.EndcapBuilder.PlacementTypes@endlink) PlacementType
          the placement type   
            
         
        """
        pass
    
    ## Setter for property: (@link EndcapBuilder.PlacementTypes NXOpen.Features.StructureDesign.EndcapBuilder.PlacementTypes@endlink) PlacementType

    ##   the placement type   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PlacementType.setter
    def PlacementType(self, placementType: EndcapBuilder.PlacementTypes):
        """
        Setter for property: (@link EndcapBuilder.PlacementTypes NXOpen.Features.StructureDesign.EndcapBuilder.PlacementTypes@endlink) PlacementType
          the placement type   
            
         
        """
        pass
    
    ## Getter for property: (bool) PreserveOverallLength
    ##   the preserveOverallLength   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def PreserveOverallLength(self) -> bool:
        """
        Getter for property: (bool) PreserveOverallLength
          the preserveOverallLength   
            
         
        """
        pass
    
    ## Setter for property: (bool) PreserveOverallLength

    ##   the preserveOverallLength   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PreserveOverallLength.setter
    def PreserveOverallLength(self, preserveOverallLength: bool):
        """
        Setter for property: (bool) PreserveOverallLength
          the preserveOverallLength   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##   the thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
          the thickness   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a endcap feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::EndcapBuilder  NXOpen::Features::StructureDesign::EndcapBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Endcap(NXOpen.Features.BodyFeature): 
    """ Represents a endcap feature """
    pass


import NXOpen
## 
##           This is to create a @link NXOpen::Features::StructureDesign::ExportDSTVBuilder NXOpen::Features::StructureDesign::ExportDSTVBuilder@endlink  which is used to export DSTV
##           <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignExportDstvBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignExportDstvBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ExportDSTVBuilder(NXOpen.Builder): 
    """
          This is to create a <ja_class>NXOpen.Features.StructureDesign.ExportDSTVBuilder</ja_class> which is used to export DSTV
         """


    ##  Settings to indicate how to save DSTV file 
    ##  Creating dataset action type. 
    class ActionTypes(Enum):
        """
        Members Include: <CreateNew> <OverwriteExisting> <ExportToFolder>
        """
        CreateNew: int
        OverwriteExisting: int
        ExportToFolder: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ExportDSTVBuilder.ActionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ExportDSTVBuilder.ActionTypes NXOpen.Features.StructureDesign.ExportDSTVBuilder.ActionTypes@endlink) ActionType
    ##   the option to indicate how to save DSTV file.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ExportDSTVBuilder.ActionTypes
    @property
    def ActionType(self) -> ExportDSTVBuilder.ActionTypes:
        """
        Getter for property: (@link ExportDSTVBuilder.ActionTypes NXOpen.Features.StructureDesign.ExportDSTVBuilder.ActionTypes@endlink) ActionType
          the option to indicate how to save DSTV file.  
             
         
        """
        pass
    
    ## Setter for property: (@link ExportDSTVBuilder.ActionTypes NXOpen.Features.StructureDesign.ExportDSTVBuilder.ActionTypes@endlink) ActionType

    ##   the option to indicate how to save DSTV file.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ActionType.setter
    def ActionType(self, actionTypeOption: ExportDSTVBuilder.ActionTypes):
        """
        Setter for property: (@link ExportDSTVBuilder.ActionTypes NXOpen.Features.StructureDesign.ExportDSTVBuilder.ActionTypes@endlink) ActionType
          the option to indicate how to save DSTV file.  
             
         
        """
        pass
    
    ## Getter for property: (str) ExportFileFolder
    ##   the DSTV file folder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ExportFileFolder(self) -> str:
        """
        Getter for property: (str) ExportFileFolder
          the DSTV file folder.  
             
         
        """
        pass
    
    ## Setter for property: (str) ExportFileFolder

    ##   the DSTV file folder.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ExportFileFolder.setter
    def ExportFileFolder(self, fileFolder: str):
        """
        Setter for property: (str) ExportFileFolder
          the DSTV file folder.  
             
         
        """
        pass
    
    ## Getter for property: (str) ExportFileName
    ##   the DSTV file name prefix.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ExportFileName(self) -> str:
        """
        Getter for property: (str) ExportFileName
          the DSTV file name prefix.  
             
         
        """
        pass
    
    ## Setter for property: (str) ExportFileName

    ##   the DSTV file name prefix.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ExportFileName.setter
    def ExportFileName(self, filenName: str):
        """
        Setter for property: (str) ExportFileName
          the DSTV file name prefix.  
             
         
        """
        pass
    
    ## Getter for property: (str) ProjectName
    ##   the project name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def ProjectName(self) -> str:
        """
        Getter for property: (str) ProjectName
          the project name.  
             
         
        """
        pass
    
    ## Setter for property: (str) ProjectName

    ##   the project name.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ProjectName.setter
    def ProjectName(self, projectName: str):
        """
        Setter for property: (str) ProjectName
          the project name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectStructureParts
    ##   the selected structures or members to export   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def SelectStructureParts(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) SelectStructureParts
          the selected structures or members to export   
            
         
        """
        pass
    
import NXOpen.Features
## 
##     This class is used to create or edit the information shared among all Structure Design features.
##      <br> Cannot create directly.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class FeatureParmsBuilder(NXOpen.Features.FeatureBuilder): 
    """
    This class is used to create or edit the information shared among all Structure Design features.
    """


    ## Getter for property: (float) AngularTolerance
    ##   the tolerance, in degrees, used to determine when angles are zero.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
          the tolerance, in degrees, used to determine when angles are zero.  
             
         
        """
        pass
    
    ## Setter for property: (float) AngularTolerance

    ##   the tolerance, in degrees, used to determine when angles are zero.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: float):
        """
        Setter for property: (float) AngularTolerance
          the tolerance, in degrees, used to determine when angles are zero.  
             
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##   the tolerance used to determine when distances are considered zero.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
          the tolerance used to determine when distances are considered zero.  
             
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##   the tolerance used to determine when distances are considered zero.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
          the tolerance used to determine when distances are considered zero.  
             
         
        """
        pass
    
import NXOpen.Features.ShipDesign
## 
##         Represents a @link NXOpen::Features::StructureDesign::FeatureSpreadsheetBuilder NXOpen::Features::StructureDesign::FeatureSpreadsheetBuilder@endlink  builder. 
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class FeatureSpreadsheetBuilder(NXOpen.Features.ShipDesign.SteelFeatureSpreadsheetBuilder): 
    """
        Represents a <ja_class>NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder</ja_class> builder. 
        """
    pass


import NXOpen
import NXOpen.Features
##  Represents a @link Features::StructureDesign::GrabTab Features::StructureDesign::GrabTab@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignGrabTabBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignGrabTabBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class GrabTabBuilder(NXOpen.Features.FeatureBuilder): 
    """ Represents a <ja_class>Features.StructureDesign.GrabTab</ja_class> builder """


    ##  Anchor Point 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Center</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item></list>
    class AnchorPoints(Enum):
        """
        Members Include: <Left> <Center> <Right>
        """
        Left: int
        Center: int
        Right: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GrabTabBuilder.AnchorPoints:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Place Direction 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Horizontal</term><description> 
    ## </description> </item><item><term> 
    ## Vertical</term><description> 
    ## </description> </item></list>
    class PlaceDirections(Enum):
        """
        Members Include: <Horizontal> <Vertical>
        """
        Horizontal: int
        Vertical: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GrabTabBuilder.PlaceDirections:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link GrabTabBuilder.AnchorPoints NXOpen.Features.StructureDesign.GrabTabBuilder.AnchorPoints@endlink) AnchorPoint
    ##   the anchor point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return GrabTabBuilder.AnchorPoints
    @property
    def AnchorPoint(self) -> GrabTabBuilder.AnchorPoints:
        """
        Getter for property: (@link GrabTabBuilder.AnchorPoints NXOpen.Features.StructureDesign.GrabTabBuilder.AnchorPoints@endlink) AnchorPoint
          the anchor point   
            
         
        """
        pass
    
    ## Setter for property: (@link GrabTabBuilder.AnchorPoints NXOpen.Features.StructureDesign.GrabTabBuilder.AnchorPoints@endlink) AnchorPoint

    ##   the anchor point   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: GrabTabBuilder.AnchorPoints):
        """
        Setter for property: (@link GrabTabBuilder.AnchorPoints NXOpen.Features.StructureDesign.GrabTabBuilder.AnchorPoints@endlink) AnchorPoint
          the anchor point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Attachment
    ##   the placement face  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Attachment(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Attachment
          the placement face  
            
         
        """
        pass
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the structure design comp   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the structure design comp   
            
         
        """
        pass
    
    ## Getter for property: (str) GrabTabName
    ##   the grab tab name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def GrabTabName(self) -> str:
        """
        Getter for property: (str) GrabTabName
          the grab tab name   
            
         
        """
        pass
    
    ## Setter for property: (str) GrabTabName

    ##   the grab tab name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @GrabTabName.setter
    def GrabTabName(self, grabTabName: str):
        """
        Setter for property: (str) GrabTabName
          the grab tab name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
    ##   the orientation vector.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def OrientVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
          the orientation vector.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector

    ##   the orientation vector.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @OrientVector.setter
    def OrientVector(self, orientVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
          the orientation vector.  
             
         
        """
        pass
    
    ## Getter for property: (@link GrabTabBuilder.PlaceDirections NXOpen.Features.StructureDesign.GrabTabBuilder.PlaceDirections@endlink) PlaceDirection
    ##   the placement direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return GrabTabBuilder.PlaceDirections
    @property
    def PlaceDirection(self) -> GrabTabBuilder.PlaceDirections:
        """
        Getter for property: (@link GrabTabBuilder.PlaceDirections NXOpen.Features.StructureDesign.GrabTabBuilder.PlaceDirections@endlink) PlaceDirection
          the placement direction   
            
         
        """
        pass
    
    ## Setter for property: (@link GrabTabBuilder.PlaceDirections NXOpen.Features.StructureDesign.GrabTabBuilder.PlaceDirections@endlink) PlaceDirection

    ##   the placement direction   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PlaceDirection.setter
    def PlaceDirection(self, placementDirection: GrabTabBuilder.PlaceDirections):
        """
        Setter for property: (@link GrabTabBuilder.PlaceDirections NXOpen.Features.StructureDesign.GrabTabBuilder.PlaceDirections@endlink) PlaceDirection
          the placement direction   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Reference1
    ##   the select reference 1   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def Reference1(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Reference1
          the select reference 1   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Reference1Offset
    ##   the x offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Reference1Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Reference1Offset
          the x offset.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Reference1ReverseFlange
    ##   the flag to specify whether the x offset direction is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Reference1ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) Reference1ReverseFlange
          the flag to specify whether the x offset direction is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Reference1ReverseFlange

    ##   the flag to specify whether the x offset direction is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Reference1ReverseFlange.setter
    def Reference1ReverseFlange(self, reference1ReverseFlange: bool):
        """
        Setter for property: (bool) Reference1ReverseFlange
          the flag to specify whether the x offset direction is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Reference2
    ##   the select reference 2   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def Reference2(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Reference2
          the select reference 2   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Reference2Offset
    ##   the y offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Reference2Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Reference2Offset
          the y offset.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Reference2ReverseFlange
    ##   the flag to specify whether the y offset direction is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def Reference2ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) Reference2ReverseFlange
          the flag to specify whether the y offset direction is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Reference2ReverseFlange

    ##   the flag to specify whether the y offset direction is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Reference2ReverseFlange.setter
    def Reference2ReverseFlange(self, reference2ReverseFlange: bool):
        """
        Setter for property: (bool) Reference2ReverseFlange
          the flag to specify whether the y offset direction is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
    ##   the rotate angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
          the rotate angle   
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
    ##   the stock data used to define the stock information of the member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
          the stock data used to define the stock information of the member.  
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a grab tab feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::GrabTabBuilder  NXOpen::Features::StructureDesign::GrabTabBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class GrabTab(NXOpen.Features.BodyFeature): 
    """ Represents a grab tab feature """
    pass


import NXOpen
import NXOpen.Features
## 
##         Represents a builder which is used to create or edit a Structure Design Gusset feature.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignGussetBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignGussetBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## AddAlignment </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ThicknessType </term> <description> 
##  
## BothSides </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class GussetBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design Gusset feature.
        """


    ## 
    ##             the alignment type 
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## GussetPlate</term><description> 
    ## </description> </item><item><term> 
    ## LappedPlate</term><description> 
    ## </description> </item></list>
    class AlignmentTypes(Enum):
        """
        Members Include: <GussetPlate> <LappedPlate>
        """
        GussetPlate: int
        LappedPlate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.AlignmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##             the position type 
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Offset</term><description> 
    ## </description> </item><item><term> 
    ## Center</term><description> 
    ## </description> </item><item><term> 
    ## AlignToEdge</term><description> 
    ## </description> </item></list>
    class PositionTypes(Enum):
        """
        Members Include: <Offset> <Center> <AlignToEdge>
        """
        Offset: int
        Center: int
        AlignToEdge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.PositionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##             the thickness type 
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BothSides</term><description> 
    ## </description> </item><item><term> 
    ## InnerSide</term><description> 
    ## </description> </item><item><term> 
    ## OuterSide</term><description> 
    ## </description> </item></list>
    class ThicknessTypes(Enum):
        """
        Members Include: <BothSides> <InnerSide> <OuterSide>
        """
        BothSides: int
        InnerSide: int
        OuterSide: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GussetBuilder.ThicknessTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AddAlignment
    ##   the flag to indicate whether to use alignment object to position the gussets or not.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def AddAlignment(self) -> bool:
        """
        Getter for property: (bool) AddAlignment
          the flag to indicate whether to use alignment object to position the gussets or not.  
            
         
        """
        pass
    
    ## Setter for property: (bool) AddAlignment

    ##   the flag to indicate whether to use alignment object to position the gussets or not.  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @AddAlignment.setter
    def AddAlignment(self, addAlignment: bool):
        """
        Setter for property: (bool) AddAlignment
          the flag to indicate whether to use alignment object to position the gussets or not.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Alignment
    ##   the alignment object used for positioning multiple gussets.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def Alignment(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) Alignment
          the alignment object used for positioning multiple gussets.  
             
         
        """
        pass
    
    ## Getter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType
    ##   the alignment type to be used to locate gusset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return GussetBuilder.AlignmentTypes
    @property
    def AlignmentType(self) -> GussetBuilder.AlignmentTypes:
        """
        Getter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType
          the alignment type to be used to locate gusset   
            
         
        """
        pass
    
    ## Setter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType

    ##   the alignment type to be used to locate gusset   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @AlignmentType.setter
    def AlignmentType(self, alignmentType: GussetBuilder.AlignmentTypes):
        """
        Setter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType
          the alignment type to be used to locate gusset   
            
         
        """
        pass
    
    ## Getter for property: (float) AngularTolerance
    ##    @brief  the angular tolerance (degrees)  
    ##   
    ##   
    ##  
    ##             
    ##                 The angular tolerance is used for:
    ##                 <ul>
    ##                     <li>gusset placement orign and orientation evaluation</li>
    ##                     <li>gusset geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
           @brief  the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        <ul>
                            <li>gusset placement orign and orientation evaluation</li>
                            <li>gusset geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Setter for property: (float) AngularTolerance

    ##    @brief  the angular tolerance (degrees)  
    ##   
    ##   
    ##  
    ##             
    ##                 The angular tolerance is used for:
    ##                 <ul>
    ##                     <li>gusset placement orign and orientation evaluation</li>
    ##                     <li>gusset geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: float):
        """
        Setter for property: (float) AngularTolerance
           @brief  the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        <ul>
                            <li>gusset placement orign and orientation evaluation</li>
                            <li>gusset geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AttachmentOffset
    ##    the lapped offset distance in the attachment face.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AttachmentOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AttachmentOffset
           the lapped offset distance in the attachment face.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal
    ##   the pick point normal on attachment face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def AttachmentPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal
          the pick point normal on attachment face.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal

    ##   the pick point normal on attachment face.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AttachmentPointNormal.setter
    def AttachmentPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal
          the pick point normal on attachment face.  
             
         
        """
        pass
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the structure design comp   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the structure design comp   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Counts
    ##   the number of gussets created   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Counts(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Counts
          the number of gussets created   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##    @brief  the distance tolerance (part units)  
    ##   
    ##   
    ##  
    ##             
    ##                 The distance tolerance is used for:
    ##                 <ul>
    ##                     <li>gusset placement orign and orientation evaluation</li>
    ##                     <li>gusset geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
           @brief  the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        <ul>
                            <li>gusset placement orign and orientation evaluation</li>
                            <li>gusset geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##    @brief  the distance tolerance (part units)  
    ##   
    ##   
    ##  
    ##             
    ##                 The distance tolerance is used for:
    ##                 <ul>
    ##                     <li>gusset placement orign and orientation evaluation</li>
    ##                     <li>gusset geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
           @brief  the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        <ul>
                            <li>gusset placement orign and orientation evaluation</li>
                            <li>gusset geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FirstFaceSelect
    ##   the firstface to be used at locate gusset  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def FirstFaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) FirstFaceSelect
          the firstface to be used at locate gusset  
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) FlangeData
    ##   the stock data used to define the stock information of the gusset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def FlangeData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) FlangeData
          the stock data used to define the stock information of the gusset.  
            
         
        """
        pass
    
    ## Getter for property: (str) GussetName
    ##   the gusset name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def GussetName(self) -> str:
        """
        Getter for property: (str) GussetName
          the gusset name   
            
         
        """
        pass
    
    ## Setter for property: (str) GussetName

    ##   the gusset name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @GussetName.setter
    def GussetName(self, gussetName: str):
        """
        Setter for property: (str) GussetName
          the gusset name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##    the offset to the alignment plane in gusset plate type.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
           the offset to the alignment plane in gusset plate type.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
    ##   the specify line to help locate gusset when one face is curved surface and the other is plane.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def OrientVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
          the specify line to help locate gusset when one face is curved surface and the other is plane.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector

    ##   the specify line to help locate gusset when one face is curved surface and the other is plane.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @OrientVector.setter
    def OrientVector(self, orientVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
          the specify line to help locate gusset when one face is curved surface and the other is plane.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment
    ##    @brief  the pick point on attachment face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the attachment face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The position which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##              <br> 
    ##             It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
    ##             is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PickPointOnAttachment(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment
           @brief  the pick point on attachment face.  
            
        
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                     <br> 
                    It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
                    is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment

    ##    @brief  the pick point on attachment face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the attachment face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The position which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##              <br> 
    ##             It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
    ##             is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
    ##            
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PickPointOnAttachment.setter
    def PickPointOnAttachment(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment
           @brief  the pick point on attachment face.  
            
        
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                     <br> 
                    It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
                    is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement
    ##    @brief  the pick point on reinforcement face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the reinforcement face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The location which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PickPointOnReinforcement(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement
           @brief  the pick point on reinforcement face.  
            
        
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement

    ##    @brief  the pick point on reinforcement face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the reinforcement face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The location which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##            
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PickPointOnReinforcement.setter
    def PickPointOnReinforcement(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement
           @brief  the pick point on reinforcement face.  
            
        
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PitchAngle
    ##   the angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PitchAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PitchAngle
          the angle   
            
         
        """
        pass
    
    ## Getter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType
    ##   the position to be used to locate origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return GussetBuilder.PositionTypes
    @property
    def PositionType(self) -> GussetBuilder.PositionTypes:
        """
        Getter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType
          the position to be used to locate origin   
            
         
        """
        pass
    
    ## Setter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType

    ##   the position to be used to locate origin   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @PositionType.setter
    def PositionType(self, positionType: GussetBuilder.PositionTypes):
        """
        Setter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType
          the position to be used to locate origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ReinforcementOffset
    ##    the lapped offset distance in the reinforcement face.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ReinforcementOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ReinforcementOffset
           the lapped offset distance in the reinforcement face.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal
    ##   the pick point normal on reinforcement face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def ReinforcementPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal
          the pick point normal on reinforcement face.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal

    ##   the pick point normal on reinforcement face.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ReinforcementPointNormal.setter
    def ReinforcementPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal
          the pick point normal on reinforcement face.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseAlignEdge
    ##   the flag to specify whether the gusset align edge direction is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ReverseAlignEdge(self) -> bool:
        """
        Getter for property: (bool) ReverseAlignEdge
          the flag to specify whether the gusset align edge direction is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseAlignEdge

    ##   the flag to specify whether the gusset align edge direction is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ReverseAlignEdge.setter
    def ReverseAlignEdge(self, reverseAlignEdge: bool):
        """
        Setter for property: (bool) ReverseAlignEdge
          the flag to specify whether the gusset align edge direction is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseAttachmentOffsetFlange
    ##   the flag to indicate whether the lapped offset direction in attachment face is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ReverseAttachmentOffsetFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseAttachmentOffsetFlange
          the flag to indicate whether the lapped offset direction in attachment face is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseAttachmentOffsetFlange

    ##   the flag to indicate whether the lapped offset direction in attachment face is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ReverseAttachmentOffsetFlange.setter
    def ReverseAttachmentOffsetFlange(self, reverseAttachmentOffsetFlange: bool):
        """
        Setter for property: (bool) ReverseAttachmentOffsetFlange
          the flag to indicate whether the lapped offset direction in attachment face is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseFirstFace
    ##   the flag to specify whether the gusset first face is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ReverseFirstFace(self) -> bool:
        """
        Getter for property: (bool) ReverseFirstFace
          the flag to specify whether the gusset first face is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseFirstFace

    ##   the flag to specify whether the gusset first face is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ReverseFirstFace.setter
    def ReverseFirstFace(self, reverseFirstFace: bool):
        """
        Setter for property: (bool) ReverseFirstFace
          the flag to specify whether the gusset first face is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseFlange
    ##   the flag to specify whether the gusset offset distance direction is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseFlange
          the flag to specify whether the gusset offset distance direction is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseFlange

    ##   the flag to specify whether the gusset offset distance direction is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ReverseFlange.setter
    def ReverseFlange(self, reverseFlange: bool):
        """
        Setter for property: (bool) ReverseFlange
          the flag to specify whether the gusset offset distance direction is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseReinforcementOffsetFlange
    ##   the flag to indicate whether the lapped offset direction in reinforcement face is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def ReverseReinforcementOffsetFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseReinforcementOffsetFlange
          the flag to indicate whether the lapped offset direction in reinforcement face is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseReinforcementOffsetFlange

    ##   the flag to indicate whether the lapped offset direction in reinforcement face is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ReverseReinforcementOffsetFlange.setter
    def ReverseReinforcementOffsetFlange(self, reverseReinforcementOffsetFlange: bool):
        """
        Setter for property: (bool) ReverseReinforcementOffsetFlange
          the flag to indicate whether the lapped offset direction in reinforcement face is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseSecondFace
    ##   the flag to specify whether the gusset second face is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ReverseSecondFace(self) -> bool:
        """
        Getter for property: (bool) ReverseSecondFace
          the flag to specify whether the gusset second face is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseSecondFace

    ##   the flag to specify whether the gusset second face is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ReverseSecondFace.setter
    def ReverseSecondFace(self, reverseSecondFace: bool):
        """
        Setter for property: (bool) ReverseSecondFace
          the flag to specify whether the gusset second face is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SecondFaceSelect
    ##    the second face to be used at locate gusset  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SecondFaceSelect(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SecondFaceSelect
           the second face to be used at locate gusset  
            
         
        """
        pass
    
    ## Getter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType
    ##   the direction to be used at thicken sketch   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return GussetBuilder.ThicknessTypes
    @property
    def ThicknessType(self) -> GussetBuilder.ThicknessTypes:
        """
        Getter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType
          the direction to be used at thicken sketch   
            
         
        """
        pass
    
    ## Setter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType

    ##   the direction to be used at thicken sketch   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ThicknessType.setter
    def ThicknessType(self, thicknessType: GussetBuilder.ThicknessTypes):
        """
        Setter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType
          the direction to be used at thicken sketch   
            
         
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##         Represents a Structure Design Gusset Connection builder.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignGussetConnectionBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignGussetConnectionBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## PreviewGenerator.AddFasteners </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## PreviewGenerator.RotateAngle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## PreviewGenerator.XOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PreviewGenerator.YOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2206.0.0  <br> 

class GussetConnectionBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a Structure Design Gusset Connection builder.
        """


    ##  Settings to indicate source face of clearance reference face. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AnchorFace</term><description> 
    ## </description> </item><item><term> 
    ## AttachmentFace</term><description> 
    ## </description> </item></list>
    class JaBoltedConnectionBuilderGussetconnectionreferenceface(Enum):
        """
        Members Include: <AnchorFace> <AttachmentFace>
        """
        AnchorFace: int
        AttachmentFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BraceFace
    ##   the brace member face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BraceFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BraceFace
          the brace member face   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Clearance
    ##   the clearance value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Clearance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Clearance
          the clearance value.  
            
         
        """
        pass
    
    ## Getter for property: (bool) Disabled
    ##   the flag to indicate whether current builder is disabled.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Disabled(self) -> bool:
        """
        Getter for property: (bool) Disabled
          the flag to indicate whether current builder is disabled.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Disabled

    ##   the flag to indicate whether current builder is disabled.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Disabled.setter
    def Disabled(self, disabled: bool):
        """
        Setter for property: (bool) Disabled
          the flag to indicate whether current builder is disabled.  
             
         
        """
        pass
    
    ## Getter for property: (bool) LappedPlateAttachedMember
    ##   the flag to indicate whether the current brace member is attached by a lapped plate.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def LappedPlateAttachedMember(self) -> bool:
        """
        Getter for property: (bool) LappedPlateAttachedMember
          the flag to indicate whether the current brace member is attached by a lapped plate.  
             
         
        """
        pass
    
    ## Setter for property: (bool) LappedPlateAttachedMember

    ##   the flag to indicate whether the current brace member is attached by a lapped plate.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @LappedPlateAttachedMember.setter
    def LappedPlateAttachedMember(self, lappedPlateAttachedMember: bool):
        """
        Setter for property: (bool) LappedPlateAttachedMember
          the flag to indicate whether the current brace member is attached by a lapped plate.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Modified
    ##   the flag to indicate whether current builder is modified.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def Modified(self) -> bool:
        """
        Getter for property: (bool) Modified
          the flag to indicate whether current builder is modified.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Modified

    ##   the flag to indicate whether current builder is modified.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Modified.setter
    def Modified(self, modified: bool):
        """
        Setter for property: (bool) Modified
          the flag to indicate whether current builder is modified.  
             
         
        """
        pass
    
    ## Getter for property: (@link BoltedConnectionBuilder NXOpen.Features.StructureDesign.BoltedConnectionBuilder@endlink) PreviewGenerator
    ##   the preview generator.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return BoltedConnectionBuilder
    @property
    def PreviewGenerator(self) -> BoltedConnectionBuilder:
        """
        Getter for property: (@link BoltedConnectionBuilder NXOpen.Features.StructureDesign.BoltedConnectionBuilder@endlink) PreviewGenerator
          the preview generator.  
            
         
        """
        pass
    
    ## Setter for property: (@link BoltedConnectionBuilder NXOpen.Features.StructureDesign.BoltedConnectionBuilder@endlink) PreviewGenerator

    ##   the preview generator.  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PreviewGenerator.setter
    def PreviewGenerator(self, previewGenerator: BoltedConnectionBuilder):
        """
        Setter for property: (@link BoltedConnectionBuilder NXOpen.Features.StructureDesign.BoltedConnectionBuilder@endlink) PreviewGenerator
          the preview generator.  
            
         
        """
        pass
    
    ## Getter for property: (@link GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features.StructureDesign.GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface@endlink) ReferenceFace
    ##   the clearance face.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface
    @property
    def ReferenceFace(self) -> GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface:
        """
        Getter for property: (@link GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features.StructureDesign.GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface@endlink) ReferenceFace
          the clearance face.  
            
         
        """
        pass
    
    ## Setter for property: (@link GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features.StructureDesign.GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface@endlink) ReferenceFace

    ##   the clearance face.  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReferenceFace.setter
    def ReferenceFace(self, referenceFace: GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface):
        """
        Setter for property: (@link GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features.StructureDesign.GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface@endlink) ReferenceFace
          the clearance face.  
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
    ##   the stock data.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
          the stock data.  
            
         
        """
        pass
    
    ##  Clones current builder data to the selected gusset connection builders. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="selectedBuilders"> (@link GussetConnectionBuilder List[NXOpen.Features.StructureDesign.GussetConnectionBuilder]@endlink) </param>
    def CloneDataToSelectedBuilders(builder: GussetConnectionBuilder, selectedBuilders: List[GussetConnectionBuilder]) -> None:
        """
         Clones current builder data to the selected gusset connection builders. 
        """
        pass
    
    ##  Reset builder data from parms. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def ResetFromParms(builder: GussetConnectionBuilder) -> None:
        """
         Reset builder data from parms. 
        """
        pass
    
    ##  Update stock section types by user input. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="sectionModified"> (bool) </param>
    def UpdateStockSectionTypes(builder: GussetConnectionBuilder, sectionModified: bool) -> None:
        """
         Update stock section types by user input. 
        """
        pass
    
import NXOpen.Features
##  Represents a gusset feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::GussetBuilder  NXOpen::Features::StructureDesign::GussetBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Gusset(NXOpen.Features.BodyFeature): 
    """ Represents a gusset feature """
    pass


import NXOpen
import NXOpen.Features
## 
##         Represents a builder which is used to create or edit a Structure Design Haunch feature.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignHaunchBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignHaunchBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class HaunchBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a builder which is used to create or edit a Structure Design Haunch feature.
        """


    ## 
    ##             the stiffening plate placement method type 
    ##             
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OnEdge</term><description> 
    ## </description> </item><item><term> 
    ## OnFace</term><description> 
    ## </description> </item></list>
    class PlacementMethods(Enum):
        """
        Members Include: <OnEdge> <OnFace>
        """
        OnEdge: int
        OnFace: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> HaunchBuilder.PlacementMethods:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType
    ##   the alignment type to be used to locate haunch   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return GussetBuilder.AlignmentTypes
    @property
    def AlignmentType(self) -> GussetBuilder.AlignmentTypes:
        """
        Getter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType
          the alignment type to be used to locate haunch   
            
         
        """
        pass
    
    ## Setter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType

    ##   the alignment type to be used to locate haunch   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AlignmentType.setter
    def AlignmentType(self, alignmentType: GussetBuilder.AlignmentTypes):
        """
        Setter for property: (@link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink) AlignmentType
          the alignment type to be used to locate haunch   
            
         
        """
        pass
    
    ## Getter for property: (float) AngularTolerance
    ##    @brief  the angular tolerance (degrees)  
    ##   
    ##   
    ##  
    ##             
    ##                 The angular tolerance is used for:
    ##                 <ul>
    ##                     <li>haunch placement orign and orientation evaluation</li>
    ##                     <li>haunch geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def AngularTolerance(self) -> float:
        """
        Getter for property: (float) AngularTolerance
           @brief  the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        <ul>
                            <li>haunch placement orign and orientation evaluation</li>
                            <li>haunch geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Setter for property: (float) AngularTolerance

    ##    @brief  the angular tolerance (degrees)  
    ##   
    ##   
    ##  
    ##             
    ##                 The angular tolerance is used for:
    ##                 <ul>
    ##                     <li>haunch placement orign and orientation evaluation</li>
    ##                     <li>haunch geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AngularTolerance.setter
    def AngularTolerance(self, angularTolerance: float):
        """
        Setter for property: (float) AngularTolerance
           @brief  the angular tolerance (degrees)  
          
          
         
                    
                        The angular tolerance is used for:
                        <ul>
                            <li>haunch placement orign and orientation evaluation</li>
                            <li>haunch geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) AttachmentFace
    ##    the attachment face to be used at locate haunch  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def AttachmentFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) AttachmentFace
           the attachment face to be used at locate haunch  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal
    ##   the pick point normal on attachment face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def AttachmentPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal
          the pick point normal on attachment face.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal

    ##   the pick point normal on attachment face.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AttachmentPointNormal.setter
    def AttachmentPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) AttachmentPointNormal
          the pick point normal on attachment face.  
             
         
        """
        pass
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the context attribute builder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the context attribute builder   
            
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##    @brief  the distance tolerance (part units)  
    ##   
    ##   
    ##  
    ##             
    ##                 The distance tolerance is used for:
    ##                 <ul>
    ##                     <li>haunch placement orign and orientation evaluation</li>
    ##                     <li>haunch geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
           @brief  the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        <ul>
                            <li>haunch placement orign and orientation evaluation</li>
                            <li>haunch geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##    @brief  the distance tolerance (part units)  
    ##   
    ##   
    ##  
    ##             
    ##                 The distance tolerance is used for:
    ##                 <ul>
    ##                     <li>haunch placement orign and orientation evaluation</li>
    ##                     <li>haunch geometry construction</li>
    ##                 </ul>
    ##             
    ##               
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
           @brief  the distance tolerance (part units)  
          
          
         
                    
                        The distance tolerance is used for:
                        <ul>
                            <li>haunch placement orign and orientation evaluation</li>
                            <li>haunch geometry construction</li>
                        </ul>
                    
                      
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FaceOffset
    ##   the stiffening plate offset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FaceOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FaceOffset
          the stiffening plate offset.  
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) GussetData
    ##   the stock data used to define the stock information of the haunch.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def GussetData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) GussetData
          the stock data used to define the stock information of the haunch.  
            
         
        """
        pass
    
    ## Getter for property: (str) HaunchName
    ##   the haunch name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def HaunchName(self) -> str:
        """
        Getter for property: (str) HaunchName
          the haunch name   
            
         
        """
        pass
    
    ## Setter for property: (str) HaunchName

    ##   the haunch name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @HaunchName.setter
    def HaunchName(self, haunchName: str):
        """
        Setter for property: (str) HaunchName
          the haunch name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##    the offset to the alignment plane in haunch plate type.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
           the offset to the alignment plane in haunch plate type.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
    ##   the orientation vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def OrientVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
          the orientation vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector

    ##   the orientation vector   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @OrientVector.setter
    def OrientVector(self, orientVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientVector
          the orientation vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment
    ##    @brief  the pick point on attachment face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the attachment face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The position which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##              <br> 
    ##             It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
    ##             is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PickPointOnAttachment(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment
           @brief  the pick point on attachment face.  
            
        
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                     <br> 
                    It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
                    is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment

    ##    @brief  the pick point on attachment face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the attachment face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The position which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##              <br> 
    ##             It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
    ##             is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
    ##            
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PickPointOnAttachment.setter
    def PickPointOnAttachment(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnAttachment
           @brief  the pick point on attachment face.  
            
        
         
                
                    When the attachment face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The position which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                     <br> 
                    It is only used when @link NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType NXOpen::Features::ShipDesign::BracketBuilder::SetAlignmentType@endlink 
                    is set to @link Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment Features::ShipDesign::BracketBuilder::AlignmentTypesDatumPlaneAlignment@endlink .  <br> 
                   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement
    ##    @brief  the pick point on reinforcement face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the reinforcement face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The location which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def PickPointOnReinforcement(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement
           @brief  the pick point on reinforcement face.  
            
        
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement

    ##    @brief  the pick point on reinforcement face.  
    ##     
    ## 
    ##  
    ##         
    ##             When the reinforcement face is curved (such as a cylindrical face), the bracket can
    ##             be placed at multiple locations, then the pick point is used.
    ##             The location which is closest to the pick point is used.
    ##              <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
    ##            
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PickPointOnReinforcement.setter
    def PickPointOnReinforcement(self, pickPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) PickPointOnReinforcement
           @brief  the pick point on reinforcement face.  
            
        
         
                
                    When the reinforcement face is curved (such as a cylindrical face), the bracket can
                    be placed at multiple locations, then the pick point is used.
                    The location which is closest to the pick point is used.
                     <br>  It is optional. If there are multiple candidate locations and this is not set, a random location is chosen. <br> 
                   
         
        """
        pass
    
    ## Getter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType
    ##   the position to be used to locate origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return GussetBuilder.PositionTypes
    @property
    def PositionType(self) -> GussetBuilder.PositionTypes:
        """
        Getter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType
          the position to be used to locate origin   
            
         
        """
        pass
    
    ## Setter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType

    ##   the position to be used to locate origin   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PositionType.setter
    def PositionType(self, positionType: GussetBuilder.PositionTypes):
        """
        Setter for property: (@link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink) PositionType
          the position to be used to locate origin   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ReinforcementFace
    ##   the reinforcement face to be used at locate haunch  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def ReinforcementFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) ReinforcementFace
          the reinforcement face to be used at locate haunch  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal
    ##   the pick point normal on reinforcement face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Vector3d
    @property
    def ReinforcementPointNormal(self) -> NXOpen.Vector3d:
        """
        Getter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal
          the pick point normal on reinforcement face.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal

    ##   the pick point normal on reinforcement face.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReinforcementPointNormal.setter
    def ReinforcementPointNormal(self, pickPoint: NXOpen.Vector3d):
        """
        Setter for property: (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) ReinforcementPointNormal
          the pick point normal on reinforcement face.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseAlignEdge
    ##   the flag to specify whether the haunch align edge direction is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ReverseAlignEdge(self) -> bool:
        """
        Getter for property: (bool) ReverseAlignEdge
          the flag to specify whether the haunch align edge direction is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseAlignEdge

    ##   the flag to specify whether the haunch align edge direction is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReverseAlignEdge.setter
    def ReverseAlignEdge(self, reverseAlignEdge: bool):
        """
        Setter for property: (bool) ReverseAlignEdge
          the flag to specify whether the haunch align edge direction is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseFlange
    ##   the flag to specify whether the haunch offset distance direction is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ReverseFlange(self) -> bool:
        """
        Getter for property: (bool) ReverseFlange
          the flag to specify whether the haunch offset distance direction is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseFlange

    ##   the flag to specify whether the haunch offset distance direction is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReverseFlange.setter
    def ReverseFlange(self, reverseFlange: bool):
        """
        Setter for property: (bool) ReverseFlange
          the flag to specify whether the haunch offset distance direction is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseStiffeningOnFace
    ##   the flag to specify whether the haunch stiffening face is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def ReverseStiffeningOnFace(self) -> bool:
        """
        Getter for property: (bool) ReverseStiffeningOnFace
          the flag to specify whether the haunch stiffening face is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseStiffeningOnFace

    ##   the flag to specify whether the haunch stiffening face is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ReverseStiffeningOnFace.setter
    def ReverseStiffeningOnFace(self, reverse: bool):
        """
        Setter for property: (bool) ReverseStiffeningOnFace
          the flag to specify whether the haunch stiffening face is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StiffeningPlateData
    ##   the stock data used to define the stock information of the stiffening plate.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StiffeningPlateData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StiffeningPlateData
          the stock data used to define the stock information of the stiffening plate.  
            
         
        """
        pass
    
    ## Getter for property: (@link HaunchBuilder.PlacementMethods NXOpen.Features.StructureDesign.HaunchBuilder.PlacementMethods@endlink) StiffeningPlatePlacementMethod
    ##   the stiffening plate placement method type    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return HaunchBuilder.PlacementMethods
    @property
    def StiffeningPlatePlacementMethod(self) -> HaunchBuilder.PlacementMethods:
        """
        Getter for property: (@link HaunchBuilder.PlacementMethods NXOpen.Features.StructureDesign.HaunchBuilder.PlacementMethods@endlink) StiffeningPlatePlacementMethod
          the stiffening plate placement method type    
            
         
        """
        pass
    
    ## Setter for property: (@link HaunchBuilder.PlacementMethods NXOpen.Features.StructureDesign.HaunchBuilder.PlacementMethods@endlink) StiffeningPlatePlacementMethod

    ##   the stiffening plate placement method type    
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @StiffeningPlatePlacementMethod.setter
    def StiffeningPlatePlacementMethod(self, placementMethod: HaunchBuilder.PlacementMethods):
        """
        Setter for property: (@link HaunchBuilder.PlacementMethods NXOpen.Features.StructureDesign.HaunchBuilder.PlacementMethods@endlink) StiffeningPlatePlacementMethod
          the stiffening plate placement method type    
            
         
        """
        pass
    
    ## Getter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType
    ##   the direction to be used to thicken the gusset plate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return GussetBuilder.ThicknessTypes
    @property
    def ThicknessType(self) -> GussetBuilder.ThicknessTypes:
        """
        Getter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType
          the direction to be used to thicken the gusset plate   
            
         
        """
        pass
    
    ## Setter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType

    ##   the direction to be used to thicken the gusset plate   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ThicknessType.setter
    def ThicknessType(self, thicknessType: GussetBuilder.ThicknessTypes):
        """
        Setter for property: (@link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink) ThicknessType
          the direction to be used to thicken the gusset plate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
    ##   the x offset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
          the x offset.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
    ##   the y offset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
          the y offset.  
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a haunch feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::HaunchBuilder  NXOpen::Features::StructureDesign::HaunchBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class Haunch(NXOpen.Features.BodyFeature): 
    """ Represents a haunch feature """
    pass


import NXOpen
import NXOpen.GeometricUtilities
## 
##         @link NXOpen::Features::StructureDesign::InheritStockBuilder NXOpen::Features::StructureDesign::InheritStockBuilder@endlink object.
##     
## 
##   <br>  Created in NX2306.0.0  <br> 

class InheritStockBuilder(NXOpen.TaggedObject): 
    """
        <ja_class>NXOpen.Features.StructureDesign.InheritStockBuilder</ja_class>object.
    """


    ##  The structure design feature types of the input stock object. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Member</term><description> 
    ## </description> </item><item><term> 
    ## EndCap</term><description> 
    ## </description> </item><item><term> 
    ## Gusset</term><description> 
    ## </description> </item><item><term> 
    ## GrabTab</term><description> 
    ## </description> </item><item><term> 
    ## Stiffener</term><description> 
    ## </description> </item><item><term> 
    ## BoltedConnection</term><description> 
    ## </description> </item></list>
    class StockObjectTypes(Enum):
        """
        Members Include: <Member> <EndCap> <Gusset> <GrabTab> <Stiffener> <BoltedConnection>
        """
        Member: int
        EndCap: int
        Gusset: int
        GrabTab: int
        Stiffener: int
        BoltedConnection: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InheritStockBuilder.StockObjectTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Update the stock data settings using the stock of the input stock object. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="stockObject"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="stockBuilder"> (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) </param>
    def UpdateStockInformation(builder: InheritStockBuilder, stockObject: NXOpen.NXObject, stockBuilder: FeatureSpreadsheetBuilder) -> None:
        """
         Update the stock data settings using the stock of the input stock object. 
        """
        pass
    
import NXOpen
## 
##         Represents a @link Features::StructureDesign::LibraryBuilder Features::StructureDesign::LibraryBuilder@endlink  which is used to select the library for structure designer object creation.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignLibraryBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignLibraryBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class LibraryBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>Features.StructureDesign.LibraryBuilder</ja_class> which is used to select the library for structure designer object creation.
        """


    ## Getter for property: (str) Catalog
    ##   the catalog to use for the stock definitions.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def Catalog(self) -> str:
        """
        Getter for property: (str) Catalog
          the catalog to use for the stock definitions.  
             
         
        """
        pass
    
    ## Setter for property: (str) Catalog

    ##   the catalog to use for the stock definitions.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @Catalog.setter
    def Catalog(self, catalog: str):
        """
        Setter for property: (str) Catalog
          the catalog to use for the stock definitions.  
             
         
        """
        pass
    
import NXOpen
## 
##     Represents a builder which is used to create or edit a Structure Design Member feature.
##      <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignMemberBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignMemberBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## EndLimit.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## MemberPathEnd.PathMethod </term> <description> 
##  
## Members </description> </item> 
## 
## <item><term> 
##  
## MemberPathEnd.PathOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RotateAngle.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## StartLimit.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## XOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## YOffset.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class MemberBuilder(FeatureParmsBuilder): 
    """
    Represents a builder which is used to create or edit a Structure Design Member feature.
    """


    ##  The settings to define the corner at the start and end of the member. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Miter</term><description> 
    ## </description> </item><item><term> 
    ## Butt</term><description> 
    ## </description> </item><item><term> 
    ## Cope</term><description> 
    ## </description> </item><item><term> 
    ## MatchedCope</term><description> 
    ## </description> </item><item><term> 
    ## SmartExtend</term><description> 
    ## </description> </item></list>
    class EndCornerTypes(Enum):
        """
        Members Include: <NotSet> <Miter> <Butt> <Cope> <MatchedCope> <SmartExtend>
        """
        NotSet: int
        Miter: int
        Butt: int
        Cope: int
        MatchedCope: int
        SmartExtend: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MemberBuilder.EndCornerTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (int) AlternateOrigin
    ##   the index number of the alternate sketch origin to use.  
    ##    This number is retrieved
    ##         from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def AlternateOrigin(self) -> int:
        """
        Getter for property: (int) AlternateOrigin
          the index number of the alternate sketch origin to use.  
           This number is retrieved
                from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".  
         
        """
        pass
    
    ## Setter for property: (int) AlternateOrigin

    ##   the index number of the alternate sketch origin to use.  
    ##    This number is retrieved
    ##         from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".  
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @AlternateOrigin.setter
    def AlternateOrigin(self, alternateOrigin: int):
        """
        Setter for property: (int) AlternateOrigin
          the index number of the alternate sketch origin to use.  
           This number is retrieved
                from points in the sketch that have an integer user attribute with a title of "SD_ANCHOR_POINT".  
         
        """
        pass
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the structure design comp   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the structure design comp   
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableMergeColinearPath
    ##   the flag to enable auto merge colinear path.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def EnableMergeColinearPath(self) -> bool:
        """
        Getter for property: (bool) EnableMergeColinearPath
          the flag to enable auto merge colinear path.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EnableMergeColinearPath

    ##   the flag to enable auto merge colinear path.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EnableMergeColinearPath.setter
    def EnableMergeColinearPath(self, bEnableMergeColinearPath: bool):
        """
        Setter for property: (bool) EnableMergeColinearPath
          the flag to enable auto merge colinear path.  
             
         
        """
        pass
    
    ## Getter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerEnd
    ##   the corner to be used at the end of the member.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return MemberBuilder.EndCornerTypes
    @property
    def EndCornerEnd(self) -> MemberBuilder.EndCornerTypes:
        """
        Getter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerEnd
          the corner to be used at the end of the member.  
             
         
        """
        pass
    
    ## Setter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerEnd

    ##   the corner to be used at the end of the member.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EndCornerEnd.setter
    def EndCornerEnd(self, endCornerEnd: MemberBuilder.EndCornerTypes):
        """
        Setter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerEnd
          the corner to be used at the end of the member.  
             
         
        """
        pass
    
    ## Getter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerStart
    ##   the corner to be used at the start of the member.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return MemberBuilder.EndCornerTypes
    @property
    def EndCornerStart(self) -> MemberBuilder.EndCornerTypes:
        """
        Getter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerStart
          the corner to be used at the start of the member.  
             
         
        """
        pass
    
    ## Setter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerStart

    ##   the corner to be used at the start of the member.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EndCornerStart.setter
    def EndCornerStart(self, endCornerStart: MemberBuilder.EndCornerTypes):
        """
        Setter for property: (@link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink) EndCornerStart
          the corner to be used at the start of the member.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndLimit
    ##   the end limit.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndLimit
          the end limit.  
            
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##   the name used for the created component file.  
    ##    If a duplicate name, will append a number to this name. This
    ##         property is only used during creation of the member.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the member.   
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the name used for the created component file.  
    ##    If a duplicate name, will append a number to this name. This
    ##         property is only used during creation of the member.   
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
          the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                property is only used during creation of the member.   
         
        """
        pass
    
    ## Getter for property: (@link InheritStockBuilder NXOpen.Features.StructureDesign.InheritStockBuilder@endlink) InheritStock
    ##   the inherit stock object for member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return InheritStockBuilder
    @property
    def InheritStock(self) -> InheritStockBuilder:
        """
        Getter for property: (@link InheritStockBuilder NXOpen.Features.StructureDesign.InheritStockBuilder@endlink) InheritStock
          the inherit stock object for member.  
            
         
        """
        pass
    
    ## Getter for property: (@link MemberPathBuilder NXOpen.Features.StructureDesign.MemberPathBuilder@endlink) MemberPathEnd
    ##   the path end data for member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return MemberPathBuilder
    @property
    def MemberPathEnd(self) -> MemberPathBuilder:
        """
        Getter for property: (@link MemberPathBuilder NXOpen.Features.StructureDesign.MemberPathBuilder@endlink) MemberPathEnd
          the path end data for member.  
            
         
        """
        pass
    
    ## Getter for property: (@link MemberPathBuilder NXOpen.Features.StructureDesign.MemberPathBuilder@endlink) MemberPathStart
    ##   the path start data for member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return MemberPathBuilder
    @property
    def MemberPathStart(self) -> MemberPathBuilder:
        """
        Getter for property: (@link MemberPathBuilder NXOpen.Features.StructureDesign.MemberPathBuilder@endlink) MemberPathStart
          the path start data for member.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PathGeometry
    ##   the path geometry.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def PathGeometry(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) PathGeometry
          the path geometry.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
    ##   the rotate angle.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotateAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotateAngle
          the rotate angle.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartLimit
    ##   the start limit.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartLimit
          the start limit.  
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
    ##   the stock data used to define the stock information of the member.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
          the stock data used to define the stock information of the member.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
    ##   the x offset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XOffset
          the x offset.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
    ##   the y offset.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YOffset
          the y offset.  
            
         
        """
        pass
    
    ##  Clean created bodies after the editing of preview corner 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="corner"> (@link Corner NXOpen.Features.StructureDesign.Corner@endlink) </param>
    def CleanAfterEditingCorner(builder: MemberBuilder, corner: Corner) -> None:
        """
         Clean created bodies after the editing of preview corner 
        """
        pass
    
    ##  Clears all adjusted paths.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def ClearAllAdjustedPath(builder: MemberBuilder) -> None:
        """
         Clears all adjusted paths.
        """
        pass
    
    ##  Clears all combined curve maps.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def ClearAllCombinedCurveMap(builder: MemberBuilder) -> None:
        """
         Clears all combined curve maps.
        """
        pass
    
    ##  Clear combined curve map
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ##  curve or edge
    def ClearCombinedCurveMap(builder: MemberBuilder, curves: List[NXOpen.NXObject]) -> None:
        """
         Clear combined curve map
        """
        pass
    
    ##  Create preview bodies 
    ##  @return errorCode (int): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    def CreatePreviewBodies(builder: MemberBuilder) -> int:
        """
         Create preview bodies 
         @return errorCode (int): .
        """
        pass
    
    ##  Delete preview corners
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def DeletePreviewCorners(builder: MemberBuilder) -> None:
        """
         Delete preview corners
        """
        pass
    
    ##  Destroy preview bodies
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def DestroyPreviewBodies(builder: MemberBuilder) -> None:
        """
         Destroy preview bodies
        """
        pass
    
    ##  Destroy preview body map
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def DestroyPreviewBodyMap(builder: MemberBuilder) -> None:
        """
         Destroy preview body map
        """
        pass
    
    ##  Enaluates structure curves or edges position information 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ##  curve or edge
    def EvaluateStructurePositionInformation(builder: MemberBuilder, curves: List[NXOpen.NXObject]) -> None:
        """
         Enaluates structure curves or edges position information 
        """
        pass
    
    ##  Rotate the sketch 180 degrees around the X axis. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def FlipX(builder: MemberBuilder) -> None:
        """
         Rotate the sketch 180 degrees around the X axis. 
        """
        pass
    
    ##  Rotate the sketch 180 degrees around the Y axis. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def FlipY(builder: MemberBuilder) -> None:
        """
         Rotate the sketch 180 degrees around the Y axis. 
        """
        pass
    
    ##  Gets the editing previewcorner. 
    ##  @return corner (@link Corner NXOpen.Features.StructureDesign.Corner@endlink):  The editing preview corner. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetEditingPreviewCorner(builder: MemberBuilder) -> Corner:
        """
         Gets the editing previewcorner. 
         @return corner (@link Corner NXOpen.Features.StructureDesign.Corner@endlink):  The editing preview corner. .
        """
        pass
    
    ##  Prepare for editing the preview corner 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="corner"> (@link Corner NXOpen.Features.StructureDesign.Corner@endlink) </param>
    def PrepareBeforeEditingCorner(builder: MemberBuilder, corner: Corner) -> None:
        """
         Prepare for editing the preview corner 
        """
        pass
    
    ##  Sets the editing preview corner
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="corner"> (@link Corner NXOpen.Features.StructureDesign.Corner@endlink) </param>
    def SetEditingPreviewCorner(builder: MemberBuilder, corner: Corner) -> None:
        """
         Sets the editing preview corner
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
## 
##     Represents a builder which is used to create or edit a Structure Design Member Path.
##     
## 
##   <br>  Created in NX2007.0.0  <br> 

class MemberPathBuilder(NXOpen.TaggedObject): 
    """
    Represents a builder which is used to create or edit a Structure Design Member Path.
    """


    ##  The settings to define path adjustment method of the member. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Members</term><description> 
    ## </description> </item><item><term> 
    ## Csys</term><description> 
    ## </description> </item><item><term> 
    ## Point</term><description> 
    ## </description> </item></list>
    class MemberPathMethod(Enum):
        """
        Members Include: <Members> <Csys> <Point>
        """
        Members: int
        Csys: int
        Point: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MemberPathBuilder.MemberPathMethod:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
    ##   the coord system   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def CoordSystem(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
          the coord system   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem

    ##   the coord system   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @CoordSystem.setter
    def CoordSystem(self, coordSystem: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) CoordSystem
          the coord system   
            
         
        """
        pass
    
    ## Getter for property: (@link MemberPathBuilder.MemberPathMethod NXOpen.Features.StructureDesign.MemberPathBuilder.MemberPathMethod@endlink) PathMethod
    ##   the path method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return MemberPathBuilder.MemberPathMethod
    @property
    def PathMethod(self) -> MemberPathBuilder.MemberPathMethod:
        """
        Getter for property: (@link MemberPathBuilder.MemberPathMethod NXOpen.Features.StructureDesign.MemberPathBuilder.MemberPathMethod@endlink) PathMethod
          the path method   
            
         
        """
        pass
    
    ## Setter for property: (@link MemberPathBuilder.MemberPathMethod NXOpen.Features.StructureDesign.MemberPathBuilder.MemberPathMethod@endlink) PathMethod

    ##   the path method   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @PathMethod.setter
    def PathMethod(self, pathMethod: MemberPathBuilder.MemberPathMethod):
        """
        Setter for property: (@link MemberPathBuilder.MemberPathMethod NXOpen.Features.StructureDesign.MemberPathBuilder.MemberPathMethod@endlink) PathMethod
          the path method   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PathOffset
    ##   the exp face path offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PathOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PathOffset
          the exp face path offset   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PathPoint
    ##   the path point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PathPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PathPoint
          the path point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PathPoint

    ##   the path point   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @PathPoint.setter
    def PathPoint(self, pathPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PathPoint
          the path point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectFirstMember
    ##   the select first face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def SelectFirstMember(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectFirstMember
          the select first face   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectSecondMember
    ##   the select second face   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def SelectSecondMember(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectSecondMember
          the select second face   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a structure design member feature.  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::MemberBuilder  NXOpen::Features::StructureDesign::MemberBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Member(NXOpen.Features.BodyFeature): 
    """ Represents a structure design member feature. """
    pass


import NXOpen
## 
##         Represents a builder which is used to create Structure Design Navigator Node.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignNavigatorNodeBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignNavigatorNodeBuilder @endlink  <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class NavigatorNodeBuilder(NXOpen.Builder): 
    """
        Represents a builder which is used to create Structure Design Navigator Node.
        """


    ## Getter for property: (str) ComponentName
    ##   the component name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def ComponentName(self) -> str:
        """
        Getter for property: (str) ComponentName
          the component name   
            
         
        """
        pass
    
    ## Setter for property: (str) ComponentName

    ##   the component name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ComponentName.setter
    def ComponentName(self, assemblyTemplateName: str):
        """
        Setter for property: (str) ComponentName
          the component name   
            
         
        """
        pass
    
import NXOpen
## 
##         Represents a @link Features::StructureDesign::PatternSettingsBuilder Features::StructureDesign::PatternSettingsBuilder@endlink  which is used to manager settings 
##         determining if structure designer object need to be automatically patterned at creation when dependant source has been patterned.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignPatternSettingsBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignPatternSettingsBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class PatternSettingsBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>Features.StructureDesign.PatternSettingsBuilder</ja_class> which is used to manager settings 
        determining if structure designer object need to be automatically patterned at creation when dependant source has been patterned.
        """


    ## Getter for property: (bool) AutoPatternEndCap
    ##   the flag to indicate whether to automatically pattern the end cap feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AutoPatternEndCap(self) -> bool:
        """
        Getter for property: (bool) AutoPatternEndCap
          the flag to indicate whether to automatically pattern the end cap feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutoPatternEndCap

    ##   the flag to indicate whether to automatically pattern the end cap feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AutoPatternEndCap.setter
    def AutoPatternEndCap(self, autoPatternEndCap: bool):
        """
        Setter for property: (bool) AutoPatternEndCap
          the flag to indicate whether to automatically pattern the end cap feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutoPatternGrabTab
    ##   the flag to indicate whether to automatically pattern the grab tab feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AutoPatternGrabTab(self) -> bool:
        """
        Getter for property: (bool) AutoPatternGrabTab
          the flag to indicate whether to automatically pattern the grab tab feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutoPatternGrabTab

    ##   the flag to indicate whether to automatically pattern the grab tab feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AutoPatternGrabTab.setter
    def AutoPatternGrabTab(self, autoPatternGrabTab: bool):
        """
        Setter for property: (bool) AutoPatternGrabTab
          the flag to indicate whether to automatically pattern the grab tab feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutoPatternGusset
    ##   the flag to indicate whether to automatically pattern the gusset feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AutoPatternGusset(self) -> bool:
        """
        Getter for property: (bool) AutoPatternGusset
          the flag to indicate whether to automatically pattern the gusset feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutoPatternGusset

    ##   the flag to indicate whether to automatically pattern the gusset feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AutoPatternGusset.setter
    def AutoPatternGusset(self, autoPatternGusset: bool):
        """
        Setter for property: (bool) AutoPatternGusset
          the flag to indicate whether to automatically pattern the gusset feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutoPatternHaunch
    ##   the flag to indicate whether to automatically pattern the haunch feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AutoPatternHaunch(self) -> bool:
        """
        Getter for property: (bool) AutoPatternHaunch
          the flag to indicate whether to automatically pattern the haunch feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutoPatternHaunch

    ##   the flag to indicate whether to automatically pattern the haunch feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AutoPatternHaunch.setter
    def AutoPatternHaunch(self, autoPatternHaunch: bool):
        """
        Setter for property: (bool) AutoPatternHaunch
          the flag to indicate whether to automatically pattern the haunch feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutoPatternMountingFeet
    ##   the flag to indicate whether to automatically pattern the mounting feet feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AutoPatternMountingFeet(self) -> bool:
        """
        Getter for property: (bool) AutoPatternMountingFeet
          the flag to indicate whether to automatically pattern the mounting feet feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutoPatternMountingFeet

    ##   the flag to indicate whether to automatically pattern the mounting feet feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AutoPatternMountingFeet.setter
    def AutoPatternMountingFeet(self, autoPatternMountingFeet: bool):
        """
        Setter for property: (bool) AutoPatternMountingFeet
          the flag to indicate whether to automatically pattern the mounting feet feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutoPatternPlate
    ##   the flag to indicate whether to automatically pattern the plate feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def AutoPatternPlate(self) -> bool:
        """
        Getter for property: (bool) AutoPatternPlate
          the flag to indicate whether to automatically pattern the plate feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutoPatternPlate

    ##   the flag to indicate whether to automatically pattern the plate feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AutoPatternPlate.setter
    def AutoPatternPlate(self, autoPatternPlate: bool):
        """
        Setter for property: (bool) AutoPatternPlate
          the flag to indicate whether to automatically pattern the plate feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AutoPatternStiffener
    ##   the flag to indicate whether to automatically pattern the stiffener feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def AutoPatternStiffener(self) -> bool:
        """
        Getter for property: (bool) AutoPatternStiffener
          the flag to indicate whether to automatically pattern the stiffener feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AutoPatternStiffener

    ##   the flag to indicate whether to automatically pattern the stiffener feature at creation when dependent source has been patterned.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @AutoPatternStiffener.setter
    def AutoPatternStiffener(self, autoPatternStiffener: bool):
        """
        Setter for property: (bool) AutoPatternStiffener
          the flag to indicate whether to automatically pattern the stiffener feature at creation when dependent source has been patterned.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
## 
##         Represents a @link NXOpen::Features::StructureDesign::Plate NXOpen::Features::StructureDesign::Plate@endlink  builder. This builder is used to
##         create and edit structure design plate feature. The plate feature can be created from construction curves, 
##         boundary faces or planes. 
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignPlateBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignPlateBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DistanceTolerance </term> <description> 
##  
## 0.0254 (millimeters part), 0.001 (inches part) </description> </item> 
## 
## <item><term> 
##  
## OffsetOption </term> <description> 
##  
## InsideOnly </description> </item> 
## 
## <item><term> 
##  
## PlateStock.OppositeThickness.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class PlateBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a <ja_class>NXOpen.Features.StructureDesign.Plate</ja_class> builder. This builder is used to
        create and edit structure design plate feature. The plate feature can be created from construction curves, 
        boundary faces or planes. 
        """


    ##  Settings to indicate the plate offset options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ## </description> </item><item><term> 
    ## InsideOnly</term><description> 
    ## </description> </item><item><term> 
    ## OutsideOnly</term><description> 
    ## </description> </item></list>
    class OffsetOptions(Enum):
        """
        Members Include: <All> <InsideOnly> <OutsideOnly>
        """
        All: int
        InsideOnly: int
        OutsideOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlateBuilder.OffsetOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the structure design comp   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the structure design comp   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurveBoundary
    ##   the curve boundary, which can be a single region or multiple regions.  
    ##    
    ##             In case of multiple regions, it creates multiple plates.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def CurveBoundary(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) CurveBoundary
          the curve boundary, which can be a single region or multiple regions.  
           
                    In case of multiple regions, it creates multiple plates.   
         
        """
        pass
    
    ## Getter for property: (float) DistanceTolerance
    ##   the distance tolerance.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def DistanceTolerance(self) -> float:
        """
        Getter for property: (float) DistanceTolerance
          the distance tolerance.  
             
         
        """
        pass
    
    ## Setter for property: (float) DistanceTolerance

    ##   the distance tolerance.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @DistanceTolerance.setter
    def DistanceTolerance(self, distanceTolerance: float):
        """
        Setter for property: (float) DistanceTolerance
          the distance tolerance.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ExpressionCollectorSetList NXOpen.ExpressionCollectorSetList@endlink) FacePlaneBoundary
    ##   the selected face/plane boundary.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.ExpressionCollectorSetList
    @property
    def FacePlaneBoundary(self) -> NXOpen.ExpressionCollectorSetList:
        """
        Getter for property: (@link NXOpen.ExpressionCollectorSetList NXOpen.ExpressionCollectorSetList@endlink) FacePlaneBoundary
          the selected face/plane boundary.  
             
         
        """
        pass
    
    ## Getter for property: (str) FileName
    ##   the name used for the created component file.  
    ##    If a duplicate name, will append a number to this name. This
    ##             property is only used during creation of the member.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
          the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                    property is only used during creation of the member.   
         
        """
        pass
    
    ## Setter for property: (str) FileName

    ##   the name used for the created component file.  
    ##    If a duplicate name, will append a number to this name. This
    ##             property is only used during creation of the member.   
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
          the name used for the created component file.  
           If a duplicate name, will append a number to this name. This
                    property is only used during creation of the member.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) MergeRegions
    ##   the multiple regions to merge together as plate body.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def MergeRegions(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) MergeRegions
          the multiple regions to merge together as plate body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) MoldFace
    ##   the mold face, which is used to create the plate body and define the plate placement.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def MoldFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) MoldFace
          the mold face, which is used to create the plate body and define the plate placement.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##    the plate offset value .  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
           the plate offset value .  
            
         
        """
        pass
    
    ## Getter for property: (@link PlateBuilder.OffsetOptions NXOpen.Features.StructureDesign.PlateBuilder.OffsetOptions@endlink) OffsetOption
    ##   the offset option, which defines the plate side faces to be offset.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return PlateBuilder.OffsetOptions
    @property
    def OffsetOption(self) -> PlateBuilder.OffsetOptions:
        """
        Getter for property: (@link PlateBuilder.OffsetOptions NXOpen.Features.StructureDesign.PlateBuilder.OffsetOptions@endlink) OffsetOption
          the offset option, which defines the plate side faces to be offset.  
             
         
        """
        pass
    
    ## Setter for property: (@link PlateBuilder.OffsetOptions NXOpen.Features.StructureDesign.PlateBuilder.OffsetOptions@endlink) OffsetOption

    ##   the offset option, which defines the plate side faces to be offset.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @OffsetOption.setter
    def OffsetOption(self, offsetOption: PlateBuilder.OffsetOptions):
        """
        Setter for property: (@link PlateBuilder.OffsetOptions NXOpen.Features.StructureDesign.PlateBuilder.OffsetOptions@endlink) OffsetOption
          the offset option, which defines the plate side faces to be offset.  
             
         
        """
        pass
    
    ## Getter for property: (@link PlateStockBuilder NXOpen.Features.StructureDesign.PlateStockBuilder@endlink) PlateStock
    ##   the plate stock builder, which defines the plate material, grade, thickness, mass density, thicken option and opposite thickness.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return PlateStockBuilder
    @property
    def PlateStock(self) -> PlateStockBuilder:
        """
        Getter for property: (@link PlateStockBuilder NXOpen.Features.StructureDesign.PlateStockBuilder@endlink) PlateStock
          the plate stock builder, which defines the plate material, grade, thickness, mass density, thicken option and opposite thickness.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectDirection
    ##   the project direction, which is used to project the boundary curves to the plate mold face.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.GeometricUtilities.ProjectionOptions
    @property
    def ProjectDirection(self) -> NXOpen.GeometricUtilities.ProjectionOptions:
        """
        Getter for property: (@link NXOpen.GeometricUtilities.ProjectionOptions NXOpen.GeometricUtilities.ProjectionOptions@endlink) ProjectDirection
          the project direction, which is used to project the boundary curves to the plate mold face.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) RegionPoint
    ##   the region point, which is used to identify the plate region.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def RegionPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) RegionPoint
          the region point, which is used to identify the plate region.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) RegionPoint

    ##   the region point, which is used to identify the plate region.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @RegionPoint.setter
    def RegionPoint(self, regionPoint: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) RegionPoint
          the region point, which is used to identify the plate region.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Regions
    ##   the regions to create plates  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Regions(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Regions
          the regions to create plates  
            
         
        """
        pass
    
    ##  Adds a merge region point. If there are multiple region points, do a loop to add one by one. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="regionPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def AddMergeRegionPoint(builder: PlateBuilder, regionPoint: NXOpen.Point3d) -> None:
        """
         Adds a merge region point. If there are multiple region points, do a loop to add one by one. 
        """
        pass
    
    ##  Adds a region point. If there are multiple region points, do a loop to add one by one. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="regionPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def AddRegionPoint(builder: PlateBuilder, regionPoint: NXOpen.Point3d) -> None:
        """
         Adds a region point. If there are multiple region points, do a loop to add one by one. 
        """
        pass
    
    ##  Clears the selected regions and merged regions. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def ClearRegions(builder: PlateBuilder) -> None:
        """
         Clears the selected regions and merged regions. 
        """
        pass
    
    ##  Creates regions to output the selected plates. 
    ##  @return regionBodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  Region Bodies .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    def CreateRegions(builder: PlateBuilder) -> List[NXOpen.Body]:
        """
         Creates regions to output the selected plates. 
         @return regionBodies (@link NXOpen.Body List[NXOpen.Body]@endlink):  Region Bodies .
        """
        pass
    
    ##  Deletes regions 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def DeleteRegions(builder: PlateBuilder) -> None:
        """
         Deletes regions 
        """
        pass
    
    ##  Gets multiple region points. 
    ##  @return region_points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetMultipleRegionPoints(builder: PlateBuilder) -> List[NXOpen.Point3d]:
        """
         Gets multiple region points. 
         @return region_points (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink): .
        """
        pass
    
    ##   Maps the user selected plate region to a region point. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="plateRegionString"> (str) </param>
    ## <param name="regionPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def MapRegionToRegionPoint(builder: PlateBuilder, plateRegionString: str, regionPoint: NXOpen.Point3d) -> None:
        """
          Maps the user selected plate region to a region point. 
        """
        pass
    
    ##  Removes all merged region points. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def RemoveAllMergedRegionPoints(builder: PlateBuilder) -> None:
        """
         Removes all merged region points. 
        """
        pass
    
    ##  Removes all region points. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RemoveAllRegionPoints(builder: PlateBuilder) -> None:
        """
         Removes all region points. 
        """
        pass
    
    ##  Removes a merge region point. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="regionPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def RemoveMergeRegionPoint(builder: PlateBuilder, regionPoint: NXOpen.Point3d) -> None:
        """
         Removes a merge region point. 
        """
        pass
    
    ##  Removes a region point. Plate will find the region body by the input region point and remove the cached region point.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="regionPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="bMerge"> (bool) </param>
    def RemoveRegionPoint(builder: PlateBuilder, regionPoint: NXOpen.Point3d, bMerge: bool) -> None:
        """
         Removes a region point. Plate will find the region body by the input region point and remove the cached region point.
        """
        pass
    
    ##  Sets the status of the preview enabling status. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="enabled"> (bool) </param>
    def SetPreviewEnabled(builder: PlateBuilder, enabled: bool) -> None:
        """
         Sets the status of the preview enabling status. 
        """
        pass
    
import NXOpen
## 
##         Represents a @link NXOpen::Features::StructureDesign::PlateStockBuilder NXOpen::Features::StructureDesign::PlateStockBuilder@endlink  builder. 
##          <br> This class is sub-object of another builder, and cannot be directly instantiated.  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## OppositeThickness.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2306.0.0  <br> 

class PlateStockBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.Features.StructureDesign.PlateStockBuilder</ja_class> builder. 
        """


    ##  the plate stock thickness direction options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Up</term><description> 
    ## </description> </item><item><term> 
    ## Down</term><description> 
    ## </description> </item><item><term> 
    ## Both</term><description> 
    ## </description> </item></list>
    class ThicknessDirs(Enum):
        """
        Members Include: <Up> <Down> <Both>
        """
        Up: int
        Down: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PlateStockBuilder.ThicknessDirs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OppositeThickness
    ##   the opposite thickness.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OppositeThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OppositeThickness
          the opposite thickness.  
             
         
        """
        pass
    
    ## Getter for property: (@link PlateStockBuilder.ThicknessDirs NXOpen.Features.StructureDesign.PlateStockBuilder.ThicknessDirs@endlink) ThicknessDirection
    ##   the thickness direction   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return PlateStockBuilder.ThicknessDirs
    @property
    def ThicknessDirection(self) -> PlateStockBuilder.ThicknessDirs:
        """
        Getter for property: (@link PlateStockBuilder.ThicknessDirs NXOpen.Features.StructureDesign.PlateStockBuilder.ThicknessDirs@endlink) ThicknessDirection
          the thickness direction   
            
         
        """
        pass
    
    ## Setter for property: (@link PlateStockBuilder.ThicknessDirs NXOpen.Features.StructureDesign.PlateStockBuilder.ThicknessDirs@endlink) ThicknessDirection

    ##   the thickness direction   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ThicknessDirection.setter
    def ThicknessDirection(self, thickness: PlateStockBuilder.ThicknessDirs):
        """
        Setter for property: (@link PlateStockBuilder.ThicknessDirs NXOpen.Features.StructureDesign.PlateStockBuilder.ThicknessDirs@endlink) ThicknessDirection
          the thickness direction   
            
         
        """
        pass
    
    ##  It is used to update spreadsheet data. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="paramNames"> (List[str]) </param>
    ## <param name="paramValues"> (List[str]) </param>
    def UpdateSpreadsheetData(builder: PlateStockBuilder, paramNames: List[str], paramValues: List[str]) -> None:
        """
         It is used to update spreadsheet data. 
        """
        pass
    
import NXOpen.Features
##  Represents a structure plate feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::PlateBuilder  NXOpen::Features::StructureDesign::PlateBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class Plate(NXOpen.Features.BodyFeature): 
    """ Represents a structure plate feature """
    pass


import NXOpen
import NXOpen.Features
## 
##         Represents a Structure Design Rule builder.
##          <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignRuleBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignRuleBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ButtOption </term> <description> 
##  
## ButtShortest </description> </item> 
## 
## <item><term> 
##  
## CopeOption </term> <description> 
##  
## CopeShortest </description> </item> 
## 
## <item><term> 
##  
## HorizontalCornerType </term> <description> 
##  
## Miter </description> </item> 
## 
## <item><term> 
##  
## InnerCornerType </term> <description> 
##  
## None </description> </item> 
## 
## <item><term> 
##  
## Placement </term> <description> 
##  
## Inside </description> </item> 
## 
## <item><term> 
##  
## VerticalCornerType </term> <description> 
##  
## Butt </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class RuleBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a Structure Design Rule builder.
        """


    ##  The Option to define the butt option type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ButtShortest</term><description> 
    ## </description> </item><item><term> 
    ## ButtLongest</term><description> 
    ## </description> </item></list>
    class ButtOptions(Enum):
        """
        Members Include: <ButtShortest> <ButtLongest>
        """
        ButtShortest: int
        ButtLongest: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.ButtOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Option to define the cope option type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CopeShortest</term><description> 
    ## </description> </item><item><term> 
    ## CopeLongest</term><description> 
    ## </description> </item></list>
    class CopeOptions(Enum):
        """
        Members Include: <CopeShortest> <CopeLongest>
        """
        CopeShortest: int
        CopeLongest: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.CopeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Option to define the corner type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Miter</term><description> 
    ## </description> </item><item><term> 
    ## Butt</term><description> 
    ## </description> </item><item><term> 
    ## Cope</term><description> 
    ## </description> </item><item><term> 
    ## MatchedCope</term><description> 
    ## </description> </item></list>
    class CornerTypes(Enum):
        """
        Members Include: <NotSet> <Miter> <Butt> <Cope> <MatchedCope>
        """
        NotSet: int
        Miter: int
        Butt: int
        Cope: int
        MatchedCope: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.CornerTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Option to define the member placement. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inside</term><description> 
    ## </description> </item><item><term> 
    ## Center</term><description> 
    ## </description> </item><item><term> 
    ## Outside</term><description> 
    ## </description> </item></list>
    class Placements(Enum):
        """
        Members Include: <Inside> <Center> <Outside>
        """
        Inside: int
        Center: int
        Outside: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RuleBuilder.Placements:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link RuleBuilder.ButtOptions NXOpen.Features.StructureDesign.RuleBuilder.ButtOptions@endlink) ButtOption
    ##   the butt option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return RuleBuilder.ButtOptions
    @property
    def ButtOption(self) -> RuleBuilder.ButtOptions:
        """
        Getter for property: (@link RuleBuilder.ButtOptions NXOpen.Features.StructureDesign.RuleBuilder.ButtOptions@endlink) ButtOption
          the butt option   
            
         
        """
        pass
    
    ## Setter for property: (@link RuleBuilder.ButtOptions NXOpen.Features.StructureDesign.RuleBuilder.ButtOptions@endlink) ButtOption

    ##   the butt option   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @ButtOption.setter
    def ButtOption(self, buttOption: RuleBuilder.ButtOptions):
        """
        Setter for property: (@link RuleBuilder.ButtOptions NXOpen.Features.StructureDesign.RuleBuilder.ButtOptions@endlink) ButtOption
          the butt option   
            
         
        """
        pass
    
    ## Getter for property: (@link RuleBuilder.CopeOptions NXOpen.Features.StructureDesign.RuleBuilder.CopeOptions@endlink) CopeOption
    ##   the cope option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return RuleBuilder.CopeOptions
    @property
    def CopeOption(self) -> RuleBuilder.CopeOptions:
        """
        Getter for property: (@link RuleBuilder.CopeOptions NXOpen.Features.StructureDesign.RuleBuilder.CopeOptions@endlink) CopeOption
          the cope option   
            
         
        """
        pass
    
    ## Setter for property: (@link RuleBuilder.CopeOptions NXOpen.Features.StructureDesign.RuleBuilder.CopeOptions@endlink) CopeOption

    ##   the cope option   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @CopeOption.setter
    def CopeOption(self, copeOption: RuleBuilder.CopeOptions):
        """
        Setter for property: (@link RuleBuilder.CopeOptions NXOpen.Features.StructureDesign.RuleBuilder.CopeOptions@endlink) CopeOption
          the cope option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Cutback
    ##   the cutback value.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Cutback(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Cutback
          the cutback value.  
            
         
        """
        pass
    
    ## Getter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) HorizontalCornerType
    ##   the horizontal corner type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return RuleBuilder.CornerTypes
    @property
    def HorizontalCornerType(self) -> RuleBuilder.CornerTypes:
        """
        Getter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) HorizontalCornerType
          the horizontal corner type   
            
         
        """
        pass
    
    ## Setter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) HorizontalCornerType

    ##   the horizontal corner type   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @HorizontalCornerType.setter
    def HorizontalCornerType(self, horizontalCornerType: RuleBuilder.CornerTypes):
        """
        Setter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) HorizontalCornerType
          the horizontal corner type   
            
         
        """
        pass
    
    ## Getter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) InnerCornerType
    ##   the inner corner type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return RuleBuilder.CornerTypes
    @property
    def InnerCornerType(self) -> RuleBuilder.CornerTypes:
        """
        Getter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) InnerCornerType
          the inner corner type   
            
         
        """
        pass
    
    ## Setter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) InnerCornerType

    ##   the inner corner type   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @InnerCornerType.setter
    def InnerCornerType(self, innerCornerType: RuleBuilder.CornerTypes):
        """
        Setter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) InnerCornerType
          the inner corner type   
            
         
        """
        pass
    
    ## Getter for property: (@link RuleBuilder.Placements NXOpen.Features.StructureDesign.RuleBuilder.Placements@endlink) Placement
    ##   the placement   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return RuleBuilder.Placements
    @property
    def Placement(self) -> RuleBuilder.Placements:
        """
        Getter for property: (@link RuleBuilder.Placements NXOpen.Features.StructureDesign.RuleBuilder.Placements@endlink) Placement
          the placement   
            
         
        """
        pass
    
    ## Setter for property: (@link RuleBuilder.Placements NXOpen.Features.StructureDesign.RuleBuilder.Placements@endlink) Placement

    ##   the placement   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Placement.setter
    def Placement(self, placement: RuleBuilder.Placements):
        """
        Setter for property: (@link RuleBuilder.Placements NXOpen.Features.StructureDesign.RuleBuilder.Placements@endlink) Placement
          the placement   
            
         
        """
        pass
    
    ## Getter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) VerticalCornerType
    ##   the vertical corner type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return RuleBuilder.CornerTypes
    @property
    def VerticalCornerType(self) -> RuleBuilder.CornerTypes:
        """
        Getter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) VerticalCornerType
          the vertical corner type   
            
         
        """
        pass
    
    ## Setter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) VerticalCornerType

    ##   the vertical corner type   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @VerticalCornerType.setter
    def VerticalCornerType(self, verticalCornerType: RuleBuilder.CornerTypes):
        """
        Setter for property: (@link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink) VerticalCornerType
          the vertical corner type   
            
         
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a list of objects on a selection list.

## 
##   <br>  Created in NX5.0.0  <br> 

class SelectCornerList(NXOpen.TaggedObject): 
    """ Represents a list of objects on a selection list.
"""


    ## Getter for property: (bool) DuplicatesAllowed
    ##   whether duplicate objects are allowed in the selection list.  
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
          whether duplicate objects are allowed in the selection list.  
          
              
         
        """
        pass
    
    ## Getter for property: (int) Size
    ##   the number of objects in the list.  
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
          the number of objects in the list.  
          
              
         
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
    ##  object to add 
    def Add(object_list: SelectCornerList, objectValue: Corner) -> bool:
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
    ##  objects to add 
    def AddWithViews(object_list: SelectCornerList, objects: List[Corner], views: List[NXOpen.View]) -> bool:
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
    ##  objects to add 
    @overload
    def Add(self, object_list: SelectCornerList, objects: List[Corner]) -> bool:
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
    ##  selection method containing objects to add 
    @overload
    def Add(self, object_list: SelectCornerList, input_selection_method: NXOpen.SelectionMethod) -> bool:
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
    ##  selected object 
    @overload
    def Add(self, object_list: SelectCornerList, selection: Corner, view: NXOpen.View, point: NXOpen.Point3d) -> bool:
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
    ##   snap point type
    @overload
    def Add(self, object_list: SelectCornerList, snap_type: NXOpen.InferSnapType.SnapType, selection1: Corner, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Corner, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    ##  selected object 
    @overload
    def Add(self, object_list: SelectCornerList, selection: Corner, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> bool:
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
    @staticmethod
    def Clear(object_list: SelectCornerList) -> None:
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
    ##  object to check 
    def Contains(object_list: SelectCornerList, objectValue: Corner) -> bool:
        """
         Returns whether the specified object is already in the list or not.
            
         @return list_contains (bool):  true if object is in the list, false otherwise .
        """
        pass
    
    ##  Returns the list of objects in the selection list.
    ##     
    ##  @return objects (@link Corner List[NXOpen.Features.StructureDesign.Corner]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetArray(object_list: SelectCornerList) -> List[Corner]:
        """
         Returns the list of objects in the selection list.
            
         @return objects (@link Corner List[NXOpen.Features.StructureDesign.Corner]@endlink):  items in list .
        """
        pass
    
    ##  Returns the list of SelectObjects in the selection list.
    ##     
    ##  @return objects (@link NXOpen.SelectObject List[NXOpen.SelectObject]@endlink):  items in list .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetSelectObjectArray(object_list: SelectCornerList) -> List[NXOpen.SelectObject]:
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
    ##  Object to remove 
    def Remove(object_list: SelectCornerList, objectValue: Corner) -> bool:
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
    ##  Objects to remove 
    def RemoveArray(object_list: SelectCornerList, objects: List[Corner]) -> bool:
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
    ##  Object to remove 
    @overload
    def Remove(self, object_list: SelectCornerList, objectValue: Corner, view: NXOpen.View) -> bool:
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
    ##   snap point type
    @overload
    def Remove(self, object_list: SelectCornerList, snap_type: NXOpen.InferSnapType.SnapType, selection1: Corner, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Corner, view2: NXOpen.View, point2: NXOpen.Point3d) -> bool:
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
    ##  selection method containing objects to add 
    @overload
    def Remove(self, object_list: SelectCornerList, input_selection_method: NXOpen.SelectionMethod) -> bool:
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
    ##  items to put in the list
    def SetArray(object_list: SelectCornerList, objects: List[Corner]) -> None:
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

class SelectCorner(NXOpen.TaggedObject): 
    """ Represents a single object selection.
"""


    ## Getter for property: (@link Corner NXOpen.Features.StructureDesign.Corner@endlink) Value
    ##   the object being selected
    ##       
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return Corner
    @property
    def Value(self) -> Corner:
        """
        Getter for property: (@link Corner NXOpen.Features.StructureDesign.Corner@endlink) Value
          the object being selected
              
            
         
        """
        pass
    
    ## Setter for property: (@link Corner NXOpen.Features.StructureDesign.Corner@endlink) Value

    ##   the object being selected
    ##       
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Value.setter
    def Value(self, selection: Corner):
        """
        Setter for property: (@link Corner NXOpen.Features.StructureDesign.Corner@endlink) Value
          the object being selected
              
            
         
        """
        pass
    
    ##  The object being selected with the object's view and point.
    ##     
    ##  @return A tuple consisting of (selection, view, point). 
    ##  - selection is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. selected object .
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
    ##  - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectCorner NXOpen.Features.StructureDesign.SelectCorner@endlink) </param>
    @staticmethod
    @overload
    def GetValue(self, select_object: SelectCorner) -> Tuple[Corner, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the object's view and point.
            
         @return A tuple consisting of (selection, view, point). 
         - selection is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. selected object .
         - view is: @link NXOpen.View NXOpen.View@endlink. selected object view.
         - point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. selected object point.

        """
        pass
    
    ##  The object being selected with the objects view and point and snap information.
    ##     
    ##  @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
    ##  - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
    ##  - selection1 is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. first selected object .
    ##  - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
    ##  - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
    ##  - selection2 is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. second selected object .
    ##  - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
    ##  - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectCorner NXOpen.Features.StructureDesign.SelectCorner@endlink) </param>
    @staticmethod
    @overload
    def GetValue(self, select_object: SelectCorner) -> Tuple[NXOpen.InferSnapType.SnapType, Corner, NXOpen.View, NXOpen.Point3d, Corner, NXOpen.View, NXOpen.Point3d]:
        """
         The object being selected with the objects view and point and snap information.
            
         @return A tuple consisting of (snap_type, selection1, view1, point1, selection2, view2, point2). 
         - snap_type is: @link NXOpen.InferSnapType.SnapType NXOpen.InferSnapType.SnapType@endlink.  snap point type.
         - selection1 is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. first selected object .
         - view1 is: @link NXOpen.View NXOpen.View@endlink. first selected object view.
         - point1 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. first selected object point.
         - selection2 is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. second selected object .
         - view2 is: @link NXOpen.View NXOpen.View@endlink. second selected object view.
         - point2 is: @link NXOpen.Point3d NXOpen.Point3d@endlink. second selected object point.

        """
        pass
    
    ##  The object being selected with CAE set object information.
    ##     
    ##  @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
    ##  - selection is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. selected object .
    ##  - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
    ##  - cae_sub_id is: int. CAE set object sub id.

    ## 
    ##   <br>  Created in NX5.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use other versions of @link NXOpen::SelectObject::GetValue NXOpen::SelectObject::GetValue@endlink .  <br> 

    ## License requirements: None.
    ## <param name="select_object"> (@link SelectCorner NXOpen.Features.StructureDesign.SelectCorner@endlink) </param>
    @staticmethod
    @overload
    def GetValue(self, select_object: SelectCorner) -> Tuple[Corner, NXOpen.CaeObjectType.CaeSubType, int]:
        """
         The object being selected with CAE set object information.
            
         @return A tuple consisting of (selection, cae_sub_type, cae_sub_id). 
         - selection is: @link Corner NXOpen.Features.StructureDesign.Corner@endlink. selected object .
         - cae_sub_type is: @link NXOpen.CaeObjectType.CaeSubType NXOpen.CaeObjectType.CaeSubType@endlink. CAE set object sub type.
         - cae_sub_id is: int. CAE set object sub id.

        """
        pass
    
    ##  The object being selected with the object's view and object's point
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  selected object 
    @overload
    def SetValue(self, select_object: SelectCorner, selection: Corner, view: NXOpen.View, point: NXOpen.Point3d) -> None:
        """
         The object being selected with the object's view and object's point
            
        """
        pass
    
    ##  The object being selected with the objects view and objects point and snap information.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##   snap point type
    @overload
    def SetValue(self, select_object: SelectCorner, snap_type: NXOpen.InferSnapType.SnapType, selection1: Corner, view1: NXOpen.View, point1: NXOpen.Point3d, selection2: Corner, view2: NXOpen.View, point2: NXOpen.Point3d) -> None:
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
    ##  selected object 
    @overload
    def SetValue(self, select_object: SelectCorner, selection: Corner, cae_sub_type: NXOpen.CaeObjectType.CaeSubType, cae_sub_id: int) -> None:
        """
         The object being selected with CAE set object information.
            
        """
        pass
    
import NXOpen
import NXOpen.Features
## 
##     Represents a @link Features::StructureDesign::Stiffener Features::StructureDesign::Stiffener@endlink  builder
##      <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignStiffenerBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignStiffenerBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DepthOffset.Value </term> <description> 
##  
## 3 (millimeters part), 1.2 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Height.Value </term> <description> 
##  
## 25 (millimeters part), 9.8 (inches part) </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class StiffenerBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>Features.StructureDesign.Stiffener</ja_class> builder
    """


    ## 
    ##         the alignment direction 
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item><item><term> 
    ## Both</term><description> 
    ## </description> </item></list>
    class AttachmentSides(Enum):
        """
        Members Include: <Left> <Right> <Both>
        """
        Left: int
        Right: int
        Both: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.AttachmentSides:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         the fill type
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UppperHalf</term><description> 
    ## </description> </item><item><term> 
    ## LowerHalf</term><description> 
    ## </description> </item><item><term> 
    ## Full</term><description> 
    ## </description> </item><item><term> 
    ## MatchedCope</term><description> 
    ## </description> </item></list>
    class FillTypes(Enum):
        """
        Members Include: <UppperHalf> <LowerHalf> <Full> <MatchedCope>
        """
        UppperHalf: int
        LowerHalf: int
        Full: int
        MatchedCope: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.FillTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##         the height type
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Default</term><description> 
    ## </description> </item><item><term> 
    ## Input</term><description> 
    ## </description> </item></list>
    class HeightTypes(Enum):
        """
        Members Include: <Default> <Input>
        """
        Default: int
        Input: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.HeightTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the thickness direction 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Upper</term><description> 
    ## </description> </item><item><term> 
    ## Lower</term><description> 
    ## </description> </item><item><term> 
    ## Center</term><description> 
    ## </description> </item></list>
    class ThicknessDirs(Enum):
        """
        Members Include: <Upper> <Lower> <Center>
        """
        Upper: int
        Lower: int
        Center: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> StiffenerBuilder.ThicknessDirs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Alignment
    ##   the alignment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectTaggedObjectList
    @property
    def Alignment(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: (@link NXOpen.SelectTaggedObjectList NXOpen.SelectTaggedObjectList@endlink) Alignment
          the alignment   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffenerBuilder.AttachmentSides NXOpen.Features.StructureDesign.StiffenerBuilder.AttachmentSides@endlink) AttachmentSide
    ##   the fill type to be used to Stiffener   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return StiffenerBuilder.AttachmentSides
    @property
    def AttachmentSide(self) -> StiffenerBuilder.AttachmentSides:
        """
        Getter for property: (@link StiffenerBuilder.AttachmentSides NXOpen.Features.StructureDesign.StiffenerBuilder.AttachmentSides@endlink) AttachmentSide
          the fill type to be used to Stiffener   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffenerBuilder.AttachmentSides NXOpen.Features.StructureDesign.StiffenerBuilder.AttachmentSides@endlink) AttachmentSide

    ##   the fill type to be used to Stiffener   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @AttachmentSide.setter
    def AttachmentSide(self, attachmentSide: StiffenerBuilder.AttachmentSides):
        """
        Setter for property: (@link StiffenerBuilder.AttachmentSides NXOpen.Features.StructureDesign.StiffenerBuilder.AttachmentSides@endlink) AttachmentSide
          the fill type to be used to Stiffener   
            
         
        """
        pass
    
    ## Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
    ##   the structure design comp   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return ContextAttributeBuilder
    @property
    def ContextAttribute(self) -> ContextAttributeBuilder:
        """
        Getter for property: (@link ContextAttributeBuilder NXOpen.Features.StructureDesign.ContextAttributeBuilder@endlink) ContextAttribute
          the structure design comp   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DepthOffset
    ##   the depth offset   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DepthOffset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DepthOffset
          the depth offset   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffenerBuilder.FillTypes NXOpen.Features.StructureDesign.StiffenerBuilder.FillTypes@endlink) FillType
    ##   the fill type to be used to Stiffener   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return StiffenerBuilder.FillTypes
    @property
    def FillType(self) -> StiffenerBuilder.FillTypes:
        """
        Getter for property: (@link StiffenerBuilder.FillTypes NXOpen.Features.StructureDesign.StiffenerBuilder.FillTypes@endlink) FillType
          the fill type to be used to Stiffener   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffenerBuilder.FillTypes NXOpen.Features.StructureDesign.StiffenerBuilder.FillTypes@endlink) FillType

    ##   the fill type to be used to Stiffener   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @FillType.setter
    def FillType(self, fillType: StiffenerBuilder.FillTypes):
        """
        Setter for property: (@link StiffenerBuilder.FillTypes NXOpen.Features.StructureDesign.StiffenerBuilder.FillTypes@endlink) FillType
          the fill type to be used to Stiffener   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height   
            
         
        """
        pass
    
    ## Getter for property: (@link StiffenerBuilder.HeightTypes NXOpen.Features.StructureDesign.StiffenerBuilder.HeightTypes@endlink) HeightType
    ##   the height value type to be used to Stiffener   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return StiffenerBuilder.HeightTypes
    @property
    def HeightType(self) -> StiffenerBuilder.HeightTypes:
        """
        Getter for property: (@link StiffenerBuilder.HeightTypes NXOpen.Features.StructureDesign.StiffenerBuilder.HeightTypes@endlink) HeightType
          the height value type to be used to Stiffener   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffenerBuilder.HeightTypes NXOpen.Features.StructureDesign.StiffenerBuilder.HeightTypes@endlink) HeightType

    ##   the height value type to be used to Stiffener   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @HeightType.setter
    def HeightType(self, fillType: StiffenerBuilder.HeightTypes):
        """
        Setter for property: (@link StiffenerBuilder.HeightTypes NXOpen.Features.StructureDesign.StiffenerBuilder.HeightTypes@endlink) HeightType
          the height value type to be used to Stiffener   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
    ##   the offset distance to the referenced object to adjust stiffener location.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetDistance
          the offset distance to the referenced object to adjust stiffener location.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReverseOffset
    ##   the flag to specify whether the stiffener offset distance direction is reversed or not.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ReverseOffset(self) -> bool:
        """
        Getter for property: (bool) ReverseOffset
          the flag to specify whether the stiffener offset distance direction is reversed or not.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ReverseOffset

    ##   the flag to specify whether the stiffener offset distance direction is reversed or not.  
    ##      
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ReverseOffset.setter
    def ReverseOffset(self, reverseOffset: bool):
        """
        Setter for property: (bool) ReverseOffset
          the flag to specify whether the stiffener offset distance direction is reversed or not.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectObject
    ##   the attachment   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SelectObject(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectObject
          the attachment   
            
         
        """
        pass
    
    ## Getter for property: (str) StiffenerName
    ##   the stiffener name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def StiffenerName(self) -> str:
        """
        Getter for property: (str) StiffenerName
          the stiffener name   
            
         
        """
        pass
    
    ## Setter for property: (str) StiffenerName

    ##   the stiffener name   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @StiffenerName.setter
    def StiffenerName(self, stiffenerName: str):
        """
        Setter for property: (str) StiffenerName
          the stiffener name   
            
         
        """
        pass
    
    ## Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
    ##   the stock data used to define the stock information of the Stiffener.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return FeatureSpreadsheetBuilder
    @property
    def StockData(self) -> FeatureSpreadsheetBuilder:
        """
        Getter for property: (@link FeatureSpreadsheetBuilder NXOpen.Features.StructureDesign.FeatureSpreadsheetBuilder@endlink) StockData
          the stock data used to define the stock information of the Stiffener.  
            
         
        """
        pass
    
    ## Getter for property: (@link StiffenerBuilder.ThicknessDirs NXOpen.Features.StructureDesign.StiffenerBuilder.ThicknessDirs@endlink) ThicknessDir
    ##   the fill type to be used to Stiffener   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return StiffenerBuilder.ThicknessDirs
    @property
    def ThicknessDir(self) -> StiffenerBuilder.ThicknessDirs:
        """
        Getter for property: (@link StiffenerBuilder.ThicknessDirs NXOpen.Features.StructureDesign.StiffenerBuilder.ThicknessDirs@endlink) ThicknessDir
          the fill type to be used to Stiffener   
            
         
        """
        pass
    
    ## Setter for property: (@link StiffenerBuilder.ThicknessDirs NXOpen.Features.StructureDesign.StiffenerBuilder.ThicknessDirs@endlink) ThicknessDir

    ##   the fill type to be used to Stiffener   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ThicknessDir.setter
    def ThicknessDir(self, fillType: StiffenerBuilder.ThicknessDirs):
        """
        Setter for property: (@link StiffenerBuilder.ThicknessDirs NXOpen.Features.StructureDesign.StiffenerBuilder.ThicknessDirs@endlink) ThicknessDir
          the fill type to be used to Stiffener   
            
         
        """
        pass
    
import NXOpen.Features
##  Represents a Stiffener feature  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::StiffenerBuilder  NXOpen::Features::StructureDesign::StiffenerBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Stiffener(NXOpen.Features.BodyFeature): 
    """ Represents a Stiffener feature """
    pass


import NXOpen
## 
##     Represents a builder which is used to create or edit a Structure Design SuperFrame feature.
##      <br> To create a new instance of this class, use @link NXOpen::Features::StructureDesignCollection::CreateStructureDesignSuperFrameBuilder  NXOpen::Features::StructureDesignCollection::CreateStructureDesignSuperFrameBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class SuperFrameBuilder(FeatureParmsBuilder): 
    """
    Represents a builder which is used to create or edit a Structure Design SuperFrame feature.
    """


    ##  the base types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Corners</term><description> 
    ## </description> </item><item><term> 
    ## Transform</term><description> 
    ## </description> </item></list>
    class BaseTypes(Enum):
        """
        Members Include: <NotSet> <Corners> <Transform>
        """
        NotSet: int
        Corners: int
        Transform: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SuperFrameBuilder.BaseTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the input mode types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Coordinates</term><description> 
    ## </description> </item><item><term> 
    ## Parameters</term><description> 
    ## </description> </item></list>
    class InputModes(Enum):
        """
        Members Include: <Coordinates> <Parameters>
        """
        Coordinates: int
        Parameters: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SuperFrameBuilder.InputModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the transform types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Move</term><description> 
    ## </description> </item><item><term> 
    ## Copy</term><description> 
    ## </description> </item><item><term> 
    ## Split</term><description> 
    ## </description> </item><item><term> 
    ## Delete</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class TransformTypes(Enum):
        """
        Members Include: <Move> <Copy> <Split> <Delete> <NotSet>
        """
        Move: int
        Copy: int
        Split: int
        Delete: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SuperFrameBuilder.TransformTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryCurve
    ##   the tool curves selected to split   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BoundaryCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BoundaryCurve
          the tool curves selected to split   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
    ##   the height dimension   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Height(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Height
          the height dimension   
            
         
        """
        pass
    
    ## Getter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode0
    ##   the first point input mode  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SuperFrameBuilder.InputModes
    @property
    def InputMode0(self) -> SuperFrameBuilder.InputModes:
        """
        Getter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode0
          the first point input mode  
            
         
        """
        pass
    
    ## Setter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode0

    ##   the first point input mode  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InputMode0.setter
    def InputMode0(self, mode0: SuperFrameBuilder.InputModes):
        """
        Setter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode0
          the first point input mode  
            
         
        """
        pass
    
    ## Getter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode1
    ##   the second point input mode  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SuperFrameBuilder.InputModes
    @property
    def InputMode1(self) -> SuperFrameBuilder.InputModes:
        """
        Getter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode1
          the second point input mode  
            
         
        """
        pass
    
    ## Setter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode1

    ##   the second point input mode  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InputMode1.setter
    def InputMode1(self, mode1: SuperFrameBuilder.InputModes):
        """
        Setter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode1
          the second point input mode  
            
         
        """
        pass
    
    ## Getter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode2
    ##   the third point input mode  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return SuperFrameBuilder.InputModes
    @property
    def InputMode2(self) -> SuperFrameBuilder.InputModes:
        """
        Getter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode2
          the third point input mode  
            
         
        """
        pass
    
    ## Setter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode2

    ##   the third point input mode  
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InputMode2.setter
    def InputMode2(self, mode2: SuperFrameBuilder.InputModes):
        """
        Setter for property: (@link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink) InputMode2
          the third point input mode  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
    ##   the length dimension   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
          the length dimension   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point0
    ##   the first point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point0(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point0
          the first point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point0

    ##   the first point   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Point0.setter
    def Point0(self, point0: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point0
          the first point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point0X
    ##   the first point x coordinate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Point0X(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point0X
          the first point x coordinate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point0Y
    ##   the first point y coordinate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Point0Y(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point0Y
          the first point y coordinate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point0Z
    ##   the first point z coordinate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Point0Z(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point0Z
          the first point z coordinate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point1
    ##   the second point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point1(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point1
          the second point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point1

    ##   the second point   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Point1.setter
    def Point1(self, point1: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point1
          the second point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point1X
    ##   the second point x coordinate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Point1X(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point1X
          the second point x coordinate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point1Y
    ##   the second point y coordinate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Point1Y(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point1Y
          the second point y coordinate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2
    ##   the third point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point2(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2
          the third point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2

    ##   the third point   
    ##     
    ##  
    ## Setter License requirements: nx_structure_design ("Structure Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Point2.setter
    def Point2(self, point2: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point2
          the third point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point2Z
    ##   the third point z coordinate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Point2Z(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Point2Z
          the third point z coordinate   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SplitCurve
    ##   the curves selected to be split   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def SplitCurve(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) SplitCurve
          the curves selected to be split   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##   the width dimension   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
          the width dimension   
            
         
        """
        pass
    
    ##  Adds action to lists. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="sourceCurves"> (@link NXOpen.Curve List[NXOpen.Curve]@endlink) </param>
    ## <param name="actionType"> (@link SuperFrameBuilder.TransformTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes@endlink) </param>
    ## <param name="actionDirection"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink) </param>
    ## <param name="actionDistance"> (float) </param>
    def AddAction(builder: SuperFrameBuilder, sourceCurves: List[NXOpen.Curve], actionType: SuperFrameBuilder.TransformTypes, actionDirection: NXOpen.Vector3d, actionDistance: float) -> None:
        """
         Adds action to lists. 
        """
        pass
    
    ##  Creates a copy of the curve. 
    ##  @return copiedCurveTag (@link NXOpen.Curve NXOpen.Curve@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="curveTag"> (@link NXOpen.Curve NXOpen.Curve@endlink) </param>
    def CopyCurve(builder: SuperFrameBuilder, curveTag: NXOpen.Curve) -> NXOpen.Curve:
        """
         Creates a copy of the curve. 
         @return copiedCurveTag (@link NXOpen.Curve NXOpen.Curve@endlink): .
        """
        pass
    
    ##  Creates the frame curves. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    def CreateCurves(builder: SuperFrameBuilder) -> None:
        """
         Creates the frame curves. 
        """
        pass
    
    ##  Deletes the curve. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="curveTag"> (@link NXOpen.Curve NXOpen.Curve@endlink) </param>
    def DeleteCurve(builder: SuperFrameBuilder, curveTag: NXOpen.Curve) -> None:
        """
         Deletes the curve. 
        """
        pass
    
    ##  Deletes the curve and reparents dependent curves. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="curveTag"> (@link NXOpen.Curve NXOpen.Curve@endlink) </param>
    def ReparentAndDeleteCurve(builder: SuperFrameBuilder, curveTag: NXOpen.Curve) -> None:
        """
         Deletes the curve and reparents dependent curves. 
        """
        pass
    
    ##  Removes last action from lists. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    @staticmethod
    def UndoAction(builder: SuperFrameBuilder) -> None:
        """
         Removes last action from lists. 
        """
        pass
    
    ##  Changes the curve's start and end points. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_structure_design ("Structure Designer")
    ## 
    ## <param name="curveTag"> (@link NXOpen.Curve NXOpen.Curve@endlink) </param>
    ## <param name="startPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="endPoint"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    def UpdateCurve(builder: SuperFrameBuilder, curveTag: NXOpen.Curve, startPoint: NXOpen.Point3d, endPoint: NXOpen.Point3d) -> None:
        """
         Changes the curve's start and end points. 
        """
        pass
    
import NXOpen.Features
##  Represents a structure design super frame feature.  <br> To create or edit an instance of this class, use @link NXOpen::Features::StructureDesign::SuperFrameBuilder  NXOpen::Features::StructureDesign::SuperFrameBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class SuperFrame(NXOpen.Features.BodyFeature): 
    """ Represents a structure design super frame feature. """
    pass


## @package NXOpen.Features.StructureDesign
## Classes, Enums and Structs under NXOpen.Features.StructureDesign namespace

##  @link BoltedConnectionBuilderBeamColumnConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilderBeamColumnConnectionSubTypes @endlink is an alias for @link BoltedConnectionBuilder.BeamColumnConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.BeamColumnConnectionSubTypes@endlink
BoltedConnectionBuilderBeamColumnConnectionSubTypes = BoltedConnectionBuilder.BeamColumnConnectionSubTypes


##  @link BoltedConnectionBuilderConnectionTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilderConnectionTypes @endlink is an alias for @link BoltedConnectionBuilder.ConnectionTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.ConnectionTypes@endlink
BoltedConnectionBuilderConnectionTypes = BoltedConnectionBuilder.ConnectionTypes


##  @link BoltedConnectionBuilderGussetPlateConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilderGussetPlateConnectionSubTypes @endlink is an alias for @link BoltedConnectionBuilder.GussetPlateConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.GussetPlateConnectionSubTypes@endlink
BoltedConnectionBuilderGussetPlateConnectionSubTypes = BoltedConnectionBuilder.GussetPlateConnectionSubTypes


##  @link BoltedConnectionBuilderMountingTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilderMountingTypes @endlink is an alias for @link BoltedConnectionBuilder.MountingTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.MountingTypes@endlink
BoltedConnectionBuilderMountingTypes = BoltedConnectionBuilder.MountingTypes


##  @link BoltedConnectionBuilderSpliceConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilderSpliceConnectionSubTypes @endlink is an alias for @link BoltedConnectionBuilder.SpliceConnectionSubTypes NXOpen.Features.StructureDesign.BoltedConnectionBuilder.SpliceConnectionSubTypes@endlink
BoltedConnectionBuilderSpliceConnectionSubTypes = BoltedConnectionBuilder.SpliceConnectionSubTypes


##  @link ComponentDrawingBuilderDrawingTypeOption NXOpen.Features.StructureDesign.ComponentDrawingBuilderDrawingTypeOption @endlink is an alias for @link ComponentDrawingBuilder.DrawingTypeOption NXOpen.Features.StructureDesign.ComponentDrawingBuilder.DrawingTypeOption@endlink
ComponentDrawingBuilderDrawingTypeOption = ComponentDrawingBuilder.DrawingTypeOption


##  @link CreateStructureBuilderPartTypes NXOpen.Features.StructureDesign.CreateStructureBuilderPartTypes @endlink is an alias for @link CreateStructureBuilder.PartTypes NXOpen.Features.StructureDesign.CreateStructureBuilder.PartTypes@endlink
CreateStructureBuilderPartTypes = CreateStructureBuilder.PartTypes


##  @link DrawingsBuilderTargetAssemblyOption NXOpen.Features.StructureDesign.DrawingsBuilderTargetAssemblyOption @endlink is an alias for @link DrawingsBuilder.TargetAssemblyOption NXOpen.Features.StructureDesign.DrawingsBuilder.TargetAssemblyOption@endlink
DrawingsBuilderTargetAssemblyOption = DrawingsBuilder.TargetAssemblyOption


##  @link EndcapBuilderCornerTreatmentTypes NXOpen.Features.StructureDesign.EndcapBuilderCornerTreatmentTypes @endlink is an alias for @link EndcapBuilder.CornerTreatmentTypes NXOpen.Features.StructureDesign.EndcapBuilder.CornerTreatmentTypes@endlink
EndcapBuilderCornerTreatmentTypes = EndcapBuilder.CornerTreatmentTypes


##  @link EndcapBuilderPlacementTypes NXOpen.Features.StructureDesign.EndcapBuilderPlacementTypes @endlink is an alias for @link EndcapBuilder.PlacementTypes NXOpen.Features.StructureDesign.EndcapBuilder.PlacementTypes@endlink
EndcapBuilderPlacementTypes = EndcapBuilder.PlacementTypes


##  @link ExportDSTVBuilderActionTypes NXOpen.Features.StructureDesign.ExportDSTVBuilderActionTypes @endlink is an alias for @link ExportDSTVBuilder.ActionTypes NXOpen.Features.StructureDesign.ExportDSTVBuilder.ActionTypes@endlink
ExportDSTVBuilderActionTypes = ExportDSTVBuilder.ActionTypes


##  @link GrabTabBuilderAnchorPoints NXOpen.Features.StructureDesign.GrabTabBuilderAnchorPoints @endlink is an alias for @link GrabTabBuilder.AnchorPoints NXOpen.Features.StructureDesign.GrabTabBuilder.AnchorPoints@endlink
GrabTabBuilderAnchorPoints = GrabTabBuilder.AnchorPoints


##  @link GrabTabBuilderPlaceDirections NXOpen.Features.StructureDesign.GrabTabBuilderPlaceDirections @endlink is an alias for @link GrabTabBuilder.PlaceDirections NXOpen.Features.StructureDesign.GrabTabBuilder.PlaceDirections@endlink
GrabTabBuilderPlaceDirections = GrabTabBuilder.PlaceDirections


##  @link GussetBuilderAlignmentTypes NXOpen.Features.StructureDesign.GussetBuilderAlignmentTypes @endlink is an alias for @link GussetBuilder.AlignmentTypes NXOpen.Features.StructureDesign.GussetBuilder.AlignmentTypes@endlink
GussetBuilderAlignmentTypes = GussetBuilder.AlignmentTypes


##  @link GussetBuilderPositionTypes NXOpen.Features.StructureDesign.GussetBuilderPositionTypes @endlink is an alias for @link GussetBuilder.PositionTypes NXOpen.Features.StructureDesign.GussetBuilder.PositionTypes@endlink
GussetBuilderPositionTypes = GussetBuilder.PositionTypes


##  @link GussetBuilderThicknessTypes NXOpen.Features.StructureDesign.GussetBuilderThicknessTypes @endlink is an alias for @link GussetBuilder.ThicknessTypes NXOpen.Features.StructureDesign.GussetBuilder.ThicknessTypes@endlink
GussetBuilderThicknessTypes = GussetBuilder.ThicknessTypes


##  @link GussetConnectionBuilderJaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features.StructureDesign.GussetConnectionBuilderJaBoltedConnectionBuilderGussetconnectionreferenceface @endlink is an alias for @link GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface NXOpen.Features.StructureDesign.GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface@endlink
GussetConnectionBuilderJaBoltedConnectionBuilderGussetconnectionreferenceface = GussetConnectionBuilder.JaBoltedConnectionBuilderGussetconnectionreferenceface


##  @link HaunchBuilderPlacementMethods NXOpen.Features.StructureDesign.HaunchBuilderPlacementMethods @endlink is an alias for @link HaunchBuilder.PlacementMethods NXOpen.Features.StructureDesign.HaunchBuilder.PlacementMethods@endlink
HaunchBuilderPlacementMethods = HaunchBuilder.PlacementMethods


##  @link InheritStockBuilderStockObjectTypes NXOpen.Features.StructureDesign.InheritStockBuilderStockObjectTypes @endlink is an alias for @link InheritStockBuilder.StockObjectTypes NXOpen.Features.StructureDesign.InheritStockBuilder.StockObjectTypes@endlink
InheritStockBuilderStockObjectTypes = InheritStockBuilder.StockObjectTypes


##  @link MemberBuilderEndCornerTypes NXOpen.Features.StructureDesign.MemberBuilderEndCornerTypes @endlink is an alias for @link MemberBuilder.EndCornerTypes NXOpen.Features.StructureDesign.MemberBuilder.EndCornerTypes@endlink
MemberBuilderEndCornerTypes = MemberBuilder.EndCornerTypes


##  @link MemberPathBuilderMemberPathMethod NXOpen.Features.StructureDesign.MemberPathBuilderMemberPathMethod @endlink is an alias for @link MemberPathBuilder.MemberPathMethod NXOpen.Features.StructureDesign.MemberPathBuilder.MemberPathMethod@endlink
MemberPathBuilderMemberPathMethod = MemberPathBuilder.MemberPathMethod


##  @link PlateBuilderOffsetOptions NXOpen.Features.StructureDesign.PlateBuilderOffsetOptions @endlink is an alias for @link PlateBuilder.OffsetOptions NXOpen.Features.StructureDesign.PlateBuilder.OffsetOptions@endlink
PlateBuilderOffsetOptions = PlateBuilder.OffsetOptions


##  @link PlateStockBuilderThicknessDirs NXOpen.Features.StructureDesign.PlateStockBuilderThicknessDirs @endlink is an alias for @link PlateStockBuilder.ThicknessDirs NXOpen.Features.StructureDesign.PlateStockBuilder.ThicknessDirs@endlink
PlateStockBuilderThicknessDirs = PlateStockBuilder.ThicknessDirs


##  @link RuleBuilderButtOptions NXOpen.Features.StructureDesign.RuleBuilderButtOptions @endlink is an alias for @link RuleBuilder.ButtOptions NXOpen.Features.StructureDesign.RuleBuilder.ButtOptions@endlink
RuleBuilderButtOptions = RuleBuilder.ButtOptions


##  @link RuleBuilderCopeOptions NXOpen.Features.StructureDesign.RuleBuilderCopeOptions @endlink is an alias for @link RuleBuilder.CopeOptions NXOpen.Features.StructureDesign.RuleBuilder.CopeOptions@endlink
RuleBuilderCopeOptions = RuleBuilder.CopeOptions


##  @link RuleBuilderCornerTypes NXOpen.Features.StructureDesign.RuleBuilderCornerTypes @endlink is an alias for @link RuleBuilder.CornerTypes NXOpen.Features.StructureDesign.RuleBuilder.CornerTypes@endlink
RuleBuilderCornerTypes = RuleBuilder.CornerTypes


##  @link RuleBuilderPlacements NXOpen.Features.StructureDesign.RuleBuilderPlacements @endlink is an alias for @link RuleBuilder.Placements NXOpen.Features.StructureDesign.RuleBuilder.Placements@endlink
RuleBuilderPlacements = RuleBuilder.Placements


##  @link StiffenerBuilderAttachmentSides NXOpen.Features.StructureDesign.StiffenerBuilderAttachmentSides @endlink is an alias for @link StiffenerBuilder.AttachmentSides NXOpen.Features.StructureDesign.StiffenerBuilder.AttachmentSides@endlink
StiffenerBuilderAttachmentSides = StiffenerBuilder.AttachmentSides


##  @link StiffenerBuilderFillTypes NXOpen.Features.StructureDesign.StiffenerBuilderFillTypes @endlink is an alias for @link StiffenerBuilder.FillTypes NXOpen.Features.StructureDesign.StiffenerBuilder.FillTypes@endlink
StiffenerBuilderFillTypes = StiffenerBuilder.FillTypes


##  @link StiffenerBuilderHeightTypes NXOpen.Features.StructureDesign.StiffenerBuilderHeightTypes @endlink is an alias for @link StiffenerBuilder.HeightTypes NXOpen.Features.StructureDesign.StiffenerBuilder.HeightTypes@endlink
StiffenerBuilderHeightTypes = StiffenerBuilder.HeightTypes


##  @link StiffenerBuilderThicknessDirs NXOpen.Features.StructureDesign.StiffenerBuilderThicknessDirs @endlink is an alias for @link StiffenerBuilder.ThicknessDirs NXOpen.Features.StructureDesign.StiffenerBuilder.ThicknessDirs@endlink
StiffenerBuilderThicknessDirs = StiffenerBuilder.ThicknessDirs


##  @link SuperFrameBuilderBaseTypes NXOpen.Features.StructureDesign.SuperFrameBuilderBaseTypes @endlink is an alias for @link SuperFrameBuilder.BaseTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.BaseTypes@endlink
SuperFrameBuilderBaseTypes = SuperFrameBuilder.BaseTypes


##  @link SuperFrameBuilderInputModes NXOpen.Features.StructureDesign.SuperFrameBuilderInputModes @endlink is an alias for @link SuperFrameBuilder.InputModes NXOpen.Features.StructureDesign.SuperFrameBuilder.InputModes@endlink
SuperFrameBuilderInputModes = SuperFrameBuilder.InputModes


##  @link SuperFrameBuilderTransformTypes NXOpen.Features.StructureDesign.SuperFrameBuilderTransformTypes @endlink is an alias for @link SuperFrameBuilder.TransformTypes NXOpen.Features.StructureDesign.SuperFrameBuilder.TransformTypes@endlink
SuperFrameBuilderTransformTypes = SuperFrameBuilder.TransformTypes


