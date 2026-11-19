from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
##  Represents a @link NXOpen::Positioning::ComponentConstraintGroupBuilder NXOpen::Positioning::ComponentConstraintGroupBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::Assemblies::ComponentAssembly::CreateConstraintGroupBuilder  NXOpen::Assemblies::ComponentAssembly::CreateConstraintGroupBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ConstraintCollectionType </term> <description> 
##  
## BetweenSelectedComponents </description> </item> 
## 
## <item><term> 
##  
## RememberComponentState </term> <description> 
##  
## true </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.0.1  <br> 

class ComponentConstraintGroupBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.Positioning.ComponentConstraintGroupBuilder</ja_class> builder """


    ## Getter for property: (@link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink) ConstraintCollectionType
    ##  Returns the constraint collection types   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## @return ComponentConstraintGroup.ConstraintsCollectionType
    @property
    def ConstraintCollectionType(self) -> ComponentConstraintGroup.ConstraintsCollectionType:
        """
        Getter for property: (@link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink) ConstraintCollectionType
         Returns the constraint collection types   
            
         
        """
        pass
    
    ## Setter for property: (@link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink) ConstraintCollectionType

    ##  Returns the constraint collection types   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    @ConstraintCollectionType.setter
    def ConstraintCollectionType(self, constraintCollectionType: ComponentConstraintGroup.ConstraintsCollectionType):
        """
        Setter for property: (@link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink) ConstraintCollectionType
         Returns the constraint collection types   
            
         
        """
        pass
    
    ## Getter for property: (str) ConstraintGroupName
    ##  Returns the name of constraint group   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## @return str
    @property
    def ConstraintGroupName(self) -> str:
        """
        Getter for property: (str) ConstraintGroupName
         Returns the name of constraint group   
            
         
        """
        pass
    
    ## Setter for property: (str) ConstraintGroupName

    ##  Returns the name of constraint group   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    @ConstraintGroupName.setter
    def ConstraintGroupName(self, nameOfConstraintGroup: str):
        """
        Setter for property: (str) ConstraintGroupName
         Returns the name of constraint group   
            
         
        """
        pass
    
    ## Getter for property: (bool) RememberComponentState
    ##  Returns the toggle to remember selected component   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## @return bool
    @property
    def RememberComponentState(self) -> bool:
        """
        Getter for property: (bool) RememberComponentState
         Returns the toggle to remember selected component   
            
         
        """
        pass
    
    ## Setter for property: (bool) RememberComponentState

    ##  Returns the toggle to remember selected component   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    @RememberComponentState.setter
    def RememberComponentState(self, rememberComponentState: bool):
        """
        Setter for property: (bool) RememberComponentState
         Returns the toggle to remember selected component   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedComponentList
    ##  Returns the selected components list   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectedComponentList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedComponentList
         Returns the selected components list   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedConstraintsList
    ##  Returns the selected constraint list   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectedConstraintsList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedConstraintsList
         Returns the selected constraint list   
            
         
        """
        pass
    
    ## 
    ##             Gets the context component which is used to decide the displayed constraints that can be in the
    ##             selected constraints list. The context component is only set by the creator and can be NULL.
    ##             If the context component is NULL the displayed constraints will be in same part as the
    ##             constraint group.
    ##         
    ##  @return component (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink): .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetContextComponent(self) -> NXOpen.Assemblies.Component:
        """
        
                    Gets the context component which is used to decide the displayed constraints that can be in the
                    selected constraints list. The context component is only set by the creator and can be NULL.
                    If the context component is NULL the displayed constraints will be in same part as the
                    constraint group.
                
         @return component (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
## 
##         Constraint group which represents a group of component constraints in NX.
##     
## 
##   <br>  Created in NX8.0.1  <br> 

class ComponentConstraintGroup(NXOpen.NXObject): 
    """
        Constraint group which represents a group of component constraints in NX.
    """


    ##  the enum to define constraint collection type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## BetweenSelectedComponents</term><description> 
    ## </description> </item><item><term> 
    ## ConnectedToSelectedComponents</term><description> 
    ## </description> </item></list>
    class ConstraintsCollectionType(Enum):
        """
        Members Include: <BetweenSelectedComponents> <ConnectedToSelectedComponents>
        """
        BetweenSelectedComponents: int
        ConnectedToSelectedComponents: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ComponentConstraintGroup.ConstraintsCollectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## 
    ##             Gets the type of constraint collection that is performed using the defining components.
    ##         
    ##  @return constraintCollectionType (@link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink): .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetConstraintCollectionType(self) -> ComponentConstraintGroup.ConstraintsCollectionType:
        """
        
                    Gets the type of constraint collection that is performed using the defining components.
                
         @return constraintCollectionType (@link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink): .
        """
        pass
    
    ## 
    ##             Returns the defining components within the group.
    ##         
    ##  @return components (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink):  Defining components .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetDefiningComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
        
                    Returns the defining components within the group.
                
         @return components (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink):  Defining components .
        """
        pass
    
    ## 
    ##             Returns the defining constraints within the group.
    ##         
    ##  @return constraints (@link ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink):  Defining constraints .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetDefiningConstraints(self) -> List[ComponentConstraint]:
        """
        
                    Returns the defining constraints within the group.
                
         @return constraints (@link ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink):  Defining constraints .
        """
        pass
    
    ## 
    ##             Returns the member constraints present in the group. The member constraints are generated from the defining
    ##             constraints and components. This attribute cannot be set directly.
    ##         
    ##  @return constraints (@link ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink):  Member constraints .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetMemberConstraints(self) -> List[ComponentConstraint]:
        """
        
                    Returns the member constraints present in the group. The member constraints are generated from the defining
                    constraints and components. This attribute cannot be set directly.
                
         @return constraints (@link ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink):  Member constraints .
        """
        pass
    
    ## 
    ##             Gets the state which indicates if defining components are remembered when updating the member constraints.
    ##         
    ##  @return rememberComponentState (bool): .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetRememberComponentState(self) -> bool:
        """
        
                    Gets the state which indicates if defining components are remembered when updating the member constraints.
                
         @return rememberComponentState (bool): .
        """
        pass
    
    ## 
    ##             Sets the type of constraint collection that is performed using the defining components.
    ##         
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraintCollectionType"> (@link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink) </param>
    def SetConstraintCollectionType(self, constraintCollectionType: ComponentConstraintGroup.ConstraintsCollectionType) -> None:
        """
        
                    Sets the type of constraint collection that is performed using the defining components.
                
        """
        pass
    
    ## 
    ##             Sets the defining constraints within the group.
    ##         
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraints"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink)  Defining components </param>
    def SetDefiningComponents(self, constraints: List[NXOpen.Assemblies.Component]) -> None:
        """
        
                    Sets the defining constraints within the group.
                
        """
        pass
    
    ## 
    ##             Sets the defining constraints within the group.
    ##         
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraints"> (@link ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink)  Defining constraints </param>
    def SetDefiningConstraints(self, constraints: List[ComponentConstraint]) -> None:
        """
        
                    Sets the defining constraints within the group.
                
        """
        pass
    
    ## 
    ##             Sets the state which indicates if defining components are remembered when updating the member constraints.
    ##         
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="rememberComponentState"> (bool) </param>
    def SetRememberComponentState(self, rememberComponentState: bool) -> None:
        """
        
                    Sets the state which indicates if defining components are remembered when updating the member constraints.
                
        """
        pass
    
    ## 
    ##             Updates the member constraints so that they match the definition implied by the defining constraints,
    ##             defining components and associated constraint collection type.
    ##         
    ##  @return changed (bool):  True if the member constraints have been changed by update .
    ## 
    ##   <br>  Created in NX8.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def UpdateMemberConstraints(self) -> bool:
        """
        
                    Updates the member constraints so that they match the definition implied by the defining constraints,
                    defining components and associated constraint collection type.
                
         @return changed (bool):  True if the member constraints have been changed by update .
        """
        pass
    
import NXOpen.Assemblies
## 
##     Constraint for use in positioning assembly objects in NX.
##     

## 
##   <br>  Created in NX5.0.1  <br> 

class ComponentConstraint(Constraint): 
    """
    Constraint for use in positioning assembly objects in NX.
    
"""


    ##  Specifies how a constraint affects the positioning of a component.
    ##     
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  No information available </description> </item><item><term> 
    ## Toward</term><description> 
    ##  Toward fixed geometry </description> </item><item><term> 
    ## AwayFrom</term><description> 
    ##  Away from fixed geometry </description> </item><item><term> 
    ## NothingFixed</term><description> 
    ##  The network does not contain any fixed geometry </description> </item><item><term> 
    ## Fix</term><description> 
    ##  The constraint is a @link NXOpen::Positioning::Constraint::TypeFix NXOpen::Positioning::Constraint::TypeFix@endlink  </description> </item><item><term> 
    ## Suppressed</term><description> 
    ##  The constraint is suppressed </description> </item><item><term> 
    ## IgnoredInArrangement</term><description> 
    ##  The current arrangement ignores all constraints </description> </item></list>
    class DirectionToFixed(Enum):
        """
        Members Include: <Unknown> <Toward> <AwayFrom> <NothingFixed> <Fix> <Suppressed> <IgnoredInArrangement>
        """
        Unknown: int
        Toward: int
        AwayFrom: int
        NothingFixed: int
        Fix: int
        Suppressed: int
        IgnoredInArrangement: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ComponentConstraint.DirectionToFixed:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) ArrangementSpecific
    ##  Returns
    ##         the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
    ##         @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink .  
    ##     Constraints can
    ##         never be arrangement specific in piece parts.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return bool
    @property
    def ArrangementSpecific(self) -> bool:
        """
        Getter for property: (bool) ArrangementSpecific
         Returns
                the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
                @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink .  
            Constraints can
                never be arrangement specific in piece parts.
              
         
        """
        pass
    
    ## Setter for property: (bool) ArrangementSpecific

    ##  Returns
    ##         the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
    ##         @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink .  
    ##     Constraints can
    ##         never be arrangement specific in piece parts.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @ArrangementSpecific.setter
    def ArrangementSpecific(self, arrangement_specific: bool):
        """
        Setter for property: (bool) ArrangementSpecific
         Returns
                the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
                @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink .  
            Constraints can
                never be arrangement specific in piece parts.
              
         
        """
        pass
    
    ## 
    ##         Given an inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  created because of Positioning Overrides, create a new constraint copied
    ##         from it in the same part.  Unlike the inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink , the new constraint can be modified by the
    ##         user in the same ways as a normal constraint.  (Inherited constraints can be suppressed or unsuppressed, but are otherwise read-only.)
    ## 
    ##         If the constraint is not an inherited constraint, an error is raised.
    ##     
    ##  @return newConstraint (@link ComponentConstraint NXOpen.Positioning.ComponentConstraint@endlink):  The new @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  copied from the inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the same part. .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def CopyInheritedToOverride(self) -> ComponentConstraint:
        """
        
                Given an inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  created because of Positioning Overrides, create a new constraint copied
                from it in the same part.  Unlike the inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink , the new constraint can be modified by the
                user in the same ways as a normal constraint.  (Inherited constraints can be suppressed or unsuppressed, but are otherwise read-only.)
        
                If the constraint is not an inherited constraint, an error is raised.
            
         @return newConstraint (@link ComponentConstraint NXOpen.Positioning.ComponentConstraint@endlink):  The new @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  copied from the inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the same part. .
        """
        pass
    
    ## 
    ##         Given an inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  created because of Positioning Overrides, create a new constraint copied
    ##         from it in the same part.  Unlike the inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink , the new constraint can be modified by the
    ##         user in the same ways as a normal constraint.  (Inherited constraints can be suppressed or unsuppressed, but are otherwise read-only.)
    ## 
    ##         If the constraint is not an inherited constraint, an error is raised.
    ##     
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1847.0.0.  Use @link ComponentConstraint::CopyInheritedToOverride ComponentConstraint::CopyInheritedToOverride@endlink  instead.  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def CopyToOverride(self) -> None:
        """
        
                Given an inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  created because of Positioning Overrides, create a new constraint copied
                from it in the same part.  Unlike the inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink , the new constraint can be modified by the
                user in the same ways as a normal constraint.  (Inherited constraints can be suppressed or unsuppressed, but are otherwise read-only.)
        
                If the constraint is not an inherited constraint, an error is raised.
            
        """
        pass
    
    ## 
    ##         Get the @link NXOpen::Positioning::ComponentConstraint::DirectionToFixed NXOpen::Positioning::ComponentConstraint::DirectionToFixed@endlink  value of the @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink 
    ##         given a component and an arrangement.
    ##         This value specifies how a constraint affects the positioning of a component.
    ##         If the arrangement is null, the "direction to fixed" value will be evaluated based on the default arrangement.
    ##     
    ##  @return direction_to_fixed (@link ComponentConstraint.DirectionToFixed NXOpen.Positioning.ComponentConstraint.DirectionToFixed@endlink):  The @link NXOpen::Positioning::ComponentConstraint::DirectionToFixed NXOpen::Positioning::ComponentConstraint::DirectionToFixed@endlink  value. .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="component"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  The component constrained to the specified constraint. </param>
    ## <param name="arrangement"> (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink)  The @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the constraint state is being evaluated. </param>
    def GetDirectionToFixed(self, component: NXOpen.Assemblies.Component, arrangement: NXOpen.Assemblies.Arrangement) -> ComponentConstraint.DirectionToFixed:
        """
        
                Get the @link NXOpen::Positioning::ComponentConstraint::DirectionToFixed NXOpen::Positioning::ComponentConstraint::DirectionToFixed@endlink  value of the @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink 
                given a component and an arrangement.
                This value specifies how a constraint affects the positioning of a component.
                If the arrangement is null, the "direction to fixed" value will be evaluated based on the default arrangement.
            
         @return direction_to_fixed (@link ComponentConstraint.DirectionToFixed NXOpen.Positioning.ComponentConstraint.DirectionToFixed@endlink):  The @link NXOpen::Positioning::ComponentConstraint::DirectionToFixed NXOpen::Positioning::ComponentConstraint::DirectionToFixed@endlink  value. .
        """
        pass
    
    ## 
    ##         Get whether this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  is 
    ##         an inherited constraint. An inherited constraint is created by the system 
    ##         to support Positioning Overrides. 
    ##     
    ##  @return inherited (bool):  The inherited state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetInherited(self) -> bool:
        """
        
                Get whether this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  is 
                an inherited constraint. An inherited constraint is created by the system 
                to support Positioning Overrides. 
            
         @return inherited (bool):  The inherited state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  .
        """
        pass
    
    ## 
    ##         An inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  can be suppressed independently of the constraint it is
    ##         derived from.  When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
    ##         of the constraint it is derived from.  This method returns true for an inherited constraint in this state.  It does not indicate
    ##         if the constraint is inherited or not: use @link NXOpen::Positioning::Constraint::Suppressed NXOpen::Positioning::Constraint::Suppressed@endlink  for this.
    ## 
    ##         Given a non-inherited constraint, this will return false.
    ##     
    ##  @return separate_suppression (bool):  The separate suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetSeparateSuppression(self) -> bool:
        """
        
                An inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  can be suppressed independently of the constraint it is
                derived from.  When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
                of the constraint it is derived from.  This method returns true for an inherited constraint in this state.  It does not indicate
                if the constraint is inherited or not: use @link NXOpen::Positioning::Constraint::Suppressed NXOpen::Positioning::Constraint::Suppressed@endlink  for this.
        
                Given a non-inherited constraint, this will return false.
            
         @return separate_suppression (bool):  The separate suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  .
        """
        pass
    
    ## 
    ##         Get the shared suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  used across all 
    ##         arrangements where the constraint is not arrangement specific.
    ##     
    ##  @return suppressed (bool):   The suppression state. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetSharedSuppressed(self) -> bool:
        """
        
                Get the shared suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  used across all 
                arrangements where the constraint is not arrangement specific.
            
         @return suppressed (bool):   The suppression state. .
        """
        pass
    
    ## 
    ##         Get the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
    ##         specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .
    ##     
    ##  @return arrangement_specific (bool):   The arrangement specific state. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="arrangement"> (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink)   The @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the arrangement specific state is being enquired. </param>
    def GetSpecificInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement) -> bool:
        """
        
                Get the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
                specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .
            
         @return arrangement_specific (bool):   The arrangement specific state. .
        """
        pass
    
    ## 
    ##         Get the suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
    ##         specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .  If the constraint is not arrangement
    ##         specific in this arrangement then the shared suppression state, used across all 
    ##         arrangements where the constraint is not arrangement specific, is used.
    ##     
    ##  @return suppressed (bool):   The suppression state. .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="arrangement"> (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink)   The @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the suppression state is being enquired. </param>
    def GetSuppressedInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement) -> bool:
        """
        
                Get the suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
                specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .  If the constraint is not arrangement
                specific in this arrangement then the shared suppression state, used across all 
                arrangements where the constraint is not arrangement specific, is used.
            
         @return suppressed (bool):   The suppression state. .
        """
        pass
    
    ## 
    ##         Remembers the constraint in the prototype part of a referenced component
    ##         for reuse in other occurrences of the part. Fix and Bond constraints are
    ##         never remembered.  If the constraint does not reference geometry in the
    ##         component, it is not remembered.
    ##     
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="component"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  The @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  on which the constraint is remembered </param>
    def RememberOnComponent(self, component: NXOpen.Assemblies.Component) -> None:
        """
        
                Remembers the constraint in the prototype part of a referenced component
                for reuse in other occurrences of the part. Fix and Bond constraints are
                never remembered.  If the constraint does not reference geometry in the
                component, it is not remembered.
            
        """
        pass
    
    ## 
    ##         An inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  can be suppressed independently of the constraint it is
    ##         derived from.  When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
    ##         of the constraint it is derived from.  This method sets this state on an inherited constraint.  Setting this flag will not in
    ##         itself suppress or unsuppress the inherited constraint: use @link NXOpen::Positioning::Constraint::Suppressed NXOpen::Positioning::Constraint::Suppressed@endlink  for this.
    ## 
    ##         If the constraint is not an inherited constraint, an error is raised.
    ##     
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="separate_suppression"> (bool) </param>
    def SetSeparateSuppression(self, separate_suppression: bool) -> None:
        """
        
                An inherited @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  can be suppressed independently of the constraint it is
                derived from.  When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
                of the constraint it is derived from.  This method sets this state on an inherited constraint.  Setting this flag will not in
                itself suppress or unsuppress the inherited constraint: use @link NXOpen::Positioning::Constraint::Suppressed NXOpen::Positioning::Constraint::Suppressed@endlink  for this.
        
                If the constraint is not an inherited constraint, an error is raised.
            
        """
        pass
    
    ## 
    ##         Set the shared suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  used across all 
    ##         arrangements where the constraint is not arrangement specific.
    ##     
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="suppressed"> (bool)   The suppression state. </param>
    def SetSharedSuppressed(self, suppressed: bool) -> None:
        """
        
                Set the shared suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  used across all 
                arrangements where the constraint is not arrangement specific.
            
        """
        pass
    
    ## 
    ##         Set the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
    ##         specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .
    ##     
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="arrangement"> (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink)   The @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the arrangement specific state is being set. </param>
    ## <param name="arrangement_specific"> (bool)   The arrangement specific state. </param>
    def SetSpecificInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement, arrangement_specific: bool) -> None:
        """
        
                Set the arrangement specific state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
                specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .
            
        """
        pass
    
    ## 
    ##         Set the suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
    ##         specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .  If the constraint is not arrangement
    ##         specific in this arrangement then the shared suppression state, used across all 
    ##         arrangements where the constraint is not arrangement specific, is set.
    ##     
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="arrangement"> (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink)   The @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the suppression state is being set. </param>
    ## <param name="suppressed"> (bool)   The suppression state. </param>
    def SetSuppressedInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement, suppressed: bool) -> None:
        """
        
                Set the suppression state of this @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  in the 
                specified @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink .  If the constraint is not arrangement
                specific in this arrangement then the shared suppression state, used across all 
                arrangements where the constraint is not arrangement specific, is set.
            
        """
        pass
    
## 
##         Network for use in positioning components in NX.
##         A component network extends the @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  by
##         adding support for @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink s.
##      <br> Use @link NXOpen::Positioning::Positioner::EstablishNetwork NXOpen::Positioning::Positioner::EstablishNetwork@endlink  to create an instance of this class.  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class ComponentNetwork(Network): 
    """
        Network for use in positioning components in NX.
        A component network extends the <ja_class>NXOpen.Positioning.Network</ja_class> by
        adding support for <ja_class>NXOpen.Assemblies.Arrangement</ja_class>s.
    """


    ##  
    ##             Specifies how changes in the network are applied to arrangements. 
    ##             This setting will be ignored when positioning geometry in a piece part.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Existing</term><description> 
    ##  Apply transforms in arrangements according to existing component properties.
    ##                                                                                 Constraints are created non-arrangement specific. </description> </item><item><term> 
    ## InUsed</term><description> 
    ##  Apply transforms in the used arrangement only. 
    ##                                                                                 Constraints are created arrangement specific in the used arrangement 
    ##                                                                                 and suppressed in all other arrangements</description> </item></list>
    class ArrangementsMode(Enum):
        """
        Members Include: <Existing> <InUsed>
        """
        Existing: int
        InUsed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ComponentNetwork.ArrangementsMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ComponentNetwork.ArrangementsMode NXOpen.Positioning.ComponentNetwork.ArrangementsMode@endlink) NetworkArrangementsMode
    ##  Returns
    ##             the arrangements mode for this network.  
    ##   
    ##           
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return ComponentNetwork.ArrangementsMode
    @property
    def NetworkArrangementsMode(self) -> ComponentNetwork.ArrangementsMode:
        """
        Getter for property: (@link ComponentNetwork.ArrangementsMode NXOpen.Positioning.ComponentNetwork.ArrangementsMode@endlink) NetworkArrangementsMode
         Returns
                    the arrangements mode for this network.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link ComponentNetwork.ArrangementsMode NXOpen.Positioning.ComponentNetwork.ArrangementsMode@endlink) NetworkArrangementsMode

    ##  Returns
    ##             the arrangements mode for this network.  
    ##   
    ##           
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @NetworkArrangementsMode.setter
    def NetworkArrangementsMode(self, mode: ComponentNetwork.ArrangementsMode):
        """
        Setter for property: (@link ComponentNetwork.ArrangementsMode NXOpen.Positioning.ComponentNetwork.ArrangementsMode@endlink) NetworkArrangementsMode
         Returns
                    the arrangements mode for this network.  
          
                  
         
        """
        pass
    
    ## Getter for property: (bool) NetworkSolveInWorksetMode
    ##  Returns
    ##             the mode that moves components in the workset instead of the model.  
    ##   
    ##           
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def NetworkSolveInWorksetMode(self) -> bool:
        """
        Getter for property: (bool) NetworkSolveInWorksetMode
         Returns
                    the mode that moves components in the workset instead of the model.  
          
                  
         
        """
        pass
    
    ## Setter for property: (bool) NetworkSolveInWorksetMode

    ##  Returns
    ##             the mode that moves components in the workset instead of the model.  
    ##   
    ##           
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NetworkSolveInWorksetMode.setter
    def NetworkSolveInWorksetMode(self, solveInWorkset: bool):
        """
        Setter for property: (bool) NetworkSolveInWorksetMode
         Returns
                    the mode that moves components in the workset instead of the model.  
          
                  
         
        """
        pass
    
import NXOpen.Assemblies
## 
##   An instance of this class can be used to create @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink s and
##   associated objects.
##  <br> To obtain an instance of this class, use @link NXOpen::Assemblies::ComponentAssembly::Positioner  NXOpen::Assemblies::ComponentAssembly::Positioner @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class ComponentPositioner(Positioner): 
    """
  An instance of this class can be used to create <ja_class>NXOpen.Positioning.Constraint</ja_class>s and
  associated objects.
"""


    ## Getter for property: (bool) DisplayConstraints
    ##  Returns
    ##         the flag indicating whether constraints in the part of this positioner
    ##         are to be displayed on the graphics window or not.  
    ##     (This is a separate
    ##         system from hiding and showing individual constraints.)  This flag controls the
    ##         visibility of both suppressed and unsuppressed constraints.
    ## 
    ##         After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
    ##         should be called to refresh the constraint display.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def DisplayConstraints(self) -> bool:
        """
        Getter for property: (bool) DisplayConstraints
         Returns
                the flag indicating whether constraints in the part of this positioner
                are to be displayed on the graphics window or not.  
            (This is a separate
                system from hiding and showing individual constraints.)  This flag controls the
                visibility of both suppressed and unsuppressed constraints.
        
                After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
                should be called to refresh the constraint display.
              
         
        """
        pass
    
    ## Setter for property: (bool) DisplayConstraints

    ##  Returns
    ##         the flag indicating whether constraints in the part of this positioner
    ##         are to be displayed on the graphics window or not.  
    ##     (This is a separate
    ##         system from hiding and showing individual constraints.)  This flag controls the
    ##         visibility of both suppressed and unsuppressed constraints.
    ## 
    ##         After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
    ##         should be called to refresh the constraint display.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DisplayConstraints.setter
    def DisplayConstraints(self, display: bool):
        """
        Setter for property: (bool) DisplayConstraints
         Returns
                the flag indicating whether constraints in the part of this positioner
                are to be displayed on the graphics window or not.  
            (This is a separate
                system from hiding and showing individual constraints.)  This flag controls the
                visibility of both suppressed and unsuppressed constraints.
        
                After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
                should be called to refresh the constraint display.
              
         
        """
        pass
    
    ## Getter for property: (bool) DisplaySuppressedConstraints
    ##  Returns
    ##         the flag indicating whether suppressed constraints in the part of this positioner
    ##         are to be displayed on the graphics window or not.  
    ##     (This is a separate
    ##         system from hiding and showing individual constraints.)
    ## 
    ##         After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
    ##         should be called to refresh the constraint display.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def DisplaySuppressedConstraints(self) -> bool:
        """
        Getter for property: (bool) DisplaySuppressedConstraints
         Returns
                the flag indicating whether suppressed constraints in the part of this positioner
                are to be displayed on the graphics window or not.  
            (This is a separate
                system from hiding and showing individual constraints.)
        
                After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
                should be called to refresh the constraint display.
              
         
        """
        pass
    
    ## Setter for property: (bool) DisplaySuppressedConstraints

    ##  Returns
    ##         the flag indicating whether suppressed constraints in the part of this positioner
    ##         are to be displayed on the graphics window or not.  
    ##     (This is a separate
    ##         system from hiding and showing individual constraints.)
    ## 
    ##         After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
    ##         should be called to refresh the constraint display.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @DisplaySuppressedConstraints.setter
    def DisplaySuppressedConstraints(self, display: bool):
        """
        Setter for property: (bool) DisplaySuppressedConstraints
         Returns
                the flag indicating whether suppressed constraints in the part of this positioner
                are to be displayed on the graphics window or not.  
            (This is a separate
                system from hiding and showing individual constraints.)
        
                After changing this flag @link NXOpen::DisplayableObject::RedisplayObject NXOpen::DisplayableObject::RedisplayObject@endlink 
                should be called to refresh the constraint display.
              
         
        """
        pass
    
    ## Getter for property: (bool) MoveDumbGeometry
    ##  Returns the flag that enables the positioner to reposition dumb geometry.  
    ##     Dumb geometry
    ##         is any geometry that is not controlled by another object such as a 
    ##         @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  object.  This flag has no effect
    ##         on Routing geometry (segments and control points) as they are always considered
    ##         movable by the positioner.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return bool
    @property
    def MoveDumbGeometry(self) -> bool:
        """
        Getter for property: (bool) MoveDumbGeometry
         Returns the flag that enables the positioner to reposition dumb geometry.  
            Dumb geometry
                is any geometry that is not controlled by another object such as a 
                @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  object.  This flag has no effect
                on Routing geometry (segments and control points) as they are always considered
                movable by the positioner.
              
         
        """
        pass
    
    ## Setter for property: (bool) MoveDumbGeometry

    ##  Returns the flag that enables the positioner to reposition dumb geometry.  
    ##     Dumb geometry
    ##         is any geometry that is not controlled by another object such as a 
    ##         @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  object.  This flag has no effect
    ##         on Routing geometry (segments and control points) as they are always considered
    ##         movable by the positioner.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @MoveDumbGeometry.setter
    def MoveDumbGeometry(self, move_dumb_geometry: bool):
        """
        Setter for property: (bool) MoveDumbGeometry
         Returns the flag that enables the positioner to reposition dumb geometry.  
            Dumb geometry
                is any geometry that is not controlled by another object such as a 
                @link NXOpen::Features::Feature NXOpen::Features::Feature@endlink  object.  This flag has no effect
                on Routing geometry (segments and control points) as they are always considered
                movable by the positioner.
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink) PrimaryArrangement
    ##  Returns 
    ##         the @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the 
    ##         primary @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  will solve.  
    ##   
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return NXOpen.Assemblies.Arrangement
    @property
    def PrimaryArrangement(self) -> NXOpen.Assemblies.Arrangement:
        """
        Getter for property: (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink) PrimaryArrangement
         Returns 
                the @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the 
                primary @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  will solve.  
          
              
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink) PrimaryArrangement

    ##  Returns 
    ##         the @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the 
    ##         primary @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  will solve.  
    ##   
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @PrimaryArrangement.setter
    def PrimaryArrangement(self, arrangement: NXOpen.Assemblies.Arrangement):
        """
        Setter for property: (@link NXOpen.Assemblies.Arrangement NXOpen.Assemblies.Arrangement@endlink) PrimaryArrangement
         Returns 
                the @link NXOpen::Assemblies::Arrangement NXOpen::Assemblies::Arrangement@endlink  in which the 
                primary @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  will solve.  
          
              
         
        """
        pass
    
    ##  
    ##         Begins a mode of operation where (1) each new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink 
    ##         created by this @link NXOpen::Positioning::ComponentPositioner NXOpen::Positioning::ComponentPositioner@endlink  applies to
    ##         components in the part of the positioner (or to components with variable component positioning
    ##         defined in the part of the positioner) and (2) and component transforms derived from
    ##         a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  will apply to components in the part of the positioner.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def BeginAssemblyConstraints(self) -> None:
        """
         
                Begins a mode of operation where (1) each new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink 
                created by this @link NXOpen::Positioning::ComponentPositioner NXOpen::Positioning::ComponentPositioner@endlink  applies to
                components in the part of the positioner (or to components with variable component positioning
                defined in the part of the positioner) and (2) and component transforms derived from
                a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  will apply to components in the part of the positioner.
            
        """
        pass
    
    ##  
    ##         Begins a mode of operation where (1) each new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink 
    ##         is created as transient and (2) a component transform is applied at the level where 
    ##         position is controlled for the component, typically in the component's immediate parent.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def BeginMoveComponent(self) -> None:
        """
         
                Begins a mode of operation where (1) each new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink 
                is created as transient and (2) a component transform is applied at the level where 
                position is controlled for the component, typically in the component's immediate parent.
            
        """
        pass
    
    ## 
    ##         Begins a mode of operation where (1) each new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink 
    ##         is created as transient and (2) a component transform is applied at the workset level.
    ##     
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def BeginMoveComponentInWorkset(self) -> None:
        """
        
                Begins a mode of operation where (1) each new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink 
                is created as transient and (2) a component transform is applied at the workset level.
            
        """
        pass
    
    ##  
    ##         Ends the mode of operation started by 
    ##         @link NXOpen::Positioning::ComponentPositioner::BeginAssemblyConstraints NXOpen::Positioning::ComponentPositioner::BeginAssemblyConstraints@endlink 
    ##         All non-persistent constraints in this @link NXOpen::Positioning::ComponentPositioner NXOpen::Positioning::ComponentPositioner@endlink 
    ##         will be deleted.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def EndAssemblyConstraints(self) -> None:
        """
         
                Ends the mode of operation started by 
                @link NXOpen::Positioning::ComponentPositioner::BeginAssemblyConstraints NXOpen::Positioning::ComponentPositioner::BeginAssemblyConstraints@endlink 
                All non-persistent constraints in this @link NXOpen::Positioning::ComponentPositioner NXOpen::Positioning::ComponentPositioner@endlink 
                will be deleted.
            
        """
        pass
    
    ##  
    ##         Ends the mode of operation started by 
    ##         @link NXOpen::Positioning::ComponentPositioner::BeginMoveComponent NXOpen::Positioning::ComponentPositioner::BeginMoveComponent@endlink 
    ##         All constraints created while in that mode will be deleted.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def EndMoveComponent(self) -> None:
        """
         
                Ends the mode of operation started by 
                @link NXOpen::Positioning::ComponentPositioner::BeginMoveComponent NXOpen::Positioning::ComponentPositioner::BeginMoveComponent@endlink 
                All constraints created while in that mode will be deleted.
            
        """
        pass
    
    ## 
    ##         Ends the mode of operation started by
    ##         @link NXOpen::Positioning::ComponentPositioner::BeginMoveComponentInWorkset NXOpen::Positioning::ComponentPositioner::BeginMoveComponentInWorkset@endlink 
    ##         All constraints created while in that mode will be deleted.
    ##     
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def EndMoveComponentInWorkset(self) -> None:
        """
        
                Ends the mode of operation started by
                @link NXOpen::Positioning::ComponentPositioner::BeginMoveComponentInWorkset NXOpen::Positioning::ComponentPositioner::BeginMoveComponentInWorkset@endlink 
                All constraints created while in that mode will be deleted.
            
        """
        pass
    
    ## 
    ##         Attempts to load all the parts that contain unloaded geometry that is referenced by the constraints
    ##         or by any related constraints. The constraints must be within the positioner otherwise an error will be
    ##         raised. Any constraints that are suppressed will be ignored.
    ## 
    ##         If the number of constraints is zero then the function attempts to load the parts for every unsuppressed
    ##         constraint in the positioner.
    ## 
    ##         Calling this function can cause objects to be logged for update and therefore the caller of this function
    ##         must call update.
    ##     
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraints"> (@link ComponentConstraint List[NXOpen.Positioning.ComponentConstraint]@endlink)  Constraints </param>
    def LoadConstraintGeometry(self, constraints: List[ComponentConstraint]) -> None:
        """
        
                Attempts to load all the parts that contain unloaded geometry that is referenced by the constraints
                or by any related constraints. The constraints must be within the positioner otherwise an error will be
                raised. Any constraints that are suppressed will be ignored.
        
                If the number of constraints is zero then the function attempts to load the parts for every unsuppressed
                constraint in the positioner.
        
                Calling this function can cause objects to be logged for update and therefore the caller of this function
                must call update.
            
        """
        pass
    
    ## 
    ##         Solves constraints in all arrangements that are currently postponing 
    ##         their solve. This could lead to updating the model if required.  This call
    ##         will have no effect if assembly constraint update has been delayed. 
    ##     
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def SolvePostponedConstraints(self) -> None:
        """
        
                Solves constraints in all arrangements that are currently postponing 
                their solve. This could lead to updating the model if required.  This call
                will have no effect if assembly constraint update has been delayed. 
            
        """
        pass
    
import NXOpen
## 
##         a collection of constraints    
##      <br> To obtain an instance of this class, refer to @link NXOpen::Positioning::Positioner  NXOpen::Positioning::Positioner @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class ConstraintCollection(NXOpen.TaggedObjectCollection): 
    """
        a collection of constraints    
    """
    pass


import NXOpen
## 
##     ConstraintReference for use in positioning objects in NX.
##     A ConstraintReference is used by a Constraint to determine 
##     the movable object to be positioned by the constraint and
##     the geometry used to define the constraint.
##  <br> To create an instance of this class, use @link NXOpen::Positioning::Constraint::CreateConstraintReference NXOpen::Positioning::Constraint::CreateConstraintReference@endlink .  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class ConstraintReference(NXOpen.NXObject): 
    """
    ConstraintReference for use in positioning objects in NX.
    A ConstraintReference is used by a Constraint to determine 
    the movable object to be positioned by the constraint and
    the geometry used to define the constraint.
"""


    ##  Specifies the order of the constraint reference used in a @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
    ##         Typically the order is set during creation, where the first constraint reference added is "outside"
    ##         and the second "outside".
    ##         For Bond constraints, the order is set to be "unknown" at creation.
    ##     
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  No order specified </description> </item><item><term> 
    ## Inside</term><description> 
    ##  Inside </description> </item><item><term> 
    ## Outside</term><description> 
    ##  Outside </description> </item></list>
    class ConstraintOrder(Enum):
        """
        Members Include: <Unknown> <Inside> <Outside>
        """
        Unknown: int
        Inside: int
        Outside: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstraintReference.ConstraintOrder:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the type of the geometry used in a @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink .
    ##         The type reflects that used in a @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  while it is being
    ##         solved and may be different from that inferred directly from 
    ##         @link NXOpen::Positioning::ConstraintReference::GetGeometry NXOpen::Positioning::ConstraintReference::GetGeometry@endlink . For example we may use
    ##         @link NXOpen::Positioning::ConstraintReference::GeometryTypeLine NXOpen::Positioning::ConstraintReference::GeometryTypeLine@endlink  as an axis when given a cylindrical face as the geometry.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  No geometry suitable for solving </description> </item><item><term> 
    ## Point</term><description> 
    ##  Point </description> </item><item><term> 
    ## Line</term><description> 
    ##  Straight line </description> </item><item><term> 
    ## Circle</term><description> 
    ##  Circle </description> </item><item><term> 
    ## Plane</term><description> 
    ##  Plane </description> </item><item><term> 
    ## Cylinder</term><description> 
    ##  Cylinder </description> </item><item><term> 
    ## Sphere</term><description> 
    ##  Sphere </description> </item><item><term> 
    ## SweepSurface</term><description> 
    ##  Swept surface </description> </item><item><term> 
    ## ParametricSurface</term><description> 
    ##  Parametric surface </description> </item><item><term> 
    ## ParametricCurve</term><description> 
    ##  Parametric curve </description> </item><item><term> 
    ## SplineCurve</term><description> 
    ##  Spline curve </description> </item><item><term> 
    ## Torus</term><description> 
    ##  Torus </description> </item><item><term> 
    ## Cone</term><description> 
    ##  Cone </description> </item><item><term> 
    ## Ellipse</term><description> 
    ##  Ellipse </description> </item><item><term> 
    ## SplineSurface</term><description> 
    ##  Spline surface </description> </item><item><term> 
    ## CoordinateSystem</term><description> 
    ##  Coordinate system </description> </item></list>
    class GeometryType(Enum):
        """
        Members Include: <Unknown> <Point> <Line> <Circle> <Plane> <Cylinder> <Sphere> <SweepSurface> <ParametricSurface> <ParametricCurve> <SplineCurve> <Torus> <Cone> <Ellipse> <SplineSurface> <CoordinateSystem>
        """
        Unknown: int
        Point: int
        Line: int
        Circle: int
        Plane: int
        Cylinder: int
        Sphere: int
        SweepSurface: int
        ParametricSurface: int
        ParametricCurve: int
        SplineCurve: int
        Torus: int
        Cone: int
        Ellipse: int
        SplineSurface: int
        CoordinateSystem: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstraintReference.GeometryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the half space value of one geometry used in a distance constraint.
    ##         This is only used for surface geometries, and it determines which side of the
    ##         surface the distance constraint is measured from.
    ##     
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Infer</term><description> 
    ##  Allow the solver to decide the half space value, or the geometry is not a surface </description> </item><item><term> 
    ## Positive</term><description> 
    ##  Measure to the positive side of the surface </description> </item><item><term> 
    ## Negative</term><description> 
    ##  Measure to the negative side of the surface </description> </item></list>
    class HalfSpace(Enum):
        """
        Members Include: <Infer> <Positive> <Negative>
        """
        Infer: int
        Positive: int
        Negative: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstraintReference.HalfSpace:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link ConstraintReference.HalfSpace NXOpen.Positioning.ConstraintReference.HalfSpace@endlink) ConstraintReferenceHalfSpace
    ##  Returns 
    ##         the half_space value for the constraint reference.  
    ##     This is only used for distance constraints.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## @return ConstraintReference.HalfSpace
    @property
    def ConstraintReferenceHalfSpace(self) -> ConstraintReference.HalfSpace:
        """
        Getter for property: (@link ConstraintReference.HalfSpace NXOpen.Positioning.ConstraintReference.HalfSpace@endlink) ConstraintReferenceHalfSpace
         Returns 
                the half_space value for the constraint reference.  
            This is only used for distance constraints.
              
         
        """
        pass
    
    ## Setter for property: (@link ConstraintReference.HalfSpace NXOpen.Positioning.ConstraintReference.HalfSpace@endlink) ConstraintReferenceHalfSpace

    ##  Returns 
    ##         the half_space value for the constraint reference.  
    ##     This is only used for distance constraints.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    @ConstraintReferenceHalfSpace.setter
    def ConstraintReferenceHalfSpace(self, half_space: ConstraintReference.HalfSpace):
        """
        Setter for property: (@link ConstraintReference.HalfSpace NXOpen.Positioning.ConstraintReference.HalfSpace@endlink) ConstraintReferenceHalfSpace
         Returns 
                the half_space value for the constraint reference.  
            This is only used for distance constraints.
              
         
        """
        pass
    
    ## Getter for property: (bool) GeometryDirectionReversed
    ##  Returns
    ##         whether the direction is reversed with respect to the direction of the geometry.  
    ##   
    ## 
    ##         This property is only used if the underlying geometry can have an associated direction.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def GeometryDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) GeometryDirectionReversed
         Returns
                whether the direction is reversed with respect to the direction of the geometry.  
          
        
                This property is only used if the underlying geometry can have an associated direction.
              
         
        """
        pass
    
    ## Setter for property: (bool) GeometryDirectionReversed

    ##  Returns
    ##         whether the direction is reversed with respect to the direction of the geometry.  
    ##   
    ## 
    ##         This property is only used if the underlying geometry can have an associated direction.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @GeometryDirectionReversed.setter
    def GeometryDirectionReversed(self, geometry_direction_reversed: bool):
        """
        Setter for property: (bool) GeometryDirectionReversed
         Returns
                whether the direction is reversed with respect to the direction of the geometry.  
          
        
                This property is only used if the underlying geometry can have an associated direction.
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HelpPoint
    ##  Returns 
    ##         the help point of the constraint reference.  
    ##   
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def HelpPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HelpPoint
         Returns 
                the help point of the constraint reference.  
          
              
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HelpPoint

    ##  Returns 
    ##         the help point of the constraint reference.  
    ##   
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @HelpPoint.setter
    def HelpPoint(self, help_point: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) HelpPoint
         Returns 
                the help point of the constraint reference.  
          
              
         
        """
        pass
    
    ## Getter for property: (@link ConstraintReference.ConstraintOrder NXOpen.Positioning.ConstraintReference.ConstraintOrder@endlink) Order
    ##  Returns 
    ##         the order of the constraint reference within its constraint.  
    ##    Note that
    ##         this order is not associated with the geometry or with the alignment 
    ##         of the constraint.  It is based on the idea that the constraint has a direction
    ##         from "outside" to "inside".  It does not affect the result of a solve.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ConstraintReference.ConstraintOrder
    @property
    def Order(self) -> ConstraintReference.ConstraintOrder:
        """
        Getter for property: (@link ConstraintReference.ConstraintOrder NXOpen.Positioning.ConstraintReference.ConstraintOrder@endlink) Order
         Returns 
                the order of the constraint reference within its constraint.  
           Note that
                this order is not associated with the geometry or with the alignment 
                of the constraint.  It is based on the idea that the constraint has a direction
                from "outside" to "inside".  It does not affect the result of a solve.
              
         
        """
        pass
    
    ## Getter for property: (@link ConstraintReference.GeometryType NXOpen.Positioning.ConstraintReference.GeometryType@endlink) SolverGeometryType
    ##  Returns 
    ##         the geometry type of the constraint reference used during a solve.  
    ##   
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return ConstraintReference.GeometryType
    @property
    def SolverGeometryType(self) -> ConstraintReference.GeometryType:
        """
        Getter for property: (@link ConstraintReference.GeometryType NXOpen.Positioning.ConstraintReference.GeometryType@endlink) SolverGeometryType
         Returns 
                the geometry type of the constraint reference used during a solve.  
          
              
         
        """
        pass
    
    ## Getter for property: (bool) UsePortRotateFlag
    ##  Returns
    ##         the flag forcing the use of the rotation vector of the 
    ##         referenced @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink  object instead of the alignment vector 
    ##         when solving the constraint system.  
    ##   
    ## 
    ##         Only effective when the referenced geometry is a @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink 
    ##         object.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## @return bool
    @property
    def UsePortRotateFlag(self) -> bool:
        """
        Getter for property: (bool) UsePortRotateFlag
         Returns
                the flag forcing the use of the rotation vector of the 
                referenced @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink  object instead of the alignment vector 
                when solving the constraint system.  
          
        
                Only effective when the referenced geometry is a @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink 
                object.
              
         
        """
        pass
    
    ## Setter for property: (bool) UsePortRotateFlag

    ##  Returns
    ##         the flag forcing the use of the rotation vector of the 
    ##         referenced @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink  object instead of the alignment vector 
    ##         when solving the constraint system.  
    ##   
    ## 
    ##         Only effective when the referenced geometry is a @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink 
    ##         object.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    @UsePortRotateFlag.setter
    def UsePortRotateFlag(self, use_rotate: bool):
        """
        Setter for property: (bool) UsePortRotateFlag
         Returns
                the flag forcing the use of the rotation vector of the 
                referenced @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink  object instead of the alignment vector 
                when solving the constraint system.  
          
        
                Only effective when the referenced geometry is a @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink 
                object.
              
         
        """
        pass
    
    ##  
    ##         Returns the geometry of the constraint reference.  This is the 
    ##         geometry used in any @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  using
    ##         this constraint reference.
    ##     
    ##  @return geometry (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The geometry referenced by the constraint .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetGeometry(self) -> NXOpen.NXObject:
        """
         
                Returns the geometry of the constraint reference.  This is the 
                geometry used in any @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  using
                this constraint reference.
            
         @return geometry (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The geometry referenced by the constraint .
        """
        pass
    
    ##  
    ##         Get the flag indicating whether the constraint reference is one that maintains a direction
    ##         perpendicular to the primary geometry.
    ##         This is only applicable to @link NXOpen::Positioning::Constraint::Type NXOpen::Positioning::Constraint::Type@endlink  
    ##         @link NXOpen::Positioning::Constraint::TypeAlignLock NXOpen::Positioning::Constraint::TypeAlignLock@endlink ,
    ##         @link NXOpen::Positioning::Constraint::TypeHinge NXOpen::Positioning::Constraint::TypeHinge@endlink ,
    ##         @link NXOpen::Positioning::Constraint::TypeSlider NXOpen::Positioning::Constraint::TypeSlider@endlink  and
    ##         @link NXOpen::Positioning::Constraint::TypeCylindrical NXOpen::Positioning::Constraint::TypeCylindrical@endlink .
    ##     
    ##  @return has_perpendicular_vector (bool):  Whether the constraint has a perpendicular vector .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetHasPerpendicularVector(self) -> bool:
        """
         
                Get the flag indicating whether the constraint reference is one that maintains a direction
                perpendicular to the primary geometry.
                This is only applicable to @link NXOpen::Positioning::Constraint::Type NXOpen::Positioning::Constraint::Type@endlink  
                @link NXOpen::Positioning::Constraint::TypeAlignLock NXOpen::Positioning::Constraint::TypeAlignLock@endlink ,
                @link NXOpen::Positioning::Constraint::TypeHinge NXOpen::Positioning::Constraint::TypeHinge@endlink ,
                @link NXOpen::Positioning::Constraint::TypeSlider NXOpen::Positioning::Constraint::TypeSlider@endlink  and
                @link NXOpen::Positioning::Constraint::TypeCylindrical NXOpen::Positioning::Constraint::TypeCylindrical@endlink .
            
         @return has_perpendicular_vector (bool):  Whether the constraint has a perpendicular vector .
        """
        pass
    
    ##  
    ##         Returns the movable object of the constraint reference.
    ##         The movable object determines the object to be 
    ##         positioned by any @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  using
    ##         this constraint reference.
    ##     
    ##  @return movable_object_id (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The object positioned by the constraint .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetMovableObject(self) -> NXOpen.NXObject:
        """
         
                Returns the movable object of the constraint reference.
                The movable object determines the object to be 
                positioned by any @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  using
                this constraint reference.
            
         @return movable_object_id (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The object positioned by the constraint .
        """
        pass
    
    ##  
    ##         Returns the prototype geometry of the constraint reference. 
    ##         This is never an occurrence.
    ##     
    ##  @return geometry (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The prototype geometry referenced by the constraint .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetPrototypeGeometry(self) -> NXOpen.NXObject:
        """
         
                Returns the prototype geometry of the constraint reference. 
                This is never an occurrence.
            
         @return geometry (@link NXOpen.NXObject NXOpen.NXObject@endlink):  The prototype geometry referenced by the constraint .
        """
        pass
    
    ##  
    ##         Get the value of the perpendicular vector, which will be (0,0,0)
    ##         for most constraints apart from @link NXOpen::Positioning::Constraint::TypeAlignLock NXOpen::Positioning::Constraint::TypeAlignLock@endlink ,
    ##         @link NXOpen::Positioning::Constraint::TypeHinge NXOpen::Positioning::Constraint::TypeHinge@endlink ,
    ##         @link NXOpen::Positioning::Constraint::TypeSlider NXOpen::Positioning::Constraint::TypeSlider@endlink  and
    ##         @link NXOpen::Positioning::Constraint::TypeCylindrical NXOpen::Positioning::Constraint::TypeCylindrical@endlink .
    ##     
    ##  @return perpendicular_vector (@link NXOpen.Vector3d NXOpen.Vector3d@endlink):  The value of the perpendicular vector .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetPrototypePerpendicularVector(self) -> NXOpen.Vector3d:
        """
         
                Get the value of the perpendicular vector, which will be (0,0,0)
                for most constraints apart from @link NXOpen::Positioning::Constraint::TypeAlignLock NXOpen::Positioning::Constraint::TypeAlignLock@endlink ,
                @link NXOpen::Positioning::Constraint::TypeHinge NXOpen::Positioning::Constraint::TypeHinge@endlink ,
                @link NXOpen::Positioning::Constraint::TypeSlider NXOpen::Positioning::Constraint::TypeSlider@endlink  and
                @link NXOpen::Positioning::Constraint::TypeCylindrical NXOpen::Positioning::Constraint::TypeCylindrical@endlink .
            
         @return perpendicular_vector (@link NXOpen.Vector3d NXOpen.Vector3d@endlink):  The value of the perpendicular vector .
        """
        pass
    
    ## 
    ##         Get the flag forcing the use of the rotation vector of the 
    ##         referenced @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink  object instead of the alignment vector 
    ##         when solving the constraint system.
    ## 
    ##         Only effective when the referenced geometry is a @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink 
    ##         object.
    ##     
    ##  @return use_rotate (bool):  .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetUsePortRotate(self) -> bool:
        """
        
                Get the flag forcing the use of the rotation vector of the 
                referenced @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink  object instead of the alignment vector 
                when solving the constraint system.
        
                Only effective when the referenced geometry is a @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink 
                object.
            
         @return use_rotate (bool):  .
        """
        pass
    
    ## 
    ##         Returns if the constraint reference should use the axis of the
    ##         geometry (for example a cylindrical face) rather than the surface
    ##     
    ##  @return geometry (bool):  If this reference is using the axis of the geometry .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetUsesGeometryAxis(self) -> bool:
        """
        
                Returns if the constraint reference should use the axis of the
                geometry (for example a cylindrical face) rather than the surface
            
         @return geometry (bool):  If this reference is using the axis of the geometry .
        """
        pass
    
    ## 
    ##         Set a hint to the solver to fix the movable object associated
    ##         with this constraint reference.
    ##         
    ##         The hint is unset when "set" is false.
    ##         
    ##         The hint can only have an effect when the constraint owning this
    ##         constraint reference has been explicitly added to 
    ##         a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink .
    ##         
    ##         The hint is forgotten after an update.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="set"> (bool)  Set or unset the hint </param>
    def SetFixHint(self, set: bool) -> None:
        """
        
                Set a hint to the solver to fix the movable object associated
                with this constraint reference.
                
                The hint is unset when "set" is false.
                
                The hint can only have an effect when the constraint owning this
                constraint reference has been explicitly added to 
                a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink .
                
                The hint is forgotten after an update.
            
        """
        pass
    
    ## 
    ##         Set a hint to the solver to fix the movable object associated
    ##         with this constraint reference.
    ##         
    ##         The hint is unset when "set" is false.
    ##         
    ##         The hint is forgotten after an update.
    ## 
    ##         Ensures that the constraint that owns this reference will
    ##         solve during the next call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="set"> (bool)  Set or unset the hint </param>
    def SetFixHintForUpdate(self, set: bool) -> None:
        """
        
                Set a hint to the solver to fix the movable object associated
                with this constraint reference.
                
                The hint is unset when "set" is false.
                
                The hint is forgotten after an update.
        
                Ensures that the constraint that owns this reference will
                solve during the next call to @link NXOpen::Update::DoUpdate NXOpen::Update::DoUpdate@endlink .
            
        """
        pass
    
    ##  
    ##         Set the value of the perpendicular vector. The value must be a unit vector given in the coordinates
    ##         of the part containing the referenced geometry.
    ##         The perpendicular vector must be set to (0,0,0) for most constraints apart from
    ##         @link NXOpen::Positioning::Constraint::TypeAlignLock NXOpen::Positioning::Constraint::TypeAlignLock@endlink ,
    ##         @link NXOpen::Positioning::Constraint::TypeHinge NXOpen::Positioning::Constraint::TypeHinge@endlink ,
    ##         @link NXOpen::Positioning::Constraint::TypeSlider NXOpen::Positioning::Constraint::TypeSlider@endlink  and
    ##         @link NXOpen::Positioning::Constraint::TypeCylindrical NXOpen::Positioning::Constraint::TypeCylindrical@endlink  which 
    ##         must have a value. An error is raised if this is not the case.
    ## 
    ##         Whenever the constraint is solved, the value of the perpendicular vector may be modified,
    ##         to ensure that the vector is perpendicular to the referenced geometry. 
    ##     
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="perpendicular_vector"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  The value of the perpendicular vector </param>
    def SetPrototypePerpendicularVector(self, perpendicular_vector: NXOpen.Vector3d) -> None:
        """
         
                Set the value of the perpendicular vector. The value must be a unit vector given in the coordinates
                of the part containing the referenced geometry.
                The perpendicular vector must be set to (0,0,0) for most constraints apart from
                @link NXOpen::Positioning::Constraint::TypeAlignLock NXOpen::Positioning::Constraint::TypeAlignLock@endlink ,
                @link NXOpen::Positioning::Constraint::TypeHinge NXOpen::Positioning::Constraint::TypeHinge@endlink ,
                @link NXOpen::Positioning::Constraint::TypeSlider NXOpen::Positioning::Constraint::TypeSlider@endlink  and
                @link NXOpen::Positioning::Constraint::TypeCylindrical NXOpen::Positioning::Constraint::TypeCylindrical@endlink  which 
                must have a value. An error is raised if this is not the case.
        
                Whenever the constraint is solved, the value of the perpendicular vector may be modified,
                to ensure that the vector is perpendicular to the referenced geometry. 
            
        """
        pass
    
import NXOpen
## 
##         Constraints for use in positioning objects in NX.
## 
##         For constraints between components, the subclass @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  should be used by preference.
##      <br> 
##         Some constraint types have an @link NXOpen::Expression NXOpen::Expression@endlink  associated with them, which the user can change to determine the value 
##         of that constraint. This expression applies to distance and angle constraints, and all joint types. The user can choose for this expression 
##         value to be driven by the system, so it will not have a fixed value set by the user.  
##      <br> 
##      <br>         
##         Some constraint types with values can be given limits. If the constraint is driven, the solver will always try to solve it to remain within 
##         those limits, and the constraint will fail if this is not possible. If the constraint is driving, it will have a failure status if its value 
##         is set to violate those limits (though it will still solve the model). 
##      <br> 
##  <br> To create a new instance of this class, use @link NXOpen::Positioning::Positioner::CreateConstraint  NXOpen::Positioning::Positioner::CreateConstraint @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class Constraint(NXOpen.NXObject): 
    """
        Constraints for use in positioning objects in NX.

        For constraints between components, the subclass <ja_class>NXOpen.Positioning.ComponentConstraint</ja_class> should be used by preference.
    <para>
        Some constraint types have an <ja_class>NXOpen.Expression</ja_class> associated with them, which the user can change to determine the value 
        of that constraint. This expression applies to distance and angle constraints, and all joint types. The user can choose for this expression 
        value to be driven by the system, so it will not have a fixed value set by the user.  
    </para>
    <para>        
        Some constraint types with values can be given limits. If the constraint is driven, the solver will always try to solve it to remain within 
        those limits, and the constraint will fail if this is not possible. If the constraint is driving, it will have a failure status if its value 
        is set to violate those limits (though it will still solve the model). 
    </para>
"""


    ##  Specifies alignment of directed geometries used in a constraint. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InferAlign</term><description> 
    ##  Allow the solver to decide the alignment </description> </item><item><term> 
    ## CoAlign</term><description> 
    ##  Directions are the same </description> </item><item><term> 
    ## ContraAlign</term><description> 
    ##  Directions are opposite </description> </item></list>
    class Alignment(Enum):
        """
        Members Include: <InferAlign> <CoAlign> <ContraAlign>
        """
        InferAlign: int
        CoAlign: int
        ContraAlign: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Constraint.Alignment:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the status of a constraint. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NewlyCreated</term><description> 
    ##  Not evaluated or suppressed since creation </description> </item><item><term> 
    ## Suppressed</term><description> 
    ##  Constraint is suppressed </description> </item><item><term> 
    ## OutOfDate</term><description> 
    ##  Needs evaluation </description> </item><item><term> 
    ## OverConstrained</term><description> 
    ##  Conflicts with other constraints </description> </item><item><term> 
    ## NotConsistentDims</term><description> 
    ##  Cannot solve with current dimension values. Model fully defined </description> </item><item><term> 
    ## NotConsistentOther</term><description> 
    ##  Cannot find a solution. Model underdefined </description> </item><item><term> 
    ## NotConsistentUnknown</term><description> 
    ##  Cannot find a solution </description> </item><item><term> 
    ## BetweenFixed</term><description> 
    ##  Attempt to put constraint between two fixed objects </description> </item><item><term> 
    ## NotSolved</term><description> 
    ##  Not evaluated because other parts of the model are over defined or inconsistent </description> </item><item><term> 
    ## Solved</term><description> 
    ##  The constraint is solved and satisfied </description> </item><item><term> 
    ## CannotSolve</term><description> 
    ##  The constraint has invalid geometry and could not be passed to the solver </description> </item><item><term> 
    ## Delayed</term><description> 
    ##  The constraint is delayed and will not solve </description> </item><item><term> 
    ## IgnoredInArrangement</term><description> 
    ##  The current arrangement ignores all constraints and they will not solve </description> </item><item><term> 
    ## InternallyInconsistent</term><description> 
    ##  The constraint references invalid geometry for this constraint type </description> </item><item><term> 
    ## UnloadedGeometry</term><description> 
    ##  The constraint could not solve as some geometry is unloaded </description> </item><item><term> 
    ## PendingConvertedMc</term><description> 
    ##  The constraint has been converted from a mating condition and has not solved since conversion </description> </item><item><term> 
    ## ConflictingWithWave</term><description> 
    ##  The constraint has been suppressed because it's conflicting with WAVE </description> </item><item><term> 
    ## InconsistentLimits</term><description> 
    ##  The constraint has limits that are inconsistent and it could not be passed to the solver </description> </item><item><term> 
    ## BeyondLimits</term><description> 
    ##  The value of the expression of the constraint is beyond its limits and it could not be passed to the solver </description> </item></list>
    class SolverStatus(Enum):
        """
        Members Include: <NewlyCreated> <Suppressed> <OutOfDate> <OverConstrained> <NotConsistentDims> <NotConsistentOther> <NotConsistentUnknown> <BetweenFixed> <NotSolved> <Solved> <CannotSolve> <Delayed> <IgnoredInArrangement> <InternallyInconsistent> <UnloadedGeometry> <PendingConvertedMc> <ConflictingWithWave> <InconsistentLimits> <BeyondLimits>
        """
        NewlyCreated: int
        Suppressed: int
        OutOfDate: int
        OverConstrained: int
        NotConsistentDims: int
        NotConsistentOther: int
        NotConsistentUnknown: int
        BetweenFixed: int
        NotSolved: int
        Solved: int
        CannotSolve: int
        Delayed: int
        IgnoredInArrangement: int
        InternallyInconsistent: int
        UnloadedGeometry: int
        PendingConvertedMc: int
        ConflictingWithWave: int
        InconsistentLimits: int
        BeyondLimits: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Constraint.SolverStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies how the spline points define the shape of the spline. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ByPoles</term><description> 
    ##  Spline points define control points. </description> </item><item><term> 
    ## ByPoints</term><description> 
    ##  Spline points define interpolation/through points. </description> </item><item><term> 
    ## Invalid</term><description> 
    ##  Not a valid spline constraint. </description> </item></list>
    class SplineType(Enum):
        """
        Members Include: <ByPoles> <ByPoints> <Invalid>
        """
        ByPoles: int
        ByPoints: int
        Invalid: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Constraint.SplineType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the type of a constraint. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Undefined</term><description> 
    ##  No type </description> </item><item><term> 
    ## Touch</term><description> 
    ##  Two geometries touch </description> </item><item><term> 
    ## Concentric</term><description> 
    ##  Two geometries share a center and plane </description> </item><item><term> 
    ## Fix</term><description> 
    ##  One movable object fixed </description> </item><item><term> 
    ## Distance</term><description> 
    ##  Two geometries have a specified distance between them </description> </item><item><term> 
    ## Parallel</term><description> 
    ##  Two geometries are parallel </description> </item><item><term> 
    ## Perpendicular</term><description> 
    ##  Two geometries are perpendicular </description> </item><item><term> 
    ## Center12</term><description> 
    ##  One geometry is positioned mid-way between two others </description> </item><item><term> 
    ## Center22</term><description> 
    ##  An implicit plane between two geometries of one movable object is positioned mid-way between two others </description> </item><item><term> 
    ## Angle</term><description> 
    ##  Two geometries have a specified angle between them </description> </item><item><term> 
    ## Fit</term><description> 
    ##  Two geometries are coincident </description> </item><item><term> 
    ## Bond</term><description> 
    ##  A number of movable objects form a rigid group </description> </item><item><term> 
    ## OrientAngle</term><description> 
    ##  Two geometries have a specified angle between them about an axis </description> </item><item><term> 
    ## SplineData</term><description> 
    ##  A spline and its defining points </description> </item><item><term> 
    ## SplineLength</term><description> 
    ##  Constrains the curve length of a spline </description> </item><item><term> 
    ## LinearPattern</term><description> 
    ##  For internal use only </description> </item><item><term> 
    ## CircularPattern</term><description> 
    ##  For internal use only </description> </item><item><term> 
    ## Linear2dPattern</term><description> 
    ##  For internal use only </description> </item><item><term> 
    ## RadiantPattern</term><description> 
    ##  For internal use only </description> </item><item><term> 
    ## AlignLock</term><description> 
    ##  Two geometries are constrained to have a common axis and no rotation about it </description> </item><item><term> 
    ## CommonOffsetTransform</term><description> 
    ##  For internal use only </description> </item><item><term> 
    ## Hinge</term><description> 
    ##  Two objects along an axis of rotation </description> </item><item><term> 
    ## Slider</term><description> 
    ##  Two objects along a linear axis </description> </item><item><term> 
    ## Cylindrical</term><description> 
    ##  Two objects along a rotatable linear axis </description> </item><item><term> 
    ## Ball</term><description> 
    ##  Two objects at a shared point </description> </item><item><term> 
    ## Screw</term><description> 
    ##  For internal use only </description> </item><item><term> 
    ## Gear</term><description> 
    ##  Defines the relative motion between two joints with angular values </description> </item><item><term> 
    ## RackPinion</term><description> 
    ##  Defines the relative motion between a joint with an angular value and a joint with a linear value </description> </item><item><term> 
    ## Cable</term><description> 
    ##  Defines the relative motion between two joints with linear values </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Undefined> <Touch> <Concentric> <Fix> <Distance> <Parallel> <Perpendicular> <Center12> <Center22> <Angle> <Fit> <Bond> <OrientAngle> <SplineData> <SplineLength> <LinearPattern> <CircularPattern> <Linear2dPattern> <RadiantPattern> <AlignLock> <CommonOffsetTransform> <Hinge> <Slider> <Cylindrical> <Ball> <Screw> <Gear> <RackPinion> <Cable>
        """
        Undefined: int
        Touch: int
        Concentric: int
        Fix: int
        Distance: int
        Parallel: int
        Perpendicular: int
        Center12: int
        Center22: int
        Angle: int
        Fit: int
        Bond: int
        OrientAngle: int
        SplineData: int
        SplineLength: int
        LinearPattern: int
        CircularPattern: int
        Linear2dPattern: int
        RadiantPattern: int
        AlignLock: int
        CommonOffsetTransform: int
        Hinge: int
        Slider: int
        Cylindrical: int
        Ball: int
        Screw: int
        Gear: int
        RackPinion: int
        Cable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Constraint.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) Automatic
    ##  Returns the flag marking the constraint as an "automatic" constraint.  
    ##     Automatic constraints are
    ##         constraints created by the system, but are visible and editable by the user.  Automatic
    ##         constraints are automatically deleted when one of the referenced objects are deleted
    ##         by update.   
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def Automatic(self) -> bool:
        """
        Getter for property: (bool) Automatic
         Returns the flag marking the constraint as an "automatic" constraint.  
            Automatic constraints are
                constraints created by the system, but are visible and editable by the user.  Automatic
                constraints are automatically deleted when one of the referenced objects are deleted
                by update.   
         
        """
        pass
    
    ## Setter for property: (bool) Automatic

    ##  Returns the flag marking the constraint as an "automatic" constraint.  
    ##     Automatic constraints are
    ##         constraints created by the system, but are visible and editable by the user.  Automatic
    ##         constraints are automatically deleted when one of the referenced objects are deleted
    ##         by update.   
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Automatic.setter
    def Automatic(self, automatic: bool):
        """
        Setter for property: (bool) Automatic
         Returns the flag marking the constraint as an "automatic" constraint.  
            Automatic constraints are
                constraints created by the system, but are visible and editable by the user.  Automatic
                constraints are automatically deleted when one of the referenced objects are deleted
                by update.   
         
        """
        pass
    
    ## Getter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintAlignment
    ##  Returns 
    ##         the alignment behavior for the constraint.  
    ##   
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return Constraint.Alignment
    @property
    def ConstraintAlignment(self) -> Constraint.Alignment:
        """
        Getter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintAlignment
         Returns 
                the alignment behavior for the constraint.  
          
              
         
        """
        pass
    
    ## Setter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintAlignment

    ##  Returns 
    ##         the alignment behavior for the constraint.  
    ##   
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @ConstraintAlignment.setter
    def ConstraintAlignment(self, alignment: Constraint.Alignment):
        """
        Setter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintAlignment
         Returns 
                the alignment behavior for the constraint.  
          
              
         
        """
        pass
    
    ## Getter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintSecondAlignment
    ##  Returns 
    ##         the second alignment behavior for the constraint.  
    ##   
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return Constraint.Alignment
    @property
    def ConstraintSecondAlignment(self) -> Constraint.Alignment:
        """
        Getter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintSecondAlignment
         Returns 
                the second alignment behavior for the constraint.  
          
              
         
        """
        pass
    
    ## Setter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintSecondAlignment

    ##  Returns 
    ##         the second alignment behavior for the constraint.  
    ##   
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @ConstraintSecondAlignment.setter
    def ConstraintSecondAlignment(self, secondAlignment: Constraint.Alignment):
        """
        Setter for property: (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink) ConstraintSecondAlignment
         Returns 
                the second alignment behavior for the constraint.  
          
              
         
        """
        pass
    
    ## Getter for property: (@link Constraint.Type NXOpen.Positioning.Constraint.Type@endlink) ConstraintType
    ##  Returns 
    ##         the constraint type.  
    ##   
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return Constraint.Type
    @property
    def ConstraintType(self) -> Constraint.Type:
        """
        Getter for property: (@link Constraint.Type NXOpen.Positioning.Constraint.Type@endlink) ConstraintType
         Returns 
                the constraint type.  
          
              
         
        """
        pass
    
    ## Setter for property: (@link Constraint.Type NXOpen.Positioning.Constraint.Type@endlink) ConstraintType

    ##  Returns 
    ##         the constraint type.  
    ##   
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @ConstraintType.setter
    def ConstraintType(self, constraint_type: Constraint.Type):
        """
        Setter for property: (@link Constraint.Type NXOpen.Positioning.Constraint.Type@endlink) ConstraintType
         Returns 
                the constraint type.  
          
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Expression
    ##  Returns 
    ##         the @link NXOpen::Expression NXOpen::Expression@endlink  of a constraint.  
    ##   
    ##         The expression will be unused unless this constraint type supports an expression, 
    ##         such as a distance or angle constraint, or a joint.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Expression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Expression
         Returns 
                the @link NXOpen::Expression NXOpen::Expression@endlink  of a constraint.  
          
                The expression will be unused unless this constraint type supports an expression, 
                such as a distance or angle constraint, or a joint.
              
         
        """
        pass
    
    ## Getter for property: (bool) ExpressionDriven
    ##  Returns 
    ##         the driven state of the expression of a constraint.  
    ##   
    ##         The value of a driven expression can change. Driven expression values are controlled 
    ##         by the solver and cannot be edited by the user. Only certain constraints with an expression
    ##         can have their expression made driven, such as a distance or angle constraint, or a joint.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def ExpressionDriven(self) -> bool:
        """
        Getter for property: (bool) ExpressionDriven
         Returns 
                the driven state of the expression of a constraint.  
          
                The value of a driven expression can change. Driven expression values are controlled 
                by the solver and cannot be edited by the user. Only certain constraints with an expression
                can have their expression made driven, such as a distance or angle constraint, or a joint.
              
         
        """
        pass
    
    ## Setter for property: (bool) ExpressionDriven

    ##  Returns 
    ##         the driven state of the expression of a constraint.  
    ##   
    ##         The value of a driven expression can change. Driven expression values are controlled 
    ##         by the solver and cannot be edited by the user. Only certain constraints with an expression
    ##         can have their expression made driven, such as a distance or angle constraint, or a joint.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ExpressionDriven.setter
    def ExpressionDriven(self, expression_driven: bool):
        """
        Setter for property: (bool) ExpressionDriven
         Returns 
                the driven state of the expression of a constraint.  
          
                The value of a driven expression can change. Driven expression values are controlled 
                by the solver and cannot be edited by the user. Only certain constraints with an expression
                can have their expression made driven, such as a distance or angle constraint, or a joint.
              
         
        """
        pass
    
    ## Getter for property: (bool) LowerLimitEnabled
    ##  Returns 
    ##         the lower limit of the expression of a constraint.  
    ##    
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def LowerLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) LowerLimitEnabled
         Returns 
                the lower limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ## Setter for property: (bool) LowerLimitEnabled

    ##  Returns 
    ##         the lower limit of the expression of a constraint.  
    ##    
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @LowerLimitEnabled.setter
    def LowerLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) LowerLimitEnabled
         Returns 
                the lower limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitExpression
    ##  Returns 
    ##         the lower limit of the expression of a constraint.  
    ##   
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimitExpression
         Returns 
                the lower limit of the expression of a constraint.  
          
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ## Getter for property: (str) LowerLimitRightHandSide
    ##  Returns 
    ##         the lower limit of the expression right hand side of a constraint.  
    ##    
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def LowerLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) LowerLimitRightHandSide
         Returns 
                the lower limit of the expression right hand side of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ## Setter for property: (str) LowerLimitRightHandSide

    ##  Returns 
    ##         the lower limit of the expression right hand side of a constraint.  
    ##    
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @LowerLimitRightHandSide.setter
    def LowerLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) LowerLimitRightHandSide
         Returns 
                the lower limit of the expression right hand side of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetExpression
    ##  Returns 
    ##         the offset of a constraint.  
    ##   
    ##         The offset will only be used for coupler constraint types. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def OffsetExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) OffsetExpression
         Returns 
                the offset of a constraint.  
          
                The offset will only be used for coupler constraint types. 
              
         
        """
        pass
    
    ## Getter for property: (str) OffsetRightHandSide
    ##  Returns 
    ##         the offset right hand side of a constraint.  
    ##    
    ##         The offset right hand side will only be used for coupler constraint types. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def OffsetRightHandSide(self) -> str:
        """
        Getter for property: (str) OffsetRightHandSide
         Returns 
                the offset right hand side of a constraint.  
           
                The offset right hand side will only be used for coupler constraint types. 
              
         
        """
        pass
    
    ## Setter for property: (str) OffsetRightHandSide

    ##  Returns 
    ##         the offset right hand side of a constraint.  
    ##    
    ##         The offset right hand side will only be used for coupler constraint types. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @OffsetRightHandSide.setter
    def OffsetRightHandSide(self, offset: str):
        """
        Setter for property: (str) OffsetRightHandSide
         Returns 
                the offset right hand side of a constraint.  
           
                The offset right hand side will only be used for coupler constraint types. 
              
         
        """
        pass
    
    ## Getter for property: (bool) Persistent
    ##  Returns 
    ##         the persistent state of the constraint.  
    ##   
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def Persistent(self) -> bool:
        """
        Getter for property: (bool) Persistent
         Returns 
                the persistent state of the constraint.  
          
              
         
        """
        pass
    
    ## Setter for property: (bool) Persistent

    ##  Returns 
    ##         the persistent state of the constraint.  
    ##   
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Persistent.setter
    def Persistent(self, persistent: bool):
        """
        Setter for property: (bool) Persistent
         Returns 
                the persistent state of the constraint.  
          
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondExpression
    ##  Returns 
    ##         the second @link NXOpen::Expression NXOpen::Expression@endlink  of a constraint.  
    ##    
    ##         The second expression will be unused unless this constraint type supports a second expression. 
    ##         This only applies to cylindrical joints.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SecondExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondExpression
         Returns 
                the second @link NXOpen::Expression NXOpen::Expression@endlink  of a constraint.  
           
                The second expression will be unused unless this constraint type supports a second expression. 
                This only applies to cylindrical joints.
              
         
        """
        pass
    
    ## Getter for property: (bool) SecondExpressionDriven
    ##  Returns 
    ##         the driven state of the second expression of a constraint.  
    ##   
    ##         The value of the driven second expression can change. Driven second expression values are controlled 
    ##         by the solver and cannot be edited by the user. This only applies to cylindrical joints.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def SecondExpressionDriven(self) -> bool:
        """
        Getter for property: (bool) SecondExpressionDriven
         Returns 
                the driven state of the second expression of a constraint.  
          
                The value of the driven second expression can change. Driven second expression values are controlled 
                by the solver and cannot be edited by the user. This only applies to cylindrical joints.
              
         
        """
        pass
    
    ## Setter for property: (bool) SecondExpressionDriven

    ##  Returns 
    ##         the driven state of the second expression of a constraint.  
    ##   
    ##         The value of the driven second expression can change. Driven second expression values are controlled 
    ##         by the solver and cannot be edited by the user. This only applies to cylindrical joints.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SecondExpressionDriven.setter
    def SecondExpressionDriven(self, second_expression_driven: bool):
        """
        Setter for property: (bool) SecondExpressionDriven
         Returns 
                the driven state of the second expression of a constraint.  
          
                The value of the driven second expression can change. Driven second expression values are controlled 
                by the solver and cannot be edited by the user. This only applies to cylindrical joints.
              
         
        """
        pass
    
    ## Getter for property: (str) SecondExpressionRightHandSide
    ##  Returns 
    ##         the second expression right hand side of a constraint.  
    ##    
    ##         The second expression right hand side will be unused unless this constraint type supports a second expression. 
    ##         This only applies to cylindrical joints.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def SecondExpressionRightHandSide(self) -> str:
        """
        Getter for property: (str) SecondExpressionRightHandSide
         Returns 
                the second expression right hand side of a constraint.  
           
                The second expression right hand side will be unused unless this constraint type supports a second expression. 
                This only applies to cylindrical joints.
              
         
        """
        pass
    
    ## Setter for property: (str) SecondExpressionRightHandSide

    ##  Returns 
    ##         the second expression right hand side of a constraint.  
    ##    
    ##         The second expression right hand side will be unused unless this constraint type supports a second expression. 
    ##         This only applies to cylindrical joints.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SecondExpressionRightHandSide.setter
    def SecondExpressionRightHandSide(self, secondExpressionRightHandSide: str):
        """
        Setter for property: (str) SecondExpressionRightHandSide
         Returns 
                the second expression right hand side of a constraint.  
           
                The second expression right hand side will be unused unless this constraint type supports a second expression. 
                This only applies to cylindrical joints.
              
         
        """
        pass
    
    ## Getter for property: (bool) SecondLowerLimitEnabled
    ##  Returns 
    ##         the lower limit of the second expression of a constraint.  
    ##    
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def SecondLowerLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) SecondLowerLimitEnabled
         Returns 
                the lower limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Setter for property: (bool) SecondLowerLimitEnabled

    ##  Returns 
    ##         the lower limit of the second expression of a constraint.  
    ##    
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SecondLowerLimitEnabled.setter
    def SecondLowerLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) SecondLowerLimitEnabled
         Returns 
                the lower limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondLowerLimitExpression
    ##  Returns 
    ##         the lower limit of the second expression of a constraint.  
    ##   
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SecondLowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondLowerLimitExpression
         Returns 
                the lower limit of the second expression of a constraint.  
          
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Getter for property: (str) SecondLowerLimitRightHandSide
    ##  Returns 
    ##         the lower limit of the second expression right hand side of a constraint.  
    ##    
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def SecondLowerLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) SecondLowerLimitRightHandSide
         Returns 
                the lower limit of the second expression right hand side of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Setter for property: (str) SecondLowerLimitRightHandSide

    ##  Returns 
    ##         the lower limit of the second expression right hand side of a constraint.  
    ##    
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SecondLowerLimitRightHandSide.setter
    def SecondLowerLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) SecondLowerLimitRightHandSide
         Returns 
                the lower limit of the second expression right hand side of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Getter for property: (bool) SecondUpperLimitEnabled
    ##  Returns 
    ##         the upper limit of the second expression of a constraint.  
    ##    
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def SecondUpperLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) SecondUpperLimitEnabled
         Returns 
                the upper limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Setter for property: (bool) SecondUpperLimitEnabled

    ##  Returns 
    ##         the upper limit of the second expression of a constraint.  
    ##    
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SecondUpperLimitEnabled.setter
    def SecondUpperLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) SecondUpperLimitEnabled
         Returns 
                the upper limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondUpperLimitExpression
    ##  Returns 
    ##         the upper limit of the second expression of a constraint.  
    ##    
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SecondUpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondUpperLimitExpression
         Returns 
                the upper limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Getter for property: (str) SecondUpperLimitRightHandSide
    ##  Returns 
    ##         the upper limit of the second expression right hand side of a constraint.  
    ##   
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def SecondUpperLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) SecondUpperLimitRightHandSide
         Returns 
                the upper limit of the second expression right hand side of a constraint.  
          
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Setter for property: (str) SecondUpperLimitRightHandSide

    ##  Returns 
    ##         the upper limit of the second expression right hand side of a constraint.  
    ##   
    ##         The second limit expression will only be used for certain constraint types, and they must have a second expression. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @SecondUpperLimitRightHandSide.setter
    def SecondUpperLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) SecondUpperLimitRightHandSide
         Returns 
                the upper limit of the second expression right hand side of a constraint.  
          
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    
    ## Getter for property: (@link Constraint.SplineType NXOpen.Positioning.Constraint.SplineType@endlink) SplinePointsType
    ##  Returns the type of the spline.  
    ##     Only valid if the type of the constraint is
    ##       set to @link NXOpen::Positioning::Constraint::TypeSplineData NXOpen::Positioning::Constraint::TypeSplineData@endlink .   
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## @return Constraint.SplineType
    @property
    def SplinePointsType(self) -> Constraint.SplineType:
        """
        Getter for property: (@link Constraint.SplineType NXOpen.Positioning.Constraint.SplineType@endlink) SplinePointsType
         Returns the type of the spline.  
            Only valid if the type of the constraint is
              set to @link NXOpen::Positioning::Constraint::TypeSplineData NXOpen::Positioning::Constraint::TypeSplineData@endlink .   
         
        """
        pass
    
    ## Setter for property: (@link Constraint.SplineType NXOpen.Positioning.Constraint.SplineType@endlink) SplinePointsType

    ##  Returns the type of the spline.  
    ##     Only valid if the type of the constraint is
    ##       set to @link NXOpen::Positioning::Constraint::TypeSplineData NXOpen::Positioning::Constraint::TypeSplineData@endlink .   
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    @SplinePointsType.setter
    def SplinePointsType(self, spline_type: Constraint.SplineType):
        """
        Setter for property: (@link Constraint.SplineType NXOpen.Positioning.Constraint.SplineType@endlink) SplinePointsType
         Returns the type of the spline.  
            Only valid if the type of the constraint is
              set to @link NXOpen::Positioning::Constraint::TypeSplineData NXOpen::Positioning::Constraint::TypeSplineData@endlink .   
         
        """
        pass
    
    ## Getter for property: (bool) Suppressed
    ##  Returns 
    ##         the suppression state for the constraint.  
    ##    In a @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  this is the state in the @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink ."
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def Suppressed(self) -> bool:
        """
        Getter for property: (bool) Suppressed
         Returns 
                the suppression state for the constraint.  
           In a @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  this is the state in the @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink ."
              
         
        """
        pass
    
    ## Setter for property: (bool) Suppressed

    ##  Returns 
    ##         the suppression state for the constraint.  
    ##    In a @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  this is the state in the @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink ."
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Suppressed.setter
    def Suppressed(self, suppressed: bool):
        """
        Setter for property: (bool) Suppressed
         Returns 
                the suppression state for the constraint.  
           In a @link NXOpen::Positioning::ComponentConstraint NXOpen::Positioning::ComponentConstraint@endlink  this is the state in the @link NXOpen::Positioning::ComponentPositioner::PrimaryArrangement NXOpen::Positioning::ComponentPositioner::PrimaryArrangement@endlink ."
              
         
        """
        pass
    
    ## Getter for property: (bool) UpperLimitEnabled
    ##  Returns 
    ##         the upper limit of the expression of a constraint.  
    ##    
    ##         The limit expression will only be used for certain constraint types, and they must have an expression.  
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def UpperLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) UpperLimitEnabled
         Returns 
                the upper limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression.  
              
         
        """
        pass
    
    ## Setter for property: (bool) UpperLimitEnabled

    ##  Returns 
    ##         the upper limit of the expression of a constraint.  
    ##    
    ##         The limit expression will only be used for certain constraint types, and they must have an expression.  
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @UpperLimitEnabled.setter
    def UpperLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) UpperLimitEnabled
         Returns 
                the upper limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression.  
              
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitExpression
    ##  Returns 
    ##         the upper limit of the expression of a constraint.  
    ##    
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def UpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimitExpression
         Returns 
                the upper limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ## Getter for property: (str) UpperLimitRightHandSide
    ##  Returns 
    ##         the upper limit of the expression right hand side of a constraint.  
    ##   
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def UpperLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) UpperLimitRightHandSide
         Returns 
                the upper limit of the expression right hand side of a constraint.  
          
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ## Setter for property: (str) UpperLimitRightHandSide

    ##  Returns 
    ##         the upper limit of the expression right hand side of a constraint.  
    ##   
    ##         The limit expression will only be used for certain constraint types, and they must have an expression. 
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @UpperLimitRightHandSide.setter
    def UpperLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) UpperLimitRightHandSide
         Returns 
                the upper limit of the expression right hand side of a constraint.  
          
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    
    ##  
    ##         Adds geometry to a constraint and sets the movable object
    ##         to be constrained.
    ##     
    ##  @return constraint_reference (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink):  The new @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="constraint"> (@link Constraint NXOpen.Positioning.Constraint@endlink) </param>
    ## <param name="movable_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Object to be positioned by constraint </param>
    ## <param name="geometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Geometry used to define constraint </param>
    ## <param name="uses_axis"> (bool)  Use axis of geometry </param>
    ## <param name="is_indirect"> (bool)  Geometry is to be used indirectly to identify geometry in another part </param>
    @overload
    def CreateConstraintReference(self, movable_object: NXOpen.NXObject, geometry: NXOpen.NXObject, uses_axis: bool, is_indirect: bool) -> ConstraintReference:
        """
         
                Adds geometry to a constraint and sets the movable object
                to be constrained.
            
         @return constraint_reference (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink):  The new @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  .
        """
        pass
    
    ##  
    ##         Adds geometry to a constraint and sets the movable object
    ##         to be constrained.  
    ##     
    ##  @return constraint_reference (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink):  The new @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="constraint"> (@link Constraint NXOpen.Positioning.Constraint@endlink) </param>
    ## <param name="movable_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Object to be positioned by constraint </param>
    ## <param name="geometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Geometry used to define constraint </param>
    ## <param name="uses_axis"> (bool)  Use axis of geometry </param>
    ## <param name="is_indirect"> (bool)  Geometry is to be used indirectly to identify geometry in another part </param>
    ## <param name="use_port_rotate"> (bool)  Use rotate vector of @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink . </param>
    @overload
    def CreateConstraintReference(self, movable_object: NXOpen.NXObject, geometry: NXOpen.NXObject, uses_axis: bool, is_indirect: bool, use_port_rotate: bool) -> ConstraintReference:
        """
         
                Adds geometry to a constraint and sets the movable object
                to be constrained.  
            
         @return constraint_reference (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink):  The new @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  .
        """
        pass
    
    ##  
    ##         Adds constraint reference to a coupler.
    ##     
    ##  @return couplerReference (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink):  The new @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="coupledConstraint"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  The @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  to be coupled </param>
    def CreateCouplerReference(self, coupledConstraint: NXOpen.NXObject) -> ConstraintReference:
        """
         
                Adds constraint reference to a coupler.
            
         @return couplerReference (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink):  The new @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  .
        """
        pass
    
    ##  
    ##         Removes a @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  from the constraint. 
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraint_reference"> (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink)  The constraint reference to remove. A list 
    ##                                                                                   of references can be obtained via
    ##                                                                                   @link NXOpen::Positioning::Constraint::GetReferences NXOpen::Positioning::Constraint::GetReferences@endlink . </param>
    def DeleteConstraintReference(self, constraint_reference: ConstraintReference) -> None:
        """
         
                Removes a @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  from the constraint. 
            
        """
        pass
    
    ##  
    ##         Adds geometry to a constraint and sets the movable object
    ##         to be constrained, replacing the properties of an existing
    ##         reference of the constraint.
    ##     
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraint_reference"> (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink)  The @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  whose properties are to be changed </param>
    ## <param name="movable_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Object to be positioned by constraint </param>
    ## <param name="geometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  Geometry used to define constraint </param>
    ## <param name="uses_axis"> (bool)  Use axis of geometry </param>
    ## <param name="is_indirect"> (bool)  Geometry is to be used indirectly to identify geometry in another part </param>
    ## <param name="use_port_rotate"> (bool)  Use rotate vector of @link NXOpen::Routing::Port NXOpen::Routing::Port@endlink . </param>
    def EditConstraintReference(self, constraint_reference: ConstraintReference, movable_object: NXOpen.NXObject, geometry: NXOpen.NXObject, uses_axis: bool, is_indirect: bool, use_port_rotate: bool) -> None:
        """
         
                Adds geometry to a constraint and sets the movable object
                to be constrained, replacing the properties of an existing
                reference of the constraint.
            
        """
        pass
    
    ##  
    ##         Edit coupler reference so that it is replaced with another constraint.
    ##     
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="couplerReference"> (@link ConstraintReference NXOpen.Positioning.ConstraintReference@endlink)  The @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink  whose properties are to be changed</param>
    ## <param name="coupledConstraint"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  The @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  to be coupled instead </param>
    def EditCouplerReference(self, couplerReference: ConstraintReference, coupledConstraint: NXOpen.NXObject) -> None:
        """
         
                Edit coupler reference so that it is replaced with another constraint.
            
        """
        pass
    
    ##  
    ##         Reverses the constraint alignment if this is possible.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def FlipAlignment(self) -> None:
        """
         
                Reverses the constraint alignment if this is possible.
            
        """
        pass
    
    ## 
    ##         Returns a textual conversion report this constraint from when it was converted from a
    ##         Mating Constraint to an Assembly Constraint. If this isn't a converted constraint
    ##         or there were no problems converting this constraint, then an empty string is returned.
    ##     
    ##  @return lines (List[str]):  The text lines of the conversion report .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GenerateConversionReport(self) -> List[str]:
        """
        
                Returns a textual conversion report this constraint from when it was converted from a
                Mating Constraint to an Assembly Constraint. If this isn't a converted constraint
                or there were no problems converting this constraint, then an empty string is returned.
            
         @return lines (List[str]):  The text lines of the conversion report .
        """
        pass
    
    ##  
    ##         Returns the solver status of a constraint.
    ##     
    ##  @return status (@link Constraint.SolverStatus NXOpen.Positioning.Constraint.SolverStatus@endlink):  The solver status of the constraint .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetConstraintStatus(self) -> Constraint.SolverStatus:
        """
         
                Returns the solver status of a constraint.
            
         @return status (@link Constraint.SolverStatus NXOpen.Positioning.Constraint.SolverStatus@endlink):  The solver status of the constraint .
        """
        pass
    
    ## 
    ##         Gets the @link NXOpen::Positioning::DisplayedConstraint NXOpen::Positioning::DisplayedConstraint@endlink  that is in the same part as that of the constraint.
    ## 
    ##         Note that this will be NULL if the part has not been the displayed part since the constraint was created.
    ##     
    ##  @return displayed_constraint (@link DisplayedConstraint NXOpen.Positioning.DisplayedConstraint@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetDisplayedConstraint(self) -> DisplayedConstraint:
        """
        
                Gets the @link NXOpen::Positioning::DisplayedConstraint NXOpen::Positioning::DisplayedConstraint@endlink  that is in the same part as that of the constraint.
        
                Note that this will be NULL if the part has not been the displayed part since the constraint was created.
            
         @return displayed_constraint (@link DisplayedConstraint NXOpen.Positioning.DisplayedConstraint@endlink): .
        """
        pass
    
    ##  
    ##         Gets all the @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink s for the 
    ##         constraint.
    ##     
    ##  @return references (@link ConstraintReference List[NXOpen.Positioning.ConstraintReference]@endlink):  ConstraintReferences used by this constraint .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetReferences(self) -> List[ConstraintReference]:
        """
         
                Gets all the @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink s for the 
                constraint.
            
         @return references (@link ConstraintReference List[NXOpen.Positioning.ConstraintReference]@endlink):  ConstraintReferences used by this constraint .
        """
        pass
    
    ##  Changes the constraint to solve with the latest version of the constraint code. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def Renew(self) -> None:
        """
         Changes the constraint to solve with the latest version of the constraint code. 
        """
        pass
    
    ##  
    ##         Reverses the constraint direction.  This operation reverses the @link NXOpen::Positioning::ConstraintReference::Order NXOpen::Positioning::ConstraintReference::Order@endlink 
    ##         on each @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink .
    ##         So "Inside" becomes "Outside", "Outside" becomes "Inside" and "Unknown" remains as it is.
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ReverseDirection(self) -> None:
        """
         
                Reverses the constraint direction.  This operation reverses the @link NXOpen::Positioning::ConstraintReference::Order NXOpen::Positioning::ConstraintReference::Order@endlink 
                on each @link NXOpen::Positioning::ConstraintReference NXOpen::Positioning::ConstraintReference@endlink .
                So "Inside" becomes "Outside", "Outside" becomes "Inside" and "Unknown" remains as it is.
            
        """
        pass
    
    ##  
    ##         Set a hint as to which alignment should be used by the
    ##         solver for this constraint.
    ##         
    ##         If the constraint does not solve using this alignment
    ##         then the hint will be ignored.                
    ##         
    ##         The hint can only have an effect when the alignment of
    ##         the constraint, as returned by @link NXOpen::Positioning::Constraint::ConstraintAlignment NXOpen::Positioning::Constraint::ConstraintAlignment@endlink ,
    ##         is @link NXOpen::Positioning::Constraint::AlignmentInferAlign NXOpen::Positioning::Constraint::AlignmentInferAlign@endlink .
    ##         
    ##         The hint can only have an effect when the constraint has been
    ##         explicitly added to a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink .
    ##         
    ##         Passing in @link NXOpen::Positioning::Constraint::AlignmentInferAlign NXOpen::Positioning::Constraint::AlignmentInferAlign@endlink  as the alignment
    ##         argument will have no effect.
    ##         
    ##         The hint is forgotten after an update.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="alignment"> (@link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink)  The alignment hint </param>
    def SetAlignmentHint(self, alignment: Constraint.Alignment) -> None:
        """
         
                Set a hint as to which alignment should be used by the
                solver for this constraint.
                
                If the constraint does not solve using this alignment
                then the hint will be ignored.                
                
                The hint can only have an effect when the alignment of
                the constraint, as returned by @link NXOpen::Positioning::Constraint::ConstraintAlignment NXOpen::Positioning::Constraint::ConstraintAlignment@endlink ,
                is @link NXOpen::Positioning::Constraint::AlignmentInferAlign NXOpen::Positioning::Constraint::AlignmentInferAlign@endlink .
                
                The hint can only have an effect when the constraint has been
                explicitly added to a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink .
                
                Passing in @link NXOpen::Positioning::Constraint::AlignmentInferAlign NXOpen::Positioning::Constraint::AlignmentInferAlign@endlink  as the alignment
                argument will have no effect.
                
                The hint is forgotten after an update.
            
        """
        pass
    
    ##  
    ##         The @link NXOpen::Expression NXOpen::Expression@endlink  of a constraint - only used if this 
    ##         constraint type supports an expression, such as a distance or angle constraint,
    ##         or a joint. 
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="expression"> (str)  Name of expression used in the constraint </param>
    def SetExpression(self, expression: str) -> None:
        """
         
                The @link NXOpen::Expression NXOpen::Expression@endlink  of a constraint - only used if this 
                constraint type supports an expression, such as a distance or angle constraint,
                or a joint. 
            
        """
        pass
    
import NXOpen
## 
##         a collection of displayed constraints    
##      <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class DisplayedConstraintCollection(NXOpen.TaggedObjectCollection): 
    """
        a collection of displayed constraints    
    """
    pass


import NXOpen
import NXOpen.Assemblies
## 
##         The displayed representation of a constraint, used for graphical
##         display and to represent it in the Assembly Navigator.
## 
##         Instances of @link NXOpen::Positioning::DisplayedConstraint NXOpen::Positioning::DisplayedConstraint@endlink  are created whenever a
##         @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  is created.
## 
##         A @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  has an instance of @link NXOpen::Positioning::DisplayedConstraint NXOpen::Positioning::DisplayedConstraint@endlink 
##         in the same part as itself, but an instance of @link NXOpen::Positioning::DisplayedConstraint NXOpen::Positioning::DisplayedConstraint@endlink  doesn't
##         necessarily exist in the same part as the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
##      <br> An instance of this class can be obtained from @link NXOpen::Positioning::Constraint::GetDisplayedConstraint NXOpen::Positioning::Constraint::GetDisplayedConstraint@endlink .  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class DisplayedConstraint(NXOpen.DisplayableObject): 
    """
        The displayed representation of a constraint, used for graphical
        display and to represent it in the Assembly Navigator.

        Instances of <ja_class>NXOpen.Positioning.DisplayedConstraint</ja_class> are created whenever a
        <ja_class>NXOpen.Positioning.Constraint</ja_class> is created.

        A <ja_class>NXOpen.Positioning.Constraint</ja_class> has an instance of <ja_class>NXOpen.Positioning.DisplayedConstraint</ja_class>
        in the same part as itself, but an instance of <ja_class>NXOpen.Positioning.DisplayedConstraint</ja_class> doesn't
        necessarily exist in the same part as the underlying <ja_class>NXOpen.Positioning.Constraint</ja_class>.
    """


    ##  
    ##             Get the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
    ##              <br> 
    ##             Note that this will be NULL if the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  is unloaded.
    ##              <br>  
    ##         
    ##  @return constraint (@link Constraint NXOpen.Positioning.Constraint@endlink):  The underlying constraint .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetConstraint(self) -> Constraint:
        """
         
                    Get the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
                     <br> 
                    Note that this will be NULL if the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  is unloaded.
                     <br>  
                
         @return constraint (@link Constraint NXOpen.Positioning.Constraint@endlink):  The underlying constraint .
        """
        pass
    
    ##  
    ##             Get the part containing the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
    ##              <br> 
    ##             Note that this will be NULL if the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  is unloaded.
    ##              <br> 
    ##         
    ##  @return part (@link NXOpen.Part NXOpen.Part@endlink):  The part containing the underlying constraint .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetConstraintPart(self) -> NXOpen.Part:
        """
         
                    Get the part containing the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
                     <br> 
                    Note that this will be NULL if the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  is unloaded.
                     <br> 
                
         @return part (@link NXOpen.Part NXOpen.Part@endlink):  The part containing the underlying constraint .
        """
        pass
    
    ## 
    ##             Get the component containing the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
    ##              <br> 
    ##             Note that this will be NULL if the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  is in the
    ##             same part as the displayed constraint.
    ##              <br> 
    ##         
    ##  @return component (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink): .
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetContextComponent(self) -> NXOpen.Assemblies.Component:
        """
        
                    Get the component containing the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink .
                     <br> 
                    Note that this will be NULL if the underlying @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  is in the
                    same part as the displayed constraint.
                     <br> 
                
         @return component (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink): .
        """
        pass
    
import NXOpen
## 
##       An instance of this class can be used to convert Mating Conditions
##       to Assembly Constraints in its owning assembly or in child parts
##       of its owning assembly. The owning assembly is the
##       @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink  from which this
##       object was obtained using
##       @link NXOpen::Assemblies::ComponentAssembly::CreateMatingConverter NXOpen::Assemblies::ComponentAssembly::CreateMatingConverter@endlink .
##      <br> Not directly created by user.  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class MatingConverter(NXOpen.TaggedObject): 
    """
      An instance of this class can be used to convert Mating Conditions
      to Assembly Constraints in its owning assembly or in child parts
      of its owning assembly. The owning assembly is the
      <ja_class>NXOpen.Assemblies.ComponentAssembly</ja_class> from which this
      object was obtained using
      <ja_method>NXOpen.Assemblies.ComponentAssembly.CreateMatingConverter</ja_method>.
    """


    ##  Defines in which parts mating conditions will be converted.
    ##          
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## InOwningPart</term><description> 
    ##  Convert mating conditions in the owning part </description> </item><item><term> 
    ## InLoadedChildren</term><description> 
    ##  Convert mating conditions in the owning part
    ##                                                                      and all loaded children. Partially-loaded
    ##                                                                      children will be fully-loaded. </description> </item><item><term> 
    ## InAllChildren</term><description> 
    ##  Convert mating conditions in the owning part
    ##                                                                      and all children. Partially-loaded and unloaded
    ##                                                                      children will be fully-loaded. </description> </item></list>
    class PartContext(Enum):
        """
        Members Include: <InOwningPart> <InLoadedChildren> <InAllChildren>
        """
        InOwningPart: int
        InLoadedChildren: int
        InAllChildren: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MatingConverter.PartContext:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link MatingConverter.PartContext NXOpen.Positioning.MatingConverter.PartContext@endlink) Context
    ##  Returns
    ##             the current conversion context in which mating conditions will be converted.  
    ##   
    ##           
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return MatingConverter.PartContext
    @property
    def Context(self) -> MatingConverter.PartContext:
        """
        Getter for property: (@link MatingConverter.PartContext NXOpen.Positioning.MatingConverter.PartContext@endlink) Context
         Returns
                    the current conversion context in which mating conditions will be converted.  
          
                  
         
        """
        pass
    
    ## Setter for property: (@link MatingConverter.PartContext NXOpen.Positioning.MatingConverter.PartContext@endlink) Context

    ##  Returns
    ##             the current conversion context in which mating conditions will be converted.  
    ##   
    ##           
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @Context.setter
    def Context(self, context: MatingConverter.PartContext):
        """
        Setter for property: (@link MatingConverter.PartContext NXOpen.Positioning.MatingConverter.PartContext@endlink) Context
         Returns
                    the current conversion context in which mating conditions will be converted.  
          
                  
         
        """
        pass
    
    ## Getter for property: (bool) LoadReferencedGeometry
    ##  Returns
    ##             whether to load unloaded referenced geometry before performing a conversion.  
    ##   
    ##             When all referenced geometry is loaded the conversion operation is more
    ##             effective. If it isn't loaded, then the conversion operation will often
    ##             need to be completed next time the assembly and geometry are loaded
    ##             together.
    ##           
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def LoadReferencedGeometry(self) -> bool:
        """
        Getter for property: (bool) LoadReferencedGeometry
         Returns
                    whether to load unloaded referenced geometry before performing a conversion.  
          
                    When all referenced geometry is loaded the conversion operation is more
                    effective. If it isn't loaded, then the conversion operation will often
                    need to be completed next time the assembly and geometry are loaded
                    together.
                  
         
        """
        pass
    
    ## Setter for property: (bool) LoadReferencedGeometry

    ##  Returns
    ##             whether to load unloaded referenced geometry before performing a conversion.  
    ##   
    ##             When all referenced geometry is loaded the conversion operation is more
    ##             effective. If it isn't loaded, then the conversion operation will often
    ##             need to be completed next time the assembly and geometry are loaded
    ##             together.
    ##           
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @LoadReferencedGeometry.setter
    def LoadReferencedGeometry(self, load_geometry: bool):
        """
        Setter for property: (bool) LoadReferencedGeometry
         Returns
                    whether to load unloaded referenced geometry before performing a conversion.  
          
                    When all referenced geometry is loaded the conversion operation is more
                    effective. If it isn't loaded, then the conversion operation will often
                    need to be completed next time the assembly and geometry are loaded
                    together.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink) LoadStatus
    ##  Returns
    ##             the load status resulting from a conversion operation.  
    ##    This indicates
    ##             any problems which arose when loading parts during conversion.
    ##           
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.PartLoadStatus
    @property
    def LoadStatus(self) -> NXOpen.PartLoadStatus:
        """
        Getter for property: (@link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink) LoadStatus
         Returns
                    the load status resulting from a conversion operation.  
           This indicates
                    any problems which arose when loading parts during conversion.
                  
         
        """
        pass
    
    ## Getter for property: (int) NumberOfConvertedParts
    ##  Returns
    ##             the number of parts parts converted by this conversion operation.  
    ##   
    ##           
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def NumberOfConvertedParts(self) -> int:
        """
        Getter for property: (int) NumberOfConvertedParts
         Returns
                    the number of parts parts converted by this conversion operation.  
          
                  
         
        """
        pass
    
    ## 
    ##             Converts Mating Conditions to Assembly Constraints according to the
    ##             properties defined on this @link NXOpen::Positioning::MatingConverter NXOpen::Positioning::MatingConverter@endlink 
    ##             object.
    ##         
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ConvertMatingConditions(self) -> None:
        """
        
                    Converts Mating Conditions to Assembly Constraints according to the
                    properties defined on this @link NXOpen::Positioning::MatingConverter NXOpen::Positioning::MatingConverter@endlink 
                    object.
                
        """
        pass
    
    ## 
    ##             Removes details from the mating conversion results of the individual constraints that were converted.
    ##             This will be applied to the mating conversion results in the parts described by the current context
    ##             (determined by @link NXOpen::Positioning::MatingConverter::SetContext NXOpen::Positioning::MatingConverter::SetContext@endlink ). Note that the
    ##             summary information for each part in the conversion results is not modified by this function.
    ##         
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def DeleteResults(self) -> None:
        """
        
                    Removes details from the mating conversion results of the individual constraints that were converted.
                    This will be applied to the mating conversion results in the parts described by the current context
                    (determined by @link NXOpen::Positioning::MatingConverter::SetContext NXOpen::Positioning::MatingConverter::SetContext@endlink ). Note that the
                    summary information for each part in the conversion results is not modified by this function.
                
        """
        pass
    
    ## 
    ##             Deletes this @link NXOpen::Positioning::MatingConverter NXOpen::Positioning::MatingConverter@endlink  immediately.
    ##         
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def Destroy(self) -> None:
        """
        
                    Deletes this @link NXOpen::Positioning::MatingConverter NXOpen::Positioning::MatingConverter@endlink  immediately.
                
        """
        pass
    
    ## 
    ##             Returns all constraints converted by this conversion operation.
    ##             Use @link NXOpen::Positioning::Constraint::GenerateConversionReport NXOpen::Positioning::Constraint::GenerateConversionReport@endlink 
    ##             to obtain the conversion status of these constraints.
    ##         
    ##  @return converted_constraints (@link Constraint List[NXOpen.Positioning.Constraint]@endlink):  The converted constraints .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetConvertedConstraints(self) -> List[Constraint]:
        """
        
                    Returns all constraints converted by this conversion operation.
                    Use @link NXOpen::Positioning::Constraint::GenerateConversionReport NXOpen::Positioning::Constraint::GenerateConversionReport@endlink 
                    to obtain the conversion status of these constraints.
                
         @return converted_constraints (@link Constraint List[NXOpen.Positioning.Constraint]@endlink):  The converted constraints .
        """
        pass
    
    ## 
    ##             Returns all parts converted by this conversion operation.
    ##         
    ##  @return converted_constraints (@link Constraint List[NXOpen.Positioning.Constraint]@endlink):  The converted constraints .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetConvertedParts(self) -> List[Constraint]:
        """
        
                    Returns all parts converted by this conversion operation.
                
         @return converted_constraints (@link Constraint List[NXOpen.Positioning.Constraint]@endlink):  The converted constraints .
        """
        pass
    
    ## 
    ##             Returns textual descriptions of the results of the last conversion operation
    ##         
    ##  @return result_lines (List[str]):  The generated results .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="show_all_results"> (bool)  Whether to show results for all converted constraints even if no issues arose during their conversion </param>
    def GetLatestResults(self, show_all_results: bool) -> List[str]:
        """
        
                    Returns textual descriptions of the results of the last conversion operation
                
         @return result_lines (List[str]):  The generated results .
        """
        pass
    
    ## 
    ##             Returns textual descriptions of the results of all prior conversion
    ##             operations for all the parts described by the current context set using
    ##             @link NXOpen::Positioning::MatingConverter::SetContext NXOpen::Positioning::MatingConverter::SetContext@endlink .
    ##         
    ##  @return result_lines (List[str]):  The generated results .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="show_all_results"> (bool)  Whether to show results for all converted constraints even if no issues arose during their conversion </param>
    def GetResults(self, show_all_results: bool) -> List[str]:
        """
        
                    Returns textual descriptions of the results of all prior conversion
                    operations for all the parts described by the current context set using
                    @link NXOpen::Positioning::MatingConverter::SetContext NXOpen::Positioning::MatingConverter::SetContext@endlink .
                
         @return result_lines (List[str]):  The generated results .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
## 
##     Network for use in positioning objects in NX.
##     A network consists of explicitly added constraints and movable objects
##     together with others implicitly added because they are connected by 
##     to those in the network.
##  <br> Use @link Positioning::Positioner::EstablishNetwork Positioning::Positioner::EstablishNetwork@endlink  to create an instance of this class.  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class Network(NXOpen.NXObject): 
    """
    Network for use in positioning objects in NX.
    A network consists of explicitly added constraints and movable objects
    together with others implicitly added because they are connected by 
    to those in the network.
"""


    ##  Specifies the solver status of a movable object. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Unknown</term><description> 
    ##  Not yet evaluated. </description> </item><item><term> 
    ## Fixed</term><description> 
    ##  Attempt to put constraint between two fixed objects. </description> </item><item><term> 
    ## OverDefined</term><description> 
    ##  Conflicts with other constraints. </description> </item><item><term> 
    ## NotConsistentDims</term><description> 
    ##  Cannot solve with current dimension values. Model fully defined. </description> </item><item><term> 
    ## NotConsistentOther</term><description> 
    ##  Cannot find a solution. Model underdefined.</description> </item><item><term> 
    ## NotConsistentUnknown</term><description> 
    ##  One movable object fixed. </description> </item><item><term> 
    ## NotChanged</term><description> 
    ##  Not evaluated because other parts of the model are over defined or inconsistent. </description> </item><item><term> 
    ## WellDefined</term><description> 
    ##  The constraint is solved and satisfied </description> </item><item><term> 
    ## UnderDefined</term><description> 
    ##  The constraint is solved and satisfied </description> </item></list>
    class ObjectStatus(Enum):
        """
        Members Include: <Unknown> <Fixed> <OverDefined> <NotConsistentDims> <NotConsistentOther> <NotConsistentUnknown> <NotChanged> <WellDefined> <UnderDefined>
        """
        Unknown: int
        Fixed: int
        OverDefined: int
        NotConsistentDims: int
        NotConsistentOther: int
        NotConsistentUnknown: int
        NotChanged: int
        WellDefined: int
        UnderDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Network.ObjectStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) DisplayComponent
    ##  Returns 
    ##         the @link Assemblies::Component Assemblies::Component@endlink  in which the display is changed
    ##         by solving the network.  
    ##    The display component can be NULL if display
    ##         changes are made in the part of the network.
    ##         The prototype of the display component should be the part containing the
    ##         network.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return NXOpen.Assemblies.Component
    @property
    def DisplayComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) DisplayComponent
         Returns 
                the @link Assemblies::Component Assemblies::Component@endlink  in which the display is changed
                by solving the network.  
           The display component can be NULL if display
                changes are made in the part of the network.
                The prototype of the display component should be the part containing the
                network.
              
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) DisplayComponent

    ##  Returns 
    ##         the @link Assemblies::Component Assemblies::Component@endlink  in which the display is changed
    ##         by solving the network.  
    ##    The display component can be NULL if display
    ##         changes are made in the part of the network.
    ##         The prototype of the display component should be the part containing the
    ##         network.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @DisplayComponent.setter
    def DisplayComponent(self, display_component: NXOpen.Assemblies.Component):
        """
        Setter for property: (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink) DisplayComponent
         Returns 
                the @link Assemblies::Component Assemblies::Component@endlink  in which the display is changed
                by solving the network.  
           The display component can be NULL if display
                changes are made in the part of the network.
                The prototype of the display component should be the part containing the
                network.
              
         
        """
        pass
    
    ## Getter for property: (bool) MoveObjectsState
    ##  Returns 
    ##         the move objects state for the network.  
    ##   
    ##         When set the display positions of objects are immediately updated
    ##         upon constraint creation or edit.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def MoveObjectsState(self) -> bool:
        """
        Getter for property: (bool) MoveObjectsState
         Returns 
                the move objects state for the network.  
          
                When set the display positions of objects are immediately updated
                upon constraint creation or edit.
              
         
        """
        pass
    
    ## Setter for property: (bool) MoveObjectsState

    ##  Returns 
    ##         the move objects state for the network.  
    ##   
    ##         When set the display positions of objects are immediately updated
    ##         upon constraint creation or edit.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @MoveObjectsState.setter
    def MoveObjectsState(self, move_objects_state: bool):
        """
        Setter for property: (bool) MoveObjectsState
         Returns 
                the move objects state for the network.  
          
                When set the display positions of objects are immediately updated
                upon constraint creation or edit.
              
         
        """
        pass
    
    ## Getter for property: (bool) NonMovingGroupGrounded
    ##  Returns 
    ##         the grounded state of non-moving_group objects.  
    ##   
    ##         When set all objects outside the moving_group are fixed and will
    ##         not move during a solve or drag.
    ##       
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def NonMovingGroupGrounded(self) -> bool:
        """
        Getter for property: (bool) NonMovingGroupGrounded
         Returns 
                the grounded state of non-moving_group objects.  
          
                When set all objects outside the moving_group are fixed and will
                not move during a solve or drag.
              
         
        """
        pass
    
    ## Setter for property: (bool) NonMovingGroupGrounded

    ##  Returns 
    ##         the grounded state of non-moving_group objects.  
    ##   
    ##         When set all objects outside the moving_group are fixed and will
    ##         not move during a solve or drag.
    ##       
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @NonMovingGroupGrounded.setter
    def NonMovingGroupGrounded(self, ground: bool):
        """
        Setter for property: (bool) NonMovingGroupGrounded
         Returns 
                the grounded state of non-moving_group objects.  
          
                When set all objects outside the moving_group are fixed and will
                not move during a solve or drag.
              
         
        """
        pass
    
    ##  
    ##         Add a @link Constraint Constraint@endlink  to the network.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraint"> (@link Constraint NXOpen.Positioning.Constraint@endlink)  The @link Constraint Constraint@endlink  to be added </param>
    def AddConstraint(self, constraint: Constraint) -> None:
        """
         
                Add a @link Constraint Constraint@endlink  to the network.
            
        """
        pass
    
    ##  
    ##         Add a movable object to the network. An object explicitly added
    ##         by this method will be directly moved by calls 
    ##         to @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
    ##         @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  and
    ##         @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink .        
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="movable_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  An @link NXObject NXObject@endlink  to be moved </param>
    def AddMovableObject(self, movable_object: NXOpen.NXObject) -> None:
        """
         
                Add a movable object to the network. An object explicitly added
                by this method will be directly moved by calls 
                to @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
                @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  and
                @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink .        
            
        """
        pass
    
    ##  
    ##         Applies the current network state to the model.  This may change the position
    ##         of movable objects and the status of constraints in the model.  Does not do 
    ##         a solve or an update.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ApplyToModel(self) -> None:
        """
         
                Applies the current network state to the model.  This may change the position
                of movable objects and the status of constraints in the model.  Does not do 
                a solve or an update.
            
        """
        pass
    
    ##  
    ##         Notify the network that a sequence of drag operations is about to
    ##         begin.
    ##          <br> 
    ##         This must be called before a series of calls to
    ##         @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
    ##         @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  or
    ##         @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink .
    ##         Following a drag, and before any other changes to a network
    ##         are made, @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink 
    ##         should be called.
    ##          <br> 
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def BeginDrag(self) -> None:
        """
         
                Notify the network that a sequence of drag operations is about to
                begin.
                 <br> 
                This must be called before a series of calls to
                @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
                @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  or
                @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink .
                Following a drag, and before any other changes to a network
                are made, @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink 
                should be called.
                 <br> 
            
        """
        pass
    
    ##  
    ##         Move objects which have been added to the network using 
    ##         @link Positioning::Network::AddMovableObject Positioning::Network::AddMovableObject@endlink .
    ##         Constraints are honored during the drag so that other
    ##         objects may also move as a result of this call.
    ##         On the first call to this method, a notional point is added to each of
    ##         the objects to be dragged.  On subsequent calls, this notional point,
    ##         and hence the dragged object, is kept as close as possible to the ray
    ##         determined by point and direction. If there are no constraints then the
    ##         point will stay on the ray.
    ## 
    ##          <br> 
    ##         A series of calls to this method can be made between calls to
    ##         @link Positioning::Network::BeginDrag Positioning::Network::BeginDrag@endlink  and
    ##         @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink .
    ##          <br> 
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="point"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  A point on the ray </param>
    ## <param name="direction"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  The direction of the ray </param>
    def DragByRay(self, point: NXOpen.Point3d, direction: NXOpen.Vector3d) -> None:
        """
         
                Move objects which have been added to the network using 
                @link Positioning::Network::AddMovableObject Positioning::Network::AddMovableObject@endlink .
                Constraints are honored during the drag so that other
                objects may also move as a result of this call.
                On the first call to this method, a notional point is added to each of
                the objects to be dragged.  On subsequent calls, this notional point,
                and hence the dragged object, is kept as close as possible to the ray
                determined by point and direction. If there are no constraints then the
                point will stay on the ray.
        
                 <br> 
                A series of calls to this method can be made between calls to
                @link Positioning::Network::BeginDrag Positioning::Network::BeginDrag@endlink  and
                @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink .
                 <br> 
            
        """
        pass
    
    ##  
    ##         Move objects which have been added to the network using 
    ##         @link Positioning::Network::AddMovableObject Positioning::Network::AddMovableObject@endlink .
    ##         Constraints are honored during the drag so that other
    ##         objects may also move as a result of this call.
    ##         The rotation is applied first, then the translation.
    ## 
    ##          <br> 
    ##         A series of calls to this method can be made between calls to
    ##         @link Positioning::Network::BeginDrag Positioning::Network::BeginDrag@endlink  and
    ##         @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink .
    ##          <br> 
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="translation"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  The translation to be applied </param>
    ## <param name="rotation"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink)  The rotation to be applied </param>
    def DragByTransform(self, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
         
                Move objects which have been added to the network using 
                @link Positioning::Network::AddMovableObject Positioning::Network::AddMovableObject@endlink .
                Constraints are honored during the drag so that other
                objects may also move as a result of this call.
                The rotation is applied first, then the translation.
        
                 <br> 
                A series of calls to this method can be made between calls to
                @link Positioning::Network::BeginDrag Positioning::Network::BeginDrag@endlink  and
                @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink .
                 <br> 
            
        """
        pass
    
    ##  
    ##         Move objects which have been added to the network using 
    ##         @link Positioning::Network::AddMovableObject Positioning::Network::AddMovableObject@endlink .
    ##         Constraints are honored during the drag so that other
    ##         objects may also move as a result of this call.
    ## 
    ##         Unlike @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink 
    ##         there is no rotational element passed in. This can improve the
    ##         behavior of the constraint solver.
    ## 
    ##          <br> 
    ##         A series of calls to this method can be made between calls to
    ##         @link Positioning::Network::BeginDrag Positioning::Network::BeginDrag@endlink  and
    ##         @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink .
    ##          <br> 
    ##     
    ## 
    ##   <br>  Created in NX6.0.4  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="translation"> (@link NXOpen.Vector3d NXOpen.Vector3d@endlink)  The translation to be applied </param>
    def DragByTranslation(self, translation: NXOpen.Vector3d) -> None:
        """
         
                Move objects which have been added to the network using 
                @link Positioning::Network::AddMovableObject Positioning::Network::AddMovableObject@endlink .
                Constraints are honored during the drag so that other
                objects may also move as a result of this call.
        
                Unlike @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink 
                there is no rotational element passed in. This can improve the
                behavior of the constraint solver.
        
                 <br> 
                A series of calls to this method can be made between calls to
                @link Positioning::Network::BeginDrag Positioning::Network::BeginDrag@endlink  and
                @link Positioning::Network::EndDrag Positioning::Network::EndDrag@endlink .
                 <br> 
            
        """
        pass
    
    ##  
    ##         Remove all elements from the moving_group.
    ##         See @link Positioning::Network::SetMovingGroup Positioning::Network::SetMovingGroup@endlink .
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def EmptyMovingGroup(self) -> None:
        """
         
                Remove all elements from the moving_group.
                See @link Positioning::Network::SetMovingGroup Positioning::Network::SetMovingGroup@endlink .
            
        """
        pass
    
    ##  
    ##         Notify the network that a sequence of drag operations has
    ##         ended.
    ##          <br> 
    ##         This must be called after a series of calls to
    ##         @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
    ##         @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  or
    ##         @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink .
    ##          <br> 
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def EndDrag(self) -> None:
        """
         
                Notify the network that a sequence of drag operations has
                ended.
                 <br> 
                This must be called after a series of calls to
                @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
                @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  or
                @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink .
                 <br> 
            
        """
        pass
    
    ##  
    ##         Returns the solver status of a movable object.
    ##     
    ##  @return status (@link Network.ObjectStatus NXOpen.Positioning.Network.ObjectStatus@endlink):  The solver status of the movable object .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="movable_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  An @link NXObject NXObject@endlink  positioned by the network </param>
    def GetMovableObjectStatus(self, movable_object: NXOpen.NXObject) -> Network.ObjectStatus:
        """
         
                Returns the solver status of a movable object.
            
         @return status (@link Network.ObjectStatus NXOpen.Positioning.Network.ObjectStatus@endlink):  The solver status of the movable object .
        """
        pass
    
    ##  
    ##         Are the necessary objects loaded so that all connected constraints can be
    ##         included during a drag or solve ?
    ##     
    ##  @return loaded (bool): .
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def IsReferencedGeometryLoaded(self) -> bool:
        """
         
                Are the necessary objects loaded so that all connected constraints can be
                included during a drag or solve ?
            
         @return loaded (bool): .
        """
        pass
    
    ##  
    ##         Load the necessary objects so that all connected constraints can be
    ##         included during a drag or solve.
    ##         If an object is not loaded then the part containing it will be 
    ##         fully loaded by this call.
    ##     
    ## 
    ##   <br>  Created in NX5.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def LoadReferencedGeometry(self) -> None:
        """
         
                Load the necessary objects so that all connected constraints can be
                included during a drag or solve.
                If an object is not loaded then the part containing it will be 
                fully loaded by this call.
            
        """
        pass
    
    ##  
    ##         Remove all @link Constraint Constraint@endlink s which have been explicitly added
    ##         to the network.  Those constraints connected to explicitly added movable
    ##         objects will still be include in a network solve.
    ##     
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def RemoveAllConstraints(self) -> None:
        """
         
                Remove all @link Constraint Constraint@endlink s which have been explicitly added
                to the network.  Those constraints connected to explicitly added movable
                objects will still be include in a network solve.
            
        """
        pass
    
    ##  
    ##         Remove a @link Constraint Constraint@endlink  from the network. A constraint
    ##         explicitly removed by this method may still included in a network solve
    ##         if connected to another constraint or movable object which has been
    ##         explicitly added.
    ##     
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="constraint"> (@link Constraint NXOpen.Positioning.Constraint@endlink)  The @link Constraint Constraint@endlink  to be removed </param>
    def RemoveConstraint(self, constraint: Constraint) -> None:
        """
         
                Remove a @link Constraint Constraint@endlink  from the network. A constraint
                explicitly removed by this method may still included in a network solve
                if connected to another constraint or movable object which has been
                explicitly added.
            
        """
        pass
    
    ##  
    ##         Remove a movable object from the network. An object explicitly
    ##         removed by this method will not be directly moved by calls 
    ##         to @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
    ##         @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  and
    ##         @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink , though it
    ##         may still be moved indirectly if constrained to other movable objects.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="movable_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  An @link NXObject NXObject@endlink  to be removed from the network </param>
    def RemoveMovableObject(self, movable_object: NXOpen.NXObject) -> None:
        """
         
                Remove a movable object from the network. An object explicitly
                removed by this method will not be directly moved by calls 
                to @link Positioning::Network::DragByRay Positioning::Network::DragByRay@endlink ,
                @link Positioning::Network::DragByTransform Positioning::Network::DragByTransform@endlink  and
                @link Positioning::Network::DragByTranslation Positioning::Network::DragByTranslation@endlink , though it
                may still be moved indirectly if constrained to other movable objects.
            
        """
        pass
    
    ##  
    ##         Returns the display objects to their model positions.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ResetDisplay(self) -> None:
        """
         
                Returns the display objects to their model positions.
            
        """
        pass
    
    ##  
    ##         Set the elements of the moving_group. 
    ##         The elements of the moving_group will move as a rigid body
    ##         during a solve or drag operation.  Objects outside the moving
    ##         group can all be prevented from moving by setting 
    ##         @link Positioning::Network::SetNonMovingGroupGrounded Positioning::Network::SetNonMovingGroupGrounded@endlink 
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="movable_objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The @link NXObject NXObject@endlink s to be moved </param>
    def SetMovingGroup(self, movable_objects: List[NXOpen.NXObject]) -> None:
        """
         
                Set the elements of the moving_group. 
                The elements of the moving_group will move as a rigid body
                during a solve or drag operation.  Objects outside the moving
                group can all be prevented from moving by setting 
                @link Positioning::Network::SetNonMovingGroupGrounded Positioning::Network::SetNonMovingGroupGrounded@endlink 
            
        """
        pass
    
    ##  
    ##         Solves the constraint network.
    ##         Does apply the results to the model but does not 
    ##         do an update.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def Solve(self) -> None:
        """
         
                Solves the constraint network.
                Does apply the results to the model but does not 
                do an update.
            
        """
        pass
    
import NXOpen
## 
##   An instance of this class can be used to create @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink s and
##   associated objects.
##  <br> To obtain an instance of this class, use @link NXOpen::Assemblies::ComponentAssembly::Positioner  NXOpen::Assemblies::ComponentAssembly::Positioner @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class Positioner(NXOpen.NXObject): 
    """
  An instance of this class can be used to create <ja_class>NXOpen.Positioning.Constraint</ja_class>s and
  associated objects.
"""


    ##  The collection of @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink s defined in the positioner 
    ## 
    ##   <br>  Created in NX3.0.0  <br> 

    ## @link ConstraintCollection NXOpen.Positioning.ConstraintCollection@endlink
    @property
    def Constraints() -> ConstraintCollection:
        """
         The collection of @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink s defined in the positioner 
        """
        pass
    
    ##  
    ##         Removes the @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  of the positioner.
    ##         The network is added to the delete list by this call.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ClearNetwork(self) -> None:
        """
         
                Removes the @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  of the positioner.
                The network is added to the delete list by this call.
            
        """
        pass
    
    ##  
    ##         Creates a new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  in the positioner.
    ##     
    ##  @return constraint (@link Constraint NXOpen.Positioning.Constraint@endlink):  The new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="positioner"> (@link Positioner NXOpen.Positioning.Positioner@endlink) </param>
    ## <param name="persistent"> (bool)  Persistent state of constraint </param>
    @overload
    def CreateConstraint(self, persistent: bool) -> Constraint:
        """
         
                Creates a new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  in the positioner.
            
         @return constraint (@link Constraint NXOpen.Positioning.Constraint@endlink):  The new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  .
        """
        pass
    
    ##  
    ##         Creates a new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  in the positioner.
    ##     
    ##  @return constraint (@link Constraint NXOpen.Positioning.Constraint@endlink):  The new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="positioner"> (@link Positioner NXOpen.Positioning.Positioner@endlink) </param>
    @overload
    def CreateConstraint(self) -> Constraint:
        """
         
                Creates a new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  in the positioner.
            
         @return constraint (@link Constraint NXOpen.Positioning.Constraint@endlink):  The new @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink  .
        """
        pass
    
    ##  
    ##         Deletes all the non-persistent @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink s of the positioner.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def DeleteNonPersistentConstraints(self) -> None:
        """
         
                Deletes all the non-persistent @link NXOpen::Positioning::Constraint NXOpen::Positioning::Constraint@endlink s of the positioner.
            
        """
        pass
    
    ##  
    ##         Establishes a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  in the positioner.
    ##     
    ##  @return network (@link Network NXOpen.Positioning.Network@endlink):  The new @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def EstablishNetwork(self) -> Network:
        """
         
                Establishes a @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  in the positioner.
            
         @return network (@link Network NXOpen.Positioning.Network@endlink):  The new @link NXOpen::Positioning::Network NXOpen::Positioning::Network@endlink  .
        """
        pass
    
## @package NXOpen.Positioning
## Classes, Enums and Structs under NXOpen.Positioning namespace

##  @link ComponentConstraintGroupConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroupConstraintsCollectionType @endlink is an alias for @link ComponentConstraintGroup.ConstraintsCollectionType NXOpen.Positioning.ComponentConstraintGroup.ConstraintsCollectionType@endlink
ComponentConstraintGroupConstraintsCollectionType = ComponentConstraintGroup.ConstraintsCollectionType


##  @link ComponentConstraintDirectionToFixed NXOpen.Positioning.ComponentConstraintDirectionToFixed @endlink is an alias for @link ComponentConstraint.DirectionToFixed NXOpen.Positioning.ComponentConstraint.DirectionToFixed@endlink
ComponentConstraintDirectionToFixed = ComponentConstraint.DirectionToFixed


##  @link ComponentNetworkArrangementsMode NXOpen.Positioning.ComponentNetworkArrangementsMode @endlink is an alias for @link ComponentNetwork.ArrangementsMode NXOpen.Positioning.ComponentNetwork.ArrangementsMode@endlink
ComponentNetworkArrangementsMode = ComponentNetwork.ArrangementsMode


##  @link ConstraintReferenceConstraintOrder NXOpen.Positioning.ConstraintReferenceConstraintOrder @endlink is an alias for @link ConstraintReference.ConstraintOrder NXOpen.Positioning.ConstraintReference.ConstraintOrder@endlink
ConstraintReferenceConstraintOrder = ConstraintReference.ConstraintOrder


##  @link ConstraintReferenceGeometryType NXOpen.Positioning.ConstraintReferenceGeometryType @endlink is an alias for @link ConstraintReference.GeometryType NXOpen.Positioning.ConstraintReference.GeometryType@endlink
ConstraintReferenceGeometryType = ConstraintReference.GeometryType


##  @link ConstraintReferenceHalfSpace NXOpen.Positioning.ConstraintReferenceHalfSpace @endlink is an alias for @link ConstraintReference.HalfSpace NXOpen.Positioning.ConstraintReference.HalfSpace@endlink
ConstraintReferenceHalfSpace = ConstraintReference.HalfSpace


##  @link ConstraintAlignment NXOpen.Positioning.ConstraintAlignment @endlink is an alias for @link Constraint.Alignment NXOpen.Positioning.Constraint.Alignment@endlink
ConstraintAlignment = Constraint.Alignment


##  @link ConstraintSolverStatus NXOpen.Positioning.ConstraintSolverStatus @endlink is an alias for @link Constraint.SolverStatus NXOpen.Positioning.Constraint.SolverStatus@endlink
ConstraintSolverStatus = Constraint.SolverStatus


##  @link ConstraintSplineType NXOpen.Positioning.ConstraintSplineType @endlink is an alias for @link Constraint.SplineType NXOpen.Positioning.Constraint.SplineType@endlink
ConstraintSplineType = Constraint.SplineType


##  @link ConstraintType NXOpen.Positioning.ConstraintType @endlink is an alias for @link Constraint.Type NXOpen.Positioning.Constraint.Type@endlink
ConstraintType = Constraint.Type


##  @link MatingConverterPartContext NXOpen.Positioning.MatingConverterPartContext @endlink is an alias for @link MatingConverter.PartContext NXOpen.Positioning.MatingConverter.PartContext@endlink
MatingConverterPartContext = MatingConverter.PartContext


##  @link NetworkObjectStatus NXOpen.Positioning.NetworkObjectStatus @endlink is an alias for @link Network.ObjectStatus NXOpen.Positioning.Network.ObjectStatus@endlink
NetworkObjectStatus = Network.ObjectStatus


