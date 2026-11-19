from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
import NXOpen.Assemblies
class ComponentConstraintGroupBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.Positioning.ComponentConstraintGroupBuilder builder """
    @property
    def ConstraintCollectionType(self) -> ComponentConstraintGroup.ConstraintsCollectionType:
        """
        Getter for property: ( ComponentConstraintGroup.ConstraintsCollectionType NXOpen.P) ConstraintCollectionType
         Returns the constraint collection types   
            
         
        """
        pass
    @ConstraintCollectionType.setter
    def ConstraintCollectionType(self, constraintCollectionType: ComponentConstraintGroup.ConstraintsCollectionType):
        """
        Setter for property: ( ComponentConstraintGroup.ConstraintsCollectionType NXOpen.P) ConstraintCollectionType
         Returns the constraint collection types   
            
         
        """
        pass
    @property
    def ConstraintGroupName(self) -> str:
        """
        Getter for property: (str) ConstraintGroupName
         Returns the name of constraint group   
            
         
        """
        pass
    @ConstraintGroupName.setter
    def ConstraintGroupName(self, nameOfConstraintGroup: str):
        """
        Setter for property: (str) ConstraintGroupName
         Returns the name of constraint group   
            
         
        """
        pass
    @property
    def RememberComponentState(self) -> bool:
        """
        Getter for property: (bool) RememberComponentState
         Returns the toggle to remember selected component   
            
         
        """
        pass
    @RememberComponentState.setter
    def RememberComponentState(self, rememberComponentState: bool):
        """
        Setter for property: (bool) RememberComponentState
         Returns the toggle to remember selected component   
            
         
        """
        pass
    @property
    def SelectedComponentList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectedComponentList
         Returns the selected components list   
            
         
        """
        pass
    @property
    def SelectedConstraintsList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectedConstraintsList
         Returns the selected constraint list   
            
         
        """
        pass
    def GetContextComponent(self) -> NXOpen.Assemblies.Component:
        """
                    Gets the context component which is used to decide the displayed constraints that can be in the
                    selected constraints list. The context component is only set by the creator and can be .
                    If the context component is  the displayed constraints will be in same part as the
                    constraint group.
                
         Returns component ( NXOpen.Assemblies.Component): .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class ComponentConstraintGroup(NXOpen.NXObject): 
    """
        Constraint group which represents a group of component constraints in NX.
    """
    class ConstraintsCollectionType(Enum):
        """
        Members Include: 
         |BetweenSelectedComponents| 
         |ConnectedToSelectedComponents| 

        """
        BetweenSelectedComponents: int
        ConnectedToSelectedComponents: int
        @staticmethod
        def ValueOf(value: int) -> ComponentConstraintGroup.ConstraintsCollectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetConstraintCollectionType(self) -> ComponentConstraintGroup.ConstraintsCollectionType:
        """
                    Gets the type of constraint collection that is performed using the defining components.
                
         Returns constraintCollectionType ( ComponentConstraintGroup.ConstraintsCollectionType NXOpen.P): .
        """
        pass
    def GetDefiningComponents(self) -> List[NXOpen.Assemblies.Component]:
        """
                    Returns the defining components within the group.
                
         Returns components ( NXOpen.Assemblies.Component Li):  Defining components .
        """
        pass
    def GetDefiningConstraints(self) -> List[ComponentConstraint]:
        """
                    Returns the defining constraints within the group.
                
         Returns constraints ( ComponentConstraint List[NXOpen):  Defining constraints .
        """
        pass
    def GetMemberConstraints(self) -> List[ComponentConstraint]:
        """
                    Returns the member constraints present in the group. The member constraints are generated from the defining
                    constraints and components. This attribute cannot be set directly.
                
         Returns constraints ( ComponentConstraint List[NXOpen):  Member constraints .
        """
        pass
    def GetRememberComponentState(self) -> bool:
        """
                    Gets the state which indicates if defining components are remembered when updating the member constraints.
                
         Returns rememberComponentState (bool): .
        """
        pass
    def SetConstraintCollectionType(self, constraintCollectionType: ComponentConstraintGroup.ConstraintsCollectionType) -> None:
        """
                    Sets the type of constraint collection that is performed using the defining components.
                
        """
        pass
    def SetDefiningComponents(self, constraints: List[NXOpen.Assemblies.Component]) -> None:
        """
                    Sets the defining constraints within the group.
                
        """
        pass
    def SetDefiningConstraints(self, constraints: List[ComponentConstraint]) -> None:
        """
                    Sets the defining constraints within the group.
                
        """
        pass
    def SetRememberComponentState(self, rememberComponentState: bool) -> None:
        """
                    Sets the state which indicates if defining components are remembered when updating the member constraints.
                
        """
        pass
    def UpdateMemberConstraints(self) -> bool:
        """
                    Updates the member constraints so that they match the definition implied by the defining constraints,
                    defining components and associated constraint collection type.
                
         Returns changed (bool):  True if the member constraints have been changed by update .
        """
        pass
import NXOpen.Assemblies
class ComponentConstraint(Constraint): 
    """
    Constraint for use in positioning assembly objects in NX.
    
"""
    class DirectionToFixed(Enum):
        """
        Members Include: 
         |Unknown|  No information available 
         |Toward|  Toward fixed geometry 
         |AwayFrom|  Away from fixed geometry 
         |NothingFixed|  The network does not contain any fixed geometry 
         |Fix|  The constraint is a NXOpen.Positioning.Constraint.Type.Fix 
         |Suppressed|  The constraint is suppressed 
         |IgnoredInArrangement|  The current arrangement ignores all constraints 

        """
        Unknown: int
        Toward: int
        AwayFrom: int
        NothingFixed: int
        Fix: int
        Suppressed: int
        IgnoredInArrangement: int
        @staticmethod
        def ValueOf(value: int) -> ComponentConstraint.DirectionToFixed:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrangementSpecific(self) -> bool:
        """
        Getter for property: (bool) ArrangementSpecific
         Returns
                the arrangement specific state of this  NXOpen::Positioning::ComponentConstraint  in the 
                 NXOpen::Positioning::ComponentPositioner::PrimaryArrangement .  
            Constraints can
                never be arrangement specific in piece parts.
              
         
        """
        pass
    @ArrangementSpecific.setter
    def ArrangementSpecific(self, arrangement_specific: bool):
        """
        Setter for property: (bool) ArrangementSpecific
         Returns
                the arrangement specific state of this  NXOpen::Positioning::ComponentConstraint  in the 
                 NXOpen::Positioning::ComponentPositioner::PrimaryArrangement .  
            Constraints can
                never be arrangement specific in piece parts.
              
         
        """
        pass
    def CopyInheritedToOverride(self) -> ComponentConstraint:
        """
                Given an inherited NXOpen.Positioning.ComponentConstraint created because of Positioning Overrides, create a new constraint copied
                from it in the same part.  Unlike the inherited NXOpen.Positioning.ComponentConstraint, the new constraint can be modified by the
                user in the same ways as a normal constraint.  (Inherited constraints can be suppressed or unsuppressed, but are otherwise read-only.)
                If the constraint is not an inherited constraint, an error is raised.
            
         Returns newConstraint ( ComponentConstraint NXOpen.P):  The new NXOpen.Positioning.ComponentConstraint copied from the inherited NXOpen.Positioning.ComponentConstraint in the same part. .
        """
        pass
    def CopyToOverride(self) -> None:
        """
                Given an inherited NXOpen.Positioning.ComponentConstraint created because of Positioning Overrides, create a new constraint copied
                from it in the same part.  Unlike the inherited NXOpen.Positioning.ComponentConstraint, the new constraint can be modified by the
                user in the same ways as a normal constraint.  (Inherited constraints can be suppressed or unsuppressed, but are otherwise read-only.)
                If the constraint is not an inherited constraint, an error is raised.
            
        """
        pass
    def GetDirectionToFixed(self, component: NXOpen.Assemblies.Component, arrangement: NXOpen.Assemblies.Arrangement) -> ComponentConstraint.DirectionToFixed:
        """
                Get the NXOpen.Positioning.ComponentConstraint.DirectionToFixed value of the NXOpen.Positioning.ComponentConstraint
                given a component and an arrangement.
                This value specifies how a constraint affects the positioning of a component.
                If the arrangement is null, the "direction to fixed" value will be evaluated based on the default arrangement.
            
         Returns direction_to_fixed ( ComponentConstraint.DirectionToFixed NXOpen.P):  The NXOpen.Positioning.ComponentConstraint.DirectionToFixed value. .
        """
        pass
    def GetInherited(self) -> bool:
        """
                Get whether this NXOpen.Positioning.ComponentConstraint is 
                an inherited constraint. An inherited constraint is created by the system 
                to support Positioning Overrides. 
            
         Returns inherited (bool):  The inherited state of this NXOpen.Positioning.ComponentConstraint .
        """
        pass
    def GetSeparateSuppression(self) -> bool:
        """
                An inherited NXOpen.Positioning.ComponentConstraint can be suppressed independently of the constraint it is
                derived from.  When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
                of the constraint it is derived from.  This method returns true for an inherited constraint in this state.  It does not indicate
                if the constraint is inherited or not: use NXOpen.Positioning.Constraint.Suppressed for this.
                Given a non-inherited constraint, this will return false.
            
         Returns separate_suppression (bool):  The separate suppression state of this NXOpen.Positioning.ComponentConstraint .
        """
        pass
    def GetSharedSuppressed(self) -> bool:
        """
                Get the shared suppression state of this NXOpen.Positioning.ComponentConstraint used across all 
                arrangements where the constraint is not arrangement specific.
            
         Returns suppressed (bool):   The suppression state. .
        """
        pass
    def GetSpecificInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement) -> bool:
        """
                Get the arrangement specific state of this NXOpen.Positioning.ComponentConstraint in the 
                specified NXOpen.Assemblies.Arrangement.
            
         Returns arrangement_specific (bool):   The arrangement specific state. .
        """
        pass
    def GetSuppressedInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement) -> bool:
        """
                Get the suppression state of this NXOpen.Positioning.ComponentConstraint in the 
                specified NXOpen.Assemblies.Arrangement.  If the constraint is not arrangement
                specific in this arrangement then the shared suppression state, used across all 
                arrangements where the constraint is not arrangement specific, is used.
            
         Returns suppressed (bool):   The suppression state. .
        """
        pass
    def RememberOnComponent(self, component: NXOpen.Assemblies.Component) -> None:
        """
                Remembers the constraint in the prototype part of a referenced component
                for reuse in other occurrences of the part. Fix and Bond constraints are
                never remembered.  If the constraint does not reference geometry in the
                component, it is not remembered.
            
        """
        pass
    def SetSeparateSuppression(self, separate_suppression: bool) -> None:
        """
                An inherited NXOpen.Positioning.ComponentConstraint can be suppressed independently of the constraint it is
                derived from.  When this has been done, it no longer becomes suppressed or unsuppressed in response to changes in the suppression
                of the constraint it is derived from.  This method sets this state on an inherited constraint.  Setting this flag will not in
                itself suppress or unsuppress the inherited constraint: use NXOpen.Positioning.Constraint.Suppressed for this.
                If the constraint is not an inherited constraint, an error is raised.
            
        """
        pass
    def SetSharedSuppressed(self, suppressed: bool) -> None:
        """
                Set the shared suppression state of this NXOpen.Positioning.ComponentConstraint used across all 
                arrangements where the constraint is not arrangement specific.
            
        """
        pass
    def SetSpecificInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement, arrangement_specific: bool) -> None:
        """
                Set the arrangement specific state of this NXOpen.Positioning.ComponentConstraint in the 
                specified NXOpen.Assemblies.Arrangement.
            
        """
        pass
    def SetSuppressedInArrangement(self, arrangement: NXOpen.Assemblies.Arrangement, suppressed: bool) -> None:
        """
                Set the suppression state of this NXOpen.Positioning.ComponentConstraint in the 
                specified NXOpen.Assemblies.Arrangement.  If the constraint is not arrangement
                specific in this arrangement then the shared suppression state, used across all 
                arrangements where the constraint is not arrangement specific, is set.
            
        """
        pass
class ComponentNetwork(Network): 
    """
        Network for use in positioning components in NX.
        A component network extends the NXOpen.Positioning.Network by
        adding support for NXOpen.Assemblies.Arrangements.
    """
    class ArrangementsMode(Enum):
        """
        Members Include: 
         |Existing|  Apply transforms in arrangements according to existing component properties.
                                                                                        Constraints are created non-arrangement specific. 
         |InUsed|  Apply transforms in the used arrangement only. 
                                                                                        Constraints are created arrangement specific in the used arrangement 
                                                                                        and suppressed in all other arrangements

        """
        Existing: int
        InUsed: int
        @staticmethod
        def ValueOf(value: int) -> ComponentNetwork.ArrangementsMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def NetworkArrangementsMode(self) -> ComponentNetwork.ArrangementsMode:
        """
        Getter for property: ( ComponentNetwork.ArrangementsMode NXOpen.P) NetworkArrangementsMode
         Returns
                    the arrangements mode for this network.  
          
                  
         
        """
        pass
    @NetworkArrangementsMode.setter
    def NetworkArrangementsMode(self, mode: ComponentNetwork.ArrangementsMode):
        """
        Setter for property: ( ComponentNetwork.ArrangementsMode NXOpen.P) NetworkArrangementsMode
         Returns
                    the arrangements mode for this network.  
          
                  
         
        """
        pass
    @property
    def NetworkSolveInWorksetMode(self) -> bool:
        """
        Getter for property: (bool) NetworkSolveInWorksetMode
         Returns
                    the mode that moves components in the workset instead of the model.  
          
                  
         
        """
        pass
    @NetworkSolveInWorksetMode.setter
    def NetworkSolveInWorksetMode(self, solveInWorkset: bool):
        """
        Setter for property: (bool) NetworkSolveInWorksetMode
         Returns
                    the mode that moves components in the workset instead of the model.  
          
                  
         
        """
        pass
import NXOpen.Assemblies
class ComponentPositioner(Positioner): 
    """
  An instance of this class can be used to create NXOpen.Positioning.Constraints and
  associated objects.
"""
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
                After changing this flag  NXOpen::DisplayableObject::RedisplayObject 
                should be called to refresh the constraint display.
              
         
        """
        pass
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
                After changing this flag  NXOpen::DisplayableObject::RedisplayObject 
                should be called to refresh the constraint display.
              
         
        """
        pass
    @property
    def DisplaySuppressedConstraints(self) -> bool:
        """
        Getter for property: (bool) DisplaySuppressedConstraints
         Returns
                the flag indicating whether suppressed constraints in the part of this positioner
                are to be displayed on the graphics window or not.  
            (This is a separate
                system from hiding and showing individual constraints.)
                After changing this flag  NXOpen::DisplayableObject::RedisplayObject 
                should be called to refresh the constraint display.
              
         
        """
        pass
    @DisplaySuppressedConstraints.setter
    def DisplaySuppressedConstraints(self, display: bool):
        """
        Setter for property: (bool) DisplaySuppressedConstraints
         Returns
                the flag indicating whether suppressed constraints in the part of this positioner
                are to be displayed on the graphics window or not.  
            (This is a separate
                system from hiding and showing individual constraints.)
                After changing this flag  NXOpen::DisplayableObject::RedisplayObject 
                should be called to refresh the constraint display.
              
         
        """
        pass
    @property
    def MoveDumbGeometry(self) -> bool:
        """
        Getter for property: (bool) MoveDumbGeometry
         Returns the flag that enables the positioner to reposition dumb geometry.  
            Dumb geometry
                is any geometry that is not controlled by another object such as a 
                 NXOpen::Features::Feature  object.  This flag has no effect
                on Routing geometry (segments and control points) as they are always considered
                movable by the positioner.
              
         
        """
        pass
    @MoveDumbGeometry.setter
    def MoveDumbGeometry(self, move_dumb_geometry: bool):
        """
        Setter for property: (bool) MoveDumbGeometry
         Returns the flag that enables the positioner to reposition dumb geometry.  
            Dumb geometry
                is any geometry that is not controlled by another object such as a 
                 NXOpen::Features::Feature  object.  This flag has no effect
                on Routing geometry (segments and control points) as they are always considered
                movable by the positioner.
              
         
        """
        pass
    @property
    def PrimaryArrangement(self) -> NXOpen.Assemblies.Arrangement:
        """
        Getter for property: ( NXOpen.Assemblies.Arrangement) PrimaryArrangement
         Returns 
                the  NXOpen::Assemblies::Arrangement  in which the 
                primary  NXOpen::Positioning::Network  will solve.  
          
              
         
        """
        pass
    @PrimaryArrangement.setter
    def PrimaryArrangement(self, arrangement: NXOpen.Assemblies.Arrangement):
        """
        Setter for property: ( NXOpen.Assemblies.Arrangement) PrimaryArrangement
         Returns 
                the  NXOpen::Assemblies::Arrangement  in which the 
                primary  NXOpen::Positioning::Network  will solve.  
          
              
         
        """
        pass
    def BeginAssemblyConstraints(self) -> None:
        """
         
                Begins a mode of operation where (1) each new NXOpen.Positioning.Constraint
                created by this NXOpen.Positioning.ComponentPositioner applies to
                components in the part of the positioner (or to components with variable component positioning
                defined in the part of the positioner) and (2) and component transforms derived from
                a NXOpen.Positioning.Network will apply to components in the part of the positioner.
            
        """
        pass
    def BeginMoveComponent(self) -> None:
        """
         
                Begins a mode of operation where (1) each new NXOpen.Positioning.Constraint
                is created as transient and (2) a component transform is applied at the level where 
                position is controlled for the component, typically in the component's immediate parent.
            
        """
        pass
    def BeginMoveComponentInWorkset(self) -> None:
        """
                Begins a mode of operation where (1) each new NXOpen.Positioning.Constraint
                is created as transient and (2) a component transform is applied at the workset level.
            
        """
        pass
    def EndAssemblyConstraints(self) -> None:
        """
         
                Ends the mode of operation started by 
                NXOpen.Positioning.ComponentPositioner.BeginAssemblyConstraints
                All non-persistent constraints in this NXOpen.Positioning.ComponentPositioner
                will be deleted.
            
        """
        pass
    def EndMoveComponent(self) -> None:
        """
         
                Ends the mode of operation started by 
                NXOpen.Positioning.ComponentPositioner.BeginMoveComponent
                All constraints created while in that mode will be deleted.
            
        """
        pass
    def EndMoveComponentInWorkset(self) -> None:
        """
                Ends the mode of operation started by
                NXOpen.Positioning.ComponentPositioner.BeginMoveComponentInWorkset
                All constraints created while in that mode will be deleted.
            
        """
        pass
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
    def SolvePostponedConstraints(self) -> None:
        """
                Solves constraints in all arrangements that are currently postponing 
                their solve. This could lead to updating the model if required.  This call
                will have no effect if assembly constraint update has been delayed. 
            
        """
        pass
import NXOpen
class ConstraintCollection(NXOpen.TaggedObjectCollection): 
    """
        a collection of constraints    
    """
    pass
import NXOpen
class ConstraintReference(NXOpen.NXObject): 
    """
    ConstraintReference for use in positioning objects in NX.
    A ConstraintReference is used by a Constraint to determine 
    the movable object to be positioned by the constraint and
    the geometry used to define the constraint.
"""
    class ConstraintOrder(Enum):
        """
        Members Include: 
         |Unknown|  No order specified 
         |Inside|  Inside 
         |Outside|  Outside 

        """
        Unknown: int
        Inside: int
        Outside: int
        @staticmethod
        def ValueOf(value: int) -> ConstraintReference.ConstraintOrder:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GeometryType(Enum):
        """
        Members Include: 
         |Unknown|  No geometry suitable for solving 
         |Point|  Point 
         |Line|  Straight line 
         |Circle|  Circle 
         |Plane|  Plane 
         |Cylinder|  Cylinder 
         |Sphere|  Sphere 
         |SweepSurface|  Swept surface 
         |ParametricSurface|  Parametric surface 
         |ParametricCurve|  Parametric curve 
         |SplineCurve|  Spline curve 
         |Torus|  Torus 
         |Cone|  Cone 
         |Ellipse|  Ellipse 
         |SplineSurface|  Spline surface 
         |CoordinateSystem|  Coordinate system 

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
        @staticmethod
        def ValueOf(value: int) -> ConstraintReference.GeometryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class HalfSpace(Enum):
        """
        Members Include: 
         |Infer|  Allow the solver to decide the half space value, or the geometry is not a surface 
         |Positive|  Measure to the positive side of the surface 
         |Negative|  Measure to the negative side of the surface 

        """
        Infer: int
        Positive: int
        Negative: int
        @staticmethod
        def ValueOf(value: int) -> ConstraintReference.HalfSpace:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConstraintReferenceHalfSpace(self) -> ConstraintReference.HalfSpace:
        """
        Getter for property: ( ConstraintReference.HalfSpace NXOpen.P) ConstraintReferenceHalfSpace
         Returns 
                the half_space value for the constraint reference.  
            This is only used for distance constraints.
              
         
        """
        pass
    @ConstraintReferenceHalfSpace.setter
    def ConstraintReferenceHalfSpace(self, half_space: ConstraintReference.HalfSpace):
        """
        Setter for property: ( ConstraintReference.HalfSpace NXOpen.P) ConstraintReferenceHalfSpace
         Returns 
                the half_space value for the constraint reference.  
            This is only used for distance constraints.
              
         
        """
        pass
    @property
    def GeometryDirectionReversed(self) -> bool:
        """
        Getter for property: (bool) GeometryDirectionReversed
         Returns
                whether the direction is reversed with respect to the direction of the geometry.  
          
                This property is only used if the underlying geometry can have an associated direction.
              
         
        """
        pass
    @GeometryDirectionReversed.setter
    def GeometryDirectionReversed(self, geometry_direction_reversed: bool):
        """
        Setter for property: (bool) GeometryDirectionReversed
         Returns
                whether the direction is reversed with respect to the direction of the geometry.  
          
                This property is only used if the underlying geometry can have an associated direction.
              
         
        """
        pass
    @property
    def HelpPoint(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) HelpPoint
         Returns 
                the help point of the constraint reference.  
          
              
         
        """
        pass
    @HelpPoint.setter
    def HelpPoint(self, help_point: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) HelpPoint
         Returns 
                the help point of the constraint reference.  
          
              
         
        """
        pass
    @property
    def Order(self) -> ConstraintReference.ConstraintOrder:
        """
        Getter for property: ( ConstraintReference.ConstraintOrder NXOpen.P) Order
         Returns 
                the order of the constraint reference within its constraint.  
           Note that
                this order is not associated with the geometry or with the alignment 
                of the constraint.  It is based on the idea that the constraint has a direction
                from "outside" to "inside".  It does not affect the result of a solve.
              
         
        """
        pass
    @property
    def SolverGeometryType(self) -> ConstraintReference.GeometryType:
        """
        Getter for property: ( ConstraintReference.GeometryType NXOpen.P) SolverGeometryType
         Returns 
                the geometry type of the constraint reference used during a solve.  
          
              
         
        """
        pass
    @property
    def UsePortRotateFlag(self) -> bool:
        """
        Getter for property: (bool) UsePortRotateFlag
         Returns
                the flag forcing the use of the rotation vector of the 
                referenced  NXOpen::Routing::Port  object instead of the alignment vector 
                when solving the constraint system.  
          
                Only effective when the referenced geometry is a  NXOpen::Routing::Port 
                object.
              
         
        """
        pass
    @UsePortRotateFlag.setter
    def UsePortRotateFlag(self, use_rotate: bool):
        """
        Setter for property: (bool) UsePortRotateFlag
         Returns
                the flag forcing the use of the rotation vector of the 
                referenced  NXOpen::Routing::Port  object instead of the alignment vector 
                when solving the constraint system.  
          
                Only effective when the referenced geometry is a  NXOpen::Routing::Port 
                object.
              
         
        """
        pass
    def GetGeometry(self) -> NXOpen.NXObject:
        """
         
                Returns the geometry of the constraint reference.  This is the 
                geometry used in any NXOpen.Positioning.Constraint using
                this constraint reference.
            
         Returns geometry ( NXOpen.NXObject):  The geometry referenced by the constraint .
        """
        pass
    def GetHasPerpendicularVector(self) -> bool:
        """
         
                Get the flag indicating whether the constraint reference is one that maintains a direction
                perpendicular to the primary geometry.
                This is only applicable to NXOpen.Positioning.Constraint.Type 
                NXOpen.Positioning.Constraint.Type.AlignLock,
                NXOpen.Positioning.Constraint.Type.Hinge,
                NXOpen.Positioning.Constraint.Type.Slider and
                NXOpen.Positioning.Constraint.Type.Cylindrical.
            
         Returns has_perpendicular_vector (bool):  Whether the constraint has a perpendicular vector .
        """
        pass
    def GetMovableObject(self) -> NXOpen.NXObject:
        """
         
                Returns the movable object of the constraint reference.
                The movable object determines the object to be 
                positioned by any NXOpen.Positioning.Constraint using
                this constraint reference.
            
         Returns movable_object_id ( NXOpen.NXObject):  The object positioned by the constraint .
        """
        pass
    def GetPrototypeGeometry(self) -> NXOpen.NXObject:
        """
         
                Returns the prototype geometry of the constraint reference. 
                This is never an occurrence.
            
         Returns geometry ( NXOpen.NXObject):  The prototype geometry referenced by the constraint .
        """
        pass
    def GetPrototypePerpendicularVector(self) -> NXOpen.Vector3d:
        """
         
                Get the value of the perpendicular vector, which will be (0,0,0)
                for most constraints apart from NXOpen.Positioning.Constraint.Type.AlignLock,
                NXOpen.Positioning.Constraint.Type.Hinge,
                NXOpen.Positioning.Constraint.Type.Slider and
                NXOpen.Positioning.Constraint.Type.Cylindrical.
            
         Returns perpendicular_vector ( NXOpen.Vector3d):  The value of the perpendicular vector .
        """
        pass
    def GetUsePortRotate(self) -> bool:
        """
                Get the flag forcing the use of the rotation vector of the 
                referenced NXOpen.Routing.Port object instead of the alignment vector 
                when solving the constraint system.
                Only effective when the referenced geometry is a NXOpen.Routing.Port
                object.
            
         Returns use_rotate (bool):  .
        """
        pass
    def GetUsesGeometryAxis(self) -> bool:
        """
                Returns if the constraint reference should use the axis of the
                geometry (for example a cylindrical face) rather than the surface
            
         Returns geometry (bool):  If this reference is using the axis of the geometry .
        """
        pass
    def SetFixHint(self, set: bool) -> None:
        """
                Set a hint to the solver to fix the movable object associated
                with this constraint reference.
                
                The hint is unset when "set" is false.
                
                The hint can only have an effect when the constraint owning this
                constraint reference has been explicitly added to 
                a NXOpen.Positioning.Network.
                
                The hint is forgotten after an update.
            
        """
        pass
    def SetFixHintForUpdate(self, set: bool) -> None:
        """
                Set a hint to the solver to fix the movable object associated
                with this constraint reference.
                
                The hint is unset when "set" is false.
                
                The hint is forgotten after an update.
                Ensures that the constraint that owns this reference will
                solve during the next call to NXOpen.Update.DoUpdate.
            
        """
        pass
    def SetPrototypePerpendicularVector(self, perpendicular_vector: NXOpen.Vector3d) -> None:
        """
         
                Set the value of the perpendicular vector. The value must be a unit vector given in the coordinates
                of the part containing the referenced geometry.
                The perpendicular vector must be set to (0,0,0) for most constraints apart from
                NXOpen.Positioning.Constraint.Type.AlignLock,
                NXOpen.Positioning.Constraint.Type.Hinge,
                NXOpen.Positioning.Constraint.Type.Slider and
                NXOpen.Positioning.Constraint.Type.Cylindrical which 
                must have a value. An error is raised if this is not the case.
                Whenever the constraint is solved, the value of the perpendicular vector may be modified,
                to ensure that the vector is perpendicular to the referenced geometry. 
            
        """
        pass
import NXOpen
class Constraint(NXOpen.NXObject): 
    """
        Constraints for use in positioning objects in NX.

        For constraints between components, the subclass NXOpen.Positioning.ComponentConstraint should be used by preference.
    
        Some constraint types have an NXOpen.Expression associated with them, which the user can change to determine the value 
        of that constraint. This expression applies to distance and angle constraints, and all joint types. The user can choose for this expression 
        value to be driven by the system, so it will not have a fixed value set by the user.  
    
            
        Some constraint types with values can be given limits. If the constraint is driven, the solver will always try to solve it to remain within 
        those limits, and the constraint will fail if this is not possible. If the constraint is driving, it will have a failure status if its value 
        is set to violate those limits (though it will still solve the model). 
    
"""
    class Alignment(Enum):
        """
        Members Include: 
         |InferAlign|  Allow the solver to decide the alignment 
         |CoAlign|  Directions are the same 
         |ContraAlign|  Directions are opposite 

        """
        InferAlign: int
        CoAlign: int
        ContraAlign: int
        @staticmethod
        def ValueOf(value: int) -> Constraint.Alignment:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SolverStatus(Enum):
        """
        Members Include: 
         |NewlyCreated|  Not evaluated or suppressed since creation 
         |Suppressed|  Constraint is suppressed 
         |OutOfDate|  Needs evaluation 
         |OverConstrained|  Conflicts with other constraints 
         |NotConsistentDims|  Cannot solve with current dimension values. Model fully defined 
         |NotConsistentOther|  Cannot find a solution. Model underdefined 
         |NotConsistentUnknown|  Cannot find a solution 
         |BetweenFixed|  Attempt to put constraint between two fixed objects 
         |NotSolved|  Not evaluated because other parts of the model are over defined or inconsistent 
         |Solved|  The constraint is solved and satisfied 
         |CannotSolve|  The constraint has invalid geometry and could not be passed to the solver 
         |Delayed|  The constraint is delayed and will not solve 
         |IgnoredInArrangement|  The current arrangement ignores all constraints and they will not solve 
         |InternallyInconsistent|  The constraint references invalid geometry for this constraint type 
         |UnloadedGeometry|  The constraint could not solve as some geometry is unloaded 
         |PendingConvertedMc|  The constraint has been converted from a mating condition and has not solved since conversion 
         |ConflictingWithWave|  The constraint has been suppressed because it's conflicting with WAVE 
         |InconsistentLimits|  The constraint has limits that are inconsistent and it could not be passed to the solver 
         |BeyondLimits|  The value of the expression of the constraint is beyond its limits and it could not be passed to the solver 

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
        @staticmethod
        def ValueOf(value: int) -> Constraint.SolverStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SplineType(Enum):
        """
        Members Include: 
         |ByPoles|  Spline points define control points. 
         |ByPoints|  Spline points define interpolationthrough points. 
         |Invalid|  Not a valid spline constraint. 

        """
        ByPoles: int
        ByPoints: int
        Invalid: int
        @staticmethod
        def ValueOf(value: int) -> Constraint.SplineType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Type(Enum):
        """
        Members Include: 
         |Undefined|  No type 
         |Touch|  Two geometries touch 
         |Concentric|  Two geometries share a center and plane 
         |Fix|  One movable object fixed 
         |Distance|  Two geometries have a specified distance between them 
         |Parallel|  Two geometries are parallel 
         |Perpendicular|  Two geometries are perpendicular 
         |Center12|  One geometry is positioned mid-way between two others 
         |Center22|  An implicit plane between two geometries of one movable object is positioned mid-way between two others 
         |Angle|  Two geometries have a specified angle between them 
         |Fit|  Two geometries are coincident 
         |Bond|  A number of movable objects form a rigid group 
         |OrientAngle|  Two geometries have a specified angle between them about an axis 
         |SplineData|  A spline and its defining points 
         |SplineLength|  Constrains the curve length of a spline 
         |LinearPattern|  For internal use only 
         |CircularPattern|  For internal use only 
         |Linear2dPattern|  For internal use only 
         |RadiantPattern|  For internal use only 
         |AlignLock|  Two geometries are constrained to have a common axis and no rotation about it 
         |CommonOffsetTransform|  For internal use only 
         |Hinge|  Two objects along an axis of rotation 
         |Slider|  Two objects along a linear axis 
         |Cylindrical|  Two objects along a rotatable linear axis 
         |Ball|  Two objects at a shared point 
         |Screw|  For internal use only 
         |Gear|  Defines the relative motion between two joints with angular values 
         |RackPinion|  Defines the relative motion between a joint with an angular value and a joint with a linear value 
         |Cable|  Defines the relative motion between two joints with linear values 

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
        @staticmethod
        def ValueOf(value: int) -> Constraint.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
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
    @property
    def ConstraintAlignment(self) -> Constraint.Alignment:
        """
        Getter for property: ( Constraint.Alignment NXOpen.P) ConstraintAlignment
         Returns 
                the alignment behavior for the constraint.  
          
              
         
        """
        pass
    @ConstraintAlignment.setter
    def ConstraintAlignment(self, alignment: Constraint.Alignment):
        """
        Setter for property: ( Constraint.Alignment NXOpen.P) ConstraintAlignment
         Returns 
                the alignment behavior for the constraint.  
          
              
         
        """
        pass
    @property
    def ConstraintSecondAlignment(self) -> Constraint.Alignment:
        """
        Getter for property: ( Constraint.Alignment NXOpen.P) ConstraintSecondAlignment
         Returns 
                the second alignment behavior for the constraint.  
          
              
         
        """
        pass
    @ConstraintSecondAlignment.setter
    def ConstraintSecondAlignment(self, secondAlignment: Constraint.Alignment):
        """
        Setter for property: ( Constraint.Alignment NXOpen.P) ConstraintSecondAlignment
         Returns 
                the second alignment behavior for the constraint.  
          
              
         
        """
        pass
    @property
    def ConstraintType(self) -> Constraint.Type:
        """
        Getter for property: ( Constraint.Type NXOpen.P) ConstraintType
         Returns 
                the constraint type.  
          
              
         
        """
        pass
    @ConstraintType.setter
    def ConstraintType(self, constraint_type: Constraint.Type):
        """
        Setter for property: ( Constraint.Type NXOpen.P) ConstraintType
         Returns 
                the constraint type.  
          
              
         
        """
        pass
    @property
    def Expression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Expression
         Returns 
                the  NXOpen::Expression  of a constraint.  
          
                The expression will be unused unless this constraint type supports an expression, 
                such as a distance or angle constraint, or a joint.
              
         
        """
        pass
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
    @property
    def LowerLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) LowerLimitEnabled
         Returns 
                the lower limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @LowerLimitEnabled.setter
    def LowerLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) LowerLimitEnabled
         Returns 
                the lower limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @property
    def LowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerLimitExpression
         Returns 
                the lower limit of the expression of a constraint.  
          
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @property
    def LowerLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) LowerLimitRightHandSide
         Returns 
                the lower limit of the expression right hand side of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @LowerLimitRightHandSide.setter
    def LowerLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) LowerLimitRightHandSide
         Returns 
                the lower limit of the expression right hand side of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @property
    def OffsetExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) OffsetExpression
         Returns 
                the offset of a constraint.  
          
                The offset will only be used for coupler constraint types. 
              
         
        """
        pass
    @property
    def OffsetRightHandSide(self) -> str:
        """
        Getter for property: (str) OffsetRightHandSide
         Returns 
                the offset right hand side of a constraint.  
           
                The offset right hand side will only be used for coupler constraint types. 
              
         
        """
        pass
    @OffsetRightHandSide.setter
    def OffsetRightHandSide(self, offset: str):
        """
        Setter for property: (str) OffsetRightHandSide
         Returns 
                the offset right hand side of a constraint.  
           
                The offset right hand side will only be used for coupler constraint types. 
              
         
        """
        pass
    @property
    def Persistent(self) -> bool:
        """
        Getter for property: (bool) Persistent
         Returns 
                the persistent state of the constraint.  
          
              
         
        """
        pass
    @Persistent.setter
    def Persistent(self, persistent: bool):
        """
        Setter for property: (bool) Persistent
         Returns 
                the persistent state of the constraint.  
          
              
         
        """
        pass
    @property
    def SecondExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondExpression
         Returns 
                the second  NXOpen::Expression  of a constraint.  
           
                The second expression will be unused unless this constraint type supports a second expression. 
                This only applies to cylindrical joints.
              
         
        """
        pass
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
    @property
    def SecondLowerLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) SecondLowerLimitEnabled
         Returns 
                the lower limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @SecondLowerLimitEnabled.setter
    def SecondLowerLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) SecondLowerLimitEnabled
         Returns 
                the lower limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @property
    def SecondLowerLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondLowerLimitExpression
         Returns 
                the lower limit of the second expression of a constraint.  
          
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @property
    def SecondLowerLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) SecondLowerLimitRightHandSide
         Returns 
                the lower limit of the second expression right hand side of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @SecondLowerLimitRightHandSide.setter
    def SecondLowerLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) SecondLowerLimitRightHandSide
         Returns 
                the lower limit of the second expression right hand side of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @property
    def SecondUpperLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) SecondUpperLimitEnabled
         Returns 
                the upper limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @SecondUpperLimitEnabled.setter
    def SecondUpperLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) SecondUpperLimitEnabled
         Returns 
                the upper limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @property
    def SecondUpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondUpperLimitExpression
         Returns 
                the upper limit of the second expression of a constraint.  
           
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @property
    def SecondUpperLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) SecondUpperLimitRightHandSide
         Returns 
                the upper limit of the second expression right hand side of a constraint.  
          
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @SecondUpperLimitRightHandSide.setter
    def SecondUpperLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) SecondUpperLimitRightHandSide
         Returns 
                the upper limit of the second expression right hand side of a constraint.  
          
                The second limit expression will only be used for certain constraint types, and they must have a second expression. 
              
         
        """
        pass
    @property
    def SplinePointsType(self) -> Constraint.SplineType:
        """
        Getter for property: ( Constraint.SplineType NXOpen.P) SplinePointsType
         Returns the type of the spline.  
            Only valid if the type of the constraint is
              set to  NXOpen::Positioning::Constraint::TypeSplineData .   
         
        """
        pass
    @SplinePointsType.setter
    def SplinePointsType(self, spline_type: Constraint.SplineType):
        """
        Setter for property: ( Constraint.SplineType NXOpen.P) SplinePointsType
         Returns the type of the spline.  
            Only valid if the type of the constraint is
              set to  NXOpen::Positioning::Constraint::TypeSplineData .   
         
        """
        pass
    @property
    def Suppressed(self) -> bool:
        """
        Getter for property: (bool) Suppressed
         Returns 
                the suppression state for the constraint.  
           In a  NXOpen::Positioning::ComponentConstraint  this is the state in the  NXOpen::Positioning::ComponentPositioner::PrimaryArrangement ."
              
         
        """
        pass
    @Suppressed.setter
    def Suppressed(self, suppressed: bool):
        """
        Setter for property: (bool) Suppressed
         Returns 
                the suppression state for the constraint.  
           In a  NXOpen::Positioning::ComponentConstraint  this is the state in the  NXOpen::Positioning::ComponentPositioner::PrimaryArrangement ."
              
         
        """
        pass
    @property
    def UpperLimitEnabled(self) -> bool:
        """
        Getter for property: (bool) UpperLimitEnabled
         Returns 
                the upper limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression.  
              
         
        """
        pass
    @UpperLimitEnabled.setter
    def UpperLimitEnabled(self, hasLimit: bool):
        """
        Setter for property: (bool) UpperLimitEnabled
         Returns 
                the upper limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression.  
              
         
        """
        pass
    @property
    def UpperLimitExpression(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UpperLimitExpression
         Returns 
                the upper limit of the expression of a constraint.  
           
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @property
    def UpperLimitRightHandSide(self) -> str:
        """
        Getter for property: (str) UpperLimitRightHandSide
         Returns 
                the upper limit of the expression right hand side of a constraint.  
          
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @UpperLimitRightHandSide.setter
    def UpperLimitRightHandSide(self, limitRightHandSide: str):
        """
        Setter for property: (str) UpperLimitRightHandSide
         Returns 
                the upper limit of the expression right hand side of a constraint.  
          
                The limit expression will only be used for certain constraint types, and they must have an expression. 
              
         
        """
        pass
    @overload
    def CreateConstraintReference(self, movable_object: NXOpen.NXObject, geometry: NXOpen.NXObject, uses_axis: bool, is_indirect: bool) -> ConstraintReference:
        """
         
                Adds geometry to a constraint and sets the movable object
                to be constrained.
            
         Returns constraint_reference ( ConstraintReference NXOpen.P):  The new NXOpen.Positioning.ConstraintReference .
        """
        pass
    @overload
    def CreateConstraintReference(self, movable_object: NXOpen.NXObject, geometry: NXOpen.NXObject, uses_axis: bool, is_indirect: bool, use_port_rotate: bool) -> ConstraintReference:
        """
         
                Adds geometry to a constraint and sets the movable object
                to be constrained.  
            
         Returns constraint_reference ( ConstraintReference NXOpen.P):  The new NXOpen.Positioning.ConstraintReference .
        """
        pass
    def CreateCouplerReference(self, coupledConstraint: NXOpen.NXObject) -> ConstraintReference:
        """
         
                Adds constraint reference to a coupler.
            
         Returns couplerReference ( ConstraintReference NXOpen.P):  The new NXOpen.Positioning.ConstraintReference .
        """
        pass
    def DeleteConstraintReference(self, constraint_reference: ConstraintReference) -> None:
        """
         
                Removes a NXOpen.Positioning.ConstraintReference from the constraint. 
            
        """
        pass
    def EditConstraintReference(self, constraint_reference: ConstraintReference, movable_object: NXOpen.NXObject, geometry: NXOpen.NXObject, uses_axis: bool, is_indirect: bool, use_port_rotate: bool) -> None:
        """
         
                Adds geometry to a constraint and sets the movable object
                to be constrained, replacing the properties of an existing
                reference of the constraint.
            
        """
        pass
    def EditCouplerReference(self, couplerReference: ConstraintReference, coupledConstraint: NXOpen.NXObject) -> None:
        """
         
                Edit coupler reference so that it is replaced with another constraint.
            
        """
        pass
    def FlipAlignment(self) -> None:
        """
         
                Reverses the constraint alignment if this is possible.
            
        """
        pass
    def GenerateConversionReport(self) -> List[str]:
        """
                Returns a textual conversion report this constraint from when it was converted from a
                Mating Constraint to an Assembly Constraint. If this isn't a converted constraint
                or there were no problems converting this constraint, then an empty string is returned.
            
         Returns lines (List[str]):  The text lines of the conversion report .
        """
        pass
    def GetConstraintStatus(self) -> Constraint.SolverStatus:
        """
         
                Returns the solver status of a constraint.
            
         Returns status ( Constraint.SolverStatus NXOpen.P):  The solver status of the constraint .
        """
        pass
    def GetCreationDate(self) -> NXOpen.DateItemBuilder:
        """
         
               Returns the constraint creation date.
               The timestamp is recorded in the timezone of the machine where the operation is done.
               The user is required to delete the returned object.
            
         Returns creationDate ( NXOpen.DateItemBuilder):  The creation data of the constraint .
        """
        pass
    def GetDisplayedConstraint(self) -> DisplayedConstraint:
        """
                Gets the NXOpen.Positioning.DisplayedConstraint that is in the same part as that of the constraint.
                Note that this will be  if the part has not been the displayed part since the constraint was created.
            
         Returns displayed_constraint ( DisplayedConstraint NXOpen.P): .
        """
        pass
    def GetModifiedDate(self) -> NXOpen.DateItemBuilder:
        """
         
                Returns the constraint most recent modification date.
                The timestamp is recorded in the timezone of the machine where the operation is done.
                The user is required to delete the returned object.
            
         Returns modifiedDate ( NXOpen.DateItemBuilder):  The constraint most recent modification date .
        """
        pass
    def GetReferences(self) -> List[ConstraintReference]:
        """
         
                Gets all the NXOpen.Positioning.ConstraintReferences for the 
                constraint.
            
         Returns references ( ConstraintReference List[NXOpen):  ConstraintReferences used by this constraint .
        """
        pass
    def Renew(self) -> None:
        """
         Changes the constraint to solve with the latest version of the constraint code. 
        """
        pass
    def ReverseDirection(self) -> None:
        """
         
                Reverses the constraint direction.  This operation reverses the NXOpen.Positioning.ConstraintReference.Order
                on each NXOpen.Positioning.ConstraintReference.
                So "Inside" becomes "Outside", "Outside" becomes "Inside" and "Unknown" remains as it is.
            
        """
        pass
    def SetAlignmentHint(self, alignment: Constraint.Alignment) -> None:
        """
         
                Set a hint as to which alignment should be used by the
                solver for this constraint.
                
                If the constraint does not solve using this alignment
                then the hint will be ignored.                
                
                The hint can only have an effect when the alignment of
                the constraint, as returned by NXOpen.Positioning.Constraint.ConstraintAlignment,
                is NXOpen.Positioning.Constraint.Alignment.InferAlign.
                
                The hint can only have an effect when the constraint has been
                explicitly added to a NXOpen.Positioning.Network.
                
                Passing in NXOpen.Positioning.Constraint.Alignment.InferAlign as the alignment
                argument will have no effect.
                
                The hint is forgotten after an update.
            
        """
        pass
    def SetExpression(self, expression: str) -> None:
        """
         
                The NXOpen.Expression of a constraint - only used if this 
                constraint type supports an expression, such as a distance or angle constraint,
                or a joint. 
            
        """
        pass
import NXOpen
class DisplayedConstraintCollection(NXOpen.TaggedObjectCollection): 
    """
        a collection of displayed constraints    
    """
    pass
import NXOpen
import NXOpen.Assemblies
class DisplayedConstraint(NXOpen.DisplayableObject): 
    """
        The displayed representation of a constraint, used for graphical
        display and to represent it in the Assembly Navigator.

        Instances of NXOpen.Positioning.DisplayedConstraint are created whenever a
        NXOpen.Positioning.Constraint is created.

        A NXOpen.Positioning.Constraint has an instance of NXOpen.Positioning.DisplayedConstraint
        in the same part as itself, but an instance of NXOpen.Positioning.DisplayedConstraint doesn't
        necessarily exist in the same part as the underlying NXOpen.Positioning.Constraint.
    """
    def GetConstraint(self) -> Constraint:
        """
         
                    Get the underlying NXOpen.Positioning.Constraint.
                    
                    Note that this will be  if the underlying NXOpen.Positioning.Constraint is unloaded.
                     
                
         Returns constraint ( Constraint NXOpen.P):  The underlying constraint .
        """
        pass
    def GetConstraintPart(self) -> NXOpen.Part:
        """
         
                    Get the part containing the underlying NXOpen.Positioning.Constraint.
                    
                    Note that this will be  if the underlying NXOpen.Positioning.Constraint is unloaded.
                    
                
         Returns part ( NXOpen.Part):  The part containing the underlying constraint .
        """
        pass
    def GetContextComponent(self) -> NXOpen.Assemblies.Component:
        """
                    Get the component containing the underlying NXOpen.Positioning.Constraint.
                    
                    Note that this will be  if the underlying NXOpen.Positioning.Constraint is in the
                    same part as the displayed constraint.
                    
                
         Returns component ( NXOpen.Assemblies.Component): .
        """
        pass
import NXOpen
class MatingConverter(NXOpen.TaggedObject): 
    """
      An instance of this class can be used to convert Mating Conditions
      to Assembly Constraints in its owning assembly or in child parts
      of its owning assembly. The owning assembly is the
      NXOpen.Assemblies.ComponentAssembly from which this
      object was obtained using
      NXOpen.Assemblies.ComponentAssembly.CreateMatingConverter.
    """
    class PartContext(Enum):
        """
        Members Include: 
         |InOwningPart|  Convert mating conditions in the owning part 
         |InLoadedChildren|  Convert mating conditions in the owning part
                                                                             and all loaded children. Partially-loaded
                                                                             children will be fully-loaded. 
         |InAllChildren|  Convert mating conditions in the owning part
                                                                             and all children. Partially-loaded and unloaded
                                                                             children will be fully-loaded. 

        """
        InOwningPart: int
        InLoadedChildren: int
        InAllChildren: int
        @staticmethod
        def ValueOf(value: int) -> MatingConverter.PartContext:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Context(self) -> MatingConverter.PartContext:
        """
        Getter for property: ( MatingConverter.PartContext NXOpen.P) Context
         Returns
                    the current conversion context in which mating conditions will be converted.  
          
                  
         
        """
        pass
    @Context.setter
    def Context(self, context: MatingConverter.PartContext):
        """
        Setter for property: ( MatingConverter.PartContext NXOpen.P) Context
         Returns
                    the current conversion context in which mating conditions will be converted.  
          
                  
         
        """
        pass
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
    @property
    def LoadStatus(self) -> NXOpen.PartLoadStatus:
        """
        Getter for property: ( NXOpen.PartLoadStatus) LoadStatus
         Returns
                    the load status resulting from a conversion operation.  
           This indicates
                    any problems which arose when loading parts during conversion.
                  
         
        """
        pass
    @property
    def NumberOfConvertedParts(self) -> int:
        """
        Getter for property: (int) NumberOfConvertedParts
         Returns
                    the number of parts parts converted by this conversion operation.  
          
                  
         
        """
        pass
    def ConvertMatingConditions(self) -> None:
        """
                    Converts Mating Conditions to Assembly Constraints according to the
                    properties defined on this NXOpen.Positioning.MatingConverter
                    object.
                
        """
        pass
    def DeleteResults(self) -> None:
        """
                    Removes details from the mating conversion results of the individual constraints that were converted.
                    This will be applied to the mating conversion results in the parts described by the current context
                    (determined by NXOpen.Positioning.MatingConverter.Context). Note that the
                    summary information for each part in the conversion results is not modified by this function.
                
        """
        pass
    def Destroy(self) -> None:
        """
                    Deletes this NXOpen.Positioning.MatingConverter immediately.
                
        """
        pass
    def GetConvertedConstraints(self) -> List[Constraint]:
        """
                    Returns all constraints converted by this conversion operation.
                    Use NXOpen.Positioning.Constraint.GenerateConversionReport
                    to obtain the conversion status of these constraints.
                
         Returns converted_constraints ( Constraint List[NXOpen):  The converted constraints .
        """
        pass
    def GetConvertedParts(self) -> List[Constraint]:
        """
                    Returns all parts converted by this conversion operation.
                
         Returns converted_constraints ( Constraint List[NXOpen):  The converted constraints .
        """
        pass
    def GetLatestResults(self, show_all_results: bool) -> List[str]:
        """
                    Returns textual descriptions of the results of the last conversion operation
                
         Returns result_lines (List[str]):  The generated results .
        """
        pass
    def GetResults(self, show_all_results: bool) -> List[str]:
        """
                    Returns textual descriptions of the results of all prior conversion
                    operations for all the parts described by the current context set using
                    NXOpen.Positioning.MatingConverter.Context.
                
         Returns result_lines (List[str]):  The generated results .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class Network(NXOpen.NXObject): 
    """
    Network for use in positioning objects in NX.
    A network consists of explicitly added constraints and movable objects
    together with others implicitly added because they are connected by 
    to those in the network.
"""
    class ObjectStatus(Enum):
        """
        Members Include: 
         |Unknown|  Not yet evaluated. 
         |Fixed|  Attempt to put constraint between two fixed objects. 
         |OverDefined|  Conflicts with other constraints. 
         |NotConsistentDims|  Cannot solve with current dimension values. Model fully defined. 
         |NotConsistentOther|  Cannot find a solution. Model underdefined.
         |NotConsistentUnknown|  One movable object fixed. 
         |NotChanged|  Not evaluated because other parts of the model are over defined or inconsistent. 
         |WellDefined|  The constraint is solved and satisfied 
         |UnderDefined|  The constraint is solved and satisfied 

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
        @staticmethod
        def ValueOf(value: int) -> Network.ObjectStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DisplayComponent(self) -> NXOpen.Assemblies.Component:
        """
        Getter for property: ( NXOpen.Assemblies.Component) DisplayComponent
         Returns 
                the  Assemblies::Component  in which the display is changed
                by solving the network.  
           The display component can be NULL if display
                changes are made in the part of the network.
                The prototype of the display component should be the part containing the
                network.
              
         
        """
        pass
    @DisplayComponent.setter
    def DisplayComponent(self, display_component: NXOpen.Assemblies.Component):
        """
        Setter for property: ( NXOpen.Assemblies.Component) DisplayComponent
         Returns 
                the  Assemblies::Component  in which the display is changed
                by solving the network.  
           The display component can be NULL if display
                changes are made in the part of the network.
                The prototype of the display component should be the part containing the
                network.
              
         
        """
        pass
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
    def AddConstraint(self, constraint: Constraint) -> None:
        """
         
                Add a Constraint to the network.
            
        """
        pass
    def AddMovableObject(self, movable_object: NXOpen.NXObject) -> None:
        """
         
                Add a movable object to the network. An object explicitly added
                by this method will be directly moved by calls 
                to Positioning.Network.DragByRay,
                Positioning.Network.DragByTransform and
                Positioning.Network.DragByTranslation.        
            
        """
        pass
    def ApplyToModel(self) -> None:
        """
         
                Applies the current network state to the model.  This may change the position
                of movable objects and the status of constraints in the model.  Does not do 
                a solve or an update.
            
        """
        pass
    def BeginDrag(self) -> None:
        """
         
                Notify the network that a sequence of drag operations is about to
                begin.
                
                This must be called before a series of calls to
                Positioning.Network.DragByRay,
                Positioning.Network.DragByTransform or
                Positioning.Network.DragByTranslation.
                Following a drag, and before any other changes to a network
                are made, Positioning.Network.EndDrag
                should be called.
                
            
        """
        pass
    def DragByRay(self, point: NXOpen.Point3d, direction: NXOpen.Vector3d) -> None:
        """
         
                Move objects which have been added to the network using 
                Positioning.Network.AddMovableObject.
                Constraints are honored during the drag so that other
                objects may also move as a result of this call.
                On the first call to this method, a notional point is added to each of
                the objects to be dragged.  On subsequent calls, this notional point,
                and hence the dragged object, is kept as close as possible to the ray
                determined by point and direction. If there are no constraints then the
                point will stay on the ray.
                
                A series of calls to this method can be made between calls to
                Positioning.Network.BeginDrag and
                Positioning.Network.EndDrag.
                
            
        """
        pass
    def DragByTransform(self, translation: NXOpen.Vector3d, rotation: NXOpen.Matrix3x3) -> None:
        """
         
                Move objects which have been added to the network using 
                Positioning.Network.AddMovableObject.
                Constraints are honored during the drag so that other
                objects may also move as a result of this call.
                The rotation is applied first, then the translation.
                
                A series of calls to this method can be made between calls to
                Positioning.Network.BeginDrag and
                Positioning.Network.EndDrag.
                
            
        """
        pass
    def DragByTranslation(self, translation: NXOpen.Vector3d) -> None:
        """
         
                Move objects which have been added to the network using 
                Positioning.Network.AddMovableObject.
                Constraints are honored during the drag so that other
                objects may also move as a result of this call.
                Unlike Positioning.Network.DragByTransform
                there is no rotational element passed in. This can improve the
                behavior of the constraint solver.
                
                A series of calls to this method can be made between calls to
                Positioning.Network.BeginDrag and
                Positioning.Network.EndDrag.
                
            
        """
        pass
    def EmptyMovingGroup(self) -> None:
        """
         
                Remove all elements from the moving_group.
                See Positioning.Network.SetMovingGroup.
            
        """
        pass
    def EndDrag(self) -> None:
        """
         
                Notify the network that a sequence of drag operations has
                ended.
                
                This must be called after a series of calls to
                Positioning.Network.DragByRay,
                Positioning.Network.DragByTransform or
                Positioning.Network.DragByTranslation.
                
            
        """
        pass
    def GetMovableObjectStatus(self, movable_object: NXOpen.NXObject) -> Network.ObjectStatus:
        """
         
                Returns the solver status of a movable object.
            
         Returns status ( Network.ObjectStatus NXOpen.P):  The solver status of the movable object .
        """
        pass
    def IsReferencedGeometryLoaded(self) -> bool:
        """
         
                Are the necessary objects loaded so that all connected constraints can be
                included during a drag or solve ?
            
         Returns loaded (bool): .
        """
        pass
    def LoadReferencedGeometry(self) -> None:
        """
         
                Load the necessary objects so that all connected constraints can be
                included during a drag or solve.
                If an object is not loaded then the part containing it will be 
                fully loaded by this call.
            
        """
        pass
    def RemoveAllConstraints(self) -> None:
        """
         
                Remove all Constraints which have been explicitly added
                to the network.  Those constraints connected to explicitly added movable
                objects will still be include in a network solve.
            
        """
        pass
    def RemoveConstraint(self, constraint: Constraint) -> None:
        """
         
                Remove a Constraint from the network. A constraint
                explicitly removed by this method may still included in a network solve
                if connected to another constraint or movable object which has been
                explicitly added.
            
        """
        pass
    def RemoveMovableObject(self, movable_object: NXOpen.NXObject) -> None:
        """
         
                Remove a movable object from the network. An object explicitly
                removed by this method will not be directly moved by calls 
                to Positioning.Network.DragByRay,
                Positioning.Network.DragByTransform and
                Positioning.Network.DragByTranslation, though it
                may still be moved indirectly if constrained to other movable objects.
            
        """
        pass
    def ResetDisplay(self) -> None:
        """
         
                Returns the display objects to their model positions.
            
        """
        pass
    def SetMovingGroup(self, movable_objects: List[NXOpen.NXObject]) -> None:
        """
         
                Set the elements of the moving_group. 
                The elements of the moving_group will move as a rigid body
                during a solve or drag operation.  Objects outside the moving
                group can all be prevented from moving by setting 
                Positioning.Network.NonMovingGroupGrounded
            
        """
        pass
    def Solve(self) -> None:
        """
         
                Solves the constraint network.
                Does apply the results to the model but does not 
                do an update.
            
        """
        pass
import NXOpen
class Positioner(NXOpen.NXObject): 
    """
  An instance of this class can be used to create NXOpen.Positioning.Constraints and
  associated objects.
"""
    @property
    def Constraints() -> ConstraintCollection:
        """
         The collection of  NXOpen::Positioning::Constraint s defined in the positioner 
        """
        pass
    def ClearNetwork(self) -> None:
        """
         
                Removes the NXOpen.Positioning.Network of the positioner.
                The network is added to the delete list by this call.
            
        """
        pass
    @overload
    def CreateConstraint(self, persistent: bool) -> Constraint:
        """
         
                Creates a new NXOpen.Positioning.Constraint in the positioner.
            
         Returns constraint ( Constraint NXOpen.P):  The new NXOpen.Positioning.Constraint .
        """
        pass
    @overload
    def CreateConstraint(self) -> Constraint:
        """
         
                Creates a new NXOpen.Positioning.Constraint in the positioner.
            
         Returns constraint ( Constraint NXOpen.P):  The new NXOpen.Positioning.Constraint .
        """
        pass
    def DeleteNonPersistentConstraints(self) -> None:
        """
         
                Deletes all the non-persistent NXOpen.Positioning.Constraints of the positioner.
            
        """
        pass
    def EstablishNetwork(self) -> Network:
        """
         
                Establishes a NXOpen.Positioning.Network in the positioner.
            
         Returns network ( Network NXOpen.P):  The new NXOpen.Positioning.Network .
        """
        pass
