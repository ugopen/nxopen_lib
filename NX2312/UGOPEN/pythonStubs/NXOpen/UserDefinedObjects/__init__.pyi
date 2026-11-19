from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Manages the user defined objects.  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedClassManager(NXOpen.Object): 
    """ Manages the user defined objects. """


    ##  
    ##           Constructs a new @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  object.
    ##          
    ##  @return udo_class (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink):  The new UserDefinedClass instance .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The  class name of the new UserDefinedClass 
    def CreateUserDefinedObjectClass(class_name: str, friendly_name: str) -> UserDefinedClass:
        """
         
                  Constructs a new @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  object.
                 
         @return udo_class (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink):  The new UserDefinedClass instance .
        """
        pass
    
    ##  
    ##           Get the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  object associated with the given class name.
    ##          
    ##  @return udo_class (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink):  The UserDefinedClass instance it may be NULL if you do not have permission to query this object .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  name of class to find 
    @staticmethod
    def GetUserDefinedClassFromClassName(class_name: str) -> UserDefinedClass:
        """
         
                  Get the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  object associated with the given class name.
                 
         @return udo_class (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink):  The UserDefinedClass instance it may be NULL if you do not have permission to query this object .
        """
        pass
    
    ##  Creats a new UserDefinedClass object 
    ##  @return udo_class (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def NewUserDefinedClass() -> UserDefinedClass:
        """
         Creats a new UserDefinedClass object 
         @return udo_class (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink): .
        """
        pass
    
import NXOpen
##  JA interface for the UserDefinedClass object  <br> To create a new instance of this class, use @link NXOpen::UserDefinedObjects::UserDefinedClassManager::NewUserDefinedClass  NXOpen::UserDefinedObjects::UserDefinedClassManager::NewUserDefinedClass @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedClass(NXOpen.TransientObject): 
    """ JA interface for the UserDefinedClass object """


    ##  Allow owned object selection on all objects owned by an object of this @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink . 
    ##  You do NOT have permission to select objects owned by this class. 
    class AllowOwnedObjectSelection(Enum):
        """
        Members Include: <Off> <On>
        """
        Off: int
        On: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedClass.AllowOwnedObjectSelection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Allow query class from name options for a @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  of this class. 
    ##  You do NOT have permission to query the class from it's name. 
    class AllowQueryClass(Enum):
        """
        Members Include: <Off> <On>
        """
        Off: int
        On: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedClass.AllowQueryClass:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Allow query class from name options for a @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink . 
    ##  UDO's of this class will NOT be selectable. 
    class Selection(Enum):
        """
        Members Include: <Off> <On>
        """
        Off: int
        On: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedClass.Selection:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link UserDefinedClass.AllowOwnedObjectSelection NXOpen.UserDefinedObjects.UserDefinedClass.AllowOwnedObjectSelection@endlink) AllowOwnedObjectSelectionOption
    ##   the allow owned object selection flag.  
    ##    Specifies whether or not you have permission to select objects owned by @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink 's of this class.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return UserDefinedClass.AllowOwnedObjectSelection
    @property
    def AllowOwnedObjectSelectionOption(self) -> UserDefinedClass.AllowOwnedObjectSelection:
        """
        Getter for property: (@link UserDefinedClass.AllowOwnedObjectSelection NXOpen.UserDefinedObjects.UserDefinedClass.AllowOwnedObjectSelection@endlink) AllowOwnedObjectSelectionOption
          the allow owned object selection flag.  
           Specifies whether or not you have permission to select objects owned by @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink 's of this class.   
         
        """
        pass
    
    ## Setter for property: (@link UserDefinedClass.AllowOwnedObjectSelection NXOpen.UserDefinedObjects.UserDefinedClass.AllowOwnedObjectSelection@endlink) AllowOwnedObjectSelectionOption

    ##   the allow owned object selection flag.  
    ##    Specifies whether or not you have permission to select objects owned by @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink 's of this class.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @AllowOwnedObjectSelectionOption.setter
    def AllowOwnedObjectSelectionOption(self, allow_owned_object_selection_option: UserDefinedClass.AllowOwnedObjectSelection):
        """
        Setter for property: (@link UserDefinedClass.AllowOwnedObjectSelection NXOpen.UserDefinedObjects.UserDefinedClass.AllowOwnedObjectSelection@endlink) AllowOwnedObjectSelectionOption
          the allow owned object selection flag.  
           Specifies whether or not you have permission to select objects owned by @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink 's of this class.   
         
        """
        pass
    
    ## Getter for property: (@link UserDefinedClass.AllowQueryClass NXOpen.UserDefinedObjects.UserDefinedClass.AllowQueryClass@endlink) AllowQueryClassFromName
    ##   the allow query class from name flag.  
    ##    Specifies whether or not you are allowed to query the @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  from the class name.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return UserDefinedClass.AllowQueryClass
    @property
    def AllowQueryClassFromName(self) -> UserDefinedClass.AllowQueryClass:
        """
        Getter for property: (@link UserDefinedClass.AllowQueryClass NXOpen.UserDefinedObjects.UserDefinedClass.AllowQueryClass@endlink) AllowQueryClassFromName
          the allow query class from name flag.  
           Specifies whether or not you are allowed to query the @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  from the class name.   
         
        """
        pass
    
    ## Setter for property: (@link UserDefinedClass.AllowQueryClass NXOpen.UserDefinedObjects.UserDefinedClass.AllowQueryClass@endlink) AllowQueryClassFromName

    ##   the allow query class from name flag.  
    ##    Specifies whether or not you are allowed to query the @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  from the class name.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @AllowQueryClassFromName.setter
    def AllowQueryClassFromName(self, allow_query_class_from_name: UserDefinedClass.AllowQueryClass):
        """
        Setter for property: (@link UserDefinedClass.AllowQueryClass NXOpen.UserDefinedObjects.UserDefinedClass.AllowQueryClass@endlink) AllowQueryClassFromName
          the allow query class from name flag.  
           Specifies whether or not you are allowed to query the @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  from the class name.   
         
        """
        pass
    
    ## Getter for property: (str) ClassName
    ##   the class name of the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
          the class name of the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (str) FriendlyName
    ##   the friendly name of the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink .  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def FriendlyName(self) -> str:
        """
        Getter for property: (str) FriendlyName
          the friendly name of the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink .  
             
         
        """
        pass
    
    ## Getter for property: (bool) WarnUserFlag
    ##   the warn user flag.  
    ##    
    ##         Specifies the behavior of warning the user if a @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  
    ##         of the given @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  
    ##         is found in a part, but the code implementing the methods for the UDO is not loaded.
    ##         The default action is to not warn the user. If the UDO author sets this flag
    ##         to TRUE, all UDO's of this class that are created will be marked so that the
    ##         user will be warned if the UDO methods have not been loaded, but a UDO of the
    ##         class is in the part. This warning will be issued to the listing window,
    ##         when the first object of the given class is retrieved. This warning will
    ##         only be given once per session.
    ## 
    ##         This flag is set on every UDO object. Therefore for any part, there may be a mixture UDO objects of a given class, 
    ##         some having this flag set to TRUE and some objects having the flag set to FALSE. This is particularly true since all 
    ##         UDO objects created before NX 3.0 will have this flag set to FALSE. If the UDO methods for a class are not loaded, 
    ##         any one UDO with this flag set to TRUE in a part is enough for the warning to be issued to the listing window.
    ##         
    ##         Note that the warning is only issued for UDO's in a part if the part is fully loaded.  
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return bool
    @property
    def WarnUserFlag(self) -> bool:
        """
        Getter for property: (bool) WarnUserFlag
          the warn user flag.  
           
                Specifies the behavior of warning the user if a @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  
                of the given @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  
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
    
    ## Setter for property: (bool) WarnUserFlag

    ##   the warn user flag.  
    ##    
    ##         Specifies the behavior of warning the user if a @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  
    ##         of the given @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  
    ##         is found in a part, but the code implementing the methods for the UDO is not loaded.
    ##         The default action is to not warn the user. If the UDO author sets this flag
    ##         to TRUE, all UDO's of this class that are created will be marked so that the
    ##         user will be warned if the UDO methods have not been loaded, but a UDO of the
    ##         class is in the part. This warning will be issued to the listing window,
    ##         when the first object of the given class is retrieved. This warning will
    ##         only be given once per session.
    ## 
    ##         This flag is set on every UDO object. Therefore for any part, there may be a mixture UDO objects of a given class, 
    ##         some having this flag set to TRUE and some objects having the flag set to FALSE. This is particularly true since all 
    ##         UDO objects created before NX 3.0 will have this flag set to FALSE. If the UDO methods for a class are not loaded, 
    ##         any one UDO with this flag set to TRUE in a part is enough for the warning to be issued to the listing window.
    ##         
    ##         Note that the warning is only issued for UDO's in a part if the part is fully loaded.  
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @WarnUserFlag.setter
    def WarnUserFlag(self, warn_user: bool):
        """
        Setter for property: (bool) WarnUserFlag
          the warn user flag.  
           
                Specifies the behavior of warning the user if a @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink  
                of the given @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  
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
    
    ##  Prototype for display, selection, attention point, fit and screen-size-fit callbacks 
    ## A callback definition with the following input arguments: 
    ##  - @link UserDefinedDisplayEvent NXOpen.UserDefinedObjects.UserDefinedDisplayEvent@endlink
    ##  and no return type
    DisplayCallback = Callable[[UserDefinedDisplayEvent], None]
    
    
    ##  Registers the attention point callback. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddAttentionPointHandler(udo_class: UserDefinedClass, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the attention point callback. 
        """
        pass
    
    ##  Prototype for update, and delete callbacks 
    ## A callback definition with the following input arguments: 
    ##  - @link UserDefinedLinkEvent NXOpen.UserDefinedObjects.UserDefinedLinkEvent@endlink
    ##  and no return type
    LinkCallback = Callable[[UserDefinedLinkEvent], None]
    
    
    ##  Registers the delete callback. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddDeleteHandler(udo_class: UserDefinedClass, link_event: UserDefinedClass.LinkCallback) -> None:
        """
         Registers the delete callback. 
        """
        pass
    
    ##  Registers UDO display callback. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddDisplayHandler(udo_class: UserDefinedClass, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers UDO display callback. 
        """
        pass
    
    ##  Prototype for information, edit, and suppress callbacks 
    ## A callback definition with the following input arguments: 
    ##  - @link UserDefinedEvent NXOpen.UserDefinedObjects.UserDefinedEvent@endlink
    ##  and no return type
    GenericCallback = Callable[[UserDefinedEvent], None]
    
    
    ##  Registers the edit callback. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddEditHandler(udo_class: UserDefinedClass, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the edit callback. 
        """
        pass
    
    ##  Registers the fit callback.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddFitHandler(udo_class: UserDefinedClass, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the fit callback.  
        """
        pass
    
    ##  Registers the information callback. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddInformationHandler(udo_class: UserDefinedClass, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the information callback. 
        """
        pass
    
    ##  Registers the screen size fit callback.  The screen size fit callback is called when
    ##             it is necesary to determine the bounding box of a screen size object (one which
    ##             remains the same size on the screen independent of the view scale) during a fit
    ##             computation.  As of NX 8.0 the only geometry types supported for User Defined Objects
    ##             which are screen size are ScreenStandardText and AbsoluteRotationScreenSizeText.
    ##             If your User Defined Object does not have any of these objects, then you should not
    ##             call @link NXOpen::UserDefinedObjects::UserDefinedClass::AddScreenSizeFitHandler NXOpen::UserDefinedObjects::UserDefinedClass::AddScreenSizeFitHandler@endlink  because to do
    ##             do would incur a performance penalty. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddScreenSizeFitHandler(udo_class: UserDefinedClass, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the screen size fit callback.  The screen size fit callback is called when
                    it is necesary to determine the bounding box of a screen size object (one which
                    remains the same size on the screen independent of the view scale) during a fit
                    computation.  As of NX 8.0 the only geometry types supported for User Defined Objects
                    which are screen size are ScreenStandardText and AbsoluteRotationScreenSizeText.
                    If your User Defined Object does not have any of these objects, then you should not
                    call @link NXOpen::UserDefinedObjects::UserDefinedClass::AddScreenSizeFitHandler NXOpen::UserDefinedObjects::UserDefinedClass::AddScreenSizeFitHandler@endlink  because to do
                    do would incur a performance penalty. 
        """
        pass
    
    ##  Registers the UDO selection callback. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddSelectionHandler(udo_class: UserDefinedClass, display_event: UserDefinedClass.DisplayCallback) -> None:
        """
         Registers the UDO selection callback. 
        """
        pass
    
    ##  Registers the suppress callback. 
    ##         
    ##         Note this callback is not called unless you have a UDO FEATURE.  Also it *may* not
    ##         get called when the system automatically suppresses the feature during update.
    ## 
    ##         Also note the user should check the suppression status of the feature in their callback to
    ##         see if the input udo feature is currently getting suppressed or unsuppressed. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddSuppressHandler(udo_class: UserDefinedClass, udo_event: UserDefinedClass.GenericCallback) -> None:
        """
         Registers the suppress callback. 
                
                Note this callback is not called unless you have a UDO FEATURE.  Also it *may* not
                get called when the system automatically suppresses the feature during update.
        
                Also note the user should check the suppression status of the feature in their callback to
                see if the input udo feature is currently getting suppressed or unsuppressed. 
        """
        pass
    
    ##  Registers the update callback. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  
    def AddUpdateHandler(udo_class: UserDefinedClass, link_event: UserDefinedClass.LinkCallback) -> None:
        """
         Registers the update callback. 
        """
        pass
    
    ##  Frees the memory associated with this object.  After invocation of this
    ##           method, the object is no longer valid.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object.  After invocation of this
                  method, the object is no longer valid.  
        """
        pass
    
    ##  Gets the is occurrenceable flag for this class. 
    ##         Legacy Open C UDO's required a reference UDO to determine Occurrenceability.  Occurrenceability is now set
    ##         on a class by class basis (no reference UDO required).  In the event that you have a legacy UDO you wish to query for occurenceability, 
    ##         you will need set the is occurrenceable flag with the new native language method (which does not require a reference UDO) 
    ##         If you do not set the is occurrenceable flag, and instead use the old open c is occurrenceable callback, you will risk error raising during this
    ##         method because we will automatically pass NULL in as the reference UDO to the legacy is occurrenceable callback.
    ##  @return is_occurrenceable (bool):  Specifies whether or not to populate occurrences for @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink 's of this class. .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetIsOccurrenceableFlag(udo_class: UserDefinedClass) -> bool:
        """
         Gets the is occurrenceable flag for this class. 
                Legacy Open C UDO's required a reference UDO to determine Occurrenceability.  Occurrenceability is now set
                on a class by class basis (no reference UDO required).  In the event that you have a legacy UDO you wish to query for occurenceability, 
                you will need set the is occurrenceable flag with the new native language method (which does not require a reference UDO) 
                If you do not set the is occurrenceable flag, and instead use the old open c is occurrenceable callback, you will risk error raising during this
                method because we will automatically pass NULL in as the reference UDO to the legacy is occurrenceable callback.
         @return is_occurrenceable (bool):  Specifies whether or not to populate occurrences for @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink 's of this class. .
        """
        pass
    
    ##  Sets the is occurrenceable flag for this class. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Specifies whether or not to populate occurrences for @link NXOpen::UserDefinedObjects::UserDefinedObject NXOpen::UserDefinedObjects::UserDefinedObject@endlink 's of this class. 
    def SetIsOccurrenceableFlag(udo_class: UserDefinedClass, is_occurrenceable: bool) -> None:
        """
         Sets the is occurrenceable flag for this class. 
        """
        pass
    
##  Implements the Display Event Object for UDO's 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedDisplayEvent(UserDefinedEvent): 
    """ Implements the Display Event Object for UDO's """


    ## Getter for property: (@link UserDefinedObjectDisplayContext NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext@endlink) DisplayContext
    ##   the display context.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return UserDefinedObjectDisplayContext
    @property
    def DisplayContext(self) -> UserDefinedObjectDisplayContext:
        """
        Getter for property: (@link UserDefinedObjectDisplayContext NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext@endlink) DisplayContext
          the display context.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##             called, it is illegal to use the object.  In .NET and Java,
    ##             his method is automatically called when the object is
    ##             deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(udo_display_event: UserDefinedDisplayEvent) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
    
import NXOpen
##  Implements the Event Object for UDO's 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedEvent(NXOpen.TransientObject): 
    """ Implements the Event Object for UDO's """


    ##  Available link types for a @link UserDefinedObject UserDefinedObject@endlink . 
    ##  Display UDO event 
    class Reason(Enum):
        """
        Members Include: <Display> <Delete> <Update> <Selection> <Fit> <AttentionPoint> <Info> <Edit> <Suppress> <ScreenSizeFit> <PreSave> <PostLoad>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedEvent.Reason:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link UserDefinedEvent.Reason NXOpen.UserDefinedObjects.UserDefinedEvent.Reason@endlink) EventReason
    ##   the reason we fired this event.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return UserDefinedEvent.Reason
    @property
    def EventReason(self) -> UserDefinedEvent.Reason:
        """
        Getter for property: (@link UserDefinedEvent.Reason NXOpen.UserDefinedObjects.UserDefinedEvent.Reason@endlink) EventReason
          the reason we fired this event.  
             
         
        """
        pass
    
    ## Getter for property: (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) UserDefinedObject
    ##   the related UDO.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return UserDefinedObject
    @property
    def UserDefinedObject(self) -> UserDefinedObject:
        """
        Getter for property: (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) UserDefinedObject
          the related UDO.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##             called, it is illegal to use the object.  In .NET and Java,
    ##             his method is automatically called when the object is
    ##             deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(udo_event: UserDefinedEvent) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
    
import NXOpen
##  Implements the Display Event Object for UDO's 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedLinkEvent(UserDefinedEvent): 
    """ Implements the Display Event Object for UDO's """


    ## Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) AssociatedObject
    ##   the associated object.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return NXOpen.TaggedObject
    @property
    def AssociatedObject(self) -> NXOpen.TaggedObject:
        """
        Getter for property: (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) AssociatedObject
          the associated object.  
             
         
        """
        pass
    
    ## Getter for property: (int) LinkStatus
    ##   the link status.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def LinkStatus(self) -> int:
        """
        Getter for property: (int) LinkStatus
          the link status.  
             
         
        """
        pass
    
    ## Getter for property: (int) LinkType
    ##   the link type.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return int
    @property
    def LinkType(self) -> int:
        """
        Getter for property: (int) LinkType
          the link type.  
             
         
        """
        pass
    
    ##  Frees the object from memory.  After this method is
    ##             called, it is illegal to use the object.  In .NET and Java,
    ##             his method is automatically called when the object is
    ##             deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Dispose(udo_link_event: UserDefinedLinkEvent) -> None:
        """
         Frees the object from memory.  After this method is
                    called, it is illegal to use the object.  In .NET and Java,
                    his method is automatically called when the object is
                    deleted by the garbage collector.  
        """
        pass
    
import NXOpen
##  This class is used to display User Defined Objects 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedObjectDisplayContext(NXOpen.TransientObject): 
    """ This class is used to display User Defined Objects """


    ##  The enumerated type facet to be displayed 
    ##  The facet topology is a triangle facet 
    class FacetType(Enum):
        """
        Members Include: <Triangle> <Polygon> <Tristrip>
        """
        Triangle: int
        Polygon: int
        Tristrip: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.FacetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enumerated type specifies the type of marker to be displayed. 
    ##   
    class PolyMarker(Enum):
        """
        Members Include: <NoMarker> <Point> <Dot> <Asterisk> <Circle> <Poundsign> <X> <Gridpoint> <Square> <TriangleMarker> <Diamond> <Centerline> <ConsFix> <ConsHorizontal> <ConsVertical> <ConsParallel> <ConsPerpendicular> <ConsTangent> <ConsConcentric> <ConsCoincident> <ConsCollinear> <ConsPointOnCurve> <ConsMidpoint> <ConsEqualLength> <ConsEqualRadius> <ConsConstantLength> <ConsConstantAngle> <ConsMirror> <DimRadius> <DimDiameter> <DimParallel> <DimPerpendicular> <ConsSlope> <ConsString> <ConsUniformScaled> <ConsNonUniformScaled> <ConsAssocTrim> <ConsAssocOffset> <Disp2tResSpotWeld> <Disp3tResSpotWeld> <Disp4tResSpotWeld> <Disp2tDcSpotWeld> <Disp3tDcSpotWeld> <Disp4tDcSpotWeld> <Disp2tKpcSpotWeld> <Disp3tKpcSpotWeld> <Disp4tKpcSpotWeld> <Disp2tProcSpotWeld> <Disp3tProcSpotWeld> <Disp4tProcSpotWeld> <ArcSpotWeld> <ClinchWeld> <Anchor> <LeftLeaderConnection> <RightLeaderConnection> <FilledCircle> <FilledSquare> <LargeFilledSquare> <DatumPoint> <SnappingDiamond> <CircleInCircle> <CircleInSquare> <SquareInSquare> <FilledLeftTriangle> <FilledRightTriangle> <FilledUpTriangle> <FilledDownTriangle> <FilledLeftTriangleInCircle> <FilledRightTriangleInCircle> <FilledUpTriangleInCircle> <FilledDownTriangleInCircle> <FilledLeftTriangleInSquare> <FilledRightTriangleInSquare> <FilledUpTriangleInSquare> <FilledDownTriangleInSquare> <RoundedCross> <FilledDiamond> <UpDownTriangles> <LeftRightTriangles> <SmallWheel> <LargeWheel> <HollowCircle> <PreviewPerpendicular> <PreviewHorizontal> <PreviewVertical> <PreviewTangent> <PreviewParallel> <PreviewPointOnCurve> <PreviewCollinear> <Ruler> <Protractor> <SketchNotebook> <ArcEndPoint> <Disp2PtArcMarker> <BigAsterisk> <LineInCircle> <PlusInCircle> <CenterOfRotation> <PreviewX> <PreviewY> <PreviewZ> <Disp2tGeneralSpotWeld> <Disp3tGeneralSpotWeld> <Disp4tGeneralSpotWeld> <Disp2tVitalSpotWeld> <Disp3tVitalSpotWeld> <Disp4tVitalSpotWeld> <Disp2tImportantSpotWeld> <Disp3tImportantSpotWeld> <Disp4tImportantSpotWeld> <Disp2tSemipanelSpotWeld> <Disp3tSemipanelSpotWeld> <Disp4tSemipanelSpotWeld> <InvalidMarker>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.PolyMarker:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enumerated type specifies the type of reference point used in the text box
    ##             for standard_text methods. 
    ##  Display the text using the system
    ##                                                                              default reference point position 
    class StandardTextRef(Enum):
        """
        Members Include: <SystemDefault> <BaselineStart> <BaselineCenter> <BaselineEnd> <TopLeft> <TopCenter> <TopRight> <MiddleLeft> <MiddleCenter> <MiddleRight> <BottomLeft> <BottomCenter> <BottomRight>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.StandardTextRef:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enumerated type specifies the type of reference point used in the text box. 
    ##  Display the text using the system default 
    class TextRef(Enum):
        """
        Members Include: <SystemDefault> <TopLeft> <TopCenter> <TopRight> <MiddleLeft> <MiddleCenter> <MiddleRight> <BottomLeft> <BottomCenter> <BottomRight>
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
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.TextRef:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##   Provides a way to specify the size of the desired text, as small,
    ##              medium or large (normal is a synonym for medium). 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Small</term><description> 
    ## </description> </item><item><term> 
    ## Normal</term><description> 
    ## </description> </item><item><term> 
    ## Medium</term><description> 
    ## </description> </item><item><term> 
    ## Large</term><description> 
    ## </description> </item><item><term> 
    ## NumSizes</term><description> 
    ## </description> </item></list>
    class TextSize(Enum):
        """
        Members Include: <Small> <Normal> <Medium> <Large> <NumSizes>
        """
        Small: int
        Normal: int
        Medium: int
        Large: int
        NumSizes: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.TextSize:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The enumerated view mode 
    ##  The view is not shaded 
    class ViewMode(Enum):
        """
        Members Include: <NotShaded> <PartiallyShaded> <FullyShaded> <AnalysisShaded> <StudioShaded>
        """
        NotShaded: int
        PartiallyShaded: int
        FullyShaded: int
        AnalysisShaded: int
        StudioShaded: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObjectDisplayContext.ViewMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Displays a single line "Standard Text" string using "Absolute Rotation and Screen
    ##             Size Geometry" for a @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text"
    ##             string uses one of the fonts available from the operating system.
    ##             "Absolute Rotation and Screen Size Geometry" means the text appears the
    ##             same physical sized on the screen regardless of the view scale (like
    ##             "Screen Geometry"), the text remains front-facing and approximately
    ##             upright (similar to "Screen Geometry"), but the orientation of the text
    ##             changes as the user rotates the view (like "Absolute Geometry").
    ##             The text will be displayed on the XY plane of the absolute coordinate system.
    ##             This method is not supported for 2D output such as CGM. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  Index of the text font to be used.
    ##                                                    This must be an index of a standard font.
    ##                                                    It may be 0 to use the default font. 
    def DisplayAbsoluteRotationScreenSizeStandardText(context: UserDefinedObjectDisplayContext, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, string: str, text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a single line "Standard Text" string using "Absolute Rotation and Screen
                    Size Geometry" for a @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text"
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
    
    ##  Displays a single line "Standard Text" string using "Absolute Geometry" for a
    ##             @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
    ##             of the fonts available from the operating system.  "Absolute Geometry"
    ##             means that the text scales and rotates with the view, so it appears larger
    ##             when you zoom in and smaller when you zoom out.  This is the type of text
    ##             normally used by NX Drafting.   Note that the text will be displayed on
    ##             the Absolute XY plane. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##   Index of the text font to be used.
    ##                                                     This must be an index of a standard font.
    ##                                                     It may be 0 to use the default font. 
    def DisplayAbsoluteStandardText(context: UserDefinedObjectDisplayContext, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, string: str, glyph_width: float, glyph_height: float) -> None:
        """
         Displays a single line "Standard Text" string using "Absolute Geometry" for a
                    @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Absolute Geometry"
                    means that the text scales and rotates with the view, so it appears larger
                    when you zoom in and smaller when you zoom out.  This is the type of text
                    normally used by NX Drafting.   Note that the text will be displayed on
                    the Absolute XY plane. 
        """
        pass
    
    ##  Displays an arc for a @link UserDefinedObject UserDefinedObject@endlink .  
    ##             The arc will be created in a plane whose normal is the Z axis 
    ##             of the orientation matrix  
    ##              (matrix[0-2] is the X axis of the orientation matrix,  
    ##               matrix[3-5] is the Y axis of the orientation matrix, and
    ##               matrix[6-8] is the Z axis of the orientation matrix.)
    ##             The start and end angles are measured relative to
    ##             the X and Y axis of this orientation matrix. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Center of the arc (absolute coordinates transformed by the orientation matrix) 
    def DisplayArc(context: UserDefinedObjectDisplayContext, center: NXOpen.Point3d, original: NXOpen.Matrix3x3, radius: float, start_angle: float, end_angle: float) -> None:
        """
         Displays an arc for a @link UserDefinedObject UserDefinedObject@endlink .  
                    The arc will be created in a plane whose normal is the Z axis 
                    of the orientation matrix  
                     (matrix[0-2] is the X axis of the orientation matrix,  
                      matrix[3-5] is the Y axis of the orientation matrix, and
                      matrix[6-8] is the Z axis of the orientation matrix.)
                    The start and end angles are measured relative to
                    the X and Y axis of this orientation matrix. 
        """
        pass
    
    ##  Displays a circle for a @link UserDefinedObject UserDefinedObject@endlink .  
    ##             The circle will be created in a plane which is normal to
    ##             the Z axis of the orientation matrix.  
    ##              (matrix[0-2] is the X axis of the orientation matrix,  
    ##               matrix[3-5] is the Y axis of the orientation matrix, and
    ##               matrix[6-8] is the Z axis of the orientation matrix.) 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Center of the arc (absolute coordinates transformed by the orientation matrix) 
    def DisplayCircle(context: UserDefinedObjectDisplayContext, center: NXOpen.Point3d, original: NXOpen.Matrix3x3, radius: float, filled: bool) -> None:
        """
         Displays a circle for a @link UserDefinedObject UserDefinedObject@endlink .  
                    The circle will be created in a plane which is normal to
                    the Z axis of the orientation matrix.  
                     (matrix[0-2] is the X axis of the orientation matrix,  
                      matrix[3-5] is the Y axis of the orientation matrix, and
                      matrix[6-8] is the Z axis of the orientation matrix.) 
        """
        pass
    
    ##  Displays a series of facets for a @link UserDefinedObject UserDefinedObject@endlink . 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Number of points to define a facet. 
    def DisplayFacets(context: UserDefinedObjectDisplayContext, num_vertices: int, num_facets: int, vertices: List[NXOpen.Point3d], normals: List[NXOpen.Vector3d], type_of_facet: UserDefinedObjectDisplayContext.FacetType) -> None:
        """
         Displays a series of facets for a @link UserDefinedObject UserDefinedObject@endlink . 
        """
        pass
    
    ##  Displays a multi-line "Standard Text" string using "Absolute Rotation and Screen
    ##             Size Geometry" for a @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text"
    ##             string uses one of the fonts available from the operating system.
    ##             "Absolute Rotation and Screen Size Geometry" means the text appears the
    ##             same physical sized on the screen regardless of the view scale (like
    ##             "Screen Geometry"), the text remains front-facing and approximately
    ##             upright (similar to "Screen Geometry"), but the orientation of the text
    ##             changes as the user rotates the view (like "Absolute Geometry").
    ##             The text will be displayed on the XY plane of the absolute coordinate system.
    ##             This method is not supported for 2D output such as CGM. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  Index of the text font to be used.
    ##                                                     This must be an index of a standard font.
    ##                                                     It may be 0 to use the default font. 
    def DisplayMultiLineAbsoluteRotationScreenSizeStandardText(context: UserDefinedObjectDisplayContext, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, strings: List[str], text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a multi-line "Standard Text" string using "Absolute Rotation and Screen
                    Size Geometry" for a @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text"
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
    
    ##  Displays a multi-line "Standard Text" string using "Absolute Geometry" for a
    ##             @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
    ##             of the fonts available from the operating system.  "Absolute Geometry"
    ##             means that the text scales and rotates with the view, so it appears larger
    ##             when you zoom in and smaller when you zoom out.  This is the type of text
    ##             normally used by NX Drafting.   Note that the text will be displayed on
    ##             the Absolute XY plane. 
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##   Index of the text font to be used.
    ##                                                      This must be an index of a standard font.
    ##                                                      It may be 0 to use the default font. 
    def DisplayMultiLineAbsoluteStandardText(context: UserDefinedObjectDisplayContext, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, strings: List[str], glyph_width: float, glyph_height: float) -> None:
        """
         Displays a multi-line "Standard Text" string using "Absolute Geometry" for a
                    @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Absolute Geometry"
                    means that the text scales and rotates with the view, so it appears larger
                    when you zoom in and smaller when you zoom out.  This is the type of text
                    normally used by NX Drafting.   Note that the text will be displayed on
                    the Absolute XY plane. 
        """
        pass
    
    ##  Displays a multi-line "Standard Text" string using "Screen Geometry" for a
    ##             @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
    ##             of the fonts available from the operating system.  "Screen Geometry" means
    ##             that the text remains parallel to the screen and appears the same physical
    ##             size on the screen regardless of the view scale. This method is not
    ##             supported for 2D output such as CGM.  Note that the text will be displayed on
    ##             the Absolute XY plane.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##   Index of the text font to be used.
    ##                                                      This must be an index of a standard font.
    ##                                                      It may be 0 to use the default font. 
    def DisplayMultiLineScreenStandardText(context: UserDefinedObjectDisplayContext, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, strings: List[str], text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a multi-line "Standard Text" string using "Screen Geometry" for a
                    @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Screen Geometry" means
                    that the text remains parallel to the screen and appears the same physical
                    size on the screen regardless of the view scale. This method is not
                    supported for 2D output such as CGM.  Note that the text will be displayed on
                    the Absolute XY plane.
        """
        pass
    
    ##  Displays a series of points for a @link UserDefinedObject UserDefinedObject@endlink . 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of point coordinates. 
    ##                                                                   points[0-2] defines the first point, points[3-5] defines the second point, etc.
    def DisplayPoints(context: UserDefinedObjectDisplayContext, points: List[NXOpen.Point3d], marker_type: UserDefinedObjectDisplayContext.PolyMarker) -> None:
        """
         Displays a series of points for a @link UserDefinedObject UserDefinedObject@endlink . 
        """
        pass
    
    ##  Displays a polygon (a closed set of line segements) for a @link UserDefinedObject UserDefinedObject@endlink .  
    ##             The line segments are defined by an array of points. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of point coordinates which define the polyline.
    ##                                                                   points[0-2] defines the first end point, points[3-5] defines the second end point, etc. 
    def DisplayPolygon(context: UserDefinedObjectDisplayContext, points: List[NXOpen.Point3d], filled: bool) -> None:
        """
         Displays a polygon (a closed set of line segements) for a @link UserDefinedObject UserDefinedObject@endlink .  
                    The line segments are defined by an array of points. 
        """
        pass
    
    ##  Displays a polyline (a connected set of line segements) for a @link UserDefinedObject UserDefinedObject@endlink .  
    ##             The line segments are defined by an array of points.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of point coordinates which define the polyline.
    ##                                                                  points[0-2] defines the first point, points[3-5] defines the second point, etc. 
    def DisplayPolyline(context: UserDefinedObjectDisplayContext, points: List[NXOpen.Point3d]) -> None:
        """
         Displays a polyline (a connected set of line segements) for a @link UserDefinedObject UserDefinedObject@endlink .  
                    The line segments are defined by an array of points.
        """
        pass
    
    ##  Displays a single line "Standard Text" string using "Screen Geometry" for a
    ##             @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
    ##             of the fonts available from the operating system.  "Screen Geometry" means
    ##             that the text remains parallel to the screen and appears the same physical
    ##             size on the screen regardless of the view scale. This method is not
    ##             supported for 2D output such as CGM.  Note that the text will be displayed on
    ##             the Absolute XY plane.
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##   Index of the text font to be used.
    ##                                                     This must be an index of a standard font.
    ##                                                     It may be 0 to use the default font. 
    def DisplayScreenStandardText(context: UserDefinedObjectDisplayContext, font_index: int, font_style: str, text_coordinates: NXOpen.Point3d, reference_point_type: UserDefinedObjectDisplayContext.StandardTextRef, string: str, text_size: UserDefinedObjectDisplayContext.TextSize) -> None:
        """
         Displays a single line "Standard Text" string using "Screen Geometry" for a
                    @link UserDefinedObject UserDefinedObject@endlink . A "Standard Text" string uses one
                    of the fonts available from the operating system.  "Screen Geometry" means
                    that the text remains parallel to the screen and appears the same physical
                    size on the screen regardless of the view scale. This method is not
                    supported for 2D output such as CGM.  Note that the text will be displayed on
                    the Absolute XY plane.
        """
        pass
    
    ##  Displays a text string using an NX text font for a
    ##             @link UserDefinedObject UserDefinedObject@endlink . 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##   Text string to display 
    def DisplayText(context: UserDefinedObjectDisplayContext, text: str, text_coordinates: NXOpen.Point3d, reference_point: UserDefinedObjectDisplayContext.TextRef) -> None:
        """
         Displays a text string using an NX text font for a
                    @link UserDefinedObject UserDefinedObject@endlink . 
        """
        pass
    
    ##  Displays a single character in the given font and style centered at the given position.
    ##             The character will always be displayed parallel to the screen.
    ##         
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ##  A single Unicode character to display
    ##                                                      at the given coordinate position. 
    def DisplayUnicodeMarker(context: UserDefinedObjectDisplayContext, unicode_char: str, font_index: int, font_style: str, marker_coordinates: NXOpen.Point3d, marker_size: float) -> None:
        """
         Displays a single character in the given font and style centered at the given position.
                    The character will always be displayed parallel to the screen.
                
        """
        pass
    
    ##  Frees the memory associated with this object.  After invocation of this
    ##           method, the object is no longer valid.  
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the memory associated with this object.  After invocation of this
                  method, the object is no longer valid.  
        """
        pass
    
    ##  Get information about the current view mode and display context in which geometry is displayed. 
    ##         
    ##  @return A tuple consisting of (view, is_view_mode_valid, view_mode, is_atten_pt_valid, attention_point, is_drawing_view_open). 
    ##  - view is: @link NXOpen.View NXOpen.View@endlink. View being displayed .
    ##  - is_view_mode_valid is: bool. True if the view mode was returned and False if no information was available .
    ##  - view_mode is: @link UserDefinedObjectDisplayContext.ViewMode NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.ViewMode@endlink. View mode describes the views shading
    ##                                                                         and face analysis mode - see enum values for more details .
    ##  - is_atten_pt_valid is: bool. True if the attention point was returned and
    ##                                                                         False if no information was available .
    ##  - attention_point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The attention point of the geometry just displayed .
    ##  - is_drawing_view_open is: bool. Is the drawing view open for display?
    ##                                                                         If true then geometry may be added to
    ##                                                                         the drawing. If false another view
    ##                                                                         which is not the drawing is open .

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetViewMode(context: UserDefinedObjectDisplayContext) -> Tuple[NXOpen.View, bool, UserDefinedObjectDisplayContext.ViewMode, bool, NXOpen.Point3d, bool]:
        """
         Get information about the current view mode and display context in which geometry is displayed. 
                
         @return A tuple consisting of (view, is_view_mode_valid, view_mode, is_atten_pt_valid, attention_point, is_drawing_view_open). 
         - view is: @link NXOpen.View NXOpen.View@endlink. View being displayed .
         - is_view_mode_valid is: bool. True if the view mode was returned and False if no information was available .
         - view_mode is: @link UserDefinedObjectDisplayContext.ViewMode NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.ViewMode@endlink. View mode describes the views shading
                                                                                and face analysis mode - see enum values for more details .
         - is_atten_pt_valid is: bool. True if the attention point was returned and
                                                                                False if no information was available .
         - attention_point is: @link NXOpen.Point3d NXOpen.Point3d@endlink. The attention point of the geometry just displayed .
         - is_drawing_view_open is: bool. Is the drawing view open for display?
                                                                                If true then geometry may be added to
                                                                                the drawing. If false another view
                                                                                which is not the drawing is open .

        """
        pass
    
import NXOpen
##  This class creates and manages UserDefinedObjects  <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedObjectManager(NXOpen.Object): 
    """ This class creates and manages UserDefinedObjects """


    ##  Used to define a link to a UserDefinedObject 
    class LinkedUdoDefinition:
        """
         Used to define a link to a UserDefinedObject 
        """
        ## Getter for property :(@link UserDefinedObject.LinkType NXOpen.UserDefinedObjects.UserDefinedObject.LinkType@endlink) LinkType@return @link UserDefinedObject.LinkType NXOpen.UserDefinedObjects.UserDefinedObject.LinkType@endlink
        @property
        def LinkType(self) -> UserDefinedObject.LinkType:
            """
            Getter for property LinkType
            """
            pass
        
        ## Setter for property :(@link UserDefinedObject.LinkType NXOpen.UserDefinedObjects.UserDefinedObject.LinkType@endlink) LinkType
        @LinkType.setter
        def LinkType(self, value: UserDefinedObject.LinkType):
            """
            Getter for property LinkTypeSetter for property LinkType
            """
            pass
        
        ## Getter for property :(@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) AssociatedUdo@return @link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink
        @property
        def AssociatedUdo(self) -> UserDefinedObject:
            """
            Getter for property AssociatedUdo
            """
            pass
        
        ## Setter for property :(@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) AssociatedUdo
        @AssociatedUdo.setter
        def AssociatedUdo(self, value: UserDefinedObject):
            """
            Getter for property AssociatedUdoSetter for property AssociatedUdo
            """
            pass
        
        ## Getter for property :(@link UserDefinedObject.LinkStatus NXOpen.UserDefinedObjects.UserDefinedObject.LinkStatus@endlink) Status@return @link UserDefinedObject.LinkStatus NXOpen.UserDefinedObjects.UserDefinedObject.LinkStatus@endlink
        @property
        def Status(self) -> UserDefinedObject.LinkStatus:
            """
            Getter for property Status
            """
            pass
        
        ## Setter for property :(@link UserDefinedObject.LinkStatus NXOpen.UserDefinedObjects.UserDefinedObject.LinkStatus@endlink) Status
        @Status.setter
        def Status(self, value: UserDefinedObject.LinkStatus):
            """
            Getter for property StatusSetter for property Status
            """
            pass
        
    
    
    ##  
    ##           Constructs a new @link NXOpen::Features::UserDefinedObjectFeature NXOpen::Features::UserDefinedObjectFeature@endlink .
    ##          
    ##  @return udo (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink):  The new UserDefinedObject instance .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The UserDefinedClass used to define the new UserDefinedObject  
    def CreateUserDefinedObject(part: UserDefinedObjectManager, udo_class: UserDefinedClass) -> UserDefinedObject:
        """
         
                  Constructs a new @link NXOpen::Features::UserDefinedObjectFeature NXOpen::Features::UserDefinedObjectFeature@endlink .
                 
         @return udo (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink):  The new UserDefinedObject instance .
        """
        pass
    
    ##  Queries an NX Object to find all @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink 's that are linked to the given NXObject (note this will not find owning udos) 
    ##  @return links (@link UserDefinedObjectManager.LinkedUdoDefinition List[NXOpen.UserDefinedObjects.UserDefinedObjectManager.LinkedUdoDefinition]@endlink):  The link definitions from UDO's to the NXObject .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  NXObject to query for links 
    def GetLinksToObject(part: UserDefinedObjectManager, link_object: NXOpen.TaggedObject) -> List[UserDefinedObjectManager.LinkedUdoDefinition]:
        """
         Queries an NX Object to find all @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink 's that are linked to the given NXObject (note this will not find owning udos) 
         @return links (@link UserDefinedObjectManager.LinkedUdoDefinition List[NXOpen.UserDefinedObjects.UserDefinedObjectManager.LinkedUdoDefinition]@endlink):  The link definitions from UDO's to the NXObject .
        """
        pass
    
    ##  Queries an NX Object to find the @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  that owns the given NXObject (note this will return null for the owning udo if the object is not owned) 
    ##  @return owning_udo (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink):  The UDO which owns the NXObject .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  NXObject to query for an owning UDO 
    def GetOwningUserDefinedObject(part: UserDefinedObjectManager, link_object: NXOpen.TaggedObject) -> UserDefinedObject:
        """
         Queries an NX Object to find the @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  that owns the given NXObject (note this will return null for the owning udo if the object is not owned) 
         @return owning_udo (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink):  The UDO which owns the NXObject .
        """
        pass
    
    ##  Finds all @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  instances that use the given @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink . 
    ##  @return udos (@link UserDefinedObject List[NXOpen.UserDefinedObjects.UserDefinedObject]@endlink):  User Defined Objects of the given class .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The UserDefinedClass we want to find 
    def GetUdosOfClass(part: UserDefinedObjectManager, udo_class: UserDefinedClass) -> List[UserDefinedObject]:
        """
         Finds all @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  instances that use the given @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink . 
         @return udos (@link UserDefinedObject List[NXOpen.UserDefinedObjects.UserDefinedObject]@endlink):  User Defined Objects of the given class .
        """
        pass
    
    ##  Queries an NX Object to see if it can be linked to a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  via the given link type 
    ##  @return linkable (bool):  TRUE - This object can be linked to a UDO with the given link type, FALSE - this object can not be NOT linked to a UDO with the given link type .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  NXObject to query for linkability 
    def IsObjectLinkable(part: UserDefinedObjectManager, link_object: NXOpen.TaggedObject, link_type: UserDefinedObject.LinkType) -> bool:
        """
         Queries an NX Object to see if it can be linked to a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  via the given link type 
         @return linkable (bool):  TRUE - This object can be linked to a UDO with the given link type, FALSE - this object can not be NOT linked to a UDO with the given link type .
        """
        pass
    
    ##  Queries an NX Object to see if it is linked to a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  (note this will not
    ##         tell you if the object is owned by a UDO with an owning link) 
    ##  @return is_linked (bool):  TRUE - This object is linked to a UDO, FALSE - this object is NOT linked to a UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  NXObject to query for links 
    def IsObjectLinkedToUserDefinedObject(part: UserDefinedObjectManager, link_object: NXOpen.TaggedObject) -> bool:
        """
         Queries an NX Object to see if it is linked to a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  (note this will not
                tell you if the object is owned by a UDO with an owning link) 
         @return is_linked (bool):  TRUE - This object is linked to a UDO, FALSE - this object is NOT linked to a UDO .
        """
        pass
    
    ##  Queries an NX Object to see if it is owned by a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  
    ##  @return is_linked (bool):  TRUE - This object is owned by a UDO, FALSE - this object is NOT owned by a UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  NXObject to query for an owning UDO 
    def IsObjectOwnedByUserDefinedObject(part: UserDefinedObjectManager, link_object: NXOpen.TaggedObject) -> bool:
        """
         Queries an NX Object to see if it is owned by a @link UserDefinedObjects::UserDefinedObject UserDefinedObjects::UserDefinedObject@endlink  
         @return is_linked (bool):  TRUE - This object is owned by a UDO, FALSE - this object is NOT owned by a UDO .
        """
        pass
    
import NXOpen
import NXOpen.Features
##  JA interface for the UserDefinedObject object 
## 
##   <br>  Created in NX5.0.0  <br> 

class UserDefinedObject(NXOpen.DisplayableObject): 
    """ JA interface for the UserDefinedObject object """


    ##  Status of the object linked to a @link NXOpen::Features::UserDefinedObjectFeature NXOpen::Features::UserDefinedObjectFeature@endlink  
    ##  The associated object is up to date. 
    class LinkStatus(Enum):
        """
        Members Include: <UpToDate> <OutOfDate>
        """
        UpToDate: int
        OutOfDate: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObject.LinkStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Available link types for a @link NXOpen::Features::UserDefinedObjectFeature NXOpen::Features::UserDefinedObjectFeature@endlink . 
    ##  The object is owned by the UDO 
    class LinkType(Enum):
        """
        Members Include: <Owning> <Type1> <Type2> <Type3> <Type4>
        """
        Owning: int
        Type1: int
        Type2: int
        Type3: int
        Type4: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> UserDefinedObject.LinkType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Contains the linked object and it's status along with the type of link.
    class LinkDefinition:
        """
         Contains the linked object and it's status along with the type of link.
        """
        ## Getter for property :(@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) AssociatedObject
        ## linked object
        ## @return @link NXOpen.TaggedObject NXOpen.TaggedObject@endlink
        @property
        def AssociatedObject(self) -> NXOpen.TaggedObject:
            """
            Getter for property AssociatedObject
            linked object

            """
            pass
        
        ## Setter for property :(@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) AssociatedObject
        @AssociatedObject.setter
        def AssociatedObject(self, value: NXOpen.TaggedObject):
            """
            Getter for property AssociatedObject
            linked object
            Setter for property AssociatedObject
            linked object

            """
            pass
        
        ## Getter for property :(@link UserDefinedObject.LinkStatus NXOpen.UserDefinedObjects.UserDefinedObject.LinkStatus@endlink) Status
        ## status of the linked object
        ## @return @link UserDefinedObject.LinkStatus NXOpen.UserDefinedObjects.UserDefinedObject.LinkStatus@endlink
        @property
        def Status(self) -> UserDefinedObject.LinkStatus:
            """
            Getter for property Status
            status of the linked object

            """
            pass
        
        ## Setter for property :(@link UserDefinedObject.LinkStatus NXOpen.UserDefinedObjects.UserDefinedObject.LinkStatus@endlink) Status
        @Status.setter
        def Status(self, value: UserDefinedObject.LinkStatus):
            """
            Getter for property Status
            status of the linked object
            Setter for property Status
            status of the linked object

            """
            pass
        
    
    
    ## Getter for property: (str) ClassName
    ##   the class name of this UDO   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return str
    @property
    def ClassName(self) -> str:
        """
        Getter for property: (str) ClassName
          the class name of this UDO   
            
         
        """
        pass
    
    ## Getter for property: (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink) UserDefinedClass
    ##   the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  for this UDO   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## @return UserDefinedClass
    @property
    def UserDefinedClass(self) -> UserDefinedClass:
        """
        Getter for property: (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink) UserDefinedClass
          the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  for this UDO   
            
         
        """
        pass
    
    ## Setter for property: (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink) UserDefinedClass

    ##   the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  for this UDO   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    @UserDefinedClass.setter
    def UserDefinedClass(self, user_defined_class: UserDefinedClass):
        """
        Setter for property: (@link UserDefinedClass NXOpen.UserDefinedObjects.UserDefinedClass@endlink) UserDefinedClass
          the @link NXOpen::UserDefinedObjects::UserDefinedClass NXOpen::UserDefinedObjects::UserDefinedClass@endlink  for this UDO   
            
         
        """
        pass
    
    ##  Clears the out of data indicator (status) of this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ClearUserDefinedObjectStatus(udo: UserDefinedObject) -> None:
        """
         Clears the out of data indicator (status) of this UDO 
        """
        pass
    
    ##  Gets all of the areas stored with this UDO 
    ##  @return areas (List[float]):  Array of areas stored with this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="udo"> (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) </param>
    @staticmethod
    @overload
    def GetAreas(self, udo: UserDefinedObject) -> List[float]:
        """
         Gets all of the areas stored with this UDO 
         @return areas (List[float]):  Array of areas stored with this UDO .
        """
        pass
    
    ##  Gets the areas stored in the specified range with this UDO 
    ##  @return areas (List[float]):  Array of areas stored within the specified  
    ##                                                         range of the area array for this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of areas at the start of the 
    ##                                                 returned range.
    ##                                                 Valid values are 0 through (number of areas in the udo - 1)
    ##                                                 and -(number of areas in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the area array.  
    ##                                                 Therefore using -1 or (number of areas in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def GetAreas(self, udo: UserDefinedObject, offset: int, length: int) -> List[float]:
        """
         Gets the areas stored in the specified range with this UDO 
         @return areas (List[float]):  Array of areas stored within the specified  
                                                                range of the area array for this UDO .
        """
        pass
    
    ##  Gets all of the doubles stored with this UDO 
    ##  @return doubles (List[float]):  Array of doubles stored with this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="udo"> (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) </param>
    @staticmethod
    @overload
    def GetDoubles(self, udo: UserDefinedObject) -> List[float]:
        """
         Gets all of the doubles stored with this UDO 
         @return doubles (List[float]):  Array of doubles stored with this UDO .
        """
        pass
    
    ##  Gets the doubles stored in the specified range with this UDO 
    ##  @return doubles (List[float]):  Array of doubles stored within the specified  
    ##                                                         range of the double array for this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of doubles at the start of the 
    ##                                                 returned range.
    ##                                                 Valid values are 0 through (number of doubles in the udo - 1)
    ##                                                 and -(number of doubles in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the double array.  
    ##                                                 Therefore using -1 or (number of doubles in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def GetDoubles(self, udo: UserDefinedObject, offset: int, length: int) -> List[float]:
        """
         Gets the doubles stored in the specified range with this UDO 
         @return doubles (List[float]):  Array of doubles stored within the specified  
                                                                range of the double array for this UDO .
        """
        pass
    
    ##  Gets all of the integers stored with this UDO 
    ##  @return integers (List[int]):  Array of integers stored with this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="udo"> (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) </param>
    @staticmethod
    @overload
    def GetIntegers(self, udo: UserDefinedObject) -> List[int]:
        """
         Gets all of the integers stored with this UDO 
         @return integers (List[int]):  Array of integers stored with this UDO .
        """
        pass
    
    ##  Gets the integers stored in the specified range with this UDO 
    ##  @return integers (List[int]):  Array of integers stored within the specified  
    ##                                                         range of the integer array for this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of integers at the start of the 
    ##                                                 returned range.
    ##                                                 Valid values are 0 through (number of integers in the udo - 1)
    ##                                                 and -(number of integers in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the integer array.  
    ##                                                 Therefore using -1 or (number of integers in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def GetIntegers(self, udo: UserDefinedObject, offset: int, length: int) -> List[int]:
        """
         Gets the integers stored in the specified range with this UDO 
         @return integers (List[int]):  Array of integers stored within the specified  
                                                                range of the integer array for this UDO .
        """
        pass
    
    ##  Gets all of the lengths stored with this UDO 
    ##  @return lengths (List[float]):  Array of lengths stored with this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="udo"> (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) </param>
    @staticmethod
    @overload
    def GetLengths(self, udo: UserDefinedObject) -> List[float]:
        """
         Gets all of the lengths stored with this UDO 
         @return lengths (List[float]):  Array of lengths stored with this UDO .
        """
        pass
    
    ##  Gets the lengths stored in the specified range with this UDO 
    ##  @return lengths (List[float]):  Array of lengths stored within the specified  
    ##                                                         range of the length array for this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of lengths at the start of the 
    ##                                                 returned range.
    ##                                                 Valid values are 0 through (number of lengths in the udo - 1)
    ##                                                 and -(number of lengths in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the length array.  
    ##                                                 Therefore using -1 or (number of lengths in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def GetLengths(self, udo: UserDefinedObject, offset: int, length: int) -> List[float]:
        """
         Gets the lengths stored in the specified range with this UDO 
         @return lengths (List[float]):  Array of lengths stored within the specified  
                                                                range of the length array for this UDO .
        """
        pass
    
    ##  Gets all links with the given link type that are stored with this UDO 
    ##  @return links (@link UserDefinedObject.LinkDefinition List[NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition]@endlink):  Array of links (with the given link type) stored with this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The type of links you wish to get 
    @overload
    def GetLinks(self, udo: UserDefinedObject, link_type: UserDefinedObject.LinkType) -> List[UserDefinedObject.LinkDefinition]:
        """
         Gets all links with the given link type that are stored with this UDO 
         @return links (@link UserDefinedObject.LinkDefinition List[NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition]@endlink):  Array of links (with the given link type) stored with this UDO .
        """
        pass
    
    ##  Gets the links with the given link type that are stored in the specified range with this UDO 
    ##  @return links (@link UserDefinedObject.LinkDefinition List[NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition]@endlink):  Array of links stored within the specified  
    ##                                                         range of the link type's link array for this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The type of links you wish to get 
    @overload
    def GetLinks(self, udo: UserDefinedObject, link_type: UserDefinedObject.LinkType, offset: int, length: int) -> List[UserDefinedObject.LinkDefinition]:
        """
         Gets the links with the given link type that are stored in the specified range with this UDO 
         @return links (@link UserDefinedObject.LinkDefinition List[NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition]@endlink):  Array of links stored within the specified  
                                                                range of the link type's link array for this UDO .
        """
        pass
    
    ##  Gets all of the strings stored with this UDO 
    ##  @return strings (List[str]):  Array of strings stored with this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="udo"> (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) </param>
    @staticmethod
    @overload
    def GetStrings(self, udo: UserDefinedObject) -> List[str]:
        """
         Gets all of the strings stored with this UDO 
         @return strings (List[str]):  Array of strings stored with this UDO .
        """
        pass
    
    ##  Gets the strings stored in the specified range with this UDO 
    ##  @return strings (List[str]):  Array of strings stored within the specified  
    ##                                                         range of the string array for this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of strings at the start of the 
    ##                                                 returned range.
    ##                                                 Valid values are 0 through (number of strings in the udo - 1)
    ##                                                 and -(number of strings in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the string array.  
    ##                                                 Therefore using -1 or (number of strings in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def GetStrings(self, udo: UserDefinedObject, offset: int, length: int) -> List[str]:
        """
         Gets the strings stored in the specified range with this UDO 
         @return strings (List[str]):  Array of strings stored within the specified  
                                                                range of the string array for this UDO .
        """
        pass
    
    ##  Gets the @link NXOpen::Features::UserDefinedObjectFeature NXOpen::Features::UserDefinedObjectFeature@endlink  associated with this UDO, if there isn't an associated feature, NULL is returned 
    ##  @return udo_feature (@link NXOpen.Features.UserDefinedObjectFeature NXOpen.Features.UserDefinedObjectFeature@endlink):  The UserDefinedObjectFeature associated this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetUserDefinedObjectFeature(udo: UserDefinedObject) -> NXOpen.Features.UserDefinedObjectFeature:
        """
         Gets the @link NXOpen::Features::UserDefinedObjectFeature NXOpen::Features::UserDefinedObjectFeature@endlink  associated with this UDO, if there isn't an associated feature, NULL is returned 
         @return udo_feature (@link NXOpen.Features.UserDefinedObjectFeature NXOpen.Features.UserDefinedObjectFeature@endlink):  The UserDefinedObjectFeature associated this UDO .
        """
        pass
    
    ##  Gets the out of date indicator (status) of this UDO 
    ##  @return status (int):  The status of this UDO 
    ##             0 - The UDO is up to date
    ##             1 - Out of date due to addition or deletion of links to the UDO
    ##             2 - Out of date due to update being performed on an associated (linked) object in the absence of a UDO Method
    ##             3 - Out of date due to addition or deletion of links to the UDO AND update being performed on an Associated (linked) object in the absence of a UDO Method 
    ##             4 - Out of date due to deletion of associated (linked) objects in the absence of a UDO method 
    ##             5 - Out of date due to addition or deletion of links to the UDO AND deletion of associated (linked) objects in the absence of a UDO method 
    ##             6 - Out of date due to update being performed on an associated (linked) object in the absence of a UDO Method AND deletion of associated (linked) objects in the absence of a UDO method 
    ##             7 - Out of date due to addition or deletion of links to the UDO AND update being performed on an Associated (linked) object in the absence of a UDO Method AND deletion of associated (linked) objects in the absence of a UDO method .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetUserDefinedObjectStatus(udo: UserDefinedObject) -> int:
        """
         Gets the out of date indicator (status) of this UDO 
         @return status (int):  The status of this UDO 
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
    
    ##  Gets all of the volumes stored with this UDO 
    ##  @return volumes (List[float]):  Array of volumes stored with this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="udo"> (@link UserDefinedObject NXOpen.UserDefinedObjects.UserDefinedObject@endlink) </param>
    @staticmethod
    @overload
    def GetVolumes(self, udo: UserDefinedObject) -> List[float]:
        """
         Gets all of the volumes stored with this UDO 
         @return volumes (List[float]):  Array of volumes stored with this UDO .
        """
        pass
    
    ##  Gets the volumes stored in the specified range with this UDO 
    ##  @return volumes (List[float]):  Array of volumes stored within the specified  
    ##                                                         range of the volume array for this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of volumes at the start of the 
    ##                                                 returned range.
    ##                                                 Valid values are 0 through (number of volumes in the udo - 1)
    ##                                                 and -(number of volumes in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the volume array.  
    ##                                                 Therefore using -1 or (number of volumes in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def GetVolumes(self, udo: UserDefinedObject, offset: int, length: int) -> List[float]:
        """
         Gets the volumes stored in the specified range with this UDO 
         @return volumes (List[float]):  Array of volumes stored within the specified  
                                                                range of the volume array for this UDO .
        """
        pass
    
    ##  Removes the areas stored at the end of the area array for this UDO, 
    ##             and returns them in an array 
    ##  @return areas (List[float]):  Array of areas that have been 
    ##                                                           removed from this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="num_areas"> (int) </param>
    def PopAreas(udo: UserDefinedObject, num_areas: int) -> List[float]:
        """
         Removes the areas stored at the end of the area array for this UDO, 
                    and returns them in an array 
         @return areas (List[float]):  Array of areas that have been 
                                                                  removed from this UDO .
        """
        pass
    
    ##  Removes the doubles stored at the end of the double array for this UDO, 
    ##             and returns them in an array 
    ##  @return doubles (List[float]):  Array of doubles that have been 
    ##                                                           removed from this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="num_doubles"> (int) </param>
    def PopDoubles(udo: UserDefinedObject, num_doubles: int) -> List[float]:
        """
         Removes the doubles stored at the end of the double array for this UDO, 
                    and returns them in an array 
         @return doubles (List[float]):  Array of doubles that have been 
                                                                  removed from this UDO .
        """
        pass
    
    ##  Removes the integers stored at the end of the integer array for this UDO, 
    ##             and returns them in an array 
    ##  @return integers (List[int]):  Array of integers that have been 
    ##                                                           removed from this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="num_integers"> (int) </param>
    def PopIntegers(udo: UserDefinedObject, num_integers: int) -> List[int]:
        """
         Removes the integers stored at the end of the integer array for this UDO, 
                    and returns them in an array 
         @return integers (List[int]):  Array of integers that have been 
                                                                  removed from this UDO .
        """
        pass
    
    ##  Removes the lengths stored at the end of the length array for this UDO, 
    ##             and returns them in an array 
    ##  @return lengths (List[float]):  Array of lengths that have been 
    ##                                                           removed from this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="num_lengths"> (int) </param>
    def PopLengths(udo: UserDefinedObject, num_lengths: int) -> List[float]:
        """
         Removes the lengths stored at the end of the length array for this UDO, 
                    and returns them in an array 
         @return lengths (List[float]):  Array of lengths that have been 
                                                                  removed from this UDO .
        """
        pass
    
    ##  Removes the links stored at the end of the given link type's link array for this UDO, 
    ##             and returns them in an array 
    ##  @return links (@link UserDefinedObject.LinkDefinition List[NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition]@endlink):  Array of links (with the given link type) that have been 
    ##                                                           removed from this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The type of links you wish to remove 
    def PopLinks(udo: UserDefinedObject, link_type: UserDefinedObject.LinkType, num_links: int) -> List[UserDefinedObject.LinkDefinition]:
        """
         Removes the links stored at the end of the given link type's link array for this UDO, 
                    and returns them in an array 
         @return links (@link UserDefinedObject.LinkDefinition List[NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition]@endlink):  Array of links (with the given link type) that have been 
                                                                  removed from this UDO .
        """
        pass
    
    ##  Removes the strings stored at the end of the string array for this UDO, 
    ##             and returns them in an array 
    ##  @return strings (List[str]):  Array of strings that have been 
    ##                                                           removed from this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="num_strings"> (int) </param>
    def PopStrings(udo: UserDefinedObject, num_strings: int) -> List[str]:
        """
         Removes the strings stored at the end of the string array for this UDO, 
                    and returns them in an array 
         @return strings (List[str]):  Array of strings that have been 
                                                                  removed from this UDO .
        """
        pass
    
    ##  Removes the volumes stored at the end of the volume array for this UDO, 
    ##             and returns them in an array 
    ##  @return volumes (List[float]):  Array of volumes that have been 
    ##                                                           removed from this UDO .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="num_volumes"> (int) </param>
    def PopVolumes(udo: UserDefinedObject, num_volumes: int) -> List[float]:
        """
         Removes the volumes stored at the end of the volume array for this UDO, 
                    and returns them in an array 
         @return volumes (List[float]):  Array of volumes that have been 
                                                                  removed from this UDO .
        """
        pass
    
    ##  Add the specified areas to the end of the area array for this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of new areas to add to this UDO.
    ##                                                          This routine is cumulutive, and will not remove
    ##                                                          any areas already stored with the UDO.
    ##                                                          It simply adds these new areas to the end of
    ##                                                          the existing area array and increases 
    ##                                                          the total number of areas stored with the UDO 
    def PushAreas(udo: UserDefinedObject, areas: List[float]) -> None:
        """
         Add the specified areas to the end of the area array for this UDO 
        """
        pass
    
    ##  Add the specified doubles to the end of the double array for this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of new doubles to add to this UDO.
    ##                                                          This routine is cumulutive, and will not remove
    ##                                                          any doubles already stored with the UDO.
    ##                                                          It simply adds these new doubles to the end of
    ##                                                          the existing double array and increases 
    ##                                                          the total number of doubles stored with the UDO 
    def PushDoubles(udo: UserDefinedObject, doubles: List[float]) -> None:
        """
         Add the specified doubles to the end of the double array for this UDO 
        """
        pass
    
    ##  Add the specified integers to the end of the integer array for this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of new integers to add to this UDO.
    ##                                                          This routine is cumulutive, and will not remove
    ##                                                          any integers already stored with the UDO.
    ##                                                          It simply adds these new integers to the end of
    ##                                                          the existing integer array and increases 
    ##                                                          the total number of integers stored with the UDO 
    def PushIntegers(udo: UserDefinedObject, integers: List[int]) -> None:
        """
         Add the specified integers to the end of the integer array for this UDO 
        """
        pass
    
    ##  Add the specified lengths to the end of the length array for this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of new lengths to add to this UDO.
    ##                                                          This routine is cumulutive, and will not remove
    ##                                                          any lengths already stored with the UDO.
    ##                                                          It simply adds these new lengths to the end of
    ##                                                          the existing length array and increases 
    ##                                                          the total number of lengths stored with the UDO 
    def PushLengths(udo: UserDefinedObject, lengths: List[float]) -> None:
        """
         Add the specified lengths to the end of the length array for this UDO 
        """
        pass
    
    ##  Add the specified links to the end of the given link type's link array for this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The type of links you wish to add 
    def PushLinks(udo: UserDefinedObject, link_type: UserDefinedObject.LinkType, links: List[UserDefinedObject.LinkDefinition]) -> None:
        """
         Add the specified links to the end of the given link type's link array for this UDO 
        """
        pass
    
    ##  Add the specified strings to the end of the string array for this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of new strings to add to this UDO.
    ##                                                          This routine is cumulutive, and will not remove
    ##                                                          any strings already stored with the UDO.
    ##                                                          It simply adds these new strings to the end of
    ##                                                          the existing string array and increases 
    ##                                                          the total number of strings stored with the UDO 
    def PushStrings(udo: UserDefinedObject, strings: List[str]) -> None:
        """
         Add the specified strings to the end of the string array for this UDO 
        """
        pass
    
    ##  Add the specified volumes to the end of the volume array for this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Array of new volumes to add to this UDO.
    ##                                                          This routine is cumulutive, and will not remove
    ##                                                          any volumes already stored with the UDO.
    ##                                                          It simply adds these new volumes to the end of
    ##                                                          the existing volume array and increases 
    ##                                                          the total number of volumes stored with the UDO 
    def PushVolumes(udo: UserDefinedObject, volumes: List[float]) -> None:
        """
         Add the specified volumes to the end of the volume array for this UDO 
        """
        pass
    
    ##  Sets all of the areas stored with this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  New Array of areas stored with this UDO 
    @overload
    def SetAreas(self, udo: UserDefinedObject, areas: List[float]) -> None:
        """
         Sets all of the areas stored with this UDO 
        """
        pass
    
    ##  Replaces the areas stored with this UDO in the specified range with a new array of areas 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of areas at the start of the 
    ##                                                 range you wish to cut and replace.
    ##                                                 Valid values are 0 through (number of areas in the udo - 1)
    ##                                                 and -(number of areas in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the area array.  
    ##                                                 Therefore using -1 or (number of areas in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def SetAreas(self, udo: UserDefinedObject, offset: int, length: int, areas: List[float]) -> None:
        """
         Replaces the areas stored with this UDO in the specified range with a new array of areas 
        """
        pass
    
    ##  Sets all of the doubles stored with this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  New Array of doubles stored with this UDO 
    @overload
    def SetDoubles(self, udo: UserDefinedObject, doubles: List[float]) -> None:
        """
         Sets all of the doubles stored with this UDO 
        """
        pass
    
    ##  Replaces the doubles stored with this UDO in the specified range with a new array of doubles 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of doubles at the start of the 
    ##                                                 range you wish to cut and replace.
    ##                                                 Valid values are 0 through (number of doubles in the udo - 1)
    ##                                                 and -(number of doubles in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the double array.  
    ##                                                 Therefore using -1 or (number of doubles in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def SetDoubles(self, udo: UserDefinedObject, offset: int, length: int, doubles: List[float]) -> None:
        """
         Replaces the doubles stored with this UDO in the specified range with a new array of doubles 
        """
        pass
    
    ##  Sets all of the integers stored with this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  New Array of integers stored with this UDO 
    @overload
    def SetIntegers(self, udo: UserDefinedObject, integers: List[int]) -> None:
        """
         Sets all of the integers stored with this UDO 
        """
        pass
    
    ##  Replaces the integers stored with this UDO in the specified range with a new array of integers 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of integers at the start of the 
    ##                                                 range you wish to cut and replace.
    ##                                                 Valid values are 0 through (number of integers in the udo - 1)
    ##                                                 and -(number of integers in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the integer array.  
    ##                                                 Therefore using -1 or (number of integers in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def SetIntegers(self, udo: UserDefinedObject, offset: int, length: int, integers: List[int]) -> None:
        """
         Replaces the integers stored with this UDO in the specified range with a new array of integers 
        """
        pass
    
    ##  Sets all of the lengths stored with this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  New Array of lengths stored with this UDO 
    @overload
    def SetLengths(self, udo: UserDefinedObject, lengths: List[float]) -> None:
        """
         Sets all of the lengths stored with this UDO 
        """
        pass
    
    ##  Replaces the lengths stored with this UDO in the specified range with a new array of lengths 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of lengths at the start of the 
    ##                                                 range you wish to cut and replace.
    ##                                                 Valid values are 0 through (number of lengths in the udo - 1)
    ##                                                 and -(number of lengths in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the length array.  
    ##                                                 Therefore using -1 or (number of lengths in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def SetLengths(self, udo: UserDefinedObject, offset: int, length: int, lengths: List[float]) -> None:
        """
         Replaces the lengths stored with this UDO in the specified range with a new array of lengths 
        """
        pass
    
    ##  Sets all of the links with the given link type stored with this UDO.
    ##             If you already had objects linked to the UDO via the specified link type,
    ##             this operation will over-write them with the newly specified links. 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The type of links you wish to set 
    @overload
    def SetLinks(self, udo: UserDefinedObject, link_type: UserDefinedObject.LinkType, links: List[UserDefinedObject.LinkDefinition]) -> None:
        """
         Sets all of the links with the given link type stored with this UDO.
                    If you already had objects linked to the UDO via the specified link type,
                    this operation will over-write them with the newly specified links. 
        """
        pass
    
    ##  Replaces the links of the given link type stored with this UDO in the specified range with a new array of links 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  The type of links you wish to set 
    @overload
    def SetLinks(self, udo: UserDefinedObject, link_type: UserDefinedObject.LinkType, offset: int, length: int, links: List[UserDefinedObject.LinkDefinition]) -> None:
        """
         Replaces the links of the given link type stored with this UDO in the specified range with a new array of links 
        """
        pass
    
    ##  Sets all of the strings stored with this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  New Array of strings stored with this UDO 
    @overload
    def SetStrings(self, udo: UserDefinedObject, strings: List[str]) -> None:
        """
         Sets all of the strings stored with this UDO 
        """
        pass
    
    ##  Replaces the strings stored with this UDO in the specified range with a new array of strings 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of strings at the start of the 
    ##                                                 range you wish to cut and replace.
    ##                                                 Valid values are 0 through (number of strings in the udo - 1)
    ##                                                 and -(number of strings in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the string array.  
    ##                                                 Therefore using -1 or (number of strings in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def SetStrings(self, udo: UserDefinedObject, offset: int, length: int, strings: List[str]) -> None:
        """
         Replaces the strings stored with this UDO in the specified range with a new array of strings 
        """
        pass
    
    ##  Sets all of the volumes stored with this UDO 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  New Array of volumes stored with this UDO 
    @overload
    def SetVolumes(self, udo: UserDefinedObject, volumes: List[float]) -> None:
        """
         Sets all of the volumes stored with this UDO 
        """
        pass
    
    ##  Replaces the volumes stored with this UDO in the specified range with a new array of volumes 
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ##  Index into the array of volumes at the start of the 
    ##                                                 range you wish to cut and replace.
    ##                                                 Valid values are 0 through (number of volumes in the udo - 1)
    ##                                                 and -(number of volumes in the udo) through -1.
    ##                                                 If the offset is negative, it is used to count back 
    ##                                                 from the end of the volume array.  
    ##                                                 Therefore using -1 or (number of volumes in the udo -1)
    ##                                                 for the offset will give the same result. 
    @overload
    def SetVolumes(self, udo: UserDefinedObject, offset: int, length: int, volumes: List[float]) -> None:
        """
         Replaces the volumes stored with this UDO in the specified range with a new array of volumes 
        """
        pass
    
## @package NXOpen.UserDefinedObjects
## Classes, Enums and Structs under NXOpen.UserDefinedObjects namespace

##  @link UserDefinedClassAllowOwnedObjectSelection NXOpen.UserDefinedObjects.UserDefinedClassAllowOwnedObjectSelection @endlink is an alias for @link UserDefinedClass.AllowOwnedObjectSelection NXOpen.UserDefinedObjects.UserDefinedClass.AllowOwnedObjectSelection@endlink
UserDefinedClassAllowOwnedObjectSelection = UserDefinedClass.AllowOwnedObjectSelection


##  @link UserDefinedClassAllowQueryClass NXOpen.UserDefinedObjects.UserDefinedClassAllowQueryClass @endlink is an alias for @link UserDefinedClass.AllowQueryClass NXOpen.UserDefinedObjects.UserDefinedClass.AllowQueryClass@endlink
UserDefinedClassAllowQueryClass = UserDefinedClass.AllowQueryClass


##  @link UserDefinedClassSelection NXOpen.UserDefinedObjects.UserDefinedClassSelection @endlink is an alias for @link UserDefinedClass.Selection NXOpen.UserDefinedObjects.UserDefinedClass.Selection@endlink
UserDefinedClassSelection = UserDefinedClass.Selection


##  @link UserDefinedEventReason NXOpen.UserDefinedObjects.UserDefinedEventReason @endlink is an alias for @link UserDefinedEvent.Reason NXOpen.UserDefinedObjects.UserDefinedEvent.Reason@endlink
UserDefinedEventReason = UserDefinedEvent.Reason


##  @link UserDefinedObjectDisplayContextFacetType NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextFacetType @endlink is an alias for @link UserDefinedObjectDisplayContext.FacetType NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.FacetType@endlink
UserDefinedObjectDisplayContextFacetType = UserDefinedObjectDisplayContext.FacetType


##  @link UserDefinedObjectDisplayContextPolyMarker NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextPolyMarker @endlink is an alias for @link UserDefinedObjectDisplayContext.PolyMarker NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.PolyMarker@endlink
UserDefinedObjectDisplayContextPolyMarker = UserDefinedObjectDisplayContext.PolyMarker


##  @link UserDefinedObjectDisplayContextStandardTextRef NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextStandardTextRef @endlink is an alias for @link UserDefinedObjectDisplayContext.StandardTextRef NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.StandardTextRef@endlink
UserDefinedObjectDisplayContextStandardTextRef = UserDefinedObjectDisplayContext.StandardTextRef


##  @link UserDefinedObjectDisplayContextTextRef NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextTextRef @endlink is an alias for @link UserDefinedObjectDisplayContext.TextRef NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.TextRef@endlink
UserDefinedObjectDisplayContextTextRef = UserDefinedObjectDisplayContext.TextRef


##  @link UserDefinedObjectDisplayContextTextSize NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextTextSize @endlink is an alias for @link UserDefinedObjectDisplayContext.TextSize NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.TextSize@endlink
UserDefinedObjectDisplayContextTextSize = UserDefinedObjectDisplayContext.TextSize


##  @link UserDefinedObjectDisplayContextViewMode NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContextViewMode @endlink is an alias for @link UserDefinedObjectDisplayContext.ViewMode NXOpen.UserDefinedObjects.UserDefinedObjectDisplayContext.ViewMode@endlink
UserDefinedObjectDisplayContextViewMode = UserDefinedObjectDisplayContext.ViewMode


## @link UserDefinedObjectManagerLinkedUdoDefinition_Struct NXOpen.UserDefinedObjects.UserDefinedObjectManagerLinkedUdoDefinition_Struct@endlink is an alias for @link UserDefinedObjectManager.LinkedUdoDefinition NXOpen.UserDefinedObjects.UserDefinedObjectManager.LinkedUdoDefinition@endlink.
UserDefinedObjectManagerLinkedUdoDefinition_Struct = UserDefinedObjectManager.LinkedUdoDefinition


## @link UserDefinedObjectLinkDefinition_Struct NXOpen.UserDefinedObjects.UserDefinedObjectLinkDefinition_Struct@endlink is an alias for @link UserDefinedObject.LinkDefinition NXOpen.UserDefinedObjects.UserDefinedObject.LinkDefinition@endlink.
UserDefinedObjectLinkDefinition_Struct = UserDefinedObject.LinkDefinition


##  @link UserDefinedObjectLinkStatus NXOpen.UserDefinedObjects.UserDefinedObjectLinkStatus @endlink is an alias for @link UserDefinedObject.LinkStatus NXOpen.UserDefinedObjects.UserDefinedObject.LinkStatus@endlink
UserDefinedObjectLinkStatus = UserDefinedObject.LinkStatus


##  @link UserDefinedObjectLinkType NXOpen.UserDefinedObjects.UserDefinedObjectLinkType @endlink is an alias for @link UserDefinedObject.LinkType NXOpen.UserDefinedObjects.UserDefinedObject.LinkType@endlink
UserDefinedObjectLinkType = UserDefinedObject.LinkType


