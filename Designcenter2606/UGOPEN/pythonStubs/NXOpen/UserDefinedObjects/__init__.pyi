from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class UserDefinedClassManager(NXOpen.Object): 
    """ Manages the user defined objects. """
    def CreateUserDefinedObjectClass(class_name: str, friendly_name: str) -> UserDefinedClass:
        """
         
                  Constructs a new NXOpen.UserDefinedObjects.UserDefinedClass object.
                 
         Returns udo_class ( UserDefinedClass NXOpen.UserD):  The new UserDefinedClass instance .
        """
        pass
    def GetUserDefinedClassFromClassName(class_name: str) -> UserDefinedClass:
        """
         
                  Get the NXOpen.UserDefinedObjects.UserDefinedClass object associated with the given class name.
                 
         Returns udo_class ( UserDefinedClass NXOpen.UserD):  The UserDefinedClass instance it may be  if you do not have permission to query this object .
        """
        pass
    def NewUserDefinedClass() -> UserDefinedClass:
        """
         Creats a new UserDefinedClass object 
         Returns udo_class ( UserDefinedClass NXOpen.UserD): .
        """
        pass
import NXOpen
class UserDefinedClass(NXOpen.TransientObject): 
    """ JA interface for the UserDefinedClass object """
    class AllowOwnedObjectSelection(Enum):
        """
        Members Include: 
         |Off|  You do NOT have permission to select objects owned by this class. 
         |On|  You have permission to select objects owned by this class. 

        """
        Off: int
        On: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedClass.AllowOwnedObjectSelection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class AllowQueryClass(Enum):
        """
        Members Include: 
         |Off|  You do NOT have permission to query the class from it's name. 
         |On|  You have permission to query the class from it's name. 

        """
        Off: int
        On: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedClass.AllowQueryClass:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class Selection(Enum):
        """
        Members Include: 
         |Off|  UDO's of this class will NOT be selectable. 
         |On|  UDO's of this class will be selectable. 

        """
        Off: int
        On: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedClass.Selection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AllowOwnedObjectSelectionOption(self) -> UserDefinedClass.AllowOwnedObjectSelection:
        """
        Getter for property: ( UserDefinedClass.AllowOwnedObjectSelection NXOpen.UserD) AllowOwnedObjectSelectionOption
         Returns the allow owned object selection flag.  
           Specifies whether or not you have permission to select objects owned by  NXOpen::UserDefinedObjects::UserDefinedObject 's of this class.   
         
        """
        pass
    @AllowOwnedObjectSelectionOption.setter
    def AllowOwnedObjectSelectionOption(self, allow_owned_object_selection_option: UserDefinedClass.AllowOwnedObjectSelection):
        """
        Setter for property: ( UserDefinedClass.AllowOwnedObjectSelection NXOpen.UserD) AllowOwnedObjectSelectionOption
         Returns the allow owned object selection flag.  
           Specifies whether or not you have permission to select objects owned by  NXOpen::UserDefinedObjects::UserDefinedObject 's of this class.   
         
        """
        pass
    @property
    def AllowQueryClassFromName(self) -> UserDefinedClass.AllowQueryClass:
        """
        Getter for property: ( UserDefinedClass.AllowQueryClass NXOpen.UserD) AllowQueryClassFromName
         Returns the allow query class from name flag.  
           Specifies whether or not you are allowed to query the  NXOpen::UserDefinedObjects::UserDefinedObject  from the class name.   
         
        """
        pass
    @AllowQueryClassFromName.setter
    def AllowQueryClassFromName(self, allow_query_class_from_name: UserDefinedClass.AllowQueryClass):
        """
        Setter for property: ( UserDefinedClass.AllowQueryClass NXOpen.UserD) AllowQueryClassFromName
         Returns the allow query class from name flag.  
           Specifies whether or not you are allowed to query the  NXOpen::UserDefinedObjects::UserDefinedObject  from the class name.   
         
        """
        pass
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
         Returns the class name of the  NXOpen::UserDefinedObjects::UserDefinedClass .  
             
         
        """
        pass
    @property
    def FriendlyName(self) -> str:
        """
        Getter for property: (str) FriendlyName
         Returns the friendly name of the  NXOpen::UserDefinedObjects::UserDefinedClass .  
             
         
        """
        pass
    @property
    def WarnUserFlag(self) -> bool:
        """
        Getter for property: (bool) WarnUserFlag
         Returns the warn user flag.  
           
                Specifies the behavior of warning the user if a  NXOpen::UserDefinedObjects::UserDefinedObject  
                of the given  NXOpen::UserDefinedObjects::UserDefinedClass  
                is found in a part, but the code implementing the methods for the UDO is not loaded.
                The default action is to not warn the user. If the UDO author sets this flag
                to TRUE, all UDO's of this class that are created will be marked so that the
                user will be warned if the UDO methods have not been loaded, but a UDO of the
                class is in the part. This warning will be issued to the listing window,
                when the first object of the given class is retrieved. This warning will
                only be given once per session.
                This flag is set on every UDO object. Therefore for any part, there may be a mixture UDO objects of a given class, 
                some having this flag set to TRUE and some objects having the flag set to FALSE. This is particularly true since all 
                UDO objects created before NX 3.0 will have this flag set to FALSE. If the UDO methods for a class are not loaded, 
                any one UDO with this flag set to TRUE in a part is enough for the warning to be issued to the listing window.
                
                Note that the warning is only issued for UDO's in a part if the part is fully loaded.  
         
        """
        pass
    @WarnUserFlag.setter
    def WarnUserFlag(self, warn_user: bool):
        """
        Setter for property: (bool) WarnUserFlag
         Returns the warn user flag.  
           
                Specifies the behavior of warning the user if a  NXOpen::UserDefinedObjects::UserDefinedObject  
                of the given  NXOpen::UserDefinedObjects::UserDefinedClass  
                is found in a part, but the code implementing the methods for the UDO is not loaded.
                The default action is to not warn the user. If the UDO author sets this flag
                to TRUE, all UDO's of this class that are created will be marked so that the
                user will be warned if the UDO methods have not been loaded, but a UDO of the
                class is in the part. This warning will be issued to the listing window,
                when the first object of the given class is retrieved. This warning will
                only be given once per session.
                This flag is set on every UDO object. Therefore for any part, there may be a mixture UDO objects of a given class, 
                some having this flag set to TRUE and some objects having the flag set to FALSE. This is particularly true since all 
                UDO objects created before NX 3.0 will have this flag set to FALSE. If the UDO methods for a class are not loaded, 
                any one UDO with this flag set to TRUE in a part is enough for the warning to be issued to the listing window.
                
                Note that the warning is only issued for UDO's in a part if the part is fully loaded.  
         
        """
        pass
    DisplayCallback = Callable[[UserDefinedDisplayEvent], None]
    def AddAttentionPointHandler(self, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the attention point callback. 
        """
        pass
    LinkCallback = Callable[[UserDefinedLinkEvent], None]
    def AddDeleteHandler(self, link_event: UserDefinedClass.LinkCallback) -> None:
        """
         Registers the delete callback. 
                This reacts to deletion of the UDO's associated object (when the link type supports delete notification).
        """
        pass
    def AddDisplayHandler(self, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers UDO display callback. 
        """
        pass
    GenericCallback = Callable[[UserDefinedEvent], None]
    def AddEditHandler(self, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the edit callback. 
        """
        pass
    def AddFitHandler(self, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the fit callback.  
        """
        pass
    def AddInformationHandler(self, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the information callback. 
        """
        pass
    def AddOnDeleteHandler(self, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the on delete callback. 
                Note this callback is invoked just before a UDO is deleted or unloaded. 
                Callback implementations should not trigger update or make changes to other objects that need updates.
        """
        pass
    def AddPostLoadHandler(self, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the post load callback. 
                Note user should not try to trigger save from this callback
                Also user should not trigger update or make changes to objects that needs update to be invoked
        """
        pass
    def AddPreSaveHandler(self, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the pre save callback. 
                Note user should not try to trigger save from this callback
                Also user should not trigger update or make changes to objects that needs update to be invoked
        """
        pass
    def AddScreenSizeFitHandler(self, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the screen size fit callback.  The screen size fit callback is called when
                    it is necesary to determine the bounding box of a screen size object (one which
                    remains the same size on the screen independent of the view scale) during a fit
                    computation.  As of NX 8.0 the only geometry types supported for User Defined Objects
                    which are screen size are ScreenStandardText and AbsoluteRotationScreenSizeText.
                    If your User Defined Object does not have any of these objects, then you should not
                    call NXOpen.UserDefinedObjects.UserDefinedClass.AddScreenSizeFitHandler because to do
                    do would incur a performance penalty. 
        """
        pass
    def AddSelectionHandler(self, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the UDO selection callback. 
        """
        pass
    def AddSuppressHandler(self, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the suppress callback. 
                
                Note this callback is not called unless you have a UDO FEATURE.  Also it may not
                get called when the system automatically suppresses the feature during update.
                Also note the user should check the suppression status of the feature in their callback to
                see if the input udo feature is currently getting suppressed or unsuppressed. 
        """
        pass
    def AddUpdateHandler(self, link_event: UserDefinedClass.LinkCallback) -> None:
        """
         Registers the update callback. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object.  After invocation of this
                  method, the object is no longer valid.  
        """
        pass
    def GetIsOccurrenceableFlag(self) -> bool:
        """
         Gets the is occurrenceable flag for this class. 
                Legacy Open C UDO's required a reference UDO to determine Occurrenceability.  Occurrenceability is now set
                on a class by class basis (no reference UDO required).  In the event that you have a legacy UDO you wish to query for occurenceability, 
                you will need set the is occurrenceable flag with the new native language method (which does not require a reference UDO) 
                If you do not set the is occurrenceable flag, and instead use the old open c is occurrenceable callback, you will risk error raising during this
                method because we will automatically pass  in as the reference UDO to the legacy is occurrenceable callback.
         Returns is_occurrenceable (bool):  Specifies whether or not to populate occurrences for NXOpen.UserDefinedObjects.UserDefinedObject's of this class. .
        """
        pass
    def SetIsOccurrenceableFlag(self, is_occurrenceable: bool) -> None:
        """
         Sets the is occurrenceable flag for this class. 
        """
        pass
class UserDefinedDisplayEvent(UserDefinedEvent): 
    """ Implements the Display Event Object for UDO's """
    @property
    def DisplayContext(self) -> UserDefinedObjectDisplayContext:
        """
        Getter for property: ( UserDefinedObjectDisplayContext NXOpen.UserD) DisplayContext
         Returns the display context.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
import NXOpen
class UserDefinedEvent(NXOpen.TransientObject): 
    """ Implements the Event Object for UDO's """
    class Reason(Enum):
        """
        Members Include: 
         |Display|  Display UDO event 
         |Delete|  An associated object was deleted - UDO cleanup event 
         |Update|  Update UDO event 
         |Selection|  Select UDO event 
         |Fit|  Fit display event 
         |AttentionPoint|  Find Attention Point for the UDO event 
         |Info|  Query UDO Information event 
         |Edit|  Edit UDO event 
         |Suppress|  SuppressUnsuppress UDO event 
         |ScreenSizeFit|  Fit operation for screen-size geometry 
         |PreSave|  Pre save UDO event 
         |PostLoad|  Post load UDO event 
         |OnDelete|  On delete UDO event 

        """
        Display: int
        Delete: int
        Update: int
        Selection: int
        Fit: int
        AttentionPoint: int
        Info: int
        Edit: int
        Suppress: int
        ScreenSizeFit: int
        PreSave: int
        PostLoad: int
        OnDelete: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedEvent.Reason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EventReason(self) -> UserDefinedEvent.Reason:
        """
        Getter for property: ( UserDefinedEvent.Reason NXOpen.UserD) EventReason
         Returns the reason we fired this event.  
             
         
        """
        pass
    @property
    def UserDefinedObject(self) -> UserDefinedObject:
        """
        Getter for property: ( UserDefinedObject NXOpen.UserD) UserDefinedObject
         Returns the related UDO.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
import NXOpen
class UserDefinedLinkEvent(UserDefinedEvent): 
    """ Implements the Display Event Object for UDO's """
    @property
    def AssociatedObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) AssociatedObject
         Returns the associated object.  
             
         
        """
        pass
    @property
    def LinkStatus(self) -> int:
        """
        Getter for property: (int) LinkStatus
         Returns the link status.  
             
         
        """
        pass
    @property
    def LinkType(self) -> int:
        """
        Getter for property: (int) LinkType
         Returns the link type.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
import NXOpen
class UserDefinedObjectDisplayContext(NXOpen.TransientObject): 
    """ This class is used to display User Defined Objects """
    class DisplayMode(Enum):
        """
        Members Include: 
         |Wireframe|  Wireframe mode display 
         |Shaded|  Shaded mode display 
         |Studio|  Studio mode display 
         |Analysis|  Analysis mode display 

        """
        Wireframe: int
        Shaded: int
        Studio: int
        Analysis: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.DisplayMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class FacetType(Enum):
        """
        Members Include: 
         |Triangle|  The facet topology is a triangle facet 
         |Polygon|  The facet topology is a polygon facet 
         |Tristrip|  The facet topology is a tristrip facet 

        """
        Triangle: int
        Polygon: int
        Tristrip: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.FacetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PolyMarker(Enum):
        """
        Members Include: 
         |NoMarker|   
         |Point|   
         |Dot|   
         |Asterisk|   
         |Circle|   
         |Poundsign|   
         |X|   
         |Gridpoint|   
         |Square|   
         |TriangleMarker|   
         |Diamond|   
         |Centerline|   
         |ConsFix|   
         |ConsHorizontal|   
         |ConsVertical|   
         |ConsParallel|   
         |ConsPerpendicular|   
         |ConsTangent|   
         |ConsConcentric|   
         |ConsCoincident|   
         |ConsCollinear|   
         |ConsPointOnCurve|   
         |ConsMidpoint|   
         |ConsEqualLength|   
         |ConsEqualRadius|   
         |ConsConstantLength|   
         |ConsConstantAngle|   
         |ConsMirror|   
         |DimRadius|   
         |DimDiameter|   
         |DimParallel|   
         |DimPerpendicular|   
         |ConsSlope|   
         |ConsString|   
         |ConsUniformScaled|   
         |ConsNonUniformScaled|   
         |ConsAssocTrim|   
         |ConsAssocOffset|   
         |Disp2tResSpotWeld|   
         |Disp3tResSpotWeld|   
         |Disp4tResSpotWeld|   
         |Disp2tDcSpotWeld|   
         |Disp3tDcSpotWeld|   
         |Disp4tDcSpotWeld|   
         |Disp2tKpcSpotWeld|   
         |Disp3tKpcSpotWeld|   
         |Disp4tKpcSpotWeld|   
         |Disp2tProcSpotWeld|   
         |Disp3tProcSpotWeld|   
         |Disp4tProcSpotWeld|   
         |ArcSpotWeld|   
         |ClinchWeld|   
         |Anchor|   
         |LeftLeaderConnection|   
         |RightLeaderConnection|   
         |FilledCircle|   
         |FilledSquare|   
         |LargeFilledSquare|   
         |DatumPoint|   
         |SnappingDiamond|   
         |CircleInCircle|   
         |CircleInSquare|   
         |SquareInSquare|   
         |FilledLeftTriangle|   
         |FilledRightTriangle|   
         |FilledUpTriangle|   
         |FilledDownTriangle|   
         |FilledLeftTriangleInCircle|   
         |FilledRightTriangleInCircle|   
         |FilledUpTriangleInCircle|   
         |FilledDownTriangleInCircle|   
         |FilledLeftTriangleInSquare|   
         |FilledRightTriangleInSquare|   
         |FilledUpTriangleInSquare|   
         |FilledDownTriangleInSquare|   
         |RoundedCross|   
         |FilledDiamond|   
         |UpDownTriangles|   
         |LeftRightTriangles|   
         |SmallWheel|   
         |LargeWheel|   
         |HollowCircle|   
         |PreviewPerpendicular|   
         |PreviewHorizontal|   
         |PreviewVertical|   
         |PreviewTangent|   
         |PreviewParallel|   
         |PreviewPointOnCurve|   
         |PreviewCollinear|   
         |Ruler|   
         |Protractor|   
         |SketchNotebook|   
         |ArcEndPoint|   
         |Disp2PtArcMarker|   
         |BigAsterisk|   
         |LineInCircle|   
         |PlusInCircle|   
         |CenterOfRotation|   
         |PreviewX|   
         |PreviewY|   
         |PreviewZ|   
         |Disp2tGeneralSpotWeld|   
         |Disp3tGeneralSpotWeld|   
         |Disp4tGeneralSpotWeld|   
         |Disp2tVitalSpotWeld|   
         |Disp3tVitalSpotWeld|   
         |Disp4tVitalSpotWeld|   
         |Disp2tImportantSpotWeld|   
         |Disp3tImportantSpotWeld|   
         |Disp4tImportantSpotWeld|   
         |Disp2tSemipanelSpotWeld|   
         |Disp3tSemipanelSpotWeld|   
         |Disp4tSemipanelSpotWeld|   
         |InvalidMarker|   

        """
        NoMarker: int
        Point: int
        Dot: int
        Asterisk: int
        Circle: int
        Poundsign: int
        X: int
        Gridpoint: int
        Square: int
        TriangleMarker: int
        Diamond: int
        Centerline: int
        ConsFix: int
        ConsHorizontal: int
        ConsVertical: int
        ConsParallel: int
        ConsPerpendicular: int
        ConsTangent: int
        ConsConcentric: int
        ConsCoincident: int
        ConsCollinear: int
        ConsPointOnCurve: int
        ConsMidpoint: int
        ConsEqualLength: int
        ConsEqualRadius: int
        ConsConstantLength: int
        ConsConstantAngle: int
        ConsMirror: int
        DimRadius: int
        DimDiameter: int
        DimParallel: int
        DimPerpendicular: int
        ConsSlope: int
        ConsString: int
        ConsUniformScaled: int
        ConsNonUniformScaled: int
        ConsAssocTrim: int
        ConsAssocOffset: int
        Disp2tResSpotWeld: int
        Disp3tResSpotWeld: int
        Disp4tResSpotWeld: int
        Disp2tDcSpotWeld: int
        Disp3tDcSpotWeld: int
        Disp4tDcSpotWeld: int
        Disp2tKpcSpotWeld: int
        Disp3tKpcSpotWeld: int
        Disp4tKpcSpotWeld: int
        Disp2tProcSpotWeld: int
        Disp3tProcSpotWeld: int
        Disp4tProcSpotWeld: int
        ArcSpotWeld: int
        ClinchWeld: int
        Anchor: int
        LeftLeaderConnection: int
        RightLeaderConnection: int
        FilledCircle: int
        FilledSquare: int
        LargeFilledSquare: int
        DatumPoint: int
        SnappingDiamond: int
        CircleInCircle: int
        CircleInSquare: int
        SquareInSquare: int
        FilledLeftTriangle: int
        FilledRightTriangle: int
        FilledUpTriangle: int
        FilledDownTriangle: int
        FilledLeftTriangleInCircle: int
        FilledRightTriangleInCircle: int
        FilledUpTriangleInCircle: int
        FilledDownTriangleInCircle: int
        FilledLeftTriangleInSquare: int
        FilledRightTriangleInSquare: int
        FilledUpTriangleInSquare: int
        FilledDownTriangleInSquare: int
        RoundedCross: int
        FilledDiamond: int
        UpDownTriangles: int
        LeftRightTriangles: int
        SmallWheel: int
        LargeWheel: int
        HollowCircle: int
        PreviewPerpendicular: int
        PreviewHorizontal: int
        PreviewVertical: int
        PreviewTangent: int
        PreviewParallel: int
        PreviewPointOnCurve: int
        PreviewCollinear: int
        Ruler: int
        Protractor: int
        SketchNotebook: int
        ArcEndPoint: int
        Disp2PtArcMarker: int
        BigAsterisk: int
        LineInCircle: int
        PlusInCircle: int
        CenterOfRotation: int
        PreviewX: int
        PreviewY: int
        PreviewZ: int
        Disp2tGeneralSpotWeld: int
        Disp3tGeneralSpotWeld: int
        Disp4tGeneralSpotWeld: int
        Disp2tVitalSpotWeld: int
        Disp3tVitalSpotWeld: int
        Disp4tVitalSpotWeld: int
        Disp2tImportantSpotWeld: int
        Disp3tImportantSpotWeld: int
        Disp4tImportantSpotWeld: int
        Disp2tSemipanelSpotWeld: int
        Disp3tSemipanelSpotWeld: int
        Disp4tSemipanelSpotWeld: int
        InvalidMarker: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.PolyMarker:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class StandardTextRef(Enum):
        """
        Members Include: 
         |SystemDefault|  Display the text using the system
                                                                                     default reference point position 
         |BaselineStart|  Display the text starting on the
                                                                                     baseline, at the left end of the
                                                                                     text box for left-to-right text,
                                                                                     or at the right end of the text box
                                                                                     for right-to-left text 
         |BaselineCenter|  Display the text with the given position
                                                                                  in the horizontal center of the text box
                                                                                  at the baseline 
         |BaselineEnd|  Display the text starting on the baseline,
                                                                                at the right end of the text box
                                                                                for left-to-right text,
                                                                                or at the left end of the text box
                                                                                for right-to-left text 
         |TopLeft|  Display the text with the given position
                                                                                in the top left of the text box 
         |TopCenter|  Display the text with the given position
                                                                                in the top center of the text box 
         |TopRight|  Display the text with the given position
                                                                                in the top right of the text box 
         |MiddleLeft|  Display the text with the given position
                                                                                in the middle left of the text box 
         |MiddleCenter|  Display the text with the given position
                                                                                in middle center of text box 
         |MiddleRight|  Display the text with the given position
                                                                                in middle right of text box 
         |BottomLeft|  Display the text with the given position
                                                                                in bottom left of text box 
         |BottomCenter|  Display the text with the given position
                                                                                in bottom center of text box 
         |BottomRight|  Display the text with the given position
                                                                                in bottom right of text box 

        """
        SystemDefault: int
        BaselineStart: int
        BaselineCenter: int
        BaselineEnd: int
        TopLeft: int
        TopCenter: int
        TopRight: int
        MiddleLeft: int
        MiddleCenter: int
        MiddleRight: int
        BottomLeft: int
        BottomCenter: int
        BottomRight: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.StandardTextRef:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TextRef(Enum):
        """
        Members Include: 
         |SystemDefault|  Display the text using the system default 
         |TopLeft|  Display the text with the given position in the top left of the text box 
         |TopCenter|  Display the text with the given position in the top center of the text box 
         |TopRight|  Display the text with the given position in the top right of the text box 
         |MiddleLeft|  Display the text with the given position in the middle left of the text box 
         |MiddleCenter|  Display the text with the given position in middle center of text box 
         |MiddleRight|  Display the text with the given position in middle right of text box 
         |BottomLeft|  Display the text with the given position in bottom left of text box 
         |BottomCenter|  Display the text with the given position in bottom center of text box 
         |BottomRight|  Display the text with the given position in bottom right of text box 

        """
        SystemDefault: int
        TopLeft: int
        TopCenter: int
        TopRight: int
        MiddleLeft: int
        MiddleCenter: int
        MiddleRight: int
        BottomLeft: int
        BottomCenter: int
        BottomRight: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.TextRef:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TextSize(Enum):
        """
        Members Include: 
         |Small| 
         |Normal| 
         |Medium| 
         |Large| 
         |NumSizes| 

        """
        Small: int
        Normal: int
        Medium: int
        Large: int
        NumSizes: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.TextSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewMode(Enum):
        """
        Members Include: 
         |NotShaded|  The view is not shaded 
         |PartiallyShaded|  The view is partially shaded 
         |FullyShaded|  The view is fully shaded 
         |AnalysisShaded|  The view is analysis shaded 
         |StudioShaded|  The view is studio shaded 

        """
        NotShaded: int
        PartiallyShaded: int
        FullyShaded: int
        AnalysisShaded: int
        StudioShaded: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.ViewMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def DisplayAbsoluteRotationScreenSizeStandardText(self, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, string: str, text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a single line "Standard Text" string using "Absolute Rotation and Screen
                    Size Geometry" for a UserDefinedObject. A "Standard Text"
                    string uses one of the fonts available from the operating system.
                    "Absolute Rotation and Screen Size Geometry" means the text appears the
                    same physical sized on the screen regardless of the view scale (like
                    "Screen Geometry"), the text remains front-facing and approximately
                    upright (similar to "Screen Geometry"), but the orientation of the text
                    changes as the user rotates the view (like "Absolute Geometry").
                    The text will be displayed on the XY plane of the absolute coordinate system.
                    This method is not supported for 2D output such as CGM. 
        """
        pass
    def DisplayAbsoluteStandardText(self, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, string: str, glyph_width: float, glyph_height: float) -> None:
        """
         Displays a single line "Standard Text" string using "Absolute Geometry" for a
                    UserDefinedObject. A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Absolute Geometry"
                    means that the text scales and rotates with the view, so it appears larger
                    when you zoom in and smaller when you zoom out.  This is the type of text
                    normally used by NX Drafting.   Note that the text will be displayed on
                    the Absolute XY plane. 
        """
        pass
    def DisplayArc(self, center: NXOpen.Point3d, original: NXOpen.Matrix3x3, radius: float, start_angle: float, end_angle: float) -> None:
        """
         Displays an arc for a UserDefinedObject.  
                    The arc will be created in a plane whose normal is the Z axis 
                    of the orientation matrix  
                     (matrix[0-2] is the X axis of the orientation matrix,  
                      matrix[3-5] is the Y axis of the orientation matrix, and
                      matrix[6-8] is the Z axis of the orientation matrix.)
                    The start and end angles are measured relative to
                    the X and Y axis of this orientation matrix. 
        """
        pass
    def DisplayCircle(self, center: NXOpen.Point3d, original: NXOpen.Matrix3x3, radius: float, filled: bool) -> None:
        """
         Displays a circle for a UserDefinedObject.  
                    The circle will be created in a plane which is normal to
                    the Z axis of the orientation matrix.  
                     (matrix[0-2] is the X axis of the orientation matrix,  
                      matrix[3-5] is the Y axis of the orientation matrix, and
                      matrix[6-8] is the Z axis of the orientation matrix.) 
        """
        pass
    def DisplayFacets(self, num_vertices: int, num_facets: int, vertices: List[NXOpen.Point3d], normals: List[NXOpen.Vector3d], type_of_facet: UserDefinedObjectDisplayContext.FacetType) -> None:
        """
         Displays a series of facets for a UserDefinedObject. 
        """
        pass
    def DisplayMultiLineAbsoluteRotationScreenSizeStandardText(self, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, strings: List[str], text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a multi-line "Standard Text" string using "Absolute Rotation and Screen
                    Size Geometry" for a UserDefinedObject. A "Standard Text"
                    string uses one of the fonts available from the operating system.
                    "Absolute Rotation and Screen Size Geometry" means the text appears the
                    same physical sized on the screen regardless of the view scale (like
                    "Screen Geometry"), the text remains front-facing and approximately
                    upright (similar to "Screen Geometry"), but the orientation of the text
                    changes as the user rotates the view (like "Absolute Geometry").
                    The text will be displayed on the XY plane of the absolute coordinate system.
                    This method is not supported for 2D output such as CGM. 
        """
        pass
    def DisplayMultiLineAbsoluteStandardText(self, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, strings: List[str], glyph_width: float, glyph_height: float) -> None:
        """
         Displays a multi-line "Standard Text" string using "Absolute Geometry" for a
                    UserDefinedObject. A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Absolute Geometry"
                    means that the text scales and rotates with the view, so it appears larger
                    when you zoom in and smaller when you zoom out.  This is the type of text
                    normally used by NX Drafting.   Note that the text will be displayed on
                    the Absolute XY plane. 
        """
        pass
    def DisplayMultiLineScreenStandardText(self, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, strings: List[str], text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a multi-line "Standard Text" string using "Screen Geometry" for a
                    UserDefinedObject. A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Screen Geometry" means
                    that the text remains parallel to the screen and appears the same physical
                    size on the screen regardless of the view scale. This method is not
                    supported for 2D output such as CGM.  Note that the text will be displayed on
                    the Absolute XY plane.
        """
        pass
    def DisplayPoints(self, points: List[NXOpen.Point3d], marker_type: UserDefinedObjectDisplayContext.PolyMarker) -> None:
        """
         Displays a series of points for a UserDefinedObject. 
        """
        pass
    def DisplayPolygon(self, points: List[NXOpen.Point3d], filled: bool) -> None:
        """
         Displays a polygon (a closed set of line segements) for a UserDefinedObject.  
                    The line segments are defined by an array of points. 
        """
        pass
    def DisplayPolyline(self, points: List[NXOpen.Point3d]) -> None:
        """
         Displays a polyline (a connected set of line segements) for a UserDefinedObject.  
                    The line segments are defined by an array of points.
        """
        pass
    def DisplayScreenStandardText(self, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, string: str, text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a single line "Standard Text" string using "Screen Geometry" for a
                    UserDefinedObject. A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Screen Geometry" means
                    that the text remains parallel to the screen and appears the same physical
                    size on the screen regardless of the view scale. This method is not
                    supported for 2D output such as CGM.  Note that the text will be displayed on
                    the Absolute XY plane.
        """
        pass
    def DisplayText(self, text: str, text_coordinates: NXOpen.Point3d, reference_point: UserDefinedObjectDisplayContext.TextRef) -> None:
        """
         Displays a text string using an NX text font for a
                    UserDefinedObject. 
        """
        pass
    def DisplayUnicodeMarker(self, unicode_char: str, font_index: int, font_style: str, marker_coordinates: NXOpen.Point3d, marker_size: float) -> None:
        """
         Displays a single character in the given font and style centered at the given position.
                    The character will always be displayed parallel to the screen.
                
        """
        pass
    PrimitiveRenderCallback = Callable[[UserDefinedObjectGraphicsContext, UserDefinedObject], None]
    def DisplayUserDefinedPrimitive(self, displayMode: UserDefinedObjectDisplayContext.DisplayMode, displayCallbackFn: UserDefinedObjectDisplayContext.PrimitiveRenderCallback) -> None:
        """
         Displays a user defined primitive in a specified display mode. A user defined primitive defined with
                a unique handle and display callback function. 
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object.  After invocation of this
                  method, the object is no longer valid.  
        """
        pass
    def GetViewMode(self) -> Tuple[NXOpen.View, bool, UserDefinedObjectDisplayContext.ViewMode, bool, NXOpen.Point3d, bool]:
        """
         Get information about the current view mode and display context in which geometry is displayed. 
                
         Returns A tuple consisting of (view, is_view_mode_valid, view_mode, is_atten_pt_valid, attention_point, is_drawing_view_open). 
         - view is:  NXOpen.View. View being displayed .
         - is_view_mode_valid is: bool. True if the view mode was returned and False if no information was available .
         - view_mode is:  UserDefinedObjectDisplayContext.ViewMode NXOpen.UserD. View mode describes the views shading
                                                                                and face analysis mode - see enum values for more details .
         - is_atten_pt_valid is: bool. True if the attention point was returned and
                                                                                False if no information was available .
         - attention_point is:  NXOpen.Point3d. The attention point of the geometry just displayed .
         - is_drawing_view_open is: bool. Is the drawing view open for display?
                                                                                If true then geometry may be added to
                                                                                the drawing. If false another view
                                                                                which is not the drawing is open .

        """
        pass
import NXOpen
class UserDefinedObjectGraphicsContext(NXOpen.TransientObject): 
    """ This class is used to render User Defined Objects """
    class ColorMode(Enum):
        """
        Members Include: 
         |Regular|  Regular 
         |Highlight|  Highlight 
         |SuperHighlight|  Super highlight 

        """
        Regular: int
        Highlight: int
        SuperHighlight: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectGraphicsContext.ColorMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RenderingPass(Enum):
        """
        Members Include: 
         |Opaque|  Opaque 
         |BackFacingTranslucency|  BackFacingTranslucency 
         |FrontFacingTranslucency|  FrontFacingTranslucency 
         |DepthBufferTranslucency|  DepthBufferTranslucency 
         |StencilBufferCapping|  StencilBufferCapping 

        """
        Opaque: int
        BackFacingTranslucency: int
        FrontFacingTranslucency: int
        DepthBufferTranslucency: int
        StencilBufferCapping: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectGraphicsContext.RenderingPass:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorAlphaValue(self) -> float:
        """
        Getter for property: (float) ColorAlphaValue
         Returns the alpha component of color.  
           Its range is [0, 1] with 0.0 being opaque, and 1.0 being totally transparent.  
         
        """
        pass
    @property
    def ColorModeType(self) -> UserDefinedObjectGraphicsContext.ColorMode:
        """
        Getter for property: ( UserDefinedObjectGraphicsContext.ColorMode NXOpen.UserD) ColorModeType
         Returns the color mode of graphics context.  
             
         
        """
        pass
    @property
    def ColorValue(self) -> NXOpen.NXColor.Rgb:
        """
        Getter for property: ( NXOpen.NXColor.Rgb) ColorValue
         Returns the RGB color value.  
           RGB values are between 0.0 and 1.0.  
         
        """
        pass
    @property
    def RenderingPassType(self) -> UserDefinedObjectGraphicsContext.RenderingPass:
        """
        Getter for property: ( UserDefinedObjectGraphicsContext.RenderingPass NXOpen.UserD) RenderingPassType
         Returns the rendering pass of graphics context.  
             
         
        """
        pass
    @property
    def ViewContext(self) -> UserDefinedObjectGraphicsViewContext:
        """
        Getter for property: ( UserDefinedObjectGraphicsViewContext NXOpen.UserD) ViewContext
         Returns the rendering graphics view context.  
             
         
        """
        pass
    @property
    def WindowContext(self) -> UserDefinedObjectGraphicsWindowContext:
        """
        Getter for property: ( UserDefinedObjectGraphicsWindowContext NXOpen.UserD) WindowContext
         Returns the rendering graphics window context.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object.  After invocation of this
                    method, the object is no longer valid.  
        """
        pass
import NXOpen
class UserDefinedObjectGraphicsViewContext(NXOpen.TransientObject): 
    """ This class is used to render User Defined Objects """
    @property
    def BackClippingDistance(self) -> float:
        """
        Getter for property: (float) BackClippingDistance
         Returns the back clipping distance of view.  
             
         
        """
        pass
    @property
    def BackClippingEnabled(self) -> bool:
        """
        Getter for property: (bool) BackClippingEnabled
         Returns the back clipping enabled state of view.  
             
         
        """
        pass
    @property
    def FrontClippingDistance(self) -> float:
        """
        Getter for property: (float) FrontClippingDistance
         Returns the front clipping distance of view.  
             
         
        """
        pass
    @property
    def FrontClippingEnabled(self) -> bool:
        """
        Getter for property: (bool) FrontClippingEnabled
         Returns the front clipping enabled state of view.  
             
         
        """
        pass
    @property
    def ModelMatrix(self) -> NXOpen.Matrix4x4:
        """
        Getter for property: ( NXOpen.Matrix4x4) ModelMatrix
         Returns the matrix of model.  
             
         
        """
        pass
    @property
    def ProjectionMatrix(self) -> NXOpen.Matrix4x4:
        """
        Getter for property: ( NXOpen.Matrix4x4) ProjectionMatrix
         Returns the projection matrix of view.  
             
         
        """
        pass
    @property
    def ViewMatrix(self) -> NXOpen.Matrix4x4:
        """
        Getter for property: ( NXOpen.Matrix4x4) ViewMatrix
         Returns the matrix of view.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object.  After invocation of this
                    method, the object is no longer valid.  
        """
        pass
    def GetBounds(self) -> Tuple[NXOpen.Vector2d, NXOpen.Vector2d]:
        """
         Returns the LL(lower-left corner), UR(upper-right) corner 
                    of view bounds in VDCs(Virtual Device Coordinates). 
         Returns A tuple consisting of (maxBounds, minBounds). 
         - maxBounds is:  NXOpen.Vector2d. max of view bounds .
         - minBounds is:  NXOpen.Vector2d. min of view bounds .

        """
        pass
    def GetWindowCoordinates(self) -> Tuple[NXOpen.Vector2d, NXOpen.Vector2d]:
        """
         Returns LL(lower-left corner), UR(upper-right) in view coordinates. 
         Returns A tuple consisting of (maxWindowCoordinates, minWindowCoordinates). 
         - maxWindowCoordinates is:  NXOpen.Vector2d. max of view coordinates .
         - minWindowCoordinates is:  NXOpen.Vector2d. min of view coordinates .

        """
        pass
import NXOpen
class UserDefinedObjectGraphicsWindowContext(NXOpen.TransientObject): 
    """ This class is used to render User Defined Objects """
    @property
    def Height(self) -> int:
        """
        Getter for property: (int) Height
         Returns the height of window.  
             
         
        """
        pass
    @property
    def Width(self) -> int:
        """
        Getter for property: (int) Width
         Returns the width of window.  
             
         
        """
        pass
    @property
    def X(self) -> int:
        """
        Getter for property: (int) X
         Returns the x location of window.  
             
         
        """
        pass
    @property
    def Y(self) -> int:
        """
        Getter for property: (int) Y
         Returns the y location of window.  
             
         
        """
        pass
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object.  After invocation of this
                    method, the object is no longer valid.  
        """
        pass
import NXOpen
class UserDefinedObjectManager(NXOpen.Object): 
    """ This class creates and manages UserDefinedObjects """
    class LinkedUdoDefinition:
        """
         Used to define a link to a UserDefinedObject 
         UserDefinedObjectManagerLinkedUdoDefinition_Struct NXOpen.UserD is an alias for  UserDefinedObjectManager.LinkedUdoDefinition NXOpen.UserD.
        """
        @property
        def LinkType(self) -> UserDefinedObject.LinkType:
            """
            Getter for property LinkType
            """
            pass
        @LinkType.setter
        def LinkType(self, value: UserDefinedObject.LinkType):
            """
            Getter for property LinkTypeSetter for property LinkType
            """
            pass
        @property
        def AssociatedUdo(self) -> UserDefinedObject:
            """
            Getter for property AssociatedUdo
            """
            pass
        @AssociatedUdo.setter
        def AssociatedUdo(self, value: UserDefinedObject):
            """
            Getter for property AssociatedUdoSetter for property AssociatedUdo
            """
            pass
        @property
        def Status(self) -> UserDefinedObject.LinkStatus:
            """
            Getter for property Status
            """
            pass
        @Status.setter
        def Status(self, value: UserDefinedObject.LinkStatus):
            """
            Getter for property StatusSetter for property Status
            """
            pass
    def CreateUserDefinedObject(self, udo_class: UserDefinedClass) -> UserDefinedObject:
        """
         
                  Constructs a new NXOpen.Features.UserDefinedObjectFeature.
                 
         Returns udo ( UserDefinedObject NXOpen.UserD):  The new UserDefinedObject instance .
        """
        pass
    def GetLinksToObject(self, link_object: NXOpen.TaggedObject) -> List[UserDefinedObjectManager.LinkedUdoDefinition]:
        """
         Queries an NX Object to find all UserDefinedObjects.UserDefinedObject's that are linked to the given NXObject (note this will not find owning udos) 
         Returns links ( UserDefinedObjectManager.LinkedUdoDefinition List[NXOpen.Use):  The link definitions from UDO's to the NXObject .
        """
        pass
    def GetOwningUserDefinedObject(self, link_object: NXOpen.TaggedObject) -> UserDefinedObject:
        """
         Queries an NX Object to find the UserDefinedObjects.UserDefinedObject that owns the given NXObject (note this will return null for the owning udo if the object is not owned) 
         Returns owning_udo ( UserDefinedObject NXOpen.UserD):  The UDO which owns the NXObject .
        """
        pass
    def GetUdosOfClass(self, udo_class: UserDefinedClass) -> List[UserDefinedObject]:
        """
         Finds all UserDefinedObjects.UserDefinedObject instances that use the given NXOpen.UserDefinedObjects.UserDefinedClass. 
         Returns udos ( UserDefinedObject List[NXOpen.Use):  User Defined Objects of the given class .
        """
        pass
    def IsObjectLinkable(self, link_object: NXOpen.TaggedObject, link_type: UserDefinedObject.LinkType) -> bool:
        """
         Queries an NX Object to see if it can be linked to a UserDefinedObjects.UserDefinedObject via the given link type 
         Returns linkable (bool):  TRUE - This object can be linked to a UDO with the given link type, FALSE - this object can not be NOT linked to a UDO with the given link type .
        """
        pass
    def IsObjectLinkedToUserDefinedObject(self, link_object: NXOpen.TaggedObject) -> bool:
        """
         Queries an NX Object to see if it is linked to a UserDefinedObjects.UserDefinedObject (note this will not
                tell you if the object is owned by a UDO with an owning link) 
         Returns is_linked (bool):  TRUE - This object is linked to a UDO, FALSE - this object is NOT linked to a UDO .
        """
        pass
    def IsObjectOwnedByUserDefinedObject(self, link_object: NXOpen.TaggedObject) -> bool:
        """
         Queries an NX Object to see if it is owned by a UserDefinedObjects.UserDefinedObject 
         Returns is_linked (bool):  TRUE - This object is owned by a UDO, FALSE - this object is NOT owned by a UDO .
        """
        pass
import NXOpen
import NXOpen.Features
class UserDefinedObject(NXOpen.DisplayableObject): 
    """ JA interface for the UserDefinedObject object """
    class LinkStatus(Enum):
        """
        Members Include: 
         |UpToDate|  The associated object is up to date. 
         |OutOfDate|  The associated object is out of date. 

        """
        UpToDate: int
        OutOfDate: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObject.LinkStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinkType(Enum):
        """
        Members Include: 
         |Owning|  The object is owned by the UDO 
         |Type1|  If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. 
                                                        If the UDO is updated the associated object is unaffected. If the associated object is deleted the UDO is also deleted.  
                                                        If the associated object is updated the UDO is updated. 
         |Type2|  If the UDO is deleted the link between the UDO and the associated object is removed and the object is deleted. 
                                                        If the UDO is updated the associated NX object is unaffected. If the associated object is deleted, it is left 
                                                        in the data model in a condemned state and remains attached to the UDO. If the associated object is updated 
                                                        the UDO is unaffected. 
         |Type3|  If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. 
                                                        If the UDO is updated the associated object is unaffected. If the associated object is deleted the link to the 
                                                        UDO is removed and the UDO is updated. If the associated object is updated the UDO is updated 
         |Type4|  If the UDO is deleted the link between the UDO and the associated object is removed and the object is unaffected. 
                                                        If the UDO is updated the associated object is unaffected. If the associated object is deleted the link to the 
                                                        UDO is removed and the UDO is unaffected. If the associated object is updated the UDO is unaffected. 

        """
        Owning: int
        Type1: int
        Type2: int
        Type3: int
        Type4: int
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObject.LinkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class LinkDefinition:
        """
         Contains the linked object and it's status along with the type of link.
         UserDefinedObjectLinkDefinition_Struct NXOpen.UserD is an alias for  UserDefinedObject.LinkDefinition NXOpen.UserD.
        """
        @property
        def AssociatedObject(self) -> NXOpen.TaggedObject:
            """
            Getter for property AssociatedObject
            linked object

            """
            pass
        @AssociatedObject.setter
        def AssociatedObject(self, value: NXOpen.TaggedObject):
            """
            Getter for property AssociatedObject
            linked object
            Setter for property AssociatedObject
            linked object

            """
            pass
        @property
        def Status(self) -> UserDefinedObject.LinkStatus:
            """
            Getter for property Status
            status of the linked object

            """
            pass
        @Status.setter
        def Status(self, value: UserDefinedObject.LinkStatus):
            """
            Getter for property Status
            status of the linked object
            Setter for property Status
            status of the linked object

            """
            pass
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
         Returns the class name of this UDO   
            
         
        """
        pass
    @property
    def UserDefinedClass(self) -> UserDefinedClass:
        """
        Getter for property: ( UserDefinedClass NXOpen.UserD) UserDefinedClass
         Returns the  NXOpen::UserDefinedObjects::UserDefinedClass  for this UDO   
            
         
        """
        pass
    @UserDefinedClass.setter
    def UserDefinedClass(self, user_defined_class: UserDefinedClass):
        """
        Setter for property: ( UserDefinedClass NXOpen.UserD) UserDefinedClass
         Returns the  NXOpen::UserDefinedObjects::UserDefinedClass  for this UDO   
            
         
        """
        pass
    def ClearUserDefinedObjectStatus(self) -> None:
        """
         Clears the out of data indicator (status) of this UDO 
        """
        pass
    @overload
    def GetAreas(self) -> List[float]:
        """
         Gets all of the areas stored with this UDO 
         Returns areas (List[float]):  Array of areas stored with this UDO .
        """
        pass
    @overload
    def GetAreas(self, offset: int, length: int) -> List[float]:
        """
         Gets the areas stored in the specified range with this UDO 
         Returns areas (List[float]):  Array of areas stored within the specified  
                                                                range of the area array for this UDO .
        """
        pass
    @overload
    def GetDoubles(self) -> List[float]:
        """
         Gets all of the doubles stored with this UDO 
         Returns doubles (List[float]):  Array of doubles stored with this UDO .
        """
        pass
    @overload
    def GetDoubles(self, offset: int, length: int) -> List[float]:
        """
         Gets the doubles stored in the specified range with this UDO 
         Returns doubles (List[float]):  Array of doubles stored within the specified  
                                                                range of the double array for this UDO .
        """
        pass
    @overload
    def GetIntegers(self) -> List[int]:
        """
         Gets all of the integers stored with this UDO 
         Returns integers (List[int]):  Array of integers stored with this UDO .
        """
        pass
    @overload
    def GetIntegers(self, offset: int, length: int) -> List[int]:
        """
         Gets the integers stored in the specified range with this UDO 
         Returns integers (List[int]):  Array of integers stored within the specified  
                                                                range of the integer array for this UDO .
        """
        pass
    @overload
    def GetLengths(self) -> List[float]:
        """
         Gets all of the lengths stored with this UDO 
         Returns lengths (List[float]):  Array of lengths stored with this UDO .
        """
        pass
    @overload
    def GetLengths(self, offset: int, length: int) -> List[float]:
        """
         Gets the lengths stored in the specified range with this UDO 
         Returns lengths (List[float]):  Array of lengths stored within the specified  
                                                                range of the length array for this UDO .
        """
        pass
    @overload
    def GetLinks(self, link_type: UserDefinedObject.LinkType) -> List[UserDefinedObject.LinkDefinition]:
        """
         Gets all links with the given link type that are stored with this UDO 
         Returns links ( UserDefinedObject.LinkDefinition List[NXOpen.Use):  Array of links (with the given link type) stored with this UDO .
        """
        pass
    @overload
    def GetLinks(self, link_type: UserDefinedObject.LinkType, offset: int, length: int) -> List[UserDefinedObject.LinkDefinition]:
        """
         Gets the links with the given link type that are stored in the specified range with this UDO 
         Returns links ( UserDefinedObject.LinkDefinition List[NXOpen.Use):  Array of links stored within the specified  
                                                                range of the link type's link array for this UDO .
        """
        pass
    @overload
    def GetStrings(self) -> List[str]:
        """
         Gets all of the strings stored with this UDO 
         Returns strings (List[str]):  Array of strings stored with this UDO .
        """
        pass
    @overload
    def GetStrings(self, offset: int, length: int) -> List[str]:
        """
         Gets the strings stored in the specified range with this UDO 
         Returns strings (List[str]):  Array of strings stored within the specified  
                                                                range of the string array for this UDO .
        """
        pass
    def GetUserDefinedObjectFeature(self) -> NXOpen.Features.UserDefinedObjectFeature:
        """
         Gets the NXOpen.Features.UserDefinedObjectFeature associated with this UDO, if there isn't an associated feature,  is returned 
         Returns udo_feature ( NXOpen.Features.UserDefinedObjectFeature):  The UserDefinedObjectFeature associated this UDO .
        """
        pass
    def GetUserDefinedObjectStatus(self) -> int:
        """
         Gets the out of date indicator (status) of this UDO 
         Returns status (int):  The status of this UDO 
                    0 - The UDO is up to date
                    1 - Out of date due to addition or deletion of links to the UDO
                    2 - Out of date due to update being performed on an associated (linked) object in the absence of a UDO Method
                    3 - Out of date due to addition or deletion of links to the UDO AND update being performed on an Associated (linked) object in the absence of a UDO Method 
                    4 - Out of date due to deletion of associated (linked) objects in the absence of a UDO method 
                    5 - Out of date due to addition or deletion of links to the UDO AND deletion of associated (linked) objects in the absence of a UDO method 
                    6 - Out of date due to update being performed on an associated (linked) object in the absence of a UDO Method AND deletion of associated (linked) objects in the absence of a UDO method 
                    7 - Out of date due to addition or deletion of links to the UDO AND update being performed on an Associated (linked) object in the absence of a UDO Method AND deletion of associated (linked) objects in the absence of a UDO method .
        """
        pass
    @overload
    def GetVolumes(self) -> List[float]:
        """
         Gets all of the volumes stored with this UDO 
         Returns volumes (List[float]):  Array of volumes stored with this UDO .
        """
        pass
    @overload
    def GetVolumes(self, offset: int, length: int) -> List[float]:
        """
         Gets the volumes stored in the specified range with this UDO 
         Returns volumes (List[float]):  Array of volumes stored within the specified  
                                                                range of the volume array for this UDO .
        """
        pass
    def PopAreas(self, num_areas: int) -> List[float]:
        """
         Removes the areas stored at the end of the area array for this UDO, 
                    and returns them in an array 
         Returns areas (List[float]):  Array of areas that have been 
                                                                  removed from this UDO .
        """
        pass
    def PopDoubles(self, num_doubles: int) -> List[float]:
        """
         Removes the doubles stored at the end of the double array for this UDO, 
                    and returns them in an array 
         Returns doubles (List[float]):  Array of doubles that have been 
                                                                  removed from this UDO .
        """
        pass
    def PopIntegers(self, num_integers: int) -> List[int]:
        """
         Removes the integers stored at the end of the integer array for this UDO, 
                    and returns them in an array 
         Returns integers (List[int]):  Array of integers that have been 
                                                                  removed from this UDO .
        """
        pass
    def PopLengths(self, num_lengths: int) -> List[float]:
        """
         Removes the lengths stored at the end of the length array for this UDO, 
                    and returns them in an array 
         Returns lengths (List[float]):  Array of lengths that have been 
                                                                  removed from this UDO .
        """
        pass
    def PopLinks(self, link_type: UserDefinedObject.LinkType, num_links: int) -> List[UserDefinedObject.LinkDefinition]:
        """
         Removes the links stored at the end of the given link type's link array for this UDO, 
                    and returns them in an array 
         Returns links ( UserDefinedObject.LinkDefinition List[NXOpen.Use):  Array of links (with the given link type) that have been 
                                                                  removed from this UDO .
        """
        pass
    def PopStrings(self, num_strings: int) -> List[str]:
        """
         Removes the strings stored at the end of the string array for this UDO, 
                    and returns them in an array 
         Returns strings (List[str]):  Array of strings that have been 
                                                                  removed from this UDO .
        """
        pass
    def PopVolumes(self, num_volumes: int) -> List[float]:
        """
         Removes the volumes stored at the end of the volume array for this UDO, 
                    and returns them in an array 
         Returns volumes (List[float]):  Array of volumes that have been 
                                                                  removed from this UDO .
        """
        pass
    def PushAreas(self, areas: List[float]) -> None:
        """
         Add the specified areas to the end of the area array for this UDO 
        """
        pass
    def PushDoubles(self, doubles: List[float]) -> None:
        """
         Add the specified doubles to the end of the double array for this UDO 
        """
        pass
    def PushIntegers(self, integers: List[int]) -> None:
        """
         Add the specified integers to the end of the integer array for this UDO 
        """
        pass
    def PushLengths(self, lengths: List[float]) -> None:
        """
         Add the specified lengths to the end of the length array for this UDO 
        """
        pass
    def PushLinks(self, link_type: UserDefinedObject.LinkType, links: List[UserDefinedObject.LinkDefinition]) -> None:
        """
         Add the specified links to the end of the given link type's link array for this UDO 
        """
        pass
    def PushStrings(self, strings: List[str]) -> None:
        """
         Add the specified strings to the end of the string array for this UDO 
        """
        pass
    def PushVolumes(self, volumes: List[float]) -> None:
        """
         Add the specified volumes to the end of the volume array for this UDO 
        """
        pass
    @overload
    def SetAreas(self, areas: List[float]) -> None:
        """
         Sets all of the areas stored with this UDO 
        """
        pass
    @overload
    def SetAreas(self, offset: int, length: int, areas: List[float]) -> None:
        """
         Replaces the areas stored with this UDO in the specified range with a new array of areas 
        """
        pass
    @overload
    def SetDoubles(self, doubles: List[float]) -> None:
        """
         Sets all of the doubles stored with this UDO 
        """
        pass
    @overload
    def SetDoubles(self, offset: int, length: int, doubles: List[float]) -> None:
        """
         Replaces the doubles stored with this UDO in the specified range with a new array of doubles 
        """
        pass
    @overload
    def SetIntegers(self, integers: List[int]) -> None:
        """
         Sets all of the integers stored with this UDO 
        """
        pass
    @overload
    def SetIntegers(self, offset: int, length: int, integers: List[int]) -> None:
        """
         Replaces the integers stored with this UDO in the specified range with a new array of integers 
        """
        pass
    @overload
    def SetLengths(self, lengths: List[float]) -> None:
        """
         Sets all of the lengths stored with this UDO 
        """
        pass
    @overload
    def SetLengths(self, offset: int, length: int, lengths: List[float]) -> None:
        """
         Replaces the lengths stored with this UDO in the specified range with a new array of lengths 
        """
        pass
    @overload
    def SetLinks(self, link_type: UserDefinedObject.LinkType, links: List[UserDefinedObject.LinkDefinition]) -> None:
        """
         Sets all of the links with the given link type stored with this UDO.
                    If you already had objects linked to the UDO via the specified link type,
                    this operation will over-write them with the newly specified links. 
        """
        pass
    @overload
    def SetLinks(self, link_type: UserDefinedObject.LinkType, offset: int, length: int, links: List[UserDefinedObject.LinkDefinition]) -> None:
        """
         Replaces the links of the given link type stored with this UDO in the specified range with a new array of links 
        """
        pass
    @overload
    def SetStrings(self, strings: List[str]) -> None:
        """
         Sets all of the strings stored with this UDO 
        """
        pass
    @overload
    def SetStrings(self, offset: int, length: int, strings: List[str]) -> None:
        """
         Replaces the strings stored with this UDO in the specified range with a new array of strings 
        """
        pass
    @overload
    def SetVolumes(self, volumes: List[float]) -> None:
        """
         Sets all of the volumes stored with this UDO 
        """
        pass
    @overload
    def SetVolumes(self, offset: int, length: int, volumes: List[float]) -> None:
        """
         Replaces the volumes stored with this UDO in the specified range with a new array of volumes 
        """
        pass
