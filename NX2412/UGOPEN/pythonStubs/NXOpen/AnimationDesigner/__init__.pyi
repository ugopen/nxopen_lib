from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ActivityOperatorBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.ActivityOperatorBuilder. """
    class ActionTypes(Enum):
        """
        Members Include: 
         |Active|  Active an event 
         |Deactive|  Inactive an event 

        """
        Active: int
        Deactive: int
        @staticmethod
        def ValueOf(value: int) -> ActivityOperatorBuilder.ActionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ActionObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) ActionObject
         Returns the base list for a Joint.  
           The list can consist of  NXOpen::AnimationDesigner::RevoluteJoint  
                objects or other objects which can active and deactive.   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    def GetTime(self, index: int) -> float:
        """
         Gets the bar start time. 
         Returns start_time (float): .
        """
        pass
    def SetBarActionType(self, index: int, actionType: ActivityOperatorBuilder.ActionTypes) -> None:
        """
         Sets the bar action type. 
        """
        pass
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    def SetTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
import NXOpen
class ActivityOperatorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Activity Operator objects. """
    def CreateActivityOperatorBuilder(part: NXOpen.Part, activityOperator: ActivityOperator) -> ActivityOperatorBuilder:
        """
         Creates a NXOpen.AnimationDesigner.ActivityOperatorBuilder. 
         Returns builder ( ActivityOperatorBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> ActivityOperator:
        """
         Finds the  NXOpen.AnimationDesigner.ActivityOperator  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns activityOperator ( ActivityOperator NXOpen.Anim):   NXOpen.AnimationDesigner.ActivityOperator  with this name. .
        """
        pass
import NXOpen
class ActivityOperator(NXOpen.DisplayableObject): 
    """ Represents a Activity Operator feature. """
    pass
import NXOpen
class AnimatedCameraBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.AnimatedCameraBuilder. """
    class CameraAxisTypes(Enum):
        """
        Members Include: 
         |X|  X 
         |Y|  Y 
         |Z|  Z 

        """
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.CameraAxisTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CameraModeTypes(Enum):
        """
        Members Include: 
         |UserDefined|  User Defined 
         |Turntable|  Turntable 
         |Trajectory|  Trajectory 

        """
        UserDefined: int
        Turntable: int
        Trajectory: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.CameraModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LookAtDirectionTypes(Enum):
        """
        Members Include: 
         |WithRigid|  associate with rigid 
         |AlongPath|  along path curve 
         |LookAtObject|  look at object 
         |Fixed|  direction fixed 

        """
        WithRigid: int
        AlongPath: int
        LookAtObject: int
        Fixed: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.LookAtDirectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TransitionModeTypes(Enum):
        """
        Members Include: 
         |Linear|  Linear 
         |Path|  Path 

        """
        Linear: int
        Path: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedCameraBuilder.TransitionModeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AnimationCamera(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) AnimationCamera
         Returns the associated animation camera.  
             
         
        """
        pass
    @AnimationCamera.setter
    def AnimationCamera(self, animation_camera: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) AnimationCamera
         Returns the associated animation camera.  
             
         
        """
        pass
    @property
    def AssociateObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) AssociateObjects
         Returns the associate object selection.  
             
         
        """
        pass
    @property
    def AvoidViewRoll(self) -> bool:
        """
        Getter for property: (bool) AvoidViewRoll
         Returns the 'Associated to Object' mode avoid view roll option.  
             
         
        """
        pass
    @AvoidViewRoll.setter
    def AvoidViewRoll(self, bAvoidRoll: bool):
        """
        Setter for property: (bool) AvoidViewRoll
         Returns the 'Associated to Object' mode avoid view roll option.  
             
         
        """
        pass
    @property
    def CameraAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CameraAngle
         Returns the camera angle.  
             
         
        """
        pass
    @property
    def CameraAxisType(self) -> AnimatedCameraBuilder.CameraAxisTypes:
        """
        Getter for property: ( AnimatedCameraBuilder.CameraAxisTypes NXOpen.Anim) CameraAxisType
         Returns    the axis type.  
            
            
         
        """
        pass
    @CameraAxisType.setter
    def CameraAxisType(self, axisType: AnimatedCameraBuilder.CameraAxisTypes):
        """
        Setter for property: ( AnimatedCameraBuilder.CameraAxisTypes NXOpen.Anim) CameraAxisType
         Returns    the axis type.  
            
            
         
        """
        pass
    @property
    def CameraModeType(self) -> AnimatedCameraBuilder.CameraModeTypes:
        """
        Getter for property: ( AnimatedCameraBuilder.CameraModeTypes NXOpen.Anim) CameraModeType
         Returns    the mode type.  
            
            
         
        """
        pass
    @CameraModeType.setter
    def CameraModeType(self, modeType: AnimatedCameraBuilder.CameraModeTypes):
        """
        Setter for property: ( AnimatedCameraBuilder.CameraModeTypes NXOpen.Anim) CameraModeType
         Returns    the mode type.  
            
            
         
        """
        pass
    @property
    def CameraOrientation(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) CameraOrientation
         Returns the 'Associated to Object' mode camera init orientation.  
             
         
        """
        pass
    @CameraOrientation.setter
    def CameraOrientation(self, camera_orientation: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) CameraOrientation
         Returns the 'Associated to Object' mode camera init orientation.  
             
         
        """
        pass
    @property
    def DirectionType(self) -> AnimatedCameraBuilder.LookAtDirectionTypes:
        """
        Getter for property: ( AnimatedCameraBuilder.LookAtDirectionTypes NXOpen.Anim) DirectionType
         Returns    the 'Associated to Object' mode look at direction type.  
            
            
         
        """
        pass
    @DirectionType.setter
    def DirectionType(self, lookAtDirType: AnimatedCameraBuilder.LookAtDirectionTypes):
        """
        Setter for property: ( AnimatedCameraBuilder.LookAtDirectionTypes NXOpen.Anim) DirectionType
         Returns    the 'Associated to Object' mode look at direction type.  
            
            
         
        """
        pass
    @property
    def EndPathPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) EndPathPoint
         Returns the 'Associated to Object' mode associated curve end point.  
             
         
        """
        pass
    @EndPathPoint.setter
    def EndPathPoint(self, endPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) EndPathPoint
         Returns the 'Associated to Object' mode associated curve end point.  
             
         
        """
        pass
    @property
    def EndTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndTime
         Returns the 'Associated to Object' mode end time.  
             
         
        """
        pass
    @property
    def LookAtObject(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) LookAtObject
         Returns the 'Associated to Object' mode look at object selection.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def PointOnLookAtRigid(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOnLookAtRigid
         Returns the 'Associated to Object' mode look at point on look at object.  
             
         
        """
        pass
    @PointOnLookAtRigid.setter
    def PointOnLookAtRigid(self, lookAtPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOnLookAtRigid
         Returns the 'Associated to Object' mode look at point on look at object.  
             
         
        """
        pass
    @property
    def RotationSpeed(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) RotationSpeed
         Returns the rotational speed.  
             
         
        """
        pass
    @property
    def SpecifyTime(self) -> bool:
        """
        Getter for property: (bool) SpecifyTime
         Returns the 'Associated to Object' mode specify time option.  
             
         
        """
        pass
    @SpecifyTime.setter
    def SpecifyTime(self, specifyTime: bool):
        """
        Setter for property: (bool) SpecifyTime
         Returns the 'Associated to Object' mode specify time option.  
             
         
        """
        pass
    @property
    def StartPathPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPathPoint
         Returns the 'Associated to Object' mode associated curve start point.  
             
         
        """
        pass
    @StartPathPoint.setter
    def StartPathPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPathPoint
         Returns the 'Associated to Object' mode associated curve start point.  
             
         
        """
        pass
    @property
    def StartTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartTime
         Returns the 'Associated to Object' mode start time.  
             
         
        """
        pass
    @property
    def TransitionModeType(self) -> AnimatedCameraBuilder.TransitionModeTypes:
        """
        Getter for property: ( AnimatedCameraBuilder.TransitionModeTypes NXOpen.Anim) TransitionModeType
         Returns    the transition mode type.  
            
            
         
        """
        pass
    @TransitionModeType.setter
    def TransitionModeType(self, transitionModeType: AnimatedCameraBuilder.TransitionModeTypes):
        """
        Setter for property: ( AnimatedCameraBuilder.TransitionModeTypes NXOpen.Anim) TransitionModeType
         Returns    the transition mode type.  
            
            
         
        """
        pass
    def CreatePOV(self, currentTime: float) -> None:
        """
         Creates a new pov. 
        """
        pass
    def DeletePOVs(self, povs: List[int]) -> None:
        """
         Deletes the povs. 
        """
        pass
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluate the composited path from associated curves. 
        """
        pass
    def PlayKeyFrameAtTime(self, time: float) -> None:
        """
         Play key frame at time 
        """
        pass
    def SetPOVName(self, pos: int, name: str) -> None:
        """
         Sets the pov name. 
        """
        pass
    def SetPOVStartTime(self, pos: int, start_time: float) -> None:
        """
         Sets the pov start time. 
        """
        pass
    def SetPOVStepNumber(self, pos: int, step_num: int) -> None:
        """
         Sets the pov step count. 
        """
        pass
    def SetViewScale(self, fViewScale: float) -> None:
        """
         Sets the view scale value. 
        """
        pass
    def UpdateCurrentView(self, rotation: NXOpen.Matrix3x3, translation: NXOpen.Point3d, scale: float) -> None:
        """
         Updates current view 
        """
        pass
    def UpdatePOV(self, pos: int) -> None:
        """
         Updates a pov 
        """
        pass
import NXOpen
class AnimatedCameraCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Camera objects. """
    def CreateAnimatedCameraBuilder(part: NXOpen.Part, animatedCamera: AnimatedCamera) -> AnimatedCameraBuilder:
        """
         Creates a NXOpen.AnimationDesigner.AnimatedCameraBuilder. 
         Returns builder ( AnimatedCameraBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedCamera:
        """
         Finds the  NXOpen.AnimationDesigner.AnimatedCamera  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns animatedCamera ( AnimatedCamera NXOpen.Anim):   NXOpen.AnimationDesigner.AnimatedCamera  with this name. .
        """
        pass
import NXOpen
class AnimatedCamera(NXOpen.DisplayableObject): 
    """ Represents an Animated Camera feature. """
    pass
import NXOpen
class AnimatedColorBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.AnimatedColorBuilder. """
    class CreationTypes(Enum):
        """
        Members Include: 
         |CreateaSingleAnimatedColorEffect| 
         |CreateanAnimatedColorEffectperObject| 

        """
        CreateaSingleAnimatedColorEffect: int
        CreateanAnimatedColorEffectperObject: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedColorBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def CreationType(self) -> AnimatedColorBuilder.CreationTypes:
        """
        Getter for property: ( AnimatedColorBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type   
            
         
        """
        pass
    @CreationType.setter
    def CreationType(self, creationType: AnimatedColorBuilder.CreationTypes):
        """
        Setter for property: ( AnimatedColorBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type   
            
         
        """
        pass
    @property
    def EnableRepeatTime(self) -> bool:
        """
        Getter for property: (bool) EnableRepeatTime
         Returns the option determines whether to set the repeat time.  
             
         
        """
        pass
    @EnableRepeatTime.setter
    def EnableRepeatTime(self, enableRepeatTime: bool):
        """
        Setter for property: (bool) EnableRepeatTime
         Returns the option determines whether to set the repeat time.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def RepeatTime(self) -> int:
        """
        Getter for property: (int) RepeatTime
         Returns the repeat time.  
             
         
        """
        pass
    @RepeatTime.setter
    def RepeatTime(self, repeatTime: int):
        """
        Setter for property: (int) RepeatTime
         Returns the repeat time.  
             
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectObject
         Returns the select object   
            
         
        """
        pass
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    def MirrorBars(self, bars: List[int], mirror_time: float) -> None:
        """
         Mirrors the bars. 
        """
        pass
    def SetBarEndColor(self, index: int, color: NXOpen.NXColor) -> None:
        """
         Sets the bar end color. 
        """
        pass
    def SetBarEndTime(self, index: int, end_time: float) -> None:
        """
         Sets the bar end time. 
        """
        pass
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    def SetBarStartColor(self, index: int, color: NXOpen.NXColor) -> None:
        """
         Sets the bar start . 
        """
        pass
    def SetBarStartTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
    def SplitBar(self, index: int, split_time: float) -> None:
        """
         Splits the bar with the split time. 
        """
        pass
import NXOpen
class AnimatedColorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Color objects. """
    def CreateAnimatedColorBuilder(part: NXOpen.Part, animatedColor: AnimatedColor) -> AnimatedColorBuilder:
        """
         Creates a NXOpen.AnimationDesigner.AnimatedColorBuilder. 
         Returns builder ( AnimatedColorBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedColor:
        """
         Finds the  NXOpen.AnimationDesigner.AnimatedColor  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns animatedcolor ( AnimatedColor NXOpen.Anim):   NXOpen.AnimationDesigner.AnimatedColor  with this name. .
        """
        pass
import NXOpen
class AnimatedColor(NXOpen.DisplayableObject): 
    """ Represents an Animated Color feature. """
    pass
import NXOpen
class AnimatedExplodeBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.AnimatedExplodeBuilder. """
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the animated explode 
         |AutomaticColor|  Auto-assigns a color to each animated explode 
         |NoColor|  Assigns no color to the animated explode 

        """
        SpecifyColor: int
        AutomaticColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedExplodeBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreationTypes(Enum):
        """
        Members Include: 
         |Combine|  Combine all motion objects into one animated explode 
         |Separate|  Create an animated explode for each motion object 

        """
        Combine: int
        Separate: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedExplodeBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> AnimatedExplodeBuilder.ColorOptions:
        """
        Getter for property: ( AnimatedExplodeBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: AnimatedExplodeBuilder.ColorOptions):
        """
        Setter for property: ( AnimatedExplodeBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @property
    def ColorPickerFlowLineColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) ColorPickerFlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    @ColorPickerFlowLineColor.setter
    def ColorPickerFlowLineColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) ColorPickerFlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    @property
    def CreationType(self) -> AnimatedExplodeBuilder.CreationTypes:
        """
        Getter for property: ( AnimatedExplodeBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type.  
             
         
        """
        pass
    @CreationType.setter
    def CreationType(self, creationType: AnimatedExplodeBuilder.CreationTypes):
        """
        Setter for property: ( AnimatedExplodeBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type.  
             
         
        """
        pass
    @property
    def DefineFlowLineStyle(self) -> bool:
        """
        Getter for property: (bool) DefineFlowLineStyle
         Returns the define flow line style.  
             
         
        """
        pass
    @DefineFlowLineStyle.setter
    def DefineFlowLineStyle(self, defineflowlinestyle: bool):
        """
        Setter for property: (bool) DefineFlowLineStyle
         Returns the define flow line style.  
             
         
        """
        pass
    @property
    def DrawFlowLinePerObject(self) -> bool:
        """
        Getter for property: (bool) DrawFlowLinePerObject
         Returns the option for enable draw flow line per object.  
             
         
        """
        pass
    @DrawFlowLinePerObject.setter
    def DrawFlowLinePerObject(self, drawflowlineperobject: bool):
        """
        Setter for property: (bool) DrawFlowLinePerObject
         Returns the option for enable draw flow line per object.  
             
         
        """
        pass
    @property
    def LineFontFlowLineFont(self) -> int:
        """
        Getter for property: (int) LineFontFlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    @LineFontFlowLineFont.setter
    def LineFontFlowLineFont(self, font: int):
        """
        Setter for property: (int) LineFontFlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    @property
    def LineWidthFlowLineWidth(self) -> int:
        """
        Getter for property: (int) LineWidthFlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    @LineWidthFlowLineWidth.setter
    def LineWidthFlowLineWidth(self, width: int):
        """
        Setter for property: (int) LineWidthFlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    @property
    def MotionObject(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) MotionObject
         Returns the object to animated explode.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def ShowFlowLineInSimulation(self) -> bool:
        """
        Getter for property: (bool) ShowFlowLineInSimulation
         Returns the use specified flow line.  
             
         
        """
        pass
    @ShowFlowLineInSimulation.setter
    def ShowFlowLineInSimulation(self, showflowlineinsimulation: bool):
        """
        Setter for property: (bool) ShowFlowLineInSimulation
         Returns the use specified flow line.  
             
         
        """
        pass
    def DeleteStep(self, pos: int) -> None:
        """
         Deletes the step. 
        """
        pass
    def GetStepCount(self) -> int:
        """
         Gets the step count. 
         Returns count (int): .
        """
        pass
    def InsertStep(self, pos: int, startTime: float, duration: float, distance: float, spin: float, angle: float, dir: NXOpen.Direction) -> None:
        """
         Inserts a step. 
        """
        pass
    def MirrorSteps(self, steps: List[int], mirror_time: float) -> List[int]:
        """
         Mirrors the steps. 
         Returns newSteps (List[int]): .
        """
        pass
    def SetStepAngle(self, pos: int, angle: float) -> None:
        """
         Sets the step angle. 
        """
        pass
    def SetStepDirection(self, pos: int, dir: NXOpen.Direction) -> None:
        """
         Sets the step direction. 
        """
        pass
    def SetStepDistance(self, pos: int, distance: float) -> None:
        """
         Sets the step distance. 
        """
        pass
    def SetStepDuration(self, pos: int, duration: float) -> None:
        """
         Sets the step duration. 
        """
        pass
    def SetStepName(self, pos: int, name: str) -> None:
        """
         Sets the step name. 
        """
        pass
    def SetStepSpin(self, pos: int, spin: float) -> None:
        """
         Sets the step spin. 
        """
        pass
    def SetStepStartTime(self, pos: int, start_time: float) -> None:
        """
         Sets the step start time. 
        """
        pass
    def SetStepTargetPosition(self, pos: int, rotation: NXOpen.Matrix4x4) -> None:
        """
         Sets the step rotation. 
        """
        pass
    def SetStepUseOrigin(self, pos: int, useOrigin: bool) -> None:
        """
         Sets the step flag use origin. 
        """
        pass
    def SplitStep(self, pos: int, split_time: float) -> bool:
        """
         Splits the step with the split time. 
         Returns splited (bool): .
        """
        pass
import NXOpen
class AnimatedExplodeCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Explode objects. """
    def CreateAnimatedExplodeBuilder(part: NXOpen.Part, animatedexplode: AnimatedExplode) -> AnimatedExplodeBuilder:
        """
         Creates a NXOpen.AnimationDesigner.AnimatedExplodeBuilder. 
         Returns builder ( AnimatedExplodeBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedExplode:
        """
         Finds the  NXOpen.AnimationDesigner.AnimatedExplode  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns explode ( AnimatedExplode NXOpen.Anim):   NXOpen.AnimationDesigner.AnimatedExplode  with this name. .
        """
        pass
import NXOpen
class AnimatedExplode(NXOpen.DisplayableObject): 
    """ Represents an animated explode feature. """
    pass
import NXOpen
class AnimatedVisibilityBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.AnimatedVisibilityBuilder. """
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the visibility 
         |AutomaticColor|  Auto-assigns a color to each visibility 
         |NoColor|  Assigns no color to the visibility 

        """
        SpecifyColor: int
        AutomaticColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedVisibilityBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreationTypes(Enum):
        """
        Members Include: 
         |Combine|  Combine selections into one animated visibility 
         |Separate|  Create an animated visibility for each selection 

        """
        Combine: int
        Separate: int
        @staticmethod
        def ValueOf(value: int) -> AnimatedVisibilityBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> AnimatedVisibilityBuilder.ColorOptions:
        """
        Getter for property: ( AnimatedVisibilityBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: AnimatedVisibilityBuilder.ColorOptions):
        """
        Setter for property: ( AnimatedVisibilityBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @property
    def CreationType(self) -> AnimatedVisibilityBuilder.CreationTypes:
        """
        Getter for property: ( AnimatedVisibilityBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type.  
             
         
        """
        pass
    @CreationType.setter
    def CreationType(self, creationType: AnimatedVisibilityBuilder.CreationTypes):
        """
        Setter for property: ( AnimatedVisibilityBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def RigidGroup(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) RigidGroup
         Returns the rigid group to display translucency.  
           This can be a  NXOpen::AnimationDesigner::RigidGroup .   
         
        """
        pass
    @property
    def Translucency(self) -> int:
        """
        Getter for property: (int) Translucency
         Returns the translucency.  
             
         
        """
        pass
    @Translucency.setter
    def Translucency(self, translucency: int):
        """
        Setter for property: (int) Translucency
         Returns the translucency.  
             
         
        """
        pass
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    def MirrorBars(self, bars: List[int], mirror_time: float) -> None:
        """
         Mirrors the bars. 
        """
        pass
    def SetBarEndTime(self, index: int, end_time: float) -> None:
        """
         Sets the bar end time. 
        """
        pass
    def SetBarEndTranslucency(self, index: int, translucency: int) -> None:
        """
         Sets the bar end translucency. 
        """
        pass
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    def SetBarStartTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
    def SetBarStartTranslucency(self, index: int, translucency: int) -> None:
        """
         Sets the bar start translucency. 
        """
        pass
    def SplitBar(self, index: int, split_time: float) -> None:
        """
         Splits the bar with the split time. 
        """
        pass
import NXOpen
class AnimatedVisibilityCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Animated Visibility objects. """
    def CreateAnimatedVisibilityBuilder(part: NXOpen.Part, animatedVisibility: AnimatedVisibility) -> AnimatedVisibilityBuilder:
        """
         Creates a NXOpen.AnimationDesigner.AnimatedVisibilityBuilder. 
         Returns builder ( AnimatedVisibilityBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> AnimatedVisibility:
        """
         Finds the  NXOpen.AnimationDesigner.AnimatedVisibility  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns animatedVisibility ( AnimatedVisibility NXOpen.Anim):   NXOpen.AnimationDesigner.AnimatedVisibility  with this name. .
        """
        pass
import NXOpen
class AnimatedVisibility(NXOpen.DisplayableObject): 
    """ Represents an Animated Visibility feature. """
    pass
import NXOpen
import NXOpen.AnimationDesigner.Nav
import NXOpen.Facet
class AnimationDesignerManager(NXOpen.Object): 
    """ Represents an object to manage Animation Designer application objects. """
    class JaAnimationDesignerDisplayColorOption(Enum):
        """
        Members Include: 
         |ShowRigid|  show rigid group color 
         |ClearRigid|  clear rigid group color 
         |ShowExplode|  show explode color 
         |ClearExplode|  clear explode color 
         |ShowVisibility|  show visibility color 
         |ClearVisibility|  clear visibility color 
         |ShowMotor|  show motor color 
         |ClearMotor|  clear motor color 
         |ShowFlexibleObject|  show flexible object color 
         |ClearFlexibleObject|  clear flexible object color 
         |ShowJoint|  show joint color 
         |ClearJoint|  clear joint color 
         |ShowCoupler|  show coupler color 
         |ClearCoupler|  clear coupler color 

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
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerDisplayColorOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaAnimationDesignerEnvelopeAccuracyMode(Enum):
        """
        Members Include: 
         |Low|  accuracy low 
         |Medium|  accuracy medium 
         |High|  accuracy high 
         |Custom|  accuracy custom 

        """
        Low: int
        Medium: int
        High: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaAnimationDesignerEnvelopeMode(Enum):
        """
        Members Include: 
         |Work|  work mode  
         |Test|  autounit test mode 

        """
        Work: int
        Test: int
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerEnvelopeMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaAnimationDesignerInterferenceType(Enum):
        """
        Members Include: 
         |Highlight|  Highlight  
         |ShowCurve|  Show Intersection Curve 

        """
        Highlight: int
        ShowCurve: int
        @staticmethod
        def ValueOf(value: int) -> AnimationDesignerManager.JaAnimationDesignerInterferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Solutions() -> NXOpen.AnimationDesigner.Nav.SolutionCollection:
        """
         Returns the  NXOpen::AnimationDesigner::Nav::SolutionCollection  belonging to this application. 
        """
        pass
    @property
    def RigidGroups() -> RigidGroupCollection:
        """
         Returns the  NXOpen::AnimationDesigner::RigidGroupCollection  belonging to this application. 
        """
        pass
    @property
    def Contacts() -> ContactCollection:
        """
         Returns the  NXOpen::AnimationDesigner::ContactCollection  belonging to this application. 
        """
        pass
    @property
    def RevoluteJoints() -> RevoluteJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::RevoluteJointCollection  belonging to this application. 
        """
        pass
    @property
    def SliderJoints() -> SliderJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::SliderJointCollection  belonging to this application. 
        """
        pass
    @property
    def CylindricalJoints() -> CylindricalJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::CylindricalJointCollection  belonging to this application. 
        """
        pass
    @property
    def SphericalJoints() -> SphericalJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::SphericalJointCollection  belonging to this application. 
        """
        pass
    @property
    def FixedJoints() -> FixedJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::FixedJointCollection  belonging to this application. 
        """
        pass
    @property
    def Gears() -> GearCollection:
        """
         Returns the  NXOpen::AnimationDesigner::GearCollection  belonging to this application. 
        """
        pass
    @property
    def RackPinions() -> RackPinionCollection:
        """
         Returns the  NXOpen::AnimationDesigner::RackPinionCollection  belonging to this application. 
        """
        pass
    @property
    def PositionMotors() -> PositionMotorCollection:
        """
         Returns the  NXOpen::AnimationDesigner::PositionMotorCollection  belonging to this application. 
        """
        pass
    @property
    def SpeedMotors() -> SpeedMotorCollection:
        """
         Returns the  NXOpen::AnimationDesigner::SpeedMotorCollection  belonging to this application. 
        """
        pass
    @property
    def Measures() -> MeasureCollection:
        """
         Returns the  NXOpen::AnimationDesigner::MeasureCollection  belonging to this application. 
        """
        pass
    @property
    def PointOnCurveJoints() -> PointOnCurveJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::PointOnCurveJointCollection  belonging to this application. 
        """
        pass
    @property
    def CurveOnCurveJoints() -> CurveOnCurveJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::CurveOnCurveJointCollection  belonging to this application. 
        """
        pass
    @property
    def MechanicalCams() -> MechanicalCamCollection:
        """
         Returns the  NXOpen::AnimationDesigner::MechanicalCamCollection  belonging to this application. 
        """
        pass
    @property
    def ScrewJoints() -> ScrewJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::ScrewJointCollection  belonging to this application. 
        """
        pass
    @property
    def PlanarJoints() -> PlanarJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::PlanarJointCollection  belonging to this application. 
        """
        pass
    @property
    def AnimatedVisibilities() -> AnimatedVisibilityCollection:
        """
         Returns the  NXOpen::AnimationDesigner::AnimatedVisibilityCollection  belonging to this application. 
        """
        pass
    @property
    def AnimatedCameras() -> AnimatedCameraCollection:
        """
         Returns the  NXOpen::AnimationDesigner::AnimatedCameraCollection  belonging to this application. 
        """
        pass
    @property
    def AnimatedExplodes() -> AnimatedExplodeCollection:
        """
         Returns the  NXOpen::AnimationDesigner::AnimatedExplodeCollection  belonging to this application. 
        """
        pass
    @property
    def AnimatedColors() -> AnimatedColorCollection:
        """
         Returns the  NXOpen::AnimationDesigner::AnimatedColorCollection  belonging to this application. 
        """
        pass
    @property
    def JointJoggers() -> JointJoggerCollection:
        """
         Returns the  NXOpen::AnimationDesigner::JointJoggerCollection  belonging to this application. 
        """
        pass
    @property
    def InverseKinematics() -> InverseKinematicsCollection:
        """
         Returns the  NXOpen::AnimationDesigner::InverseKinematicsCollection  belonging to this application. 
        """
        pass
    @property
    def PathConstraintJoints() -> PathConstraintJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::PathConstraintJointCollection  belonging to this application. 
        """
        pass
    @property
    def Tracers() -> TracerCollection:
        """
         Returns the  NXOpen::AnimationDesigner::TracerCollection  belonging to this application. 
        """
        pass
    @property
    def BondJoints() -> BondJointCollection:
        """
         Returns the  NXOpen::AnimationDesigner::BondJointCollection  belonging to this application. 
        """
        pass
    @property
    def Containers() -> NXOpen.AnimationDesigner.Nav.ContainerCollection:
        """
         Returns the  NXOpen::AnimationDesigner::Nav::ContainerCollection  belonging to this application. 
        """
        pass
    @property
    def SubFolders() -> NXOpen.AnimationDesigner.Nav.SubFolderCollection:
        """
         Returns the  NXOpen::AnimationDesigner::Nav::SubFolderCollection  belonging to this application. 
        """
        pass
    @property
    def BulletCables() -> BulletCableCollection:
        """
           Returns the  NXOpen::AnimationDesigner::BulletCableCollection   belonging to this part  
         
        """
        pass
    @property
    def BulletFlexibleMaterials() -> BulletFlexibleMaterialCollection:
        """
           Returns the  NXOpen::AnimationDesigner::BulletFlexibleMaterialCollection   belonging to this part  
         
        """
        pass
    @property
    def FlexibleCables() -> FlexibleCableCollection:
        """
           Returns the  NXOpen::AnimationDesigner::FlexibleCableCollection   belonging to this part  
         
        """
        pass
    @property
    def FlexibleMaterials() -> FlexibleMaterialCollection:
        """
           Returns the  NXOpen::AnimationDesigner::FlexibleMaterialCollection   belonging to this part  
         
        """
        pass
    @property
    def PointOnCurveKinematicsChains() -> PointOnCurveKinematicsChainCollection:
        """
           Returns the  NXOpen::AnimationDesigner::PointOnCurveKinematicsChainCollection  belonging to this application.  
         
        """
        pass
    @property
    def ActivityOperators() -> ActivityOperatorCollection:
        """
           Returns the  NXOpen::AnimationDesigner::ActivityOperatorCollection  belonging to this application.  
         
        """
        pass
    def ApplyPhysicsColor(displayOption: AnimationDesignerManager.JaAnimationDesignerDisplayColorOption) -> None:
        """
        Show or clear physics color.  
        """
        pass
    def AutoSolve(part: NXOpen.Part) -> None:
        """
         Records the auto solve data for Animation Designer. 
        """
        pass
    def AutoSolveClear(part: NXOpen.Part) -> None:
        """
         Clears the auto solve data for Animation Designer. 
        """
        pass
    def AutoSolveRecord(part: NXOpen.Part, physics_object: NXOpen.NXObject, matrix: List[float]) -> None:
        """
         Records the auto solve data for Animation Designer. 
        """
        pass
    def ChangeMotionType(part: NXOpen.Part, objects: List[NXOpen.NXObject], motionType: PhysicsJointBuilder.MotionTypes) -> None:
        """
         Changes motion type. 
        """
        pass
    def CreateConstraintConversionBuilder(part: NXOpen.Part) -> ConstraintConversionBuilder:
        """
         Creates a AnimationDesigner.ConstraintConversionBuilder 
         Returns builder ( ConstraintConversionBuilder NXOpen.Anim): .
        """
        pass
    def CreateContainer(part: NXOpen.Part, containerName: str) -> None:
        """
         Creates a container in navigator. 
        """
        pass
    def CreateEnvelope(physics_object: NXOpen.NXObject, geometry: NXOpen.NXObject, tolerance: float, mode: AnimationDesignerManager.JaAnimationDesignerEnvelopeMode, translucency: int) -> NXOpen.Facet.FacetedBody:
        """
         Creates an Envelope object. 
         Returns envelope ( NXOpen.Facet.FacetedBody): .
        """
        pass
    def CreateEnvelopes(physicsObject: List[NXOpen.NXObject], geometry: List[NXOpen.NXObject], physicsToGeometry: List[int], tolerance: float, mode: AnimationDesignerManager.JaAnimationDesignerEnvelopeMode, translucency: int) -> List[NXOpen.Facet.FacetedBody]:
        """
         Creates Envelope objects. 
         Returns envelopeList ( NXOpen.Facet.FacetedBody Li): .
        """
        pass
    def CreateExportTraceBuilder(part: NXOpen.Part, tracer: Tracer) -> ExportTraceBuilder:
        """
         Creates a NXOpen.AnimationDesigner.ExportTraceBuilder object. 
         Returns builder ( ExportTraceBuilder NXOpen.Anim):  ExportTraceBuilder.
        """
        pass
    def CreateFlexibleCableFacetBody(flexibleCableTag: NXOpen.NXObject, vertexList: List[NXOpen.Point3d], widthDirectionList: List[NXOpen.Vector3d], radius: float, width: float, thickness: float) -> NXOpen.NXObject:
        """
         Create facet body for flexible cable. 
         Returns facetBody ( NXOpen.NXObject): .
        """
        pass
    def CreateInterference(firstEnvelope: NXOpen.Facet.FacetedBody, secondEnvelope: NXOpen.Facet.FacetedBody, outputType: AnimationDesignerManager.JaAnimationDesignerInterferenceType) -> None:
        """
         Creates an Interference object. 
        """
        pass
    def CreateInverseKinematicsBuilder(part: NXOpen.Part) -> InverseKinematicsBuilder:
        """
         Creates a AnimationDesigner.InverseKinematicsBuilder 
         Returns builder ( InverseKinematicsBuilder NXOpen.Anim): .
        """
        pass
    def CreatePreferenceBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates the preferences builder for Animation Designer. 
         Returns builder ( PreferencesBuilder NXOpen.Anim): .
        """
        pass
    def CreateSingleEnvelope(geometry: NXOpen.NXObject, transformMatrixList: List[NXOpen.Matrix4x4], destinationPart: NXOpen.NXObject, tolerance: float, translucency: int, color: int) -> NXOpen.Facet.FacetedBody:
        """
         Creates an envelope object for a signle geometry. 
         Returns createEnvelope ( NXOpen.Facet.FacetedBody): .
        """
        pass
    def CreateSingleEnvelope2(geometry: NXOpen.NXObject, transformMatrixList: List[NXOpen.Matrix4x4], destinationPart: NXOpen.NXObject, accuracyMode: AnimationDesignerManager.JaAnimationDesignerEnvelopeAccuracyMode, tolerance: float, translucency: int, color: int) -> NXOpen.Facet.FacetedBody:
        """
         Creates an envelope object for a signle geometry 2. 
         Returns createEnvelope ( NXOpen.Facet.FacetedBody): .
        """
        pass
    def CreateSnapshot(time: float, isRecordManagerMode: bool) -> None:
        """
        Simulation first to ensure AutoSolveRecordData is not empty , then create a snapshot.  
        """
        pass
    def CreateSolution(part: NXOpen.Part) -> NXOpen.AnimationDesigner.Nav.Solution:
        """
         Creates the solution for Animation Designer. 
         Returns studyFolder ( NXOpen.AnimationDesigner.Nav.Solution): .
        """
        pass
    def DuplicateSolution(part: NXOpen.Part, originalSolution: NXOpen.AnimationDesigner.Nav.Solution, copiedSolution: NXOpen.AnimationDesigner.Nav.Solution) -> List[NXOpen.NXObject]:
        """
         Clones the solution for Animation Designer. 
         Returns failList ( NXOpen.NXObject Li): .
        """
        pass
    def EditSnapshotAddTime(physics_object: NXOpen.NXObject, time: float, isRecordManagerMode: bool) -> None:
        """
        Add one spot in snapshot. Please simulation first to ensuer AutoSolveRecordData is not empty 
        """
        pass
    def EditSnapshotDeleteTime(physics_object: NXOpen.NXObject, time: float) -> None:
        """
         Delete one spot in snapshot. 
        """
        pass
    def ExportPlmxmlInNative(dirName: str, configFileName: str, reportWind: bool) -> None:
        """
         Exports the PLMXML from Animation Designer in native. 
        """
        pass
    def ExportPlmxmlInTeamcenter() -> None:
        """
         Exports the PLMXML from Animation Designer in teamcenter. 
        """
        pass
    def GetActiveSolution(part: NXOpen.Part) -> NXOpen.AnimationDesigner.Nav.Solution:
        """
         Gets the active solution for Animation Designer. 
         Returns studyFolder ( NXOpen.AnimationDesigner.Nav.Solution): .
        """
        pass
    def IgnoreCollisionInterferedNode(part: NXOpen.Part, firstGeometry: NXOpen.NXObject, secondGeometry: NXOpen.NXObject) -> None:
        """
         Ignores a collision interfered node. 
        """
        pass
    def ImportPlmxmlInNative(fileName: str, reportWind: bool) -> None:
        """
         Imports the PLMXML for Animation Designer in native. 
        """
        pass
    def ImportPlmxmlInTeamcenter() -> None:
        """
         Imports the PLMXML for Animation Designer in teamcenter. 
        """
        pass
    def ModelingInAnimationContext(part: NXOpen.Part, bFreeze: bool) -> None:
        """
         Indicates whether to freeze the animation position to do modeling operations. 
        """
        pass
    def MoveContactFacesToRigid(solutionTag: NXOpen.AnimationDesigner.Nav.Solution, objects: List[Contact], target: RigidGroup) -> None:
        """
         Moves contact face objects to their rigid parent. 
        """
        pass
    def MovePhysicsToContainer(solutionTag: NXOpen.AnimationDesigner.Nav.Solution, objects: List[NXOpen.NXObject], target: NXOpen.AnimationDesigner.Nav.Container) -> None:
        """
         Moves objects to container in navigator. 
        """
        pass
    def MovePhysicsToSubfolder(solutionTag: NXOpen.AnimationDesigner.Nav.Solution, objects: List[NXOpen.NXObject], target: NXOpen.AnimationDesigner.Nav.SubFolder) -> None:
        """
         Moves objects to back to default folder in navigator. 
        """
        pass
    def ReorderContainers(parent: NXOpen.AnimationDesigner.Nav.Solution, objects: List[NXOpen.AnimationDesigner.Nav.Container], target: NXOpen.AnimationDesigner.Nav.Container) -> None:
        """
         Reorders containers in navigator. 
        """
        pass
    def ResetReservedLicense(licenseModule: str) -> None:
        """
         Frees the Animation Designer reserved license for autotest. 
        """
        pass
    def RestoreCollisionIgnoredNode(part: NXOpen.Part, firstGeometry: NXOpen.NXObject, secondGeometry: NXOpen.NXObject) -> None:
        """
         Restores a collision ignored node. 
        """
        pass
    def SetActiveSolution(part: NXOpen.Part, studyFolder: NXOpen.AnimationDesigner.Nav.Solution) -> None:
        """
         Sets the active solution for Animation Designer. 
        """
        pass
    def SetCollisionThreshold(part: NXOpen.Part, threshold: float) -> None:
        """
         Sets a collision threshold. 
        """
        pass
    def SetName(part: NXOpen.Part, physics_object: NXOpen.NXObject, name: str) -> None:
        """
         Renames the physics object for Animation Designer. 
        """
        pass
    def SetSubfolderDisplayOrHide(folder_object: NXOpen.NXObject, bDisplay: bool) -> None:
        """
         Sets the display or hide state of folder object in OM class. 
        """
        pass
    def ShowHideRigidGroupGeometry(rigidTag: List[NXOpen.NXObject], isShown: bool) -> None:
        """
         Showshides rigid groups. 
        """
        pass
    def UpdateMotorIndex(part: NXOpen.Part, motor: NXOpen.NXObject, index: int) -> None:
        """
         Update the motor index for Animation Designer. 
        """
        pass
    def UpdateSubfolderAndIconsDisplayState(folder_object: NXOpen.NXObject, bDisplay: bool, bHandleIcons: bool) -> None:
        """
         Updates the display or hide state of folder object in OM class and icons in 3D graphic. 
        """
        pass
    def WriteBlankStatus(physics_object: NXOpen.NXObject, blank: int) -> None:
        """
         Blanks the physics object for Animation Designer. 
        """
        pass
class BondJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.BondJointBuilder. """
    pass
import NXOpen
class BondJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Bond Joint objects. """
    def CreateBondJointBuilder(part: NXOpen.Part, bondJoint: BondJoint) -> BondJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.BondJointBuilder. 
         Returns builder ( BondJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> BondJoint:
        """
         Finds the  NXOpen.AnimationDesigner.BondJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns bondJoint ( BondJoint NXOpen.Anim):   NXOpen.AnimationDesigner.BondJoint  with this name. .
        """
        pass
class BondJoint(PhysicsJoint): 
    """ Represents a Bond Joint feature. """
    pass
import NXOpen
class BulletCableAttachmentBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[BulletCableAttachmentBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: BulletCableAttachmentBuilder) -> None:
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
    def Erase(self, obj: BulletCableAttachmentBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: BulletCableAttachmentBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: BulletCableAttachmentBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> BulletCableAttachmentBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( BulletCableAttachmentBuilder NXOpen.Anim):  object found at input index .
        """
        pass
    def GetContents(self) -> List[BulletCableAttachmentBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( BulletCableAttachmentBuilder List[NXOpen.An):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: BulletCableAttachmentBuilder) -> None:
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
    def SetContents(self, objects: List[BulletCableAttachmentBuilder]) -> None:
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
    def Swap(self, object1: BulletCableAttachmentBuilder, object2: BulletCableAttachmentBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class BulletCableAttachmentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.BulletCableAttachmentBuilder. """
    @property
    def Anchor(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Anchor
         Returns   the anchor point.  
            
           
         
        """
        pass
    @Anchor.setter
    def Anchor(self, anchor: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Anchor
         Returns   the anchor point.  
            
           
         
        """
        pass
    @property
    def Attachment(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Attachment
         Returns   the atttachment.  
            
           
         
        """
        pass
    @property
    def Direction(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Direction
         Returns   the direction vector.  
            
           
         
        """
        pass
    @Direction.setter
    def Direction(self, direction: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Direction
         Returns   the direction vector.  
            
           
         
        """
        pass
import NXOpen
class BulletCableBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.BulletCableBuilder. """
    class DerivationType(Enum):
        """
        Members Include: 
         |Curve|  the guide curves 
         |Body|  the cable body 

        """
        Curve: int
        Body: int
        @staticmethod
        def ValueOf(value: int) -> BulletCableBuilder.DerivationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttachmentList(self) -> BulletCableAttachmentBuilderList:
        """
        Getter for property: ( BulletCableAttachmentBuilderList NXOpen.Anim) AttachmentList
         Returns   the list containing the defined attachments.  
            
           
         
        """
        pass
    @property
    def CableBody(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) CableBody
         Returns   the cable body.  
            
           
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns   the diameter.  
            
           
         
        """
        pass
    @property
    def GeometryType(self) -> BulletCableBuilder.DerivationType:
        """
        Getter for property: ( BulletCableBuilder.DerivationType NXOpen.Anim) GeometryType
         Returns   the geometry type used to derive the bullet cable.  
            
           
         
        """
        pass
    @GeometryType.setter
    def GeometryType(self, geometryType: BulletCableBuilder.DerivationType):
        """
        Setter for property: ( BulletCableBuilder.DerivationType NXOpen.Anim) GeometryType
         Returns   the geometry type used to derive the bullet cable.  
            
           
         
        """
        pass
    @property
    def GuideCurves(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) GuideCurves
         Returns   the guide curves.  
            
           
         
        """
        pass
    @property
    def Material(self) -> BulletFlexibleMaterial:
        """
        Getter for property: ( BulletFlexibleMaterial NXOpen.Anim) Material
         Returns   the material.  
           This can be a  NXOpen::AnimationDesigner::BulletFlexibleMaterial .  
           
         
        """
        pass
    @Material.setter
    def Material(self, material: BulletFlexibleMaterial):
        """
        Setter for property: ( BulletFlexibleMaterial NXOpen.Anim) Material
         Returns   the material.  
           This can be a  NXOpen::AnimationDesigner::BulletFlexibleMaterial .  
           
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
import NXOpen
class BulletCableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Bullet Cable object. """
    def CreateBulletCableAttachmentBuilder(part: NXOpen.Part) -> BulletCableAttachmentBuilder:
        """
         Creates a NXOpen.AnimationDesigner.BulletCableAttachmentBuilder. 
         Returns builder ( BulletCableAttachmentBuilder NXOpen.Anim): .
        """
        pass
    def CreateBulletCableBuilder(part: NXOpen.Part, cable: BulletCable) -> BulletCableBuilder:
        """
         Creates a NXOpen.AnimationDesigner.BulletCableBuilder. 
         Returns builder ( BulletCableBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> BulletCable:
        """
         Finds the  NXOpen.AnimationDesigner.BulletCable  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns cable ( BulletCable NXOpen.Anim):   NXOpen.AnimationDesigner.BulletCable  with this name. .
        """
        pass
import NXOpen
class BulletCable(NXOpen.DisplayableObject): 
    """ Represents a Bullet Cable feature. """
    pass
import NXOpen
class BulletFlexibleMaterialBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.BulletFlexibleMaterialBuilder. """
    @property
    def DampingValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DampingValue
         Returns   the damping value  
          
          
           
         
        """
        pass
    @property
    def DensityValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DensityValue
         Returns   the density value  
          
          
           
         
        """
        pass
    @property
    def DynamicFrictionValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DynamicFrictionValue
         Returns   the dynamic friction value  
          
          
           
         
        """
        pass
    @property
    def LinearStiffnessValue(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearStiffnessValue
         Returns   the linear stiffness value  
          
          
           
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
import NXOpen
class BulletFlexibleMaterialCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Bullet Flexible Material object. """
    def CreateBulletFlexibleMaterialBuilder(part: NXOpen.Part, material: BulletFlexibleMaterial) -> BulletFlexibleMaterialBuilder:
        """
         Creates a NXOpen.AnimationDesigner.BulletFlexibleMaterialBuilder. 
         Returns builder ( BulletFlexibleMaterialBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> BulletFlexibleMaterial:
        """
         Finds the  NXOpen.AnimationDesigner.BulletFlexibleMaterial  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns material ( BulletFlexibleMaterial NXOpen.Anim):   NXOpen.AnimationDesigner.BulletFlexibleMaterial  with this name. .
        """
        pass
import NXOpen
class BulletFlexibleMaterial(NXOpen.DisplayableObject): 
    """ Represents a Bullet Flexible Material feature. """
    pass
import NXOpen
class ConstraintConversionBuilder(NXOpen.Builder): 
    """ Represents a AnimationDesigner.ConstraintConversionBuilder builder """
    class AssemblyObjectTypes(Enum):
        """
        Members Include: 
         |Constraint|  Assembly Constraint 
         |JointAndCoupler|  Assembly Joint and Coupler 
         |All|  Adopt all mode Joint and Coupler 

        """
        Constraint: int
        JointAndCoupler: int
        All: int
        @staticmethod
        def ValueOf(value: int) -> ConstraintConversionBuilder.AssemblyObjectTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def EnableObjectsConversion(self, physics: List[NXOpen.NXObject], enable: bool) -> None:
        """
          Enables the conversion of objects. If it is impossible, the objects will keep unable status.  
        """
        pass
    def GetTentativeAssemblyNames(self) -> List[str]:
        """
          Returns the tentatively converting assembly names.  
         Returns assNames (List[str]): .
        """
        pass
    def GetTentativePhysics(self) -> List[NXOpen.NXObject]:
        """
          Returns the tentatively converting physics objects.  
         Returns physics ( NXOpen.NXObject Li): .
        """
        pass
    def SetAssemblyObjectType(self, type: ConstraintConversionBuilder.AssemblyObjectTypes) -> None:
        """
          Sets the assembly object type to convert.  
        """
        pass
    def TentativelyConvert(self) -> None:
        """
          Tentatively converts assembly constraints.  
        """
        pass
import NXOpen
class ContactBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.ContactBuilder. """
    @property
    def Geometry(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Geometry
         Returns the geometries.  
           This can be a  NXOpen::Assemblies::ComponentAssembly ,
                     NXOpen::Point ,  NXOpen::Face ,
                     NXOpen::Edge , bodies and curves.   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    def SetGeometry(self, geometries: List[NXOpen.NXObject]) -> None:
        """
         Sets the geometry 
        """
        pass
import NXOpen
class ContactCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Contact objects. """
    def CreateContactBuilder(part: NXOpen.Part, contactFace: Contact) -> ContactBuilder:
        """
         Creates a NXOpen.AnimationDesigner.ContactBuilder. 
         Returns builder ( ContactBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> Contact:
        """
         Finds the  NXOpen.AnimationDesigner.Contact  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns contactFace ( Contact NXOpen.Anim):   NXOpen.AnimationDesigner.Contact  with this name. .
        """
        pass
import NXOpen
class Contact(NXOpen.DisplayableObject): 
    """ Represents a Contact feature. """
    pass
class Convention(Enum):
    """
    Members Include: 
     |Xyz|  
     |Xzy|  
     |Yxz|  
     |Yzx|  
     |Zxy|  
     |Zyx|  
     |Xyx|  
     |Xzx|  
     |Yxy|  
     |Yzy|  
     |Zxz|  
     |Zyz|  

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
    @staticmethod
    def ValueOf(value: int) -> Convention:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass
import NXOpen
class CouplerBuilder(NXOpen.Builder): 
    """ Represents a base builder for Couplers. """
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the coupler 
         |NoColor|  Assigns no color to the coupler 

        """
        SpecifyColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> CouplerBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> CouplerBuilder.ColorOptions:
        """
        Getter for property: ( CouplerBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color options.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: CouplerBuilder.ColorOptions):
        """
        Setter for property: ( CouplerBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color options.  
             
         
        """
        pass
    @property
    def MasterAxisJoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) MasterAxisJoint
         Returns the master axis joint.  
           This can be a  NXOpen::AnimationDesigner::RevoluteJoint ,  NXOpen::AnimationDesigner::SliderJoint  or
                     NXOpen::AnimationDesigner::CylindricalJoint .   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def SlaveAxisJoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SlaveAxisJoint
         Returns the slave axis joint.  
           This can be a  NXOpen::AnimationDesigner::RevoluteJoint ,  NXOpen::AnimationDesigner::SliderJoint  or
                     NXOpen::AnimationDesigner::CylindricalJoint .   
         
        """
        pass
import NXOpen
class Coupler(NXOpen.DisplayableObject): 
    """ Represents the Animation Designer coupler class. """
    pass
import NXOpen
class CurveOnCurveJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.CurveOnCurveJointBuilder. """
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset specifies the "Zero Point" on the curve whose distance to the point along the curve is the offset value.  
          
                    Zero Point is on the opposite direction of the axis with respect to the point on the curve.   
         
        """
        pass
    @property
    def PointOnCurve(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    @PointOnCurve.setter
    def PointOnCurve(self, pointOnCurve: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    @property
    def Sliding(self) -> bool:
        """
        Getter for property: (bool) Sliding
         Returns the sliding flag.  
             
         
        """
        pass
    @Sliding.setter
    def Sliding(self, sliding: bool):
        """
        Setter for property: (bool) Sliding
         Returns the sliding flag.  
             
         
        """
        pass
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluates the path. If there is no path, create it, otherwise evaluate it. 
        """
        pass
    def GetConnectedCurve(self) -> List[NXOpen.NXObject]:
        """
         Gets the connected curve which the attachment will move along. 
         Returns curves ( NXOpen.NXObject Li):  curve or edge .
        """
        pass
    def GetSectionCurve(self) -> List[NXOpen.NXObject]:
        """
         Gets the section curve which belong to the attachment. 
         Returns curves ( NXOpen.NXObject Li):  curve or edge .
        """
        pass
    def SetConnectedCurve(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Sets the connected curve which the attachment will move along. 
        """
        pass
    def SetSectionCurve(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Sets the section curve which belong to the attachment. 
        """
        pass
import NXOpen
class CurveOnCurveJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Curve On Curve Joint objects. """
    def CreateCurveOnCurveJointBuilder(part: NXOpen.Part, joint: CurveOnCurveJoint) -> CurveOnCurveJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.CurveOnCurveJointBuilder. 
         Returns builder ( CurveOnCurveJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> CurveOnCurveJoint:
        """
         Finds the  NXOpen.AnimationDesigner.CurveOnCurveJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns curveOnCurveJoint ( CurveOnCurveJoint NXOpen.Anim):   NXOpen.AnimationDesigner.CurveOnCurveJoint  with this name. .
        """
        pass
class CurveOnCurveJoint(PhysicsJoint): 
    """ Represents a Curve On Curve Joint feature. """
    pass
import NXOpen
class CylindricalJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.CylindricalJointBuilder. """
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
    @property
    def AngularLowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularLowerLimit
         Returns the angular lower limit.  
           The lower limit setup for joint angular movement.   
         
        """
        pass
    @property
    def AngularUpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularUpperLimit
         Returns the angular upper limit.  
           The upper limit setup for joint angular movement.   
         
        """
        pass
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    @property
    def EnableAngularLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableAngularLowerLimit
         Returns the angular lower limit option.  
           If the enable is true, then this joint will be
                    applied the lower limit in angular direction.   
         
        """
        pass
    @EnableAngularLowerLimit.setter
    def EnableAngularLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableAngularLowerLimit
         Returns the angular lower limit option.  
           If the enable is true, then this joint will be
                    applied the lower limit in angular direction.   
         
        """
        pass
    @property
    def EnableAngularUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableAngularUpperLimit
         Returns the angular upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in angular direction.   
         
        """
        pass
    @EnableAngularUpperLimit.setter
    def EnableAngularUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableAngularUpperLimit
         Returns the angular upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in angular direction.   
         
        """
        pass
    @property
    def EnableLinearLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLinearLowerLimit
         Returns the linear lower limit option.  
          If the enable is true, then this joint will be
                    applied the lower limit in linear direction.   
         
        """
        pass
    @EnableLinearLowerLimit.setter
    def EnableLinearLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLinearLowerLimit
         Returns the linear lower limit option.  
          If the enable is true, then this joint will be
                    applied the lower limit in linear direction.   
         
        """
        pass
    @property
    def EnableLinearUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLinearUpperLimit
         Returns the linear upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in linear direction.   
         
        """
        pass
    @EnableLinearUpperLimit.setter
    def EnableLinearUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLinearUpperLimit
         Returns the linear upper limit option.  
           If the enable is true, then this joint will be
                    applied the upper limit in linear direction.   
         
        """
        pass
    @property
    def LinearLowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearLowerLimit
         Returns the linear lower limit.  
           The lower limit setup for joint linear movement.   
         
        """
        pass
    @property
    def LinearUpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearUpperLimit
         Returns the linear upper limit.  
           The upper limit setup for joint linear movement.   
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset value.  
             
         
        """
        pass
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartAngle
         Returns the start angle.  
             
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class CylindricalJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Cylindrical Joint objects. """
    @overload
    def CreateCylindricalJointBuilder(part: NXOpen.Part, cylindricalJoint: CylindricalJoint) -> CylindricalJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.CylindricalJointBuilder. 
         Returns builder ( CylindricalJointBuilder NXOpen.Anim): .
        """
        pass
    @overload
    def CreateCylindricalJointBuilder(part: NXOpen.Part, cylindricalJoint: CylindricalJoint, partOcc: NXOpen.Assemblies.Component) -> CylindricalJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.CylindricalJointBuilder. 
         Returns builder ( CylindricalJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> CylindricalJoint:
        """
         Finds the  NXOpen.AnimationDesigner.CylindricalJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns cylindricalJoint ( CylindricalJoint NXOpen.Anim):   NXOpen.AnimationDesigner.CylindricalJoint  with this name. .
        """
        pass
class CylindricalJoint(PhysicsJoint): 
    """ Represents a Cylindrical Joint feature. """
    pass
import NXOpen
class ExportTraceBuilder(NXOpen.Builder): 
    """ Represents a builder to export a trace from NXOpen.AnimationDesigner.Tracer. """
    @property
    def EulerAngleConvention(self) -> Convention:
        """
        Getter for property: ( Convention NXOpen.Anim) EulerAngleConvention
         Returns    the Euler angle convention.  
            
            
         
        """
        pass
    @EulerAngleConvention.setter
    def EulerAngleConvention(self, type: Convention):
        """
        Setter for property: ( Convention NXOpen.Anim) EulerAngleConvention
         Returns    the Euler angle convention.  
            
            
         
        """
        pass
    @property
    def ExportFile(self) -> str:
        """
        Getter for property: (str) ExportFile
         Returns    the export file name  
          
          
            
         
        """
        pass
    @ExportFile.setter
    def ExportFile(self, exportFile: str):
        """
        Setter for property: (str) ExportFile
         Returns    the export file name  
          
          
            
         
        """
        pass
import NXOpen
class FixedJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.FixedJointBuilder. """
    @property
    def FeedbackPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FeedbackPoint
         Returns the position of visual feedback point.  
             
         
        """
        pass
    @FeedbackPoint.setter
    def FeedbackPoint(self, feedback: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FeedbackPoint
         Returns the position of visual feedback point.  
             
         
        """
        pass
import NXOpen
class FixedJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Fixed Joint objects. """
    def CreateFixedJointBuilder(part: NXOpen.Part, fixedJoint: FixedJoint) -> FixedJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.FixedJointBuilder. 
         Returns builder ( FixedJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> FixedJoint:
        """
         Finds the  NXOpen.AnimationDesigner.FixedJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns fixedJoint ( FixedJoint NXOpen.Anim):   NXOpen.AnimationDesigner.FixedJoint  with this name. .
        """
        pass
class FixedJoint(PhysicsJoint): 
    """ Represents a Fixed Joint feature. """
    pass
import NXOpen
class FlexibleCableAttachmentBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[FlexibleCableAttachmentBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: FlexibleCableAttachmentBuilder) -> None:
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
    def Erase(self, obj: FlexibleCableAttachmentBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: FlexibleCableAttachmentBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: FlexibleCableAttachmentBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> FlexibleCableAttachmentBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( FlexibleCableAttachmentBuilder NXOpen.Anim):  object found at input index .
        """
        pass
    def GetContents(self) -> List[FlexibleCableAttachmentBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( FlexibleCableAttachmentBuilder List[NXOpen.An):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: FlexibleCableAttachmentBuilder) -> None:
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
    def SetContents(self, objects: List[FlexibleCableAttachmentBuilder]) -> None:
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
    def Swap(self, object1: FlexibleCableAttachmentBuilder, object2: FlexibleCableAttachmentBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
class FlexibleCableAttachmentBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder. """
    class AttachmentTypes(Enum):
        """
        Members Include: 
         |Fixed|  The fixed attachment 
         |Rotating|  The rotating attachment 
         |RotatingSliding|  The rotating and sliding attachment 
         |RetractSystemType1|  The retract system type1 attachment 
         |RetractSystemType2|  The retract system type2 attachment 
         |RetractSystemType3|  The retract system type3 attachment 

        """
        Fixed: int
        Rotating: int
        RotatingSliding: int
        RetractSystemType1: int
        RetractSystemType2: int
        RetractSystemType3: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableAttachmentBuilder.AttachmentTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RotationAxes(Enum):
        """
        Members Include: 
         |X|  The X axis 
         |Y|  The Y axis 
         |Z|  The Z axis 
         |All|  All axes 
         |NotSet|  No axis 

        """
        X: int
        Y: int
        Z: int
        All: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableAttachmentBuilder.RotationAxes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Attachment(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Attachment
         Returns   the atttachment.  
            
           
         
        """
        pass
    @property
    def AttachmentFrame(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) AttachmentFrame
         Returns   the attachment frame.  
            
           
         
        """
        pass
    @AttachmentFrame.setter
    def AttachmentFrame(self, attachmentFrame: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) AttachmentFrame
         Returns   the attachment frame.  
            
           
         
        """
        pass
    @property
    def AttachmentType(self) -> FlexibleCableAttachmentBuilder.AttachmentTypes:
        """
        Getter for property: ( FlexibleCableAttachmentBuilder.AttachmentTypes NXOpen.Anim) AttachmentType
         Returns   the attachment type.  
            
           
         
        """
        pass
    @AttachmentType.setter
    def AttachmentType(self, attachmentType: FlexibleCableAttachmentBuilder.AttachmentTypes):
        """
        Setter for property: ( FlexibleCableAttachmentBuilder.AttachmentTypes NXOpen.Anim) AttachmentType
         Returns   the attachment type.  
            
           
         
        """
        pass
    @property
    def DistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromStart
         Returns   the distance along cable between the attachment point and the cable start point.  
            
           
         
        """
        pass
    @property
    def MaxRetractedLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxRetractedLength
         Returns   the maximum length of cable that can be retracted.  
            
           
         
        """
        pass
    @property
    def MinRetractedLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinRetractedLength
         Returns   the minimum length of cable that can be retracted.  
            
           
         
        """
        pass
    @property
    def RotationAxis(self) -> FlexibleCableAttachmentBuilder.RotationAxes:
        """
        Getter for property: ( FlexibleCableAttachmentBuilder.RotationAxes NXOpen.Anim) RotationAxis
         Returns   the attachment rotation axis.  
            
           
         
        """
        pass
    @RotationAxis.setter
    def RotationAxis(self, rotationAxis: FlexibleCableAttachmentBuilder.RotationAxes):
        """
        Setter for property: ( FlexibleCableAttachmentBuilder.RotationAxes NXOpen.Anim) RotationAxis
         Returns   the attachment rotation axis.  
            
           
         
        """
        pass
    @property
    def SecondaryAttachmentFrame(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) SecondaryAttachmentFrame
         Returns   the secondary attachment frame.  
            
           
         
        """
        pass
    @SecondaryAttachmentFrame.setter
    def SecondaryAttachmentFrame(self, secondaryAttachmentFrame: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) SecondaryAttachmentFrame
         Returns   the secondary attachment frame.  
            
           
         
        """
        pass
    @property
    def SecondaryDistanceFromStart(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SecondaryDistanceFromStart
         Returns   the distance along cable between the secondary attachment point and the cable start point.  
            
           
         
        """
        pass
    @property
    def SpringConstant(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) SpringConstant
         Returns   the physical constant that determines how hard or easy it is to move the attachment when retracting or extending the cable.  
            
           
         
        """
        pass
import NXOpen
class FlexibleCableBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.FlexibleCableBuilder. """
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the flexible cable 
         |NoColor|  Assigns no color to the flexible cable 

        """
        SpecifyColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GeometryTypes(Enum):
        """
        Members Include: 
         |Curve|  Use the curves to create 
         |Body|  Use the body to create 
         |Parameter|  Use the parameters to create 

        """
        Curve: int
        Body: int
        Parameter: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.GeometryTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SectionTypes(Enum):
        """
        Members Include: 
         |Circle|  Circle Section 
         |Rectangle|  Rectangle Section 

        """
        Circle: int
        Rectangle: int
        @staticmethod
        def ValueOf(value: int) -> FlexibleCableBuilder.SectionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttachmentList(self) -> FlexibleCableAttachmentBuilderList:
        """
        Getter for property: ( FlexibleCableAttachmentBuilderList NXOpen.Anim) AttachmentList
         Returns   the list containing the defined attachments.  
            
           
         
        """
        pass
    @property
    def AttachmentsReversed(self) -> bool:
        """
        Getter for property: (bool) AttachmentsReversed
         Returns   the attachments reversed flag.  
            
           
         
        """
        pass
    @AttachmentsReversed.setter
    def AttachmentsReversed(self, attachmentsReversed: bool):
        """
        Setter for property: (bool) AttachmentsReversed
         Returns   the attachments reversed flag.  
            
           
         
        """
        pass
    @property
    def Body(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Body
         Returns   the body.  
            
           
         
        """
        pass
    @property
    def Collisions(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Collisions
         Returns   the collision bodies.  
            
           
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> FlexibleCableBuilder.ColorOptions:
        """
        Getter for property: ( FlexibleCableBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: FlexibleCableBuilder.ColorOptions):
        """
        Setter for property: ( FlexibleCableBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @property
    def Curves(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Curves
         Returns   the curves.  
            
           
         
        """
        pass
    @property
    def Diameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Diameter
         Returns   the diameter for circle section type.  
            
           
         
        """
        pass
    @property
    def GeometryType(self) -> FlexibleCableBuilder.GeometryTypes:
        """
        Getter for property: ( FlexibleCableBuilder.GeometryTypes NXOpen.Anim) GeometryType
         Returns   the geometry type.  
            
           
         
        """
        pass
    @GeometryType.setter
    def GeometryType(self, geometryType: FlexibleCableBuilder.GeometryTypes):
        """
        Setter for property: ( FlexibleCableBuilder.GeometryTypes NXOpen.Anim) GeometryType
         Returns   the geometry type.  
            
           
         
        """
        pass
    @property
    def Length(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Length
         Returns   the length.  
            
           
         
        """
        pass
    @property
    def Material(self) -> FlexibleMaterial:
        """
        Getter for property: ( FlexibleMaterial NXOpen.Anim) Material
         Returns   the material.  
           This can be a  NXOpen::AnimationDesigner::FlexibleMaterial .  
           
         
        """
        pass
    @Material.setter
    def Material(self, material: FlexibleMaterial):
        """
        Setter for property: ( FlexibleMaterial NXOpen.Anim) Material
         Returns   the material.  
           This can be a  NXOpen::AnimationDesigner::FlexibleMaterial .  
           
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
    @property
    def SectionType(self) -> FlexibleCableBuilder.SectionTypes:
        """
        Getter for property: ( FlexibleCableBuilder.SectionTypes NXOpen.Anim) SectionType
         Returns   the section type.  
            
           
         
        """
        pass
    @SectionType.setter
    def SectionType(self, sectionType: FlexibleCableBuilder.SectionTypes):
        """
        Setter for property: ( FlexibleCableBuilder.SectionTypes NXOpen.Anim) SectionType
         Returns   the section type.  
            
           
         
        """
        pass
    @property
    def Thickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Thickness
         Returns   the thickness for rectangle section type.  
            
           
         
        """
        pass
    @property
    def Width(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Width
         Returns   the width for rectangle section type.  
            
           
         
        """
        pass
    def UpdateAttachmentData(self, curveOrBodyUpdated: bool) -> None:
        """
         Updates all attachment data if the curves or body are changed. 
        """
        pass
    def UpdatePreviewedCableFacet(self, points: List[NXOpen.Point3d], widthDirections: List[NXOpen.Vector3d], radius: float, width: float, thickness: float) -> None:
        """
         Updates the previewed cable facet body. 
        """
        pass
import NXOpen
class FlexibleCableCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Flexible Cable object. """
    def CreateFlexibleCableAttachmentBuilder(part: NXOpen.Part) -> FlexibleCableAttachmentBuilder:
        """
         Creates a NXOpen.AnimationDesigner.FlexibleCableAttachmentBuilder. 
         Returns builder ( FlexibleCableAttachmentBuilder NXOpen.Anim): .
        """
        pass
    def CreateFlexibleCableBuilder(part: NXOpen.Part, cable: FlexibleCable) -> FlexibleCableBuilder:
        """
         Creates a NXOpen.AnimationDesigner.FlexibleCableBuilder. 
         Returns builder ( FlexibleCableBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> FlexibleCable:
        """
         Finds the  NXOpen.AnimationDesigner.FlexibleCable  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns cable ( FlexibleCable NXOpen.Anim):   NXOpen.AnimationDesigner.FlexibleCable  with this name. .
        """
        pass
import NXOpen
class FlexibleCable(NXOpen.DisplayableObject): 
    """ Represents a Flexible Cable feature. """
    pass
import NXOpen
class FlexibleMaterialBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.FlexibleMaterialBuilder. """
    @property
    def Density(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Density
         Returns   the density.  
            
           
         
        """
        pass
    @property
    def EnableMaxContactForce(self) -> bool:
        """
        Getter for property: (bool) EnableMaxContactForce
         Returns   the option determines whether to set the maximum contact force.  
            
           
         
        """
        pass
    @EnableMaxContactForce.setter
    def EnableMaxContactForce(self, enableMaxContactForce: bool):
        """
        Setter for property: (bool) EnableMaxContactForce
         Returns   the option determines whether to set the maximum contact force.  
            
           
         
        """
        pass
    @property
    def EnableMaxTwist(self) -> bool:
        """
        Getter for property: (bool) EnableMaxTwist
         Returns   the option determines whether to set the maximum twist.  
            
           
         
        """
        pass
    @EnableMaxTwist.setter
    def EnableMaxTwist(self, enableMaxTwist: bool):
        """
        Setter for property: (bool) EnableMaxTwist
         Returns   the option determines whether to set the maximum twist.  
            
           
         
        """
        pass
    @property
    def EnableMinCurvature(self) -> bool:
        """
        Getter for property: (bool) EnableMinCurvature
         Returns   the option determines whether to set the minimum curvature.  
            
           
         
        """
        pass
    @EnableMinCurvature.setter
    def EnableMinCurvature(self, enableMinCurvature: bool):
        """
        Setter for property: (bool) EnableMinCurvature
         Returns   the option determines whether to set the minimum curvature.  
            
           
         
        """
        pass
    @property
    def FulcrumLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FulcrumLength
         Returns   the fulcrum length.  
            
           
         
        """
        pass
    @property
    def MaxContactForce(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxContactForce
         Returns   the maximum contact force.  
            
           
         
        """
        pass
    @property
    def MaxTension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxTension
         Returns   the maximum tension.  
            
           
         
        """
        pass
    @property
    def MaxTwist(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxTwist
         Returns   the maximum twist.  
            
           
         
        """
        pass
    @property
    def MinCurvature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinCurvature
         Returns   the minimum curvature.  
            
           
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns   the name.  
            
           
         
        """
        pass
    @property
    def Oscillation(self) -> float:
        """
        Getter for property: (float) Oscillation
         Returns   the oscillation.  
            
           
         
        """
        pass
    @Oscillation.setter
    def Oscillation(self, oscillation: float):
        """
        Setter for property: (float) Oscillation
         Returns   the oscillation.  
            
           
         
        """
        pass
    @property
    def YoungModulus(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YoungModulus
         Returns   the Young's modulus.  
            
           
         
        """
        pass
import NXOpen
class FlexibleMaterialCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Flexible Material object. """
    def CreateFlexibleMaterialBuilder(part: NXOpen.Part, material: FlexibleMaterial) -> FlexibleMaterialBuilder:
        """
         Creates a NXOpen.AnimationDesigner.FlexibleMaterialBuilder. 
         Returns builder ( FlexibleMaterialBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> FlexibleMaterial:
        """
         Finds the  NXOpen.AnimationDesigner.FlexibleMaterial  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns material ( FlexibleMaterial NXOpen.Anim):   NXOpen.AnimationDesigner.FlexibleMaterial  with this name. .
        """
        pass
import NXOpen
class FlexibleMaterial(NXOpen.DisplayableObject): 
    """ Represents a Flexible Material feature. """
    pass
import NXOpen
class GearBuilder(CouplerBuilder): 
    """ Represents a NXOpen.AnimationDesigner.GearBuilder. """
    class GearType(Enum):
        """
        Members Include: 
         |General| general gear
         |Chainbelt| chain belt
         |Cable| cable

        """
        General: int
        Chainbelt: int
        Cable: int
        @staticmethod
        def ValueOf(value: int) -> GearBuilder.GearType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ChangeDirection(self) -> bool:
        """
        Getter for property: (bool) ChangeDirection
         Returns the inner gear option.  
             
         
        """
        pass
    @ChangeDirection.setter
    def ChangeDirection(self, change: bool):
        """
        Setter for property: (bool) ChangeDirection
         Returns the inner gear option.  
             
         
        """
        pass
    @property
    def ExpressionRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpressionRatio
         Returns the ratio expression.  
             
         
        """
        pass
    @property
    def UseType(self) -> GearBuilder.GearType:
        """
        Getter for property: ( GearBuilder.GearType NXOpen.Anim) UseType
         Returns the gear type.  
            
         
        """
        pass
    @UseType.setter
    def UseType(self, useType: GearBuilder.GearType):
        """
        Setter for property: ( GearBuilder.GearType NXOpen.Anim) UseType
         Returns the gear type.  
            
         
        """
        pass
import NXOpen
class GearCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Gear objects. """
    def CreateGearBuilder(part: NXOpen.Part, gear: Gear) -> GearBuilder:
        """
         Creates a NXOpen.AnimationDesigner.GearBuilder. 
         Returns builder ( GearBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> Gear:
        """
         Finds the  NXOpen.AnimationDesigner.Gear  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns gear ( Gear NXOpen.Anim):   NXOpen.AnimationDesigner.Gear  with this name. .
        """
        pass
class Gear(Coupler): 
    """ Represents a Gear feature. """
    pass
import NXOpen
import NXOpen.Mechatronics
class InverseKinematicsBuilder(NXOpen.Builder): 
    """ Represents a AnimationDesigner.InverseKinematicsBuilder """
    class AlignTypes(Enum):
        """
        Members Include: 
         |All|  align aLL vector.
         |Z|  align z vector.
         |Y|  align y vector.
         |X|  align x vector.
         |NotSet|  no vector alignment.

        """
        All: int
        Z: int
        Y: int
        X: int
        NotSet: int
        @staticmethod
        def ValueOf(value: int) -> InverseKinematicsBuilder.AlignTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BodyTypes(Enum):
        """
        Members Include: 
         |OneBody|  one kinematics chain.
         |TwoBodies|  two kinematics chain.

        """
        OneBody: int
        TwoBodies: int
        @staticmethod
        def ValueOf(value: int) -> InverseKinematicsBuilder.BodyTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Result(Enum):
        """
        Members Include: 
         |Success|  Successfully solved. 
         |NotSolved|  Could not solve due to error. 
         |Approximate|  The target is not reachable, closest solution is returned. 
         |Limits|  The target is not reachable due to limits, closest solution is returned. 
         |ReachError|  A reach error occurs. 
         |Timeout|  A timeout error occurs due to collision avoidance. 
         |CollisionTarget|  The target pose is colliding. 
         |CollisionStart|  The start pose is colliding. 
         |Limit|  Cannot move toward the target due to limits. 
         |TargetEqualsStart|  It is not possible to go closer to the target due to the kinematics. 
         |Unknown|  An unknown error occurs in the inverse kinematics solver. 

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
        @staticmethod
        def ValueOf(value: int) -> InverseKinematicsBuilder.Result:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AlignType(self) -> InverseKinematicsBuilder.AlignTypes:
        """
        Getter for property: ( InverseKinematicsBuilder.AlignTypes NXOpen.Anim) AlignType
         Returns the option of align type for two bodies type.  
             
         
        """
        pass
    @AlignType.setter
    def AlignType(self, alignType: InverseKinematicsBuilder.AlignTypes):
        """
        Setter for property: ( InverseKinematicsBuilder.AlignTypes NXOpen.Anim) AlignType
         Returns the option of align type for two bodies type.  
             
         
        """
        pass
    @property
    def AvoidCollision(self) -> bool:
        """
        Getter for property: (bool) AvoidCollision
         Returns the option of avoiding collision.  
             
         
        """
        pass
    @AvoidCollision.setter
    def AvoidCollision(self, avoidCollision: bool):
        """
        Setter for property: (bool) AvoidCollision
         Returns the option of avoiding collision.  
             
         
        """
        pass
    @property
    def BodyType(self) -> InverseKinematicsBuilder.BodyTypes:
        """
        Getter for property: ( InverseKinematicsBuilder.BodyTypes NXOpen.Anim) BodyType
         Returns the type   
            
         
        """
        pass
    @BodyType.setter
    def BodyType(self, type: InverseKinematicsBuilder.BodyTypes):
        """
        Setter for property: ( InverseKinematicsBuilder.BodyTypes NXOpen.Anim) BodyType
         Returns the type   
            
         
        """
        pass
    @property
    def EulerAngleConvention(self) -> NXOpen.Mechatronics.Convention:
        """
        Getter for property: ( NXOpen.Mechatronics.Convention) EulerAngleConvention
         Returns the Euler angle convention.  
             
         
        """
        pass
    @EulerAngleConvention.setter
    def EulerAngleConvention(self, type: NXOpen.Mechatronics.Convention):
        """
        Setter for property: ( NXOpen.Mechatronics.Convention) EulerAngleConvention
         Returns the Euler angle convention.  
             
         
        """
        pass
    @property
    def FirstPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FirstPoint
         Returns the first point for two bodies type.  
             
         
        """
        pass
    @FirstPoint.setter
    def FirstPoint(self, firstPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FirstPoint
         Returns the first point for two bodies type.  
             
         
        """
        pass
    @property
    def FirstRigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) FirstRigidGroup
         Returns the first rigid group for two bodies type.  
             
         
        """
        pass
    @property
    def FrameList(self) -> NXOpen.Mechatronics.FrameBuilderList:
        """
        Getter for property: ( NXOpen.Mechatronics.FrameBuilderList) FrameList
         Returns the list containing the defined frames.  
             
         
        """
        pass
    @property
    def GenerateTracer(self) -> bool:
        """
        Getter for property: (bool) GenerateTracer
         Returns the option of generating tracer object.  
             
         
        """
        pass
    @GenerateTracer.setter
    def GenerateTracer(self, bTracer: bool):
        """
        Setter for property: (bool) GenerateTracer
         Returns the option of generating tracer object.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def PointTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PointTolerance
         Returns the tolerance of point alignment for two bodies type  
            
         
        """
        pass
    @property
    def RigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) RigidGroup
         Returns the rigid group.  
             
         
        """
        pass
    @property
    def SecondPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SecondPoint
         Returns the second point for two bodies type.  
             
         
        """
        pass
    @SecondPoint.setter
    def SecondPoint(self, secondPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SecondPoint
         Returns the second point for two bodies type.  
             
         
        """
        pass
    @property
    def SecondRigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SecondRigidGroup
         Returns the second rigid group for two bodies type.  
             
         
        """
        pass
    @property
    def StartPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPoint
         Returns the start point.  
             
         
        """
        pass
    @StartPoint.setter
    def StartPoint(self, startPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPoint
         Returns the start point.  
             
         
        """
        pass
    @property
    def TargetPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TargetPoint
         Returns the target point.  
             
         
        """
        pass
    @TargetPoint.setter
    def TargetPoint(self, targetPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TargetPoint
         Returns the target point.  
             
         
        """
        pass
    @property
    def VectorTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VectorTolerance
         Returns the tolerance of vector alignment for two bodies type.  
             
         
        """
        pass
    def GetErrorPose(self) -> NXOpen.CoordinateSystem:
        """
         Returns the pose that encounters error. 
         Returns pose ( NXOpen.CoordinateSystem): .
        """
        pass
    def GetFirstPointOrientation(self) -> NXOpen.Matrix3x3:
        """
         Gets the first point orientations for two bodies type. 
         Returns startOrit ( NXOpen.Matrix3x3):  The first orientation matrix. .
        """
        pass
    def GetOrientation(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Matrix3x3]:
        """
         Gets the orientations. 
         Returns A tuple consisting of (startOrit, targetOrit). 
         - startOrit is:  NXOpen.Matrix3x3. The start orientation matrix. .
         - targetOrit is:  NXOpen.Matrix3x3. The target orientation matrix. .

        """
        pass
    def GetResult(self) -> InverseKinematicsBuilder.Result:
        """
         Returns the solver result. 
         Returns result ( InverseKinematicsBuilder.Result NXOpen.Anim):  The result of the inverse kinematics solver .
        """
        pass
    def GetSecondPointOrientation(self) -> NXOpen.Matrix3x3:
        """
         Gets the second point orientations for two bodies type. 
         Returns startOrit ( NXOpen.Matrix3x3):  The second orientation matrix. .
        """
        pass
    def GetStartPointOrientation(self) -> NXOpen.Matrix3x3:
        """
         Gets the start point orientations. 
         Returns startOrit ( NXOpen.Matrix3x3):  The start orientation matrix. .
        """
        pass
    def SetFirstPointOrientation(self, startOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the first point orientations for two bodies type. 
        """
        pass
    def SetOrientation(self, startOrit: NXOpen.Matrix3x3, targetOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the orientations. 
        """
        pass
    def SetSecondPointOrientation(self, startOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the second point orientations for two bodies type. 
        """
        pass
    def SetStartPointOrientation(self, startOrit: NXOpen.Matrix3x3) -> None:
        """
         Sets the start point orientations. 
        """
        pass
    def UpdateIk(self) -> None:
        """
         Update IK object. 
        """
        pass
    def UpdateIkStatus(self) -> None:
        """
         Update IK status to out of date. 
        """
        pass
import NXOpen
class InverseKinematicsCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Inverse Kinematics. """
    def CreateInverseKinematicsBuilder(part: NXOpen.Part, inverseKinematics: InverseKinematics) -> InverseKinematicsBuilder:
        """
         Creates a NXOpen.AnimationDesigner.InverseKinematicsBuilder. 
         Returns builder ( InverseKinematicsBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> InverseKinematics:
        """
         Finds the  NXOpen.AnimationDesigner.InverseKinematics  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns inverseKinematics ( InverseKinematics NXOpen.Anim):   NXOpen.AnimationDesigner.InverseKinematics  with this name. .
        """
        pass
import NXOpen
class InverseKinematics(NXOpen.DisplayableObject): 
    """ Represents the Inverse Kinematics class. It defines the configuration of inverse kinematics in a mechanism. """
    pass
import NXOpen
class JointJoggerBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.JointJoggerBuilder. """
    @property
    def CaptureArrangement(self) -> bool:
        """
        Getter for property: (bool) CaptureArrangement
         Returns the capture arrangement option.  
             
         
        """
        pass
    @CaptureArrangement.setter
    def CaptureArrangement(self, captureArrangement: bool):
        """
        Setter for property: (bool) CaptureArrangement
         Returns the capture arrangement option.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    def AddJointData(self, joint: NXOpen.NXObject) -> None:
        """
         Adds the joint data. 
        """
        pass
    def EditJointAngle(self, joint: NXOpen.NXObject, angleValue: float) -> None:
        """
         Edits the joint angle. 
        """
        pass
    def EditJointDistance(self, joint: NXOpen.NXObject, distanceValue: float) -> None:
        """
         Edits the joint distance. 
        """
        pass
    def RemoveJointData(self, joint: NXOpen.NXObject) -> None:
        """
         Removes the joint data. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class JointJoggerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Joint Jogger objects. """
    @overload
    def CreateJointJoggerBuilder(part: NXOpen.Part, jointJogger: JointJogger) -> JointJoggerBuilder:
        """
         Creates a NXOpen.AnimationDesigner.JointJoggerBuilder. 
         Returns builder ( JointJoggerBuilder NXOpen.Anim): .
        """
        pass
    @overload
    def CreateJointJoggerBuilder(part: NXOpen.Part, jointJogger: JointJogger, partOcc: NXOpen.Assemblies.Component) -> JointJoggerBuilder:
        """
         Creates a NXOpen.AnimationDesigner.JointJoggerBuilder. 
         Returns builder ( JointJoggerBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> JointJogger:
        """
         Finds the  NXOpen.AnimationDesigner.JointJogger  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns jointJogger ( JointJogger NXOpen.Anim):   NXOpen.AnimationDesigner.JointJogger  with this name. .
        """
        pass
import NXOpen
class JointJogger(NXOpen.DisplayableObject): 
    """ Represents a Joint Jogger feature. """
    pass
import NXOpen
class MeasureBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.MeasureBuilder. """
    class MeasureTypes(Enum):
        """
        Members Include: 
         |Distance| 
         |Angle| 
         |MotorParameter| 

        """
        Distance: int
        Angle: int
        MotorParameter: int
        @staticmethod
        def ValueOf(value: int) -> MeasureBuilder.MeasureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MotorParameterTypes(Enum):
        """
        Members Include: 
         |Displacement| 
         |Velocity| 
         |Acceleration| 

        """
        Displacement: int
        Velocity: int
        Acceleration: int
        @staticmethod
        def ValueOf(value: int) -> MeasureBuilder.MotorParameterTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Direction1(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Direction1
         Returns the first direction used to measure the angle with the second direction.  
             
         
        """
        pass
    @Direction1.setter
    def Direction1(self, direction1: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Direction1
         Returns the first direction used to measure the angle with the second direction.  
             
         
        """
        pass
    @property
    def Direction2(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Direction2
         Returns the second direction used to measure the angle with the first direction.  
             
         
        """
        pass
    @Direction2.setter
    def Direction2(self, direction2: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Direction2
         Returns the second direction used to measure the angle with the first direction.  
             
         
        """
        pass
    @property
    def List1(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) List1
         Returns the first object list used to be measured with the second object list.  
             
         
        """
        pass
    @property
    def List2(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) List2
         Returns the second object list used to be measured with the first object list.  
             
         
        """
        pass
    @property
    def MeasureType(self) -> MeasureBuilder.MeasureTypes:
        """
        Getter for property: ( MeasureBuilder.MeasureTypes NXOpen.Anim) MeasureType
         Returns the measure type.  
             
         
        """
        pass
    @MeasureType.setter
    def MeasureType(self, measureType: MeasureBuilder.MeasureTypes):
        """
        Setter for property: ( MeasureBuilder.MeasureTypes NXOpen.Anim) MeasureType
         Returns the measure type.  
             
         
        """
        pass
    @property
    def Motor(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Motor
         Returns the motor.  
           This can be a  NXOpen::AnimationDesigner::SpeedMotor 
                    or  NXOpen::AnimationDesigner::PositionMotor .   
         
        """
        pass
    @property
    def MotorParameterType(self) -> MeasureBuilder.MotorParameterTypes:
        """
        Getter for property: ( MeasureBuilder.MotorParameterTypes NXOpen.Anim) MotorParameterType
         Returns the motor parameter type.  
             
         
        """
        pass
    @MotorParameterType.setter
    def MotorParameterType(self, motorParameterType: MeasureBuilder.MotorParameterTypes):
        """
        Setter for property: ( MeasureBuilder.MotorParameterTypes NXOpen.Anim) MotorParameterType
         Returns the motor parameter type.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def UseVector(self) -> bool:
        """
        Getter for property: (bool) UseVector
         Returns the use vector flag.  
             
         
        """
        pass
    @UseVector.setter
    def UseVector(self, useVector: bool):
        """
        Setter for property: (bool) UseVector
         Returns the use vector flag.  
             
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the vector.  
             
         
        """
        pass
    @Vector.setter
    def Vector(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the vector.  
             
         
        """
        pass
import NXOpen
class MeasureCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Measure objects. """
    def CreateMeasureBuilder(part: NXOpen.Part, measure: Measure) -> MeasureBuilder:
        """
         Creates a NXOpen.AnimationDesigner.MeasureBuilder. 
         Returns builder ( MeasureBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> Measure:
        """
         Finds the  NXOpen.AnimationDesigner.Measure  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns measure ( Measure NXOpen.Anim):   NXOpen.AnimationDesigner.Measure  with this name. .
        """
        pass
import NXOpen
class Measure(NXOpen.DisplayableObject): 
    """ Represents a Measure feature. """
    pass
import NXOpen
class MechanicalCamBuilder(NXOpen.Builder): 
    """
    Represents a NXOpen.AnimationDesigner.MechanicalCamBuilder.
    """
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the mechanical cam 
         |NoColor|  Assigns no color to the mechanical cam 

        """
        SpecifyColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> MechanicalCamBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> MechanicalCamBuilder.ColorOptions:
        """
        Getter for property: ( MechanicalCamBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: MechanicalCamBuilder.ColorOptions):
        """
        Setter for property: ( MechanicalCamBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @property
    def FollowerAxis(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) FollowerAxis
         Returns the follower axis joint.  
           This can be a  NXOpen::AnimationDesigner::RevoluteJoint  or  NXOpen::AnimationDesigner::SliderJoint    
         
        """
        pass
    @property
    def FollowerFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) FollowerFaces
         Returns the follower faces.  
           This can be a  NXOpen::Face .   
         
        """
        pass
    @property
    def MasterAxis(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) MasterAxis
         Returns the master axis joint.  
           This can be a  NXOpen::AnimationDesigner::RevoluteJoint  or  NXOpen::AnimationDesigner::SliderJoint    
         
        """
        pass
    @property
    def MasterFaces(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) MasterFaces
         Returns the master faces.  
           This can be a  NXOpen::Face .   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
import NXOpen
class MechanicalCamCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Mechanical Cam objects. """
    def CreateMechanicalCamBuilder(part: NXOpen.Part, mechanicalCam: MechanicalCam) -> MechanicalCamBuilder:
        """
         Creates a NXOpen.AnimationDesigner.MechanicalCamBuilder. 
         Returns builder ( MechanicalCamBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> MechanicalCam:
        """
         Finds the  NXOpen.AnimationDesigner.MechanicalCam  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns obj ( MechanicalCam NXOpen.Anim):   NXOpen.AnimationDesigner.MechanicalCam  with this name. .
        """
        pass
import NXOpen
class MechanicalCam(NXOpen.DisplayableObject): 
    """ Represents a Mechanical Cam feature."""
    pass
import NXOpen
class MotorBuilder(NXOpen.Builder): 
    """ Represents a base builder for Motor. """
    @property
    def AxisJoint(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) AxisJoint
         Returns the joint select.  
           This can be a  NXOpen::AnimationDesigner::RevoluteJoint .   
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
import NXOpen
class Motor(NXOpen.DisplayableObject): 
    """ Represents the Animation Designer motor class. """
    pass
import NXOpen
class PathConstraintFrameBuilderList(NXOpen.TaggedObject): 
    """ Represents a list of objects."""
    @property
    def Length(self) -> int:
        """
        Getter for property: (int) Length
         Returns the length of the list   
            
         
        """
        pass
    @overload
    def Append(self, objects: List[PathConstraintFrameBuilder]) -> None:
        """
         Appends a set of objects to the list
            
        """
        pass
    @overload
    def Append(self, objectValue: PathConstraintFrameBuilder) -> None:
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
    def Erase(self, obj: PathConstraintFrameBuilder) -> None:
        """
         Erases the object from the list, but does not delete the object.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    @overload
    def Erase(self, obj: PathConstraintFrameBuilder, delete_option: NXOpen.ObjectList.DeleteOption) -> None:
        """
         Erases the object from the list.
                The list is shifted so that there isn't a null where the object used to exist. 
        """
        pass
    def FindIndex(self, obj: PathConstraintFrameBuilder) -> int:
        """
         Finds the index where the input object appears.  If it does not appear,
               -1 is returned.
            
         Returns index (int):  index of input object, -1 if not on list .
        """
        pass
    def FindItem(self, index: int) -> PathConstraintFrameBuilder:
        """
         Returns the object at the input index.  May be NULL.
            
         Returns obj ( PathConstraintFrameBuilder NXOpen.Anim):  object found at input index .
        """
        pass
    def GetContents(self) -> List[PathConstraintFrameBuilder]:
        """
         Gets the contents of the entire list 
         Returns objects ( PathConstraintFrameBuilder List[NXOpen.An):  The list contents .
        """
        pass
    def Insert(self, location: int, objectValue: PathConstraintFrameBuilder) -> None:
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
    def SetContents(self, objects: List[PathConstraintFrameBuilder]) -> None:
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
    def Swap(self, object1: PathConstraintFrameBuilder, object2: PathConstraintFrameBuilder) -> None:
        """
         Exchanges the position of two objects inside the list.
                The first object is placed where the second used to be,
                and second object where the first used to be. 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PathConstraintFrameBuilder(NXOpen.TaggedObject): 
    """ Represents a frame that constrains the orientation along the path curve. """
    class CurveTypes(Enum):
        """
        Members Include: 
         |Line|  line 
         |Spline|  spline 

        """
        Line: int
        Spline: int
        @staticmethod
        def ValueOf(value: int) -> PathConstraintFrameBuilder.CurveTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AssociatedCurve(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) AssociatedCurve
         Returns the associated curve.  
             
         
        """
        pass
    @AssociatedCurve.setter
    def AssociatedCurve(self, curve: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) AssociatedCurve
         Returns the associated curve.  
             
         
        """
        pass
    @property
    def CurveType(self) -> PathConstraintFrameBuilder.CurveTypes:
        """
        Getter for property: ( PathConstraintFrameBuilder.CurveTypes NXOpen.Anim) CurveType
         Returns the curve type.  
             
         
        """
        pass
    @CurveType.setter
    def CurveType(self, curveType: PathConstraintFrameBuilder.CurveTypes):
        """
        Setter for property: ( PathConstraintFrameBuilder.CurveTypes NXOpen.Anim) CurveType
         Returns the curve type.  
             
         
        """
        pass
    @property
    def PathFrame(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) PathFrame
         Returns the path frame.  
             
         
        """
        pass
    @PathFrame.setter
    def PathFrame(self, pathFrame: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) PathFrame
         Returns the path frame.  
             
         
        """
        pass
    @property
    def PathParameter(self) -> float:
        """
        Getter for property: (float) PathParameter
         Returns the path parameter.  
             
         
        """
        pass
    @PathParameter.setter
    def PathParameter(self, pathParameter: float):
        """
        Setter for property: (float) PathParameter
         Returns the path parameter.  
             
         
        """
        pass
import NXOpen
class PathConstraintJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.PathConstraintJoint builder. """
    class PathTypes(Enum):
        """
        Members Include: 
         |FromCoordinateSystems|  from coordinate systems 
         |FromCurves|  from curves 

        """
        FromCoordinateSystems: int
        FromCurves: int
        @staticmethod
        def ValueOf(value: int) -> PathConstraintJointBuilder.PathTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector which is tangent to the path curve at the selected point   
            
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector which is tangent to the path curve at the selected point   
            
         
        """
        pass
    @property
    def FrameList(self) -> PathConstraintFrameBuilderList:
        """
        Getter for property: ( PathConstraintFrameBuilderList NXOpen.Anim) FrameList
         Returns the list containing the defined frames.  
             
         
        """
        pass
    @property
    def PathPreview(self) -> bool:
        """
        Getter for property: (bool) PathPreview
         Returns the path preview   
            
         
        """
        pass
    @PathPreview.setter
    def PathPreview(self, enable: bool):
        """
        Setter for property: (bool) PathPreview
         Returns the path preview   
            
         
        """
        pass
    @property
    def PathType(self) -> PathConstraintJointBuilder.PathTypes:
        """
        Getter for property: ( PathConstraintJointBuilder.PathTypes NXOpen.Anim) PathType
         Returns the path type.  
             
         
        """
        pass
    @PathType.setter
    def PathType(self, pathType: PathConstraintJointBuilder.PathTypes):
        """
        Setter for property: ( PathConstraintJointBuilder.PathTypes NXOpen.Anim) PathType
         Returns the path type.  
             
         
        """
        pass
    @property
    def PointOnCurve(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOnCurve
         Returns the selected point on curve   
            
         
        """
        pass
    @PointOnCurve.setter
    def PointOnCurve(self, pointOnCurve: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOnCurve
         Returns the selected point on curve   
            
         
        """
        pass
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluate the composited path with the curves. 
        """
        pass
    def GeneratePathCurves(self) -> None:
        """
         Generate the path curves from the coordinates systems. 
        """
        pass
    def GetPathCurves(self) -> List[NXOpen.NXObject]:
        """
         Get the path curves that constrain the movement of the attachment
         Returns pathCurves ( NXOpen.NXObject Li):  curve or edge.
        """
        pass
    def NewPathFrame(self) -> PathConstraintFrameBuilder:
        """
         Creates a NXOpen.AnimationDesigner.PathConstraintFrameBuilder object. 
         Returns pathFrameBuilder ( PathConstraintFrameBuilder NXOpen.Anim): .
        """
        pass
    def SetPathCurvesFromCurves(self, pathCurves: List[NXOpen.NXObject]) -> None:
        """
         Set the path curves that constrain the movement of the attachment
        """
        pass
import NXOpen
class PathConstraintJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Path Constraint Joint objects. """
    def CreatePathConstraintJointBuilder(part: NXOpen.Part, joint: PathConstraintJoint) -> PathConstraintJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.PathConstraintJointBuilder. 
         Returns builder ( PathConstraintJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> PathConstraintJoint:
        """
         Finds the  NXOpen.AnimationDesigner.PathConstraintJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns pathConstraintJoint ( PathConstraintJoint NXOpen.Anim):   NXOpen.AnimationDesigner.PathConstraintJoint  with this name. .
        """
        pass
class PathConstraintJoint(PhysicsJoint): 
    """ Represents a Path Constraint Joint feature. """
    pass
import NXOpen
class PhysicsJointBuilder(NXOpen.Builder): 
    """ Represents a base builder for Physics Joints. """
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the joint 
         |NoColor|  Assigns no color to the joint 

        """
        SpecifyColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> PhysicsJointBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MotionTypes(Enum):
        """
        Members Include: 
         |Dynamics|  dynamics type 
         |Kinematics|  kinematics type 

        """
        Dynamics: int
        Kinematics: int
        @staticmethod
        def ValueOf(value: int) -> PhysicsJointBuilder.MotionTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttachmentList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) AttachmentList
         Returns the attachment list for a Joint.  
           The list can consist of  NXOpen::AnimationDesigner::RigidGroup  
                objects or objects which can create a Rigid Group.   
         
        """
        pass
    @property
    def BaseList(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) BaseList
         Returns the base list for a Joint.  
           The list can consist of  NXOpen::AnimationDesigner::RigidGroup  
                objects or objects which can create a Rigid Group.   
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> PhysicsJointBuilder.ColorOptions:
        """
        Getter for property: ( PhysicsJointBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color options.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: PhysicsJointBuilder.ColorOptions):
        """
        Setter for property: ( PhysicsJointBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color options.  
             
         
        """
        pass
    @property
    def MotionType(self) -> PhysicsJointBuilder.MotionTypes:
        """
        Getter for property: ( PhysicsJointBuilder.MotionTypes NXOpen.Anim) MotionType
         Returns the motion type.  
             
         
        """
        pass
    @MotionType.setter
    def MotionType(self, motionType: PhysicsJointBuilder.MotionTypes):
        """
        Setter for property: ( PhysicsJointBuilder.MotionTypes NXOpen.Anim) MotionType
         Returns the motion type.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
import NXOpen
class PhysicsJoint(NXOpen.DisplayableObject): 
    """ Represents the Animation Designer joint class."""
    pass
import NXOpen
class PlanarJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.PlanarJointBuilder. """
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns    a value that specifies axis vector.  
            
            
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns    a value that specifies axis vector.  
            
            
         
        """
        pass
    @property
    def PointOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOrigin
         Returns    a value that indicates the origin point.  
            
            
         
        """
        pass
    @PointOrigin.setter
    def PointOrigin(self, origin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOrigin
         Returns    a value that indicates the origin point.  
            
            
         
        """
        pass
import NXOpen
class PlanarJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Planar Joint objects. """
    def CreatePlanarJointBuilder(part: NXOpen.Part, planarJoint: PlanarJoint) -> PlanarJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.PlanarJointBuilder. 
         Returns builder ( PlanarJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> PlanarJoint:
        """
         Finds the  NXOpen.AnimationDesigner.PlanarJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns planarJoint ( PlanarJoint NXOpen.Anim):   NXOpen.AnimationDesigner.PlanarJoint  with this name. .
        """
        pass
class PlanarJoint(PhysicsJoint): 
    """ Represents a Planar Joint feature. """
    pass
import NXOpen
class PointOnCurveJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.PointOnCurveJoint builder. """
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector which is tangent to the connected curve at the selected point.  
             
         
        """
        pass
    @property
    def OrientationVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) OrientationVector
         Returns the orientation vector for kinematics motion type.  
             
         
        """
        pass
    @OrientationVector.setter
    def OrientationVector(self, orientationVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) OrientationVector
         Returns the orientation vector for kinematics motion type.  
             
         
        """
        pass
    @property
    def PointOnCurve(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    @PointOnCurve.setter
    def PointOnCurve(self, pointOnCurve: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOnCurve
         Returns the selected point on curve.  
             
         
        """
        pass
    @property
    def UseOrientationVector(self) -> bool:
        """
        Getter for property: (bool) UseOrientationVector
         Returns the flag to use orientation vector or not for kinematics motion type.  
             
         
        """
        pass
    @UseOrientationVector.setter
    def UseOrientationVector(self, useOrientationVector: bool):
        """
        Setter for property: (bool) UseOrientationVector
         Returns the flag to use orientation vector or not for kinematics motion type.  
             
         
        """
        pass
    def EvaluatePath(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Evaluates the path. If there is no path, create it, otherwise evaluate it. 
        """
        pass
    def GetConnectedCurves(self) -> List[NXOpen.NXObject]:
        """
         Gets the connected curves which the attachment will move along. 
         Returns curves ( NXOpen.NXObject Li):  curve or edge .
        """
        pass
    def SetConnectedCurves(self, curves: List[NXOpen.NXObject]) -> None:
        """
         Sets the connected curves which the attachment will move along. 
        """
        pass
import NXOpen
class PointOnCurveJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Point On Curve Joint objects. """
    def CreatePointOnCurveJointBuilder(part: NXOpen.Part, joint: PointOnCurveJoint) -> PointOnCurveJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.PointOnCurveJointBuilder. 
         Returns builder ( PointOnCurveJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> PointOnCurveJoint:
        """
         Finds the  NXOpen.AnimationDesigner.PointOnCurveJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns pointOnCurveJoint ( PointOnCurveJoint NXOpen.Anim):   NXOpen.AnimationDesigner.PointOnCurveJoint  with this name. .
        """
        pass
class PointOnCurveJoint(PhysicsJoint): 
    """ Represents a Point On Curve Joint feature. """
    pass
import NXOpen
class PointOnCurveKinematicsChainBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder. """
    class ProjectionDirectionType(Enum):
        """
        Members Include: 
         |AlongCurveNormal|  Along Curve Normal 
         |AlongVector|  Along Vector  

        """
        AlongCurveNormal: int
        AlongVector: int
        @staticmethod
        def ValueOf(value: int) -> PointOnCurveKinematicsChainBuilder.ProjectionDirectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MasterRigidGroup(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) MasterRigidGroup
         Returns   the master rigid group selection.  
           This should be a  NXOpen::AnimationDesigner::RigidGroup .  
           
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns   the name  
          
          
           
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns   the name  
          
          
           
         
        """
        pass
    @property
    def ProjectionDirection(self) -> PointOnCurveKinematicsChainBuilder.ProjectionDirectionType:
        """
        Getter for property: ( PointOnCurveKinematicsChainBuilder.ProjectionDirectionType NXOpen.Anim) ProjectionDirection
         Returns   the projection direction type of the slave rigid center point.  
            
           
         
        """
        pass
    @ProjectionDirection.setter
    def ProjectionDirection(self, projectionDirection: PointOnCurveKinematicsChainBuilder.ProjectionDirectionType):
        """
        Setter for property: ( PointOnCurveKinematicsChainBuilder.ProjectionDirectionType NXOpen.Anim) ProjectionDirection
         Returns   the projection direction type of the slave rigid center point.  
            
           
         
        """
        pass
    @property
    def ProjectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ProjectionVector
         Returns   the projection vector when choosing ProjectionDirectionType_AlongVector.  
            
           
         
        """
        pass
    @ProjectionVector.setter
    def ProjectionVector(self, projectionVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ProjectionVector
         Returns   the projection vector when choosing ProjectionDirectionType_AlongVector.  
            
           
         
        """
        pass
    @property
    def SlaveRigidGroups(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SlaveRigidGroups
         Returns   the slave rigid groups selection.  
           This should be a  NXOpen::AnimationDesigner::RigidGroup .  
           
         
        """
        pass
import NXOpen
class PointOnCurveKinematicsChainCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Point On Curve Kinematics Chain objects. """
    def CreatePointOnCurveKinematicsChainBuilder(part: NXOpen.Part, objectValue: PointOnCurveKinematicsChain) -> PointOnCurveKinematicsChainBuilder:
        """
         Creates a NXOpen.AnimationDesigner.PointOnCurveKinematicsChainBuilder. 
         Returns builder ( PointOnCurveKinematicsChainBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> PointOnCurveKinematicsChain:
        """
         Finds the  NXOpen.AnimationDesigner.PointOnCurveKinematicsChain  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns objectTag ( PointOnCurveKinematicsChain NXOpen.Anim):   NXOpen.AnimationDesigner.PointOnCurveKinematicsChain  with this name. .
        """
        pass
import NXOpen
class PointOnCurveKinematicsChain(NXOpen.DisplayableObject): 
    """ Represents a Point On Curve Kinematics Chain feature. """
    pass
import NXOpen
class PositionMotorBuilder(MotorBuilder): 
    """ Represents a NXOpen.AnimationDesigner.PositionMotorBuilder. """
    class AutoCalculate(Enum):
        """
        Members Include: 
         |EndTime|  Auto calculate end time 
         |Speed|  Auto calculate speed 
         |Destination|  Auto calculate destination 

        """
        EndTime: int
        Speed: int
        Destination: int
        @staticmethod
        def ValueOf(value: int) -> PositionMotorBuilder.AutoCalculate:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Axis(Enum):
        """
        Members Include: 
         |Angular|  Angular 
         |Linear|  Linear 
         |Mixed|  Mix angular and linear 

        """
        Angular: int
        Linear: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> PositionMotorBuilder.Axis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the position motor 
         |NoColor|  Assigns no color to the position motor 

        """
        SpecifyColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> PositionMotorBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AxisType(self) -> PositionMotorBuilder.Axis:
        """
        Getter for property: ( PositionMotorBuilder.Axis NXOpen.Anim) AxisType
         Returns the axis type.  
             
         
        """
        pass
    @AxisType.setter
    def AxisType(self, axisType: PositionMotorBuilder.Axis):
        """
        Setter for property: ( PositionMotorBuilder.Axis NXOpen.Anim) AxisType
         Returns the axis type.  
             
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> PositionMotorBuilder.ColorOptions:
        """
        Getter for property: ( PositionMotorBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: PositionMotorBuilder.ColorOptions):
        """
        Setter for property: ( PositionMotorBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    def BarCalculate(self, index: int) -> None:
        """
         Calculates the bar. 
        """
        pass
    def CreateBar(self, index: int) -> None:
        """
         Creates a new bar. 
        """
        pass
    def DeleteBars(self, bars: List[int]) -> None:
        """
         Deletes the bars. 
        """
        pass
    def MirrorBars(self, bars: List[int], mirror_time: float) -> None:
        """
         Mirrors the bars. 
        """
        pass
    def PasteBars(self, bars: List[int], shift_time: float, isCut: bool) -> None:
        """
         Pastes the bars. 
        """
        pass
    def SetBarAcceleration(self, index: int, acceleration: float) -> None:
        """
         Sets the bar acceleration. 
        """
        pass
    def SetBarCalcType(self, index: int, calc_type: int) -> None:
        """
         Sets the bar calculation type. 
        """
        pass
    def SetBarDeceleration(self, index: int, deceleration: float) -> None:
        """
         Sets the bar deceleration. 
        """
        pass
    def SetBarEndTime(self, index: int, end_time: float) -> None:
        """
         Sets the bar end time. 
        """
        pass
    def SetBarIncrement(self, index: int, increment: float) -> None:
        """
         Sets the bar increment. 
        """
        pass
    def SetBarLimitAcceleration(self, index: int, limit_acceleration: bool) -> None:
        """
         Sets the bar limit acceleration. 
        """
        pass
    def SetBarName(self, index: int, name: str) -> None:
        """
         Sets the bar name. 
        """
        pass
    def SetBarSpeed(self, index: int, speed: float) -> None:
        """
         Sets the bar speed. 
        """
        pass
    def SetBarStartTime(self, index: int, start_time: float) -> None:
        """
         Sets the bar start time. 
        """
        pass
    def SetBarTime(self, bars: List[int], deltaStart: float, deltaDuration: float) -> None:
        """
         Sets the bar time. 
        """
        pass
    def SplitBar(self, index: int, split_time: float) -> None:
        """
         Splits the bars with the start time exp tag. 
        """
        pass
    def UpdateDestination(self) -> None:
        """
         Updates the motor destination. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class PositionMotorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Position Motor objects. """
    @overload
    def CreatePositionMotorBuilder(part: NXOpen.Part, positionMotor: PositionMotor) -> PositionMotorBuilder:
        """
         Creates a NXOpen.AnimationDesigner.PositionMotorBuilder. 
         Returns builder ( PositionMotorBuilder NXOpen.Anim): .
        """
        pass
    @overload
    def CreatePositionMotorBuilder(part: NXOpen.Part, positionMotor: PositionMotor, partOcc: NXOpen.Assemblies.Component) -> PositionMotorBuilder:
        """
         Creates a NXOpen.AnimationDesigner.PositionMotorBuilder. 
         Returns builder ( PositionMotorBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> PositionMotor:
        """
         Finds the  NXOpen.AnimationDesigner.PositionMotor  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns positionMotor ( PositionMotor NXOpen.Anim):   NXOpen.AnimationDesigner.PositionMotor  with this name. .
        """
        pass
class PositionMotor(Motor): 
    """ Represents a Position Motor feature. """
    pass
import NXOpen
class PreferencesBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.PreferencesBuilder builder. """
    class ArrangementTypes(Enum):
        """
        Members Include: 
         |Isolated|  Isolated 
         |Standard|  Standard 

        """
        Isolated: int
        Standard: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.ArrangementTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class BodyToUseForMeasureTypes(Enum):
        """
        Members Include: 
         |FacetBody|  Facet Body 
         |SolidBody|  Solid Body 

        """
        FacetBody: int
        SolidBody: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.BodyToUseForMeasureTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes(Enum):
        """
        Members Include: 
         |Value|  Length value 
         |Percentage|  Length percentage 

        """
        Value: int
        Percentage: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FlowLineStyleTypes(Enum):
        """
        Members Include: 
         |Original|  Original 
         |Solid|  Solid 
         |Dashed|  Dashed 
         |Phantom|  Phantom 
         |Centerline|  Centerline 
         |Dotted|  Dotted 
         |LongDashed|  Long Dashed 
         |DottedDashed|  Dotted Dashed 
         |LongDashedDoubleDotted|  Long Dashed Double Dotted 
         |LongDashedDotted|  Long Dashed Dotted 
         |LongDashedTriplicateDotted|  Long Dashed Triplicate Dotted 
         |LongDashedDoubleShortDashed|  Solid 

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
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.FlowLineStyleTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class GraphPlotTypes(Enum):
        """
        Members Include: 
         |Plot2D|  2D plot type 
         |Plot3D|  3D plot type 

        """
        Plot2D: int
        Plot3D: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.GraphPlotTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class KineoFlexibleFacetBodyPrecision(Enum):
        """
        Members Include: 
         |Low|  Low 
         |Medium|  Medium 
         |High|  High 
         |UserDefined|  User Defined 

        """
        Low: int
        Medium: int
        High: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PhysicsEngines(Enum):
        """
        Members Include: 
         |Bullet|  Bullet Engine 
         |PhysX|  PhysX Engine 
         |Kineo|  Kineo Engine 

        """
        Bullet: int
        PhysX: int
        Kineo: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.PhysicsEngines:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PrecisionPresetModes(Enum):
        """
        Members Include: 
         |Fine| 
         |Balance| 
         |Rough| 
         |UserDefined| 
         |Num| 

        """
        Fine: int
        Balance: int
        Rough: int
        UserDefined: int
        Num: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.PrecisionPresetModes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RigidGroupSelectionDisplayTypes(Enum):
        """
        Members Include: 
         |SelectionColor|  Selection Color 
         |BoundingBox|  Bounding Box 

        """
        SelectionColor: int
        BoundingBox: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.RigidGroupSelectionDisplayTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SolutionSearchScopeTypes(Enum):
        """
        Members Include: 
         |EntireAssembly|  Entire Assembly 
         |WithinWorkPartOnly|  Within Work Part Only 

        """
        EntireAssembly: int
        WithinWorkPartOnly: int
        @staticmethod
        def ValueOf(value: int) -> PreferencesBuilder.SolutionSearchScopeTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ArrangementType(self) -> PreferencesBuilder.ArrangementTypes:
        """
        Getter for property: ( PreferencesBuilder.ArrangementTypes NXOpen.Anim) ArrangementType
         Returns the option specifies the arrangement type.  
             
         
        """
        pass
    @ArrangementType.setter
    def ArrangementType(self, arrangementType: PreferencesBuilder.ArrangementTypes):
        """
        Setter for property: ( PreferencesBuilder.ArrangementTypes NXOpen.Anim) ArrangementType
         Returns the option specifies the arrangement type.  
             
         
        """
        pass
    @property
    def BulletFlexibleMaterialDensity(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BulletFlexibleMaterialDensity
         Returns the bullet flexible material density expression which specifies the density of a flexible body.  
             
         
        """
        pass
    @property
    def CollisionPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CollisionPrecision
         Returns the collision precision expression.  
             
         
        """
        pass
    @property
    def ContactColor(self) -> int:
        """
        Getter for property: (int) ContactColor
         Returns the color for contact face.  
             
         
        """
        pass
    @ContactColor.setter
    def ContactColor(self, color: int):
        """
        Setter for property: (int) ContactColor
         Returns the color for contact face.  
             
         
        """
        pass
    @property
    def ContactHardnessWithCollisionBody(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ContactHardnessWithCollisionBody
         Returns the flexible material contact hardness with collision expression which specifies how strict any overlap between a flexible body and collision body is treated.  
             
         
        """
        pass
    @property
    def ContactHardnessWithFlexibleBody(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ContactHardnessWithFlexibleBody
         Returns the flexible material contact hardness with flexible body expression which specifies how strict any overlap between flexible bodies is treated.  
             
         
        """
        pass
    @property
    def CurveSmoothing(self) -> bool:
        """
        Getter for property: (bool) CurveSmoothing
         Returns the smooth curve flag.  
             
         
        """
        pass
    @CurveSmoothing.setter
    def CurveSmoothing(self, isSoomth: bool):
        """
        Setter for property: (bool) CurveSmoothing
         Returns the smooth curve flag.  
             
         
        """
        pass
    @property
    def DelaySolve(self) -> bool:
        """
        Getter for property: (bool) DelaySolve
         Returns the delay solve flag.  
             
         
        """
        pass
    @DelaySolve.setter
    def DelaySolve(self, delay_solve: bool):
        """
        Setter for property: (bool) DelaySolve
         Returns the delay solve flag.  
             
         
        """
        pass
    @property
    def EnableParallel(self) -> bool:
        """
        Getter for property: (bool) EnableParallel
         Returns the enable parallel calculation flag.  
             
         
        """
        pass
    @EnableParallel.setter
    def EnableParallel(self, enableParallel: bool):
        """
        Setter for property: (bool) EnableParallel
         Returns the enable parallel calculation flag.  
             
         
        """
        pass
    @property
    def ErrorReduction(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ErrorReduction
         Returns the error reduction.  
             
         
        """
        pass
    @property
    def FlexibleCollisionSkipStep(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleCollisionSkipStep
         Returns the flexible collision skip step expression which specifies how many steps to skip when a flexible body collides.  
             
         
        """
        pass
    @property
    def FlexibleEngineTuningEnableMultithreading(self) -> bool:
        """
        Getter for property: (bool) FlexibleEngineTuningEnableMultithreading
         Returns the option determines whether to use multithreading.  
             
         
        """
        pass
    @FlexibleEngineTuningEnableMultithreading.setter
    def FlexibleEngineTuningEnableMultithreading(self, flexibleEngineTuningEnableMultithreading: bool):
        """
        Setter for property: (bool) FlexibleEngineTuningEnableMultithreading
         Returns the option determines whether to use multithreading.  
             
         
        """
        pass
    @property
    def FlexibleEngineTuningMinNumberOfNodesBetweenAttachments(self) -> int:
        """
        Getter for property: (int) FlexibleEngineTuningMinNumberOfNodesBetweenAttachments
         Returns the option specifies how many min number of nodes between attachments to create cable.  
             
         
        """
        pass
    @FlexibleEngineTuningMinNumberOfNodesBetweenAttachments.setter
    def FlexibleEngineTuningMinNumberOfNodesBetweenAttachments(self, flexibleEngineTuningMinNumberOfNodesBetweenAttachments: int):
        """
        Setter for property: (int) FlexibleEngineTuningMinNumberOfNodesBetweenAttachments
         Returns the option specifies how many min number of nodes between attachments to create cable.  
             
         
        """
        pass
    @property
    def FlexibleEngineTuningNumberOfThreads(self) -> int:
        """
        Getter for property: (int) FlexibleEngineTuningNumberOfThreads
         Returns the option specifies the number of threads.  
             
         
        """
        pass
    @FlexibleEngineTuningNumberOfThreads.setter
    def FlexibleEngineTuningNumberOfThreads(self, flexibleEngineTuningNumberOfThreads: int):
        """
        Setter for property: (int) FlexibleEngineTuningNumberOfThreads
         Returns the option specifies the number of threads.  
             
         
        """
        pass
    @property
    def FlexibleEngineTuningPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleEngineTuningPrecision
         Returns the flexible engine tuning precision.  
             
         
        """
        pass
    @property
    def FlexibleEngineTuningSkipStepsNumber(self) -> int:
        """
        Getter for property: (int) FlexibleEngineTuningSkipStepsNumber
         Returns the option specifies how many steps to skip during the simulation.  
             
         
        """
        pass
    @FlexibleEngineTuningSkipStepsNumber.setter
    def FlexibleEngineTuningSkipStepsNumber(self, flexibleEngineTuningSkipStepsNumber: int):
        """
        Setter for property: (int) FlexibleEngineTuningSkipStepsNumber
         Returns the option specifies how many steps to skip during the simulation.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyAngularPrecision(self) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
        """
        Getter for property: ( PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.Anim) FlexibleFacetBodyAngularPrecision
         Returns the flexible facet body angular precision.  
             
         
        """
        pass
    @FlexibleFacetBodyAngularPrecision.setter
    def FlexibleFacetBodyAngularPrecision(self, precision: PreferencesBuilder.KineoFlexibleFacetBodyPrecision):
        """
        Setter for property: ( PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.Anim) FlexibleFacetBodyAngularPrecision
         Returns the flexible facet body angular precision.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyFacetPrecisionOption(self) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
        """
        Getter for property: ( PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.Anim) FlexibleFacetBodyFacetPrecisionOption
         Returns the fineness of the facets and the smoothness of a circular cross section in a flexible body.  
             
         
        """
        pass
    @FlexibleFacetBodyFacetPrecisionOption.setter
    def FlexibleFacetBodyFacetPrecisionOption(self, precision: PreferencesBuilder.KineoFlexibleFacetBodyPrecision):
        """
        Setter for property: ( PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.Anim) FlexibleFacetBodyFacetPrecisionOption
         Returns the fineness of the facets and the smoothness of a circular cross section in a flexible body.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyLinearPrecision(self) -> PreferencesBuilder.KineoFlexibleFacetBodyPrecision:
        """
        Getter for property: ( PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.Anim) FlexibleFacetBodyLinearPrecision
         Returns the flexible facet body linear precision.  
             
         
        """
        pass
    @FlexibleFacetBodyLinearPrecision.setter
    def FlexibleFacetBodyLinearPrecision(self, precision: PreferencesBuilder.KineoFlexibleFacetBodyPrecision):
        """
        Setter for property: ( PreferencesBuilder.KineoFlexibleFacetBodyPrecision NXOpen.Anim) FlexibleFacetBodyLinearPrecision
         Returns the flexible facet body linear precision.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleFacetBodyPrecision
         Returns the flexible facet body precision.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodySameWithEngineTuningPrecision(self) -> bool:
        """
        Getter for property: (bool) FlexibleFacetBodySameWithEngineTuningPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    @FlexibleFacetBodySameWithEngineTuningPrecision.setter
    def FlexibleFacetBodySameWithEngineTuningPrecision(self, flexibleFacetBodySameWithEngineTuningPrecision: bool):
        """
        Setter for property: (bool) FlexibleFacetBodySameWithEngineTuningPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyUserDefinedAngularPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleFacetBodyUserDefinedAngularPrecision
         Returns the flexible facet body user defined angular precision.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyUserDefinedLinearPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleFacetBodyUserDefinedLinearPrecision
         Returns the flexible facet body user defined linear precision.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage(self) -> float:
        """
        Getter for property: (float) FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage
         Returns the user defined linear precision percentage of a kineo facet body.  
             
         
        """
        pass
    @FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage.setter
    def FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage(self, precision: float):
        """
        Setter for property: (float) FlexibleFacetBodyUserDefinedLinearPrecisionByPercentage
         Returns the user defined linear precision percentage of a kineo facet body.  
             
         
        """
        pass
    @property
    def FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType(self) -> PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes:
        """
        Getter for property: ( PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.Anim) FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType
         Returns the option determines whether to use a length value instead of a percentage.  
             
         
        """
        pass
    @FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType.setter
    def FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType(self, inputType: PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes):
        """
        Setter for property: ( PreferencesBuilder.FlexibleFacetBodyUserDefinedLinearPrecisionInputTypes NXOpen.Anim) FlexibleFacetBodyUserUsingDefinedLinearPrecisionInputType
         Returns the option determines whether to use a length value instead of a percentage.  
             
         
        """
        pass
    @property
    def FlexibleFacetPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleFacetPrecision
         Returns the flexible facet precision expression which specifies the fineness of the facets in a flexible body.  
           A larger value means larger facets and relatively better simulation performance.   
         
        """
        pass
    @property
    def FlexibleMaterialAnchorHardness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialAnchorHardness
         Returns the flexible material anchor hardness expression which specifies how strongly a flexible body is expected to stick to another object, e.  
          g. a roller.   
         
        """
        pass
    @property
    def FlexibleMaterialDamping(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialDamping
         Returns the flexible material damping expression which specifies the coefficient of damping forces acting on flexible bodies to reduce their oscillation over time.  
             
         
        """
        pass
    @property
    def FlexibleMaterialDensity(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialDensity
         Returns the flexible material density expression which specifies the density of a flexible body.  
             
         
        """
        pass
    @property
    def FlexibleMaterialDynamicFriction(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialDynamicFriction
         Returns the flexible material dynamic friction expression which specifies the coefficient of the dynamic friction acting on a flexible body against a surface.  
             
         
        """
        pass
    @property
    def FlexibleMaterialEnableMaxContactForce(self) -> bool:
        """
        Getter for property: (bool) FlexibleMaterialEnableMaxContactForce
         Returns the option determines whether to set the maximum contact force.  
             
         
        """
        pass
    @FlexibleMaterialEnableMaxContactForce.setter
    def FlexibleMaterialEnableMaxContactForce(self, flexibleMaterialEnableMaxContactForce: bool):
        """
        Setter for property: (bool) FlexibleMaterialEnableMaxContactForce
         Returns the option determines whether to set the maximum contact force.  
             
         
        """
        pass
    @property
    def FlexibleMaterialEnableMaxTwist(self) -> bool:
        """
        Getter for property: (bool) FlexibleMaterialEnableMaxTwist
         Returns the option determines whether to set the maximum twist.  
             
         
        """
        pass
    @FlexibleMaterialEnableMaxTwist.setter
    def FlexibleMaterialEnableMaxTwist(self, flexibleMaterialEnableMaxTwist: bool):
        """
        Setter for property: (bool) FlexibleMaterialEnableMaxTwist
         Returns the option determines whether to set the maximum twist.  
             
         
        """
        pass
    @property
    def FlexibleMaterialEnableMinCurvature(self) -> bool:
        """
        Getter for property: (bool) FlexibleMaterialEnableMinCurvature
         Returns the option determines whether to set the minimum curvature.  
             
         
        """
        pass
    @FlexibleMaterialEnableMinCurvature.setter
    def FlexibleMaterialEnableMinCurvature(self, flexibleMaterialEnableMinCurvature: bool):
        """
        Setter for property: (bool) FlexibleMaterialEnableMinCurvature
         Returns the option determines whether to set the minimum curvature.  
             
         
        """
        pass
    @property
    def FlexibleMaterialFulcrumLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialFulcrumLength
         Returns the flexible material fulcrum length.  
             
         
        """
        pass
    @property
    def FlexibleMaterialLinearStiffness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialLinearStiffness
         Returns the flexible material linear stiffness expression which specifies the coefficient of conservation of distance between adjacent particles.  
             
         
        """
        pass
    @property
    def FlexibleMaterialMaxContactForce(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialMaxContactForce
         Returns the flexible material maximum contact force.  
             
         
        """
        pass
    @property
    def FlexibleMaterialMaxTension(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialMaxTension
         Returns the flexible material maximum tension.  
             
         
        """
        pass
    @property
    def FlexibleMaterialMaxTwist(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialMaxTwist
         Returns the flexible material maximum twist.  
             
         
        """
        pass
    @property
    def FlexibleMaterialMinCurvature(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialMinCurvature
         Returns the flexible material minimum curvature.  
             
         
        """
        pass
    @property
    def FlexibleMaterialOscillation(self) -> float:
        """
        Getter for property: (float) FlexibleMaterialOscillation
         Returns the flexible material oscillation.  
             
         
        """
        pass
    @FlexibleMaterialOscillation.setter
    def FlexibleMaterialOscillation(self, flexibleMaterialOscillation: float):
        """
        Setter for property: (float) FlexibleMaterialOscillation
         Returns the flexible material oscillation.  
             
         
        """
        pass
    @property
    def FlexibleMaterialPrecision(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialPrecision
         Returns the flexible material precision expression which specifies the fineness of the elements in a flexible body.  
             
         
        """
        pass
    @property
    def FlexibleMaterialYoungModulus(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FlexibleMaterialYoungModulus
         Returns the flexible material Young's modulus.  
             
         
        """
        pass
    @property
    def FlowLineColor(self) -> int:
        """
        Getter for property: (int) FlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    @FlowLineColor.setter
    def FlowLineColor(self, flowlinecolor: int):
        """
        Setter for property: (int) FlowLineColor
         Returns the flow line color.  
             
         
        """
        pass
    @property
    def FlowLineFont(self) -> PreferencesBuilder.FlowLineStyleTypes:
        """
        Getter for property: ( PreferencesBuilder.FlowLineStyleTypes NXOpen.Anim) FlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    @FlowLineFont.setter
    def FlowLineFont(self, flowlinefont: PreferencesBuilder.FlowLineStyleTypes):
        """
        Setter for property: ( PreferencesBuilder.FlowLineStyleTypes NXOpen.Anim) FlowLineFont
         Returns the flow line font.  
             
         
        """
        pass
    @property
    def FlowLineWidth(self) -> int:
        """
        Getter for property: (int) FlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    @FlowLineWidth.setter
    def FlowLineWidth(self, flowlinewidth: int):
        """
        Setter for property: (int) FlowLineWidth
         Returns the flow line width.  
             
         
        """
        pass
    @property
    def GraphPlotType(self) -> PreferencesBuilder.GraphPlotTypes:
        """
        Getter for property: ( PreferencesBuilder.GraphPlotTypes NXOpen.Anim) GraphPlotType
         Returns the option specifies the graph plot type.  
             
         
        """
        pass
    @GraphPlotType.setter
    def GraphPlotType(self, plotType: PreferencesBuilder.GraphPlotTypes):
        """
        Setter for property: ( PreferencesBuilder.GraphPlotTypes NXOpen.Anim) GraphPlotType
         Returns the option specifies the graph plot type.  
             
         
        """
        pass
    @property
    def GraphSampleTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) GraphSampleTime
         Returns the graph sample time expression.  
             
         
        """
        pass
    @property
    def GravityDirection(self) -> int:
        """
        Getter for property: (int) GravityDirection
         Returns the gravity direction.  
           0 - Gx, 1 - Gy, 2 - Gz, 3 - None.  
         
        """
        pass
    @GravityDirection.setter
    def GravityDirection(self, direction: int):
        """
        Setter for property: (int) GravityDirection
         Returns the gravity direction.  
           0 - Gx, 1 - Gy, 2 - Gz, 3 - None.  
         
        """
        pass
    @property
    def HideMeasureRuler(self) -> bool:
        """
        Getter for property: (bool) HideMeasureRuler
         Returns the hide measure ruler flag.  
             
         
        """
        pass
    @HideMeasureRuler.setter
    def HideMeasureRuler(self, hide: bool):
        """
        Setter for property: (bool) HideMeasureRuler
         Returns the hide measure ruler flag.  
             
         
        """
        pass
    @property
    def ImpulseSplitWithCollisionBody(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ImpulseSplitWithCollisionBody
         Returns the flexible material impulse split when contact with collision body expression which specifies how to proportion the impulse generated by a collision between a flexible body and collision body.  
             
         
        """
        pass
    @property
    def ImpulseSplitWithFlexibleBody(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ImpulseSplitWithFlexibleBody
         Returns the flexible material impulse split when contact with flexible body expression which specifies how to proportion the impulse generated by a collision between flexible bodies.  
             
         
        """
        pass
    @property
    def KineoAngularTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) KineoAngularTolerance
         Returns the kineo angular tolerance.  
             
         
        """
        pass
    @property
    def KineoLinearTolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) KineoLinearTolerance
         Returns the kineo linear tolerance.  
             
         
        """
        pass
    @property
    def MaxIteration(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxIteration
         Returns the max iteration.  
             
         
        """
        pass
    @property
    def NonRigidGroupColor(self) -> int:
        """
        Getter for property: (int) NonRigidGroupColor
         Returns the color for non rigid group body.  
             
         
        """
        pass
    @NonRigidGroupColor.setter
    def NonRigidGroupColor(self, color: int):
        """
        Setter for property: (int) NonRigidGroupColor
         Returns the color for non rigid group body.  
             
         
        """
        pass
    @property
    def OnlySimulateActiveDisplayPart(self) -> bool:
        """
        Getter for property: (bool) OnlySimulateActiveDisplayPart
         Returns the only simulate active display part flag.  
             
         
        """
        pass
    @OnlySimulateActiveDisplayPart.setter
    def OnlySimulateActiveDisplayPart(self, bOnly: bool):
        """
        Setter for property: (bool) OnlySimulateActiveDisplayPart
         Returns the only simulate active display part flag.  
             
         
        """
        pass
    @property
    def OptimizeRigidGroupProperty(self) -> bool:
        """
        Getter for property: (bool) OptimizeRigidGroupProperty
         Returns the option indicates whether the optimized properties of rigid group are being used.  
             
         
        """
        pass
    @OptimizeRigidGroupProperty.setter
    def OptimizeRigidGroupProperty(self, optimizeRigidProp: bool):
        """
        Setter for property: (bool) OptimizeRigidGroupProperty
         Returns the option indicates whether the optimized properties of rigid group are being used.  
             
         
        """
        pass
    @property
    def PhysicsEngine(self) -> PreferencesBuilder.PhysicsEngines:
        """
        Getter for property: ( PreferencesBuilder.PhysicsEngines NXOpen.Anim) PhysicsEngine
         Returns the physics engine.  
             
         
        """
        pass
    @PhysicsEngine.setter
    def PhysicsEngine(self, engine: PreferencesBuilder.PhysicsEngines):
        """
        Setter for property: ( PreferencesBuilder.PhysicsEngines NXOpen.Anim) PhysicsEngine
         Returns the physics engine.  
             
         
        """
        pass
    @property
    def PrecisionPresetMode(self) -> PreferencesBuilder.PrecisionPresetModes:
        """
        Getter for property: ( PreferencesBuilder.PrecisionPresetModes NXOpen.Anim) PrecisionPresetMode
         Returns the simulation preset mode   
            
         
        """
        pass
    @PrecisionPresetMode.setter
    def PrecisionPresetMode(self, presetMode: PreferencesBuilder.PrecisionPresetModes):
        """
        Setter for property: ( PreferencesBuilder.PrecisionPresetModes NXOpen.Anim) PrecisionPresetMode
         Returns the simulation preset mode   
            
         
        """
        pass
    @property
    def RandomizeSolvingOrder(self) -> bool:
        """
        Getter for property: (bool) RandomizeSolvingOrder
         Returns the option indicates whether to randomize the solving order by the engine.  
             
         
        """
        pass
    @RandomizeSolvingOrder.setter
    def RandomizeSolvingOrder(self, randomOrder: bool):
        """
        Setter for property: (bool) RandomizeSolvingOrder
         Returns the option indicates whether to randomize the solving order by the engine.  
             
         
        """
        pass
    @property
    def RichGeomType(self) -> bool:
        """
        Getter for property: (bool) RichGeomType
         Returns the rich geometry type.  
            
         
        """
        pass
    @RichGeomType.setter
    def RichGeomType(self, richGeomType: bool):
        """
        Setter for property: (bool) RichGeomType
         Returns the rich geometry type.  
            
         
        """
        pass
    @property
    def RigidGroupSelectionDisplay(self) -> PreferencesBuilder.RigidGroupSelectionDisplayTypes:
        """
        Getter for property: ( PreferencesBuilder.RigidGroupSelectionDisplayTypes NXOpen.Anim) RigidGroupSelectionDisplay
         Returns the option specifies the selection display for rigid groups.  
             
         
        """
        pass
    @RigidGroupSelectionDisplay.setter
    def RigidGroupSelectionDisplay(self, displayType: PreferencesBuilder.RigidGroupSelectionDisplayTypes):
        """
        Setter for property: ( PreferencesBuilder.RigidGroupSelectionDisplayTypes NXOpen.Anim) RigidGroupSelectionDisplay
         Returns the option specifies the selection display for rigid groups.  
             
         
        """
        pass
    @property
    def SameWithFlexibleMaterialPrecision(self) -> bool:
        """
        Getter for property: (bool) SameWithFlexibleMaterialPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    @SameWithFlexibleMaterialPrecision.setter
    def SameWithFlexibleMaterialPrecision(self, sameWithFlexibleMaterialPrecision: bool):
        """
        Setter for property: (bool) SameWithFlexibleMaterialPrecision
         Returns the option determines whether facet bodies should use the same precision as engine tuning.  
             
         
        """
        pass
    @property
    def ShowFlowLine(self) -> bool:
        """
        Getter for property: (bool) ShowFlowLine
         Returns the option for enable draw flow line.  
             
         
        """
        pass
    @ShowFlowLine.setter
    def ShowFlowLine(self, showflowline: bool):
        """
        Setter for property: (bool) ShowFlowLine
         Returns the option for enable draw flow line.  
             
         
        """
        pass
    @property
    def SolutionSearchScope(self) -> PreferencesBuilder.SolutionSearchScopeTypes:
        """
        Getter for property: ( PreferencesBuilder.SolutionSearchScopeTypes NXOpen.Anim) SolutionSearchScope
         Returns the option specifies the search scope for the Animation Designer definition.  
             
         
        """
        pass
    @SolutionSearchScope.setter
    def SolutionSearchScope(self, scopeType: PreferencesBuilder.SolutionSearchScopeTypes):
        """
        Setter for property: ( PreferencesBuilder.SolutionSearchScopeTypes NXOpen.Anim) SolutionSearchScope
         Returns the option specifies the search scope for the Animation Designer definition.  
             
         
        """
        pass
    @property
    def StepIncrementTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StepIncrementTime
         Returns the step time expression.  
             
         
        """
        pass
    @property
    def StepTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StepTime
         Returns the step time.  
             
         
        """
        pass
    @property
    def TimeScaleFactor(self) -> float:
        """
        Getter for property: (float) TimeScaleFactor
         Returns the time scale factor   
            
         
        """
        pass
    @TimeScaleFactor.setter
    def TimeScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) TimeScaleFactor
         Returns the time scale factor   
            
         
        """
        pass
    @property
    def Tolerance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Tolerance
         Returns the tolerance.  
             
         
        """
        pass
    @property
    def UseFacetToMeasure(self) -> PreferencesBuilder.BodyToUseForMeasureTypes:
        """
        Getter for property: ( PreferencesBuilder.BodyToUseForMeasureTypes NXOpen.Anim) UseFacetToMeasure
         Returns the option indicates whether to use facet body instead of solid body to measure distance or angle in order to improve performance.  
             
         
        """
        pass
    @UseFacetToMeasure.setter
    def UseFacetToMeasure(self, bodyType: PreferencesBuilder.BodyToUseForMeasureTypes):
        """
        Setter for property: ( PreferencesBuilder.BodyToUseForMeasureTypes NXOpen.Anim) UseFacetToMeasure
         Returns the option indicates whether to use facet body instead of solid body to measure distance or angle in order to improve performance.  
             
         
        """
        pass
import NXOpen
class RackPinionBuilder(CouplerBuilder): 
    """ Represents a NXOpen.AnimationDesigner.RackPinionBuilder. """
    @property
    def ContactPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ContactPoint
         Returns the contact point.  
             
         
        """
        pass
    @ContactPoint.setter
    def ContactPoint(self, contactPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ContactPoint
         Returns the contact point.  
             
         
        """
        pass
    @property
    def Radius(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Radius
         Returns the radius expression.  
             
         
        """
        pass
import NXOpen
class RackPinionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Rack Pinion objects. """
    def CreateRackPinionBuilder(part: NXOpen.Part, rackPinion: RackPinion) -> RackPinionBuilder:
        """
         Creates a NXOpen.AnimationDesigner.RackPinionBuilder. 
         Returns builder ( RackPinionBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> RackPinion:
        """
         Finds the  NXOpen.AnimationDesigner.RackPinion  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns rackPinion ( RackPinion NXOpen.Anim):   NXOpen.AnimationDesigner.RackPinion  with this name. .
        """
        pass
class RackPinion(Coupler): 
    """ Represents a Rack Pinion feature. """
    pass
import NXOpen
class RevoluteJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.RevoluteJointBuilder. """
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    @property
    def EnableLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.   
         
        """
        pass
    @EnableLowerLimit.setter
    def EnableLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.   
         
        """
        pass
    @property
    def EnableUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    @EnableUpperLimit.setter
    def EnableUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    @property
    def LowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerLimit
         Returns the lower limit.  
           The lower limit setup for joint movement.   
         
        """
        pass
    @property
    def Point(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Point
         Returns the origin point.  
             
         
        """
        pass
    @Point.setter
    def Point(self, point: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Point
         Returns the origin point.  
             
         
        """
        pass
    @property
    def StartAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartAngle
         Returns the start angle.  
             
         
        """
        pass
    @property
    def UpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UpperLimit
         Returns the upper limit.  
           The upper limit setup for joint movement.   
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class RevoluteJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Revolute Joint objects. """
    @overload
    def CreateRevoluteJointBuilder(part: NXOpen.Part, hingeJoint: RevoluteJoint) -> RevoluteJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.RevoluteJointBuilder. 
         Returns builder ( RevoluteJointBuilder NXOpen.Anim): .
        """
        pass
    @overload
    def CreateRevoluteJointBuilder(part: NXOpen.Part, hingeJoint: RevoluteJoint, partOcc: NXOpen.Assemblies.Component) -> RevoluteJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.RevoluteJointBuilder. 
         Returns builder ( RevoluteJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> RevoluteJoint:
        """
         Finds the  NXOpen.AnimationDesigner.RevoluteJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns revoluteJoint ( RevoluteJoint NXOpen.Anim):   NXOpen.AnimationDesigner.RevoluteJoint  with this name. .
        """
        pass
class RevoluteJoint(PhysicsJoint): 
    """ Represents a Revolute Joint feature. """
    pass
import NXOpen
class RigidGroupBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.AnimationDesigner.RigidGroupBuilder. """
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the group 
         |AutomaticColor|  Auto-assigns a color to each group 
         |NoColor|  Assigns no color to the groups 

        """
        SpecifyColor: int
        AutomaticColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> RigidGroupBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class CreationTypes(Enum):
        """
        Members Include: 
         |Combine|  Combine selections into one Rigid Group 
         |Separate|  Create a Rigid Group for each selection 

        """
        Combine: int
        Separate: int
        @staticmethod
        def ValueOf(value: int) -> RigidGroupBuilder.CreationTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MassPropertiesOption(Enum):
        """
        Members Include: 
         |Automatic|  automatic 
         |UserDefined|  user defined 

        """
        Automatic: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> RigidGroupBuilder.MassPropertiesOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AngularVelocityDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AngularVelocityDirection
         Returns the angular velocity direction.  
           It is only used when angular velocity is not zero.   
         
        """
        pass
    @AngularVelocityDirection.setter
    def AngularVelocityDirection(self, dir: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AngularVelocityDirection
         Returns the angular velocity direction.  
           It is only used when angular velocity is not zero.   
         
        """
        pass
    @property
    def AngularVelocityMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularVelocityMagnitude
         Returns the angular velocity magnitude.  
             
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> RigidGroupBuilder.ColorOptions:
        """
        Getter for property: ( RigidGroupBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: RigidGroupBuilder.ColorOptions):
        """
        Setter for property: ( RigidGroupBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @property
    def CreationType(self) -> RigidGroupBuilder.CreationTypes:
        """
        Getter for property: ( RigidGroupBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type.  
             
         
        """
        pass
    @CreationType.setter
    def CreationType(self, creationType: RigidGroupBuilder.CreationTypes):
        """
        Setter for property: ( RigidGroupBuilder.CreationTypes NXOpen.Anim) CreationType
         Returns the creation type.  
             
         
        """
        pass
    @property
    def Geometry(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Geometry
         Returns the geometries.  
           This can be  NXOpen::Assemblies::ComponentAssembly ,
                     NXOpen::Point ,  NXOpen::Body ,  NXOpen::Curve ,
                     NXOpen::CoordinateSystem ,  NXOpen::DatumAxis ,
                     NXOpen::DatumPlane ,  NXOpen::Annotations::Pmi ,
                    Line Designer Connectors, etc.   
         
        """
        pass
    @property
    def InertiaIxx(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaIxx
         Returns the inertia Ixx.  
             
         
        """
        pass
    @property
    def InertiaIxy(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaIxy
         Returns the inertia Ixy.  
             
         
        """
        pass
    @property
    def InertiaIxz(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaIxz
         Returns the inertia Ixz.  
             
         
        """
        pass
    @property
    def InertiaIyy(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaIyy
         Returns the inertia Iyy.  
             
         
        """
        pass
    @property
    def InertiaIyz(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaIyz
         Returns the inertia Iyz.  
             
         
        """
        pass
    @property
    def InertiaIzz(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) InertiaIzz
         Returns the inertia Izz.  
             
         
        """
        pass
    @property
    def LinearVelocityDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) LinearVelocityDirection
         Returns the linear velocity.  
           It is only used when linear velocity is not zero.   
         
        """
        pass
    @LinearVelocityDirection.setter
    def LinearVelocityDirection(self, dir: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) LinearVelocityDirection
         Returns the linear velocity.  
           It is only used when linear velocity is not zero.   
         
        """
        pass
    @property
    def LinearVelocityMagnitude(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearVelocityMagnitude
         Returns the linear velocity magnitude.  
             
         
        """
        pass
    @property
    def Mass(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Mass
         Returns the mass.  
             
         
        """
        pass
    @property
    def MassCenterPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) MassCenterPoint
         Returns the mass center point.  
             
         
        """
        pass
    @MassCenterPoint.setter
    def MassCenterPoint(self, center: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) MassCenterPoint
         Returns the mass center point.  
             
         
        """
        pass
    @property
    def MassProperty(self) -> RigidGroupBuilder.MassPropertiesOption:
        """
        Getter for property: ( RigidGroupBuilder.MassPropertiesOption NXOpen.Anim) MassProperty
         Returns the auto-calculate mass property flag which is used to indicate whether
                    all mass properties are calculated by system.  
             
         
        """
        pass
    @MassProperty.setter
    def MassProperty(self, massProperty: RigidGroupBuilder.MassPropertiesOption):
        """
        Setter for property: ( RigidGroupBuilder.MassPropertiesOption NXOpen.Anim) MassProperty
         Returns the auto-calculate mass property flag which is used to indicate whether
                    all mass properties are calculated by system.  
             
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name.  
             
         
        """
        pass
    @property
    def Orientation(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Orientation
         Returns the orientation.  
             
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Orientation
         Returns the orientation.  
             
         
        """
        pass
import NXOpen
class RigidGroupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Rigid Group objects. """
    def CreateRigidGroupBuilder(part: NXOpen.Part, rigidGroup: RigidGroup) -> RigidGroupBuilder:
        """
         Creates a NXOpen.AnimationDesigner.RigidGroupBuilder. 
         Returns builder ( RigidGroupBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> RigidGroup:
        """
         Finds the  NXOpen.AnimationDesigner.RigidGroup  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns rigidGroup ( RigidGroup NXOpen.Anim):   NXOpen.AnimationDesigner.RigidGroup  with this name. .
        """
        pass
import NXOpen
class RigidGroup(NXOpen.DisplayableObject): 
    """ Represents a Rigid Group feature. """
    pass
import NXOpen
class ScrewJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.ScrewJointBuilder. """
    @property
    def AxisVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    @AxisVector.setter
    def AxisVector(self, axisVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) AxisVector
         Returns the axis vector.  
             
         
        """
        pass
    @property
    def ExpressionRatio(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExpressionRatio
         Returns    a value that indicates pitch value for the screw joint.  
            
            
         
        """
        pass
    @property
    def PointOrigin(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOrigin
         Returns the origin point.  
             
         
        """
        pass
    @PointOrigin.setter
    def PointOrigin(self, origin: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOrigin
         Returns the origin point.  
             
         
        """
        pass
import NXOpen
class ScrewJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Screw Joint objects. """
    def CreateScrewJointBuilder(part: NXOpen.Part, screwJoint: ScrewJoint) -> ScrewJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.ScrewJointBuilder. 
         Returns builder ( ScrewJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> ScrewJoint:
        """
         Finds the  NXOpen.AnimationDesigner.ScrewJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns screwJoint ( ScrewJoint NXOpen.Anim):   NXOpen.AnimationDesigner.ScrewJoint  with this name. .
        """
        pass
class ScrewJoint(PhysicsJoint): 
    """ Represents a Screw Joint feature. """
    pass
import NXOpen
class SliderJointBuilder(PhysicsJointBuilder): 
    """ Represents a NXOpen.AnimationDesigner.SliderJointBuilder. """
    @property
    def EnableLowerLimit(self) -> bool:
        """
        Getter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.  
         
        """
        pass
    @EnableLowerLimit.setter
    def EnableLowerLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableLowerLimit
         Returns the lower limit option.  
           If the enable is true, then the joint will be 
                    applied a lower limit in movement.  
         
        """
        pass
    @property
    def EnableUpperLimit(self) -> bool:
        """
        Getter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    @EnableUpperLimit.setter
    def EnableUpperLimit(self, enable: bool):
        """
        Setter for property: (bool) EnableUpperLimit
         Returns the upper limit option.  
           If the enable is true, then the joint will be 
                    applied an upper limit in movement.   
         
        """
        pass
    @property
    def LowerLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LowerLimit
         Returns the lower limit.  
           The lower limit setup for joint movement.   
         
        """
        pass
    @property
    def Offset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Offset
         Returns the offset value.  
             
         
        """
        pass
    @property
    def UpperLimit(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) UpperLimit
         Returns the upper limit.  
           The upper limit setup for joint movement.   
         
        """
        pass
    @property
    def Vector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) Vector
         Returns the vector.  
             
         
        """
        pass
    @Vector.setter
    def Vector(self, specifyVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) Vector
         Returns the vector.  
             
         
        """
        pass
import NXOpen
import NXOpen.Assemblies
class SliderJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Slider Joint objects. """
    @overload
    def CreateSliderJointBuilder(part: NXOpen.Part, slidingJoint: SliderJoint) -> SliderJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.SliderJointBuilder. 
         Returns builder ( SliderJointBuilder NXOpen.Anim): .
        """
        pass
    @overload
    def CreateSliderJointBuilder(part: NXOpen.Part, slidingJoint: SliderJoint, partOcc: NXOpen.Assemblies.Component) -> SliderJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.SliderJointBuilder. 
         Returns builder ( SliderJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> SliderJoint:
        """
         Finds the  NXOpen.AnimationDesigner.SliderJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns sliderJoint ( SliderJoint NXOpen.Anim):   NXOpen.AnimationDesigner.SliderJoint  with this name. .
        """
        pass
class SliderJoint(PhysicsJoint): 
    """ Represents a Slider Joint feature. """
    pass
import NXOpen
class SpeedMotorBuilder(MotorBuilder): 
    """ Represents a NXOpen.AnimationDesigner.SpeedMotorBuilder. """
    class Axis(Enum):
        """
        Members Include: 
         |Angular|  Angular 
         |Linear|  Linear 
         |Mixed|  Mix angular and linear 

        """
        Angular: int
        Linear: int
        Mixed: int
        @staticmethod
        def ValueOf(value: int) -> SpeedMotorBuilder.Axis:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColorOptions(Enum):
        """
        Members Include: 
         |SpecifyColor|  Assigns a color to the speed motor 
         |NoColor|  Assigns no color to the speed motor 

        """
        SpecifyColor: int
        NoColor: int
        @staticmethod
        def ValueOf(value: int) -> SpeedMotorBuilder.ColorOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AxisType(self) -> SpeedMotorBuilder.Axis:
        """
        Getter for property: ( SpeedMotorBuilder.Axis NXOpen.Anim) AxisType
         Returns the axis type.  
             
         
        """
        pass
    @AxisType.setter
    def AxisType(self, axisType: SpeedMotorBuilder.Axis):
        """
        Setter for property: ( SpeedMotorBuilder.Axis NXOpen.Anim) AxisType
         Returns the axis type.  
             
         
        """
        pass
    @property
    def Color(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @Color.setter
    def Color(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) Color
         Returns the color.  
             
         
        """
        pass
    @property
    def ColorOption(self) -> SpeedMotorBuilder.ColorOptions:
        """
        Getter for property: ( SpeedMotorBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @ColorOption.setter
    def ColorOption(self, colorOption: SpeedMotorBuilder.ColorOptions):
        """
        Setter for property: ( SpeedMotorBuilder.ColorOptions NXOpen.Anim) ColorOption
         Returns the color option.  
             
         
        """
        pass
    @property
    def MaxAcceleration(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxAcceleration
         Returns the max acceleration.  
             
         
        """
        pass
    @property
    def Speed(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Speed
         Returns the speed.  
             
         
        """
        pass
    @property
    def StartTime(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartTime
         Returns the start time.  
             
         
        """
        pass
    @property
    def UseAcceleration(self) -> bool:
        """
        Getter for property: (bool) UseAcceleration
         Returns the limit acceleration.  
             
         
        """
        pass
    @UseAcceleration.setter
    def UseAcceleration(self, useAcceleration: bool):
        """
        Setter for property: (bool) UseAcceleration
         Returns the limit acceleration.  
             
         
        """
        pass
    def EditStartTime(self, deltaStart: float) -> None:
        """
         Sets the start time value. 
        """
        pass
import NXOpen
import NXOpen.Assemblies
class SpeedMotorCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Speed Motor objects. """
    @overload
    def CreateSpeedMotorBuilder(part: NXOpen.Part, speedMotor: SpeedMotor) -> SpeedMotorBuilder:
        """
         Creates a NXOpen.AnimationDesigner.SpeedMotorBuilder. 
         Returns builder ( SpeedMotorBuilder NXOpen.Anim): .
        """
        pass
    @overload
    def CreateSpeedMotorBuilder(part: NXOpen.Part, speedMotor: SpeedMotor, partOcc: NXOpen.Assemblies.Component) -> SpeedMotorBuilder:
        """
         Creates a NXOpen.AnimationDesigner.SpeedMotorBuilder. 
         Returns builder ( SpeedMotorBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> SpeedMotor:
        """
         Finds the  NXOpen.AnimationDesigner.SpeedMotor  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns speedMotor ( SpeedMotor NXOpen.Anim):   NXOpen.AnimationDesigner.SpeedMotor  with this name. .
        """
        pass
class SpeedMotor(Motor): 
    """ Represents a Speed Motor feature. """
    pass
import NXOpen
class SphericalJointBuilder(PhysicsJointBuilder): 
    """ Represents a AnimationDesigner.SphericalJointBuilder builder """
    @property
    def AnchorPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
    @AnchorPoint.setter
    def AnchorPoint(self, anchorPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) AnchorPoint
         Returns the anchor point.  
             
         
        """
        pass
import NXOpen
class SphericalJointCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Spherical Joint objects. """
    def CreateSphericalJointBuilder(part: NXOpen.Part, ballJoint: SphericalJoint) -> SphericalJointBuilder:
        """
         Creates a NXOpen.AnimationDesigner.SphericalJointBuilder. 
         Returns builder ( SphericalJointBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> SphericalJoint:
        """
         Finds the  NXOpen.AnimationDesigner.SphericalJoint  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns sphericalJoint ( SphericalJoint NXOpen.Anim):   NXOpen.AnimationDesigner.SphericalJoint  with this name. .
        """
        pass
class SphericalJoint(PhysicsJoint): 
    """ Represents a Spherical Joint feature. """
    pass
import NXOpen
class TracerBuilder(NXOpen.Builder): 
    """ Represents a AnimationDesigner.Tracer builder """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the name   
            
         
        """
        pass
    @property
    def SelectPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SelectPoint
         Returns the origin point.  
             
         
        """
        pass
    @SelectPoint.setter
    def SelectPoint(self, selectPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SelectPoint
         Returns the origin point.  
             
         
        """
        pass
    @property
    def SelectRefBody(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) SelectRefBody
         Returns the specify reference body selection.  
           This should be a  NXOpen::AnimationDesigner::RigidGroup    
         
        """
        pass
    @property
    def Selection(self) -> NXOpen.SelectNXObject:
        """
        Getter for property: ( NXOpen.SelectNXObject) Selection
         Returns the body selection.  
           This should be a  NXOpen::AnimationDesigner::RigidGroup    
         
        """
        pass
    @property
    def ShowInSimulation(self) -> bool:
        """
        Getter for property: (bool) ShowInSimulation
         Returns    the option of show during simulation.  
            
            
         
        """
        pass
    @ShowInSimulation.setter
    def ShowInSimulation(self, show: bool):
        """
        Setter for property: (bool) ShowInSimulation
         Returns    the option of show during simulation.  
            
            
         
        """
        pass
    @property
    def TraceRateSetting(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TraceRateSetting
         Returns the trace rate setting   
            
         
        """
        pass
import NXOpen
class TracerCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of Tracer. """
    def CreateTracerBuilder(part: NXOpen.Part, tracer: Tracer) -> TracerBuilder:
        """
         Creates a NXOpen.AnimationDesigner.TracerBuilder. 
         Returns builder ( TracerBuilder NXOpen.Anim): .
        """
        pass
    def FindObject(part: NXOpen.Part, name: str) -> Tracer:
        """
         Finds the  NXOpen.AnimationDesigner.Tracer  with the given name.
                    An exception will be thrown if no object can be found with given name. 
         Returns traceObject ( Tracer NXOpen.Anim):   NXOpen.AnimationDesigner.Tracer  with this name. .
        """
        pass
import NXOpen
class Tracer(NXOpen.DisplayableObject): 
    """ Represents the Tracer class. A Tracer can make an object be able
        to trace an point on it. """
    pass
