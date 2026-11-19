from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features
class OnestepUnformBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a NXOpen.BodyDes.OnestepUnformBuilder. This allows the creation of an Onestep Unform.
    """
    class Constraint(Enum):
        """
        Members Include: 
         |CurveToCurve| Curve to Curve Constraint, used for intermediate unform only 
         |PointToPoint| Point to Point Constraint, used for complete unform only
         |CurveAlongCurve| Curve along Curve Constraint, used for complete unform only 

        """
        CurveToCurve: int
        PointToPoint: int
        CurveAlongCurve: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Constraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Convergency(Enum):
        """
        Members Include: 
         |Low| Onestep solver convergency level is low
         |Medium| Onestep solver convergency level is medium
         |High| Onestep solver convergency level is high

        """
        Low: int
        Medium: int
        High: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Convergency:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DisplaySpringbackMode(Enum):
        """
        Members Include: 
         |Displacement| Onestep display springback mode is displacement
         |Alongx| Onestep display springback mode is along X
         |Alongy| Onestep display springback mode is along Y
         |Alongz| Onestep display springback mode is along Z

        """
        Displacement: int
        Alongx: int
        Alongy: int
        Alongz: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.DisplaySpringbackMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MeshElement(Enum):
        """
        Members Include: 
         |Triangle| Generate 2D triangle mesh element
         |Quadrate| Generate 2D quadrate mesh element

        """
        Triangle: int
        Quadrate: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.MeshElement:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Object(Enum):
        """
        Members Include: 
         |Solid| solid 
         |Face| face 

        """
        Solid: int
        Face: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Object:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Part(Enum):
        """
        Members Include: 
         |WithAddendum| part with addendum 
         |WithoutAddendum| part without addendum 

        """
        WithAddendum: int
        WithoutAddendum: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Part:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Process(Enum):
        """
        Members Include: 
         |EntireUnform| entire 
         |IntermediateUnform| intermediate 
         |AdvancedUnform| spring back 
         |TrimLine| trim line 

        """
        EntireUnform: int
        IntermediateUnform: int
        AdvancedUnform: int
        TrimLine: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Process:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Surface(Enum):
        """
        Members Include: 
         |Inner| Onestep solver will offset inner surface and enlarge it
         |Middle| Onestep solver will not offset middle surface 
         |Outer| Onestep solver will offset outer surface and shrink it 

        """
        Inner: int
        Middle: int
        Outer: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Surface:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class UnfoldMode(Enum):
        """
        Members Include: 
         |Complete|  Onestep unfold mode is complete 
         |Intermediate|  Onestep unfold mode is intermediate 
         |Trimline|  Onestep unfold mode is trimline
         |Unknown|  Onestep unfold mode is unknown 

        """
        Complete: int
        Intermediate: int
        Trimline: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.UnfoldMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BinderRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) BinderRegion
         Returns the binder region which is a group of faces user chooses as holder.  
             
         
        """
        pass
    @property
    def ConstraintType(self) -> OnestepUnformBuilder.Constraint:
        """
        Getter for property: ( OnestepUnformBuilder.Constraint NXOpen) ConstraintType
         Returns the constraint type for intermediate unform or complete unform.  
             
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraintType: OnestepUnformBuilder.Constraint):
        """
        Setter for property: ( OnestepUnformBuilder.Constraint NXOpen) ConstraintType
         Returns the constraint type for intermediate unform or complete unform.  
             
         
        """
        pass
    @property
    def ContactPointsTolerance(self) -> float:
        """
        Getter for property: (float) ContactPointsTolerance
         Returns the tolerance to find contact points.  
             
         
        """
        pass
    @ContactPointsTolerance.setter
    def ContactPointsTolerance(self, tolerance: float):
        """
        Setter for property: (float) ContactPointsTolerance
         Returns the tolerance to find contact points.  
             
         
        """
        pass
    @property
    def DrawDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DrawDirection
         Returns the draw direction used to define the normal of unform base plane.  
             
         
        """
        pass
    @DrawDirection.setter
    def DrawDirection(self, drawDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DrawDirection
         Returns the draw direction used to define the normal of unform base plane.  
             
         
        """
        pass
    @property
    def Force(self) -> float:
        """
        Getter for property: (float) Force
         Returns the force on blank holder.  
             
         
        """
        pass
    @Force.setter
    def Force(self, force: float):
        """
        Setter for property: (float) Force
         Returns the force on blank holder.  
             
         
        """
        pass
    @property
    def ForceStrength(self) -> float:
        """
        Getter for property: (float) ForceStrength
         Returns the force strength on blank holder.  
             
         
        """
        pass
    @ForceStrength.setter
    def ForceStrength(self, forceStrength: float):
        """
        Setter for property: (float) ForceStrength
         Returns the force strength on blank holder.  
             
         
        """
        pass
    @property
    def InferElementSize(self) -> bool:
        """
        Getter for property: (bool) InferElementSize
         Returns the option to infer 2-D element size.  
           
                If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
         
        """
        pass
    @InferElementSize.setter
    def InferElementSize(self, inforElementSize: bool):
        """
        Setter for property: (bool) InferElementSize
         Returns the option to infer 2-D element size.  
           
                If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
         
        """
        pass
    @property
    def InferThickness(self) -> bool:
        """
        Getter for property: (bool) InferThickness
         Returns the option to infer thickness.  
          
                If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
         
        """
        pass
    @InferThickness.setter
    def InferThickness(self, inferThickness: bool):
        """
        Setter for property: (bool) InferThickness
         Returns the option to infer thickness.  
          
                If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
         
        """
        pass
    @property
    def MatchPointOne(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) MatchPointOne
         Returns the first match point for spring back calculation.  
             
         
        """
        pass
    @MatchPointOne.setter
    def MatchPointOne(self, matchPointOne: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) MatchPointOne
         Returns the first match point for spring back calculation.  
             
         
        """
        pass
    @property
    def MatchPointThree(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) MatchPointThree
         Returns the third match point for spring back calculation.  
             
         
        """
        pass
    @MatchPointThree.setter
    def MatchPointThree(self, matchPointThree: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) MatchPointThree
         Returns the third match point for spring back calculation.  
             
         
        """
        pass
    @property
    def MatchPointTwo(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) MatchPointTwo
         Returns the second match point for spring back calculation.  
             
         
        """
        pass
    @MatchPointTwo.setter
    def MatchPointTwo(self, matchPointTwo: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) MatchPointTwo
         Returns the second match point for spring back calculation.  
             
         
        """
        pass
    @property
    def MaterialPropertyDensity(self) -> float:
        """
        Getter for property: (float) MaterialPropertyDensity
         Returns the density of material.  
             
         
        """
        pass
    @MaterialPropertyDensity.setter
    def MaterialPropertyDensity(self, materialPropertyDensity: float):
        """
        Setter for property: (float) MaterialPropertyDensity
         Returns the density of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyE(self) -> float:
        """
        Getter for property: (float) MaterialPropertyE
         Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
             
         
        """
        pass
    @MaterialPropertyE.setter
    def MaterialPropertyE(self, materialPropertyE: float):
        """
        Setter for property: (float) MaterialPropertyE
         Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
             
         
        """
        pass
    @property
    def MaterialPropertyF(self) -> float:
        """
        Getter for property: (float) MaterialPropertyF
         Returns the friction of material.  
             
         
        """
        pass
    @MaterialPropertyF.setter
    def MaterialPropertyF(self, materialPropertyF: float):
        """
        Setter for property: (float) MaterialPropertyF
         Returns the friction of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyInitialStrain(self) -> float:
        """
        Getter for property: (float) MaterialPropertyInitialStrain
         Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
             
         
        """
        pass
    @MaterialPropertyInitialStrain.setter
    def MaterialPropertyInitialStrain(self, materialPropertyInitialStrain: float):
        """
        Setter for property: (float) MaterialPropertyInitialStrain
         Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
             
         
        """
        pass
    @property
    def MaterialPropertyK(self) -> float:
        """
        Getter for property: (float) MaterialPropertyK
         Returns the K(Strength Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyK.setter
    def MaterialPropertyK(self, materialPropertyK: float):
        """
        Setter for property: (float) MaterialPropertyK
         Returns the K(Strength Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyN(self) -> float:
        """
        Getter for property: (float) MaterialPropertyN
         Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
             
         
        """
        pass
    @MaterialPropertyN.setter
    def MaterialPropertyN(self, materialPropertyN: float):
        """
        Setter for property: (float) MaterialPropertyN
         Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
             
         
        """
        pass
    @property
    def MaterialPropertyPoisson(self) -> float:
        """
        Getter for property: (float) MaterialPropertyPoisson
         Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
             
         
        """
        pass
    @MaterialPropertyPoisson.setter
    def MaterialPropertyPoisson(self, materialPropertyPoisson: float):
        """
        Setter for property: (float) MaterialPropertyPoisson
         Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
             
         
        """
        pass
    @property
    def MaterialPropertyR0(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR0
         Returns the r0(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyR0.setter
    def MaterialPropertyR0(self, materialPropertyR0: float):
        """
        Setter for property: (float) MaterialPropertyR0
         Returns the r0(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyR45(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR45
         Returns the r45(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyR45.setter
    def MaterialPropertyR45(self, materialPropertyR45: float):
        """
        Setter for property: (float) MaterialPropertyR45
         Returns the r45(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyR90(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR90
         Returns the r90(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @MaterialPropertyR90.setter
    def MaterialPropertyR90(self, materialPropertyR90: float):
        """
        Setter for property: (float) MaterialPropertyR90
         Returns the r90(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    @property
    def MaterialPropertyYieldStress(self) -> float:
        """
        Getter for property: (float) MaterialPropertyYieldStress
         Returns the yield stress of material.  
             
         
        """
        pass
    @MaterialPropertyYieldStress.setter
    def MaterialPropertyYieldStress(self, materialPropertyYieldStress: float):
        """
        Setter for property: (float) MaterialPropertyYieldStress
         Returns the yield stress of material.  
             
         
        """
        pass
    @property
    def MeshAttemptMapping(self) -> bool:
        """
        Getter for property: (bool) MeshAttemptMapping
         Returns the option to attemp mapping for mesh elements.  
           
                If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
         
        """
        pass
    @MeshAttemptMapping.setter
    def MeshAttemptMapping(self, meshAttemptMapping: bool):
        """
        Setter for property: (bool) MeshAttemptMapping
         Returns the option to attemp mapping for mesh elements.  
           
                If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
         
        """
        pass
    @property
    def MeshElementSize(self) -> float:
        """
        Getter for property: (float) MeshElementSize
         Returns the 2-D element size for mesh.  
             
         
        """
        pass
    @MeshElementSize.setter
    def MeshElementSize(self, meshElementSize: float):
        """
        Setter for property: (float) MeshElementSize
         Returns the 2-D element size for mesh.  
             
         
        """
        pass
    @property
    def MeshElementType(self) -> OnestepUnformBuilder.MeshElement:
        """
        Getter for property: ( OnestepUnformBuilder.MeshElement NXOpen) MeshElementType
         Returns the 2-D mesh element type, either triangle or quadrate element.  
            
         
        """
        pass
    @MeshElementType.setter
    def MeshElementType(self, meshElementType: OnestepUnformBuilder.MeshElement):
        """
        Setter for property: ( OnestepUnformBuilder.MeshElement NXOpen) MeshElementType
         Returns the 2-D mesh element type, either triangle or quadrate element.  
            
         
        """
        pass
    @property
    def MeshMaxJacobian(self) -> float:
        """
        Getter for property: (float) MeshMaxJacobian
         Returns the maximum Jacobian for mesh elements.  
           It is used to control the element shape and quality.   
         
        """
        pass
    @MeshMaxJacobian.setter
    def MeshMaxJacobian(self, meshMaxJacobian: float):
        """
        Setter for property: (float) MeshMaxJacobian
         Returns the maximum Jacobian for mesh elements.  
           It is used to control the element shape and quality.   
         
        """
        pass
    @property
    def MeshMaxWarp(self) -> float:
        """
        Getter for property: (float) MeshMaxWarp
         Returns the maximum warp for meshing.  
             
         
        """
        pass
    @MeshMaxWarp.setter
    def MeshMaxWarp(self, meshMaxWarp: float):
        """
        Setter for property: (float) MeshMaxWarp
         Returns the maximum warp for meshing.  
             
         
        """
        pass
    @property
    def MeshProcessFillet(self) -> bool:
        """
        Getter for property: (bool) MeshProcessFillet
         Returns the option to process fillet for mesh element.  
          
                If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
         
        """
        pass
    @MeshProcessFillet.setter
    def MeshProcessFillet(self, meshProcessFillet: bool):
        """
        Setter for property: (bool) MeshProcessFillet
         Returns the option to process fillet for mesh element.  
          
                If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
         
        """
        pass
    @property
    def MeshSizeVariation(self) -> int:
        """
        Getter for property: (int) MeshSizeVariation
         Returns the variation of mesh element size.  
             
         
        """
        pass
    @MeshSizeVariation.setter
    def MeshSizeVariation(self, meshSizeVariation: int):
        """
        Setter for property: (int) MeshSizeVariation
         Returns the variation of mesh element size.  
             
         
        """
        pass
    @property
    def MeshSmallFeature(self) -> float:
        """
        Getter for property: (float) MeshSmallFeature
         Returns the value of small feature for mesh setting  
            
         
        """
        pass
    @MeshSmallFeature.setter
    def MeshSmallFeature(self, meshSmallFeature: float):
        """
        Setter for property: (float) MeshSmallFeature
         Returns the value of small feature for mesh setting  
            
         
        """
        pass
    @property
    def MeshSplitQuad(self) -> bool:
        """
        Getter for property: (bool) MeshSplitQuad
         Returns the option to split quadrate element to triangle element when creating meshes.  
             
         
        """
        pass
    @MeshSplitQuad.setter
    def MeshSplitQuad(self, meshSplitQuad: bool):
        """
        Setter for property: (bool) MeshSplitQuad
         Returns the option to split quadrate element to triangle element when creating meshes.  
             
         
        """
        pass
    @property
    def ObjectType(self) -> OnestepUnformBuilder.Object:
        """
        Getter for property: ( OnestepUnformBuilder.Object NXOpen) ObjectType
         Returns the object type for onestep unform.  
             
         
        """
        pass
    @ObjectType.setter
    def ObjectType(self, objectType: OnestepUnformBuilder.Object):
        """
        Setter for property: ( OnestepUnformBuilder.Object NXOpen) ObjectType
         Returns the object type for onestep unform.  
             
         
        """
        pass
    @property
    def PartBoundary(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) PartBoundary
         Returns the boundary which is a group of edges user chooses to apply on equivalent force.  
             
         
        """
        pass
    @property
    def PartType(self) -> OnestepUnformBuilder.Part:
        """
        Getter for property: ( OnestepUnformBuilder.Part NXOpen) PartType
         Returns the part type for onestep unform.  
             
         
        """
        pass
    @PartType.setter
    def PartType(self, partType: OnestepUnformBuilder.Part):
        """
        Setter for property: ( OnestepUnformBuilder.Part NXOpen) PartType
         Returns the part type for onestep unform.  
             
         
        """
        pass
    @property
    def Pressure(self) -> float:
        """
        Getter for property: (float) Pressure
         Returns the pressure on blank holder.  
             
         
        """
        pass
    @Pressure.setter
    def Pressure(self, pressure: float):
        """
        Setter for property: (float) Pressure
         Returns the pressure on blank holder.  
             
         
        """
        pass
    @property
    def ProcessType(self) -> OnestepUnformBuilder.Process:
        """
        Getter for property: ( OnestepUnformBuilder.Process NXOpen) ProcessType
         Returns the process type for onestep unform.  
             
         
        """
        pass
    @ProcessType.setter
    def ProcessType(self, processType: OnestepUnformBuilder.Process):
        """
        Setter for property: ( OnestepUnformBuilder.Process NXOpen) ProcessType
         Returns the process type for onestep unform.  
             
         
        """
        pass
    @property
    def ReportDisplayFlattenShape(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayFlattenShape
         Returns the option to display result flatten shape in report.  
          
                If it is true, the report will display the flatten shape result. If it is false, the flatten shape will not be displayed in report.  
         
        """
        pass
    @ReportDisplayFlattenShape.setter
    def ReportDisplayFlattenShape(self, reportDisplayFlattenShape: bool):
        """
        Setter for property: (bool) ReportDisplayFlattenShape
         Returns the option to display result flatten shape in report.  
          
                If it is true, the report will display the flatten shape result. If it is false, the flatten shape will not be displayed in report.  
         
        """
        pass
    @property
    def ReportDisplaySpringback(self) -> bool:
        """
        Getter for property: (bool) ReportDisplaySpringback
         Returns the option to display springback result in report.  
          
                If it is true, the report will display springback result. If it is false, the springback will not be displayed.  
         
        """
        pass
    @ReportDisplaySpringback.setter
    def ReportDisplaySpringback(self, reportDisplaySpringback: bool):
        """
        Setter for property: (bool) ReportDisplaySpringback
         Returns the option to display springback result in report.  
          
                If it is true, the report will display springback result. If it is false, the springback will not be displayed.  
         
        """
        pass
    @property
    def ReportDisplayStrain(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayStrain
         Returns the option to display strain in report.  
          
                If it is true, the report will display strain information. If it is false, the report will not display strain information.  
         
        """
        pass
    @ReportDisplayStrain.setter
    def ReportDisplayStrain(self, reportDisplayStrain: bool):
        """
        Setter for property: (bool) ReportDisplayStrain
         Returns the option to display strain in report.  
          
                If it is true, the report will display strain information. If it is false, the report will not display strain information.  
         
        """
        pass
    @property
    def ReportDisplayStress(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayStress
         Returns the option to display stress in report.  
          
                If it is true, the stress information will be displayed in report. If it is false, the report will not display stress information.  
         
        """
        pass
    @ReportDisplayStress.setter
    def ReportDisplayStress(self, reportDisplayStress: bool):
        """
        Setter for property: (bool) ReportDisplayStress
         Returns the option to display stress in report.  
          
                If it is true, the stress information will be displayed in report. If it is false, the report will not display stress information.  
         
        """
        pass
    @property
    def ReportDisplayThickness(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayThickness
         Returns the option to display thickness information in report.  
          
                If it is true, the thickness information will be displayed in report. If it is false, the report will not display thickness information.  
         
        """
        pass
    @ReportDisplayThickness.setter
    def ReportDisplayThickness(self, reportDisplayThickness: bool):
        """
        Setter for property: (bool) ReportDisplayThickness
         Returns the option to display thickness information in report.  
          
                If it is true, the thickness information will be displayed in report. If it is false, the report will not display thickness information.  
         
        """
        pass
    @property
    def ReportDisplayViewControl(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayViewControl
         Returns the option to control view while creating screen image in report.  
          
                If it is true, customer can control the view when capturing the screen image. If it is false, default view will be used in report.  
         
        """
        pass
    @ReportDisplayViewControl.setter
    def ReportDisplayViewControl(self, reportDisplayViewControl: bool):
        """
        Setter for property: (bool) ReportDisplayViewControl
         Returns the option to control view while creating screen image in report.  
          
                If it is true, customer can control the view when capturing the screen image. If it is false, default view will be used in report.  
         
        """
        pass
    @property
    def ReverseSide(self) -> bool:
        """
        Getter for property: (bool) ReverseSide
         Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
           
                 This option is appliable only in case the following conditions are all satisfied: entire unform to separate target body, Curve to Curve constraint on inner edges.  
         
        """
        pass
    @ReverseSide.setter
    def ReverseSide(self, reverseSide: bool):
        """
        Setter for property: (bool) ReverseSide
         Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
           
                 This option is appliable only in case the following conditions are all satisfied: entire unform to separate target body, Curve to Curve constraint on inner edges.  
         
        """
        pass
    @property
    def SolverConvergencyLevel(self) -> OnestepUnformBuilder.Convergency:
        """
        Getter for property: ( OnestepUnformBuilder.Convergency NXOpen) SolverConvergencyLevel
         Returns the convergency level of onestep solver.  
             
         
        """
        pass
    @SolverConvergencyLevel.setter
    def SolverConvergencyLevel(self, solverConvergencyLevel: OnestepUnformBuilder.Convergency):
        """
        Setter for property: ( OnestepUnformBuilder.Convergency NXOpen) SolverConvergencyLevel
         Returns the convergency level of onestep solver.  
             
         
        """
        pass
    @property
    def SolverDisplaySpringbackMode(self) -> OnestepUnformBuilder.DisplaySpringbackMode:
        """
        Getter for property: ( OnestepUnformBuilder.DisplaySpringbackMode NXOpen) SolverDisplaySpringbackMode
         Returns the option for springback display.  
           
                If it is true, it will display springback in absolution 3D distance, or projecte in xyz directions.  
         
        """
        pass
    @SolverDisplaySpringbackMode.setter
    def SolverDisplaySpringbackMode(self, solverDisplaySpringbackMode: OnestepUnformBuilder.DisplaySpringbackMode):
        """
        Setter for property: ( OnestepUnformBuilder.DisplaySpringbackMode NXOpen) SolverDisplaySpringbackMode
         Returns the option for springback display.  
           
                If it is true, it will display springback in absolution 3D distance, or projecte in xyz directions.  
         
        """
        pass
    @property
    def SolverDoSpringbackCalculation(self) -> bool:
        """
        Getter for property: (bool) SolverDoSpringbackCalculation
         Returns the option to do springback calculation in onestep solver.  
          
                If it is true, the onestep solver will do springback calculation. If it is false, the solver will not do springback calculation.  
         
        """
        pass
    @SolverDoSpringbackCalculation.setter
    def SolverDoSpringbackCalculation(self, solverDoSpringbackCalculation: bool):
        """
        Setter for property: (bool) SolverDoSpringbackCalculation
         Returns the option to do springback calculation in onestep solver.  
          
                If it is true, the onestep solver will do springback calculation. If it is false, the solver will not do springback calculation.  
         
        """
        pass
    @property
    def SolverJoinOutputCurves(self) -> bool:
        """
        Getter for property: (bool) SolverJoinOutputCurves
         Returns the option to join output curves.  
          
                If it is true, join output curves. If it is false, do not join output curves  
         
        """
        pass
    @SolverJoinOutputCurves.setter
    def SolverJoinOutputCurves(self, solverJoinOutputCurves: bool):
        """
        Setter for property: (bool) SolverJoinOutputCurves
         Returns the option to join output curves.  
          
                If it is true, join output curves. If it is false, do not join output curves  
         
        """
        pass
    @property
    def SolverMaxIterationSteps(self) -> int:
        """
        Getter for property: (int) SolverMaxIterationSteps
         Returnsthe maximum number of iteration steps in onestep solver.  
             
         
        """
        pass
    @SolverMaxIterationSteps.setter
    def SolverMaxIterationSteps(self, solverMaxIterationSteps: int):
        """
        Setter for property: (int) SolverMaxIterationSteps
         Returnsthe maximum number of iteration steps in onestep solver.  
             
         
        """
        pass
    @property
    def SolverSaveAnalysisResultsIntoFeature(self) -> bool:
        """
        Getter for property: (bool) SolverSaveAnalysisResultsIntoFeature
         Returns the option to save analysis result into feature.  
          
                If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
         
        """
        pass
    @SolverSaveAnalysisResultsIntoFeature.setter
    def SolverSaveAnalysisResultsIntoFeature(self, solverSaveAnalysisResultsIntoFeature: bool):
        """
        Setter for property: (bool) SolverSaveAnalysisResultsIntoFeature
         Returns the option to save analysis result into feature.  
          
                If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
         
        """
        pass
    @property
    def SurfaceType(self) -> OnestepUnformBuilder.Surface:
        """
        Getter for property: ( OnestepUnformBuilder.Surface NXOpen) SurfaceType
         Returns the surface type used to determine offset direction.  
             
         
        """
        pass
    @SurfaceType.setter
    def SurfaceType(self, surfaceType: OnestepUnformBuilder.Surface):
        """
        Setter for property: ( OnestepUnformBuilder.Surface NXOpen) SurfaceType
         Returns the surface type used to determine offset direction.  
             
         
        """
        pass
    @property
    def TargetRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) TargetRegion
         Returns the target region which is a group of faces user chooses to unfrom to.  
             
         
        """
        pass
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of sheet metal model.  
             
         
        """
        pass
    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of sheet metal model.  
             
         
        """
        pass
    @property
    def ThicknessDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ThicknessDirection
         Returns the thickness direction used to define the direction of product thickness at the specific point in trimline.  
            
         
        """
        pass
    @ThicknessDirection.setter
    def ThicknessDirection(self, thicknessDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ThicknessDirection
         Returns the thickness direction used to define the direction of product thickness at the specific point in trimline.  
            
         
        """
        pass
    @property
    def TrimlinePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TrimlinePoint
         Returns the point where the thickness direction is defined for trimline.  
             
         
        """
        pass
    @TrimlinePoint.setter
    def TrimlinePoint(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TrimlinePoint
         Returns the point where the thickness direction is defined for trimline.  
             
         
        """
        pass
    @property
    def UnfoldModeType(self) -> OnestepUnformBuilder.UnfoldMode:
        """
        Getter for property: ( OnestepUnformBuilder.UnfoldMode NXOpen) UnfoldModeType
         Returns the onestep unfold mode.  
             
         
        """
        pass
    @UnfoldModeType.setter
    def UnfoldModeType(self, unfoldModeType: OnestepUnformBuilder.UnfoldMode):
        """
        Setter for property: ( OnestepUnformBuilder.UnfoldMode NXOpen) UnfoldModeType
         Returns the onestep unfold mode.  
             
         
        """
        pass
    @property
    def UnfoldSolid(self) -> NXOpen.Body:
        """
        Getter for property: ( NXOpen.Body) UnfoldSolid
         Returns the solid body to unform.  
             
         
        """
        pass
    @UnfoldSolid.setter
    def UnfoldSolid(self, unfoldSolidTag: NXOpen.Body):
        """
        Setter for property: ( NXOpen.Body) UnfoldSolid
         Returns the solid body to unform.  
             
         
        """
        pass
    @property
    def UnfoldSolidRegion(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: ( NXOpen.SelectBodyList) UnfoldSolidRegion
         Returns the unfold solid regions which are a group of faces user chooses to unform.  
             
         
        """
        pass
    @property
    def UnformRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: ( NXOpen.ScCollector) UnformRegion
         Returns the unform region which is a group of faces user chooses to unform.  
             
         
        """
        pass
    @property
    def UnformSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) UnformSection
         Returns the unform section which includes a group of user selected points or curves.  
             
         
        """
        pass
    @UnformSection.setter
    def UnformSection(self, unformsection: NXOpen.Section):
        """
        Setter for property: ( NXOpen.Section) UnformSection
         Returns the unform section which includes a group of user selected points or curves.  
             
         
        """
        pass
    def Calculation(self) -> None:
        """
         Starts solver to calculate. 
        """
        pass
    def Constructor(self, tOnestepSolverType: int) -> None:
        """
         Constructs solver to prepare the data. 
        """
        pass
    def CreateSheetBody(self, readResultFromFeature: bool) -> None:
        """
         Creates unform sheet body result. 
        """
        pass
    def DeleteOffsetSheetBody(self) -> None:
        """
         Deletes the offset body when the object type is body. 
        """
        pass
    def Destructor(self) -> None:
        """
         Destructs solver to release the data. 
        """
        pass
    def DisplayProfile(self, readResultFromFeature: bool) -> None:
        """
         Displays profile result. 
        """
        pass
    def GetBlankShape(self) -> List[float]:
        """
         Gets the blank result nodes. 
         Returns nodes (List[float]): .
        """
        pass
    def GetBorderLoops(self) -> Tuple[List[int], List[int]]:
        """
         Gets the boundary loop IDs.
         Returns A tuple consisting of (index, nodeIdentifications). 
         - index is: List[int].
         - nodeIdentifications is: List[int].

        """
        pass
    def GetBottomSurfaceStrain(self) -> List[float]:
        """
         Gets the bottom surface strain result. 
         Returns nodes (List[float]): .
        """
        pass
    def GetBottomSurfaceStress(self) -> List[float]:
        """
         Gets the bottom surface stress result. 
         Returns nodes (List[float]): .
        """
        pass
    def GetContactNodeIds(self) -> List[int]:
        """
         Gets the element node IDs where the product face meshes and addendum faces mesh are contacting within the given tolerance. 
         Returns id (List[int]): .
        """
        pass
    def GetMeshes(self) -> Tuple[List[float], List[int], List[int]]:
        """
         Gets the mesh element data. 
         Returns A tuple consisting of (vnode, constraint_id, element). 
         - vnode is: List[float].
         - constraint_id is: List[int].
         - element is: List[int].

        """
        pass
    def GetMinNodeID(self) -> int:
        """
         Gets the minimum node ID. 
         Returns min_id (int): .
        """
        pass
    def GetNodeIdsOnFreeEdge(self) -> Tuple[List[int], List[int]]:
        """
         Gets the node IDs on the free edges (non-constrainted boundary edges). 
         Returns A tuple consisting of (index, nodeIdentifications). 
         - index is: List[int].
         - nodeIdentifications is: List[int].

        """
        pass
    def GetRefNode(self) -> int:
        """
         Gets the reference node ID. 
         Returns eid (int): .
        """
        pass
    def GetSolverType(self) -> int:
        """
         Gets the solver calculation type. 
         Returns tOnestepSolverType (int): .
        """
        pass
    def GetSpringbackShape(self) -> List[float]:
        """
         Gets the springbrack result. 
         Returns nodes (List[float]): .
        """
        pass
    def GetStrain(self) -> List[float]:
        """
         Gets the strain result. 
         Returns strains (List[float]): .
        """
        pass
    def GetStress(self) -> List[float]:
        """
         Gets the stress result. 
         Returns stress (List[float]): .
        """
        pass
    @overload
    def GetThickness(self) -> List[float]:
        """
         Gets Thickness. 
         Returns thickness (List[float]): .
        """
        pass
    def GetTopSurfaceStrain(self) -> List[float]:
        """
         Gets the top surface strain result. 
         Returns nodes (List[float]): .
        """
        pass
    def GetTopSurfaceStress(self) -> List[float]:
        """
         Gets the top surface stress result. 
         Returns nodes (List[float]): .
        """
        pass
    def IsResultExist(self) -> None:
        """
         Checks whether the result is available or not.
        """
        pass
    def Mesh(self) -> None:
        """
         Create FEM 2-D meshes based on the unform region surfaces and the target region surfaces.
        """
        pass
    def OnestepUnformRegisterProjectCallback(self) -> None:
        """
         Register the callback to solver.
        """
        pass
    def SetAdvancedConstraintInformation(self, advancedConstraintPartType: int, blankHolderWithAddendumBinderRegion: List[NXOpen.TaggedObject], blankHolderWithoutAddendumBoundaryOfPart: List[NXOpen.TaggedObject], blankHolderWithAddendumPressure: float, blankHolderWithAddendumForce: float, blankHolderWithoutAddendumTension: float, blankHolderWithoutAddendumForce: float, blankHolderWithoutAddendumForceStrength: float, drawbeadTag: List[NXOpen.TaggedObject], drawbeadTtension: List[float], drawbeadNtension: List[float], drawbeadForceStrength: List[float]) -> None:
        """
         Set advanced constraint information. 
        """
        pass
    def SetBlankThickness(self, thickness: float) -> None:
        """
         Sets the blank thickness. 
        """
        pass
    def SetBorderInfo(self, edgeTags: List[NXOpen.TaggedObject], nids: List[int], groupInfo: List[int]) -> None:
        """
         Sets the boundary condition information.
        """
        pass
    def SetConstraintInformation(self, noCommonEdges: bool, revisedDirU: List[int], revisedDirT: List[int], index: List[int], constraintType: List[int], cacNumsUnform: List[int], cacNumsTarget: List[int], consCurveFromUnform: List[NXOpen.TaggedObject], consCurveFromTarget: List[NXOpen.TaggedObject], consPointFromUnform: List[NXOpen.Point], consPointFromTarget: List[NXOpen.Point], startPtOfConsCrvsUnform: List[float], startPtOfConsCrvsTarget: List[float]) -> None:
        """
         Set constraint information. 
        """
        pass
    @overload
    def SetDrawDirection(self, tdx: int, tdy: int, tdz: int) -> None:
        """
         Sets the unform draw direction. 
        """
        pass
    def SetFacesOnOffsetSheet(self, unfoldBody: NXOpen.Body) -> bool:
        """
         Sets the offset faces when the object type is body. 
         Returns setMark (bool): .
        """
        pass
    def SetNodeIDsOnFreeEdge(self, index: List[int], nids: List[int]) -> None:
        """
         Sets the node IDs on the free edges (non-constrainted boundary edges). 
        """
        pass
    def SetResultBlankShape(self, blankshape: List[float]) -> None:
        """
         Sets blank shape result. 
        """
        pass
    def SetResultNodesIdsOnProfile(self, nids: List[int]) -> None:
        """
         Sets profile node ID result. 
        """
        pass
    def SetResultNodesNumEachProfileCurve(self, indexs: List[int]) -> None:
        """
         Sets total number of node on each profile. 
        """
        pass
    def SetResultRefNodeId(self, resultRefNodeId: int) -> None:
        """
         Sets reference node ID. 
        """
        pass
    def SetResultSpringBack(self, springback: List[float]) -> None:
        """
         Sets springback result. 
        """
        pass
    def SetResultStrain(self, strain: List[float]) -> None:
        """
         Sets strain result. 
        """
        pass
    def SetResultStress(self, stress: List[float]) -> None:
        """
         Sets stress result. 
        """
        pass
    def SetResultThickness(self, thickness: List[float]) -> None:
        """
         Sets thickness result. 
        """
        pass
    @overload
    def SetSurfaceType(self, tOnestepSolverSurfaceType: int) -> None:
        """
         Sets the unform surface type. 
        """
        pass
    def UpdateInputMeshDataToSolver(self) -> None:
        """
         Updates the mesh elements to solver.
        """
        pass
import NXOpen
import NXOpen.Features
class OnestepUnformCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of OnestepUnform """
    def CreateOnestepBuilder(self, onestepunform: NXOpen.Features.Feature) -> OnestepUnformBuilder:
        """
         Creates an Onestep Unform builder. 
         Returns builder ( OnestepUnformBuilder NXOpen):   OnestepUnformBuilder  object object .
        """
        pass
import NXOpen.Features
class OnestepUnform(NXOpen.Features.Feature): 
    """ Represents a onestep unform feature """
    pass
