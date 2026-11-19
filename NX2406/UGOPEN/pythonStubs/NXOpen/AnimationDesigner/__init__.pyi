from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::ActivityOperatorBuilder NXOpen::AnimationDesigner::ActivityOperatorBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::ActivityOperatorCollection::CreateActivityOperatorBuilder  NXOpen::AnimationDesigner::ActivityOperatorCollection::CreateActivityOperatorBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class ActivityOperatorBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.ActivityOperatorBuilder</ja_class>. """


    ##  the active action types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Active</term><description> 
    ##  Active an event </description> </item><item><term> 
    ## Deactive</term><description> 
    ##  Inactive an event </description> </item></list>
    class ActionTypes(Enum):
        """
        Members Include: <Active> <Deactive>
        """
        Active: int
        Deactive: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ActivityOperatorBuilder.ActionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) ActionObject
    ##  Returns the base list for a Joint.  
    ##    The list can consist of @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  
    ##         objects or other objects which can active and deactive.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def ActionObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) ActionObject
         Returns the base list for a Joint.  
           The list can consist of @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  
                objects or other objects which can active and deactive.   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ##  Creates a new bar. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    
    ##  Deletes the bars. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    
    ##  Gets the bar start time. 
    ##  @return start_time (float): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    def GetTime(self, index: int) -> float:
        """
         Gets the bar start time. 
         @return start_time (float): .
        """
        pass
    
    ##  Sets the bar action type. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="actionType"> (@link ActivityOperatorBuilder.ActionTypes NXOpen.AnimationDesigner.ActivityOperatorBuilder.ActionTypes@endlink) </param>
    def SetBarActionType(self, index: int, actionType: ActivityOperatorBuilder.ActionTypes) -> None:
        """
         Sets the bar action type. 
        """
        pass
    
    ##  Sets the bar name. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="name"> (str) </param>
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    
    ##  Sets the bar start time. 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="start_time"> (float) </param>
    def SetTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
    
import NXOpen
##  Represents a collection of Activity Operator objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class ActivityOperatorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Activity Operator objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::ActivityOperatorBuilder NXOpen::AnimationDesigner::ActivityOperatorBuilder@endlink . 
    ##  @return builder (@link ActivityOperatorBuilder NXOpen.AnimationDesigner.ActivityOperatorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="activityOperator"> (@link ActivityOperator NXOpen.AnimationDesigner.ActivityOperator@endlink)  @link NXOpen::AnimationDesigner::ActivityOperator NXOpen::AnimationDesigner::ActivityOperator@endlink  to be edited, if NULL then create a new one </param>
    def CreateActivityOperatorBuilder(part: NXOpen.Part, activityOperator: ActivityOperator) -> ActivityOperatorBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::ActivityOperatorBuilder NXOpen::AnimationDesigner::ActivityOperatorBuilder@endlink . 
         @return builder (@link ActivityOperatorBuilder NXOpen.AnimationDesigner.ActivityOperatorBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::ActivityOperator   NXOpen::AnimationDesigner::ActivityOperator @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return activityOperator (@link ActivityOperator NXOpen.AnimationDesigner.ActivityOperator@endlink):  @link  NXOpen::AnimationDesigner::ActivityOperator   NXOpen::AnimationDesigner::ActivityOperator @endlink  with this name. .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::ActivityOperator   NXOpen::AnimationDesigner::ActivityOperator @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> ActivityOperator:
        """
         Finds the @link  NXOpen::AnimationDesigner::ActivityOperator   NXOpen::AnimationDesigner::ActivityOperator @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return activityOperator (@link ActivityOperator NXOpen.AnimationDesigner.ActivityOperator@endlink):  @link  NXOpen::AnimationDesigner::ActivityOperator   NXOpen::AnimationDesigner::ActivityOperator @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a Activity Operator feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::ActivityOperatorBuilder  NXOpen::AnimationDesigner::ActivityOperatorBuilder @endlink  <br> 
## 
##   <br>  Created in NX2406.0.0  <br> 

class ActivityOperator(NXOpen.DisplayableObject): 
    """ Represents a Activity Operator feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::AnimatedCameraBuilder NXOpen::AnimationDesigner::AnimatedCameraBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::AnimatedCameraCollection::CreateAnimatedCameraBuilder  NXOpen::AnimationDesigner::AnimatedCameraCollection::CreateAnimatedCameraBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedCameraBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.AnimatedCameraBuilder</ja_class>. """


    ##   @brief  the camera axis types.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ##  X </description> </item><item><term> 
    ## Y</term><description> 
    ##  Y </description> </item><item><term> 
    ## Z</term><description> 
    ##  Z </description> </item></list>
    class CameraAxisTypes(Enum):
        """
        Members Include: <X> <Y> <Z>
        """
        X: int
        Y: int
        Z: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.CameraAxisTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief  the camera mode types.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## UserDefined</term><description> 
    ##  User Defined </description> </item><item><term> 
    ## Turntable</term><description> 
    ##  Turntable </description> </item><item><term> 
    ## Trajectory</term><description> 
    ##  Trajectory </description> </item></list>
    class CameraModeTypes(Enum):
        """
        Members Include: <UserDefined> <Turntable> <Trajectory>
        """
        UserDefined: int
        Turntable: int
        Trajectory: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.CameraModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief  the look at direction types.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## WithRigid</term><description> 
    ##  associate with rigid </description> </item><item><term> 
    ## AlongPath</term><description> 
    ##  along path curve </description> </item><item><term> 
    ## LookAtObject</term><description> 
    ##  look at object </description> </item><item><term> 
    ## Fixed</term><description> 
    ##  direction fixed </description> </item></list>
    class LookAtDirectionTypes(Enum):
        """
        Members Include: <WithRigid> <AlongPath> <LookAtObject> <Fixed>
        """
        WithRigid: int
        AlongPath: int
        LookAtObject: int
        Fixed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.LookAtDirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief  the transition mode types.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Path</term><description> 
    ##  Path </description> </item></list>
    class TransitionModeTypes(Enum):
        """
        Members Include: <Linear> <Path>
        """
        Linear: int
        Path: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.TransitionModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AnimationCamera
    ##  Returns the associated animation camera.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def AnimationCamera(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AnimationCamera
         Returns the associated animation camera.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AnimationCamera

    ##  Returns the associated animation camera.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AnimationCamera.setter
    def AnimationCamera(self, animation_camera: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AnimationCamera
         Returns the associated animation camera.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) AssociateObjects
    ##  Returns the associate object selection.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def AssociateObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) AssociateObjects
         Returns the associate object selection.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AvoidViewRoll
    ##  Returns the 'Associated to Object' mode avoid view roll option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def AvoidViewRoll(self) -> bool:
        """
        Getter for property: (bool) AvoidViewRoll
         Returns the 'Associated to Object' mode avoid view roll option.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AvoidViewRoll

    ##  Returns the 'Associated to Object' mode avoid view roll option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AvoidViewRoll.setter
    def AvoidViewRoll(self, bAvoidRoll: bool):
        """
        Setter for property: (bool) AvoidViewRoll
         Returns the 'Associated to Object' mode avoid view roll option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CameraAngle
    ##  Returns the camera angle.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CameraAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CameraAngle
         Returns the camera angle.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedCameraBuilder.CameraAxisTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraAxisTypes@endlink) CameraAxisType
    ##  Returns  @brief  the axis type.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AnimatedCameraBuilder.CameraAxisTypes
    @property
    def CameraAxisType(self) -> AnimatedCameraBuilder.CameraAxisTypes:
        """
        Getter for property: (@link AnimatedCameraBuilder.CameraAxisTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraAxisTypes@endlink) CameraAxisType
         Returns  @brief  the axis type.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link AnimatedCameraBuilder.CameraAxisTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraAxisTypes@endlink) CameraAxisType

    ##  Returns  @brief  the axis type.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CameraAxisType.setter
    def CameraAxisType(self, axisType: AnimatedCameraBuilder.CameraAxisTypes):
        """
        Setter for property: (@link AnimatedCameraBuilder.CameraAxisTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraAxisTypes@endlink) CameraAxisType
         Returns  @brief  the axis type.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link AnimatedCameraBuilder.CameraModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraModeTypes@endlink) CameraModeType
    ##  Returns  @brief  the mode type.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AnimatedCameraBuilder.CameraModeTypes
    @property
    def CameraModeType(self) -> AnimatedCameraBuilder.CameraModeTypes:
        """
        Getter for property: (@link AnimatedCameraBuilder.CameraModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraModeTypes@endlink) CameraModeType
         Returns  @brief  the mode type.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link AnimatedCameraBuilder.CameraModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraModeTypes@endlink) CameraModeType

    ##  Returns  @brief  the mode type.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @CameraModeType.setter
    def CameraModeType(self, modeType: AnimatedCameraBuilder.CameraModeTypes):
        """
        Setter for property: (@link AnimatedCameraBuilder.CameraModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraModeTypes@endlink) CameraModeType
         Returns  @brief  the mode type.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) CameraOrientation
    ##  Returns the 'Associated to Object' mode camera init orientation.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def CameraOrientation(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) CameraOrientation
         Returns the 'Associated to Object' mode camera init orientation.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) CameraOrientation

    ##  Returns the 'Associated to Object' mode camera init orientation.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @CameraOrientation.setter
    def CameraOrientation(self, camera_orientation: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) CameraOrientation
         Returns the 'Associated to Object' mode camera init orientation.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedCameraBuilder.LookAtDirectionTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.LookAtDirectionTypes@endlink) DirectionType
    ##  Returns  @brief  the 'Associated to Object' mode look at direction type.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return AnimatedCameraBuilder.LookAtDirectionTypes
    @property
    def DirectionType(self) -> AnimatedCameraBuilder.LookAtDirectionTypes:
        """
        Getter for property: (@link AnimatedCameraBuilder.LookAtDirectionTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.LookAtDirectionTypes@endlink) DirectionType
         Returns  @brief  the 'Associated to Object' mode look at direction type.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link AnimatedCameraBuilder.LookAtDirectionTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.LookAtDirectionTypes@endlink) DirectionType

    ##  Returns  @brief  the 'Associated to Object' mode look at direction type.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DirectionType.setter
    def DirectionType(self, lookAtDirType: AnimatedCameraBuilder.LookAtDirectionTypes):
        """
        Setter for property: (@link AnimatedCameraBuilder.LookAtDirectionTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.LookAtDirectionTypes@endlink) DirectionType
         Returns  @brief  the 'Associated to Object' mode look at direction type.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndPathPoint
    ##  Returns the 'Associated to Object' mode associated curve end point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def EndPathPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndPathPoint
         Returns the 'Associated to Object' mode associated curve end point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndPathPoint

    ##  Returns the 'Associated to Object' mode associated curve end point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @EndPathPoint.setter
    def EndPathPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) EndPathPoint
         Returns the 'Associated to Object' mode associated curve end point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndTime
    ##  Returns the 'Associated to Object' mode end time.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def EndTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) EndTime
         Returns the 'Associated to Object' mode end time.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) LookAtObject
    ##  Returns the 'Associated to Object' mode look at object selection.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def LookAtObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) LookAtObject
         Returns the 'Associated to Object' mode look at object selection.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnLookAtRigid
    ##  Returns the 'Associated to Object' mode look at point on look at object.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointOnLookAtRigid(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnLookAtRigid
         Returns the 'Associated to Object' mode look at point on look at object.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnLookAtRigid

    ##  Returns the 'Associated to Object' mode look at point on look at object.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @PointOnLookAtRigid.setter
    def PointOnLookAtRigid(self, lookAtPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnLookAtRigid
         Returns the 'Associated to Object' mode look at point on look at object.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationSpeed
    ##  Returns the rotational speed.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def RotationSpeed(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) RotationSpeed
         Returns the rotational speed.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SpecifyTime
    ##  Returns the 'Associated to Object' mode specify time option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def SpecifyTime(self) -> bool:
        """
        Getter for property: (bool) SpecifyTime
         Returns the 'Associated to Object' mode specify time option.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SpecifyTime

    ##  Returns the 'Associated to Object' mode specify time option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SpecifyTime.setter
    def SpecifyTime(self, specifyTime: bool):
        """
        Setter for property: (bool) SpecifyTime
         Returns the 'Associated to Object' mode specify time option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPathPoint
    ##  Returns the 'Associated to Object' mode associated curve start point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def StartPathPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPathPoint
         Returns the 'Associated to Object' mode associated curve start point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPathPoint

    ##  Returns the 'Associated to Object' mode associated curve start point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @StartPathPoint.setter
    def StartPathPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPathPoint
         Returns the 'Associated to Object' mode associated curve start point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartTime
    ##  Returns the 'Associated to Object' mode start time.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartTime
         Returns the 'Associated to Object' mode start time.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedCameraBuilder.TransitionModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.TransitionModeTypes@endlink) TransitionModeType
    ##  Returns  @brief  the transition mode type.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return AnimatedCameraBuilder.TransitionModeTypes
    @property
    def TransitionModeType(self) -> AnimatedCameraBuilder.TransitionModeTypes:
        """
        Getter for property: (@link AnimatedCameraBuilder.TransitionModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.TransitionModeTypes@endlink) TransitionModeType
         Returns  @brief  the transition mode type.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link AnimatedCameraBuilder.TransitionModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.TransitionModeTypes@endlink) TransitionModeType

    ##  Returns  @brief  the transition mode type.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @TransitionModeType.setter
    def TransitionModeType(self, transitionModeType: AnimatedCameraBuilder.TransitionModeTypes):
        """
        Setter for property: (@link AnimatedCameraBuilder.TransitionModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.TransitionModeTypes@endlink) TransitionModeType
         Returns  @brief  the transition mode type.  
            
        
            
         
        """
        pass
    
    ##  Creates a new pov. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="currentTime"> (float) </param>
    def CreatePOV(self, currentTime: float) -> None:
        """
         Creates a new pov. 
        """
        pass
    
    ##  Deletes the povs. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="povs"> (List[int]) </param>
    def DeletePOVs(self, povs: List[int]) -> None:
        """
         Deletes the povs. 
        """
        pass
    
    ##  Evaluate the composited path from associated curves. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge</param>
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluate the composited path from associated curves. 
        """
        pass
    
    ##  Play key frame at time 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="time"> (float) </param>
    def PlayKeyFrameAtTime(self, time: float) -> None:
        """
         Play key frame at time 
        """
        pass
    
    ##  Sets the pov name. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="name"> (str) </param>
    def SetPOVName(self, pos: int, name: str) -> None:
        """
         Sets the pov name. 
        """
        pass
    
    ##  Sets the pov start time. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="start_time"> (float) </param>
    def SetPOVStartTime(self, pos: int, start_time: float) -> None:
        """
         Sets the pov start time. 
        """
        pass
    
    ##  Sets the pov step count. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="step_num"> (int) </param>
    def SetPOVStepNumber(self, pos: int, step_num: int) -> None:
        """
         Sets the pov step count. 
        """
        pass
    
    ##  Sets the view scale value. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="fViewScale"> (float) </param>
    def SetViewScale(self, fViewScale: float) -> None:
        """
         Sets the view scale value. 
        """
        pass
    
    ##  Updates current view 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="rotation"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink) </param>
    ## <param name="translation"> (@link NXOpen.Point3d NXOpen.Point3d@endlink) </param>
    ## <param name="scale"> (float) </param>
    def UpdateCurrentView(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Point3d, scale: float) -> None:
        """
         Updates current view 
        """
        pass
    
    ##  Updates a pov 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    def UpdatePOV(self, pos: int) -> None:
        """
         Updates a pov 
        """
        pass
    
import NXOpen
##  Represents a collection of Animated Camera objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedCameraCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Camera objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::AnimatedCameraBuilder NXOpen::AnimationDesigner::AnimatedCameraBuilder@endlink . 
    ##  @return builder (@link AnimatedCameraBuilder NXOpen.AnimationDesigner.AnimatedCameraBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="animatedCamera"> (@link AnimatedCamera NXOpen.AnimationDesigner.AnimatedCamera@endlink)  @link NXOpen::AnimationDesigner::AnimatedCamera NXOpen::AnimationDesigner::AnimatedCamera@endlink  to be edited, if NULL then create a new one </param>
    def CreateAnimatedCameraBuilder(part: NXOpen.Part, animatedCamera: AnimatedCamera) -> AnimatedCameraBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::AnimatedCameraBuilder NXOpen::AnimationDesigner::AnimatedCameraBuilder@endlink . 
         @return builder (@link AnimatedCameraBuilder NXOpen.AnimationDesigner.AnimatedCameraBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::AnimatedCamera   NXOpen::AnimationDesigner::AnimatedCamera @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return animatedCamera (@link AnimatedCamera NXOpen.AnimationDesigner.AnimatedCamera@endlink):  @link  NXOpen::AnimationDesigner::AnimatedCamera   NXOpen::AnimationDesigner::AnimatedCamera @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::AnimatedCamera   NXOpen::AnimationDesigner::AnimatedCamera @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedCamera:
        """
         Finds the @link  NXOpen::AnimationDesigner::AnimatedCamera   NXOpen::AnimationDesigner::AnimatedCamera @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return animatedCamera (@link AnimatedCamera NXOpen.AnimationDesigner.AnimatedCamera@endlink):  @link  NXOpen::AnimationDesigner::AnimatedCamera   NXOpen::AnimationDesigner::AnimatedCamera @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents an Animated Camera feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::AnimatedCameraBuilder  NXOpen::AnimationDesigner::AnimatedCameraBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedCamera(NXOpen.DisplayableObject): 
    """ Represents an Animated Camera feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::AnimatedColorBuilder NXOpen::AnimationDesigner::AnimatedColorBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::AnimatedColorCollection::CreateAnimatedColorBuilder  NXOpen::AnimationDesigner::AnimatedColorCollection::CreateAnimatedColorBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CreationType </term> <description> 
##  
## CreateaSingleAnimatedColorEffect </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1953.0.0  <br> 

class AnimatedColorBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.AnimatedColorBuilder</ja_class>. """


    ##  the enumeration types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CreateaSingleAnimatedColorEffect</term><description> 
    ## </description> </item><item><term> 
    ## CreateanAnimatedColorEffectperObject</term><description> 
    ## </description> </item></list>
    class CreationTypes(Enum):
        """
        Members Include: <CreateaSingleAnimatedColorEffect> <CreateanAnimatedColorEffectperObject>
        """
        CreateaSingleAnimatedColorEffect: int
        CreateanAnimatedColorEffectperObject: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedColorBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedColorBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedColorBuilder.CreationTypes@endlink) CreationType
    ##  Returns the creation type   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return AnimatedColorBuilder.CreationTypes
    @property
    def CreationType(self) -> AnimatedColorBuilder.CreationTypes:
        """
        Getter for property: (@link AnimatedColorBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedColorBuilder.CreationTypes@endlink) CreationType
         Returns the creation type   
            
         
        """
        pass
    
    ## Setter for property: (@link AnimatedColorBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedColorBuilder.CreationTypes@endlink) CreationType

    ##  Returns the creation type   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CreationType.setter
    def CreationType(self, creationType: AnimatedColorBuilder.CreationTypes):
        """
        Setter for property: (@link AnimatedColorBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedColorBuilder.CreationTypes@endlink) CreationType
         Returns the creation type   
            
         
        """
        pass
    
    ## Getter for property: (bool) EnableRepeatTime
    ##  Returns the option determines whether to set the repeat time.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def EnableRepeatTime(self) -> bool:
        """
        Getter for property: (bool) EnableRepeatTime
         Returns the option determines whether to set the repeat time.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EnableRepeatTime

    ##  Returns the option determines whether to set the repeat time.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @EnableRepeatTime.setter
    def EnableRepeatTime(self, enableRepeatTime: bool):
        """
        Setter for property: (bool) EnableRepeatTime
         Returns the option determines whether to set the repeat time.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (int) RepeatTime
    ##  Returns the repeat time.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def RepeatTime(self) -> int:
        """
        Getter for property: (int) RepeatTime
         Returns the repeat time.  
             
         
        """
        pass
    
    ## Setter for property: (int) RepeatTime

    ##  Returns the repeat time.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @RepeatTime.setter
    def RepeatTime(self, repeatTime: int):
        """
        Setter for property: (int) RepeatTime
         Returns the repeat time.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectObject
    ##  Returns the select object   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectObject
         Returns the select object   
            
         
        """
        pass
    
    ##  Creates a new bar. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    
    ##  Deletes the bars. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    
    ##  Mirrors the bars. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    ## <param name="mirror_time"> (float) </param>
    def MirrorBars(self, bars: List[int], mirror_time: float) -> None:
        """
         Mirrors the bars. 
        """
        pass
    
    ##  Sets the bar end color. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="color"> (@link NXOpen.NXColor NXOpen.NXColor@endlink) </param>
    def SetBarEndColor(self, index: int, color: NXOpen.NXColor) -> None:
        """
         Sets the bar end color. 
        """
        pass
    
    ##  Sets the bar end time. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="end_time"> (float) </param>
    def SetBarEndTime(self, index: int, end_time: float) -> None:
        """
         Sets the bar end time. 
        """
        pass
    
    ##  Sets the bar name. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="name"> (str) </param>
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    
    ##  Sets the bar start . 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="color"> (@link NXOpen.NXColor NXOpen.NXColor@endlink) </param>
    def SetBarStartColor(self, index: int, color: NXOpen.NXColor) -> None:
        """
         Sets the bar start . 
        """
        pass
    
    ##  Sets the bar start time. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="start_time"> (float) </param>
    def SetBarStartTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
    
    ##  Splits the bar with the split time. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="split_time"> (float) </param>
    def SplitBar(self, index: int, split_time: float) -> None:
        """
         Splits the bar with the split time. 
        """
        pass
    
import NXOpen
##  Represents a collection of Animated Color objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AnimatedColorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Color objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::AnimatedColorBuilder NXOpen::AnimationDesigner::AnimatedColorBuilder@endlink . 
    ##  @return builder (@link AnimatedColorBuilder NXOpen.AnimationDesigner.AnimatedColorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="animatedColor"> (@link AnimatedColor NXOpen.AnimationDesigner.AnimatedColor@endlink)  @link NXOpen::AnimationDesigner::AnimatedColor NXOpen::AnimationDesigner::AnimatedColor@endlink  to be edited, if NULL then create a new one </param>
    def CreateAnimatedColorBuilder(part: NXOpen.Part, animatedColor: AnimatedColor) -> AnimatedColorBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::AnimatedColorBuilder NXOpen::AnimationDesigner::AnimatedColorBuilder@endlink . 
         @return builder (@link AnimatedColorBuilder NXOpen.AnimationDesigner.AnimatedColorBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::AnimatedColor   NXOpen::AnimationDesigner::AnimatedColor @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return animatedcolor (@link AnimatedColor NXOpen.AnimationDesigner.AnimatedColor@endlink):  @link  NXOpen::AnimationDesigner::AnimatedColor   NXOpen::AnimationDesigner::AnimatedColor @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::AnimatedColor   NXOpen::AnimationDesigner::AnimatedColor @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedColor:
        """
         Finds the @link  NXOpen::AnimationDesigner::AnimatedColor   NXOpen::AnimationDesigner::AnimatedColor @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return animatedcolor (@link AnimatedColor NXOpen.AnimationDesigner.AnimatedColor@endlink):  @link  NXOpen::AnimationDesigner::AnimatedColor   NXOpen::AnimationDesigner::AnimatedColor @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents an Animated Color feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::AnimatedColorBuilder  NXOpen::AnimationDesigner::AnimatedColorBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class AnimatedColor(NXOpen.DisplayableObject): 
    """ Represents an Animated Color feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::AnimatedExplodeBuilder NXOpen::AnimationDesigner::AnimatedExplodeBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::AnimatedExplodeCollection::CreateAnimatedExplodeBuilder  NXOpen::AnimationDesigner::AnimatedExplodeCollection::CreateAnimatedExplodeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedExplodeBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.AnimatedExplodeBuilder</ja_class>. """


    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the animated explode </description> </item><item><term> 
    ## AutomaticColor</term><description> 
    ##  Auto-assigns a color to each animated explode </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the animated explode </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <AutomaticColor> <NoColor>
        """
        SpecifyColor: int
        AutomaticColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedExplodeBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the creation types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Combine</term><description> 
    ##  Combine all motion objects into one animated explode </description> </item><item><term> 
    ## Separate</term><description> 
    ##  Create an animated explode for each motion object </description> </item></list>
    class CreationTypes(Enum):
        """
        Members Include: <Combine> <Separate>
        """
        Combine: int
        Separate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedExplodeBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedExplodeBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedExplodeBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return AnimatedExplodeBuilder.ColorOptions
    @property
    def ColorOption(self) -> AnimatedExplodeBuilder.ColorOptions:
        """
        Getter for property: (@link AnimatedExplodeBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedExplodeBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Setter for property: (@link AnimatedExplodeBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedExplodeBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: AnimatedExplodeBuilder.ColorOptions):
        """
        Setter for property: (@link AnimatedExplodeBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedExplodeBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorPickerFlowLineColor
    ##  Returns the flow line color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def ColorPickerFlowLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorPickerFlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorPickerFlowLineColor

    ##  Returns the flow line color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ColorPickerFlowLineColor.setter
    def ColorPickerFlowLineColor(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) ColorPickerFlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedExplodeBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedExplodeBuilder.CreationTypes@endlink) CreationType
    ##  Returns the creation type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return AnimatedExplodeBuilder.CreationTypes
    @property
    def CreationType(self) -> AnimatedExplodeBuilder.CreationTypes:
        """
        Getter for property: (@link AnimatedExplodeBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedExplodeBuilder.CreationTypes@endlink) CreationType
         Returns the creation type.  
             
         
        """
        pass
    
    ## Setter for property: (@link AnimatedExplodeBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedExplodeBuilder.CreationTypes@endlink) CreationType

    ##  Returns the creation type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CreationType.setter
    def CreationType(self, creationType: AnimatedExplodeBuilder.CreationTypes):
        """
        Setter for property: (@link AnimatedExplodeBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedExplodeBuilder.CreationTypes@endlink) CreationType
         Returns the creation type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) DefineFlowLineStyle
    ##  Returns the define flow line style.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def DefineFlowLineStyle(self) -> bool:
        """
        Getter for property: (bool) DefineFlowLineStyle
         Returns the define flow line style.  
             
         
        """
        pass
    
    ## Setter for property: (bool) DefineFlowLineStyle

    ##  Returns the define flow line style.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DefineFlowLineStyle.setter
    def DefineFlowLineStyle(self, defineflowlinestyle: bool):
        """
        Setter for property: (bool) DefineFlowLineStyle
         Returns the define flow line style.  
             
         
        """
        pass
    
    ## Getter for property: (bool) DrawFlowLinePerObject
    ##  Returns the option for enable draw flow line per object.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def DrawFlowLinePerObject(self) -> bool:
        """
        Getter for property: (bool) DrawFlowLinePerObject
         Returns the option for enable draw flow line per object.  
             
         
        """
        pass
    
    ## Setter for property: (bool) DrawFlowLinePerObject

    ##  Returns the option for enable draw flow line per object.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @DrawFlowLinePerObject.setter
    def DrawFlowLinePerObject(self, drawflowlineperobject: bool):
        """
        Setter for property: (bool) DrawFlowLinePerObject
         Returns the option for enable draw flow line per object.  
             
         
        """
        pass
    
    ## Getter for property: (int) LineFontFlowLineFont
    ##  Returns the flow line font.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def LineFontFlowLineFont(self) -> int:
        """
        Getter for property: (int) LineFontFlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    
    ## Setter for property: (int) LineFontFlowLineFont

    ##  Returns the flow line font.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @LineFontFlowLineFont.setter
    def LineFontFlowLineFont(self, font: int):
        """
        Setter for property: (int) LineFontFlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    
    ## Getter for property: (int) LineWidthFlowLineWidth
    ##  Returns the flow line width.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def LineWidthFlowLineWidth(self) -> int:
        """
        Getter for property: (int) LineWidthFlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    
    ## Setter for property: (int) LineWidthFlowLineWidth

    ##  Returns the flow line width.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @LineWidthFlowLineWidth.setter
    def LineWidthFlowLineWidth(self, width: int):
        """
        Setter for property: (int) LineWidthFlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MotionObject
    ##  Returns the object to animated explode.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def MotionObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MotionObject
         Returns the object to animated explode.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowFlowLineInSimulation
    ##  Returns the use specified flow line.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ShowFlowLineInSimulation(self) -> bool:
        """
        Getter for property: (bool) ShowFlowLineInSimulation
         Returns the use specified flow line.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowFlowLineInSimulation

    ##  Returns the use specified flow line.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ShowFlowLineInSimulation.setter
    def ShowFlowLineInSimulation(self, showflowlineinsimulation: bool):
        """
        Setter for property: (bool) ShowFlowLineInSimulation
         Returns the use specified flow line.  
             
         
        """
        pass
    
    ##  Deletes the step. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    def DeleteStep(self, pos: int) -> None:
        """
         Deletes the step. 
        """
        pass
    
    ##  Gets the step count. 
    ##  @return count (int): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetStepCount(self) -> int:
        """
         Gets the step count. 
         @return count (int): .
        """
        pass
    
    ##  Inserts a step. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="startTime"> (float) </param>
    ## <param name="duration"> (float) </param>
    ## <param name="distance"> (float) </param>
    ## <param name="spin"> (float) </param>
    ## <param name="angle"> (float) </param>
    ## <param name="dir"> (@link NXOpen.Direction NXOpen.Direction@endlink) </param>
    def InsertStep(self, pos: int, startTime: float, duration: float, distance: float, spin: float, angle: float, dir: NXOpen.Direction) -> None:
        """
         Inserts a step. 
        """
        pass
    
    ##  Mirrors the steps. 
    ##  @return newSteps (List[int]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="steps"> (List[int]) </param>
    ## <param name="mirror_time"> (float) </param>
    def MirrorSteps(self, steps: List[int], mirror_time: float) -> List[int]:
        """
         Mirrors the steps. 
         @return newSteps (List[int]): .
        """
        pass
    
    ##  Sets the step angle. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="angle"> (float) </param>
    def SetStepAngle(self, pos: int, angle: float) -> None:
        """
         Sets the step angle. 
        """
        pass
    
    ##  Sets the step direction. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="dir"> (@link NXOpen.Direction NXOpen.Direction@endlink) </param>
    def SetStepDirection(self, pos: int, dir: NXOpen.Direction) -> None:
        """
         Sets the step direction. 
        """
        pass
    
    ##  Sets the step distance. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="distance"> (float) </param>
    def SetStepDistance(self, pos: int, distance: float) -> None:
        """
         Sets the step distance. 
        """
        pass
    
    ##  Sets the step duration. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="duration"> (float) </param>
    def SetStepDuration(self, pos: int, duration: float) -> None:
        """
         Sets the step duration. 
        """
        pass
    
    ##  Sets the step name. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="name"> (str) </param>
    def SetStepName(self, pos: int, name: str) -> None:
        """
         Sets the step name. 
        """
        pass
    
    ##  Sets the step spin. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="spin"> (float) </param>
    def SetStepSpin(self, pos: int, spin: float) -> None:
        """
         Sets the step spin. 
        """
        pass
    
    ##  Sets the step start time. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="start_time"> (float) </param>
    def SetStepStartTime(self, pos: int, start_time: float) -> None:
        """
         Sets the step start time. 
        """
        pass
    
    ##  Sets the step rotation. 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="rotation"> (@link NXOpen.Matrix4x4 NXOpen.Matrix4x4@endlink) </param>
    def SetStepTargetPosition(self, pos: int, rotation: NXOpen.Matrix4x4) -> None:
        """
         Sets the step rotation. 
        """
        pass
    
    ##  Sets the step flag use origin. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="useOrigin"> (bool) </param>
    def SetStepUseOrigin(self, pos: int, useOrigin: bool) -> None:
        """
         Sets the step flag use origin. 
        """
        pass
    
    ##  Splits the step with the split time. 
    ##  @return splited (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pos"> (int) </param>
    ## <param name="split_time"> (float) </param>
    def SplitStep(self, pos: int, split_time: float) -> bool:
        """
         Splits the step with the split time. 
         @return splited (bool): .
        """
        pass
    
import NXOpen
##  Represents a collection of Animated Explode objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedExplodeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Explode objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::AnimatedExplodeBuilder NXOpen::AnimationDesigner::AnimatedExplodeBuilder@endlink . 
    ##  @return builder (@link AnimatedExplodeBuilder NXOpen.AnimationDesigner.AnimatedExplodeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="animatedexplode"> (@link AnimatedExplode NXOpen.AnimationDesigner.AnimatedExplode@endlink)  @link NXOpen::AnimationDesigner::AnimatedExplode NXOpen::AnimationDesigner::AnimatedExplode@endlink  to be edited, if NULL then create a new one </param>
    def CreateAnimatedExplodeBuilder(part: NXOpen.Part, animatedexplode: AnimatedExplode) -> AnimatedExplodeBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::AnimatedExplodeBuilder NXOpen::AnimationDesigner::AnimatedExplodeBuilder@endlink . 
         @return builder (@link AnimatedExplodeBuilder NXOpen.AnimationDesigner.AnimatedExplodeBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::AnimatedExplode   NXOpen::AnimationDesigner::AnimatedExplode @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return explode (@link AnimatedExplode NXOpen.AnimationDesigner.AnimatedExplode@endlink):  @link  NXOpen::AnimationDesigner::AnimatedExplode   NXOpen::AnimationDesigner::AnimatedExplode @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::AnimatedExplode   NXOpen::AnimationDesigner::AnimatedExplode @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedExplode:
        """
         Finds the @link  NXOpen::AnimationDesigner::AnimatedExplode   NXOpen::AnimationDesigner::AnimatedExplode @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return explode (@link AnimatedExplode NXOpen.AnimationDesigner.AnimatedExplode@endlink):  @link  NXOpen::AnimationDesigner::AnimatedExplode   NXOpen::AnimationDesigner::AnimatedExplode @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents an animated explode feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::AnimatedExplodeBuilder  NXOpen::AnimationDesigner::AnimatedExplodeBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedExplode(NXOpen.DisplayableObject): 
    """ Represents an animated explode feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::AnimatedVisibilityBuilder NXOpen::AnimationDesigner::AnimatedVisibilityBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::AnimatedVisibilityCollection::CreateAnimatedVisibilityBuilder  NXOpen::AnimationDesigner::AnimatedVisibilityCollection::CreateAnimatedVisibilityBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedVisibilityBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.AnimatedVisibilityBuilder</ja_class>. """


    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the visibility </description> </item><item><term> 
    ## AutomaticColor</term><description> 
    ##  Auto-assigns a color to each visibility </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the visibility </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <AutomaticColor> <NoColor>
        """
        SpecifyColor: int
        AutomaticColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedVisibilityBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the creation types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Combine</term><description> 
    ##  Combine selections into one animated visibility </description> </item><item><term> 
    ## Separate</term><description> 
    ##  Create an animated visibility for each selection </description> </item></list>
    class CreationTypes(Enum):
        """
        Members Include: <Combine> <Separate>
        """
        Combine: int
        Separate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimatedVisibilityBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedVisibilityBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return AnimatedVisibilityBuilder.ColorOptions
    @property
    def ColorOption(self) -> AnimatedVisibilityBuilder.ColorOptions:
        """
        Getter for property: (@link AnimatedVisibilityBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Setter for property: (@link AnimatedVisibilityBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: AnimatedVisibilityBuilder.ColorOptions):
        """
        Setter for property: (@link AnimatedVisibilityBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Getter for property: (@link AnimatedVisibilityBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.CreationTypes@endlink) CreationType
    ##  Returns the creation type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return AnimatedVisibilityBuilder.CreationTypes
    @property
    def CreationType(self) -> AnimatedVisibilityBuilder.CreationTypes:
        """
        Getter for property: (@link AnimatedVisibilityBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.CreationTypes@endlink) CreationType
         Returns the creation type.  
             
         
        """
        pass
    
    ## Setter for property: (@link AnimatedVisibilityBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.CreationTypes@endlink) CreationType

    ##  Returns the creation type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CreationType.setter
    def CreationType(self, creationType: AnimatedVisibilityBuilder.CreationTypes):
        """
        Setter for property: (@link AnimatedVisibilityBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.CreationTypes@endlink) CreationType
         Returns the creation type.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) RigidGroup
    ##  Returns the rigid group to display translucency.  
    ##    This can be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink .   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def RigidGroup(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) RigidGroup
         Returns the rigid group to display translucency.  
           This can be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink .   
         
        """
        pass
    
    ## Getter for property: (int) Translucency
    ##  Returns the translucency.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def Translucency(self) -> int:
        """
        Getter for property: (int) Translucency
         Returns the translucency.  
             
         
        """
        pass
    
    ## Setter for property: (int) Translucency

    ##  Returns the translucency.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Translucency.setter
    def Translucency(self, translucency: int):
        """
        Setter for property: (int) Translucency
         Returns the translucency.  
             
         
        """
        pass
    
    ##  Creates a new bar. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    
    ##  Deletes the bars. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    
    ##  Mirrors the bars. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    ## <param name="mirror_time"> (float) </param>
    def MirrorBars(self, bars: List[int], mirror_time: float) -> None:
        """
         Mirrors the bars. 
        """
        pass
    
    ##  Sets the bar end time. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="end_time"> (float) </param>
    def SetBarEndTime(self, index: int, end_time: float) -> None:
        """
         Sets the bar end time. 
        """
        pass
    
    ##  Sets the bar end translucency. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="translucency"> (int) </param>
    def SetBarEndTranslucency(self, index: int, translucency: int) -> None:
        """
         Sets the bar end translucency. 
        """
        pass
    
    ##  Sets the bar name. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="name"> (str) </param>
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    
    ##  Sets the bar start time. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="start_time"> (float) </param>
    def SetBarStartTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
    
    ##  Sets the bar start translucency. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="translucency"> (int) </param>
    def SetBarStartTranslucency(self, index: int, translucency: int) -> None:
        """
         Sets the bar start translucency. 
        """
        pass
    
    ##  Splits the bar with the split time. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="split_time"> (float) </param>
    def SplitBar(self, index: int, split_time: float) -> None:
        """
         Splits the bar with the split time. 
        """
        pass
    
import NXOpen
##  Represents a collection of Animated Visibility objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedVisibilityCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Visibility objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::AnimatedVisibilityBuilder NXOpen::AnimationDesigner::AnimatedVisibilityBuilder@endlink . 
    ##  @return builder (@link AnimatedVisibilityBuilder NXOpen.AnimationDesigner.AnimatedVisibilityBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="animatedVisibility"> (@link AnimatedVisibility NXOpen.AnimationDesigner.AnimatedVisibility@endlink)  @link NXOpen::AnimationDesigner::AnimatedVisibility NXOpen::AnimationDesigner::AnimatedVisibility@endlink  to be edited, if NULL then create a new one </param>
    def CreateAnimatedVisibilityBuilder(part: NXOpen.Part, animatedVisibility: AnimatedVisibility) -> AnimatedVisibilityBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::AnimatedVisibilityBuilder NXOpen::AnimationDesigner::AnimatedVisibilityBuilder@endlink . 
         @return builder (@link AnimatedVisibilityBuilder NXOpen.AnimationDesigner.AnimatedVisibilityBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::AnimatedVisibility   NXOpen::AnimationDesigner::AnimatedVisibility @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return animatedVisibility (@link AnimatedVisibility NXOpen.AnimationDesigner.AnimatedVisibility@endlink):  @link  NXOpen::AnimationDesigner::AnimatedVisibility   NXOpen::AnimationDesigner::AnimatedVisibility @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::AnimatedVisibility   NXOpen::AnimationDesigner::AnimatedVisibility @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedVisibility:
        """
         Finds the @link  NXOpen::AnimationDesigner::AnimatedVisibility   NXOpen::AnimationDesigner::AnimatedVisibility @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return animatedVisibility (@link AnimatedVisibility NXOpen.AnimationDesigner.AnimatedVisibility@endlink):  @link  NXOpen::AnimationDesigner::AnimatedVisibility   NXOpen::AnimationDesigner::AnimatedVisibility @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents an Animated Visibility feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::AnimatedVisibilityBuilder  NXOpen::AnimationDesigner::AnimatedVisibilityBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class AnimatedVisibility(NXOpen.DisplayableObject): 
    """ Represents an Animated Visibility feature. """
    pass


import NXOpen
import NXOpen.AnimationDesigner.Nav
import NXOpen.Facet
##  Represents an object to manage Animation Designer application objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class AnimationDesignerManager(NXOpen.Object): 
    """ Represents an object to manage Animation Designer application objects. """


    ##   @brief  Represents display color option.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ShowRigid</term><description> 
    ##  show rigid group color </description> </item><item><term> 
    ## ClearRigid</term><description> 
    ##  clear rigid group color </description> </item><item><term> 
    ## ShowExplode</term><description> 
    ##  show explode color </description> </item><item><term> 
    ## ClearExplode</term><description> 
    ##  clear explode color </description> </item><item><term> 
    ## ShowVisibility</term><description> 
    ##  show visibility color </description> </item><item><term> 
    ## ClearVisibility</term><description> 
    ##  clear visibility color </description> </item><item><term> 
    ## ShowMotor</term><description> 
    ##  show motor color </description> </item><item><term> 
    ## ClearMotor</term><description> 
    ##  clear motor color </description> </item><item><term> 
    ## ShowFlexibleObject</term><description> 
    ##  show flexible object color </description> </item><item><term> 
    ## ClearFlexibleObject</term><description> 
    ##  clear flexible object color </description> </item><item><term> 
    ## ShowJoint</term><description> 
    ##  show joint color </description> </item><item><term> 
    ## ClearJoint</term><description> 
    ##  clear joint color </description> </item><item><term> 
    ## ShowCoupler</term><description> 
    ##  show coupler color </description> </item><item><term> 
    ## ClearCoupler</term><description> 
    ##  clear coupler color </description> </item></list>
    class JaAnimationDesignerDisplayColorOption(Enum):
        """
        Members Include: <ShowRigid> <ClearRigid> <ShowExplode> <ClearExplode> <ShowVisibility> <ClearVisibility> <ShowMotor> <ClearMotor> <ShowFlexibleObject> <ClearFlexibleObject> <ShowJoint> <ClearJoint> <ShowCoupler> <ClearCoupler>
        """
        ShowRigid: int
        ClearRigid: int
        ShowExplode: int
        ClearExplode: int
        ShowVisibility: int
        ClearVisibility: int
        ShowMotor: int
        ClearMotor: int
        ShowFlexibleObject: int
        ClearFlexibleObject: int
        ShowJoint: int
        ClearJoint: int
        ShowCoupler: int
        ClearCoupler: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerDisplayColorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief  Represents envelope accuracy mode.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Low</term><description> 
    ##  accuracy low </description> </item><item><term> 
    ## Medium</term><description> 
    ##  accuracy medium </description> </item><item><term> 
    ## High</term><description> 
    ##  accuracy high </description> </item><item><term> 
    ## Custom</term><description> 
    ##  accuracy custom </description> </item></list>
    class JaAnimationDesignerEnvelopeAccuracyMode(Enum):
        """
        Members Include: <Low> <Medium> <High> <Custom>
        """
        Low: int
        Medium: int
        High: int
        Custom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief  Represents create envelope mode.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Work</term><description> 
    ##  work mode  </description> </item><item><term> 
    ## Test</term><description> 
    ##  auto/unit test mode </description> </item></list>
    class JaAnimationDesignerEnvelopeMode(Enum):
        """
        Members Include: <Work> <Test>
        """
        Work: int
        Test: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerEnvelopeMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief  Represents create interference type.  
    ## 
    ##   
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Highlight</term><description> 
    ##  Highlight  </description> </item><item><term> 
    ## ShowCurve</term><description> 
    ##  Show Intersection Curve </description> </item></list>
    class JaAnimationDesignerInterferenceType(Enum):
        """
        Members Include: <Highlight> <ShowCurve>
        """
        Highlight: int
        ShowCurve: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerInterferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns the @link NXOpen::AnimationDesigner::Nav::SolutionCollection NXOpen::AnimationDesigner::Nav::SolutionCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link NXOpen.AnimationDesigner.Nav.SolutionCollection NXOpen.AnimationDesigner.Nav.SolutionCollection@endlink
    @property
    def Solutions() -> NXOpen.AnimationDesigner.Nav.SolutionCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::Nav::SolutionCollection NXOpen::AnimationDesigner::Nav::SolutionCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::RigidGroupCollection NXOpen::AnimationDesigner::RigidGroupCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link RigidGroupCollection NXOpen.AnimationDesigner.RigidGroupCollection@endlink
    @property
    def RigidGroups() -> RigidGroupCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::RigidGroupCollection NXOpen::AnimationDesigner::RigidGroupCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::ContactCollection NXOpen::AnimationDesigner::ContactCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link ContactCollection NXOpen.AnimationDesigner.ContactCollection@endlink
    @property
    def Contacts() -> ContactCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::ContactCollection NXOpen::AnimationDesigner::ContactCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::RevoluteJointCollection NXOpen::AnimationDesigner::RevoluteJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link RevoluteJointCollection NXOpen.AnimationDesigner.RevoluteJointCollection@endlink
    @property
    def RevoluteJoints() -> RevoluteJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::RevoluteJointCollection NXOpen::AnimationDesigner::RevoluteJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::SliderJointCollection NXOpen::AnimationDesigner::SliderJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link SliderJointCollection NXOpen.AnimationDesigner.SliderJointCollection@endlink
    @property
    def SliderJoints() -> SliderJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::SliderJointCollection NXOpen::AnimationDesigner::SliderJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::CylindricalJointCollection NXOpen::AnimationDesigner::CylindricalJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link CylindricalJointCollection NXOpen.AnimationDesigner.CylindricalJointCollection@endlink
    @property
    def CylindricalJoints() -> CylindricalJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::CylindricalJointCollection NXOpen::AnimationDesigner::CylindricalJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::SphericalJointCollection NXOpen::AnimationDesigner::SphericalJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link SphericalJointCollection NXOpen.AnimationDesigner.SphericalJointCollection@endlink
    @property
    def SphericalJoints() -> SphericalJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::SphericalJointCollection NXOpen::AnimationDesigner::SphericalJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::FixedJointCollection NXOpen::AnimationDesigner::FixedJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link FixedJointCollection NXOpen.AnimationDesigner.FixedJointCollection@endlink
    @property
    def FixedJoints() -> FixedJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::FixedJointCollection NXOpen::AnimationDesigner::FixedJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::GearCollection NXOpen::AnimationDesigner::GearCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link GearCollection NXOpen.AnimationDesigner.GearCollection@endlink
    @property
    def Gears() -> GearCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::GearCollection NXOpen::AnimationDesigner::GearCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::RackPinionCollection NXOpen::AnimationDesigner::RackPinionCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link RackPinionCollection NXOpen.AnimationDesigner.RackPinionCollection@endlink
    @property
    def RackPinions() -> RackPinionCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::RackPinionCollection NXOpen::AnimationDesigner::RackPinionCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::PositionMotorCollection NXOpen::AnimationDesigner::PositionMotorCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link PositionMotorCollection NXOpen.AnimationDesigner.PositionMotorCollection@endlink
    @property
    def PositionMotors() -> PositionMotorCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::PositionMotorCollection NXOpen::AnimationDesigner::PositionMotorCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::SpeedMotorCollection NXOpen::AnimationDesigner::SpeedMotorCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link SpeedMotorCollection NXOpen.AnimationDesigner.SpeedMotorCollection@endlink
    @property
    def SpeedMotors() -> SpeedMotorCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::SpeedMotorCollection NXOpen::AnimationDesigner::SpeedMotorCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::MeasureCollection NXOpen::AnimationDesigner::MeasureCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link MeasureCollection NXOpen.AnimationDesigner.MeasureCollection@endlink
    @property
    def Measures() -> MeasureCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::MeasureCollection NXOpen::AnimationDesigner::MeasureCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::PointOnCurveJointCollection NXOpen::AnimationDesigner::PointOnCurveJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link PointOnCurveJointCollection NXOpen.AnimationDesigner.PointOnCurveJointCollection@endlink
    @property
    def PointOnCurveJoints() -> PointOnCurveJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::PointOnCurveJointCollection NXOpen::AnimationDesigner::PointOnCurveJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::CurveOnCurveJointCollection NXOpen::AnimationDesigner::CurveOnCurveJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link CurveOnCurveJointCollection NXOpen.AnimationDesigner.CurveOnCurveJointCollection@endlink
    @property
    def CurveOnCurveJoints() -> CurveOnCurveJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::CurveOnCurveJointCollection NXOpen::AnimationDesigner::CurveOnCurveJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::MechanicalCamCollection NXOpen::AnimationDesigner::MechanicalCamCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @link MechanicalCamCollection NXOpen.AnimationDesigner.MechanicalCamCollection@endlink
    @property
    def MechanicalCams() -> MechanicalCamCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::MechanicalCamCollection NXOpen::AnimationDesigner::MechanicalCamCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::ScrewJointCollection NXOpen::AnimationDesigner::ScrewJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @link ScrewJointCollection NXOpen.AnimationDesigner.ScrewJointCollection@endlink
    @property
    def ScrewJoints() -> ScrewJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::ScrewJointCollection NXOpen::AnimationDesigner::ScrewJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::PlanarJointCollection NXOpen::AnimationDesigner::PlanarJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @link PlanarJointCollection NXOpen.AnimationDesigner.PlanarJointCollection@endlink
    @property
    def PlanarJoints() -> PlanarJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::PlanarJointCollection NXOpen::AnimationDesigner::PlanarJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::AnimatedVisibilityCollection NXOpen::AnimationDesigner::AnimatedVisibilityCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link AnimatedVisibilityCollection NXOpen.AnimationDesigner.AnimatedVisibilityCollection@endlink
    @property
    def AnimatedVisibilities() -> AnimatedVisibilityCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::AnimatedVisibilityCollection NXOpen::AnimationDesigner::AnimatedVisibilityCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::AnimatedCameraCollection NXOpen::AnimationDesigner::AnimatedCameraCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link AnimatedCameraCollection NXOpen.AnimationDesigner.AnimatedCameraCollection@endlink
    @property
    def AnimatedCameras() -> AnimatedCameraCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::AnimatedCameraCollection NXOpen::AnimationDesigner::AnimatedCameraCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::AnimatedExplodeCollection NXOpen::AnimationDesigner::AnimatedExplodeCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @link AnimatedExplodeCollection NXOpen.AnimationDesigner.AnimatedExplodeCollection@endlink
    @property
    def AnimatedExplodes() -> AnimatedExplodeCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::AnimatedExplodeCollection NXOpen::AnimationDesigner::AnimatedExplodeCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::AnimatedColorCollection NXOpen::AnimationDesigner::AnimatedColorCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @link AnimatedColorCollection NXOpen.AnimationDesigner.AnimatedColorCollection@endlink
    @property
    def AnimatedColors() -> AnimatedColorCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::AnimatedColorCollection NXOpen::AnimationDesigner::AnimatedColorCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::JointJoggerCollection NXOpen::AnimationDesigner::JointJoggerCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @link JointJoggerCollection NXOpen.AnimationDesigner.JointJoggerCollection@endlink
    @property
    def JointJoggers() -> JointJoggerCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::JointJoggerCollection NXOpen::AnimationDesigner::JointJoggerCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::InverseKinematicsCollection NXOpen::AnimationDesigner::InverseKinematicsCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @link InverseKinematicsCollection NXOpen.AnimationDesigner.InverseKinematicsCollection@endlink
    @property
    def InverseKinematics() -> InverseKinematicsCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::InverseKinematicsCollection NXOpen::AnimationDesigner::InverseKinematicsCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::PathConstraintJointCollection NXOpen::AnimationDesigner::PathConstraintJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @link PathConstraintJointCollection NXOpen.AnimationDesigner.PathConstraintJointCollection@endlink
    @property
    def PathConstraintJoints() -> PathConstraintJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::PathConstraintJointCollection NXOpen::AnimationDesigner::PathConstraintJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::TracerCollection NXOpen::AnimationDesigner::TracerCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link TracerCollection NXOpen.AnimationDesigner.TracerCollection@endlink
    @property
    def Tracers() -> TracerCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::TracerCollection NXOpen::AnimationDesigner::TracerCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::BondJointCollection NXOpen::AnimationDesigner::BondJointCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @link BondJointCollection NXOpen.AnimationDesigner.BondJointCollection@endlink
    @property
    def BondJoints() -> BondJointCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::BondJointCollection NXOpen::AnimationDesigner::BondJointCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::Nav::ContainerCollection NXOpen::AnimationDesigner::Nav::ContainerCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @link NXOpen.AnimationDesigner.Nav.ContainerCollection NXOpen.AnimationDesigner.Nav.ContainerCollection@endlink
    @property
    def Containers() -> NXOpen.AnimationDesigner.Nav.ContainerCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::Nav::ContainerCollection NXOpen::AnimationDesigner::Nav::ContainerCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  Returns the @link NXOpen::AnimationDesigner::Nav::SubFolderCollection NXOpen::AnimationDesigner::Nav::SubFolderCollection@endlink  belonging to this application. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @link NXOpen.AnimationDesigner.Nav.SubFolderCollection NXOpen.AnimationDesigner.Nav.SubFolderCollection@endlink
    @property
    def SubFolders() -> NXOpen.AnimationDesigner.Nav.SubFolderCollection:
        """
         Returns the @link NXOpen::AnimationDesigner::Nav::SubFolderCollection NXOpen::AnimationDesigner::Nav::SubFolderCollection@endlink  belonging to this application. 
        """
        pass
    
    ##  @brief  Returns the @link NXOpen::AnimationDesigner::BulletCableCollection  NXOpen::AnimationDesigner::BulletCableCollection @endlink  belonging to this part  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @link BulletCableCollection NXOpen.AnimationDesigner.BulletCableCollection@endlink
    @property
    def BulletCables() -> BulletCableCollection:
        """
         @brief  Returns the @link NXOpen::AnimationDesigner::BulletCableCollection  NXOpen::AnimationDesigner::BulletCableCollection @endlink  belonging to this part  
        
         
        """
        pass
    
    ##  @brief  Returns the @link NXOpen::AnimationDesigner::BulletFlexibleMaterialCollection  NXOpen::AnimationDesigner::BulletFlexibleMaterialCollection @endlink  belonging to this part  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @link BulletFlexibleMaterialCollection NXOpen.AnimationDesigner.BulletFlexibleMaterialCollection@endlink
    @property
    def BulletFlexibleMaterials() -> BulletFlexibleMaterialCollection:
        """
         @brief  Returns the @link NXOpen::AnimationDesigner::BulletFlexibleMaterialCollection  NXOpen::AnimationDesigner::BulletFlexibleMaterialCollection @endlink  belonging to this part  
        
         
        """
        pass
    
    ##  @brief  Returns the @link NXOpen::AnimationDesigner::FlexibleCableCollection  NXOpen::AnimationDesigner::FlexibleCableCollection @endlink  belonging to this part  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @link FlexibleCableCollection NXOpen.AnimationDesigner.FlexibleCableCollection@endlink
    @property
    def FlexibleCables() -> FlexibleCableCollection:
        """
         @brief  Returns the @link NXOpen::AnimationDesigner::FlexibleCableCollection  NXOpen::AnimationDesigner::FlexibleCableCollection @endlink  belonging to this part  
        
         
        """
        pass
    
    ##  @brief  Returns the @link NXOpen::AnimationDesigner::FlexibleMaterialCollection  NXOpen::AnimationDesigner::FlexibleMaterialCollection @endlink  belonging to this part  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @link FlexibleMaterialCollection NXOpen.AnimationDesigner.FlexibleMaterialCollection@endlink
    @property
    def FlexibleMaterials() -> FlexibleMaterialCollection:
        """
         @brief  Returns the @link NXOpen::AnimationDesigner::FlexibleMaterialCollection  NXOpen::AnimationDesigner::FlexibleMaterialCollection @endlink  belonging to this part  
        
         
        """
        pass
    
    ##  @brief  Returns the @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChainCollection NXOpen::AnimationDesigner::PointOnCurveKinematicsChainCollection@endlink  belonging to this application.  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @link PointOnCurveKinematicsChainCollection NXOpen.AnimationDesigner.PointOnCurveKinematicsChainCollection@endlink
    @property
    def PointOnCurveKinematicsChains() -> PointOnCurveKinematicsChainCollection:
        """
         @brief  Returns the @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChainCollection NXOpen::AnimationDesigner::PointOnCurveKinematicsChainCollection@endlink  belonging to this application.  
        
         
        """
        pass
    
    ##  @brief  Returns the @link NXOpen::AnimationDesigner::ActivityOperatorCollection NXOpen::AnimationDesigner::ActivityOperatorCollection@endlink  belonging to this application.  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @link ActivityOperatorCollection NXOpen.AnimationDesigner.ActivityOperatorCollection@endlink
    @property
    def ActivityOperators() -> ActivityOperatorCollection:
        """
         @brief  Returns the @link NXOpen::AnimationDesigner::ActivityOperatorCollection NXOpen::AnimationDesigner::ActivityOperatorCollection@endlink  belonging to this application.  
        
         
        """
        pass
    
    ## Show or clear physics color.  
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="displayOption"> (@link AnimationDesignerManager.JaAnimationDesignerDisplayColorOption NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerDisplayColorOption@endlink) </param>
    def ApplyPhysicsColor(displayOption: AnimationDesignerManager.JaAnimationDesignerDisplayColorOption) -> None:
        """
        Show or clear physics color.  
        """
        pass
    
    ##  Records the auto solve data for Animation Designer. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def AutoSolve(part: NXOpen.Part) -> None:
        """
         Records the auto solve data for Animation Designer. 
        """
        pass
    
    ##  Clears the auto solve data for Animation Designer. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def AutoSolveClear(part: NXOpen.Part) -> None:
        """
         Clears the auto solve data for Animation Designer. 
        """
        pass
    
    ##  Records the auto solve data for Animation Designer. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="physics_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="matrix"> (List[float]) </param>
    def AutoSolveRecord(part: NXOpen.Part, physics_object: NXOpen.NXObject, matrix: List[float]) -> None:
        """
         Records the auto solve data for Animation Designer. 
        """
        pass
    
    ##  Changes motion type. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="motionType"> (@link PhysicsJointBuilder.MotionTypes NXOpen.AnimationDesigner.PhysicsJointBuilder.MotionTypes@endlink) </param>
    def ChangeMotionType(part: NXOpen.Part, objects: List[NXOpen.NXObject], motionType: PhysicsJointBuilder.MotionTypes) -> None:
        """
         Changes motion type. 
        """
        pass
    
    ##  Creates a @link AnimationDesigner::ConstraintConversionBuilder AnimationDesigner::ConstraintConversionBuilder@endlink  
    ##  @return builder (@link ConstraintConversionBuilder NXOpen.AnimationDesigner.ConstraintConversionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateConstraintConversionBuilder(part: NXOpen.Part) -> ConstraintConversionBuilder:
        """
         Creates a @link AnimationDesigner::ConstraintConversionBuilder AnimationDesigner::ConstraintConversionBuilder@endlink  
         @return builder (@link ConstraintConversionBuilder NXOpen.AnimationDesigner.ConstraintConversionBuilder@endlink): .
        """
        pass
    
    ##  Creates a container in navigator. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="containerName"> (str)  the container name </param>
    def CreateContainer(part: NXOpen.Part, containerName: str) -> None:
        """
         Creates a container in navigator. 
        """
        pass
    
    ##  Creates an Envelope object. 
    ##  @return envelope (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Use JA_MOTION_DESIGNER_MANAGER_CreateEnvelopes instead.  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="physics_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="geometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="tolerance"> (float) </param>
    ## <param name="mode"> (@link AnimationDesignerManager.JaAnimationDesignerEnvelopeMode NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerEnvelopeMode@endlink) </param>
    ## <param name="translucency"> (int) </param>
    def CreateEnvelope(physics_object: NXOpen.NXObject, geometry: NXOpen.NXObject, tolerance: float, mode: AnimationDesignerManager.JaAnimationDesignerEnvelopeMode, translucency: int) -> NXOpen.Facet.FacetedBody:
        """
         Creates an Envelope object. 
         @return envelope (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink): .
        """
        pass
    
    ##  Creates Envelope objects. 
    ##  @return envelopeList (@link NXOpen.Facet.FacetedBody List[NXOpen.Facet.FacetedBody]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2206.0.0.  Use JA_MOTION_DESIGNER_MANAGER_CreateSingleEnvelope instead.  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="physicsObject"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="geometry"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="physicsToGeometry"> (List[int]) </param>
    ## <param name="tolerance"> (float) </param>
    ## <param name="mode"> (@link AnimationDesignerManager.JaAnimationDesignerEnvelopeMode NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerEnvelopeMode@endlink) </param>
    ## <param name="translucency"> (int) </param>
    def CreateEnvelopes(physicsObject: List[NXOpen.NXObject], geometry: List[NXOpen.NXObject], physicsToGeometry: List[int], tolerance: float, mode: AnimationDesignerManager.JaAnimationDesignerEnvelopeMode, translucency: int) -> List[NXOpen.Facet.FacetedBody]:
        """
         Creates Envelope objects. 
         @return envelopeList (@link NXOpen.Facet.FacetedBody List[NXOpen.Facet.FacetedBody]@endlink): .
        """
        pass
    
    ##  Creates a NXOpen.AnimationDesigner.ExportTraceBuilder object. 
    ##  @return builder (@link ExportTraceBuilder NXOpen.AnimationDesigner.ExportTraceBuilder@endlink):  ExportTraceBuilder.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="tracer"> (@link Tracer NXOpen.AnimationDesigner.Tracer@endlink)  @link NXOpen::AnimationDesigner::Tracer NXOpen::AnimationDesigner::Tracer@endlink  to be exported </param>
    def CreateExportTraceBuilder(part: NXOpen.Part, tracer: Tracer) -> ExportTraceBuilder:
        """
         Creates a NXOpen.AnimationDesigner.ExportTraceBuilder object. 
         @return builder (@link ExportTraceBuilder NXOpen.AnimationDesigner.ExportTraceBuilder@endlink):  ExportTraceBuilder.
        """
        pass
    
    ##  Create facet body for flexible cable. 
    ##  @return facetBody (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="flexibleCableTag"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="vertexList"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink) </param>
    ## <param name="widthDirectionList"> (@link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink) </param>
    ## <param name="radius"> (float) </param>
    ## <param name="width"> (float) </param>
    ## <param name="thickness"> (float) </param>
    def CreateFlexibleCableFacetBody(flexibleCableTag: NXOpen.NXObject, vertexList: List[NXOpen.Point3d], widthDirectionList: List[NXOpen.Vector3d], radius: float, width: float, thickness: float) -> NXOpen.NXObject:
        """
         Create facet body for flexible cable. 
         @return facetBody (@link NXOpen.NXObject NXOpen.NXObject@endlink): .
        """
        pass
    
    ##  Creates an Interference object. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="firstEnvelope"> (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink) </param>
    ## <param name="secondEnvelope"> (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink) </param>
    ## <param name="outputType"> (@link AnimationDesignerManager.JaAnimationDesignerInterferenceType NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerInterferenceType@endlink) </param>
    def CreateInterference(firstEnvelope: NXOpen.Facet.FacetedBody, secondEnvelope: NXOpen.Facet.FacetedBody, outputType: AnimationDesignerManager.JaAnimationDesignerInterferenceType) -> None:
        """
         Creates an Interference object. 
        """
        pass
    
    ##  Creates a @link AnimationDesigner::InverseKinematicsBuilder AnimationDesigner::InverseKinematicsBuilder@endlink  
    ##  @return builder (@link InverseKinematicsBuilder NXOpen.AnimationDesigner.InverseKinematicsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateInverseKinematicsBuilder(part: NXOpen.Part) -> InverseKinematicsBuilder:
        """
         Creates a @link AnimationDesigner::InverseKinematicsBuilder AnimationDesigner::InverseKinematicsBuilder@endlink  
         @return builder (@link InverseKinematicsBuilder NXOpen.AnimationDesigner.InverseKinematicsBuilder@endlink): .
        """
        pass
    
    ##  Creates the preferences builder for Animation Designer. 
    ##  @return builder (@link PreferencesBuilder NXOpen.AnimationDesigner.PreferencesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreatePreferenceBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates the preferences builder for Animation Designer. 
         @return builder (@link PreferencesBuilder NXOpen.AnimationDesigner.PreferencesBuilder@endlink): .
        """
        pass
    
    ##  Creates an envelope object for a signle geometry. 
    ##  @return createEnvelope (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2212.0.0.  Use JA_MOTION_DESIGNER_MANAGER_CreateSingleEnvelope2 instead.  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="geometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="transformMatrixList"> (@link NXOpen.Matrix4x4 List[NXOpen.Matrix4x4]@endlink) </param>
    ## <param name="destinationPart"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="tolerance"> (float) </param>
    ## <param name="translucency"> (int) </param>
    ## <param name="color"> (int) </param>
    def CreateSingleEnvelope(geometry: NXOpen.NXObject, transformMatrixList: List[NXOpen.Matrix4x4], destinationPart: NXOpen.NXObject, tolerance: float, translucency: int, color: int) -> NXOpen.Facet.FacetedBody:
        """
         Creates an envelope object for a signle geometry. 
         @return createEnvelope (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink): .
        """
        pass
    
    ##  Creates an envelope object for a signle geometry 2. 
    ##  @return createEnvelope (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="geometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="transformMatrixList"> (@link NXOpen.Matrix4x4 List[NXOpen.Matrix4x4]@endlink) </param>
    ## <param name="destinationPart"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="accuracyMode"> (@link AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode@endlink) </param>
    ## <param name="tolerance"> (float) </param>
    ## <param name="translucency"> (int) </param>
    ## <param name="color"> (int) </param>
    def CreateSingleEnvelope2(geometry: NXOpen.NXObject, transformMatrixList: List[NXOpen.Matrix4x4], destinationPart: NXOpen.NXObject, accuracyMode: AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode, tolerance: float, translucency: int, color: int) -> NXOpen.Facet.FacetedBody:
        """
         Creates an envelope object for a signle geometry 2. 
         @return createEnvelope (@link NXOpen.Facet.FacetedBody NXOpen.Facet.FacetedBody@endlink): .
        """
        pass
    
    ## Simulation first to ensure AutoSolveRecordData is not empty , then create a snapshot.  
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="time"> (float)  add time </param>
    ## <param name="isRecordManagerMode"> (bool) </param>
    def CreateSnapshot(time: float, isRecordManagerMode: bool) -> None:
        """
        Simulation first to ensure AutoSolveRecordData is not empty , then create a snapshot.  
        """
        pass
    
    ##  Creates the solution for Animation Designer. 
    ##  @return studyFolder (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateSolution(part: NXOpen.Part) -> NXOpen.AnimationDesigner.Nav.Solution:
        """
         Creates the solution for Animation Designer. 
         @return studyFolder (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink): .
        """
        pass
    
    ##  Clones the solution for Animation Designer. 
    ##  @return failList (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="originalSolution"> (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink) </param>
    ## <param name="copiedSolution"> (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink) </param>
    def DuplicateSolution(part: NXOpen.Part, originalSolution: NXOpen.AnimationDesigner.Nav.Solution, copiedSolution: NXOpen.AnimationDesigner.Nav.Solution) -> List[NXOpen.NXObject]:
        """
         Clones the solution for Animation Designer. 
         @return failList (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ## Add one spot in snapshot. Please simulation first to ensuer AutoSolveRecordData is not empty 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="physics_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  snapshot tag </param>
    ## <param name="time"> (float)  add time </param>
    ## <param name="isRecordManagerMode"> (bool) </param>
    def EditSnapshotAddTime(physics_object: NXOpen.NXObject, time: float, isRecordManagerMode: bool) -> None:
        """
        Add one spot in snapshot. Please simulation first to ensuer AutoSolveRecordData is not empty 
        """
        pass
    
    ##  Delete one spot in snapshot. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="physics_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  snapshot tag </param>
    ## <param name="time"> (float)  delete time </param>
    def EditSnapshotDeleteTime(physics_object: NXOpen.NXObject, time: float) -> None:
        """
         Delete one spot in snapshot. 
        """
        pass
    
    ##  Exports the PLMXML from Animation Designer in native. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="dirName"> (str)  the plmxml dir name </param>
    ## <param name="configFileName"> (str)  the config file name </param>
    ## <param name="reportWind"> (bool) </param>
    def ExportPlmxmlInNative(dirName: str, configFileName: str, reportWind: bool) -> None:
        """
         Exports the PLMXML from Animation Designer in native. 
        """
        pass
    
    ##  Exports the PLMXML from Animation Designer in teamcenter. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def ExportPlmxmlInTeamcenter() -> None:
        """
         Exports the PLMXML from Animation Designer in teamcenter. 
        """
        pass
    
    ##  Gets the active solution for Animation Designer. 
    ##  @return studyFolder (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def GetActiveSolution(part: NXOpen.Part) -> NXOpen.AnimationDesigner.Nav.Solution:
        """
         Gets the active solution for Animation Designer. 
         @return studyFolder (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink): .
        """
        pass
    
    ##  Ignores a collision interfered node. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="firstGeometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="secondGeometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def IgnoreCollisionInterferedNode(part: NXOpen.Part, firstGeometry: NXOpen.NXObject, secondGeometry: NXOpen.NXObject) -> None:
        """
         Ignores a collision interfered node. 
        """
        pass
    
    ##  Imports the PLMXML for Animation Designer in native. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="fileName"> (str)  the plmxml file name </param>
    ## <param name="reportWind"> (bool) </param>
    def ImportPlmxmlInNative(fileName: str, reportWind: bool) -> None:
        """
         Imports the PLMXML for Animation Designer in native. 
        """
        pass
    
    ##  Imports the PLMXML for Animation Designer in teamcenter. 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def ImportPlmxmlInTeamcenter() -> None:
        """
         Imports the PLMXML for Animation Designer in teamcenter. 
        """
        pass
    
    ##  Indicates whether to freeze the animation position to do modeling operations. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="bFreeze"> (bool) </param>
    def ModelingInAnimationContext(part: NXOpen.Part, bFreeze: bool) -> None:
        """
         Indicates whether to freeze the animation position to do modeling operations. 
        """
        pass
    
    ##  Moves contact face objects to their rigid parent. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="solutionTag"> (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink) </param>
    ## <param name="objects"> (@link Contact List[NXOpen.AnimationDesigner.Contact]@endlink)  The contacts to be moved </param>
    ## <param name="target"> (@link RigidGroup NXOpen.AnimationDesigner.RigidGroup@endlink)  target rigid </param>
    def MoveContactFacesToRigid(solutionTag: NXOpen.AnimationDesigner.Nav.Solution, objects: List[Contact], target: RigidGroup) -> None:
        """
         Moves contact face objects to their rigid parent. 
        """
        pass
    
    ##  Moves objects to container in navigator. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="solutionTag"> (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink) </param>
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The physics objects to be moved </param>
    ## <param name="target"> (@link NXOpen.AnimationDesigner.Nav.Container NXOpen.AnimationDesigner.Nav.Container@endlink)  target container tag </param>
    def MovePhysicsToContainer(solutionTag: NXOpen.AnimationDesigner.Nav.Solution, objects: List[NXOpen.NXObject], target: NXOpen.AnimationDesigner.Nav.Container) -> None:
        """
         Moves objects to container in navigator. 
        """
        pass
    
    ##  Moves objects to back to default folder in navigator. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="solutionTag"> (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink) </param>
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  The physics objects to be moved </param>
    ## <param name="target"> (@link NXOpen.AnimationDesigner.Nav.SubFolder NXOpen.AnimationDesigner.Nav.SubFolder@endlink)  target subfolder tag </param>
    def MovePhysicsToSubfolder(solutionTag: NXOpen.AnimationDesigner.Nav.Solution, objects: List[NXOpen.NXObject], target: NXOpen.AnimationDesigner.Nav.SubFolder) -> None:
        """
         Moves objects to back to default folder in navigator. 
        """
        pass
    
    ##  Reorders containers in navigator. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="parent"> (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink)  parent tag </param>
    ## <param name="objects"> (@link NXOpen.AnimationDesigner.Nav.Container List[NXOpen.AnimationDesigner.Nav.Container]@endlink)  The containers to be moved </param>
    ## <param name="target"> (@link NXOpen.AnimationDesigner.Nav.Container NXOpen.AnimationDesigner.Nav.Container@endlink)  target container tag </param>
    def ReorderContainers(parent: NXOpen.AnimationDesigner.Nav.Solution, objects: List[NXOpen.AnimationDesigner.Nav.Container], target: NXOpen.AnimationDesigner.Nav.Container) -> None:
        """
         Reorders containers in navigator. 
        """
        pass
    
    ##  Frees the Animation Designer reserved license for autotest. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="licenseModule"> (str)  the license module </param>
    def ResetReservedLicense(licenseModule: str) -> None:
        """
         Frees the Animation Designer reserved license for autotest. 
        """
        pass
    
    ##  Restores a collision ignored node. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="firstGeometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="secondGeometry"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def RestoreCollisionIgnoredNode(part: NXOpen.Part, firstGeometry: NXOpen.NXObject, secondGeometry: NXOpen.NXObject) -> None:
        """
         Restores a collision ignored node. 
        """
        pass
    
    ##  Sets the active solution for Animation Designer. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="studyFolder"> (@link NXOpen.AnimationDesigner.Nav.Solution NXOpen.AnimationDesigner.Nav.Solution@endlink) </param>
    def SetActiveSolution(part: NXOpen.Part, studyFolder: NXOpen.AnimationDesigner.Nav.Solution) -> None:
        """
         Sets the active solution for Animation Designer. 
        """
        pass
    
    ##  Sets a collision threshold. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="threshold"> (float) </param>
    def SetCollisionThreshold(part: NXOpen.Part, threshold: float) -> None:
        """
         Sets a collision threshold. 
        """
        pass
    
    ##  Renames the physics object for Animation Designer. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="physics_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)   </param>
    ## <param name="name"> (str)  the new name </param>
    def SetName(part: NXOpen.Part, physics_object: NXOpen.NXObject, name: str) -> None:
        """
         Renames the physics object for Animation Designer. 
        """
        pass
    
    ##  Sets the display or hide state of folder object in OM class. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="folder_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="bDisplay"> (bool) </param>
    def SetSubfolderDisplayOrHide(folder_object: NXOpen.NXObject, bDisplay: bool) -> None:
        """
         Sets the display or hide state of folder object in OM class. 
        """
        pass
    
    ##  Shows/hides rigid groups. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="rigidTag"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="isShown"> (bool) </param>
    def ShowHideRigidGroupGeometry(rigidTag: List[NXOpen.NXObject], isShown: bool) -> None:
        """
         Shows/hides rigid groups. 
        """
        pass
    
    ##  Update the motor index for Animation Designer. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="motor"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="index"> (int) </param>
    def UpdateMotorIndex(part: NXOpen.Part, motor: NXOpen.NXObject, index: int) -> None:
        """
         Update the motor index for Animation Designer. 
        """
        pass
    
    ##  Updates the display or hide state of folder object in OM class and icons in 3D graphic. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="folder_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="bDisplay"> (bool) </param>
    ## <param name="bHandleIcons"> (bool) </param>
    def UpdateSubfolderAndIconsDisplayState(folder_object: NXOpen.NXObject, bDisplay: bool, bHandleIcons: bool) -> None:
        """
         Updates the display or hide state of folder object in OM class and icons in 3D graphic. 
        """
        pass
    
    ##  Blanks the physics object for Animation Designer. 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="physics_object"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)   </param>
    ## <param name="blank"> (int)  Blank status: 0 - Unblanked, 1 - Blanked </param>
    def WriteBlankStatus(physics_object: NXOpen.NXObject, blank: int) -> None:
        """
         Blanks the physics object for Animation Designer. 
        """
        pass
    
##  Represents a @link NXOpen::AnimationDesigner::BondJointBuilder NXOpen::AnimationDesigner::BondJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::BondJointCollection::CreateBondJointBuilder  NXOpen::AnimationDesigner::BondJointCollection::CreateBondJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class BondJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.BondJointBuilder</ja_class>. """
    pass


import NXOpen
##  Represents a collection of Bond Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class BondJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Bond Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::BondJointBuilder NXOpen::AnimationDesigner::BondJointBuilder@endlink . 
    ##  @return builder (@link BondJointBuilder NXOpen.AnimationDesigner.BondJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="bondJoint"> (@link BondJoint NXOpen.AnimationDesigner.BondJoint@endlink)  @link NXOpen::AnimationDesigner::BondJoint NXOpen::AnimationDesigner::BondJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreateBondJointBuilder(part: NXOpen.Part, bondJoint: BondJoint) -> BondJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::BondJointBuilder NXOpen::AnimationDesigner::BondJointBuilder@endlink . 
         @return builder (@link BondJointBuilder NXOpen.AnimationDesigner.BondJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::BondJoint   NXOpen::AnimationDesigner::BondJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return bondJoint (@link BondJoint NXOpen.AnimationDesigner.BondJoint@endlink):  @link  NXOpen::AnimationDesigner::BondJoint   NXOpen::AnimationDesigner::BondJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::BondJoint   NXOpen::AnimationDesigner::BondJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> BondJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::BondJoint   NXOpen::AnimationDesigner::BondJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return bondJoint (@link BondJoint NXOpen.AnimationDesigner.BondJoint@endlink):  @link  NXOpen::AnimationDesigner::BondJoint   NXOpen::AnimationDesigner::BondJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Bond Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::BondJointBuilder  NXOpen::AnimationDesigner::BondJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class BondJoint(PhysicsJoint): 
    """ Represents a Bond Joint feature. """
    pass


import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class BulletCableAttachmentBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="objects"> (@link BulletCableAttachmentBuilder List[NXOpen.AnimationDesigner.BulletCableAttachmentBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[BulletCableAttachmentBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: BulletCableAttachmentBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="obj"> (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: BulletCableAttachmentBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="obj"> (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: BulletCableAttachmentBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: BulletCableAttachmentBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> BulletCableAttachmentBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link BulletCableAttachmentBuilder List[NXOpen.AnimationDesigner.BulletCableAttachmentBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[BulletCableAttachmentBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link BulletCableAttachmentBuilder List[NXOpen.AnimationDesigner.BulletCableAttachmentBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: BulletCableAttachmentBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link BulletCableAttachmentBuilder List[NXOpen.AnimationDesigner.BulletCableAttachmentBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[BulletCableAttachmentBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) </param>
    ## <param name="object1"> (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: BulletCableAttachmentBuilder, object2: BulletCableAttachmentBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  @brief  Represents a @link NXOpen::AnimationDesigner::BulletCableAttachmentBuilder NXOpen::AnimationDesigner::BulletCableAttachmentBuilder@endlink .  
## 
##   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::BulletCableCollection::CreateBulletCableAttachmentBuilder  NXOpen::AnimationDesigner::BulletCableCollection::CreateBulletCableAttachmentBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class BulletCableAttachmentBuilder(NXOpen.Builder): 
    """<summary> Represents a <ja_class>NXOpen.AnimationDesigner.BulletCableAttachmentBuilder</ja_class>. </summary>"""


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Anchor
    ##  Returns @brief  the anchor point.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Anchor(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Anchor
         Returns @brief  the anchor point.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Anchor

    ##  Returns @brief  the anchor point.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Anchor.setter
    def Anchor(self, anchor: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Anchor
         Returns @brief  the anchor point.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Attachment
    ##  Returns @brief  the atttachment.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def Attachment(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Attachment
         Returns @brief  the atttachment.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
    ##  Returns @brief  the direction vector.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns @brief  the direction vector.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction

    ##  Returns @brief  the direction vector.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction
         Returns @brief  the direction vector.  
            
        
           
         
        """
        pass
    
import NXOpen
##  @brief  Represents a @link NXOpen::AnimationDesigner::BulletCableBuilder NXOpen::AnimationDesigner::BulletCableBuilder@endlink .  
## 
##   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::BulletCableCollection::CreateBulletCableBuilder  NXOpen::AnimationDesigner::BulletCableCollection::CreateBulletCableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class BulletCableBuilder(NXOpen.Builder): 
    """<summary> Represents a <ja_class>NXOpen.AnimationDesigner.BulletCableBuilder</ja_class>. </summary>"""


    ##  @brief  the derivation type for bullet cable creation.  
    ## 
    ##  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curve</term><description> 
    ##  the guide curves </description> </item><item><term> 
    ## Body</term><description> 
    ##  the cable body </description> </item></list>
    class DerivationType(Enum):
        """
        Members Include: <Curve> <Body>
        """
        Curve: int
        Body: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> BulletCableBuilder.DerivationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) AttachmentList
    ##  Returns @brief  the list containing the defined attachments.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BulletCableAttachmentBuilderList
    @property
    def AttachmentList(self) -> BulletCableAttachmentBuilderList:
        """
        Getter for property: (@link BulletCableAttachmentBuilderList NXOpen.AnimationDesigner.BulletCableAttachmentBuilderList@endlink) AttachmentList
         Returns @brief  the list containing the defined attachments.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) CableBody
    ##  Returns @brief  the cable body.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def CableBody(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) CableBody
         Returns @brief  the cable body.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns @brief  the diameter.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
         Returns @brief  the diameter.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link BulletCableBuilder.DerivationType NXOpen.AnimationDesigner.BulletCableBuilder.DerivationType@endlink) GeometryType
    ##  Returns @brief  the geometry type used to derive the bullet cable.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BulletCableBuilder.DerivationType
    @property
    def GeometryType(self) -> BulletCableBuilder.DerivationType:
        """
        Getter for property: (@link BulletCableBuilder.DerivationType NXOpen.AnimationDesigner.BulletCableBuilder.DerivationType@endlink) GeometryType
         Returns @brief  the geometry type used to derive the bullet cable.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link BulletCableBuilder.DerivationType NXOpen.AnimationDesigner.BulletCableBuilder.DerivationType@endlink) GeometryType

    ##  Returns @brief  the geometry type used to derive the bullet cable.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @GeometryType.setter
    def GeometryType(self, geometryType: BulletCableBuilder.DerivationType):
        """
        Setter for property: (@link BulletCableBuilder.DerivationType NXOpen.AnimationDesigner.BulletCableBuilder.DerivationType@endlink) GeometryType
         Returns @brief  the geometry type used to derive the bullet cable.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) GuideCurves
    ##  Returns @brief  the guide curves.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def GuideCurves(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) GuideCurves
         Returns @brief  the guide curves.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link BulletFlexibleMaterial NXOpen.AnimationDesigner.BulletFlexibleMaterial@endlink) Material
    ##  Returns @brief  the material.  
    ##    This can be a @link NXOpen::AnimationDesigner::BulletFlexibleMaterial NXOpen::AnimationDesigner::BulletFlexibleMaterial@endlink .  
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return BulletFlexibleMaterial
    @property
    def Material(self) -> BulletFlexibleMaterial:
        """
        Getter for property: (@link BulletFlexibleMaterial NXOpen.AnimationDesigner.BulletFlexibleMaterial@endlink) Material
         Returns @brief  the material.  
           This can be a @link NXOpen::AnimationDesigner::BulletFlexibleMaterial NXOpen::AnimationDesigner::BulletFlexibleMaterial@endlink .  
        
           
         
        """
        pass
    
    ## Setter for property: (@link BulletFlexibleMaterial NXOpen.AnimationDesigner.BulletFlexibleMaterial@endlink) Material

    ##  Returns @brief  the material.  
    ##    This can be a @link NXOpen::AnimationDesigner::BulletFlexibleMaterial NXOpen::AnimationDesigner::BulletFlexibleMaterial@endlink .  
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Material.setter
    def Material(self, material: BulletFlexibleMaterial):
        """
        Setter for property: (@link BulletFlexibleMaterial NXOpen.AnimationDesigner.BulletFlexibleMaterial@endlink) Material
         Returns @brief  the material.  
           This can be a @link NXOpen::AnimationDesigner::BulletFlexibleMaterial NXOpen::AnimationDesigner::BulletFlexibleMaterial@endlink .  
        
           
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
import NXOpen
##  @brief  Represents a collection of Bullet Cable object.  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class BulletCableCollection(NXOpen.TaggedObjectCollection): 
    """<summary> Represents a collection of Bullet Cable object. </summary>"""


    ##  @brief  Creates a @link NXOpen::AnimationDesigner::BulletCableAttachmentBuilder NXOpen::AnimationDesigner::BulletCableAttachmentBuilder@endlink .  
    ## 
    ##  
    ##  @return builder (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateBulletCableAttachmentBuilder(part: NXOpen.Part) -> BulletCableAttachmentBuilder:
        """
         @brief  Creates a @link NXOpen::AnimationDesigner::BulletCableAttachmentBuilder NXOpen::AnimationDesigner::BulletCableAttachmentBuilder@endlink .  
        
         
         @return builder (@link BulletCableAttachmentBuilder NXOpen.AnimationDesigner.BulletCableAttachmentBuilder@endlink): .
        """
        pass
    
    ##  @brief  Creates a @link NXOpen::AnimationDesigner::BulletCableBuilder NXOpen::AnimationDesigner::BulletCableBuilder@endlink .  
    ## 
    ##  
    ##  @return builder (@link BulletCableBuilder NXOpen.AnimationDesigner.BulletCableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="cable"> (@link BulletCable NXOpen.AnimationDesigner.BulletCable@endlink)  @link NXOpen::AnimationDesigner::BulletCable NXOpen::AnimationDesigner::BulletCable@endlink  to be edited, if NULL then create a new one </param>
    def CreateBulletCableBuilder(part: NXOpen.Part, cable: BulletCable) -> BulletCableBuilder:
        """
         @brief  Creates a @link NXOpen::AnimationDesigner::BulletCableBuilder NXOpen::AnimationDesigner::BulletCableBuilder@endlink .  
        
         
         @return builder (@link BulletCableBuilder NXOpen.AnimationDesigner.BulletCableBuilder@endlink): .
        """
        pass
    
    ##  @brief  Finds the @link  NXOpen::AnimationDesigner::BulletCable   NXOpen::AnimationDesigner::BulletCable @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name.  
    ## 
    ##  
    ##  @return cable (@link BulletCable NXOpen.AnimationDesigner.BulletCable@endlink):  @link  NXOpen::AnimationDesigner::BulletCable   NXOpen::AnimationDesigner::BulletCable @endlink  with this name. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::BulletCable   NXOpen::AnimationDesigner::BulletCable @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> BulletCable:
        """
         @brief  Finds the @link  NXOpen::AnimationDesigner::BulletCable   NXOpen::AnimationDesigner::BulletCable @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name.  
        
         
         @return cable (@link BulletCable NXOpen.AnimationDesigner.BulletCable@endlink):  @link  NXOpen::AnimationDesigner::BulletCable   NXOpen::AnimationDesigner::BulletCable @endlink  with this name. .
        """
        pass
    
import NXOpen
##  @brief  Represents a Bullet Cable feature.  
## 
##   <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::BulletCableBuilder  NXOpen::AnimationDesigner::BulletCableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class BulletCable(NXOpen.DisplayableObject): 
    """<summary> Represents a Bullet Cable feature. </summary>"""
    pass


import NXOpen
##  @brief  Represents a @link NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder@endlink .  
## 
##   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::BulletFlexibleMaterialCollection::CreateBulletFlexibleMaterialBuilder  NXOpen::AnimationDesigner::BulletFlexibleMaterialCollection::CreateBulletFlexibleMaterialBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class BulletFlexibleMaterialBuilder(NXOpen.Builder): 
    """<summary> Represents a <ja_class>NXOpen.AnimationDesigner.BulletFlexibleMaterialBuilder</ja_class>. </summary>"""


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DampingValue
    ##  Returns @brief  the damping value  
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DampingValue(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DampingValue
         Returns @brief  the damping value  
          
          
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DensityValue
    ##  Returns @brief  the density value  
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DensityValue(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DensityValue
         Returns @brief  the density value  
          
          
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DynamicFrictionValue
    ##  Returns @brief  the dynamic friction value  
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DynamicFrictionValue(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DynamicFrictionValue
         Returns @brief  the dynamic friction value  
          
          
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearStiffnessValue
    ##  Returns @brief  the linear stiffness value  
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearStiffnessValue(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearStiffnessValue
         Returns @brief  the linear stiffness value  
          
          
           
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
import NXOpen
##  @brief  Represents a collection of Bullet Flexible Material object.  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class BulletFlexibleMaterialCollection(NXOpen.TaggedObjectCollection): 
    """<summary> Represents a collection of Bullet Flexible Material object. </summary>"""


    ##  @brief  Creates a @link NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder@endlink .  
    ## 
    ##  
    ##  @return builder (@link BulletFlexibleMaterialBuilder NXOpen.AnimationDesigner.BulletFlexibleMaterialBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="material"> (@link BulletFlexibleMaterial NXOpen.AnimationDesigner.BulletFlexibleMaterial@endlink)  @link NXOpen::AnimationDesigner::BulletFlexibleMaterial NXOpen::AnimationDesigner::BulletFlexibleMaterial@endlink  to be edited, if NULL then create a new one </param>
    def CreateBulletFlexibleMaterialBuilder(part: NXOpen.Part, material: BulletFlexibleMaterial) -> BulletFlexibleMaterialBuilder:
        """
         @brief  Creates a @link NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder@endlink .  
        
         
         @return builder (@link BulletFlexibleMaterialBuilder NXOpen.AnimationDesigner.BulletFlexibleMaterialBuilder@endlink): .
        """
        pass
    
    ##  @brief  Finds the @link  NXOpen::AnimationDesigner::BulletFlexibleMaterial   NXOpen::AnimationDesigner::BulletFlexibleMaterial @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name.  
    ## 
    ##  
    ##  @return material (@link BulletFlexibleMaterial NXOpen.AnimationDesigner.BulletFlexibleMaterial@endlink):  @link  NXOpen::AnimationDesigner::BulletFlexibleMaterial   NXOpen::AnimationDesigner::BulletFlexibleMaterial @endlink  with this name. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::BulletFlexibleMaterial   NXOpen::AnimationDesigner::BulletFlexibleMaterial @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> BulletFlexibleMaterial:
        """
         @brief  Finds the @link  NXOpen::AnimationDesigner::BulletFlexibleMaterial   NXOpen::AnimationDesigner::BulletFlexibleMaterial @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name.  
        
         
         @return material (@link BulletFlexibleMaterial NXOpen.AnimationDesigner.BulletFlexibleMaterial@endlink):  @link  NXOpen::AnimationDesigner::BulletFlexibleMaterial   NXOpen::AnimationDesigner::BulletFlexibleMaterial @endlink  with this name. .
        """
        pass
    
import NXOpen
##  @brief  Represents a Bullet Flexible Material feature.  
## 
##   <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder  NXOpen::AnimationDesigner::BulletFlexibleMaterialBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class BulletFlexibleMaterial(NXOpen.DisplayableObject): 
    """<summary> Represents a Bullet Flexible Material feature. </summary>"""
    pass


import NXOpen
##  Represents a @link AnimationDesigner::ConstraintConversionBuilder AnimationDesigner::ConstraintConversionBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::AnimationDesignerManager::CreateConstraintConversionBuilder  NXOpen::AnimationDesigner::AnimationDesignerManager::CreateConstraintConversionBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ConstraintConversionBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>AnimationDesigner.ConstraintConversionBuilder</ja_class> builder """


    ##  the assembly object types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Constraint</term><description> 
    ##  Assembly Constraint </description> </item><item><term> 
    ## JointAndCoupler</term><description> 
    ##  Assembly Joint and Coupler </description> </item><item><term> 
    ## All</term><description> 
    ##  Adopt all mode Joint and Coupler </description> </item></list>
    class AssemblyObjectTypes(Enum):
        """
        Members Include: <Constraint> <JointAndCoupler> <All>
        """
        Constraint: int
        JointAndCoupler: int
        All: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConstraintConversionBuilder.AssemblyObjectTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   @brief  Enables the conversion of objects. If it is impossible, the objects will keep unable status.  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="physics"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="enable"> (bool) </param>
    def EnableObjectsConversion(self, physics: List[NXOpen.NXObject], enable: bool) -> None:
        """
          @brief  Enables the conversion of objects. If it is impossible, the objects will keep unable status.  
        
          
        """
        pass
    
    ##   @brief  Returns the tentatively converting assembly names.  
    ## 
    ##   
    ##  @return assNames (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetTentativeAssemblyNames(self) -> List[str]:
        """
          @brief  Returns the tentatively converting assembly names.  
        
          
         @return assNames (List[str]): .
        """
        pass
    
    ##   @brief  Returns the tentatively converting physics objects.  
    ## 
    ##   
    ##  @return physics (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetTentativePhysics(self) -> List[NXOpen.NXObject]:
        """
          @brief  Returns the tentatively converting physics objects.  
        
          
         @return physics (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##   @brief  Sets the assembly object type to convert.  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="type"> (@link ConstraintConversionBuilder.AssemblyObjectTypes NXOpen.AnimationDesigner.ConstraintConversionBuilder.AssemblyObjectTypes@endlink) </param>
    def SetAssemblyObjectType(self, type: ConstraintConversionBuilder.AssemblyObjectTypes) -> None:
        """
          @brief  Sets the assembly object type to convert.  
        
          
        """
        pass
    
    ##   @brief  Tentatively converts assembly constraints.  
    ## 
    ##   
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def TentativelyConvert(self) -> None:
        """
          @brief  Tentatively converts assembly constraints.  
        
          
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::ContactBuilder NXOpen::AnimationDesigner::ContactBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::ContactCollection::CreateContactBuilder  NXOpen::AnimationDesigner::ContactCollection::CreateContactBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ContactBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.ContactBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Geometry
    ##  Returns the geometries.  
    ##    This can be a @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink ,
    ##             @link NXOpen::Point NXOpen::Point@endlink , @link NXOpen::Face NXOpen::Face@endlink ,
    ##             @link NXOpen::Edge NXOpen::Edge@endlink , bodies and curves.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Geometry(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Geometry
         Returns the geometries.  
           This can be a @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink ,
                    @link NXOpen::Point NXOpen::Point@endlink , @link NXOpen::Face NXOpen::Face@endlink ,
                    @link NXOpen::Edge NXOpen::Edge@endlink , bodies and curves.   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ##  Sets the geometry 
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="geometries"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Input geometries </param>
    def SetGeometry(self, geometries: List[NXOpen.NXObject]) -> None:
        """
         Sets the geometry 
        """
        pass
    
import NXOpen
##  Represents a collection of Contact objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class ContactCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Contact objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::ContactBuilder NXOpen::AnimationDesigner::ContactBuilder@endlink . 
    ##  @return builder (@link ContactBuilder NXOpen.AnimationDesigner.ContactBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="contactFace"> (@link Contact NXOpen.AnimationDesigner.Contact@endlink)  @link NXOpen::AnimationDesigner::Contact NXOpen::AnimationDesigner::Contact@endlink  to be edited, if NULL then create a new one </param>
    def CreateContactBuilder(part: NXOpen.Part, contactFace: Contact) -> ContactBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::ContactBuilder NXOpen::AnimationDesigner::ContactBuilder@endlink . 
         @return builder (@link ContactBuilder NXOpen.AnimationDesigner.ContactBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return contactFace (@link Contact NXOpen.AnimationDesigner.Contact@endlink):  @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> Contact:
        """
         Finds the @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return contactFace (@link Contact NXOpen.AnimationDesigner.Contact@endlink):  @link  NXOpen::AnimationDesigner::Contact   NXOpen::AnimationDesigner::Contact @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a Contact feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::ContactBuilder  NXOpen::AnimationDesigner::ContactBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Contact(NXOpen.DisplayableObject): 
    """ Represents a Contact feature. """
    pass


##  Specifies convention of Euler angle 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Xyz</term><description> 
##  </description> </item><item><term> 
## Xzy</term><description> 
##  </description> </item><item><term> 
## Yxz</term><description> 
##  </description> </item><item><term> 
## Yzx</term><description> 
##  </description> </item><item><term> 
## Zxy</term><description> 
##  </description> </item><item><term> 
## Zyx</term><description> 
##  </description> </item><item><term> 
## Xyx</term><description> 
##  </description> </item><item><term> 
## Xzx</term><description> 
##  </description> </item><item><term> 
## Yxy</term><description> 
##  </description> </item><item><term> 
## Yzy</term><description> 
##  </description> </item><item><term> 
## Zxz</term><description> 
##  </description> </item><item><term> 
## Zyz</term><description> 
##  </description> </item></list>
class Convention(Enum):
    """
    Members Include: <Xyz> <Xzy> <Yxz> <Yzx> <Zxy> <Zyx> <Xyx> <Xzx> <Yxy> <Yzy> <Zxz> <Zyz>
    """
    Xyz: int
    Xzy: int
    Yxz: int
    Yzx: int
    Zxy: int
    Zyx: int
    Xyx: int
    Xzx: int
    Yxy: int
    Yzy: int
    Zxz: int
    Zyz: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> Convention:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
##  Represents a base builder for Couplers.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class CouplerBuilder(NXOpen.Builder): 
    """ Represents a base builder for Couplers. """


    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the coupler </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the coupler </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <NoColor>
        """
        SpecifyColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CouplerBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link CouplerBuilder.ColorOptions NXOpen.AnimationDesigner.CouplerBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color options.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return CouplerBuilder.ColorOptions
    @property
    def ColorOption(self) -> CouplerBuilder.ColorOptions:
        """
        Getter for property: (@link CouplerBuilder.ColorOptions NXOpen.AnimationDesigner.CouplerBuilder.ColorOptions@endlink) ColorOption
         Returns the color options.  
             
         
        """
        pass
    
    ## Setter for property: (@link CouplerBuilder.ColorOptions NXOpen.AnimationDesigner.CouplerBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color options.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: CouplerBuilder.ColorOptions):
        """
        Setter for property: (@link CouplerBuilder.ColorOptions NXOpen.AnimationDesigner.CouplerBuilder.ColorOptions@endlink) ColorOption
         Returns the color options.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) MasterAxisJoint
    ##  Returns the master axis joint.  
    ##    This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink , @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  or
    ##             @link NXOpen::AnimationDesigner::CylindricalJoint NXOpen::AnimationDesigner::CylindricalJoint@endlink .   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def MasterAxisJoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) MasterAxisJoint
         Returns the master axis joint.  
           This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink , @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  or
                    @link NXOpen::AnimationDesigner::CylindricalJoint NXOpen::AnimationDesigner::CylindricalJoint@endlink .   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SlaveAxisJoint
    ##  Returns the slave axis joint.  
    ##    This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink , @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  or
    ##             @link NXOpen::AnimationDesigner::CylindricalJoint NXOpen::AnimationDesigner::CylindricalJoint@endlink .   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def SlaveAxisJoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SlaveAxisJoint
         Returns the slave axis joint.  
           This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink , @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  or
                    @link NXOpen::AnimationDesigner::CylindricalJoint NXOpen::AnimationDesigner::CylindricalJoint@endlink .   
         
        """
        pass
    
import NXOpen
##  Represents the Animation Designer coupler class.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class Coupler(NXOpen.DisplayableObject): 
    """ Represents the Animation Designer coupler class. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::CurveOnCurveJointBuilder NXOpen::AnimationDesigner::CurveOnCurveJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::CurveOnCurveJointCollection::CreateCurveOnCurveJointBuilder  NXOpen::AnimationDesigner::CurveOnCurveJointCollection::CreateCurveOnCurveJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CurveOnCurveJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.CurveOnCurveJointBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##  Returns the axis vector which is tangent to the connected curve at the selected point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##  Returns the axis vector which is tangent to the connected curve at the selected point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns the offset specifies the "Zero Point" on the curve whose distance to the point along the curve is the offset value.  
    ##   
    ##             Zero Point is on the opposite direction of the axis with respect to the point on the curve.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns the offset specifies the "Zero Point" on the curve whose distance to the point along the curve is the offset value.  
          
                    Zero Point is on the opposite direction of the axis with respect to the point on the curve.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
    ##  Returns the selected point on curve.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointOnCurve(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve

    ##  Returns the selected point on curve.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PointOnCurve.setter
    def PointOnCurve(self, pointOnCurve: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    
    ## Getter for property: (bool) Sliding
    ##  Returns the sliding flag.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def Sliding(self) -> bool:
        """
        Getter for property: (bool) Sliding
         Returns the sliding flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) Sliding

    ##  Returns the sliding flag.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Sliding.setter
    def Sliding(self, sliding: bool):
        """
        Setter for property: (bool) Sliding
         Returns the sliding flag.  
             
         
        """
        pass
    
    ##  Evaluates the path. If there is no path, create it, otherwise evaluate it. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge </param>
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluates the path. If there is no path, create it, otherwise evaluate it. 
        """
        pass
    
    ##  Gets the connected curve which the attachment will move along. 
    ##  @return curves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetConnectedCurve(self) -> List[NXOpen.NXObject]:
        """
         Gets the connected curve which the attachment will move along. 
         @return curves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge .
        """
        pass
    
    ##  Gets the section curve which belong to the attachment. 
    ##  @return curves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetSectionCurve(self) -> List[NXOpen.NXObject]:
        """
         Gets the section curve which belong to the attachment. 
         @return curves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge .
        """
        pass
    
    ##  Sets the connected curve which the attachment will move along. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge </param>
    def SetConnectedCurve(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Sets the connected curve which the attachment will move along. 
        """
        pass
    
    ##  Sets the section curve which belong to the attachment. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge </param>
    def SetSectionCurve(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Sets the section curve which belong to the attachment. 
        """
        pass
    
import NXOpen
##  Represents a collection of Curve On Curve Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CurveOnCurveJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Curve On Curve Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::CurveOnCurveJointBuilder NXOpen::AnimationDesigner::CurveOnCurveJointBuilder@endlink . 
    ##  @return builder (@link CurveOnCurveJointBuilder NXOpen.AnimationDesigner.CurveOnCurveJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="joint"> (@link CurveOnCurveJoint NXOpen.AnimationDesigner.CurveOnCurveJoint@endlink)  @link NXOpen::AnimationDesigner::CurveOnCurveJoint NXOpen::AnimationDesigner::CurveOnCurveJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreateCurveOnCurveJointBuilder(part: NXOpen.Part, joint: CurveOnCurveJoint) -> CurveOnCurveJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::CurveOnCurveJointBuilder NXOpen::AnimationDesigner::CurveOnCurveJointBuilder@endlink . 
         @return builder (@link CurveOnCurveJointBuilder NXOpen.AnimationDesigner.CurveOnCurveJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::CurveOnCurveJoint   NXOpen::AnimationDesigner::CurveOnCurveJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return curveOnCurveJoint (@link CurveOnCurveJoint NXOpen.AnimationDesigner.CurveOnCurveJoint@endlink):  @link  NXOpen::AnimationDesigner::CurveOnCurveJoint   NXOpen::AnimationDesigner::CurveOnCurveJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::CurveOnCurveJoint   NXOpen::AnimationDesigner::CurveOnCurveJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> CurveOnCurveJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::CurveOnCurveJoint   NXOpen::AnimationDesigner::CurveOnCurveJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return curveOnCurveJoint (@link CurveOnCurveJoint NXOpen.AnimationDesigner.CurveOnCurveJoint@endlink):  @link  NXOpen::AnimationDesigner::CurveOnCurveJoint   NXOpen::AnimationDesigner::CurveOnCurveJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Curve On Curve Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::CurveOnCurveJointBuilder  NXOpen::AnimationDesigner::CurveOnCurveJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CurveOnCurveJoint(PhysicsJoint): 
    """ Represents a Curve On Curve Joint feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::CylindricalJointBuilder NXOpen::AnimationDesigner::CylindricalJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::CylindricalJointCollection::CreateCylindricalJointBuilder  NXOpen::AnimationDesigner::CylindricalJointCollection::CreateCylindricalJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CylindricalJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.CylindricalJointBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
    ##  Returns the anchor point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint

    ##  Returns the anchor point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularLowerLimit
    ##  Returns the angular lower limit.  
    ##    The lower limit setup for joint angular movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AngularLowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularLowerLimit
         Returns the angular lower limit.  
           The lower limit setup for joint angular movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularUpperLimit
    ##  Returns the angular upper limit.  
    ##    The upper limit setup for joint angular movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AngularUpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularUpperLimit
         Returns the angular upper limit.  
           The upper limit setup for joint angular movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##  Returns the axis vector.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##  Returns the axis vector.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EnableAngularLowerLimit
    ##  Returns the angular lower limit option.  
    ##    If the enable is true, then this joint will be
    ##             applied the lower limit in angular direction.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableAngularLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableAngularLowerLimit
         Returns the angular lower limit option.  
           If the enable is true, then this joint will be
                    applied the lower limit in angular direction.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableAngularLowerLimit

    ##  Returns the angular lower limit option.  
    ##    If the enable is true, then this joint will be
    ##             applied the lower limit in angular direction.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableAngularLowerLimit.setter
    def EnableAngularLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableAngularLowerLimit
         Returns the angular lower limit option.  
           If the enable is true, then this joint will be
                    applied the lower limit in angular direction.   
         
        """
        pass
    
    ## Getter for property: (bool) EnableAngularUpperLimit
    ##  Returns the angular upper limit option.  
    ##    If the enable is true, then this joint will be
    ##             applied the upper limit in angular direction.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableAngularUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableAngularUpperLimit
         Returns the angular upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in angular direction.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableAngularUpperLimit

    ##  Returns the angular upper limit option.  
    ##    If the enable is true, then this joint will be
    ##             applied the upper limit in angular direction.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableAngularUpperLimit.setter
    def EnableAngularUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableAngularUpperLimit
         Returns the angular upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in angular direction.   
         
        """
        pass
    
    ## Getter for property: (bool) EnableLinearLowerLimit
    ##  Returns the linear lower limit option.  
    ##   If the enable is true, then this joint will be
    ##             applied the lower limit in linear direction.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableLinearLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLinearLowerLimit
         Returns the linear lower limit option.  
          If the enable is true, then this joint will be
                    applied the lower limit in linear direction.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableLinearLowerLimit

    ##  Returns the linear lower limit option.  
    ##   If the enable is true, then this joint will be
    ##             applied the lower limit in linear direction.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableLinearLowerLimit.setter
    def EnableLinearLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLinearLowerLimit
         Returns the linear lower limit option.  
          If the enable is true, then this joint will be
                    applied the lower limit in linear direction.   
         
        """
        pass
    
    ## Getter for property: (bool) EnableLinearUpperLimit
    ##  Returns the linear upper limit option.  
    ##    If the enable is true, then this joint will be
    ##             applied the upper limit in linear direction.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableLinearUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLinearUpperLimit
         Returns the linear upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in linear direction.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableLinearUpperLimit

    ##  Returns the linear upper limit option.  
    ##    If the enable is true, then this joint will be
    ##             applied the upper limit in linear direction.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableLinearUpperLimit.setter
    def EnableLinearUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLinearUpperLimit
         Returns the linear upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in linear direction.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearLowerLimit
    ##  Returns the linear lower limit.  
    ##    The lower limit setup for joint linear movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearLowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearLowerLimit
         Returns the linear lower limit.  
           The lower limit setup for joint linear movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearUpperLimit
    ##  Returns the linear upper limit.  
    ##    The upper limit setup for joint linear movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearUpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearUpperLimit
         Returns the linear upper limit.  
           The upper limit setup for joint linear movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns the offset value.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns the offset value.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartAngle
    ##  Returns the start angle.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Expression
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartAngle
         Returns the start angle.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a collection of Cylindrical Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CylindricalJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Cylindrical Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::CylindricalJointBuilder NXOpen::AnimationDesigner::CylindricalJointBuilder@endlink . 
    ##  @return builder (@link CylindricalJointBuilder NXOpen.AnimationDesigner.CylindricalJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="cylindricalJoint"> (@link CylindricalJoint NXOpen.AnimationDesigner.CylindricalJoint@endlink)  @link NXOpen::AnimationDesigner::CylindricalJoint NXOpen::AnimationDesigner::CylindricalJoint@endlink  to be edited, if NULL then create a new one </param>
    @overload
    def CreateCylindricalJointBuilder(part: NXOpen.Part, cylindricalJoint: CylindricalJoint) -> CylindricalJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::CylindricalJointBuilder NXOpen::AnimationDesigner::CylindricalJointBuilder@endlink . 
         @return builder (@link CylindricalJointBuilder NXOpen.AnimationDesigner.CylindricalJointBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::AnimationDesigner::CylindricalJointBuilder NXOpen::AnimationDesigner::CylindricalJointBuilder@endlink . 
    ##  @return builder (@link CylindricalJointBuilder NXOpen.AnimationDesigner.CylindricalJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="cylindricalJoint"> (@link CylindricalJoint NXOpen.AnimationDesigner.CylindricalJoint@endlink)  @link NXOpen::AnimationDesigner::CylindricalJoint NXOpen::AnimationDesigner::CylindricalJoint@endlink  to be edited, if NULL then create a new one </param>
    ## <param name="partOcc"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  for the edited cylindrical joint occurrence </param>
    @overload
    def CreateCylindricalJointBuilder(part: NXOpen.Part, cylindricalJoint: CylindricalJoint, partOcc: NXOpen.Assemblies.Component) -> CylindricalJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::CylindricalJointBuilder NXOpen::AnimationDesigner::CylindricalJointBuilder@endlink . 
         @return builder (@link CylindricalJointBuilder NXOpen.AnimationDesigner.CylindricalJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::CylindricalJoint   NXOpen::AnimationDesigner::CylindricalJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return cylindricalJoint (@link CylindricalJoint NXOpen.AnimationDesigner.CylindricalJoint@endlink):  @link  NXOpen::AnimationDesigner::CylindricalJoint   NXOpen::AnimationDesigner::CylindricalJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::CylindricalJoint   NXOpen::AnimationDesigner::CylindricalJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> CylindricalJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::CylindricalJoint   NXOpen::AnimationDesigner::CylindricalJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return cylindricalJoint (@link CylindricalJoint NXOpen.AnimationDesigner.CylindricalJoint@endlink):  @link  NXOpen::AnimationDesigner::CylindricalJoint   NXOpen::AnimationDesigner::CylindricalJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Cylindrical Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::CylindricalJointBuilder  NXOpen::AnimationDesigner::CylindricalJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class CylindricalJoint(PhysicsJoint): 
    """ Represents a Cylindrical Joint feature. """
    pass


import NXOpen
##  Represents a builder to export a trace from @link NXOpen::AnimationDesigner::Tracer NXOpen::AnimationDesigner::Tracer@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::AnimationDesignerManager::CreateExportTraceBuilder  NXOpen::AnimationDesigner::AnimationDesignerManager::CreateExportTraceBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class ExportTraceBuilder(NXOpen.Builder): 
    """ Represents a builder to export a trace from <ja_class>NXOpen.AnimationDesigner.Tracer</ja_class>. """


    ## Getter for property: (@link Convention NXOpen.AnimationDesigner.Convention@endlink) EulerAngleConvention
    ##  Returns  @brief  the Euler angle convention.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return Convention
    @property
    def EulerAngleConvention(self) -> Convention:
        """
        Getter for property: (@link Convention NXOpen.AnimationDesigner.Convention@endlink) EulerAngleConvention
         Returns  @brief  the Euler angle convention.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link Convention NXOpen.AnimationDesigner.Convention@endlink) EulerAngleConvention

    ##  Returns  @brief  the Euler angle convention.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @EulerAngleConvention.setter
    def EulerAngleConvention(self, type: Convention):
        """
        Setter for property: (@link Convention NXOpen.AnimationDesigner.Convention@endlink) EulerAngleConvention
         Returns  @brief  the Euler angle convention.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (str) ExportFile
    ##  Returns  @brief  the export file name  
    ##   
    ##   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def ExportFile(self) -> str:
        """
        Getter for property: (str) ExportFile
         Returns  @brief  the export file name  
          
          
            
         
        """
        pass
    
    ## Setter for property: (str) ExportFile

    ##  Returns  @brief  the export file name  
    ##   
    ##   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ExportFile.setter
    def ExportFile(self, exportFile: str):
        """
        Setter for property: (str) ExportFile
         Returns  @brief  the export file name  
          
          
            
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::FixedJointBuilder NXOpen::AnimationDesigner::FixedJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::FixedJointCollection::CreateFixedJointBuilder  NXOpen::AnimationDesigner::FixedJointCollection::CreateFixedJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class FixedJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.FixedJointBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FeedbackPoint
    ##  Returns the position of visual feedback point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Get feedback point mechanism deprecated in 1899.  Always get null tag.  <br> 

    ## @return NXOpen.Point
    @property
    def FeedbackPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FeedbackPoint
         Returns the position of visual feedback point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FeedbackPoint

    ##  Returns the position of visual feedback point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1899.0.0.  Set feedback point mechanism deprecated in 1899.  Always sets failed.  <br> 

    @FeedbackPoint.setter
    def FeedbackPoint(self, feedback: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FeedbackPoint
         Returns the position of visual feedback point.  
             
         
        """
        pass
    
import NXOpen
##  Represents a collection of Fixed Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class FixedJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Fixed Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::FixedJointBuilder NXOpen::AnimationDesigner::FixedJointBuilder@endlink . 
    ##  @return builder (@link FixedJointBuilder NXOpen.AnimationDesigner.FixedJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="fixedJoint"> (@link FixedJoint NXOpen.AnimationDesigner.FixedJoint@endlink)  @link NXOpen::AnimationDesigner::FixedJoint NXOpen::AnimationDesigner::FixedJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreateFixedJointBuilder(part: NXOpen.Part, fixedJoint: FixedJoint) -> FixedJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::FixedJointBuilder NXOpen::AnimationDesigner::FixedJointBuilder@endlink . 
         @return builder (@link FixedJointBuilder NXOpen.AnimationDesigner.FixedJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::FixedJoint   NXOpen::AnimationDesigner::FixedJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return fixedJoint (@link FixedJoint NXOpen.AnimationDesigner.FixedJoint@endlink):  @link  NXOpen::AnimationDesigner::FixedJoint   NXOpen::AnimationDesigner::FixedJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::FixedJoint   NXOpen::AnimationDesigner::FixedJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> FixedJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::FixedJoint   NXOpen::AnimationDesigner::FixedJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return fixedJoint (@link FixedJoint NXOpen.AnimationDesigner.FixedJoint@endlink):  @link  NXOpen::AnimationDesigner::FixedJoint   NXOpen::AnimationDesigner::FixedJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Fixed Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::FixedJointBuilder  NXOpen::AnimationDesigner::FixedJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class FixedJoint(PhysicsJoint): 
    """ Represents a Fixed Joint feature. """
    pass


import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class FlexibleCableAttachmentBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="objects"> (@link FlexibleCableAttachmentBuilder List[NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[FlexibleCableAttachmentBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: FlexibleCableAttachmentBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="obj"> (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: FlexibleCableAttachmentBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="obj"> (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: FlexibleCableAttachmentBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: FlexibleCableAttachmentBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> FlexibleCableAttachmentBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link FlexibleCableAttachmentBuilder List[NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[FlexibleCableAttachmentBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link FlexibleCableAttachmentBuilder List[NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: FlexibleCableAttachmentBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link FlexibleCableAttachmentBuilder List[NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[FlexibleCableAttachmentBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) </param>
    ## <param name="object1"> (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: FlexibleCableAttachmentBuilder, object2: FlexibleCableAttachmentBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
##  @brief  Represents a @link NXOpen::AnimationDesigner::FlexibleCableAttachmentBuilder NXOpen::AnimationDesigner::FlexibleCableAttachmentBuilder@endlink .  
## 
##   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::FlexibleCableCollection::CreateFlexibleCableAttachmentBuilder  NXOpen::AnimationDesigner::FlexibleCableCollection::CreateFlexibleCableAttachmentBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class FlexibleCableAttachmentBuilder(NXOpen.Builder): 
    """<summary> Represents a <ja_class>NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder</ja_class>. </summary>"""


    ##  @brief  the attachment types.  
    ## 
    ##  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fixed</term><description> 
    ##  The fixed attachment </description> </item><item><term> 
    ## Rotating</term><description> 
    ##  The rotating attachment </description> </item><item><term> 
    ## RotatingSliding</term><description> 
    ##  The rotating and sliding attachment </description> </item><item><term> 
    ## RetractSystemType1</term><description> 
    ##  The retract system type1 attachment </description> </item><item><term> 
    ## RetractSystemType2</term><description> 
    ##  The retract system type2 attachment </description> </item><item><term> 
    ## RetractSystemType3</term><description> 
    ##  The retract system type3 attachment </description> </item></list>
    class AttachmentTypes(Enum):
        """
        Members Include: <Fixed> <Rotating> <RotatingSliding> <RetractSystemType1> <RetractSystemType2> <RetractSystemType3>
        """
        Fixed: int
        Rotating: int
        RotatingSliding: int
        RetractSystemType1: int
        RetractSystemType2: int
        RetractSystemType3: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableAttachmentBuilder.AttachmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  @brief  the attachment rotation axes.  
    ## 
    ##  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## X</term><description> 
    ##  The X axis </description> </item><item><term> 
    ## Y</term><description> 
    ##  The Y axis </description> </item><item><term> 
    ## Z</term><description> 
    ##  The Z axis </description> </item><item><term> 
    ## All</term><description> 
    ##  All axes </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  No axis </description> </item></list>
    class RotationAxes(Enum):
        """
        Members Include: <X> <Y> <Z> <All> <NotSet>
        """
        X: int
        Y: int
        Z: int
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableAttachmentBuilder.RotationAxes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Attachment
    ##  Returns @brief  the atttachment.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def Attachment(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Attachment
         Returns @brief  the atttachment.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) AttachmentFrame
    ##  Returns @brief  the attachment frame.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def AttachmentFrame(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) AttachmentFrame
         Returns @brief  the attachment frame.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) AttachmentFrame

    ##  Returns @brief  the attachment frame.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AttachmentFrame.setter
    def AttachmentFrame(self, attachmentFrame: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) AttachmentFrame
         Returns @brief  the attachment frame.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link FlexibleCableAttachmentBuilder.AttachmentTypes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.AttachmentTypes@endlink) AttachmentType
    ##  Returns @brief  the attachment type.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FlexibleCableAttachmentBuilder.AttachmentTypes
    @property
    def AttachmentType(self) -> FlexibleCableAttachmentBuilder.AttachmentTypes:
        """
        Getter for property: (@link FlexibleCableAttachmentBuilder.AttachmentTypes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.AttachmentTypes@endlink) AttachmentType
         Returns @brief  the attachment type.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link FlexibleCableAttachmentBuilder.AttachmentTypes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.AttachmentTypes@endlink) AttachmentType

    ##  Returns @brief  the attachment type.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AttachmentType.setter
    def AttachmentType(self, attachmentType: FlexibleCableAttachmentBuilder.AttachmentTypes):
        """
        Setter for property: (@link FlexibleCableAttachmentBuilder.AttachmentTypes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.AttachmentTypes@endlink) AttachmentType
         Returns @brief  the attachment type.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
    ##  Returns @brief  the distance along cable between the attachment point and the cable start point.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) DistanceFromStart
         Returns @brief  the distance along cable between the attachment point and the cable start point.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxRetractedLength
    ##  Returns @brief  the maximum length of cable that can be retracted.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxRetractedLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxRetractedLength
         Returns @brief  the maximum length of cable that can be retracted.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinRetractedLength
    ##  Returns @brief  the minimum length of cable that can be retracted.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinRetractedLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinRetractedLength
         Returns @brief  the minimum length of cable that can be retracted.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link FlexibleCableAttachmentBuilder.RotationAxes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.RotationAxes@endlink) RotationAxis
    ##  Returns @brief  the attachment rotation axis.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FlexibleCableAttachmentBuilder.RotationAxes
    @property
    def RotationAxis(self) -> FlexibleCableAttachmentBuilder.RotationAxes:
        """
        Getter for property: (@link FlexibleCableAttachmentBuilder.RotationAxes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.RotationAxes@endlink) RotationAxis
         Returns @brief  the attachment rotation axis.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link FlexibleCableAttachmentBuilder.RotationAxes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.RotationAxes@endlink) RotationAxis

    ##  Returns @brief  the attachment rotation axis.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: FlexibleCableAttachmentBuilder.RotationAxes):
        """
        Setter for property: (@link FlexibleCableAttachmentBuilder.RotationAxes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.RotationAxes@endlink) RotationAxis
         Returns @brief  the attachment rotation axis.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) SecondaryAttachmentFrame
    ##  Returns @brief  the secondary attachment frame.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def SecondaryAttachmentFrame(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) SecondaryAttachmentFrame
         Returns @brief  the secondary attachment frame.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) SecondaryAttachmentFrame

    ##  Returns @brief  the secondary attachment frame.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SecondaryAttachmentFrame.setter
    def SecondaryAttachmentFrame(self, secondaryAttachmentFrame: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) SecondaryAttachmentFrame
         Returns @brief  the secondary attachment frame.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondaryDistanceFromStart
    ##  Returns @brief  the distance along cable between the secondary attachment point and the cable start point.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SecondaryDistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SecondaryDistanceFromStart
         Returns @brief  the distance along cable between the secondary attachment point and the cable start point.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SpringConstant
    ##  Returns @brief  the physical constant that determines how hard or easy it is to move the attachment when retracting or extending the cable.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def SpringConstant(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) SpringConstant
         Returns @brief  the physical constant that determines how hard or easy it is to move the attachment when retracting or extending the cable.  
            
        
           
         
        """
        pass
    
import NXOpen
##  @brief  Represents a @link NXOpen::AnimationDesigner::FlexibleCableBuilder NXOpen::AnimationDesigner::FlexibleCableBuilder@endlink .  
## 
##   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::FlexibleCableCollection::CreateFlexibleCableBuilder  NXOpen::AnimationDesigner::FlexibleCableCollection::CreateFlexibleCableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class FlexibleCableBuilder(NXOpen.Builder): 
    """<summary> Represents a <ja_class>NXOpen.AnimationDesigner.FlexibleCableBuilder</ja_class>. </summary>"""


    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the flexible cable </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the flexible cable </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <NoColor>
        """
        SpecifyColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  @brief  the geometry types for flexible cable creation.  
    ## 
    ##  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Curve</term><description> 
    ##  Use the curves to create </description> </item><item><term> 
    ## Body</term><description> 
    ##  Use the body to create </description> </item><item><term> 
    ## Parameter</term><description> 
    ##  Use the parameters to create </description> </item></list>
    class GeometryTypes(Enum):
        """
        Members Include: <Curve> <Body> <Parameter>
        """
        Curve: int
        Body: int
        Parameter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.GeometryTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  @brief  the section types for flexible cable creation.  
    ## 
    ##  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Circle</term><description> 
    ##  Circle Section </description> </item><item><term> 
    ## Rectangle</term><description> 
    ##  Rectangle Section </description> </item></list>
    class SectionTypes(Enum):
        """
        Members Include: <Circle> <Rectangle>
        """
        Circle: int
        Rectangle: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.SectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) AttachmentList
    ##  Returns @brief  the list containing the defined attachments.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FlexibleCableAttachmentBuilderList
    @property
    def AttachmentList(self) -> FlexibleCableAttachmentBuilderList:
        """
        Getter for property: (@link FlexibleCableAttachmentBuilderList NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderList@endlink) AttachmentList
         Returns @brief  the list containing the defined attachments.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (bool) AttachmentsReversed
    ##  Returns @brief  the attachments reversed flag.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def AttachmentsReversed(self) -> bool:
        """
        Getter for property: (bool) AttachmentsReversed
         Returns @brief  the attachments reversed flag.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (bool) AttachmentsReversed

    ##  Returns @brief  the attachments reversed flag.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AttachmentsReversed.setter
    def AttachmentsReversed(self, attachmentsReversed: bool):
        """
        Setter for property: (bool) AttachmentsReversed
         Returns @brief  the attachments reversed flag.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Body
    ##  Returns @brief  the body.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def Body(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Body
         Returns @brief  the body.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Collisions
    ##  Returns @brief  the collision bodies.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Collisions(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Collisions
         Returns @brief  the collision bodies.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link FlexibleCableBuilder.ColorOptions NXOpen.AnimationDesigner.FlexibleCableBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FlexibleCableBuilder.ColorOptions
    @property
    def ColorOption(self) -> FlexibleCableBuilder.ColorOptions:
        """
        Getter for property: (@link FlexibleCableBuilder.ColorOptions NXOpen.AnimationDesigner.FlexibleCableBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Setter for property: (@link FlexibleCableBuilder.ColorOptions NXOpen.AnimationDesigner.FlexibleCableBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: FlexibleCableBuilder.ColorOptions):
        """
        Setter for property: (@link FlexibleCableBuilder.ColorOptions NXOpen.AnimationDesigner.FlexibleCableBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Curves
    ##  Returns @brief  the curves.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Curves(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Curves
         Returns @brief  the curves.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
    ##  Returns @brief  the diameter for circle section type.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Diameter
         Returns @brief  the diameter for circle section type.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link FlexibleCableBuilder.GeometryTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.GeometryTypes@endlink) GeometryType
    ##  Returns @brief  the geometry type.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FlexibleCableBuilder.GeometryTypes
    @property
    def GeometryType(self) -> FlexibleCableBuilder.GeometryTypes:
        """
        Getter for property: (@link FlexibleCableBuilder.GeometryTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.GeometryTypes@endlink) GeometryType
         Returns @brief  the geometry type.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link FlexibleCableBuilder.GeometryTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.GeometryTypes@endlink) GeometryType

    ##  Returns @brief  the geometry type.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @GeometryType.setter
    def GeometryType(self, geometryType: FlexibleCableBuilder.GeometryTypes):
        """
        Setter for property: (@link FlexibleCableBuilder.GeometryTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.GeometryTypes@endlink) GeometryType
         Returns @brief  the geometry type.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
    ##  Returns @brief  the length.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Length
         Returns @brief  the length.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link FlexibleMaterial NXOpen.AnimationDesigner.FlexibleMaterial@endlink) Material
    ##  Returns @brief  the material.  
    ##    This can be a @link NXOpen::AnimationDesigner::FlexibleMaterial NXOpen::AnimationDesigner::FlexibleMaterial@endlink .  
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FlexibleMaterial
    @property
    def Material(self) -> FlexibleMaterial:
        """
        Getter for property: (@link FlexibleMaterial NXOpen.AnimationDesigner.FlexibleMaterial@endlink) Material
         Returns @brief  the material.  
           This can be a @link NXOpen::AnimationDesigner::FlexibleMaterial NXOpen::AnimationDesigner::FlexibleMaterial@endlink .  
        
           
         
        """
        pass
    
    ## Setter for property: (@link FlexibleMaterial NXOpen.AnimationDesigner.FlexibleMaterial@endlink) Material

    ##  Returns @brief  the material.  
    ##    This can be a @link NXOpen::AnimationDesigner::FlexibleMaterial NXOpen::AnimationDesigner::FlexibleMaterial@endlink .  
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Material.setter
    def Material(self, material: FlexibleMaterial):
        """
        Setter for property: (@link FlexibleMaterial NXOpen.AnimationDesigner.FlexibleMaterial@endlink) Material
         Returns @brief  the material.  
           This can be a @link NXOpen::AnimationDesigner::FlexibleMaterial NXOpen::AnimationDesigner::FlexibleMaterial@endlink .  
        
           
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link FlexibleCableBuilder.SectionTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.SectionTypes@endlink) SectionType
    ##  Returns @brief  the section type.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return FlexibleCableBuilder.SectionTypes
    @property
    def SectionType(self) -> FlexibleCableBuilder.SectionTypes:
        """
        Getter for property: (@link FlexibleCableBuilder.SectionTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.SectionTypes@endlink) SectionType
         Returns @brief  the section type.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link FlexibleCableBuilder.SectionTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.SectionTypes@endlink) SectionType

    ##  Returns @brief  the section type.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SectionType.setter
    def SectionType(self, sectionType: FlexibleCableBuilder.SectionTypes):
        """
        Setter for property: (@link FlexibleCableBuilder.SectionTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.SectionTypes@endlink) SectionType
         Returns @brief  the section type.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
    ##  Returns @brief  the thickness for rectangle section type.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Thickness
         Returns @brief  the thickness for rectangle section type.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
    ##  Returns @brief  the width for rectangle section type.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Width
         Returns @brief  the width for rectangle section type.  
            
        
           
         
        """
        pass
    
    ##  @brief  Updates all attachment data if the curves or body are changed.  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curveOrBodyUpdated"> (bool) </param>
    def UpdateAttachmentData(self, curveOrBodyUpdated: bool) -> None:
        """
         @brief  Updates all attachment data if the curves or body are changed.  
        
         
        """
        pass
    
    ##  @brief  Updates the previewed cable facet body.  
    ## 
    ##  
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="points"> (@link NXOpen.Point3d List[NXOpen.Point3d]@endlink) </param>
    ## <param name="widthDirections"> (@link NXOpen.Vector3d List[NXOpen.Vector3d]@endlink) </param>
    ## <param name="radius"> (float) </param>
    ## <param name="width"> (float) </param>
    ## <param name="thickness"> (float) </param>
    def UpdatePreviewedCableFacet(self, points: List[NXOpen.Point3d], widthDirections: List[NXOpen.Vector3d], radius: float, width: float, thickness: float) -> None:
        """
         @brief  Updates the previewed cable facet body.  
        
         
        """
        pass
    
import NXOpen
##  @brief  Represents a collection of Flexible Cable object.  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class FlexibleCableCollection(NXOpen.TaggedObjectCollection): 
    """<summary> Represents a collection of Flexible Cable object. </summary>"""


    ##  @brief  Creates a @link NXOpen::AnimationDesigner::FlexibleCableAttachmentBuilder NXOpen::AnimationDesigner::FlexibleCableAttachmentBuilder@endlink .  
    ## 
    ##  
    ##  @return builder (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateFlexibleCableAttachmentBuilder(part: NXOpen.Part) -> FlexibleCableAttachmentBuilder:
        """
         @brief  Creates a @link NXOpen::AnimationDesigner::FlexibleCableAttachmentBuilder NXOpen::AnimationDesigner::FlexibleCableAttachmentBuilder@endlink .  
        
         
         @return builder (@link FlexibleCableAttachmentBuilder NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder@endlink): .
        """
        pass
    
    ##  @brief  Creates a @link NXOpen::AnimationDesigner::FlexibleCableBuilder NXOpen::AnimationDesigner::FlexibleCableBuilder@endlink .  
    ## 
    ##  
    ##  @return builder (@link FlexibleCableBuilder NXOpen.AnimationDesigner.FlexibleCableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="cable"> (@link FlexibleCable NXOpen.AnimationDesigner.FlexibleCable@endlink)  @link NXOpen::AnimationDesigner::FlexibleCable NXOpen::AnimationDesigner::FlexibleCable@endlink  to be edited, if NULL then create a new one </param>
    def CreateFlexibleCableBuilder(part: NXOpen.Part, cable: FlexibleCable) -> FlexibleCableBuilder:
        """
         @brief  Creates a @link NXOpen::AnimationDesigner::FlexibleCableBuilder NXOpen::AnimationDesigner::FlexibleCableBuilder@endlink .  
        
         
         @return builder (@link FlexibleCableBuilder NXOpen.AnimationDesigner.FlexibleCableBuilder@endlink): .
        """
        pass
    
    ##  @brief  Finds the @link  NXOpen::AnimationDesigner::FlexibleCable   NXOpen::AnimationDesigner::FlexibleCable @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name.  
    ## 
    ##  
    ##  @return cable (@link FlexibleCable NXOpen.AnimationDesigner.FlexibleCable@endlink):  @link  NXOpen::AnimationDesigner::FlexibleCable   NXOpen::AnimationDesigner::FlexibleCable @endlink  with this name. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::FlexibleCable   NXOpen::AnimationDesigner::FlexibleCable @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> FlexibleCable:
        """
         @brief  Finds the @link  NXOpen::AnimationDesigner::FlexibleCable   NXOpen::AnimationDesigner::FlexibleCable @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name.  
        
         
         @return cable (@link FlexibleCable NXOpen.AnimationDesigner.FlexibleCable@endlink):  @link  NXOpen::AnimationDesigner::FlexibleCable   NXOpen::AnimationDesigner::FlexibleCable @endlink  with this name. .
        """
        pass
    
import NXOpen
##  @brief  Represents a Flexible Cable feature.  
## 
##   <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::FlexibleCableBuilder  NXOpen::AnimationDesigner::FlexibleCableBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class FlexibleCable(NXOpen.DisplayableObject): 
    """<summary> Represents a Flexible Cable feature. </summary>"""
    pass


import NXOpen
##  @brief  Represents a @link NXOpen::AnimationDesigner::FlexibleMaterialBuilder NXOpen::AnimationDesigner::FlexibleMaterialBuilder@endlink .  
## 
##   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::FlexibleMaterialCollection::CreateFlexibleMaterialBuilder  NXOpen::AnimationDesigner::FlexibleMaterialCollection::CreateFlexibleMaterialBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class FlexibleMaterialBuilder(NXOpen.Builder): 
    """<summary> Represents a <ja_class>NXOpen.AnimationDesigner.FlexibleMaterialBuilder</ja_class>. </summary>"""


    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Density
    ##  Returns @brief  the density.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Density(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Density
         Returns @brief  the density.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (bool) EnableMaxContactForce
    ##  Returns @brief  the option determines whether to set the maximum contact force.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def EnableMaxContactForce(self) -> bool:
        """
        Getter for property: (bool) EnableMaxContactForce
         Returns @brief  the option determines whether to set the maximum contact force.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (bool) EnableMaxContactForce

    ##  Returns @brief  the option determines whether to set the maximum contact force.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnableMaxContactForce.setter
    def EnableMaxContactForce(self, enableMaxContactForce: bool):
        """
        Setter for property: (bool) EnableMaxContactForce
         Returns @brief  the option determines whether to set the maximum contact force.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (bool) EnableMaxTwist
    ##  Returns @brief  the option determines whether to set the maximum twist.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def EnableMaxTwist(self) -> bool:
        """
        Getter for property: (bool) EnableMaxTwist
         Returns @brief  the option determines whether to set the maximum twist.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (bool) EnableMaxTwist

    ##  Returns @brief  the option determines whether to set the maximum twist.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnableMaxTwist.setter
    def EnableMaxTwist(self, enableMaxTwist: bool):
        """
        Setter for property: (bool) EnableMaxTwist
         Returns @brief  the option determines whether to set the maximum twist.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (bool) EnableMinCurvature
    ##  Returns @brief  the option determines whether to set the minimum curvature.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def EnableMinCurvature(self) -> bool:
        """
        Getter for property: (bool) EnableMinCurvature
         Returns @brief  the option determines whether to set the minimum curvature.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (bool) EnableMinCurvature

    ##  Returns @brief  the option determines whether to set the minimum curvature.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @EnableMinCurvature.setter
    def EnableMinCurvature(self, enableMinCurvature: bool):
        """
        Setter for property: (bool) EnableMinCurvature
         Returns @brief  the option determines whether to set the minimum curvature.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FulcrumLength
    ##  Returns @brief  the fulcrum length.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FulcrumLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FulcrumLength
         Returns @brief  the fulcrum length.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxContactForce
    ##  Returns @brief  the maximum contact force.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxContactForce(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxContactForce
         Returns @brief  the maximum contact force.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxTension
    ##  Returns @brief  the maximum tension.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxTension(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxTension
         Returns @brief  the maximum tension.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxTwist
    ##  Returns @brief  the maximum twist.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxTwist(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxTwist
         Returns @brief  the maximum twist.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinCurvature
    ##  Returns @brief  the minimum curvature.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinCurvature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinCurvature
         Returns @brief  the minimum curvature.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns @brief  the name.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns @brief  the name.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (float) Oscillation
    ##  Returns @brief  the oscillation.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def Oscillation(self) -> float:
        """
        Getter for property: (float) Oscillation
         Returns @brief  the oscillation.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (float) Oscillation

    ##  Returns @brief  the oscillation.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Oscillation.setter
    def Oscillation(self, oscillation: float):
        """
        Setter for property: (float) Oscillation
         Returns @brief  the oscillation.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YoungModulus
    ##  Returns @brief  the Young's modulus.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YoungModulus(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YoungModulus
         Returns @brief  the Young's modulus.  
            
        
           
         
        """
        pass
    
import NXOpen
##  @brief  Represents a collection of Flexible Material object.  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class FlexibleMaterialCollection(NXOpen.TaggedObjectCollection): 
    """<summary> Represents a collection of Flexible Material object. </summary>"""


    ##  @brief  Creates a @link NXOpen::AnimationDesigner::FlexibleMaterialBuilder NXOpen::AnimationDesigner::FlexibleMaterialBuilder@endlink .  
    ## 
    ##  
    ##  @return builder (@link FlexibleMaterialBuilder NXOpen.AnimationDesigner.FlexibleMaterialBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="material"> (@link FlexibleMaterial NXOpen.AnimationDesigner.FlexibleMaterial@endlink)  @link NXOpen::AnimationDesigner::FlexibleMaterial NXOpen::AnimationDesigner::FlexibleMaterial@endlink  to be edited, if NULL then create a new one </param>
    def CreateFlexibleMaterialBuilder(part: NXOpen.Part, material: FlexibleMaterial) -> FlexibleMaterialBuilder:
        """
         @brief  Creates a @link NXOpen::AnimationDesigner::FlexibleMaterialBuilder NXOpen::AnimationDesigner::FlexibleMaterialBuilder@endlink .  
        
         
         @return builder (@link FlexibleMaterialBuilder NXOpen.AnimationDesigner.FlexibleMaterialBuilder@endlink): .
        """
        pass
    
    ##  @brief  Finds the @link  NXOpen::AnimationDesigner::FlexibleMaterial   NXOpen::AnimationDesigner::FlexibleMaterial @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name.  
    ## 
    ##  
    ##  @return material (@link FlexibleMaterial NXOpen.AnimationDesigner.FlexibleMaterial@endlink):  @link  NXOpen::AnimationDesigner::FlexibleMaterial   NXOpen::AnimationDesigner::FlexibleMaterial @endlink  with this name. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::FlexibleMaterial   NXOpen::AnimationDesigner::FlexibleMaterial @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> FlexibleMaterial:
        """
         @brief  Finds the @link  NXOpen::AnimationDesigner::FlexibleMaterial   NXOpen::AnimationDesigner::FlexibleMaterial @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name.  
        
         
         @return material (@link FlexibleMaterial NXOpen.AnimationDesigner.FlexibleMaterial@endlink):  @link  NXOpen::AnimationDesigner::FlexibleMaterial   NXOpen::AnimationDesigner::FlexibleMaterial @endlink  with this name. .
        """
        pass
    
import NXOpen
##  @brief  Represents a Flexible Material feature.  
## 
##   <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::FlexibleMaterialBuilder  NXOpen::AnimationDesigner::FlexibleMaterialBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class FlexibleMaterial(NXOpen.DisplayableObject): 
    """<summary> Represents a Flexible Material feature. </summary>"""
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::GearBuilder NXOpen::AnimationDesigner::GearBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::GearCollection::CreateGearBuilder  NXOpen::AnimationDesigner::GearCollection::CreateGearBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class GearBuilder(CouplerBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.GearBuilder</ja_class>. """


    ##  Definitions of gear type  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## General</term><description> 
    ## general gear</description> </item><item><term> 
    ## Chainbelt</term><description> 
    ## chain belt</description> </item><item><term> 
    ## Cable</term><description> 
    ## cable</description> </item></list>
    class GearType(Enum):
        """
        Members Include: <General> <Chainbelt> <Cable>
        """
        General: int
        Chainbelt: int
        Cable: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> GearBuilder.GearType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) ChangeDirection
    ##  Returns the inner gear option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def ChangeDirection(self) -> bool:
        """
        Getter for property: (bool) ChangeDirection
         Returns the inner gear option.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ChangeDirection

    ##  Returns the inner gear option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ChangeDirection.setter
    def ChangeDirection(self, change: bool):
        """
        Setter for property: (bool) ChangeDirection
         Returns the inner gear option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpressionRatio
    ##  Returns the ratio expression.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ExpressionRatio(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpressionRatio
         Returns the ratio expression.  
             
         
        """
        pass
    
    ## Getter for property: (@link GearBuilder.GearType NXOpen.AnimationDesigner.GearBuilder.GearType@endlink) UseType
    ##  Returns the gear type.  
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return GearBuilder.GearType
    @property
    def UseType(self) -> GearBuilder.GearType:
        """
        Getter for property: (@link GearBuilder.GearType NXOpen.AnimationDesigner.GearBuilder.GearType@endlink) UseType
         Returns the gear type.  
            
         
        """
        pass
    
    ## Setter for property: (@link GearBuilder.GearType NXOpen.AnimationDesigner.GearBuilder.GearType@endlink) UseType

    ##  Returns the gear type.  
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseType.setter
    def UseType(self, useType: GearBuilder.GearType):
        """
        Setter for property: (@link GearBuilder.GearType NXOpen.AnimationDesigner.GearBuilder.GearType@endlink) UseType
         Returns the gear type.  
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Gear objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class GearCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Gear objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::GearBuilder NXOpen::AnimationDesigner::GearBuilder@endlink . 
    ##  @return builder (@link GearBuilder NXOpen.AnimationDesigner.GearBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="gear"> (@link Gear NXOpen.AnimationDesigner.Gear@endlink)  @link NXOpen::AnimationDesigner::Gear NXOpen::AnimationDesigner::Gear@endlink  to be edited, if NULL then create a new one </param>
    def CreateGearBuilder(part: NXOpen.Part, gear: Gear) -> GearBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::GearBuilder NXOpen::AnimationDesigner::GearBuilder@endlink . 
         @return builder (@link GearBuilder NXOpen.AnimationDesigner.GearBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::Gear   NXOpen::AnimationDesigner::Gear @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return gear (@link Gear NXOpen.AnimationDesigner.Gear@endlink):  @link  NXOpen::AnimationDesigner::Gear   NXOpen::AnimationDesigner::Gear @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::Gear   NXOpen::AnimationDesigner::Gear @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> Gear:
        """
         Finds the @link  NXOpen::AnimationDesigner::Gear   NXOpen::AnimationDesigner::Gear @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return gear (@link Gear NXOpen.AnimationDesigner.Gear@endlink):  @link  NXOpen::AnimationDesigner::Gear   NXOpen::AnimationDesigner::Gear @endlink  with this name. .
        """
        pass
    
##  Represents a Gear feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::GearBuilder  NXOpen::AnimationDesigner::GearBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Gear(Coupler): 
    """ Represents a Gear feature. """
    pass


import NXOpen
import NXOpen.Mechatronics
##  Represents a @link AnimationDesigner::InverseKinematicsBuilder AnimationDesigner::InverseKinematicsBuilder@endlink   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::InverseKinematicsCollection::CreateInverseKinematicsBuilder  NXOpen::AnimationDesigner::InverseKinematicsCollection::CreateInverseKinematicsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class InverseKinematicsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>AnimationDesigner.InverseKinematicsBuilder</ja_class> """


    ##  the inverse kinematics vector alignment types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ##  align aLL vector.</description> </item><item><term> 
    ## Z</term><description> 
    ##  align z vector.</description> </item><item><term> 
    ## Y</term><description> 
    ##  align y vector.</description> </item><item><term> 
    ## X</term><description> 
    ##  align x vector.</description> </item><item><term> 
    ## NotSet</term><description> 
    ##  no vector alignment.</description> </item></list>
    class AlignTypes(Enum):
        """
        Members Include: <All> <Z> <Y> <X> <NotSet>
        """
        All: int
        Z: int
        Y: int
        X: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InverseKinematicsBuilder.AlignTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the inverse kinematics body types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## OneBody</term><description> 
    ##  one kinematics chain.</description> </item><item><term> 
    ## TwoBodies</term><description> 
    ##  two kinematics chain.</description> </item></list>
    class BodyTypes(Enum):
        """
        Members Include: <OneBody> <TwoBodies>
        """
        OneBody: int
        TwoBodies: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InverseKinematicsBuilder.BodyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Specifies the result of the inverse kinematics solver. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Success</term><description> 
    ##  Successfully solved. </description> </item><item><term> 
    ## NotSolved</term><description> 
    ##  Could not solve due to error. </description> </item><item><term> 
    ## Approximate</term><description> 
    ##  The target is not reachable, closest solution is returned. </description> </item><item><term> 
    ## Limits</term><description> 
    ##  The target is not reachable due to limits, closest solution is returned. </description> </item><item><term> 
    ## ReachError</term><description> 
    ##  A reach error occurs. </description> </item><item><term> 
    ## Timeout</term><description> 
    ##  A timeout error occurs due to collision avoidance. </description> </item><item><term> 
    ## CollisionTarget</term><description> 
    ##  The target pose is colliding. </description> </item><item><term> 
    ## CollisionStart</term><description> 
    ##  The start pose is colliding. </description> </item><item><term> 
    ## Limit</term><description> 
    ##  Cannot move toward the target due to limits. </description> </item><item><term> 
    ## TargetEqualsStart</term><description> 
    ##  It is not possible to go closer to the target due to the kinematics. </description> </item><item><term> 
    ## Unknown</term><description> 
    ##  An unknown error occurs in the inverse kinematics solver. </description> </item></list>
    class Result(Enum):
        """
        Members Include: <Success> <NotSolved> <Approximate> <Limits> <ReachError> <Timeout> <CollisionTarget> <CollisionStart> <Limit> <TargetEqualsStart> <Unknown>
        """
        Success: int
        NotSolved: int
        Approximate: int
        Limits: int
        ReachError: int
        Timeout: int
        CollisionTarget: int
        CollisionStart: int
        Limit: int
        TargetEqualsStart: int
        Unknown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> InverseKinematicsBuilder.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link InverseKinematicsBuilder.AlignTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.AlignTypes@endlink) AlignType
    ##  Returns the option of align type for two bodies type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return InverseKinematicsBuilder.AlignTypes
    @property
    def AlignType(self) -> InverseKinematicsBuilder.AlignTypes:
        """
        Getter for property: (@link InverseKinematicsBuilder.AlignTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.AlignTypes@endlink) AlignType
         Returns the option of align type for two bodies type.  
             
         
        """
        pass
    
    ## Setter for property: (@link InverseKinematicsBuilder.AlignTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.AlignTypes@endlink) AlignType

    ##  Returns the option of align type for two bodies type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @AlignType.setter
    def AlignType(self, alignType: InverseKinematicsBuilder.AlignTypes):
        """
        Setter for property: (@link InverseKinematicsBuilder.AlignTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.AlignTypes@endlink) AlignType
         Returns the option of align type for two bodies type.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AvoidCollision
    ##  Returns the option of avoiding collision.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def AvoidCollision(self) -> bool:
        """
        Getter for property: (bool) AvoidCollision
         Returns the option of avoiding collision.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AvoidCollision

    ##  Returns the option of avoiding collision.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @AvoidCollision.setter
    def AvoidCollision(self, avoidCollision: bool):
        """
        Setter for property: (bool) AvoidCollision
         Returns the option of avoiding collision.  
             
         
        """
        pass
    
    ## Getter for property: (@link InverseKinematicsBuilder.BodyTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.BodyTypes@endlink) BodyType
    ##  Returns the type   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return InverseKinematicsBuilder.BodyTypes
    @property
    def BodyType(self) -> InverseKinematicsBuilder.BodyTypes:
        """
        Getter for property: (@link InverseKinematicsBuilder.BodyTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.BodyTypes@endlink) BodyType
         Returns the type   
            
         
        """
        pass
    
    ## Setter for property: (@link InverseKinematicsBuilder.BodyTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.BodyTypes@endlink) BodyType

    ##  Returns the type   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @BodyType.setter
    def BodyType(self, type: InverseKinematicsBuilder.BodyTypes):
        """
        Setter for property: (@link InverseKinematicsBuilder.BodyTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.BodyTypes@endlink) BodyType
         Returns the type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Mechatronics.Convention NXOpen.Mechatronics.Convention@endlink) EulerAngleConvention
    ##  Returns the Euler angle convention.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Mechatronics.Convention
    @property
    def EulerAngleConvention(self) -> NXOpen.Mechatronics.Convention:
        """
        Getter for property: (@link NXOpen.Mechatronics.Convention NXOpen.Mechatronics.Convention@endlink) EulerAngleConvention
         Returns the Euler angle convention.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Mechatronics.Convention NXOpen.Mechatronics.Convention@endlink) EulerAngleConvention

    ##  Returns the Euler angle convention.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @EulerAngleConvention.setter
    def EulerAngleConvention(self, type: NXOpen.Mechatronics.Convention):
        """
        Setter for property: (@link NXOpen.Mechatronics.Convention NXOpen.Mechatronics.Convention@endlink) EulerAngleConvention
         Returns the Euler angle convention.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstPoint
    ##  Returns the first point for two bodies type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def FirstPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstPoint
         Returns the first point for two bodies type.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstPoint

    ##  Returns the first point for two bodies type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FirstPoint.setter
    def FirstPoint(self, firstPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) FirstPoint
         Returns the first point for two bodies type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) FirstRigidGroup
    ##  Returns the first rigid group for two bodies type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def FirstRigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) FirstRigidGroup
         Returns the first rigid group for two bodies type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Mechatronics.FrameBuilderList NXOpen.Mechatronics.FrameBuilderList@endlink) FrameList
    ##  Returns the list containing the defined frames.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Mechatronics.FrameBuilderList
    @property
    def FrameList(self) -> NXOpen.Mechatronics.FrameBuilderList:
        """
        Getter for property: (@link NXOpen.Mechatronics.FrameBuilderList NXOpen.Mechatronics.FrameBuilderList@endlink) FrameList
         Returns the list containing the defined frames.  
             
         
        """
        pass
    
    ## Getter for property: (bool) GenerateTracer
    ##  Returns the option of generating tracer object.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def GenerateTracer(self) -> bool:
        """
        Getter for property: (bool) GenerateTracer
         Returns the option of generating tracer object.  
             
         
        """
        pass
    
    ## Setter for property: (bool) GenerateTracer

    ##  Returns the option of generating tracer object.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @GenerateTracer.setter
    def GenerateTracer(self, bTracer: bool):
        """
        Setter for property: (bool) GenerateTracer
         Returns the option of generating tracer object.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PointTolerance
    ##  Returns the tolerance of point alignment for two bodies type  
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PointTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PointTolerance
         Returns the tolerance of point alignment for two bodies type  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) RigidGroup
    ##  Returns the rigid group.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def RigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) RigidGroup
         Returns the rigid group.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondPoint
    ##  Returns the second point for two bodies type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def SecondPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondPoint
         Returns the second point for two bodies type.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondPoint

    ##  Returns the second point for two bodies type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @SecondPoint.setter
    def SecondPoint(self, secondPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SecondPoint
         Returns the second point for two bodies type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SecondRigidGroup
    ##  Returns the second rigid group for two bodies type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def SecondRigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SecondRigidGroup
         Returns the second rigid group for two bodies type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint
    ##  Returns the start point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint
         Returns the start point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint

    ##  Returns the start point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) StartPoint
         Returns the start point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TargetPoint
    ##  Returns the target point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Please use @link NXOpen::AnimationDesigner::InverseKinematicsBuilder::FrameList NXOpen::AnimationDesigner::InverseKinematicsBuilder::FrameList@endlink  instead.  <br> 

    ## @return NXOpen.Point
    @property
    def TargetPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) TargetPoint
         Returns the target point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TargetPoint

    ##  Returns the target point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Please use @link NXOpen::AnimationDesigner::InverseKinematicsBuilder::FrameList NXOpen::AnimationDesigner::InverseKinematicsBuilder::FrameList@endlink  instead.  <br> 

    @TargetPoint.setter
    def TargetPoint(self, targetPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) TargetPoint
         Returns the target point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VectorTolerance
    ##  Returns the tolerance of vector alignment for two bodies type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def VectorTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) VectorTolerance
         Returns the tolerance of vector alignment for two bodies type.  
             
         
        """
        pass
    
    ##  Returns the pose that encounters error. 
    ##  @return pose (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetErrorPose(self) -> NXOpen.CoordinateSystem:
        """
         Returns the pose that encounters error. 
         @return pose (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink): .
        """
        pass
    
    ##  Gets the first point orientations for two bodies type. 
    ##  @return startOrit (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The first orientation matrix. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetFirstPointOrientation(self) -> NXOpen.Matrix3x3:
        """
         Gets the first point orientations for two bodies type. 
         @return startOrit (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The first orientation matrix. .
        """
        pass
    
    ##  Gets the orientations. 
    ##  @return A tuple consisting of (startOrit, targetOrit). 
    ##  - startOrit is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink. The start orientation matrix. .
    ##  - targetOrit is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink. The target orientation matrix. .

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Please use @link NXOpen::AnimationDesigner::InverseKinematicsBuilder::GetStartPointOrientation NXOpen::AnimationDesigner::InverseKinematicsBuilder::GetStartPointOrientation@endlink  instead  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetOrientation(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Matrix3x3]:
        """
         Gets the orientations. 
         @return A tuple consisting of (startOrit, targetOrit). 
         - startOrit is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink. The start orientation matrix. .
         - targetOrit is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink. The target orientation matrix. .

        """
        pass
    
    ##  Returns the solver result. 
    ##  @return result (@link InverseKinematicsBuilder.Result NXOpen.AnimationDesigner.InverseKinematicsBuilder.Result@endlink):  The result of the inverse kinematics solver .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetResult(self) -> InverseKinematicsBuilder.Result:
        """
         Returns the solver result. 
         @return result (@link InverseKinematicsBuilder.Result NXOpen.AnimationDesigner.InverseKinematicsBuilder.Result@endlink):  The result of the inverse kinematics solver .
        """
        pass
    
    ##  Gets the second point orientations for two bodies type. 
    ##  @return startOrit (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The second orientation matrix. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetSecondPointOrientation(self) -> NXOpen.Matrix3x3:
        """
         Gets the second point orientations for two bodies type. 
         @return startOrit (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The second orientation matrix. .
        """
        pass
    
    ##  Gets the start point orientations. 
    ##  @return startOrit (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The start orientation matrix. .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetStartPointOrientation(self) -> NXOpen.Matrix3x3:
        """
         Gets the start point orientations. 
         @return startOrit (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink):  The start orientation matrix. .
        """
        pass
    
    ##  Sets the first point orientations for two bodies type. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="startOrit"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink)  The first orientation matrix. </param>
    def SetFirstPointOrientation(self, startOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the first point orientations for two bodies type. 
        """
        pass
    
    ##  Sets the orientations. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX1926.0.0.  Please use @link NXOpen::AnimationDesigner::InverseKinematicsBuilder::SetStartPointOrientation NXOpen::AnimationDesigner::InverseKinematicsBuilder::SetStartPointOrientation@endlink  instead  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="startOrit"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink)  The start orientation matrix. </param>
    ## <param name="targetOrit"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink)  The target orientation matrix. </param>
    def SetOrientation(self, startOrit: NXOpen.Matrix3x3, targetOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the orientations. 
        """
        pass
    
    ##  Sets the second point orientations for two bodies type. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="startOrit"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink)  The second orientation matrix. </param>
    def SetSecondPointOrientation(self, startOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the second point orientations for two bodies type. 
        """
        pass
    
    ##  Sets the start point orientations. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="startOrit"> (@link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink)  The start orientation matrix. </param>
    def SetStartPointOrientation(self, startOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the start point orientations. 
        """
        pass
    
    ##  Update IK object. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def UpdateIk(self) -> None:
        """
         Update IK object. 
        """
        pass
    
    ##  Update IK status to out of date. 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def UpdateIkStatus(self) -> None:
        """
         Update IK status to out of date. 
        """
        pass
    
import NXOpen
##  Represents a collection of Inverse Kinematics.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class InverseKinematicsCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Inverse Kinematics. """


    ##  Creates a @link NXOpen::AnimationDesigner::InverseKinematicsBuilder NXOpen::AnimationDesigner::InverseKinematicsBuilder@endlink . 
    ##  @return builder (@link InverseKinematicsBuilder NXOpen.AnimationDesigner.InverseKinematicsBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="inverseKinematics"> (@link InverseKinematics NXOpen.AnimationDesigner.InverseKinematics@endlink)  @link NXOpen::AnimationDesigner::InverseKinematics NXOpen::AnimationDesigner::InverseKinematics@endlink  to be edited, if NULL then create a new one </param>
    def CreateInverseKinematicsBuilder(part: NXOpen.Part, inverseKinematics: InverseKinematics) -> InverseKinematicsBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::InverseKinematicsBuilder NXOpen::AnimationDesigner::InverseKinematicsBuilder@endlink . 
         @return builder (@link InverseKinematicsBuilder NXOpen.AnimationDesigner.InverseKinematicsBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::InverseKinematics   NXOpen::AnimationDesigner::InverseKinematics @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return inverseKinematics (@link InverseKinematics NXOpen.AnimationDesigner.InverseKinematics@endlink):  @link  NXOpen::AnimationDesigner::InverseKinematics   NXOpen::AnimationDesigner::InverseKinematics @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::InverseKinematics   NXOpen::AnimationDesigner::InverseKinematics @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> InverseKinematics:
        """
         Finds the @link  NXOpen::AnimationDesigner::InverseKinematics   NXOpen::AnimationDesigner::InverseKinematics @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return inverseKinematics (@link InverseKinematics NXOpen.AnimationDesigner.InverseKinematics@endlink):  @link  NXOpen::AnimationDesigner::InverseKinematics   NXOpen::AnimationDesigner::InverseKinematics @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents the Inverse Kinematics class. It defines the configuration of inverse kinematics in a mechanism.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::InverseKinematicsBuilder  NXOpen::AnimationDesigner::InverseKinematicsBuilder @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class InverseKinematics(NXOpen.DisplayableObject): 
    """ Represents the Inverse Kinematics class. It defines the configuration of inverse kinematics in a mechanism. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::JointJoggerBuilder NXOpen::AnimationDesigner::JointJoggerBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::JointJoggerCollection::CreateJointJoggerBuilder  NXOpen::AnimationDesigner::JointJoggerCollection::CreateJointJoggerBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class JointJoggerBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.JointJoggerBuilder</ja_class>. """


    ## Getter for property: (bool) CaptureArrangement
    ##  Returns the capture arrangement option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def CaptureArrangement(self) -> bool:
        """
        Getter for property: (bool) CaptureArrangement
         Returns the capture arrangement option.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CaptureArrangement

    ##  Returns the capture arrangement option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CaptureArrangement.setter
    def CaptureArrangement(self, captureArrangement: bool):
        """
        Setter for property: (bool) CaptureArrangement
         Returns the capture arrangement option.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ##  Adds the joint data. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="joint"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  RevoluteJoint or SliderJoint or CylindricalJoint or ScrewJoint </param>
    def AddJointData(self, joint: NXOpen.NXObject) -> None:
        """
         Adds the joint data. 
        """
        pass
    
    ##  Edits the joint angle. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="joint"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  RevoluteJoint or CylindricalJoint </param>
    ## <param name="angleValue"> (float) </param>
    def EditJointAngle(self, joint: NXOpen.NXObject, angleValue: float) -> None:
        """
         Edits the joint angle. 
        """
        pass
    
    ##  Edits the joint distance. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="joint"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  SliderJoint or CylindricalJoint or ScrewJoint </param>
    ## <param name="distanceValue"> (float) </param>
    def EditJointDistance(self, joint: NXOpen.NXObject, distanceValue: float) -> None:
        """
         Edits the joint distance. 
        """
        pass
    
    ##  Removes the joint data. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="joint"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  RevoluteJoint or SliderJoint or CylindricalJoint or ScrewJoint </param>
    def RemoveJointData(self, joint: NXOpen.NXObject) -> None:
        """
         Removes the joint data. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a collection of Joint Jogger objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class JointJoggerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Joint Jogger objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::JointJoggerBuilder NXOpen::AnimationDesigner::JointJoggerBuilder@endlink . 
    ##  @return builder (@link JointJoggerBuilder NXOpen.AnimationDesigner.JointJoggerBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="jointJogger"> (@link JointJogger NXOpen.AnimationDesigner.JointJogger@endlink)  @link NXOpen::AnimationDesigner::JointJogger NXOpen::AnimationDesigner::JointJogger@endlink  to be edited, if NULL then create a new one </param>
    @overload
    def CreateJointJoggerBuilder(part: NXOpen.Part, jointJogger: JointJogger) -> JointJoggerBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::JointJoggerBuilder NXOpen::AnimationDesigner::JointJoggerBuilder@endlink . 
         @return builder (@link JointJoggerBuilder NXOpen.AnimationDesigner.JointJoggerBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::AnimationDesigner::JointJoggerBuilder NXOpen::AnimationDesigner::JointJoggerBuilder@endlink . 
    ##  @return builder (@link JointJoggerBuilder NXOpen.AnimationDesigner.JointJoggerBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="jointJogger"> (@link JointJogger NXOpen.AnimationDesigner.JointJogger@endlink)  @link NXOpen::AnimationDesigner::JointJogger NXOpen::AnimationDesigner::JointJogger@endlink  to be edited, if NULL then create a new one </param>
    ## <param name="partOcc"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  for the edited joint jogger occurrence </param>
    @overload
    def CreateJointJoggerBuilder(part: NXOpen.Part, jointJogger: JointJogger, partOcc: NXOpen.Assemblies.Component) -> JointJoggerBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::JointJoggerBuilder NXOpen::AnimationDesigner::JointJoggerBuilder@endlink . 
         @return builder (@link JointJoggerBuilder NXOpen.AnimationDesigner.JointJoggerBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::JointJogger   NXOpen::AnimationDesigner::JointJogger @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return jointJogger (@link JointJogger NXOpen.AnimationDesigner.JointJogger@endlink):  @link  NXOpen::AnimationDesigner::JointJogger   NXOpen::AnimationDesigner::JointJogger @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::JointJogger   NXOpen::AnimationDesigner::JointJogger @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> JointJogger:
        """
         Finds the @link  NXOpen::AnimationDesigner::JointJogger   NXOpen::AnimationDesigner::JointJogger @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return jointJogger (@link JointJogger NXOpen.AnimationDesigner.JointJogger@endlink):  @link  NXOpen::AnimationDesigner::JointJogger   NXOpen::AnimationDesigner::JointJogger @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a Joint Jogger feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::JointJoggerBuilder  NXOpen::AnimationDesigner::JointJoggerBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class JointJogger(NXOpen.DisplayableObject): 
    """ Represents a Joint Jogger feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::MeasureBuilder NXOpen::AnimationDesigner::MeasureBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::MeasureCollection::CreateMeasureBuilder  NXOpen::AnimationDesigner::MeasureCollection::CreateMeasureBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MeasureBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.MeasureBuilder</ja_class>. """


    ##  the measure types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Distance</term><description> 
    ## </description> </item><item><term> 
    ## Angle</term><description> 
    ## </description> </item><item><term> 
    ## MotorParameter</term><description> 
    ## </description> </item></list>
    class MeasureTypes(Enum):
        """
        Members Include: <Distance> <Angle> <MotorParameter>
        """
        Distance: int
        Angle: int
        MotorParameter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeasureBuilder.MeasureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the motor parameter types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Displacement</term><description> 
    ## </description> </item><item><term> 
    ## Velocity</term><description> 
    ## </description> </item><item><term> 
    ## Acceleration</term><description> 
    ## </description> </item></list>
    class MotorParameterTypes(Enum):
        """
        Members Include: <Displacement> <Velocity> <Acceleration>
        """
        Displacement: int
        Velocity: int
        Acceleration: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MeasureBuilder.MotorParameterTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction1
    ##  Returns the first direction used to measure the angle with the second direction.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Direction1(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction1
         Returns the first direction used to measure the angle with the second direction.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction1

    ##  Returns the first direction used to measure the angle with the second direction.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Direction1.setter
    def Direction1(self, direction1: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction1
         Returns the first direction used to measure the angle with the second direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction2
    ##  Returns the second direction used to measure the angle with the first direction.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Direction2(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction2
         Returns the second direction used to measure the angle with the first direction.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction2

    ##  Returns the second direction used to measure the angle with the first direction.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Direction2.setter
    def Direction2(self, direction2: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Direction2
         Returns the second direction used to measure the angle with the first direction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) List1
    ##  Returns the first object list used to be measured with the second object list.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def List1(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) List1
         Returns the first object list used to be measured with the second object list.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) List2
    ##  Returns the second object list used to be measured with the first object list.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def List2(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) List2
         Returns the second object list used to be measured with the first object list.  
             
         
        """
        pass
    
    ## Getter for property: (@link MeasureBuilder.MeasureTypes NXOpen.AnimationDesigner.MeasureBuilder.MeasureTypes@endlink) MeasureType
    ##  Returns the measure type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return MeasureBuilder.MeasureTypes
    @property
    def MeasureType(self) -> MeasureBuilder.MeasureTypes:
        """
        Getter for property: (@link MeasureBuilder.MeasureTypes NXOpen.AnimationDesigner.MeasureBuilder.MeasureTypes@endlink) MeasureType
         Returns the measure type.  
             
         
        """
        pass
    
    ## Setter for property: (@link MeasureBuilder.MeasureTypes NXOpen.AnimationDesigner.MeasureBuilder.MeasureTypes@endlink) MeasureType

    ##  Returns the measure type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MeasureType.setter
    def MeasureType(self, measureType: MeasureBuilder.MeasureTypes):
        """
        Setter for property: (@link MeasureBuilder.MeasureTypes NXOpen.AnimationDesigner.MeasureBuilder.MeasureTypes@endlink) MeasureType
         Returns the measure type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Motor
    ##  Returns the motor.  
    ##    This can be a @link NXOpen::AnimationDesigner::SpeedMotor NXOpen::AnimationDesigner::SpeedMotor@endlink 
    ##             or @link NXOpen::AnimationDesigner::PositionMotor NXOpen::AnimationDesigner::PositionMotor@endlink .   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def Motor(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Motor
         Returns the motor.  
           This can be a @link NXOpen::AnimationDesigner::SpeedMotor NXOpen::AnimationDesigner::SpeedMotor@endlink 
                    or @link NXOpen::AnimationDesigner::PositionMotor NXOpen::AnimationDesigner::PositionMotor@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link MeasureBuilder.MotorParameterTypes NXOpen.AnimationDesigner.MeasureBuilder.MotorParameterTypes@endlink) MotorParameterType
    ##  Returns the motor parameter type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return MeasureBuilder.MotorParameterTypes
    @property
    def MotorParameterType(self) -> MeasureBuilder.MotorParameterTypes:
        """
        Getter for property: (@link MeasureBuilder.MotorParameterTypes NXOpen.AnimationDesigner.MeasureBuilder.MotorParameterTypes@endlink) MotorParameterType
         Returns the motor parameter type.  
             
         
        """
        pass
    
    ## Setter for property: (@link MeasureBuilder.MotorParameterTypes NXOpen.AnimationDesigner.MeasureBuilder.MotorParameterTypes@endlink) MotorParameterType

    ##  Returns the motor parameter type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MotorParameterType.setter
    def MotorParameterType(self, motorParameterType: MeasureBuilder.MotorParameterTypes):
        """
        Setter for property: (@link MeasureBuilder.MotorParameterTypes NXOpen.AnimationDesigner.MeasureBuilder.MotorParameterTypes@endlink) MotorParameterType
         Returns the motor parameter type.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseVector
    ##  Returns the use vector flag.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def UseVector(self) -> bool:
        """
        Getter for property: (bool) UseVector
         Returns the use vector flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseVector

    ##  Returns the use vector flag.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @UseVector.setter
    def UseVector(self, useVector: bool):
        """
        Setter for property: (bool) UseVector
         Returns the use vector flag.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the vector.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the vector.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector.  
             
         
        """
        pass
    
import NXOpen
##  Represents a collection of Measure objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MeasureCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Measure objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::MeasureBuilder NXOpen::AnimationDesigner::MeasureBuilder@endlink . 
    ##  @return builder (@link MeasureBuilder NXOpen.AnimationDesigner.MeasureBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="measure"> (@link Measure NXOpen.AnimationDesigner.Measure@endlink)  @link NXOpen::AnimationDesigner::Measure NXOpen::AnimationDesigner::Measure@endlink  to be edited, if NULL then create a new one </param>
    def CreateMeasureBuilder(part: NXOpen.Part, measure: Measure) -> MeasureBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::MeasureBuilder NXOpen::AnimationDesigner::MeasureBuilder@endlink . 
         @return builder (@link MeasureBuilder NXOpen.AnimationDesigner.MeasureBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::Measure   NXOpen::AnimationDesigner::Measure @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return measure (@link Measure NXOpen.AnimationDesigner.Measure@endlink):  @link  NXOpen::AnimationDesigner::Measure   NXOpen::AnimationDesigner::Measure @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::Measure   NXOpen::AnimationDesigner::Measure @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> Measure:
        """
         Finds the @link  NXOpen::AnimationDesigner::Measure   NXOpen::AnimationDesigner::Measure @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return measure (@link Measure NXOpen.AnimationDesigner.Measure@endlink):  @link  NXOpen::AnimationDesigner::Measure   NXOpen::AnimationDesigner::Measure @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a Measure feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::MeasureBuilder  NXOpen::AnimationDesigner::MeasureBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class Measure(NXOpen.DisplayableObject): 
    """ Represents a Measure feature. """
    pass


import NXOpen
## 
##     Represents a @link NXOpen::AnimationDesigner::MechanicalCamBuilder NXOpen::AnimationDesigner::MechanicalCamBuilder@endlink .
##      <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::MechanicalCamCollection::CreateMechanicalCamBuilder  NXOpen::AnimationDesigner::MechanicalCamCollection::CreateMechanicalCamBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MechanicalCamBuilder(NXOpen.Builder): 
    """
    Represents a <ja_class>NXOpen.AnimationDesigner.MechanicalCamBuilder</ja_class>.
    """


    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the mechanical cam </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the mechanical cam </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <NoColor>
        """
        SpecifyColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> MechanicalCamBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link MechanicalCamBuilder.ColorOptions NXOpen.AnimationDesigner.MechanicalCamBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return MechanicalCamBuilder.ColorOptions
    @property
    def ColorOption(self) -> MechanicalCamBuilder.ColorOptions:
        """
        Getter for property: (@link MechanicalCamBuilder.ColorOptions NXOpen.AnimationDesigner.MechanicalCamBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Setter for property: (@link MechanicalCamBuilder.ColorOptions NXOpen.AnimationDesigner.MechanicalCamBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: MechanicalCamBuilder.ColorOptions):
        """
        Setter for property: (@link MechanicalCamBuilder.ColorOptions NXOpen.AnimationDesigner.MechanicalCamBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) FollowerAxis
    ##  Returns the follower axis joint.  
    ##    This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  or @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def FollowerAxis(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) FollowerAxis
         Returns the follower axis joint.  
           This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  or @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FollowerFaces
    ##  Returns the follower faces.  
    ##    This can be a @link NXOpen::Face NXOpen::Face@endlink .   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def FollowerFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) FollowerFaces
         Returns the follower faces.  
           This can be a @link NXOpen::Face NXOpen::Face@endlink .   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) MasterAxis
    ##  Returns the master axis joint.  
    ##    This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  or @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def MasterAxis(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) MasterAxis
         Returns the master axis joint.  
           This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  or @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MasterFaces
    ##  Returns the master faces.  
    ##    This can be a @link NXOpen::Face NXOpen::Face@endlink .   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def MasterFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MasterFaces
         Returns the master faces.  
           This can be a @link NXOpen::Face NXOpen::Face@endlink .   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
import NXOpen
##  Represents a collection of Mechanical Cam objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MechanicalCamCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Mechanical Cam objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::MechanicalCamBuilder NXOpen::AnimationDesigner::MechanicalCamBuilder@endlink . 
    ##  @return builder (@link MechanicalCamBuilder NXOpen.AnimationDesigner.MechanicalCamBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="mechanicalCam"> (@link MechanicalCam NXOpen.AnimationDesigner.MechanicalCam@endlink)  @link NXOpen::AnimationDesigner::MechanicalCam NXOpen::AnimationDesigner::MechanicalCam@endlink  to be edited, if NULL then create a new one </param>
    def CreateMechanicalCamBuilder(part: NXOpen.Part, mechanicalCam: MechanicalCam) -> MechanicalCamBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::MechanicalCamBuilder NXOpen::AnimationDesigner::MechanicalCamBuilder@endlink . 
         @return builder (@link MechanicalCamBuilder NXOpen.AnimationDesigner.MechanicalCamBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::MechanicalCam   NXOpen::AnimationDesigner::MechanicalCam @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return obj (@link MechanicalCam NXOpen.AnimationDesigner.MechanicalCam@endlink):  @link  NXOpen::AnimationDesigner::MechanicalCam   NXOpen::AnimationDesigner::MechanicalCam @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::MechanicalCam   NXOpen::AnimationDesigner::MechanicalCam @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> MechanicalCam:
        """
         Finds the @link  NXOpen::AnimationDesigner::MechanicalCam   NXOpen::AnimationDesigner::MechanicalCam @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return obj (@link MechanicalCam NXOpen.AnimationDesigner.MechanicalCam@endlink):  @link  NXOpen::AnimationDesigner::MechanicalCam   NXOpen::AnimationDesigner::MechanicalCam @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a Mechanical Cam feature. <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::MechanicalCamBuilder  NXOpen::AnimationDesigner::MechanicalCamBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class MechanicalCam(NXOpen.DisplayableObject): 
    """ Represents a Mechanical Cam feature."""
    pass


import NXOpen
##  Represents a base builder for Motor.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class MotorBuilder(NXOpen.Builder): 
    """ Represents a base builder for Motor. """


    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) AxisJoint
    ##  Returns the joint select.  
    ##    This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink .   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def AxisJoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) AxisJoint
         Returns the joint select.  
           This can be a @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink .   
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
import NXOpen
##  Represents the Animation Designer motor class.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class Motor(NXOpen.DisplayableObject): 
    """ Represents the Animation Designer motor class. """
    pass


import NXOpen
##  Represents a list of objects. <br> To create a new instance of this class, use @link NXOpen::Part::CreateObjectList  NXOpen::Part::CreateObjectList @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PathConstraintFrameBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""


    ## Getter for property: (int) Length
    ##  Returns the length of the list   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    
    ##  Appends a set of objects to the list
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="objects"> (@link PathConstraintFrameBuilder List[NXOpen.AnimationDesigner.PathConstraintFrameBuilder]@endlink)  items to append </param>
    @overload
    def Append(self, objects: List[PathConstraintFrameBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    
    ##  Appends an object to the list
    ##     
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="objectValue"> (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink)  item to append </param>
    @overload
    def Append(self, objectValue: PathConstraintFrameBuilder) -> None:
        """
         Appends an object to the list
            
        """
        pass
    
    ##  Clears the entire list without deleting the objects.  The caller is responsible for 
    ##         accounting for these objects.  If they are not used or deleted by the time the part is 
    ##         closed (in other words, leaked) an error will occur 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    @overload
    def Clear(self) -> None:
        """
         Clears the entire list without deleting the objects.  The caller is responsible for 
                accounting for these objects.  If they are not used or deleted by the time the part is 
                closed (in other words, leaked) an error will occur 
        """
        pass
    
    ##  Deletes the item at the index specified.  The size of the list does
    ##     *   not change, but the item at this index is set to NULL.
    ##     
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="delete_idx"> (int)  index of item to be deleted </param>
    def ClearIndex(self, delete_idx: int) -> None:
        """
         Deletes the item at the index specified.  The size of the list does
            *   not change, but the item at this index is set to NULL.
            
        """
        pass
    
    ##  Clears the entire list 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the objects when removing them </param>
    @overload
    def Clear(self, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Clears the entire list 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    @overload
    def Erase(self, index: int) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object at the given position from the list.
    ##         The list is shifted so that there isn't a null where the object used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="index"> (int)  index of item to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, index: int, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object at the given position from the list.
                The list is shifted so that there isn't a null where the object used to be. 
        """
        pass
    
    ##  Erases the object from the list, but does not delete the object.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="obj"> (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink)  object to be removed from the list </param>
    @overload
    def Erase(self, obj: PathConstraintFrameBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Erases the object from the list.
    ##         The list is shifted so that there isn't a null where the object used to exist. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="obj"> (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink)  object to be removed from the list </param>
    ## <param name="delete_option"> (@link NXOpen.ObjectList.DeleteOption NXOpen.ObjectList.DeleteOption@endlink)  whether to delete the object </param>
    @overload
    def Erase(self, obj: PathConstraintFrameBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    
    ##  Finds the index where the input object appears.  If it does not appear,
    ##     *   -1 is returned.
    ##     
    ##  @return index (int):  index of input object, -1 if not on list .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="obj"> (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink)  Object to find index for </param>
    def FindIndex(self, obj: PathConstraintFrameBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
            *   -1 is returned.
            
         @return index (int):  index of input object, -1 if not on list .
        """
        pass
    
    ##  Returns the object at the input index.  May be NULL.
    ##     
    ##  @return obj (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink):  object found at input index .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of object to return </param>
    def FindItem(self, index: int) -> PathConstraintFrameBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         @return obj (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink):  object found at input index .
        """
        pass
    
    ##  Gets the contents of the entire list 
    ##  @return objects (@link PathConstraintFrameBuilder List[NXOpen.AnimationDesigner.PathConstraintFrameBuilder]@endlink):  The list contents .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def GetContents(self) -> List[PathConstraintFrameBuilder]:
        """
         Gets the contents of the entire list 
         @return objects (@link PathConstraintFrameBuilder List[NXOpen.AnimationDesigner.PathConstraintFrameBuilder]@endlink):  The list contents .
        """
        pass
    
    ##  Inserts an object at the specified location 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="location"> (int)  location at which to insert the object </param>
    ## <param name="objectValue"> (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink)  object to be inserted </param>
    def Insert(self, location: int, objectValue: PathConstraintFrameBuilder) -> None:
        """
         Inserts an object at the specified location 
        """
        pass
    
    ##  Move object at the specified location to the bottom of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToBottom(self, index: int) -> None:
        """
         Move object at the specified location to the bottom of the list.
        """
        pass
    
    ##  Move object at the specified location to the top of the list.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  location of the item </param>
    def MoveToTop(self, index: int) -> None:
        """
         Move object at the specified location to the top of the list.
        """
        pass
    
    ##  Sets the contents of the entire list. This overwrites the previous contents of this list, 
    ##         but does not delete any objects that were originally on the list.
    ##      
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objects"> (@link PathConstraintFrameBuilder List[NXOpen.AnimationDesigner.PathConstraintFrameBuilder]@endlink)  The list contents </param>
    def SetContents(self, objects: List[PathConstraintFrameBuilder]) -> None:
        """
         Sets the contents of the entire list. This overwrites the previous contents of this list, 
                but does not delete any objects that were originally on the list.
             
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    @overload
    def Swap(self, index1: int, index2: int) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
    ##  Exchanges the position of two objects inside the list.
    ##         The first object is placed where the second used to be,
    ##         and second object where the first used to be. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="object_list"> (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) </param>
    ## <param name="object1"> (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink)  first item </param>
    ## <param name="object2"> (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink)  second item </param>
    @overload
    def Swap(self, object1: PathConstraintFrameBuilder, object2: PathConstraintFrameBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a frame that constrains the orientation along the path curve.  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::PathConstraintJointBuilder::NewPathFrame  NXOpen::AnimationDesigner::PathConstraintJointBuilder::NewPathFrame @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PathConstraintFrameBuilder(NXOpen.TaggedObject): 
    """ Represents a frame that constrains the orientation along the path curve. """


    ##  the curve types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Line</term><description> 
    ##  line </description> </item><item><term> 
    ## Spline</term><description> 
    ##  spline </description> </item></list>
    class CurveTypes(Enum):
        """
        Members Include: <Line> <Spline>
        """
        Line: int
        Spline: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PathConstraintFrameBuilder.CurveTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AssociatedCurve
    ##  Returns the associated curve.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.NXObject
    @property
    def AssociatedCurve(self) -> NXOpen.NXObject:
        """
        Getter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AssociatedCurve
         Returns the associated curve.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AssociatedCurve

    ##  Returns the associated curve.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AssociatedCurve.setter
    def AssociatedCurve(self, curve: NXOpen.NXObject):
        """
        Setter for property: (@link NXOpen.NXObject NXOpen.NXObject@endlink) AssociatedCurve
         Returns the associated curve.  
             
         
        """
        pass
    
    ## Getter for property: (@link PathConstraintFrameBuilder.CurveTypes NXOpen.AnimationDesigner.PathConstraintFrameBuilder.CurveTypes@endlink) CurveType
    ##  Returns the curve type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PathConstraintFrameBuilder.CurveTypes
    @property
    def CurveType(self) -> PathConstraintFrameBuilder.CurveTypes:
        """
        Getter for property: (@link PathConstraintFrameBuilder.CurveTypes NXOpen.AnimationDesigner.PathConstraintFrameBuilder.CurveTypes@endlink) CurveType
         Returns the curve type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PathConstraintFrameBuilder.CurveTypes NXOpen.AnimationDesigner.PathConstraintFrameBuilder.CurveTypes@endlink) CurveType

    ##  Returns the curve type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @CurveType.setter
    def CurveType(self, curveType: PathConstraintFrameBuilder.CurveTypes):
        """
        Setter for property: (@link PathConstraintFrameBuilder.CurveTypes NXOpen.AnimationDesigner.PathConstraintFrameBuilder.CurveTypes@endlink) CurveType
         Returns the curve type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) PathFrame
    ##  Returns the path frame.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def PathFrame(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) PathFrame
         Returns the path frame.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) PathFrame

    ##  Returns the path frame.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PathFrame.setter
    def PathFrame(self, pathFrame: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) PathFrame
         Returns the path frame.  
             
         
        """
        pass
    
    ## Getter for property: (float) PathParameter
    ##  Returns the path parameter.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return float
    @property
    def PathParameter(self) -> float:
        """
        Getter for property: (float) PathParameter
         Returns the path parameter.  
             
         
        """
        pass
    
    ## Setter for property: (float) PathParameter

    ##  Returns the path parameter.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PathParameter.setter
    def PathParameter(self, pathParameter: float):
        """
        Setter for property: (float) PathParameter
         Returns the path parameter.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::PathConstraintJoint NXOpen::AnimationDesigner::PathConstraintJoint@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::PathConstraintJointCollection::CreatePathConstraintJointBuilder  NXOpen::AnimationDesigner::PathConstraintJointCollection::CreatePathConstraintJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PathConstraintJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.PathConstraintJoint</ja_class> builder. """


    ##  the path types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromCoordinateSystems</term><description> 
    ##  from coordinate systems </description> </item><item><term> 
    ## FromCurves</term><description> 
    ##  from curves </description> </item></list>
    class PathTypes(Enum):
        """
        Members Include: <FromCoordinateSystems> <FromCurves>
        """
        FromCoordinateSystems: int
        FromCurves: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PathConstraintJointBuilder.PathTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##  Returns the axis vector which is tangent to the path curve at the selected point   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector which is tangent to the path curve at the selected point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##  Returns the axis vector which is tangent to the path curve at the selected point   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector which is tangent to the path curve at the selected point   
            
         
        """
        pass
    
    ## Getter for property: (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) FrameList
    ##  Returns the list containing the defined frames.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PathConstraintFrameBuilderList
    @property
    def FrameList(self) -> PathConstraintFrameBuilderList:
        """
        Getter for property: (@link PathConstraintFrameBuilderList NXOpen.AnimationDesigner.PathConstraintFrameBuilderList@endlink) FrameList
         Returns the list containing the defined frames.  
             
         
        """
        pass
    
    ## Getter for property: (bool) PathPreview
    ##  Returns the path preview   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return bool
    @property
    def PathPreview(self) -> bool:
        """
        Getter for property: (bool) PathPreview
         Returns the path preview   
            
         
        """
        pass
    
    ## Setter for property: (bool) PathPreview

    ##  Returns the path preview   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PathPreview.setter
    def PathPreview(self, enable: bool):
        """
        Setter for property: (bool) PathPreview
         Returns the path preview   
            
         
        """
        pass
    
    ## Getter for property: (@link PathConstraintJointBuilder.PathTypes NXOpen.AnimationDesigner.PathConstraintJointBuilder.PathTypes@endlink) PathType
    ##  Returns the path type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PathConstraintJointBuilder.PathTypes
    @property
    def PathType(self) -> PathConstraintJointBuilder.PathTypes:
        """
        Getter for property: (@link PathConstraintJointBuilder.PathTypes NXOpen.AnimationDesigner.PathConstraintJointBuilder.PathTypes@endlink) PathType
         Returns the path type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PathConstraintJointBuilder.PathTypes NXOpen.AnimationDesigner.PathConstraintJointBuilder.PathTypes@endlink) PathType

    ##  Returns the path type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PathType.setter
    def PathType(self, pathType: PathConstraintJointBuilder.PathTypes):
        """
        Setter for property: (@link PathConstraintJointBuilder.PathTypes NXOpen.AnimationDesigner.PathConstraintJointBuilder.PathTypes@endlink) PathType
         Returns the path type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
    ##  Returns the selected point on curve   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointOnCurve(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
         Returns the selected point on curve   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve

    ##  Returns the selected point on curve   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @PointOnCurve.setter
    def PointOnCurve(self, pointOnCurve: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
         Returns the selected point on curve   
            
         
        """
        pass
    
    ##  Evaluate the composited path with the curves. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge</param>
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluate the composited path with the curves. 
        """
        pass
    
    ##  Generate the path curves from the coordinates systems. 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GeneratePathCurves(self) -> None:
        """
         Generate the path curves from the coordinates systems. 
        """
        pass
    
    ##  Get the path curves that constrain the movement of the attachment
    ##  @return pathCurves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetPathCurves(self) -> List[NXOpen.NXObject]:
        """
         Get the path curves that constrain the movement of the attachment
         @return pathCurves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge.
        """
        pass
    
    ##  Creates a @link NXOpen::AnimationDesigner::PathConstraintFrameBuilder NXOpen::AnimationDesigner::PathConstraintFrameBuilder@endlink  object. 
    ##  @return pathFrameBuilder (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def NewPathFrame(self) -> PathConstraintFrameBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::PathConstraintFrameBuilder NXOpen::AnimationDesigner::PathConstraintFrameBuilder@endlink  object. 
         @return pathFrameBuilder (@link PathConstraintFrameBuilder NXOpen.AnimationDesigner.PathConstraintFrameBuilder@endlink): .
        """
        pass
    
    ##  Set the path curves that constrain the movement of the attachment
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="pathCurves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge</param>
    def SetPathCurvesFromCurves(self, pathCurves: List[NXOpen.NXObject]) -> None:
        """
         Set the path curves that constrain the movement of the attachment
        """
        pass
    
import NXOpen
##  Represents a collection of Path Constraint Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PathConstraintJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Path Constraint Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::PathConstraintJointBuilder NXOpen::AnimationDesigner::PathConstraintJointBuilder@endlink . 
    ##  @return builder (@link PathConstraintJointBuilder NXOpen.AnimationDesigner.PathConstraintJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="joint"> (@link PathConstraintJoint NXOpen.AnimationDesigner.PathConstraintJoint@endlink)  @link NXOpen::AnimationDesigner::PathConstraintJoint NXOpen::AnimationDesigner::PathConstraintJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreatePathConstraintJointBuilder(part: NXOpen.Part, joint: PathConstraintJoint) -> PathConstraintJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::PathConstraintJointBuilder NXOpen::AnimationDesigner::PathConstraintJointBuilder@endlink . 
         @return builder (@link PathConstraintJointBuilder NXOpen.AnimationDesigner.PathConstraintJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::PathConstraintJoint   NXOpen::AnimationDesigner::PathConstraintJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return pathConstraintJoint (@link PathConstraintJoint NXOpen.AnimationDesigner.PathConstraintJoint@endlink):  @link  NXOpen::AnimationDesigner::PathConstraintJoint   NXOpen::AnimationDesigner::PathConstraintJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::PathConstraintJoint   NXOpen::AnimationDesigner::PathConstraintJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> PathConstraintJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::PathConstraintJoint   NXOpen::AnimationDesigner::PathConstraintJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return pathConstraintJoint (@link PathConstraintJoint NXOpen.AnimationDesigner.PathConstraintJoint@endlink):  @link  NXOpen::AnimationDesigner::PathConstraintJoint   NXOpen::AnimationDesigner::PathConstraintJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Path Constraint Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::PathConstraintJointBuilder  NXOpen::AnimationDesigner::PathConstraintJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PathConstraintJoint(PhysicsJoint): 
    """ Represents a Path Constraint Joint feature. """
    pass


import NXOpen
##  Represents a base builder for Physics Joints.  <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class PhysicsJointBuilder(NXOpen.Builder): 
    """ Represents a base builder for Physics Joints. """


    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the joint </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the joint </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <NoColor>
        """
        SpecifyColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PhysicsJointBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the motion types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Dynamics</term><description> 
    ##  dynamics type </description> </item><item><term> 
    ## Kinematics</term><description> 
    ##  kinematics type </description> </item></list>
    class MotionTypes(Enum):
        """
        Members Include: <Dynamics> <Kinematics>
        """
        Dynamics: int
        Kinematics: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PhysicsJointBuilder.MotionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) AttachmentList
    ##  Returns the attachment list for a Joint.  
    ##    The list can consist of @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink  
    ##         objects or objects which can create a Rigid Group.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def AttachmentList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) AttachmentList
         Returns the attachment list for a Joint.  
           The list can consist of @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink  
                objects or objects which can create a Rigid Group.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BaseList
    ##  Returns the base list for a Joint.  
    ##    The list can consist of @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink  
    ##         objects or objects which can create a Rigid Group.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def BaseList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) BaseList
         Returns the base list for a Joint.  
           The list can consist of @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink  
                objects or objects which can create a Rigid Group.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link PhysicsJointBuilder.ColorOptions NXOpen.AnimationDesigner.PhysicsJointBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color options.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return PhysicsJointBuilder.ColorOptions
    @property
    def ColorOption(self) -> PhysicsJointBuilder.ColorOptions:
        """
        Getter for property: (@link PhysicsJointBuilder.ColorOptions NXOpen.AnimationDesigner.PhysicsJointBuilder.ColorOptions@endlink) ColorOption
         Returns the color options.  
             
         
        """
        pass
    
    ## Setter for property: (@link PhysicsJointBuilder.ColorOptions NXOpen.AnimationDesigner.PhysicsJointBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color options.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: PhysicsJointBuilder.ColorOptions):
        """
        Setter for property: (@link PhysicsJointBuilder.ColorOptions NXOpen.AnimationDesigner.PhysicsJointBuilder.ColorOptions@endlink) ColorOption
         Returns the color options.  
             
         
        """
        pass
    
    ## Getter for property: (@link PhysicsJointBuilder.MotionTypes NXOpen.AnimationDesigner.PhysicsJointBuilder.MotionTypes@endlink) MotionType
    ##  Returns the motion type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return PhysicsJointBuilder.MotionTypes
    @property
    def MotionType(self) -> PhysicsJointBuilder.MotionTypes:
        """
        Getter for property: (@link PhysicsJointBuilder.MotionTypes NXOpen.AnimationDesigner.PhysicsJointBuilder.MotionTypes@endlink) MotionType
         Returns the motion type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PhysicsJointBuilder.MotionTypes NXOpen.AnimationDesigner.PhysicsJointBuilder.MotionTypes@endlink) MotionType

    ##  Returns the motion type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @MotionType.setter
    def MotionType(self, motionType: PhysicsJointBuilder.MotionTypes):
        """
        Setter for property: (@link PhysicsJointBuilder.MotionTypes NXOpen.AnimationDesigner.PhysicsJointBuilder.MotionTypes@endlink) MotionType
         Returns the motion type.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
import NXOpen
##  Represents the Animation Designer joint class. <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class PhysicsJoint(NXOpen.DisplayableObject): 
    """ Represents the Animation Designer joint class."""
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::PlanarJointBuilder NXOpen::AnimationDesigner::PlanarJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::PlanarJointCollection::CreatePlanarJointBuilder  NXOpen::AnimationDesigner::PlanarJointCollection::CreatePlanarJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class PlanarJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.PlanarJointBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##  Returns  @brief  a value that specifies axis vector.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns  @brief  a value that specifies axis vector.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##  Returns  @brief  a value that specifies axis vector.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns  @brief  a value that specifies axis vector.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin
    ##  Returns  @brief  a value that indicates the origin point.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Point
    @property
    def PointOrigin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin
         Returns  @brief  a value that indicates the origin point.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin

    ##  Returns  @brief  a value that indicates the origin point.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @PointOrigin.setter
    def PointOrigin(self, origin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin
         Returns  @brief  a value that indicates the origin point.  
            
        
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Planar Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class PlanarJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Planar Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::PlanarJointBuilder NXOpen::AnimationDesigner::PlanarJointBuilder@endlink . 
    ##  @return builder (@link PlanarJointBuilder NXOpen.AnimationDesigner.PlanarJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="planarJoint"> (@link PlanarJoint NXOpen.AnimationDesigner.PlanarJoint@endlink)  @link NXOpen::AnimationDesigner::PlanarJoint NXOpen::AnimationDesigner::PlanarJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreatePlanarJointBuilder(part: NXOpen.Part, planarJoint: PlanarJoint) -> PlanarJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::PlanarJointBuilder NXOpen::AnimationDesigner::PlanarJointBuilder@endlink . 
         @return builder (@link PlanarJointBuilder NXOpen.AnimationDesigner.PlanarJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::PlanarJoint   NXOpen::AnimationDesigner::PlanarJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return planarJoint (@link PlanarJoint NXOpen.AnimationDesigner.PlanarJoint@endlink):  @link  NXOpen::AnimationDesigner::PlanarJoint   NXOpen::AnimationDesigner::PlanarJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::PlanarJoint   NXOpen::AnimationDesigner::PlanarJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> PlanarJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::PlanarJoint   NXOpen::AnimationDesigner::PlanarJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return planarJoint (@link PlanarJoint NXOpen.AnimationDesigner.PlanarJoint@endlink):  @link  NXOpen::AnimationDesigner::PlanarJoint   NXOpen::AnimationDesigner::PlanarJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Planar Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::PlanarJointBuilder  NXOpen::AnimationDesigner::PlanarJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class PlanarJoint(PhysicsJoint): 
    """ Represents a Planar Joint feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::PointOnCurveJoint NXOpen::AnimationDesigner::PointOnCurveJoint@endlink  builder.  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::PointOnCurveJointCollection::CreatePointOnCurveJointBuilder  NXOpen::AnimationDesigner::PointOnCurveJointCollection::CreatePointOnCurveJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PointOnCurveJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.PointOnCurveJoint</ja_class> builder. """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##  Returns the axis vector which is tangent to the connected curve at the selected point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##  Returns the axis vector which is tangent to the connected curve at the selected point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientationVector
    ##  Returns the orientation vector for kinematics motion type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def OrientationVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientationVector
         Returns the orientation vector for kinematics motion type.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientationVector

    ##  Returns the orientation vector for kinematics motion type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @OrientationVector.setter
    def OrientationVector(self, orientationVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) OrientationVector
         Returns the orientation vector for kinematics motion type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
    ##  Returns the selected point on curve.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointOnCurve(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve

    ##  Returns the selected point on curve.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @PointOnCurve.setter
    def PointOnCurve(self, pointOnCurve: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseOrientationVector
    ##  Returns the flag to use orientation vector or not for kinematics motion type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def UseOrientationVector(self) -> bool:
        """
        Getter for property: (bool) UseOrientationVector
         Returns the flag to use orientation vector or not for kinematics motion type.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseOrientationVector

    ##  Returns the flag to use orientation vector or not for kinematics motion type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @UseOrientationVector.setter
    def UseOrientationVector(self, useOrientationVector: bool):
        """
        Setter for property: (bool) UseOrientationVector
         Returns the flag to use orientation vector or not for kinematics motion type.  
             
         
        """
        pass
    
    ##  Evaluates the path. If there is no path, create it, otherwise evaluate it. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge</param>
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluates the path. If there is no path, create it, otherwise evaluate it. 
        """
        pass
    
    ##  Gets the connected curves which the attachment will move along. 
    ##  @return curves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def GetConnectedCurves(self) -> List[NXOpen.NXObject]:
        """
         Gets the connected curves which the attachment will move along. 
         @return curves (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink):  curve or edge .
        """
        pass
    
    ##  Sets the connected curves which the attachment will move along. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="curves"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  curve or edge </param>
    def SetConnectedCurves(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Sets the connected curves which the attachment will move along. 
        """
        pass
    
import NXOpen
##  Represents a collection of Point On Curve Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PointOnCurveJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Point On Curve Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::PointOnCurveJointBuilder NXOpen::AnimationDesigner::PointOnCurveJointBuilder@endlink . 
    ##  @return builder (@link PointOnCurveJointBuilder NXOpen.AnimationDesigner.PointOnCurveJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="joint"> (@link PointOnCurveJoint NXOpen.AnimationDesigner.PointOnCurveJoint@endlink)  @link NXOpen::AnimationDesigner::PointOnCurveJoint NXOpen::AnimationDesigner::PointOnCurveJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreatePointOnCurveJointBuilder(part: NXOpen.Part, joint: PointOnCurveJoint) -> PointOnCurveJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::PointOnCurveJointBuilder NXOpen::AnimationDesigner::PointOnCurveJointBuilder@endlink . 
         @return builder (@link PointOnCurveJointBuilder NXOpen.AnimationDesigner.PointOnCurveJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::PointOnCurveJoint   NXOpen::AnimationDesigner::PointOnCurveJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return pointOnCurveJoint (@link PointOnCurveJoint NXOpen.AnimationDesigner.PointOnCurveJoint@endlink):  @link  NXOpen::AnimationDesigner::PointOnCurveJoint   NXOpen::AnimationDesigner::PointOnCurveJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::PointOnCurveJoint   NXOpen::AnimationDesigner::PointOnCurveJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> PointOnCurveJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::PointOnCurveJoint   NXOpen::AnimationDesigner::PointOnCurveJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return pointOnCurveJoint (@link PointOnCurveJoint NXOpen.AnimationDesigner.PointOnCurveJoint@endlink):  @link  NXOpen::AnimationDesigner::PointOnCurveJoint   NXOpen::AnimationDesigner::PointOnCurveJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Point On Curve Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::PointOnCurveJointBuilder  NXOpen::AnimationDesigner::PointOnCurveJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PointOnCurveJoint(PhysicsJoint): 
    """ Represents a Point On Curve Joint feature. """
    pass


import NXOpen
##  @brief  Represents a @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder@endlink .  
## 
##   <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChainCollection::CreatePointOnCurveKinematicsChainBuilder  NXOpen::AnimationDesigner::PointOnCurveKinematicsChainCollection::CreatePointOnCurveKinematicsChainBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class PointOnCurveKinematicsChainBuilder(NXOpen.Builder): 
    """<summary> Represents a <ja_class>NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder</ja_class>. </summary>"""


    ##  @brief  the projection direction types.  
    ## 
    ##  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AlongCurveNormal</term><description> 
    ##  Along Curve Normal </description> </item><item><term> 
    ## AlongVector</term><description> 
    ##  Along Vector  </description> </item></list>
    class ProjectionDirectionType(Enum):
        """
        Members Include: <AlongCurveNormal> <AlongVector>
        """
        AlongCurveNormal: int
        AlongVector: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PointOnCurveKinematicsChainBuilder.ProjectionDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) MasterRigidGroup
    ##  Returns @brief  the master rigid group selection.  
    ##    This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink .  
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def MasterRigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) MasterRigidGroup
         Returns @brief  the master rigid group selection.  
           This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink .  
        
           
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns @brief  the name  
    ##   
    ##   
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns @brief  the name  
          
          
           
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns @brief  the name  
    ##   
    ##   
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns @brief  the name  
          
          
           
         
        """
        pass
    
    ## Getter for property: (@link PointOnCurveKinematicsChainBuilder.ProjectionDirectionType NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder.ProjectionDirectionType@endlink) ProjectionDirection
    ##  Returns @brief  the projection direction type of the slave rigid center point.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return PointOnCurveKinematicsChainBuilder.ProjectionDirectionType
    @property
    def ProjectionDirection(self) -> PointOnCurveKinematicsChainBuilder.ProjectionDirectionType:
        """
        Getter for property: (@link PointOnCurveKinematicsChainBuilder.ProjectionDirectionType NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder.ProjectionDirectionType@endlink) ProjectionDirection
         Returns @brief  the projection direction type of the slave rigid center point.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link PointOnCurveKinematicsChainBuilder.ProjectionDirectionType NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder.ProjectionDirectionType@endlink) ProjectionDirection

    ##  Returns @brief  the projection direction type of the slave rigid center point.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ProjectionDirection.setter
    def ProjectionDirection(self, projectionDirection: PointOnCurveKinematicsChainBuilder.ProjectionDirectionType):
        """
        Setter for property: (@link PointOnCurveKinematicsChainBuilder.ProjectionDirectionType NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder.ProjectionDirectionType@endlink) ProjectionDirection
         Returns @brief  the projection direction type of the slave rigid center point.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
    ##  Returns @brief  the projection vector when choosing ProjectionDirectionType_AlongVector.  
    ##     
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def ProjectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
         Returns @brief  the projection vector when choosing ProjectionDirectionType_AlongVector.  
            
        
           
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector

    ##  Returns @brief  the projection vector when choosing ProjectionDirectionType_AlongVector.  
    ##     
    ## 
    ##    
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @ProjectionVector.setter
    def ProjectionVector(self, projectionVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) ProjectionVector
         Returns @brief  the projection vector when choosing ProjectionDirectionType_AlongVector.  
            
        
           
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SlaveRigidGroups
    ##  Returns @brief  the slave rigid groups selection.  
    ##    This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink .  
    ## 
    ##    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SlaveRigidGroups(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SlaveRigidGroups
         Returns @brief  the slave rigid groups selection.  
           This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink .  
        
           
         
        """
        pass
    
import NXOpen
##  @brief  Represents a collection of Point On Curve Kinematics Chain objects.  
## 
##   <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class PointOnCurveKinematicsChainCollection(NXOpen.TaggedObjectCollection): 
    """<summary> Represents a collection of Point On Curve Kinematics Chain objects. </summary>"""


    ##  @brief  Creates a @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder@endlink .  
    ## 
    ##  
    ##  @return builder (@link PointOnCurveKinematicsChainBuilder NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="objectValue"> (@link PointOnCurveKinematicsChain NXOpen.AnimationDesigner.PointOnCurveKinematicsChain@endlink)  @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChain NXOpen::AnimationDesigner::PointOnCurveKinematicsChain@endlink  to be edited, if NULL then create a new one </param>
    def CreatePointOnCurveKinematicsChainBuilder(part: NXOpen.Part, objectValue: PointOnCurveKinematicsChain) -> PointOnCurveKinematicsChainBuilder:
        """
         @brief  Creates a @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder@endlink .  
        
         
         @return builder (@link PointOnCurveKinematicsChainBuilder NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder@endlink): .
        """
        pass
    
    ##  @brief  Finds the @link  NXOpen::AnimationDesigner::PointOnCurveKinematicsChain   NXOpen::AnimationDesigner::PointOnCurveKinematicsChain @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name.  
    ## 
    ##  
    ##  @return objectTag (@link PointOnCurveKinematicsChain NXOpen.AnimationDesigner.PointOnCurveKinematicsChain@endlink):  @link  NXOpen::AnimationDesigner::PointOnCurveKinematicsChain   NXOpen::AnimationDesigner::PointOnCurveKinematicsChain @endlink  with this name. .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::PointOnCurveKinematicsChain   NXOpen::AnimationDesigner::PointOnCurveKinematicsChain @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> PointOnCurveKinematicsChain:
        """
         @brief  Finds the @link  NXOpen::AnimationDesigner::PointOnCurveKinematicsChain   NXOpen::AnimationDesigner::PointOnCurveKinematicsChain @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name.  
        
         
         @return objectTag (@link PointOnCurveKinematicsChain NXOpen.AnimationDesigner.PointOnCurveKinematicsChain@endlink):  @link  NXOpen::AnimationDesigner::PointOnCurveKinematicsChain   NXOpen::AnimationDesigner::PointOnCurveKinematicsChain @endlink  with this name. .
        """
        pass
    
import NXOpen
##  @brief  Represents a Point On Curve Kinematics Chain feature.  
## 
##   <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder  NXOpen::AnimationDesigner::PointOnCurveKinematicsChainBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class PointOnCurveKinematicsChain(NXOpen.DisplayableObject): 
    """<summary> Represents a Point On Curve Kinematics Chain feature. </summary>"""
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::PositionMotorBuilder NXOpen::AnimationDesigner::PositionMotorBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::PositionMotorCollection::CreatePositionMotorBuilder  NXOpen::AnimationDesigner::PositionMotorCollection::CreatePositionMotorBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PositionMotorBuilder(MotorBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.PositionMotorBuilder</ja_class>. """


    ##  the auto calculate types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EndTime</term><description> 
    ##  Auto calculate end time </description> </item><item><term> 
    ## Speed</term><description> 
    ##  Auto calculate speed </description> </item><item><term> 
    ## Destination</term><description> 
    ##  Auto calculate destination </description> </item></list>
    class AutoCalculate(Enum):
        """
        Members Include: <EndTime> <Speed> <Destination>
        """
        EndTime: int
        Speed: int
        Destination: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PositionMotorBuilder.AutoCalculate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the axis types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Angular</term><description> 
    ##  Angular </description> </item><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Mixed</term><description> 
    ##  Mix angular and linear </description> </item></list>
    class Axis(Enum):
        """
        Members Include: <Angular> <Linear> <Mixed>
        """
        Angular: int
        Linear: int
        Mixed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PositionMotorBuilder.Axis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the position motor </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the position motor </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <NoColor>
        """
        SpecifyColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PositionMotorBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PositionMotorBuilder.Axis NXOpen.AnimationDesigner.PositionMotorBuilder.Axis@endlink) AxisType
    ##  Returns the axis type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return PositionMotorBuilder.Axis
    @property
    def AxisType(self) -> PositionMotorBuilder.Axis:
        """
        Getter for property: (@link PositionMotorBuilder.Axis NXOpen.AnimationDesigner.PositionMotorBuilder.Axis@endlink) AxisType
         Returns the axis type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PositionMotorBuilder.Axis NXOpen.AnimationDesigner.PositionMotorBuilder.Axis@endlink) AxisType

    ##  Returns the axis type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AxisType.setter
    def AxisType(self, axisType: PositionMotorBuilder.Axis):
        """
        Setter for property: (@link PositionMotorBuilder.Axis NXOpen.AnimationDesigner.PositionMotorBuilder.Axis@endlink) AxisType
         Returns the axis type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link PositionMotorBuilder.ColorOptions NXOpen.AnimationDesigner.PositionMotorBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PositionMotorBuilder.ColorOptions
    @property
    def ColorOption(self) -> PositionMotorBuilder.ColorOptions:
        """
        Getter for property: (@link PositionMotorBuilder.ColorOptions NXOpen.AnimationDesigner.PositionMotorBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Setter for property: (@link PositionMotorBuilder.ColorOptions NXOpen.AnimationDesigner.PositionMotorBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: PositionMotorBuilder.ColorOptions):
        """
        Setter for property: (@link PositionMotorBuilder.ColorOptions NXOpen.AnimationDesigner.PositionMotorBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ##  Calculates the bar. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    def BarCalculate(self, index: int) -> None:
        """
         Calculates the bar. 
        """
        pass
    
    ##  Creates a new bar. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    
    ##  Deletes the bars. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    
    ##  Mirrors the bars. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    ## <param name="mirror_time"> (float) </param>
    def MirrorBars(self, bars: List[int], mirror_time: float) -> None:
        """
         Mirrors the bars. 
        """
        pass
    
    ##  Pastes the bars. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    ## <param name="shift_time"> (float) </param>
    ## <param name="isCut"> (bool) </param>
    def PasteBars(self, bars: List[int], shift_time: float, isCut: bool) -> None:
        """
         Pastes the bars. 
        """
        pass
    
    ##  Sets the bar acceleration. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="acceleration"> (float) </param>
    def SetBarAcceleration(self, index: int, acceleration: float) -> None:
        """
         Sets the bar acceleration. 
        """
        pass
    
    ##  Sets the bar calculation type. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="calc_type"> (int) </param>
    def SetBarCalcType(self, index: int, calc_type: int) -> None:
        """
         Sets the bar calculation type. 
        """
        pass
    
    ##  Sets the bar deceleration. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="deceleration"> (float) </param>
    def SetBarDeceleration(self, index: int, deceleration: float) -> None:
        """
         Sets the bar deceleration. 
        """
        pass
    
    ##  Sets the bar end time. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="end_time"> (float) </param>
    def SetBarEndTime(self, index: int, end_time: float) -> None:
        """
         Sets the bar end time. 
        """
        pass
    
    ##  Sets the bar increment. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="increment"> (float) </param>
    def SetBarIncrement(self, index: int, increment: float) -> None:
        """
         Sets the bar increment. 
        """
        pass
    
    ##  Sets the bar limit acceleration. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="limit_acceleration"> (bool) </param>
    def SetBarLimitAcceleration(self, index: int, limit_acceleration: bool) -> None:
        """
         Sets the bar limit acceleration. 
        """
        pass
    
    ##  Sets the bar name. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="name"> (str) </param>
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    
    ##  Sets the bar speed. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="speed"> (float) </param>
    def SetBarSpeed(self, index: int, speed: float) -> None:
        """
         Sets the bar speed. 
        """
        pass
    
    ##  Sets the bar start time. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="start_time"> (float) </param>
    def SetBarStartTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
    
    ##  Sets the bar time. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="bars"> (List[int]) </param>
    ## <param name="deltaStart"> (float) </param>
    ## <param name="deltaDuration"> (float) </param>
    def SetBarTime(self, bars: List[int], deltaStart: float, deltaDuration: float) -> None:
        """
         Sets the bar time. 
        """
        pass
    
    ##  Splits the bars with the start time exp tag. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="index"> (int) </param>
    ## <param name="split_time"> (float) </param>
    def SplitBar(self, index: int, split_time: float) -> None:
        """
         Splits the bars with the start time exp tag. 
        """
        pass
    
    ##  Updates the motor destination. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    def UpdateDestination(self) -> None:
        """
         Updates the motor destination. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a collection of Position Motor objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PositionMotorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Position Motor objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::PositionMotorBuilder NXOpen::AnimationDesigner::PositionMotorBuilder@endlink . 
    ##  @return builder (@link PositionMotorBuilder NXOpen.AnimationDesigner.PositionMotorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="positionMotor"> (@link PositionMotor NXOpen.AnimationDesigner.PositionMotor@endlink)  @link NXOpen::AnimationDesigner::PositionMotor NXOpen::AnimationDesigner::PositionMotor@endlink  to be edited, if NULL then create a new one </param>
    @overload
    def CreatePositionMotorBuilder(part: NXOpen.Part, positionMotor: PositionMotor) -> PositionMotorBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::PositionMotorBuilder NXOpen::AnimationDesigner::PositionMotorBuilder@endlink . 
         @return builder (@link PositionMotorBuilder NXOpen.AnimationDesigner.PositionMotorBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::AnimationDesigner::PositionMotorBuilder NXOpen::AnimationDesigner::PositionMotorBuilder@endlink . 
    ##  @return builder (@link PositionMotorBuilder NXOpen.AnimationDesigner.PositionMotorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="positionMotor"> (@link PositionMotor NXOpen.AnimationDesigner.PositionMotor@endlink)  @link NXOpen::AnimationDesigner::PositionMotor NXOpen::AnimationDesigner::PositionMotor@endlink  to be edited, if NULL then create a new one </param>
    ## <param name="partOcc"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  for the edited position motor occurrence </param>
    @overload
    def CreatePositionMotorBuilder(part: NXOpen.Part, positionMotor: PositionMotor, partOcc: NXOpen.Assemblies.Component) -> PositionMotorBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::PositionMotorBuilder NXOpen::AnimationDesigner::PositionMotorBuilder@endlink . 
         @return builder (@link PositionMotorBuilder NXOpen.AnimationDesigner.PositionMotorBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::PositionMotor   NXOpen::AnimationDesigner::PositionMotor @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return positionMotor (@link PositionMotor NXOpen.AnimationDesigner.PositionMotor@endlink):  @link  NXOpen::AnimationDesigner::PositionMotor   NXOpen::AnimationDesigner::PositionMotor @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::PositionMotor   NXOpen::AnimationDesigner::PositionMotor @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> PositionMotor:
        """
         Finds the @link  NXOpen::AnimationDesigner::PositionMotor   NXOpen::AnimationDesigner::PositionMotor @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return positionMotor (@link PositionMotor NXOpen.AnimationDesigner.PositionMotor@endlink):  @link  NXOpen::AnimationDesigner::PositionMotor   NXOpen::AnimationDesigner::PositionMotor @endlink  with this name. .
        """
        pass
    
##  Represents a Position Motor feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::PositionMotorBuilder  NXOpen::AnimationDesigner::PositionMotorBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PositionMotor(Motor): 
    """ Represents a Position Motor feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::PreferencesBuilder NXOpen::AnimationDesigner::PreferencesBuilder@endlink  builder.  <br> Use the static method in @link NXOpen::AnimationDesigner::AnimationDesignerManager NXOpen::AnimationDesigner::AnimationDesignerManager@endlink  to obtain an instance.  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.PreferencesBuilder</ja_class> builder. """


    ##  the arrangement types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Isolated</term><description> 
    ##  Isolated </description> </item><item><term> 
    ## Standard</term><description> 
    ##  Standard </description> </item></list>
    class ArrangementTypes(Enum):
        """
        Members Include: <Isolated> <Standard>
        """
        Isolated: int
        Standard: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ArrangementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the body types to use for measure. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FacetBody</term><description> 
    ##  Facet Body </description> </item><item><term> 
    ## SolidBody</term><description> 
    ##  Solid Body </description> </item></list>
    class BodyToUseForMeasureTypes(Enum):
        """
        Members Include: <FacetBody> <SolidBody>
        """
        FacetBody: int
        SolidBody: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.BodyToUseForMeasureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the input type for using a length value or a percentage for kineo flexible facet body user defined linear precision. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Value</term><description> 
    ##  Length value </description> </item><item><term> 
    ## Percentage</term><description> 
    ##  Length percentage </description> </item></list>
    class FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes(Enum):
        """
        Members Include: <Value> <Percentage>
        """
        Value: int
        Percentage: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the flow line style types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Original</term><description> 
    ##  Original </description> </item><item><term> 
    ## Solid</term><description> 
    ##  Solid </description> </item><item><term> 
    ## Dashed</term><description> 
    ##  Dashed </description> </item><item><term> 
    ## Phantom</term><description> 
    ##  Phantom </description> </item><item><term> 
    ## Centerline</term><description> 
    ##  Centerline </description> </item><item><term> 
    ## Dotted</term><description> 
    ##  Dotted </description> </item><item><term> 
    ## LongDashed</term><description> 
    ##  Long Dashed </description> </item><item><term> 
    ## DottedDashed</term><description> 
    ##  Dotted Dashed </description> </item><item><term> 
    ## LongDashedDoubleDotted</term><description> 
    ##  Long Dashed Double Dotted </description> </item><item><term> 
    ## LongDashedDotted</term><description> 
    ##  Long Dashed Dotted </description> </item><item><term> 
    ## LongDashedTriplicateDotted</term><description> 
    ##  Long Dashed Triplicate Dotted </description> </item><item><term> 
    ## LongDashedDoubleShortDashed</term><description> 
    ##  Solid </description> </item></list>
    class FlowLineStyleTypes(Enum):
        """
        Members Include: <Original> <Solid> <Dashed> <Phantom> <Centerline> <Dotted> <LongDashed> <DottedDashed> <LongDashedDoubleDotted> <LongDashedDotted> <LongDashedTriplicateDotted> <LongDashedDoubleShortDashed>
        """
        Original: int
        Solid: int
        Dashed: int
        Phantom: int
        Centerline: int
        Dotted: int
        LongDashed: int
        DottedDashed: int
        LongDashedDoubleDotted: int
        LongDashedDotted: int
        LongDashedTriplicateDotted: int
        LongDashedDoubleShortDashed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.FlowLineStyleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the graph plot types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Plot2D</term><description> 
    ##  2D plot type </description> </item><item><term> 
    ## Plot3D</term><description> 
    ##  3D plot type </description> </item></list>
    class GraphPlotTypes(Enum):
        """
        Members Include: <Plot2D> <Plot3D>
        """
        Plot2D: int
        Plot3D: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.GraphPlotTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the kineo flexible facet body precision. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Low</term><description> 
    ##  Low </description> </item><item><term> 
    ## Medium</term><description> 
    ##  Medium </description> </item><item><term> 
    ## High</term><description> 
    ##  High </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  User Defined </description> </item></list>
    class KineoFlexibleFacetBodyPrecision(Enum):
        """
        Members Include: <Low> <Medium> <High> <UserDefined>
        """
        Low: int
        Medium: int
        High: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the physics engine. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Bullet</term><description> 
    ##  Bullet Engine </description> </item><item><term> 
    ## PhysX</term><description> 
    ##  PhysX Engine </description> </item><item><term> 
    ## Kineo</term><description> 
    ##  Kineo Engine </description> </item></list>
    class PhysicsEngines(Enum):
        """
        Members Include: <Bullet> <PhysX> <Kineo>
        """
        Bullet: int
        PhysX: int
        Kineo: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.PhysicsEngines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the Precision Preset Mode. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Fine</term><description> 
    ## </description> </item><item><term> 
    ## Balance</term><description> 
    ## </description> </item><item><term> 
    ## Rough</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item><item><term> 
    ## Num</term><description> 
    ## </description> </item></list>
    class PrecisionPresetModes(Enum):
        """
        Members Include: <Fine> <Balance> <Rough> <UserDefined> <Num>
        """
        Fine: int
        Balance: int
        Rough: int
        UserDefined: int
        Num: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.PrecisionPresetModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the rigid group selection display types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SelectionColor</term><description> 
    ##  Selection Color </description> </item><item><term> 
    ## BoundingBox</term><description> 
    ##  Bounding Box </description> </item></list>
    class RigidGroupSelectionDisplayTypes(Enum):
        """
        Members Include: <SelectionColor> <BoundingBox>
        """
        SelectionColor: int
        BoundingBox: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.RigidGroupSelectionDisplayTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the solution search scope types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## EntireAssembly</term><description> 
    ##  Entire Assembly </description> </item><item><term> 
    ## WithinWorkPartOnly</term><description> 
    ##  Within Work Part Only </description> </item></list>
    class SolutionSearchScopeTypes(Enum):
        """
        Members Include: <EntireAssembly> <WithinWorkPartOnly>
        """
        EntireAssembly: int
        WithinWorkPartOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.SolutionSearchScopeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PreferencesBuilder.ArrangementTypes NXOpen.AnimationDesigner.PreferencesBuilder.ArrangementTypes@endlink) ArrangementType
    ##  Returns the option specifies the arrangement type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return PreferencesBuilder.ArrangementTypes
    @property
    def ArrangementType(self) -> PreferencesBuilder.ArrangementTypes:
        """
        Getter for property: (@link PreferencesBuilder.ArrangementTypes NXOpen.AnimationDesigner.PreferencesBuilder.ArrangementTypes@endlink) ArrangementType
         Returns the option specifies the arrangement type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.ArrangementTypes NXOpen.AnimationDesigner.PreferencesBuilder.ArrangementTypes@endlink) ArrangementType

    ##  Returns the option specifies the arrangement type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @ArrangementType.setter
    def ArrangementType(self, arrangementType: PreferencesBuilder.ArrangementTypes):
        """
        Setter for property: (@link PreferencesBuilder.ArrangementTypes NXOpen.AnimationDesigner.PreferencesBuilder.ArrangementTypes@endlink) ArrangementType
         Returns the option specifies the arrangement type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BulletFlexibleMaterialDensity
    ##  Returns the bullet flexible material density expression which specifies the density of a flexible body.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def BulletFlexibleMaterialDensity(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) BulletFlexibleMaterialDensity
         Returns the bullet flexible material density expression which specifies the density of a flexible body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CollisionPrecision
    ##  Returns the collision precision expression.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def CollisionPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) CollisionPrecision
         Returns the collision precision expression.  
             
         
        """
        pass
    
    ## Getter for property: (int) ContactColor
    ##  Returns the color for contact face.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def ContactColor(self) -> int:
        """
        Getter for property: (int) ContactColor
         Returns the color for contact face.  
             
         
        """
        pass
    
    ## Setter for property: (int) ContactColor

    ##  Returns the color for contact face.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ContactColor.setter
    def ContactColor(self, color: int):
        """
        Setter for property: (int) ContactColor
         Returns the color for contact face.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ContactHardnessWithCollisionBody
    ##  Returns the flexible material contact hardness with collision expression which specifies how strict any overlap between a flexible body and collision body is treated.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ContactHardnessWithCollisionBody(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ContactHardnessWithCollisionBody
         Returns the flexible material contact hardness with collision expression which specifies how strict any overlap between a flexible body and collision body is treated.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ContactHardnessWithFlexibleBody
    ##  Returns the flexible material contact hardness with flexible body expression which specifies how strict any overlap between flexible bodies is treated.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ContactHardnessWithFlexibleBody(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ContactHardnessWithFlexibleBody
         Returns the flexible material contact hardness with flexible body expression which specifies how strict any overlap between flexible bodies is treated.  
             
         
        """
        pass
    
    ## Getter for property: (bool) CurveSmoothing
    ##  Returns the smooth curve flag.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def CurveSmoothing(self) -> bool:
        """
        Getter for property: (bool) CurveSmoothing
         Returns the smooth curve flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) CurveSmoothing

    ##  Returns the smooth curve flag.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CurveSmoothing.setter
    def CurveSmoothing(self, isSoomth: bool):
        """
        Setter for property: (bool) CurveSmoothing
         Returns the smooth curve flag.  
             
         
        """
        pass
    
    ## Getter for property: (bool) DelaySolve
    ##  Returns the delay solve flag.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def DelaySolve(self) -> bool:
        """
        Getter for property: (bool) DelaySolve
         Returns the delay solve flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) DelaySolve

    ##  Returns the delay solve flag.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DelaySolve.setter
    def DelaySolve(self, delay_solve: bool):
        """
        Setter for property: (bool) DelaySolve
         Returns the delay solve flag.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EnableParallel
    ##  Returns the enable parallel calculation flag.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def EnableParallel(self) -> bool:
        """
        Getter for property: (bool) EnableParallel
         Returns the enable parallel calculation flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) EnableParallel

    ##  Returns the enable parallel calculation flag.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @EnableParallel.setter
    def EnableParallel(self, enableParallel: bool):
        """
        Setter for property: (bool) EnableParallel
         Returns the enable parallel calculation flag.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ErrorReduction
    ##  Returns the error reduction.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ErrorReduction(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ErrorReduction
         Returns the error reduction.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleCollisionSkipStep
    ##  Returns the flexible collision skip step expression which specifies how many steps to skip when a flexible body collides.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleCollisionSkipStep(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleCollisionSkipStep
         Returns the flexible collision skip step expression which specifies how many steps to skip when a flexible body collides.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FlexibleEngineTuningEnableMultithreading
    ##  Returns the option determines whether to use multithreading.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def FlexibleEngineTuningEnableMultithreading(self) -> bool:
        """
        Getter for property: (bool) FlexibleEngineTuningEnableMultithreading
         Returns the option determines whether to use multithreading.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlexibleEngineTuningEnableMultithreading

    ##  Returns the option determines whether to use multithreading.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @FlexibleEngineTuningEnableMultithreading.setter
    def FlexibleEngineTuningEnableMultithreading(self, flexibleEngineTuningEnableMultithreading: bool):
        """
        Setter for property: (bool) FlexibleEngineTuningEnableMultithreading
         Returns the option determines whether to use multithreading.  
             
         
        """
        pass
    
    ## Getter for property: (int) FlexibleEngineTuningMinNumberOfNodesBetweenAttachments
    ##  Returns the option specifies how many min number of nodes between attachments to create cable.  
    ##      
    ##  
    ## Getter License requirements: nx_mcd_core ("Mechatronics Concept Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def FlexibleEngineTuningMinNumberOfNodesBetweenAttachments(self) -> int:
        """
        Getter for property: (int) FlexibleEngineTuningMinNumberOfNodesBetweenAttachments
         Returns the option specifies how many min number of nodes between attachments to create cable.  
             
         
        """
        pass
    
    ## Setter for property: (int) FlexibleEngineTuningMinNumberOfNodesBetweenAttachments

    ##  Returns the option specifies how many min number of nodes between attachments to create cable.  
    ##      
    ##  
    ## Setter License requirements: nx_mcd_core ("Mechatronics Concept Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FlexibleEngineTuningMinNumberOfNodesBetweenAttachments.setter
    def FlexibleEngineTuningMinNumberOfNodesBetweenAttachments(self, flexibleEngineTuningMinNumberOfNodesBetweenAttachments: int):
        """
        Setter for property: (int) FlexibleEngineTuningMinNumberOfNodesBetweenAttachments
         Returns the option specifies how many min number of nodes between attachments to create cable.  
             
         
        """
        pass
    
    ## Getter for property: (int) FlexibleEngineTuningNumberOfThreads
    ##  Returns the option specifies the number of threads.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return int
    @property
    def FlexibleEngineTuningNumberOfThreads(self) -> int:
        """
        Getter for property: (int) FlexibleEngineTuningNumberOfThreads
         Returns the option specifies the number of threads.  
             
         
        """
        pass
    
    ## Setter for property: (int) FlexibleEngineTuningNumberOfThreads

    ##  Returns the option specifies the number of threads.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @FlexibleEngineTuningNumberOfThreads.setter
    def FlexibleEngineTuningNumberOfThreads(self, flexibleEngineTuningNumberOfThreads: int):
        """
        Setter for property: (int) FlexibleEngineTuningNumberOfThreads
         Returns the option specifies the number of threads.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleEngineTuningPrecision
    ##  Returns the flexible engine tuning precision.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleEngineTuningPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleEngineTuningPrecision
         Returns the flexible engine tuning precision.  
             
         
        """
        pass
    
    ## Getter for property: (int) FlexibleEngineTuningSkipStepsNumber
    ##  Returns the option specifies how many steps to skip during the simulation.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return int
    @property
    def FlexibleEngineTuningSkipStepsNumber(self) -> int:
        """
        Getter for property: (int) FlexibleEngineTuningSkipStepsNumber
         Returns the option specifies how many steps to skip during the simulation.  
             
         
        """
        pass
    
    ## Setter for property: (int) FlexibleEngineTuningSkipStepsNumber

    ##  Returns the option specifies how many steps to skip during the simulation.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FlexibleEngineTuningSkipStepsNumber.setter
    def FlexibleEngineTuningSkipStepsNumber(self, flexibleEngineTuningSkipStepsNumber: int):
        """
        Setter for property: (int) FlexibleEngineTuningSkipStepsNumber
         Returns the option specifies how many steps to skip during the simulation.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyAngularPrecision
    ##  Returns the flexible facet body angular precision.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    ## @return PreferencesBuilder.KineoFlexibleFacetBodyPrecision
    @property
    def FlexibleFacetBodyAngularPrecision(self) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
        """
        Getter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyAngularPrecision
         Returns the flexible facet body angular precision.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyAngularPrecision

    ##  Returns the flexible facet body angular precision.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    @FlexibleFacetBodyAngularPrecision.setter
    def FlexibleFacetBodyAngularPrecision(self, precision: PreferencesBuilder.KineoFlexibleFacetBodyPrecision):
        """
        Setter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyAngularPrecision
         Returns the flexible facet body angular precision.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyFacetPrecisionOption
    ##  Returns the fineness of the facets and the smoothness of a circular cross section in a flexible body.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return PreferencesBuilder.KineoFlexibleFacetBodyPrecision
    @property
    def FlexibleFacetBodyFacetPrecisionOption(self) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
        """
        Getter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyFacetPrecisionOption
         Returns the fineness of the facets and the smoothness of a circular cross section in a flexible body.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyFacetPrecisionOption

    ##  Returns the fineness of the facets and the smoothness of a circular cross section in a flexible body.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FlexibleFacetBodyFacetPrecisionOption.setter
    def FlexibleFacetBodyFacetPrecisionOption(self, precision: PreferencesBuilder.KineoFlexibleFacetBodyPrecision):
        """
        Setter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyFacetPrecisionOption
         Returns the fineness of the facets and the smoothness of a circular cross section in a flexible body.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyLinearPrecision
    ##  Returns the flexible facet body linear precision.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    ## @return PreferencesBuilder.KineoFlexibleFacetBodyPrecision
    @property
    def FlexibleFacetBodyLinearPrecision(self) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
        """
        Getter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyLinearPrecision
         Returns the flexible facet body linear precision.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyLinearPrecision

    ##  Returns the flexible facet body linear precision.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    @FlexibleFacetBodyLinearPrecision.setter
    def FlexibleFacetBodyLinearPrecision(self, precision: PreferencesBuilder.KineoFlexibleFacetBodyPrecision):
        """
        Setter for property: (@link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink) FlexibleFacetBodyLinearPrecision
         Returns the flexible facet body linear precision.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetBodyPrecision
    ##  Returns the flexible facet body precision.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleFacetBodyPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetBodyPrecision
         Returns the flexible facet body precision.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FlexibleFacetBodySameWithEngineTuningPrecision
    ##  Returns the option determines whether facet bodies should use the same precision as engine tuning.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    ## @return bool
    @property
    def FlexibleFacetBodySameWithEngineTuningPrecision(self) -> bool:
        """
        Getter for property: (bool) FlexibleFacetBodySameWithEngineTuningPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlexibleFacetBodySameWithEngineTuningPrecision

    ##  Returns the option determines whether facet bodies should use the same precision as engine tuning.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  This functionality is no longer supported.  <br> 

    @FlexibleFacetBodySameWithEngineTuningPrecision.setter
    def FlexibleFacetBodySameWithEngineTuningPrecision(self, flexibleFacetBodySameWithEngineTuningPrecision: bool):
        """
        Setter for property: (bool) FlexibleFacetBodySameWithEngineTuningPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetBodyUserDefinedAngularPrecision
    ##  Returns the flexible facet body user defined angular precision.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleFacetBodyUserDefinedAngularPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetBodyUserDefinedAngularPrecision
         Returns the flexible facet body user defined angular precision.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetBodyUserDefinedLinearPrecision
    ##  Returns the flexible facet body user defined linear precision.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleFacetBodyUserDefinedLinearPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetBodyUserDefinedLinearPrecision
         Returns the flexible facet body user defined linear precision.  
             
         
        """
        pass
    
    ## Getter for property: (float) FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage
    ##  Returns the user defined linear precision percentage of a kineo facet body.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return float
    @property
    def FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage(self) -> float:
        """
        Getter for property: (float) FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage
         Returns the user defined linear precision percentage of a kineo facet body.  
             
         
        """
        pass
    
    ## Setter for property: (float) FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage

    ##  Returns the user defined linear precision percentage of a kineo facet body.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage.setter
    def FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage(self, precision: float):
        """
        Setter for property: (float) FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage
         Returns the user defined linear precision percentage of a kineo facet body.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes@endlink) FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType
    ##  Returns the option determines whether to use a length value instead of a percentage.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes
    @property
    def FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType(self) -> PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes:
        """
        Getter for property: (@link PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes@endlink) FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType
         Returns the option determines whether to use a length value instead of a percentage.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes@endlink) FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType

    ##  Returns the option determines whether to use a length value instead of a percentage.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType.setter
    def FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType(self, inputType: PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes):
        """
        Setter for property: (@link PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes@endlink) FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType
         Returns the option determines whether to use a length value instead of a percentage.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetPrecision
    ##  Returns the flexible facet precision expression which specifies the fineness of the facets in a flexible body.  
    ##    A larger value means larger facets and relatively better simulation performance.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleFacetPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleFacetPrecision
         Returns the flexible facet precision expression which specifies the fineness of the facets in a flexible body.  
           A larger value means larger facets and relatively better simulation performance.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialAnchorHardness
    ##  Returns the flexible material anchor hardness expression which specifies how strongly a flexible body is expected to stick to another object, e.  
    ##   g. a roller.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialAnchorHardness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialAnchorHardness
         Returns the flexible material anchor hardness expression which specifies how strongly a flexible body is expected to stick to another object, e.  
          g. a roller.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialDamping
    ##  Returns the flexible material damping expression which specifies the coefficient of damping forces acting on flexible bodies to reduce their oscillation over time.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialDamping(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialDamping
         Returns the flexible material damping expression which specifies the coefficient of damping forces acting on flexible bodies to reduce their oscillation over time.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialDensity
    ##  Returns the flexible material density expression which specifies the density of a flexible body.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialDensity(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialDensity
         Returns the flexible material density expression which specifies the density of a flexible body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialDynamicFriction
    ##  Returns the flexible material dynamic friction expression which specifies the coefficient of the dynamic friction acting on a flexible body against a surface.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialDynamicFriction(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialDynamicFriction
         Returns the flexible material dynamic friction expression which specifies the coefficient of the dynamic friction acting on a flexible body against a surface.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FlexibleMaterialEnableMaxContactForce
    ##  Returns the option determines whether to set the maximum contact force.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def FlexibleMaterialEnableMaxContactForce(self) -> bool:
        """
        Getter for property: (bool) FlexibleMaterialEnableMaxContactForce
         Returns the option determines whether to set the maximum contact force.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlexibleMaterialEnableMaxContactForce

    ##  Returns the option determines whether to set the maximum contact force.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FlexibleMaterialEnableMaxContactForce.setter
    def FlexibleMaterialEnableMaxContactForce(self, flexibleMaterialEnableMaxContactForce: bool):
        """
        Setter for property: (bool) FlexibleMaterialEnableMaxContactForce
         Returns the option determines whether to set the maximum contact force.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FlexibleMaterialEnableMaxTwist
    ##  Returns the option determines whether to set the maximum twist.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def FlexibleMaterialEnableMaxTwist(self) -> bool:
        """
        Getter for property: (bool) FlexibleMaterialEnableMaxTwist
         Returns the option determines whether to set the maximum twist.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlexibleMaterialEnableMaxTwist

    ##  Returns the option determines whether to set the maximum twist.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FlexibleMaterialEnableMaxTwist.setter
    def FlexibleMaterialEnableMaxTwist(self, flexibleMaterialEnableMaxTwist: bool):
        """
        Setter for property: (bool) FlexibleMaterialEnableMaxTwist
         Returns the option determines whether to set the maximum twist.  
             
         
        """
        pass
    
    ## Getter for property: (bool) FlexibleMaterialEnableMinCurvature
    ##  Returns the option determines whether to set the minimum curvature.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return bool
    @property
    def FlexibleMaterialEnableMinCurvature(self) -> bool:
        """
        Getter for property: (bool) FlexibleMaterialEnableMinCurvature
         Returns the option determines whether to set the minimum curvature.  
             
         
        """
        pass
    
    ## Setter for property: (bool) FlexibleMaterialEnableMinCurvature

    ##  Returns the option determines whether to set the minimum curvature.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FlexibleMaterialEnableMinCurvature.setter
    def FlexibleMaterialEnableMinCurvature(self, flexibleMaterialEnableMinCurvature: bool):
        """
        Setter for property: (bool) FlexibleMaterialEnableMinCurvature
         Returns the option determines whether to set the minimum curvature.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialFulcrumLength
    ##  Returns the flexible material fulcrum length.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialFulcrumLength(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialFulcrumLength
         Returns the flexible material fulcrum length.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialLinearStiffness
    ##  Returns the flexible material linear stiffness expression which specifies the coefficient of conservation of distance between adjacent particles.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialLinearStiffness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialLinearStiffness
         Returns the flexible material linear stiffness expression which specifies the coefficient of conservation of distance between adjacent particles.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMaxContactForce
    ##  Returns the flexible material maximum contact force.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialMaxContactForce(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMaxContactForce
         Returns the flexible material maximum contact force.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMaxTension
    ##  Returns the flexible material maximum tension.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialMaxTension(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMaxTension
         Returns the flexible material maximum tension.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMaxTwist
    ##  Returns the flexible material maximum twist.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialMaxTwist(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMaxTwist
         Returns the flexible material maximum twist.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMinCurvature
    ##  Returns the flexible material minimum curvature.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialMinCurvature(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialMinCurvature
         Returns the flexible material minimum curvature.  
             
         
        """
        pass
    
    ## Getter for property: (float) FlexibleMaterialOscillation
    ##  Returns the flexible material oscillation.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def FlexibleMaterialOscillation(self) -> float:
        """
        Getter for property: (float) FlexibleMaterialOscillation
         Returns the flexible material oscillation.  
             
         
        """
        pass
    
    ## Setter for property: (float) FlexibleMaterialOscillation

    ##  Returns the flexible material oscillation.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @FlexibleMaterialOscillation.setter
    def FlexibleMaterialOscillation(self, flexibleMaterialOscillation: float):
        """
        Setter for property: (float) FlexibleMaterialOscillation
         Returns the flexible material oscillation.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialPrecision
    ##  Returns the flexible material precision expression which specifies the fineness of the elements in a flexible body.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialPrecision
         Returns the flexible material precision expression which specifies the fineness of the elements in a flexible body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialYoungModulus
    ##  Returns the flexible material Young's modulus.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def FlexibleMaterialYoungModulus(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) FlexibleMaterialYoungModulus
         Returns the flexible material Young's modulus.  
             
         
        """
        pass
    
    ## Getter for property: (int) FlowLineColor
    ##  Returns the flow line color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def FlowLineColor(self) -> int:
        """
        Getter for property: (int) FlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    
    ## Setter for property: (int) FlowLineColor

    ##  Returns the flow line color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @FlowLineColor.setter
    def FlowLineColor(self, flowlinecolor: int):
        """
        Setter for property: (int) FlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.FlowLineStyleTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlowLineStyleTypes@endlink) FlowLineFont
    ##  Returns the flow line font.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return PreferencesBuilder.FlowLineStyleTypes
    @property
    def FlowLineFont(self) -> PreferencesBuilder.FlowLineStyleTypes:
        """
        Getter for property: (@link PreferencesBuilder.FlowLineStyleTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlowLineStyleTypes@endlink) FlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.FlowLineStyleTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlowLineStyleTypes@endlink) FlowLineFont

    ##  Returns the flow line font.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @FlowLineFont.setter
    def FlowLineFont(self, flowlinefont: PreferencesBuilder.FlowLineStyleTypes):
        """
        Setter for property: (@link PreferencesBuilder.FlowLineStyleTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlowLineStyleTypes@endlink) FlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    
    ## Getter for property: (int) FlowLineWidth
    ##  Returns the flow line width.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def FlowLineWidth(self) -> int:
        """
        Getter for property: (int) FlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    
    ## Setter for property: (int) FlowLineWidth

    ##  Returns the flow line width.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @FlowLineWidth.setter
    def FlowLineWidth(self, flowlinewidth: int):
        """
        Setter for property: (int) FlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.GraphPlotTypes NXOpen.AnimationDesigner.PreferencesBuilder.GraphPlotTypes@endlink) GraphPlotType
    ##  Returns the option specifies the graph plot type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return PreferencesBuilder.GraphPlotTypes
    @property
    def GraphPlotType(self) -> PreferencesBuilder.GraphPlotTypes:
        """
        Getter for property: (@link PreferencesBuilder.GraphPlotTypes NXOpen.AnimationDesigner.PreferencesBuilder.GraphPlotTypes@endlink) GraphPlotType
         Returns the option specifies the graph plot type.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.GraphPlotTypes NXOpen.AnimationDesigner.PreferencesBuilder.GraphPlotTypes@endlink) GraphPlotType

    ##  Returns the option specifies the graph plot type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @GraphPlotType.setter
    def GraphPlotType(self, plotType: PreferencesBuilder.GraphPlotTypes):
        """
        Setter for property: (@link PreferencesBuilder.GraphPlotTypes NXOpen.AnimationDesigner.PreferencesBuilder.GraphPlotTypes@endlink) GraphPlotType
         Returns the option specifies the graph plot type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GraphSampleTime
    ##  Returns the graph sample time expression.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def GraphSampleTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) GraphSampleTime
         Returns the graph sample time expression.  
             
         
        """
        pass
    
    ## Getter for property: (int) GravityDirection
    ##  Returns the gravity direction.  
    ##    0 - Gx, 1 - Gy, 2 - Gz, 3 - None.  
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def GravityDirection(self) -> int:
        """
        Getter for property: (int) GravityDirection
         Returns the gravity direction.  
           0 - Gx, 1 - Gy, 2 - Gz, 3 - None.  
         
        """
        pass
    
    ## Setter for property: (int) GravityDirection

    ##  Returns the gravity direction.  
    ##    0 - Gx, 1 - Gy, 2 - Gz, 3 - None.  
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @GravityDirection.setter
    def GravityDirection(self, direction: int):
        """
        Setter for property: (int) GravityDirection
         Returns the gravity direction.  
           0 - Gx, 1 - Gy, 2 - Gz, 3 - None.  
         
        """
        pass
    
    ## Getter for property: (bool) HideMeasureRuler
    ##  Returns the hide measure ruler flag.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def HideMeasureRuler(self) -> bool:
        """
        Getter for property: (bool) HideMeasureRuler
         Returns the hide measure ruler flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) HideMeasureRuler

    ##  Returns the hide measure ruler flag.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @HideMeasureRuler.setter
    def HideMeasureRuler(self, hide: bool):
        """
        Setter for property: (bool) HideMeasureRuler
         Returns the hide measure ruler flag.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ImpulseSplitWithCollisionBody
    ##  Returns the flexible material impulse split when contact with collision body expression which specifies how to proportion the impulse generated by a collision between a flexible body and collision body.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ImpulseSplitWithCollisionBody(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ImpulseSplitWithCollisionBody
         Returns the flexible material impulse split when contact with collision body expression which specifies how to proportion the impulse generated by a collision between a flexible body and collision body.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ImpulseSplitWithFlexibleBody
    ##  Returns the flexible material impulse split when contact with flexible body expression which specifies how to proportion the impulse generated by a collision between flexible bodies.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ImpulseSplitWithFlexibleBody(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ImpulseSplitWithFlexibleBody
         Returns the flexible material impulse split when contact with flexible body expression which specifies how to proportion the impulse generated by a collision between flexible bodies.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) KineoAngularTolerance
    ##  Returns the kineo angular tolerance.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def KineoAngularTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) KineoAngularTolerance
         Returns the kineo angular tolerance.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) KineoLinearTolerance
    ##  Returns the kineo linear tolerance.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def KineoLinearTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) KineoLinearTolerance
         Returns the kineo linear tolerance.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxIteration
    ##  Returns the max iteration.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxIteration(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxIteration
         Returns the max iteration.  
             
         
        """
        pass
    
    ## Getter for property: (int) NonRigidGroupColor
    ##  Returns the color for non rigid group body.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return int
    @property
    def NonRigidGroupColor(self) -> int:
        """
        Getter for property: (int) NonRigidGroupColor
         Returns the color for non rigid group body.  
             
         
        """
        pass
    
    ## Setter for property: (int) NonRigidGroupColor

    ##  Returns the color for non rigid group body.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @NonRigidGroupColor.setter
    def NonRigidGroupColor(self, color: int):
        """
        Setter for property: (int) NonRigidGroupColor
         Returns the color for non rigid group body.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OnlySimulateActiveDisplayPart
    ##  Returns the only simulate active display part flag.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def OnlySimulateActiveDisplayPart(self) -> bool:
        """
        Getter for property: (bool) OnlySimulateActiveDisplayPart
         Returns the only simulate active display part flag.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OnlySimulateActiveDisplayPart

    ##  Returns the only simulate active display part flag.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @OnlySimulateActiveDisplayPart.setter
    def OnlySimulateActiveDisplayPart(self, bOnly: bool):
        """
        Setter for property: (bool) OnlySimulateActiveDisplayPart
         Returns the only simulate active display part flag.  
             
         
        """
        pass
    
    ## Getter for property: (bool) OptimizeRigidGroupProperty
    ##  Returns the option indicates whether the optimized properties of rigid group are being used.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def OptimizeRigidGroupProperty(self) -> bool:
        """
        Getter for property: (bool) OptimizeRigidGroupProperty
         Returns the option indicates whether the optimized properties of rigid group are being used.  
             
         
        """
        pass
    
    ## Setter for property: (bool) OptimizeRigidGroupProperty

    ##  Returns the option indicates whether the optimized properties of rigid group are being used.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OptimizeRigidGroupProperty.setter
    def OptimizeRigidGroupProperty(self, optimizeRigidProp: bool):
        """
        Setter for property: (bool) OptimizeRigidGroupProperty
         Returns the option indicates whether the optimized properties of rigid group are being used.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.PhysicsEngines NXOpen.AnimationDesigner.PreferencesBuilder.PhysicsEngines@endlink) PhysicsEngine
    ##  Returns the physics engine.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return PreferencesBuilder.PhysicsEngines
    @property
    def PhysicsEngine(self) -> PreferencesBuilder.PhysicsEngines:
        """
        Getter for property: (@link PreferencesBuilder.PhysicsEngines NXOpen.AnimationDesigner.PreferencesBuilder.PhysicsEngines@endlink) PhysicsEngine
         Returns the physics engine.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.PhysicsEngines NXOpen.AnimationDesigner.PreferencesBuilder.PhysicsEngines@endlink) PhysicsEngine

    ##  Returns the physics engine.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @PhysicsEngine.setter
    def PhysicsEngine(self, engine: PreferencesBuilder.PhysicsEngines):
        """
        Setter for property: (@link PreferencesBuilder.PhysicsEngines NXOpen.AnimationDesigner.PreferencesBuilder.PhysicsEngines@endlink) PhysicsEngine
         Returns the physics engine.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.PrecisionPresetModes NXOpen.AnimationDesigner.PreferencesBuilder.PrecisionPresetModes@endlink) PrecisionPresetMode
    ##  Returns the simulation preset mode   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return PreferencesBuilder.PrecisionPresetModes
    @property
    def PrecisionPresetMode(self) -> PreferencesBuilder.PrecisionPresetModes:
        """
        Getter for property: (@link PreferencesBuilder.PrecisionPresetModes NXOpen.AnimationDesigner.PreferencesBuilder.PrecisionPresetModes@endlink) PrecisionPresetMode
         Returns the simulation preset mode   
            
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.PrecisionPresetModes NXOpen.AnimationDesigner.PreferencesBuilder.PrecisionPresetModes@endlink) PrecisionPresetMode

    ##  Returns the simulation preset mode   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @PrecisionPresetMode.setter
    def PrecisionPresetMode(self, presetMode: PreferencesBuilder.PrecisionPresetModes):
        """
        Setter for property: (@link PreferencesBuilder.PrecisionPresetModes NXOpen.AnimationDesigner.PreferencesBuilder.PrecisionPresetModes@endlink) PrecisionPresetMode
         Returns the simulation preset mode   
            
         
        """
        pass
    
    ## Getter for property: (bool) RandomizeSolvingOrder
    ##  Returns the option indicates whether to randomize the solving order by the engine.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def RandomizeSolvingOrder(self) -> bool:
        """
        Getter for property: (bool) RandomizeSolvingOrder
         Returns the option indicates whether to randomize the solving order by the engine.  
             
         
        """
        pass
    
    ## Setter for property: (bool) RandomizeSolvingOrder

    ##  Returns the option indicates whether to randomize the solving order by the engine.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @RandomizeSolvingOrder.setter
    def RandomizeSolvingOrder(self, randomOrder: bool):
        """
        Setter for property: (bool) RandomizeSolvingOrder
         Returns the option indicates whether to randomize the solving order by the engine.  
             
         
        """
        pass
    
    ## Getter for property: (bool) RichGeomType
    ##  Returns the rich geometry type.  
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def RichGeomType(self) -> bool:
        """
        Getter for property: (bool) RichGeomType
         Returns the rich geometry type.  
            
         
        """
        pass
    
    ## Setter for property: (bool) RichGeomType

    ##  Returns the rich geometry type.  
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RichGeomType.setter
    def RichGeomType(self, richGeomType: bool):
        """
        Setter for property: (bool) RichGeomType
         Returns the rich geometry type.  
            
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.RigidGroupSelectionDisplayTypes NXOpen.AnimationDesigner.PreferencesBuilder.RigidGroupSelectionDisplayTypes@endlink) RigidGroupSelectionDisplay
    ##  Returns the option specifies the selection display for rigid groups.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PreferencesBuilder.RigidGroupSelectionDisplayTypes
    @property
    def RigidGroupSelectionDisplay(self) -> PreferencesBuilder.RigidGroupSelectionDisplayTypes:
        """
        Getter for property: (@link PreferencesBuilder.RigidGroupSelectionDisplayTypes NXOpen.AnimationDesigner.PreferencesBuilder.RigidGroupSelectionDisplayTypes@endlink) RigidGroupSelectionDisplay
         Returns the option specifies the selection display for rigid groups.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.RigidGroupSelectionDisplayTypes NXOpen.AnimationDesigner.PreferencesBuilder.RigidGroupSelectionDisplayTypes@endlink) RigidGroupSelectionDisplay

    ##  Returns the option specifies the selection display for rigid groups.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RigidGroupSelectionDisplay.setter
    def RigidGroupSelectionDisplay(self, displayType: PreferencesBuilder.RigidGroupSelectionDisplayTypes):
        """
        Setter for property: (@link PreferencesBuilder.RigidGroupSelectionDisplayTypes NXOpen.AnimationDesigner.PreferencesBuilder.RigidGroupSelectionDisplayTypes@endlink) RigidGroupSelectionDisplay
         Returns the option specifies the selection display for rigid groups.  
             
         
        """
        pass
    
    ## Getter for property: (bool) SameWithFlexibleMaterialPrecision
    ##  Returns the option determines whether facet bodies should use the same precision as engine tuning.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def SameWithFlexibleMaterialPrecision(self) -> bool:
        """
        Getter for property: (bool) SameWithFlexibleMaterialPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    
    ## Setter for property: (bool) SameWithFlexibleMaterialPrecision

    ##  Returns the option determines whether facet bodies should use the same precision as engine tuning.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @SameWithFlexibleMaterialPrecision.setter
    def SameWithFlexibleMaterialPrecision(self, sameWithFlexibleMaterialPrecision: bool):
        """
        Setter for property: (bool) SameWithFlexibleMaterialPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    
    ## Getter for property: (bool) ShowFlowLine
    ##  Returns the option for enable draw flow line.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ShowFlowLine(self) -> bool:
        """
        Getter for property: (bool) ShowFlowLine
         Returns the option for enable draw flow line.  
             
         
        """
        pass
    
    ## Setter for property: (bool) ShowFlowLine

    ##  Returns the option for enable draw flow line.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ShowFlowLine.setter
    def ShowFlowLine(self, showflowline: bool):
        """
        Setter for property: (bool) ShowFlowLine
         Returns the option for enable draw flow line.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.SolutionSearchScopeTypes NXOpen.AnimationDesigner.PreferencesBuilder.SolutionSearchScopeTypes@endlink) SolutionSearchScope
    ##  Returns the option specifies the search scope for the Animation Designer definition.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PreferencesBuilder.SolutionSearchScopeTypes
    @property
    def SolutionSearchScope(self) -> PreferencesBuilder.SolutionSearchScopeTypes:
        """
        Getter for property: (@link PreferencesBuilder.SolutionSearchScopeTypes NXOpen.AnimationDesigner.PreferencesBuilder.SolutionSearchScopeTypes@endlink) SolutionSearchScope
         Returns the option specifies the search scope for the Animation Designer definition.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.SolutionSearchScopeTypes NXOpen.AnimationDesigner.PreferencesBuilder.SolutionSearchScopeTypes@endlink) SolutionSearchScope

    ##  Returns the option specifies the search scope for the Animation Designer definition.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SolutionSearchScope.setter
    def SolutionSearchScope(self, scopeType: PreferencesBuilder.SolutionSearchScopeTypes):
        """
        Setter for property: (@link PreferencesBuilder.SolutionSearchScopeTypes NXOpen.AnimationDesigner.PreferencesBuilder.SolutionSearchScopeTypes@endlink) SolutionSearchScope
         Returns the option specifies the search scope for the Animation Designer definition.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StepIncrementTime
    ##  Returns the step time expression.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StepIncrementTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StepIncrementTime
         Returns the step time expression.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StepTime
    ##  Returns the step time.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StepTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StepTime
         Returns the step time.  
             
         
        """
        pass
    
    ## Getter for property: (float) TimeScaleFactor
    ##  Returns the time scale factor   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return float
    @property
    def TimeScaleFactor(self) -> float:
        """
        Getter for property: (float) TimeScaleFactor
         Returns the time scale factor   
            
         
        """
        pass
    
    ## Setter for property: (float) TimeScaleFactor

    ##  Returns the time scale factor   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    @TimeScaleFactor.setter
    def TimeScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) TimeScaleFactor
         Returns the time scale factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Tolerance
    ##  Returns the tolerance.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Tolerance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Tolerance
         Returns the tolerance.  
             
         
        """
        pass
    
    ## Getter for property: (@link PreferencesBuilder.BodyToUseForMeasureTypes NXOpen.AnimationDesigner.PreferencesBuilder.BodyToUseForMeasureTypes@endlink) UseFacetToMeasure
    ##  Returns the option indicates whether to use facet body instead of solid body to measure distance or angle in order to improve performance.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PreferencesBuilder.BodyToUseForMeasureTypes
    @property
    def UseFacetToMeasure(self) -> PreferencesBuilder.BodyToUseForMeasureTypes:
        """
        Getter for property: (@link PreferencesBuilder.BodyToUseForMeasureTypes NXOpen.AnimationDesigner.PreferencesBuilder.BodyToUseForMeasureTypes@endlink) UseFacetToMeasure
         Returns the option indicates whether to use facet body instead of solid body to measure distance or angle in order to improve performance.  
             
         
        """
        pass
    
    ## Setter for property: (@link PreferencesBuilder.BodyToUseForMeasureTypes NXOpen.AnimationDesigner.PreferencesBuilder.BodyToUseForMeasureTypes@endlink) UseFacetToMeasure

    ##  Returns the option indicates whether to use facet body instead of solid body to measure distance or angle in order to improve performance.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @UseFacetToMeasure.setter
    def UseFacetToMeasure(self, bodyType: PreferencesBuilder.BodyToUseForMeasureTypes):
        """
        Setter for property: (@link PreferencesBuilder.BodyToUseForMeasureTypes NXOpen.AnimationDesigner.PreferencesBuilder.BodyToUseForMeasureTypes@endlink) UseFacetToMeasure
         Returns the option indicates whether to use facet body instead of solid body to measure distance or angle in order to improve performance.  
             
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::RackPinionBuilder NXOpen::AnimationDesigner::RackPinionBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::RackPinionCollection::CreateRackPinionBuilder  NXOpen::AnimationDesigner::RackPinionCollection::CreateRackPinionBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RackPinionBuilder(CouplerBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.RackPinionBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ContactPoint
    ##  Returns the contact point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def ContactPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) ContactPoint
         Returns the contact point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ContactPoint

    ##  Returns the contact point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ContactPoint.setter
    def ContactPoint(self, contactPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) ContactPoint
         Returns the contact point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
    ##  Returns the radius expression.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Radius
         Returns the radius expression.  
             
         
        """
        pass
    
import NXOpen
##  Represents a collection of Rack Pinion objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RackPinionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Rack Pinion objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::RackPinionBuilder NXOpen::AnimationDesigner::RackPinionBuilder@endlink . 
    ##  @return builder (@link RackPinionBuilder NXOpen.AnimationDesigner.RackPinionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="rackPinion"> (@link RackPinion NXOpen.AnimationDesigner.RackPinion@endlink)  @link NXOpen::AnimationDesigner::RackPinion NXOpen::AnimationDesigner::RackPinion@endlink  to be edited, if NULL then create a new one </param>
    def CreateRackPinionBuilder(part: NXOpen.Part, rackPinion: RackPinion) -> RackPinionBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::RackPinionBuilder NXOpen::AnimationDesigner::RackPinionBuilder@endlink . 
         @return builder (@link RackPinionBuilder NXOpen.AnimationDesigner.RackPinionBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::RackPinion   NXOpen::AnimationDesigner::RackPinion @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return rackPinion (@link RackPinion NXOpen.AnimationDesigner.RackPinion@endlink):  @link  NXOpen::AnimationDesigner::RackPinion   NXOpen::AnimationDesigner::RackPinion @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::RackPinion   NXOpen::AnimationDesigner::RackPinion @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> RackPinion:
        """
         Finds the @link  NXOpen::AnimationDesigner::RackPinion   NXOpen::AnimationDesigner::RackPinion @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return rackPinion (@link RackPinion NXOpen.AnimationDesigner.RackPinion@endlink):  @link  NXOpen::AnimationDesigner::RackPinion   NXOpen::AnimationDesigner::RackPinion @endlink  with this name. .
        """
        pass
    
##  Represents a Rack Pinion feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::RackPinionBuilder  NXOpen::AnimationDesigner::RackPinionBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RackPinion(Coupler): 
    """ Represents a Rack Pinion feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::RevoluteJointBuilder NXOpen::AnimationDesigner::RevoluteJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::RevoluteJointCollection::CreateRevoluteJointBuilder  NXOpen::AnimationDesigner::RevoluteJointCollection::CreateRevoluteJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RevoluteJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.RevoluteJointBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##  Returns the axis vector.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##  Returns the axis vector.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    
    ## Getter for property: (bool) EnableLowerLimit
    ##  Returns the lower limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied a lower limit in movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableLowerLimit

    ##  Returns the lower limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied a lower limit in movement.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableLowerLimit.setter
    def EnableLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.   
         
        """
        pass
    
    ## Getter for property: (bool) EnableUpperLimit
    ##  Returns the upper limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied an upper limit in movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableUpperLimit

    ##  Returns the upper limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied an upper limit in movement.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableUpperLimit.setter
    def EnableUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimit
    ##  Returns the lower limit.  
    ##    The lower limit setup for joint movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimit
         Returns the lower limit.  
           The lower limit setup for joint movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
    ##  Returns the origin point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the origin point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point

    ##  Returns the origin point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) Point
         Returns the origin point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartAngle
    ##  Returns the start angle.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Expression
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartAngle
         Returns the start angle.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimit
    ##  Returns the upper limit.  
    ##    The upper limit setup for joint movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def UpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimit
         Returns the upper limit.  
           The upper limit setup for joint movement.   
         
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a collection of Revolute Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RevoluteJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Revolute Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::RevoluteJointBuilder NXOpen::AnimationDesigner::RevoluteJointBuilder@endlink . 
    ##  @return builder (@link RevoluteJointBuilder NXOpen.AnimationDesigner.RevoluteJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="hingeJoint"> (@link RevoluteJoint NXOpen.AnimationDesigner.RevoluteJoint@endlink)  @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  to be edited, if NULL then create a new one </param>
    @overload
    def CreateRevoluteJointBuilder(part: NXOpen.Part, hingeJoint: RevoluteJoint) -> RevoluteJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::RevoluteJointBuilder NXOpen::AnimationDesigner::RevoluteJointBuilder@endlink . 
         @return builder (@link RevoluteJointBuilder NXOpen.AnimationDesigner.RevoluteJointBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::AnimationDesigner::RevoluteJointBuilder NXOpen::AnimationDesigner::RevoluteJointBuilder@endlink . 
    ##  @return builder (@link RevoluteJointBuilder NXOpen.AnimationDesigner.RevoluteJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="hingeJoint"> (@link RevoluteJoint NXOpen.AnimationDesigner.RevoluteJoint@endlink)  @link NXOpen::AnimationDesigner::RevoluteJoint NXOpen::AnimationDesigner::RevoluteJoint@endlink  to be edited, if NULL then create a new one </param>
    ## <param name="partOcc"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  for the edited revolute joint occurrence </param>
    @overload
    def CreateRevoluteJointBuilder(part: NXOpen.Part, hingeJoint: RevoluteJoint, partOcc: NXOpen.Assemblies.Component) -> RevoluteJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::RevoluteJointBuilder NXOpen::AnimationDesigner::RevoluteJointBuilder@endlink . 
         @return builder (@link RevoluteJointBuilder NXOpen.AnimationDesigner.RevoluteJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::RevoluteJoint   NXOpen::AnimationDesigner::RevoluteJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return revoluteJoint (@link RevoluteJoint NXOpen.AnimationDesigner.RevoluteJoint@endlink):  @link  NXOpen::AnimationDesigner::RevoluteJoint   NXOpen::AnimationDesigner::RevoluteJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::RevoluteJoint   NXOpen::AnimationDesigner::RevoluteJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> RevoluteJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::RevoluteJoint   NXOpen::AnimationDesigner::RevoluteJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return revoluteJoint (@link RevoluteJoint NXOpen.AnimationDesigner.RevoluteJoint@endlink):  @link  NXOpen::AnimationDesigner::RevoluteJoint   NXOpen::AnimationDesigner::RevoluteJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Revolute Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::RevoluteJointBuilder  NXOpen::AnimationDesigner::RevoluteJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RevoluteJoint(PhysicsJoint): 
    """ Represents a Revolute Joint feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::RigidGroupBuilder NXOpen::AnimationDesigner::RigidGroupBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::RigidGroupCollection::CreateRigidGroupBuilder  NXOpen::AnimationDesigner::RigidGroupCollection::CreateRigidGroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RigidGroupBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.RigidGroupBuilder</ja_class>. """


    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the group </description> </item><item><term> 
    ## AutomaticColor</term><description> 
    ##  Auto-assigns a color to each group </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the groups </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <AutomaticColor> <NoColor>
        """
        SpecifyColor: int
        AutomaticColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RigidGroupBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the creation types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Combine</term><description> 
    ##  Combine selections into one Rigid Group </description> </item><item><term> 
    ## Separate</term><description> 
    ##  Create a Rigid Group for each selection </description> </item></list>
    class CreationTypes(Enum):
        """
        Members Include: <Combine> <Separate>
        """
        Combine: int
        Separate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RigidGroupBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the mass property options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Automatic</term><description> 
    ##  automatic </description> </item><item><term> 
    ## UserDefined</term><description> 
    ##  user defined </description> </item></list>
    class MassPropertiesOption(Enum):
        """
        Members Include: <Automatic> <UserDefined>
        """
        Automatic: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> RigidGroupBuilder.MassPropertiesOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AngularVelocityDirection
    ##  Returns the angular velocity direction.  
    ##    It is only used when angular velocity is not zero.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def AngularVelocityDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AngularVelocityDirection
         Returns the angular velocity direction.  
           It is only used when angular velocity is not zero.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AngularVelocityDirection

    ##  Returns the angular velocity direction.  
    ##    It is only used when angular velocity is not zero.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AngularVelocityDirection.setter
    def AngularVelocityDirection(self, dir: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AngularVelocityDirection
         Returns the angular velocity direction.  
           It is only used when angular velocity is not zero.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularVelocityMagnitude
    ##  Returns the angular velocity magnitude.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def AngularVelocityMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) AngularVelocityMagnitude
         Returns the angular velocity magnitude.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link RigidGroupBuilder.ColorOptions NXOpen.AnimationDesigner.RigidGroupBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return RigidGroupBuilder.ColorOptions
    @property
    def ColorOption(self) -> RigidGroupBuilder.ColorOptions:
        """
        Getter for property: (@link RigidGroupBuilder.ColorOptions NXOpen.AnimationDesigner.RigidGroupBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Setter for property: (@link RigidGroupBuilder.ColorOptions NXOpen.AnimationDesigner.RigidGroupBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: RigidGroupBuilder.ColorOptions):
        """
        Setter for property: (@link RigidGroupBuilder.ColorOptions NXOpen.AnimationDesigner.RigidGroupBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Getter for property: (@link RigidGroupBuilder.CreationTypes NXOpen.AnimationDesigner.RigidGroupBuilder.CreationTypes@endlink) CreationType
    ##  Returns the creation type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return RigidGroupBuilder.CreationTypes
    @property
    def CreationType(self) -> RigidGroupBuilder.CreationTypes:
        """
        Getter for property: (@link RigidGroupBuilder.CreationTypes NXOpen.AnimationDesigner.RigidGroupBuilder.CreationTypes@endlink) CreationType
         Returns the creation type.  
             
         
        """
        pass
    
    ## Setter for property: (@link RigidGroupBuilder.CreationTypes NXOpen.AnimationDesigner.RigidGroupBuilder.CreationTypes@endlink) CreationType

    ##  Returns the creation type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @CreationType.setter
    def CreationType(self, creationType: RigidGroupBuilder.CreationTypes):
        """
        Setter for property: (@link RigidGroupBuilder.CreationTypes NXOpen.AnimationDesigner.RigidGroupBuilder.CreationTypes@endlink) CreationType
         Returns the creation type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Geometry
    ##  Returns the geometries.  
    ##    This can be @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink ,
    ##             @link NXOpen::Point NXOpen::Point@endlink , @link NXOpen::Body NXOpen::Body@endlink , @link NXOpen::Curve NXOpen::Curve@endlink ,
    ##             @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink , @link NXOpen::DatumAxis NXOpen::DatumAxis@endlink ,
    ##             @link NXOpen::DatumPlane NXOpen::DatumPlane@endlink , @link NXOpen::Annotations::Pmi NXOpen::Annotations::Pmi@endlink ,
    ##             Line Designer Connectors, etc.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Geometry(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Geometry
         Returns the geometries.  
           This can be @link NXOpen::Assemblies::ComponentAssembly NXOpen::Assemblies::ComponentAssembly@endlink ,
                    @link NXOpen::Point NXOpen::Point@endlink , @link NXOpen::Body NXOpen::Body@endlink , @link NXOpen::Curve NXOpen::Curve@endlink ,
                    @link NXOpen::CoordinateSystem NXOpen::CoordinateSystem@endlink , @link NXOpen::DatumAxis NXOpen::DatumAxis@endlink ,
                    @link NXOpen::DatumPlane NXOpen::DatumPlane@endlink , @link NXOpen::Annotations::Pmi NXOpen::Annotations::Pmi@endlink ,
                    Line Designer Connectors, etc.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIxx
    ##  Returns the inertia Ixx.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaIxx(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIxx
         Returns the inertia Ixx.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIxy
    ##  Returns the inertia Ixy.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaIxy(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIxy
         Returns the inertia Ixy.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIxz
    ##  Returns the inertia Ixz.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaIxz(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIxz
         Returns the inertia Ixz.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIyy
    ##  Returns the inertia Iyy.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaIyy(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIyy
         Returns the inertia Iyy.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIyz
    ##  Returns the inertia Iyz.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaIyz(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIyz
         Returns the inertia Iyz.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIzz
    ##  Returns the inertia Izz.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def InertiaIzz(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) InertiaIzz
         Returns the inertia Izz.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearVelocityDirection
    ##  Returns the linear velocity.  
    ##    It is only used when linear velocity is not zero.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def LinearVelocityDirection(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearVelocityDirection
         Returns the linear velocity.  
           It is only used when linear velocity is not zero.   
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearVelocityDirection

    ##  Returns the linear velocity.  
    ##    It is only used when linear velocity is not zero.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LinearVelocityDirection.setter
    def LinearVelocityDirection(self, dir: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) LinearVelocityDirection
         Returns the linear velocity.  
           It is only used when linear velocity is not zero.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearVelocityMagnitude
    ##  Returns the linear velocity magnitude.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LinearVelocityMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LinearVelocityMagnitude
         Returns the linear velocity magnitude.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
    ##  Returns the mass.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Mass
         Returns the mass.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MassCenterPoint
    ##  Returns the mass center point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def MassCenterPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) MassCenterPoint
         Returns the mass center point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MassCenterPoint

    ##  Returns the mass center point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MassCenterPoint.setter
    def MassCenterPoint(self, center: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) MassCenterPoint
         Returns the mass center point.  
             
         
        """
        pass
    
    ## Getter for property: (@link RigidGroupBuilder.MassPropertiesOption NXOpen.AnimationDesigner.RigidGroupBuilder.MassPropertiesOption@endlink) MassProperty
    ##  Returns the auto-calculate mass property flag which is used to indicate whether
    ##             all mass properties are calculated by system.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return RigidGroupBuilder.MassPropertiesOption
    @property
    def MassProperty(self) -> RigidGroupBuilder.MassPropertiesOption:
        """
        Getter for property: (@link RigidGroupBuilder.MassPropertiesOption NXOpen.AnimationDesigner.RigidGroupBuilder.MassPropertiesOption@endlink) MassProperty
         Returns the auto-calculate mass property flag which is used to indicate whether
                    all mass properties are calculated by system.  
             
         
        """
        pass
    
    ## Setter for property: (@link RigidGroupBuilder.MassPropertiesOption NXOpen.AnimationDesigner.RigidGroupBuilder.MassPropertiesOption@endlink) MassProperty

    ##  Returns the auto-calculate mass property flag which is used to indicate whether
    ##             all mass properties are calculated by system.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @MassProperty.setter
    def MassProperty(self, massProperty: RigidGroupBuilder.MassPropertiesOption):
        """
        Setter for property: (@link RigidGroupBuilder.MassPropertiesOption NXOpen.AnimationDesigner.RigidGroupBuilder.MassPropertiesOption@endlink) MassProperty
         Returns the auto-calculate mass property flag which is used to indicate whether
                    all mass properties are calculated by system.  
             
         
        """
        pass
    
    ## Getter for property: (str) Name
    ##  Returns the name.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Orientation
    ##  Returns the orientation.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Orientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Orientation
         Returns the orientation.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Orientation

    ##  Returns the orientation.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Orientation.setter
    def Orientation(self, orientation: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Orientation
         Returns the orientation.  
             
         
        """
        pass
    
import NXOpen
##  Represents a collection of Rigid Group objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RigidGroupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Rigid Group objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::RigidGroupBuilder NXOpen::AnimationDesigner::RigidGroupBuilder@endlink . 
    ##  @return builder (@link RigidGroupBuilder NXOpen.AnimationDesigner.RigidGroupBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="rigidGroup"> (@link RigidGroup NXOpen.AnimationDesigner.RigidGroup@endlink)  @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink  to be edited, if NULL then create a new one </param>
    def CreateRigidGroupBuilder(part: NXOpen.Part, rigidGroup: RigidGroup) -> RigidGroupBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::RigidGroupBuilder NXOpen::AnimationDesigner::RigidGroupBuilder@endlink . 
         @return builder (@link RigidGroupBuilder NXOpen.AnimationDesigner.RigidGroupBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::RigidGroup   NXOpen::AnimationDesigner::RigidGroup @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return rigidGroup (@link RigidGroup NXOpen.AnimationDesigner.RigidGroup@endlink):  @link  NXOpen::AnimationDesigner::RigidGroup   NXOpen::AnimationDesigner::RigidGroup @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::RigidGroup   NXOpen::AnimationDesigner::RigidGroup @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> RigidGroup:
        """
         Finds the @link  NXOpen::AnimationDesigner::RigidGroup   NXOpen::AnimationDesigner::RigidGroup @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return rigidGroup (@link RigidGroup NXOpen.AnimationDesigner.RigidGroup@endlink):  @link  NXOpen::AnimationDesigner::RigidGroup   NXOpen::AnimationDesigner::RigidGroup @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents a Rigid Group feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::RigidGroupBuilder  NXOpen::AnimationDesigner::RigidGroupBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class RigidGroup(NXOpen.DisplayableObject): 
    """ Represents a Rigid Group feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::ScrewJointBuilder NXOpen::AnimationDesigner::ScrewJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::ScrewJointCollection::CreateScrewJointBuilder  NXOpen::AnimationDesigner::ScrewJointCollection::CreateScrewJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class ScrewJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.ScrewJointBuilder</ja_class>. """


    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
    ##  Returns the axis vector.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Direction
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector

    ##  Returns the axis vector.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpressionRatio
    ##  Returns  @brief  a value that indicates pitch value for the screw joint.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Expression
    @property
    def ExpressionRatio(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ExpressionRatio
         Returns  @brief  a value that indicates pitch value for the screw joint.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin
    ##  Returns the origin point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Point
    @property
    def PointOrigin(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin
         Returns the origin point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin

    ##  Returns the origin point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    @PointOrigin.setter
    def PointOrigin(self, origin: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointOrigin
         Returns the origin point.  
             
         
        """
        pass
    
import NXOpen
##  Represents a collection of Screw Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class ScrewJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Screw Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::ScrewJointBuilder NXOpen::AnimationDesigner::ScrewJointBuilder@endlink . 
    ##  @return builder (@link ScrewJointBuilder NXOpen.AnimationDesigner.ScrewJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="screwJoint"> (@link ScrewJoint NXOpen.AnimationDesigner.ScrewJoint@endlink)  @link NXOpen::AnimationDesigner::ScrewJoint NXOpen::AnimationDesigner::ScrewJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreateScrewJointBuilder(part: NXOpen.Part, screwJoint: ScrewJoint) -> ScrewJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::ScrewJointBuilder NXOpen::AnimationDesigner::ScrewJointBuilder@endlink . 
         @return builder (@link ScrewJointBuilder NXOpen.AnimationDesigner.ScrewJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::ScrewJoint   NXOpen::AnimationDesigner::ScrewJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return screwJoint (@link ScrewJoint NXOpen.AnimationDesigner.ScrewJoint@endlink):  @link  NXOpen::AnimationDesigner::ScrewJoint   NXOpen::AnimationDesigner::ScrewJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::ScrewJoint   NXOpen::AnimationDesigner::ScrewJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> ScrewJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::ScrewJoint   NXOpen::AnimationDesigner::ScrewJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return screwJoint (@link ScrewJoint NXOpen.AnimationDesigner.ScrewJoint@endlink):  @link  NXOpen::AnimationDesigner::ScrewJoint   NXOpen::AnimationDesigner::ScrewJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Screw Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::ScrewJointBuilder  NXOpen::AnimationDesigner::ScrewJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.2  <br> 

class ScrewJoint(PhysicsJoint): 
    """ Represents a Screw Joint feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::SliderJointBuilder NXOpen::AnimationDesigner::SliderJointBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::SliderJointCollection::CreateSliderJointBuilder  NXOpen::AnimationDesigner::SliderJointCollection::CreateSliderJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SliderJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.SliderJointBuilder</ja_class>. """


    ## Getter for property: (bool) EnableLowerLimit
    ##  Returns the lower limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied a lower limit in movement.  
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.  
         
        """
        pass
    
    ## Setter for property: (bool) EnableLowerLimit

    ##  Returns the lower limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied a lower limit in movement.  
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableLowerLimit.setter
    def EnableLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.  
         
        """
        pass
    
    ## Getter for property: (bool) EnableUpperLimit
    ##  Returns the upper limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied an upper limit in movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def EnableUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    
    ## Setter for property: (bool) EnableUpperLimit

    ##  Returns the upper limit option.  
    ##    If the enable is true, then the joint will be 
    ##             applied an upper limit in movement.   
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @EnableUpperLimit.setter
    def EnableUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimit
    ##  Returns the lower limit.  
    ##    The lower limit setup for joint movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def LowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) LowerLimit
         Returns the lower limit.  
           The lower limit setup for joint movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
    ##  Returns the offset value.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## @return NXOpen.Expression
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Offset
         Returns the offset value.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimit
    ##  Returns the upper limit.  
    ##    The upper limit setup for joint movement.   
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def UpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) UpperLimit
         Returns the upper limit.  
           The upper limit setup for joint movement.   
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
    ##  Returns the vector.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector

    ##  Returns the vector.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @Vector.setter
    def Vector(self, specifyVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) Vector
         Returns the vector.  
             
         
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a collection of Slider Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SliderJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Slider Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::SliderJointBuilder NXOpen::AnimationDesigner::SliderJointBuilder@endlink . 
    ##  @return builder (@link SliderJointBuilder NXOpen.AnimationDesigner.SliderJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="slidingJoint"> (@link SliderJoint NXOpen.AnimationDesigner.SliderJoint@endlink)  @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  to be edited, if NULL then create a new one </param>
    @overload
    def CreateSliderJointBuilder(part: NXOpen.Part, slidingJoint: SliderJoint) -> SliderJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::SliderJointBuilder NXOpen::AnimationDesigner::SliderJointBuilder@endlink . 
         @return builder (@link SliderJointBuilder NXOpen.AnimationDesigner.SliderJointBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::AnimationDesigner::SliderJointBuilder NXOpen::AnimationDesigner::SliderJointBuilder@endlink . 
    ##  @return builder (@link SliderJointBuilder NXOpen.AnimationDesigner.SliderJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="slidingJoint"> (@link SliderJoint NXOpen.AnimationDesigner.SliderJoint@endlink)  @link NXOpen::AnimationDesigner::SliderJoint NXOpen::AnimationDesigner::SliderJoint@endlink  to be edited, if NULL then create a new one </param>
    ## <param name="partOcc"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  for the edited sliding joint occurrence </param>
    @overload
    def CreateSliderJointBuilder(part: NXOpen.Part, slidingJoint: SliderJoint, partOcc: NXOpen.Assemblies.Component) -> SliderJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::SliderJointBuilder NXOpen::AnimationDesigner::SliderJointBuilder@endlink . 
         @return builder (@link SliderJointBuilder NXOpen.AnimationDesigner.SliderJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::SliderJoint   NXOpen::AnimationDesigner::SliderJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return sliderJoint (@link SliderJoint NXOpen.AnimationDesigner.SliderJoint@endlink):  @link  NXOpen::AnimationDesigner::SliderJoint   NXOpen::AnimationDesigner::SliderJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::SliderJoint   NXOpen::AnimationDesigner::SliderJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> SliderJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::SliderJoint   NXOpen::AnimationDesigner::SliderJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return sliderJoint (@link SliderJoint NXOpen.AnimationDesigner.SliderJoint@endlink):  @link  NXOpen::AnimationDesigner::SliderJoint   NXOpen::AnimationDesigner::SliderJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Slider Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::SliderJointBuilder  NXOpen::AnimationDesigner::SliderJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SliderJoint(PhysicsJoint): 
    """ Represents a Slider Joint feature. """
    pass


import NXOpen
##  Represents a @link NXOpen::AnimationDesigner::SpeedMotorBuilder NXOpen::AnimationDesigner::SpeedMotorBuilder@endlink .  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::SpeedMotorCollection::CreateSpeedMotorBuilder  NXOpen::AnimationDesigner::SpeedMotorCollection::CreateSpeedMotorBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SpeedMotorBuilder(MotorBuilder): 
    """ Represents a <ja_class>NXOpen.AnimationDesigner.SpeedMotorBuilder</ja_class>. """


    ##  the axis types. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Angular</term><description> 
    ##  Angular </description> </item><item><term> 
    ## Linear</term><description> 
    ##  Linear </description> </item><item><term> 
    ## Mixed</term><description> 
    ##  Mix angular and linear </description> </item></list>
    class Axis(Enum):
        """
        Members Include: <Angular> <Linear> <Mixed>
        """
        Angular: int
        Linear: int
        Mixed: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpeedMotorBuilder.Axis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the color options. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SpecifyColor</term><description> 
    ##  Assigns a color to the speed motor </description> </item><item><term> 
    ## NoColor</term><description> 
    ##  Assigns no color to the speed motor </description> </item></list>
    class ColorOptions(Enum):
        """
        Members Include: <SpecifyColor> <NoColor>
        """
        SpecifyColor: int
        NoColor: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SpeedMotorBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SpeedMotorBuilder.Axis NXOpen.AnimationDesigner.SpeedMotorBuilder.Axis@endlink) AxisType
    ##  Returns the axis type.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return SpeedMotorBuilder.Axis
    @property
    def AxisType(self) -> SpeedMotorBuilder.Axis:
        """
        Getter for property: (@link SpeedMotorBuilder.Axis NXOpen.AnimationDesigner.SpeedMotorBuilder.Axis@endlink) AxisType
         Returns the axis type.  
             
         
        """
        pass
    
    ## Setter for property: (@link SpeedMotorBuilder.Axis NXOpen.AnimationDesigner.SpeedMotorBuilder.Axis@endlink) AxisType

    ##  Returns the axis type.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AxisType.setter
    def AxisType(self, axisType: SpeedMotorBuilder.Axis):
        """
        Setter for property: (@link SpeedMotorBuilder.Axis NXOpen.AnimationDesigner.SpeedMotorBuilder.Axis@endlink) AxisType
         Returns the axis type.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
    ##  Returns the color.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color

    ##  Returns the color.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) Color
         Returns the color.  
             
         
        """
        pass
    
    ## Getter for property: (@link SpeedMotorBuilder.ColorOptions NXOpen.AnimationDesigner.SpeedMotorBuilder.ColorOptions@endlink) ColorOption
    ##  Returns the color option.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return SpeedMotorBuilder.ColorOptions
    @property
    def ColorOption(self) -> SpeedMotorBuilder.ColorOptions:
        """
        Getter for property: (@link SpeedMotorBuilder.ColorOptions NXOpen.AnimationDesigner.SpeedMotorBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Setter for property: (@link SpeedMotorBuilder.ColorOptions NXOpen.AnimationDesigner.SpeedMotorBuilder.ColorOptions@endlink) ColorOption

    ##  Returns the color option.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ColorOption.setter
    def ColorOption(self, colorOption: SpeedMotorBuilder.ColorOptions):
        """
        Setter for property: (@link SpeedMotorBuilder.ColorOptions NXOpen.AnimationDesigner.SpeedMotorBuilder.ColorOptions@endlink) ColorOption
         Returns the color option.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAcceleration
    ##  Returns the max acceleration.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxAcceleration(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxAcceleration
         Returns the max acceleration.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Speed
    ##  Returns the speed.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Speed(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Speed
         Returns the speed.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartTime
    ##  Returns the start time.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def StartTime(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) StartTime
         Returns the start time.  
             
         
        """
        pass
    
    ## Getter for property: (bool) UseAcceleration
    ##  Returns the limit acceleration.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def UseAcceleration(self) -> bool:
        """
        Getter for property: (bool) UseAcceleration
         Returns the limit acceleration.  
             
         
        """
        pass
    
    ## Setter for property: (bool) UseAcceleration

    ##  Returns the limit acceleration.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @UseAcceleration.setter
    def UseAcceleration(self, useAcceleration: bool):
        """
        Setter for property: (bool) UseAcceleration
         Returns the limit acceleration.  
             
         
        """
        pass
    
    ##  Sets the start time value. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ## <param name="deltaStart"> (float) </param>
    def EditStartTime(self, deltaStart: float) -> None:
        """
         Sets the start time value. 
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a collection of Speed Motor objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SpeedMotorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Speed Motor objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::SpeedMotorBuilder NXOpen::AnimationDesigner::SpeedMotorBuilder@endlink . 
    ##  @return builder (@link SpeedMotorBuilder NXOpen.AnimationDesigner.SpeedMotorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="speedMotor"> (@link SpeedMotor NXOpen.AnimationDesigner.SpeedMotor@endlink)  @link NXOpen::AnimationDesigner::SpeedMotor NXOpen::AnimationDesigner::SpeedMotor@endlink  to be edited, if NULL then create a new one </param>
    @overload
    def CreateSpeedMotorBuilder(part: NXOpen.Part, speedMotor: SpeedMotor) -> SpeedMotorBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::SpeedMotorBuilder NXOpen::AnimationDesigner::SpeedMotorBuilder@endlink . 
         @return builder (@link SpeedMotorBuilder NXOpen.AnimationDesigner.SpeedMotorBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link NXOpen::AnimationDesigner::SpeedMotorBuilder NXOpen::AnimationDesigner::SpeedMotorBuilder@endlink . 
    ##  @return builder (@link SpeedMotorBuilder NXOpen.AnimationDesigner.SpeedMotorBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="speedMotor"> (@link SpeedMotor NXOpen.AnimationDesigner.SpeedMotor@endlink)  @link NXOpen::AnimationDesigner::SpeedMotor NXOpen::AnimationDesigner::SpeedMotor@endlink  to be edited, if NULL then create a new one </param>
    ## <param name="partOcc"> (@link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink)  @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink  for the edited speed motor occurrence </param>
    @overload
    def CreateSpeedMotorBuilder(part: NXOpen.Part, speedMotor: SpeedMotor, partOcc: NXOpen.Assemblies.Component) -> SpeedMotorBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::SpeedMotorBuilder NXOpen::AnimationDesigner::SpeedMotorBuilder@endlink . 
         @return builder (@link SpeedMotorBuilder NXOpen.AnimationDesigner.SpeedMotorBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::SpeedMotor   NXOpen::AnimationDesigner::SpeedMotor @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return speedMotor (@link SpeedMotor NXOpen.AnimationDesigner.SpeedMotor@endlink):  @link  NXOpen::AnimationDesigner::SpeedMotor   NXOpen::AnimationDesigner::SpeedMotor @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::SpeedMotor   NXOpen::AnimationDesigner::SpeedMotor @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> SpeedMotor:
        """
         Finds the @link  NXOpen::AnimationDesigner::SpeedMotor   NXOpen::AnimationDesigner::SpeedMotor @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return speedMotor (@link SpeedMotor NXOpen.AnimationDesigner.SpeedMotor@endlink):  @link  NXOpen::AnimationDesigner::SpeedMotor   NXOpen::AnimationDesigner::SpeedMotor @endlink  with this name. .
        """
        pass
    
##  Represents a Speed Motor feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::SpeedMotorBuilder  NXOpen::AnimationDesigner::SpeedMotorBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SpeedMotor(Motor): 
    """ Represents a Speed Motor feature. """
    pass


import NXOpen
##  Represents a @link AnimationDesigner::SphericalJointBuilder AnimationDesigner::SphericalJointBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::SphericalJointCollection::CreateSphericalJointBuilder  NXOpen::AnimationDesigner::SphericalJointCollection::CreateSphericalJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SphericalJointBuilder(PhysicsJointBuilder): 
    """ Represents a <ja_class>AnimationDesigner.SphericalJointBuilder</ja_class> builder """


    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
    ##  Returns the anchor point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint

    ##  Returns the anchor point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
    
import NXOpen
##  Represents a collection of Spherical Joint objects.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SphericalJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Spherical Joint objects. """


    ##  Creates a @link NXOpen::AnimationDesigner::SphericalJointBuilder NXOpen::AnimationDesigner::SphericalJointBuilder@endlink . 
    ##  @return builder (@link SphericalJointBuilder NXOpen.AnimationDesigner.SphericalJointBuilder@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="ballJoint"> (@link SphericalJoint NXOpen.AnimationDesigner.SphericalJoint@endlink)  @link NXOpen::AnimationDesigner::SphericalJoint NXOpen::AnimationDesigner::SphericalJoint@endlink  to be edited, if NULL then create a new one </param>
    def CreateSphericalJointBuilder(part: NXOpen.Part, ballJoint: SphericalJoint) -> SphericalJointBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::SphericalJointBuilder NXOpen::AnimationDesigner::SphericalJointBuilder@endlink . 
         @return builder (@link SphericalJointBuilder NXOpen.AnimationDesigner.SphericalJointBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::SphericalJoint   NXOpen::AnimationDesigner::SphericalJoint @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return sphericalJoint (@link SphericalJoint NXOpen.AnimationDesigner.SphericalJoint@endlink):  @link  NXOpen::AnimationDesigner::SphericalJoint   NXOpen::AnimationDesigner::SphericalJoint @endlink  with this name. .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::SphericalJoint   NXOpen::AnimationDesigner::SphericalJoint @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> SphericalJoint:
        """
         Finds the @link  NXOpen::AnimationDesigner::SphericalJoint   NXOpen::AnimationDesigner::SphericalJoint @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return sphericalJoint (@link SphericalJoint NXOpen.AnimationDesigner.SphericalJoint@endlink):  @link  NXOpen::AnimationDesigner::SphericalJoint   NXOpen::AnimationDesigner::SphericalJoint @endlink  with this name. .
        """
        pass
    
##  Represents a Spherical Joint feature.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::SphericalJointBuilder  NXOpen::AnimationDesigner::SphericalJointBuilder @endlink  <br> 
## 
##   <br>  Created in NX12.0.0  <br> 

class SphericalJoint(PhysicsJoint): 
    """ Represents a Spherical Joint feature. """
    pass


import NXOpen
##  Represents a @link AnimationDesigner::Tracer AnimationDesigner::Tracer@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::AnimationDesigner::TracerCollection::CreateTracerBuilder  NXOpen::AnimationDesigner::TracerCollection::CreateTracerBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class TracerBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>AnimationDesigner.Tracer</ja_class> builder """


    ## Getter for property: (str) Name
    ##  Returns the name   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##  Returns the name   
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
    ##  Returns the origin point.  
    ##      
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def SelectPoint(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
         Returns the origin point.  
             
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint

    ##  Returns the origin point.  
    ##      
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SelectPoint.setter
    def SelectPoint(self, selectPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) SelectPoint
         Returns the origin point.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectRefBody
    ##  Returns the specify reference body selection.  
    ##    This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def SelectRefBody(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) SelectRefBody
         Returns the specify reference body selection.  
           This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink    
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Selection
    ##  Returns the body selection.  
    ##    This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink    
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.SelectNXObject
    @property
    def Selection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: (@link NXOpen.SelectNXObject NXOpen.SelectNXObject@endlink) Selection
         Returns the body selection.  
           This should be a @link NXOpen::AnimationDesigner::RigidGroup NXOpen::AnimationDesigner::RigidGroup@endlink    
         
        """
        pass
    
    ## Getter for property: (bool) ShowInSimulation
    ##  Returns  @brief  the option of show during simulation.  
    ##     
    ## 
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ShowInSimulation(self) -> bool:
        """
        Getter for property: (bool) ShowInSimulation
         Returns  @brief  the option of show during simulation.  
            
        
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowInSimulation

    ##  Returns  @brief  the option of show during simulation.  
    ##     
    ## 
    ##     
    ##  
    ## Setter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ShowInSimulation.setter
    def ShowInSimulation(self, show: bool):
        """
        Setter for property: (bool) ShowInSimulation
         Returns  @brief  the option of show during simulation.  
            
        
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TraceRateSetting
    ##  Returns the trace rate setting   
    ##     
    ##  
    ## Getter License requirements: nx_animationdesigner (" NX Animation Designer")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TraceRateSetting(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TraceRateSetting
         Returns the trace rate setting   
            
         
        """
        pass
    
import NXOpen
##  Represents a collection of Tracer.  <br> To obtain an instance of this class, refer to @link NXOpen::AnimationDesigner::AnimationDesignerManager  NXOpen::AnimationDesigner::AnimationDesignerManager @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class TracerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Tracer. """


    ##  Creates a @link NXOpen::AnimationDesigner::TracerBuilder NXOpen::AnimationDesigner::TracerBuilder@endlink . 
    ##  @return builder (@link TracerBuilder NXOpen.AnimationDesigner.TracerBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="tracer"> (@link Tracer NXOpen.AnimationDesigner.Tracer@endlink)  @link NXOpen::AnimationDesigner::Tracer NXOpen::AnimationDesigner::Tracer@endlink  to be edited, if NULL then create a new one </param>
    def CreateTracerBuilder(part: NXOpen.Part, tracer: Tracer) -> TracerBuilder:
        """
         Creates a @link NXOpen::AnimationDesigner::TracerBuilder NXOpen::AnimationDesigner::TracerBuilder@endlink . 
         @return builder (@link TracerBuilder NXOpen.AnimationDesigner.TracerBuilder@endlink): .
        """
        pass
    
    ##  Finds the @link  NXOpen::AnimationDesigner::Tracer   NXOpen::AnimationDesigner::Tracer @endlink  with the given name.
    ##             An exception will be thrown if no object can be found with given name. 
    ##  @return traceObject (@link Tracer NXOpen.AnimationDesigner.Tracer@endlink):  @link  NXOpen::AnimationDesigner::Tracer   NXOpen::AnimationDesigner::Tracer @endlink  with this name. .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: nx_animationdesigner (" NX Animation Designer")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="name"> (str)  The name of the @link  NXOpen::AnimationDesigner::Tracer   NXOpen::AnimationDesigner::Tracer @endlink . </param>
    def FindObject(part: NXOpen.Part, name: str) -> Tracer:
        """
         Finds the @link  NXOpen::AnimationDesigner::Tracer   NXOpen::AnimationDesigner::Tracer @endlink  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         @return traceObject (@link Tracer NXOpen.AnimationDesigner.Tracer@endlink):  @link  NXOpen::AnimationDesigner::Tracer   NXOpen::AnimationDesigner::Tracer @endlink  with this name. .
        """
        pass
    
import NXOpen
##  Represents the Tracer class. A Tracer can make an object be able
##         to trace an point on it.  <br> To create or edit an instance of this class, use @link NXOpen::AnimationDesigner::TracerBuilder  NXOpen::AnimationDesigner::TracerBuilder @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class Tracer(NXOpen.DisplayableObject): 
    """ Represents the Tracer class. A Tracer can make an object be able
        to trace an point on it. """
    pass


## @package NXOpen.AnimationDesigner
## Classes, Enums and Structs under NXOpen.AnimationDesigner namespace

##  @link ActivityOperatorBuilderActionTypes NXOpen.AnimationDesigner.ActivityOperatorBuilderActionTypes @endlink is an alias for @link ActivityOperatorBuilder.ActionTypes NXOpen.AnimationDesigner.ActivityOperatorBuilder.ActionTypes@endlink
ActivityOperatorBuilderActionTypes = ActivityOperatorBuilder.ActionTypes


##  @link AnimatedCameraBuilderCameraAxisTypes NXOpen.AnimationDesigner.AnimatedCameraBuilderCameraAxisTypes @endlink is an alias for @link AnimatedCameraBuilder.CameraAxisTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraAxisTypes@endlink
AnimatedCameraBuilderCameraAxisTypes = AnimatedCameraBuilder.CameraAxisTypes


##  @link AnimatedCameraBuilderCameraModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilderCameraModeTypes @endlink is an alias for @link AnimatedCameraBuilder.CameraModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.CameraModeTypes@endlink
AnimatedCameraBuilderCameraModeTypes = AnimatedCameraBuilder.CameraModeTypes


##  @link AnimatedCameraBuilderLookAtDirectionTypes NXOpen.AnimationDesigner.AnimatedCameraBuilderLookAtDirectionTypes @endlink is an alias for @link AnimatedCameraBuilder.LookAtDirectionTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.LookAtDirectionTypes@endlink
AnimatedCameraBuilderLookAtDirectionTypes = AnimatedCameraBuilder.LookAtDirectionTypes


##  @link AnimatedCameraBuilderTransitionModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilderTransitionModeTypes @endlink is an alias for @link AnimatedCameraBuilder.TransitionModeTypes NXOpen.AnimationDesigner.AnimatedCameraBuilder.TransitionModeTypes@endlink
AnimatedCameraBuilderTransitionModeTypes = AnimatedCameraBuilder.TransitionModeTypes


##  @link AnimatedColorBuilderCreationTypes NXOpen.AnimationDesigner.AnimatedColorBuilderCreationTypes @endlink is an alias for @link AnimatedColorBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedColorBuilder.CreationTypes@endlink
AnimatedColorBuilderCreationTypes = AnimatedColorBuilder.CreationTypes


##  @link AnimatedExplodeBuilderColorOptions NXOpen.AnimationDesigner.AnimatedExplodeBuilderColorOptions @endlink is an alias for @link AnimatedExplodeBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedExplodeBuilder.ColorOptions@endlink
AnimatedExplodeBuilderColorOptions = AnimatedExplodeBuilder.ColorOptions


##  @link AnimatedExplodeBuilderCreationTypes NXOpen.AnimationDesigner.AnimatedExplodeBuilderCreationTypes @endlink is an alias for @link AnimatedExplodeBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedExplodeBuilder.CreationTypes@endlink
AnimatedExplodeBuilderCreationTypes = AnimatedExplodeBuilder.CreationTypes


##  @link AnimatedVisibilityBuilderColorOptions NXOpen.AnimationDesigner.AnimatedVisibilityBuilderColorOptions @endlink is an alias for @link AnimatedVisibilityBuilder.ColorOptions NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.ColorOptions@endlink
AnimatedVisibilityBuilderColorOptions = AnimatedVisibilityBuilder.ColorOptions


##  @link AnimatedVisibilityBuilderCreationTypes NXOpen.AnimationDesigner.AnimatedVisibilityBuilderCreationTypes @endlink is an alias for @link AnimatedVisibilityBuilder.CreationTypes NXOpen.AnimationDesigner.AnimatedVisibilityBuilder.CreationTypes@endlink
AnimatedVisibilityBuilderCreationTypes = AnimatedVisibilityBuilder.CreationTypes


##  @link AnimationDesignerManagerJaAnimationDesignerDisplayColorOption NXOpen.AnimationDesigner.AnimationDesignerManagerJaAnimationDesignerDisplayColorOption @endlink is an alias for @link AnimationDesignerManager.JaAnimationDesignerDisplayColorOption NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerDisplayColorOption@endlink
AnimationDesignerManagerJaAnimationDesignerDisplayColorOption = AnimationDesignerManager.JaAnimationDesignerDisplayColorOption


##  @link AnimationDesignerManagerJaAnimationDesignerEnvelopeAccuracyMode NXOpen.AnimationDesigner.AnimationDesignerManagerJaAnimationDesignerEnvelopeAccuracyMode @endlink is an alias for @link AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode@endlink
AnimationDesignerManagerJaAnimationDesignerEnvelopeAccuracyMode = AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode


##  @link AnimationDesignerManagerJaAnimationDesignerEnvelopeMode NXOpen.AnimationDesigner.AnimationDesignerManagerJaAnimationDesignerEnvelopeMode @endlink is an alias for @link AnimationDesignerManager.JaAnimationDesignerEnvelopeMode NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerEnvelopeMode@endlink
AnimationDesignerManagerJaAnimationDesignerEnvelopeMode = AnimationDesignerManager.JaAnimationDesignerEnvelopeMode


##  @link AnimationDesignerManagerJaAnimationDesignerInterferenceType NXOpen.AnimationDesigner.AnimationDesignerManagerJaAnimationDesignerInterferenceType @endlink is an alias for @link AnimationDesignerManager.JaAnimationDesignerInterferenceType NXOpen.AnimationDesigner.AnimationDesignerManager.JaAnimationDesignerInterferenceType@endlink
AnimationDesignerManagerJaAnimationDesignerInterferenceType = AnimationDesignerManager.JaAnimationDesignerInterferenceType


##  @link BulletCableBuilderDerivationType NXOpen.AnimationDesigner.BulletCableBuilderDerivationType @endlink is an alias for @link BulletCableBuilder.DerivationType NXOpen.AnimationDesigner.BulletCableBuilder.DerivationType@endlink
BulletCableBuilderDerivationType = BulletCableBuilder.DerivationType


##  @link ConstraintConversionBuilderAssemblyObjectTypes NXOpen.AnimationDesigner.ConstraintConversionBuilderAssemblyObjectTypes @endlink is an alias for @link ConstraintConversionBuilder.AssemblyObjectTypes NXOpen.AnimationDesigner.ConstraintConversionBuilder.AssemblyObjectTypes@endlink
ConstraintConversionBuilderAssemblyObjectTypes = ConstraintConversionBuilder.AssemblyObjectTypes


##  @link CouplerBuilderColorOptions NXOpen.AnimationDesigner.CouplerBuilderColorOptions @endlink is an alias for @link CouplerBuilder.ColorOptions NXOpen.AnimationDesigner.CouplerBuilder.ColorOptions@endlink
CouplerBuilderColorOptions = CouplerBuilder.ColorOptions


##  @link FlexibleCableAttachmentBuilderAttachmentTypes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderAttachmentTypes @endlink is an alias for @link FlexibleCableAttachmentBuilder.AttachmentTypes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.AttachmentTypes@endlink
FlexibleCableAttachmentBuilderAttachmentTypes = FlexibleCableAttachmentBuilder.AttachmentTypes


##  @link FlexibleCableAttachmentBuilderRotationAxes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilderRotationAxes @endlink is an alias for @link FlexibleCableAttachmentBuilder.RotationAxes NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder.RotationAxes@endlink
FlexibleCableAttachmentBuilderRotationAxes = FlexibleCableAttachmentBuilder.RotationAxes


##  @link FlexibleCableBuilderColorOptions NXOpen.AnimationDesigner.FlexibleCableBuilderColorOptions @endlink is an alias for @link FlexibleCableBuilder.ColorOptions NXOpen.AnimationDesigner.FlexibleCableBuilder.ColorOptions@endlink
FlexibleCableBuilderColorOptions = FlexibleCableBuilder.ColorOptions


##  @link FlexibleCableBuilderGeometryTypes NXOpen.AnimationDesigner.FlexibleCableBuilderGeometryTypes @endlink is an alias for @link FlexibleCableBuilder.GeometryTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.GeometryTypes@endlink
FlexibleCableBuilderGeometryTypes = FlexibleCableBuilder.GeometryTypes


##  @link FlexibleCableBuilderSectionTypes NXOpen.AnimationDesigner.FlexibleCableBuilderSectionTypes @endlink is an alias for @link FlexibleCableBuilder.SectionTypes NXOpen.AnimationDesigner.FlexibleCableBuilder.SectionTypes@endlink
FlexibleCableBuilderSectionTypes = FlexibleCableBuilder.SectionTypes


##  @link GearBuilderGearType NXOpen.AnimationDesigner.GearBuilderGearType @endlink is an alias for @link GearBuilder.GearType NXOpen.AnimationDesigner.GearBuilder.GearType@endlink
GearBuilderGearType = GearBuilder.GearType


##  @link InverseKinematicsBuilderAlignTypes NXOpen.AnimationDesigner.InverseKinematicsBuilderAlignTypes @endlink is an alias for @link InverseKinematicsBuilder.AlignTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.AlignTypes@endlink
InverseKinematicsBuilderAlignTypes = InverseKinematicsBuilder.AlignTypes


##  @link InverseKinematicsBuilderBodyTypes NXOpen.AnimationDesigner.InverseKinematicsBuilderBodyTypes @endlink is an alias for @link InverseKinematicsBuilder.BodyTypes NXOpen.AnimationDesigner.InverseKinematicsBuilder.BodyTypes@endlink
InverseKinematicsBuilderBodyTypes = InverseKinematicsBuilder.BodyTypes


##  @link InverseKinematicsBuilderResult NXOpen.AnimationDesigner.InverseKinematicsBuilderResult @endlink is an alias for @link InverseKinematicsBuilder.Result NXOpen.AnimationDesigner.InverseKinematicsBuilder.Result@endlink
InverseKinematicsBuilderResult = InverseKinematicsBuilder.Result


##  @link MeasureBuilderMeasureTypes NXOpen.AnimationDesigner.MeasureBuilderMeasureTypes @endlink is an alias for @link MeasureBuilder.MeasureTypes NXOpen.AnimationDesigner.MeasureBuilder.MeasureTypes@endlink
MeasureBuilderMeasureTypes = MeasureBuilder.MeasureTypes


##  @link MeasureBuilderMotorParameterTypes NXOpen.AnimationDesigner.MeasureBuilderMotorParameterTypes @endlink is an alias for @link MeasureBuilder.MotorParameterTypes NXOpen.AnimationDesigner.MeasureBuilder.MotorParameterTypes@endlink
MeasureBuilderMotorParameterTypes = MeasureBuilder.MotorParameterTypes


##  @link MechanicalCamBuilderColorOptions NXOpen.AnimationDesigner.MechanicalCamBuilderColorOptions @endlink is an alias for @link MechanicalCamBuilder.ColorOptions NXOpen.AnimationDesigner.MechanicalCamBuilder.ColorOptions@endlink
MechanicalCamBuilderColorOptions = MechanicalCamBuilder.ColorOptions


##  @link PathConstraintFrameBuilderCurveTypes NXOpen.AnimationDesigner.PathConstraintFrameBuilderCurveTypes @endlink is an alias for @link PathConstraintFrameBuilder.CurveTypes NXOpen.AnimationDesigner.PathConstraintFrameBuilder.CurveTypes@endlink
PathConstraintFrameBuilderCurveTypes = PathConstraintFrameBuilder.CurveTypes


##  @link PathConstraintJointBuilderPathTypes NXOpen.AnimationDesigner.PathConstraintJointBuilderPathTypes @endlink is an alias for @link PathConstraintJointBuilder.PathTypes NXOpen.AnimationDesigner.PathConstraintJointBuilder.PathTypes@endlink
PathConstraintJointBuilderPathTypes = PathConstraintJointBuilder.PathTypes


##  @link PhysicsJointBuilderColorOptions NXOpen.AnimationDesigner.PhysicsJointBuilderColorOptions @endlink is an alias for @link PhysicsJointBuilder.ColorOptions NXOpen.AnimationDesigner.PhysicsJointBuilder.ColorOptions@endlink
PhysicsJointBuilderColorOptions = PhysicsJointBuilder.ColorOptions


##  @link PhysicsJointBuilderMotionTypes NXOpen.AnimationDesigner.PhysicsJointBuilderMotionTypes @endlink is an alias for @link PhysicsJointBuilder.MotionTypes NXOpen.AnimationDesigner.PhysicsJointBuilder.MotionTypes@endlink
PhysicsJointBuilderMotionTypes = PhysicsJointBuilder.MotionTypes


##  @link PointOnCurveKinematicsChainBuilderProjectionDirectionType NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilderProjectionDirectionType @endlink is an alias for @link PointOnCurveKinematicsChainBuilder.ProjectionDirectionType NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder.ProjectionDirectionType@endlink
PointOnCurveKinematicsChainBuilderProjectionDirectionType = PointOnCurveKinematicsChainBuilder.ProjectionDirectionType


##  @link PositionMotorBuilderAutoCalculate NXOpen.AnimationDesigner.PositionMotorBuilderAutoCalculate @endlink is an alias for @link PositionMotorBuilder.AutoCalculate NXOpen.AnimationDesigner.PositionMotorBuilder.AutoCalculate@endlink
PositionMotorBuilderAutoCalculate = PositionMotorBuilder.AutoCalculate


##  @link PositionMotorBuilderAxis NXOpen.AnimationDesigner.PositionMotorBuilderAxis @endlink is an alias for @link PositionMotorBuilder.Axis NXOpen.AnimationDesigner.PositionMotorBuilder.Axis@endlink
PositionMotorBuilderAxis = PositionMotorBuilder.Axis


##  @link PositionMotorBuilderColorOptions NXOpen.AnimationDesigner.PositionMotorBuilderColorOptions @endlink is an alias for @link PositionMotorBuilder.ColorOptions NXOpen.AnimationDesigner.PositionMotorBuilder.ColorOptions@endlink
PositionMotorBuilderColorOptions = PositionMotorBuilder.ColorOptions


##  @link PreferencesBuilderArrangementTypes NXOpen.AnimationDesigner.PreferencesBuilderArrangementTypes @endlink is an alias for @link PreferencesBuilder.ArrangementTypes NXOpen.AnimationDesigner.PreferencesBuilder.ArrangementTypes@endlink
PreferencesBuilderArrangementTypes = PreferencesBuilder.ArrangementTypes


##  @link PreferencesBuilderBodyToUseForMeasureTypes NXOpen.AnimationDesigner.PreferencesBuilderBodyToUseForMeasureTypes @endlink is an alias for @link PreferencesBuilder.BodyToUseForMeasureTypes NXOpen.AnimationDesigner.PreferencesBuilder.BodyToUseForMeasureTypes@endlink
PreferencesBuilderBodyToUseForMeasureTypes = PreferencesBuilder.BodyToUseForMeasureTypes


##  @link PreferencesBuilderFlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.AnimationDesigner.PreferencesBuilderFlexibleFacetBodyUserDefinedLinearPrecisionInputTypes @endlink is an alias for @link PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes@endlink
PreferencesBuilderFlexibleFacetBodyUserDefinedLinearPrecisionInputTypes = PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes


##  @link PreferencesBuilderFlowLineStyleTypes NXOpen.AnimationDesigner.PreferencesBuilderFlowLineStyleTypes @endlink is an alias for @link PreferencesBuilder.FlowLineStyleTypes NXOpen.AnimationDesigner.PreferencesBuilder.FlowLineStyleTypes@endlink
PreferencesBuilderFlowLineStyleTypes = PreferencesBuilder.FlowLineStyleTypes


##  @link PreferencesBuilderGraphPlotTypes NXOpen.AnimationDesigner.PreferencesBuilderGraphPlotTypes @endlink is an alias for @link PreferencesBuilder.GraphPlotTypes NXOpen.AnimationDesigner.PreferencesBuilder.GraphPlotTypes@endlink
PreferencesBuilderGraphPlotTypes = PreferencesBuilder.GraphPlotTypes


##  @link PreferencesBuilderKineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilderKineoFlexibleFacetBodyPrecision @endlink is an alias for @link PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.AnimationDesigner.PreferencesBuilder.KineoFlexibleFacetBodyPrecision@endlink
PreferencesBuilderKineoFlexibleFacetBodyPrecision = PreferencesBuilder.KineoFlexibleFacetBodyPrecision


##  @link PreferencesBuilderPhysicsEngines NXOpen.AnimationDesigner.PreferencesBuilderPhysicsEngines @endlink is an alias for @link PreferencesBuilder.PhysicsEngines NXOpen.AnimationDesigner.PreferencesBuilder.PhysicsEngines@endlink
PreferencesBuilderPhysicsEngines = PreferencesBuilder.PhysicsEngines


##  @link PreferencesBuilderPrecisionPresetModes NXOpen.AnimationDesigner.PreferencesBuilderPrecisionPresetModes @endlink is an alias for @link PreferencesBuilder.PrecisionPresetModes NXOpen.AnimationDesigner.PreferencesBuilder.PrecisionPresetModes@endlink
PreferencesBuilderPrecisionPresetModes = PreferencesBuilder.PrecisionPresetModes


##  @link PreferencesBuilderRigidGroupSelectionDisplayTypes NXOpen.AnimationDesigner.PreferencesBuilderRigidGroupSelectionDisplayTypes @endlink is an alias for @link PreferencesBuilder.RigidGroupSelectionDisplayTypes NXOpen.AnimationDesigner.PreferencesBuilder.RigidGroupSelectionDisplayTypes@endlink
PreferencesBuilderRigidGroupSelectionDisplayTypes = PreferencesBuilder.RigidGroupSelectionDisplayTypes


##  @link PreferencesBuilderSolutionSearchScopeTypes NXOpen.AnimationDesigner.PreferencesBuilderSolutionSearchScopeTypes @endlink is an alias for @link PreferencesBuilder.SolutionSearchScopeTypes NXOpen.AnimationDesigner.PreferencesBuilder.SolutionSearchScopeTypes@endlink
PreferencesBuilderSolutionSearchScopeTypes = PreferencesBuilder.SolutionSearchScopeTypes


##  @link RigidGroupBuilderColorOptions NXOpen.AnimationDesigner.RigidGroupBuilderColorOptions @endlink is an alias for @link RigidGroupBuilder.ColorOptions NXOpen.AnimationDesigner.RigidGroupBuilder.ColorOptions@endlink
RigidGroupBuilderColorOptions = RigidGroupBuilder.ColorOptions


##  @link RigidGroupBuilderCreationTypes NXOpen.AnimationDesigner.RigidGroupBuilderCreationTypes @endlink is an alias for @link RigidGroupBuilder.CreationTypes NXOpen.AnimationDesigner.RigidGroupBuilder.CreationTypes@endlink
RigidGroupBuilderCreationTypes = RigidGroupBuilder.CreationTypes


##  @link RigidGroupBuilderMassPropertiesOption NXOpen.AnimationDesigner.RigidGroupBuilderMassPropertiesOption @endlink is an alias for @link RigidGroupBuilder.MassPropertiesOption NXOpen.AnimationDesigner.RigidGroupBuilder.MassPropertiesOption@endlink
RigidGroupBuilderMassPropertiesOption = RigidGroupBuilder.MassPropertiesOption


##  @link SpeedMotorBuilderAxis NXOpen.AnimationDesigner.SpeedMotorBuilderAxis @endlink is an alias for @link SpeedMotorBuilder.Axis NXOpen.AnimationDesigner.SpeedMotorBuilder.Axis@endlink
SpeedMotorBuilderAxis = SpeedMotorBuilder.Axis


##  @link SpeedMotorBuilderColorOptions NXOpen.AnimationDesigner.SpeedMotorBuilderColorOptions @endlink is an alias for @link SpeedMotorBuilder.ColorOptions NXOpen.AnimationDesigner.SpeedMotorBuilder.ColorOptions@endlink
SpeedMotorBuilderColorOptions = SpeedMotorBuilder.ColorOptions


