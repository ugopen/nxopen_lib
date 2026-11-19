from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen.Fields
class DynaFieldApplication(NXOpen.Fields.IApplication): 
    """ Implementation of the NXOpen.Fields.IApplication. 
    This application extends fields with solver specific attributes."""
    def CreateAttributes(self, loadCurveUsage: DynaFieldAttributes.LoadCurveUsage, dataType: DynaFieldAttributes.DataType, numDiscPts: int) -> DynaFieldAttributes:
        """
         Creates a new set of attributes that can be attached to a field. 
                See NXOpen.PhysMat.DynaFieldAttributes for more information about
                these attributes.
         Returns attributes ( DynaFieldAttributes NXOpen): .
        """
        pass
import NXOpen
import NXOpen.Fields
class DynaFieldAttributes(NXOpen.NXObject): 
    """ Implementation of the NXOpen.Fields.IApplicationData. 
    This specific implementation extends fields with solver specific attributes.
    Instances of this class are created through the NXOpen.PhysMat.DynaFieldApplication object."""
    class DataType(Enum):
        """
        Members Include: 
         |ChemicalShrinkage| 
         |FabricStress| 
         |General| 
         |GeneralXY| 
         |GeneralRS| 

        """
        ChemicalShrinkage: int
        FabricStress: int
        General: int
        GeneralXY: int
        GeneralRS: int
        @staticmethod
        def ValueOf(value: int) -> DynaFieldAttributes.DataType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LoadCurveUsage(Enum):
        """
        Members Include: 
         |NormalAnalysisPhase| 
         |DynamicRelaxationPhase| 
         |BothPhases| 

        """
        NormalAnalysisPhase: int
        DynamicRelaxationPhase: int
        BothPhases: int
        @staticmethod
        def ValueOf(value: int) -> DynaFieldAttributes.LoadCurveUsage:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DataTypeAttribute(self) -> DynaFieldAttributes.DataType:
        """
        Getter for property: ( DynaFieldAttributes.DataType NXOpen) DataTypeAttribute
         Returns a data type attribute.  
            
         
        """
        pass
    @DataTypeAttribute.setter
    def DataTypeAttribute(self, dataType: DynaFieldAttributes.DataType):
        """
        Setter for property: ( DynaFieldAttributes.DataType NXOpen) DataTypeAttribute
         Returns a data type attribute.  
            
         
        """
        pass
    @property
    def LoadCurveUsageAttribute(self) -> DynaFieldAttributes.LoadCurveUsage:
        """
        Getter for property: ( DynaFieldAttributes.LoadCurveUsage NXOpen) LoadCurveUsageAttribute
         Returns a load curve usage attribute.  
            
         
        """
        pass
    @LoadCurveUsageAttribute.setter
    def LoadCurveUsageAttribute(self, loadCurveUsage: DynaFieldAttributes.LoadCurveUsage):
        """
        Setter for property: ( DynaFieldAttributes.LoadCurveUsage NXOpen) LoadCurveUsageAttribute
         Returns a load curve usage attribute.  
            
         
        """
        pass
    @property
    def NumDiscretizationPointsAttribute(self) -> int:
        """
        Getter for property: (int) NumDiscretizationPointsAttribute
         Returns the number of discretization points.  
            
         
        """
        pass
    @NumDiscretizationPointsAttribute.setter
    def NumDiscretizationPointsAttribute(self, numDiscPts: int):
        """
        Setter for property: (int) NumDiscretizationPointsAttribute
         Returns the number of discretization points.  
            
         
        """
        pass
import NXOpen
class PhysicalMaterialAssignBuilder(NXOpen.Builder): 
    """ Represents a Physical Material Assign Builder """
    pass
import NXOpen
class PhysicalMaterialLibMgrBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.PhysMat.PhysicalMaterialLibMgrBuilder builder """
    pass
import NXOpen
class PhysicalMaterialListBuilder(NXOpen.Builder): 
    """ This builder is used by the Materials list component that allows copying, editing, deleting. etc.
     materials.
    """
    pass
