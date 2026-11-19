from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Acceleration(NXOpen.NXObject): 
    """ Represents an Acceleration type load in the NXOpen.DesignSimulation.Study context. """
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Direction
         Returns the direction   
            
         
        """
        pass
    @property
    def Magnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Magnitude
         Returns the magnitude   
            
         
        """
        pass
import NXOpen
class AnalysisBodyResults(NXOpen.NXObject): 
    """ Represents analysis results for an NXOpen.DesignSimulation.AnalysisBody. """
    class Facet:
        """
         Represents a triangular facet with ordered indices of its vertices. 
         AnalysisBodyResultsFacet_Struct NXOpen.Desi is an alias for  AnalysisBodyResults.Facet NXOpen.Desi.
        """
        @property
        def V1(self) -> int:
            """
            Getter for property V1
            vertex 1

            """
            pass
        @V1.setter
        def V1(self, value: int):
            """
            Getter for property V1
            vertex 1
            Setter for property V1
            vertex 1

            """
            pass
        @property
        def V2(self) -> int:
            """
            Getter for property V2
            vertex 2

            """
            pass
        @V2.setter
        def V2(self, value: int):
            """
            Getter for property V2
            vertex 2
            Setter for property V2
            vertex 2

            """
            pass
        @property
        def V3(self) -> int:
            """
            Getter for property V3
            vertex 3

            """
            pass
        @V3.setter
        def V3(self, value: int):
            """
            Getter for property V3
            vertex 3
            Setter for property V3
            vertex 3

            """
            pass
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis body result.  
             
         
        """
        pass
    @property
    def NumberOfContourFacets(self) -> int:
        """
        Getter for property: (int) NumberOfContourFacets
         Returns the number of facets in the analysis results contour   
            
         
        """
        pass
    @property
    def NumberOfContourVertices(self) -> int:
        """
        Getter for property: (int) NumberOfContourVertices
         Returns the number of vertices in the analysis results contour   
            
         
        """
        pass
    def Blank(self) -> None:
        """
         Blanks the analysis body result. 
        """
        pass
    def GetContourFacetAt(self, index: int) -> AnalysisBodyResults.Facet:
        """
         Get facet at given index. The index must be between 0 and NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourFacets. 
         Returns facet ( AnalysisBodyResults.Facet NXOpen.Desi): .
        """
        pass
    def GetContourFacets(self) -> List[AnalysisBodyResults.Facet]:
        """
         Gets all the facets (triangular) in the analysis results contour. Count should match NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourFacets. 
         Returns facets ( AnalysisBodyResults.Facet List[NXOpen.De): .
        """
        pass
    def GetContourVertexAt(self, index: int) -> NXOpen.Point3d:
        """
         Get vertex coordinates at given index. The index must be between 0 and NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourVertices. 
         Returns vertex ( NXOpen.Point3d): .
        """
        pass
    def GetContourVertices(self) -> List[NXOpen.Point3d]:
        """
         Gets all the vertices in the analysis results contour. Count should match NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourVertices. 
         Returns vertices ( NXOpen.Point3d Li): .
        """
        pass
    def GetSubcaseResults(self) -> List[AnalysisBodySubcaseResults]:
        """
         Returns the analysis result data per NXOpen.DesignSimulation.Subcase in the owning NXOpen.DesignSimulation.Study.
                    NXOpen.DesignSimulation.AnalysisBodySubcaseResults will have results for NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourVertices vertices. 
         Returns subcaseResults ( AnalysisBodySubcaseResults List[NXOpen.De): .
        """
        pass
    def Unblank(self) -> None:
        """
         Unblanks the analysis body result. 
        """
        pass
import NXOpen
class AnalysisBodySubcaseResults(NXOpen.NXObject): 
    """ Represents analysis results for an NXOpen.DesignSimulation.AnalysisBody per NXOpen.DesignSimulation.Subcase in the NXOpen.DesignSimulation.Study context. """
    class ResultType(Enum):
        """
        Members Include: 
         |Displacement|  Nodal displacement vector 
         |StressVonMises|  Nodal stress scalar 
         |StressWorstPrincipal|  Nodal stress scalar 

        """
        Displacement: int
        StressVonMises: int
        StressWorstPrincipal: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisBodySubcaseResults.ResultType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetAllScalarResults(self, resultType: AnalysisBodySubcaseResults.ResultType) -> List[float]:
        """
         Get all scalar result values of given type. Count should match NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourVertices. 
                    Stress results are returned as a scalar value. 
         Returns values (List[float]): .
        """
        pass
    def GetAllVectorResults(self, resultType: AnalysisBodySubcaseResults.ResultType) -> List[NXOpen.Vector3d]:
        """
         Get all vector results of given type. Count should match NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourVertices. 
                    Displacement results are returned as a vector with X, Y and Z components. 
         Returns values ( NXOpen.Vector3d Li): .
        """
        pass
    def GetMaxMagnitudeAndLocation(self, resultType: AnalysisBodySubcaseResults.ResultType) -> Tuple[NXOpen.Vector3d, float]:
        """
         Get maximum magnitude of given type of analysis result and the position of the maxima. 
         Returns A tuple consisting of (maxMagnitudePosition, maxMagnitude). 
         - maxMagnitudePosition is:  NXOpen.Vector3d.
         - maxMagnitude is: float.

        """
        pass
    def GetScalarResultAt(self, resultType: AnalysisBodySubcaseResults.ResultType, index: int) -> float:
        """
         Get scalar result value of given type at given index. The index must be between 0 and NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourVertices. 
                    Stress results are returned as a scalar value. 
         Returns value (float): .
        """
        pass
    def GetVectorResultAt(self, resultType: AnalysisBodySubcaseResults.ResultType, index: int) -> NXOpen.Vector3d:
        """
         Get vector result of given type at given index. The index must be between 0 and NXOpen.DesignSimulation.AnalysisBodyResults.NumberOfContourVertices. 
                    Displacement results are returned as a vector with X, Y and Z components. 
         Returns value ( NXOpen.Vector3d): .
        """
        pass
    def HasResults(self, resultType: AnalysisBodySubcaseResults.ResultType) -> bool:
        """
         Checks availability of analysis results by result type. 
         Returns hasResults (bool): .
        """
        pass
import NXOpen
class AnalysisBody(NXOpen.NXObject): 
    """ Represents an Analysis Body in the NXOpen.DesignSimulation.Study context. """
    @property
    def Body(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) Body
         Returns the referenced body   
            
         
        """
        pass
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis body.  
             
         
        """
        pass
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: ( NXOpen.Material) Material
         Returns the physical material (if any) to be used for analysis   
            
         
        """
        pass
    @property
    def ReferencedBodyName(self) -> str:
        """
        Getter for property: (str) ReferencedBodyName
         Returns the name of the referenced body   
            
         
        """
        pass
    @property
    def Results(self) -> AnalysisBodyResults:
        """
        Getter for property: ( AnalysisBodyResults NXOpen.Desi) Results
         Returns the analysis results data from the last simulation run, if any, for the owning  NXOpen::DesignSimulation::Study    
            
         
        """
        pass
    def Blank(self) -> None:
        """
         Blanks the analysis body. 
        """
        pass
    def GetMass(self) -> Tuple[float, NXOpen.Unit]:
        """
         Get the mass of the analysis body in part base units 
         Returns A tuple consisting of (massValue, massUnit). 
         - massValue is: float.
         - massUnit is:  NXOpen.Unit.

        """
        pass
    def Unblank(self) -> None:
        """
         Unblanks the analysis body. 
        """
        pass
import NXOpen
class AnalysisConstraintBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.DesignSimulation.AnalysisConstraint builder
    """
    class ConstraintType(Enum):
        """
        Members Include: 
         |Fixed| 
         |Pinned| 
         |PinnedSlider| 
         |LinearSlider| 
         |PlanarSlider| 
         |Temperature| 

        """
        Fixed: int
        Pinned: int
        PinnedSlider: int
        LinearSlider: int
        PlanarSlider: int
        Temperature: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisConstraintBuilder.ConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LinearSliderVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) LinearSliderVector
         Returns the linear slider vector   
            
         
        """
        pass
    @LinearSliderVector.setter
    def LinearSliderVector(self, linearSliderVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) LinearSliderVector
         Returns the linear slider vector   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the fe constraint name   
            
         
        """
        pass
    @Name.setter
    def Name(self, feConstraintName: str):
        """
        Setter for property: (str) Name
         Returns the fe constraint name   
            
         
        """
        pass
    @property
    def PlanarSliderPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) PlanarSliderPlane
         Returns the planar slider plane   
            
         
        """
        pass
    @PlanarSliderPlane.setter
    def PlanarSliderPlane(self, planarSliderPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) PlanarSliderPlane
         Returns the planar slider plane   
            
         
        """
        pass
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFace
         Returns the fe selected face   
            
         
        """
        pass
    @property
    def Temperature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Temperature
         Returns the temperature expression   
            
         
        """
        pass
    @property
    def ThickenOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThickenOffset
         Returns the thicken offset   
            
         
        """
        pass
    @property
    def Type(self) -> AnalysisConstraintBuilder.ConstraintType:
        """
        Getter for property: ( AnalysisConstraintBuilder.ConstraintType NXOpen.Desi) Type
         Returns the constraint type enum   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: AnalysisConstraintBuilder.ConstraintType):
        """
        Setter for property: ( AnalysisConstraintBuilder.ConstraintType NXOpen.Desi) Type
         Returns the constraint type enum   
            
         
        """
        pass
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    def UpdateDisplay(self) -> None:
        """
         Update constraint display symbol 
        """
        pass
import NXOpen
class AnalysisConstraint(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Analysis Constraint """
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis constraint.  
             
         
        """
        pass
    @property
    def LinearSliderVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) LinearSliderVector
         Returns the slider vector for LinearSlider type   
            
         
        """
        pass
    @property
    def PlanarSliderPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) PlanarSliderPlane
         Returns the planar slider plane for PlanarSlider type   
            
         
        """
        pass
    @property
    def Temperature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Temperature
         Returns the temperature expression   
            
         
        """
        pass
    @property
    def ThickenOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThickenOffset
         Returns the thicken offset   
            
         
        """
        pass
    @property
    def Type(self) -> AnalysisConstraintBuilder.ConstraintType:
        """
        Getter for property: ( AnalysisConstraintBuilder.ConstraintType NXOpen.Desi) Type
         Returns the constraint type   
            
         
        """
        pass
    def Blank(self) -> None:
        """
         Blanks the analysis constraint. 
        """
        pass
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         Gets the faces which the constraint is applied on. 
         Returns faces ( NXOpen.Face Li): .
        """
        pass
    def Unblank(self) -> None:
        """
         Unblanks the analysis constraint. 
        """
        pass
import NXOpen
class AnalysisLoadBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.DesignSimulation.AnalysisLoad builder """
    class AnalysisLoadForceType(Enum):
        """
        Members Include: 
         |ByVector| 
         |ByComponent| 

        """
        ByVector: int
        ByComponent: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.AnalysisLoadForceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AnalysisLoadType(Enum):
        """
        Members Include: 
         |Force| 
         |BearingLoad| 
         |Pressure| 
         |Torque| 
         |Acceleration| 
         |EnforcedDisplacement| 
         |RemoteForce| 
         |HeatFlux| 

        """
        Force: int
        BearingLoad: int
        Pressure: int
        Torque: int
        Acceleration: int
        EnforcedDisplacement: int
        RemoteForce: int
        HeatFlux: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.AnalysisLoadType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ForceDistributionType(Enum):
        """
        Members Include: 
         |EvenOverFaceArea| 
         |EvenOverFaceNumber| 
         |ConstantPerFace| 

        """
        EvenOverFaceArea: int
        EvenOverFaceNumber: int
        ConstantPerFace: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.ForceDistributionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ForceObjectType(Enum):
        """
        Members Include: 
         |Face| 
         |Point| 

        """
        Face: int
        Point: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.ForceObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RemoteForceType(Enum):
        """
        Members Include: 
         |Force| 
         |Moment| 
         |ForceAndMoment| 

        """
        Force: int
        Moment: int
        ForceAndMoment: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisLoadBuilder.RemoteForceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Acceleration(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Acceleration
         Returns the acceleration expression   
            
         
        """
        pass
    @property
    def AnalysisRemoteForceType(self) -> AnalysisLoadBuilder.AnalysisLoadForceType:
        """
        Getter for property: ( AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.Desi) AnalysisRemoteForceType
         Returns the analysis remote force type   
            
         
        """
        pass
    @AnalysisRemoteForceType.setter
    def AnalysisRemoteForceType(self, typeOfForce: AnalysisLoadBuilder.AnalysisLoadForceType):
        """
        Setter for property: ( AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.Desi) AnalysisRemoteForceType
         Returns the analysis remote force type   
            
         
        """
        pass
    @property
    def BearingAngular(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BearingAngular
         Returns the bearing angular expression   
            
         
        """
        pass
    @property
    def ComponentCSYS(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) ComponentCSYS
         Returns the component CSYS   
            
         
        """
        pass
    @ComponentCSYS.setter
    def ComponentCSYS(self, componentCSYS: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) ComponentCSYS
         Returns the component CSYS   
            
         
        """
        pass
    @property
    def FaceVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) FaceVector
         Returns the face vector   
            
         
        """
        pass
    @FaceVector.setter
    def FaceVector(self, faceVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) FaceVector
         Returns the face vector   
            
         
        """
        pass
    @property
    def Force(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Force
         Returns the force expression   
            
         
        """
        pass
    @property
    def ForceDistributionMethod(self) -> AnalysisLoadBuilder.ForceDistributionType:
        """
        Getter for property: ( AnalysisLoadBuilder.ForceDistributionType NXOpen.Desi) ForceDistributionMethod
         Returns the distribution method   
            
         
        """
        pass
    @ForceDistributionMethod.setter
    def ForceDistributionMethod(self, distributionMethod: AnalysisLoadBuilder.ForceDistributionType):
        """
        Setter for property: ( AnalysisLoadBuilder.ForceDistributionType NXOpen.Desi) ForceDistributionMethod
         Returns the distribution method   
            
         
        """
        pass
    @property
    def ForceLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ForceLocation
         Returns the point selection   
            
         
        """
        pass
    @ForceLocation.setter
    def ForceLocation(self, forcePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ForceLocation
         Returns the point selection   
            
         
        """
        pass
    @property
    def ForceObjectOption(self) -> AnalysisLoadBuilder.ForceObjectType:
        """
        Getter for property: ( AnalysisLoadBuilder.ForceObjectType NXOpen.Desi) ForceObjectOption
         Returns the face point type   
            
         
        """
        pass
    @ForceObjectOption.setter
    def ForceObjectOption(self, forceObjectOption: AnalysisLoadBuilder.ForceObjectType):
        """
        Setter for property: ( AnalysisLoadBuilder.ForceObjectType NXOpen.Desi) ForceObjectOption
         Returns the face point type   
            
         
        """
        pass
    @property
    def ForceType(self) -> AnalysisLoadBuilder.AnalysisLoadForceType:
        """
        Getter for property: ( AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.Desi) ForceType
         Returns the force type   
            
         
        """
        pass
    @ForceType.setter
    def ForceType(self, typeOfForce: AnalysisLoadBuilder.AnalysisLoadForceType):
        """
        Setter for property: ( AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.Desi) ForceType
         Returns the force type   
            
         
        """
        pass
    @property
    def ForceX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForceX
         Returns the force x expression   
            
         
        """
        pass
    @property
    def ForceY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForceY
         Returns the force y expression   
            
         
        """
        pass
    @property
    def ForceZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForceZ
         Returns the force z expression   
            
         
        """
        pass
    @property
    def HeatFlux(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeatFlux
         Returns the thermal load expression   
            
         
        """
        pass
    @property
    def MaxDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDisplacement
         Returns the maximum displacement expression   
            
         
        """
        pass
    @property
    def Moment(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Moment
         Returns the moment expression   
            
         
        """
        pass
    @property
    def MomentX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentX
         Returns the moment x expression   
            
         
        """
        pass
    @property
    def MomentY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentY
         Returns the moment y expression   
            
         
        """
        pass
    @property
    def MomentZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentZ
         Returns the moment z expression   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the Analysis Load name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the Analysis Load name   
            
         
        """
        pass
    @property
    def Pressure(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Pressure
         Returns the pressure expression   
            
         
        """
        pass
    @property
    def RemoteForceOption(self) -> AnalysisLoadBuilder.RemoteForceType:
        """
        Getter for property: ( AnalysisLoadBuilder.RemoteForceType NXOpen.Desi) RemoteForceOption
         Returns the remote load type   
            
         
        """
        pass
    @RemoteForceOption.setter
    def RemoteForceOption(self, remoteForceOption: AnalysisLoadBuilder.RemoteForceType):
        """
        Setter for property: ( AnalysisLoadBuilder.RemoteForceType NXOpen.Desi) RemoteForceOption
         Returns the remote load type   
            
         
        """
        pass
    @property
    def RemoteForcePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) RemoteForcePoint
         Returns the remote point selection   
            
         
        """
        pass
    @RemoteForcePoint.setter
    def RemoteForcePoint(self, remotePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) RemoteForcePoint
         Returns the remote point selection   
            
         
        """
        pass
    @property
    def RemoteMomentVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) RemoteMomentVector
         Returns the remote moment vector   
            
         
        """
        pass
    @RemoteMomentVector.setter
    def RemoteMomentVector(self, remoteMomentVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) RemoteMomentVector
         Returns the remote moment vector   
            
         
        """
        pass
    @property
    def ReverseBearingLoadDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseBearingLoadDirection
         Returns the flag indicating bearing load force direction is reversed or not   
            
         
        """
        pass
    @ReverseBearingLoadDirection.setter
    def ReverseBearingLoadDirection(self, reverseForceDirection: bool):
        """
        Setter for property: (bool) ReverseBearingLoadDirection
         Returns the flag indicating bearing load force direction is reversed or not   
            
         
        """
        pass
    @property
    def ReversePressureDirection(self) -> bool:
        """
        Getter for property: (bool) ReversePressureDirection
         Returns the flag indicating pressure direction is reversed or not   
            
         
        """
        pass
    @ReversePressureDirection.setter
    def ReversePressureDirection(self, reverseFlag: bool):
        """
        Setter for property: (bool) ReversePressureDirection
         Returns the flag indicating pressure direction is reversed or not   
            
         
        """
        pass
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFace
         Returns the face(s) to apply the load on   
            
         
        """
        pass
    @property
    def Torque(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Torque
         Returns the torque expression   
            
         
        """
        pass
    @property
    def TorqueAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) TorqueAxis
         Returns the torque axis   
            
         
        """
        pass
    @TorqueAxis.setter
    def TorqueAxis(self, torqueAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) TorqueAxis
         Returns the torque axis   
            
         
        """
        pass
    @property
    def Type(self) -> AnalysisLoadBuilder.AnalysisLoadType:
        """
        Getter for property: ( AnalysisLoadBuilder.AnalysisLoadType NXOpen.Desi) Type
         Returns the Analysis Load type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: AnalysisLoadBuilder.AnalysisLoadType):
        """
        Setter for property: ( AnalysisLoadBuilder.AnalysisLoadType NXOpen.Desi) Type
         Returns the Analysis Load type   
            
         
        """
        pass
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    def UpdateDisplay(self) -> None:
        """
         Update load display symbol 
        """
        pass
import NXOpen
class AnalysisLoad(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Analysis Load """
    @property
    def Acceleration(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Acceleration
         Returns the acceleration expression   
            
         
        """
        pass
    @property
    def AngularRange(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularRange
         Returns the angular range expression   
            
         
        """
        pass
    @property
    def ComponentCSYS(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) ComponentCSYS
         Returns the component CSYS   
            
         
        """
        pass
    @property
    def FaceVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) FaceVector
         Returns the face vector   
            
         
        """
        pass
    @property
    def Force(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Force
         Returns the force expression   
            
         
        """
        pass
    @property
    def ForceDistributionMethod(self) -> AnalysisLoadBuilder.ForceDistributionType:
        """
        Getter for property: ( AnalysisLoadBuilder.ForceDistributionType NXOpen.Desi) ForceDistributionMethod
         Returns the distribution method   
            
         
        """
        pass
    @property
    def ForceLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ForceLocation
         Returns the point selection   
            
         
        """
        pass
    @property
    def ForceObjectOption(self) -> AnalysisLoadBuilder.ForceObjectType:
        """
        Getter for property: ( AnalysisLoadBuilder.ForceObjectType NXOpen.Desi) ForceObjectOption
         Returns the face point type   
            
         
        """
        pass
    @property
    def ForceType(self) -> AnalysisLoadBuilder.AnalysisLoadForceType:
        """
        Getter for property: ( AnalysisLoadBuilder.AnalysisLoadForceType NXOpen.Desi) ForceType
         Returns the force type   
            
         
        """
        pass
    @property
    def ForceX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForceX
         Returns the force x expression   
            
         
        """
        pass
    @property
    def ForceY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForceY
         Returns the force y expression   
            
         
        """
        pass
    @property
    def ForceZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ForceZ
         Returns the force z expression   
            
         
        """
        pass
    @property
    def HeatFlux(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HeatFlux
         Returns the heat flux expression   
            
         
        """
        pass
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this analysis load.  
             
         
        """
        pass
    @property
    def MaxDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDisplacement
         Returns the maximum displacement expression   
            
         
        """
        pass
    @property
    def Moment(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Moment
         Returns the moment expression   
            
         
        """
        pass
    @property
    def MomentX(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentX
         Returns the moment x expression   
            
         
        """
        pass
    @property
    def MomentY(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentY
         Returns the moment y expression   
            
         
        """
        pass
    @property
    def MomentZ(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MomentZ
         Returns the moment z expression   
            
         
        """
        pass
    @property
    def Pressure(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Pressure
         Returns the pressure expression   
            
         
        """
        pass
    @property
    def RemoteForceOption(self) -> AnalysisLoadBuilder.RemoteForceType:
        """
        Getter for property: ( AnalysisLoadBuilder.RemoteForceType NXOpen.Desi) RemoteForceOption
         Returns the remote force load type   
            
         
        """
        pass
    @property
    def RemoteMomentVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) RemoteMomentVector
         Returns the remote moment vector   
            
         
        """
        pass
    @property
    def ReverseBearingLoadDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseBearingLoadDirection
         Returns the flag indicating bearing load force direction is reversed or not   
            
         
        """
        pass
    @property
    def ReversePressureDirection(self) -> bool:
        """
        Getter for property: (bool) ReversePressureDirection
         Returns the flag indicating pressure direction is reversed or not   
            
         
        """
        pass
    @property
    def Torque(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Torque
         Returns the torque expression   
            
         
        """
        pass
    @property
    def TorqueAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) TorqueAxis
         Returns the torque axis   
            
         
        """
        pass
    @property
    def Type(self) -> AnalysisLoadBuilder.AnalysisLoadType:
        """
        Getter for property: ( AnalysisLoadBuilder.AnalysisLoadType NXOpen.Desi) Type
         Returns the Analysis Load type   
            
         
        """
        pass
    def Blank(self) -> None:
        """
         Blanks the analysis load. 
        """
        pass
    def GetFaces(self) -> List[NXOpen.Face]:
        """
         Gets the faces which the load is applied on. 
         Returns faces ( NXOpen.Face Li): .
        """
        pass
    def GetLoadExpressions(self) -> List[NXOpen.Expression]:
        """
         Returns the load expressions, typically just one. Force load specified by components has three. Editing the expression values will make
                   the NXOpen.DesignSimulation.Study results out of date until the analysis or optimization operation is rerun. 
         Returns expressions ( NXOpen.Expression Li): .
        """
        pass
    def Unblank(self) -> None:
        """
         Unblanks the analysis load. 
        """
        pass
import NXOpen
class AnalysisReportBuilder(NXOpen.Builder): 
    """ Represents a builder for specifying Analysis Report Settings used to publish a report for a Performance Predictor Analysis."""
    class ImageBackgroundOption(Enum):
        """
        Members Include: 
         |Original| 
         |Transparent| 

        """
        Original: int
        Transparent: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisReportBuilder.ImageBackgroundOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ImageSizeOption(Enum):
        """
        Members Include: 
         |Small| 
         |Medium| 
         |Large| 

        """
        Small: int
        Medium: int
        Large: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisReportBuilder.ImageSizeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SaveBehaviorOption(Enum):
        """
        Members Include: 
         |Create| 
         |Overwrite| 
         |Native| 

        """
        Create: int
        Overwrite: int
        Native: int
        @staticmethod
        def ValueOf(value: int) -> AnalysisReportBuilder.SaveBehaviorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DatasetName(self) -> str:
        """
        Getter for property: (str) DatasetName
         Returns the dataset name  
            
         
        """
        pass
    @DatasetName.setter
    def DatasetName(self, datasetName: str):
        """
        Setter for property: (str) DatasetName
         Returns the dataset name  
            
         
        """
        pass
    @property
    def ImageBackground(self) -> AnalysisReportBuilder.ImageBackgroundOption:
        """
        Getter for property: ( AnalysisReportBuilder.ImageBackgroundOption NXOpen.Desi) ImageBackground
         Returns the image background option   
            
         
        """
        pass
    @ImageBackground.setter
    def ImageBackground(self, imageBackgroundType: AnalysisReportBuilder.ImageBackgroundOption):
        """
        Setter for property: ( AnalysisReportBuilder.ImageBackgroundOption NXOpen.Desi) ImageBackground
         Returns the image background option   
            
         
        """
        pass
    @property
    def ImageSize(self) -> AnalysisReportBuilder.ImageSizeOption:
        """
        Getter for property: ( AnalysisReportBuilder.ImageSizeOption NXOpen.Desi) ImageSize
         Returns the image size option   
            
         
        """
        pass
    @ImageSize.setter
    def ImageSize(self, imageSize: AnalysisReportBuilder.ImageSizeOption):
        """
        Setter for property: ( AnalysisReportBuilder.ImageSizeOption NXOpen.Desi) ImageSize
         Returns the image size option   
            
         
        """
        pass
    @property
    def NumTextLabels(self) -> int:
        """
        Getter for property: (int) NumTextLabels
         Returns the number of text labels.  
            
         
        """
        pass
    @property
    def OpenDocument(self) -> bool:
        """
        Getter for property: (bool) OpenDocument
         Returns a flag specifying if the report should be opened automatically after creation   
            
         
        """
        pass
    @OpenDocument.setter
    def OpenDocument(self, openDocument: bool):
        """
        Setter for property: (bool) OpenDocument
         Returns a flag specifying if the report should be opened automatically after creation   
            
         
        """
        pass
    @property
    def OutputFileName(self) -> str:
        """
        Getter for property: (str) OutputFileName
         Returns the output file name  
            
         
        """
        pass
    @OutputFileName.setter
    def OutputFileName(self, outputFileName: str):
        """
        Setter for property: (str) OutputFileName
         Returns the output file name  
            
         
        """
        pass
    @property
    def SaveBehavior(self) -> AnalysisReportBuilder.SaveBehaviorOption:
        """
        Getter for property: ( AnalysisReportBuilder.SaveBehaviorOption NXOpen.Desi) SaveBehavior
         Returns the save option to be used when running in Teamcenter managed mode   
            
         
        """
        pass
    @SaveBehavior.setter
    def SaveBehavior(self, saveBehaviorOption: AnalysisReportBuilder.SaveBehaviorOption):
        """
        Setter for property: ( AnalysisReportBuilder.SaveBehaviorOption NXOpen.Desi) SaveBehavior
         Returns the save option to be used when running in Teamcenter managed mode   
            
         
        """
        pass
    @property
    def SaveImages(self) -> bool:
        """
        Getter for property: (bool) SaveImages
         Returns a flag specifying if the Viewport images should be saved in the report folder   
            
         
        """
        pass
    @SaveImages.setter
    def SaveImages(self, saveImages: bool):
        """
        Setter for property: (bool) SaveImages
         Returns a flag specifying if the Viewport images should be saved in the report folder   
            
         
        """
        pass
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the name of the analysis report template file  
            
         
        """
        pass
    @TemplateFileName.setter
    def TemplateFileName(self, templateFileName: str):
        """
        Setter for property: (str) TemplateFileName
         Returns the name of the analysis report template file  
            
         
        """
        pass
    @property
    def ViewportSettingsBuilderCount(self) -> int:
        """
        Getter for property: (int) ViewportSettingsBuilderCount
         Returns the number of viewport settings builders   
            
         
        """
        pass
    def CreateViewportSettingsBuilder(self) -> ViewportSettingsBuilder:
        """
         Creates a NXOpen.DesignSimulation.ViewportSettingsBuilder. 
         Returns newBuilder ( ViewportSettingsBuilder NXOpen.Desi): .
        """
        pass
    def GetNthTextLabelID(self, textLabelIndex: int) -> str:
        """
         Returns the ID text label of index.
         Returns label (str): .
        """
        pass
    def GetNthTextLabelUserName(self, textLabelIndex: int) -> str:
        """
         Returns the user name text label of index.
         Returns userName (str): .
        """
        pass
    def GetTextValueOfLabel(self, label: str) -> str:
        """
         Returns the value of the text with the given label, if the text exists.
         Returns value (str): .
        """
        pass
    def GetViewportSettingsBuilder(self, index: int) -> ViewportSettingsBuilder:
        """
         Returns the viewport settings builder of specified index 
         Returns viewportSettingsBuilder ( ViewportSettingsBuilder NXOpen.Desi): .
        """
        pass
    def IsNthTextLabelReadOnly(self, textLabelIndex: int) -> bool:
        """
         Returns the user name text label of index.
         Returns isReadOnly (bool): .
        """
        pass
    def RemoveViewportSettingsBuilder(self, index: int) -> None:
        """
         Removes viewport settings builder and viewport settings at specified index 
        """
        pass
    def SetTextValueOfLabel(self, label: str, value: str) -> None:
        """
         Sets the value of the text with the given label, if the text exists.
        """
        pass
import NXOpen
class AnalysisReportSettings(NXOpen.NXObject): 
    """ Represents an Analysis Report Settings used to publish a report for a Performance Predictor Analysis."""
    @property
    def ImageBackground(self) -> AnalysisReportBuilder.ImageBackgroundOption:
        """
        Getter for property: ( AnalysisReportBuilder.ImageBackgroundOption NXOpen.Desi) ImageBackground
         Returns the image background option   
            
         
        """
        pass
    @property
    def ImageSize(self) -> AnalysisReportBuilder.ImageSizeOption:
        """
        Getter for property: ( AnalysisReportBuilder.ImageSizeOption NXOpen.Desi) ImageSize
         Returns the image size option   
            
         
        """
        pass
    @property
    def OpenDocument(self) -> bool:
        """
        Getter for property: (bool) OpenDocument
         Returns a flag specifying if the report should be opened automatically after creation   
            
         
        """
        pass
    @property
    def OutputFileName(self) -> str:
        """
        Getter for property: (str) OutputFileName
         Returns the output file name   
            
         
        """
        pass
    @property
    def SaveImages(self) -> bool:
        """
        Getter for property: (bool) SaveImages
         Returns a flag specifying if the Viewport images should be saved in the report folder   
            
         
        """
        pass
    @property
    def TemplateFileName(self) -> str:
        """
        Getter for property: (str) TemplateFileName
         Returns the name of the analysis report template file   
            
         
        """
        pass
    @property
    def ViewportSettingsCount(self) -> int:
        """
        Getter for property: (int) ViewportSettingsCount
         Returns the number of viewport settings   
            
         
        """
        pass
    def GetTextValueOfLabel(self, label: str) -> str:
        """
         Returns the value of the text with the given label, if the text exists. 
         Returns value (str): .
        """
        pass
    def GetViewportSettings(self, index: int) -> ViewportSettings:
        """
         Returns the viewport settings of specified index 
         Returns viewportSettings ( ViewportSettings NXOpen.Desi): .
        """
        pass
import NXOpen
class AnimationController(NXOpen.TransientObject): 
    """
    Represents animation controls and play settings
    """
    class State(Enum):
        """
        Members Include: 
         |Play| 
         |Stop| 
         |Pause| 
         |Next| 
         |Previous| 

        """
        Play: int
        Stop: int
        Pause: int
        Next: int
        Previous: int
        @staticmethod
        def ValueOf(value: int) -> AnimationController.State:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FullCycle(self) -> bool:
        """
        Getter for property: (bool) FullCycle
         Returns the animation is full cycle or not   
            
         
        """
        pass
    @FullCycle.setter
    def FullCycle(self, isFullCycle: bool):
        """
        Setter for property: (bool) FullCycle
         Returns the animation is full cycle or not   
            
         
        """
        pass
    def AnimateContour(self, animState: AnimationController.State) -> None:
        """
         Controls the contour animation 
        """
        pass
    def Dispose(self) -> None:
        """
         Destroys the object. 
        """
        pass
import NXOpen
class ConnectionBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.DesignSimulation.Connection builder
    """
    class Types(Enum):
        """
        Members Include: 
         |BodyToBody| 
         |FaceToFace| 

        """
        BodyToBody: int
        FaceToFace: int
        @staticmethod
        def ValueOf(value: int) -> ConnectionBuilder.Types:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AutoConnection(self) -> bool:
        """
        Getter for property: (bool) AutoConnection
         Returns the flag indicating whether or not to utilize automatic connection detection   
            
         
        """
        pass
    @AutoConnection.setter
    def AutoConnection(self, autoConnection: bool):
        """
        Setter for property: (bool) AutoConnection
         Returns the flag indicating whether or not to utilize automatic connection detection   
            
         
        """
        pass
    @property
    def ConnectionName(self) -> str:
        """
        Getter for property: (str) ConnectionName
         Returns the connection name   
            
         
        """
        pass
    @ConnectionName.setter
    def ConnectionName(self, connectionName: str):
        """
        Setter for property: (str) ConnectionName
         Returns the connection name   
            
         
        """
        pass
    @property
    def SelectBody1(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) SelectBody1
         Returns the select body1   
            
         
        """
        pass
    @property
    def SelectBody2(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) SelectBody2
         Returns the select body2   
            
         
        """
        pass
    @property
    def SelectFaces1(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFaces1
         Returns the select faces1   
            
         
        """
        pass
    @property
    def SelectFaces2(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFaces2
         Returns the select faces2   
            
         
        """
        pass
    @property
    def ShellOffset1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ShellOffset1
         Returns the shell offset for faces1 or body1   
            
         
        """
        pass
    @property
    def ShellOffset2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ShellOffset2
         Returns the shell offset for faces2 or body2   
            
         
        """
        pass
    @property
    def Type(self) -> ConnectionBuilder.Types:
        """
        Getter for property: ( ConnectionBuilder.Types NXOpen.Desi) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ConnectionBuilder.Types):
        """
        Setter for property: ( ConnectionBuilder.Types NXOpen.Desi) Type
         Returns the type   
            
         
        """
        pass
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
import NXOpen
class Connection(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Connection """
    pass
import NXOpen
class ConstructionBodyBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.DesignSimulation.ConstructionBody builder """
    class ConstructionType(Enum):
        """
        Members Include: 
         |ByBody| 
         |ByFace| 

        """
        ByBody: int
        ByFace: int
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.ConstructionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GroupingType(Enum):
        """
        Members Include: 
         |Separate| 
         |Collection| 

        """
        Separate: int
        Collection: int
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.GroupingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MethodOption(Enum):
        """
        Members Include: 
         |KeepIn| 
         |KeepOut| 
         |Shell| 

        """
        KeepIn: int
        KeepOut: int
        Shell: int
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.MethodOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OffsetType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Automatic| 
         |WithRadius| 
         |WithChamfer| 

        """
        NotSet: int
        Automatic: int
        WithRadius: int
        WithChamfer: int
        @staticmethod
        def ValueOf(value: int) -> ConstructionBodyBuilder.OffsetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BlendRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BlendRadius
         Returns the blend radius   
            
         
        """
        pass
    @property
    def Bodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) Bodies
         Returns the body selection for 'Single' grouping type   
            
         
        """
        pass
    @property
    def BodyCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BodyCollector
         Returns the body collector for 'Collection' grouping type   
            
         
        """
        pass
    @property
    def ChamferDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ChamferDistance
         Returns the chamfer distance   
            
         
        """
        pass
    @property
    def DesignSpace(self) -> DesignSpace:
        """
        Getter for property: ( DesignSpace NXOpen.Desi) DesignSpace
         Returns the design space   
            
         
        """
        pass
    @DesignSpace.setter
    def DesignSpace(self, designSpace: DesignSpace):
        """
        Setter for property: ( DesignSpace NXOpen.Desi) DesignSpace
         Returns the design space   
            
         
        """
        pass
    @property
    def FaceCollector(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) FaceCollector
         Returns the face collector for 'By Face' type   
            
         
        """
        pass
    @property
    def GroupingOption(self) -> ConstructionBodyBuilder.GroupingType:
        """
        Getter for property: ( ConstructionBodyBuilder.GroupingType NXOpen.Desi) GroupingOption
         Returns the grouping option for construction bodies   
            
         
        """
        pass
    @GroupingOption.setter
    def GroupingOption(self, groupAs: ConstructionBodyBuilder.GroupingType):
        """
        Setter for property: ( ConstructionBodyBuilder.GroupingType NXOpen.Desi) GroupingOption
         Returns the grouping option for construction bodies   
            
         
        """
        pass
    @property
    def Method(self) -> ConstructionBodyBuilder.MethodOption:
        """
        Getter for property: ( ConstructionBodyBuilder.MethodOption NXOpen.Desi) Method
         Returns the method type   
            
         
        """
        pass
    @Method.setter
    def Method(self, methodOption: ConstructionBodyBuilder.MethodOption):
        """
        Setter for property: ( ConstructionBodyBuilder.MethodOption NXOpen.Desi) Method
         Returns the method type   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the construction body name   
            
         
        """
        pass
    @Name.setter
    def Name(self, constructionBodyName: str):
        """
        Setter for property: (str) Name
         Returns the construction body name   
            
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset   
            
         
        """
        pass
    @property
    def OffsetEdgesType(self) -> ConstructionBodyBuilder.OffsetType:
        """
        Getter for property: ( ConstructionBodyBuilder.OffsetType NXOpen.Desi) OffsetEdgesType
         Returns the offset edges   
            
         
        """
        pass
    @OffsetEdgesType.setter
    def OffsetEdgesType(self, offsetEdgesType: ConstructionBodyBuilder.OffsetType):
        """
        Setter for property: ( ConstructionBodyBuilder.OffsetType NXOpen.Desi) OffsetEdgesType
         Returns the offset edges   
            
         
        """
        pass
    @property
    def ThickenOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThickenOffset
         Returns the thicken offset   
            
         
        """
        pass
    @property
    def Type(self) -> ConstructionBodyBuilder.ConstructionType:
        """
        Getter for property: ( ConstructionBodyBuilder.ConstructionType NXOpen.Desi) Type
         Returns the input type for defining a construction body   
            
         
        """
        pass
    @Type.setter
    def Type(self, constrOption: ConstructionBodyBuilder.ConstructionType):
        """
        Setter for property: ( ConstructionBodyBuilder.ConstructionType NXOpen.Desi) Type
         Returns the input type for defining a construction body   
            
         
        """
        pass
    @property
    def WallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) WallThickness
         Returns the wall thickness   
            
         
        """
        pass
import NXOpen
class ConstructionBodyByFaces(NXOpen.NXObject): 
    """ Represents a NXOpen.DesignSimulation.ConstructionBody created by selecting faces. """
    pass
import NXOpen
class ConstructionBodyCollector(NXOpen.NXObject): 
    """ Represents a NXOpen.DesignSimulation.ConstructionBody collection for a NXOpen.DesignSimulation.DesignSpace """
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this construction body collector.  
             
         
        """
        pass
    def AddMember(self, bFromCollectorToCollector: bool, constructionBody: ConstructionBody) -> None:
        """
        Add a NXOpen.DesignSimulation.ConstructionBody to this NXOpen.DesignSimulation.ConstructionBodyCollector collection.
        """
        pass
    def Blank(self) -> None:
        """
         Blanks the construction body collector (blank ojects within collector). 
        """
        pass
    def RemoveMember(self, bFromCollectorToCollector: bool, constructionBody: ConstructionBody) -> None:
        """
        Remove a NXOpen.DesignSimulation.ConstructionBody from this NXOpen.DesignSimulation.ConstructionBodyCollector collection.
        """
        pass
    def Unblank(self) -> None:
        """
         Unblanks the construction body collector (allow ojects within collector to be visible). 
        """
        pass
    def Ungroup(self) -> None:
        """
        Separate all NXOpen.DesignSimulation.ConstructionBody members and delete this NXOpen.DesignSimulation.ConstructionBodyCollector collection.
        """
        pass
class ConstructionBody(AnalysisBody): 
    """ Represents a NXOpen.DesignSimulation.ConstructionBody for a NXOpen.DesignSimulation.DesignSpace"""
    pass
import NXOpen
class Container(NXOpen.NXObject): 
    """ Represents a Design Simulation Container object"""
    class ReorderType(Enum):
        """
        Members Include: 
         |Before|  Reorder an object before another object in the same container 
         |After|  Reorder an object after another object in the same container 
         |Into|  Reorder an object into the container which does not have it 

        """
        Before: int
        After: int
        Into: int
        @staticmethod
        def ValueOf(value: int) -> Container.ReorderType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetMembers(self) -> List[NXOpen.NXObject]:
        """
         Gets all NXOpen.NXObject members in the order they are referenced. 
         Returns members ( NXOpen.NXObject Li): .
        """
        pass
    def Reorder(self, source: NXOpen.NXObject, target: NXOpen.NXObject, type: Container.ReorderType) -> None:
        """
         Reorders a child object 'before' or 'after' another child object belonging to the same NXOpen.DesignSimulation.Container.
                    Reordering an object 'into' the NXOpen.DesignSimulation.Container that does not have it will be implemented in the future. 
        """
        pass
import NXOpen
class ContourSettingsBuilder(NXOpen.Builder): 
    """ Represents a base class for the builders creating contour result settings."""
    class ColorStyleOption(Enum):
        """
        Members Include: 
         |Default| 
         |Spotlight| 
         |MaterialLimit| 

        """
        Default: int
        Spotlight: int
        MaterialLimit: int
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ColorStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ComponentTypeOption(Enum):
        """
        Members Include: 
         |Magnitude| 
         |WorstInXYZ| 
         |X| 
         |Y| 
         |Z| 
         |All|  All includes Worst in XYZ, X, Y and Z
         |VonMises| 
         |WorstPrincipal| 
         |Scalar| 

        """
        Magnitude: int
        WorstInXYZ: int
        X: int
        Y: int
        Z: int
        All: int
        VonMises: int
        WorstPrincipal: int
        Scalar: int
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ComponentTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ContourLimitOption(Enum):
        """
        Members Include: 
         |AnalysisBodyMaterial| 
         |UserDefined| 

        """
        AnalysisBodyMaterial: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ContourLimitOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ContourStyleOption(Enum):
        """
        Members Include: 
         |Smooth| 
         |Banded| 

        """
        Smooth: int
        Banded: int
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ContourStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultTypeOption(Enum):
        """
        Members Include: 
         |Displacement| 
         |Stress| 
         |FactorOfSafety| 
         |ModalAmplitude| 
         |Temperature| 

        """
        Displacement: int
        Stress: int
        FactorOfSafety: int
        ModalAmplitude: int
        Temperature: int
        @staticmethod
        def ValueOf(value: int) -> ContourSettingsBuilder.ResultTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorStyle(self) -> ContourSettingsBuilder.ColorStyleOption:
        """
        Getter for property: ( ContourSettingsBuilder.ColorStyleOption NXOpen.Desi) ColorStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    @ColorStyle.setter
    def ColorStyle(self, colorStyle: ContourSettingsBuilder.ColorStyleOption):
        """
        Setter for property: ( ContourSettingsBuilder.ColorStyleOption NXOpen.Desi) ColorStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    @property
    def ComponentType(self) -> ContourSettingsBuilder.ComponentTypeOption:
        """
        Getter for property: ( ContourSettingsBuilder.ComponentTypeOption NXOpen.Desi) ComponentType
         Returns the result component type   
            
         
        """
        pass
    @ComponentType.setter
    def ComponentType(self, componentType: ContourSettingsBuilder.ComponentTypeOption):
        """
        Setter for property: ( ContourSettingsBuilder.ComponentTypeOption NXOpen.Desi) ComponentType
         Returns the result component type   
            
         
        """
        pass
    @property
    def ContourStyle(self) -> ContourSettingsBuilder.ContourStyleOption:
        """
        Getter for property: ( ContourSettingsBuilder.ContourStyleOption NXOpen.Desi) ContourStyle
         Returns the display contour style   
            
         
        """
        pass
    @ContourStyle.setter
    def ContourStyle(self, contourStyle: ContourSettingsBuilder.ContourStyleOption):
        """
        Setter for property: ( ContourSettingsBuilder.ContourStyleOption NXOpen.Desi) ContourStyle
         Returns the display contour style   
            
         
        """
        pass
    @property
    def FrequenciesCount(self) -> int:
        """
        Getter for property: (int) FrequenciesCount
         Returns the number of frequencies.  
            
         
        """
        pass
    @property
    def FrequencyIndex(self) -> int:
        """
        Getter for property: (int) FrequencyIndex
         Returns the index of the Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @FrequencyIndex.setter
    def FrequencyIndex(self, frequencyIndex: int):
        """
        Setter for property: (int) FrequencyIndex
         Returns the index of the Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @property
    def ResultType(self) -> ContourSettingsBuilder.ResultTypeOption:
        """
        Getter for property: ( ContourSettingsBuilder.ResultTypeOption NXOpen.Desi) ResultType
         Returns the result type   
            
         
        """
        pass
    @ResultType.setter
    def ResultType(self, resultType: ContourSettingsBuilder.ResultTypeOption):
        """
        Setter for property: ( ContourSettingsBuilder.ResultTypeOption NXOpen.Desi) ResultType
         Returns the result type   
            
         
        """
        pass
    def GetAvailableColorStyles(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> List[ContourSettingsBuilder.ColorStyleOption]:
        """
         Returns the color display styles available for a result type
         Returns colorStyles ( ContourSettingsBuilder.ColorStyleOption List[NXOpen.De): .
        """
        pass
    def GetAvailableComponentTypes(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> List[ContourSettingsBuilder.ComponentTypeOption]:
        """
         Returns the result components available for a result type
         Returns componentTypes ( ContourSettingsBuilder.ComponentTypeOption List[NXOpen.De): .
        """
        pass
    def GetAvailableContourStyles(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> List[ContourSettingsBuilder.ContourStyleOption]:
        """
         Returns the contour display styles available for a available for a result type
         Returns contourStyles ( ContourSettingsBuilder.ContourStyleOption List[NXOpen.De): .
        """
        pass
    def GetAvailableResultTypes(self) -> List[ContourSettingsBuilder.ResultTypeOption]:
        """
         Returns the available result types 
         Returns resultTypes ( ContourSettingsBuilder.ResultTypeOption List[NXOpen.De): .
        """
        pass
    def GetColorStyleInfo(self, colorStyle: ContourSettingsBuilder.ColorStyleOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a color display option
         Returns A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    def GetComponentTypeInfo(self, componentType: ContourSettingsBuilder.ComponentTypeOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a result component
         Returns A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    def GetContourStyleInfo(self, contourStyle: ContourSettingsBuilder.ContourStyleOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a contour display option
         Returns A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    def GetFrequencyId(self, index: int) -> int:
        """
         Returns the frequency id of specified index 
         Returns frequencyId (int): .
        """
        pass
    def GetResultTypeInfo(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> Tuple[str, str]:
        """
         Returns the name and the description of a result type
         Returns A tuple consisting of (name, description). 
         - name is: str.
         - description is: str.

        """
        pass
    def ResetContourOptions(self, resultType: ContourSettingsBuilder.ResultTypeOption) -> None:
        """
         Reset contour options: Result Component, Color Style and Contour Style to 
                    the default values of the result type received as parameter.
        """
        pass
import NXOpen
class DesignSpaceBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.DesignSimulation.DesignSpace builder
    """
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: ( NXOpen.Material) Material
         Returns the material   
            
         
        """
        pass
    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: ( NXOpen.Material) Material
         Returns the material   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the scenery body name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the scenery body name   
            
         
        """
        pass
    @property
    def SelectBody(self) -> NXOpen.SelectBody:
        """
        Getter for property: ( NXOpen.SelectBody) SelectBody
         Returns the selected body   
            
         
        """
        pass
import NXOpen
class DesignSpace(AnalysisBody): 
    """ Represents a Design Simulation Design Space data """
    def AddConstraint(self, constraintObjectTag: NXOpen.NXObject) -> None:
        """
        Add a NXOpen.DesignSimulation.ShapeConstraint or NXOpen.DesignSimulation.OptimizationConstraint to the NXOpen.DesignSimulation.DesignSpace.
        """
        pass
    def CreateConstructionBodyGroup(self, constructionBodies: List[ConstructionBody]) -> ConstructionBodyCollector:
        """
         Creates a NXOpen.DesignSimulation.ConstructionBodyCollector from NXOpen.DesignSimulation.ConstructionBody members. 
         Returns collection ( ConstructionBodyCollector NXOpen.Desi): .
        """
        pass
    def RemoveConstraint(self, constraintObjectTag: NXOpen.NXObject) -> None:
        """
        Remove a NXOpen.DesignSimulation.ShapeConstraint or NXOpen.DesignSimulation.OptimizationConstraint  from the NXOpen.DesignSimulation.DesignSpace.
        """
        pass
import NXOpen
class EnvironmentLoadBuilder(NXOpen.Builder): 
    """ Represents a builder to define environmental loads for an optimization study or analysis. """
    @property
    def AmbientTemperatureEnabled(self) -> bool:
        """
        Getter for property: (bool) AmbientTemperatureEnabled
         Returns the control to enable  disable use of ambient temperature for thermal analysis   
            
         
        """
        pass
    @AmbientTemperatureEnabled.setter
    def AmbientTemperatureEnabled(self, enabled: bool):
        """
        Setter for property: (bool) AmbientTemperatureEnabled
         Returns the control to enable  disable use of ambient temperature for thermal analysis   
            
         
        """
        pass
    @property
    def AmbientTemperatureMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AmbientTemperatureMagnitude
         Returns the ambient temperature magnitude   
            
         
        """
        pass
    @property
    def GravityDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) GravityDirection
         Returns the gravity direction   
            
         
        """
        pass
    @GravityDirection.setter
    def GravityDirection(self, gravityDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) GravityDirection
         Returns the gravity direction   
            
         
        """
        pass
    @property
    def GravityEnabled(self) -> bool:
        """
        Getter for property: (bool) GravityEnabled
         Returns the control to enable  disable use of gravity for the optimization or analysis   
            
         
        """
        pass
    @GravityEnabled.setter
    def GravityEnabled(self, enabled: bool):
        """
        Setter for property: (bool) GravityEnabled
         Returns the control to enable  disable use of gravity for the optimization or analysis   
            
         
        """
        pass
    @property
    def GravityMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GravityMagnitude
         Returns the gravity magnitude   
            
         
        """
        pass
import NXOpen
class ExportToCaeBuilder(NXOpen.Builder): 
    """
    Represents a builder to specify contour display settings and plot contours according to the settings
    """
    class SolverTypeOption(Enum):
        """
        Members Include: 
         |SimcenterNastran| 

        """
        SimcenterNastran: int
        @staticmethod
        def ValueOf(value: int) -> ExportToCaeBuilder.SolverTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UseBodyOption(Enum):
        """
        Members Include: 
         |AllBodies| 
         |StudyBodies| 

        """
        AllBodies: int
        StudyBodies: int
        @staticmethod
        def ValueOf(value: int) -> ExportToCaeBuilder.UseBodyOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BodyOption(self) -> ExportToCaeBuilder.UseBodyOption:
        """
        Getter for property: ( ExportToCaeBuilder.UseBodyOption NXOpen.Desi) BodyOption
         Returns the use body option choice   
            
         
        """
        pass
    @BodyOption.setter
    def BodyOption(self, bodyOption: ExportToCaeBuilder.UseBodyOption):
        """
        Setter for property: ( ExportToCaeBuilder.UseBodyOption NXOpen.Desi) BodyOption
         Returns the use body option choice   
            
         
        """
        pass
    @property
    def CreateIdealizedPart(self) -> bool:
        """
        Getter for property: (bool) CreateIdealizedPart
         Returns the create idealized part option
                  
            
         
        """
        pass
    @CreateIdealizedPart.setter
    def CreateIdealizedPart(self, createIdealizedPart: bool):
        """
        Setter for property: (bool) CreateIdealizedPart
         Returns the create idealized part option
                  
            
         
        """
        pass
    @property
    def FemPartName(self) -> str:
        """
        Getter for property: (str) FemPartName
         Returns the fem part name   
            
         
        """
        pass
    @FemPartName.setter
    def FemPartName(self, femPartName: str):
        """
        Setter for property: (str) FemPartName
         Returns the fem part name   
            
         
        """
        pass
    @property
    def IdealizedPartName(self) -> str:
        """
        Getter for property: (str) IdealizedPartName
         Returns the idealized part name   
            
         
        """
        pass
    @IdealizedPartName.setter
    def IdealizedPartName(self, idealizedPartName: str):
        """
        Setter for property: (str) IdealizedPartName
         Returns the idealized part name   
            
         
        """
        pass
    @property
    def SimPartName(self) -> str:
        """
        Getter for property: (str) SimPartName
         Returns the sim part name   
            
         
        """
        pass
    @SimPartName.setter
    def SimPartName(self, simPartName: str):
        """
        Setter for property: (str) SimPartName
         Returns the sim part name   
            
         
        """
        pass
    @property
    def SolverType(self) -> ExportToCaeBuilder.SolverTypeOption:
        """
        Getter for property: ( ExportToCaeBuilder.SolverTypeOption NXOpen.Desi) SolverType
         Returns the solver name   
            
         
        """
        pass
    @SolverType.setter
    def SolverType(self, solverType: ExportToCaeBuilder.SolverTypeOption):
        """
        Setter for property: ( ExportToCaeBuilder.SolverTypeOption NXOpen.Desi) SolverType
         Returns the solver name   
            
         
        """
        pass
import NXOpen
class OptimizationConstraintBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.DesignSimulation.OptimizationConstraint builder """
    class ConstraintType(Enum):
        """
        Members Include: 
         |MassTarget| 
         |MinimumMassLimit| 
         |MaximumMassLimit| 
         |MaximumStressLimit| 
         |MaximumDisplacementLimit| 
         |FirstFlexibleModeTarget| 
         |MinimumFirstFlexibleModeLimit| 
         |MaximumFirstFlexibleModeLimit| 

        """
        MassTarget: int
        MinimumMassLimit: int
        MaximumMassLimit: int
        MaximumStressLimit: int
        MaximumDisplacementLimit: int
        FirstFlexibleModeTarget: int
        MinimumFirstFlexibleModeLimit: int
        MaximumFirstFlexibleModeLimit: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationConstraintBuilder.ConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplacementOption(Enum):
        """
        Members Include: 
         |AbsoluteMagnitude| 
         |X| 
         |Y| 
         |Z| 
         |AlongVector| 

        """
        AbsoluteMagnitude: int
        X: int
        Y: int
        Z: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationConstraintBuilder.DisplacementOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaximumStressOption(Enum):
        """
        Members Include: 
         |UltimateTensileStrength| 
         |Yield| 
         |Absolute| 

        """
        UltimateTensileStrength: int
        Yield: int
        Absolute: int
        @staticmethod
        def ValueOf(value: int) -> OptimizationConstraintBuilder.MaximumStressOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AbsoluteValueOfStress(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AbsoluteValueOfStress
         Returns the finite value of stress expression   
            
         
        """
        pass
    @property
    def DesignSpace(self) -> DesignSpace:
        """
        Getter for property: ( DesignSpace NXOpen.Desi) DesignSpace
         Returns the design space   
            
         
        """
        pass
    @DesignSpace.setter
    def DesignSpace(self, designSpace: DesignSpace):
        """
        Setter for property: ( DesignSpace NXOpen.Desi) DesignSpace
         Returns the design space   
            
         
        """
        pass
    @property
    def DisplacementLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) DisplacementLocation
         Returns the defined location for displacement limit   
            
         
        """
        pass
    @DisplacementLocation.setter
    def DisplacementLocation(self, location: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) DisplacementLocation
         Returns the defined location for displacement limit   
            
         
        """
        pass
    @property
    def DisplacementType(self) -> OptimizationConstraintBuilder.DisplacementOption:
        """
        Getter for property: ( OptimizationConstraintBuilder.DisplacementOption NXOpen.Desi) DisplacementType
         Returns the displacement type   
            
         
        """
        pass
    @DisplacementType.setter
    def DisplacementType(self, displacementType: OptimizationConstraintBuilder.DisplacementOption):
        """
        Setter for property: ( OptimizationConstraintBuilder.DisplacementOption NXOpen.Desi) DisplacementType
         Returns the displacement type   
            
         
        """
        pass
    @property
    def DisplacementVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DisplacementVector
         Returns the displacement vector   
            
         
        """
        pass
    @DisplacementVector.setter
    def DisplacementVector(self, displacementVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DisplacementVector
         Returns the displacement vector   
            
         
        """
        pass
    @property
    def FirstFlexibleFrequency(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FirstFlexibleFrequency
         Returns the first flexible frequency expression   
            
         
        """
        pass
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass expression   
            
         
        """
        pass
    @property
    def MaxDisplacement(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxDisplacement
         Returns the max displacement expression   
            
         
        """
        pass
    @property
    def MaxFirstFlexFrequency(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxFirstFlexFrequency
         Returns the max first flex frequency expression   
            
         
        """
        pass
    @property
    def MaxPercentOfStress(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxPercentOfStress
         Returns the max percent of stress expression   
            
         
        """
        pass
    @property
    def MaximumMass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumMass
         Returns the maximum mass expression   
            
         
        """
        pass
    @property
    def MaximumStressType(self) -> OptimizationConstraintBuilder.MaximumStressOption:
        """
        Getter for property: ( OptimizationConstraintBuilder.MaximumStressOption NXOpen.Desi) MaximumStressType
         Returns the maximum stress type   
            
         
        """
        pass
    @MaximumStressType.setter
    def MaximumStressType(self, maxStressType: OptimizationConstraintBuilder.MaximumStressOption):
        """
        Setter for property: ( OptimizationConstraintBuilder.MaximumStressOption NXOpen.Desi) MaximumStressType
         Returns the maximum stress type   
            
         
        """
        pass
    @property
    def MinFirstFlexFrequency(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinFirstFlexFrequency
         Returns the min first flex frequency expression   
            
         
        """
        pass
    @property
    def MinimumMass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumMass
         Returns the minimum mass expression   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the optimization constraint name   
            
         
        """
        pass
    @Name.setter
    def Name(self, optimizationConstraintName: str):
        """
        Setter for property: (str) Name
         Returns the optimization constraint name   
            
         
        """
        pass
    @property
    def SelectFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectFace
         Returns the select face   
            
         
        """
        pass
    @property
    def Type(self) -> OptimizationConstraintBuilder.ConstraintType:
        """
        Getter for property: ( OptimizationConstraintBuilder.ConstraintType NXOpen.Desi) Type
         Returns the type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: OptimizationConstraintBuilder.ConstraintType):
        """
        Setter for property: ( OptimizationConstraintBuilder.ConstraintType NXOpen.Desi) Type
         Returns the type   
            
         
        """
        pass
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
import NXOpen
class OptimizationConstraint(NXOpen.NXObject): 
    """ Represents a Design Simulation Study Optimization Constraint """
    pass
import NXOpen
class PerformancePredictorManager(NXOpen.Object): 
    """ Represents the Performance Predictor Manager class."""
    def AbortAllSimulations() -> None:
        """
         Abort all running Performance Predictor Analysis 
        """
        pass
    def CreateAttributes() -> None:
        """
         Prepare for export for CAE 
        """
        pass
    def EnterPerformancePredictorApplication() -> None:
        """
         Enter live simulation application 
        """
        pass
    def ExitPerformancePredictorApplication() -> None:
        """
         Exit live simulation application 
        """
        pass
    def GetDelay() -> bool:
        """
         Gets whether delay is enabled or not 
         Returns delay (bool): .
        """
        pass
    def GetStoreResults() -> bool:
        """
         Gets whether store results is enabled or not 
         Returns storeResult (bool): .
        """
        pass
    def ResetMeasureHistory() -> None:
        """
         Resets measure histories of Performance Predictor 
        """
        pass
    def SetDelay(delay: bool) -> None:
        """
         Sets delay of Performance Predictor 
        """
        pass
    def SetStoreResults(storeResult: bool) -> None:
        """
         Sets store results of Performance Predictor 
        """
        pass
import NXOpen
class PostManager(NXOpen.Object): 
    """ Represents a Design Simulation Post Manager """
    def CreateAnimationController(self) -> AnimationController:
        """
         Creates a NXOpen.DesignSimulation.AnimationController.
                
         Returns animationController ( AnimationController NXOpen.Desi): .
        """
        pass
    def CreateResultSettingsBuilder(self) -> ResultSettingsBuilder:
        """
         Creates a NXOpen.DesignSimulation.ResultSettingsBuilder.
                
         Returns builder ( ResultSettingsBuilder NXOpen.Desi): .
        """
        pass
    def CreateViewContourBuilder(self) -> ViewContourBuilder:
        """
         Creates a NXOpen.DesignSimulation.ViewContourBuilder.
                
         Returns builder ( ViewContourBuilder NXOpen.Desi): .
        """
        pass
    def CreateViewTabularResultBuilder(self) -> ViewTabularResultBuilder:
        """
         Creates a NXOpen.DesignSimulation.ViewTabularResultBuilder.
                
         Returns builder ( ViewTabularResultBuilder NXOpen.Desi): .
        """
        pass
    def CreateViewXygraphBuilder(self) -> ViewXygraphBuilder:
        """
         Creates a NXOpen.DesignSimulation.ViewXygraphBuilder.
                
         Returns builder ( ViewXygraphBuilder NXOpen.Desi): .
        """
        pass
    def ExportAnimationToGif(self, fileName: str) -> None:
        """
         Exports the playing contour animation to a GIF file. If there is no contour animation playing, an error will be thrown.
                
        """
        pass
    def GetContourLimits(self, contourIndex: int) -> Tuple[float, float, NXOpen.Unit]:
        """
         Gets the Min and Max limits of a displayed Contour Plot.
                
         Returns A tuple consisting of (minValue, maxValue, unitTag). 
         - minValue is: float.
         - maxValue is: float.
         - unitTag is:  NXOpen.Unit.

        """
        pass
    def HideContour(self) -> None:
        """
         Hides the contour.
                
        """
        pass
    def IsAnimationPlaying(self) -> bool:
        """
         Asks whether there is animation playing.
                
         Returns isPlaying (bool): .
        """
        pass
    def IsContourShown(self) -> bool:
        """
         Asks whether there is contour shown.
                
         Returns isContourShown (bool): .
        """
        pass
    def ShowContour(self) -> None:
        """
         Plots contour according to existing view contour settings.
                
        """
        pass
import NXOpen
class ResultMeasureBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.DesignSimulation.ResultMeasure builder
    """
    class ResultComponentOption(Enum):
        """
        Members Include: 
         |DisplacementMagnitude| 
         |DisplacementWorstInXYZ| 
         |DisplacementX| 
         |DisplacementY| 
         |DisplacementZ| 
         |StressVonMises| 
         |StressWorstPrincipal| 
         |SafetyFactorVonMises| 
         |Temperature| 

        """
        DisplacementMagnitude: int
        DisplacementWorstInXYZ: int
        DisplacementX: int
        DisplacementY: int
        DisplacementZ: int
        StressVonMises: int
        StressWorstPrincipal: int
        SafetyFactorVonMises: int
        Temperature: int
        @staticmethod
        def ValueOf(value: int) -> ResultMeasureBuilder.ResultComponentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultTypeOption(Enum):
        """
        Members Include: 
         |Displacement| 
         |Stress| 
         |SafetyFactor| 
         |Thermal| 

        """
        Displacement: int
        Stress: int
        SafetyFactor: int
        Thermal: int
        @staticmethod
        def ValueOf(value: int) -> ResultMeasureBuilder.ResultTypeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultValueOption(Enum):
        """
        Members Include: 
         |Minimum| 
         |Maximum| 

        """
        Minimum: int
        Maximum: int
        @staticmethod
        def ValueOf(value: int) -> ResultMeasureBuilder.ResultValueOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LabelPMI(self) -> bool:
        """
        Getter for property: (bool) LabelPMI
         Returns the label PMI   
            
         
        """
        pass
    @LabelPMI.setter
    def LabelPMI(self, labelPMI: bool):
        """
        Setter for property: (bool) LabelPMI
         Returns the label PMI   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the result measure name   
            
         
        """
        pass
    @Name.setter
    def Name(self, resultMeasureName: str):
        """
        Setter for property: (str) Name
         Returns the result measure name   
            
         
        """
        pass
    @property
    def NaturalFrequenciesCount(self) -> int:
        """
        Getter for property: (int) NaturalFrequenciesCount
         Returns the number of Natural Frequencies computed for Natural Frequencies analysis type.  
            
         
        """
        pass
    @property
    def NaturalFrequencyIndex(self) -> int:
        """
        Getter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @NaturalFrequencyIndex.setter
    def NaturalFrequencyIndex(self, resultModeIndex: int):
        """
        Setter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @property
    def ResultComponent(self) -> ResultMeasureBuilder.ResultComponentOption:
        """
        Getter for property: ( ResultMeasureBuilder.ResultComponentOption NXOpen.Desi) ResultComponent
         Returns the result component   
            
         
        """
        pass
    @ResultComponent.setter
    def ResultComponent(self, resultComponentType: ResultMeasureBuilder.ResultComponentOption):
        """
        Setter for property: ( ResultMeasureBuilder.ResultComponentOption NXOpen.Desi) ResultComponent
         Returns the result component   
            
         
        """
        pass
    @property
    def ResultType(self) -> ResultMeasureBuilder.ResultTypeOption:
        """
        Getter for property: ( ResultMeasureBuilder.ResultTypeOption NXOpen.Desi) ResultType
         Returns the result type   
            
         
        """
        pass
    @ResultType.setter
    def ResultType(self, resultType: ResultMeasureBuilder.ResultTypeOption):
        """
        Setter for property: ( ResultMeasureBuilder.ResultTypeOption NXOpen.Desi) ResultType
         Returns the result type   
            
         
        """
        pass
    @property
    def ResultValue(self) -> ResultMeasureBuilder.ResultValueOption:
        """
        Getter for property: ( ResultMeasureBuilder.ResultValueOption NXOpen.Desi) ResultValue
         Returns the oepration type   
            
         
        """
        pass
    @ResultValue.setter
    def ResultValue(self, resultValueType: ResultMeasureBuilder.ResultValueOption):
        """
        Setter for property: ( ResultMeasureBuilder.ResultValueOption NXOpen.Desi) ResultValue
         Returns the oepration type   
            
         
        """
        pass
    @property
    def SelectedEntities(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SelectedEntities
         Returns the selected entity  
            
         
        """
        pass
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
import NXOpen
class ResultMeasure(NXOpen.NXObject): 
    """ Represents a Design Simulation Result Measure """
    @property
    def IsBlanked(self) -> bool:
        """
        Getter for property: (bool) IsBlanked
         Returns the blank status of this result measure.  
             
         
        """
        pass
    @property
    def LabelPMI(self) -> bool:
        """
        Getter for property: (bool) LabelPMI
         Returns the label PMI   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the result measure name   
            
         
        """
        pass
    @property
    def NaturalFrequency(self) -> float:
        """
        Getter for property: (float) NaturalFrequency
         Returns the Natural Frequency (in Hz) for result measures created for natural frequencies analysis.  
            
         
        """
        pass
    @property
    def NaturalFrequencyIndex(self) -> int:
        """
        Getter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @property
    def ResultComponent(self) -> ResultMeasureBuilder.ResultComponentOption:
        """
        Getter for property: ( ResultMeasureBuilder.ResultComponentOption NXOpen.Desi) ResultComponent
         Returns the result component   
            
         
        """
        pass
    @property
    def ResultMeasureType(self) -> ResultMeasureBuilder.ResultTypeOption:
        """
        Getter for property: ( ResultMeasureBuilder.ResultTypeOption NXOpen.Desi) ResultMeasureType
         Returns the result type   
            
         
        """
        pass
    @property
    def ResultValueType(self) -> ResultMeasureBuilder.ResultValueOption:
        """
        Getter for property: ( ResultMeasureBuilder.ResultValueOption NXOpen.Desi) ResultValueType
         Returns the operation type   
            
         
        """
        pass
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the flag indicating whether the object uses an user-defined name   
            
         
        """
        pass
    @property
    def Value(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Value
         Returns the value of Result Measure as an Expression   
            
         
        """
        pass
    def Blank(self) -> None:
        """
         Blanks the result measure. 
        """
        pass
    def GetSelectedObjects(self) -> List[NXOpen.DisplayableObject]:
        """
         Get the objects selected for measuring 
         Returns displayableObject ( NXOpen.DisplayableObject Li): .
        """
        pass
    def PopulateValidation(self, validationTag: NXOpen.Validation) -> None:
        """
         Populates the validation object. 
        """
        pass
    def Unblank(self) -> None:
        """
         Unblanks the result measure. 
        """
        pass
import NXOpen
class ResultSettingsBuilder(ContourSettingsBuilder): 
    """ Represents a builder for specifying result settings used to display contour results for Performance Predictor Analysis."""
    @property
    def ColorDisplayStyle(self) -> ViewContourBuilder.ColorDisplayStyleOption:
        """
        Getter for property: ( ViewContourBuilder.ColorDisplayStyleOption NXOpen.Desi) ColorDisplayStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    @ColorDisplayStyle.setter
    def ColorDisplayStyle(self, colorDisplayStyle: ViewContourBuilder.ColorDisplayStyleOption):
        """
        Setter for property: ( ViewContourBuilder.ColorDisplayStyleOption NXOpen.Desi) ColorDisplayStyle
         Returns the display color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    @property
    def ContourDisplayStyle(self) -> ViewContourBuilder.ContourDisplayStyleOption:
        """
        Getter for property: ( ViewContourBuilder.ContourDisplayStyleOption NXOpen.Desi) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    @ContourDisplayStyle.setter
    def ContourDisplayStyle(self, contourDisplayStyle: ViewContourBuilder.ContourDisplayStyleOption):
        """
        Setter for property: ( ViewContourBuilder.ContourDisplayStyleOption NXOpen.Desi) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    @property
    def ContourLimit(self) -> ContourSettingsBuilder.ContourLimitOption:
        """
        Getter for property: ( ContourSettingsBuilder.ContourLimitOption NXOpen.Desi) ContourLimit
         Returns the Contour limit computation option for displaying results contour.  
             
         
        """
        pass
    @ContourLimit.setter
    def ContourLimit(self, contourLimit: ContourSettingsBuilder.ContourLimitOption):
        """
        Setter for property: ( ContourSettingsBuilder.ContourLimitOption NXOpen.Desi) ContourLimit
         Returns the Contour limit computation option for displaying results contour.  
             
         
        """
        pass
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: ( NXOpen.Material) Material
         Returns the Material used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material     
            
         
        """
        pass
    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: ( NXOpen.Material) Material
         Returns the Material used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material     
            
         
        """
        pass
    @property
    def MaterialLimit(self) -> ViewContourBuilder.MaterialLimitOption:
        """
        Getter for property: ( ViewContourBuilder.MaterialLimitOption NXOpen.Desi) MaterialLimit
         Returns the Material Option  
            
         
        """
        pass
    @MaterialLimit.setter
    def MaterialLimit(self, materialLimitOption: ViewContourBuilder.MaterialLimitOption):
        """
        Setter for property: ( ViewContourBuilder.MaterialLimitOption NXOpen.Desi) MaterialLimit
         Returns the Material Option  
            
         
        """
        pass
    @property
    def MaterialLimitBody(self) -> AnalysisBody:
        """
        Getter for property: ( AnalysisBody NXOpen.Desi) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody     
            
         
        """
        pass
    @MaterialLimitBody.setter
    def MaterialLimitBody(self, body: AnalysisBody):
        """
        Setter for property: ( AnalysisBody NXOpen.Desi) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody     
            
         
        """
        pass
    @property
    def MaxStressCompression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxStressCompression
         Returns the Max Stress Compression expression used for Stress Worst Principal when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined     
            
         
        """
        pass
    @property
    def MaxStressTension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxStressTension
         Returns the Max Stress Tension expression used for Stress Worst Principal when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined     
            
         
        """
        pass
    @property
    def NaturalFrequenciesCount(self) -> int:
        """
        Getter for property: (int) NaturalFrequenciesCount
         Returns the number of Natural Frequencies computed for Natural Frequencies analysis type.  
            
         
        """
        pass
    @property
    def NaturalFrequencyIndex(self) -> int:
        """
        Getter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @NaturalFrequencyIndex.setter
    def NaturalFrequencyIndex(self, frequencyIndex: int):
        """
        Setter for property: (int) NaturalFrequencyIndex
         Returns the index of the Natural Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @property
    def ResultComponent(self) -> ViewContourBuilder.ResultComponentOption:
        """
        Getter for property: ( ViewContourBuilder.ResultComponentOption NXOpen.Desi) ResultComponent
         Returns the result component type   
            
         
        """
        pass
    @ResultComponent.setter
    def ResultComponent(self, resultComponentType: ViewContourBuilder.ResultComponentOption):
        """
        Setter for property: ( ViewContourBuilder.ResultComponentOption NXOpen.Desi) ResultComponent
         Returns the result component type   
            
         
        """
        pass
    @property
    def YieldStrength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YieldStrength
         Returns the Yield Strength expression used for Stress Von Mises when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined     
            
         
        """
        pass
    def IsFrequencySelectedForAnimation(self, frequrncyIndex: int) -> bool:
        """
         Checks the selected for animation state of coresponding Frequency index.
         Returns isFrequencySelected (bool): .
        """
        pass
    def IsNaturalFrequencySelectedForAnimation(self, frequrncyIndex: int) -> bool:
        """
         The check state of coresponding Natural Frequency mode 
         Returns isFrequencySelected (bool): .
        """
        pass
    def SetFrequencySelectedForAnimation(self, frequencyIndex: int, isFrequencySelected: bool) -> None:
        """
         Sets the selected for animation state of coresponding Frequency index.
        """
        pass
    def SetNaturalFrequencySelectedForAnimation(self, frequencyIndex: int, isFrequencySelected: bool) -> None:
        """
         The check state of coresponding Natural Frequency mode.
        """
        pass
import NXOpen
class SceneryBodyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.DesignSimulation.SceneryBody builder
    """
    class MaterialDefinitionType(Enum):
        """
        Members Include: 
         |InheritedFromBody| 
         |UserDefined| 
         |Default| 

        """
        InheritedFromBody: int
        UserDefined: int
        Default: int
        @staticmethod
        def ValueOf(value: int) -> SceneryBodyBuilder.MaterialDefinitionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Bodies(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) Bodies
         Returns the selected body   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: ( NXOpen.Material) Material
         Returns the assigned material   
            
         
        """
        pass
    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: ( NXOpen.Material) Material
         Returns the assigned material   
            
         
        """
        pass
    @property
    def MaterialDefinition(self) -> SceneryBodyBuilder.MaterialDefinitionType:
        """
        Getter for property: ( SceneryBodyBuilder.MaterialDefinitionType NXOpen.Desi) MaterialDefinition
         Returns the way material is assigned   
            
         
        """
        pass
    @MaterialDefinition.setter
    def MaterialDefinition(self, materialDefinition: SceneryBodyBuilder.MaterialDefinitionType):
        """
        Setter for property: ( SceneryBodyBuilder.MaterialDefinitionType NXOpen.Desi) MaterialDefinition
         Returns the way material is assigned   
            
         
        """
        pass
    @property
    def SceneryBodyName(self) -> str:
        """
        Getter for property: (str) SceneryBodyName
         Returns the scenery body name   
            
         
        """
        pass
    @SceneryBodyName.setter
    def SceneryBodyName(self, sceneryBodyName: str):
        """
        Setter for property: (str) SceneryBodyName
         Returns the scenery body name   
            
         
        """
        pass
class SceneryBody(AnalysisBody): 
    """ Represents a Design Simulation Study Scenery Body  """
    pass
import NXOpen
class ShapeConstraintBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.DesignSimulation.ShapeConstraint builder """
    class CenterOfGravityLocationType(Enum):
        """
        Members Include: 
         |KeepWithinSphere| 
         |KeepWithinCylinder| 
         |KeepOnPlane| 
         |KeepWithinDistanceToPlane| 

        """
        KeepWithinSphere: int
        KeepWithinCylinder: int
        KeepOnPlane: int
        KeepWithinDistanceToPlane: int
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.CenterOfGravityLocationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ConstraintType(Enum):
        """
        Members Include: 
         |PlanarSymmetry| 
         |RepeatedRotationalSymmetry| 
         |SegmentalRotationalSymmetry| 
         |ExtrudeAlongVector| 
         |DraftAngle| 
         |MinimumMemberSize| 
         |MaximumMemberSize| 
         |MinimumWallThickness| 
         |MaximumWallThickness| 
         |OverhangingGeometryPrevention| 
         |SelfSupporting| 
         |ThroughHolePrevention| 
         |RevolutionAxis| 
         |CenterOfGravityLocation| 
         |FillVoid| 
         |FillFromDirection| 
         |MultiAxisTooling| 

        """
        PlanarSymmetry: int
        RepeatedRotationalSymmetry: int
        SegmentalRotationalSymmetry: int
        ExtrudeAlongVector: int
        DraftAngle: int
        MinimumMemberSize: int
        MaximumMemberSize: int
        MinimumWallThickness: int
        MaximumWallThickness: int
        OverhangingGeometryPrevention: int
        SelfSupporting: int
        ThroughHolePrevention: int
        RevolutionAxis: int
        CenterOfGravityLocation: int
        FillVoid: int
        FillFromDirection: int
        MultiAxisTooling: int
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.ConstraintType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DraftPartingObjectType(Enum):
        """
        Members Include: 
         |SpecifiedPlane| 
         |SpecifiedFace| 
         |AutomaticFace| 

        """
        SpecifiedPlane: int
        SpecifiedFace: int
        AutomaticFace: int
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.DraftPartingObjectType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FillFromDirectionType(Enum):
        """
        Members Include: 
         |Unidirectional| 
         |BidirectionalFromPlane| 
         |SymmetricalFromPlane| 
         |BidirectionalInBetween| 

        """
        Unidirectional: int
        BidirectionalFromPlane: int
        SymmetricalFromPlane: int
        BidirectionalInBetween: int
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.FillFromDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaxOverhangAngleValue(Enum):
        """
        Members Include: 
         |Degrees27| 
         |Degrees45| 
         |Degrees65| 

        """
        Degrees27: int
        Degrees45: int
        Degrees65: int
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.MaxOverhangAngleValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MultiAxisToolingType(Enum):
        """
        Members Include: 
         |TwoAndHalfAxis| 
         |ThreeAxis| 
         |FiveAxis| 

        """
        TwoAndHalfAxis: int
        ThreeAxis: int
        FiveAxis: int
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.MultiAxisToolingType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PlanarSymmetryInputOption(Enum):
        """
        Members Include: 
         |Segment| 
         |Whole| 

        """
        Segment: int
        Whole: int
        @staticmethod
        def ValueOf(value: int) -> ShapeConstraintBuilder.PlanarSymmetryInputOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BasePlaneNormal(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) BasePlaneNormal
         Returns the Multi Axis Tooling base plane normal   
            
         
        """
        pass
    @BasePlaneNormal.setter
    def BasePlaneNormal(self, basePlaneNormal: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) BasePlaneNormal
         Returns the Multi Axis Tooling base plane normal   
            
         
        """
        pass
    @property
    def CenterOfGravityAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) CenterOfGravityAxis
         Returns the Center of Gravity Axis   
            
         
        """
        pass
    @CenterOfGravityAxis.setter
    def CenterOfGravityAxis(self, centerOfGravityAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) CenterOfGravityAxis
         Returns the Center of Gravity Axis   
            
         
        """
        pass
    @property
    def CenterOfGravityLocationOption(self) -> ShapeConstraintBuilder.CenterOfGravityLocationType:
        """
        Getter for property: ( ShapeConstraintBuilder.CenterOfGravityLocationType NXOpen.Desi) CenterOfGravityLocationOption
         Returns the Center of Gravity Option   
            
         
        """
        pass
    @CenterOfGravityLocationOption.setter
    def CenterOfGravityLocationOption(self, centerOfGravityOption: ShapeConstraintBuilder.CenterOfGravityLocationType):
        """
        Setter for property: ( ShapeConstraintBuilder.CenterOfGravityLocationType NXOpen.Desi) CenterOfGravityLocationOption
         Returns the Center of Gravity Option   
            
         
        """
        pass
    @property
    def CenterOfGravityPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) CenterOfGravityPlane
         Returns the Center of Gravity Plane   
            
         
        """
        pass
    @CenterOfGravityPlane.setter
    def CenterOfGravityPlane(self, centerOfGravityPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) CenterOfGravityPlane
         Returns the Center of Gravity Plane   
            
         
        """
        pass
    @property
    def CenterOfGravityPlaneOffset1(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CenterOfGravityPlaneOffset1
         Returns the Center of Gravity Plane Upper Limit   
            
         
        """
        pass
    @property
    def CenterOfGravityPlaneOffset2(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CenterOfGravityPlaneOffset2
         Returns the Center of Gravity Plane Lower Limit   
            
         
        """
        pass
    @property
    def CenterOfGravityPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) CenterOfGravityPoint
         Returns the Center of Gravity Location   
            
         
        """
        pass
    @CenterOfGravityPoint.setter
    def CenterOfGravityPoint(self, locationPt: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) CenterOfGravityPoint
         Returns the Center of Gravity Location   
            
         
        """
        pass
    @property
    def CenterOfGravityZoneRadius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CenterOfGravityZoneRadius
         Returns the Center of Gravity Zone Radius   
            
         
        """
        pass
    @property
    def DesignSpace(self) -> DesignSpace:
        """
        Getter for property: ( DesignSpace NXOpen.Desi) DesignSpace
         Returns the design space   
            
         
        """
        pass
    @DesignSpace.setter
    def DesignSpace(self, designSpace: DesignSpace):
        """
        Setter for property: ( DesignSpace NXOpen.Desi) DesignSpace
         Returns the design space   
            
         
        """
        pass
    @property
    def DraftAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DraftAngle
         Returns the draft angle   
            
         
        """
        pass
    @property
    def DraftDrawDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DraftDrawDirection
         Returns the draft draw direction   
            
         
        """
        pass
    @DraftDrawDirection.setter
    def DraftDrawDirection(self, draftDrawDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DraftDrawDirection
         Returns the draft draw direction   
            
         
        """
        pass
    @property
    def DraftPartingFace(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) DraftPartingFace
         Returns the draft parting faces   
            
         
        """
        pass
    @property
    def DraftPartingObjectOptions(self) -> ShapeConstraintBuilder.DraftPartingObjectType:
        """
        Getter for property: ( ShapeConstraintBuilder.DraftPartingObjectType NXOpen.Desi) DraftPartingObjectOptions
         Returns the Draft Angle Parting Object Options   
            
         
        """
        pass
    @DraftPartingObjectOptions.setter
    def DraftPartingObjectOptions(self, draftPartingObjectOptions: ShapeConstraintBuilder.DraftPartingObjectType):
        """
        Setter for property: ( ShapeConstraintBuilder.DraftPartingObjectType NXOpen.Desi) DraftPartingObjectOptions
         Returns the Draft Angle Parting Object Options   
            
         
        """
        pass
    @property
    def DraftPartingPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) DraftPartingPlane
         Returns the draft parting plane   
            
         
        """
        pass
    @DraftPartingPlane.setter
    def DraftPartingPlane(self, draftPartingPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) DraftPartingPlane
         Returns the draft parting plane   
            
         
        """
        pass
    @property
    def ExtrudeBiDirectionFlag(self) -> bool:
        """
        Getter for property: (bool) ExtrudeBiDirectionFlag
         Returns the extrude along vector bi-direction flag   
            
         
        """
        pass
    @ExtrudeBiDirectionFlag.setter
    def ExtrudeBiDirectionFlag(self, extBiDirection: bool):
        """
        Setter for property: (bool) ExtrudeBiDirectionFlag
         Returns the extrude along vector bi-direction flag   
            
         
        """
        pass
    @property
    def ExtrudeDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ExtrudeDirection
         Returns the extrude along vector   
            
         
        """
        pass
    @ExtrudeDirection.setter
    def ExtrudeDirection(self, extDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ExtrudeDirection
         Returns the extrude along vector   
            
         
        """
        pass
    @property
    def FillBasePlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) FillBasePlane
         Returns the fill base plane   
            
         
        """
        pass
    @FillBasePlane.setter
    def FillBasePlane(self, fillBasePlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) FillBasePlane
         Returns the fill base plane   
            
         
        """
        pass
    @property
    def FillDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) FillDirection
         Returns the fill direction   
            
         
        """
        pass
    @FillDirection.setter
    def FillDirection(self, fillDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) FillDirection
         Returns the fill direction   
            
         
        """
        pass
    @property
    def FillFromDirectionOptions(self) -> ShapeConstraintBuilder.FillFromDirectionType:
        """
        Getter for property: ( ShapeConstraintBuilder.FillFromDirectionType NXOpen.Desi) FillFromDirectionOptions
         Returns the Fill from Direction Options   
            
         
        """
        pass
    @FillFromDirectionOptions.setter
    def FillFromDirectionOptions(self, fillFromDirectionOptions: ShapeConstraintBuilder.FillFromDirectionType):
        """
        Setter for property: ( ShapeConstraintBuilder.FillFromDirectionType NXOpen.Desi) FillFromDirectionOptions
         Returns the Fill from Direction Options   
            
         
        """
        pass
    @property
    def FirstLimitPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) FirstLimitPlane
         Returns the first limit plane for Segmental Rotational Symmetry type   
            
         
        """
        pass
    @FirstLimitPlane.setter
    def FirstLimitPlane(self, firstLimitPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) FirstLimitPlane
         Returns the first limit plane for Segmental Rotational Symmetry type   
            
         
        """
        pass
    @property
    def MaxOverhangAngle(self) -> ShapeConstraintBuilder.MaxOverhangAngleValue:
        """
        Getter for property: ( ShapeConstraintBuilder.MaxOverhangAngleValue NXOpen.Desi) MaxOverhangAngle
         Returns the Max Overhang Angle   
            
         
        """
        pass
    @MaxOverhangAngle.setter
    def MaxOverhangAngle(self, maxOverhangAngle: ShapeConstraintBuilder.MaxOverhangAngleValue):
        """
        Setter for property: ( ShapeConstraintBuilder.MaxOverhangAngleValue NXOpen.Desi) MaxOverhangAngle
         Returns the Max Overhang Angle   
            
         
        """
        pass
    @property
    def MaximumDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumDiameter
         Returns the Maximum Member Size diameter value   
            
         
        """
        pass
    @property
    def MaximumWallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaximumWallThickness
         Returns the Maximum Member Wall Thickness value   
            
         
        """
        pass
    @property
    def MinimumDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumDiameter
         Returns the Minimum Member Size diameter value   
            
         
        """
        pass
    @property
    def MinimumWallThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinimumWallThickness
         Returns the Minimum Member Wall Thickness value   
            
         
        """
        pass
    @property
    def MultiAxisToolingOption(self) -> ShapeConstraintBuilder.MultiAxisToolingType:
        """
        Getter for property: ( ShapeConstraintBuilder.MultiAxisToolingType NXOpen.Desi) MultiAxisToolingOption
         Returns the Multi Axis Tooling Option   
            
         
        """
        pass
    @MultiAxisToolingOption.setter
    def MultiAxisToolingOption(self, multiAxisToolingOption: ShapeConstraintBuilder.MultiAxisToolingType):
        """
        Setter for property: ( ShapeConstraintBuilder.MultiAxisToolingType NXOpen.Desi) MultiAxisToolingOption
         Returns the Multi Axis Tooling Option   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the shape constraint name   
            
         
        """
        pass
    @Name.setter
    def Name(self, shapeConstraintName: str):
        """
        Setter for property: (str) Name
         Returns the shape constraint name   
            
         
        """
        pass
    @property
    def NumberOfSegments(self) -> int:
        """
        Getter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
    @NumberOfSegments.setter
    def NumberOfSegments(self, numberOfSegments: int):
        """
        Setter for property: (int) NumberOfSegments
         Returns the number of segments   
            
         
        """
        pass
    @property
    def OverhangVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) OverhangVector
         Returns the overhang vector   
            
         
        """
        pass
    @OverhangVector.setter
    def OverhangVector(self, overhangVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) OverhangVector
         Returns the overhang vector   
            
         
        """
        pass
    @property
    def PlanarSymmetryInputMode(self) -> ShapeConstraintBuilder.PlanarSymmetryInputOption:
        """
        Getter for property: ( ShapeConstraintBuilder.PlanarSymmetryInputOption NXOpen.Desi) PlanarSymmetryInputMode
         Returns the input mode for planar symmetry    
            
         
        """
        pass
    @PlanarSymmetryInputMode.setter
    def PlanarSymmetryInputMode(self, planarSymmetyrInputMode: ShapeConstraintBuilder.PlanarSymmetryInputOption):
        """
        Setter for property: ( ShapeConstraintBuilder.PlanarSymmetryInputOption NXOpen.Desi) PlanarSymmetryInputMode
         Returns the input mode for planar symmetry    
            
         
        """
        pass
    @property
    def PlanarSymmetryPlane1(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) PlanarSymmetryPlane1
         Returns the first symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    @PlanarSymmetryPlane1.setter
    def PlanarSymmetryPlane1(self, symmetryPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) PlanarSymmetryPlane1
         Returns the first symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    @property
    def PlanarSymmetryPlane2(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) PlanarSymmetryPlane2
         Returns the second symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    @PlanarSymmetryPlane2.setter
    def PlanarSymmetryPlane2(self, symmetryPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) PlanarSymmetryPlane2
         Returns the second symmetry plane for Planar Symmetry type   
            
         
        """
        pass
    @property
    def RevolutionAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) RevolutionAxis
         Returns the Revolve about axis   
            
         
        """
        pass
    @RevolutionAxis.setter
    def RevolutionAxis(self, revolutionAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) RevolutionAxis
         Returns the Revolve about axis   
            
         
        """
        pass
    @property
    def RotationalSymmetryAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) RotationalSymmetryAxis
         Returns the Rotational Symmetry axis   
            
         
        """
        pass
    @RotationalSymmetryAxis.setter
    def RotationalSymmetryAxis(self, symmetryAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) RotationalSymmetryAxis
         Returns the Rotational Symmetry axis   
            
         
        """
        pass
    @property
    def SecondLimitPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SecondLimitPlane
         Returns the first second plane for Segmental Rotational Symmetry type    
            
         
        """
        pass
    @SecondLimitPlane.setter
    def SecondLimitPlane(self, secondLimitPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SecondLimitPlane
         Returns the first second plane for Segmental Rotational Symmetry type    
            
         
        """
        pass
    @property
    def SegmentLimitHelpAxis(self) -> NXOpen.Axis:
        """
        Getter for property: ( NXOpen.Axis) SegmentLimitHelpAxis
         Returns the help axis for Segmental Rotational Symmetry    
            
         
        """
        pass
    @SegmentLimitHelpAxis.setter
    def SegmentLimitHelpAxis(self, helpAxis: NXOpen.Axis):
        """
        Setter for property: ( NXOpen.Axis) SegmentLimitHelpAxis
         Returns the help axis for Segmental Rotational Symmetry    
            
         
        """
        pass
    @property
    def SupportedFaces(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) SupportedFaces
         Returns the supported faces for self supporting   
            
         
        """
        pass
    @property
    def ThroughHoleVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ThroughHoleVector
         Returns the Through Hole vector   
            
         
        """
        pass
    @ThroughHoleVector.setter
    def ThroughHoleVector(self, throughHoleVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ThroughHoleVector
         Returns the Through Hole vector   
            
         
        """
        pass
    @property
    def ToolDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ToolDiameter
         Returns the tool diameter   
            
         
        """
        pass
    @property
    def ToolLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ToolLength
         Returns the tool length   
            
         
        """
        pass
    @property
    def ToolTipAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ToolTipAngle
         Returns the tool tip angle   
            
         
        """
        pass
    @property
    def Type(self) -> ShapeConstraintBuilder.ConstraintType:
        """
        Getter for property: ( ShapeConstraintBuilder.ConstraintType NXOpen.Desi) Type
         Returns the Constraint type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: ShapeConstraintBuilder.ConstraintType):
        """
        Setter for property: ( ShapeConstraintBuilder.ConstraintType NXOpen.Desi) Type
         Returns the Constraint type   
            
         
        """
        pass
    @property
    def UserSetName(self) -> bool:
        """
        Getter for property: (bool) UserSetName
         Returns the user set name flag   
            
         
        """
        pass
    @UserSetName.setter
    def UserSetName(self, userSetName: bool):
        """
        Setter for property: (bool) UserSetName
         Returns the user set name flag   
            
         
        """
        pass
import NXOpen
class ShapeConstraint(NXOpen.NXObject): 
    """ Represents a NXOpen.DesignSimulation.ShapeConstraint for a NXOpen.DesignSimulation.DesignSpace """
    pass
import NXOpen
class StudyBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.DesignSimulation.Study builder
    """
    class AnalysisOption(Enum):
        """
        Members Include: 
         |LinearStatics| 
         |NormalModes| 
         |Thermal| 

        """
        LinearStatics: int
        NormalModes: int
        Thermal: int
        @staticmethod
        def ValueOf(value: int) -> StudyBuilder.AnalysisOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OptimizationObjectiveOption(Enum):
        """
        Members Include: 
         |MinimumMass| 
         |MinimumVolume| 
         |MaximumStiffness| 
         |MaximumFirstFlexibleMode| 

        """
        MinimumMass: int
        MinimumVolume: int
        MaximumStiffness: int
        MaximumFirstFlexibleMode: int
        @staticmethod
        def ValueOf(value: int) -> StudyBuilder.OptimizationObjectiveOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SubcaseSummationOption(Enum):
        """
        Members Include: 
         |Maximum| 
         |Normalized| 

        """
        Maximum: int
        Normalized: int
        @staticmethod
        def ValueOf(value: int) -> StudyBuilder.SubcaseSummationOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnalysisType(self) -> StudyBuilder.AnalysisOption:
        """
        Getter for property: ( StudyBuilder.AnalysisOption NXOpen.Desi) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    @AnalysisType.setter
    def AnalysisType(self, analysisType: StudyBuilder.AnalysisOption):
        """
        Setter for property: ( StudyBuilder.AnalysisOption NXOpen.Desi) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    @property
    def FixedVoxelSize(self) -> bool:
        """
        Getter for property: (bool) FixedVoxelSize
         Returns the control for automatic or user-defined fixed voxel size.  
          
                    Set to false to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to true to use a user-defined fixed value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    @FixedVoxelSize.setter
    def FixedVoxelSize(self, isFixed: bool):
        """
        Setter for property: (bool) FixedVoxelSize
         Returns the control for automatic or user-defined fixed voxel size.  
          
                    Set to false to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to true to use a user-defined fixed value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    @property
    def NumberOfFrequencies(self) -> int:
        """
        Getter for property: (int) NumberOfFrequencies
         Returns the number of frequencies.  
           It has range 1 to 100.  
         
        """
        pass
    @NumberOfFrequencies.setter
    def NumberOfFrequencies(self, numberOfFrequencies: int):
        """
        Setter for property: (int) NumberOfFrequencies
         Returns the number of frequencies.  
           It has range 1 to 100.  
         
        """
        pass
    @property
    def OptimizationObjectiveType(self) -> StudyBuilder.OptimizationObjectiveOption:
        """
        Getter for property: ( StudyBuilder.OptimizationObjectiveOption NXOpen.Desi) OptimizationObjectiveType
         Returns the optimization objective type   
            
         
        """
        pass
    @OptimizationObjectiveType.setter
    def OptimizationObjectiveType(self, optimizationObjectiveType: StudyBuilder.OptimizationObjectiveOption):
        """
        Setter for property: ( StudyBuilder.OptimizationObjectiveOption NXOpen.Desi) OptimizationObjectiveType
         Returns the optimization objective type   
            
         
        """
        pass
    @property
    def ResolutionVoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ResolutionVoxelSize
         Returns the resolution voxel size   
            
         
        """
        pass
    @property
    def StudyName(self) -> str:
        """
        Getter for property: (str) StudyName
         Returns the study name   
            
         
        """
        pass
    @StudyName.setter
    def StudyName(self, studyName: str):
        """
        Setter for property: (str) StudyName
         Returns the study name   
            
         
        """
        pass
    @property
    def StudyQuality(self) -> int:
        """
        Getter for property: (int) StudyQuality
         Returns the study quality.  
           It has range 1 to 9. 
                    value 1 means high quality but could take long time to get ultra fine optimization result;
                    value 9 means low quality and get coarse optimization result.
                  
         
        """
        pass
    @StudyQuality.setter
    def StudyQuality(self, studyQualityFactor: int):
        """
        Setter for property: (int) StudyQuality
         Returns the study quality.  
           It has range 1 to 9. 
                    value 1 means high quality but could take long time to get ultra fine optimization result;
                    value 9 means low quality and get coarse optimization result.
                  
         
        """
        pass
    @property
    def SubcaseSummationType(self) -> StudyBuilder.SubcaseSummationOption:
        """
        Getter for property: ( StudyBuilder.SubcaseSummationOption NXOpen.Desi) SubcaseSummationType
         Returns the subcase summation type   
            
         
        """
        pass
    @SubcaseSummationType.setter
    def SubcaseSummationType(self, subcaseSummationType: StudyBuilder.SubcaseSummationOption):
        """
        Setter for property: ( StudyBuilder.SubcaseSummationOption NXOpen.Desi) SubcaseSummationType
         Returns the subcase summation type   
            
         
        """
        pass
    def SetResolutionVoxelSizeByStudyQuality(self, studyQualityFactor: int) -> None:
        """
         Set resolution voxel size by the given study quality (on a scale of 1 - 9) 
        """
        pass
import NXOpen
class Study(Container): 
    """ Represents a Design Simulation Study """
    @property
    def Active(self) -> bool:
        """
        Getter for property: (bool) Active
         Returns the active state.  
           There should be only one active Study per  NXOpen::Features::TopologyOptimizationFeature 
                    and only one active  NXOpen::GeometricAnalysis::PerformancePredictor  Study per part.   
         
        """
        pass
    @property
    def AnalysisReportSettings(self) -> AnalysisReportSettings:
        """
        Getter for property: ( AnalysisReportSettings NXOpen.Desi) AnalysisReportSettings
         Returns the Analysis Report Settings to be used when publishing a report for this study.  
             
         
        """
        pass
    @property
    def AnalysisType(self) -> StudyBuilder.AnalysisOption:
        """
        Getter for property: ( StudyBuilder.AnalysisOption NXOpen.Desi) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    @AnalysisType.setter
    def AnalysisType(self, type: StudyBuilder.AnalysisOption):
        """
        Setter for property: ( StudyBuilder.AnalysisOption NXOpen.Desi) AnalysisType
         Returns the analysis type   
            
         
        """
        pass
    @property
    def AnalysisTypeDesc(self) -> str:
        """
        Getter for property: (str) AnalysisTypeDesc
         Returns the analysis type description   
            
         
        """
        pass
    @property
    def AutoInferVoxelResolution(self) -> bool:
        """
        Getter for property: (bool) AutoInferVoxelResolution
         Returns the control for automatic or user-defined voxel resolution.  
          
                    Set to TRUE to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to FALSE to use a user-defined fixed resolution value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    @AutoInferVoxelResolution.setter
    def AutoInferVoxelResolution(self, isAutoInferred: bool):
        """
        Setter for property: (bool) AutoInferVoxelResolution
         Returns the control for automatic or user-defined voxel resolution.  
          
                    Set to TRUE to automatically calculate voxel size based on the study quality control and size of selected bodies.
                    Set to FALSE to use a user-defined fixed resolution value for voxel size independent of the size of selected bodies.
                  
         
        """
        pass
    @property
    def NumberOfFrequencies(self) -> int:
        """
        Getter for property: (int) NumberOfFrequencies
         Returns the number of frequencies.  
           It has range 1 to 100.  
         
        """
        pass
    @property
    def OptimizationObjective(self) -> StudyBuilder.OptimizationObjectiveOption:
        """
        Getter for property: ( StudyBuilder.OptimizationObjectiveOption NXOpen.Desi) OptimizationObjective
         Returns the optimization objective type   
            
         
        """
        pass
    @OptimizationObjective.setter
    def OptimizationObjective(self, objective: StudyBuilder.OptimizationObjectiveOption):
        """
        Setter for property: ( StudyBuilder.OptimizationObjectiveOption NXOpen.Desi) OptimizationObjective
         Returns the optimization objective type   
            
         
        """
        pass
    @property
    def ResolutionVoxelSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ResolutionVoxelSize
         Returns the voxel size (resolution); editing the expression value will make  NXOpen::DesignSimulation::Study  results out of date until the analysis or optimization operation is rerun.  
             
         
        """
        pass
    @property
    def StudyQuality(self) -> int:
        """
        Getter for property: (int) StudyQuality
         Returns the study quality or the solution balance factor.  
           The value ranges from 1, for High Accuracy, to 9, for High Performance.   
         
        """
        pass
    @property
    def SubcaseSummation(self) -> StudyBuilder.SubcaseSummationOption:
        """
        Getter for property: ( StudyBuilder.SubcaseSummationOption NXOpen.Desi) SubcaseSummation
         Returns the subcase summation type   
            
         
        """
        pass
    @SubcaseSummation.setter
    def SubcaseSummation(self, subcaseSummation: StudyBuilder.SubcaseSummationOption):
        """
        Setter for property: ( StudyBuilder.SubcaseSummationOption NXOpen.Desi) SubcaseSummation
         Returns the subcase summation type   
            
         
        """
        pass
    def AbortOptimizationProcess(self) -> bool:
        """
         Terminates the optimization process, if any, for this NXOpen.DesignSimulation.Study after it was launched using
                    NXOpen.DesignSimulation.Study.RunOptimization and before the process completes or errors out. Calling this method
                    does not guarantee that the optimization process will indeed terminate; process state is subject to its progress, hardware and software resources,
                    the real time elapsed since it was launched, and other factors. Returns TRUE if the process was previously running and indeed stopped by this method.
                    Aborting the optimization will NOT produce partial results and the optimization cannot be resumed (restarted) after being terminated.
                
         Returns wasAborted (bool): .
        """
        pass
    def CloneAnalysisConstraint(self, existingConstraint: AnalysisConstraint) -> AnalysisConstraint:
        """
         Clones (copies) a NXOpen.DesignSimulation.AnalysisConstraint object and returns the cloned (copied) object if successful. 
         Returns clonedConstraint ( AnalysisConstraint NXOpen.Desi): .
        """
        pass
    def CloneAnalysisLoad(self, existingload: AnalysisLoad) -> AnalysisLoad:
        """
         Clones (copies) a NXOpen.DesignSimulation.AnalysisLoad object and returns the cloned (copied) object if successful. 
         Returns clonedLoad ( AnalysisLoad NXOpen.Desi): .
        """
        pass
    def CloneSubcase(self, existingSubcase: Subcase) -> Subcase:
        """
         Clones (copies) a NXOpen.DesignSimulation.Subcase object and returns the cloned (copied) object if successful. 
         Returns clonedStudy ( Subcase NXOpen.Desi): .
        """
        pass
    def ContinueOptimizationProcess(self) -> bool:
        """
         Resumes the Topology Optimization process, if any, for this NXOpen.DesignSimulation.Study after it was suspended (paused) using
                    NXOpen.DesignSimulation.Study.PauseOptimizationProcess and before the process completes or errors out. Returns TRUE if the process was
                    previously paused and indeed resumed by this method.
                
         Returns wasResumed (bool): .
        """
        pass
    def CreateAnalysisConstraintBuilder(self, constraint: AnalysisConstraint) -> AnalysisConstraintBuilder:
        """
         Creates a NXOpen.DesignSimulation.AnalysisConstraintBuilder 
         Returns builder ( AnalysisConstraintBuilder NXOpen.Desi): .
        """
        pass
    def CreateAnalysisLoadBuilder(self, load: AnalysisLoad) -> AnalysisLoadBuilder:
        """
         Creates a NXOpen.DesignSimulation.AnalysisLoadBuilder 
         Returns builder ( AnalysisLoadBuilder NXOpen.Desi): .
        """
        pass
    def CreateAnalysisReportBuilder(self) -> AnalysisReportBuilder:
        """
         Creates a NXOpen.DesignSimulation.AnalysisReportBuilder. 
         Returns reportBuilder ( AnalysisReportBuilder NXOpen.Desi): .
        """
        pass
    def CreateConnectionBuilder(self, connection: Connection) -> ConnectionBuilder:
        """
         Creates a NXOpen.DesignSimulation.Connection 
         Returns builder ( ConnectionBuilder NXOpen.Desi): .
        """
        pass
    def CreateConstructionBodyBuilder(self, topOptConstructionBody: ConstructionBody) -> ConstructionBodyBuilder:
        """
         Creates a NXOpen.DesignSimulation.ConstructionBodyBuilder that can be used to create one or more NXOpen.DesignSimulation.ConstructionBody objects,
                a single NXOpen.DesignSimulation.ConstructionBodyCollector object, or to edit a single NXOpen.DesignSimulation.ConstructionBody object. 
         Returns builder ( ConstructionBodyBuilder NXOpen.Desi): .
        """
        pass
    def CreateConstructionBodyByFacesBuilder(self, constrBodyByFaces: ConstructionBodyByFaces) -> ConstructionBodyBuilder:
        """
         Creates a NXOpen.DesignSimulation.ConstructionBodyBuilder that can be used to edit a single NXOpen.DesignSimulation.ConstructionBodyByFaces object. 
         Returns builder ( ConstructionBodyBuilder NXOpen.Desi): .
        """
        pass
    def CreateConstructionBodyCollectorBuilder(self, constrBodyCollector: ConstructionBodyCollector) -> ConstructionBodyBuilder:
        """
         Creates a NXOpen.DesignSimulation.ConstructionBodyBuilder that can be used to edit a single NXOpen.DesignSimulation.ConstructionBodyCollector object. 
         Returns builder ( ConstructionBodyBuilder NXOpen.Desi): .
        """
        pass
    def CreateDesignSpaceBuilder(self, designSpace: DesignSpace) -> DesignSpaceBuilder:
        """
         Creates a NXOpen.DesignSimulation.DesignSpaceBuilder 
         Returns builder ( DesignSpaceBuilder NXOpen.Desi): .
        """
        pass
    def CreateEnvironmentLoadBuilder(self) -> EnvironmentLoadBuilder:
        """
         Creates a NXOpen.DesignSimulation.EnvironmentLoadBuilder 
         Returns builder ( EnvironmentLoadBuilder NXOpen.Desi): .
        """
        pass
    def CreateExportToCaeBuilder(self) -> ExportToCaeBuilder:
        """
         Creates a NXOpen.DesignSimulation.ExportToCaeBuilder 
         Returns builder ( ExportToCaeBuilder NXOpen.Desi): .
        """
        pass
    def CreateOptimizationConstraintBuilder(self, optConstraint: OptimizationConstraint) -> OptimizationConstraintBuilder:
        """
         Creates a NXOpen.DesignSimulation.OptimizationConstraintBuilder 
         Returns builder ( OptimizationConstraintBuilder NXOpen.Desi): .
        """
        pass
    def CreateResultMeasureBuilder(self, resultMeasure: ResultMeasure) -> ResultMeasureBuilder:
        """
         Creates a NXOpen.DesignSimulation.ResultMeasureBuilder 
         Returns builder ( ResultMeasureBuilder NXOpen.Desi): .
        """
        pass
    def CreateSceneryBodyBuilder(self, topOptSceneryBody: SceneryBody) -> SceneryBodyBuilder:
        """
         Creates a NXOpen.DesignSimulation.SceneryBody 
         Returns builder ( SceneryBodyBuilder NXOpen.Desi): .
        """
        pass
    def CreateShapeConstraintBuilder(self, topOptShapeConstraint: ShapeConstraint) -> ShapeConstraintBuilder:
        """
         Creates a NXOpen.DesignSimulation.ShapeConstraint 
         Returns builder ( ShapeConstraintBuilder NXOpen.Desi): .
        """
        pass
    def CreateSubcaseManager(self) -> SubcaseManager:
        """
         Creates a NXOpen.DesignSimulation.SubcaseManager 
         Returns builder ( SubcaseManager NXOpen.Desi): .
        """
        pass
    def DiscardOptimizationResults(self) -> None:
        """
         Discards optimization results and the optimized bodies for this NXOpen.DesignSimulation.Study if the topology optimization was previous executed. 
        """
        pass
    def DiscardUnretrievedOptimizationResults(self) -> None:
        """
         Delete optimization results from a completed optimization process instead of loading them into this NXOpen.DesignSimulation.Study.
                    This method follows NXOpen.DesignSimulation.Study.RunOptimization and will wait for topology optimization process to complete.
                    Use NXOpen.DesignSimulation.Study.AbortOptimizationProcess to terminate a running optimization process and delete in-process results.
                    The owning NXOpen.Features.TopologyOptimizationFeature should be active (i.e. not suppressed) before calling this method.
                
        """
        pass
    def FinishOptimizationProcess(self) -> bool:
        """
         Stops and finishes the optimization process for this NXOpen.DesignSimulation.Study after it was launched using
                    NXOpen.DesignSimulation.Study.RunOptimization and before the optimization has converged or completed.
                    The optimization process will attempt to produce partial results before terminating. The optimization cannot be resumed (restarted) after
                    it has been stopped and optimization results have been loaded. Calling this method does not guarantee that the optimization process will
                    produce partial results or that the optimization results will comply with optimization and shape constraints or even meet quality expectations.
                    Returns TRUE if the process was previously running and stopped by this method to produce partial results.
                
         Returns finished (bool): .
        """
        pass
    def GetAllAnalysisBodies(self) -> List[AnalysisBody]:
        """
         Gets all NXOpen.DesignSimulation.AnalysisBody objects from a NXOpen.DesignSimulation.Study. 
                    These are NXOpen.DesignSimulation.DesignSpace and NXOpen.DesignSimulation.SceneryBody which are
                    directly referenced by the NXOpen.DesignSimulation.Study. 
         Returns bodies ( AnalysisBody List[NXOpen.De): .
        """
        pass
    def GetAllAnalysisConstraints(self) -> List[AnalysisConstraint]:
        """
         Gets all NXOpen.DesignSimulation.AnalysisConstraint objects from the given NXOpen.DesignSimulation.Study. 
         Returns analysisConstraints ( AnalysisConstraint List[NXOpen.De): .
        """
        pass
    def GetAllAnalysisLoads(self) -> List[AnalysisLoad]:
        """
         Gets all NXOpen.DesignSimulation.AnalysisLoad objects from the given NXOpen.DesignSimulation.Study. 
         Returns analysisLoads ( AnalysisLoad List[NXOpen.De): .
        """
        pass
    def GetAllConnections(self) -> List[Connection]:
        """
         Gets all NXOpen.DesignSimulation.Connection objects from the given NXOpen.DesignSimulation.Study. 
         Returns topOptConnections ( Connection List[NXOpen.De): .
        """
        pass
    def GetAllDesignSpaces(self) -> List[DesignSpace]:
        """
         Gets all NXOpen.DesignSimulation.DesignSpace objects from the NXOpen.DesignSimulation.Study. 
         Returns designSpaces ( DesignSpace List[NXOpen.De): .
        """
        pass
    def GetAllEnvironmentLoads(self) -> List[NXOpen.NXObject]:
        """
         Gets all environment load objects from the given NXOpen.DesignSimulation.Study.
                    NXOpen.DesignSimulation.Acceleration as Gravity is the only environment load currently. 
         Returns loads ( NXOpen.NXObject Li): .
        """
        pass
    def GetAllOptimizationConstraints(self) -> List[OptimizationConstraint]:
        """
         Gets all NXOpen.DesignSimulation.OptimizationConstraint objects from the given NXOpen.DesignSimulation.Study. 
         Returns optimizationConstraints ( OptimizationConstraint List[NXOpen.De): .
        """
        pass
    def GetAllResultMeasures(self) -> List[ResultMeasure]:
        """
         Gets all NXOpen.DesignSimulation.ResultMeasure objects from the given NXOpen.DesignSimulation.Study. 
         Returns resultMeasures ( ResultMeasure List[NXOpen.De): .
        """
        pass
    def GetAllSceneryBodies(self) -> List[SceneryBody]:
        """
         Gets all NXOpen.DesignSimulation.SceneryBody objects from the given NXOpen.DesignSimulation.Study.. 
         Returns topOptSceneryBodies ( SceneryBody List[NXOpen.De): .
        """
        pass
    def GetAllSubcases(self) -> List[Subcase]:
        """
         Gets all NXOpen.DesignSimulation.Subcase objects from the given NXOpen.DesignSimulation.Study. 
         Returns subcases ( Subcase List[NXOpen.De): .
        """
        pass
    def GetOptimizedBodies(self) -> List[NXOpen.Body]:
        """
         Get optimized bodies for this NXOpen.DesignSimulation.Study 
         Returns bodies ( NXOpen.Body Li):  the optimized bodies .
        """
        pass
    def PauseOptimizationProcess(self) -> bool:
        """
         Suspends (pauses) the Topology Optimization process, if any, for this NXOpen.DesignSimulation.Study after it was launched using
                    NXOpen.DesignSimulation.Study.RunOptimization and before the process completes or errors out. Calling this method does not guarantee that the
                    optimization process will indeed be suspended; process state is subject to its progress, hardware and software resources, the real time elapsed since it was launched,
                    and other factors. The optimization process can be resumed (restarted) using NXOpen.DesignSimulation.Study.ContinueOptimizationProcess.
                
         Returns wasPaused (bool): .
        """
        pass
    def RemoveAnalysisResults(self) -> None:
        """
         Remove the analysis results from this NXOpen.DesignSimulation.Study. Optimized bodies, if applicable, will be kept. 
        """
        pass
    def RetrieveOptimizationResults(self) -> None:
        """
         Loads results and the optimized bodies from the optimization into this NXOpen.DesignSimulation.Study when the process has completed. 
                    This method follows NXOpen.DesignSimulation.Study.RunOptimization and will wait for topology optimization process to complete.
                    The owning NXOpen.Features.TopologyOptimizationFeature should be active (i.e. not suppressed) before calling this method.
                
        """
        pass
    def RunAnalysis(self) -> None:
        """
         Analyzes this NXOpen.DesignSimulation.Study if the Performance Predictor analysis is fully setup and ready to analyze.
                    The analysis can be executed independent of the owning NXOpen.GeometricAnalysis.AnalysisObject state. The owning
                    NXOpen.GeometricAnalysis.AnalysisObject could be inactive or delayed for update. This method completes all stages
                    of the CAE analysis in the foreground, i.e. control returns to call only after CAE analysis is done.
                
        """
        pass
    def RunOptimization(self) -> None:
        """
         Optimizes (solves) this NXOpen.DesignSimulation.Study if the optimization is fully setup and ready to optimize.
                    The optimization (solve) can be executed independent of the owning NXOpen.Features.TopologyOptimizationFeature state.
                    The owning NXOpen.Features.TopologyOptimizationFeature could be suppressed or delayed for update.
                    This method will return aftering pre-processing and launching the optimization process to run independent of the NX session. In other words, the
                    method will not wait for the topology optimization process to complete.
                    Optimization results from the solve need to be loaded into the NXOpen.DesignSimulation.Study object by calling
                    NXOpen.DesignSimulation.Study.RetrieveOptimizationResults.
                
        """
        pass
    def Unlock(self) -> None:
        """
         Unlocks the NXOpen.DesignSimulation.Study if it is read-only. This method can be used to make a NXOpen.DesignSimulation.Study
                    editable if optimization results could not be loaded due to errors or due to missing data. Use NXOpen.DesignSimulation.Study.AbortOptimizationProcess to
                    terminate a running optimization process or NXOpen.DesignSimulation.Study.DiscardUnretrievedOptimizationResults to delete results instead of loading them.
                    The owning NXOpen.Features.TopologyOptimizationFeature should be active (i.e. not suppressed) before calling this method.
                
        """
        pass
import NXOpen
class SubcaseItemList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[SubcaseItem]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: SubcaseItem) -> None:
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
    def Erase(self, obj: SubcaseItem) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: SubcaseItem, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: SubcaseItem) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> SubcaseItem:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( SubcaseItem NXOpen.Desi):  object found at input index .
        """
        pass
    def GetContents(self) -> List[SubcaseItem]:
        """
         Gets the contents of the entire list 
         Returns objects ( SubcaseItem List[NXOpen.De):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: SubcaseItem) -> None:
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
    def SetContents(self, objects: List[SubcaseItem]) -> None:
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
    def Swap(self, object1: SubcaseItem, object2: SubcaseItem) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class SubcaseItem(NXOpen.TaggedObject): 
    """
    Represents a NXOpen.DesignSimulation.SubcaseItem list item
    """
    class ItemType(Enum):
        """
        Members Include: 
         |Load| 
         |Constraint| 

        """
        Load: int
        Constraint: int
        @staticmethod
        def ValueOf(value: int) -> SubcaseItem.ItemType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IncludedInOptimization(self) -> bool:
        """
        Getter for property: (bool) IncludedInOptimization
         Returns the flag indicating whether a subcase is included in Optimization   
            
         
        """
        pass
    @IncludedInOptimization.setter
    def IncludedInOptimization(self, includedInOptimization: bool):
        """
        Setter for property: (bool) IncludedInOptimization
         Returns the flag indicating whether a subcase is included in Optimization   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the current subcase name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the current subcase name   
            
         
        """
        pass
    def AddReference(self, reference: NXOpen.NXObject) -> None:
        """
         Enable a Loadconstraint
        """
        pass
    def RemoveReference(self, reference: NXOpen.NXObject) -> None:
        """
         Disable a Loadconstraint
        """
        pass
import NXOpen
class SubcaseManager(NXOpen.Builder): 
    """
    A class which defines the Subcase Manager for Topology Optimization
    """
    @property
    def SubcaseList(self) -> SubcaseItemList:
        """
        Getter for property: ( SubcaseItemList NXOpen.Desi) SubcaseList
         Returns a list of subcases in a specific Topology Optimization Study   
            
         
        """
        pass
    def CreateSubcase(self) -> SubcaseItem:
        """
         Creates a Subcase item builder
         Returns item ( SubcaseItem NXOpen.Desi): .
        """
        pass
import NXOpen
class Subcase(Container): 
    """ Represents a Design Simulation Subcase """
    class IncludeInOptimization(Enum):
        """
        Members Include: 
         |TrueValue| 
         |FalseValue| 

        """
        TrueValue: int
        FalseValue: int
        @staticmethod
        def ValueOf(value: int) -> Subcase.IncludeInOptimization:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IsIncludedInOptimization(self) -> Subcase.IncludeInOptimization:
        """
        Getter for property: ( Subcase.IncludeInOptimization NXOpen.Desi) IsIncludedInOptimization
         Returns the Included in optimization flag  
            
         
        """
        pass
    @IsIncludedInOptimization.setter
    def IsIncludedInOptimization(self, isIncludedInOptimization: Subcase.IncludeInOptimization):
        """
        Setter for property: ( Subcase.IncludeInOptimization NXOpen.Desi) IsIncludedInOptimization
         Returns the Included in optimization flag  
            
         
        """
        pass
    def AddReference(self, reference: NXOpen.NXObject) -> None:
        """
        Add reference to a NXOpen.DesignSimulation.AnalysisLoad or NXOpen.DesignSimulation.AnalysisConstraint to the NXOpen.DesignSimulation.Subcase.
        """
        pass
    def GetReferences(self) -> List[NXOpen.NXObject]:
        """
         Get all NXOpen.DesignSimulation.AnalysisLoad or NXOpen.DesignSimulation.AnalysisConstraint in this NXOpen.DesignSimulation.Subcase.
         Returns references ( NXOpen.NXObject Li): .
        """
        pass
    def RemoveReference(self, reference: NXOpen.NXObject) -> None:
        """
        Remove a NXOpen.DesignSimulation.AnalysisLoad or NXOpen.DesignSimulation.AnalysisConstraint from the NXOpen.DesignSimulation.Subcase.
        """
        pass
import NXOpen
class Temperature(NXOpen.NXObject): 
    """ Represents an Temperature type constraint in the NXOpen.DesignSimulation.Study context. """
    @property
    def ReferenceTemperature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ReferenceTemperature
         Returns the ambient temperature magnitude   
            
         
        """
        pass
import NXOpen
class ViewContourBuilder(NXOpen.Builder): 
    """
    Represents a builder to specify contour display settings and plot contours according to the settings
    """
    class ColorDisplayStyleOption(Enum):
        """
        Members Include: 
         |Default| 
         |Spotlight| 
         |MaterialLimit| 

        """
        Default: int
        Spotlight: int
        MaterialLimit: int
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ColorDisplayStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColorScaleRangeOption(Enum):
        """
        Members Include: 
         |PerView| 
         |CommonAcrossViews| 

        """
        PerView: int
        CommonAcrossViews: int
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ColorScaleRangeOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ContourDisplayStyleOption(Enum):
        """
        Members Include: 
         |Smooth| 
         |Banded| 

        """
        Smooth: int
        Banded: int
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ContourDisplayStyleOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplayOption(Enum):
        """
        Members Include: 
         |Single| 
         |Comparison| 

        """
        Single: int
        Comparison: int
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.DisplayOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MaterialLimitOption(Enum):
        """
        Members Include: 
         |AnalysisBody| 
         |Material| 
         |UserDefined| 

        """
        AnalysisBody: int
        Material: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.MaterialLimitOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ResultComponentOption(Enum):
        """
        Members Include: 
         |DisplacementMagnitude| 
         |DisplacementWorstInXYZ| 
         |DisplacementX| 
         |DisplacementY| 
         |DisplacementZ| 
         |DisplacementAll|  Displacement All includes Worst in XYZ, X, Y and Z
         |StressVonMises| 
         |StressWorstPrincipal| 
         |SafetyFactor| 

        """
        DisplacementMagnitude: int
        DisplacementWorstInXYZ: int
        DisplacementX: int
        DisplacementY: int
        DisplacementZ: int
        DisplacementAll: int
        StressVonMises: int
        StressWorstPrincipal: int
        SafetyFactor: int
        @staticmethod
        def ValueOf(value: int) -> ViewContourBuilder.ResultComponentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorDisplayStyle(self) -> ViewContourBuilder.ColorDisplayStyleOption:
        """
        Getter for property: ( ViewContourBuilder.ColorDisplayStyleOption NXOpen.Desi) ColorDisplayStyle
         Returns the color display style   
            
         
        """
        pass
    @ColorDisplayStyle.setter
    def ColorDisplayStyle(self, colorDisplayStyle: ViewContourBuilder.ColorDisplayStyleOption):
        """
        Setter for property: ( ViewContourBuilder.ColorDisplayStyleOption NXOpen.Desi) ColorDisplayStyle
         Returns the color display style   
            
         
        """
        pass
    @property
    def ColorScaleRangeType(self) -> ViewContourBuilder.ColorScaleRangeOption:
        """
        Getter for property: ( ViewContourBuilder.ColorScaleRangeOption NXOpen.Desi) ColorScaleRangeType
         Returns the color scale range type.  
           This option is only available for multiple contours display like comparison report, single report with specified
                  DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll     
         
        """
        pass
    @ColorScaleRangeType.setter
    def ColorScaleRangeType(self, colorScaleRangeOption: ViewContourBuilder.ColorScaleRangeOption):
        """
        Setter for property: ( ViewContourBuilder.ColorScaleRangeOption NXOpen.Desi) ColorScaleRangeType
         Returns the color scale range type.  
           This option is only available for multiple contours display like comparison report, single report with specified
                  DesignSimulation::ViewContourBuilder::ResultComponentOption::DisplacementAll     
         
        """
        pass
    @property
    def ContourDisplayStyle(self) -> ViewContourBuilder.ContourDisplayStyleOption:
        """
        Getter for property: ( ViewContourBuilder.ContourDisplayStyleOption NXOpen.Desi) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    @ContourDisplayStyle.setter
    def ContourDisplayStyle(self, contourDisplayStyle: ViewContourBuilder.ContourDisplayStyleOption):
        """
        Setter for property: ( ViewContourBuilder.ContourDisplayStyleOption NXOpen.Desi) ContourDisplayStyle
         Returns the contour display style   
            
         
        """
        pass
    @property
    def DisplayType(self) -> ViewContourBuilder.DisplayOption:
        """
        Getter for property: ( ViewContourBuilder.DisplayOption NXOpen.Desi) DisplayType
         Returns the display type choice   
            
         
        """
        pass
    @DisplayType.setter
    def DisplayType(self, displayType: ViewContourBuilder.DisplayOption):
        """
        Setter for property: ( ViewContourBuilder.DisplayOption NXOpen.Desi) DisplayType
         Returns the display type choice   
            
         
        """
        pass
    @property
    def FirstStudy(self) -> Study:
        """
        Getter for property: ( Study NXOpen.Desi) FirstStudy
         Returns the first study choice   
            
         
        """
        pass
    @FirstStudy.setter
    def FirstStudy(self, study: Study):
        """
        Setter for property: ( Study NXOpen.Desi) FirstStudy
         Returns the first study choice   
            
         
        """
        pass
    @property
    def Material(self) -> NXOpen.Material:
        """
        Getter for property: ( NXOpen.Material) Material
         Returns the Material used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material     
            
         
        """
        pass
    @Material.setter
    def Material(self, assignedMaterial: NXOpen.Material):
        """
        Setter for property: ( NXOpen.Material) Material
         Returns the Material used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::Material     
            
         
        """
        pass
    @property
    def MaterialLimit(self) -> ViewContourBuilder.MaterialLimitOption:
        """
        Getter for property: ( ViewContourBuilder.MaterialLimitOption NXOpen.Desi) MaterialLimit
         Returns the Material Limit Option   
            
         
        """
        pass
    @MaterialLimit.setter
    def MaterialLimit(self, materialLimitOption: ViewContourBuilder.MaterialLimitOption):
        """
        Setter for property: ( ViewContourBuilder.MaterialLimitOption NXOpen.Desi) MaterialLimit
         Returns the Material Limit Option   
            
         
        """
        pass
    @property
    def MaterialLimitBody(self) -> AnalysisBody:
        """
        Getter for property: ( AnalysisBody NXOpen.Desi) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody     
            
         
        """
        pass
    @MaterialLimitBody.setter
    def MaterialLimitBody(self, body: AnalysisBody):
        """
        Setter for property: ( AnalysisBody NXOpen.Desi) MaterialLimitBody
         Returns the Analysis Body used when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::AnalysisBody     
            
         
        """
        pass
    @property
    def MaxStressCompression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxStressCompression
         Returns the Max Stress Compression expression used for Stress Worst Principal when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined     
            
         
        """
        pass
    @property
    def MaxStressTension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxStressTension
         Returns the Max Stress Tension expression used for Stress Worst Principal when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined     
            
         
        """
        pass
    @property
    def ResultComponentType(self) -> ViewContourBuilder.ResultComponentOption:
        """
        Getter for property: ( ViewContourBuilder.ResultComponentOption NXOpen.Desi) ResultComponentType
         Returns the result component type   
            
         
        """
        pass
    @ResultComponentType.setter
    def ResultComponentType(self, resultComponentType: ViewContourBuilder.ResultComponentOption):
        """
        Setter for property: ( ViewContourBuilder.ResultComponentOption NXOpen.Desi) ResultComponentType
         Returns the result component type   
            
         
        """
        pass
    @property
    def SecondStudy(self) -> Study:
        """
        Getter for property: ( Study NXOpen.Desi) SecondStudy
         Returns the second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    @SecondStudy.setter
    def SecondStudy(self, study: Study):
        """
        Setter for property: ( Study NXOpen.Desi) SecondStudy
         Returns the second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    @property
    def SubcaseIndexForFirstStudy(self) -> int:
        """
        Getter for property: (int) SubcaseIndexForFirstStudy
         Returns the subcase index for first study choice   
            
         
        """
        pass
    @SubcaseIndexForFirstStudy.setter
    def SubcaseIndexForFirstStudy(self, subcaseIndexForFirstStudy: int):
        """
        Setter for property: (int) SubcaseIndexForFirstStudy
         Returns the subcase index for first study choice   
            
         
        """
        pass
    @property
    def SubcaseIndexForSecondStudy(self) -> int:
        """
        Getter for property: (int) SubcaseIndexForSecondStudy
         Returns the subcase index for second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    @SubcaseIndexForSecondStudy.setter
    def SubcaseIndexForSecondStudy(self, subcaseIndexForSecondStudy: int):
        """
        Setter for property: (int) SubcaseIndexForSecondStudy
         Returns the subcase index for second study choice, this choice is available for study comparison case   
            
         
        """
        pass
    @property
    def YieldStrength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YieldStrength
         Returns the Yield Strength expression used for Stress Von Mises when Material Limit is set as
                  DesignSimulation::ViewContourBuilder::MaterialLimitOption::UserDefined     
            
         
        """
        pass
import NXOpen
class ViewportSettingsBuilder(ContourSettingsBuilder): 
    """ Represents a builder for creating viewport settings for the analysis report settings used to publish an analysis report."""
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
          
                    The report writer replaces the text tags having the Viewport Settings Id with an image
                    capturing a contour result created with the Viewport Settings attribute: 
                    Result Component, Contour Style, Color Style, etc.   
         
        """
        pass
    @Id.setter
    def Id(self, id: str):
        """
        Setter for property: (str) Id
         Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
          
                    The report writer replaces the text tags having the Viewport Settings Id with an image
                    capturing a contour result created with the Viewport Settings attribute: 
                    Result Component, Contour Style, Color Style, etc.   
         
        """
        pass
    @property
    def IsAnimatedGif(self) -> bool:
        """
        Getter for property: (bool) IsAnimatedGif
         Returns the animated GIF flag  
            
         
        """
        pass
    @IsAnimatedGif.setter
    def IsAnimatedGif(self, isAnimatedGif: bool):
        """
        Setter for property: (bool) IsAnimatedGif
         Returns the animated GIF flag  
            
         
        """
        pass
    @property
    def ModelingView(self) -> NXOpen.ModelingView:
        """
        Getter for property: ( NXOpen.ModelingView) ModelingView
         Returns the Modeling View  
            
         
        """
        pass
    @ModelingView.setter
    def ModelingView(self, modelingView: NXOpen.ModelingView):
        """
        Setter for property: ( NXOpen.ModelingView) ModelingView
         Returns the Modeling View  
            
         
        """
        pass
import NXOpen
class ViewportSettings(NXOpen.NXObject): 
    """ Represents a Viewport Settings for the Analysis Report Settings used to publish an Analysis Report."""
    @property
    def ColorStyle(self) -> ContourSettingsBuilder.ColorStyleOption:
        """
        Getter for property: ( ContourSettingsBuilder.ColorStyleOption NXOpen.Desi) ColorStyle
         Returns the color style.  
           This option is for different color schema's for highlighting the results ranges.  
         
        """
        pass
    @property
    def ComponentType(self) -> ContourSettingsBuilder.ComponentTypeOption:
        """
        Getter for property: ( ContourSettingsBuilder.ComponentTypeOption NXOpen.Desi) ComponentType
         Returns the component type   
            
         
        """
        pass
    @property
    def ContourStyle(self) -> ContourSettingsBuilder.ContourStyleOption:
        """
        Getter for property: ( ContourSettingsBuilder.ContourStyleOption NXOpen.Desi) ContourStyle
         Returns the contour style   
            
         
        """
        pass
    @property
    def FrequencyIndex(self) -> int:
        """
        Getter for property: (int) FrequencyIndex
         Returns the index of the Frequency to display for Natural Frequencies analysis type.  
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the Viewport Settings Id that uniquely identifies the object in the context of its parent.  
          
                    The report writer replaces the text tags having the Viewport Settings Id with an image
                    capturing a contour result created with the Viewport Settings attribute: 
                    Result Component, Contour Style, Color Style, etc.  
         
        """
        pass
    @property
    def IsAnimatedGif(self) -> bool:
        """
        Getter for property: (bool) IsAnimatedGif
         Returns the animated GIF flag  
            
         
        """
        pass
    @property
    def ModelingView(self) -> NXOpen.ModelingView:
        """
        Getter for property: ( NXOpen.ModelingView) ModelingView
         Returns the Modeling View  
            
         
        """
        pass
    @property
    def ResultType(self) -> ContourSettingsBuilder.ResultTypeOption:
        """
        Getter for property: ( ContourSettingsBuilder.ResultTypeOption NXOpen.Desi) ResultType
         Returns the result type   
            
         
        """
        pass
import NXOpen
class ViewTabularResultBuilder(NXOpen.Builder): 
    """
    Represents a builder to specify tabular result contents and list tabular results according to the contents
    """
    class ReportContentOption(Enum):
        """
        Members Include: 
         |OptimizationObjective| 
         |OptimizationConstraint| 
         |All| 

        """
        OptimizationObjective: int
        OptimizationConstraint: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ViewTabularResultBuilder.ReportContentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Bodies(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Bodies
         Returns the selected solid bodies for scenery bodies or design spaces   
            
         
        """
        pass
    @property
    def ReportContent(self) -> ViewTabularResultBuilder.ReportContentOption:
        """
        Getter for property: ( ViewTabularResultBuilder.ReportContentOption NXOpen.Desi) ReportContent
         Returns the report content choice   
            
         
        """
        pass
    @ReportContent.setter
    def ReportContent(self, reportContent: ViewTabularResultBuilder.ReportContentOption):
        """
        Setter for property: ( ViewTabularResultBuilder.ReportContentOption NXOpen.Desi) ReportContent
         Returns the report content choice   
            
         
        """
        pass
    def GetStudies(self) -> List[Study]:
        """
         Gets the selected studies. 
         Returns studies ( Study List[NXOpen.De): .
        """
        pass
    def SetStudies(self, studies: List[Study]) -> None:
        """
         Sets the selected studies. 
        """
        pass
import NXOpen
class ViewXygraphBuilder(NXOpen.Builder): 
    """
    Represents a builder to draw xygraph for optimization objective or optimization constraint
    """
    class ContentOption(Enum):
        """
        Members Include: 
         |OptimizationObjective| 
         |OptimizationConstraint| 

        """
        OptimizationObjective: int
        OptimizationConstraint: int
        @staticmethod
        def ValueOf(value: int) -> ViewXygraphBuilder.ContentOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def OptimizationConstraint(self) -> OptimizationConstraint:
        """
        Getter for property: ( OptimizationConstraint NXOpen.Desi) OptimizationConstraint
         Returns the optimization constraint.  
          
                
                This property needs to be set when  NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent 
                is  NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint .
                
                  
         
        """
        pass
    @OptimizationConstraint.setter
    def OptimizationConstraint(self, constraint: OptimizationConstraint):
        """
        Setter for property: ( OptimizationConstraint NXOpen.Desi) OptimizationConstraint
         Returns the optimization constraint.  
          
                
                This property needs to be set when  NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent 
                is  NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint .
                
                  
         
        """
        pass
    @property
    def Study(self) -> Study:
        """
        Getter for property: ( Study NXOpen.Desi) Study
         Returns the target study.  
             
         
        """
        pass
    @Study.setter
    def Study(self, study: Study):
        """
        Setter for property: ( Study NXOpen.Desi) Study
         Returns the target study.  
             
         
        """
        pass
    @property
    def SubcaseName(self) -> str:
        """
        Getter for property: (str) SubcaseName
         Returns the corresponding subcase name for optimization constraint.  
          
                
                This property needs to be set when  NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent 
                is  NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint .
                For following constraints, their iterative results are independent on subcase, the subcase name should be set as empty.
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit 
                
                
                
                  
         
        """
        pass
    @SubcaseName.setter
    def SubcaseName(self, subcaseName: str):
        """
        Setter for property: (str) SubcaseName
         Returns the corresponding subcase name for optimization constraint.  
          
                
                This property needs to be set when  NXOpen::DesignSimulation::ViewXygraphBuilder::XygraphContent 
                is  NXOpen::DesignSimulation::ViewXygraphBuilder::ContentOptionOptimizationConstraint .
                For following constraints, their iterative results are independent on subcase, the subcase name should be set as empty.
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMassTarget 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumMassLimit 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumMassLimit 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeFirstFlexibleModeTarget 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMinimumFirstFlexibleModeLimit 
                
                
                 NXOpen::DesignSimulation::OptimizationConstraintBuilder::ConstraintTypeMaximumFirstFlexibleModeLimit 
                
                
                
                  
         
        """
        pass
    @property
    def TargetWindowDevice(self) -> int:
        """
        Getter for property: (int) TargetWindowDevice
         Returns the ID of target window device on which XY graph is displayed.  
          
                
                The window device ID is returned when calling  NXOpen::CAE::Xyplot::WindowManager::NewWindow 
                to create a new graphics window. To get existing window device IDs, call  NXOpen::CAE::Xyplot::WindowManager::GetWindows .
                
                  
         
        """
        pass
    @TargetWindowDevice.setter
    def TargetWindowDevice(self, winDevice: int):
        """
        Setter for property: (int) TargetWindowDevice
         Returns the ID of target window device on which XY graph is displayed.  
          
                
                The window device ID is returned when calling  NXOpen::CAE::Xyplot::WindowManager::NewWindow 
                to create a new graphics window. To get existing window device IDs, call  NXOpen::CAE::Xyplot::WindowManager::GetWindows .
                
                  
         
        """
        pass
    @property
    def XygraphContent(self) -> ViewXygraphBuilder.ContentOption:
        """
        Getter for property: ( ViewXygraphBuilder.ContentOption NXOpen.Desi) XygraphContent
         Returns the xygraph content.  
             
         
        """
        pass
    @XygraphContent.setter
    def XygraphContent(self, xygraphContent: ViewXygraphBuilder.ContentOption):
        """
        Setter for property: ( ViewXygraphBuilder.ContentOption NXOpen.Desi) XygraphContent
         Returns the xygraph content.  
             
         
        """
        pass
