from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Features
## 
##     Represents a @link NXOpen::BodyDes::OnestepUnformBuilder NXOpen::BodyDes::OnestepUnformBuilder@endlink . This allows the creation of an Onestep Unform.
##      <br> To create a new instance of this class, use @link NXOpen::BodyDes::OnestepUnformCollection::CreateOnestepBuilder  NXOpen::BodyDes::OnestepUnformCollection::CreateOnestepBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class OnestepUnformBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a <ja_class>NXOpen.BodyDes.OnestepUnformBuilder</ja_class>. This allows the creation of an Onestep Unform.
    """


    ##  The constraints of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CurveToCurve</term><description> 
    ## Curve to Curve Constraint, used for intermediate unform only </description> </item><item><term> 
    ## PointToPoint</term><description> 
    ## Point to Point Constraint, used for complete unform only</description> </item><item><term> 
    ## CurveAlongCurve</term><description> 
    ## Curve along Curve Constraint, used for complete unform only </description> </item></list>
    class Constraint(Enum):
        """
        Members Include: <CurveToCurve> <PointToPoint> <CurveAlongCurve>
        """
        CurveToCurve: int
        PointToPoint: int
        CurveAlongCurve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Constraint:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The solver convergency level of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Low</term><description> 
    ## Onestep solver convergency level is low</description> </item><item><term> 
    ## Medium</term><description> 
    ## Onestep solver convergency level is medium</description> </item><item><term> 
    ## High</term><description> 
    ## Onestep solver convergency level is high</description> </item></list>
    class Convergency(Enum):
        """
        Members Include: <Low> <Medium> <High>
        """
        Low: int
        Medium: int
        High: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Convergency:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The mode of display springback. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Displacement</term><description> 
    ## Onestep display springback mode is displacement</description> </item><item><term> 
    ## Alongx</term><description> 
    ## Onestep display springback mode is along X</description> </item><item><term> 
    ## Alongy</term><description> 
    ## Onestep display springback mode is along Y</description> </item><item><term> 
    ## Alongz</term><description> 
    ## Onestep display springback mode is along Z</description> </item></list>
    class DisplaySpringbackMode(Enum):
        """
        Members Include: <Displacement> <Alongx> <Alongy> <Alongz>
        """
        Displacement: int
        Alongx: int
        Alongy: int
        Alongz: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.DisplaySpringbackMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The 2-D mesh element type of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Triangle</term><description> 
    ## Generate 2D triangle mesh element</description> </item><item><term> 
    ## Quadrate</term><description> 
    ## Generate 2D quadrate mesh element</description> </item></list>
    class MeshElement(Enum):
        """
        Members Include: <Triangle> <Quadrate>
        """
        Triangle: int
        Quadrate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.MeshElement:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The object types of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Solid</term><description> 
    ## solid </description> </item><item><term> 
    ## Face</term><description> 
    ## face </description> </item></list>
    class Object(Enum):
        """
        Members Include: <Solid> <Face>
        """
        Solid: int
        Face: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Object:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The part types of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## WithAddendum</term><description> 
    ## part with addendum </description> </item><item><term> 
    ## WithoutAddendum</term><description> 
    ## part without addendum </description> </item></list>
    class Part(Enum):
        """
        Members Include: <WithAddendum> <WithoutAddendum>
        """
        WithAddendum: int
        WithoutAddendum: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Part:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The process types of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EntireUnform</term><description> 
    ## entire </description> </item><item><term> 
    ## IntermediateUnform</term><description> 
    ## intermediate </description> </item><item><term> 
    ## AdvancedUnform</term><description> 
    ## spring back </description> </item><item><term> 
    ## TrimLine</term><description> 
    ## trim line </description> </item></list>
    class Process(Enum):
        """
        Members Include: <EntireUnform> <IntermediateUnform> <AdvancedUnform> <TrimLine>
        """
        EntireUnform: int
        IntermediateUnform: int
        AdvancedUnform: int
        TrimLine: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Process:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The surface types of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inner</term><description> 
    ## Onestep solver will offset inner surface and enlarge it</description> </item><item><term> 
    ## Middle</term><description> 
    ## Onestep solver will not offset middle surface </description> </item><item><term> 
    ## Outer</term><description> 
    ## Onestep solver will offset outer surface and shrink it </description> </item></list>
    class Surface(Enum):
        """
        Members Include: <Inner> <Middle> <Outer>
        """
        Inner: int
        Middle: int
        Outer: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.Surface:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The Onesetp unfold mode of onestep unform. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Complete</term><description> 
    ##  Onestep unfold mode is complete </description> </item><item><term> 
    ## Intermediate</term><description> 
    ##  Onestep unfold mode is intermediate </description> </item><item><term> 
    ## Trimline</term><description> 
    ##  Onestep unfold mode is trimline</description> </item><item><term> 
    ## Unknown</term><description> 
    ##  Onestep unfold mode is unknown </description> </item></list>
    class UnfoldMode(Enum):
        """
        Members Include: <Complete> <Intermediate> <Trimline> <Unknown>
        """
        Complete: int
        Intermediate: int
        Trimline: int
        Unknown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> OnestepUnformBuilder.UnfoldMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BinderRegion
    ##  Returns the binder region which is a group of faces user chooses as holder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def BinderRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) BinderRegion
         Returns the binder region which is a group of faces user chooses as holder.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.Constraint NXOpen.BodyDes.OnestepUnformBuilder.Constraint@endlink) ConstraintType
    ##  Returns the constraint type for intermediate unform or complete unform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return OnestepUnformBuilder.Constraint
    @property
    def ConstraintType(self) -> OnestepUnformBuilder.Constraint:
        """
        Getter for property: (@link OnestepUnformBuilder.Constraint NXOpen.BodyDes.OnestepUnformBuilder.Constraint@endlink) ConstraintType
         Returns the constraint type for intermediate unform or complete unform.  
             
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.Constraint NXOpen.BodyDes.OnestepUnformBuilder.Constraint@endlink) ConstraintType

    ##  Returns the constraint type for intermediate unform or complete unform.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ConstraintType.setter
    def ConstraintType(self, constraintType: OnestepUnformBuilder.Constraint):
        """
        Setter for property: (@link OnestepUnformBuilder.Constraint NXOpen.BodyDes.OnestepUnformBuilder.Constraint@endlink) ConstraintType
         Returns the constraint type for intermediate unform or complete unform.  
             
         
        """
        pass
    
    ## Getter for property: (float) ContactPointsTolerance
    ##  Returns the tolerance to find contact points.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return float
    @property
    def ContactPointsTolerance(self) -> float:
        """
        Getter for property: (float) ContactPointsTolerance
         Returns the tolerance to find contact points.  
             
         
        """
        pass
    
    ## Setter for property: (float) ContactPointsTolerance

    ##  Returns the tolerance to find contact points.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @ContactPointsTolerance.setter
    def ContactPointsTolerance(self, tolerance: float):
        """
        Setter for property: (float) ContactPointsTolerance
         Returns the tolerance to find contact points.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawDirection
    ##  Returns the draw direction used to define the normal of unform base plane.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def DrawDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawDirection
         Returns the draw direction used to define the normal of unform base plane.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawDirection

    ##  Returns the draw direction used to define the normal of unform base plane.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @DrawDirection.setter
    def DrawDirection(self, drawDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DrawDirection
         Returns the draw direction used to define the normal of unform base plane.  
             
         
        """
        pass
    
    ## Getter for property: (float) Force
    ##  Returns the force on blank holder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def Force(self) -> float:
        """
        Getter for property: (float) Force
         Returns the force on blank holder.  
             
         
        """
        pass
    
    ## Setter for property: (float) Force

    ##  Returns the force on blank holder.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Force.setter
    def Force(self, force: float):
        """
        Setter for property: (float) Force
         Returns the force on blank holder.  
             
         
        """
        pass
    
    ## Getter for property: (float) ForceStrength
    ##  Returns the force strength on blank holder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def ForceStrength(self) -> float:
        """
        Getter for property: (float) ForceStrength
         Returns the force strength on blank holder.  
             
         
        """
        pass
    
    ## Setter for property: (float) ForceStrength

    ##  Returns the force strength on blank holder.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ForceStrength.setter
    def ForceStrength(self, forceStrength: float):
        """
        Setter for property: (float) ForceStrength
         Returns the force strength on blank holder.  
             
         
        """
        pass
    
    ## Getter for property: (bool) InferElementSize
    ##  Returns the option to infer 2-D element size.  
    ##    
    ##         If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def InferElementSize(self) -> bool:
        """
        Getter for property: (bool) InferElementSize
         Returns the option to infer 2-D element size.  
           
                If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
         
        """
        pass
    
    ## Setter for property: (bool) InferElementSize

    ##  Returns the option to infer 2-D element size.  
    ##    
    ##         If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InferElementSize.setter
    def InferElementSize(self, inforElementSize: bool):
        """
        Setter for property: (bool) InferElementSize
         Returns the option to infer 2-D element size.  
           
                If it is true, the element size will be auto-detected. If it is false, the element size will be required as input.   
         
        """
        pass
    
    ## Getter for property: (bool) InferThickness
    ##  Returns the option to infer thickness.  
    ##   
    ##         If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def InferThickness(self) -> bool:
        """
        Getter for property: (bool) InferThickness
         Returns the option to infer thickness.  
          
                If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
         
        """
        pass
    
    ## Setter for property: (bool) InferThickness

    ##  Returns the option to infer thickness.  
    ##   
    ##         If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @InferThickness.setter
    def InferThickness(self, inferThickness: bool):
        """
        Setter for property: (bool) InferThickness
         Returns the option to infer thickness.  
          
                If it is true, the thickness will be auto-detected. If it is false, thickness will be required to input.  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointOne
    ##  Returns the first match point for spring back calculation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def MatchPointOne(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointOne
         Returns the first match point for spring back calculation.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointOne

    ##  Returns the first match point for spring back calculation.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MatchPointOne.setter
    def MatchPointOne(self, matchPointOne: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointOne
         Returns the first match point for spring back calculation.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointThree
    ##  Returns the third match point for spring back calculation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def MatchPointThree(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointThree
         Returns the third match point for spring back calculation.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointThree

    ##  Returns the third match point for spring back calculation.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MatchPointThree.setter
    def MatchPointThree(self, matchPointThree: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointThree
         Returns the third match point for spring back calculation.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointTwo
    ##  Returns the second match point for spring back calculation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def MatchPointTwo(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointTwo
         Returns the second match point for spring back calculation.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointTwo

    ##  Returns the second match point for spring back calculation.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @MatchPointTwo.setter
    def MatchPointTwo(self, matchPointTwo: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MatchPointTwo
         Returns the second match point for spring back calculation.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyDensity
    ##  Returns the density of material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyDensity(self) -> float:
        """
        Getter for property: (float) MaterialPropertyDensity
         Returns the density of material.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyDensity

    ##  Returns the density of material.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyDensity.setter
    def MaterialPropertyDensity(self, materialPropertyDensity: float):
        """
        Setter for property: (float) MaterialPropertyDensity
         Returns the density of material.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyE
    ##  Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyE(self) -> float:
        """
        Getter for property: (float) MaterialPropertyE
         Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyE

    ##  Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyE.setter
    def MaterialPropertyE(self, materialPropertyE: float):
        """
        Setter for property: (float) MaterialPropertyE
         Returns the material property elasticity(E) which enables a material to return to its original shape and dimension.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyF
    ##  Returns the friction of material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyF(self) -> float:
        """
        Getter for property: (float) MaterialPropertyF
         Returns the friction of material.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyF

    ##  Returns the friction of material.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyF.setter
    def MaterialPropertyF(self, materialPropertyF: float):
        """
        Setter for property: (float) MaterialPropertyF
         Returns the friction of material.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyInitialStrain
    ##  Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyInitialStrain(self) -> float:
        """
        Getter for property: (float) MaterialPropertyInitialStrain
         Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyInitialStrain

    ##  Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyInitialStrain.setter
    def MaterialPropertyInitialStrain(self, materialPropertyInitialStrain: float):
        """
        Setter for property: (float) MaterialPropertyInitialStrain
         Returns the material initial strain to represent in a material upon achieving the given loading conditions in a relaxation or creep test.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyK
    ##  Returns the K(Strength Coefficient) of material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyK(self) -> float:
        """
        Getter for property: (float) MaterialPropertyK
         Returns the K(Strength Coefficient) of material.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyK

    ##  Returns the K(Strength Coefficient) of material.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyK.setter
    def MaterialPropertyK(self, materialPropertyK: float):
        """
        Setter for property: (float) MaterialPropertyK
         Returns the K(Strength Coefficient) of material.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyN
    ##  Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyN(self) -> float:
        """
        Getter for property: (float) MaterialPropertyN
         Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyN

    ##  Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyN.setter
    def MaterialPropertyN(self, materialPropertyN: float):
        """
        Setter for property: (float) MaterialPropertyN
         Returns the  material n(Hardening Exponent) to represent the constant index used in calculations for stress-strain behaviour.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyPoisson
    ##  Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyPoisson(self) -> float:
        """
        Getter for property: (float) MaterialPropertyPoisson
         Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyPoisson

    ##  Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyPoisson.setter
    def MaterialPropertyPoisson(self, materialPropertyPoisson: float):
        """
        Setter for property: (float) MaterialPropertyPoisson
         Returns the material Poisson's ratio between the contraction at right angles to a stress and the direct extension.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyR0
    ##  Returns the r0(Anisotropy Coefficient) of material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyR0(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR0
         Returns the r0(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyR0

    ##  Returns the r0(Anisotropy Coefficient) of material.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyR0.setter
    def MaterialPropertyR0(self, materialPropertyR0: float):
        """
        Setter for property: (float) MaterialPropertyR0
         Returns the r0(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyR45
    ##  Returns the r45(Anisotropy Coefficient) of material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyR45(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR45
         Returns the r45(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyR45

    ##  Returns the r45(Anisotropy Coefficient) of material.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyR45.setter
    def MaterialPropertyR45(self, materialPropertyR45: float):
        """
        Setter for property: (float) MaterialPropertyR45
         Returns the r45(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyR90
    ##  Returns the r90(Anisotropy Coefficient) of material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyR90(self) -> float:
        """
        Getter for property: (float) MaterialPropertyR90
         Returns the r90(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyR90

    ##  Returns the r90(Anisotropy Coefficient) of material.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyR90.setter
    def MaterialPropertyR90(self, materialPropertyR90: float):
        """
        Setter for property: (float) MaterialPropertyR90
         Returns the r90(Anisotropy Coefficient) of material.  
             
         
        """
        pass
    
    ## Getter for property: (float) MaterialPropertyYieldStress
    ##  Returns the yield stress of material.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MaterialPropertyYieldStress(self) -> float:
        """
        Getter for property: (float) MaterialPropertyYieldStress
         Returns the yield stress of material.  
             
         
        """
        pass
    
    ## Setter for property: (float) MaterialPropertyYieldStress

    ##  Returns the yield stress of material.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MaterialPropertyYieldStress.setter
    def MaterialPropertyYieldStress(self, materialPropertyYieldStress: float):
        """
        Setter for property: (float) MaterialPropertyYieldStress
         Returns the yield stress of material.  
             
         
        """
        pass
    
    ## Getter for property: (bool) MeshAttemptMapping
    ##  Returns the option to attemp mapping for mesh elements.  
    ##    
    ##         If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def MeshAttemptMapping(self) -> bool:
        """
        Getter for property: (bool) MeshAttemptMapping
         Returns the option to attemp mapping for mesh elements.  
           
                If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
         
        """
        pass
    
    ## Setter for property: (bool) MeshAttemptMapping

    ##  Returns the option to attemp mapping for mesh elements.  
    ##    
    ##         If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshAttemptMapping.setter
    def MeshAttemptMapping(self, meshAttemptMapping: bool):
        """
        Setter for property: (bool) MeshAttemptMapping
         Returns the option to attemp mapping for mesh elements.  
           
                If it is true, mesh element nodes will be mapped to the orginal surface to ensure the accuracy. if it is false, it will not do mapping.   
         
        """
        pass
    
    ## Getter for property: (float) MeshElementSize
    ##  Returns the 2-D element size for mesh.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MeshElementSize(self) -> float:
        """
        Getter for property: (float) MeshElementSize
         Returns the 2-D element size for mesh.  
             
         
        """
        pass
    
    ## Setter for property: (float) MeshElementSize

    ##  Returns the 2-D element size for mesh.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshElementSize.setter
    def MeshElementSize(self, meshElementSize: float):
        """
        Setter for property: (float) MeshElementSize
         Returns the 2-D element size for mesh.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.MeshElement NXOpen.BodyDes.OnestepUnformBuilder.MeshElement@endlink) MeshElementType
    ##  Returns the 2-D mesh element type, either triangle or quadrate element.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return OnestepUnformBuilder.MeshElement
    @property
    def MeshElementType(self) -> OnestepUnformBuilder.MeshElement:
        """
        Getter for property: (@link OnestepUnformBuilder.MeshElement NXOpen.BodyDes.OnestepUnformBuilder.MeshElement@endlink) MeshElementType
         Returns the 2-D mesh element type, either triangle or quadrate element.  
            
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.MeshElement NXOpen.BodyDes.OnestepUnformBuilder.MeshElement@endlink) MeshElementType

    ##  Returns the 2-D mesh element type, either triangle or quadrate element.  
    ##     
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshElementType.setter
    def MeshElementType(self, meshElementType: OnestepUnformBuilder.MeshElement):
        """
        Setter for property: (@link OnestepUnformBuilder.MeshElement NXOpen.BodyDes.OnestepUnformBuilder.MeshElement@endlink) MeshElementType
         Returns the 2-D mesh element type, either triangle or quadrate element.  
            
         
        """
        pass
    
    ## Getter for property: (float) MeshMaxJacobian
    ##  Returns the maximum Jacobian for mesh elements.  
    ##    It is used to control the element shape and quality.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MeshMaxJacobian(self) -> float:
        """
        Getter for property: (float) MeshMaxJacobian
         Returns the maximum Jacobian for mesh elements.  
           It is used to control the element shape and quality.   
         
        """
        pass
    
    ## Setter for property: (float) MeshMaxJacobian

    ##  Returns the maximum Jacobian for mesh elements.  
    ##    It is used to control the element shape and quality.   
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshMaxJacobian.setter
    def MeshMaxJacobian(self, meshMaxJacobian: float):
        """
        Setter for property: (float) MeshMaxJacobian
         Returns the maximum Jacobian for mesh elements.  
           It is used to control the element shape and quality.   
         
        """
        pass
    
    ## Getter for property: (float) MeshMaxWarp
    ##  Returns the maximum warp for meshing.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MeshMaxWarp(self) -> float:
        """
        Getter for property: (float) MeshMaxWarp
         Returns the maximum warp for meshing.  
             
         
        """
        pass
    
    ## Setter for property: (float) MeshMaxWarp

    ##  Returns the maximum warp for meshing.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshMaxWarp.setter
    def MeshMaxWarp(self, meshMaxWarp: float):
        """
        Setter for property: (float) MeshMaxWarp
         Returns the maximum warp for meshing.  
             
         
        """
        pass
    
    ## Getter for property: (bool) MeshProcessFillet
    ##  Returns the option to process fillet for mesh element.  
    ##   
    ##         If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def MeshProcessFillet(self) -> bool:
        """
        Getter for property: (bool) MeshProcessFillet
         Returns the option to process fillet for mesh element.  
          
                If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
         
        """
        pass
    
    ## Setter for property: (bool) MeshProcessFillet

    ##  Returns the option to process fillet for mesh element.  
    ##   
    ##         If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshProcessFillet.setter
    def MeshProcessFillet(self, meshProcessFillet: bool):
        """
        Setter for property: (bool) MeshProcessFillet
         Returns the option to process fillet for mesh element.  
          
                If it is true, the small fillet area will be specially processed when generate mesh element. If it is false, it will be not specially processed.   
         
        """
        pass
    
    ## Getter for property: (int) MeshSizeVariation
    ##  Returns the variation of mesh element size.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def MeshSizeVariation(self) -> int:
        """
        Getter for property: (int) MeshSizeVariation
         Returns the variation of mesh element size.  
             
         
        """
        pass
    
    ## Setter for property: (int) MeshSizeVariation

    ##  Returns the variation of mesh element size.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshSizeVariation.setter
    def MeshSizeVariation(self, meshSizeVariation: int):
        """
        Setter for property: (int) MeshSizeVariation
         Returns the variation of mesh element size.  
             
         
        """
        pass
    
    ## Getter for property: (float) MeshSmallFeature
    ##  Returns the value of small feature for mesh setting  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def MeshSmallFeature(self) -> float:
        """
        Getter for property: (float) MeshSmallFeature
         Returns the value of small feature for mesh setting  
            
         
        """
        pass
    
    ## Setter for property: (float) MeshSmallFeature

    ##  Returns the value of small feature for mesh setting  
    ##     
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshSmallFeature.setter
    def MeshSmallFeature(self, meshSmallFeature: float):
        """
        Setter for property: (float) MeshSmallFeature
         Returns the value of small feature for mesh setting  
            
         
        """
        pass
    
    ## Getter for property: (bool) MeshSplitQuad
    ##  Returns the option to split quadrate element to triangle element when creating meshes.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def MeshSplitQuad(self) -> bool:
        """
        Getter for property: (bool) MeshSplitQuad
         Returns the option to split quadrate element to triangle element when creating meshes.  
             
         
        """
        pass
    
    ## Setter for property: (bool) MeshSplitQuad

    ##  Returns the option to split quadrate element to triangle element when creating meshes.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @MeshSplitQuad.setter
    def MeshSplitQuad(self, meshSplitQuad: bool):
        """
        Setter for property: (bool) MeshSplitQuad
         Returns the option to split quadrate element to triangle element when creating meshes.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.Object NXOpen.BodyDes.OnestepUnformBuilder.Object@endlink) ObjectType
    ##  Returns the object type for onestep unform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return OnestepUnformBuilder.Object
    @property
    def ObjectType(self) -> OnestepUnformBuilder.Object:
        """
        Getter for property: (@link OnestepUnformBuilder.Object NXOpen.BodyDes.OnestepUnformBuilder.Object@endlink) ObjectType
         Returns the object type for onestep unform.  
             
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.Object NXOpen.BodyDes.OnestepUnformBuilder.Object@endlink) ObjectType

    ##  Returns the object type for onestep unform.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @ObjectType.setter
    def ObjectType(self, objectType: OnestepUnformBuilder.Object):
        """
        Setter for property: (@link OnestepUnformBuilder.Object NXOpen.BodyDes.OnestepUnformBuilder.Object@endlink) ObjectType
         Returns the object type for onestep unform.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) PartBoundary
    ##  Returns the boundary which is a group of edges user chooses to apply on equivalent force.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def PartBoundary(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) PartBoundary
         Returns the boundary which is a group of edges user chooses to apply on equivalent force.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.Part NXOpen.BodyDes.OnestepUnformBuilder.Part@endlink) PartType
    ##  Returns the part type for onestep unform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return OnestepUnformBuilder.Part
    @property
    def PartType(self) -> OnestepUnformBuilder.Part:
        """
        Getter for property: (@link OnestepUnformBuilder.Part NXOpen.BodyDes.OnestepUnformBuilder.Part@endlink) PartType
         Returns the part type for onestep unform.  
             
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.Part NXOpen.BodyDes.OnestepUnformBuilder.Part@endlink) PartType

    ##  Returns the part type for onestep unform.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @PartType.setter
    def PartType(self, partType: OnestepUnformBuilder.Part):
        """
        Setter for property: (@link OnestepUnformBuilder.Part NXOpen.BodyDes.OnestepUnformBuilder.Part@endlink) PartType
         Returns the part type for onestep unform.  
             
         
        """
        pass
    
    ## Getter for property: (float) Pressure
    ##  Returns the pressure on blank holder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return float
    @property
    def Pressure(self) -> float:
        """
        Getter for property: (float) Pressure
         Returns the pressure on blank holder.  
             
         
        """
        pass
    
    ## Setter for property: (float) Pressure

    ##  Returns the pressure on blank holder.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @Pressure.setter
    def Pressure(self, pressure: float):
        """
        Setter for property: (float) Pressure
         Returns the pressure on blank holder.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.Process NXOpen.BodyDes.OnestepUnformBuilder.Process@endlink) ProcessType
    ##  Returns the process type for onestep unform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return OnestepUnformBuilder.Process
    @property
    def ProcessType(self) -> OnestepUnformBuilder.Process:
        """
        Getter for property: (@link OnestepUnformBuilder.Process NXOpen.BodyDes.OnestepUnformBuilder.Process@endlink) ProcessType
         Returns the process type for onestep unform.  
             
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.Process NXOpen.BodyDes.OnestepUnformBuilder.Process@endlink) ProcessType

    ##  Returns the process type for onestep unform.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @ProcessType.setter
    def ProcessType(self, processType: OnestepUnformBuilder.Process):
        """
        Setter for property: (@link OnestepUnformBuilder.Process NXOpen.BodyDes.OnestepUnformBuilder.Process@endlink) ProcessType
         Returns the process type for onestep unform.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ReportDisplayFlattenShape
    ##  Returns the option to display result flatten shape in report.  
    ##   
    ##         If it is true, the report will display the flatten shape result. If it is false, the flatten shape will not be displayed in report.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ReportDisplayFlattenShape(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayFlattenShape
         Returns the option to display result flatten shape in report.  
          
                If it is true, the report will display the flatten shape result. If it is false, the flatten shape will not be displayed in report.  
         
        """
        pass
    
    ## Setter for property: (bool) ReportDisplayFlattenShape

    ##  Returns the option to display result flatten shape in report.  
    ##   
    ##         If it is true, the report will display the flatten shape result. If it is false, the flatten shape will not be displayed in report.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ReportDisplayFlattenShape.setter
    def ReportDisplayFlattenShape(self, reportDisplayFlattenShape: bool):
        """
        Setter for property: (bool) ReportDisplayFlattenShape
         Returns the option to display result flatten shape in report.  
          
                If it is true, the report will display the flatten shape result. If it is false, the flatten shape will not be displayed in report.  
         
        """
        pass
    
    ## Getter for property: (bool) ReportDisplaySpringback
    ##  Returns the option to display springback result in report.  
    ##   
    ##         If it is true, the report will display springback result. If it is false, the springback will not be displayed.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ReportDisplaySpringback(self) -> bool:
        """
        Getter for property: (bool) ReportDisplaySpringback
         Returns the option to display springback result in report.  
          
                If it is true, the report will display springback result. If it is false, the springback will not be displayed.  
         
        """
        pass
    
    ## Setter for property: (bool) ReportDisplaySpringback

    ##  Returns the option to display springback result in report.  
    ##   
    ##         If it is true, the report will display springback result. If it is false, the springback will not be displayed.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ReportDisplaySpringback.setter
    def ReportDisplaySpringback(self, reportDisplaySpringback: bool):
        """
        Setter for property: (bool) ReportDisplaySpringback
         Returns the option to display springback result in report.  
          
                If it is true, the report will display springback result. If it is false, the springback will not be displayed.  
         
        """
        pass
    
    ## Getter for property: (bool) ReportDisplayStrain
    ##  Returns the option to display strain in report.  
    ##   
    ##         If it is true, the report will display strain information. If it is false, the report will not display strain information.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ReportDisplayStrain(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayStrain
         Returns the option to display strain in report.  
          
                If it is true, the report will display strain information. If it is false, the report will not display strain information.  
         
        """
        pass
    
    ## Setter for property: (bool) ReportDisplayStrain

    ##  Returns the option to display strain in report.  
    ##   
    ##         If it is true, the report will display strain information. If it is false, the report will not display strain information.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ReportDisplayStrain.setter
    def ReportDisplayStrain(self, reportDisplayStrain: bool):
        """
        Setter for property: (bool) ReportDisplayStrain
         Returns the option to display strain in report.  
          
                If it is true, the report will display strain information. If it is false, the report will not display strain information.  
         
        """
        pass
    
    ## Getter for property: (bool) ReportDisplayStress
    ##  Returns the option to display stress in report.  
    ##   
    ##         If it is true, the stress information will be displayed in report. If it is false, the report will not display stress information.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ReportDisplayStress(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayStress
         Returns the option to display stress in report.  
          
                If it is true, the stress information will be displayed in report. If it is false, the report will not display stress information.  
         
        """
        pass
    
    ## Setter for property: (bool) ReportDisplayStress

    ##  Returns the option to display stress in report.  
    ##   
    ##         If it is true, the stress information will be displayed in report. If it is false, the report will not display stress information.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ReportDisplayStress.setter
    def ReportDisplayStress(self, reportDisplayStress: bool):
        """
        Setter for property: (bool) ReportDisplayStress
         Returns the option to display stress in report.  
          
                If it is true, the stress information will be displayed in report. If it is false, the report will not display stress information.  
         
        """
        pass
    
    ## Getter for property: (bool) ReportDisplayThickness
    ##  Returns the option to display thickness information in report.  
    ##   
    ##         If it is true, the thickness information will be displayed in report. If it is false, the report will not display thickness information.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ReportDisplayThickness(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayThickness
         Returns the option to display thickness information in report.  
          
                If it is true, the thickness information will be displayed in report. If it is false, the report will not display thickness information.  
         
        """
        pass
    
    ## Setter for property: (bool) ReportDisplayThickness

    ##  Returns the option to display thickness information in report.  
    ##   
    ##         If it is true, the thickness information will be displayed in report. If it is false, the report will not display thickness information.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ReportDisplayThickness.setter
    def ReportDisplayThickness(self, reportDisplayThickness: bool):
        """
        Setter for property: (bool) ReportDisplayThickness
         Returns the option to display thickness information in report.  
          
                If it is true, the thickness information will be displayed in report. If it is false, the report will not display thickness information.  
         
        """
        pass
    
    ## Getter for property: (bool) ReportDisplayViewControl
    ##  Returns the option to control view while creating screen image in report.  
    ##   
    ##         If it is true, customer can control the view when capturing the screen image. If it is false, default view will be used in report.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def ReportDisplayViewControl(self) -> bool:
        """
        Getter for property: (bool) ReportDisplayViewControl
         Returns the option to control view while creating screen image in report.  
          
                If it is true, customer can control the view when capturing the screen image. If it is false, default view will be used in report.  
         
        """
        pass
    
    ## Setter for property: (bool) ReportDisplayViewControl

    ##  Returns the option to control view while creating screen image in report.  
    ##   
    ##         If it is true, customer can control the view when capturing the screen image. If it is false, default view will be used in report.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @ReportDisplayViewControl.setter
    def ReportDisplayViewControl(self, reportDisplayViewControl: bool):
        """
        Setter for property: (bool) ReportDisplayViewControl
         Returns the option to control view while creating screen image in report.  
          
                If it is true, customer can control the view when capturing the screen image. If it is false, default view will be used in report.  
         
        """
        pass
    
    ## Getter for property: (bool) ReverseSide
    ##  Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
    ##    
    ##          This option is appliable only in case the following conditions are all satisfied: entire unform to separate target body, Curve to Curve constraint on inner edges.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def ReverseSide(self) -> bool:
        """
        Getter for property: (bool) ReverseSide
         Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
           
                 This option is appliable only in case the following conditions are all satisfied: entire unform to separate target body, Curve to Curve constraint on inner edges.  
         
        """
        pass
    
    ## Setter for property: (bool) ReverseSide

    ##  Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
    ##    
    ##          This option is appliable only in case the following conditions are all satisfied: entire unform to separate target body, Curve to Curve constraint on inner edges.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ReverseSide.setter
    def ReverseSide(self, reverseSide: bool):
        """
        Setter for property: (bool) ReverseSide
         Returns the option to indicate whether or not to unform the profile to the other side on the target body.  
           
                 This option is appliable only in case the following conditions are all satisfied: entire unform to separate target body, Curve to Curve constraint on inner edges.  
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.Convergency NXOpen.BodyDes.OnestepUnformBuilder.Convergency@endlink) SolverConvergencyLevel
    ##  Returns the convergency level of onestep solver.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return OnestepUnformBuilder.Convergency
    @property
    def SolverConvergencyLevel(self) -> OnestepUnformBuilder.Convergency:
        """
        Getter for property: (@link OnestepUnformBuilder.Convergency NXOpen.BodyDes.OnestepUnformBuilder.Convergency@endlink) SolverConvergencyLevel
         Returns the convergency level of onestep solver.  
             
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.Convergency NXOpen.BodyDes.OnestepUnformBuilder.Convergency@endlink) SolverConvergencyLevel

    ##  Returns the convergency level of onestep solver.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SolverConvergencyLevel.setter
    def SolverConvergencyLevel(self, solverConvergencyLevel: OnestepUnformBuilder.Convergency):
        """
        Setter for property: (@link OnestepUnformBuilder.Convergency NXOpen.BodyDes.OnestepUnformBuilder.Convergency@endlink) SolverConvergencyLevel
         Returns the convergency level of onestep solver.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.DisplaySpringbackMode NXOpen.BodyDes.OnestepUnformBuilder.DisplaySpringbackMode@endlink) SolverDisplaySpringbackMode
    ##  Returns the option for springback display.  
    ##    
    ##         If it is true, it will display springback in absolution 3D distance, or projecte in x/y/z directions.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return OnestepUnformBuilder.DisplaySpringbackMode
    @property
    def SolverDisplaySpringbackMode(self) -> OnestepUnformBuilder.DisplaySpringbackMode:
        """
        Getter for property: (@link OnestepUnformBuilder.DisplaySpringbackMode NXOpen.BodyDes.OnestepUnformBuilder.DisplaySpringbackMode@endlink) SolverDisplaySpringbackMode
         Returns the option for springback display.  
           
                If it is true, it will display springback in absolution 3D distance, or projecte in x/y/z directions.  
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.DisplaySpringbackMode NXOpen.BodyDes.OnestepUnformBuilder.DisplaySpringbackMode@endlink) SolverDisplaySpringbackMode

    ##  Returns the option for springback display.  
    ##    
    ##         If it is true, it will display springback in absolution 3D distance, or projecte in x/y/z directions.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SolverDisplaySpringbackMode.setter
    def SolverDisplaySpringbackMode(self, solverDisplaySpringbackMode: OnestepUnformBuilder.DisplaySpringbackMode):
        """
        Setter for property: (@link OnestepUnformBuilder.DisplaySpringbackMode NXOpen.BodyDes.OnestepUnformBuilder.DisplaySpringbackMode@endlink) SolverDisplaySpringbackMode
         Returns the option for springback display.  
           
                If it is true, it will display springback in absolution 3D distance, or projecte in x/y/z directions.  
         
        """
        pass
    
    ## Getter for property: (bool) SolverDoSpringbackCalculation
    ##  Returns the option to do springback calculation in onestep solver.  
    ##   
    ##         If it is true, the onestep solver will do springback calculation. If it is false, the solver will not do springback calculation.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def SolverDoSpringbackCalculation(self) -> bool:
        """
        Getter for property: (bool) SolverDoSpringbackCalculation
         Returns the option to do springback calculation in onestep solver.  
          
                If it is true, the onestep solver will do springback calculation. If it is false, the solver will not do springback calculation.  
         
        """
        pass
    
    ## Setter for property: (bool) SolverDoSpringbackCalculation

    ##  Returns the option to do springback calculation in onestep solver.  
    ##   
    ##         If it is true, the onestep solver will do springback calculation. If it is false, the solver will not do springback calculation.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SolverDoSpringbackCalculation.setter
    def SolverDoSpringbackCalculation(self, solverDoSpringbackCalculation: bool):
        """
        Setter for property: (bool) SolverDoSpringbackCalculation
         Returns the option to do springback calculation in onestep solver.  
          
                If it is true, the onestep solver will do springback calculation. If it is false, the solver will not do springback calculation.  
         
        """
        pass
    
    ## Getter for property: (bool) SolverJoinOutputCurves
    ##  Returns the option to join output curves.  
    ##   
    ##         If it is true, join output curves. If it is false, do not join output curves  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def SolverJoinOutputCurves(self) -> bool:
        """
        Getter for property: (bool) SolverJoinOutputCurves
         Returns the option to join output curves.  
          
                If it is true, join output curves. If it is false, do not join output curves  
         
        """
        pass
    
    ## Setter for property: (bool) SolverJoinOutputCurves

    ##  Returns the option to join output curves.  
    ##   
    ##         If it is true, join output curves. If it is false, do not join output curves  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SolverJoinOutputCurves.setter
    def SolverJoinOutputCurves(self, solverJoinOutputCurves: bool):
        """
        Setter for property: (bool) SolverJoinOutputCurves
         Returns the option to join output curves.  
          
                If it is true, join output curves. If it is false, do not join output curves  
         
        """
        pass
    
    ## Getter for property: (int) SolverMaxIterationSteps
    ##  Returnsthe maximum number of iteration steps in onestep solver.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def SolverMaxIterationSteps(self) -> int:
        """
        Getter for property: (int) SolverMaxIterationSteps
         Returnsthe maximum number of iteration steps in onestep solver.  
             
         
        """
        pass
    
    ## Setter for property: (int) SolverMaxIterationSteps

    ##  Returnsthe maximum number of iteration steps in onestep solver.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SolverMaxIterationSteps.setter
    def SolverMaxIterationSteps(self, solverMaxIterationSteps: int):
        """
        Setter for property: (int) SolverMaxIterationSteps
         Returnsthe maximum number of iteration steps in onestep solver.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SolverSaveAnalysisResultsIntoFeature
    ##  Returns the option to save analysis result into feature.  
    ##   
    ##         If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## @return bool
    @property
    def SolverSaveAnalysisResultsIntoFeature(self) -> bool:
        """
        Getter for property: (bool) SolverSaveAnalysisResultsIntoFeature
         Returns the option to save analysis result into feature.  
          
                If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
         
        """
        pass
    
    ## Setter for property: (bool) SolverSaveAnalysisResultsIntoFeature

    ##  Returns the option to save analysis result into feature.  
    ##   
    ##         If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    @SolverSaveAnalysisResultsIntoFeature.setter
    def SolverSaveAnalysisResultsIntoFeature(self, solverSaveAnalysisResultsIntoFeature: bool):
        """
        Setter for property: (bool) SolverSaveAnalysisResultsIntoFeature
         Returns the option to save analysis result into feature.  
          
                If it is true, save analysis result into feature. If it is false, do not save analysis result into feature.  
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.Surface NXOpen.BodyDes.OnestepUnformBuilder.Surface@endlink) SurfaceType
    ##  Returns the surface type used to determine offset direction.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return OnestepUnformBuilder.Surface
    @property
    def SurfaceType(self) -> OnestepUnformBuilder.Surface:
        """
        Getter for property: (@link OnestepUnformBuilder.Surface NXOpen.BodyDes.OnestepUnformBuilder.Surface@endlink) SurfaceType
         Returns the surface type used to determine offset direction.  
             
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.Surface NXOpen.BodyDes.OnestepUnformBuilder.Surface@endlink) SurfaceType

    ##  Returns the surface type used to determine offset direction.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @SurfaceType.setter
    def SurfaceType(self, surfaceType: OnestepUnformBuilder.Surface):
        """
        Setter for property: (@link OnestepUnformBuilder.Surface NXOpen.BodyDes.OnestepUnformBuilder.Surface@endlink) SurfaceType
         Returns the surface type used to determine offset direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) TargetRegion
    ##  Returns the target region which is a group of faces user chooses to unfrom to.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def TargetRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) TargetRegion
         Returns the target region which is a group of faces user chooses to unfrom to.  
             
         
        """
        pass
    
    ## Getter for property: (float) Thickness
    ##  Returns the thickness of sheet metal model.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return float
    @property
    def Thickness(self) -> float:
        """
        Getter for property: (float) Thickness
         Returns the thickness of sheet metal model.  
             
         
        """
        pass
    
    ## Setter for property: (float) Thickness

    ##  Returns the thickness of sheet metal model.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Thickness.setter
    def Thickness(self, thickness: float):
        """
        Setter for property: (float) Thickness
         Returns the thickness of sheet metal model.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThicknessDirection
    ##  Returns the thickness direction used to define the direction of product thickness at the specific point in trimline.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.Direction
    @property
    def ThicknessDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThicknessDirection
         Returns the thickness direction used to define the direction of product thickness at the specific point in trimline.  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThicknessDirection

    ##  Returns the thickness direction used to define the direction of product thickness at the specific point in trimline.  
    ##     
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    @ThicknessDirection.setter
    def ThicknessDirection(self, thicknessDirection: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ThicknessDirection
         Returns the thickness direction used to define the direction of product thickness at the specific point in trimline.  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TrimlinePoint
    ##  Returns the point where the thickness direction is defined for trimline.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## @return NXOpen.Point
    @property
    def TrimlinePoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TrimlinePoint
         Returns the point where the thickness direction is defined for trimline.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TrimlinePoint

    ##  Returns the point where the thickness direction is defined for trimline.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    @TrimlinePoint.setter
    def TrimlinePoint(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TrimlinePoint
         Returns the point where the thickness direction is defined for trimline.  
             
         
        """
        pass
    
    ## Getter for property: (@link OnestepUnformBuilder.UnfoldMode NXOpen.BodyDes.OnestepUnformBuilder.UnfoldMode@endlink) UnfoldModeType
    ##  Returns the onestep unfold mode.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return OnestepUnformBuilder.UnfoldMode
    @property
    def UnfoldModeType(self) -> OnestepUnformBuilder.UnfoldMode:
        """
        Getter for property: (@link OnestepUnformBuilder.UnfoldMode NXOpen.BodyDes.OnestepUnformBuilder.UnfoldMode@endlink) UnfoldModeType
         Returns the onestep unfold mode.  
             
         
        """
        pass
    
    ## Setter for property: (@link OnestepUnformBuilder.UnfoldMode NXOpen.BodyDes.OnestepUnformBuilder.UnfoldMode@endlink) UnfoldModeType

    ##  Returns the onestep unfold mode.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @UnfoldModeType.setter
    def UnfoldModeType(self, unfoldModeType: OnestepUnformBuilder.UnfoldMode):
        """
        Setter for property: (@link OnestepUnformBuilder.UnfoldMode NXOpen.BodyDes.OnestepUnformBuilder.UnfoldMode@endlink) UnfoldModeType
         Returns the onestep unfold mode.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) UnfoldSolid
    ##  Returns the solid body to unform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.Body
    @property
    def UnfoldSolid(self) -> NXOpen.Body:
        """
        Getter for property: (@link NXOpen.Body NXOpen.Body@endlink) UnfoldSolid
         Returns the solid body to unform.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) UnfoldSolid

    ##  Returns the solid body to unform.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    @UnfoldSolid.setter
    def UnfoldSolid(self, unfoldSolidTag: NXOpen.Body):
        """
        Setter for property: (@link NXOpen.Body NXOpen.Body@endlink) UnfoldSolid
         Returns the solid body to unform.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) UnfoldSolidRegion
    ##  Returns the unfold solid regions which are a group of faces user chooses to unform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## @return NXOpen.SelectBodyList
    @property
    def UnfoldSolidRegion(self) -> NXOpen.SelectBodyList:
        """
        Getter for property: (@link NXOpen.SelectBodyList NXOpen.SelectBodyList@endlink) UnfoldSolidRegion
         Returns the unfold solid regions which are a group of faces user chooses to unform.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) UnformRegion
    ##  Returns the unform region which is a group of faces user chooses to unform.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.ScCollector
    @property
    def UnformRegion(self) -> NXOpen.ScCollector:
        """
        Getter for property: (@link NXOpen.ScCollector NXOpen.ScCollector@endlink) UnformRegion
         Returns the unform region which is a group of faces user chooses to unform.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) UnformSection
    ##  Returns the unform section which includes a group of user selected points or curves.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.Section
    @property
    def UnformSection(self) -> NXOpen.Section:
        """
        Getter for property: (@link NXOpen.Section NXOpen.Section@endlink) UnformSection
         Returns the unform section which includes a group of user selected points or curves.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Section NXOpen.Section@endlink) UnformSection

    ##  Returns the unform section which includes a group of user selected points or curves.  
    ##      
    ##  
    ## Setter License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @UnformSection.setter
    def UnformSection(self, unformsection: NXOpen.Section):
        """
        Setter for property: (@link NXOpen.Section NXOpen.Section@endlink) UnformSection
         Returns the unform section which includes a group of user selected points or curves.  
             
         
        """
        pass
    
    ##  Starts solver to calculate. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def Calculation(self) -> None:
        """
         Starts solver to calculate. 
        """
        pass
    
    ##  Constructs solver to prepare the data. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="tOnestepSolverType"> (int) </param>
    def Constructor(self, tOnestepSolverType: int) -> None:
        """
         Constructs solver to prepare the data. 
        """
        pass
    
    ##  Creates unform sheet body result. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="readResultFromFeature"> (bool) </param>
    def CreateSheetBody(self, readResultFromFeature: bool) -> None:
        """
         Creates unform sheet body result. 
        """
        pass
    
    ##  Deletes the offset body when the object type is body. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def DeleteOffsetSheetBody(self) -> None:
        """
         Deletes the offset body when the object type is body. 
        """
        pass
    
    ##  Destructs solver to release the data. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def Destructor(self) -> None:
        """
         Destructs solver to release the data. 
        """
        pass
    
    ##  Displays profile result. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="readResultFromFeature"> (bool) </param>
    def DisplayProfile(self, readResultFromFeature: bool) -> None:
        """
         Displays profile result. 
        """
        pass
    
    ##  Gets the blank result nodes. 
    ##  @return nodes (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetBlankShape(self) -> List[float]:
        """
         Gets the blank result nodes. 
         @return nodes (List[float]): .
        """
        pass
    
    ##  Gets the boundary loop IDs.
    ##  @return A tuple consisting of (index, nodeIdentifications). 
    ##  - index is: List[int].
    ##  - nodeIdentifications is: List[int].

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetBorderLoops(self) -> Tuple[List[int], List[int]]:
        """
         Gets the boundary loop IDs.
         @return A tuple consisting of (index, nodeIdentifications). 
         - index is: List[int].
         - nodeIdentifications is: List[int].

        """
        pass
    
    ##  Gets the bottom surface strain result. 
    ##  @return nodes (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetBottomSurfaceStrain(self) -> List[float]:
        """
         Gets the bottom surface strain result. 
         @return nodes (List[float]): .
        """
        pass
    
    ##  Gets the bottom surface stress result. 
    ##  @return nodes (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetBottomSurfaceStress(self) -> List[float]:
        """
         Gets the bottom surface stress result. 
         @return nodes (List[float]): .
        """
        pass
    
    ##  Gets the element node IDs where the product face meshes and addendum faces mesh are contacting within the given tolerance. 
    ##  @return id (List[int]): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetContactNodeIds(self) -> List[int]:
        """
         Gets the element node IDs where the product face meshes and addendum faces mesh are contacting within the given tolerance. 
         @return id (List[int]): .
        """
        pass
    
    ##  Gets the mesh element data. 
    ##  @return A tuple consisting of (vnode, constraint_id, element). 
    ##  - vnode is: List[float].
    ##  - constraint_id is: List[int].
    ##  - element is: List[int].

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetMeshes(self) -> Tuple[List[float], List[int], List[int]]:
        """
         Gets the mesh element data. 
         @return A tuple consisting of (vnode, constraint_id, element). 
         - vnode is: List[float].
         - constraint_id is: List[int].
         - element is: List[int].

        """
        pass
    
    ##  Gets the minimum node ID. 
    ##  @return min_id (int): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetMinNodeID(self) -> int:
        """
         Gets the minimum node ID. 
         @return min_id (int): .
        """
        pass
    
    ##  Gets the node IDs on the free edges (non-constrainted boundary edges). 
    ##  @return A tuple consisting of (index, nodeIdentifications). 
    ##  - index is: List[int].
    ##  - nodeIdentifications is: List[int].

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetNodeIdsOnFreeEdge(self) -> Tuple[List[int], List[int]]:
        """
         Gets the node IDs on the free edges (non-constrainted boundary edges). 
         @return A tuple consisting of (index, nodeIdentifications). 
         - index is: List[int].
         - nodeIdentifications is: List[int].

        """
        pass
    
    ##  Gets the reference node ID. 
    ##  @return eid (int): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetRefNode(self) -> int:
        """
         Gets the reference node ID. 
         @return eid (int): .
        """
        pass
    
    ##  Gets the solver calculation type. 
    ##  @return tOnestepSolverType (int): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetSolverType(self) -> int:
        """
         Gets the solver calculation type. 
         @return tOnestepSolverType (int): .
        """
        pass
    
    ##  Gets the springbrack result. 
    ##  @return nodes (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetSpringbackShape(self) -> List[float]:
        """
         Gets the springbrack result. 
         @return nodes (List[float]): .
        """
        pass
    
    ##  Gets the strain result. 
    ##  @return strains (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetStrain(self) -> List[float]:
        """
         Gets the strain result. 
         @return strains (List[float]): .
        """
        pass
    
    ##  Gets the stress result. 
    ##  @return stress (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetStress(self) -> List[float]:
        """
         Gets the stress result. 
         @return stress (List[float]): .
        """
        pass
    
    ##  Gets Thickness. 
    ##  @return thickness (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## <param name="builder"> (@link OnestepUnformBuilder NXOpen.BodyDes.OnestepUnformBuilder@endlink) </param>
    @overload
    def GetThickness(self) -> List[float]:
        """
         Gets Thickness. 
         @return thickness (List[float]): .
        """
        pass
    
    ##  Gets the top surface strain result. 
    ##  @return nodes (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetTopSurfaceStrain(self) -> List[float]:
        """
         Gets the top surface strain result. 
         @return nodes (List[float]): .
        """
        pass
    
    ##  Gets the top surface stress result. 
    ##  @return nodes (List[float]): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def GetTopSurfaceStress(self) -> List[float]:
        """
         Gets the top surface stress result. 
         @return nodes (List[float]): .
        """
        pass
    
    ##  Checks whether the result is available or not.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def IsResultExist(self) -> None:
        """
         Checks whether the result is available or not.
        """
        pass
    
    ##  Create FEM 2-D meshes based on the unform region surfaces and the target region surfaces.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def Mesh(self) -> None:
        """
         Create FEM 2-D meshes based on the unform region surfaces and the target region surfaces.
        """
        pass
    
    ##  Register the callback to solver.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def OnestepUnformRegisterProjectCallback(self) -> None:
        """
         Register the callback to solver.
        """
        pass
    
    ##  Set advanced constraint information. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="advancedConstraintPartType"> (int) </param>
    ## <param name="blankHolderWithAddendumBinderRegion"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Objects to be checked</param>
    ## <param name="blankHolderWithoutAddendumBoundaryOfPart"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Objects to be checked</param>
    ## <param name="blankHolderWithAddendumPressure"> (float) </param>
    ## <param name="blankHolderWithAddendumForce"> (float) </param>
    ## <param name="blankHolderWithoutAddendumTension"> (float) </param>
    ## <param name="blankHolderWithoutAddendumForce"> (float) </param>
    ## <param name="blankHolderWithoutAddendumForceStrength"> (float) </param>
    ## <param name="drawbeadTag"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Objects to be checked</param>
    ## <param name="drawbeadTtension"> (List[float]) </param>
    ## <param name="drawbeadNtension"> (List[float]) </param>
    ## <param name="drawbeadForceStrength"> (List[float]) </param>
    def SetAdvancedConstraintInformation(self, advancedConstraintPartType: int, blankHolderWithAddendumBinderRegion: List[NXOpen.TaggedObject], blankHolderWithoutAddendumBoundaryOfPart: List[NXOpen.TaggedObject], blankHolderWithAddendumPressure: float, blankHolderWithAddendumForce: float, blankHolderWithoutAddendumTension: float, blankHolderWithoutAddendumForce: float, blankHolderWithoutAddendumForceStrength: float, drawbeadTag: List[NXOpen.TaggedObject], drawbeadTtension: List[float], drawbeadNtension: List[float], drawbeadForceStrength: List[float]) -> None:
        """
         Set advanced constraint information. 
        """
        pass
    
    ##  Sets the blank thickness. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="thickness"> (float) </param>
    def SetBlankThickness(self, thickness: float) -> None:
        """
         Sets the blank thickness. 
        """
        pass
    
    ##  Sets the boundary condition information.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="edgeTags"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Objects to be checked</param>
    ## <param name="nids"> (List[int]) </param>
    ## <param name="groupInfo"> (List[int]) </param>
    def SetBorderInfo(self, edgeTags: List[NXOpen.TaggedObject], nids: List[int], groupInfo: List[int]) -> None:
        """
         Sets the boundary condition information.
        """
        pass
    
    ##  Set constraint information. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="noCommonEdges"> (bool) </param>
    ## <param name="revisedDirU"> (List[int]) </param>
    ## <param name="revisedDirT"> (List[int]) </param>
    ## <param name="index"> (List[int]) </param>
    ## <param name="constraintType"> (List[int]) </param>
    ## <param name="cacNumsUnform"> (List[int]) </param>
    ## <param name="cacNumsTarget"> (List[int]) </param>
    ## <param name="consCurveFromUnform"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Objects to be checked</param>
    ## <param name="consCurveFromTarget"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  Objects to be checked</param>
    ## <param name="consPointFromUnform"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  Objects to be checked</param>
    ## <param name="consPointFromTarget"> (@link NXOpen.Point List[NXOpen.Point]@endlink)  Objects to be checked</param>
    ## <param name="startPtOfConsCrvsUnform"> (List[float]) </param>
    ## <param name="startPtOfConsCrvsTarget"> (List[float]) </param>
    def SetConstraintInformation(self, noCommonEdges: bool, revisedDirU: List[int], revisedDirT: List[int], index: List[int], constraintType: List[int], cacNumsUnform: List[int], cacNumsTarget: List[int], consCurveFromUnform: List[NXOpen.TaggedObject], consCurveFromTarget: List[NXOpen.TaggedObject], consPointFromUnform: List[NXOpen.Point], consPointFromTarget: List[NXOpen.Point], startPtOfConsCrvsUnform: List[float], startPtOfConsCrvsTarget: List[float]) -> None:
        """
         Set constraint information. 
        """
        pass
    
    ##  Sets the unform draw direction. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## <param name="builder"> (@link OnestepUnformBuilder NXOpen.BodyDes.OnestepUnformBuilder@endlink) </param>
    ## <param name="tdx"> (int) </param>
    ## <param name="tdy"> (int) </param>
    ## <param name="tdz"> (int) </param>
    @overload
    def SetDrawDirection(self, tdx: int, tdy: int, tdz: int) -> None:
        """
         Sets the unform draw direction. 
        """
        pass
    
    ##  Sets the offset faces when the object type is body. 
    ##  @return setMark (bool): .
    ## 
    ##   <br>  Created in NX11.0.2  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="unfoldBody"> (@link NXOpen.Body NXOpen.Body@endlink) </param>
    def SetFacesOnOffsetSheet(self, unfoldBody: NXOpen.Body) -> bool:
        """
         Sets the offset faces when the object type is body. 
         @return setMark (bool): .
        """
        pass
    
    ##  Sets the node IDs on the free edges (non-constrainted boundary edges). 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="index"> (List[int]) </param>
    ## <param name="nids"> (List[int]) </param>
    def SetNodeIDsOnFreeEdge(self, index: List[int], nids: List[int]) -> None:
        """
         Sets the node IDs on the free edges (non-constrainted boundary edges). 
        """
        pass
    
    ##  Sets blank shape result. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="blankshape"> (List[float]) </param>
    def SetResultBlankShape(self, blankshape: List[float]) -> None:
        """
         Sets blank shape result. 
        """
        pass
    
    ##  Sets profile node ID result. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nids"> (List[int]) </param>
    def SetResultNodesIdsOnProfile(self, nids: List[int]) -> None:
        """
         Sets profile node ID result. 
        """
        pass
    
    ##  Sets total number of node on each profile. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indexs"> (List[int]) </param>
    def SetResultNodesNumEachProfileCurve(self, indexs: List[int]) -> None:
        """
         Sets total number of node on each profile. 
        """
        pass
    
    ##  Sets reference node ID. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="resultRefNodeId"> (int) </param>
    def SetResultRefNodeId(self, resultRefNodeId: int) -> None:
        """
         Sets reference node ID. 
        """
        pass
    
    ##  Sets springback result. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="springback"> (List[float]) </param>
    def SetResultSpringBack(self, springback: List[float]) -> None:
        """
         Sets springback result. 
        """
        pass
    
    ##  Sets strain result. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="strain"> (List[float]) </param>
    def SetResultStrain(self, strain: List[float]) -> None:
        """
         Sets strain result. 
        """
        pass
    
    ##  Sets stress result. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="stress"> (List[float]) </param>
    def SetResultStress(self, stress: List[float]) -> None:
        """
         Sets stress result. 
        """
        pass
    
    ##  Sets thickness result. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="thickness"> (List[float]) </param>
    def SetResultThickness(self, thickness: List[float]) -> None:
        """
         Sets thickness result. 
        """
        pass
    
    ##  Sets the unform surface type. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## <param name="builder"> (@link OnestepUnformBuilder NXOpen.BodyDes.OnestepUnformBuilder@endlink) </param>
    ## <param name="tOnestepSolverSurfaceType"> (int) </param>
    @overload
    def SetSurfaceType(self, tOnestepSolverSurfaceType: int) -> None:
        """
         Sets the unform surface type. 
        """
        pass
    
    ##  Updates the mesh elements to solver.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    def UpdateInputMeshDataToSolver(self) -> None:
        """
         Updates the mesh elements to solver.
        """
        pass
    
import NXOpen
import NXOpen.Features
##  Represents a collection of OnestepUnform  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class OnestepUnformCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of OnestepUnform """


    ##  Creates an Onestep Unform builder. 
    ##  @return builder (@link OnestepUnformBuilder NXOpen.BodyDes.OnestepUnformBuilder@endlink):  @link  OnestepUnformBuilder   OnestepUnformBuilder @endlink  object object .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: nx_onestep_analysis ("NX Onestep Analysis") OR nx_general_packaging ("NX General Packaging") OR die_engineering ("DIE ENGINEERING") OR aero_sheet_metal ("Aerospace Sheet Metal") OR adv_sheet_metal_dsgn ("ADVANCED SHEET METAL DESIGN")
    ## 
    ## <param name="onestepunform"> (@link NXOpen.Features.Feature NXOpen.Features.Feature@endlink)  @link Features::Feature Features::Feature@endlink  to be edited </param>
    def CreateOnestepBuilder(self, onestepunform: NXOpen.Features.Feature) -> OnestepUnformBuilder:
        """
         Creates an Onestep Unform builder. 
         @return builder (@link OnestepUnformBuilder NXOpen.BodyDes.OnestepUnformBuilder@endlink):  @link  OnestepUnformBuilder   OnestepUnformBuilder @endlink  object object .
        """
        pass
    
import NXOpen.Features
##  Represents a onestep unform feature  <br> To create or edit an instance of this class, use @link NXOpen::BodyDes::OnestepUnformBuilder  NXOpen::BodyDes::OnestepUnformBuilder @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class OnestepUnform(NXOpen.Features.Feature): 
    """ Represents a onestep unform feature """
    pass


## @package NXOpen.BodyDes
## Classes, Enums and Structs under NXOpen.BodyDes namespace

##  @link OnestepUnformBuilderConstraint NXOpen.BodyDes.OnestepUnformBuilderConstraint @endlink is an alias for @link OnestepUnformBuilder.Constraint NXOpen.BodyDes.OnestepUnformBuilder.Constraint@endlink
OnestepUnformBuilderConstraint = OnestepUnformBuilder.Constraint


##  @link OnestepUnformBuilderConvergency NXOpen.BodyDes.OnestepUnformBuilderConvergency @endlink is an alias for @link OnestepUnformBuilder.Convergency NXOpen.BodyDes.OnestepUnformBuilder.Convergency@endlink
OnestepUnformBuilderConvergency = OnestepUnformBuilder.Convergency


##  @link OnestepUnformBuilderDisplaySpringbackMode NXOpen.BodyDes.OnestepUnformBuilderDisplaySpringbackMode @endlink is an alias for @link OnestepUnformBuilder.DisplaySpringbackMode NXOpen.BodyDes.OnestepUnformBuilder.DisplaySpringbackMode@endlink
OnestepUnformBuilderDisplaySpringbackMode = OnestepUnformBuilder.DisplaySpringbackMode


##  @link OnestepUnformBuilderMeshElement NXOpen.BodyDes.OnestepUnformBuilderMeshElement @endlink is an alias for @link OnestepUnformBuilder.MeshElement NXOpen.BodyDes.OnestepUnformBuilder.MeshElement@endlink
OnestepUnformBuilderMeshElement = OnestepUnformBuilder.MeshElement


##  @link OnestepUnformBuilderObject NXOpen.BodyDes.OnestepUnformBuilderObject @endlink is an alias for @link OnestepUnformBuilder.Object NXOpen.BodyDes.OnestepUnformBuilder.Object@endlink
OnestepUnformBuilderObject = OnestepUnformBuilder.Object


##  @link OnestepUnformBuilderPart NXOpen.BodyDes.OnestepUnformBuilderPart @endlink is an alias for @link OnestepUnformBuilder.Part NXOpen.BodyDes.OnestepUnformBuilder.Part@endlink
OnestepUnformBuilderPart = OnestepUnformBuilder.Part


##  @link OnestepUnformBuilderProcess NXOpen.BodyDes.OnestepUnformBuilderProcess @endlink is an alias for @link OnestepUnformBuilder.Process NXOpen.BodyDes.OnestepUnformBuilder.Process@endlink
OnestepUnformBuilderProcess = OnestepUnformBuilder.Process


##  @link OnestepUnformBuilderSurface NXOpen.BodyDes.OnestepUnformBuilderSurface @endlink is an alias for @link OnestepUnformBuilder.Surface NXOpen.BodyDes.OnestepUnformBuilder.Surface@endlink
OnestepUnformBuilderSurface = OnestepUnformBuilder.Surface


##  @link OnestepUnformBuilderUnfoldMode NXOpen.BodyDes.OnestepUnformBuilderUnfoldMode @endlink is an alias for @link OnestepUnformBuilder.UnfoldMode NXOpen.BodyDes.OnestepUnformBuilder.UnfoldMode@endlink
OnestepUnformBuilderUnfoldMode = OnestepUnformBuilder.UnfoldMode


