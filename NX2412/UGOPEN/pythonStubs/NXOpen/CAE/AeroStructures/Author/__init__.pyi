from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AbbContext(NXOpen.NXObject): 
    """  ABB context is passed to the ABB implementation. 
                  It contains methods to log messages   """
    class CallType(Enum):
        """
        Members Include: 
         |Abb|  ABB call type 
         |Method|  Method call type 

        """
        Abb: int
        Method: int
        @staticmethod
        def ValueOf(value: int) -> AbbContext.CallType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetCallType(self) -> AbbContext.CallType:
        """
         Get the call type of the ABB 
         Returns call_type ( AbbContext.CallType NXOpen.CAE.Aero): .
        """
        pass
    def GetFailureMode(self) -> str:
        """
         Get the failure mode of the ABB
         Returns fm (str): .
        """
        pass
    def GetLoadCaseIndexes(self) -> List[int]:
        """
         Returns the list of load case indexes passed to the ABB 
         Returns indexes (List[int]):  list of indexes .
        """
        pass
    def SetCallType(self, call_type: AbbContext.CallType) -> None:
        """
         Set the call type of the ABB 
        """
        pass
    def SetFailureMode(self, fm: str) -> None:
        """
         Set the failure mode of the ABB
        """
        pass
    def SetLoadCaseIndexes(self, indexes: List[int]) -> None:
        """
         Sets the list of load case indexes passed to the ABB 
        """
        pass
import NXOpen
import NXOpen.CAE.AeroStructures
class ABB(NXOpen.Object): 
    """ Represents a AeroStruct application building block (ABB) """
    class EdgeSupportType(Enum):
        """
        Members Include: 
         |SimplySupported|  Simply Supported 
         |Clamped|  Clamped 

        """
        SimplySupported: int
        Clamped: int
        @staticmethod
        def ValueOf(value: int) -> ABB.EdgeSupportType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialBehaviour(Enum):
        """
        Members Include: 
         |Elastic|  Elastic behaviour 
         |ElasticPlastic|  Elastic-plastic behaviour 

        """
        Elastic: int
        ElasticPlastic: int
        @staticmethod
        def ValueOf(value: int) -> ABB.MaterialBehaviour:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlaneStressBoundaryConditions(Enum):
        """
        Members Include: 
         |Ssss|  loaded edges: simply supported, unloaded edges: simply supported - simply supported 
         |Cscs|  loaded edges: clamped,          unloaded edges: simply supported - simply supported 
         |Scsc|  loaded edges: simply supported, unloaded edges: clamped - clamped 
         |Cccc|  loaded edges: clamped,          unloaded edges: clamped - clamped 
         |Sfss|  loaded edges: simply supported, unloaded edges: free - simply supported 

        """
        Ssss: int
        Cscs: int
        Scsc: int
        Cccc: int
        Sfss: int
        @staticmethod
        def ValueOf(value: int) -> ABB.PlaneStressBoundaryConditions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Status(Enum):
        """
        Members Include: 
         |Success|  ABB computation success 
         |Failed|  ABB computation failed 

        """
        Success: int
        Failed: int
        @staticmethod
        def ValueOf(value: int) -> ABB.Status:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UnloadedEdgeSupportType(Enum):
        """
        Members Include: 
         |ClampedClamped|  Clamped-Clamped 
         |SimplySupportedClamped|  Simply Supported-Clamped 
         |SimplySupportedSimplySupported|  Simply Supported-Simply Supported 
         |FreeClamped|  Free-Clamped 
         |FreeSimplySupported|  Free-Simply Supported 

        """
        ClampedClamped: int
        SimplySupportedClamped: int
        SimplySupportedSimplySupported: int
        FreeClamped: int
        FreeSimplySupported: int
        @staticmethod
        def ValueOf(value: int) -> ABB.UnloadedEdgeSupportType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
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
                        
         Returns A tuple consisting of (status, kc). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - kc is: float. Compressive-buckling coefficient .

        """
        pass
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
                        
         Returns A tuple consisting of (status, ks). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - ks is: float. Compressive-buckling coefficient .

        """
        pass
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
                        
         Returns A tuple consisting of (status, A, oYcog, E, oIxx). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - A is: List[float]. Area of the equivalent section (sum of all sub-sections) .
         - oYcog is: List[float]. Center of gravity of the equivalent section in Y direction .
         - E is: List[float]. Young's modulus of the equivalent section .
         - oIxx is: List[float]. Moment of inertia of the equivalent section around XX (expressed at the center of gravity of the equivalent section) .

        """
        pass
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
                        
         Returns A tuple consisting of (status, iFcc). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - iFcc is: float. Equivalent stress allowable .

        """
        pass
    def FlatMetallicPanelBendingBucklingCoefficient(abbContext: AbbContext, a_over_b: float, beta: float) -> Tuple[ABB.Status, float]:
        """
                            Curves for finding the bending buckling stress coefficient for thin flat plates
                            Used for finding 'kb' the bending buckling stress coefficient as a function of:
                             'ab', the panel length ratio
                             'a' is the unloaded edge length
                             'b' is the loaded edge length
                             'beta',  is the factor which, divided to b, gives the edge length in compression (while
                            the remaining edge length is in tension).
                            Input
                                a_over_b    Panel length ratio
                                beta        Loading length ratio
                            Output
                                kb          Bending buckling stress coefficient
                            Returns
                                False if input values are out of bounds
                        
         Returns A tuple consisting of (status, kb). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - kb is: float. Bending buckling stress coefficient .

        """
        pass
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
                        
         Returns A tuple consisting of (status, kc). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - kc is: float. Compressive buckling coefficient .

        """
        pass
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
                        
         Returns A tuple consisting of (status, ks). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - ks is: float. Shear-buckling coefficient .

        """
        pass
    def GetIntegerNa() -> int:
        """
                            Integer NA value
                        
         Returns value (int): .
        """
        pass
    def GetMsThreshold() -> float:
        """
                            The MS (margin of safety) threshold
                        
         Returns ret (float): .
        """
        pass
    def GetPi() -> float:
        """
                            PI number
                        
         Returns value (float): .
        """
        pass
    def GetRealEpsilon() -> float:
        """
                            Real epsilon
                        
         Returns value (float): .
        """
        pass
    def GetRealMax() -> float:
        """
                            Maximum real number
                        
         Returns value (float): .
        """
        pass
    def GetRealNa() -> float:
        """
                            Real NA
                        
         Returns value (float): .
        """
        pass
    def GetRealNegativeInfinity() -> float:
        """
                            The negative infinity value
                        
         Returns value (float): .
        """
        pass
    def GetRealPositiveInfinity() -> float:
        """
                            The positive infinity value
                        
         Returns value (float): .
        """
        pass
    def GetUltimateLimitFactor() -> float:
        """
                            Ultimate limit factor from the customer default
                        
         Returns value (float): .
        """
        pass
    def IsRealNa(value: float) -> bool:
        """
                            Tests if a value is NA
                        
         Returns ret (bool): .
        """
        pass
    def IsRealNegativeInfinity(value: float) -> bool:
        """
                            Tests if a value equals negative infinity
                        
         Returns ret (bool): .
        """
        pass
    def IsRealPositiveInfinity(value: float) -> bool:
        """
                            Tests if a value equals positive infinity
                        
         Returns ret (bool): .
        """
        pass
    def Lcf1dMinMax(abbContext: AbbContext, load: NXOpen.GeneralScalarTable, tolerance: float, nb_loadcases: int) -> Tuple[ABB.Status, List[float], List[bool], NXOpen.GeneralScalarTable, float, float, float, float]:
        """
         
                            Min Max 1D Method
                            A single load case extraction result table (general scalar table) is provided.
                            Returns:
                            - centrality data (how near the boundary each value is)
                            - an array of boolean set true for each selected load case
                            - the boundary values and tolerance thresholds
                         
         Returns A tuple consisting of (status, centrality, lc_selected, point_centrality, boundary_min, boundary_max, tolerance_min, tolerance_max). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - centrality is: List[float].
         - lc_selected is: List[bool].
         - point_centrality is:  NXOpen.GeneralScalarTable.
         - boundary_min is: float.
         - boundary_max is: float.
         - tolerance_min is: float.
         - tolerance_max is: float.

        """
        pass
    def LcfConvexHull(abbContext: AbbContext, load1: NXOpen.GeneralScalarTable, load2: NXOpen.GeneralScalarTable, tolerance: float, nb_loadcases: int) -> Tuple[ABB.Status, List[float], List[bool], NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, NXOpen.GeneralScalarTable, float, float, float, float]:
        """
         
                            Convex hull Method
                            The two load case extraction result tables (general scalar table) are given to the method.
                            They should be related to the same meshing entities, columns should be in the same order.
                            Use the FilterByLoadSupport if needed.
                            Tolerance should be in [0,1].
                            The centrality of a load case LC_i is defined as the shortest distance from the entity 
                            loads to the convex hull in the direction and relative to centroid (reference point).
                            
                            Centrality_i = min_(j in [1,NbEntities])(distance(C_j,L_j)distance(C_j,R))
                            with
                                - Centrality_i the centrality of the ith loadcase LC_i.
                                - L_j the value of the input load LC_i in the jth selected entity.
                                - C_j the point where the line between the reference point and the 
                                  LC_i of the jth selected entity intersects the convex hull.
                                - R the reference point used in the computation of the relative 
                                  distance is the centroid of the convex hull polygon.
                                - NbEntities the number of entities in LC_i
                            
                            A load case is critical when Centrality_i is lower or equal to tolerance, for all i in [1,NbLC].
                         
         Returns A tuple consisting of (status, centrality, lc_selected, point_centrality, boundary_envelope, boundary_tolerance, load1_min, load1_max, load2_min, load2_max). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - centrality is: List[float]. Centralities.
         - lc_selected is: List[bool]. True if the load case is selected, false otherwise.
         - point_centrality is:  NXOpen.GeneralScalarTable.
         - boundary_envelope is:  NXOpen.GeneralScalarTable. Boundary Envelope .
         - boundary_tolerance is:  NXOpen.GeneralScalarTable. Boundary Tolerance .
         - load1_min is: float. Load 1 min.
         - load1_max is: float. Load 1 max.
         - load2_min is: float. Load 2 min.
         - load2_max is: float. Load 2 max.

        """
        pass
    def LcfFilterLoadsBySupport(abbContext: AbbContext, inputLoads: List[InputLoad]) -> Tuple[ABB.Status, List[NXOpen.GeneralScalarTable]]:
        """
         
                            Obtain load extraction GeneralScalarTables whose columns
                            (support entities) are common to all load extractions.  This
                            assumes GSTs where aggregation is done 'by method'.  Only
                            entities common to all load extractions are returned.
                         
         Returns A tuple consisting of (status, tables). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - tables is:  NXOpen.GeneralScalarTable Li. filtered GeneralScalarTables .

        """
        pass
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
                         
         Returns A tuple consisting of (status, load1_max, load1_min, load2_max, load2_min, centrality_1, centrality_2, centrality, lc_selected, point_centrality_1, point_centrality_2, boundary_envelope, boundary_tolerance). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - load1_max is: float.
         - load1_min is: float.
         - load2_max is: float.
         - load2_min is: float.
         - centrality_1 is: List[float].
         - centrality_2 is: List[float].
         - centrality is: List[float].
         - lc_selected is: List[bool].
         - point_centrality_1 is:  NXOpen.GeneralScalarTable.
         - point_centrality_2 is:  NXOpen.GeneralScalarTable.
         - boundary_envelope is:  NXOpen.GeneralScalarTable. Boundary Envelope .
         - boundary_tolerance is:  NXOpen.GeneralScalarTable. Boundary Tolerance .

        """
        pass
    def LoadDistributionBoltsConcentricLoads(abbContext: AbbContext, P: List[float], iPsn: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            Computes bolt loads for multiple bolt fitting - Concentric load
                            Formula
                                Pn = P  (Psn  SUM(Psn))
                            where:
                                 'P' is the load acting on the fitting
                                 'Psn' is the allowable strength of bolt n
                                 'Pn' is the shear load on bolt n
                            Input
                                nblc    Number of load cases
                                P       Load acting on fitting (nblc)
                                nbbolt  Number of bolts
                                Psn     Allowable shear strength of bolt (nbbolt)
                            Output
                                Pn      Shear load on bolt (nblc x nbbolt)
                            Return
                                Status of the calculation
                        
         Returns A tuple consisting of (status, oPn). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - oPn is: List[float]. Shear load on bolt (nblc x nbbolt) .

        """
        pass
    def MaterialFsyEstimation(abbContext: AbbContext, iFtyL: float, iFtyLT: float, iFcyL: float, iFcyLT: float, iFsu: float, iFtuL: float, iFtuLT: float) -> Tuple[ABB.Status, float]:
        """
                            Estimation of shear yield stress (Fsy)
                            Shear yield stress allowable ('Fsy') is estimated on the basis of the following formula:
                            'Fsy=( FtyL + FtyLT + FcyL + FcyLT )  4  ( 2  Fsu)( FtuL + FtuLT )'
                            where:
                             'FtyL' is the tensile yield stress under longitudinal direction
                             'FtyLT' is the tensile yield stress under long transverse direction
                             'FcyL' is  the compressive yield stress under longitudinal direction
                             'FcyLT' is the compressive yield stress under long transverse direction
                             'Fsu' is the shear ultimate stress
                             'FtuL' is the tensile ultimate stress under longitudinal direction
                             'FtuLT' is the tensile ultimate stress under long transverse direction
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
                        
         Returns A tuple consisting of (status, oFsy). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - oFsy is: float. Shear yield stress .

        """
        pass
    def MetallicPanelCompressivePlasticityCurveBc1(abbContext: AbbContext, X: float, n: float) -> Tuple[ABB.Status, float]:
        """
                        Metallic panel compressive plasticity curve BC1
                        Curves for finding critical buckling stress  secant yield stress F0.7
                        Used for finding 'sigma_cr' the inelastic buckling strength of metallic flat rectangular plate in compression.
                        The Boundary Condition for the unloaded edges is Simply Supported-Free. It computes:
                         'sigma_cr sigma_0.7' as a function of '(kc  pi^2E)  (12  (1-nu^2)  sigma_0.7)(tb)^2'  and 'n' where
                         'sigma_cr' is the  critical stress allowable
                         'sigma_0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
                         'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
                         'E' is the Young's modulus
                         'nu' is the Poisson's ratio
                         't' is the plate thickness
                         'b' is the loaded edge length
                         'n' is the Ramberg-Osgood parameter
                        Input
                            X   Critical buckling stress (elastic)  secant yield stress F0.7
                            n   Ramberg-Osgood parameter
                        Output
                            Z   Critical buckling stress (including plasticity)  secant yield stress F0.7
                        Returns
                            Status of the computation
                        
         Returns A tuple consisting of (status, Z). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - Z is: float. Critical buckling stress (including plasticity)  secant yield stress F0.7 .

        """
        pass
    def MetallicPanelCompressivePlasticityCurveBc2(abbContext: AbbContext, X: float, n: float) -> Tuple[ABB.Status, float]:
        """
                            Metallic panel compressive plasticity curve BC2
                            Curves for finding critical inter-rivet buckling stress (or critical wrinkling stress)  secant yield stress F0.7
                            Used for finding 'Fir' or 'Fw'.
                            It computes either:
                             'Fir F0.7' as a function of '(C  pi^2E)(12  (1-nu^2)  F0.7)(tsp)^2' and 'n' where
                                  'Fir' is the Inter-Rivet Buckling stress allowable (with plasticity)
                                  'F0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
                                  'C' is the end fixity coefficient
                                  'E' is the Young's modulus
                                  'nu' is the Poisson's ratio
                                  'ts' is the thickness of the sheet
                                  'p' is the rivet spacing
                                  'n' is the Ramberg-Osgood parameter
                            Or:
                             'Fw F0.7' as a function of '(kw  pi^2E)(12  (1-nu^2)  F0.7)(tsbs)^2' and 'n' where
                                  'Fw' is the wrinkling stress allowable
                                  'kw' is the wrinkling failing stress coefficient
                                  'ts' is the thickness of the sheet
                                  'bs' is the stiffener spacing
                                  'n' is the Ramberg-Osgood parameter
                            Input
                                X   Critical buckling stress (elastic)  secant yield stress F0.7
                                n   Ramberg-Osgood parameter
                            Output
                                Z   Critical bucklingwrinkling stress (including plasticity)  secant yield stress F0.7
                            Returns
                                Status of the computation
                        
         Returns A tuple consisting of (status, Z). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - Z is: float. Critical bucklingwrinkling stress (including plasticity)  secant yield stress F0.7 .

        """
        pass
    def MetallicPanelCompressivePlasticityCurveBc3(abbContext: AbbContext, X: float, n: float) -> Tuple[ABB.Status, float]:
        """
                            Metallic panel compressive plasticity curve BC3
                            Curves for finding critical buckling stress  secant yield stress F0.7
                            Used for finding 'sigma_cr' the inelastic buckling strength of metallic cylinder in compression.
                            It computes:
                             'sigma_cr sigma_0.7' as a function of '(kc  pi^2E)(12  (1-nu^2)  sigma_0.7)(tb)^2'  and 'n' where
                                  'sigma_cr' is the  critical stress allowable
                                  'sigma_0.7' is the [stress for secant modulus equal to 70% of Young's modulus]
                                  'kc' is the buckling coefficient, computed in Figure FlatMetallicPanelCompressiveBucklingCoefficient
                                  'E' is the Young's modulus
                                  'nu' is the Poisson's ratio
                                  't' is the plate thickness
                                  'b' is the loaded edge length
                                  'n' is the Ramberg-Osgood parameter
                            Input
                                X   Critical buckling stress (elastic)  secant yield stress F0.7
                                n   Ramberg-Osgood parameter
                            Output
                                Z   Critical buckling stress (including plasticity)  secant yield stress F0.7
                            Returns
                                Status of the computation
                        
         Returns A tuple consisting of (status, Z). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - Z is: float. Critical buckling stress (including plasticity)  secant yield stress F0.7 .

        """
        pass
    def MsAllowable(abbContext: AbbContext, allowable: float, value: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS allowable.
                            Computes margin of safety based on an allowable
                            The formula is MS = Allowable  Value - 1
                            where:
                             'Allowable' is the manual input
                             'Value' is the value coming from load extractor
                             'MS' is the margin of safety
                            Input
                                Allowable   Manual input
                                Value(nblc) Value coming from load extractor
                            Output
                                MS(nblc)    Margin of safety
                            Return
                                Status of the calculation
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsBearing(abbContext: AbbContext, D: float, t: float, iFbr: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS bearing
                            Computes margin of bearing
                            The formula is 'MS = PBearingAllowable  P - 1'
                            where
                             'PBearingAllowable' is the bearing load allowable ('PBearingAllowable = Fbr  D  t')
                                'Fbr' is the bearing stress allowable
                                'D' is the diameter
                                't' is the thickness
                             'P' is the bearing load (P = FactorLoad  PExtracted)
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsBoltBending(abbContext: AbbContext, b: float, iMba: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS bolt bending
                            Computes margin of safety of a bolt under bending load
                            The formula is 'MS = MBendingAllowable  M - 1'
                            where
                             'MBendingAllowable' is the bending moment allowable of the bolt.
                             'M' is the bending moment applied to the bolt. ('M = b  P')
                                where:
                                'b' is the arm
                                'P' is the load ('P = FactorLoad  PExtracted')
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsBoltCombinedShearTension(abbContext: AbbContext, iPtx: float, iPss: float, iPx: List[float], f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS bolt combined shear tension
                            Computes margin of safety of a bolt under shear load and tension load
                            The formula is 'MS = 1  sqrt( Rt ^ 2 + Rs ^ 3 )  - 1'
                            where
                                 Rt = PTensileXPTensileAllowable
                                 Rs = PShearPShearAllowable
                                'PTensileAllowable' is the tensile load allowable of the bolt
                                 'PTensileX' is the tensile load applied on the fastener
                                 'PShearAllowable' is the single shear load allowable of the bolt
                                 'Pshear' is the shearing load applied through the shear area. PShear = FactorLoad  PExtracted
                                 'FactorLoad' is the ratio of load between extracted load PExtracted and PShear
                                 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
                                 'Py' is the shear load in Y direction
                                 'Pz' is the shear load in Z direction
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsBoltCombinedShearTensionBending(abbContext: AbbContext, b: float, iMba: float, iPtx: float, iPss: float, fb: float, iPb: List[float], iPx: List[float], fs: float, iPs: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS bolt combined shear tension bending
                            Computes margin of safety of a bolt under shear, tension and bending load
                            The formula is MS = 1  sqrt ( ( Rt + Rb ) ^ 2 + Rs ^ 3 ) - 1
                            where
                                 Rt = PTensileX  PTensileAllowable
                                 Rb = M  MAllowable
                                 Rs = PShear  PShearAllowable
                                Tensile data
                                 'PTensileAllowable' is the tensile load allowable of the bolt
                                 'PTensileX' is the tensile load applied on the fastener
                                Bending data
                                 'MAllowable' is the bending moment allowable of the bolt
                                 'M' is the bending moment applied to the bolt.
                                    M = b  PBend
                                    PBend = FactorLoadBend  sqrt(PyBend^2 + PzBend^2)
                                 'b' is the arm
                                 'FactorLoadBend' is the load factor for bending
                                 'PyBend' is the bending load in Y direction
                                 'PzBend' is the shear load in Z direction
                                Shear data
                                 'PShearAllowable' is the single shear load allowable of the bolt
                                 'PShear' is the shearing load applied through the shear area.
                                    PShear = FactorLoadShear  sqrt(PyShear^2 + PzShear^2)
                                 'FactorLoadShear' is the load factor for shearing
                                 'PyShear' is the shear load in Y direction
                                 'PzShear' is the shear load in Z direction
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsBoltShear(abbContext: AbbContext, iPss: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS bolt shear
                            Computes margin of safety of a bolt under shear load
                            The formula is MS = PShearAllowable  P  - 1
                            where
                                 'PShearAllowable' is the single shear load allowable of the bolt
                                 'P' is the shearing load applied through the shear area. P = FactorLoad  PExtracted
                                 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
                                 'PExtracted' is the extracted load ('PExtracted = sqrt(Py^2 + Pz^2)')
                                 'Py' is the shear load in Y direction
                                 'Pz' is the shear load in Z direction
                            Input
                                NbLC                Number of loadcases
                                Pss                 Single shear load allowable
                                f                   Load factor
                                P(NbLC)             Shear load
                            Output
                                MS                  Margin of safety
                            Return
                                Status of the calculation
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsColumnEccentricLoadSecantFormula(abbContext: AbbContext, A: float, L: float, E: float, I: float, sigmacr: float, C: float, ecc: float, extrmfbrdist: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
                            MS Column Eccentric Load
                            Computes margin of safety of column under eccentric axial compressive load (secant formula theory)
                            When the axial compressive load is not applied on the centroid of the column cross section eccentricity has to be taken into account.
                            MS = Pcr  (abs(P)) - 1
                            where:
                                 Pcr is the compressive load allowable
                                 P is the axial compressive load (MS is not calculated in case of tensile stress)
                            Pcr = (sigmacrA)(1 + (eccc)rho^2 sec (12 sqrt(Pcr)(EA)(L')rho))
                            where:
                                 sigmacr is the material stress allowable
                                 A the area of the cross section
                                 I is the bending inertia of the column
                                 ecc the eccentricity of the load (distance between the line of action of P and the axis of the column)
                                 c the distance of extreme fiber to neutral axis
                                 rho is the radius of gyration of cross-section given by rho=sqrt(IA)
                                 E the material Young modulus
                                 L' is the column effective length given by L'=Lsqrt(C)
                                     L the column length
                                     C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
                                         Pinned-Pinned: C=1
                                         Fixed-Fixed: C=4
                                         Fixed-Pinned: C=2.05
                                         Fixed-Free: C=0.25
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
                        
         Returns A tuple consisting of (status, iPcr, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - iPcr is: float. Compressive load allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsColumnEngesser(abbContext: AbbContext, A: float, L: float, E: float, I: float, n: float, iFy: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
                            MS Engesser
                            Computes margin of safety on the basis of Engesser column buckling theory (also called tangent-modulus theory)
                            MS = sigmacr  (abs(sigma)) - 1
                            where:
                                 sigmacr is the Engesser buckling stress allowable
                                 sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
                            sigmacr = (pi^2 Et)((L') rho)^2
                            where:
                                 Et is the tangent Young modulus of the column material given by Et=sigma((sigmaE)+0.002n(sigmafy)^n)) with
                                     sigma is the stress
                                     fy is the yield stress
                                     E is the Young's modulus
                                     n is the Ramberg-Osgood parameter
                                 L' is the column effective length given by L'=Lsqrt(C) with
                                     L the column length
                                     C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
                                         Pinned-Pinned: C=1
                                         Fixed-Fixed: C=4
                                         Fixed-Pinned: C=2.05
                                         Fixed-Free: C=0.25
                                 rho is the radius of gyration of cross-section given by rho=sqrt(IA) with
                                     I is the bending inertia of the column
                                     A is the column cross section area
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
                        
         Returns A tuple consisting of (status, sigmacr, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - sigmacr is: float. Engesser buckling stress allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsColumnEuler(abbContext: AbbContext, A: float, L: float, E: float, I: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
                            MS Euler
                            Computes margin of safety on the basis of Euler column buckling theory
                            MS = sigmacr  (abs(sigma)) - 1
                            where:
                                 sigmacr is the Euler buckling stress allowable
                                 sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
                            sigmacr = (pi^2 E)((L') rho)^2
                            where:
                                 E is the Young modulus of the column material
                                 L' is the column effective length given by L'=Lsqrt(C) with
                                     L the column length
                                     C the end fixity coefficient depending on the Boundary Condition given at both extremities. Please find some values:
                                         Pinned-Pinned: C=1
                                         Fixed-Fixed: C=4
                                         Fixed-Pinned: C=2.05
                                         Fixed-Free: C=0.25
                                 rho is the radius of gyration of cross-section given by rho=sqrt(IA) with
                                     I is the bending inertia of the column
                                     A is the column cross section area
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
                        
         Returns A tuple consisting of (status, sigmacr, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - sigmacr is: float. Euler buckling stress allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsColumnJohnsonEuler(abbContext: AbbContext, A: float, L: float, I: float, E: float, C: float, sigma0: float, sigma: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
                            MS Column Johnson-Euler
                            Computes margin of safety on the basis of Johnson-Euler column theory
                            MS = sigmacr  (abs(sigma)) - 1
                            where:
                                 sigmacr is the Johnson-Euler stress allowable
                                 sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
                            To find the column failing stress under axial compressive load (sigmacr)) Euler or Johnson-Euler equations are used (choice is done depending L'rho):
                                 The Euler equation is sigmacr = (pi^2E)(L'rho)^2 (use in case L'rho greater than sigma02)
                                 The Johnson-Euler equation is sigmacr = sigma0-sigma0^2(4pi^2E)(L'rho)^2 (use in case L'rho smaller than sigma02)
                            where:
                             sigma0 is the column stress allowable for a column slenderness equals to 0. It is the minimal value between crippling stress and yield allowable in compression of column.
                             E is the Young modulus of the column material
                                 L' is the column effective length given by L'=Lsqrt(C)
                                     L the column length
                                     C the end fixity coefficient depending on the Boundary Condition (BC) given at both extremities. Please find some values:
                                         Pinned-Pinned: C=1
                                         Fixed-Fixed: C=4
                                         Fixed-Pinned: C=2.05
                                         Fixed-Free: C=0.25
                             rho is the radius of gyration of cross-section given by rho=sqrt(IA)
                                 I is the bending inertia of the column
                                 A is the column cross section area
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
                        
         Returns A tuple consisting of (status, sigmacr, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - sigmacr is: float. Johnson-Euler Stress Allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsColumnTorsionalbuckling(abbContext: AbbContext, L: float, E: float, G: float, J: float, gamma: float, r0: float, C: float, load: List[float]) -> Tuple[ABB.Status, float, List[float]]:
        """
                            MS Torsional Buckling
                            Computes margin of safety of torsional buckling of a column
                            MS = iPcr  (abs(load)) - 1
                            where:
                                 iPcr is the torsional buckling load allowable
                                 load is the axial compressive load (MS is not calculated in case of tensile load)
                            Hypotheses: Column cross section has two axes of symetry or is point symmetric and the shear center and centroid is coinciding.
                            iPcr = 1r0^2(GJ+(Egammapi^2)(L')^2)
                            where:
                                 E is the Young modulus of the column material
                                 G is the shear modulus of elasticity
                                 L' is the column effective length L'=Lsqrt(C) with:
                                     L the column length
                                     C the end fixity coefficient depending on the Boundary Condition given at both extremities.
                                 r0 is the polar radius of gyration of the section about its shear center
                                 J is the torsion constant of the section
                                 gamma is the warping constant of the section
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
                        
         Returns A tuple consisting of (status, iPcr, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - iPcr is: float. Torsional buckling load allowable .
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsCompositePlateBucklingFlatCompressive(abbContext: AbbContext, b: float, a: float, bc: ABB.PlaneStressBoundaryConditions, laminate: NXOpen.CAE.AeroStructures.Laminate, sigma: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
         
                            Computes margin of safety of a rectangular flat composite panel in buckling under compressive loads.
                            sigma_allowable is the allowable compressive stress computed as:
                            'sigma_allowable = N_xcrt' 
                            where:
                             'N_xcr' is the allowable compressive load in longitudinal direction and 
                             't' is the total thickness of the laminate
         
                            A margin of safety can be derived from this formulation:
                            'MS=sigma_allowable(abs(sigma))-1  (Compression; sigma less than 0)'
                            'MS=NaN (Tension; sigma greater or equal than 0)'
                            Where:
                             'sigma' is the measured compressive stress
                            the allowable compressive load depends on the boundary conditions:
                             SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
                            N_xcr = pi^2(D_11m^4 + 2(D_12+2D_66)m^2AR^2 + D_22AR^4)(a^2m^2)
                             CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
                            'N_xcr = pi^2b^2  sqrt(D_11D22)K_min'
                            'K(m) = 4lambda^2 + 2(D_12+2D_66)sqrt(D_11D_22) + 34lambda^2, for lambda between 0 and 1.662'
                            'K(m) = (m^4+8m^2+1)(lambda^2(m^2+1)) + 2(D_12+2D_66)sqrt(D_11D_22) + lambda^2(m^2+1), for lambda larger than 1.662'
                             SCSC (loaded edges: simply supported, unloaded edges: clamped - clamped)
                            'N_xcr = pi^2b^2sqrt(D_11D_22)K_min'
                            'K = m^2lambda^2 + 2(D_12+2D_66)sqrt(D_11D_22) + 163lambda^2m^2'
                             CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
                            'N_xcr = pi^2b^2sqrt(D_11D22)K_min'
                            'K(m) = 4lambda^2 + (8(D_12+2D_66))(3sqrt(D_11D_22 )) + 4lambda^2, for lambda between 0 and 1.094'
                            'K(m) = (m^4+8m^2+1)(lambda^2(m^2+1)) + (2(D_12+2D_66))sqrt(D_11D_22) + lambda^2(m^2+1), for lambda larger than 1.094'
                             SFSS (loaded edges: simply supported, unloaded edges: free - simply supported)
                            'N_xcr = pi^2b^2sqrt(D_11D22)K_min'
                            'K(m) = 12pi^2D_66sqrt(D_11D22) + 1lambda^2'
                            Where:
                             'a' is the unloaded edge length
                             'b' is the loaded edge length
                             'AR =ab' is the length to width ratio
                             'D_ij' are the equivalent flexural stiffenesses of the laminate
                             'lambda' is obtained from 'lambda = AR(D_22D_11)^(14)'
                             'K = K(m) is the buckling coefficient
                             'm' is the longitudinal half-waves number (buckling mode)
                             'Kmin' is the minimum value of K(m) for m integer.
                        
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
                        
         Returns A tuple consisting of (status, MS, sigmaAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Compressive stress allowable .

        """
        pass
    def MsCompositePlateBucklingFlatLongitudinalShearCombined(abbContext: AbbContext, b: float, a: float, bc: ABB.PlaneStressBoundaryConditions, laminate: NXOpen.CAE.AeroStructures.Laminate, sigma: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
         
                            Computes margin of safety of a rectangular flat composite panel in buckling under combined shear and longitudinal loads.
                            Under longitudinal and shear loads, the interaction equation is:
                            'R_L + R_S^(1.9+0.1beta) = 1'
                            Where:
                             'R_L = sigmasigma_cr' is the stress ratio due to longitudinal stress
                                 'sigma' is the given longitudinal stress
                                 'sigma_cr' is the compression stress allowable for buckling, as computed by method MS_Composite_PlateBuckling_FlatCompressive
                             'R_S = tautau_cr' is the critical ratio of buckling coefficients due to shear stress
                                 'tau' the given shear stress
                                 'tau_cr' the shear stress allowable for buckling as computed by method MS_Composite_PlateBuckling_FlatShear
                             'beta = (D_12+2D_66)sqrt(D_11D_22)' is a non-dimensional orthotropic material parameter defined by the interaction equation
                             'D_ij' are the equivalent flexural stiffenesses of the laminate
                            The following boundary conditions are supported:
                             SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
                             CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
                             CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
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
                        
         Returns A tuple consisting of (status, MS, sigmaAllowable, tauAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Compressive stress allowable .
         - tauAllowable is: float. Shear stress allowable .

        """
        pass
    def MsCompositePlateBucklingFlatShear(abbContext: AbbContext, b: float, a: float, bc: ABB.PlaneStressBoundaryConditions, laminate: NXOpen.CAE.AeroStructures.Laminate, tau: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
         
                            Computes margin of safety of a rectangular flat composite panel in buckling under shear loads.
                            The MS is calculated by the formula:
                            'MS = sigma_Allowable(abs(tau)) - 1'
                            Where:
                             'tau_allowable=N_xycrt' is the allowable shear stress
                             'tau' is the shear stress
                             'N_xycr = (k_spi^2)b^2(D_11D_22^3)^(14)' is the allowable shear load
                             't' is the total thickness of the laminate
                             'b' is the first edge length
                             'a' is the second edge length
                             'D_ij' are the equivalent flexural stiffenesses of the laminate
                             'theta=sqrt(D_11D_22)(D_12+2D_66)'
                             'B = ba(D_11D_22)^(14)'
                            The shear buckling coefficient k_s is expressed in terms of two non-dimensional parameters theta and B as a 
                            function of the aspect ratio and the orthotropic bending stiffnesses. The value depends on the boundary conditions:
                             SSSS (loaded edges: simply supported, unloaded edges: simply supported - simply supported)
                            'k_s = 3.32 + 2.17theta - 0.163theta^2 + B^2(1.54+2.36theta+0.1theta^2)'
                             CSCS (loaded edges: clamped, unloaded edges: simply supported - simply supported)
                            'k_s(theta,B)' is interpolated from a 2D table of values
                             CCCC (loaded edges: clamped, unloaded edges: clamped - clamped)
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
                        
         Returns A tuple consisting of (status, MS, tauAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - tauAllowable is: float. Shear stress allowable .

        """
        pass
    def MsInterrivetbucklingColumn(abbContext: AbbContext, t: float, p: float, behaviour: ABB.MaterialBehaviour, E: float, iFy: float, n: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
         
                            MS Inter-rivet buckling (Column)
                            Computes margin of safety of inter-rivet buckling (theory coming from Euler column theory)
                            MS = sigmacr  (abs(sigma)) - 1
                            where:
                                 sigmacr is the inter-rivet buckling stress allowable
                                 sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
                            Inter-rivet buckling stress allowable (sigmacr) assumes that sheet between adjacent rivets acts as a column.
                            The formula (derived from Euler theory) is:
                                 sigmacr=(Pi^2E)(psqrt(C)0.29t)^2 if material is considered as elastic (Material behaviour = Elastic)
                                 sigmacr=(Pi^2Et)(psqrt(C)0.29t)^2 if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic). This formulation is a derivation of tangent modulus therory (Engesser).
                            where:
                                 Et is the tangent modulus given by Et=sigma((sigmaE)+0.002n(sigmafy)^n)) with
                                     sigma is the stress
                                     fy is the yield stress
                                     E is the Young's modulus
                                     n is the Ramberg-Osgood parameter
                                 E is the Young's modulus
                                 p is the the rivet spacing
                                 t is the thickness of sheet
                                 C is the end fixity coefficient
                                     Universal head (or flat head) - C = 4
                                     Brazier head - C = 3
                                     Countersunk rivet - C = 1
                                     Spotwelds - C = 3.5
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsInterrivetbucklingWidecolumn(abbContext: AbbContext, t: float, p: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, C: float, sigma: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
         
                            MS Inter-rivet buckling (wide column)
                            Computes margin of safety of inter-rivet buckling (theory  based on plate buckling - wide column assumption)
                            MS = sigmacr  abs(sigma) - 1
                            where:
                             sigmacr is the inter-rivet buckling stress allowable
                             sigma is the axial compressive stress (MS is not calculated in case of tensile stress)
                            Inter-rivet buckling stress allowable (sigmacr) assumes that the sheet acts as a wide column at its ends and whose length is equal to the rivet spacing.
                            The formula (derived from buckling plate theory) is: sigmacr=(C pi^2eta E)(12 (1-nu^2))(tp)^2
                            where:
                                 E is the young's modulus
                                 eta is the clad correction factor (supposed to be equal to 1)
                                 nu is the Poisson coefficient
                                 t is the thickness of the sheet
                                 p is the the rivet spacing
                                 C is the end fixity coefficient
                                     Universal head (or flat head) - `C` = 4
                                     Brazier head - `C` = 3
                                     Countersunk rivet - `C` = 1
                                     Spotwelds - `C` = 3.5
                                 eta is the plasticity reduction factor: sigmacr(Plastic)=eta.sigmacr(Elastic)
                                 eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                                 eta is obtain from following charts sigmacr(Plastic))sigma(0.7)=f(sigmacr(Elastic)sigma(0.7)) if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsNetSection(abbContext: AbbContext, D: float, b: float, t: float, iFx: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS Net section
                            Computes margin of net section (due to bolt hole)
                            The formula is MS = PNetSectionAllowable  P - 1
                            where:
                             'PNetSectionAllowable' is the net section load allowable.
                                PNetSectionAllowable = SigmaAllowable  t  ( b - D )
                                 'SigmaAllowable' is the material stress allowable. For instance, it could be Ftu
                                 'D'    is the hole diameter
                                 't' is the thickness
                                 'b' is the width of the net section
                             'P' is the load.
                                P = FactorLoad  PExtracted
                                 'FactorLoad' is the ratio of load between extracted load 'PExtracted' and 'P'
                                 'PExtracted' is the extracted load
                             'MS' is the margin of safety
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsPlateBuckling(abbContext: AbbContext, b: float, t: float, E: float, nu: float, eta: float, k: float, sigma: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS Plate Buckling
                            Computes margin of safety of a metallic plate under buckling load (generic formula)
                            The formula is MS = Allowable  Stress - 1
                            where:
                             'Allowable' is the compressive buckling stress allowable
                             'Stress' is the stress
                             'MS' is the margin of safety
                            Allowable = eta  PI^2kE(12(1-nu^2))  (tb)^2
                            where
                             'k' is the buckling coefficient
                             'E' is the Young's modulus
                             'nu' is the elastic Poisson's ratio
                             't' is the panel thickness
                             'b' is the panel dimension
                             'eta' is the plasticity reduction factor: SigmaAllowablePlastic = etaSigmaAllowableElastic
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsPlateBucklingCurvedCompressive(abbContext: AbbContext, b: float, a: float, t: float, r: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
                            MS Plate Buckling Curved Compressive
                            Computes margin of safety of a curved metallic rectangular panel under compressive load
                            The formula is MS = Allowable  |Stress| - 1
                            where:
                             'Allowable' is the compressive buckling stress allowable
                             'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
                             'MS' is the margin of safety
                            Allowable = eta  PI^2kcE(12(1-nu^2))  (tc)^2
                            where
                             'kc' is the buckling coefficient
                             'E' is the Young's modulus
                             'nu' is the elastic Poisson's ratio
                             't' is the panel thickness
                             'c' is the shorter panel dimension c = min(a,b)
                             'eta' is the plasticity reduction factor: SigmaAllowablePlastic = etaSigmaAllowableElastic
                             eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                             eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
                            SigmaAllowablePlasticF0.7 = f(SigmaAllowableElasticF0.7)
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
                        
         Returns A tuple consisting of (status, MS, sigmaAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Stress allowable .

        """
        pass
    def MsPlateBucklingCurvedLongitudinalShearCombined(abbContext: AbbContext, b: float, a: float, bc: ABB.EdgeSupportType, t: float, r: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
                            MS Plate Buckling Curved Longitudinal Shear Combined
                            Computes margin of safety of a rectangular curved metallic panel in buckling under combined shear and longitudinal loads
                            Under compressive loads
                            Under compressive and shear loads, the interaction equation is:
                            RL^2 + RS^2 = 1.0
                            The Margin Safety is given by the following formula:
                            MS=2(RL+sqrt(RL^2+4RS^2))-1
                            where:
                             RL = sigma  sigma_cr is the stress ratio due to longitudinal stress, with:
                             sigma is the given longitudinal stress
                             sigma_cr is the compression stress allowable for buckling (sigma_cr &lt; 0, as consequence RL &lt; 0 in tension)
                             RS = tau  tau_cr is the stress ratio due to shear stress with:
                             tau is the given shear stress
                             tau_cr is the shear stress allowable for buckling (tau and tau_cr always positive)
                            Under tensile loads
                            Under tensile and shear loads, the interaction equation is:
                            12  RL + RS = 1.0
                            The Margin Safety is given by the following formula:
                            MS = (2 - RL)  ( 2  RS ) - 1
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
                        
         Returns A tuple consisting of (status, MS, sigmacr, taucr). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmacr is: float. Compressive stress allowable .
         - taucr is: float. Shear stress allowable .

        """
        pass
    def MsPlateBucklingCurvedShear(abbContext: AbbContext, b: float, a: float, bc: ABB.EdgeSupportType, t: float, r: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, tau: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
                            MS Plate Buckling Curved Shear
                            Computes margin of safety of a curved metallic rectangular panel under shear load
                            The formula is MS = Allowable  |Stress| - 1
                            where:
                             'Allowable' is the compressive buckling stress allowable
                             'Stress' is the compressive stress (MS is not calculated in case of tensile stress),
                             'MS' is the margin of safety
                            Allowable = eta  PI^2ksE(12(1-nu^2))  (tc)^2
                            where
                             'ks' is the buckling coefficient
                             'E' is the Young's modulus
                             'nu' is the elastic Poisson's ratio
                             't' is the panel thickness
                             'c' is the shorter panel dimension c = min(a,b)
                             'eta' is the plasticity reduction factor: TauAllowablePlastic = etaTauAllowableElastic
                             eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                             eta is obtained from the MetallicPanelCompressivePlasticityCurveBC1 charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
                                 TauAllowablePlasticF0.7 = f(TauAllowableElasticF0.7)
                                 F0.7 is the stress for secant modulus equal to 70% of Young's modulus
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
                        
         Returns A tuple consisting of (status, MS, tauAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - tauAllowable is: float. Stress allowable .

        """
        pass
    def MsPlateBucklingFlatBending(abbContext: AbbContext, b: float, a: float, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, beta: float, sigma1: List[float], sigma2: List[float]) -> Tuple[ABB.Status, List[float], List[float]]:
        """
                            MS Plate Buckling Flat Bending
                            Computes margin of safety of a flat metallic rectangular panel under bending load
                            The formula is MS = sigmaAllowable  abs(sigma) - 1
                            where:
                             'sigmaAllowable' is the bending buckling stress allowable
                             'sigma' is the compressive stress at one edge of the panel, sigma = min( sigma1, sigma2 )
                             'MS' is the margin of safety
                            Allowable = eta  PI^2kbE(12(1-nu^2))  (tb)^2
                            where
                             'kb' is the bending buckling stress coefficient
                             'E' is the Young's modulus
                             'nu' is the elastic Poisson's ratio
                             't' is the panel thickness
                             'a' is the unloaded edge length
                             'b' is the loaded edge length
                             'beta' Loading length ratio,  the factor which, divided by b, gives the edge length in compression (while the remaining edge length is in tension).
                             'beta' is calculated on the basis of sigma1 and sigma2 with an hypothesis of linear behaviour with the formula:
                             beta = (fc - ft)  fc where fc = min(sigma1, sigma2) and ft = max(sigma1, sigma2) )
                             'eta' is the plasticity reduction factor: SigmaAllowablePlastic = etaSigmaAllowableElastic
                             eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                             eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
                            SigmaAllowablePlasticF0.7 = f(SigmaAllowableElasticF0.7)
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
                        
         Returns A tuple consisting of (status, MS, sigmaAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: List[float]. Stress allowables .

        """
        pass
    def MsPlateBucklingFlatCompressive(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
                            MS Plate Buckling Flat Compressive
                            Computes margin of safety of a flat metallic rectangular panel under compressive load
                            The formula is MS = sigmaAllowable  abs(sigma) - 1
                            where:
                             'sigmaAllowable' is the compressive buckling stress allowable,
                             'sigma' is the compressive stress (MS is not calculated in case of tensile stress),
                             'MS' is the margin of safety
                            Allowable = eta  PI^2kcE(12(1-nu^2))  (tb)^2
                            where
                             'kc' is the bending buckling stress coefficient
                             'E' is the Young's modulus
                             'nu' is the elastic Poisson's ratio
                             't' is the panel thickness
                             'a' is the unloaded edge length
                             'b' is the loaded edge length
                             'eta' is the plasticity reduction factor: SigmaAllowablePlastic = etaSigmaAllowableElastic
                             eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                             eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
                            SigmaAllowablePlasticF0.7 = f(SigmaAllowableElasticF0.7)
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
                        
         Returns A tuple consisting of (status, MS, sigmaAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmaAllowable is: float. Stress allowable .

        """
        pass
    def MsPlateBucklingFlatLongitudinalBendingCombined(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma1: List[float], sigma2: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
                            MS Plate Buckling Flat Longitudinal Bending Combined
                            Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and longitudinal loads
                            This formula is derived from the interaction equation
                            Rb ^ 1.75 + Rc = 1.0
                            where:
                             Rc = sigmac  sigmacr is the stress ratio due to compression stress, with:
                             sigmac is the given longitudinal stress
                             sigmacr  is the compression stress allowable for buckling
                             Rb = sigmab  sigmabcr is the stress ratio due to bending stress with
                             sigmab is the given compressive stress due to bending
                             sigmabcr  is the bending stress allowable for buckling
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
                        
         Returns A tuple consisting of (status, MS, sigmacr, sigmabcr). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmacr is: float. Compressive stress allowable .
         - sigmabcr is: float. Bending stress allowable .

        """
        pass
    def MsPlateBucklingFlatLongitudinalShearCombined(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], float, float]:
        """
                            MS Plate Buckling Flat Longitudinal Shear Combined
                            Computes margin of safety of a rectangular flat metallic panel in buckling under combined shear and longitudinal loads
                            Under longitudinal and shear loads, the interaction equation is:
                            MS=2(RL + sqrt(RL ^ 2 + 4  RS ^ 2)
                            This formula is derived from the interaction equation RL+R2S=1.0
                            RL + RS ^ 2 = 1.0
                            where:
                                 RL = sigma  sigmacr is the stress ratio due to longitudinal stress, with:
                                 sigma is the given longitudinal stress
                                 sigmacr is the compression stress allowable for buckling (sigmacr &lt; 0, as consequence RL &lt; 0 in tension)
                                 RS = tau  taucr is the stress ratio due to shear stress with
                                 tau is the given shear stress
                                 taucr is the shear stress allowable for buckling (taucr and tau always positive)
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
                        
         Returns A tuple consisting of (status, MS, sigmacr, taucr). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmacr is: float. Compressive stress allowable .
         - taucr is: float. Shear stress allowable .

        """
        pass
    def MsPlateBucklingFlatShear(abbContext: AbbContext, b: float, a: float, bc: ABB.EdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, tau: List[float]) -> Tuple[ABB.Status, List[float], float]:
        """
                            MS Plate Buckling Flat Shear
                            Computes margin of safety of a flat metallic rectangular panel under shear load
                            The formula is MS = tauAllowable  abs(tau) - 1
                            where:
                             'tauAllowable' is the shear buckling stress allowable,
                             'tau' is the compressive stress (MS is not calculated in case of tensile stress),
                             'MS' is the margin of safety
                            Allowable = eta  PI^2ksE(12(1-nu^2))  (tb)^2
                            where
                             'ks' is the bending buckling stress coefficient
                             'E' is the Young's modulus
                             'nu' is the elastic Poisson's ratio
                             't' is the panel thickness
                             'a' is the panel's longer edge length
                             'b' is panel's shorter edge length
                             'eta' is the plasticity reduction factor: SigmaAllowablePlastic = etaSigmaAllowableElastic
                             eta = 1 if material is considered as elastic (Material behaviour = Elastic)
                             eta is obtain from following charts if material is considered as elastic-plastic (Material behaviour = Elastic-Plastic):
                            TauAllowablePlasticF0.7 = f(TauAllowableElasticF0.7)
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
                        
         Returns A tuple consisting of (status, MS, tauAllowable). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - tauAllowable is: float. Stress allowable .

        """
        pass
    def MsPlateBucklingFlatShearBendingCombined(abbContext: AbbContext, b: float, bc_loaded: ABB.EdgeSupportType, a: float, bc_unloaded: ABB.UnloadedEdgeSupportType, t: float, behaviour: ABB.MaterialBehaviour, E: float, nu: float, n: float, iFy: float, sigma1: List[float], sigma2: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float], List[float], float]:
        """
                            MS Plate Buckling Flat Shear Bending Combined
                            Computes margin of safety of a rectangular flat metallic panel in buckling under combined bending and shear loads
                            Under longitudinal and shear loads, the interaction equation is:
                            MS = 1  sqrt(Rb ^ 2 + Rs ^ 2)
                            This formula is derived from the interaction equation
                            Rb ^ 2 + Rs ^ 2 = 1.0
                            where:
                                 Rb = sigmab  sigmabcr  is the stress ratio due to bendoing stress with
                                 sigmab is the given compressive stress due to bending
                                 sigmabcr is the bending stress allowable for buckling
                                 Rs = tau  taucr is the stress ratio due to shear stress with
                                 tau is the given shear stress
                                 taucr is the shear stress allowable for buckling (taucr and tau always positive)
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
                                taucr        Shear stress allowable that takes into account compressivetensile stress
                                sigmabcr     Bending stress allowable
                                MS           Margin of safety
                            Return
                                Status of the calculation
                        
         Returns A tuple consisting of (status, MS, sigmabcr, taucr). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .
         - sigmabcr is: List[float]. Bending stress allowable .
         - taucr is: float. Shear stress allowable .

        """
        pass
    def MsShearTearOut(abbContext: AbbContext, D: float, b: float, t: float, iFs: float, f: float, P: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS Shear Tear Out
                            Computes margin of shear tear out (due to bolt hole)
                            The formula is MS = PShearTearOutAllowable  P  - 1
                             'PShearTearOutAllowable' is the shear tear out load allowable. PShearTearOutAllowable = tauAllowable  2  t  ( b - D  2 )
                                 'tauAllowable' is the material shear stress allowable. For instance, it could be Fsu.
                                 'D' is the hole diameter
                                 't' is the thickness
                                 'b' is the distance from hole center to edge of the plate
                             'P' is the axial load. P = FactorLoad  PExtracted
                                 FactorLoad is the ratio of load between extracted load 'PExtracted' and 'P'
                                 PExtracted is the extracted load.
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsTrescaPlaneStress(abbContext: AbbContext, iSTresca: float, iFx: List[float], iFy: List[float], iFxy: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                            MS Tresca.
                            Computes margin of safety based on Tresca yield criterion under plane stress condition
                            The yield criteria of isotropic materials limit the elastic domain during loading.
                            According to the Tresca criterion, yield failure is expected when the greatest shear stress reaches the shear strength of the material.
                            Thus, the maximum shear stress yield criterion can be specified as
                            'max((|S1-S2|)2 , (|S1-S3|)2, (|S2-S3|)2) &lt;= (STresca)2'
                            where
                             'S1', 'S2' and 'S3' are the principal stresses.
                             'STresca' is the Tresca equivalent stress allowable  
                            A margin of safety can be derived from this formulation:
                            'MS = (STresca)  (max(|S1-S2| , |S1-S3|, |S2-S3|)) - 1'
                            that must be greater than 0.
                            In a plane stress configuration, principal stresses are computed as
                            'S1 = (FX + FY)2 + sqrt(((FX-FY)2)^2 + FXY^2)'
                            'S2 = (FX + FY)2 - sqrt(((FX-FY)2)^2 + FXY^2)'
                            where
                             'FX' the normal stress in the X direction
                             'FY' the normal stress in the Y direction
                             'FXY' the shearing stress
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of safety .

        """
        pass
    def MsTsaiHillPlaneStress(abbContext: AbbContext, iXt: float, iXc: float, iYt: float, iYc: float, S: float, sigma1: List[float], sigma2: List[float], tau: List[float]) -> Tuple[ABB.Status, List[float]]:
        """
                        MS Tsai-Hill
                        Computes margin of safety on the basis of Tsai-Hill failure theory (plane stress 
                        hypothesis)
                        For plane stress, this criterion can be written as:
                            sigma1^2X^2 - (sigma1  sigma2)X^2 + sigma2^2Y^2 + tau^2S^2  1
                        where:
                             sigma1, sigma2 and tau are the components of the symmetric plane stress tensor 
                              in the material direction,
                             X is the longitudinal tensile (Xt; if sigma1 is in tension, e.g., sigma1 
                              greater than 0) or compressive (Xc; if sigma1 is in compression, e.g., sigma1 
                              less than 0) stress,
                             Y is the transverse tensile (Yt; if sigma2 is in tension, e.g., sigma2 greater
                              than 0) or compressive (Yc; if sigma2 is in compression, e.g., sigma2 less
                              than 0) stress, and
                             S is the in-plane shear stress.
                        Note: This equation is specialized for plane stress with the longitudinal strength X 
                        in the 1-direction.
                         
                        The Margin of Safety, MS, is deduced from the criterion:
                            MS = 1  sqrt(sigma1^2X^2 - (sigma1  sigma2)X^2 + sigma2^2Y^2 + tau^2S^2) - 1
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
                        
         Returns A tuple consisting of (status, MS). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - MS is: List[float]. Margin of Safety .

        """
        pass
    def SecantModulus(abbContext: AbbContext, E: float, n: float, fy: float, sigma: float) -> Tuple[ABB.Status, float]:
        """
                            Secant modulus
                            Computes the secant modulus from material properties and stress.
                            The secant modulus ('Es') is defined as the stress('f') to strain ('epsilon') ratio at each value of stress.
                            The formula is 'Es = f  ( f  E + 0.002  ( f  fy ) ^ n )'
                            where:
                                 'f' is the stress
                                 'fy' is the yield stress
                                 'E' is the Young's modulus
                                 'n' is the Ramberg-Osgood parameter
                            The formula can be applied in compression and is 'Es = f  ( f  Ec + 0.002  ( f  Fcy ) ^ nc)'
                            where:
                                 'Fcy' is the compressive yield stress
                                 'Ec' is the compressive Young's modulus
                                 'nc' is the compressive Ramberg-Osgood parameter
                            Input
                                E       Young's modulus
                                n       Ramberg-Osgood parameter
                                fy      Yield stress
                                sigma   Stress
                            Output
                                Es      Secant modulus
                            Return
                                Status of the computation
                        
         Returns A tuple consisting of (status, iEs). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - iEs is: float. Secant modulus .

        """
        pass
    def StressF07(abbContext: AbbContext, iFy: float, E: float, n: float) -> Tuple[ABB.Status, float]:
        """
                            Stress F0.7
                            Computes the stress for secant modulus equal to 70% of Young's modulus.
                            The calculation is based upon the material properties. 'F0.7' is defined by:
                            'F0.7epsilon=0.7E', where 'epsilon' is the strain, and 'E' is the Young's modulus.
                            The formula can be applied for tensile and compressive stress, hence:
                            'F0.7 = ( (10.7 - 1)  0.002  Fty ^ n  E ) ^ ( 1  ( n - 1 ) )' for tension,
                            and 'F0.7c = ( ( 1  0.7 - 1 )  0.002  Fcy ^ nc  Ec ) ^ ( 1  ( nc - 1 ) )' for compression.
                            where:
                             'Fcy' is the compressive yield stress allowable
                             'Fty' the tensile yield stress allowable
                             'n' the Ramberg-Osgood parameter
                             'Ec' the compressive Young's modulus
                             'nc' the compressive Ramberg-Osgood parameter
                            Input
                                iFy Yield stress allowable
                                E Young's modulus
                                n Ramberg-Osgood parameter
                            Output
                                F07 Secant yield stress F0.7
                        
         Returns A tuple consisting of (status, F07). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - F07 is: float. Secant yield stress F0.7 .

        """
        pass
    def StressFromStrainInPlasticDomain(abbContext: AbbContext, strain: float, E: float, iF02ys: float, n: float) -> Tuple[ABB.Status, float]:
        """
                            Compute stress from strain with the help of Ramberg-Osgood relationship
                            The Ramberg-Osgood relationship allows to describe stress-strain curve with the help of a dedicated material parameter ('n').
                            'e = f  E + 0.002  ( f  f0.2ys ) ^ n'
                            where:
                             'e' is the total strain that takes into account elastic and plastic strains.
                             'f' is the stress
                             'E' is the material Young's modulus
                             'f0.2ys' is the material yield allowable (Fcy or Fty depending load type).
                             'n' is the Ramberg-Osgood parameter (in case of compressive load, it is common to call it 'nc').
                            The Ramberg-Osgood equation can not be inverted. As a consequence, stress is determined by numerical iterative calculation.
                            Input
                                strain  Total strain
                                E       Young's modulus
                                F02ys   Yield allowable (typically Fcy)
                                n       Ramberg-Osgood's parameter
                            Output
                                sigma Stress
                        
         Returns A tuple consisting of (status, sigma). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - sigma is: float. Stress .

        """
        pass
    def TangentModulus(abbContext: AbbContext, E: float, n: float, iFy: float, sigma: float) -> Tuple[ABB.Status, float]:
        """
                            Computes the tangent modulus from material properties and stress.
                            The tangent modulus ('Et') is defined as the slope of the stress('f')-strain('epsilon') curve at each value of stress.
                            The formula is 'Et = f  ( f  E + 0.002  n  ( f  FY ) ^ n )'
                            where:
                             'f' is the stress
                             'FY' is the yield stress
                             'E' is the Young's modulus
                             'n' is the Ramberg-Osgood parameter
                            The formula can be applied in compression and is 'Et=f(fEc+0.002nc(f(Fcy))^(nc))'
                            where:
                             'Fcy' is the compressive yield stress
                             'Ec' is the compressive Young's modulus
                             'nc' is the compressive Ramberg-Osgood parameter
                            Input
                                E Young's modulus
                                n Ramberg-Osgood parameter
                                iFy Yield stress Allowable
                                sigma Stress
                            Output
                                Et Tangent modulus
                        
         Returns A tuple consisting of (status, oEt). 
         - status is:  ABB.Status NXOpen.CAE.Aero.
         - oEt is: float. Tangent modulus .

        """
        pass
import NXOpen
import NXOpen.CAE.AeroStructures
class CalculationContext(NXOpen.NXObject): 
    """  Calculation context is passed to the method implementation. 
                  It contains methods to retrieve the load case set and input parameter values,
                  method to set the output values and log messages   """
    class UnitSystem(Enum):
        """
        Members Include: 
         |Metric|  Metric Unit System 
         |English|  SI Unit System 
         |Si|  English Unit System 
         |Unknown|  Unknown Unit System 

        """
        Metric: int
        English: int
        Si: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> CalculationContext.UnitSystem:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def NumLoadCases(self) -> int:
        """
        Getter for property: (int) NumLoadCases
         Returns the number of load cases for the calculation  
            
         
        """
        pass
    def AddGeneralScalarTable(self, nRows: int, nCols: int, measure_name: str) -> NXOpen.GeneralScalarTable:
        """
         Add a general scalar table to the context: 
                 - The unit system of the calculation context is used for the values 
                 - The table will exist for the duration of the context
                
         Returns scalarTable ( NXOpen.GeneralScalarTable): .
        """
        pass
    @overload
    def Error(self, message: str) -> None:
        """
         Log an error message
        """
        pass
    @overload
    def Error(self, failureMode: str, lcIndex: int, message: str) -> None:
        """
         Log an error message indexed by possibly empty failure mode and load case
        """
        pass
    @overload
    def Error(self, failureMode: str, loadCase: str, message: str) -> None:
        """
         Log an error message indexed by possibly empty failure mode and load case
        """
        pass
    def GetAbbContext(self) -> AbbContext:
        """
         Returns the ABB context object
         Returns abbContext ( AbbContext NXOpen.CAE.Aero): .
        """
        pass
    def GetInput(self, inputName: str) -> InputParameter:
        """
         Get an input parameter 
         Returns param ( InputParameter NXOpen.CAE.Aero):  .
        """
        pass
    def GetLoadCaseArray(self) -> List[NXOpen.CAE.AeroStructures.LoadCase]:
        """
         Get the load case array used by the calculation
         Returns lcarray ( NXOpen.CAE.AeroStructures.LoadCase Li):  .
        """
        pass
    def GetOutput(self, outputName: str) -> OutputParameter:
        """
         Get an output parameter 
         Returns param ( OutputParameter NXOpen.CAE.Aero):  .
        """
        pass
    def GetOutputMs(self) -> OutputScalar:
        """
         Get MS output parameter 
         Returns param ( OutputScalar NXOpen.CAE.Aero):  .
        """
        pass
    def GetTempPath(self) -> str:
        """
         Creates and return a path to an empty temporary directory 
         Returns path (str):  .
        """
        pass
    def GetUnit(self, unitName: str) -> NXOpen.Unit:
        """
         Get unit from its name 
         Returns unit_type ( NXOpen.Unit): .
        """
        pass
    def GetUnitForMeasure(self, measure_name: str) -> NXOpen.Unit:
        """
         Returns the unit type object for a given measure in the method unit system. The unit system
                    can be defined by an author in the definition of the method or by the user in the margin solution 
                    editor. If there is no method or solution unit system the method uses the current base unit system.
                
         Returns unit_type ( NXOpen.Unit):  unit type of the measure .
        """
        pass
    def GetUnitType(self, measure_name: str, unit_symbol: str) -> NXOpen.Unit:
        """
         Returns the unit type object for a given measure and unit name  
         Returns unit_type ( NXOpen.Unit):  unit type of the measure .
        """
        pass
    @overload
    def Log(self, message: str) -> None:
        """
         Log an info message
        """
        pass
    @overload
    def Log(self, failureMode: str, lcIndex: int, message: str) -> None:
        """
         Log an info message indexed by possibly empty failure mode and load case
        """
        pass
    @overload
    def Log(self, failureMode: str, loadCase: str, message: str) -> None:
        """
         Log an info message indexed by possibly empty failure mode and load case
        """
        pass
    def SetEnvelopeResults(self, xValues: List[float], yValues: List[float]) -> None:
        """
         Set Envelope Results 
        """
        pass
    def SetLoadResults(self, lcIndex: int, xValues: List[float], yValues: List[float], centralities: List[float], selected: List[bool]) -> None:
        """
         Set Load Results 
        """
        pass
    def SetResultUnits(self, x_unit_type: NXOpen.Unit, y_unit_type: NXOpen.Unit) -> None:
        """
         Set Result Units  
        """
        pass
    def SetSelectedLoadCase(self, lcIndex: int, selected: bool) -> None:
        """
         Set Selected LC 
        """
        pass
    def SetSelectedLoadCases(self, lcIndexes: List[int]) -> None:
        """
         Set Selected LCs by array 
        """
        pass
    def SetToleranceResults(self, xValues: List[float], yValues: List[float]) -> None:
        """
         Set Tolerance Results 
        """
        pass
    def SetToleranceValue(self, tolerance: float) -> None:
        """
         Set Tolerance Value 
        """
        pass
    @overload
    def Warn(self, message: str) -> None:
        """
         Log a warning message
        """
        pass
    @overload
    def Warn(self, failureMode: str, lcIndex: int, message: str) -> None:
        """
         Log a warning message indexed by possibly empty failure mode and load case
        """
        pass
    @overload
    def Warn(self, failureMode: str, loadCase: str, message: str) -> None:
        """
         Log a warning message indexed by possibly empty failure mode and load case
        """
        pass
class InputBoolean(InputParameter): 
    """  Represents a boolean input parameter  """
    @property
    def Value(self) -> bool:
        """
        Getter for property: (bool) Value
         Returns the value.  
             
         
        """
        pass
class InputFile(InputParameter): 
    """  Represents a File input parameter  """
    def GetPath(self) -> str:
        """
         Retrieve the absolutr path of the file 
         Returns pathVal (str):  the directory used.
        """
        pass
class InputInteger(InputParameter): 
    """  Represents an integer input parameter  """
    @property
    def Value(self) -> int:
        """
        Getter for property: (int) Value
         Returns the value.  
             
         
        """
        pass
import NXOpen.CAE.AeroStructures
class InputLaminate(InputParameter): 
    """  represent a laminate input parameter  """
    @property
    def RawValue(self) -> NXOpen.CAE.AeroStructures.Laminate:
        """
        Getter for property: ( NXOpen.CAE.AeroStructures.Laminate) RawValue
         Returns the laminate without considering extraction transformations   
            
         
        """
        pass
    @property
    def Value(self) -> NXOpen.CAE.AeroStructures.Laminate:
        """
        Getter for property: ( NXOpen.CAE.AeroStructures.Laminate) Value
         Returns the laminate taking into account extraction transformations   
            
         
        """
        pass
    def HasValue(self) -> bool:
        """
         The laminate is well set up.
         Returns hasValue (bool): .
        """
        pass
import NXOpen
import NXOpen.CAE
class InputLoad(InputParameter): 
    """  represent a load input parameter  """
    class LoadSupportType(Enum):
        """
        Members Include: 
         |NotSet|  Not available (the aggregation has been done at the calculation level, ValuesGetValues() will return a vector of aggregated values) 
         |Node|  Node (the method has aggregated values that have been extracted per node, ValuesGetValues() will return a table of values) 
         |Element|  Element (the method has aggregated values that have been extracted per element, ValuesGetValues() will return a table of values) 

        """
        NotSet: int
        Node: int
        Element: int
        @staticmethod
        def ValueOf(value: int) -> InputLoad.LoadSupportType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def SupportType(self) -> InputLoad.LoadSupportType:
        """
        Getter for property: ( InputLoad.LoadSupportType NXOpen.CAE.Aero) SupportType
         Returns the support type   
            
         
        """
        pass
    @property
    def Unit(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) Unit
         Returns the unit type.  
             
         
        """
        pass
    @property
    def Values(self) -> NXOpen.GeneralScalarTable:
        """
        Getter for property: ( NXOpen.GeneralScalarTable) Values
         Returns the values   
            
         
        """
        pass
    def GetElements(self) -> List[NXOpen.CAE.FEElement]:
        """
         Get support elements 
         Returns elementArray ( NXOpen.CAE.FEElement Li):  the list of support elements, if available .
        """
        pass
    def GetNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Get support nodes 
         Returns nodeArray ( NXOpen.CAE.FENode Li):  the list of support nodes, if available .
        """
        pass
    @overload
    def GetValues(self, unit_type: NXOpen.Unit) -> NXOpen.GeneralScalarTable:
        """
         Get value using a specific unit type. 
         Returns matrix ( NXOpen.GeneralScalarTable):  either a one- or two-dimensional array of doubles .
        """
        pass
import NXOpen
import NXOpen.CAE.AeroStructures
class InputParameter(NXOpen.NXObject): 
    """  parent class of all typed input parameter classes  """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def Type(self) -> NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType:
        """
        Getter for property: ( NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType) Type
         Returns the parameter type.  
             
         
        """
        pass
import NXOpen
class InputScalar(InputParameter): 
    """  Represents a scalar input parameter  """
    @property
    def Unit(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) Unit
         Returns the unit type.  
             
         
        """
        pass
    @property
    def Value(self) -> float:
        """
        Getter for property: (float) Value
         Returns the value in default unit.  
            
         
        """
        pass
    def GetValueIn(self, unit_type: NXOpen.Unit) -> float:
        """
         Get the value in a specific unit. 
         Returns doubleVal (float):  the double value of the parameter expressed in the specified unit.
        """
        pass
import NXOpen.CAE.AeroStructures
class InputTable(InputParameter): 
    """  Represents an Table input parameter  """
    @property
    def Value(self) -> NXOpen.CAE.AeroStructures.TableParameter:
        """
        Getter for property: ( NXOpen.CAE.AeroStructures.TableParameter) Value
         Returns the value.  
             
         
        """
        pass
class InputText(InputParameter): 
    """  Represents a text input parameter  """
    @property
    def Value(self) -> str:
        """
        Getter for property: (str) Value
         Returns the value.  
             
         
        """
        pass
import NXOpen
class MethodLibrary(NXOpen.Object): 
    """ Represents a NXOpen.CAE.AeroStructures.Author.MethodLibrary object. """
    Callback = Callable[[CalculationContext], None]
    CallbackMulti = Callable[[MultiCalculationContext], None]
    CallbackPost = Callable[[NXOpen.CAE.AeroStructures.MarginCalculation], None]
    def RegisterEvaluate(methodID: str, version: int, cb: MethodLibrary.Callback) -> None:
        """
         Routine to register an evaluate callback 
        """
        pass
    def RegisterEvaluateScript(methodID: str, version: int) -> None:
        """
         Routine to register an evaluate script (internal use only)
        """
        pass
    def RegisterMultiEvaluate(methodID: str, version: int, cb: MethodLibrary.CallbackMulti) -> None:
        """
         Routine to register a multi evaluate callback 
        """
        pass
    def RegisterMultiEvaluateScript(methodID: str, version: int) -> None:
        """
         Routine to register a multi evaluate script (internal use only)
        """
        pass
    def RegisterPostProcessing(methodID: str, version: int, cb: MethodLibrary.CallbackPost) -> None:
        """
         Routine to register a Post Processing callback 
        """
        pass
    def RegisterPostProcessingScript(methodID: str, version: int) -> None:
        """
         Routine to register a post processing script (internal use only) 
        """
        pass
    def RegisterValidate(methodID: str, version: int, cb: MethodLibrary.Callback) -> None:
        """
         Routine to register a validate callback 
        """
        pass
    def RegisterValidateScript(methodID: str, version: int) -> None:
        """
         Routine to register a validate script (internal use only) 
        """
        pass
import NXOpen
class MultiCalculationContext(NXOpen.NXObject): 
    """  Multi Calculation context is passed to the multi evaluate method implementation. 
                  It contains methods to retrieve the load case set and input parameter values,
                  and to set the output values and log messages   """
    def GetContextArray(self) -> List[CalculationContext]:
        """
         Get calculation context array
         Returns ccArray ( CalculationContext List[NXOpen.CAE.Ae):  .
        """
        pass
    def SetSuccess(self, idx: int, success: bool) -> None:
        """
         Reports the success or failure of the evaluation of a calculation context 
        """
        pass
class OutputBoolean(OutputParameter): 
    """  Represents a boolean output parameter  """
    @overload
    def SetValue(self, boolVal: bool) -> None:
        """
         Set boolean value. 
        """
        pass
    @overload
    def SetValue(self, fmName: str, boolVal: bool) -> None:
        """
         Set boolean value for a failure mode 
        """
        pass
    @overload
    def SetValue(self, fmName: str, lcIndex: int, boolVal: bool) -> None:
        """
         Set boolean value for a failure mode and a loadcase specified by its index
        """
        pass
class OutputFile(OutputParameter): 
    """  Represents a File Output parameter  """
    def GetCalculationDirectory(self) -> str:
        """
         Retrieve the absolute path of the directory used to write output files 
         Returns pathVal (str):  the directory used.
        """
        pass
    def GetPath(self) -> str:
        """
         Retrieve the absolute path of the file 
         Returns pathVal (str):  the directory used.
        """
        pass
    def SetPath(self, pathVal: str) -> None:
        """
         Set the path of the output file being added to the output directory 
        """
        pass
class OutputInteger(OutputParameter): 
    """  Represents an integer output parameter  """
    @overload
    def SetValue(self, intVal: int) -> None:
        """
         Set integer value. 
        """
        pass
    @overload
    def SetValue(self, fmName: str, intVal: int) -> None:
        """
         Set integer value for a failure mode 
        """
        pass
    @overload
    def SetValue(self, fmName: str, lcIndex: int, intVal: int) -> None:
        """
         Set integer value for a failure mode and a loadcase specified by its index
        """
        pass
import NXOpen
import NXOpen.CAE.AeroStructures
class OutputParameter(NXOpen.NXObject): 
    """  Parent class of all the typed output parameter classes   """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def Type(self) -> NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType:
        """
        Getter for property: ( NXOpen.CAE.AeroStructures.ParameterDescriptor.ParameterType) Type
         Returns the parameter type.  
             
         
        """
        pass
import NXOpen
class OutputScalar(OutputParameter): 
    """  Represents a scalar output parameter  """
    @property
    def Unit(self) -> NXOpen.Unit:
        """
        Getter for property: ( NXOpen.Unit) Unit
         Returns the unit type.  
             
         
        """
        pass
    @overload
    def SetValue(self, doubleVal: float) -> None:
        """
         Set scalar value according to default unit 
        """
        pass
    @overload
    def SetValue(self, doubleVal: float, unit_type: NXOpen.Unit) -> None:
        """
         Set scalar value with a specific unit type. 
        """
        pass
    @overload
    def SetValue(self, fmName: str, doubleVal: float) -> None:
        """
         Set scalar value according to default unit for a failure mode 
        """
        pass
    @overload
    def SetValue(self, fmName: str, lcIndex: int, doubleVal: float) -> None:
        """
         Set scalar value according to default unit for a failure mode and a loadcase specified by its index
        """
        pass
    @overload
    def SetValue(self, fmName: str, doubleVal: float, unit_type: NXOpen.Unit) -> None:
        """
         Set scalar value with a specific unit type for a failure mode 
        """
        pass
    @overload
    def SetValue(self, fmName: str, lcIndex: int, doubleVal: float, unit_type: NXOpen.Unit) -> None:
        """
         Set scalar valuewith a specific unit type  for a failure mode and a loadcase specified by its index
        """
        pass
class OutputText(OutputParameter): 
    """  Represents a text output parameter  """
    @overload
    def SetValue(self, textVal: str) -> None:
        """
         Set text value. 
        """
        pass
    @overload
    def SetValue(self, fmName: str, textVal: str) -> None:
        """
         Set text value for a failure mode 
        """
        pass
    @overload
    def SetValue(self, fmName: str, lcIndex: int, textVal: str) -> None:
        """
         Set text value for a failure mode and a loadcase specified by its index
        """
        pass
