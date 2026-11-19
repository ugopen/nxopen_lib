from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link MoldCooling::AnalysisParams MoldCooling::AnalysisParams@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::MoldCooling::Manager::CreateAnalysisParamsBuilder  NXOpen::MoldCooling::Manager::CreateAnalysisParamsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConstantTimeStep.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## EndTime.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## FluidMeshResolution </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MeshResolution </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## MoldTemperature.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## NumTimeSteps </term> <description> 
##  
## 10 </description> </item> 
## 
## <item><term> 
##  
## PartTemperature.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## PhaseChangeActivation </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## SimulationType </term> <description> 
##  
## SteadyState </description> </item> 
## 
## <item><term> 
##  
## TargetTemperature.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## TimeStepOption </term> <description> 
##  
## Automatic </description> </item> 
## 
## <item><term> 
##  
## TransientTargetType </term> <description> 
##  
## EndTime </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class AnalysisParamsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>MoldCooling.AnalysisParams</ja_class> builder """


    ##  The type of thermal simulation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SteadyState</term><description> 
    ##  Steady State Simulation </description> </item><item><term> 
    ## Transient</term><description> 
    ##  Transient Simulation </description> </item></list>
    class SimulationTypeEnum(Enum):
        """
        Members Include: <SteadyState> <Transient>
        """
        SteadyState: int
        Transient: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisParamsBuilder.SimulationTypeEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The time step option 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Automatic</term><description> 
    ##  Use the default automatic time step option </description> </item><item><term> 
    ## NumSteps</term><description> 
    ##  Specify a number of time steps </description> </item><item><term> 
    ## Constant</term><description> 
    ##  Specify a constant time step value </description> </item></list>
    class TimeStepOptionEnum(Enum):
        """
        Members Include: <Automatic> <NumSteps> <Constant>
        """
        Automatic: int
        NumSteps: int
        Constant: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisParamsBuilder.TimeStepOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The target type of the transient simulation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EndTime</term><description> 
    ##  Stop after end-type is reached </description> </item><item><term> 
    ## Temperature</term><description> 
    ##  Stop when target temperature is reached </description> </item></list>
    class TransientTargetEnum(Enum):
        """
        Members Include: <EndTime> <Temperature>
        """
        EndTime: int
        Temperature: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnalysisParamsBuilder.TransientTargetEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConstantTimeStep
    ##  Returns the constant time step value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ConstantTimeStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ConstantTimeStep
         Returns the constant time step value   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndTime
    ##  Returns the end time for a transient simulation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndTime
         Returns the end time for a transient simulation   
            
         
        """
        pass
    
    ## Getter for property: (int) FluidMeshResolution
    ##  Returns the fluid mesh resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def FluidMeshResolution(self) -> int:
        """
        Getter for property: (int) FluidMeshResolution
         Returns the fluid mesh resolution   
            
         
        """
        pass
    
    ## Setter for property: (int) FluidMeshResolution

    ##  Returns the fluid mesh resolution   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FluidMeshResolution.setter
    def FluidMeshResolution(self, fluidMeshResolution: int):
        """
        Setter for property: (int) FluidMeshResolution
         Returns the fluid mesh resolution   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxEndTime
    ##  Returns the maximum end time for a temperature target transient simulation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxEndTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxEndTime
         Returns the maximum end time for a temperature target transient simulation   
            
         
        """
        pass
    
    ## Getter for property: (int) MeshResolution
    ##  Returns the mesh resolution   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def MeshResolution(self) -> int:
        """
        Getter for property: (int) MeshResolution
         Returns the mesh resolution   
            
         
        """
        pass
    
    ## Setter for property: (int) MeshResolution

    ##  Returns the mesh resolution   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @MeshResolution.setter
    def MeshResolution(self, meshResolution: int):
        """
        Setter for property: (int) MeshResolution
         Returns the mesh resolution   
            
         
        """
        pass
    
    ## Getter for property: (int) MeshSizeFactor
    ##  Returns the mesh size factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link JA_MOLD_COOLING_ANALYSIS_PARAMS_BUILDER_get_MeshResolution JA_MOLD_COOLING_ANALYSIS_PARAMS_BUILDER_get_MeshResolution@endlink  instead.  <br> 

    ## @return int
    @property
    def MeshSizeFactor(self) -> int:
        """
        Getter for property: (int) MeshSizeFactor
         Returns the mesh size factor   
            
         
        """
        pass
    
    ## Setter for property: (int) MeshSizeFactor

    ##  Returns the mesh size factor   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1953.0.0.  Use @link JA_MOLD_COOLING_ANALYSIS_PARAMS_BUILDER_set_MeshResolution JA_MOLD_COOLING_ANALYSIS_PARAMS_BUILDER_set_MeshResolution@endlink  instead.  <br> 

    @MeshSizeFactor.setter
    def MeshSizeFactor(self, meshSizeFactor: int):
        """
        Setter for property: (int) MeshSizeFactor
         Returns the mesh size factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MoldTemperature
    ##  Returns the initial mold temperature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MoldTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MoldTemperature
         Returns the initial mold temperature   
            
         
        """
        pass
    
    ## Getter for property: (int) NumTimeSteps
    ##  Returns the number of time steps   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return int
    @property
    def NumTimeSteps(self) -> int:
        """
        Getter for property: (int) NumTimeSteps
         Returns the number of time steps   
            
         
        """
        pass
    
    ## Setter for property: (int) NumTimeSteps

    ##  Returns the number of time steps   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @NumTimeSteps.setter
    def NumTimeSteps(self, numTimeSteps: int):
        """
        Setter for property: (int) NumTimeSteps
         Returns the number of time steps   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PartTemperature
    ##  Returns the initial part temperature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PartTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PartTemperature
         Returns the initial part temperature   
            
         
        """
        pass
    
    ## Getter for property: (bool) PhaseChangeActivation
    ##  Returns the phase change activation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def PhaseChangeActivation(self) -> bool:
        """
        Getter for property: (bool) PhaseChangeActivation
         Returns the phase change activation   
            
         
        """
        pass
    
    ## Setter for property: (bool) PhaseChangeActivation

    ##  Returns the phase change activation   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PhaseChangeActivation.setter
    def PhaseChangeActivation(self, phaseChangeActivation: bool):
        """
        Setter for property: (bool) PhaseChangeActivation
         Returns the phase change activation   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisParamsBuilder.SimulationTypeEnum NXOpen.MoldCooling.AnalysisParamsBuilder.SimulationTypeEnum@endlink) SimulationType
    ##  Returns the type of simulation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AnalysisParamsBuilder.SimulationTypeEnum
    @property
    def SimulationType(self) -> AnalysisParamsBuilder.SimulationTypeEnum:
        """
        Getter for property: (@link AnalysisParamsBuilder.SimulationTypeEnum NXOpen.MoldCooling.AnalysisParamsBuilder.SimulationTypeEnum@endlink) SimulationType
         Returns the type of simulation   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisParamsBuilder.SimulationTypeEnum NXOpen.MoldCooling.AnalysisParamsBuilder.SimulationTypeEnum@endlink) SimulationType

    ##  Returns the type of simulation   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SimulationType.setter
    def SimulationType(self, simulationType: AnalysisParamsBuilder.SimulationTypeEnum):
        """
        Setter for property: (@link AnalysisParamsBuilder.SimulationTypeEnum NXOpen.MoldCooling.AnalysisParamsBuilder.SimulationTypeEnum@endlink) SimulationType
         Returns the type of simulation   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TargetTemperature
    ##  Returns the temperature target for a transient simulation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TargetTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TargetTemperature
         Returns the temperature target for a transient simulation   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisParamsBuilder.TimeStepOptionEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TimeStepOptionEnum@endlink) TimeStepOption
    ##  Returns the time step option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return AnalysisParamsBuilder.TimeStepOptionEnum
    @property
    def TimeStepOption(self) -> AnalysisParamsBuilder.TimeStepOptionEnum:
        """
        Getter for property: (@link AnalysisParamsBuilder.TimeStepOptionEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TimeStepOptionEnum@endlink) TimeStepOption
         Returns the time step option   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisParamsBuilder.TimeStepOptionEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TimeStepOptionEnum@endlink) TimeStepOption

    ##  Returns the time step option   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TimeStepOption.setter
    def TimeStepOption(self, timeStepOption: AnalysisParamsBuilder.TimeStepOptionEnum):
        """
        Setter for property: (@link AnalysisParamsBuilder.TimeStepOptionEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TimeStepOptionEnum@endlink) TimeStepOption
         Returns the time step option   
            
         
        """
        pass
    
    ## Getter for property: (@link AnalysisParamsBuilder.TransientTargetEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TransientTargetEnum@endlink) TransientTargetType
    ##  Returns the target type of the transient simulation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AnalysisParamsBuilder.TransientTargetEnum
    @property
    def TransientTargetType(self) -> AnalysisParamsBuilder.TransientTargetEnum:
        """
        Getter for property: (@link AnalysisParamsBuilder.TransientTargetEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TransientTargetEnum@endlink) TransientTargetType
         Returns the target type of the transient simulation   
            
         
        """
        pass
    
    ## Setter for property: (@link AnalysisParamsBuilder.TransientTargetEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TransientTargetEnum@endlink) TransientTargetType

    ##  Returns the target type of the transient simulation   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @TransientTargetType.setter
    def TransientTargetType(self, transientTargetType: AnalysisParamsBuilder.TransientTargetEnum):
        """
        Setter for property: (@link AnalysisParamsBuilder.TransientTargetEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TransientTargetEnum@endlink) TransientTargetType
         Returns the target type of the transient simulation   
            
         
        """
        pass
    
import NXOpen
##  Encapsulates the various parameters needed for a mold cooling simulation  <br> To create or edit an instance of this class, use @link NXOpen::MoldCooling::AnalysisParamsBuilder  NXOpen::MoldCooling::AnalysisParamsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AnalysisParams(NXOpen.NXObject): 
    """ Encapsulates the various parameters needed for a mold cooling simulation """
    pass


import NXOpen
##  Represents a @link MoldCooling::Circuit MoldCooling::Circuit@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::MoldCooling::Manager::CreateCircuitBuilder  NXOpen::MoldCooling::Manager::CreateCircuitBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Diameter.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## RoughnessHeight.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## WallFriction </term> <description> 
##  
## Smooth </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class CircuitBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>MoldCooling.Circuit</ja_class> builder """


    ##  The type of thermal simulation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Smooth</term><description> 
    ##  Smooth     </description> </item><item><term> 
    ## Rough</term><description> 
    ##  Rough </description> </item></list>
    class WallFrictionType(Enum):
        """
        Members Include: <Smooth> <Rough>
        """
        Smooth: int
        Rough: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CircuitBuilder.WallFrictionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns the cooling circuit section diameter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
         Returns the cooling circuit section diameter   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) Inlets
    ##  Returns the cooling circuit inlets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def Inlets(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) Inlets
         Returns the cooling circuit inlets   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the cooling circuit name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the cooling circuit name   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) Outlets
    ##  Returns the cooling circuit outlets   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectPointList
    @property
    def Outlets(self) -> NXOpen.SelectPointList:
        """
        Getter for property: (@link NXOpen.SelectPointList NXOpen.SelectPointList@endlink) Outlets
         Returns the cooling circuit outlets   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Path
    ##  Returns the cooling circuit path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectCurveList
    @property
    def Path(self) -> NXOpen.SelectCurveList:
        """
        Getter for property: (@link NXOpen.SelectCurveList NXOpen.SelectCurveList@endlink) Path
         Returns the cooling circuit path   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RoughnessHeight
    ##  Returns the cooling circuit roughness height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RoughnessHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RoughnessHeight
         Returns the cooling circuit roughness height   
            
         
        """
        pass
    
    ## Getter for property: (@link CircuitBuilder.WallFrictionType NXOpen.MoldCooling.CircuitBuilder.WallFrictionType@endlink) WallFriction
    ##  Returns the cooling circuit wall friction type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return CircuitBuilder.WallFrictionType
    @property
    def WallFriction(self) -> CircuitBuilder.WallFrictionType:
        """
        Getter for property: (@link CircuitBuilder.WallFrictionType NXOpen.MoldCooling.CircuitBuilder.WallFrictionType@endlink) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
    
    ## Setter for property: (@link CircuitBuilder.WallFrictionType NXOpen.MoldCooling.CircuitBuilder.WallFrictionType@endlink) WallFriction

    ##  Returns the cooling circuit wall friction type   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @WallFriction.setter
    def WallFriction(self, wallFriction: CircuitBuilder.WallFrictionType):
        """
        Setter for property: (@link CircuitBuilder.WallFrictionType NXOpen.MoldCooling.CircuitBuilder.WallFrictionType@endlink) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents collection @link MoldCooling::Circuit MoldCooling::Circuit@endlink .  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::MoldCooling::Manager  NXOpen::MoldCooling::Manager @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class CircuitCollection(NXOpen.TaggedObjectCollection): 
    """ <summary> Represents collection <ja_class>MoldCooling.Circuit</ja_class>. </summary>"""


    ##  Finds a cooling circuit with the specified name 
    ##  @return found (@link Circuit NXOpen.MoldCooling.Circuit@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  Name of the circuit being looked for. </param>
    def FindObject(part: NXOpen.Part, name: str) -> Circuit:
        """
         Finds a cooling circuit with the specified name 
         @return found (@link Circuit NXOpen.MoldCooling.Circuit@endlink): .
        """
        pass
    
    ##  Returns the list of cooling circuits 
    ##  @return circuits (@link Circuit List[NXOpen.MoldCooling.Circuit]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def GetCircuits(part: NXOpen.Part) -> List[Circuit]:
        """
         Returns the list of cooling circuits 
         @return circuits (@link Circuit List[NXOpen.MoldCooling.Circuit]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a @link MoldCooling::CircuitParams MoldCooling::CircuitParams@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::MoldCooling::Manager::CreateCircuitParamsBuilder  NXOpen::MoldCooling::Manager::CreateCircuitParamsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## FlowMode </term> <description> 
##  
## VolumeFlowRate </description> </item> 
## 
## <item><term> 
##  
## InletStaticPressure.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## InletTemperature.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## InletVolumeFlowRate.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## OutletStaticPressure.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class CircuitParamsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>MoldCooling.CircuitParams</ja_class> builder """


    ##  The flow mode 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## VolumeFlowRate</term><description> 
    ## </description> </item><item><term> 
    ## StaticPressureGauge</term><description> 
    ## </description> </item></list>
    class FlowModeOption(Enum):
        """
        Members Include: <VolumeFlowRate> <StaticPressureGauge>
        """
        VolumeFlowRate: int
        StaticPressureGauge: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CircuitParamsBuilder.FlowModeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link CircuitParamsBuilder.FlowModeOption NXOpen.MoldCooling.CircuitParamsBuilder.FlowModeOption@endlink) FlowMode
    ##  Returns the flow mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return CircuitParamsBuilder.FlowModeOption
    @property
    def FlowMode(self) -> CircuitParamsBuilder.FlowModeOption:
        """
        Getter for property: (@link CircuitParamsBuilder.FlowModeOption NXOpen.MoldCooling.CircuitParamsBuilder.FlowModeOption@endlink) FlowMode
         Returns the flow mode   
            
         
        """
        pass
    
    ## Setter for property: (@link CircuitParamsBuilder.FlowModeOption NXOpen.MoldCooling.CircuitParamsBuilder.FlowModeOption@endlink) FlowMode

    ##  Returns the flow mode   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @FlowMode.setter
    def FlowMode(self, flowMode: CircuitParamsBuilder.FlowModeOption):
        """
        Setter for property: (@link CircuitParamsBuilder.FlowModeOption NXOpen.MoldCooling.CircuitParamsBuilder.FlowModeOption@endlink) FlowMode
         Returns the flow mode   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) FluidMaterial
    ##  Returns the fluid material   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def FluidMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) FluidMaterial
         Returns the fluid material   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) FluidMaterial

    ##  Returns the fluid material   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @FluidMaterial.setter
    def FluidMaterial(self, fluidMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) FluidMaterial
         Returns the fluid material   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InletStaticPressure
    ##  Returns the inlet static pressure   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InletStaticPressure(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InletStaticPressure
         Returns the inlet static pressure   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InletTemperature
    ##  Returns the inlet temperature   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InletTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InletTemperature
         Returns the inlet temperature   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InletVolumeFlowRate
    ##  Returns the inlet volume flow rate   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InletVolumeFlowRate(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InletVolumeFlowRate
         Returns the inlet volume flow rate   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name of the thermal parameter object   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name of the thermal parameter object   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name of the thermal parameter object   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name of the thermal parameter object   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OutletStaticPressure
    ##  Returns the outlet static pressure   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OutletStaticPressure(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OutletStaticPressure
         Returns the outlet static pressure   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents collection @link MoldCooling::CircuitParams MoldCooling::CircuitParams@endlink .  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::MoldCooling::Manager  NXOpen::MoldCooling::Manager @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class CircuitParamsCollection(NXOpen.TaggedObjectCollection): 
    """ <summary> Represents collection <ja_class>MoldCooling.CircuitParams</ja_class>. </summary>"""


    ##  Finds a cooling circuit fluid parameters set with the specified name 
    ##  @return found (@link CircuitParams NXOpen.MoldCooling.CircuitParams@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  Name of the cooling circuit fluid parameters set being looked for. </param>
    def FindObject(part: NXOpen.Part, name: str) -> CircuitParams:
        """
         Finds a cooling circuit fluid parameters set with the specified name 
         @return found (@link CircuitParams NXOpen.MoldCooling.CircuitParams@endlink): .
        """
        pass
    
    ##  Returns the list of cooling circuit fluid parameters 
    ##  @return params (@link CircuitParams List[NXOpen.MoldCooling.CircuitParams]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def GetParams(part: NXOpen.Part) -> List[CircuitParams]:
        """
         Returns the list of cooling circuit fluid parameters 
         @return params (@link CircuitParams List[NXOpen.MoldCooling.CircuitParams]@endlink): .
        """
        pass
    
import NXOpen
##  Encapsulates the various parameters needed for a mold cooling simulation  <br> To create or edit an instance of this class, use @link NXOpen::MoldCooling::CircuitParamsBuilder  NXOpen::MoldCooling::CircuitParamsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class CircuitParams(NXOpen.NXObject): 
    """ Encapsulates the various parameters needed for a mold cooling simulation """
    pass


import NXOpen
##  Represents a mold cooling circuit  <br> Circuit are created manually thru the MoldCooling.CircuitCollection interface  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Circuit(NXOpen.NXObject): 
    """ Represents a mold cooling circuit """


    ##  Assigns thermal parameters to the circuit. The circuit actually creates an internal reference
    ##             to the @link MoldCooling::CircuitParams MoldCooling::CircuitParams@endlink  object and you can assign the same 
    ##             parameter set to more than one circuit. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ## <param name="params"> (@link CircuitParams NXOpen.MoldCooling.CircuitParams@endlink) </param>
    def AssignParams(self, params: CircuitParams) -> None:
        """
         Assigns thermal parameters to the circuit. The circuit actually creates an internal reference
                    to the @link MoldCooling::CircuitParams MoldCooling::CircuitParams@endlink  object and you can assign the same 
                    parameter set to more than one circuit. 
        """
        pass
    
    ##  Returns the @link MoldCooling::CircuitParams MoldCooling::CircuitParams@endlink  object assigned to that cooling circuit 
    ##  @return params (@link CircuitParams NXOpen.MoldCooling.CircuitParams@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    def GetAssignedParams(self) -> CircuitParams:
        """
         Returns the @link MoldCooling::CircuitParams MoldCooling::CircuitParams@endlink  object assigned to that cooling circuit 
         @return params (@link CircuitParams NXOpen.MoldCooling.CircuitParams@endlink): .
        """
        pass
    
import NXOpen
##  Represents a @link MoldCooling::Circuit MoldCooling::Circuit@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::MoldCooling::Manager::CreateFlowCircuitBuilder  NXOpen::MoldCooling::Manager::CreateFlowCircuitBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## RoughnessHeight.Value </term> <description> 
##  
## 0 (millimeters part), 0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## WallFriction </term> <description> 
##  
## Smooth </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class FlowCircuitBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>MoldCooling.Circuit</ja_class> builder """


    ##  The type of thermal simulation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Smooth</term><description> 
    ##  Smooth </description> </item><item><term> 
    ## Rough</term><description> 
    ##  Rough </description> </item></list>
    class WallFrictionType(Enum):
        """
        Members Include: <Smooth> <Rough>
        """
        Smooth: int
        Rough: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlowCircuitBuilder.WallFrictionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) CircuitBodies
    ##  Returns the cooling circuit channel bodies   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def CircuitBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) CircuitBodies
         Returns the cooling circuit channel bodies   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectFaceList NXOpen.SelectFaceList@endlink) Inlets
    ##  Returns the cooling circuit inlet faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectFaceList
    @property
    def Inlets(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: (@link NXOpen.SelectFaceList NXOpen.SelectFaceList@endlink) Inlets
         Returns the cooling circuit inlet faces   
            
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the cooling circuit name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the cooling circuit name   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the cooling circuit name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectFaceList NXOpen.SelectFaceList@endlink) Outlets
    ##  Returns the cooling circuit outlet faces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectFaceList
    @property
    def Outlets(self) -> NXOpen.SelectFaceList:
        """
        Getter for property: (@link NXOpen.SelectFaceList NXOpen.SelectFaceList@endlink) Outlets
         Returns the cooling circuit outlet faces   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RoughnessHeight
    ##  Returns the cooling circuit roughness height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RoughnessHeight(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RoughnessHeight
         Returns the cooling circuit roughness height   
            
         
        """
        pass
    
    ## Getter for property: (@link FlowCircuitBuilder.WallFrictionType NXOpen.MoldCooling.FlowCircuitBuilder.WallFrictionType@endlink) WallFriction
    ##  Returns the cooling circuit wall friction type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return FlowCircuitBuilder.WallFrictionType
    @property
    def WallFriction(self) -> FlowCircuitBuilder.WallFrictionType:
        """
        Getter for property: (@link FlowCircuitBuilder.WallFrictionType NXOpen.MoldCooling.FlowCircuitBuilder.WallFrictionType@endlink) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
    
    ## Setter for property: (@link FlowCircuitBuilder.WallFrictionType NXOpen.MoldCooling.FlowCircuitBuilder.WallFrictionType@endlink) WallFriction

    ##  Returns the cooling circuit wall friction type   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @WallFriction.setter
    def WallFriction(self, wallFriction: FlowCircuitBuilder.WallFrictionType):
        """
        Setter for property: (@link FlowCircuitBuilder.WallFrictionType NXOpen.MoldCooling.FlowCircuitBuilder.WallFrictionType@endlink) WallFriction
         Returns the cooling circuit wall friction type   
            
         
        """
        pass
    
import NXOpen
##   Manager class for the mold cooling application. This is the main entry point to access and create mold cooling objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Manager(NXOpen.Object): 
    """  Manager class for the mold cooling application. This is the main entry point to access and create mold cooling objects. """


    ##  The type of thermal simulation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Thermal</term><description> 
    ##  Thermal Mold Cooling Analysis Context </description> </item><item><term> 
    ## Flow</term><description> 
    ##  Coupled Thermal-Flow Mold Cooling Analysis Context </description> </item></list>
    class AnalysisContext(Enum):
        """
        Members Include: <Thermal> <Flow>
        """
        Thermal: int
        Flow: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Manager.AnalysisContext:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns cooling circuits collection 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @link CircuitCollection NXOpen.MoldCooling.CircuitCollection@endlink
    @property
    def Circuits() -> CircuitCollection:
        """
         Returns cooling circuits collection 
        """
        pass
    
    ##  Returns cooling circuits collection 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @link CircuitParamsCollection NXOpen.MoldCooling.CircuitParamsCollection@endlink
    @property
    def CircuitFluidParams() -> CircuitParamsCollection:
        """
         Returns cooling circuits collection 
        """
        pass
    
    ##  Creates a @link NXOpen::MoldCooling::AnalysisParamsBuilder NXOpen::MoldCooling::AnalysisParamsBuilder@endlink . 
    ##  @return builder (@link AnalysisParamsBuilder NXOpen.MoldCooling.AnalysisParamsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="params"> (@link AnalysisParams NXOpen.MoldCooling.AnalysisParams@endlink) </param>
    def CreateAnalysisParamsBuilder(part: NXOpen.Part, params: AnalysisParams) -> AnalysisParamsBuilder:
        """
         Creates a @link NXOpen::MoldCooling::AnalysisParamsBuilder NXOpen::MoldCooling::AnalysisParamsBuilder@endlink . 
         @return builder (@link AnalysisParamsBuilder NXOpen.MoldCooling.AnalysisParamsBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::MoldCooling::CircuitBuilder NXOpen::MoldCooling::CircuitBuilder@endlink . 
    ##  @return builder (@link CircuitBuilder NXOpen.MoldCooling.CircuitBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="circuit"> (@link Circuit NXOpen.MoldCooling.Circuit@endlink) </param>
    def CreateCircuitBuilder(part: NXOpen.Part, circuit: Circuit) -> CircuitBuilder:
        """
         Creates a @link NXOpen::MoldCooling::CircuitBuilder NXOpen::MoldCooling::CircuitBuilder@endlink . 
         @return builder (@link CircuitBuilder NXOpen.MoldCooling.CircuitBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::MoldCooling::CircuitParamsBuilder NXOpen::MoldCooling::CircuitParamsBuilder@endlink . 
    ##  @return builder (@link CircuitParamsBuilder NXOpen.MoldCooling.CircuitParamsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="params"> (@link CircuitParams NXOpen.MoldCooling.CircuitParams@endlink) </param>
    def CreateCircuitParamsBuilder(part: NXOpen.Part, params: CircuitParams) -> CircuitParamsBuilder:
        """
         Creates a @link NXOpen::MoldCooling::CircuitParamsBuilder NXOpen::MoldCooling::CircuitParamsBuilder@endlink . 
         @return builder (@link CircuitParamsBuilder NXOpen.MoldCooling.CircuitParamsBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::MoldCooling::FlowCircuitBuilder NXOpen::MoldCooling::FlowCircuitBuilder@endlink . 
    ##  @return builder (@link FlowCircuitBuilder NXOpen.MoldCooling.FlowCircuitBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="circuit"> (@link Circuit NXOpen.MoldCooling.Circuit@endlink) </param>
    def CreateFlowCircuitBuilder(part: NXOpen.Part, circuit: Circuit) -> FlowCircuitBuilder:
        """
         Creates a @link NXOpen::MoldCooling::FlowCircuitBuilder NXOpen::MoldCooling::FlowCircuitBuilder@endlink . 
         @return builder (@link FlowCircuitBuilder NXOpen.MoldCooling.FlowCircuitBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::MoldCooling::MoldBodyBuilder NXOpen::MoldCooling::MoldBodyBuilder@endlink . 
    ##  @return builder (@link MoldBodyBuilder NXOpen.MoldCooling.MoldBodyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="mold"> (@link MoldBody NXOpen.MoldCooling.MoldBody@endlink) </param>
    def CreateMoldBodyBuilder(part: NXOpen.Part, mold: MoldBody) -> MoldBodyBuilder:
        """
         Creates a @link NXOpen::MoldCooling::MoldBodyBuilder NXOpen::MoldCooling::MoldBodyBuilder@endlink . 
         @return builder (@link MoldBodyBuilder NXOpen.MoldCooling.MoldBodyBuilder@endlink): .
        """
        pass
    
    ##  Deletes the selected cooling circuit 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="circuit"> (@link Circuit NXOpen.MoldCooling.Circuit@endlink) </param>
    def DeleteCircuit(part: NXOpen.Part, circuit: Circuit) -> None:
        """
         Deletes the selected cooling circuit 
        """
        pass
    
    ##  Deletes the selected cooling circuit fluid parameters 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="params"> (@link CircuitParams NXOpen.MoldCooling.CircuitParams@endlink) </param>
    def DeleteCircuitParams(part: NXOpen.Part, params: CircuitParams) -> None:
        """
         Deletes the selected cooling circuit fluid parameters 
        """
        pass
    
    ##  Finds the @link NXOpen::MoldCooling::AnalysisParams NXOpen::MoldCooling::AnalysisParams@endlink  stored in the part, or NULL if it hasn't been created yet. 
    ##  @return params (@link AnalysisParams NXOpen.MoldCooling.AnalysisParams@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def FindAnalysisParams(part: NXOpen.Part) -> AnalysisParams:
        """
         Finds the @link NXOpen::MoldCooling::AnalysisParams NXOpen::MoldCooling::AnalysisParams@endlink  stored in the part, or NULL if it hasn't been created yet. 
         @return params (@link AnalysisParams NXOpen.MoldCooling.AnalysisParams@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::MoldCooling::MoldBody NXOpen::MoldCooling::MoldBody@endlink  stored in the part, or NULL if it hasn't been created yet. 
    ##  @return mold (@link MoldBody NXOpen.MoldCooling.MoldBody@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def FindMoldBody(part: NXOpen.Part) -> MoldBody:
        """
         Finds the @link NXOpen::MoldCooling::MoldBody NXOpen::MoldCooling::MoldBody@endlink  stored in the part, or NULL if it hasn't been created yet. 
         @return mold (@link MoldBody NXOpen.MoldCooling.MoldBody@endlink): .
        """
        pass
    
    ##  Finds the @link NXOpen::MoldCooling::SolverOptions NXOpen::MoldCooling::SolverOptions@endlink  stored in the part. 
    ##  @return options (@link SolverOptions NXOpen.MoldCooling.SolverOptions@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def FindSolverOptions(part: NXOpen.Part) -> SolverOptions:
        """
         Finds the @link NXOpen::MoldCooling::SolverOptions NXOpen::MoldCooling::SolverOptions@endlink  stored in the part. 
         @return options (@link SolverOptions NXOpen.MoldCooling.SolverOptions@endlink): .
        """
        pass
    
    ##  Returns the mold cooling analysis context for the given part. 
    ##  @return context (@link Manager.AnalysisContext NXOpen.MoldCooling.Manager.AnalysisContext@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def GetAnalysisContext(part: NXOpen.Part) -> Manager.AnalysisContext:
        """
         Returns the mold cooling analysis context for the given part. 
         @return context (@link Manager.AnalysisContext NXOpen.MoldCooling.Manager.AnalysisContext@endlink): .
        """
        pass
    
    ##  Import mold wizard cooling circuits 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def ImportMoldWizardCircuits(part: NXOpen.Part) -> None:
        """
         Import mold wizard cooling circuits 
        """
        pass
    
    ##  Runs the mold cooling thermal simulation. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def RunSimulation(part: NXOpen.Part) -> None:
        """
         Runs the mold cooling thermal simulation. 
        """
        pass
    
    ##  Internally Runs the mold cooling thermal simulation. This method should not be called in an NXOpen program,
    ##         * it is meant to be used internally only.
    ##         
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="logfile"> (str) </param>
    def RunSimulationInternal(part: NXOpen.Part, logfile: str) -> None:
        """
         Internally Runs the mold cooling thermal simulation. This method should not be called in an NXOpen program,
                * it is meant to be used internally only.
                
        """
        pass
    
    ##  Changes the mold cooling analysis context for the given part. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="context"> (@link Manager.AnalysisContext NXOpen.MoldCooling.Manager.AnalysisContext@endlink) </param>
    def SetAnalysisContext(part: NXOpen.Part, context: Manager.AnalysisContext) -> None:
        """
         Changes the mold cooling analysis context for the given part. 
        """
        pass
    
import NXOpen
##  Represents a @link MoldCooling::MoldBodyBuilder MoldCooling::MoldBodyBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::MoldCooling::Manager::CreateMoldBodyBuilder  NXOpen::MoldCooling::Manager::CreateMoldBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MoldBodyBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>MoldCooling.MoldBodyBuilder</ja_class> builder """


    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CavityMaterial
    ##  Returns the selected material for the mold cavity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def CavityMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CavityMaterial
         Returns the selected material for the mold cavity   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CavityMaterial

    ##  Returns the selected material for the mold cavity   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CavityMaterial.setter
    def CavityMaterial(self, cavityMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CavityMaterial
         Returns the selected material for the mold cavity   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CoreMaterial
    ##  Returns the selected material for the mold core   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def CoreMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CoreMaterial
         Returns the selected material for the mold core   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CoreMaterial

    ##  Returns the selected material for the mold core   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CoreMaterial.setter
    def CoreMaterial(self, coreMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) CoreMaterial
         Returns the selected material for the mold core   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) PartMaterial
    ##  Returns the selected material for the mold part   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.PhysicalMaterial
    @property
    def PartMaterial(self) -> NXOpen.PhysicalMaterial:
        """
        Getter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) PartMaterial
         Returns the selected material for the mold part   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) PartMaterial

    ##  Returns the selected material for the mold part   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PartMaterial.setter
    def PartMaterial(self, partMaterial: NXOpen.PhysicalMaterial):
        """
        Setter for property: (@link NXOpen.PhysicalMaterial NXOpen.PhysicalMaterial@endlink) PartMaterial
         Returns the selected material for the mold part   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) SelectCavityBodies
    ##  Returns the cavity bodies selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def SelectCavityBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) SelectCavityBodies
         Returns the cavity bodies selection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) SelectCoreBodies
    ##  Returns the core bodies selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def SelectCoreBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) SelectCoreBodies
         Returns the core bodies selection   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) SelectPartBodies
    ##  Returns the part bodies selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def SelectPartBodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) SelectPartBodies
         Returns the part bodies selection   
            
         
        """
        pass
    
import NXOpen
##  Represents mold body that is to be modeled in a mold cooling simulation  <br> To create or edit an instance of this class, use @link NXOpen::MoldCooling::MoldBodyBuilder  NXOpen::MoldCooling::MoldBodyBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class MoldBody(NXOpen.NXObject): 
    """ Represents mold body that is to be modeled in a mold cooling simulation """
    pass


import NXOpen
##  Represents the solver options for the mold cooling analysis  <br> No Creator.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class SolverOptions(NXOpen.NXObject): 
    """ Represents the solver options for the mold cooling analysis """


    ## Getter for property: (bool) KeepAllFiles
    ##  Returns the option to keep all analysis generated files   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def KeepAllFiles(self) -> bool:
        """
        Getter for property: (bool) KeepAllFiles
         Returns the option to keep all analysis generated files   
            
         
        """
        pass
    
    ## Setter for property: (bool) KeepAllFiles

    ##  Returns the option to keep all analysis generated files   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @KeepAllFiles.setter
    def KeepAllFiles(self, keepAllFiles: bool):
        """
        Setter for property: (bool) KeepAllFiles
         Returns the option to keep all analysis generated files   
            
         
        """
        pass
    
    ## Getter for property: (int) NumProcessors
    ##  Returns the number of processors to use for the parallel run   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return int
    @property
    def NumProcessors(self) -> int:
        """
        Getter for property: (int) NumProcessors
         Returns the number of processors to use for the parallel run   
            
         
        """
        pass
    
    ## Setter for property: (int) NumProcessors

    ##  Returns the number of processors to use for the parallel run   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @NumProcessors.setter
    def NumProcessors(self, numProcessors: int):
        """
        Setter for property: (int) NumProcessors
         Returns the number of processors to use for the parallel run   
            
         
        """
        pass
    
    ## Getter for property: (bool) ParallelRun
    ##  Returns the option to run the analysis in parallel   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def ParallelRun(self) -> bool:
        """
        Getter for property: (bool) ParallelRun
         Returns the option to run the analysis in parallel   
            
         
        """
        pass
    
    ## Setter for property: (bool) ParallelRun

    ##  Returns the option to run the analysis in parallel   
    ##     
    ##  
    ## Setter License requirements: nx_mold_cool_basic (" NX Mold Cooling Application")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ParallelRun.setter
    def ParallelRun(self, parallelRun: bool):
        """
        Setter for property: (bool) ParallelRun
         Returns the option to run the analysis in parallel   
            
         
        """
        pass
    
## @package NXOpen.MoldCooling
## Classes, Enums and Structs under NXOpen.MoldCooling namespace

##  @link AnalysisParamsBuilderSimulationTypeEnum NXOpen.MoldCooling.AnalysisParamsBuilderSimulationTypeEnum @endlink is an alias for @link AnalysisParamsBuilder.SimulationTypeEnum NXOpen.MoldCooling.AnalysisParamsBuilder.SimulationTypeEnum@endlink
AnalysisParamsBuilderSimulationTypeEnum = AnalysisParamsBuilder.SimulationTypeEnum


##  @link AnalysisParamsBuilderTimeStepOptionEnum NXOpen.MoldCooling.AnalysisParamsBuilderTimeStepOptionEnum @endlink is an alias for @link AnalysisParamsBuilder.TimeStepOptionEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TimeStepOptionEnum@endlink
AnalysisParamsBuilderTimeStepOptionEnum = AnalysisParamsBuilder.TimeStepOptionEnum


##  @link AnalysisParamsBuilderTransientTargetEnum NXOpen.MoldCooling.AnalysisParamsBuilderTransientTargetEnum @endlink is an alias for @link AnalysisParamsBuilder.TransientTargetEnum NXOpen.MoldCooling.AnalysisParamsBuilder.TransientTargetEnum@endlink
AnalysisParamsBuilderTransientTargetEnum = AnalysisParamsBuilder.TransientTargetEnum


##  @link CircuitBuilderWallFrictionType NXOpen.MoldCooling.CircuitBuilderWallFrictionType @endlink is an alias for @link CircuitBuilder.WallFrictionType NXOpen.MoldCooling.CircuitBuilder.WallFrictionType@endlink
CircuitBuilderWallFrictionType = CircuitBuilder.WallFrictionType


##  @link CircuitParamsBuilderFlowModeOption NXOpen.MoldCooling.CircuitParamsBuilderFlowModeOption @endlink is an alias for @link CircuitParamsBuilder.FlowModeOption NXOpen.MoldCooling.CircuitParamsBuilder.FlowModeOption@endlink
CircuitParamsBuilderFlowModeOption = CircuitParamsBuilder.FlowModeOption


##  @link FlowCircuitBuilderWallFrictionType NXOpen.MoldCooling.FlowCircuitBuilderWallFrictionType @endlink is an alias for @link FlowCircuitBuilder.WallFrictionType NXOpen.MoldCooling.FlowCircuitBuilder.WallFrictionType@endlink
FlowCircuitBuilderWallFrictionType = FlowCircuitBuilder.WallFrictionType


##  @link ManagerAnalysisContext NXOpen.MoldCooling.ManagerAnalysisContext @endlink is an alias for @link Manager.AnalysisContext NXOpen.MoldCooling.Manager.AnalysisContext@endlink
ManagerAnalysisContext = Manager.AnalysisContext


