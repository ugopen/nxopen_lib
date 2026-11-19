from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   @brief  ABB context is passed to the ABB implementation. 
##                   It contains methods to log messages   
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class AbbContext(NXOpen.NXObject): 
    """ <summary> ABB context is passed to the ABB implementation. 
                  It contains methods to log messages  </summary> """


    ## 
    ##             ABB call type
    ##         
    ##  ABB call type 
    class CallType(Enum):
        """
        Members Include: <Abb> <Method>
        """
        Abb: int
        Method: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AbbContext.CallType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Get the call type of the ABB 
    ##  @return call_type (@link AbbContext.CallType NXOpen.CAE.AeroStructures.Author.AbbContext.CallType@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCallType(context: AbbContext) -> AbbContext.CallType:
        """
         Get the call type of the ABB 
         @return call_type (@link AbbContext.CallType NXOpen.CAE.AeroStructures.Author.AbbContext.CallType@endlink): .
        """
        pass
    
    ##  Get the failure mode of the ABB
    ##  @return fm (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetFailureMode(context: AbbContext) -> str:
        """
         Get the failure mode of the ABB
         @return fm (str): .
        """
        pass
    
    ##  Returns the list of load case indexes passed to the ABB 
    ##  @return indexes (List[int]):  list of indexes .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLoadCaseIndexes(context: AbbContext) -> List[int]:
        """
         Returns the list of load case indexes passed to the ABB 
         @return indexes (List[int]):  list of indexes .
        """
        pass
    
    ##  Set the call type of the ABB 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="call_type"> (@link AbbContext.CallType NXOpen.CAE.AeroStructures.Author.AbbContext.CallType@endlink) </param>
    def SetCallType(context: AbbContext, call_type: AbbContext.CallType) -> None:
        """
         Set the call type of the ABB 
        """
        pass
    
    ##  Set the failure mode of the ABB
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="fm"> (str) </param>
    def SetFailureMode(context: AbbContext, fm: str) -> None:
        """
         Set the failure mode of the ABB
        """
        pass
    
    ##  Sets the list of load case indexes passed to the ABB 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ##  list of indexes 
    def SetLoadCaseIndexes(context: AbbContext, indexes: List[int]) -> None:
        """
         Sets the list of load case indexes passed to the ABB 
        """
        pass
    
import NXOpen
import NXOpen.CAE.AeroStructures
##  Represents a AeroStruct application building block (ABB)  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ABB(NXOpen.Object): 
    """ Represents a AeroStruct application building block (ABB) """


    ## 
    ##                     Support along the edges, the choice is between SimplySupported and Clamped
    ##                 
    ##  Simply Supported 
    class EdgeSupportType(Enum):
        """
        Members Include: <SimplySupported> <Clamped>
        """
        SimplySupported: int
        Clamped: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ABB.EdgeSupportType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##                     Material behaivour type, the choices are: {Elastic, Elastic-plastic}
    ##                 
    ##  Elastic behaviour 
    class MaterialBehaviour(Enum):
        """
        Members Include: <Elastic> <ElasticPlastic>
        """
        Elastic: int
        ElasticPlastic: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ABB.MaterialBehaviour:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##                     Plane stress boundary conditions, the choices are: {SSSS, SCSC, CCCC, SFSS}
    ##                 
    ##  loaded edges: simply supported, unloaded edges: simply supported - simply supported 
    class PlaneStressBoundaryConditions(Enum):
        """
        Members Include: <Ssss> <Cscs> <Scsc> <Cccc> <Sfss>
        """
        Ssss: int
        Cscs: int
        Scsc: int
        Cccc: int
        Sfss: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ABB.PlaneStressBoundaryConditions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##                     ABB return status
    ##                 
    ##  ABB computation success 
    class Status(Enum):
        """
        Members Include: <Success> <Failed>
        """
        Success: int
        Failed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ABB.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##                     Support along unloaded edges, the choices are: {Clamped-Clamped, Simply Supported-Clamped, Simply Supported-Simply Supported, Free-Clamped, Free-Simply Supported}
    ##                 
    ##  Clamped-Clamped 
    class UnloadedEdgeSupportType(Enum):
        """
        Members Include: <ClampedClamped> <SimplySupportedClamped> <SimplySupportedSimplySupported> <FreeClamped> <FreeSimplySupported>
        """
        ClampedClamped: int
        SimplySupportedClamped: int
        SimplySupportedSimplySupported: int
        FreeClamped: int
        FreeSimplySupported: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ABB.UnloadedEdgeSupportType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##                     Curves for finding 'kc' the compressive-buckling coefficient for curved sheet panel
    ## 
    ##                     This curve is extracted from Bruhn manual, figure C9.1
    ##                     Used for finding 'kc' the compressive-buckling coefficient for curved sheet panel, with
    ##                     simply-supported edges.
    ## 
    ##                     Input
    ##                         b   shorter panel dimension
    ##                         t   thickness
    ##                         r   radius
    ##                         nu  Poisson's ratio
    ##                     Output
    ##                         kc  compressive-buckling coefficient
    ##                     Returns
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, kc). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - kc is: float. Compressive-buckling coefficient .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def CurvedMetallicPanelCompressiveBucklingCoefficient(abbContext: AbbContext, b: float, t: float, r: float, nu: float) -> Tuple[ABB.Status, float]:
        """
        
                            Curves for finding 'kc' the compressive-buckling coefficient for curved sheet panel
        
                            This curve is extracted from Bruhn manual, figure C9.1
                            Used for finding 'kc' the compressive-buckling coefficient for curved sheet panel, with
                            simply-supported edges.
        
                            Input
                                b   shorter panel dimension
                                t   thickness
                                r   radius
                                nu  Poisson's ratio
                            Output
                                kc  compressive-buckling coefficient
                            Returns
                                Status of the calculation
                        
         @return A tuple consisting of (status, kc). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - kc is: float. Compressive-buckling coefficient .

        """
        pass
    
    ## 
    ##                     Curves for finding 'ks' the shear-buckling coefficient for curved sheet panel
    ## 
    ##                     These curves are extracted from Bruhn manual, figures C9.2 to C9.5
    ##                     Used for finding 'ks' the shear-buckling coefficient for curved sheet panel, with
    ##                     simply-supported or clamped edges.
    ## 
    ##                     Input
    ##                         a   Dimension in longitudinal axis
    ##                         b   Dimension in radial axis
    ##                         t   Thickness
    ##                         r   Radius
    ##                         nu  Poisson's ratio
    ##                         BC  Support along the edges, the choice is between SimplySupported and Clamped
    ##                     Output
    ##                         ks  Shear-buckling coefficient
    ##                     Returns
    ##                         False if input values are out of bounds
    ##                 
    ##  @return A tuple consisting of (status, ks). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - ks is: float. Compressive-buckling coefficient .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def CurvedMetallicPanelShearBucklingCoefficient(abbContext: AbbContext, a: float, b: float, t: float, r: float, nu: float, bc: ABB.EdgeSupportType) -> Tuple[ABB.Status, float]:
        """
        
                            Curves for finding 'ks' the shear-buckling coefficient for curved sheet panel
        
                            These curves are extracted from Bruhn manual, figures C9.2 to C9.5
                            Used for finding 'ks' the shear-buckling coefficient for curved sheet panel, with
                            simply-supported or clamped edges.
        
                            Input
                                a   Dimension in longitudinal axis
                                b   Dimension in radial axis
                                t   Thickness
                                r   Radius
                                nu  Poisson's ratio
                                BC  Support along the edges, the choice is between SimplySupported and Clamped
                            Output
                                ks  Shear-buckling coefficient
                            Returns
                                False if input values are out of bounds
                        
         @return A tuple consisting of (status, ks). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - ks is: float. Compressive-buckling coefficient .

        """
        pass
    
    ## 
    ##                     Compute equivalent section properties (area, center of gravity, Young's modulus and inertia) of a profile composed of different sub-sections.
    ## 
    ##                     Input
    ##                         n Number of sub-sections that compose the section
    ##                         Ai Areas of sub-sections                        
    ##                         Ei Young's modulus of sub-sections
    ##                         Ycogi Center of gravity of sub-sections in Y direction
    ##                         Ixxi Moments of inertia (Quadratic moments) of sub-sections around XX (expressed at the center of gravity of each sub-section)
    ##                     Output
    ##                         A Area of the equivalent section (sum of all sub-sections)
    ##                         E Young's modulus of the equivalent section
    ##                         Ycog Center of gravity of the equivalent section in Y direction
    ##                         Ixx Moment of inertia of the equivalent section around XX (expressed at the center of gravity of the equivalent section)
    ##                 
    ##  @return A tuple consisting of (status, A, oYcog, E, oIxx). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - A is: List[float]. Area of the equivalent section (sum of all sub-sections) .
    ##  - oYcog is: List[float]. Center of gravity of the equivalent section in Y direction .
    ##  - E is: List[float]. Young's modulus of the equivalent section .
    ##  - oIxx is: List[float]. Moment of inertia of the equivalent section around XX (expressed at the center of gravity of the equivalent section) .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def EquivalentSectionProperties(abbContext: AbbContext, iAi: List[float], iYcog: List[float], iEi: List[float], iIxxi: List[float]) -> Tuple[ABB.Status, List[float], List[float], List[float], List[float]]:
        """
        
                            Compute equivalent section properties (area, center of gravity, Young's modulus and inertia) of a profile composed of different sub-sections.
        
                            Input
                                n Number of sub-sections that compose the section
                                Ai Areas of sub-sections                        
                                Ei Young's modulus of sub-sections
                                Ycogi Center of gravity of sub-sections in Y direction
                                Ixxi Moments of inertia (Quadratic moments) of sub-sections around XX (expressed at the center of gravity of each sub-section)
                            Output
                                A Area of the equivalent section (sum of all sub-sections)
                                E Young's modulus of the equivalent section
                                Ycog Center of gravity of the equivalent section in Y direction
                                Ixx Moment of inertia of the equivalent section around XX (expressed at the center of gravity of the equivalent section)
                        
         @return A tuple consisting of (status, A, oYcog, E, oIxx). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - A is: List[float]. Area of the equivalent section (sum of all sub-sections) .
         - oYcog is: List[float]. Center of gravity of the equivalent section in Y direction .
         - E is: List[float]. Young's modulus of the equivalent section .
         - oIxx is: List[float]. Moment of inertia of the equivalent section around XX (expressed at the center of gravity of the equivalent section) .

        """
        pass
    
    ## 
    ##                     Compute Crippling stress allowable for a given segment
    ## 
    ##                     Crippling curves for a sub-section (also called a segment) of extruded metallic profiles.
    ## 
    ##                     The computed value is 'Fcc'.
    ##                     'Fcc' is thresholded by 'Fcy', to avoid plasticity of material.
    ##                     Segment's width ('b') is assumed to be greater than its thickness ('t').
    ## 
    ##                     Input
    ##                         Fcy Compressive yield allowable stress
    ##                         E   Young's modulus
    ##                         FE  Segment's number of free edges
    ##                         b   Segment's width
    ##                         t   Segment's thickness
    ##                     Output
    ##                         Fcc Equivalent stress allowable
    ##                     Returns
    ##                         Computation status
    ##                 
    ##  @return A tuple consisting of (status, iFcc). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - iFcc is: float. Equivalent stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def ExtrudedMetallicSubSectionCripplingAllowable(abbContext: AbbContext, iFcy: float, E: float, FE: int, b: float, t: float) -> Tuple[ABB.Status, float]:
        """
        
                            Compute Crippling stress allowable for a given segment
        
                            Crippling curves for a sub-section (also called a segment) of extruded metallic profiles.
        
                            The computed value is 'Fcc'.
                            'Fcc' is thresholded by 'Fcy', to avoid plasticity of material.
                            Segment's width ('b') is assumed to be greater than its thickness ('t').
        
                            Input
                                Fcy Compressive yield allowable stress
                                E   Young's modulus
                                FE  Segment's number of free edges
                                b   Segment's width
                                t   Segment's thickness
                            Output
                                Fcc Equivalent stress allowable
                            Returns
                                Computation status
                        
         @return A tuple consisting of (status, iFcc). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - iFcc is: float. Equivalent stress allowable .

        """
        pass
    
    ## 
    ##                     Curves for finding the bending buckling stress coefficient for thin flat plates
    ## 
    ##                     Used for finding 'kb' the bending buckling stress coefficient as a function of:
    ##                     * 'a/b', the panel length ratio
    ##                     * 'a' is the unloaded edge length
    ##                     * 'b' is the loaded edge length
    ##                     * 'beta',  is the factor which, divided to b, gives the edge length in compression (while
    ##                     the remaining edge length is in tension).
    ## 
    ##                     Input
    ##                         a_over_b    Panel length ratio
    ##                         beta        Loading length ratio
    ##                     Output
    ##                         kb          Bending buckling stress coefficient
    ##                     Returns
    ##                         False if input values are out of bounds
    ##                 
    ##  @return A tuple consisting of (status, kb). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - kb is: float. Bending buckling stress coefficient .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def FlatMetallicPanelBendingBucklingCoefficient(abbContext: AbbContext, a_over_b: float, beta: float) -> Tuple[ABB.Status, float]:
        """
        
                            Curves for finding the bending buckling stress coefficient for thin flat plates
        
                            Used for finding 'kb' the bending buckling stress coefficient as a function of:
                            * 'a/b', the panel length ratio
                            * 'a' is the unloaded edge length
                            * 'b' is the loaded edge length
                            * 'beta',  is the factor which, divided to b, gives the edge length in compression (while
                            the remaining edge length is in tension).
        
                            Input
                                a_over_b    Panel length ratio
                                beta        Loading length ratio
                            Output
                                kb          Bending buckling stress coefficient
                            Returns
                                False if input values are out of bounds
                        
         @return A tuple consisting of (status, kb). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - kb is: float. Bending buckling stress coefficient .

        """
        pass
    
    ## 
    ##                     Curves for finding 'kc' the compressive-buckling coefficient for rectangular metallic flat plate
    ## 
    ##                     Used for finding 'kc' the compressive-buckling coefficient for rectangular metallic flat plate,
    ##                     as a function of edge lengths and edge boundary conditions
    ## 
    ##                     Input
    ##                         a           Unloaded edge length
    ##                         b           Loaded edge length
    ##                         BC_Unloaded Support along unloaded edges {Clamped-Clamped, Simply Supported-Clamped, Simply Supported-Simply Supported, Free-Clamped, Free-Simply Supported}
    ##                         BC_Loaded   Support along loaded edges {Clamped or Simply Supported}
    ##                     Output
    ##                         kc          Compressive buckling coefficient
    ##                     Returns
    ##                         Computation status
    ## 
    ##                 
    ##  @return A tuple consisting of (status, kc). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - kc is: float. Compressive buckling coefficient .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def FlatMetallicPanelCompressiveBucklingCoefficient(abbContext: AbbContext, a: float, b: float, bc_unloaded: ABB.UnloadedEdgeSupportType, bc_loaded: ABB.EdgeSupportType) -> Tuple[ABB.Status, float]:
        """
        
                            Curves for finding 'kc' the compressive-buckling coefficient for rectangular metallic flat plate
        
                            Used for finding 'kc' the compressive-buckling coefficient for rectangular metallic flat plate,
                            as a function of edge lengths and edge boundary conditions
        
                            Input
                                a           Unloaded edge length
                                b           Loaded edge length
                                BC_Unloaded Support along unloaded edges {Clamped-Clamped, Simply Supported-Clamped, Simply Supported-Simply Supported, Free-Clamped, Free-Simply Supported}
                                BC_Loaded   Support along loaded edges {Clamped or Simply Supported}
                            Output
                                kc          Compressive buckling coefficient
                            Returns
                                Computation status
        
                        
         @return A tuple consisting of (status, kc). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - kc is: float. Compressive buckling coefficient .

        """
        pass
    
    ## 
    ##                     Curves for finding 'ks' the shear-buckling coefficient for flat rectangular plate
    ## 
    ##                     These curves are inspired by Bruhn manual.
    ##                     Used for finding 'ks' the shear-buckling coefficient for flat rectangular plate, as a function of edge lengths and boundary conditions
    ## 
    ##                     Input
    ##                         a   First plate dimension
    ##                         b   Second plate dimension
    ##                         BC  Support along the edges {Simply Supported or Clamped}
    ##                     Output
    ##                         ks  Shear-buckling coefficient
    ##                     Returns
    ##                         Computation status
    ##                 
    ##  @return A tuple consisting of (status, ks). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - ks is: float. Shear-buckling coefficient .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def FlatMetallicPanelShearBucklingCoefficient(abbContext: AbbContext, a: float, b: float, bc: ABB.EdgeSupportType) -> Tuple[ABB.Status, float]:
        """
        
                            Curves for finding 'ks' the shear-buckling coefficient for flat rectangular plate
        
                            These curves are inspired by Bruhn manual.
                            Used for finding 'ks' the shear-buckling coefficient for flat rectangular plate, as a function of edge lengths and boundary conditions
        
                            Input
                                a   First plate dimension
                                b   Second plate dimension
                                BC  Support along the edges {Simply Supported or Clamped}
                            Output
                                ks  Shear-buckling coefficient
                            Returns
                                Computation status
                        
         @return A tuple consisting of (status, ks). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - ks is: float. Shear-buckling coefficient .

        """
        pass
    
    ## 
    ##                     Integer NA value
    ##                 
    ##  @return value (int): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetIntegerNa() -> int:
        """
        
                            Integer NA value
                        
         @return value (int): .
        """
        pass
    
    ## 
    ##                     The MS (margin of safety) threshold
    ##                 
    ##  @return ret (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    @staticmethod
    def GetMsThreshold() -> float:
        """
        
                            The MS (margin of safety) threshold
                        
         @return ret (float): .
        """
        pass
    
    ## 
    ##                     PI number
    ##                 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPi() -> float:
        """
        
                            PI number
                        
         @return value (float): .
        """
        pass
    
    ## 
    ##                     Real epsilon
    ##                 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRealEpsilon() -> float:
        """
        
                            Real epsilon
                        
         @return value (float): .
        """
        pass
    
    ## 
    ##                     Maximum real number
    ##                 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRealMax() -> float:
        """
        
                            Maximum real number
                        
         @return value (float): .
        """
        pass
    
    ## 
    ##                     Real NA
    ##                 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRealNa() -> float:
        """
        
                            Real NA
                        
         @return value (float): .
        """
        pass
    
    ## 
    ##                     The negative infinity value
    ##                 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRealNegativeInfinity() -> float:
        """
        
                            The negative infinity value
                        
         @return value (float): .
        """
        pass
    
    ## 
    ##                     The positive infinity value
    ##                 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetRealPositiveInfinity() -> float:
        """
        
                            The positive infinity value
                        
         @return value (float): .
        """
        pass
    
    ## 
    ##                     Ultimate limit factor from the customer default
    ##                 
    ##  @return value (float): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetUltimateLimitFactor() -> float:
        """
        
                            Ultimate limit factor from the customer default
                        
         @return value (float): .
        """
        pass
    
    ## 
    ##                     Tests if a value is NA
    ##                 
    ##  @return ret (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="value"> (float) </param>
    @staticmethod
    def IsRealNa(value: float) -> bool:
        """
        
                            Tests if a value is NA
                        
         @return ret (bool): .
        """
        pass
    
    ## 
    ##                     Tests if a value equals negative infinity
    ##                 
    ##  @return ret (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="value"> (float) </param>
    @staticmethod
    def IsRealNegativeInfinity(value: float) -> bool:
        """
        
                            Tests if a value equals negative infinity
                        
         @return ret (bool): .
        """
        pass
    
    ## 
    ##                     Tests if a value equals positive infinity
    ##                 
    ##  @return ret (bool): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## <param name="value"> (float) </param>
    @staticmethod
    def IsRealPositiveInfinity(value: float) -> bool:
        """
        
                            Tests if a value equals positive infinity
                        
         @return ret (bool): .
        """
        pass
    
    ##  
    ##                     Min Max 1D Method
    ##                     A single load case extraction result table (general scalar table) is provided.
    ##                     Returns:
    ##                     - centrality data (how near the boundary each value is)
    ##                     - an array of boolean set true for each selected load case
    ##                     - the boundary values and tolerance thresholds
    ##                  
    ##  @return A tuple consisting of (status, centrality, lc_selected, point_centrality, boundary_min, boundary_max, tolerance_min, tolerance_max). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - centrality is: List[float].
    ##  - lc_selected is: List[bool].
    ##  - point_centrality is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
    ##  - boundary_min is: float.
    ##  - boundary_max is: float.
    ##  - tolerance_min is: float.
    ##  - tolerance_max is: float.

    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ##  the ABB context 
    @staticmethod
    def Lcf1dMinMax(abbContext: AbbContext, load: NXOpen.GeneralScalarTable, tolerance: float, nb_loadcases: int) -> Tuple[ABB.Status, List[float], List[bool], NXOpen.GeneralScalarTable, float, float, float, float]:
        """
         
                            Min Max 1D Method
                            A single load case extraction result table (general scalar table) is provided.
                            Returns:
                            - centrality data (how near the boundary each value is)
                            - an array of boolean set true for each selected load case
                            - the boundary values and tolerance thresholds
                         
         @return A tuple consisting of (status, centrality, lc_selected, point_centrality, boundary_min, boundary_max, tolerance_min, tolerance_max). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - centrality is: List[float].
         - lc_selected is: List[bool].
         - point_centrality is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
         - boundary_min is: float.
         - boundary_max is: float.
         - tolerance_min is: float.
         - tolerance_max is: float.

        """
        pass
    
    ##  
    ##                     Convex hull Method
    ##                     The two load case extraction result tables (general scalar table) are given to the method.
    ##                     They should be related to the same meshing entities, columns should be in the same order.
    ##                     Use the FilterByLoadSupport if needed.
    ##                     Tolerance should be in [0,1].
    ## 
    ##                     The centrality of a load case LC_i is defined as the shortest distance from the entity 
    ##                     loads to the convex hull in the direction and relative to centroid (reference point).
    ##                     
    ##                     Centrality_i = min_(j in [1,NbEntities])(distance(C_j,L_j)/distance(C_j,R))
    ##                     with
    ##                         - Centrality_i the centrality of the ith loadcase LC_i.
    ##                         - L_j the value of the input load LC_i in the jth selected entity.
    ##                         - C_j the point where the line between the reference point and the 
    ##                           LC_i of the jth selected entity intersects the convex hull.
    ##                         - R the reference point used in the computation of the relative 
    ##                           distance is the centroid of the convex hull polygon.
    ##                         - NbEntities the number of entities in LC_i
    ##                     
    ##                     A load case is critical when Centrality_i is lower or equal to tolerance, for all i in [1,NbLC].
    ##                  
    ##  @return A tuple consisting of (status, centrality, lc_selected, point_centrality, boundary_envelope, boundary_tolerance, load1_min, load1_max, load2_min, load2_max). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - centrality is: List[float]. Centralities.
    ##  - lc_selected is: List[bool]. True if the load case is selected, false otherwise.
    ##  - point_centrality is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
    ##  - boundary_envelope is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Envelope .
    ##  - boundary_tolerance is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Tolerance .
    ##  - load1_min is: float. Load 1 min.
    ##  - load1_max is: float. Load 1 max.
    ##  - load2_min is: float. Load 2 min.
    ##  - load2_max is: float. Load 2 max.

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  the ABB context 
    @staticmethod
    def LcfConvexHull(abbContext: AbbContext, load1: NXOpen.GeneralScalarTable, load2: NXOpen.GeneralScalarTable, tolerance: float, nb_loadcases: int) -> Tuple[ABB.Status, List[float], List[bool], NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, float, float, float, float]:
        """
         
                            Convex hull Method
                            The two load case extraction result tables (general scalar table) are given to the method.
                            They should be related to the same meshing entities, columns should be in the same order.
                            Use the FilterByLoadSupport if needed.
                            Tolerance should be in [0,1].
        
                            The centrality of a load case LC_i is defined as the shortest distance from the entity 
                            loads to the convex hull in the direction and relative to centroid (reference point).
                            
                            Centrality_i = min_(j in [1,NbEntities])(distance(C_j,L_j)/distance(C_j,R))
                            with
                                - Centrality_i the centrality of the ith loadcase LC_i.
                                - L_j the value of the input load LC_i in the jth selected entity.
                                - C_j the point where the line between the reference point and the 
                                  LC_i of the jth selected entity intersects the convex hull.
                                - R the reference point used in the computation of the relative 
                                  distance is the centroid of the convex hull polygon.
                                - NbEntities the number of entities in LC_i
                            
                            A load case is critical when Centrality_i is lower or equal to tolerance, for all i in [1,NbLC].
                         
         @return A tuple consisting of (status, centrality, lc_selected, point_centrality, boundary_envelope, boundary_tolerance, load1_min, load1_max, load2_min, load2_max). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - centrality is: List[float]. Centralities.
         - lc_selected is: List[bool]. True if the load case is selected, false otherwise.
         - point_centrality is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
         - boundary_envelope is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Envelope .
         - boundary_tolerance is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Tolerance .
         - load1_min is: float. Load 1 min.
         - load1_max is: float. Load 1 max.
         - load2_min is: float. Load 2 min.
         - load2_max is: float. Load 2 max.

        """
        pass
    
    ##  
    ##                     Obtain load extraction GeneralScalarTables whose columns
    ##                     (support entities) are common to all load extractions.  This
    ##                     assumes GSTs where aggregation is done 'by method'.  Only
    ##                     entities common to all load extractions are returned.
    ##                  
    ##  @return A tuple consisting of (status, tables). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - tables is: @link NXOpen.GeneralScalarTable List[NXOpen.GeneralScalarTable]@endlink. filtered GeneralScalarTables .

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  the ABB context 
    @staticmethod
    def LcfFilterLoadsBySupport(abbContext: AbbContext, inputLoads: List[InputLoad]) -> Tuple[ABB.Status, List[NXOpen.GeneralScalarTable]]:
        """
         
                            Obtain load extraction GeneralScalarTables whose columns
                            (support entities) are common to all load extractions.  This
                            assumes GSTs where aggregation is done 'by method'.  Only
                            entities common to all load extractions are returned.
                         
         @return A tuple consisting of (status, tables). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - tables is: @link NXOpen.GeneralScalarTable List[NXOpen.GeneralScalarTable]@endlink. filtered GeneralScalarTables .

        """
        pass
    
    ##  
    ##                     Min Max Bounding Box 2D Method
    ##                     The two load case extraction result tables (general scalar table) are given to the method.
    ##                     They should be related to the same meshing entities. 
    ##                     They should have NaN values at the same location on both tables.
    ##                     Use the FilterByLoadSupport if needed.
    ##                     Set the two tolerances.
    ##                     Results returns some centrality data and an array of boolean which are true 
    ##                     if the load case of corresponding index is selected.
    ##                  
    ##  @return A tuple consisting of (status, load1_max, load1_min, load2_max, load2_min, centrality_1, centrality_2, centrality, lc_selected, point_centrality_1, point_centrality_2, boundary_envelope, boundary_tolerance). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - load1_max is: float.
    ##  - load1_min is: float.
    ##  - load2_max is: float.
    ##  - load2_min is: float.
    ##  - centrality_1 is: List[float].
    ##  - centrality_2 is: List[float].
    ##  - centrality is: List[float].
    ##  - lc_selected is: List[bool].
    ##  - point_centrality_1 is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
    ##  - point_centrality_2 is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
    ##  - boundary_envelope is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Envelope .
    ##  - boundary_tolerance is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Tolerance .

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  the ABB context 
    @staticmethod
    def LcfMinMaxBoundingBox(abbContext: AbbContext, load1: NXOpen.GeneralScalarTable, load2: NXOpen.GeneralScalarTable, tolerance_1: float, tolerance_2: float, nb_loadcases: int) -> Tuple[ABB.Status, float, float, float, float, List[float], List[float], List[float], List[bool], NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable]:
        """
         
                            Min Max Bounding Box 2D Method
                            The two load case extraction result tables (general scalar table) are given to the method.
                            They should be related to the same meshing entities. 
                            They should have NaN values at the same location on both tables.
                            Use the FilterByLoadSupport if needed.
                            Set the two tolerances.
                            Results returns some centrality data and an array of boolean which are true 
                            if the load case of corresponding index is selected.
                         
         @return A tuple consisting of (status, load1_max, load1_min, load2_max, load2_min, centrality_1, centrality_2, centrality, lc_selected, point_centrality_1, point_centrality_2, boundary_envelope, boundary_tolerance). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - load1_max is: float.
         - load1_min is: float.
         - load2_max is: float.
         - load2_min is: float.
         - centrality_1 is: List[float].
         - centrality_2 is: List[float].
         - centrality is: List[float].
         - lc_selected is: List[bool].
         - point_centrality_1 is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
         - point_centrality_2 is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink.
         - boundary_envelope is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Envelope .
         - boundary_tolerance is: @link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink. Boundary Tolerance .

        """
        pass
    
    ## 
    ##                     Computes bolt loads for multiple bolt fitting - Concentric load
    ## 
    ##                     Formula
    ##                         Pn = P * (Psn / SUM(Psn))
    ##                     where:
    ##                         * 'P' is the load acting on the fitting
    ##                         * 'Psn' is the allowable strength of bolt n
    ##                         * 'Pn' is the shear load on bolt n
    ## 
    ##                     Input
    ##                         nblc    Number of load cases
    ##                         P       Load acting on fitting (nblc)
    ##                         nbbolt  Number of bolts
    ##                         Psn     Allowable shear strength of bolt (nbbolt)
    ##                     Output
    ##                         Pn      Shear load on bolt (nblc x nbbolt)
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, oPn). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - oPn is: List[float]. Shear load on bolt (nblc x nbbolt) .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def LoadDistributionBoltsConcentricLoads(abbContext: AbbContext, P: List[float], iPsn: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            Computes bolt loads for multiple bolt fitting - Concentric load
        
                            Formula
                                Pn = P * (Psn / SUM(Psn))
                            where:
                                * 'P' is the load acting on the fitting
                                * 'Psn' is the allowable strength of bolt n
                                * 'Pn' is the shear load on bolt n
        
                            Input
                                nblc    Number of load cases
                                P       Load acting on fitting (nblc)
                                nbbolt  Number of bolts
                                Psn     Allowable shear strength of bolt (nbbolt)
                            Output
                                Pn      Shear load on bolt (nblc x nbbolt)
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, oPn). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - oPn is: List[float]. Shear load on bolt (nblc x nbbolt) .

        """
        pass
    
    ## 
    ##                     Estimation of shear yield stress (Fsy)
    ## 
    ##                     Shear yield stress allowable ('Fsy') is estimated on the basis of the following formula:
    ##                     'Fsy=( FtyL + FtyLT + FcyL + FcyLT ) / 4 * ( 2 * Fsu)/( FtuL + FtuLT )'
    ##                     where:
    ##                     * 'FtyL' is the tensile yield stress under longitudinal direction
    ##                     * 'FtyLT' is the tensile yield stress under long transverse direction
    ##                     * 'FcyL' is  the compressive yield stress under longitudinal direction
    ##                     * 'FcyLT' is the compressive yield stress under long transverse direction
    ##                     * 'Fsu' is the shear ultimate stress
    ##                     * 'FtuL' is the tensile ultimate stress under longitudinal direction
    ##                     * 'FtuLT' is the tensile ultimate stress under long transverse direction
    ## 
    ##                     Input
    ##                         FtyL    Tensile yield stress, longitudinal direction
    ##                         FtyLT   Tensile yield stress, long transverse direction
    ##                         FcyL    Compressive yield stress, longitudinal direction
    ##                         FcyLT   Compressive yield stress, long transverse direction
    ##                         Fsu     Shear ultimate stress
    ##                         FtuL    Tensile ultimate stress, longitudinal direction
    ##                         FtuLT   Tensile ultimate stress, long transverse direction
    ##                     Output
    ##                         Fsy     Shear yield stress
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, oFsy). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - oFsy is: float. Shear yield stress .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MaterialFsyEstimation(abbContext: AbbContext, iFtyL: float, iFtyLT: float, iFcyL: float, iFcyLT: float, iFsu: float, iFtuL: float, iFtuLT: float) -> Tuple[ABB.Status, float]:
        """
        
                            Estimation of shear yield stress (Fsy)
        
                            Shear yield stress allowable ('Fsy') is estimated on the basis of the following formula:
                            'Fsy=( FtyL + FtyLT + FcyL + FcyLT ) / 4 * ( 2 * Fsu)/( FtuL + FtuLT )'
                            where:
                            * 'FtyL' is the tensile yield stress under longitudinal direction
                            * 'FtyLT' is the tensile yield stress under long transverse direction
                            * 'FcyL' is  the compressive yield stress under longitudinal direction
                            * 'FcyLT' is the compressive yield stress under long transverse direction
                            * 'Fsu' is the shear ultimate stress
                            * 'FtuL' is the tensile ultimate stress under longitudinal direction
                            * 'FtuLT' is the tensile ultimate stress under long transverse direction
        
                            Input
                                FtyL    Tensile yield stress, longitudinal direction
                                FtyLT   Tensile yield stress, long transverse direction
                                FcyL    Compressive yield stress, longitudinal direction
                                FcyLT   Compressive yield stress, long transverse direction
                                Fsu     Shear ultimate stress
                                FtuL    Tensile ultimate stress, longitudinal direction
                                FtuLT   Tensile ultimate stress, long transverse direction
                            Output
                                Fsy     Shear yield stress
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, oFsy). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - oFsy is: float. Shear yield stress .

        """
        pass
    
    ## 
    ##                 Metallic panel compressive plasticity curve BC1
    ##                 Curves for finding critical buckling stress / secant yield stress F0.7
    ## 
    ##                 Used for finding 'sigma_cr' the inelastic buckling strength of metallic flat rectangular plate in compression.
    ##                 The Boundary Condition for the unloaded edges is Simply Supported-Free. It computes:
    ##                 * 'sigma_cr /sigma_0.7' as a function of '(kc * pi^2E) / (12 * (1-nu^2) * sigma_0.7)(t/b)^2'  and 'n' where
    ##                 * 'sigma_cr' is the  critical stress allowable
    ##                 * 'sigma_0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
    ##                 * 'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
    ##                 * 'E' is the Young's modulus
    ##                 * 'nu' is the Poisson's ratio
    ##                 * 't' is the plate thickness
    ##                 * 'b' is the loaded edge length
    ##                 * 'n' is the Ramberg-Osgood parameter
    ## 
    ##                 Input
    ##                     X   Critical buckling stress (elastic) / secant yield stress F0.7
    ##                     n   Ramberg-Osgood parameter
    ##                 Output
    ##                     Z   Critical buckling stress (including plasticity) / secant yield stress F0.7
    ##                 Returns
    ##                     Status of the computation
    ##                 
    ##  @return A tuple consisting of (status, Z). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - Z is: float. Critical buckling stress (including plasticity) / secant yield stress F0.7 .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MetallicPanelCompressivePlasticityCurveBc1(abbContext: AbbContext, X: float, n: float) -> Tuple[ABB.Status, float]:
        """
        
                        Metallic panel compressive plasticity curve BC1
                        Curves for finding critical buckling stress / secant yield stress F0.7
        
                        Used for finding 'sigma_cr' the inelastic buckling strength of metallic flat rectangular plate in compression.
                        The Boundary Condition for the unloaded edges is Simply Supported-Free. It computes:
                        * 'sigma_cr /sigma_0.7' as a function of '(kc * pi^2E) / (12 * (1-nu^2) * sigma_0.7)(t/b)^2'  and 'n' where
                        * 'sigma_cr' is the  critical stress allowable
                        * 'sigma_0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
                        * 'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
                        * 'E' is the Young's modulus
                        * 'nu' is the Poisson's ratio
                        * 't' is the plate thickness
                        * 'b' is the loaded edge length
                        * 'n' is the Ramberg-Osgood parameter
        
                        Input
                            X   Critical buckling stress (elastic) / secant yield stress F0.7
                            n   Ramberg-Osgood parameter
                        Output
                            Z   Critical buckling stress (including plasticity) / secant yield stress F0.7
                        Returns
                            Status of the computation
                        
         @return A tuple consisting of (status, Z). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - Z is: float. Critical buckling stress (including plasticity) / secant yield stress F0.7 .

        """
        pass
    
    ## 
    ##                     Metallic panel compressive plasticity curve BC2
    ##                     Curves for finding critical inter-rivet buckling stress (or critical wrinkling stress) / secant yield stress F0.7
    ## 
    ##                     Used for finding 'Fir' or 'Fw'.
    ##                     It computes either:
    ##                     * 'Fir /F0.7' as a function of '(C * pi^2E)/(12 * (1-nu^2) * F0.7)(ts/p)^2' and 'n' where
    ##                         *  'Fir' is the Inter-Rivet Buckling stress allowable (with plasticity)
    ##                         *  'F0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
    ##                         *  'C' is the end fixity coefficient
    ##                         *  'E' is the Young's modulus
    ##                         *  'nu' is the Poisson's ratio
    ##                         *  'ts' is the thickness of the sheet
    ##                         *  'p' is the rivet spacing
    ##                         *  'n' is the Ramberg-Osgood parameter
    ## 
    ##                     Or:
    ##                     * 'Fw /F0.7' as a function of '(kw * pi^2E)/(12 * (1-nu^2) * F0.7)(ts/bs)^2' and 'n' where
    ##                         *  'Fw' is the wrinkling stress allowable
    ##                         *  'kw' is the wrinkling failing stress coefficient
    ##                         *  'ts' is the thickness of the sheet
    ##                         *  'bs' is the stiffener spacing
    ##                         *  'n' is the Ramberg-Osgood parameter
    ## 
    ##                     Input
    ##                         X   Critical buckling stress (elastic) / secant yield stress F0.7
    ##                         n   Ramberg-Osgood parameter
    ##                     Output
    ##                         Z   Critical buckling/wrinkling stress (including plasticity) / secant yield stress F0.7
    ##                     Returns
    ##                         Status of the computation
    ##                 
    ##  @return A tuple consisting of (status, Z). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - Z is: float. Critical buckling/wrinkling stress (including plasticity) / secant yield stress F0.7 .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MetallicPanelCompressivePlasticityCurveBc2(abbContext: AbbContext, X: float, n: float) -> Tuple[ABB.Status, float]:
        """
        
                            Metallic panel compressive plasticity curve BC2
                            Curves for finding critical inter-rivet buckling stress (or critical wrinkling stress) / secant yield stress F0.7
        
                            Used for finding 'Fir' or 'Fw'.
                            It computes either:
                            * 'Fir /F0.7' as a function of '(C * pi^2E)/(12 * (1-nu^2) * F0.7)(ts/p)^2' and 'n' where
                                *  'Fir' is the Inter-Rivet Buckling stress allowable (with plasticity)
                                *  'F0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
                                *  'C' is the end fixity coefficient
                                *  'E' is the Young's modulus
                                *  'nu' is the Poisson's ratio
                                *  'ts' is the thickness of the sheet
                                *  'p' is the rivet spacing
                                *  'n' is the Ramberg-Osgood parameter
        
                            Or:
                            * 'Fw /F0.7' as a function of '(kw * pi^2E)/(12 * (1-nu^2) * F0.7)(ts/bs)^2' and 'n' where
                                *  'Fw' is the wrinkling stress allowable
                                *  'kw' is the wrinkling failing stress coefficient
                                *  'ts' is the thickness of the sheet
                                *  'bs' is the stiffener spacing
                                *  'n' is the Ramberg-Osgood parameter
        
                            Input
                                X   Critical buckling stress (elastic) / secant yield stress F0.7
                                n   Ramberg-Osgood parameter
                            Output
                                Z   Critical buckling/wrinkling stress (including plasticity) / secant yield stress F0.7
                            Returns
                                Status of the computation
                        
         @return A tuple consisting of (status, Z). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - Z is: float. Critical buckling/wrinkling stress (including plasticity) / secant yield stress F0.7 .

        """
        pass
    
    ## 
    ##                     Metallic panel compressive plasticity curve BC3
    ##                     Curves for finding critical buckling stress / secant yield stress F0.7
    ## 
    ##                     Used for finding 'sigma_cr' the inelastic buckling strength of metallic cylinder in compression.
    ## 
    ##                     It computes:
    ##                     * 'sigma_cr /sigma_0.7' as a function of '(kc * pi^2E)/(12 * (1-nu^2) * sigma_0.7)(t/b)^2'  and 'n' where
    ##                         *  'sigma_cr' is the  critical stress allowable
    ##                         *  'sigma_0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
    ##                         *  'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
    ##                         *  'E' is the Young's modulus
    ##                         *  'nu' is the Poisson's ratio
    ##                         *  't' is the plate thickness
    ##                         *  'b' is the loaded edge length
    ##                         *  'n' is the Ramberg-Osgood parameter
    ## 
    ##                     Input
    ##                         X   Critical buckling stress (elastic) / secant yield stress F0.7
    ##                         n   Ramberg-Osgood parameter
    ##                     Output
    ##                         Z   Critical buckling stress (including plasticity) / secant yield stress F0.7
    ##                     Returns
    ##                         Status of the computation
    ##                 
    ##  @return A tuple consisting of (status, Z). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - Z is: float. Critical buckling stress (including plasticity) / secant yield stress F0.7 .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MetallicPanelCompressivePlasticityCurveBc3(abbContext: AbbContext, X: float, n: float) -> Tuple[ABB.Status, float]:
        """
        
                            Metallic panel compressive plasticity curve BC3
                            Curves for finding critical buckling stress / secant yield stress F0.7
        
                            Used for finding 'sigma_cr' the inelastic buckling strength of metallic cylinder in compression.
        
                            It computes:
                            * 'sigma_cr /sigma_0.7' as a function of '(kc * pi^2E)/(12 * (1-nu^2) * sigma_0.7)(t/b)^2'  and 'n' where
                                *  'sigma_cr' is the  critical stress allowable
                                *  'sigma_0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
                                *  'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
                                *  'E' is the Young's modulus
                                *  'nu' is the Poisson's ratio
                                *  't' is the plate thickness
                                *  'b' is the loaded edge length
                                *  'n' is the Ramberg-Osgood parameter
        
                            Input
                                X   Critical buckling stress (elastic) / secant yield stress F0.7
                                n   Ramberg-Osgood parameter
                            Output
                                Z   Critical buckling stress (including plasticity) / secant yield stress F0.7
                            Returns
                                Status of the computation
                        
         @return A tuple consisting of (status, Z). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - Z is: float. Critical buckling stress (including plasticity) / secant yield stress F0.7 .

        """
        pass
    
    ## 
    ##                     MS allowable.
    ##                     Computes margin of safety based on an allowable
    ## 
    ##                     The formula is MS = Allowable / Value - 1
    ## 
    ##                     where:
    ##                     * 'Allowable' is the manual input
    ##                     * 'Value' is the value coming from load extractor
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Input
    ##                         Allowable   Manual input
    ##                         Value(nblc) Value coming from load extractor
    ##                     Output
    ##                         MS(nblc)    Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsAllowable(abbContext: AbbContext, allowable: float, value: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS allowable.
                            Computes margin of safety based on an allowable
        
                            The formula is MS = Allowable / Value - 1
        
                            where:
                            * 'Allowable' is the manual input
                            * 'Value' is the value coming from load extractor
                            * 'MS' is the margin of safety
        
                            Input
                                Allowable   Manual input
                                Value(nblc) Value coming from load extractor
                            Output
                                MS(nblc)    Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS bearing
    ##                     Computes margin of bearing
    ## 
    ##                     The formula is 'MS = PBearingAllowable / P - 1'
    ## 
    ##                     where
    ##                     * 'PBearingAllowable' is the bearing load allowable ('PBearingAllowable = Fbr * D * t')
    ##                         'Fbr' is the bearing stress allowable
    ##                         'D' is the diameter
    ##                         't' is the thickness
    ##                     * 'P' is the bearing load (P = FactorLoad * PExtracted)
    ##                         'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
    ##                         'PExtracted' is the extracted load ('PExtracted = sqrt( Py ^ 2 + Pz ^ 2 )')
    ##                         'Py' is the shear load in Y direction
    ##                         'Pz' is the shear load in Z direction
    ## 
    ##                     Input
    ##                         D        Diameter
    ##                         t        Thickness
    ##                         Fbr      Bearing stress allowable
    ##                         f        Load factor
    ##                         Py       Shear load Y direction
    ##                         Pz       Shear load Z direction
    ##                     Output
    ##                         MS       Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsBearing(abbContext: AbbContext, D: float, t: float, iFbr: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS bearing
                            Computes margin of bearing
        
                            The formula is 'MS = PBearingAllowable / P - 1'
        
                            where
                            * 'PBearingAllowable' is the bearing load allowable ('PBearingAllowable = Fbr * D * t')
                                'Fbr' is the bearing stress allowable
                                'D' is the diameter
                                't' is the thickness
                            * 'P' is the bearing load (P = FactorLoad * PExtracted)
                                'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
                                'PExtracted' is the extracted load ('PExtracted = sqrt( Py ^ 2 + Pz ^ 2 )')
                                'Py' is the shear load in Y direction
                                'Pz' is the shear load in Z direction
        
                            Input
                                D        Diameter
                                t        Thickness
                                Fbr      Bearing stress allowable
                                f        Load factor
                                Py       Shear load Y direction
                                Pz       Shear load Z direction
                            Output
                                MS       Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS bolt bending
    ##                     Computes margin of safety of a bolt under bending load
    ## 
    ##                     The formula is 'MS = MBendingAllowable / M - 1'
    ## 
    ##                     where
    ##                     * 'MBendingAllowable' is the bending moment allowable of the bolt.
    ##                     * 'M' is the bending moment applied to the bolt. ('M = b * P')
    ##                         where:
    ##                         'b' is the arm
    ##                         'P' is the load ('P = FactorLoad * PExtracted')
    ##                         'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
    ##                         'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
    ##                         'Py' is the shear load in Y direction
    ##                         'Pz' is the shear load in Z direction
    ## 
    ##                     Input
    ##                         b         Arm
    ##                         Mba       Bending moment allowable of bolt
    ##                         f         Load factor
    ##                         P         Shear load
    ##                     Output
    ##                         MS        Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsBoltBending(abbContext: AbbContext, b: float, iMba: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS bolt bending
                            Computes margin of safety of a bolt under bending load
        
                            The formula is 'MS = MBendingAllowable / M - 1'
        
                            where
                            * 'MBendingAllowable' is the bending moment allowable of the bolt.
                            * 'M' is the bending moment applied to the bolt. ('M = b * P')
                                where:
                                'b' is the arm
                                'P' is the load ('P = FactorLoad * PExtracted')
                                'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
                                'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
                                'Py' is the shear load in Y direction
                                'Pz' is the shear load in Z direction
        
                            Input
                                b         Arm
                                Mba       Bending moment allowable of bolt
                                f         Load factor
                                P         Shear load
                            Output
                                MS        Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS bolt combined shear tension
    ##                     Computes margin of safety of a bolt under shear load and tension load
    ## 
    ##                     The formula is 'MS = 1 / sqrt( Rt ^ 2 + Rs ^ 3 )  - 1'
    ##                     where
    ##                         * Rt = PTensileX/PTensileAllowable
    ##                         * Rs = PShear/PShearAllowable
    ##                         *'PTensileAllowable' is the tensile load allowable of the bolt
    ##                         * 'PTensileX' is the tensile load applied on the fastener
    ##                         * 'PShearAllowable' is the single shear load allowable of the bolt
    ##                         * 'Pshear' is the shearing load applied through the shear area. PShear = FactorLoad * PExtracted
    ##                         * 'FactorLoad' is the ratio of load between extracted load PExtracted and PShear
    ##                         * 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
    ##                         * 'Py' is the shear load in Y direction
    ##                         * 'Pz' is the shear load in Z direction
    ## 
    ##                     Input
    ##                         nblc                Number of loadcases
    ##                         Ptx                 Tensile load allowable
    ##                         Pss                 Single shear load allowable
    ##                         Px(nblc)            Tensile load
    ##                         f                   Load factor
    ##                         P(nblc)             Shear load
    ##                     Output
    ##                         MS                  Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsBoltCombinedShearTension(abbContext: AbbContext, iPtx: float, iPss: float, iPx: List[float], f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS bolt combined shear tension
                            Computes margin of safety of a bolt under shear load and tension load
        
                            The formula is 'MS = 1 / sqrt( Rt ^ 2 + Rs ^ 3 )  - 1'
                            where
                                * Rt = PTensileX/PTensileAllowable
                                * Rs = PShear/PShearAllowable
                                *'PTensileAllowable' is the tensile load allowable of the bolt
                                * 'PTensileX' is the tensile load applied on the fastener
                                * 'PShearAllowable' is the single shear load allowable of the bolt
                                * 'Pshear' is the shearing load applied through the shear area. PShear = FactorLoad * PExtracted
                                * 'FactorLoad' is the ratio of load between extracted load PExtracted and PShear
                                * 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
                                * 'Py' is the shear load in Y direction
                                * 'Pz' is the shear load in Z direction
        
                            Input
                                nblc                Number of loadcases
                                Ptx                 Tensile load allowable
                                Pss                 Single shear load allowable
                                Px(nblc)            Tensile load
                                f                   Load factor
                                P(nblc)             Shear load
                            Output
                                MS                  Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS bolt combined shear tension bending
    ##                     Computes margin of safety of a bolt under shear, tension and bending load
    ## 
    ##                     The formula is MS = 1 / sqrt ( ( Rt + Rb ) ^ 2 + Rs ^ 3 ) - 1
    ##                     where
    ##                         * Rt = PTensileX / PTensileAllowable
    ##                         * Rb = M / MAllowable
    ##                         * Rs = PShear / PShearAllowable
    ## 
    ##                         Tensile data
    ##                         * 'PTensileAllowable' is the tensile load allowable of the bolt
    ##                         * 'PTensileX' is the tensile load applied on the fastener
    ## 
    ##                         Bending data
    ##                         * 'MAllowable' is the bending moment allowable of the bolt
    ##                         * 'M' is the bending moment applied to the bolt.
    ##                             M = b * PBend
    ##                             PBend = FactorLoadBend * sqrt(PyBend^2 + PzBend^2)
    ##                         * 'b' is the arm
    ##                         * 'FactorLoadBend' is the load factor for bending
    ##                         * 'PyBend' is the bending load in Y direction
    ##                         * 'PzBend' is the shear load in Z direction
    ## 
    ##                         Shear data
    ##                         * 'PShearAllowable' is the single shear load allowable of the bolt
    ##                         * 'PShear' is the shearing load applied through the shear area.
    ##                             PShear = FactorLoadShear * sqrt(PyShear^2 + PzShear^2)
    ##                         * 'FactorLoadShear' is the load factor for shearing
    ##                         * 'PyShear' is the shear load in Y direction
    ##                         * 'PzShear' is the shear load in Z direction
    ## 
    ##                     Input
    ##                         nblc            Number of loadcases
    ##                         b               Arm
    ##                         Mba             Bending moment allowable of bolt
    ##                         Ptx             Tensile load allowable
    ##                         Pss             Single shear load allowable
    ##                         fb              Load factor for bending
    ##                         Pb(nblc)        Bending load
    ##                         Px(nblc)        Tensile load
    ##                         fs              Load factor for shear
    ##                         Ps(nblc)        Shear load
    ##                     Output
    ##                         MS              Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsBoltCombinedShearTensionBending(abbContext: AbbContext, b: float, iMba: float, iPtx: float, iPss: float, fb: float, iPb: List[float], iPx: List[float], fs: float, iPs: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS bolt combined shear tension bending
                            Computes margin of safety of a bolt under shear, tension and bending load
        
                            The formula is MS = 1 / sqrt ( ( Rt + Rb ) ^ 2 + Rs ^ 3 ) - 1
                            where
                                * Rt = PTensileX / PTensileAllowable
                                * Rb = M / MAllowable
                                * Rs = PShear / PShearAllowable
        
                                Tensile data
                                * 'PTensileAllowable' is the tensile load allowable of the bolt
                                * 'PTensileX' is the tensile load applied on the fastener
        
                                Bending data
                                * 'MAllowable' is the bending moment allowable of the bolt
                                * 'M' is the bending moment applied to the bolt.
                                    M = b * PBend
                                    PBend = FactorLoadBend * sqrt(PyBend^2 + PzBend^2)
                                * 'b' is the arm
                                * 'FactorLoadBend' is the load factor for bending
                                * 'PyBend' is the bending load in Y direction
                                * 'PzBend' is the shear load in Z direction
        
                                Shear data
                                * 'PShearAllowable' is the single shear load allowable of the bolt
                                * 'PShear' is the shearing load applied through the shear area.
                                    PShear = FactorLoadShear * sqrt(PyShear^2 + PzShear^2)
                                * 'FactorLoadShear' is the load factor for shearing
                                * 'PyShear' is the shear load in Y direction
                                * 'PzShear' is the shear load in Z direction
        
                            Input
                                nblc            Number of loadcases
                                b               Arm
                                Mba             Bending moment allowable of bolt
                                Ptx             Tensile load allowable
                                Pss             Single shear load allowable
                                fb              Load factor for bending
                                Pb(nblc)        Bending load
                                Px(nblc)        Tensile load
                                fs              Load factor for shear
                                Ps(nblc)        Shear load
                            Output
                                MS              Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS bolt shear
    ##                     Computes margin of safety of a bolt under shear load
    ## 
    ##                     The formula is MS = PShearAllowable / P  - 1
    ##                     where
    ##                         * 'PShearAllowable' is the single shear load allowable of the bolt
    ##                         * 'P' is the shearing load applied through the shear area. P = FactorLoad * PExtracted
    ##                         * 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
    ##                         * 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
    ##                         * 'Py' is the shear load in Y direction
    ##                         * 'Pz' is the shear load in Z direction
    ## 
    ##                     Input
    ##                         NbLC                Number of loadcases
    ##                         Pss                 Single shear load allowable
    ##                         f                   Load factor
    ##                         P(NbLC)             Shear load
    ##                     Output
    ##                         MS                  Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsBoltShear(abbContext: AbbContext, iPss: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS bolt shear
                            Computes margin of safety of a bolt under shear load
        
                            The formula is MS = PShearAllowable / P  - 1
                            where
                                * 'PShearAllowable' is the single shear load allowable of the bolt
                                * 'P' is the shearing load applied through the shear area. P = FactorLoad * PExtracted
                                * 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
                                * 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
                                * 'Py' is the shear load in Y direction
                                * 'Pz' is the shear load in Z direction
        
                            Input
                                NbLC                Number of loadcases
                                Pss                 Single shear load allowable
                                f                   Load factor
                                P(NbLC)             Shear load
                            Output
                                MS                  Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Column Eccentric Load
    ## 
    ##                     Computes margin of safety of column under eccentric axial compressive load (secant formula theory)
    ## 
    ##                     When the axial compressive load is not applied on the centroid of the column cross section eccentricity has to be taken into account.
    ## 
    ##                     MS = Pcr / (abs(P)) - 1
    ## 
    ##                     where:
    ##                         * Pcr is the compressive load allowable
    ##                         * P is the axial compressive load (MS is not calculated in case of tensile stress)
    ## 
    ##                     Pcr = (sigmacr*A)/(1 + (ecc*c)/rho^2 sec (1/2 sqrt(Pcr)/(EA)(L')/rho))
    ## 
    ##                     where:
    ##                         * sigmacr is the material stress allowable
    ##                         * A the area of the cross section
    ##                         * I is the bending inertia of the column
    ##                         * ecc the eccentricity of the load (distance between the line of action of P and the axis of the column)
    ##                         * c the distance of extreme fiber to neutral axis
    ##                         * rho is the radius of gyration of cross-section given by rho=sqrt(I/A)
    ##                         * E the material Young modulus
    ##                         * L' is the column effective length given by L'=L/sqrt(C)
    ##                             * L the column length
    ##                             * C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
    ##                                 * Pinned-Pinned: C=1
    ##                                 * Fixed-Fixed: C=4
    ##                                 * Fixed-Pinned: C=2.05
    ##                                 * Fixed-Free: C=0.25
    ## 
    ##                     Remark: Pcr is declared in each side of the formula. As consequence an iterative process is used to evaluate it.
    ## 
    ##                     Input
    ##                         A            Area of the cross section
    ##                         L            Column length
    ##                         E            Young's modulus
    ##                         I            Bending inertia of the column
    ##                         sigmacr      Material stress allowable
    ##                         C            End fixity coefficient depending on the Boundary Condition given at both extremities
    ##                         ecc          Eccentricity of the load
    ##                         nblc         Number of load cases
    ##                         sigma        Stress
    ##                     Output
    ##                         iPcr         Compressive load allowable
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, iPcr, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - iPcr is: float. Compressive load allowable .
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsColumnEccentricLoadSecantFormula(abbContext: AbbContext, A: float, L: float, E: float, I: float, sigmacr: float, C: float, ecc: float, extrmfbrdist: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
        
                            MS Column Eccentric Load
        
                            Computes margin of safety of column under eccentric axial compressive load (secant formula theory)
        
                            When the axial compressive load is not applied on the centroid of the column cross section eccentricity has to be taken into account.
        
                            MS = Pcr / (abs(P)) - 1
        
                            where:
                                * Pcr is the compressive load allowable
                                * P is the axial compressive load (MS is not calculated in case of tensile stress)
        
                            Pcr = (sigmacr*A)/(1 + (ecc*c)/rho^2 sec (1/2 sqrt(Pcr)/(EA)(L')/rho))
        
                            where:
                                * sigmacr is the material stress allowable
                                * A the area of the cross section
                                * I is the bending inertia of the column
                                * ecc the eccentricity of the load (distance between the line of action of P and the axis of the column)
                                * c the distance of extreme fiber to neutral axis
                                * rho is the radius of gyration of cross-section given by rho=sqrt(I/A)
                                * E the material Young modulus
                                * L' is the column effective length given by L'=L/sqrt(C)
                                    * L the column length
                                    * C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
                                        * Pinned-Pinned: C=1
                                        * Fixed-Fixed: C=4
                                        * Fixed-Pinned: C=2.05
                                        * Fixed-Free: C=0.25
        
                            Remark: Pcr is declared in each side of the formula. As consequence an iterative process is used to evaluate it.
        
                            Input
                                A            Area of the cross section
                                L            Column length
                                E            Young's modulus
                                I            Bending inertia of the column
                                sigmacr      Material stress allowable
                                C            End fixity coefficient depending on the Boundary Condition given at both extremities
                                ecc          Eccentricity of the load
                                nblc         Number of load cases
                                sigma        Stress
                            Output
                                iPcr         Compressive load allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, iPcr, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - iPcr is: float. Compressive load allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Engesser
    ## 
    ##                     Computes margin of safety on the basis of Engesser column buckling theory (also called tangent-modulus theory)
    ## 
    ##                     MS = sigmacr / (abs(sigma)) - 1
    ## 
    ##                     where:
    ##                         * sigmacr is the Engesser buckling stress allowable
    ##                         * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
    ## 
    ##                     sigmacr = (pi^2 Et)/((L') /rho)^2
    ## 
    ##                     where:
    ##                         * Et is the tangent Young modulus of the column material given by Et=sigma/((sigma/E)+0.002*n*(sigma/fy)^n)) with
    ##                             * sigma is the stress
    ##                             * fy is the yield stress
    ##                             * E is the Young's modulus
    ##                             * n is the Ramberg-Osgood parameter
    ##                         * L' is the column effective length given by L'=L/sqrt(C) with
    ##                             * L the column length
    ##                             * C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
    ##                                 * Pinned-Pinned: C=1
    ##                                 * Fixed-Fixed: C=4
    ##                                 * Fixed-Pinned: C=2.05
    ##                                 * Fixed-Free: C=0.25
    ##                         * rho is the radius of gyration of cross-section given by rho=sqrt(I/A) with
    ##                             * I is the bending inertia of the column
    ##                             * A is the column cross section area
    ## 
    ##                     Input
    ##                         A            Area of the cross section
    ##                         L            Column length
    ##                         E            Young's modulus
    ##                         I            Bending inertia of the column
    ##                         n            Ramberg-Ossgood coefficient
    ##                         iFy          Yield stress allowable
    ##                         C            End fixity coefficient depending on the Boundary Condition given at both extremities
    ##                         nblc         Number of load cases
    ##                         sigma        Stress
    ##                     Output
    ##                         sigmacr      Engesser buckling stress allowable
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ## 
    ##                 
    ##  @return A tuple consisting of (status, sigmacr, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - sigmacr is: float. Engesser buckling stress allowable .
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The ABB context 
    @staticmethod
    def MsColumnEngesser(abbContext: AbbContext, A: float, L: float, E: float, I: float, n: float, iFy: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
        
                            MS Engesser
        
                            Computes margin of safety on the basis of Engesser column buckling theory (also called tangent-modulus theory)
        
                            MS = sigmacr / (abs(sigma)) - 1
        
                            where:
                                * sigmacr is the Engesser buckling stress allowable
                                * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
        
                            sigmacr = (pi^2 Et)/((L') /rho)^2
        
                            where:
                                * Et is the tangent Young modulus of the column material given by Et=sigma/((sigma/E)+0.002*n*(sigma/fy)^n)) with
                                    * sigma is the stress
                                    * fy is the yield stress
                                    * E is the Young's modulus
                                    * n is the Ramberg-Osgood parameter
                                * L' is the column effective length given by L'=L/sqrt(C) with
                                    * L the column length
                                    * C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
                                        * Pinned-Pinned: C=1
                                        * Fixed-Fixed: C=4
                                        * Fixed-Pinned: C=2.05
                                        * Fixed-Free: C=0.25
                                * rho is the radius of gyration of cross-section given by rho=sqrt(I/A) with
                                    * I is the bending inertia of the column
                                    * A is the column cross section area
        
                            Input
                                A            Area of the cross section
                                L            Column length
                                E            Young's modulus
                                I            Bending inertia of the column
                                n            Ramberg-Ossgood coefficient
                                iFy          Yield stress allowable
                                C            End fixity coefficient depending on the Boundary Condition given at both extremities
                                nblc         Number of load cases
                                sigma        Stress
                            Output
                                sigmacr      Engesser buckling stress allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
        
                        
         @return A tuple consisting of (status, sigmacr, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - sigmacr is: float. Engesser buckling stress allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Euler
    ## 
    ##                     Computes margin of safety on the basis of Euler column buckling theory
    ## 
    ##                     MS = sigmacr / (abs(sigma)) - 1
    ## 
    ##                     where:
    ##                         * sigmacr is the Euler buckling stress allowable
    ##                         * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
    ## 
    ##                     sigmacr = (pi^2 E)/((L') /rho)^2
    ## 
    ##                     where:
    ##                         * E is the Young modulus of the column material
    ##                         * L' is the column effective length given by L'=L/sqrt(C) with
    ##                             * L the column length
    ##                             * C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
    ##                                 * Pinned-Pinned: C=1
    ##                                 * Fixed-Fixed: C=4
    ##                                 * Fixed-Pinned: C=2.05
    ##                                 * Fixed-Free: C=0.25
    ##                         * rho is the radius of gyration of cross-section given by rho=sqrt(I/A) with
    ##                             * I is the bending inertia of the column
    ##                             * A is the column cross section area
    ## 
    ##                     Input
    ##                         A            Area of the cross section
    ##                         L            Column length
    ##                         E            Young's modulus
    ##                         I            Bending inertia of the column
    ##                         C            End fixity coefficient depending on the Boundary Condition given at both extremities
    ##                         nblc         Number of load cases
    ##                         sigma        Axial compressive stress
    ##                     Output
    ##                         sigmacr      Euler buckling stress allowable
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ## 
    ##                 
    ##  @return A tuple consisting of (status, sigmacr, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - sigmacr is: float. Euler buckling stress allowable .
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsColumnEuler(abbContext: AbbContext, A: float, L: float, E: float, I: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
        
                            MS Euler
        
                            Computes margin of safety on the basis of Euler column buckling theory
        
                            MS = sigmacr / (abs(sigma)) - 1
        
                            where:
                                * sigmacr is the Euler buckling stress allowable
                                * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
        
                            sigmacr = (pi^2 E)/((L') /rho)^2
        
                            where:
                                * E is the Young modulus of the column material
                                * L' is the column effective length given by L'=L/sqrt(C) with
                                    * L the column length
                                    * C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
                                        * Pinned-Pinned: C=1
                                        * Fixed-Fixed: C=4
                                        * Fixed-Pinned: C=2.05
                                        * Fixed-Free: C=0.25
                                * rho is the radius of gyration of cross-section given by rho=sqrt(I/A) with
                                    * I is the bending inertia of the column
                                    * A is the column cross section area
        
                            Input
                                A            Area of the cross section
                                L            Column length
                                E            Young's modulus
                                I            Bending inertia of the column
                                C            End fixity coefficient depending on the Boundary Condition given at both extremities
                                nblc         Number of load cases
                                sigma        Axial compressive stress
                            Output
                                sigmacr      Euler buckling stress allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
        
                        
         @return A tuple consisting of (status, sigmacr, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - sigmacr is: float. Euler buckling stress allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Column Johnson-Euler
    ## 
    ##                     Computes margin of safety on the basis of Johnson-Euler column theory
    ## 
    ##                     MS = sigmacr / (abs(sigma)) - 1
    ## 
    ##                     where:
    ##                         * sigmacr is the Johnson-Euler stress allowable
    ##                         * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
    ## 
    ##                     To find the column failing stress under axial compressive load (sigmacr)) Euler or Johnson-Euler equations are used (choice is done depending L'/rho):
    ##                         * The Euler equation is sigmacr = (pi^2E)/(L'/rho)^2 (use in case L'/rho greater than sigma0/2)
    ##                         * The Johnson-Euler equation is sigmacr = sigma0-sigma0^2/(4*pi^2*E)(L'/rho)^2 (use in case L'/rho smaller than sigma0/2)
    ##                     where:
    ##                     * sigma0 is the column stress allowable for a column slenderness equals to 0. It is the minimal value between crippling stress and yield allowable in compression of column.
    ##                     * E is the Young modulus of the column material
    ##                         * L' is the column effective length given by L'=L/sqrt(C)
    ##                             * L the column length
    ##                             * C the end fixity coefficient depending on the Boundary Condition (BC) given at both extremities. Please find some values:
    ##                                 * Pinned-Pinned: C=1
    ##                                 * Fixed-Fixed: C=4
    ##                                 * Fixed-Pinned: C=2.05
    ##                                 * Fixed-Free: C=0.25
    ##                     * rho is the radius of gyration of cross-section given by rho=sqrt(I/A)
    ##                         * I is the bending inertia of the column
    ##                         * A is the column cross section area
    ## 
    ##                     Input
    ##                         A            Column cross section area
    ##                         L            Column length
    ##                         I            Bending inertia of the column
    ##                         E            Young's modulus
    ##                         C            End fixity coefficient depending on the Boundary Condition given at both extremities
    ##                         sigma0       Column stress allowable for a column slenderness equals to 0
    ##                         nblc         Number of load cases
    ##                         sigma        Axial compressive stress
    ##                     Output
    ##                         sigmacr      Johnson-Euler Stress Allowable
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, sigmacr, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - sigmacr is: float. Johnson-Euler Stress Allowable .
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsColumnJohnsonEuler(abbContext: AbbContext, A: float, L: float, I: float, E: float, C: float, sigma0: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
        
                            MS Column Johnson-Euler
        
                            Computes margin of safety on the basis of Johnson-Euler column theory
        
                            MS = sigmacr / (abs(sigma)) - 1
        
                            where:
                                * sigmacr is the Johnson-Euler stress allowable
                                * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
        
                            To find the column failing stress under axial compressive load (sigmacr)) Euler or Johnson-Euler equations are used (choice is done depending L'/rho):
                                * The Euler equation is sigmacr = (pi^2E)/(L'/rho)^2 (use in case L'/rho greater than sigma0/2)
                                * The Johnson-Euler equation is sigmacr = sigma0-sigma0^2/(4*pi^2*E)(L'/rho)^2 (use in case L'/rho smaller than sigma0/2)
                            where:
                            * sigma0 is the column stress allowable for a column slenderness equals to 0. It is the minimal value between crippling stress and yield allowable in compression of column.
                            * E is the Young modulus of the column material
                                * L' is the column effective length given by L'=L/sqrt(C)
                                    * L the column length
                                    * C the end fixity coefficient depending on the Boundary Condition (BC) given at both extremities. Please find some values:
                                        * Pinned-Pinned: C=1
                                        * Fixed-Fixed: C=4
                                        * Fixed-Pinned: C=2.05
                                        * Fixed-Free: C=0.25
                            * rho is the radius of gyration of cross-section given by rho=sqrt(I/A)
                                * I is the bending inertia of the column
                                * A is the column cross section area
        
                            Input
                                A            Column cross section area
                                L            Column length
                                I            Bending inertia of the column
                                E            Young's modulus
                                C            End fixity coefficient depending on the Boundary Condition given at both extremities
                                sigma0       Column stress allowable for a column slenderness equals to 0
                                nblc         Number of load cases
                                sigma        Axial compressive stress
                            Output
                                sigmacr      Johnson-Euler Stress Allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, sigmacr, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - sigmacr is: float. Johnson-Euler Stress Allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Torsional Buckling
    ## 
    ##                     Computes margin of safety of torsional buckling of a column
    ## 
    ##                     MS = iPcr / (abs(load)) - 1
    ## 
    ##                     where:
    ##                         * iPcr is the torsional buckling load allowable
    ##                         * load is the axial compressive load (MS is not calculated in case of tensile load)
    ## 
    ##                     Hypotheses: Column cross section has two axes of symetry or is point symmetric and the shear center and centroid is coinciding.
    ## 
    ##                     iPcr = 1/r0^2(G*J+(E*gamma*pi^2)/(L')^2)
    ## 
    ##                     where:
    ##                         * E is the Young modulus of the column material
    ##                         * G is the shear modulus of elasticity
    ##                         * L' is the column effective length L'=L/sqrt(C) with:
    ##                             * L the column length
    ##                             * C the end fixity coefficient depending on the Boundary Condition given at both extremities.
    ##                         * r0 is the polar radius of gyration of the section about its shear center
    ##                         * J is the torsion constant of the section
    ##                         * gamma is the warping constant of the section
    ## 
    ##                     Input
    ##                         L            Column effective length
    ##                         E            Young's modulus
    ##                         G            Shear modulus of elasticity
    ##                         J            Torsion constant of the section
    ##                         gamma        Warping constant of the section
    ##                         r0           Polar radius of gyration of the section about its shear center
    ##                         C            End fixity coefficient depending on the Boundary Condition given at both extremities
    ##                         nblc         Number of load cases
    ##                         load         Axial compressive load
    ##                     Output
    ##                         iPcr         Torsional buckling load allowable
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, iPcr, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - iPcr is: float. Torsional buckling load allowable .
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsColumnTorsionalbuckling(abbContext: AbbContext, L: float, E: float, G: float, J: float, gamma: float, r0: float, C: float, load: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
        
                            MS Torsional Buckling
        
                            Computes margin of safety of torsional buckling of a column
        
                            MS = iPcr / (abs(load)) - 1
        
                            where:
                                * iPcr is the torsional buckling load allowable
                                * load is the axial compressive load (MS is not calculated in case of tensile load)
        
                            Hypotheses: Column cross section has two axes of symetry or is point symmetric and the shear center and centroid is coinciding.
        
                            iPcr = 1/r0^2(G*J+(E*gamma*pi^2)/(L')^2)
        
                            where:
                                * E is the Young modulus of the column material
                                * G is the shear modulus of elasticity
                                * L' is the column effective length L'=L/sqrt(C) with:
                                    * L the column length
                                    * C the end fixity coefficient depending on the Boundary Condition given at both extremities.
                                * r0 is the polar radius of gyration of the section about its shear center
                                * J is the torsion constant of the section
                                * gamma is the warping constant of the section
        
                            Input
                                L            Column effective length
                                E            Young's modulus
                                G            Shear modulus of elasticity
                                J            Torsion constant of the section
                                gamma        Warping constant of the section
                                r0           Polar radius of gyration of the section about its shear center
                                C            End fixity coefficient depending on the Boundary Condition given at both extremities
                                nblc         Number of load cases
                                load         Axial compressive load
                            Output
                                iPcr         Torsional buckling load allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, iPcr, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - iPcr is: float. Torsional buckling load allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ##  
    ##                     Computes margin of safety of a rectangular flat composite panel in buckling under compressive loads.
    ## 
    ##                     sigma_allowable is the allowable compressive stress computed as:
    ##                     'sigma_allowable = N_xcr/t' 
    ##                     where:
    ##                     * 'N_xcr' is the allowable compressive load in longitudinal direction and 
    ##                     * 't' is the total thickness of the laminate
    ##  
    ##                     A margin of safety can be derived from this formulation:
    ##                     'MS=sigma_allowable/(abs(sigma))-1  (Compression; sigma less than 0)'
    ##                     'MS=NaN (Tension; sigma greater or equal than 0)'
    ##                     Where:
    ##                     * 'sigma' is the measured compressive stress
    ## 
    ##                     the allowable compressive load depends on the boundary conditions:
    ##                     * SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
    ##                     N_xcr = pi^2*(D_11*m^4 + 2*(D_12+2*D_66)*m^2*AR^2 + D_22*AR^4)/(a^2*m^2)
    ## 
    ##                     * CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
    ##                     'N_xcr = pi^2/b^2 * sqrt(D_11*D22)*K_min'
    ##                     'K(m) = 4/lambda^2 + 2*(D_12+2*D_66)/sqrt(D_11*D_22) + 3/4*lambda^2, for lambda between 0 and 1.662'
    ##                     'K(m) = (m^4+8*m^2+1)/(lambda^2*(m^2+1)) + 2*(D_12+2*D_66)/sqrt(D_11*D_22) + lambda^2/(m^2+1), for lambda larger than 1.662'
    ## 
    ##                     * SCSC (loaded edges: simply supported, unloaded edges: clamped - clamped)
    ##                     'N_xcr = pi^2/b^2*sqrt(D_11*D_22)*K_min'
    ##                     'K = m^2/lambda^2 + 2*(D_12+2*D_66)/sqrt(D_11*D_22) + 16/3*lambda^2/m^2'
    ## 
    ##                     * CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
    ##                     'N_xcr = pi^2/b^2*sqrt(D_11*D22)*K_min'
    ##                     'K(m) = 4/lambda^2 + (8*(D_12+2*D_66))/(3*sqrt(D_11*D_22 )) + 4*lambda^2, for lambda between 0 and 1.094'
    ##                     'K(m) = (m^4+8*m^2+1)/(lambda^2*(m^2+1)) + (2*(D_12+2*D_66))/sqrt(D_11*D_22) + lambda^2/(m^2+1), for lambda larger than 1.094'
    ## 
    ##                     * SFSS (loaded edges: simply supported, unloaded edges: free - simply supported)
    ##                     'N_xcr = pi^2/b^2*sqrt(D_11*D22)*K_min'
    ##                     'K(m) = 12/pi^2*D_66/sqrt(D_11*D22) + 1/lambda^2'
    ## 
    ##                     Where:
    ##                     * 'a' is the unloaded edge length
    ##                     * 'b' is the loaded edge length
    ##                     * 'AR =a/b' is the length to width ratio
    ##                     * 'D_ij' are the equivalent flexural stiffenesses of the laminate
    ##                     * 'lambda' is obtained from 'lambda = AR*(D_22/D_11)^(1/4)'
    ##                     * 'K = K(m) is the buckling coefficient
    ##                     * 'm' is the longitudinal half-waves number (buckling mode)
    ##                     * 'Kmin' is the minimum value of K(m) for m integer.
    ##                 
    ##                     Input
    ##                         b               Loaded edge length
    ##                         a               Unloaded edge length
    ##                         bc              Edges boundary conditions {SSSS; CSCS; SCSC; CCCC; SFSS}
    ##                         laminate        Laminate
    ##                         sigma           Compressive Stress
    ##                     Output
    ##                         MS              Margin of safety
    ##                         sigmaAllowable  Allowable compressive stress indexed by failure mode
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmaAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmaAllowable is: float. Compressive stress allowable .

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsCompositePlateBucklingFlatCompressive(abbContext: AbbContext, b: float, a: float, bc: ABB.PlaneStressBoundaryConditions, laminate: NXOpen.CAE.AeroStructures.Laminate, sigma: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
         
                            Computes margin of safety of a rectangular flat composite panel in buckling under compressive loads.
        
                            sigma_allowable is the allowable compressive stress computed as:
                            'sigma_allowable = N_xcr/t' 
                            where:
                            * 'N_xcr' is the allowable compressive load in longitudinal direction and 
                            * 't' is the total thickness of the laminate
         
                            A margin of safety can be derived from this formulation:
                            'MS=sigma_allowable/(abs(sigma))-1  (Compression; sigma less than 0)'
                            'MS=NaN (Tension; sigma greater or equal than 0)'
                            Where:
                            * 'sigma' is the measured compressive stress
        
                            the allowable compressive load depends on the boundary conditions:
                            * SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
                            N_xcr = pi^2*(D_11*m^4 + 2*(D_12+2*D_66)*m^2*AR^2 + D_22*AR^4)/(a^2*m^2)
        
                            * CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
                            'N_xcr = pi^2/b^2 * sqrt(D_11*D22)*K_min'
                            'K(m) = 4/lambda^2 + 2*(D_12+2*D_66)/sqrt(D_11*D_22) + 3/4*lambda^2, for lambda between 0 and 1.662'
                            'K(m) = (m^4+8*m^2+1)/(lambda^2*(m^2+1)) + 2*(D_12+2*D_66)/sqrt(D_11*D_22) + lambda^2/(m^2+1), for lambda larger than 1.662'
        
                            * SCSC (loaded edges: simply supported, unloaded edges: clamped - clamped)
                            'N_xcr = pi^2/b^2*sqrt(D_11*D_22)*K_min'
                            'K = m^2/lambda^2 + 2*(D_12+2*D_66)/sqrt(D_11*D_22) + 16/3*lambda^2/m^2'
        
                            * CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
                            'N_xcr = pi^2/b^2*sqrt(D_11*D22)*K_min'
                            'K(m) = 4/lambda^2 + (8*(D_12+2*D_66))/(3*sqrt(D_11*D_22 )) + 4*lambda^2, for lambda between 0 and 1.094'
                            'K(m) = (m^4+8*m^2+1)/(lambda^2*(m^2+1)) + (2*(D_12+2*D_66))/sqrt(D_11*D_22) + lambda^2/(m^2+1), for lambda larger than 1.094'
        
                            * SFSS (loaded edges: simply supported, unloaded edges: free - simply supported)
                            'N_xcr = pi^2/b^2*sqrt(D_11*D22)*K_min'
                            'K(m) = 12/pi^2*D_66/sqrt(D_11*D22) + 1/lambda^2'
        
                            Where:
                            * 'a' is the unloaded edge length
                            * 'b' is the loaded edge length
                            * 'AR =a/b' is the length to width ratio
                            * 'D_ij' are the equivalent flexural stiffenesses of the laminate
                            * 'lambda' is obtained from 'lambda = AR*(D_22/D_11)^(1/4)'
                            * 'K = K(m) is the buckling coefficient
                            * 'm' is the longitudinal half-waves number (buckling mode)
                            * 'Kmin' is the minimum value of K(m) for m integer.
                        
                            Input
                                b               Loaded edge length
                                a               Unloaded edge length
                                bc              Edges boundary conditions {SSSS; CSCS; SCSC; CCCC; SFSS}
                                laminate        Laminate
                                sigma           Compressive Stress
                            Output
                                MS              Margin of safety
                                sigmaAllowable  Allowable compressive stress indexed by failure mode
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmaAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Compressive stress allowable .

        """
        pass
    
    ##  
    ##                     Computes margin of safety of a rectangular flat composite panel in buckling under combined shear and longitudinal loads.
    ## 
    ##                     Under longitudinal and shear loads, the interaction equation is:
    ##                     'R_L + R_S^(1.9+0.1*beta) = 1'
    ## 
    ##                     Where:
    ##                     * 'R_L = sigma/sigma_cr' is the stress ratio due to longitudinal stress
    ##                         * 'sigma' is the given longitudinal stress
    ##                         * 'sigma_cr' is the compression stress allowable for buckling, as computed by method MS_Composite_PlateBuckling_FlatCompressive
    ##                     * 'R_S = tau/tau_cr' is the critical ratio of buckling coefficients due to shear stress
    ##                         * 'tau' the given shear stress
    ##                         * 'tau_cr' the shear stress allowable for buckling as computed by method MS_Composite_PlateBuckling_FlatShear
    ##                     * 'beta = (D_12+2*D_66)/sqrt(D_11*D_22)' is a non-dimensional orthotropic material parameter defined by the interaction equation
    ##                     * 'D_ij' are the equivalent flexural stiffenesses of the laminate
    ## 
    ##                     The following boundary conditions are supported:
    ##                     * SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
    ##                     * CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
    ##                     * CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
    ## 
    ##                     Input
    ##                         b               Loaded edge length
    ##                         a               Unloaded edge length
    ##                         bc              Edges boundary conditions {SSSS; CSCS; CCCC}
    ##                         laminate        Laminate
    ##                         sigma           Compressive Stress
    ##                         tau             Shear Stress
    ##                     Output
    ##                         sigmaAllowable  Allowable compressive stress
    ##                         tauAllowable    Allowable shear stress
    ##                         MS              Margin of safety
    ##                     Return
    ##                     Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmaAllowable, tauAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmaAllowable is: float. Compressive stress allowable .
    ##  - tauAllowable is: float. Shear stress allowable .

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsCompositePlateBucklingFlatLongitudinalShearCombined(abbContext: AbbContext, b: float, a: float, bc: ABB.PlaneStressBoundaryConditions, laminate: NXOpen.CAE.AeroStructures.Laminate, sigma: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
         
                            Computes margin of safety of a rectangular flat composite panel in buckling under combined shear and longitudinal loads.
        
                            Under longitudinal and shear loads, the interaction equation is:
                            'R_L + R_S^(1.9+0.1*beta) = 1'
        
                            Where:
                            * 'R_L = sigma/sigma_cr' is the stress ratio due to longitudinal stress
                                * 'sigma' is the given longitudinal stress
                                * 'sigma_cr' is the compression stress allowable for buckling, as computed by method MS_Composite_PlateBuckling_FlatCompressive
                            * 'R_S = tau/tau_cr' is the critical ratio of buckling coefficients due to shear stress
                                * 'tau' the given shear stress
                                * 'tau_cr' the shear stress allowable for buckling as computed by method MS_Composite_PlateBuckling_FlatShear
                            * 'beta = (D_12+2*D_66)/sqrt(D_11*D_22)' is a non-dimensional orthotropic material parameter defined by the interaction equation
                            * 'D_ij' are the equivalent flexural stiffenesses of the laminate
        
                            The following boundary conditions are supported:
                            * SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
                            * CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
                            * CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
        
                            Input
                                b               Loaded edge length
                                a               Unloaded edge length
                                bc              Edges boundary conditions {SSSS; CSCS; CCCC}
                                laminate        Laminate
                                sigma           Compressive Stress
                                tau             Shear Stress
                            Output
                                sigmaAllowable  Allowable compressive stress
                                tauAllowable    Allowable shear stress
                                MS              Margin of safety
                            Return
                            Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmaAllowable, tauAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Compressive stress allowable .
         - tauAllowable is: float. Shear stress allowable .

        """
        pass
    
    ##  
    ##                     Computes margin of safety of a rectangular flat composite panel in buckling under shear loads.
    ## 
    ##                     The MS is calculated by the formula:
    ##                     'MS = sigma_Allowable/(abs(tau)) - 1'
    ## 
    ##                     Where:
    ##                     * 'tau_allowable=N_xycr/t' is the allowable shear stress
    ##                     * 'tau' is the shear stress
    ##                     * 'N_xycr = (k_s*pi^2)/b^2*(D_11*D_22^3)^(1/4)' is the allowable shear load
    ##                     * 't' is the total thickness of the laminate
    ##                     * 'b' is the first edge length
    ##                     * 'a' is the second edge length
    ##                     * 'D_ij' are the equivalent flexural stiffenesses of the laminate
    ##                     * 'theta=sqrt(D_11*D_22)/(D_12+2*D_66)'
    ##                     * 'B = b/a*(D_11/D_22)^(1/4)'
    ## 
    ##                     The shear buckling coefficient k_s is expressed in terms of two non-dimensional parameters theta and B as a 
    ##                     function of the aspect ratio and the orthotropic bending stiffnesses. The value depends on the boundary conditions:
    ## 
    ##                     * SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
    ##                     'k_s = 3.32 + 2.17/theta - 0.163/theta^2 + B^2*(1.54+2.36/theta+0.1/theta^2)'
    ## 
    ##                     * CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
    ##                     'k_s(theta,B)' is interpolated from a 2D table of values
    ## 
    ##                     * CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
    ##                     'k_s(theta,B)' is interpolated from a 2D table of values
    ## 
    ##                      Input
    ##                         b             First edge length
    ##                         a             Second edge length
    ##                         bc            Edges boundary conditions {SSSS; CSCS; CCCC}
    ##                         laminate      Laminate
    ##                         sigma         Compressive Stress
    ##                     Output
    ##                         MS            Margin of safety
    ##                         tauAllowable  Allowable shear stress indexed by failure mode
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, tauAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - tauAllowable is: float. Shear stress allowable .

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsCompositePlateBucklingFlatShear(abbContext: AbbContext, b: float, a: float, bc: ABB.PlaneStressBoundaryConditions, laminate: NXOpen.CAE.AeroStructures.Laminate, tau: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
         
                            Computes margin of safety of a rectangular flat composite panel in buckling under shear loads.
        
                            The MS is calculated by the formula:
                            'MS = sigma_Allowable/(abs(tau)) - 1'
        
                            Where:
                            * 'tau_allowable=N_xycr/t' is the allowable shear stress
                            * 'tau' is the shear stress
                            * 'N_xycr = (k_s*pi^2)/b^2*(D_11*D_22^3)^(1/4)' is the allowable shear load
                            * 't' is the total thickness of the laminate
                            * 'b' is the first edge length
                            * 'a' is the second edge length
                            * 'D_ij' are the equivalent flexural stiffenesses of the laminate
                            * 'theta=sqrt(D_11*D_22)/(D_12+2*D_66)'
                            * 'B = b/a*(D_11/D_22)^(1/4)'
        
                            The shear buckling coefficient k_s is expressed in terms of two non-dimensional parameters theta and B as a 
                            function of the aspect ratio and the orthotropic bending stiffnesses. The value depends on the boundary conditions:
        
                            * SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
                            'k_s = 3.32 + 2.17/theta - 0.163/theta^2 + B^2*(1.54+2.36/theta+0.1/theta^2)'
        
                            * CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
                            'k_s(theta,B)' is interpolated from a 2D table of values
        
                            * CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
                            'k_s(theta,B)' is interpolated from a 2D table of values
        
                             Input
                                b             First edge length
                                a             Second edge length
                                bc            Edges boundary conditions {SSSS; CSCS; CCCC}
                                laminate      Laminate
                                sigma         Compressive Stress
                            Output
                                MS            Margin of safety
                                tauAllowable  Allowable shear stress indexed by failure mode
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, tauAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - tauAllowable is: float. Shear stress allowable .

        """
        pass
    
    ##  
    ##                     MS Inter-rivet buckling (Column)
    ## 
    ##                     Computes margin of safety of inter-rivet buckling (theory coming from Euler column theory)
    ## 
    ##                     MS = sigmacr / (abs(sigma)) - 1
    ## 
    ##                     where:
    ##                         * sigmacr is the inter-rivet buckling stress allowable
    ##                         * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
    ## 
    ##                     Inter-rivet buckling stress allowable (sigmacr) assumes that sheet between adjacent rivets acts as a **column**.
    ## 
    ##                     The formula (derived from Euler theory) is:
    ##                         * sigmacr=(Pi^2E)/(p/sqrt(C)/0.29t)^2 if material is considered as elastic (Material behaviour = Elastic)
    ##                         * sigmacr=(Pi^2Et)/(p/sqrt(C)/0.29t)^2 if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic). This formulation is a derivation of tangent modulus therory (Engesser).
    ## 
    ##                     where:
    ##                         * Et is the tangent modulus given by Et=sigma/((sigma/E)+0.002*n*(sigma/fy)^n)) with
    ##                             * sigma is the stress
    ##                             * fy is the yield stress
    ##                             * E is the Young's modulus
    ##                             * n is the Ramberg-Osgood parameter
    ##                         * E is the Young's modulus
    ##                         * p is the the rivet spacing
    ##                         * t is the thickness of sheet
    ##                         * C is the end fixity coefficient
    ##                             * Universal head (or flat head) - C = 4
    ##                             * Brazier head - C = 3
    ##                             * Countersunk rivet - C = 1
    ##                             * Spotwelds - C = 3.5
    ## 
    ##                     Input
    ##                         t            Sheet thickness
    ##                         p            Rivet spacing
    ##                         behaviour    Material behaviour
    ##                         E            Young's Modulus
    ##                         iFy          Compressive yield stress
    ##                         n            Ramberg-Osgood coefficient
    ##                         C            End fixity coefficient
    ##                         nblc         Number of load cases
    ##                         sigma        Stress
    ##                     Output
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The ABB context 
    @staticmethod
    def MsInterrivetbucklingColumn(abbContext: AbbContext, t: float, p: float, behaviour: ABB.MaterialBehaviour, E: float, iFy: float, n: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
         
                            MS Inter-rivet buckling (Column)
        
                            Computes margin of safety of inter-rivet buckling (theory coming from Euler column theory)
        
                            MS = sigmacr / (abs(sigma)) - 1
        
                            where:
                                * sigmacr is the inter-rivet buckling stress allowable
                                * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
        
                            Inter-rivet buckling stress allowable (sigmacr) assumes that sheet between adjacent rivets acts as a **column**.
        
                            The formula (derived from Euler theory) is:
                                * sigmacr=(Pi^2E)/(p/sqrt(C)/0.29t)^2 if material is considered as elastic (Material behaviour = Elastic)
                                * sigmacr=(Pi^2Et)/(p/sqrt(C)/0.29t)^2 if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic). This formulation is a derivation of tangent modulus therory (Engesser).
        
                            where:
                                * Et is the tangent modulus given by Et=sigma/((sigma/E)+0.002*n*(sigma/fy)^n)) with
                                    * sigma is the stress
                                    * fy is the yield stress
                                    * E is the Young's modulus
                                    * n is the Ramberg-Osgood parameter
                                * E is the Young's modulus
                                * p is the the rivet spacing
                                * t is the thickness of sheet
                                * C is the end fixity coefficient
                                    * Universal head (or flat head) - C = 4
                                    * Brazier head - C = 3
                                    * Countersunk rivet - C = 1
                                    * Spotwelds - C = 3.5
        
                            Input
                                t            Sheet thickness
                                p            Rivet spacing
                                behaviour    Material behaviour
                                E            Young's Modulus
                                iFy          Compressive yield stress
                                n            Ramberg-Osgood coefficient
                                C            End fixity coefficient
                                nblc         Number of load cases
                                sigma        Stress
                            Output
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ##  
    ##                     MS Inter-rivet buckling (wide column)
    ## 
    ##                     Computes margin of safety of inter-rivet buckling (theory  based on plate buckling - wide column assumption)
    ## 
    ##                     MS = sigmacr / abs(sigma) - 1
    ## 
    ##                     where:
    ## 
    ##                     * sigmacr is the inter-rivet buckling stress allowable
    ##                     * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
    ## 
    ##                     Inter-rivet buckling stress allowable (sigmacr) assumes that the sheet acts as a **wide column** at its ends and whose length is equal to the rivet spacing.
    ## 
    ##                     The formula (derived from buckling plate theory) is: sigmacr=(C pi^2eta E)/(12 (1-nu^2))(t/p)^2
    ## 
    ##                     where:
    ##                         * E is the young's modulus
    ##                         * eta is the clad correction factor (supposed to be equal to 1)
    ##                         * nu is the Poisson coefficient
    ##                         * t is the thickness of the sheet
    ##                         * p is the the rivet spacing
    ##                         * C is the end fixity coefficient
    ##                             * Universal head (or flat head) - `C` = 4
    ##                             * Brazier head - `C` = 3
    ##                             * Countersunk rivet - `C` = 1
    ##                             * Spotwelds - `C` = 3.5
    ##                         * eta is the plasticity reduction factor: sigmacr(Plastic)=eta.sigmacr(Elastic)
    ##                         * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
    ##                         * eta is obtain from following charts sigmacr(Plastic))/sigma(0.7)=f(sigmacr(Elastic)/sigma(0.7)) if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
    ##                             with: sigma(0.7) is the stress for secant modulus equal to 70% of Young modulus
    ##             
    ##                     Input
    ##                         t            Sheet thickness
    ##                         p            Rivet pitch
    ##                         behaviour    Material behaviour
    ##                         E            Young's Modulus
    ##                         nu           Elastic Poisson's ratio
    ##                         n            Ramberg-Osgood coefficient
    ##                         iFy          Yield Stress Allowable
    ##                         C            End fixity coefficient
    ##                         nblc         Number of load cases
    ##                         sigma        Stress
    ##                     Output
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    ##  The ABB context 
    @staticmethod
    def MsInterrivetbucklingWidecolumn(abbContext: AbbContext, t: float, p: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
         
                            MS Inter-rivet buckling (wide column)
        
                            Computes margin of safety of inter-rivet buckling (theory  based on plate buckling - wide column assumption)
        
                            MS = sigmacr / abs(sigma) - 1
        
                            where:
        
                            * sigmacr is the inter-rivet buckling stress allowable
                            * sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
        
                            Inter-rivet buckling stress allowable (sigmacr) assumes that the sheet acts as a **wide column** at its ends and whose length is equal to the rivet spacing.
        
                            The formula (derived from buckling plate theory) is: sigmacr=(C pi^2eta E)/(12 (1-nu^2))(t/p)^2
        
                            where:
                                * E is the young's modulus
                                * eta is the clad correction factor (supposed to be equal to 1)
                                * nu is the Poisson coefficient
                                * t is the thickness of the sheet
                                * p is the the rivet spacing
                                * C is the end fixity coefficient
                                    * Universal head (or flat head) - `C` = 4
                                    * Brazier head - `C` = 3
                                    * Countersunk rivet - `C` = 1
                                    * Spotwelds - `C` = 3.5
                                * eta is the plasticity reduction factor: sigmacr(Plastic)=eta.sigmacr(Elastic)
                                * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                                * eta is obtain from following charts sigmacr(Plastic))/sigma(0.7)=f(sigmacr(Elastic)/sigma(0.7)) if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
                                    with: sigma(0.7) is the stress for secant modulus equal to 70% of Young modulus
                    
                            Input
                                t            Sheet thickness
                                p            Rivet pitch
                                behaviour    Material behaviour
                                E            Young's Modulus
                                nu           Elastic Poisson's ratio
                                n            Ramberg-Osgood coefficient
                                iFy          Yield Stress Allowable
                                C            End fixity coefficient
                                nblc         Number of load cases
                                sigma        Stress
                            Output
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Net section
    ##                     Computes margin of net section (due to bolt hole)
    ## 
    ##                     The formula is MS = PNetSectionAllowable / P - 1
    ## 
    ##                     where:
    ##                     * 'PNetSectionAllowable' is the net section load allowable.
    ##                         PNetSectionAllowable = SigmaAllowable * t * ( b - D )
    ##                         * 'SigmaAllowable' is the material stress allowable. For instance, it could be Ftu
    ##                         * 'D'    is the hole diameter
    ##                         * 't' is the thickness
    ##                         * 'b' is the width of the net section
    ## 
    ##                     * 'P' is the load.
    ##                         P = FactorLoad * PExtracted
    ##                         * 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
    ##                         * 'PExtracted' is the extracted load
    ## 
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Input
    ##                         D                     Diameter
    ##                         b                     Width
    ##                         t                     Thickness
    ##                         Fx                    Material stress allowable
    ##                         f                     Load factor
    ##                         P(nblc)               Axial load
    ##                     Output
    ##                         MS                    Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsNetSection(abbContext: AbbContext, D: float, b: float, t: float, iFx: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS Net section
                            Computes margin of net section (due to bolt hole)
        
                            The formula is MS = PNetSectionAllowable / P - 1
        
                            where:
                            * 'PNetSectionAllowable' is the net section load allowable.
                                PNetSectionAllowable = SigmaAllowable * t * ( b - D )
                                * 'SigmaAllowable' is the material stress allowable. For instance, it could be Ftu
                                * 'D'    is the hole diameter
                                * 't' is the thickness
                                * 'b' is the width of the net section
        
                            * 'P' is the load.
                                P = FactorLoad * PExtracted
                                * 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
                                * 'PExtracted' is the extracted load
        
                            * 'MS' is the margin of safety
        
                            Input
                                D                     Diameter
                                b                     Width
                                t                     Thickness
                                Fx                    Material stress allowable
                                f                     Load factor
                                P(nblc)               Axial load
                            Output
                                MS                    Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling
    ##                     Computes margin of safety of a metallic plate under buckling load (generic formula)
    ## 
    ##                     The formula is MS = Allowable / Stress - 1
    ## 
    ##                     where:
    ##                     * 'Allowable' is the compressive buckling stress allowable
    ##                     * 'Stress' is the stress
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Allowable = eta * PI^2*k*E/(12*(1-nu^2)) * (t/b)^2
    ##                     where
    ##                     * 'k' is the buckling coefficient
    ##                     * 'E' is the Young's modulus
    ##                     * 'nu' is the elastic Poisson's ratio
    ##                     * 't' is the panel thickness
    ##                     * 'b' is the panel dimension
    ##                     * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
    ## 
    ##                     Input
    ##                         b        Panel's dimension
    ##                         t        Panel's thickness
    ##                         E        Young's modulus
    ##                         nu       Elastic Poisson's ratio
    ##                         eta      Plasticity reduction factor
    ##                         k        Buckling coefficient
    ##                         nblc     Number of load cases
    ##                         sigma    Compressive stress
    ##                     Output
    ##                         MS       Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBuckling(abbContext: AbbContext, b: float, t: float, E: float, nu: float, eta: float, k: float, sigma: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS Plate Buckling
                            Computes margin of safety of a metallic plate under buckling load (generic formula)
        
                            The formula is MS = Allowable / Stress - 1
        
                            where:
                            * 'Allowable' is the compressive buckling stress allowable
                            * 'Stress' is the stress
                            * 'MS' is the margin of safety
        
                            Allowable = eta * PI^2*k*E/(12*(1-nu^2)) * (t/b)^2
                            where
                            * 'k' is the buckling coefficient
                            * 'E' is the Young's modulus
                            * 'nu' is the elastic Poisson's ratio
                            * 't' is the panel thickness
                            * 'b' is the panel dimension
                            * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
        
                            Input
                                b        Panel's dimension
                                t        Panel's thickness
                                E        Young's modulus
                                nu       Elastic Poisson's ratio
                                eta      Plasticity reduction factor
                                k        Buckling coefficient
                                nblc     Number of load cases
                                sigma    Compressive stress
                            Output
                                MS       Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Curved Compressive
    ##                     Computes margin of safety of a curved metallic rectangular panel under compressive load
    ## 
    ##                     The formula is MS = Allowable / |Stress| - 1
    ## 
    ##                     where:
    ##                     * 'Allowable' is the compressive buckling stress allowable
    ##                     * 'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Allowable = eta * PI^2*kc*E/(12*(1-nu^2)) * (t/c)^2
    ##                     where
    ##                     * 'kc' is the buckling coefficient
    ##                     * 'E' is the Young's modulus
    ##                     * 'nu' is the elastic Poisson's ratio
    ##                     * 't' is the panel thickness
    ##                     * 'c' is the shorter panel dimension c = min(a,b)
    ##                     * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
    ##                     * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
    ##                     * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
    ## 
    ##                     SigmaAllowablePlastic/F0.7 = f(SigmaAllowableElastic/F0.7)
    ## 
    ##                     MetallicPanelCompressivePlasticityCurveBC3 with F0.7 is the stress for secant modulus equal to 70% of Young's modulus
    ## 
    ##                     Input
    ##                         b               Loaded edge length
    ##                         a               Unloaded edge length
    ##                         t               Panel thickness
    ##                         r               Panel radius of curvature
    ##                         behaviour       Material behaviour
    ##                         E               Young's modulus
    ##                         nu              Elastic Poisson's ratio
    ##                         n               Ramberg-Osgood parameter
    ##                         iFy             Yield stress Allowable
    ##                         nblc            Number of load cases
    ##                         sigma           Compressive stress
    ##                     Output
    ##                         sigmaAllowable  Stress allowable
    ##                         MS              Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmaAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmaAllowable is: float. Stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingCurvedCompressive(abbContext: AbbContext, b: float, a: float, t: float, r: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
        
                            MS Plate Buckling Curved Compressive
                            Computes margin of safety of a curved metallic rectangular panel under compressive load
        
                            The formula is MS = Allowable / |Stress| - 1
        
                            where:
                            * 'Allowable' is the compressive buckling stress allowable
                            * 'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
                            * 'MS' is the margin of safety
        
                            Allowable = eta * PI^2*kc*E/(12*(1-nu^2)) * (t/c)^2
                            where
                            * 'kc' is the buckling coefficient
                            * 'E' is the Young's modulus
                            * 'nu' is the elastic Poisson's ratio
                            * 't' is the panel thickness
                            * 'c' is the shorter panel dimension c = min(a,b)
                            * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
                            * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                            * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
                            SigmaAllowablePlastic/F0.7 = f(SigmaAllowableElastic/F0.7)
        
                            MetallicPanelCompressivePlasticityCurveBC3 with F0.7 is the stress for secant modulus equal to 70% of Young's modulus
        
                            Input
                                b               Loaded edge length
                                a               Unloaded edge length
                                t               Panel thickness
                                r               Panel radius of curvature
                                behaviour       Material behaviour
                                E               Young's modulus
                                nu              Elastic Poisson's ratio
                                n               Ramberg-Osgood parameter
                                iFy             Yield stress Allowable
                                nblc            Number of load cases
                                sigma           Compressive stress
                            Output
                                sigmaAllowable  Stress allowable
                                MS              Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmaAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Stress allowable .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Curved Longitudinal Shear Combined
    ##                     Computes margin of safety of a rectangular curved metallic panel in buckling under combined shear and longitudinal loads
    ## 
    ##                     Under compressive loads
    ## 
    ##                     Under compressive and shear loads, the interaction equation is:
    ##                     RL^2 + RS^2 = 1.0
    ## 
    ##                     The Margin Safety is given by the following formula:
    ## 
    ##                     MS=2/(RL+sqrt(RL^2+4*RS^2))-1
    ##                     where:
    ## 
    ##                     * RL = sigma / sigma_cr is the stress ratio due to longitudinal stress, with:
    ##                     * sigma is the given longitudinal stress
    ##                     * sigma_cr is the compression stress allowable for buckling (sigma_cr &lt; 0, as consequence RL &lt; 0 in tension)
    ## 
    ##                     * RS = tau / tau_cr is the stress ratio due to shear stress with:
    ##                     * tau is the given shear stress
    ##                     * tau_cr is the shear stress allowable for buckling (tau and tau_cr always positive)
    ## 
    ##                     Under tensile loads
    ## 
    ##                     Under tensile and shear loads, the interaction equation is:
    ##                     1/2 * RL + RS = 1.0
    ## 
    ##                     The Margin Safety is given by the following formula:
    ##                     MS = (2 - RL) / ( 2 * RS ) - 1
    ## 
    ##                     The panel edges are either clamped or simply supported.
    ##                     Plasticity is not taken into account.
    ## 
    ##                     Input
    ##                         b            Loaded edge length
    ##                         a            Unloaded edge length
    ##                         BC           Support along edges ('Clamped' or 'Simply Supported')
    ##                         t            Panel thickness
    ##                         r            Panel radius of curvature
    ##                         behaviour    Material behaviour ('Elastic' or 'Elastic-Plastic')
    ##                         E            Young's modulus
    ##                         nu           Elastic Poisson's ratio
    ##                         n            Ramberg-Osgood parameter
    ##                         iFy          Yield Stress Allowable
    ##                         nblc         Number of load cases
    ##                         sigma        Compressive stress
    ##                         tau          Shear stress
    ##                     Output
    ##                         MS           Margin of safety
    ##                         sigmacr      Compressive stress allowable
    ##                         taucr        Shear stress allowable
    ## 
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmacr, taucr). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmacr is: float. Compressive stress allowable .
    ##  - taucr is: float. Shear stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingCurvedLongitudinalShearCombined(abbContext: AbbContext, b: float, a: float, bc: ABB.EdgeSupportType, t: float, r: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
        
                            MS Plate Buckling Curved Longitudinal Shear Combined
                            Computes margin of safety of a rectangular curved metallic panel in buckling under combined shear and longitudinal loads
        
                            Under compressive loads
        
                            Under compressive and shear loads, the interaction equation is:
                            RL^2 + RS^2 = 1.0
        
                            The Margin Safety is given by the following formula:
        
                            MS=2/(RL+sqrt(RL^2+4*RS^2))-1
                            where:
        
                            * RL = sigma / sigma_cr is the stress ratio due to longitudinal stress, with:
                            * sigma is the given longitudinal stress
                            * sigma_cr is the compression stress allowable for buckling (sigma_cr &lt; 0, as consequence RL &lt; 0 in tension)
        
                            * RS = tau / tau_cr is the stress ratio due to shear stress with:
                            * tau is the given shear stress
                            * tau_cr is the shear stress allowable for buckling (tau and tau_cr always positive)
        
                            Under tensile loads
        
                            Under tensile and shear loads, the interaction equation is:
                            1/2 * RL + RS = 1.0
        
                            The Margin Safety is given by the following formula:
                            MS = (2 - RL) / ( 2 * RS ) - 1
        
                            The panel edges are either clamped or simply supported.
                            Plasticity is not taken into account.
        
                            Input
                                b            Loaded edge length
                                a            Unloaded edge length
                                BC           Support along edges ('Clamped' or 'Simply Supported')
                                t            Panel thickness
                                r            Panel radius of curvature
                                behaviour    Material behaviour ('Elastic' or 'Elastic-Plastic')
                                E            Young's modulus
                                nu           Elastic Poisson's ratio
                                n            Ramberg-Osgood parameter
                                iFy          Yield Stress Allowable
                                nblc         Number of load cases
                                sigma        Compressive stress
                                tau          Shear stress
                            Output
                                MS           Margin of safety
                                sigmacr      Compressive stress allowable
                                taucr        Shear stress allowable
        
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmacr, taucr). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmacr is: float. Compressive stress allowable .
         - taucr is: float. Shear stress allowable .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Curved Shear
    ##                     Computes margin of safety of a curved metallic rectangular panel under shear load
    ## 
    ##                     The formula is MS = Allowable / |Stress| - 1
    ## 
    ##                     where:
    ##                     * 'Allowable' is the compressive buckling stress allowable
    ##                     * 'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Allowable = eta * PI^2*ks*E/(12*(1-nu^2)) * (t/c)^2
    ##                     where
    ##                     * 'ks' is the buckling coefficient
    ##                     * 'E' is the Young's modulus
    ##                     * 'nu' is the elastic Poisson's ratio
    ##                     * 't' is the panel thickness
    ##                     * 'c' is the shorter panel dimension c = min(a,b)
    ##                     * 'eta' is the plasticity reduction factor: TauAllowablePlastic = eta*TauAllowableElastic
    ##                     * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
    ##                     * eta is obtained from the MetallicPanelCompressivePlasticityCurveBC1 charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
    ##                         * TauAllowablePlastic/F0.7 = f(TauAllowableElastic/F0.7)
    ##                         * F0.7 is the stress for secant modulus equal to 70% of Young's modulus
    ## 
    ##                     Input
    ##                         b               Dimension in radial axis
    ##                         a               Dimension in longitudinal axis
    ##                         BC              Support along edges
    ##                         t               Panel thickness
    ##                         r               Panel radius of curvature
    ##                         behaviour       Material behaviour
    ##                         E               Young's modulus
    ##                         nu              Elastic Poisson's ratio
    ##                         n               Ramberg-Osgood parameter
    ##                         iFy             Yield Stress Allowable
    ##                         nblc            Number of load cases
    ##                         tau             Shear stress
    ##                     Output
    ##                         tauAllowable    Stress allowable
    ##                         MS              Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, tauAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - tauAllowable is: float. Stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingCurvedShear(abbContext: AbbContext, b: float, a: float, bc: ABB.EdgeSupportType, t: float, r: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, tau: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
        
                            MS Plate Buckling Curved Shear
                            Computes margin of safety of a curved metallic rectangular panel under shear load
        
                            The formula is MS = Allowable / |Stress| - 1
        
                            where:
                            * 'Allowable' is the compressive buckling stress allowable
                            * 'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
                            * 'MS' is the margin of safety
        
                            Allowable = eta * PI^2*ks*E/(12*(1-nu^2)) * (t/c)^2
                            where
                            * 'ks' is the buckling coefficient
                            * 'E' is the Young's modulus
                            * 'nu' is the elastic Poisson's ratio
                            * 't' is the panel thickness
                            * 'c' is the shorter panel dimension c = min(a,b)
                            * 'eta' is the plasticity reduction factor: TauAllowablePlastic = eta*TauAllowableElastic
                            * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                            * eta is obtained from the MetallicPanelCompressivePlasticityCurveBC1 charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
                                * TauAllowablePlastic/F0.7 = f(TauAllowableElastic/F0.7)
                                * F0.7 is the stress for secant modulus equal to 70% of Young's modulus
        
                            Input
                                b               Dimension in radial axis
                                a               Dimension in longitudinal axis
                                BC              Support along edges
                                t               Panel thickness
                                r               Panel radius of curvature
                                behaviour       Material behaviour
                                E               Young's modulus
                                nu              Elastic Poisson's ratio
                                n               Ramberg-Osgood parameter
                                iFy             Yield Stress Allowable
                                nblc            Number of load cases
                                tau             Shear stress
                            Output
                                tauAllowable    Stress allowable
                                MS              Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, tauAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - tauAllowable is: float. Stress allowable .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Flat Bending
    ##                     Computes margin of safety of a flat metallic rectangular panel under bending load
    ## 
    ##                     The formula is MS = sigmaAllowable / abs(sigma) - 1
    ## 
    ##                     where:
    ##                     * 'sigmaAllowable' is the bending buckling stress allowable
    ##                     * 'sigma' is the compressive stress at one edge of the panel, sigma = min( sigma1, sigma2 )
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Allowable = eta * PI^2*kb*E/(12*(1-nu^2)) * (t/b)^2
    ##                     where
    ##                     * 'kb' is the bending buckling stress coefficient
    ##                     * 'E' is the Young's modulus
    ##                     * 'nu' is the elastic Poisson's ratio
    ##                     * 't' is the panel thickness
    ##                     * 'a' is the unloaded edge length
    ##                     * 'b' is the loaded edge length
    ##                     * 'beta' Loading length ratio,  the factor which, divided by b, gives the edge length in compression (while the remaining edge length is in tension).
    ##                     * 'beta' is calculated on the basis of sigma1 and sigma2 with an hypothesis of linear behaviour with the formula:
    ##                     * beta = (fc - ft) / fc where fc = min(sigma1, sigma2) and ft = max(sigma1, sigma2) )
    ##                     * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
    ##                     * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
    ##                     * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
    ## 
    ##                     SigmaAllowablePlastic/F0.7 = f(SigmaAllowableElastic/F0.7)
    ## 
    ##                     MetallicPanelCompressivePlasticityCurveBC2 with F0.7 is the stress for secant modulus equal to 70% of Young's modulus
    ##                     Input
    ##                         b                       Loaded edge length
    ##                         a                       Unloaded edge length
    ##                         t                       Panel thickness
    ##                         behaviour               Material behaviour
    ##                         E                       Young's modulus
    ##                         nu                      Elastic Poisson's ratio
    ##                         n                       Ramberg-Osgood parameter
    ##                         iFy                     Yield Stress Allowable
    ##                         beta                    Loading length ratio. If not specified (beta = NA), beta is computed
    ##                         nblc                    Number of load cases
    ##                         sigma1                  Compressive stress, side 1
    ##                         sigma2                  Compressive stress, side 2
    ##                     Output
    ##                         MS                      Margin of safety
    ##                         sigmaAllowable          Stress allowable
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmaAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmaAllowable is: List[float]. Stress allowables .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingFlatBending(abbContext: AbbContext, b: float, a: float, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, beta: float, sigma1: List[float], sigma2: List[float]) -> Tuple[ABB.Status, List[float], List[float]]:
        """
        
                            MS Plate Buckling Flat Bending
                            Computes margin of safety of a flat metallic rectangular panel under bending load
        
                            The formula is MS = sigmaAllowable / abs(sigma) - 1
        
                            where:
                            * 'sigmaAllowable' is the bending buckling stress allowable
                            * 'sigma' is the compressive stress at one edge of the panel, sigma = min( sigma1, sigma2 )
                            * 'MS' is the margin of safety
        
                            Allowable = eta * PI^2*kb*E/(12*(1-nu^2)) * (t/b)^2
                            where
                            * 'kb' is the bending buckling stress coefficient
                            * 'E' is the Young's modulus
                            * 'nu' is the elastic Poisson's ratio
                            * 't' is the panel thickness
                            * 'a' is the unloaded edge length
                            * 'b' is the loaded edge length
                            * 'beta' Loading length ratio,  the factor which, divided by b, gives the edge length in compression (while the remaining edge length is in tension).
                            * 'beta' is calculated on the basis of sigma1 and sigma2 with an hypothesis of linear behaviour with the formula:
                            * beta = (fc - ft) / fc where fc = min(sigma1, sigma2) and ft = max(sigma1, sigma2) )
                            * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
                            * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                            * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
                            SigmaAllowablePlastic/F0.7 = f(SigmaAllowableElastic/F0.7)
        
                            MetallicPanelCompressivePlasticityCurveBC2 with F0.7 is the stress for secant modulus equal to 70% of Young's modulus
                            Input
                                b                       Loaded edge length
                                a                       Unloaded edge length
                                t                       Panel thickness
                                behaviour               Material behaviour
                                E                       Young's modulus
                                nu                      Elastic Poisson's ratio
                                n                       Ramberg-Osgood parameter
                                iFy                     Yield Stress Allowable
                                beta                    Loading length ratio. If not specified (beta = NA), beta is computed
                                nblc                    Number of load cases
                                sigma1                  Compressive stress, side 1
                                sigma2                  Compressive stress, side 2
                            Output
                                MS                      Margin of safety
                                sigmaAllowable          Stress allowable
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmaAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: List[float]. Stress allowables .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Flat Compressive
    ##                     Computes margin of safety of a flat metallic rectangular panel under compressive load
    ## 
    ##                     The formula is MS = sigmaAllowable / abs(sigma) - 1
    ## 
    ##                     where:
    ##                     * 'sigmaAllowable' is the compressive buckling stress allowable,
    ##                     * 'sigma' is the compressive stress (MS is not calculated in case of tensile stress),
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Allowable = eta * PI^2*kc*E/(12*(1-nu^2)) * (t/b)^2
    ##                     where
    ##                     * 'kc' is the bending buckling stress coefficient
    ##                     * 'E' is the Young's modulus
    ##                     * 'nu' is the elastic Poisson's ratio
    ##                     * 't' is the panel thickness
    ##                     * 'a' is the unloaded edge length
    ##                     * 'b' is the loaded edge length
    ##                     * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
    ##                     * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
    ##                     * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
    ## 
    ##                     SigmaAllowablePlastic/F0.7 = f(SigmaAllowableElastic/F0.7)
    ##                     MetallicPanelCompressivePlasticityCurveBC1 if the Boundary Condition for the unloaded edges is Simply Supported-Free,
    ##                     MetallicPanelCompressivePlasticityCurveBC2 if the boundary condition for the unloaded edges is different of Simply Supported-Free
    ## 
    ##                     Input
    ##                         b               Loaded edge length
    ##                         BC_Loaded       Support along loaded edges {'Clamped';'Simply Supported'}
    ##                         a               Unloaded edge length
    ##                         BC_Unloaded     Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
    ##                         t               Panel thickness
    ##                         behaviour       Material behaviour
    ##                         E               Young's modulus
    ##                         nu              Elastic Poisson's ratio
    ##                         n               Ramberg-Osgood parameter
    ##                         iFy             Yield Stress Allowable
    ##                         nblc            Number of load cases
    ##                         sigma           Compressive stress
    ##                     Output
    ##                         sigmaAllowable  Stress allowable
    ##                         MS              Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmaAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmaAllowable is: float. Stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingFlatCompressive(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
        
                            MS Plate Buckling Flat Compressive
                            Computes margin of safety of a flat metallic rectangular panel under compressive load
        
                            The formula is MS = sigmaAllowable / abs(sigma) - 1
        
                            where:
                            * 'sigmaAllowable' is the compressive buckling stress allowable,
                            * 'sigma' is the compressive stress (MS is not calculated in case of tensile stress),
                            * 'MS' is the margin of safety
        
                            Allowable = eta * PI^2*kc*E/(12*(1-nu^2)) * (t/b)^2
                            where
                            * 'kc' is the bending buckling stress coefficient
                            * 'E' is the Young's modulus
                            * 'nu' is the elastic Poisson's ratio
                            * 't' is the panel thickness
                            * 'a' is the unloaded edge length
                            * 'b' is the loaded edge length
                            * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
                            * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                            * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
                            SigmaAllowablePlastic/F0.7 = f(SigmaAllowableElastic/F0.7)
                            MetallicPanelCompressivePlasticityCurveBC1 if the Boundary Condition for the unloaded edges is Simply Supported-Free,
                            MetallicPanelCompressivePlasticityCurveBC2 if the boundary condition for the unloaded edges is different of Simply Supported-Free
        
                            Input
                                b               Loaded edge length
                                BC_Loaded       Support along loaded edges {'Clamped';'Simply Supported'}
                                a               Unloaded edge length
                                BC_Unloaded     Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
                                t               Panel thickness
                                behaviour       Material behaviour
                                E               Young's modulus
                                nu              Elastic Poisson's ratio
                                n               Ramberg-Osgood parameter
                                iFy             Yield Stress Allowable
                                nblc            Number of load cases
                                sigma           Compressive stress
                            Output
                                sigmaAllowable  Stress allowable
                                MS              Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmaAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Stress allowable .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Flat Longitudinal Bending Combined
    ##                     Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and longitudinal loads
    ## 
    ##                     This formula is derived from the interaction equation
    ##                     Rb ^ 1.75 + Rc = 1.0
    ## 
    ##                     where:
    ##                     * Rc = sigmac / sigmacr is the stress ratio due to compression stress, with:
    ##                     * sigmac is the given longitudinal stress
    ##                     * sigmacr  is the compression stress allowable for buckling
    ## 
    ##                     * Rb = sigmab / sigmabcr is the stress ratio due to bending stress with
    ##                     * sigmab is the given compressive stress due to bending
    ##                     * sigmabcr  is the bending stress allowable for buckling
    ## 
    ##                     Input
    ##                         b            Loaded edge length
    ##                         BC_Loaded    Support along loaded edges {'Clamped';'Simply Supported'}
    ##                         a            Unloaded edge length
    ##                         BC_Unloaded  Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
    ##                         t            Panel thickness
    ##                         behaviour    Material behaviour
    ##                         E            Young's modulus
    ##                         nu           Elastic Poisson's ratio
    ##                         n            Ramberg-Osgood parameter
    ##                         iFy          Yield Stress Allowable
    ##                         beta         Loading length ratio
    ##                         nblc         Number of load cases
    ##                         sigma1       Compressive stress, side 1
    ##                         sigma2       Compressive stress, side 2
    ##                     Output
    ##                         sigmacr      Compressive stress allowable
    ##                         sigmabcr     Bending stress allowable
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmacr, sigmabcr). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmacr is: float. Compressive stress allowable .
    ##  - sigmabcr is: float. Bending stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingFlatLongitudinalBendingCombined(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma1: List[float], sigma2: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
        
                            MS Plate Buckling Flat Longitudinal Bending Combined
                            Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and longitudinal loads
        
                            This formula is derived from the interaction equation
                            Rb ^ 1.75 + Rc = 1.0
        
                            where:
                            * Rc = sigmac / sigmacr is the stress ratio due to compression stress, with:
                            * sigmac is the given longitudinal stress
                            * sigmacr  is the compression stress allowable for buckling
        
                            * Rb = sigmab / sigmabcr is the stress ratio due to bending stress with
                            * sigmab is the given compressive stress due to bending
                            * sigmabcr  is the bending stress allowable for buckling
        
                            Input
                                b            Loaded edge length
                                BC_Loaded    Support along loaded edges {'Clamped';'Simply Supported'}
                                a            Unloaded edge length
                                BC_Unloaded  Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
                                t            Panel thickness
                                behaviour    Material behaviour
                                E            Young's modulus
                                nu           Elastic Poisson's ratio
                                n            Ramberg-Osgood parameter
                                iFy          Yield Stress Allowable
                                beta         Loading length ratio
                                nblc         Number of load cases
                                sigma1       Compressive stress, side 1
                                sigma2       Compressive stress, side 2
                            Output
                                sigmacr      Compressive stress allowable
                                sigmabcr     Bending stress allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmacr, sigmabcr). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmacr is: float. Compressive stress allowable .
         - sigmabcr is: float. Bending stress allowable .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Flat Longitudinal Shear Combined
    ##                     Computes margin of safety of a rectangular flat metallic panel in buckling under combined shear and longitudinal loads
    ## 
    ##                     Under longitudinal and shear loads, the interaction equation is:
    ##                     MS=2/(RL + sqrt(RL ^ 2 + 4 * RS ^ 2)
    ## 
    ##                     This formula is derived from the interaction equation RL+R2S=1.0
    ##                     RL + RS ^ 2 = 1.0
    ## 
    ##                     where:
    ##                         * RL = sigma / sigmacr is the stress ratio due to longitudinal stress, with:
    ##                         * sigma is the given longitudinal stress
    ##                         * sigmacr is the compression stress allowable for buckling (sigmacr &lt; 0, as consequence RL &lt; 0 in tension)
    ##                         * RS = tau / taucr is the stress ratio due to shear stress with
    ##                         * tau is the given shear stress
    ##                         * taucr is the shear stress allowable for buckling (taucr and tau always positive)
    ## 
    ##                         The panel edges are either clamped or simply supported.
    ## 
    ##                     Input
    ##                         b            Loaded edge length
    ##                         BC_Loaded    Support along loaded edges {'Clamped';'Simply Supported'}
    ##                         a            Unloaded edge length
    ##                         BC_Unloaded  Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
    ##                         t            Panel thickness
    ##                         behaviour    Material behaviour {'Elastic'; 'Elastic-Plastic'}
    ##                         E            Young's modulus
    ##                         nu           Elastic Poisson's ratio
    ##                         n            Ramberg-Osgood parameter
    ##                         iFy          Yield Stress Allowable
    ##                         nblc         Number of load cases
    ##                         sigma        Compressive stress
    ##                         tau          Shear stress
    ##                     Output
    ##                         sigmacr         Compressive stress allowable
    ##                         taucr           Shear stress allowable
    ##                         MS              Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmacr, taucr). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmacr is: float. Compressive stress allowable .
    ##  - taucr is: float. Shear stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingFlatLongitudinalShearCombined(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
        
                            MS Plate Buckling Flat Longitudinal Shear Combined
                            Computes margin of safety of a rectangular flat metallic panel in buckling under combined shear and longitudinal loads
        
                            Under longitudinal and shear loads, the interaction equation is:
                            MS=2/(RL + sqrt(RL ^ 2 + 4 * RS ^ 2)
        
                            This formula is derived from the interaction equation RL+R2S=1.0
                            RL + RS ^ 2 = 1.0
        
                            where:
                                * RL = sigma / sigmacr is the stress ratio due to longitudinal stress, with:
                                * sigma is the given longitudinal stress
                                * sigmacr is the compression stress allowable for buckling (sigmacr &lt; 0, as consequence RL &lt; 0 in tension)
                                * RS = tau / taucr is the stress ratio due to shear stress with
                                * tau is the given shear stress
                                * taucr is the shear stress allowable for buckling (taucr and tau always positive)
        
                                The panel edges are either clamped or simply supported.
        
                            Input
                                b            Loaded edge length
                                BC_Loaded    Support along loaded edges {'Clamped';'Simply Supported'}
                                a            Unloaded edge length
                                BC_Unloaded  Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
                                t            Panel thickness
                                behaviour    Material behaviour {'Elastic'; 'Elastic-Plastic'}
                                E            Young's modulus
                                nu           Elastic Poisson's ratio
                                n            Ramberg-Osgood parameter
                                iFy          Yield Stress Allowable
                                nblc         Number of load cases
                                sigma        Compressive stress
                                tau          Shear stress
                            Output
                                sigmacr         Compressive stress allowable
                                taucr           Shear stress allowable
                                MS              Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmacr, taucr). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmacr is: float. Compressive stress allowable .
         - taucr is: float. Shear stress allowable .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Flat Shear
    ##                     Computes margin of safety of a flat metallic rectangular panel under shear load
    ## 
    ##                     The formula is MS = tauAllowable / abs(tau) - 1
    ## 
    ##                     where:
    ##                     * 'tauAllowable' is the shear buckling stress allowable,
    ##                     * 'tau' is the compressive stress (MS is not calculated in case of tensile stress),
    ##                     * 'MS' is the margin of safety
    ## 
    ##                     Allowable = eta * PI^2*ks*E/(12*(1-nu^2)) * (t/b)^2
    ##                     where
    ##                     * 'ks' is the bending buckling stress coefficient
    ##                     * 'E' is the Young's modulus
    ##                     * 'nu' is the elastic Poisson's ratio
    ##                     * 't' is the panel thickness
    ##                     * 'a' is the panel's longer edge length
    ##                     * 'b' is panel's shorter edge length
    ##                     * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
    ##                     * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
    ##                     * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
    ## 
    ##                     TauAllowablePlastic/F0.7 = f(TauAllowableElastic/F0.7)
    ##                     MetallicPanelCompressivePlasticityCurveBC1, Warning: in fact graph is fig C5.13 but it is C5.7 graph divided by 2
    ## 
    ##                     Input
    ##                         b               First edge length
    ##                         a               Second edge length
    ##                         BC              Support along the edges {'Clamped';'Simply Supported'}
    ##                         t               Panel thickness
    ##                         behaviour       Material behaviour
    ##                         E               Young's modulus
    ##                         nu              Elastic Poisson's ratio
    ##                         n               Ramberg-Osgood parameter
    ##                         iFy             Yield Stress Allowable
    ##                         nblc            Number of load cases
    ##                         tau             Shear stress
    ##                     Output
    ##                         tauAllowable    Stress allowable
    ##                         MS              Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, tauAllowable). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - tauAllowable is: float. Stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingFlatShear(abbContext: AbbContext, b: float, a: float, bc: ABB.EdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, tau: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
        
                            MS Plate Buckling Flat Shear
                            Computes margin of safety of a flat metallic rectangular panel under shear load
        
                            The formula is MS = tauAllowable / abs(tau) - 1
        
                            where:
                            * 'tauAllowable' is the shear buckling stress allowable,
                            * 'tau' is the compressive stress (MS is not calculated in case of tensile stress),
                            * 'MS' is the margin of safety
        
                            Allowable = eta * PI^2*ks*E/(12*(1-nu^2)) * (t/b)^2
                            where
                            * 'ks' is the bending buckling stress coefficient
                            * 'E' is the Young's modulus
                            * 'nu' is the elastic Poisson's ratio
                            * 't' is the panel thickness
                            * 'a' is the panel's longer edge length
                            * 'b' is panel's shorter edge length
                            * 'eta' is the plasticity reduction factor: SigmaAllowablePlastic = eta*SigmaAllowableElastic
                            * eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                            * eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
        
                            TauAllowablePlastic/F0.7 = f(TauAllowableElastic/F0.7)
                            MetallicPanelCompressivePlasticityCurveBC1, Warning: in fact graph is fig C5.13 but it is C5.7 graph divided by 2
        
                            Input
                                b               First edge length
                                a               Second edge length
                                BC              Support along the edges {'Clamped';'Simply Supported'}
                                t               Panel thickness
                                behaviour       Material behaviour
                                E               Young's modulus
                                nu              Elastic Poisson's ratio
                                n               Ramberg-Osgood parameter
                                iFy             Yield Stress Allowable
                                nblc            Number of load cases
                                tau             Shear stress
                            Output
                                tauAllowable    Stress allowable
                                MS              Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, tauAllowable). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - tauAllowable is: float. Stress allowable .

        """
        pass
    
    ## 
    ##                     MS Plate Buckling Flat Shear Bending Combined
    ##                     Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and shear loads
    ## 
    ##                     Under longitudinal and shear loads, the interaction equation is:
    ##                     MS = 1 / sqrt(Rb ^ 2 + Rs ^ 2)
    ## 
    ##                     This formula is derived from the interaction equation
    ##                     Rb ^ 2 + Rs ^ 2 = 1.0
    ## 
    ##                     where:
    ##                         * Rb = sigmab / sigmabcr  is the stress ratio due to bendoing stress with
    ##                         * sigmab is the given compressive stress due to bending
    ##                         * sigmabcr is the bending stress allowable for buckling
    ##                         * Rs = tau / taucr is the stress ratio due to shear stress with
    ##                         * tau is the given shear stress
    ##                         * taucr is the shear stress allowable for buckling (taucr and tau always positive)
    ## 
    ##                     Input
    ##                         b            Loaded edge length
    ##                         BC_Loaded    Support along loaded edges {'Clamped';'Simply Supported'}
    ##                         a            Unloaded edge length
    ##                         BC_Unloaded  Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
    ##                         t            Panel thickness
    ##                         behaviour    Material behaviour {'Elastic'; 'Elastic-Plastic'}
    ##                         E            Young's modulus
    ##                         nu           Elastic Poisson's ratio
    ##                         n            Ramberg-Osgood parameter
    ##                         iFy          Yield Stress Allowable
    ##                         nblc         Number of load cases
    ##                         sigma1       Compressive stress, side 1
    ##                         sigma2       Compressive stress, side 2
    ##                         tau          Shear stress
    ##                     Output
    ##                         taucr        Shear stress allowable that takes into account compressive/tensile stress
    ##                         sigmabcr     Bending stress allowable
    ##                         MS           Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS, sigmabcr, taucr). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .
    ##  - sigmabcr is: List[float]. Bending stress allowable .
    ##  - taucr is: float. Shear stress allowable .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsPlateBucklingFlatShearBendingCombined(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma1: List[float], sigma2: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], List[float], float]:
        """
        
                            MS Plate Buckling Flat Shear Bending Combined
                            Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and shear loads
        
                            Under longitudinal and shear loads, the interaction equation is:
                            MS = 1 / sqrt(Rb ^ 2 + Rs ^ 2)
        
                            This formula is derived from the interaction equation
                            Rb ^ 2 + Rs ^ 2 = 1.0
        
                            where:
                                * Rb = sigmab / sigmabcr  is the stress ratio due to bendoing stress with
                                * sigmab is the given compressive stress due to bending
                                * sigmabcr is the bending stress allowable for buckling
                                * Rs = tau / taucr is the stress ratio due to shear stress with
                                * tau is the given shear stress
                                * taucr is the shear stress allowable for buckling (taucr and tau always positive)
        
                            Input
                                b            Loaded edge length
                                BC_Loaded    Support along loaded edges {'Clamped';'Simply Supported'}
                                a            Unloaded edge length
                                BC_Unloaded  Support along unloaded edges {'Clamped-Clamped';'Simply Supported-Clamped';'Simply Supported-Simply Supported';'Free-Clamped';'Free-Simply Supported'}
                                t            Panel thickness
                                behaviour    Material behaviour {'Elastic'; 'Elastic-Plastic'}
                                E            Young's modulus
                                nu           Elastic Poisson's ratio
                                n            Ramberg-Osgood parameter
                                iFy          Yield Stress Allowable
                                nblc         Number of load cases
                                sigma1       Compressive stress, side 1
                                sigma2       Compressive stress, side 2
                                tau          Shear stress
                            Output
                                taucr        Shear stress allowable that takes into account compressive/tensile stress
                                sigmabcr     Bending stress allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS, sigmabcr, taucr). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .
         - sigmabcr is: List[float]. Bending stress allowable .
         - taucr is: float. Shear stress allowable .

        """
        pass
    
    ## 
    ##                     MS Shear Tear Out
    ##                     Computes margin of shear tear out (due to bolt hole)
    ## 
    ##                     The formula is MS = PShearTearOutAllowable / P  - 1
    ##                     * 'PShearTearOutAllowable' is the shear tear out load allowable. PShearTearOutAllowable = tauAllowable * 2 * t * ( b - D / 2 )
    ##                         * 'tauAllowable' is the material shear stress allowable. For instance, it could be Fsu.
    ##                         * 'D' is the hole diameter
    ##                         * 't' is the thickness
    ##                         * 'b' is the distance from hole center to edge of the plate
    ##                     * 'P' is the axial load. P = FactorLoad * PExtracted
    ##                         * FactorLoad is the ratio of load between extracted load 'PExtracted' and 'P'
    ##                         * PExtracted is the extracted load.
    ## 
    ##                     Input
    ##                         nblc                Number of loadcases
    ##                         D                   Diameter
    ##                         b                   Edge distance
    ##                         t                   Thickness
    ##                         Fs                  Material shear stress allowable
    ##                         f                   Load factor
    ##                         P(nblc)             Axial load
    ##                     Output
    ##                         MS                  Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsShearTearOut(abbContext: AbbContext, D: float, b: float, t: float, iFs: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS Shear Tear Out
                            Computes margin of shear tear out (due to bolt hole)
        
                            The formula is MS = PShearTearOutAllowable / P  - 1
                            * 'PShearTearOutAllowable' is the shear tear out load allowable. PShearTearOutAllowable = tauAllowable * 2 * t * ( b - D / 2 )
                                * 'tauAllowable' is the material shear stress allowable. For instance, it could be Fsu.
                                * 'D' is the hole diameter
                                * 't' is the thickness
                                * 'b' is the distance from hole center to edge of the plate
                            * 'P' is the axial load. P = FactorLoad * PExtracted
                                * FactorLoad is the ratio of load between extracted load 'PExtracted' and 'P'
                                * PExtracted is the extracted load.
        
                            Input
                                nblc                Number of loadcases
                                D                   Diameter
                                b                   Edge distance
                                t                   Thickness
                                Fs                  Material shear stress allowable
                                f                   Load factor
                                P(nblc)             Axial load
                            Output
                                MS                  Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                     MS Tresca.
    ##                     Computes margin of safety based on Tresca yield criterion under plane stress condition
    ## 
    ##                     The yield criteria of isotropic materials limit the elastic domain during loading.
    ##                     According to the Tresca criterion, yield failure is expected when the greatest shear stress reaches the shear strength of the material.
    ##                     Thus, the maximum shear stress yield criterion can be specified as
    ##                     'max((|S1-S2|)/2 , (|S1-S3|)/2, (|S2-S3|)/2) &lt;= (STresca)/2'
    ##                     where
    ##                     * 'S1', 'S2' and 'S3' are the principal stresses.
    ##                     * 'STresca' is the Tresca equivalent stress allowable  
    ## 
    ##                     A margin of safety can be derived from this formulation:
    ##                     'MS = (STresca) / (max(|S1-S2| , |S1-S3|, |S2-S3|)) - 1'
    ##                     that must be greater than 0.
    ## 
    ##                     In a plane stress configuration, principal stresses are computed as
    ##                     'S1 = (FX + FY)/2 + sqrt(((FX-FY)/2)^2 + FXY^2)'
    ##                     'S2 = (FX + FY)/2 - sqrt(((FX-FY)/2)^2 + FXY^2)'
    ##                     where
    ##                     * 'FX' the normal stress in the X direction
    ##                     * 'FY' the normal stress in the Y direction
    ##                     * 'FXY' the shearing stress
    ## 
    ##                     Input
    ##                         iSTresca Tresca equivalent stress allowable 
    ##                         nblc     Number of load cases
    ##                         Fx       Normal stress in the X direction
    ##                         iFy      Normal stress in the Y direction
    ##                         Fxy      Shear stress
    ##                     Output
    ##                         MS       Margin of safety
    ##                     Return
    ##                         Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of safety .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsTrescaPlaneStress(abbContext: AbbContext, iSTresca: float, iFx: List[float], iFy: List[float], iFxy: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                            MS Tresca.
                            Computes margin of safety based on Tresca yield criterion under plane stress condition
        
                            The yield criteria of isotropic materials limit the elastic domain during loading.
                            According to the Tresca criterion, yield failure is expected when the greatest shear stress reaches the shear strength of the material.
                            Thus, the maximum shear stress yield criterion can be specified as
                            'max((|S1-S2|)/2 , (|S1-S3|)/2, (|S2-S3|)/2) &lt;= (STresca)/2'
                            where
                            * 'S1', 'S2' and 'S3' are the principal stresses.
                            * 'STresca' is the Tresca equivalent stress allowable  
        
                            A margin of safety can be derived from this formulation:
                            'MS = (STresca) / (max(|S1-S2| , |S1-S3|, |S2-S3|)) - 1'
                            that must be greater than 0.
        
                            In a plane stress configuration, principal stresses are computed as
                            'S1 = (FX + FY)/2 + sqrt(((FX-FY)/2)^2 + FXY^2)'
                            'S2 = (FX + FY)/2 - sqrt(((FX-FY)/2)^2 + FXY^2)'
                            where
                            * 'FX' the normal stress in the X direction
                            * 'FY' the normal stress in the Y direction
                            * 'FXY' the shearing stress
        
                            Input
                                iSTresca Tresca equivalent stress allowable 
                                nblc     Number of load cases
                                Fx       Normal stress in the X direction
                                iFy      Normal stress in the Y direction
                                Fxy      Shear stress
                            Output
                                MS       Margin of safety
                            Return
                                Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of safety .

        """
        pass
    
    ## 
    ##                 MS Tsai-Hill
    ## 
    ##                 Computes margin of safety on the basis of Tsai-Hill failure theory (plane stress 
    ##                 hypothesis)
    ## 
    ##                 For plane stress, this criterion can be written as:
    ##                     sigma1^2/X^2 - (sigma1 * sigma2)/X^2 + sigma2^2/Y^2 + tau^2/S^2 > 1
    ## 
    ##                 where:
    ## 
    ##                     * sigma1, sigma2 and tau are the components of the symmetric plane stress tensor 
    ##                       in the material direction,
    ##                     * X is the longitudinal tensile (Xt; if sigma1 is in tension, e.g., sigma1 
    ##                       greater than 0) or compressive (Xc; if sigma1 is in compression, e.g., sigma1 
    ##                       less than 0) stress,
    ##                     * Y is the transverse tensile (Yt; if sigma2 is in tension, e.g., sigma2 greater
    ##                       than 0) or compressive (Yc; if sigma2 is in compression, e.g., sigma2 less
    ##                       than 0) stress, and
    ##                     * S is the in-plane shear stress.
    ## 
    ##                 Note: This equation is specialized for plane stress with the longitudinal strength X 
    ##                 in the 1-direction.
    ##                  
    ##                 The Margin of Safety, MS, is deduced from the criterion:
    ##                     MS = 1 / sqrt(sigma1^2/X^2 - (sigma1 * sigma2)/X^2 + sigma2^2/Y^2 + tau^2/S^2) - 1
    ## 
    ##                  Input
    ##                     Xt          Longitudinal Tensile Strength
    ##                     Xc          Longitudinal Compressive Strength
    ##                     Yt          Transverse Tensile Strength
    ##                     Yc          Transverse Compressive Strength 
    ##                     S           In-plane Shear Strength
    ##                     sigma1      Longitudinal Stresses
    ##                     sigma2      Transverse Stresses
    ##                     tau         Shear Stresses
    ##                 Output
    ##                     MS          Margin of safety
    ##                 Return
    ##                     Status of the calculation
    ##                 
    ##  @return A tuple consisting of (status, MS). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - MS is: List[float]. Margin of Safety .

    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def MsTsaiHillPlaneStress(abbContext: AbbContext, iXt: float, iXc: float, iYt: float, iYc: float, S: float, sigma1: List[float], sigma2: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
        
                        MS Tsai-Hill
        
                        Computes margin of safety on the basis of Tsai-Hill failure theory (plane stress 
                        hypothesis)
        
                        For plane stress, this criterion can be written as:
                            sigma1^2/X^2 - (sigma1 * sigma2)/X^2 + sigma2^2/Y^2 + tau^2/S^2 > 1
        
                        where:
        
                            * sigma1, sigma2 and tau are the components of the symmetric plane stress tensor 
                              in the material direction,
                            * X is the longitudinal tensile (Xt; if sigma1 is in tension, e.g., sigma1 
                              greater than 0) or compressive (Xc; if sigma1 is in compression, e.g., sigma1 
                              less than 0) stress,
                            * Y is the transverse tensile (Yt; if sigma2 is in tension, e.g., sigma2 greater
                              than 0) or compressive (Yc; if sigma2 is in compression, e.g., sigma2 less
                              than 0) stress, and
                            * S is the in-plane shear stress.
        
                        Note: This equation is specialized for plane stress with the longitudinal strength X 
                        in the 1-direction.
                         
                        The Margin of Safety, MS, is deduced from the criterion:
                            MS = 1 / sqrt(sigma1^2/X^2 - (sigma1 * sigma2)/X^2 + sigma2^2/Y^2 + tau^2/S^2) - 1
        
                         Input
                            Xt          Longitudinal Tensile Strength
                            Xc          Longitudinal Compressive Strength
                            Yt          Transverse Tensile Strength
                            Yc          Transverse Compressive Strength 
                            S           In-plane Shear Strength
                            sigma1      Longitudinal Stresses
                            sigma2      Transverse Stresses
                            tau         Shear Stresses
                        Output
                            MS          Margin of safety
                        Return
                            Status of the calculation
                        
         @return A tuple consisting of (status, MS). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - MS is: List[float]. Margin of Safety .

        """
        pass
    
    ## 
    ##                     Secant modulus
    ##                     Computes the secant modulus from material properties and stress.
    ## 
    ##                     The secant modulus ('Es') is defined as the stress('f') to strain ('epsilon') ratio at each value of stress.
    ## 
    ##                     The formula is 'Es = f / ( f / E + 0.002 * ( f / fy ) ^ n )'
    ##                     where:
    ##                         * 'f' is the stress
    ##                         * 'fy' is the yield stress
    ##                         * 'E' is the Young's modulus
    ##                         * 'n' is the Ramberg-Osgood parameter
    ## 
    ##                     The formula can be applied in compression and is 'Es = f / ( f / Ec + 0.002 * ( f / Fcy ) ^ nc)'
    ##                     where:
    ##                         * 'Fcy' is the compressive yield stress
    ##                         * 'Ec' is the compressive Young's modulus
    ##                         * 'nc' is the compressive Ramberg-Osgood parameter
    ## 
    ##                     Input
    ##                         E       Young's modulus
    ##                         n       Ramberg-Osgood parameter
    ##                         fy      Yield stress
    ##                         sigma   Stress
    ##                     Output
    ##                         Es      Secant modulus
    ##                     Return
    ##                         Status of the computation
    ##                 
    ##  @return A tuple consisting of (status, iEs). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - iEs is: float. Secant modulus .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def SecantModulus(abbContext: AbbContext, E: float, n: float, fy: float, sigma: float) -> Tuple[ABB.Status, float]:
        """
        
                            Secant modulus
                            Computes the secant modulus from material properties and stress.
        
                            The secant modulus ('Es') is defined as the stress('f') to strain ('epsilon') ratio at each value of stress.
        
                            The formula is 'Es = f / ( f / E + 0.002 * ( f / fy ) ^ n )'
                            where:
                                * 'f' is the stress
                                * 'fy' is the yield stress
                                * 'E' is the Young's modulus
                                * 'n' is the Ramberg-Osgood parameter
        
                            The formula can be applied in compression and is 'Es = f / ( f / Ec + 0.002 * ( f / Fcy ) ^ nc)'
                            where:
                                * 'Fcy' is the compressive yield stress
                                * 'Ec' is the compressive Young's modulus
                                * 'nc' is the compressive Ramberg-Osgood parameter
        
                            Input
                                E       Young's modulus
                                n       Ramberg-Osgood parameter
                                fy      Yield stress
                                sigma   Stress
                            Output
                                Es      Secant modulus
                            Return
                                Status of the computation
                        
         @return A tuple consisting of (status, iEs). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - iEs is: float. Secant modulus .

        """
        pass
    
    ## 
    ##                     Stress F0.7
    ##                     Computes the stress for secant modulus equal to 70% of Young's modulus.
    ## 
    ##                     The calculation is based upon the material properties. 'F0.7' is defined by:
    ##                     'F0.7/epsilon=0.7E', where 'epsilon' is the strain, and 'E' is the Young's modulus.
    ##                     The formula can be applied for tensile and compressive stress, hence:
    ##                     'F0.7 = ( (1/0.7 - 1) / 0.002 * Fty ^ n / E ) ^ ( 1 / ( n - 1 ) )' for tension,
    ##                     and 'F0.7c = ( ( 1 / 0.7 - 1 ) / 0.002 * Fcy ^ nc / Ec ) ^ ( 1 / ( nc - 1 ) )' for compression.
    ## 
    ##                     where:
    ##                     * 'Fcy' is the compressive yield stress allowable
    ##                     * 'Fty' the tensile yield stress allowable
    ##                     * 'n' the Ramberg-Osgood parameter
    ##                     * 'Ec' the compressive Young's modulus
    ##                     * 'nc' the compressive Ramberg-Osgood parameter
    ## 
    ##                     Input
    ##                         iFy Yield stress allowable
    ##                         E Young's modulus
    ##                         n Ramberg-Osgood parameter
    ##                     Output
    ##                         F07 Secant yield stress F0.7
    ##                 
    ##  @return A tuple consisting of (status, F07). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - F07 is: float. Secant yield stress F0.7 .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def StressF07(abbContext: AbbContext, iFy: float, E: float, n: float) -> Tuple[ABB.Status, float]:
        """
        
                            Stress F0.7
                            Computes the stress for secant modulus equal to 70% of Young's modulus.
        
                            The calculation is based upon the material properties. 'F0.7' is defined by:
                            'F0.7/epsilon=0.7E', where 'epsilon' is the strain, and 'E' is the Young's modulus.
                            The formula can be applied for tensile and compressive stress, hence:
                            'F0.7 = ( (1/0.7 - 1) / 0.002 * Fty ^ n / E ) ^ ( 1 / ( n - 1 ) )' for tension,
                            and 'F0.7c = ( ( 1 / 0.7 - 1 ) / 0.002 * Fcy ^ nc / Ec ) ^ ( 1 / ( nc - 1 ) )' for compression.
        
                            where:
                            * 'Fcy' is the compressive yield stress allowable
                            * 'Fty' the tensile yield stress allowable
                            * 'n' the Ramberg-Osgood parameter
                            * 'Ec' the compressive Young's modulus
                            * 'nc' the compressive Ramberg-Osgood parameter
        
                            Input
                                iFy Yield stress allowable
                                E Young's modulus
                                n Ramberg-Osgood parameter
                            Output
                                F07 Secant yield stress F0.7
                        
         @return A tuple consisting of (status, F07). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - F07 is: float. Secant yield stress F0.7 .

        """
        pass
    
    ## 
    ##                     Compute stress from strain with the help of Ramberg-Osgood relationship
    ## 
    ##                     The Ramberg-Osgood relationship allows to describe stress-strain curve with the help of a dedicated material parameter ('n').
    ##                     'e = f / E + 0.002 * ( f / f0.2ys ) ^ n'
    ##                     where:
    ##                     * 'e' is the total strain that takes into account elastic and plastic strains.
    ##                     * 'f' is the stress
    ##                     * 'E' is the material Young's modulus
    ##                     * 'f0.2ys' is the material yield allowable (Fcy or Fty depending load type).
    ##                     * 'n' is the Ramberg-Osgood parameter (in case of compressive load, it is common to call it 'nc').
    ## 
    ##                     The Ramberg-Osgood equation can not be inverted. As a consequence, stress is determined by numerical iterative calculation.
    ## 
    ##                     Input
    ##                         strain  Total strain
    ##                         E       Young's modulus
    ##                         F02ys   Yield allowable (typically Fcy)
    ##                         n       Ramberg-Osgood's parameter
    ##                     Output
    ##                         sigma Stress
    ##                 
    ##  @return A tuple consisting of (status, sigma). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - sigma is: float. Stress .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def StressFromStrainInPlasticDomain(abbContext: AbbContext, strain: float, E: float, iF02ys: float, n: float) -> Tuple[ABB.Status, float]:
        """
        
                            Compute stress from strain with the help of Ramberg-Osgood relationship
        
                            The Ramberg-Osgood relationship allows to describe stress-strain curve with the help of a dedicated material parameter ('n').
                            'e = f / E + 0.002 * ( f / f0.2ys ) ^ n'
                            where:
                            * 'e' is the total strain that takes into account elastic and plastic strains.
                            * 'f' is the stress
                            * 'E' is the material Young's modulus
                            * 'f0.2ys' is the material yield allowable (Fcy or Fty depending load type).
                            * 'n' is the Ramberg-Osgood parameter (in case of compressive load, it is common to call it 'nc').
        
                            The Ramberg-Osgood equation can not be inverted. As a consequence, stress is determined by numerical iterative calculation.
        
                            Input
                                strain  Total strain
                                E       Young's modulus
                                F02ys   Yield allowable (typically Fcy)
                                n       Ramberg-Osgood's parameter
                            Output
                                sigma Stress
                        
         @return A tuple consisting of (status, sigma). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - sigma is: float. Stress .

        """
        pass
    
    ## 
    ##                     Computes the tangent modulus from material properties and stress.
    ## 
    ##                     The tangent modulus ('Et') is defined as the slope of the stress('f')-strain('epsilon') curve at each value of stress.
    ## 
    ##                     The formula is 'Et = f / ( f / E + 0.002 * n * ( f / FY ) ^ n )'
    ##                     where:
    ##                     * 'f' is the stress
    ##                     * 'FY' is the yield stress
    ##                     * 'E' is the Young's modulus
    ##                     * 'n' is the Ramberg-Osgood parameter
    ## 
    ##                     The formula can be applied in compression and is 'Et=f/(f/Ec+0.002nc(f/(Fcy))^(nc))'
    ##                     where:
    ##                     * 'Fcy' is the compressive yield stress
    ##                     * 'Ec' is the compressive Young's modulus
    ##                     * 'nc' is the compressive Ramberg-Osgood parameter
    ## 
    ##                     Input
    ##                         E Young's modulus
    ##                         n Ramberg-Osgood parameter
    ##                         iFy Yield stress Allowable
    ##                         sigma Stress
    ##                     Output
    ##                         Et Tangent modulus
    ##                 
    ##  @return A tuple consisting of (status, oEt). 
    ##  - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
    ##  - oEt is: float. Tangent modulus .

    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: sc_margin_safety ("Simcenter Margin Of Safety")
    ##  The ABB context 
    @staticmethod
    def TangentModulus(abbContext: AbbContext, E: float, n: float, iFy: float, sigma: float) -> Tuple[ABB.Status, float]:
        """
        
                            Computes the tangent modulus from material properties and stress.
        
                            The tangent modulus ('Et') is defined as the slope of the stress('f')-strain('epsilon') curve at each value of stress.
        
                            The formula is 'Et = f / ( f / E + 0.002 * n * ( f / FY ) ^ n )'
                            where:
                            * 'f' is the stress
                            * 'FY' is the yield stress
                            * 'E' is the Young's modulus
                            * 'n' is the Ramberg-Osgood parameter
        
                            The formula can be applied in compression and is 'Et=f/(f/Ec+0.002nc(f/(Fcy))^(nc))'
                            where:
                            * 'Fcy' is the compressive yield stress
                            * 'Ec' is the compressive Young's modulus
                            * 'nc' is the compressive Ramberg-Osgood parameter
        
                            Input
                                E Young's modulus
                                n Ramberg-Osgood parameter
                                iFy Yield stress Allowable
                                sigma Stress
                            Output
                                Et Tangent modulus
                        
         @return A tuple consisting of (status, oEt). 
         - status is: @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink.
         - oEt is: float. Tangent modulus .

        """
        pass
    
import NXOpen
import NXOpen.CAE.AeroStructures
##   @brief  Calculation context is passed to the method implementation. 
##                   It contains methods to retrieve the load case set and input parameter values,
##                   method to set the output values and log messages   
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CalculationContext(NXOpen.NXObject): 
    """ <summary> Calculation context is passed to the method implementation. 
                  It contains methods to retrieve the load case set and input parameter values,
                  method to set the output values and log messages  </summary> """


    ## 
    ##             Unit systems that can be used by a calculation method.
    ##         
    ##  Metric Unit System 
    class UnitSystem(Enum):
        """
        Members Include: <Metric> <English> <Si> <Unknown>
        """
        Metric: int
        English: int
        Si: int
        Unknown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CalculationContext.UnitSystem:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Name
    ##   the name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ##  Add a general scalar table to the context: 
    ##          - The unit system of the calculation context is used for the values 
    ##          - The table will exist for the duration of the context
    ##         
    ##  @return scalarTable (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nRows"> (int) </param>
    ## <param name="nCols"> (int) </param>
    ## <param name="measure_name"> (str) </param>
    def AddGeneralScalarTable(context: CalculationContext, nRows: int, nCols: int, measure_name: str) -> NXOpen.GeneralScalarTable:
        """
         Add a general scalar table to the context: 
                 - The unit system of the calculation context is used for the values 
                 - The table will exist for the duration of the context
                
         @return scalarTable (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink): .
        """
        pass
    
    ##  Log an error message
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  an error message 
    @overload
    def Error(self, context: CalculationContext, message: str) -> None:
        """
         Log an error message
        """
        pass
    
    ##  Log an error message indexed by possibly empty failure mode and load case
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  a failure mode name (an empty string indicates that the message is not failure mode specific)
    @overload
    def Error(self, context: CalculationContext, failureMode: str, lcIndex: int, message: str) -> None:
        """
         Log an error message indexed by possibly empty failure mode and load case
        """
        pass
    
    ##  Log an error message indexed by possibly empty failure mode and load case
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  a failure mode name (an empty string indicates that the message is not failure mode specific)
    @overload
    def Error(self, context: CalculationContext, failureMode: str, loadCase: str, message: str) -> None:
        """
         Log an error message indexed by possibly empty failure mode and load case
        """
        pass
    
    ##  Returns the ABB context object
    ##  @return abbContext (@link AbbContext NXOpen.CAE.AeroStructures.Author.AbbContext@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetAbbContext(context: CalculationContext) -> AbbContext:
        """
         Returns the ABB context object
         @return abbContext (@link AbbContext NXOpen.CAE.AeroStructures.Author.AbbContext@endlink): .
        """
        pass
    
    ##  Get an input parameter 
    ##  @return param (@link InputParameter NXOpen.CAE.AeroStructures.Author.InputParameter@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="inputName"> (str) </param>
    def GetInput(context: CalculationContext, inputName: str) -> InputParameter:
        """
         Get an input parameter 
         @return param (@link InputParameter NXOpen.CAE.AeroStructures.Author.InputParameter@endlink):  .
        """
        pass
    
    ##  Get the load case array used by the calculation
    ##  @return lcarray (@link NXOpen.CAE.AeroStructures.LoadCase List[NXOpen.CAE.AeroStructures.LoadCase]@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetLoadCaseArray(context: CalculationContext) -> List[NXOpen.CAE.AeroStructures.LoadCase]:
        """
         Get the load case array used by the calculation
         @return lcarray (@link NXOpen.CAE.AeroStructures.LoadCase List[NXOpen.CAE.AeroStructures.LoadCase]@endlink):  .
        """
        pass
    
    ##  Get an output parameter 
    ##  @return param (@link OutputParameter NXOpen.CAE.AeroStructures.Author.OutputParameter@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="outputName"> (str) </param>
    def GetOutput(context: CalculationContext, outputName: str) -> OutputParameter:
        """
         Get an output parameter 
         @return param (@link OutputParameter NXOpen.CAE.AeroStructures.Author.OutputParameter@endlink):  .
        """
        pass
    
    ##  Get MS output parameter 
    ##  @return param (@link OutputScalar NXOpen.CAE.AeroStructures.Author.OutputScalar@endlink):  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetOutputMs(context: CalculationContext) -> OutputScalar:
        """
         Get MS output parameter 
         @return param (@link OutputScalar NXOpen.CAE.AeroStructures.Author.OutputScalar@endlink):  .
        """
        pass
    
    ##  Creates and return a path to an empty temporary directory 
    ##  @return path (str):  .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetTempPath(context: CalculationContext) -> str:
        """
         Creates and return a path to an empty temporary directory 
         @return path (str):  .
        """
        pass
    
    ##  Get unit from its name 
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="unitName"> (str) </param>
    def GetUnit(context: CalculationContext, unitName: str) -> NXOpen.Unit:
        """
         Get unit from its name 
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink): .
        """
        pass
    
    ##  Returns the unit type object for a given measure in the method unit system. The unit system
    ##             can be defined by an author in the definition of the method or by the user in the margin solution 
    ##             editor. If there is no method or solution unit system the method uses the current base unit system.
    ##         
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  unit type of the measure .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  the input measure name 
    def GetUnitForMeasure(context: CalculationContext, measure_name: str) -> NXOpen.Unit:
        """
         Returns the unit type object for a given measure in the method unit system. The unit system
                    can be defined by an author in the definition of the method or by the user in the margin solution 
                    editor. If there is no method or solution unit system the method uses the current base unit system.
                
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  unit type of the measure .
        """
        pass
    
    ##  Returns the unit type object for a given measure and unit name  
    ##  @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  unit type of the measure .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  the input measure name 
    def GetUnitType(context: CalculationContext, measure_name: str, unit_symbol: str) -> NXOpen.Unit:
        """
         Returns the unit type object for a given measure and unit name  
         @return unit_type (@link NXOpen.Unit NXOpen.Unit@endlink):  unit type of the measure .
        """
        pass
    
    ##  Log an info message
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  an info message 
    @overload
    def Log(self, context: CalculationContext, message: str) -> None:
        """
         Log an info message
        """
        pass
    
    ##  Log an info message indexed by possibly empty failure mode and load case
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  a failure mode name (an empty string indicates that the message is not failure mode specific)
    @overload
    def Log(self, context: CalculationContext, failureMode: str, lcIndex: int, message: str) -> None:
        """
         Log an info message indexed by possibly empty failure mode and load case
        """
        pass
    
    ##  Log an info message indexed by possibly empty failure mode and load case
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  a failure mode name (an empty string indicates that the message is not failure mode specific)
    @overload
    def Log(self, context: CalculationContext, failureMode: str, loadCase: str, message: str) -> None:
        """
         Log an info message indexed by possibly empty failure mode and load case
        """
        pass
    
    ##  Set Envelope Results 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="xValues"> (List[float]) </param>
    ## <param name="yValues"> (List[float]) </param>
    def SetEnvelopeResults(context: CalculationContext, xValues: List[float], yValues: List[float]) -> None:
        """
         Set Envelope Results 
        """
        pass
    
    ##  Set Load Results 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="lcIndex"> (int) </param>
    ## <param name="xValues"> (List[float]) </param>
    ## <param name="yValues"> (List[float]) </param>
    ## <param name="centralities"> (List[float]) </param>
    ## <param name="selected"> (List[bool]) </param>
    def SetLoadResults(context: CalculationContext, lcIndex: int, xValues: List[float], yValues: List[float], centralities: List[float], selected: List[bool]) -> None:
        """
         Set Load Results 
        """
        pass
    
    ##  Set Result Units  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="x_unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    ## <param name="y_unit_type"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    def SetResultUnits(context: CalculationContext, x_unit_type: NXOpen.Unit, y_unit_type: NXOpen.Unit) -> None:
        """
         Set Result Units  
        """
        pass
    
    ##  Set Selected LC 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  load case index corresponding to the load case position in the load case array of the calculation context starting from 0 (-1 means that the message is not load case specific) 
    def SetSelectedLoadCase(context: CalculationContext, lcIndex: int, selected: bool) -> None:
        """
         Set Selected LC 
        """
        pass
    
    ##  Set Selected LCs by array 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  list of indexes for selected load cases 
    def SetSelectedLoadCases(context: CalculationContext, lcIndexes: List[int]) -> None:
        """
         Set Selected LCs by array 
        """
        pass
    
    ##  Set Tolerance Results 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="xValues"> (List[float]) </param>
    ## <param name="yValues"> (List[float]) </param>
    def SetToleranceResults(context: CalculationContext, xValues: List[float], yValues: List[float]) -> None:
        """
         Set Tolerance Results 
        """
        pass
    
    ##  Set Tolerance Value 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tolerance"> (float) </param>
    def SetToleranceValue(context: CalculationContext, tolerance: float) -> None:
        """
         Set Tolerance Value 
        """
        pass
    
    ##  Log a warning message
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  a warning message 
    @overload
    def Warn(self, context: CalculationContext, message: str) -> None:
        """
         Log a warning message
        """
        pass
    
    ##  Log a warning message indexed by possibly empty failure mode and load case
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  a failure mode name (an empty string indicates that the message is not failure mode specific)
    @overload
    def Warn(self, context: CalculationContext, failureMode: str, lcIndex: int, message: str) -> None:
        """
         Log a warning message indexed by possibly empty failure mode and load case
        """
        pass
    
    ##  Log a warning message indexed by possibly empty failure mode and load case
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  a failure mode name (an empty string indicates that the message is not failure mode specific)
    @overload
    def Warn(self, context: CalculationContext, failureMode: str, loadCase: str, message: str) -> None:
        """
         Log a warning message indexed by possibly empty failure mode and load case
        """
        pass
    
##   @brief  Represents a boolean input parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class InputBoolean(InputParameter): 
    """ <summary> Represents a boolean input parameter </summary> """


    ## Getter for property: (bool) Value
    ##   the value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Value(self) -> bool:
        """
        Getter for property: (bool) Value
          the value.  
             
         
        """
        pass
    
##   @brief  Represents a File input parameter  
## 
##    <br> No support for KF  <br> 
class InputFile(InputParameter): 
    """ <summary> Represents a File input parameter </summary> """


    ##  Retrieve the absolutr path of the file 
    ##  @return pathVal (str):  the directory used.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPath(param: InputFile) -> str:
        """
         Retrieve the absolutr path of the file 
         @return pathVal (str):  the directory used.
        """
        pass
    
##   @brief  Represents an integer input parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class InputInteger(InputParameter): 
    """ <summary> Represents an integer input parameter </summary> """


    ## Getter for property: (int) Value
    ##   the value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def Value(self) -> int:
        """
        Getter for property: (int) Value
          the value.  
             
         
        """
        pass
    
import NXOpen.CAE.AeroStructures
##   @brief  represent a laminate input parameter  
## 
##   
## 
##   <br>  Created in NX1847.0.0  <br> 

class InputLaminate(InputParameter): 
    """ <summary> represent a laminate input parameter </summary> """


    ## Getter for property: (@link NXOpen.CAE.AeroStructures.Laminate NXOpen.CAE.AeroStructures.Laminate@endlink) RawValue
    ##   the laminate without considering extraction transformations   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.AeroStructures.Laminate
    @property
    def RawValue(self) -> NXOpen.CAE.AeroStructures.Laminate:
        """
        Getter for property: (@link NXOpen.CAE.AeroStructures.Laminate NXOpen.CAE.AeroStructures.Laminate@endlink) RawValue
          the laminate without considering extraction transformations   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.AeroStructures.Laminate NXOpen.CAE.AeroStructures.Laminate@endlink) Value
    ##   the laminate taking into account extraction transformations   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.AeroStructures.Laminate
    @property
    def Value(self) -> NXOpen.CAE.AeroStructures.Laminate:
        """
        Getter for property: (@link NXOpen.CAE.AeroStructures.Laminate NXOpen.CAE.AeroStructures.Laminate@endlink) Value
          the laminate taking into account extraction transformations   
            
         
        """
        pass
    
    ##  The laminate is well set up.
    ##  @return hasValue (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def HasValue(param: InputLaminate) -> bool:
        """
         The laminate is well set up.
         @return hasValue (bool): .
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  represent a load input parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class InputLoad(InputParameter): 
    """ <summary> represent a load input parameter </summary> """


    ##  the support type 
    ##  Not available (the aggregation has been done at the calculation level, Values/GetValues() will return a vector of aggregated values) 
    class LoadSupportType(Enum):
        """
        Members Include: <NotSet> <Node> <Element>
        """
        NotSet: int
        Node: int
        Element: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InputLoad.LoadSupportType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link InputLoad.LoadSupportType NXOpen.CAE.AeroStructures.Author.InputLoad.LoadSupportType@endlink) SupportType
    ##   the support type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return InputLoad.LoadSupportType
    @property
    def SupportType(self) -> InputLoad.LoadSupportType:
        """
        Getter for property: (@link InputLoad.LoadSupportType NXOpen.CAE.AeroStructures.Author.InputLoad.LoadSupportType@endlink) SupportType
          the support type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Unit
    ##   the unit type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def Unit(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Unit
          the unit type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink) Values
    ##   the values   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.GeneralScalarTable
    @property
    def Values(self) -> NXOpen.GeneralScalarTable:
        """
        Getter for property: (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink) Values
          the values   
            
         
        """
        pass
    
    ##  Get support elements 
    ##  @return elementArray (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  the list of support elements, if available .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetElements(param: InputLoad) -> List[NXOpen.CAE.FEElement]:
        """
         Get support elements 
         @return elementArray (@link NXOpen.CAE.FEElement List[NXOpen.CAE.FEElement]@endlink):  the list of support elements, if available .
        """
        pass
    
    ##  Get support nodes 
    ##  @return nodeArray (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  the list of support nodes, if available .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetNodes(param: InputLoad) -> List[NXOpen.CAE.FENode]:
        """
         Get support nodes 
         @return nodeArray (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink):  the list of support nodes, if available .
        """
        pass
    
    ##  Get value using a specific unit type. 
    ##  @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink):  either a one- or two-dimensional array of doubles .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the unit in which the value must be converted if necessary
    @overload
    def GetValues(self, param: InputLoad, unit_type: NXOpen.Unit) -> NXOpen.GeneralScalarTable:
        """
         Get value using a specific unit type. 
         @return matrix (@link NXOpen.GeneralScalarTable NXOpen.GeneralScalarTable@endlink):  either a one- or two-dimensional array of doubles .
        """
        pass
    
import NXOpen
import NXOpen.CAE.AeroStructures
##   @brief  parent class of all typed input parameter classes  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class InputParameter(NXOpen.NXObject): 
    """ <summary> parent class of all typed input parameter classes </summary> """


    ## Getter for property: (str) Name
    ##   the name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink) Type
    ##   the parameter type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType
    @property
    def Type(self) -> NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType:
        """
        Getter for property: (@link NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink) Type
          the parameter type.  
             
         
        """
        pass
    
import NXOpen
##   @brief  Represents a scalar input parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class InputScalar(InputParameter): 
    """ <summary> Represents a scalar input parameter </summary> """


    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Unit
    ##   the unit type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def Unit(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Unit
          the unit type.  
             
         
        """
        pass
    
    ## Getter for property: (float) Value
    ##   the value in default unit.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return float
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
          the value in default unit.  
            
         
        """
        pass
    
    ##  Get the value in a specific unit. 
    ##  @return doubleVal (float):  the double value of the parameter expressed in the specified unit.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the unit in which the value must be converted if necessary
    def GetValueIn(param: InputScalar, unit_type: NXOpen.Unit) -> float:
        """
         Get the value in a specific unit. 
         @return doubleVal (float):  the double value of the parameter expressed in the specified unit.
        """
        pass
    
import NXOpen.CAE.AeroStructures
##   @brief  Represents an Table input parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class InputTable(InputParameter): 
    """ <summary> Represents an Table input parameter </summary> """


    ## Getter for property: (@link NXOpen.CAE.AeroStructures.TableParameter NXOpen.CAE.AeroStructures.TableParameter@endlink) Value
    ##   the value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.CAE.AeroStructures.TableParameter
    @property
    def Value(self) -> NXOpen.CAE.AeroStructures.TableParameter:
        """
        Getter for property: (@link NXOpen.CAE.AeroStructures.TableParameter NXOpen.CAE.AeroStructures.TableParameter@endlink) Value
          the value.  
             
         
        """
        pass
    
##   @brief  Represents a text input parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class InputText(InputParameter): 
    """ <summary> Represents a text input parameter </summary> """


    ## Getter for property: (str) Value
    ##   the value.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
          the value.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::CAE::AeroStructures::Author::MethodLibrary NXOpen::CAE::AeroStructures::Author::MethodLibrary@endlink  object.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MethodLibrary(NXOpen.Object): 
    """ Represents a <ja_class>NXOpen.CAE.AeroStructures.Author.MethodLibrary</ja_class> object. """


    ##  Callback type 
    ## A callback definition with the following input arguments: 
    ##  - @link CalculationContext NXOpen.CAE.AeroStructures.Author.CalculationContext@endlink
    ##  and no return type
    Callback = Callable[[CalculationContext], None]
    
    
    ##  CallbackMulti type 
    ## A callback definition with the following input arguments: 
    ##  - @link MultiCalculationContext NXOpen.CAE.AeroStructures.Author.MultiCalculationContext@endlink
    ##  and no return type
    CallbackMulti = Callable[[MultiCalculationContext], None]
    
    
    ##  CallbackPost type 
    ## A callback definition with the following input arguments: 
    ##  - @link NXOpen.CAE.AeroStructures.MarginCalculation NXOpen.CAE.AeroStructures.MarginCalculation@endlink
    ##  and no return type
    CallbackPost = Callable[[NXOpen.CAE.AeroStructures.MarginCalculation], None]
    
    
    ##  Routine to register an evaluate callback 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterEvaluate(methodID: str, version: int, cb: MethodLibrary.Callback) -> None:
        """
         Routine to register an evaluate callback 
        """
        pass
    
    ##  Routine to register an evaluate script (internal use only)
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterEvaluateScript(methodID: str, version: int) -> None:
        """
         Routine to register an evaluate script (internal use only)
        """
        pass
    
    ##  Routine to register a multi evaluate callback 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterMultiEvaluate(methodID: str, version: int, cb: MethodLibrary.CallbackMulti) -> None:
        """
         Routine to register a multi evaluate callback 
        """
        pass
    
    ##  Routine to register a multi evaluate script (internal use only)
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterMultiEvaluateScript(methodID: str, version: int) -> None:
        """
         Routine to register a multi evaluate script (internal use only)
        """
        pass
    
    ##  Routine to register a Post Processing callback 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterPostProcessing(methodID: str, version: int, cb: MethodLibrary.CallbackPost) -> None:
        """
         Routine to register a Post Processing callback 
        """
        pass
    
    ##  Routine to register a post processing script (internal use only) 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterPostProcessingScript(methodID: str, version: int) -> None:
        """
         Routine to register a post processing script (internal use only) 
        """
        pass
    
    ##  Routine to register a validate callback 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterValidate(methodID: str, version: int, cb: MethodLibrary.Callback) -> None:
        """
         Routine to register a validate callback 
        """
        pass
    
    ##  Routine to register a validate script (internal use only) 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  must match 'id' field in method descriptor 
    def RegisterValidateScript(methodID: str, version: int) -> None:
        """
         Routine to register a validate script (internal use only) 
        """
        pass
    
import NXOpen
##   @brief  Multi Calculation context is passed to the multi evaluate method implementation. 
##                   It contains methods to retrieve the load case set and input parameter values,
##                   and to set the output values and log messages   
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class MultiCalculationContext(NXOpen.NXObject): 
    """ <summary> Multi Calculation context is passed to the multi evaluate method implementation. 
                  It contains methods to retrieve the load case set and input parameter values,
                  and to set the output values and log messages  </summary> """


    ##  Get calculation context array
    ##  @return ccArray (@link CalculationContext List[NXOpen.CAE.AeroStructures.Author.CalculationContext]@endlink):  .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetContextArray(context: MultiCalculationContext) -> List[CalculationContext]:
        """
         Get calculation context array
         @return ccArray (@link CalculationContext List[NXOpen.CAE.AeroStructures.Author.CalculationContext]@endlink):  .
        """
        pass
    
    ##  Reports the success or failure of the evaluation of a calculation context 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="idx"> (int) </param>
    ## <param name="success"> (bool) </param>
    def SetSuccess(context: MultiCalculationContext, idx: int, success: bool) -> None:
        """
         Reports the success or failure of the evaluation of a calculation context 
        """
        pass
    
##   @brief  Represents a boolean output parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class OutputBoolean(OutputParameter): 
    """ <summary> Represents a boolean output parameter </summary> """


    ##  Set boolean value. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def SetValue(self, param: OutputBoolean, boolVal: bool) -> None:
        """
         Set boolean value. 
        """
        pass
    
    ##  Set boolean value for a failure mode 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name 
    @overload
    def SetValue(self, param: OutputBoolean, fmName: str, boolVal: bool) -> None:
        """
         Set boolean value for a failure mode 
        """
        pass
    
    ##  Set boolean value for a failure mode and a loadcase specified by its index
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name, if empty the value will be set for any failure mode 
    @overload
    def SetValue(self, param: OutputBoolean, fmName: str, lcIndex: int, boolVal: bool) -> None:
        """
         Set boolean value for a failure mode and a loadcase specified by its index
        """
        pass
    
##   @brief  Represents a File Output parameter  
## 
##    <br> No support for KF  <br> 
class OutputFile(OutputParameter): 
    """ <summary> Represents a File Output parameter </summary> """


    ##  Retrieve the absolute path of the directory used to write output files 
    ##  @return pathVal (str):  the directory used.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetCalculationDirectory(param: OutputFile) -> str:
        """
         Retrieve the absolute path of the directory used to write output files 
         @return pathVal (str):  the directory used.
        """
        pass
    
    ##  Retrieve the absolute path of the file 
    ##  @return pathVal (str):  the directory used.
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetPath(param: OutputFile) -> str:
        """
         Retrieve the absolute path of the file 
         @return pathVal (str):  the directory used.
        """
        pass
    
    ##  Set the path of the output file being added to the output directory 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ##  the directory used
    def SetPath(param: OutputFile, pathVal: str) -> None:
        """
         Set the path of the output file being added to the output directory 
        """
        pass
    
##   @brief  Represents an integer output parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class OutputInteger(OutputParameter): 
    """ <summary> Represents an integer output parameter </summary> """


    ##  Set integer value. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def SetValue(self, param: OutputInteger, intVal: int) -> None:
        """
         Set integer value. 
        """
        pass
    
    ##  Set integer value for a failure mode 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name 
    @overload
    def SetValue(self, param: OutputInteger, fmName: str, intVal: int) -> None:
        """
         Set integer value for a failure mode 
        """
        pass
    
    ##  Set integer value for a failure mode and a loadcase specified by its index
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name, if empty the value will be set for any failure mode 
    @overload
    def SetValue(self, param: OutputInteger, fmName: str, lcIndex: int, intVal: int) -> None:
        """
         Set integer value for a failure mode and a loadcase specified by its index
        """
        pass
    
import NXOpen
import NXOpen.CAE.AeroStructures
##   @brief  Parent class of all the typed output parameter classes   
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class OutputParameter(NXOpen.NXObject): 
    """ <summary> Parent class of all the typed output parameter classes  </summary> """


    ## Getter for property: (str) Name
    ##   the name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink) Type
    ##   the parameter type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @return NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType
    @property
    def Type(self) -> NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType:
        """
        Getter for property: (@link NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType@endlink) Type
          the parameter type.  
             
         
        """
        pass
    
import NXOpen
##   @brief  Represents a scalar output parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class OutputScalar(OutputParameter): 
    """ <summary> Represents a scalar output parameter </summary> """


    ## Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Unit
    ##   the unit type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Unit
    @property
    def Unit(self) -> NXOpen.Unit:
        """
        Getter for property: (@link NXOpen.Unit NXOpen.Unit@endlink) Unit
          the unit type.  
             
         
        """
        pass
    
    ##  Set scalar value according to default unit 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the double value of the parameter
    @overload
    def SetValue(self, param: OutputScalar, doubleVal: float) -> None:
        """
         Set scalar value according to default unit 
        """
        pass
    
    ##  Set scalar value with a specific unit type. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  the double value of the parameter expressed in the specified unit
    @overload
    def SetValue(self, param: OutputScalar, doubleVal: float, unit_type: NXOpen.Unit) -> None:
        """
         Set scalar value with a specific unit type. 
        """
        pass
    
    ##  Set scalar value according to default unit for a failure mode 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name 
    @overload
    def SetValue(self, param: OutputScalar, fmName: str, doubleVal: float) -> None:
        """
         Set scalar value according to default unit for a failure mode 
        """
        pass
    
    ##  Set scalar value according to default unit for a failure mode and a loadcase specified by its index
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name, if empty the value will be set for any failure mode 
    @overload
    def SetValue(self, param: OutputScalar, fmName: str, lcIndex: int, doubleVal: float) -> None:
        """
         Set scalar value according to default unit for a failure mode and a loadcase specified by its index
        """
        pass
    
    ##  Set scalar value with a specific unit type for a failure mode 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name 
    @overload
    def SetValue(self, param: OutputScalar, fmName: str, doubleVal: float, unit_type: NXOpen.Unit) -> None:
        """
         Set scalar value with a specific unit type for a failure mode 
        """
        pass
    
    ##  Set scalar valuewith a specific unit type  for a failure mode and a loadcase specified by its index
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name, if empty the value will be set for any failure mode 
    @overload
    def SetValue(self, param: OutputScalar, fmName: str, lcIndex: int, doubleVal: float, unit_type: NXOpen.Unit) -> None:
        """
         Set scalar valuewith a specific unit type  for a failure mode and a loadcase specified by its index
        """
        pass
    
##   @brief  Represents a text output parameter  
## 
##    <br> No support for KF  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class OutputText(OutputParameter): 
    """ <summary> Represents a text output parameter </summary> """


    ##  Set text value. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  
    @overload
    def SetValue(self, param: OutputText, textVal: str) -> None:
        """
         Set text value. 
        """
        pass
    
    ##  Set text value for a failure mode 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name 
    @overload
    def SetValue(self, param: OutputText, fmName: str, textVal: str) -> None:
        """
         Set text value for a failure mode 
        """
        pass
    
    ##  Set text value for a failure mode and a loadcase specified by its index
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ##  failure mode name, if empty the value will be set for any failure mode 
    @overload
    def SetValue(self, param: OutputText, fmName: str, lcIndex: int, textVal: str) -> None:
        """
         Set text value for a failure mode and a loadcase specified by its index
        """
        pass
    
## @package NXOpen.CAE.AeroStructures.Author
## Classes, Enums and Structs under NXOpen.CAE.AeroStructures.Author namespace

##  @link AbbContextCallType NXOpen.CAE.AeroStructures.Author.AbbContextCallType @endlink is an alias for @link AbbContext.CallType NXOpen.CAE.AeroStructures.Author.AbbContext.CallType@endlink
AbbContextCallType = AbbContext.CallType


##  @link ABBEdgeSupportType NXOpen.CAE.AeroStructures.Author.ABBEdgeSupportType @endlink is an alias for @link ABB.EdgeSupportType NXOpen.CAE.AeroStructures.Author.ABB.EdgeSupportType@endlink
ABBEdgeSupportType = ABB.EdgeSupportType


##  @link ABBMaterialBehaviour NXOpen.CAE.AeroStructures.Author.ABBMaterialBehaviour @endlink is an alias for @link ABB.MaterialBehaviour NXOpen.CAE.AeroStructures.Author.ABB.MaterialBehaviour@endlink
ABBMaterialBehaviour = ABB.MaterialBehaviour


##  @link ABBPlaneStressBoundaryConditions NXOpen.CAE.AeroStructures.Author.ABBPlaneStressBoundaryConditions @endlink is an alias for @link ABB.PlaneStressBoundaryConditions NXOpen.CAE.AeroStructures.Author.ABB.PlaneStressBoundaryConditions@endlink
ABBPlaneStressBoundaryConditions = ABB.PlaneStressBoundaryConditions


##  @link ABBStatus NXOpen.CAE.AeroStructures.Author.ABBStatus @endlink is an alias for @link ABB.Status NXOpen.CAE.AeroStructures.Author.ABB.Status@endlink
ABBStatus = ABB.Status


##  @link ABBUnloadedEdgeSupportType NXOpen.CAE.AeroStructures.Author.ABBUnloadedEdgeSupportType @endlink is an alias for @link ABB.UnloadedEdgeSupportType NXOpen.CAE.AeroStructures.Author.ABB.UnloadedEdgeSupportType@endlink
ABBUnloadedEdgeSupportType = ABB.UnloadedEdgeSupportType


##  @link CalculationContextUnitSystem NXOpen.CAE.AeroStructures.Author.CalculationContextUnitSystem @endlink is an alias for @link CalculationContext.UnitSystem NXOpen.CAE.AeroStructures.Author.CalculationContext.UnitSystem@endlink
CalculationContextUnitSystem = CalculationContext.UnitSystem


##  @link InputLoadLoadSupportType NXOpen.CAE.AeroStructures.Author.InputLoadLoadSupportType @endlink is an alias for @link InputLoad.LoadSupportType NXOpen.CAE.AeroStructures.Author.InputLoad.LoadSupportType@endlink
InputLoadLoadSupportType = InputLoad.LoadSupportType


