from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  This class is responsible for setting and getting NX Manager database attribute.  <br> Use @link PDM::PartBuilder::NewAlternateIdManager PDM::PartBuilder::NewAlternateIdManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class AlternateIdManager(NXOpen.TransientObject): 
    """ This class is responsible for setting and getting NX Manager database attribute. """


    ## Contains alternate Ids data 
    ## @link AlternateIdManagerAlternateIdsData_Struct NXOpen.PDM.AlternateIdManagerAlternateIdsData_Struct@endlink is an alias for @link AlternateIdManager.AlternateIdsData NXOpen.PDM.AlternateIdManager.AlternateIdsData@endlink.
    class AlternateIdsData:
        """
        Contains alternate Ids data 
        @link AlternateIdManagerAlternateIdsData_Struct NXOpen.PDM.AlternateIdManagerAlternateIdsData_Struct@endlink is an alias for @link AlternateIdManager.AlternateIdsData NXOpen.PDM.AlternateIdManager.AlternateIdsData@endlink.
        """
        ## Getter for property :(str) AlternateItemId
        ## the new value for the alternate item ID
        ## @return str
        @property
        def AlternateItemId(self) -> str:
            """
            Getter for property AlternateItemId
            the new value for the alternate item ID

            """
            pass
        
        ## Setter for property :(str) AlternateItemId
        @AlternateItemId.setter
        def AlternateItemId(self, value: str):
            """
            Getter for property AlternateItemId
            the new value for the alternate item ID
            Setter for property AlternateItemId
            the new value for the alternate item ID

            """
            pass
        
        ## Getter for property :(str) AlternateRevId
        ## the new value for the alternate Revision ID
        ## @return str
        @property
        def AlternateRevId(self) -> str:
            """
            Getter for property AlternateRevId
            the new value for the alternate Revision ID

            """
            pass
        
        ## Setter for property :(str) AlternateRevId
        @AlternateRevId.setter
        def AlternateRevId(self, value: str):
            """
            Getter for property AlternateRevId
            the new value for the alternate Revision ID
            Setter for property AlternateRevId
            the new value for the alternate Revision ID

            """
            pass
        
        ## Getter for property :(str) AlternateName
        ## the new value for the alternate Name
        ## @return str
        @property
        def AlternateName(self) -> str:
            """
            Getter for property AlternateName
            the new value for the alternate Name

            """
            pass
        
        ## Setter for property :(str) AlternateName
        @AlternateName.setter
        def AlternateName(self, value: str):
            """
            Getter for property AlternateName
            the new value for the alternate Name
            Setter for property AlternateName
            the new value for the alternate Name

            """
            pass
        
        ## Getter for property :(str) AlternateDescription
        ## the new value for the alternate Description
        ## @return str
        @property
        def AlternateDescription(self) -> str:
            """
            Getter for property AlternateDescription
            the new value for the alternate Description

            """
            pass
        
        ## Setter for property :(str) AlternateDescription
        @AlternateDescription.setter
        def AlternateDescription(self, value: str):
            """
            Getter for property AlternateDescription
            the new value for the alternate Description
            Setter for property AlternateDescription
            the new value for the alternate Description

            """
            pass
        
        ## Getter for property :(bool) Modifiable
        ## the new value for the alternate for modifiable flag
        ## @return bool
        @property
        def Modifiable(self) -> bool:
            """
            Getter for property Modifiable
            the new value for the alternate for modifiable flag

            """
            pass
        
        ## Setter for property :(bool) Modifiable
        @Modifiable.setter
        def Modifiable(self, value: bool):
            """
            Getter for property Modifiable
            the new value for the alternate for modifiable flag
            Setter for property Modifiable
            the new value for the alternate for modifiable flag

            """
            pass
        
    
    
    ## Contains alternate Revision Id data 
    ## @link AlternateIdManagerAssignAlternateRevData_Struct NXOpen.PDM.AlternateIdManagerAssignAlternateRevData_Struct@endlink is an alias for @link AlternateIdManager.AssignAlternateRevData NXOpen.PDM.AlternateIdManager.AssignAlternateRevData@endlink.
    class AssignAlternateRevData:
        """
        Contains alternate Revision Id data 
        @link AlternateIdManagerAssignAlternateRevData_Struct NXOpen.PDM.AlternateIdManagerAssignAlternateRevData_Struct@endlink is an alias for @link AlternateIdManager.AssignAlternateRevData NXOpen.PDM.AlternateIdManager.AssignAlternateRevData@endlink.
        """
        ## Getter for property :(str) AlternateRevId
        ## the new value the alternate Revision ID
        ## @return str
        @property
        def AlternateRevId(self) -> str:
            """
            Getter for property AlternateRevId
            the new value the alternate Revision ID

            """
            pass
        
        ## Setter for property :(str) AlternateRevId
        @AlternateRevId.setter
        def AlternateRevId(self, value: str):
            """
            Getter for property AlternateRevId
            the new value the alternate Revision ID
            Setter for property AlternateRevId
            the new value the alternate Revision ID

            """
            pass
        
        ## Getter for property :(bool) Modifiable
        ## the new value of flag for revision modifiable
        ## @return bool
        @property
        def Modifiable(self) -> bool:
            """
            Getter for property Modifiable
            the new value of flag for revision modifiable

            """
            pass
        
        ## Setter for property :(bool) Modifiable
        @Modifiable.setter
        def Modifiable(self, value: bool):
            """
            Getter for property Modifiable
            the new value of flag for revision modifiable
            Setter for property Modifiable
            the new value of flag for revision modifiable

            """
            pass
        
    
    
    ##  This method generates alternate item and revision IDs and sets these generated
    ##         values on this manager class. Note that the ID context and type must be set on the
    ##         builder in order for this assign operation to be successful. 
    ##  @return A tuple consisting of (alternate_item_id, alternate_rev_id). 
    ##  - alternate_item_id is: str. the newly generated alternate item ID value
    ##                                                that was set on this manager .
    ##  - alternate_rev_id is: str. the newly generated alternate revision ID value
    ##                                                that was set on this manager .

    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def AssignAlternateId(self) -> Tuple[str, str]:
        """
         This method generates alternate item and revision IDs and sets these generated
                values on this manager class. Note that the ID context and type must be set on the
                builder in order for this assign operation to be successful. 
         @return A tuple consisting of (alternate_item_id, alternate_rev_id). 
         - alternate_item_id is: str. the newly generated alternate item ID value
                                                       that was set on this manager .
         - alternate_rev_id is: str. the newly generated alternate revision ID value
                                                       that was set on this manager .

        """
        pass
    
    ##  Generates the alternate ID information by calling
    ##         @link AssignAlternateIds AssignAlternateIds@endlink  . Returns pointer to  PDM.Altids.AlternateIdsData object. 
    ##         Sets Alternate Name,Alternate Id,Alternate Revision ,Alternate Description,
    ##         flag for alternate Id modifiable and flag for revision modifiable into Alternate Manager object.
    ##         
    ##  @return alt_info (@link AlternateIdManager.AlternateIdsData NXOpen.PDM.AlternateIdManager.AlternateIdsData@endlink): Contains alternate Ids data .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="context"> (str)  the context </param>
    ## <param name="id_type"> (str)  the Id type </param>
    def AssignAlternateIds(self, context: str, id_type: str) -> AlternateIdManager.AlternateIdsData:
        """
         Generates the alternate ID information by calling
                @link AssignAlternateIds AssignAlternateIds@endlink  . Returns pointer to  PDM.Altids.AlternateIdsData object. 
                Sets Alternate Name,Alternate Id,Alternate Revision ,Alternate Description,
                flag for alternate Id modifiable and flag for revision modifiable into Alternate Manager object.
                
         @return alt_info (@link AlternateIdManager.AlternateIdsData NXOpen.PDM.AlternateIdManager.AlternateIdsData@endlink): Contains alternate Ids data .
        """
        pass
    
    ##  This method generates an alternate rev ID and sets this generated value on
    ##         this manager class.  Note that the ID context and type must be set on the
    ##         builder in order for this assign operation to be successful. 
    ##  @return alternate_rev_id (str):  the newly generated alternate rev ID
    ##                                                value that was set on this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def AssignAlternateRevId(self) -> str:
        """
         This method generates an alternate rev ID and sets this generated value on
                this manager class.  Note that the ID context and type must be set on the
                builder in order for this assign operation to be successful. 
         @return alternate_rev_id (str):  the newly generated alternate rev ID
                                                       value that was set on this manager .
        """
        pass
    
    ##  Generates the alternate Revision ID information. 
    ##         Sets Alternate Revision and flag for revision modifiable into Alternate Manager object.
    ##         
    ##  @return revInfo (@link AlternateIdManager.AssignAlternateRevData NXOpen.PDM.AlternateIdManager.AssignAlternateRevData@endlink): Contains alternate Revision Id data .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def AssignAlternateRevision(self) -> AlternateIdManager.AssignAlternateRevData:
        """
         Generates the alternate Revision ID information. 
                Sets Alternate Revision and flag for revision modifiable into Alternate Manager object.
                
         @return revInfo (@link AlternateIdManager.AssignAlternateRevData NXOpen.PDM.AlternateIdManager.AssignAlternateRevData@endlink): Contains alternate Revision Id data .
        """
        pass
    
    ##  Adds the alternate ID information set by calling
    ##         @link SetAlternateIdInformation SetAlternateIdInformation@endlink  and the various "assign" and "set"
    ##         methods. The context, ID type, alternate ID, alternate revision ID, and the
    ##         alternate name must all be set before calling this method. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def CreateAlternateIdInformation(self) -> None:
        """
         Adds the alternate ID information set by calling
                @link SetAlternateIdInformation SetAlternateIdInformation@endlink  and the various "assign" and "set"
                methods. The context, ID type, alternate ID, alternate revision ID, and the
                alternate name must all be set before calling this method. 
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Gets a list of all the available contexts. 
    ##  @return contexts (List[str]):  list of contexts .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetAllContexts(self) -> List[str]:
        """
         Gets a list of all the available contexts. 
         @return contexts (List[str]):  list of contexts .
        """
        pass
    
    ##  Gets a list of all the available ID types for a given context. 
    ##  @return id_types (List[str]):  list of ID types .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="context"> (str)  the context </param>
    def GetAllIdTypes(self, context: str) -> List[str]:
        """
         Gets a list of all the available ID types for a given context. 
         @return id_types (List[str]):  list of ID types .
        """
        pass
    
    ##  Gets the value of a alternate name as it is currently set on this manager class. 
    ##  @return alternate_description (str):  the current value of the alternate
    ##                                                     description on this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetAlternateDescription(self) -> str:
        """
         Gets the value of a alternate name as it is currently set on this manager class. 
         @return alternate_description (str):  the current value of the alternate
                                                            description on this manager .
        """
        pass
    
    ##  Gets (as it is currently set on this manager class) whether the
    ##         alternate ID information should be the default indentifier. 
    ##  @return alternate_id_as_default_indentifier (bool):  the current value of option
    ##                                                                     on this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetAlternateIdAsDefaultIndentifier(self) -> bool:
        """
         Gets (as it is currently set on this manager class) whether the
                alternate ID information should be the default indentifier. 
         @return alternate_id_as_default_indentifier (bool):  the current value of option
                                                                            on this manager .
        """
        pass
    
    ##  Gets the value of a alternate ID as it is currently set on this manager class. 
    ##  @return alternate_item_id (str):  the current value of the alternate item ID on this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetAlternateItemId(self) -> str:
        """
         Gets the value of a alternate ID as it is currently set on this manager class. 
         @return alternate_item_id (str):  the current value of the alternate item ID on this manager .
        """
        pass
    
    ##  Gets the value of a alternate name as it is currently set on this manager class. 
    ##  @return alternate_name (str):  the current value of the alternate name on
    ##                                              this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetAlternateName(self) -> str:
        """
         Gets the value of a alternate name as it is currently set on this manager class. 
         @return alternate_name (str):  the current value of the alternate name on
                                                     this manager .
        """
        pass
    
    ##  Gets the value of a alternate rev ID as it is currently set on this manager class. 
    ##  @return alternate_rev_id (str):  the current value of the alternate rev ID
    ##                                                on this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetAlternateRevId(self) -> str:
        """
         Gets the value of a alternate rev ID as it is currently set on this manager class. 
         @return alternate_rev_id (str):  the current value of the alternate rev ID
                                                       on this manager .
        """
        pass
    
    ##  Gets the value of a context as it is currently set on this manager class. 
    ##  @return context (str):  the current value of the context on this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetContext(self) -> str:
        """
         Gets the value of a context as it is currently set on this manager class. 
         @return context (str):  the current value of the context on this manager .
        """
        pass
    
    ##  Gets the value of a ID type as it is currently set on this manager class. 
    ##  @return id_type (str):  the current value of the ID type on this manager .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetIdType(self) -> str:
        """
         Gets the value of a ID type as it is currently set on this manager class. 
         @return id_type (str):  the current value of the ID type on this manager .
        """
        pass
    
    ##  Sets the value of the alternate description. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="alternate_description"> (str)  the new value the alternate description
    ##                                                      is to be set to </param>
    def SetAlternateDescription(self, alternate_description: str) -> None:
        """
         Sets the value of the alternate description. 
        """
        pass
    
    ##  Sets whether the alternate ID information should be the default indentifier. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="alternate_id_as_default_indentifier"> (bool)  the new value the option
    ##                                                               is to be set to </param>
    def SetAlternateIdAsDefaultIndentifier(self, alternate_id_as_default_indentifier: bool) -> None:
        """
         Sets whether the alternate ID information should be the default indentifier. 
        """
        pass
    
    ##  Sets alternate ID information on this manager class. NULL can be specified
    ##         for parameters which are set via other set or assign methods on this builder. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="context"> (str)  the new value the context is to be set to </param>
    ## <param name="id_type"> (str)  the new value the ID type is to be set to </param>
    ## <param name="alternate_item_id"> (str)  the new value the alternate item ID is to be set to </param>
    ## <param name="alternate_rev_id"> (str)  the new value the alternate rev ID
    ##                                                 is to be set to </param>
    ## <param name="alternate_name"> (str)  the new value the alternate name is to be set to </param>
    ## <param name="alternate_description"> (str)  the new value the alternate description
    ##                                                       is to be set to </param>
    ## <param name="alternate_id_as_default_indentifier"> (bool)  the new value the option
    ##                                                                is to be set to </param>
    def SetAlternateIdInformation(self, context: str, id_type: str, alternate_item_id: str, alternate_rev_id: str, alternate_name: str, alternate_description: str, alternate_id_as_default_indentifier: bool) -> None:
        """
         Sets alternate ID information on this manager class. NULL can be specified
                for parameters which are set via other set or assign methods on this builder. 
        """
        pass
    
    ##  Sets the value of the alternate item ID. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="alternate_item_id"> (str)  the new value the alternate item ID is to be set to </param>
    def SetAlternateItemId(self, alternate_item_id: str) -> None:
        """
         Sets the value of the alternate item ID. 
        """
        pass
    
    ##  Sets the value of the alternate name. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="alternate_name"> (str)  the new value the alternate name is to be set to </param>
    def SetAlternateName(self, alternate_name: str) -> None:
        """
         Sets the value of the alternate name. 
        """
        pass
    
    ##  Sets the value of the alternate rev ID. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="alternate_rev_id"> (str)  the new value the alternate rev ID
    ##                                                 is to be set to </param>
    def SetAlternateRevId(self, alternate_rev_id: str) -> None:
        """
         Sets the value of the alternate rev ID. 
        """
        pass
    
    ##  Sets the value of a context. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="context"> (str)  the new value the context is to be set to </param>
    def SetContext(self, context: str) -> None:
        """
         Sets the value of a context. 
        """
        pass
    
    ##  Sets the value of an ID type. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="id_type"> (str)  the new value the ID type is to be set to </param>
    def SetIdType(self, id_type: str) -> None:
        """
         Sets the value of an ID type. 
        """
        pass
    
import NXOpen
##  Represents a ASSY_clone_comp_disp class  <br> Instances of this class can only be accessed through the Clone or Export applications.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AssyCloneCompDisp(NXOpen.NXObject): 
    """ Represents a ASSY_clone_comp_disp class """
    pass


import NXOpen
##  Represents a collection of attribute group objects.  A smaller list of attribute groups can be
##     retrieved by using the method @link NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroups NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroups@endlink 
##     for classes that implement the @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink  interface.   <br> To obtain an instance of this class, refer to @link NXOpen::CollaborativeDesign  NXOpen::CollaborativeDesign @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class AttributeGroupCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of attribute group objects.  A smaller list of attribute groups can be
    retrieved by using the method <ja_method>NXOpen.PDM.IAttributeGroupOwner.GetAttributeGroups</ja_method>
    for classes that implement the <ja_class>NXOpen.PDM.IAttributeGroupOwner</ja_class> interface.  """


    ##  Finds the @link  NXOpen::PDM::AttributeGroup   NXOpen::PDM::AttributeGroup @endlink  with the given identifier as recorded in a journal. 
    ##     An object may not return the same value as its JournalIdentifier in different versions of 
    ##     the software. However newer versions of the software should find the same object when 
    ##     FindObject is passed older versions of its journal identifier. In general, this method 
    ##     should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##     An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link AttributeGroup NXOpen.PDM.AttributeGroup@endlink):  AttributeGroup found, or null if no such attribute group exists.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Journal identifier to be found </param>
    def FindObject(self, journal_identifier: str) -> AttributeGroup:
        """
         Finds the @link  NXOpen::PDM::AttributeGroup   NXOpen::PDM::AttributeGroup @endlink  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.
        
            An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link AttributeGroup NXOpen.PDM.AttributeGroup@endlink):  AttributeGroup found, or null if no such attribute group exists.
        """
        pass
    
import NXOpen
##  Represents a collection of attribute group description objects.  A smaller list of attribute groups
##     descriptions can be retrieved by using the method
##     @link NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroupDescriptions NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroupDescriptions@endlink 
##     for classes that implement the @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink  interface. <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class AttributeGroupDescriptionCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of attribute group description objects.  A smaller list of attribute groups
    descriptions can be retrieved by using the method
    <ja_method>NXOpen.PDM.IAttributeGroupOwner.GetAttributeGroupDescriptions</ja_method>
    for classes that implement the <ja_class>NXOpen.PDM.IAttributeGroupOwner</ja_class> interface."""


    ##  Finds the @link  NXOpen::PDM::AttributeGroupDescription   NXOpen::PDM::AttributeGroupDescription @endlink  with the given identifier as recorded in a journal. 
    ##     An object may not return the same value as its JournalIdentifier in different versions of 
    ##     the software. However newer versions of the software should find the same object when 
    ##     FindObject is passed older versions of its journal identifier. In general, this method 
    ##     should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##     An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link AttributeGroupDescription NXOpen.PDM.AttributeGroupDescription@endlink):  AttributeGroupDescription found, or null if no such attribute group description exists.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Journal identifier to be found </param>
    def FindObject(self, journal_identifier: str) -> AttributeGroupDescription:
        """
         Finds the @link  NXOpen::PDM::AttributeGroupDescription   NXOpen::PDM::AttributeGroupDescription @endlink  with the given identifier as recorded in a journal. 
            An object may not return the same value as its JournalIdentifier in different versions of 
            the software. However newer versions of the software should find the same object when 
            FindObject is passed older versions of its journal identifier. In general, this method 
            should not be used in handwritten code and exists to support record and playback of journals.
        
            An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link AttributeGroupDescription NXOpen.PDM.AttributeGroupDescription@endlink):  AttributeGroupDescription found, or null if no such attribute group description exists.
        """
        pass
    
import NXOpen
##  Represents an attribute group type.  <br> PDM.AttributeGroupDescription object cannot be created.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class AttributeGroupDescription(NXOpen.NXObject): 
    """ Represents an attribute group type. """


    ## Getter for property: (str) DisplayName
    ##  Returns the display name for the attribute group description.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the display name for the attribute group description.  
             
         
        """
        pass
    
    ## Getter for property: (int) MaximumNumberOfAttributeGroupsAllowed
    ##  Returns the maximum number of attribute groups of this type that can be assigned to an object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def MaximumNumberOfAttributeGroupsAllowed(self) -> int:
        """
        Getter for property: (int) MaximumNumberOfAttributeGroupsAllowed
         Returns the maximum number of attribute groups of this type that can be assigned to an object.  
              
         
        """
        pass
    
    ## Getter for property: (int) MinimumNumberOfAttributeGroupsAllowed
    ##  Returns the minimum number of attribute groups of this type that can be assigned to an object.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return int
    @property
    def MinimumNumberOfAttributeGroupsAllowed(self) -> int:
        """
        Getter for property: (int) MinimumNumberOfAttributeGroupsAllowed
         Returns the minimum number of attribute groups of this type that can be assigned to an object.  
              
         
        """
        pass
    
import NXOpen
##  Represents an attribute group revise builder.  Given a list of existing attribute groups for an
##     attribute group owner, a new revision for each attribute group is created.
## 
##     Note: The @link Builder::Commit Builder::Commit@endlink  returns NULL for this builder.  Use the 
##     @link NXOpen::PDM::AttributeGroupReviseBuilder::GetRevisedAttributeGroups NXOpen::PDM::AttributeGroupReviseBuilder::GetRevisedAttributeGroups@endlink  to get the
##     successfully revised attribute groups after the builder is committed.
##   <br> Use @link NXOpen::PDM::IAttributeGroupOwner::CreateAttributeGroupReviseBuilder NXOpen::PDM::IAttributeGroupOwner::CreateAttributeGroupReviseBuilder@endlink  to create an instance of this class  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class AttributeGroupReviseBuilder(NXOpen.Builder): 
    """ Represents an attribute group revise builder.  Given a list of existing attribute groups for an
    attribute group owner, a new revision for each attribute group is created.

    Note: The <ja_method>Builder.Commit</ja_method> returns <ja_NULL> for this builder.  Use the 
    <ja_method>NXOpen.PDM.AttributeGroupReviseBuilder.GetRevisedAttributeGroups</ja_method> to get the
    successfully revised attribute groups after the builder is committed.
 """


    ##  Represents the save as action on a managed attribute group 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NewRevision</term><description> 
    ## </description> </item><item><term> 
    ## NewAttributeGroup</term><description> 
    ## </description> </item></list>
    class SaveAsActionType(Enum):
        """
        Members Include: <NewRevision> <NewAttributeGroup>
        """
        NewRevision: int
        NewAttributeGroup: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AttributeGroupReviseBuilder.SaveAsActionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns list of logical objects created by the builder for use during the revise operation. 
    ##  @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetLogicalObjects(self) -> List[LogicalObject]:
        """
         Returns list of logical objects created by the builder for use during the revise operation. 
         @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink):   .
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::OperationErrors NXOpen::PDM::OperationErrors@endlink  object containing
    ##         information about the attribute groups that failed to revise. 
    ##  @return operationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetOperationErrors(self) -> OperationErrors:
        """
         Returns the @link NXOpen::PDM::OperationErrors NXOpen::PDM::OperationErrors@endlink  object containing
                information about the attribute groups that failed to revise. 
         @return operationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink): .
        """
        pass
    
    ##  Returns the operation failures during revise of the attribute groups 
    ##  @return operationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns the operation failures during revise of the attribute groups 
         @return operationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
        """
        pass
    
    ##  Returns a list of attribute groups for use during the revise operation.  Before the builder is committed
    ##         this list of attribute groups is used to set any required user attribute.  The attribute groups do
    ##         not exist in Teamcenter until the builder is committed.  After the builder is committed the list only
    ##         contains successfully revised attribute groups.  Any attribute groups that failed to revise are removed
    ##         from the list and are no longer valid after commit.  Call this method after commit to get a list of the
    ##         successfully revised attribute groups. 
    ##  @return attributeGroups (@link AttributeGroup List[NXOpen.PDM.AttributeGroup]@endlink):   .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetRevisedAttributeGroups(self) -> List[AttributeGroup]:
        """
         Returns a list of attribute groups for use during the revise operation.  Before the builder is committed
                this list of attribute groups is used to set any required user attribute.  The attribute groups do
                not exist in Teamcenter until the builder is committed.  After the builder is committed the list only
                contains successfully revised attribute groups.  Any attribute groups that failed to revise are removed
                from the list and are no longer valid after commit.  Call this method after commit to get a list of the
                successfully revised attribute groups. 
         @return attributeGroups (@link AttributeGroup List[NXOpen.PDM.AttributeGroup]@endlink):   .
        """
        pass
    
import NXOpen
##  Represents an attribute group.  <br> KF not supported.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class AttributeGroup(NXOpen.NXObject): 
    """ Represents an attribute group. """


    ## Getter for property: (str) DisplayName
    ##  Returns the display name for the attribute group.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def DisplayName(self) -> str:
        """
        Getter for property: (str) DisplayName
         Returns the display name for the attribute group.  
             
         
        """
        pass
    
    ##  Detaches Attribute Group 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeGroupOwner"> (@link IAttributeGroupOwner NXOpen.PDM.IAttributeGroupOwner@endlink) </param>
    def DetachAttributeGroup(self, attributeGroupOwner: IAttributeGroupOwner) -> None:
        """
         Detaches Attribute Group 
        """
        pass
    
    ##  Returns a list of @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink  objects referencing this attribute group. 
    ##  @return attributeGroupOwners (@link IAttributeGroupOwner List[NXOpen.PDM.IAttributeGroupOwner]@endlink):   .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetReferencingAttributeGroupOwners(self) -> List[IAttributeGroupOwner]:
        """
         Returns a list of @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink  objects referencing this attribute group. 
         @return attributeGroupOwners (@link IAttributeGroupOwner List[NXOpen.PDM.IAttributeGroupOwner]@endlink):   .
        """
        pass
    
##  This search filter term can be used to filter based on attributes.  <br> To create a new instance of this class, use @link NXOpen::PDM::SearchRecipeFilterBuilder::CreateAttributeTerm  NXOpen::PDM::SearchRecipeFilterBuilder::CreateAttributeTerm @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class AttributeSearchFilterTerm(SearchFilterTerm): 
    """ This search filter term can be used to filter based on attributes. """


    ##  This function adds a property value to the filter. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="internalValue"> (str) </param>
    ## <param name="displayValue"> (str) </param>
    def AddValue(self, internalValue: str, displayValue: str) -> None:
        """
         This function adds a property value to the filter. 
        """
        pass
    
    ##  This function removes all property values from the filter. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    def ClearAllValues(self) -> None:
        """
         This function removes all property values from the filter. 
        """
        pass
    
    ##  This function gets whether the term is excluded or included. 
    ##  @return excludeToggle (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetExcludeToggle(self) -> bool:
        """
         This function gets whether the term is excluded or included. 
         @return excludeToggle (bool): .
        """
        pass
    
    ##  This function checks if the search filter term has a specified value. 
    ##  @return hasValue (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="internalValue"> (str) </param>
    def HasValue(self, internalValue: str) -> bool:
        """
         This function checks if the search filter term has a specified value. 
         @return hasValue (bool): .
        """
        pass
    
    ##  This function removes a property value from the filter. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="internalValue"> (str) </param>
    def RemoveValue(self, internalValue: str) -> None:
        """
         This function removes a property value from the filter. 
        """
        pass
    
    ##  This function sets whether the term is excluded or included. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="excludeToggle"> (bool) </param>
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets whether the term is excluded or included. 
        """
        pass
    
import NXOpen
##   @brief  This class is used for executing CAE Clone on a Simulation File or a FeModel File.
##      
## 
##    <br> Use @link NXOpen::PDM::PartManager NXOpen::PDM::PartManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

class CaeCloneManager(NXOpen.TransientObject): 
    """ <summary> This class is used for executing CAE Clone on a Simulation File or a FeModel File.
    </summary> """


    ##  Option for creation of part builder for CAE Clone 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ## </description> </item><item><term> 
    ## Sim</term><description> 
    ##  </description> </item><item><term> 
    ## Fem</term><description> 
    ##  </description> </item><item><term> 
    ## Ideal</term><description> 
    ##  </description> </item><item><term> 
    ## Master</term><description> 
    ##  </description> </item></list>
    class CloneOption(Enum):
        """
        Members Include: <NotSet> <Sim> <Fem> <Ideal> <Master>
        """
        NotSet: int
        Sim: int
        Fem: int
        Ideal: int
        Master: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> CaeCloneManager.CloneOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Commits the Clone Operation for the Clone Manager class @link NXOpen::PDM::CaeCloneManager NXOpen::PDM::CaeCloneManager@endlink .
    ##         Deletes all the Part Builders associated with the Clone Manager
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def CommitClone(self) -> None:
        """
         Commits the Clone Operation for the Clone Manager class @link NXOpen::PDM::CaeCloneManager NXOpen::PDM::CaeCloneManager@endlink .
                Deletes all the Part Builders associated with the Clone Manager
                
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ## 
    ##         Gets the container in Teamcenter where the cloned part is saved
    ##         
    ##  @return container (str): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="option"> (@link CaeCloneManager.CloneOption NXOpen.PDM.CaeCloneManager.CloneOption@endlink) </param>
    def GetContainer(self, option: CaeCloneManager.CloneOption) -> str:
        """
        
                Gets the container in Teamcenter where the cloned part is saved
                
         @return container (str): .
        """
        pass
    
    ##  Get Part Builders for Clone Operation of a CAE Simulation or a CAE Model part.  
    ##         Get  builder class @link NXOpen::PDM::PartFromPartBuilder NXOpen::PDM::PartFromPartBuilder@endlink  using this function.
    ##         
    ##  @return part_builder (@link PartFromPartBuilder NXOpen.PDM.PartFromPartBuilder@endlink):  the part builder .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="option"> (@link CaeCloneManager.CloneOption NXOpen.PDM.CaeCloneManager.CloneOption@endlink) </param>
    def GetPartBuilderForClone(self, option: CaeCloneManager.CloneOption) -> PartFromPartBuilder:
        """
         Get Part Builders for Clone Operation of a CAE Simulation or a CAE Model part.  
                Get  builder class @link NXOpen::PDM::PartFromPartBuilder NXOpen::PDM::PartFromPartBuilder@endlink  using this function.
                
         @return part_builder (@link PartFromPartBuilder NXOpen.PDM.PartFromPartBuilder@endlink):  the part builder .
        """
        pass
    
    ## 
    ##         Sets the container in Teamcenter where the cloned part is saved
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="option"> (@link CaeCloneManager.CloneOption NXOpen.PDM.CaeCloneManager.CloneOption@endlink) </param>
    ## <param name="container"> (str) </param>
    def SetContainer(self, option: CaeCloneManager.CloneOption, container: str) -> None:
        """
        
                Sets the container in Teamcenter where the cloned part is saved
                
        """
        pass
    
    ## 
    ##         Sets the option for include master on the Clone Manager class 
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="value"> (bool) </param>
    def SetIncludeMaster(self, value: bool) -> None:
        """
        
                Sets the option for include master on the Clone Manager class 
                
        """
        pass
    
import NXOpen
##   @brief  This class is a File Container class for uploading JT files created by NX CAE Post Processing to Teamcenter. 
##     Users can add the JT file names and their corresponding dataset names to this container class.
##     Once all the JT file names are added, this class can be used to upload the JT files to Teamcenter.
##     The class can be used to upload only to a a single part at a time.
##      
## 
##    <br> Use @link NXOpen::PDM::PdmSession NXOpen::PDM::PdmSession@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class CAEFileContainer(NXOpen.TransientObject): 
    """ <summary> This class is a File Container class for uploading JT files created by NX CAE Post Processing to Teamcenter. 
    Users can add the JT file names and their corresponding dataset names to this container class.
    Once all the JT file names are added, this class can be used to upload the JT files to Teamcenter.
    The class can be used to upload only to a a single part at a time.
    </summary> """


    ##   Add a file to the list of files in the file container class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="datasetname"> (str) </param>
    ## <param name="filename"> (str) </param>
    def AddFile(self, datasetname: str, filename: str) -> None:
        """
          Add a file to the list of files in the file container class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
        """
        pass
    
    ##   Delete a file from the list of files in the file container class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="datasetname"> (str) </param>
    ## <param name="filename"> (str) </param>
    def DeleteFile(self, datasetname: str, filename: str) -> None:
        """
          Delete a file from the list of files in the file container class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##   Upload CAE files to Teamcenter, independent of a standard file->save.  
    ##         Upload all the files in the file container class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink  using this function.
    ##         The JT files should be present in the temporary directory of the system prior to calling this function.
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def DoUpload(self) -> None:
        """
          Upload CAE files to Teamcenter, independent of a standard file->save.  
                Upload all the files in the file container class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink  using this function.
                The JT files should be present in the temporary directory of the system prior to calling this function.
                
        """
        pass
    
    ##  Get the part tag of the owning part of the class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
    ##  @return partspec (str): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    def GetOwningPart(self) -> str:
        """
         Get the part tag of the owning part of the class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
         @return partspec (str): .
        """
        pass
    
    ##  Sets the part tag of the owning part of the class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## 
    ## <param name="partspec"> (str) </param>
    def SetOwningPart(self, partspec: str) -> None:
        """
         Sets the part tag of the owning part of the class @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink .
        """
        pass
    
##  This enum is used to specify the CAE types related to the component that should be pulled into the operation. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## SimFemIdeal</term><description> 
## </description> </item><item><term> 
## FemIdeal</term><description> 
## </description> </item><item><term> 
## Ideal</term><description> 
## </description> </item><item><term> 
## NotSet</term><description> 
## </description> </item></list>
class CloneRelatedCae(Enum):
    """
    Members Include: <SimFemIdeal> <FemIdeal> <Ideal> <NotSet>
    """
    SimFemIdeal: int
    FemIdeal: int
    Ideal: int
    NotSet: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> CloneRelatedCae:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  
##         Represents a base class that provides common methods for various conditional model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Instance of this class can not be created  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ConditionalElementRevision(ModelElement): 
    """ 
        Represents a base class that provides common methods for various conditional model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """


    ## Getter for property: (str) EffectivityFormula
    ##  Returns the formula string that represents the effectivity of this object in database.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return str
    @property
    def EffectivityFormula(self) -> str:
        """
        Getter for property: (str) EffectivityFormula
         Returns the formula string that represents the effectivity of this object in database.  
          
                  
         
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::PDM::ConfigurationManager::CreateConfigurationContextBuilder  NXOpen::PDM::ConfigurationManager::CreateConfigurationContextBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ConfigurationContextBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.PDM.ConfigurationContextBuilder</ja_class> builder """


    ##  configuration mode 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Nx4gd</term><description> 
    ## </description> </item><item><term> 
    ## Assemblies</term><description> 
    ## </description> </item><item><term> 
    ## ReturnConfigContextDontSetCurrent</term><description> 
    ## </description> </item><item><term> 
    ## CustomConfigContext</term><description> 
    ## </description> </item></list>
    class ConfigContextMode(Enum):
        """
        Members Include: <Nx4gd> <Assemblies> <ReturnConfigContextDontSetCurrent> <CustomConfigContext>
        """
        Nx4gd: int
        Assemblies: int
        ReturnConfigContextDontSetCurrent: int
        CustomConfigContext: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurationContextBuilder.ConfigContextMode:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  configuration type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AsSaved</term><description> 
    ## </description> </item><item><term> 
    ## PushedfromTeamcenter</term><description> 
    ## </description> </item><item><term> 
    ## DefineorLoadContext</term><description> 
    ## </description> </item></list>
    class ConfigContextType(Enum):
        """
        Members Include: <AsSaved> <PushedfromTeamcenter> <DefineorLoadContext>
        """
        AsSaved: int
        PushedfromTeamcenter: int
        DefineorLoadContext: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurationContextBuilder.ConfigContextType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  configuration detail 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## LoadfromTeamcenter</term><description> 
    ## </description> </item><item><term> 
    ## DefineinNX</term><description> 
    ## </description> </item></list>
    class ConfigurationDetail(Enum):
        """
        Members Include: <LoadfromTeamcenter> <DefineinNX>
        """
        LoadfromTeamcenter: int
        DefineinNX: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ConfigurationContextBuilder.ConfigurationDetail:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) CollaborativeDesign
    ##  Returns the collaborative design   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.CollaborativeDesign
    @property
    def CollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) CollaborativeDesign
         Returns the collaborative design   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) CollaborativeDesign

    ##  Returns the collaborative design   
    ##     
    ##  
    ## Setter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @CollaborativeDesign.setter
    def CollaborativeDesign(self, collaborativeDesign: NXOpen.CollaborativeDesign):
        """
        Setter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) CollaborativeDesign
         Returns the collaborative design   
            
         
        """
        pass
    
    ## Getter for property: (@link ConfigurationContextBuilder.ConfigurationDetail NXOpen.PDM.ConfigurationContextBuilder.ConfigurationDetail@endlink) ConfigDetail
    ##  Returns the configuration detail   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ConfigurationContextBuilder.ConfigurationDetail
    @property
    def ConfigDetail(self) -> ConfigurationContextBuilder.ConfigurationDetail:
        """
        Getter for property: (@link ConfigurationContextBuilder.ConfigurationDetail NXOpen.PDM.ConfigurationContextBuilder.ConfigurationDetail@endlink) ConfigDetail
         Returns the configuration detail   
            
         
        """
        pass
    
    ## Setter for property: (@link ConfigurationContextBuilder.ConfigurationDetail NXOpen.PDM.ConfigurationContextBuilder.ConfigurationDetail@endlink) ConfigDetail

    ##  Returns the configuration detail   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConfigDetail.setter
    def ConfigDetail(self, configDetail: ConfigurationContextBuilder.ConfigurationDetail):
        """
        Setter for property: (@link ConfigurationContextBuilder.ConfigurationDetail NXOpen.PDM.ConfigurationContextBuilder.ConfigurationDetail@endlink) ConfigDetail
         Returns the configuration detail   
            
         
        """
        pass
    
    ## Getter for property: (@link ConfigurationContextBuilder.ConfigContextMode NXOpen.PDM.ConfigurationContextBuilder.ConfigContextMode@endlink) ConfigMode
    ##  Returns the configuration mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ConfigurationContextBuilder.ConfigContextMode
    @property
    def ConfigMode(self) -> ConfigurationContextBuilder.ConfigContextMode:
        """
        Getter for property: (@link ConfigurationContextBuilder.ConfigContextMode NXOpen.PDM.ConfigurationContextBuilder.ConfigContextMode@endlink) ConfigMode
         Returns the configuration mode   
            
         
        """
        pass
    
    ## Getter for property: (@link ConfigurationContextBuilder.ConfigContextType NXOpen.PDM.ConfigurationContextBuilder.ConfigContextType@endlink) ConfigType
    ##  Returns the configuration type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return ConfigurationContextBuilder.ConfigContextType
    @property
    def ConfigType(self) -> ConfigurationContextBuilder.ConfigContextType:
        """
        Getter for property: (@link ConfigurationContextBuilder.ConfigContextType NXOpen.PDM.ConfigurationContextBuilder.ConfigContextType@endlink) ConfigType
         Returns the configuration type   
            
         
        """
        pass
    
    ## Setter for property: (@link ConfigurationContextBuilder.ConfigContextType NXOpen.PDM.ConfigurationContextBuilder.ConfigContextType@endlink) ConfigType

    ##  Returns the configuration type   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @ConfigType.setter
    def ConfigType(self, configType: ConfigurationContextBuilder.ConfigContextType):
        """
        Setter for property: (@link ConfigurationContextBuilder.ConfigContextType NXOpen.PDM.ConfigurationContextBuilder.ConfigContextType@endlink) ConfigType
         Returns the configuration type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.ContentDefinition NXOpen.ContentDefinition@endlink) ContentDefinition
    ##  Returns the @link NXOpen::ContentDefinition NXOpen::ContentDefinition@endlink  of the subset.  
    ##    
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.ContentDefinition
    @property
    def ContentDefinition(self) -> NXOpen.ContentDefinition:
        """
        Getter for property: (@link NXOpen.ContentDefinition NXOpen.ContentDefinition@endlink) ContentDefinition
         Returns the @link NXOpen::ContentDefinition NXOpen::ContentDefinition@endlink  of the subset.  
           
                  
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.ContentDefinition NXOpen.ContentDefinition@endlink) ContentDefinition

    ##  Returns the @link NXOpen::ContentDefinition NXOpen::ContentDefinition@endlink  of the subset.  
    ##    
    ##           
    ##  
    ## Setter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @ContentDefinition.setter
    def ContentDefinition(self, contentDefinition: NXOpen.ContentDefinition):
        """
        Setter for property: (@link NXOpen.ContentDefinition NXOpen.ContentDefinition@endlink) ContentDefinition
         Returns the @link NXOpen::ContentDefinition NXOpen::ContentDefinition@endlink  of the subset.  
           
                  
         
        """
        pass
    
    ## Getter for property: (@link EffectivityTableBuilder NXOpen.PDM.EffectivityTableBuilder@endlink) EffectivityTable
    ##  Returns the @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  builder used to edit the effectivity   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return EffectivityTableBuilder
    @property
    def EffectivityTable(self) -> EffectivityTableBuilder:
        """
        Getter for property: (@link EffectivityTableBuilder NXOpen.PDM.EffectivityTableBuilder@endlink) EffectivityTable
         Returns the @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  builder used to edit the effectivity   
            
         
        """
        pass
    
    ## Getter for property: (str) OverrideFolder
    ##  Returns the override folder   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def OverrideFolder(self) -> str:
        """
        Getter for property: (str) OverrideFolder
         Returns the override folder   
            
         
        """
        pass
    
    ## Setter for property: (str) OverrideFolder

    ##  Returns the override folder   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @OverrideFolder.setter
    def OverrideFolder(self, folderName: str):
        """
        Setter for property: (str) OverrideFolder
         Returns the override folder   
            
         
        """
        pass
    
    ## Getter for property: (str) RevisionRule
    ##  Returns the revision rule    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def RevisionRule(self) -> str:
        """
        Getter for property: (str) RevisionRule
         Returns the revision rule    
            
         
        """
        pass
    
    ## Setter for property: (str) RevisionRule

    ##  Returns the revision rule    
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @RevisionRule.setter
    def RevisionRule(self, revisionRule: str):
        """
        Setter for property: (str) RevisionRule
         Returns the revision rule    
            
         
        """
        pass
    
    ## Getter for property: (@link VariantConfigurationBuilder NXOpen.PDM.VariantConfigurationBuilder@endlink) VariantConfiguration
    ##  Returns the @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink  builder used to edit variant rule configuration   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return VariantConfigurationBuilder
    @property
    def VariantConfiguration(self) -> VariantConfigurationBuilder:
        """
        Getter for property: (@link VariantConfigurationBuilder NXOpen.PDM.VariantConfigurationBuilder@endlink) VariantConfiguration
         Returns the @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink  builder used to edit variant rule configuration   
            
         
        """
        pass
    
import NXOpen
##  Represents a Teamcenter Integration configuration context  <br> A ConfigurationContext is obtained from an @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink   <br> 
## 
##   <br>  Created in NX2206.0.0  <br> 

class ConfigurationContext(NXOpen.NXObject): 
    """ Represents a Teamcenter Integration configuration context """
    pass


import NXOpen
##  Represents Configuration Manager   <br> Use @link NXOpen::Session::ConfigurationManager NXOpen::Session::ConfigurationManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ConfigurationManager(NXOpen.Object): 
    """ Represents Configuration Manager  """


    ##  Creates a new @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink  object for 
    ##             @link  NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeAssemblies   NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeAssemblies @endlink 
    ##             mode configuration. 
    ##  @return builder (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def CreateConfigurationContextBuilder() -> ConfigurationContextBuilder:
        """
         Creates a new @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink  object for 
                    @link  NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeAssemblies   NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeAssemblies @endlink 
                    mode configuration. 
         @return builder (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink  object for 
    ##             @link  NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeReturnConfigContextDontSetCurrent   NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeReturnConfigContextDontSetCurrent @endlink 
    ##             mode configuration. 
    ##  @return builder (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def CreateConfigurationContextBuilderForMultiConfig() -> ConfigurationContextBuilder:
        """
         Creates a new @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink  object for 
                    @link  NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeReturnConfigContextDontSetCurrent   NXOpen::PDM::ConfigurationContextBuilder::ConfigContextModeReturnConfigContextDontSetCurrent @endlink 
                    mode configuration. 
         @return builder (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink  object which maintains custom config context of product part in design workset. 
    ##  @return builder (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_designworkset (" Design Workset")
    ## <param name="worksetPart"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="subsetPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateDesignWorksetProductConfigurationContextBuilder(worksetPart: NXOpen.NXObject, subsetPartOcc: NXOpen.NXObject) -> ConfigurationContextBuilder:
        """
         Creates a new @link NXOpen::PDM::ConfigurationContextBuilder NXOpen::PDM::ConfigurationContextBuilder@endlink  object which maintains custom config context of product part in design workset. 
         @return builder (@link ConfigurationContextBuilder NXOpen.PDM.ConfigurationContextBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::EffectivityAttributePropertiesBuilder NXOpen::PDM::EffectivityAttributePropertiesBuilder@endlink  object. 
    ##  @return builder (@link EffectivityAttributePropertiesBuilder NXOpen.PDM.EffectivityAttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  The part that owns the builder. The builder owner is not
    ##                                                     strictly required (that is, it can be NULL), but it is
    ##                                                     highly suggested to ensure proper cleanup of the builder in
    ##                                                     case the client does not explicitly clean it up properly.  </param>
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreateEffectivityAttributePropertiesBuilder(part: NXOpen.BasePart, objects: List[NXOpen.NXObject]) -> EffectivityAttributePropertiesBuilder:
        """
         Creates a new @link NXOpen::PDM::EffectivityAttributePropertiesBuilder NXOpen::PDM::EffectivityAttributePropertiesBuilder@endlink  object. 
         @return builder (@link EffectivityAttributePropertiesBuilder NXOpen.PDM.EffectivityAttributePropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink  object. 
    ##  @return builder (@link VariantRulesConfigurationBuilder NXOpen.PDM.VariantRulesConfigurationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::PDM::PdmManager::CreateVariantRulesConfigurationBuilder NXOpen::PDM::PdmManager::CreateVariantRulesConfigurationBuilder@endlink  instead  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  The part that owns the builder. The builder owner is not
    ##                                                     strictly required (that is, it can be NULL), but it is
    ##                                                     highly suggested to ensure proper cleanup of the builder in
    ##                                                     case the client does not explicitly clean it up properly.  </param>
    def CreateVariantRulesConfigurationBuilder(part: NXOpen.BasePart) -> VariantRulesConfigurationBuilder:
        """
         Creates a new @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink  object. 
         @return builder (@link VariantRulesConfigurationBuilder NXOpen.PDM.VariantRulesConfigurationBuilder@endlink): .
        """
        pass
    
##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ConnectionElementRevision(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """
    pass


##  This enum is used to specify the name conversion rule for generating name/number for the operation candidates. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## WithPrefix</term><description> 
## </description> </item><item><term> 
## WithSuffix</term><description> 
## </description> </item><item><term> 
## WithReplaceString</term><description> 
## </description> </item><item><term> 
## WithRename</term><description> 
## </description> </item><item><term> 
## MixedRule</term><description> 
## </description> </item></list>
class ConversionRule(Enum):
    """
    Members Include: <WithPrefix> <WithSuffix> <WithReplaceString> <WithRename> <MixedRule>
    """
    WithPrefix: int
    WithSuffix: int
    WithReplaceString: int
    WithRename: int
    MixedRule: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ConversionRule:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents a builder class that performs Create operations  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateCreateSessionBuilder  NXOpen::PDM::PdmSession::CreateCreateSessionBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class CreateSessionBuilder(PartOperationCreateBuilder): 
    """ Represents a builder class that performs Create operations """


    ##  Auto assign session name 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def AutoAssignSessionNameOnPartSelection(self) -> None:
        """
         Auto assign session name 
        """
        pass
    
    ##  Creates the pre-creation objects for the parts 
    ##  @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def CreateLogicalObjectsForDialog(self) -> List[LogicalObject]:
        """
         Creates the pre-creation objects for the parts 
         @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
    ##  Returns the selected part 
    ##  @return selectedPartName (str): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetSelectedPart(self) -> str:
        """
         Returns the selected part 
         @return selectedPartName (str): .
        """
        pass
    
    ##  Returns the selected session type 
    ##  @return sessionType (int): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetSelectedSessionType(self) -> int:
        """
         Returns the selected session type 
         @return sessionType (int): .
        """
        pass
    
    ##  Returns all session types
    ##  @return sessionTypes (List[str]):  the session types .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetSessionTypes(self) -> List[str]:
        """
         Returns all session types
         @return sessionTypes (List[str]):  the session types .
        """
        pass
    
    ##  Returns logical value to indicate whether the session name is auto assigned 
    ##  @return allowSessionNameAutoAssignOnPartSelection (bool): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def IsAllowSessionNameAutoAssignOnPartSelection(self) -> bool:
        """
         Returns logical value to indicate whether the session name is auto assigned 
         @return allowSessionNameAutoAssignOnPartSelection (bool): .
        """
        pass
    
    ##  Sets logical value to indicate whether the session name is auto assigned 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="allowSessionNameAutoAssignOnPartSelection"> (bool) </param>
    def SetAllowSessionNameAutoAssignOnPartSelection(self, allowSessionNameAutoAssignOnPartSelection: bool) -> None:
        """
         Sets logical value to indicate whether the session name is auto assigned 
        """
        pass
    
    ##  Sets the selected part 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedPartName"> (str) </param>
    def SetSelectedPart(self, selectedPartName: str) -> None:
        """
         Sets the selected part 
        """
        pass
    
    ##  Sets the selected session type 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sessionType"> (int) </param>
    def SetSelectedSessionType(self, sessionType: int) -> None:
        """
         Sets the selected session type 
        """
        pass
    
##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class CrossSheetReference(ModelElement): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """
    pass


import NXOpen
##  Represents Custom WebApp Menu Handler class 
## 
##   <br>  Created in NX11.0.0  <br> 

class CustomWebAppMenuHandler(NXOpen.TransientObject): 
    """ Represents Custom WebApp Menu Handler class """


    ##  This callback will be invoked by NX when user clicks on a custom webapp menu item. The picked menu
    ##            and object(s) selected can be queried from within this callback.The custom implementation can 
    ##            perform appropriate action associated with this menu pick. 
    ## A callback definition with no input arguments and no return type
    CustomWebAppInvokedCallback = Callable[[], None]
    
    
    ##  Frees the object from memory.  After this method is called,
    ##            it is illegal to use the object.  In .NET, this method is automatically
    ##            called when the object is deleted by the garbage collector. 
    ##        
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                   it is illegal to use the object.  In .NET, this method is automatically
                   called when the object is deleted by the garbage collector. 
               
        """
        pass
    
    ##  Returns the command name 
    ##  @return command_name (str):  the command name .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetCommandName(self) -> str:
        """
         Returns the command name 
         @return command_name (str):  the command name .
        """
        pass
    
    ##  Returns the unique identifier of the uids in PDM 
    ##  @return uids (List[str]):  Selected uids .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetSelectedUids(self) -> List[str]:
        """
         Returns the unique identifier of the uids in PDM 
         @return uids (List[str]):  Selected uids .
        """
        pass
    
    ##  Registers the add_custom_web_app_menu_callback callback method with the webApp menu
    ##            handler object.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="webapp_cb"> (@link CustomWebAppMenuHandler.CustomWebAppInvokedCallback NXOpen.PDM.CustomWebAppMenuHandler.CustomWebAppInvokedCallback@endlink)  </param>
    def RegisterCustomWebAppInvokedCallback(self, webapp_cb: CustomWebAppMenuHandler.CustomWebAppInvokedCallback) -> None:
        """
         Registers the add_custom_web_app_menu_callback callback method with the webApp menu
                   handler object.
        """
        pass
    
import NXOpen
##  This class is responsible for setting and getting NX Manager database attribute.  <br> Use @link PDM::PartBuilder::NewDatabaseAttributeManager PDM::PartBuilder::NewDatabaseAttributeManager@endlink  or @link PDM::PdmPart::NewDatabaseAttributeManager PDM::PdmPart::NewDatabaseAttributeManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class DatabaseAttributeManager(NXOpen.TransientObject): 
    """ This class is responsible for setting and getting NX Manager database attribute. """


    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Gets the value of a writable database attribute. 
    ##  @return attribute_value (str):  the value of the attribute .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attribute_title"> (str)  the title of the attribute </param>
    def GetAttribute(self, attribute_title: str) -> str:
        """
         Gets the value of a writable database attribute. 
         @return attribute_value (str):  the value of the attribute .
        """
        pass
    
    ##  Load the Database Attributes from Teamcenter.
    ##         This operation will not discard any changes made in this session that aren't committed to Teamcenter.
    ##         If 'reload' is set to 'true', attributes that have already been loaded will be loaded again, if otherwise allowed.
    ##          
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="reload"> (bool)  Reload attributes that have already been loaded, if otherwise allowed. </param>
    def LoadAttributes(self, reload: bool) -> None:
        """
         Load the Database Attributes from Teamcenter.
                This operation will not discard any changes made in this session that aren't committed to Teamcenter.
                If 'reload' is set to 'true', attributes that have already been loaded will be loaded again, if otherwise allowed.
                 
        """
        pass
    
    ##  Recursively load the Database Attributes of this part and all its partially or fully loaded components from Teamcenter. 
    ##         This operation will not discard any changes made in this session that aren't committed to Teamcenter.
    ##          
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="reload"> (bool)  Reload attributes that have already been loaded, if otherwise allowed. </param>
    def LoadAttributesRecursively(self, reload: bool) -> None:
        """
         Recursively load the Database Attributes of this part and all its partially or fully loaded components from Teamcenter. 
                This operation will not discard any changes made in this session that aren't committed to Teamcenter.
                 
        """
        pass
    
    ##  Force load the Database Attributes from Teamcenter. This removes changes to values made in NX. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def RefreshAttributes(self) -> None:
        """
         Force load the Database Attributes from Teamcenter. This removes changes to values made in NX. 
        """
        pass
    
    ##  Sets the value of a writable database attribute. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attribute_title"> (str)  the title of the attribute to be set </param>
    ## <param name="attribute_value"> (str)  the new value the attribute is to be set to </param>
    def SetAttribute(self, attribute_title: str, attribute_value: str) -> None:
        """
         Sets the value of a writable database attribute. 
        """
        pass
    
    ##  Register DB_PART_NAME and DB_PART_DESC attributes with values set in the attribute_manager 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def StoreAttributes(self) -> None:
        """
         Register DB_PART_NAME and DB_PART_DESC attributes with values set in the attribute_manager 
        """
        pass
    
import NXOpen
##   @brief  This class is used for retrieving PDM database objects.  
## 
##    <br> Use @link PDM::PdmSession::GetDatabaseObjectManager PDM::PdmSession::GetDatabaseObjectManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DatabaseObjectManager(NXOpen.TransientObject): 
    """ <summary> This class is used for retrieving PDM database objects. </summary> """


    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  This API finds database object for specified design session search criteria in the Teamcenter database using saved query.
    ##         This API will return @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink  only if session name is unique, else it will return error.
    ##         Note: Search criteria parameter should contain object_name(Required), object_type(optional), UID(optional) etc.
    ##  @return databaseObject (@link DatabaseObject NXOpen.PDM.DatabaseObject@endlink):  Database object .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="designSessionParamNames"> (List[str])  search criteria titles </param>
    ## <param name="designSessionParamValues"> (List[str])  search criteria values </param>
    def FindDesignSessionObjects(self, designSessionParamNames: List[str], designSessionParamValues: List[str]) -> DatabaseObject:
        """
         This API finds database object for specified design session search criteria in the Teamcenter database using saved query.
                This API will return @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink  only if session name is unique, else it will return error.
                Note: Search criteria parameter should contain object_name(Required), object_type(optional), UID(optional) etc.
         @return databaseObject (@link DatabaseObject NXOpen.PDM.DatabaseObject@endlink):  Database object .
        """
        pass
    
    ##  This API finds database objects in the Teamcenter database using a Teamcenter saved query. 
    ##  @return databaseObjects (@link DatabaseObjects List[NXOpen.PDM.DatabaseObjects]@endlink):  Database objects .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="findCriterias"> (@link FindCriteria List[NXOpen.PDM.FindCriteria]@endlink)  Find critieria </param>
    def FindObjects(self, findCriterias: List[FindCriteria]) -> List[DatabaseObjects]:
        """
         This API finds database objects in the Teamcenter database using a Teamcenter saved query. 
         @return databaseObjects (@link DatabaseObjects List[NXOpen.PDM.DatabaseObjects]@endlink):  Database objects .
        """
        pass
    
    ##  Gets a database object from UID 
    ##  @return databaseObject (@link DatabaseObject NXOpen.PDM.DatabaseObject@endlink):  Database object .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="uId"> (str)  UID of the database identifier </param>
    def GetDatabaseObjectFromAppSessionUid(self, uId: str) -> DatabaseObject:
        """
         Gets a database object from UID 
         @return databaseObject (@link DatabaseObject NXOpen.PDM.DatabaseObject@endlink):  Database object .
        """
        pass
    
    ##  This API constructs a new @link NXOpen::PDM::DatabaseObjects NXOpen::PDM::DatabaseObjects@endlink  object. 
    ##  @return databaseObjects (@link DatabaseObjects NXOpen.PDM.DatabaseObjects@endlink):  Database objects .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def NewDatabaseobjects(self) -> DatabaseObjects:
        """
         This API constructs a new @link NXOpen::PDM::DatabaseObjects NXOpen::PDM::DatabaseObjects@endlink  object. 
         @return databaseObjects (@link DatabaseObjects NXOpen.PDM.DatabaseObjects@endlink):  Database objects .
        """
        pass
    
    ##  This API constructs an array of empty @link NXOpen::PDM::FindCriteria NXOpen::PDM::FindCriteria@endlink  objects. 
    ##  @return findCriterias (@link FindCriteria List[NXOpen.PDM.FindCriteria]@endlink):  Find criteria .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nCriteria"> (int) </param>
    def NewFindcriteria(self, nCriteria: int) -> List[FindCriteria]:
        """
         This API constructs an array of empty @link NXOpen::PDM::FindCriteria NXOpen::PDM::FindCriteria@endlink  objects. 
         @return findCriterias (@link FindCriteria List[NXOpen.PDM.FindCriteria]@endlink):  Find criteria .
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink . 
## 
##   <br>  Created in NX11.0.0  <br> 

class DatabaseObjects(NXOpen.TransientObject): 
    """ Represents a collection of <ja_class>NXOpen.PDM.DatabaseObject</ja_class>. """


    ##  This API appends to the collection of @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink . 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="databaseObjects"> (@link DatabaseObjects List[NXOpen.PDM.DatabaseObjects]@endlink)  Database objects </param>
    def Append(self, databaseObjects: List[DatabaseObjects]) -> None:
        """
         This API appends to the collection of @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink . 
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  This API returns the collection of @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink  as an array. 
    ##  @return databaseObjects (@link DatabaseObject List[NXOpen.PDM.DatabaseObject]@endlink):  Database objects .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetDatabaseObjects(self) -> List[DatabaseObject]:
        """
         This API returns the collection of @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink  as an array. 
         @return databaseObjects (@link DatabaseObject List[NXOpen.PDM.DatabaseObject]@endlink):  Database objects .
        """
        pass
    
    ##  This API sets the collection of @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink . 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="databaseObjects"> (@link DatabaseObject List[NXOpen.PDM.DatabaseObject]@endlink)  Database objects </param>
    def SetDatabaseObjects(self, databaseObjects: List[DatabaseObject]) -> None:
        """
         This API sets the collection of @link NXOpen::PDM::DatabaseObject NXOpen::PDM::DatabaseObject@endlink . 
        """
        pass
    
import NXOpen
##  Represents a Teamcenter database object 
## 
##   <br>  Created in NX11.0.0  <br> 

class DatabaseObject(NXOpen.TransientObject): 
    """ Represents a Teamcenter database object """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
import NXOpen
##  Represents a collection of @link NXOpen::PDM::DBEntityProxy NXOpen::PDM::DBEntityProxy@endlink  objects  <br> To obtain an instance of this class, refer to @link NXOpen::Part  NXOpen::Part @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class DBEntityProxyCollection(NXOpen.TaggedObjectCollection): 
    """ Represents a collection of <ja_class>NXOpen.PDM.DBEntityProxy</ja_class> objects """


    ##  Creates a @link NXOpen::PDM::DBEntityProxy NXOpen::PDM::DBEntityProxy@endlink  
    ##  @return dbentityProxy (@link DBEntityProxy NXOpen.PDM.DBEntityProxy@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="title"> (str) </param>
    ## <param name="index"> (int) </param>
    ## <param name="context"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    ## <param name="attributeOwner"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateDbEntityProxy(self, title: str, index: int, context: NXOpen.TaggedObject, attributeOwner: NXOpen.TaggedObject) -> DBEntityProxy:
        """
         Creates a @link NXOpen::PDM::DBEntityProxy NXOpen::PDM::DBEntityProxy@endlink  
         @return dbentityProxy (@link DBEntityProxy NXOpen.PDM.DBEntityProxy@endlink): .
        """
        pass
    
    ##  Find the DBEntityProxy object with input name 
    ##  @return found (@link NXOpen.NXObject NXOpen.NXObject@endlink):  DBEntity Object with this identifier .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="journal_identifier"> (str)  Identifier of the DBEntity object you want </param>
    def FindProxy(self, journal_identifier: str) -> NXOpen.NXObject:
        """
         Find the DBEntityProxy object with input name 
         @return found (@link NXOpen.NXObject NXOpen.NXObject@endlink):  DBEntity Object with this identifier .
        """
        pass
    
import NXOpen
##  JA class for the DBEntityProxy object <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class DBEntityProxy(NXOpen.NXObject): 
    """ JA class for the DBEntityProxy object"""
    pass


import NXOpen
## 
##         Represents the design element revision in the database. An instance of this class can be obtained from the @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink .
##      <br> Instance of this class can not be created  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class DesignElementRevision(ModelElementRevision): 
    """
        Represents the design element revision in the database. An instance of this class can be obtained from the <ja_class>NXOpen.Assemblies.Component</ja_class>.
    """


    ## 
    ##            Represents the category for this design element revision.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Shape</term><description> 
    ## </description> </item><item><term> 
    ## Reuse</term><description> 
    ## </description> </item><item><term> 
    ## Promissory</term><description> 
    ## </description> </item><item><term> 
    ## DesignControlElement</term><description> 
    ## </description> </item></list>
    class DesignElementCategory(Enum):
        """
        Members Include: <Shape> <Reuse> <Promissory> <DesignControlElement>
        """
        Shape: int
        Reuse: int
        Promissory: int
        DesignControlElement: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> DesignElementRevision.DesignElementCategory:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link DesignElementRevision.DesignElementCategory NXOpen.PDM.DesignElementRevision.DesignElementCategory@endlink) Category
    ##  Returns the category for design element.  
    ##    Category can be unknown 
    ##             if the design element is new and does not yet exist in database.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return DesignElementRevision.DesignElementCategory
    @property
    def Category(self) -> DesignElementRevision.DesignElementCategory:
        """
        Getter for property: (@link DesignElementRevision.DesignElementCategory NXOpen.PDM.DesignElementRevision.DesignElementCategory@endlink) Category
         Returns the category for design element.  
           Category can be unknown 
                    if the design element is new and does not yet exist in database.
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) DesignPart
    ##  Returns the part of the underlying design element.  
    ##    This can be NULL for a promissory design element.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return NXOpen.Part
    @property
    def DesignPart(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) DesignPart
         Returns the part of the underlying design element.  
           This can be NULL for a promissory design element.
                  
         
        """
        pass
    
    ## Getter for property: (bool) Modified
    ##  Returns
    ##             whether the selected @link NXOpen::PDM::DesignElementRevision NXOpen::PDM::DesignElementRevision@endlink  is modified in the session.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## @return bool
    @property
    def Modified(self) -> bool:
        """
        Getter for property: (bool) Modified
         Returns
                    whether the selected @link NXOpen::PDM::DesignElementRevision NXOpen::PDM::DesignElementRevision@endlink  is modified in the session.  
          
                  
         
        """
        pass
    
    ##  
    ##             Get the immediate child @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  objects.
    ##             This will return NULL.for non subordinate design element.
    ##          
    ##  @return designSubordinateRevision (@link DesignSubordinateRevision List[NXOpen.PDM.DesignSubordinateRevision]@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetDesignSubordinateRevisions(self) -> List[DesignSubordinateRevision]:
        """
         
                    Get the immediate child @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  objects.
                    This will return NULL.for non subordinate design element.
                 
         @return designSubordinateRevision (@link DesignSubordinateRevision List[NXOpen.PDM.DesignSubordinateRevision]@endlink): .
        """
        pass
    
    ##  Get the transform.
    ##             Note: The translation component is in meters.
    ##         
    ##  @return A tuple consisting of (orientation, positionInMeters). 
    ##  - orientation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.
    ##  - positionInMeters is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetTransform(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Point3d]:
        """
         Get the transform.
                    Note: The translation component is in meters.
                
         @return A tuple consisting of (orientation, positionInMeters). 
         - orientation is: @link NXOpen.Matrix3x3 NXOpen.Matrix3x3@endlink.
         - positionInMeters is: @link NXOpen.Point3d NXOpen.Point3d@endlink.

        """
        pass
    
## 
##         Represents the design feature revision in the database.
##      <br> Instance of this class can not be created  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class DesignFeatureRevision(ModelElementRevision): 
    """
        Represents the design feature revision in the database.
    """
    pass


import NXOpen
## 
##         Represents the design subordinate revision in the database. An instance of this class can be obtained from the @link NXOpen::Assemblies::Component NXOpen::Assemblies::Component@endlink .
##      <br> Instance of this class can not be created  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class DesignSubordinateRevision(ModelElementRevision): 
    """
        Represents the design subordinate revision in the database. An instance of this class can be obtained from the <ja_class>NXOpen.Assemblies.Component</ja_class>.
    """


    ## Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) DesignPart
    ##  Returns the underlying loaded part of this subordinate.  
    ##    Note that it will return NULL if part is not loaded.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.Part
    @property
    def DesignPart(self) -> NXOpen.Part:
        """
        Getter for property: (@link NXOpen.Part NXOpen.Part@endlink) DesignPart
         Returns the underlying loaded part of this subordinate.  
           Note that it will return NULL if part is not loaded.
                  
         
        """
        pass
    
    ## Getter for property: (bool) Modified
    ##  Returns
    ##             whether the selected @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  is modified in the session.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.3  <br> 

    ## @return bool
    @property
    def Modified(self) -> bool:
        """
        Getter for property: (bool) Modified
         Returns
                    whether the selected @link NXOpen::PDM::DesignSubordinateRevision NXOpen::PDM::DesignSubordinateRevision@endlink  is modified in the session.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link DesignElementRevision NXOpen.PDM.DesignElementRevision@endlink) RootDesignElementRevision
    ##  Returns the root reuse design element revision.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return DesignElementRevision
    @property
    def RootDesignElementRevision(self) -> DesignElementRevision:
        """
        Getter for property: (@link DesignElementRevision NXOpen.PDM.DesignElementRevision@endlink) RootDesignElementRevision
         Returns the root reuse design element revision.  
          
                  
         
        """
        pass
    
import NXOpen
## 
##         Represents an @link NXOpen::PDM::EffectivityAttributePropertiesBuilder NXOpen::PDM::EffectivityAttributePropertiesBuilder@endlink  to be used for creating effectivity attributes.
##         The attribute will be distributed to all objects supplied in the selected object list.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::ConfigurationManager::CreateEffectivityAttributePropertiesBuilder  NXOpen::PDM::ConfigurationManager::CreateEffectivityAttributePropertiesBuilder @endlink  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class EffectivityAttributePropertiesBuilder(NXOpen.Builder): 
    """
        Represents an <ja_class>NXOpen.PDM.EffectivityAttributePropertiesBuilder</ja_class> to be used for creating effectivity attributes.
        The attribute will be distributed to all objects supplied in the selected object list.
    """


    ## Getter for property: (str) Category
    ##  Returns the category.  
    ##     The category is an optional, user-defined string that allows 
    ##         attributes to be grouped together.   
    ##  
    ## Getter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Category(self) -> str:
        """
        Getter for property: (str) Category
         Returns the category.  
            The category is an optional, user-defined string that allows 
                attributes to be grouped together.   
         
        """
        pass
    
    ## Setter for property: (str) Category

    ##  Returns the category.  
    ##     The category is an optional, user-defined string that allows 
    ##         attributes to be grouped together.   
    ##  
    ## Setter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Category.setter
    def Category(self, category: str):
        """
        Setter for property: (str) Category
         Returns the category.  
            The category is an optional, user-defined string that allows 
                attributes to be grouped together.   
         
        """
        pass
    
    ## Getter for property: (str) DisplayValue
    ##  Returns the display value.  
    ##     Required if creating an attribute of type String.   
    ##  
    ## Getter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DisplayValue(self) -> str:
        """
        Getter for property: (str) DisplayValue
         Returns the display value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    
    ## Setter for property: (str) DisplayValue

    ##  Returns the display value.  
    ##     Required if creating an attribute of type String.   
    ##  
    ## Setter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DisplayValue.setter
    def DisplayValue(self, displayValue: str):
        """
        Setter for property: (str) DisplayValue
         Returns the display value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    
    ## Getter for property: (@link EffectivityTableBuilder NXOpen.PDM.EffectivityTableBuilder@endlink) EffectivityTableBuilder
    ##  Returns the effectivity table builder.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return EffectivityTableBuilder
    @property
    def EffectivityTableBuilder(self) -> EffectivityTableBuilder:
        """
        Getter for property: (@link EffectivityTableBuilder NXOpen.PDM.EffectivityTableBuilder@endlink) EffectivityTableBuilder
         Returns the effectivity table builder.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedObjects
    ##  Returns the selected object(s) list.  
    ##     The created attribute will be applied to
    ##         all objects in this list.    
    ##  
    ## Getter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def SelectedObjects(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) SelectedObjects
         Returns the selected object(s) list.  
            The created attribute will be applied to
                all objects in this list.    
         
        """
        pass
    
    ## Getter for property: (str) StringValue
    ##  Returns the string value.  
    ##     Required if creating an attribute of type String.   
    ##  
    ## Getter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def StringValue(self) -> str:
        """
        Getter for property: (str) StringValue
         Returns the string value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    
    ## Setter for property: (str) StringValue

    ##  Returns the string value.  
    ##     Required if creating an attribute of type String.   
    ##  
    ## Setter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @StringValue.setter
    def StringValue(self, stringValue: str):
        """
        Setter for property: (str) StringValue
         Returns the string value.  
            Required if creating an attribute of type String.   
         
        """
        pass
    
    ## Getter for property: (str) Title
    ##  Returns the attribute title.  
    ##     The title is required for creating an attribute
    ##         and must be unique on the given object.  Once the attribute is created,
    ##         the title cannot be modified.   
    ##  
    ## Getter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def Title(self) -> str:
        """
        Getter for property: (str) Title
         Returns the attribute title.  
            The title is required for creating an attribute
                and must be unique on the given object.  Once the attribute is created,
                the title cannot be modified.   
         
        """
        pass
    
    ## Setter for property: (str) Title

    ##  Returns the attribute title.  
    ##     The title is required for creating an attribute
    ##         and must be unique on the given object.  Once the attribute is created,
    ##         the title cannot be modified.   
    ##  
    ## Setter License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    @Title.setter
    def Title(self, title: str):
        """
        Setter for property: (str) Title
         Returns the attribute title.  
            The title is required for creating an attribute
                and must be unique on the given object.  Once the attribute is created,
                the title cannot be modified.   
         
        """
        pass
    
    ##  Create the attribute from the data set in the builder.  Unlike calling commit,
    ##         this method will not perform an update.  
    ##  @return changed (bool):  True if the attribute was created/edited successfully .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    def CreateAttribute(self) -> bool:
        """
         Create the attribute from the data set in the builder.  Unlike calling commit,
                this method will not perform an update.  
         @return changed (bool):  True if the attribute was created/edited successfully .
        """
        pass
    
    ##  Delete the attribute from the given object. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ## <param name="objectValue"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  The object containing the attribute </param>
    def Delete(self, objectValue: NXOpen.NXObject) -> None:
        """
         Delete the attribute from the given object. 
        """
        pass
    
    ##  Sets the array of objects that have this attribute 
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def SetAttributeObjects(self, objects: List[NXOpen.NXObject]) -> None:
        """
         Sets the array of objects that have this attribute 
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a builder class for effectivity configuration. 
## 
##   <br>  Created in NX9.0.0  <br> 

class EffectivityTableBuilder(NXOpen.TaggedObject): 
    """ Represents a builder class for effectivity configuration. """


    ##  Adds the given effectivity row to @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ## <param name="effectivityRow"> (@link EffectivityTableRow NXOpen.PDM.EffectivityTableRow@endlink) </param>
    def AddEffectivityRow(self, effectivityRow: EffectivityTableRow) -> None:
        """
         Adds the given effectivity row to @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  
        """
        pass
    
    ##  Commit the modified effectivity rows 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def Commit(self) -> None:
        """
         Commit the modified effectivity rows 
        """
        pass
    
    ##  Creates new effectivity row in @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  object 
    ##  @return effectivityRow (@link EffectivityTableRow NXOpen.PDM.EffectivityTableRow@endlink):  newly created empty effectivity row .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    def CreateNewEffectivityRow(self) -> EffectivityTableRow:
        """
         Creates new effectivity row in @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  object 
         @return effectivityRow (@link EffectivityTableRow NXOpen.PDM.EffectivityTableRow@endlink):  newly created empty effectivity row .
        """
        pass
    
    ##  Gets the existing effectivity rows from effectivity table
    ##  @return effectivityRows (@link EffectivityTableRow List[NXOpen.PDM.EffectivityTableRow]@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetEffectivityRows(self) -> List[EffectivityTableRow]:
        """
         Gets the existing effectivity rows from effectivity table
         @return effectivityRows (@link EffectivityTableRow List[NXOpen.PDM.EffectivityTableRow]@endlink): .
        """
        pass
    
    ##  Removes the given effectivity rows from @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ## <param name="effectivityRows"> (@link EffectivityTableRow List[NXOpen.PDM.EffectivityTableRow]@endlink)  effectivity rows to be removed</param>
    def RemoveEffectivityRows(self, effectivityRows: List[EffectivityTableRow]) -> None:
        """
         Removes the given effectivity rows from @link NXOpen::PDM::EffectivityTableBuilder NXOpen::PDM::EffectivityTableBuilder@endlink  
        """
        pass
    
    ##  Updates this builder with new @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink , validation basis formula and effectivity formulae to edit.
    ##             Effectivity formulae will be validated against provided validation basis formula.
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ## <param name="cd"> (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) </param>
    ## <param name="validationBasisFormula"> (str) </param>
    ## <param name="effectivityFormulae"> (List[str]) </param>
    def UpdateBuilderDetails(self, cd: NXOpen.CollaborativeDesign, validationBasisFormula: str, effectivityFormulae: List[str]) -> None:
        """
         Updates this builder with new @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink , validation basis formula and effectivity formulae to edit.
                    Effectivity formulae will be validated against provided validation basis formula.
                
        """
        pass
    
import NXOpen
## 
##         Represents the class that contains effectivity parameters.
##      <br> Instances of this class can be accessed through various application specific builders  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class EffectivityTableRow(NXOpen.NXObject): 
    """
        Represents the class that contains effectivity parameters.
    """
    pass


##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ElementGroup(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """
    pass


import NXOpen
## 
##         Represents the class that contains ErrorObjects and Failed Logical Objects.
##     
## 
##   <br>  Created in NX11.0.0  <br> 

class ErrorMessageHandler(NXOpen.TransientObject): 
    """
        Represents the class that contains ErrorObjects and Failed Logical Objects.
    """


    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Returns ERROR_LIST_s 
    ##  @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetErrorList(self) -> NXOpen.ErrorList:
        """
         Returns ERROR_LIST_s 
         @return errorList (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
        """
        pass
    
    ##  Returns Error Messages 
    ##  @return errorMessages (List[str]):  Error Messages  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetErrorMessages(self) -> List[str]:
        """
         Returns Error Messages 
         @return errorMessages (List[str]):  Error Messages  .
        """
        pass
    
    ##  Returns Warning Messages 
    ##  @return warningMessages (List[str]):  Warning Messages  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetWarningMessages(self) -> List[str]:
        """
         Returns Warning Messages 
         @return warningMessages (List[str]):  Warning Messages  .
        """
        pass
    
##  This enum is used to specify the existing part action that will be applied to operation candidates. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Overwrite</term><description> 
## </description> </item><item><term> 
## UseExisting</term><description> 
## </description> </item><item><term> 
## Exclude</term><description> 
## </description> </item><item><term> 
## Clone</term><description> 
## </description> </item><item><term> 
## Retain</term><description> 
## </description> </item><item><term> 
## Default</term><description> 
## </description> </item></list>
class ExistingPartAction(Enum):
    """
    Members Include: <Overwrite> <UseExisting> <Exclude> <Clone> <Retain> <Default>
    """
    Overwrite: int
    UseExisting: int
    Exclude: int
    Clone: int
    Retain: int
    Default: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> ExistingPartAction:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  Represents a Export class that performs Create operations  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateExportFromTeamcenterBuilderForDesignWorkset  NXOpen::PDM::PdmSession::CreateExportFromTeamcenterBuilderForDesignWorkset @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ExportFromTeamcenter(ICloneOperation): 
    """ Represents a Export class that performs Create operations """


    ##  This API adds the dfa file to the export operation. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dfaFile"> (str) </param>
    def AddDFAFile(self, dfaFile: str) -> None:
        """
         This API adds the dfa file to the export operation. 
        """
        pass
    
    ##  This API creates the zip of exported parts. 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="zipFilePath"> (str) </param>
    ## <param name="overwrite"> (bool) </param>
    def CreateZipFileOfExportedParts(self, zipFilePath: str, overwrite: bool) -> int:
        """
         This API creates the zip of exported parts. 
         @return status (int): .
        """
        pass
    
    ##  This API exports the dfa files to the the specified export directory. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dfaFiles"> (List[str]) </param>
    ## <param name="defDir"> (str) </param>
    ## <param name="doMixins"> (bool) </param>
    def ExportDFAFiles(self, dfaFiles: List[str], defDir: str, doMixins: bool) -> None:
        """
         This API exports the dfa files to the the specified export directory. 
        """
        pass
    
    ##  This API specifies whether to add DFA mixins or not. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="isAddDfaMixins"> (bool) </param>
    def SetAddDfaMixins(self, isAddDfaMixins: bool) -> None:
        """
         This API specifies whether to add DFA mixins or not. 
        """
        pass
    
    ##  This API sets the directory in which associated files for the specified component will be placed. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectToBeCloned"> (@link AssyCloneCompDisp NXOpen.PDM.AssyCloneCompDisp@endlink) </param>
    ## <param name="directoryName"> (str) </param>
    def SetAssociatedFilesDir(self, objectToBeCloned: AssyCloneCompDisp, directoryName: str) -> None:
        """
         This API sets the directory in which associated files for the specified component will be placed. 
        """
        pass
    
    ##  This API sets the root directory below which part specific associated file directories will be placed.
    ##             If the associated files root directory is not set then the associated files will be copied to the directory
    ##             of the exported parts.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rootDirName"> (str) </param>
    def SetAssociatedFilesRootDir(self, rootDirName: str) -> None:
        """
         This API sets the root directory below which part specific associated file directories will be placed.
                    If the associated files root directory is not set then the associated files will be copied to the directory
                    of the exported parts.
                
        """
        pass
    
    ##  This API sets the check-out data to be used for checking out a particular part. 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectToBeCloned"> (@link AssyCloneCompDisp NXOpen.PDM.AssyCloneCompDisp@endlink) </param>
    ## <param name="checkoutComment"> (str) </param>
    def SetCheckOutData(self, objectToBeCloned: AssyCloneCompDisp, checkoutComment: str) -> int:
        """
         This API sets the check-out data to be used for checking out a particular part. 
         @return status (int): .
        """
        pass
    
    ##  This API sets the default check-out data to be used for checking out all the exported parts. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="checkoutComment"> (str) </param>
    def SetDefaultCheckOutData(self, checkoutComment: str) -> None:
        """
         This API sets the default check-out data to be used for checking out all the exported parts. 
        """
        pass
    
    ##  This API sets the default directory for the parts created during export will be placed in.
    ##             If this option is never set then the current directory will be used.
    ##             Note: This option is ignored for user name numbering technique.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="directoryName"> (str) </param>
    def SetDefaultDirectory(self, directoryName: str) -> None:
        """
         This API sets the default directory for the parts created during export will be placed in.
                    If this option is never set then the current directory will be used.
                    Note: This option is ignored for user name numbering technique.
                
        """
        pass
    
    ##  This API specifies whether to export DFA file or not. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="isExportDfaWithPart"> (bool) </param>
    def SetExportDfaWithPart(self, isExportDfaWithPart: bool) -> None:
        """
         This API specifies whether to export DFA file or not. 
        """
        pass
    
    ##  This API sets the option to export the related External files during export operation. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="setExternalFiles"> (bool) </param>
    def SetExternalFiles(self, setExternalFiles: bool) -> None:
        """
         This API sets the option to export the related External files during export operation. 
        """
        pass
    
    ##  This API stores the current identifier display rule as previous identifier display rule and then sets new for current export session. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="displayRule"> (str) </param>
    def SetIdentifierDisplayRule(self, displayRule: str) -> None:
        """
         This API stores the current identifier display rule as previous identifier display rule and then sets new for current export session. 
        """
        pass
    
import NXOpen
##  Represents a builder class that performs Create operations  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmManager::CreateExportWorksetForReferenceBuilder  NXOpen::PDM::PdmManager::CreateExportWorksetForReferenceBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ExportWorksetForReferenceBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Create operations """


    ## Getter for property: (str) DestinationFolder
    ##  Returns the export directory path   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def DestinationFolder(self) -> str:
        """
        Getter for property: (str) DestinationFolder
         Returns the export directory path   
            
         
        """
        pass
    
    ## Setter for property: (str) DestinationFolder

    ##  Returns the export directory path   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DestinationFolder.setter
    def DestinationFolder(self, folderPath: str):
        """
        Setter for property: (str) DestinationFolder
         Returns the export directory path   
            
         
        """
        pass
    
    ##  Gets the objects for the modified objects in session. 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets the objects for the modified objects in session. 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Validate the inputs provided for export 
    ##  @return validationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def ValidateObjects(self) -> NXOpen.ErrorList:
        """
         Validate the inputs provided for export 
         @return validationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
        """
        pass
    
import NXOpen
##  Represents a builder class  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateExternalFileReferenceListBuilder  NXOpen::PDM::PdmSession::CreateExternalFileReferenceListBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ExternalFileReferenceListBuilder(NXOpen.Builder): 
    """ Represents a builder class """


    ##  Gets the external file objects for the source part. 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetExternalFileObjects(self) -> List[NXOpen.NXObject]:
        """
         Gets the external file objects for the source part. 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
import NXOpen
##  This class is responsible for Teamcenter file management related activities.   <br> Use @link PDM::PdmSession::NewFileManagement PDM::PdmSession::NewFileManagement@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX6.0.3  <br> 

class FileManagement(NXOpen.TransientObject): 
    """ This class is responsible for Teamcenter file management related activities.  """


    ##  PDM file types  
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## CmmDmi</term><description> 
    ## </description> </item><item><term> 
    ## CpdFeaturePart</term><description> 
    ##  </description> </item><item><term> 
    ## CpdGeometryOverride</term><description> 
    ##  </description> </item><item><term> 
    ## DirectModel</term><description> 
    ##  </description> </item><item><term> 
    ## Excel</term><description> 
    ##  </description> </item><item><term> 
    ## ExcelX</term><description> 
    ##  </description> </item><item><term> 
    ## Image</term><description> 
    ##  </description> </item><item><term> 
    ## Jpeg</term><description> 
    ##  </description> </item><item><term> 
    ## NxDesignatorAssignmentsFile</term><description> 
    ##  </description> </item><item><term> 
    ## NxAttachedPart</term><description> 
    ##  </description> </item><item><term> 
    ## NxPart</term><description> 
    ##  </description> </item><item><term> 
    ## NxPosBin</term><description> 
    ##  </description> </item><item><term> 
    ## NxleSymbolXml</term><description> 
    ##  </description> </item><item><term> 
    ## NxleSymbolPreview</term><description> 
    ##  </description> </item><item><term> 
    ## Preview2d</term><description> 
    ##  </description> </item><item><term> 
    ## Preview3d</term><description> 
    ##  </description> </item><item><term> 
    ## QafBinary</term><description> 
    ##  </description> </item><item><term> 
    ## QafText</term><description> 
    ##  </description> </item><item><term> 
    ## RoutePipeRun</term><description> 
    ##  </description> </item><item><term> 
    ## RoutePipeSpec</term><description> 
    ##  </description> </item><item><term> 
    ## RoutePipeRunAttachment</term><description> 
    ##  </description> </item><item><term> 
    ## Text</term><description> 
    ##  </description> </item><item><term> 
    ## Tif</term><description> 
    ##  </description> </item><item><term> 
    ## TrushapeData</term><description> 
    ##  </description> </item><item><term> 
    ## ValidationRuleSet</term><description> 
    ##  </description> </item></list>
    class FileType(Enum):
        """
        Members Include: <CmmDmi> <CpdFeaturePart> <CpdGeometryOverride> <DirectModel> <Excel> <ExcelX> <Image> <Jpeg> <NxDesignatorAssignmentsFile> <NxAttachedPart> <NxPart> <NxPosBin> <NxleSymbolXml> <NxleSymbolPreview> <Preview2d> <Preview3d> <QafBinary> <QafText> <RoutePipeRun> <RoutePipeSpec> <RoutePipeRunAttachment> <Text> <Tif> <TrushapeData> <ValidationRuleSet>
        """
        CmmDmi: int
        CpdFeaturePart: int
        CpdGeometryOverride: int
        DirectModel: int
        Excel: int
        ExcelX: int
        Image: int
        Jpeg: int
        NxDesignatorAssignmentsFile: int
        NxAttachedPart: int
        NxPart: int
        NxPosBin: int
        NxleSymbolXml: int
        NxleSymbolPreview: int
        Preview2d: int
        Preview3d: int
        QafBinary: int
        QafText: int
        RoutePipeRun: int
        RoutePipeSpec: int
        RoutePipeRunAttachment: int
        Text: int
        Tif: int
        TrushapeData: int
        ValidationRuleSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> FileManagement.FileType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Delete Attached Files From Teamcenter.
    ##         Delete attached files from dataset.
    ##          . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
    ##          . associationTypeName - Teamcenter relation type name
    ##          . datasetTypeName - Teamcenter dataset type name
    ##          . datasetName - Dataset name for creation or for matching existing dataset
    ##          . namedReferenceName - Named reference name
    ##          . isText - Named reference isText flag
    ##          . logicalFileName - Named reference logical filename
    ##          . keepEmptyDataset - Flag indicating if datasets should be kept even if they become empty
    ##         
    ##  @return resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="associatedObject"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Teamcenter object the files are attached to </param>
    ## <param name="associationTypeName"> (List[str])  Teamcenter relation type name or property name if association is through property </param>
    ## <param name="datasetTypeName"> (List[str])  Teamcenter dataset type name </param>
    ## <param name="datasetName"> (List[str])  Dataset name for creation or for matching existing dataset </param>
    ## <param name="namedReferenceName"> (List[str])  Named reference name </param>
    ## <param name="isText"> (List[str])  Named reference isText flag </param>
    ## <param name="logicalFileName"> (List[str])  Named reference logical filename </param>
    ## <param name="keepEmptyDataset"> (bool)  True (default) - keep dataset even if empty; False - don'e keep empty dataset </param>
    def DeleteAttachedFiles(self, associatedObject: List[NXOpen.NXObject], associationTypeName: List[str], datasetTypeName: List[str], datasetName: List[str], namedReferenceName: List[str], isText: List[str], logicalFileName: List[str], keepEmptyDataset: bool) -> List[int]:
        """
         Delete Attached Files From Teamcenter.
                Delete attached files from dataset.
                 . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
                 . associationTypeName - Teamcenter relation type name
                 . datasetTypeName - Teamcenter dataset type name
                 . datasetName - Dataset name for creation or for matching existing dataset
                 . namedReferenceName - Named reference name
                 . isText - Named reference isText flag
                 . logicalFileName - Named reference logical filename
                 . keepEmptyDataset - Flag indicating if datasets should be kept even if they become empty
                
         @return resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
        """
        pass
    
    ##  Delete Attached Files From Teamcenter.
    ##         Delete given attached files from dataset.
    ##         
    ##  @return resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="files"> (@link PdmFile List[NXOpen.PDM.PdmFile]@endlink)  Files to delete </param>
    ## <param name="keepEmptyDataset"> (bool)  True (default) - keep dataset even if empty; False - don'e keep empty dataset </param>
    def DeleteExistingAttachedFiles(self, files: List[PdmFile], keepEmptyDataset: bool) -> List[int]:
        """
         Delete Attached Files From Teamcenter.
                Delete given attached files from dataset.
                
         @return resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.3  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##   Download the specified named reference files for NX use. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parts"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    ## <param name="files"> (@link PdmFile List[NXOpen.PDM.PdmFile]@endlink) </param>
    def DownloadAssociatedFiles(self, parts: List[NXOpen.BasePart], files: List[PdmFile]) -> None:
        """
          Download the specified named reference files for NX use. 
        """
        pass
    
    ##  Exports all associated files for the specified dataset(s)
    ##         to a directory. The dataset(s) are identified by their Teamcenter 
    ##         item id, Teamcenter item revision id, Teamcenter dataset name, 
    ##         NX dataset type, and  NX dataset relation type.  A base export directory
    ##         name must be specified for each dataset along with the tool name that
    ##         is requesting the export.  The full path to the exported files is 
    ##         returned in an output array.  The full path will be 
    ##         NX_default_directory or export_directory.  Additionally, an array of
    ##         PDI result codes is returned indicating the success (0) or failure 
    ##         (non-zero) of each export.
    ##         The dataset types for FOREIGN_MODEL are the ones included in the 
    ##         Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
    ##         input relation type should be "Foreign".
    ##         The exporting of the associated file is governed by following conditions:        
    ##         The associated filetype should be exportable for combination of the Tool 
    ##         used and the Open action for operation.
    ##         The associated file should not be in the excluded named reference list. 
    ##         For Foreign Datasets it will not export file types included in the Teamcenter
    ##         preference "TC_NX_Foreign_Datasets".
    ##         In case of NX CAM dataset type like "UGCAMCLSF", "UGCAMPTP", "UGCAMShopDoc",
    ##         all the associated files will be exported irrespective of above conditions.
    ##         <ol>
    ##         <li>Excluded Named Reference List:</li>
    ##         <li>"UGPART"</li>             
    ##         <li>"UGPART-MASSPR</li>            
    ##         <li>"UGPART-BBOX</li>              
    ##         <li>"UGPART-ATTRIBUTES</li>        
    ##         <li>"UGPART-ATTR</li>             
    ##         <li>"Trushape-Data</li>            
    ##         <li>"BVRSYNCINFO</li>              
    ##         <li>"UG-QuickAccess-Binary</li>    
    ##         <li>"UG-QuickAccess-Text</li>   
    ##         </ol>
    ##         <ol>
    ##         <li>NX dataset types and relation names</li>
    ##         <li>NX Model Type         NX Relation Type        NX Dataset Type</li>
    ##         <li>MASTER_MODEL          "has shape"             "UGMASTER"</li>
    ##         <li>SPEC_MODEL            "has specification"     "UGPART"</li>
    ##         <li>MAN_MODEL             "has manifestation"     "UGPART"</li>
    ##         <li>ALTREP_MODEL          "has altrep"            "UGALTREP"</li>
    ##         <li>SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"</li>
    ##         <li>SIMULATION_MODEL      "NX_simulation"         "NXSimulation"</li>
    ##         <li>MOTION_MODEL          "NX_simulation"         "NXMotion"</li>
    ##         <li>CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"</li>
    ##         <li>CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"</li>
    ##         <li>CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"</li>
    ##         <li>FOREIGN_MODEL         "Foreign"               "*"</li>
    ##         <li>MOTION_MODEL_SPEC     "has specification"     "MotionSim"</li>
    ##         </ol>
    ##         For the input itemIds:
    ##         In case of Default Domain: it is Teamcenter item ID.
    ##         In case of non-Default Domain: it is the multifield key.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         And the encoded part filename would be containing the MFK.
    ##         
    ##  @return A tuple consisting of (resultCodes, exportDirectoryNames). 
    ##  - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
    ##  - exportDirectoryNames is: List[str]. Resulting location of export directory .

    ## 
    ##   <br>  Created in NX6.0.3  <br> 

    ## License requirements: None.
    ## 
    ## <param name="itemIds"> (List[str])  Multifield Key. </param>
    ## <param name="itemRevisionIds"> (List[str])  Teamcenter item revision ids. </param>
    ## <param name="datasetNames"> (List[str])  Teamcenter dataset names. </param>
    ## <param name="datasetTypeNames"> (List[str])  NX dataset type names. </param>
    ## <param name="datasetRelationTypeNames"> (List[str])  NX dataset relation type names. </param>
    ## <param name="baseDirectoryNames"> (List[str])  Base export directory name. </param>
    ## <param name="toolNames"> (List[str])  Tool names ("UGII V10-ALL"). </param>
    def ExportFiles(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], baseDirectoryNames: List[str], toolNames: List[str]) -> Tuple[List[int], List[str]]:
        """
         Exports all associated files for the specified dataset(s)
                to a directory. The dataset(s) are identified by their Teamcenter 
                item id, Teamcenter item revision id, Teamcenter dataset name, 
                NX dataset type, and  NX dataset relation type.  A base export directory
                name must be specified for each dataset along with the tool name that
                is requesting the export.  The full path to the exported files is 
                returned in an output array.  The full path will be 
                NX_default_directory or export_directory.  Additionally, an array of
                PDI result codes is returned indicating the success (0) or failure 
                (non-zero) of each export.
                The dataset types for FOREIGN_MODEL are the ones included in the 
                Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
                input relation type should be "Foreign".
                The exporting of the associated file is governed by following conditions:        
                The associated filetype should be exportable for combination of the Tool 
                used and the Open action for operation.
                The associated file should not be in the excluded named reference list. 
                For Foreign Datasets it will not export file types included in the Teamcenter
                preference "TC_NX_Foreign_Datasets".
                In case of NX CAM dataset type like "UGCAMCLSF", "UGCAMPTP", "UGCAMShopDoc",
                all the associated files will be exported irrespective of above conditions.
                <ol>
                <li>Excluded Named Reference List:</li>
                <li>"UGPART"</li>             
                <li>"UGPART-MASSPR</li>            
                <li>"UGPART-BBOX</li>              
                <li>"UGPART-ATTRIBUTES</li>        
                <li>"UGPART-ATTR</li>             
                <li>"Trushape-Data</li>            
                <li>"BVRSYNCINFO</li>              
                <li>"UG-QuickAccess-Binary</li>    
                <li>"UG-QuickAccess-Text</li>   
                </ol>
                <ol>
                <li>NX dataset types and relation names</li>
                <li>NX Model Type         NX Relation Type        NX Dataset Type</li>
                <li>MASTER_MODEL          "has shape"             "UGMASTER"</li>
                <li>SPEC_MODEL            "has specification"     "UGPART"</li>
                <li>MAN_MODEL             "has manifestation"     "UGPART"</li>
                <li>ALTREP_MODEL          "has altrep"            "UGALTREP"</li>
                <li>SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"</li>
                <li>SIMULATION_MODEL      "NX_simulation"         "NXSimulation"</li>
                <li>MOTION_MODEL          "NX_simulation"         "NXMotion"</li>
                <li>CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"</li>
                <li>CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"</li>
                <li>CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"</li>
                <li>FOREIGN_MODEL         "Foreign"               "*"</li>
                <li>MOTION_MODEL_SPEC     "has specification"     "MotionSim"</li>
                </ol>
                For the input itemIds:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
         @return A tuple consisting of (resultCodes, exportDirectoryNames). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
         - exportDirectoryNames is: List[str]. Resulting location of export directory .

        """
        pass
    
    ##  Export Named Reference From Teamcenter.
    ##         The Dataset Relation Type Names are the names of the Teamcenter relationships used to find the Datasets
    ##         to the correponding Item Revisions.
    ##         Any ImanRelation types can be used.
    ##         
    ##  @return namedReferences (List[str]):  NamedReferences, full pathnames of files .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="fileManagement"> (@link FileManagement NXOpen.PDM.FileManagement@endlink) </param>
    ## <param name="itemId"> (str)  Multifield key. </param>
    ## <param name="itemRevisionId"> (str)  Teamcenter item revision ids. </param>
    ## <param name="datasetName"> (str)  Teamcenter dataset names. </param>
    ## <param name="datasetTypeName"> (str)  NX dataset type names. </param>
    ## <param name="datasetRelationTypeName"> (str)  Exact Teamcenter relation type names. </param>
    ## <param name="datasetNamedReference"> (str)  NX dataset named reference names. </param>
    ## <param name="exportDirectoryName"> (str)  Where to export files to, if empty then files will not be downloaded </param>
    @overload
    def ExportNamedReferences(self, itemId: str, itemRevisionId: str, datasetName: str, datasetTypeName: str, datasetRelationTypeName: str, datasetNamedReference: str, exportDirectoryName: str) -> List[str]:
        """
         Export Named Reference From Teamcenter.
                The Dataset Relation Type Names are the names of the Teamcenter relationships used to find the Datasets
                to the correponding Item Revisions.
                Any ImanRelation types can be used.
                
         @return namedReferences (List[str]):  NamedReferences, full pathnames of files .
        """
        pass
    
    ##  Export Named Reference From Teamcenter.
    ##         The Dataset Relation Type Names are the names of the Teamcenter relationships used to find the Datasets
    ##         to the correponding Item Revisions.
    ##         Any ImanRelation types can be used.
    ##         
    ##  @return A tuple consisting of (resultCodes, numNamedReferences, namedReferences). 
    ##  - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
    ##  - numNamedReferences is: List[int]. Array of the number of named references for each itemid .
    ##  - namedReferences is: List[str]. NamedReferences, full pathnames of files, array size is namedReferencesLength  .

    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## <param name="fileManagement"> (@link FileManagement NXOpen.PDM.FileManagement@endlink) </param>
    ## <param name="itemIds"> (List[str])  Multifield key. </param>
    ## <param name="itemRevisionIds"> (List[str])  Teamcenter item revision ids. </param>
    ## <param name="datasetNames"> (List[str])  Teamcenter dataset names. </param>
    ## <param name="datasetTypeNames"> (List[str])  NX dataset type names. </param>
    ## <param name="datasetRelationTypeNames"> (List[str])  Exact Teamcenter relation type names. </param>
    ## <param name="datasetNamedReferences"> (List[str])  NX dataset named reference names. </param>
    ## <param name="exportDirectoryName"> (str)  Where to export files to, if empty then files will not be downloaded</param>
    @overload
    def ExportNamedReferences(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], datasetNamedReferences: List[str], exportDirectoryName: str) -> Tuple[List[int], List[int], List[str]]:
        """
         Export Named Reference From Teamcenter.
                The Dataset Relation Type Names are the names of the Teamcenter relationships used to find the Datasets
                to the correponding Item Revisions.
                Any ImanRelation types can be used.
                
         @return A tuple consisting of (resultCodes, numNamedReferences, namedReferences). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
         - numNamedReferences is: List[int]. Array of the number of named references for each itemid .
         - namedReferences is: List[str]. NamedReferences, full pathnames of files, array size is namedReferencesLength  .

        """
        pass
    
    ##   Given an NX part, this method will return a list of named
    ##         reference files in the corresponding Teamcenter dataset. 
    ##  @return files (@link PdmFile List[NXOpen.PDM.PdmFile]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parts"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    ## <param name="fileTypesToExclude"> (@link FileManagement.FileType List[NXOpen.PDM.FileManagement.FileType]@endlink) </param>
    def GetAssociatedFiles(self, parts: List[NXOpen.BasePart], fileTypesToExclude: List[FileManagement.FileType]) -> List[PdmFile]:
        """
          Given an NX part, this method will return a list of named
                reference files in the corresponding Teamcenter dataset. 
         @return files (@link PdmFile List[NXOpen.PDM.PdmFile]@endlink): .
        """
        pass
    
    ##  Get Attached Files Information From Teamcenter.
    ##         Query attached files information for given specifications.
    ##          . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
    ##          . associationTypeName - Teamcenter relation type name
    ##          . datasetTypeName - Teamcenter dataset type name
    ##          . datasetName - Dataset name for creation or for matching existing dataset
    ##          . namedReferenceName - Named reference name
    ##          . isText - Named reference isText flag
    ##          . logicalFileName - Named reference logical filename
    ##          . exportDirectoryName - Where to export files to, if empty then files will not be downloaded
    ##          . outputFilesLength - Number of total files returned
    ##         
    ##  @return A tuple consisting of (resultCodes, numOutputFiles, files). 
    ##  - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
    ##  - numOutputFiles is: List[int]. Number of output files for each input .
    ##  - files is: @link PdmFile List[NXOpen.PDM.PdmFile]@endlink. Output - arry of PdmFiles .

    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="associatedObject"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Teamcenter object the files are attached to </param>
    ## <param name="associationTypeName"> (List[str])  Teamcenter relation type name or property name if association is through property </param>
    ## <param name="datasetTypeName"> (List[str])  Teamcenter dataset type name </param>
    ## <param name="datasetName"> (List[str])  Dataset name for creation or for matching existing dataset </param>
    ## <param name="namedReferenceName"> (List[str])  Named reference name </param>
    ## <param name="isText"> (List[str])  Named reference isText flag </param>
    ## <param name="logicalFileName"> (List[str])  Named reference logical filename </param>
    ## <param name="exportDirectoryName"> (str)  Where to export files to, if empty then files will not be downloaded </param>
    def GetAttachedFiles(self, associatedObject: List[NXOpen.NXObject], associationTypeName: List[str], datasetTypeName: List[str], datasetName: List[str], namedReferenceName: List[str], isText: List[str], logicalFileName: List[str], exportDirectoryName: str) -> Tuple[List[int], List[int], List[PdmFile]]:
        """
         Get Attached Files Information From Teamcenter.
                Query attached files information for given specifications.
                 . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
                 . associationTypeName - Teamcenter relation type name
                 . datasetTypeName - Teamcenter dataset type name
                 . datasetName - Dataset name for creation or for matching existing dataset
                 . namedReferenceName - Named reference name
                 . isText - Named reference isText flag
                 . logicalFileName - Named reference logical filename
                 . exportDirectoryName - Where to export files to, if empty then files will not be downloaded
                 . outputFilesLength - Number of total files returned
                
         @return A tuple consisting of (resultCodes, numOutputFiles, files). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). .
         - numOutputFiles is: List[int]. Number of output files for each input .
         - files is: @link PdmFile List[NXOpen.PDM.PdmFile]@endlink. Output - arry of PdmFiles .

        """
        pass
    
    ##  Imports all associated files for the specified dataset(s)
    ##         into the Teamcenter database.  The files will be attached to the
    ##         dataset(s) as named references.  The dataset(s) are identified by
    ##         their Teamcenter multifield key, Teamcenter item revision id, Teamcenter 
    ##         dataset name, NX dataset type, and NX dataset relation type.  
    ##         An import directory containing the files must be specified for each 
    ##         dataset.  An array of PDI result codes is returned indicating the 
    ##         success (0) or failure (non-zero) of each import.
    ##         The dataset types for FOREIGN_MODEL are the ones included in the 
    ##         Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
    ##         input relation type should be "Foreign". The named reference information
    ##         from BMIDE setting will be used for the imported file extension.
    ##         <ol>
    ##         <li>NX dataset types and relation names</li>
    ##         <li>NX Model Type         NX Relation Type        NX Dataset Type</li>
    ##         <li>MASTER_MODEL          "has shape"             "UGMASTER"</li>
    ##         <li>SPEC_MODEL            "has specification"     "UGPART"</li>
    ##         <li>MAN_MODEL             "has manifestation"     "UGPART"</li>
    ##         <li>ALTREP_MODEL          "has altrep"            "UGALTREP"</li>
    ##         <li>SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"</li>
    ##         <li>SIMULATION_MODEL      "NX_simulation"         "NXSimulation"</li>
    ##         <li>MOTION_MODEL          "NX_simulation"         "NXMotion"</li>
    ##         <li>CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"</li>
    ##         <li>CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"</li>
    ##         <li>CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"</li>
    ##         <li>FOREIGN_MODEL         "Foreign"               "*"</li>
    ##         <li>MOTION_MODEL_SPEC     "has specification"     "MotionSim"</li>
    ##         </ol>
    ## 
    ##         For the input itemIds:
    ##         In case of Default Domain: it is Teamcenter item ID.
    ##         In case of non-Default Domain: it is the multifield key.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         And the encoded part filename would be containing the MFK.
    ##         
    ##  @return resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
    ## 
    ##   <br>  Created in NX6.0.3  <br> 

    ## License requirements: None.
    ## 
    ## <param name="itemIds"> (List[str])  Multifield key. </param>
    ## <param name="itemRevisionIds"> (List[str])  Teamcenter item revision ids. </param>
    ## <param name="datasetNames"> (List[str])  Teamcenter dataset names. </param>
    ## <param name="datasetTypeNames"> (List[str])  NX dataset type names. </param>
    ## <param name="datasetRelationTypeNames"> (List[str])  NX dataset relation type names. </param>
    ## <param name="importDirectoryNames"> (List[str])  Import directories which contain the files to import. </param>
    def ImportFiles(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], importDirectoryNames: List[str]) -> List[int]:
        """
         Imports all associated files for the specified dataset(s)
                into the Teamcenter database.  The files will be attached to the
                dataset(s) as named references.  The dataset(s) are identified by
                their Teamcenter multifield key, Teamcenter item revision id, Teamcenter 
                dataset name, NX dataset type, and NX dataset relation type.  
                An import directory containing the files must be specified for each 
                dataset.  An array of PDI result codes is returned indicating the 
                success (0) or failure (non-zero) of each import.
                The dataset types for FOREIGN_MODEL are the ones included in the 
                Teamcenter preference "TC_NX_Foreign_Datasets". In such a case the 
                input relation type should be "Foreign". The named reference information
                from BMIDE setting will be used for the imported file extension.
                <ol>
                <li>NX dataset types and relation names</li>
                <li>NX Model Type         NX Relation Type        NX Dataset Type</li>
                <li>MASTER_MODEL          "has shape"             "UGMASTER"</li>
                <li>SPEC_MODEL            "has specification"     "UGPART"</li>
                <li>MAN_MODEL             "has manifestation"     "UGPART"</li>
                <li>ALTREP_MODEL          "has altrep"            "UGALTREP"</li>
                <li>SCENARIO_MODEL        "UG_scenario"           "UGSCENARIO"</li>
                <li>SIMULATION_MODEL      "NX_simulation"         "NXSimulation"</li>
                <li>MOTION_MODEL          "NX_simulation"         "NXMotion"</li>
                <li>CAE_SOLN_MODEL        "NX_simulation"         "CAESolution"</li>
                <li>CAE_MESH_MODEL        "NX_simulation"         "CAEMesh"</li>
                <li>CAE_GEOM_MODEL        "NX_simulation"         "CAEGeom"</li>
                <li>FOREIGN_MODEL         "Foreign"               "*"</li>
                <li>MOTION_MODEL_SPEC     "has specification"     "MotionSim"</li>
                </ol>
        
                For the input itemIds:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
         @return resultCodes (List[int]):  Result codes. Success (0), failure (non-zero). .
        """
        pass
    
    ##  Import files and create datasets in Teamcenter.
    ##         In order to create multiple datasets at once, please make sure to declare all the arrays of the same desired size.
    ##         This creates the Items (with the specified item ids) and Item Revisions (with the specified item revision ids) in case they don't exist in Teamcenter.
    ##         This creates the datasets if no matching dataset exists in Teamcenter.
    ##         The dataset relation type names are the exact names of the Teamcenter relations used to attach the Datasets to the corresponding Item Revisions. (Any ImanRelation types can be used.)
    ##         
    ##  @return resultCodes (List[int]):  Result codes. Success (zero), Failure (non-zero). .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="itemIds"> (List[str])  Multifield key. Creates a new item if it does not exist in Teamcenter; updates it if it exists. </param>
    ## <param name="itemRevisionIds"> (List[str])  Teamcenter item revision ids. Creates a new item revision id if it does not exist in Teamcenter; updates it if it exists. </param>
    ## <param name="datasetNames"> (List[str])  Teamcenter dataset names. Creates a new dataset if it does not exist in Teamcenter; updates it if it exists. </param>
    ## <param name="datasetTypeNames"> (List[str])  NX dataset type names. </param>
    ## <param name="datasetRelationTypeNames"> (List[str])  Exact Teamcenter relation type names. </param>
    ## <param name="datasetToolNames"> (List[str])  NX dataset tool names. This is not currently supported. For future use only. </param>
    ## <param name="fileType"> (List[bool])  Types of files - true = Binary, false = Ascii.</param>
    ## <param name="namedReferenceNames"> (List[str])  Names of named references per NX dataset. </param>
    ## <param name="importFileNames"> (List[str])  Names of files (with file extension) to import per NX dataset. Please do not include the full directory path. </param>
    ## <param name="importFileDirectoryNames"> (List[str])  Names of the file directories which contain the files to import. </param>
    def ImportFilesAndCreateDatasets(self, itemIds: List[str], itemRevisionIds: List[str], datasetNames: List[str], datasetTypeNames: List[str], datasetRelationTypeNames: List[str], datasetToolNames: List[str], fileType: List[bool], namedReferenceNames: List[str], importFileNames: List[str], importFileDirectoryNames: List[str]) -> List[int]:
        """
         Import files and create datasets in Teamcenter.
                In order to create multiple datasets at once, please make sure to declare all the arrays of the same desired size.
                This creates the Items (with the specified item ids) and Item Revisions (with the specified item revision ids) in case they don't exist in Teamcenter.
                This creates the datasets if no matching dataset exists in Teamcenter.
                The dataset relation type names are the exact names of the Teamcenter relations used to attach the Datasets to the corresponding Item Revisions. (Any ImanRelation types can be used.)
                
         @return resultCodes (List[int]):  Result codes. Success (zero), Failure (non-zero). .
        """
        pass
    
    ##  Save Attached Files To Teamcenter.
    ##         Save attached files for given specifications.
    ##          . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
    ##          . associationTypeName - Teamcenter relation type name
    ##          . datasetTypeName - Teamcenter dataset type name
    ##          . datasetName - Dataset name for creation or for matching existing dataset
    ##          . numDatasetPropertyInput - Number of dataset property names input for each dataset input
    ##          . numTotalDatasetProperties - Number of total dataset properties
    ##          . datasetPropertyNames - To specify required properties when creating new dataset or for updating existing dataset properties
    ##          . datasetPropertyValues - Dataset property values; need to match one-to-one with datasetPropertyNames
    ##          . ownershipToMatchForNewDataset - Teamcenter object used to assign new dataset owner, default is current user if not set
    ##          . fileVolumeToStore - Teamcenter volume for storing file, default is current session volume if not set
    ##          . toolUsed - Teamcenter toolUsed for new dataset
    ##          . datasetDescription - Dataset description for new dataset
    ##          . alwaysCreateNewDataset - Flag indicating if a new dataset should always be created
    ##          . createNewDatasetVersion - Flag indicating if new dataset version should be created
    ##          . refreshInSessionLoadedLMD - Flag indicating if in-session loaded Last-Modified-Date should be refreshed
    ##          . numNamedReferencesPerInput - Number of named references input for each dataset input
    ##          . numTotalNamedReferences - Number of total named references input
    ##          . namedReferenceName - Named reference name for each named reference input
    ##          . isText - Named reference isText flag for each named reference input
    ##          . filePath - Named reference file path for each named reference input
    ##          . logicalFileName - Named reference logical filename for each named reference input
    ##          . allowReplace - Flag indicating to replace if named reference already exists for each named reference input
    ##          . outputFiles - Flag indicating if files should be returned
    ##         
    ##  @return A tuple consisting of (resultCodes, files). 
    ##  - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). Array size is total number of named references .
    ##  - files is: @link PdmFile List[NXOpen.PDM.PdmFile]@endlink. Output - arry of PdmFiles. Array size is total number of named references .

    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="associatedObject"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Teamcenter object the files to be attached to </param>
    ## <param name="associationTypeName"> (List[str])  Teamcenter relation type name or property name if association is through property </param>
    ## <param name="datasetTypeName"> (List[str])  Teamcenter dataset type name </param>
    ## <param name="datasetName"> (List[str])  Dataset name for creation or for matching existing dataset </param>
    ## <param name="numDatasetPropertyInput"> (List[int])  Number of dataset property names input for each dataset input </param>
    ## <param name="datasetPropertyNames"> (List[str])  Dataset property names; to specify required properties when creating new dataset or for updating existing dataset properties </param>
    ## <param name="datasetPropertyValues"> (List[str])  Dataset property values; need to match 1-1 with above datasetPropertyNames </param>
    ## <param name="ownershipToMatchForNewDataset"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  Teamcenter object used to assign new dataset owner, default is current owner if set to NULL_TAG </param>
    ## <param name="fileVolumeToStore"> (@link PdmFile List[NXOpen.PDM.PdmFile]@endlink)  Teamcenter volume for storing file, default is current session volume if set to NULL </param>
    ## <param name="toolUsed"> (List[str])  Teamcenter toolUsed for new dataset </param>
    ## <param name="datasetDescription"> (List[str])  Dataset description for new dataset </param>
    ## <param name="alwaysCreateNewDataset"> (List[bool])  False (default) - use existing if present; True - always create new </param>
    ## <param name="createNewDatasetVersion"> (List[bool])  False (default) - use existing if present; True - create new version even if present </param>
    ## <param name="refreshInSessionLoadedLMD"> (List[bool])  True (default) - refresh in-session loaded Last-Modified-Date; False  - do nothing </param>
    ## <param name="numNamedReferencesPerInput"> (List[int])  Number of named references input for each dataset input </param>
    ## <param name="namedReferenceName"> (List[str])  Named reference name. Array size is total number of named references </param>
    ## <param name="isText"> (List[bool])  Named reference isText flag. Array size is total number of named references </param>
    ## <param name="filePath"> (List[str])  Named reference file path. Array size is total number of named references </param>
    ## <param name="logicalFileName"> (List[str])  Named reference logical filename. Array size is total number of named references </param>
    ## <param name="allowReplace"> (List[bool])  True (default) - replace existing if present; False - always create new. Array size is total number of named references </param>
    ## <param name="outputFiles"> (bool)  False (default) - do not return files; True - return files </param>
    def SaveAttachedFiles(self, associatedObject: List[NXOpen.NXObject], associationTypeName: List[str], datasetTypeName: List[str], datasetName: List[str], numDatasetPropertyInput: List[int], datasetPropertyNames: List[str], datasetPropertyValues: List[str], ownershipToMatchForNewDataset: List[NXOpen.NXObject], fileVolumeToStore: List[PdmFile], toolUsed: List[str], datasetDescription: List[str], alwaysCreateNewDataset: List[bool], createNewDatasetVersion: List[bool], refreshInSessionLoadedLMD: List[bool], numNamedReferencesPerInput: List[int], namedReferenceName: List[str], isText: List[bool], filePath: List[str], logicalFileName: List[str], allowReplace: List[bool], outputFiles: bool) -> Tuple[List[int], List[PdmFile]]:
        """
         Save Attached Files To Teamcenter.
                Save attached files for given specifications.
                 . associatedObject - Teamcenter object the files are attached to; only Parts or Design Elements are supported
                 . associationTypeName - Teamcenter relation type name
                 . datasetTypeName - Teamcenter dataset type name
                 . datasetName - Dataset name for creation or for matching existing dataset
                 . numDatasetPropertyInput - Number of dataset property names input for each dataset input
                 . numTotalDatasetProperties - Number of total dataset properties
                 . datasetPropertyNames - To specify required properties when creating new dataset or for updating existing dataset properties
                 . datasetPropertyValues - Dataset property values; need to match one-to-one with datasetPropertyNames
                 . ownershipToMatchForNewDataset - Teamcenter object used to assign new dataset owner, default is current user if not set
                 . fileVolumeToStore - Teamcenter volume for storing file, default is current session volume if not set
                 . toolUsed - Teamcenter toolUsed for new dataset
                 . datasetDescription - Dataset description for new dataset
                 . alwaysCreateNewDataset - Flag indicating if a new dataset should always be created
                 . createNewDatasetVersion - Flag indicating if new dataset version should be created
                 . refreshInSessionLoadedLMD - Flag indicating if in-session loaded Last-Modified-Date should be refreshed
                 . numNamedReferencesPerInput - Number of named references input for each dataset input
                 . numTotalNamedReferences - Number of total named references input
                 . namedReferenceName - Named reference name for each named reference input
                 . isText - Named reference isText flag for each named reference input
                 . filePath - Named reference file path for each named reference input
                 . logicalFileName - Named reference logical filename for each named reference input
                 . allowReplace - Flag indicating to replace if named reference already exists for each named reference input
                 . outputFiles - Flag indicating if files should be returned
                
         @return A tuple consisting of (resultCodes, files). 
         - resultCodes is: List[int]. Result codes. Success (0), failure (non-zero). Array size is total number of named references .
         - files is: @link PdmFile List[NXOpen.PDM.PdmFile]@endlink. Output - arry of PdmFiles. Array size is total number of named references .

        """
        pass
    
import NXOpen
##  Represents find criteria objects 
## 
##   <br>  Created in NX11.0.0  <br> 

class FindCriteria(NXOpen.TransientObject): 
    """ Represents find criteria objects """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  This API returns the search query name, entries, and values. 
    ##  @return A tuple consisting of (queryName, entries, values). 
    ##  - queryName is: str. Search query name .
    ##  - entries is: List[str]. Search criteria entries .
    ##  - values is: List[str]. Search criteria values .

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetCriteria(self) -> Tuple[str, List[str], List[str]]:
        """
         This API returns the search query name, entries, and values. 
         @return A tuple consisting of (queryName, entries, values). 
         - queryName is: str. Search query name .
         - entries is: List[str]. Search criteria entries .
         - values is: List[str]. Search criteria values .

        """
        pass
    
    ##  This API sets the search query name, entries, and values. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="queryName"> (str)  Search query name </param>
    ## <param name="entries"> (List[str])  Search criteria entries </param>
    ## <param name="values"> (List[str])  Search criteria values </param>
    def SetCriteria(self, queryName: str, entries: List[str], values: List[str]) -> None:
        """
         This API sets the search query name, entries, and values. 
        """
        pass
    
import NXOpen
## 
##         Represents the class that contains database business logic or pre-creation information for the objects.
##      <br> Instances of this class can be accessed through various application specific builders  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class GenericObjectAttributeHolder(NXOpen.NXObject): 
    """
        Represents the class that contains database business logic or pre-creation information for the objects.
    """
    pass


import NXOpen
##  An interface class for objects that own attribute groups. 
## 
##   <br>  Created in NX9.0.0  <br> 

class IAttributeGroupOwner(NXOpen.Object): 
    """ An interface class for objects that own attribute groups. """


    ##  Creates an attribute group for a @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink , based on an attribute
    ##         group type.  An attribute group type is represented by an @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink .
    ##     
    ##  @return attributeGroup (@link AttributeGroup NXOpen.PDM.AttributeGroup@endlink):  The new attribute group. .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeGroupDescription"> (@link AttributeGroupDescription NXOpen.PDM.AttributeGroupDescription@endlink) </param>
    @abstractmethod
    def Create(self, attributeGroupDescription: AttributeGroupDescription) -> AttributeGroup:
        """
         Creates an attribute group for a @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink , based on an attribute
                group type.  An attribute group type is represented by an @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink .
            
         @return attributeGroup (@link AttributeGroup NXOpen.PDM.AttributeGroup@endlink):  The new attribute group. .
        """
        pass
    
    ##  Creates a @link NXOpen::PDM::AttributeGroupReviseBuilder NXOpen::PDM::AttributeGroupReviseBuilder@endlink  object.  The builder creates a
    ##         revision for each attribute group in the input list of existing attribute groups. 
    ##  @return attributeGroupReviseBuilder (@link AttributeGroupReviseBuilder NXOpen.PDM.AttributeGroupReviseBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## <param name="attirbuteGroupOwner"> (@link IAttributeGroupOwner NXOpen.PDM.IAttributeGroupOwner@endlink) </param>
    ## <param name="attributeGroups"> (@link AttributeGroup List[NXOpen.PDM.AttributeGroup]@endlink)   </param>
    @abstractmethod
    @overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: List[AttributeGroup]) -> AttributeGroupReviseBuilder:
        """
         Creates a @link NXOpen::PDM::AttributeGroupReviseBuilder NXOpen::PDM::AttributeGroupReviseBuilder@endlink  object.  The builder creates a
                revision for each attribute group in the input list of existing attribute groups. 
         @return attributeGroupReviseBuilder (@link AttributeGroupReviseBuilder NXOpen.PDM.AttributeGroupReviseBuilder@endlink):   .
        """
        pass
    
    ##  The builder will do a revise or save-as operation for each attribute group in the input list of existing attribute groups 
    ##         depending on input operation type. 
    ##  @return attributeGroupReviseBuilder (@link AttributeGroupReviseBuilder NXOpen.PDM.AttributeGroupReviseBuilder@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="attirbuteGroupOwner"> (@link IAttributeGroupOwner NXOpen.PDM.IAttributeGroupOwner@endlink) </param>
    ## <param name="attributeGroups"> (@link AttributeGroup List[NXOpen.PDM.AttributeGroup]@endlink)   </param>
    ## <param name="keepOriginal"> (bool)   </param>
    ## <param name="saveAsActionType"> (@link AttributeGroupReviseBuilder.SaveAsActionType NXOpen.PDM.AttributeGroupReviseBuilder.SaveAsActionType@endlink)   </param>
    @abstractmethod
    @overload
    def CreateAttributeGroupReviseBuilder(self, attributeGroups: List[AttributeGroup], keepOriginal: bool, saveAsActionType: AttributeGroupReviseBuilder.SaveAsActionType) -> AttributeGroupReviseBuilder:
        """
         The builder will do a revise or save-as operation for each attribute group in the input list of existing attribute groups 
                depending on input operation type. 
         @return attributeGroupReviseBuilder (@link AttributeGroupReviseBuilder NXOpen.PDM.AttributeGroupReviseBuilder@endlink):   .
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink  objects representing the attribute
    ##         group types supported by this object. 
    ##  @return attributeGroups (@link AttributeGroupDescription List[NXOpen.PDM.AttributeGroupDescription]@endlink):   .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetAttributeGroupDescriptions(self) -> List[AttributeGroupDescription]:
        """
         Returns the @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink  objects representing the attribute
                group types supported by this object. 
         @return attributeGroups (@link AttributeGroupDescription List[NXOpen.PDM.AttributeGroupDescription]@endlink):   .
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::AttributeGroup NXOpen::PDM::AttributeGroup@endlink  objects owned by this object. 
    ##  @return attributeGroups (@link AttributeGroup List[NXOpen.PDM.AttributeGroup]@endlink):   .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    @abstractmethod
    def GetAttributeGroups(self) -> List[AttributeGroup]:
        """
         Returns the @link NXOpen::PDM::AttributeGroup NXOpen::PDM::AttributeGroup@endlink  objects owned by this object. 
         @return attributeGroups (@link AttributeGroup List[NXOpen.PDM.AttributeGroup]@endlink):   .
        """
        pass
    
import NXOpen
##  An interface to perform clone operations  <br> This is an abstract class, and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ICloneOperation(NXOpen.TaggedObject): 
    """ An interface to perform clone operations """


    ##  This API could be used by application to add related parts in export/clone operation. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def AddApplicationRelatedParts(self) -> None:
        """
         This API could be used by application to add related parts in export/clone operation. 
        """
        pass
    
    ##  This API adds an assembly to the operation. Any load errors will be placed in the loadStatus argument. 
    ##  @return loadStatus (@link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="assemblyName"> (str) </param>
    def AddAssembly(self, assemblyName: str) -> NXOpen.PartLoadStatus:
        """
         This API adds an assembly to the operation. Any load errors will be placed in the loadStatus argument. 
         @return loadStatus (@link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink): .
        """
        pass
    
    ##  This API adds a part to the operation. If the part is an assembly part, any components
    ##             of the assembly, not already in the operation, will be added as name-only references. 
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partName"> (str) </param>
    def AddPart(self, partName: str) -> None:
        """
         This API adds a part to the operation. If the part is an assembly part, any components
                    of the assembly, not already in the operation, will be added as name-only references. 
                
        """
        pass
    
    ##  This API applies checkin/checkout flags as appropriate for the export operation. 
    ##  @return namingWarnings (@link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def ApplyCICODefaults(self) -> NXOpen.AssyCloneNamingFailures:
        """
         This API applies checkin/checkout flags as appropriate for the export operation. 
         @return namingWarnings (@link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink): .
        """
        pass
    
    ##  This API performs the export/clone operation, if any naming failures generated during the operation will be
    ##             reported through the namingFailures argument and naming warnings through namingWarnings argument.
    ##             In case of naming failures the operation will not be performed. 
    ##             If skipExecute is true, then only the default values will be populated on objects, but export operation will not be performed(just like dry run).
    ##             If skipExecute is false, then first default values will be populated on objects and then export will be performed.
    ##         
    ##  @return A tuple consisting of (namingFailures, namingWarnings). 
    ##  - namingFailures is: @link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink.
    ##  - namingWarnings is: @link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink.

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="skipExecute"> (bool) </param>
    def ApplyDefaultsAndExecute(self, skipExecute: bool) -> Tuple[NXOpen.AssyCloneNamingFailures, NXOpen.AssyCloneNamingFailures]:
        """
         This API performs the export/clone operation, if any naming failures generated during the operation will be
                    reported through the namingFailures argument and naming warnings through namingWarnings argument.
                    In case of naming failures the operation will not be performed. 
                    If skipExecute is true, then only the default values will be populated on objects, but export operation will not be performed(just like dry run).
                    If skipExecute is false, then first default values will be populated on objects and then export will be performed.
                
         @return A tuple consisting of (namingFailures, namingWarnings). 
         - namingFailures is: @link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink.
         - namingWarnings is: @link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink.

        """
        pass
    
    ##  This API assigns the final name for the cloned component using the specified naming technique option. 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectToBeCloned"> (@link AssyCloneCompDisp NXOpen.PDM.AssyCloneCompDisp@endlink) </param>
    ## <param name="namingTechnique"> (@link NamingTechniqueOption NXOpen.PDM.NamingTechniqueOption@endlink) </param>
    ## <param name="finalName"> (str) </param>
    def AssignCloneNaming(self, objectToBeCloned: AssyCloneCompDisp, namingTechnique: NamingTechniqueOption, finalName: str) -> int:
        """
         This API assigns the final name for the cloned component using the specified naming technique option. 
         @return status (int): .
        """
        pass
    
    ##  This API assigns an explicit disposition to the specified object undergoing clone (which represents a component part referenced in the input assembly).
    ##             Specifying an explicit disposition assignment means the component will not take advantage of the default disposition value (even if the explicit
    ##             disposition assigned was equal to the current default disposition value).
    ## 
    ##             Disposition assignments in a export/clone operation can trigger disposition cascading. Disposition cascading is the automatic assignment of
    ##             dispositions made to related components in order to protect the seed assembly from modification. If disposition cascading occurs as a result
    ##             of a disposition assignment, the 'cascadeDispositions' argument will be true. The 'cascadedComponentDispositions' argument will contain the list of objects
    ##             to which the cascaded disposition was assigned and 'numCascadedComponents' will indicate the number of objects in that list.
    ##         
    ##  @return A tuple consisting of (cascadeDispositions, cascadedComponentDispositions, conflictingComponentDispositions). 
    ##  - cascadeDispositions is: bool.
    ##  - cascadedComponentDispositions is: @link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink.
    ##  - conflictingComponentDispositions is: @link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink.

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectToBeCloned"> (@link AssyCloneCompDisp NXOpen.PDM.AssyCloneCompDisp@endlink) </param>
    ## <param name="action"> (@link ExistingPartAction NXOpen.PDM.ExistingPartAction@endlink) </param>
    def AssignCompDisposition(self, objectToBeCloned: AssyCloneCompDisp, action: ExistingPartAction) -> Tuple[bool, List[AssyCloneCompDisp], List[AssyCloneCompDisp]]:
        """
         This API assigns an explicit disposition to the specified object undergoing clone (which represents a component part referenced in the input assembly).
                    Specifying an explicit disposition assignment means the component will not take advantage of the default disposition value (even if the explicit
                    disposition assigned was equal to the current default disposition value).
        
                    Disposition assignments in a export/clone operation can trigger disposition cascading. Disposition cascading is the automatic assignment of
                    dispositions made to related components in order to protect the seed assembly from modification. If disposition cascading occurs as a result
                    of a disposition assignment, the 'cascadeDispositions' argument will be true. The 'cascadedComponentDispositions' argument will contain the list of objects
                    to which the cascaded disposition was assigned and 'numCascadedComponents' will indicate the number of objects in that list.
                
         @return A tuple consisting of (cascadeDispositions, cascadedComponentDispositions, conflictingComponentDispositions). 
         - cascadeDispositions is: bool.
         - cascadedComponentDispositions is: @link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink.
         - conflictingComponentDispositions is: @link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink.

        """
        pass
    
    ##  This API is used to specify whether to attach the clone log file as a associated file to root parts in export/clone operation. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attachLogFileToAssociatedFiles"> (bool) </param>
    def AttachLogFileToAssociatedFiles(self, attachLogFileToAssociatedFiles: bool) -> None:
        """
         This API is used to specify whether to attach the clone log file as a associated file to root parts in export/clone operation. 
        """
        pass
    
    ##  This API sets the option in the current export/clone operation indicating whether associated files 
    ##             should by default be exported/cloned in the current operation. Associated files will be exported/cloned to the 
    ##             associated files root directory set by the user. If the associated files root directory is not set
    ##             then it will be exported/cloned to the directory of the exported/cloned parts.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="copyAssociatedFiles"> (bool) </param>
    def CopyAssociatedFiles(self, copyAssociatedFiles: bool) -> None:
        """
         This API sets the option in the current export/clone operation indicating whether associated files 
                    should by default be exported/cloned in the current operation. Associated files will be exported/cloned to the 
                    associated files root directory set by the user. If the associated files root directory is not set
                    then it will be exported/cloned to the directory of the exported/cloned parts.
                
        """
        pass
    
    ##  This API specifies whether the objects with the specified relation type to be exported/cloned when the component they are related to gets exported/cloned.
    ##             Relation types are strings containing the name of a nonmaster type defined in the database, such as 'manifestation', 'specification', and 'altrep'. 
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="relationTypes"> (List[str]) </param>
    ## <param name="copyRelations"> (bool) </param>
    def CopyRelations(self, relationTypes: List[str], copyRelations: bool) -> None:
        """
         This API specifies whether the objects with the specified relation type to be exported/cloned when the component they are related to gets exported/cloned.
                    Relation types are strings containing the name of a nonmaster type defined in the database, such as 'manifestation', 'specification', and 'altrep'. 
                
        """
        pass
    
    ##  This API allows the destruction of an instance of the ICloneOpertion. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def Destroy(self) -> None:
        """
         This API allows the destruction of an instance of the ICloneOpertion. 
        """
        pass
    
    ##  This API fetches the tags of all the components(objects to be cloned) that are added in current export/clone operation. 
    ##  @return objectsToBeCloned (@link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def FetchObjects(self) -> List[AssyCloneCompDisp]:
        """
         This API fetches the tags of all the components(objects to be cloned) that are added in current export/clone operation. 
         @return objectsToBeCloned (@link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink): .
        """
        pass
    
    ##  This API fetches all the objects that are to be excluded from the export operation due to ExcludeReferenceOnly, ExcludeNGC and ExcludeSuppressed options. 
    ##  @return objectsToBeExcluded (@link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def FetchObjectsToExcludeFromExport(self) -> List[AssyCloneCompDisp]:
        """
         This API fetches all the objects that are to be excluded from the export operation due to ExcludeReferenceOnly, ExcludeNGC and ExcludeSuppressed options. 
         @return objectsToBeExcluded (@link AssyCloneCompDisp List[NXOpen.PDM.AssyCloneCompDisp]@endlink): .
        """
        pass
    
    ##  This API will open a log file for writing. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logFileName"> (str) </param>
    def InitCloneLog(self, logFileName: str) -> None:
        """
         This API will open a log file for writing. 
        """
        pass
    
    ##  This API reads the specified log file and applies the data in it to the current export/clone operation.
    ##             If any naming failures occur during loading the log file, these will be reported via the namingFailures  
    ##             argument and any errors related to log file will be reported through logFileFailures argument.
    ## 
    ##             If processing the log file causes new assemblies to be loaded, then any errors
    ##             while loading the assembly will be reported through the loadStatus argument.
    ## 
    ##             If both naming failures and load failures occur, it is not defined which error
    ##             code the return value of the function will be - if you wish to report both
    ##             you should check the n_failures member of the namingFailures structure and
    ##             the failed member of the loadStatus structure to see if errors have occurred.
    ##         
    ##  @return A tuple consisting of (namingFailures, logFileFailures, loadStatus). 
    ##  - namingFailures is: @link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink.
    ##  - logFileFailures is: @link NXOpen.AssyCloneLogFileFailures NXOpen.AssyCloneLogFileFailures@endlink.
    ##  - loadStatus is: @link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink.

    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logFileName"> (str) </param>
    def LoadFromLogFile(self, logFileName: str) -> Tuple[NXOpen.AssyCloneNamingFailures, NXOpen.AssyCloneLogFileFailures, NXOpen.PartLoadStatus]:
        """
         This API reads the specified log file and applies the data in it to the current export/clone operation.
                    If any naming failures occur during loading the log file, these will be reported via the namingFailures  
                    argument and any errors related to log file will be reported through logFileFailures argument.
        
                    If processing the log file causes new assemblies to be loaded, then any errors
                    while loading the assembly will be reported through the loadStatus argument.
        
                    If both naming failures and load failures occur, it is not defined which error
                    code the return value of the function will be - if you wish to report both
                    you should check the n_failures member of the namingFailures structure and
                    the failed member of the loadStatus structure to see if errors have occurred.
                
         @return A tuple consisting of (namingFailures, logFileFailures, loadStatus). 
         - namingFailures is: @link NXOpen.AssyCloneNamingFailures NXOpen.AssyCloneNamingFailures@endlink.
         - logFileFailures is: @link NXOpen.AssyCloneLogFileFailures NXOpen.AssyCloneLogFileFailures@endlink.
         - loadStatus is: @link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink.

        """
        pass
    
    ##  This API will perform application specific post-commit tasks. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def PerformPostCommit(self) -> None:
        """
         This API will perform application specific post-commit tasks. 
        """
        pass
    
    ##  This API will perform application specific pre-commit tasks. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def PerformPreCommit(self) -> None:
        """
         This API will perform application specific pre-commit tasks. 
        """
        pass
    
    ##  This API is used to generate final name for parts being exported/cloned using renameStr. 
    ##             Here 'renameStr' will be used as final name for the first part,
    ##             For the remaining parts to have unique names, _number(where number will be 1,2,3....) will be appended to renameStr to generate unique final names.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="renameStr"> (str) </param>
    def RenameString(self, renameStr: str) -> None:
        """
         This API is used to generate final name for parts being exported/cloned using renameStr. 
                    Here 'renameStr' will be used as final name for the first part,
                    For the remaining parts to have unique names, _number(where number will be 1,2,3....) will be appended to renameStr to generate unique final names.
                
        """
        pass
    
    ##  This API is used to generate final name for parts being exported/cloned, by replacing baseString with newString. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="baseString"> (str) </param>
    ## <param name="newString"> (str) </param>
    def ReplaceString(self, baseString: str, newString: str) -> None:
        """
         This API is used to generate final name for parts being exported/cloned, by replacing baseString with newString. 
        """
        pass
    
    ##  This API will reprocess the non-component refs for objects to be exported/cloned which were not resolved first time. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def ReprocessNonComponentReferences(self) -> None:
        """
         This API will reprocess the non-component refs for objects to be exported/cloned which were not resolved first time. 
        """
        pass
    
    ##  This API sets the option to exclude the Non Geometric components from Export. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="excludeNGC"> (bool) </param>
    def SetCloneExcludeNGC(self, excludeNGC: bool) -> None:
        """
         This API sets the option to exclude the Non Geometric components from Export. 
        """
        pass
    
    ##  This API sets the option to exclude the reference only components from Export. 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="excludeReferenceOnly"> (bool) </param>
    def SetCloneExcludeReferenceOnly(self, excludeReferenceOnly: bool) -> None:
        """
         This API sets the option to exclude the reference only components from Export. 
        """
        pass
    
    ##  This API sets the option to export/clone the related CAE parts when cloning any CAD parts. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="cloneRelatedCae"> (@link CloneRelatedCae NXOpen.PDM.CloneRelatedCae@endlink) </param>
    def SetCloneRelatedCae(self, cloneRelatedCae: CloneRelatedCae) -> None:
        """
         This API sets the option to export/clone the related CAE parts when cloning any CAD parts. 
        """
        pass
    
    ##  This API sets the option to export/clone the related drawings when cloning any CAD parts. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="cloneRelatedDrawings"> (bool) </param>
    def SetCloneRelatedDrawings(self, cloneRelatedDrawings: bool) -> None:
        """
         This API sets the option to export/clone the related drawings when cloning any CAD parts. 
        """
        pass
    
    ##  This API sets the configuration context using the Revision Rule Name. 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="setDefault"> (bool) </param>
    ## <param name="revisionRuleName"> (str) </param>
    def SetConfigurationContextUsingRevRule(self, setDefault: bool, revisionRuleName: str) -> int:
        """
         This API sets the configuration context using the Revision Rule Name. 
         @return status (int): .
        """
        pass
    
    ##  This API sets the default action for the current export/clone operation. Any action inappropriate to the current operation will return an error. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="defaultAction"> (@link ExistingPartAction NXOpen.PDM.ExistingPartAction@endlink) </param>
    def SetDefaultAction(self, defaultAction: ExistingPartAction) -> None:
        """
         This API sets the default action for the current export/clone operation. Any action inappropriate to the current operation will return an error. 
        """
        pass
    
    ##  This API sets the dry run flag for the current export/clone operation. If this flag is true and JA_ICLONE_OPERATION_ApplyDefaultsAndExecute is called, 
    ##             the operation will actually not be performed. Please set JA_ICLONE_OPERATION_SetOutputLogFile for the log file to be generated.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="isDryRun"> (bool) </param>
    def SetDryRun(self, isDryRun: bool) -> None:
        """
         This API sets the dry run flag for the current export/clone operation. If this flag is true and JA_ICLONE_OPERATION_ApplyDefaultsAndExecute is called, 
                    the operation will actually not be performed. Please set JA_ICLONE_OPERATION_SetOutputLogFile for the log file to be generated.
                
        """
        pass
    
    ##  This API sets the final name on specified component. If duplicate names are identifed and allowDuplicates flag is true then
    ##             new name is generated for one of the component to avoid conflicts, if allowDuplicates flag is false then it will return
    ##             with appropriate error code. 
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="objectToBeCloned"> (@link AssyCloneCompDisp NXOpen.PDM.AssyCloneCompDisp@endlink) </param>
    ## <param name="finalName"> (str) </param>
    ## <param name="allowDuplicates"> (bool) </param>
    def SetFinalName(self, objectToBeCloned: AssyCloneCompDisp, finalName: str, allowDuplicates: bool) -> None:
        """
         This API sets the final name on specified component. If duplicate names are identifed and allowDuplicates flag is true then
                    new name is generated for one of the component to avoid conflicts, if allowDuplicates flag is false then it will return
                    with appropriate error code. 
                
        """
        pass
    
    ##  This API sets the value of the assembly load option for managed mode. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="loadOption"> (@link NXOpen.LoadOptions.ManagedModeLoadMethod NXOpen.LoadOptions.ManagedModeLoadMethod@endlink) </param>
    def SetLoadOption(self, loadOption: NXOpen.LoadOptions.ManagedModeLoadMethod) -> None:
        """
         This API sets the value of the assembly load option for managed mode. 
        """
        pass
    
    ##  This API sets the mixed rule naming conversion type. 
    ##             It enables user to combine the naming rule conversion types prefix, suffix and replace.
    ##             User must give atleast one of the naming rules input as non-empty value for mixed rule to work. 
    ##             Note: To enable replace naming rule (i.e. JA_ICLONE_OPERATION_ConversionRule_WithReplaceString)
    ##             user must give both stringToReplace and replacementString as non-empty values
    ##         
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prefixString"> (str) </param>
    ## <param name="suffixString"> (str) </param>
    ## <param name="stringToReplace"> (str) </param>
    ## <param name="replacementString"> (str) </param>
    def SetMixedRuleString(self, prefixString: str, suffixString: str, stringToReplace: str, replacementString: str) -> None:
        """
         This API sets the mixed rule naming conversion type. 
                    It enables user to combine the naming rule conversion types prefix, suffix and replace.
                    User must give atleast one of the naming rules input as non-empty value for mixed rule to work. 
                    Note: To enable replace naming rule (i.e. JA_ICLONE_OPERATION_ConversionRule_WithReplaceString)
                    user must give both stringToReplace and replacementString as non-empty values
                
        """
        pass
    
    ##  This API is used to set the naming technique, that will be used to generate final name for all the components being exported/cloned. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="namingTechnique"> (@link NamingTechniqueOption NXOpen.PDM.NamingTechniqueOption@endlink) </param>
    def SetNamingTechnique(self, namingTechnique: NamingTechniqueOption) -> None:
        """
         This API is used to set the naming technique, that will be used to generate final name for all the components being exported/cloned. 
        """
        pass
    
    ##  This API is used to specify the absolute path name of the log-file to be used to record export/clone operation,
    ##             If the value specified is NULL, no logfile will be written.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logFileName"> (str) </param>
    def SetOutputLogFile(self, logFileName: str) -> None:
        """
         This API is used to specify the absolute path name of the log-file to be used to record export/clone operation,
                    If the value specified is NULL, no logfile will be written.
                
        """
        pass
    
    ##  This API will decide how to treat the Part Family members present in export operation depending on 
    ##             the partFamilyTreatment input value.
    ## 
    ##             This API should be used only after assembly has been added for export operation as it will
    ##             iterate over all the Part Family Members added in export operation and set their behavior specified by
    ##             the partFamilyTreatment input value.
    ## 
    ##             Note 1: If 'UGMGR_CloneImportExportAutoRemovePFM' customer default is enabled then it will always treat
    ##             Part Family Members as 'Lost' in export, So please do not use this API if this customer default is enabled,
    ##             since using this API to change the behavior of Part Family Members will not work in that case. 
    ##             Note 2: If 'UGMGR_CloneImportExportAutoRemovePFM' customer default is disabled then the user must use this API
    ##             to set the desired behavior of Part Family Members. If the desired behavior is not set using this API then 
    ##             Part Family Members will not participate anymore in export operation.
    ##         
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partFamilyTreatment"> (@link PartFamilyTreatment NXOpen.PDM.PartFamilyTreatment@endlink) </param>
    def SetPartFamilyTreatment(self, partFamilyTreatment: PartFamilyTreatment) -> None:
        """
         This API will decide how to treat the Part Family members present in export operation depending on 
                    the partFamilyTreatment input value.
        
                    This API should be used only after assembly has been added for export operation as it will
                    iterate over all the Part Family Members added in export operation and set their behavior specified by
                    the partFamilyTreatment input value.
        
                    Note 1: If 'UGMGR_CloneImportExportAutoRemovePFM' customer default is enabled then it will always treat
                    Part Family Members as 'Lost' in export, So please do not use this API if this customer default is enabled,
                    since using this API to change the behavior of Part Family Members will not work in that case. 
                    Note 2: If 'UGMGR_CloneImportExportAutoRemovePFM' customer default is disabled then the user must use this API
                    to set the desired behavior of Part Family Members. If the desired behavior is not set using this API then 
                    Part Family Members will not participate anymore in export operation.
                
        """
        pass
    
    ##  This API is used to set the prefix string that will be prepended to generate final name for parts being exported/cloned. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="prefixStr"> (str) </param>
    def SetPrefixString(self, prefixStr: str) -> None:
        """
         This API is used to set the prefix string that will be prepended to generate final name for parts being exported/cloned. 
        """
        pass
    
    ##  This API is used to set the sufffix string that will be appended to generate final name for parts being exported/cloned. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="suffixStr"> (str) </param>
    def SetSuffixString(self, suffixStr: str) -> None:
        """
         This API is used to set the sufffix string that will be appended to generate final name for parts being exported/cloned. 
        """
        pass
    
    ##  This API is used to terminate the running export/clone operation. Error is returned if the terminate operation encounters an error. 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    def TerminateOperation(self) -> None:
        """
         This API is used to terminate the running export/clone operation. Error is returned if the terminate operation encounters an error. 
        """
        pass
    
import NXOpen
##  Represents list of values to be used in search query 
## 
##   <br>  Created in NX6.0.0  <br> 

class ListOfValues(NXOpen.TransientObject): 
    """ Represents list of values to be used in search query """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class LogicalElementRevision(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """
    pass


import NXOpen
## 
##         Represents the class that contains database business logic or pre-creation information for the objects.
##      <br> Instances of this class can be accessed through various application specific builders  <br> 
## 
##   <br>  Created in NX8.5.0  <br> 

class LogicalObject(NXOpen.NXObject): 
    """
        Represents the class that contains database business logic or pre-creation information for the objects.
    """
    pass


import NXOpen
import NXOpen.Assemblies
##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Instance of this class can not be created  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class ModelElementRevision(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """


    ##  Represents the positioning status of a design element 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AbsolutelyPositioned</term><description> 
    ## </description> </item><item><term> 
    ## OutOfDate</term><description> 
    ## </description> </item><item><term> 
    ## UpToDate</term><description> 
    ## </description> </item><item><term> 
    ## Unknown</term><description> 
    ## </description> </item></list>
    class PositioningStatus(Enum):
        """
        Members Include: <AbsolutelyPositioned> <OutOfDate> <UpToDate> <Unknown>
        """
        AbsolutelyPositioned: int
        OutOfDate: int
        UpToDate: int
        Unknown: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> ModelElementRevision.PositioningStatus:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) EffectivityFormula
    ##  Returns the formula string that represents the effectivity of this object in database.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return str
    @property
    def EffectivityFormula(self) -> str:
        """
        Getter for property: (str) EffectivityFormula
         Returns the formula string that represents the effectivity of this object in database.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) OwningCollaborativeDesign
    ##  Returns the owning @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @return NXOpen.CollaborativeDesign
    @property
    def OwningCollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) OwningCollaborativeDesign
         Returns the owning @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .  
          
                  
         
        """
        pass
    
    ##  Get all the partitions of this model element revision.
    ##         
    ##  @return partitions (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetMemberPartitions(self) -> List[NXOpen.Assemblies.Partition]:
        """
         Get all the partitions of this model element revision.
                
         @return partitions (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink): .
        """
        pass
    
    ##  Get the override part of this model element revision if it has any.
    ##         
    ##  @return overridePart (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetOverridePart(self) -> NXOpen.Part:
        """
         Get the override part of this model element revision if it has any.
                
         @return overridePart (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Gets positioning status of design element. 
    ##             It returns absolute position if design element is absolutely positioned, 
    ##             up-to-date if design element is in work collection of positioning task, 
    ##             out-of-date if design element is in context collection of positioning task and 
    ##             unknown if design element is not in any of the above.
    ##             Return status will be one of @link NXOpen::PDM::ModelElementRevision::PositioningStatus NXOpen::PDM::ModelElementRevision::PositioningStatus@endlink .
    ##         
    ##  @return positioningStatus (@link ModelElementRevision.PositioningStatus NXOpen.PDM.ModelElementRevision.PositioningStatus@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    def GetPositionStatus(self) -> ModelElementRevision.PositioningStatus:
        """
         Gets positioning status of design element. 
                    It returns absolute position if design element is absolutely positioned, 
                    up-to-date if design element is in work collection of positioning task, 
                    out-of-date if design element is in context collection of positioning task and 
                    unknown if design element is not in any of the above.
                    Return status will be one of @link NXOpen::PDM::ModelElementRevision::PositioningStatus NXOpen::PDM::ModelElementRevision::PositioningStatus@endlink .
                
         @return positioningStatus (@link ModelElementRevision.PositioningStatus NXOpen.PDM.ModelElementRevision.PositioningStatus@endlink): .
        """
        pass
    
    ##  Gets all positioning group which are associated with this design element.
    ##         
    ##  @return positioningGroups (@link NXOpen.Assemblies.PositioningGroup List[NXOpen.Assemblies.PositioningGroup]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    def GetPositioningGroups(self) -> List[NXOpen.Assemblies.PositioningGroup]:
        """
         Gets all positioning group which are associated with this design element.
                
         @return positioningGroups (@link NXOpen.Assemblies.PositioningGroup List[NXOpen.Assemblies.PositioningGroup]@endlink): .
        """
        pass
    
    ##  Determine whether this design element is absolutely positioned or not.
    ##         
    ##  @return absolutelyPositioned (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def IsAbsolutelyPositioned(self) -> bool:
        """
         Determine whether this design element is absolutely positioned or not.
                
         @return absolutelyPositioned (bool): .
        """
        pass
    
    ##  Determines whether this model element revision is excluded from spatial search.
    ##         
    ##  @return isExcludedFromSpatialSearch (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def IsExcludedFromSpatialSearch(self) -> bool:
        """
         Determines whether this model element revision is excluded from spatial search.
                
         @return isExcludedFromSpatialSearch (bool): .
        """
        pass
    
    ##  Determine whether this design element is part of positioning group or not.
    ##         
    ##  @return isMemberOfPositioningGroup (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def IsMemberOfPositioningGroup(self) -> bool:
        """
         Determine whether this design element is part of positioning group or not.
                
         @return isMemberOfPositioningGroup (bool): .
        """
        pass
    
    ##  Set or unset this model element revision from exclusion from spatial search.
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="excludeFromSpatialSearch"> (bool) </param>
    def SetExcludeFromSpatialSearch(self, excludeFromSpatialSearch: bool) -> None:
        """
         Set or unset this model element revision from exclusion from spatial search.
                
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Instance of this class can not be created  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class ModelElement(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """


    ## Getter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) OwningCollaborativeDesign
    ##  Returns the owning @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return NXOpen.CollaborativeDesign
    @property
    def OwningCollaborativeDesign(self) -> NXOpen.CollaborativeDesign:
        """
        Getter for property: (@link NXOpen.CollaborativeDesign NXOpen.CollaborativeDesign@endlink) OwningCollaborativeDesign
         Returns the owning @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .  
          
                  
         
        """
        pass
    
    ##  Get all the partitions of this model element revision.
    ##         
    ##  @return partitions (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetMemberPartitions(self) -> List[NXOpen.Assemblies.Partition]:
        """
         Get all the partitions of this model element revision.
                
         @return partitions (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink): .
        """
        pass
    
##  This enum is used to specify the naming technique. 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## AutoTranslate</term><description> 
## </description> </item><item><term> 
## NamingRule</term><description> 
## </description> </item><item><term> 
## AutoTranslateWithAlternateID</term><description> 
## </description> </item><item><term> 
## UserName</term><description> 
## </description> </item><item><term> 
## AutoGenerate</term><description> 
## </description> </item><item><term> 
## Default</term><description> 
## </description> </item></list>
class NamingTechniqueOption(Enum):
    """
    Members Include: <AutoTranslate> <NamingRule> <AutoTranslateWithAlternateID> <UserName> <AutoGenerate> <Default>
    """
    AutoTranslate: int
    NamingRule: int
    AutoTranslateWithAlternateID: int
    UserName: int
    AutoGenerate: int
    Default: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> NamingTechniqueOption:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


## 
##         Represents the class that contains information for the objects participating in import operation.
##      <br> Instances of this class can be accessed through various application specific builders  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class NativePartLogicalObject(LogicalObject): 
    """
        Represents the class that contains information for the objects participating in import operation.
    """


    ##  Gets the existing part action defined for this part 
    ##  @return existingPartAction (@link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetExistingPartAction(self) -> PartOperationImportBuilder.ExistingPartAction:
        """
         Gets the existing part action defined for this part 
         @return existingPartAction (@link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink): .
        """
        pass
    
    ##  Gets the final name of this logical object. 
    ##  @return finalName (str):  the database name assigned to the part being imported .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetFinalName(self) -> str:
        """
         Gets the final name of this logical object. 
         @return finalName (str):  the database name assigned to the part being imported .
        """
        pass
    
    ##  Gets the initial name of this logical object. 
    ##  @return initialName (str):  the filename of added for import .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetInitialName(self) -> str:
        """
         Gets the initial name of this logical object. 
         @return initialName (str):  the filename of added for import .
        """
        pass
    
    ##  Gets the validation mode setting defined for this part 
    ##  @return validationMode (@link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetValidationMode(self) -> PartOperationImportBuilder.Validation:
        """
         Gets the validation mode setting defined for this part 
         @return validationMode (@link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink): .
        """
        pass
    
    ##  Gets the validation rule set file browse option defined for this part 
    ##  @return browseOption (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetValidationRuleSetFileBrowseOption(self) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
        """
         Gets the validation rule set file browse option defined for this part 
         @return browseOption (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink): .
        """
        pass
    
    ##  Checks if the part represented by this logical object is a candidate for import.
    ##             The part is not a candidate for import if it is lost or name-only. 
    ##  @return isCandidateForImport (bool):  .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def IsCandidateForImport(self) -> bool:
        """
         Checks if the part represented by this logical object is a candidate for import.
                    The part is not a candidate for import if it is lost or name-only. 
         @return isCandidateForImport (bool):  .
        """
        pass
    
    ##  Gets the flag indicating whether part name is autoassigned or not. 
    ##  @return isPartNameAutoAssigned (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def IsPartNameAutoAssigned(self) -> bool:
        """
         Gets the flag indicating whether part name is autoassigned or not. 
         @return isPartNameAutoAssigned (bool): .
        """
        pass
    
    ##  Sets the existing part action defined for this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="existingPartAction"> (@link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink) </param>
    def SetExistingPartAction(self, existingPartAction: PartOperationImportBuilder.ExistingPartAction) -> None:
        """
         Sets the existing part action defined for this part 
        """
        pass
    
    ##  Sets the validation mode setting defined for this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="validationMode"> (@link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink) </param>
    def SetValidationMode(self, validationMode: PartOperationImportBuilder.Validation) -> None:
        """
         Sets the validation mode setting defined for this part 
        """
        pass
    
    ##  Sets the validation rule set file browse option defined for this part 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="browseOption"> (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink) </param>
    def SetValidationRuleSetFileBrowseOption(self, browseOption: PartOperationImportBuilder.ValidationRuleSetFileBrowseOption) -> None:
        """
         Sets the validation rule set file browse option defined for this part 
        """
        pass
    
import NXOpen
##  Represents a class that performs various operations on NonMaster Datasets 
## 
##   <br>  Created in NX11.0.0  <br> 

class NonMasterData(NXOpen.TransientObject): 
    """ Represents a class that performs various operations on NonMaster Datasets """


    ##  This enum is used to specify which non-master parts 
    ##         should be copied to new part during the save as operation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ##  save all during save as </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  save none during save as </description> </item></list>
    class CopyNonMasterPartsOption(Enum):
        """
        Members Include: <All> <NotSet>
        """
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> NonMasterData.CopyNonMasterPartsOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Create NonMaster list for the selected logical Object 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def CreateNonMasterListForLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
         Create NonMaster list for the selected logical Object 
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Sets the name the non-master part will get saved as. It will get saved as the
    ##         original non-master name if this method is not called. 
    ##  @return isNameValid (bool):  flag to indicate whether the newName is valid .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="oldName"> (str)  the non-master part whose save as name is being set here </param>
    ## <param name="newName"> (str)  the new name </param>
    def EditNonMasterToCopyName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called. 
         @return isNameValid (bool):  flag to indicate whether the newName is valid .
        """
        pass
    
    ## Get the nonmasters saveAs option for given logical object. Save As option can be one of these
    ##         @link NonMasterData::CopyNonMasterPartsOptionAll NonMasterData::CopyNonMasterPartsOptionAll@endlink  and 
    ##         @link NonMasterData::CopyNonMasterPartsOptionNone NonMasterData::CopyNonMasterPartsOptionNone@endlink 
    ##  @return saveOption (@link NonMasterData.CopyNonMasterPartsOption NXOpen.PDM.NonMasterData.CopyNonMasterPartsOption@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetCopyNonMasterPartsOption(self, logicalObject: LogicalObject) -> NonMasterData.CopyNonMasterPartsOption:
        """
        Get the nonmasters saveAs option for given logical object. Save As option can be one of these
                @link NonMasterData::CopyNonMasterPartsOptionAll NonMasterData::CopyNonMasterPartsOptionAll@endlink  and 
                @link NonMasterData::CopyNonMasterPartsOptionNone NonMasterData::CopyNonMasterPartsOptionNone@endlink 
         @return saveOption (@link NonMasterData.CopyNonMasterPartsOption NXOpen.PDM.NonMasterData.CopyNonMasterPartsOption@endlink): .
        """
        pass
    
    ##  Gets NonMaster list for the given logical Object 
    ##  @return partFileNames (List[str]):  Non-master part file names .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> List[str]:
        """
         Gets NonMaster list for the given logical Object 
         @return partFileNames (List[str]):  Non-master part file names .
        """
        pass
    
    ##  Returns whether or not the non-master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually
    ##         get saved during the save as operation. 
    ##  @return do_save_as (bool):  True means that this non-master will be saved.
    ##                 False means that this non-master will not be saved. .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="part_name"> (str)  the non-master part that the caller wants to save or not save </param>
    def IsNonMasterForLogicalObjectBeingCopied(self, logicalObject: LogicalObject, part_name: str) -> bool:
        """
         Returns whether or not the non-master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually
                get saved during the save as operation. 
         @return do_save_as (bool):  True means that this non-master will be saved.
                        False means that this non-master will not be saved. .
        """
        pass
    
    ## Set the nonmasters saveAs option for given logical object. Save As option can be one of these
    ##         @link NonMasterData::CopyNonMasterPartsOptionAll NonMasterData::CopyNonMasterPartsOptionAll@endlink  and 
    ##         @link NonMasterData::CopyNonMasterPartsOptionNone NonMasterData::CopyNonMasterPartsOptionNone@endlink 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="saveOption"> (@link NonMasterData.CopyNonMasterPartsOption NXOpen.PDM.NonMasterData.CopyNonMasterPartsOption@endlink) </param>
    def SetNonMasterSaveAsOption(self, logicalObject: LogicalObject, saveOption: NonMasterData.CopyNonMasterPartsOption) -> None:
        """
        Set the nonmasters saveAs option for given logical object. Save As option can be one of these
                @link NonMasterData::CopyNonMasterPartsOptionAll NonMasterData::CopyNonMasterPartsOptionAll@endlink  and 
                @link NonMasterData::CopyNonMasterPartsOptionNone NonMasterData::CopyNonMasterPartsOptionNone@endlink 
        """
        pass
    
    ##  Sets whether or not the non-master part specified will actually
    ##         get saved during the save as operation. True means that it will be
    ##         saved. False means that it will not be saved.  
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="partName"> (str)  the non-master part whose save option is being set here </param>
    def SetSelectedNonMasterToCopy(self, logicalObject: LogicalObject, partName: str) -> None:
        """
         Sets whether or not the non-master part specified will actually
                get saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.  
        """
        pass
    
import NXOpen
##  Represents a builder class that perofrms create operation <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateObjectCreateBuilder  NXOpen::PDM::PdmSession::CreateObjectCreateBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class ObjectCreateBuilder(NXOpen.Builder): 
    """ Represents a builder class that perofrms create operation"""


    ## Getter for property: (str) DefaultDestinationFolder
    ##  Returns the default destination folder string for the object being created.  
    ##   
    ##         The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
    ##         In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DefaultDestinationFolder(self) -> str:
        """
        Getter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the object being created.  
          
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    
    ## Setter for property: (str) DefaultDestinationFolder

    ##  Returns the default destination folder string for the object being created.  
    ##   
    ##         The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
    ##         In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultDestinationFolder.setter
    def DefaultDestinationFolder(self, defaultDestinationFolder: str):
        """
        Setter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the object being created.  
          
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    
    ##  Creates Pre-Creation LogicalObjects 
    ##  @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def CreateLogicalObjects(self) -> List[LogicalObject]:
        """
         Creates Pre-Creation LogicalObjects 
         @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
    ##  Returns an array of AttributeHolderObjects created as part of commit. 
    ##  @return attributeHolderObjects (@link GenericObjectAttributeHolder List[NXOpen.PDM.GenericObjectAttributeHolder]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetAttributeHolderObjects(self) -> List[GenericObjectAttributeHolder]:
        """
         Returns an array of AttributeHolderObjects created as part of commit. 
         @return attributeHolderObjects (@link GenericObjectAttributeHolder List[NXOpen.PDM.GenericObjectAttributeHolder]@endlink): .
        """
        pass
    
    ##  Set Types for which AttributeHolderObject needs to be created.
    ##            This method will remove all previously set types.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="tcTypes"> (List[str]) </param>
    ## <param name="baseTCTypes"> (List[str]) </param>
    def SetTypes(self, tcTypes: List[str], baseTCTypes: List[str]) -> None:
        """
         Set Types for which AttributeHolderObject needs to be created.
                   This method will remove all previously set types.
        """
        pass
    
import NXOpen
##  Represents Operation Errors to be returned in TCIN related operations 
## 
##   <br>  Created in NX8.5.0  <br> 

class OperationErrors(NXOpen.TransientObject): 
    """ Represents Operation Errors to be returned in TCIN related operations """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
import NXOpen
##  
##         Represents a base class that provides common methods for ordered elements group in a @link NXOpen::PDM::ElementGroup NXOpen::PDM::ElementGroup@endlink .
##      <br> Instance of this can not directly created.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class OrderedElementGroup(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for ordered elements group in a <ja_class>NXOpen.PDM.ElementGroup</ja_class>.
    """
    pass


import NXOpen
##  JA interface for PartAttributeAssignmentObserverCallbackData object  <br> This cannot be created  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PartAttributeAssignmentObserverCallbackData(NXOpen.TaggedObject): 
    """ JA interface for PartAttributeAssignmentObserverCallbackData object """


    ##  Gets the @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  for NX Objects participating in attribute assignment operation 
    ##  @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    def GetLogicalObjects(self) -> List[LogicalObject]:
        """
         Gets the @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  for NX Objects participating in attribute assignment operation 
         @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
import NXOpen
##  This class is responsible for invoking user registered callback on attribute assignment in NX  <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class PartAttributeAssignmentObserver(NXOpen.Object): 
    """ This class is responsible for invoking user registered callback on attribute assignment in NX """


    ##  User defined function which accepts logical objects and gets called on part attribute assignment
    ## A callback definition with the following input arguments: 
    ##  - @link PartAttributeAssignmentObserverCallbackData NXOpen.PDM.PartAttributeAssignmentObserverCallbackData@endlink
    ##  and no return type
    UserFunctionHandler = Callable[[PartAttributeAssignmentObserverCallbackData], None]
    
    
    ##  This function registers the user-defined function 
    ##  @return id (int):  The identifier of the method being registered. This can be used to unregister (using UnRegisterUserDefinedFunction()) if needed  .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="handler"> (@link PartAttributeAssignmentObserver.UserFunctionHandler NXOpen.PDM.PartAttributeAssignmentObserver.UserFunctionHandler@endlink)  method to register </param>
    def RegisterUserDefinedFunction(handler: PartAttributeAssignmentObserver.UserFunctionHandler) -> int:
        """
         This function registers the user-defined function 
         @return id (int):  The identifier of the method being registered. This can be used to unregister (using UnRegisterUserDefinedFunction()) if needed  .
        """
        pass
    
    ##  This function unregisters the user-defined function 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def UnRegisterUserDefinedFunction(id: int) -> None:
        """
         This function unregisters the user-defined function 
        """
        pass
    
import NXOpen
##  This class serves as the base class for NX Manager part builders. The
##         NX Manager part builders are used to create new parts in NX Manager mode.
## 
##          <br> 
##         This class is <b>deprecated in NX10</b> for "Create" and "Save As of master parts" operations.
##         This class should only be used in case of Save As Non Master parts and
##         Save As New Item Type Operations.
##         For Create of all parts use @link NXOpen::PDM::PartOperationBuilder NXOpen::PDM::PartOperationBuilder@endlink  and @link NXOpen::FileNew NXOpen::FileNew@endlink 
##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink .
##          <br> 
##      <br> This is an abstract class, and cannot be created.  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PartBuilder(NXOpen.TransientObject): 
    """ This class serves as the base class for NX Manager part builders. The
        NX Manager part builders are used to create new parts in NX Manager mode.

        <para>
        This class is <b>deprecated in NX10</b> for "Create" and "Save As of master parts" operations.
        This class should only be used in case of Save As Non Master parts and
        Save As New Item Type Operations.
        For Create of all parts use <ja_class>NXOpen.PDM.PartOperationBuilder</ja_class> and <ja_class>NXOpen.FileNew</ja_class>
        For Save As of master parts, use <ja_class>NXOpen.PDM.PartOperationCopyBuilder</ja_class>.
        </para>
    """


    ##  Tokens identifying every possible UG/Manager part selection dialog. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## ExportPartNew</term><description> 
    ##  File-\>Export-\>NXOpen.Part:New radio button</description> </item><item><term> 
    ## AssemblyDiagram</term><description> 
    ##  Assembly-\>Report-\>Assembly Diagram... </description> </item><item><term> 
    ## AssemblyCreateNewComponent</term><description> 
    ##  Assembly-\>NXOpen.Assemblies.Component-\>Create New... </description> </item><item><term> 
    ## Default</term><description> 
    ##  Default UG/Manager part selection dialog</description> </item></list>
    class Operation(Enum):
        """
        Members Include: <ExportPartNew> <AssemblyDiagram> <AssemblyCreateNewComponent> <Default>
        """
        ExportPartNew: int
        AssemblyDiagram: int
        AssemblyCreateNewComponent: int
        Default: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartBuilder.Operation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Contains part file name information 
    ## @link PartBuilderPartFileNameData_Struct NXOpen.PDM.PartBuilderPartFileNameData_Struct@endlink is an alias for @link PartBuilder.PartFileNameData NXOpen.PDM.PartBuilder.PartFileNameData@endlink.
    class PartFileNameData:
        """
         Contains part file name information 
        @link PartBuilderPartFileNameData_Struct NXOpen.PDM.PartBuilderPartFileNameData_Struct@endlink is an alias for @link PartBuilder.PartFileNameData NXOpen.PDM.PartBuilder.PartFileNameData@endlink.
        """
        ## Getter for property :(str) PartFileName
        ## Part file name
        ## @return str
        @property
        def PartFileName(self) -> str:
            """
            Getter for property PartFileName
            Part file name

            """
            pass
        
        ## Setter for property :(str) PartFileName
        @PartFileName.setter
        def PartFileName(self, value: str):
            """
            Getter for property PartFileName
            Part file name
            Setter for property PartFileName
            Part file name

            """
            pass
        
        ## Getter for property :(bool) PartFileNameModifiable
        ## False if part file name is not modifiable
        ## @return bool
        @property
        def PartFileNameModifiable(self) -> bool:
            """
            Getter for property PartFileNameModifiable
            False if part file name is not modifiable

            """
            pass
        
        ## Setter for property :(bool) PartFileNameModifiable
        @PartFileNameModifiable.setter
        def PartFileNameModifiable(self, value: bool):
            """
            Getter for property PartFileNameModifiable
            False if part file name is not modifiable
            Setter for property PartFileNameModifiable
            False if part file name is not modifiable

            """
            pass
        
    
    
    ##  Contains part number information.
    ## @link PartBuilderPartNumberData_Struct NXOpen.PDM.PartBuilderPartNumberData_Struct@endlink is an alias for @link PartBuilder.PartNumberData NXOpen.PDM.PartBuilder.PartNumberData@endlink.
    class PartNumberData:
        """
         Contains part number information.
        @link PartBuilderPartNumberData_Struct NXOpen.PDM.PartBuilderPartNumberData_Struct@endlink is an alias for @link PartBuilder.PartNumberData NXOpen.PDM.PartBuilder.PartNumberData@endlink.
        """
        ## Getter for property :(str) PartName
        ## The part name
        ## @return str
        @property
        def PartName(self) -> str:
            """
            Getter for property PartName
            The part name

            """
            pass
        
        ## Setter for property :(str) PartName
        @PartName.setter
        def PartName(self, value: str):
            """
            Getter for property PartName
            The part name
            Setter for property PartName
            The part name

            """
            pass
        
        ## Getter for property :(bool) PartNameModifiable
        ## Modifiable flag for part name.
        ## @return bool
        @property
        def PartNameModifiable(self) -> bool:
            """
            Getter for property PartNameModifiable
            Modifiable flag for part name.

            """
            pass
        
        ## Setter for property :(bool) PartNameModifiable
        @PartNameModifiable.setter
        def PartNameModifiable(self, value: bool):
            """
            Getter for property PartNameModifiable
            Modifiable flag for part name.
            Setter for property PartNameModifiable
            Modifiable flag for part name.

            """
            pass
        
        ## Getter for property :(str) PartDescription
        ## The part description
        ## @return str
        @property
        def PartDescription(self) -> str:
            """
            Getter for property PartDescription
            The part description

            """
            pass
        
        ## Setter for property :(str) PartDescription
        @PartDescription.setter
        def PartDescription(self, value: str):
            """
            Getter for property PartDescription
            The part description
            Setter for property PartDescription
            The part description

            """
            pass
        
        ## Getter for property :(bool) PartDescriptionModifiable
        ## Modifiable flag for part description.
        ## @return bool
        @property
        def PartDescriptionModifiable(self) -> bool:
            """
            Getter for property PartDescriptionModifiable
            Modifiable flag for part description.

            """
            pass
        
        ## Setter for property :(bool) PartDescriptionModifiable
        @PartDescriptionModifiable.setter
        def PartDescriptionModifiable(self, value: bool):
            """
            Getter for property PartDescriptionModifiable
            Modifiable flag for part description.
            Setter for property PartDescriptionModifiable
            Modifiable flag for part description.

            """
            pass
        
        ## Getter for property :(str) PartNumber
        ## The multifield key
        ## @return str
        @property
        def PartNumber(self) -> str:
            """
            Getter for property PartNumber
            The multifield key

            """
            pass
        
        ## Setter for property :(str) PartNumber
        @PartNumber.setter
        def PartNumber(self, value: str):
            """
            Getter for property PartNumber
            The multifield key
            Setter for property PartNumber
            The multifield key

            """
            pass
        
        ## Getter for property :(bool) PartNumberModifiable
        ## Modifiable flag for part number.
        ## @return bool
        @property
        def PartNumberModifiable(self) -> bool:
            """
            Getter for property PartNumberModifiable
            Modifiable flag for part number.

            """
            pass
        
        ## Setter for property :(bool) PartNumberModifiable
        @PartNumberModifiable.setter
        def PartNumberModifiable(self, value: bool):
            """
            Getter for property PartNumberModifiable
            Modifiable flag for part number.
            Setter for property PartNumberModifiable
            Modifiable flag for part number.

            """
            pass
        
    
    
    ##  Contains part revision information 
    ## @link PartBuilderPartRevisionData_Struct NXOpen.PDM.PartBuilderPartRevisionData_Struct@endlink is an alias for @link PartBuilder.PartRevisionData NXOpen.PDM.PartBuilder.PartRevisionData@endlink.
    class PartRevisionData:
        """
         Contains part revision information 
        @link PartBuilderPartRevisionData_Struct NXOpen.PDM.PartBuilderPartRevisionData_Struct@endlink is an alias for @link PartBuilder.PartRevisionData NXOpen.PDM.PartBuilder.PartRevisionData@endlink.
        """
        ## Getter for property :(str) PartRevision
        ## Part revision
        ## @return str
        @property
        def PartRevision(self) -> str:
            """
            Getter for property PartRevision
            Part revision

            """
            pass
        
        ## Setter for property :(str) PartRevision
        @PartRevision.setter
        def PartRevision(self, value: str):
            """
            Getter for property PartRevision
            Part revision
            Setter for property PartRevision
            Part revision

            """
            pass
        
        ## Getter for property :(bool) PartRevisionModifiable
        ## Revision Modifiable flag.
        ## @return bool
        @property
        def PartRevisionModifiable(self) -> bool:
            """
            Getter for property PartRevisionModifiable
            Revision Modifiable flag.

            """
            pass
        
        ## Setter for property :(bool) PartRevisionModifiable
        @PartRevisionModifiable.setter
        def PartRevisionModifiable(self, value: bool):
            """
            Getter for property PartRevisionModifiable
            Revision Modifiable flag.
            Setter for property PartRevisionModifiable
            Revision Modifiable flag.

            """
            pass
        
    
    
    ## This method generates a part file name given an input part file type and
    ##         assigns this part file name to the builder.
    ## 
    ##          <br> 
    ##         This method depends on the part type, part number, and part revision
    ##         already being set on the builder. Therefore, a call to
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
    ##         more likely, calls to @link PDM::PartBuilder::AssignPartNumber PDM::PartBuilder::AssignPartNumber@endlink  and
    ##         @link PDM::PartBuilder::AssignPartRevision PDM::PartBuilder::AssignPartRevision@endlink  must be made
    ##         before calling this method.
    ##          <br> 
    ## 
    ##          <br> 
    ##         If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         (as will typically be the case) then the <b>part_file_type</b> and
    ##         <b>part_file_name</b> parameters of
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         should be set to NULL so that the builder will use the values assigned
    ##         by this method. Otherwise, CreatePartSpec will override the values assigned
    ##         here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
    ##         parameters to the builder.
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations.  Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
    ##         instead.
    ##          <br> 
    ##         
    ##  @return part_file_name (str):  the assigned part file name .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartBuilder NXOpen.PDM.PartBuilder@endlink) </param>
    ## <param name="part_file_type"> (str)  the part file type. Note that if the
    ##                part file type is "master", then this method will return NULL but
    ##                will still set the part file type in the builder. </param>
    @overload
    def AssignPartFileName(self, part_file_type: str) -> str:
        """
        This method generates a part file name given an input part file type and
                assigns this part file name to the builder.
        
                 <br> 
                This method depends on the part type, part number, and part revision
                already being set on the builder. Therefore, a call to
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
                more likely, calls to @link PDM::PartBuilder::AssignPartNumber PDM::PartBuilder::AssignPartNumber@endlink  and
                @link PDM::PartBuilder::AssignPartRevision PDM::PartBuilder::AssignPartRevision@endlink  must be made
                before calling this method.
                 <br> 
        
                 <br> 
                If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                (as will typically be the case) then the <b>part_file_type</b> and
                <b>part_file_name</b> parameters of
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                should be set to NULL so that the builder will use the values assigned
                by this method. Otherwise, CreatePartSpec will override the values assigned
                here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
                parameters to the builder.
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations.  Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
                instead.
                 <br> 
                
         @return part_file_name (str):  the assigned part file name .
        """
        pass
    
    ## This method generates a part file name and assigns this part 
    ##         file name to the builder.
    ## 
    ##          <br> 
    ##         If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         then the <b>part_file_name</b> parameter of @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         should be set to NULL so that the builder will use the value assigned
    ##         by this method. Otherwise, CreatePartSpec will override the value assigned
    ##         here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
    ##         parameters to the builder.
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations.  Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
    ##         instead.
    ##          <br> 
    ##         
    ##  @return part_info (@link PartBuilder.PartFileNameData NXOpen.PDM.PartBuilder.PartFileNameData@endlink): .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartBuilder NXOpen.PDM.PartBuilder@endlink) </param>
    ## <param name="part_number"> (str) Part Number</param>
    ## <param name="part_revision"> (str)  part revision</param>
    ## <param name="part_file_name_type"> (str) Part file name type.
    ##                 Note that if the part file type is "master", then this method will set the 
    ##                 field <b>PartFileName</b> of @link PDM::PartBuilder::PartFileNameData PDM::PartBuilder::PartFileNameData@endlink 
    ##                 with NULL</param>
    ## <param name="old_part_file_name"> (str) Old part file name</param>
    @overload
    def AssignPartFileName(self, part_number: str, part_revision: str, part_file_name_type: str, old_part_file_name: str) -> PartBuilder.PartFileNameData:
        """
        This method generates a part file name and assigns this part 
                file name to the builder.
        
                 <br> 
                If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                then the <b>part_file_name</b> parameter of @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                should be set to NULL so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the values of the <b>part_file_type</b> and <b>part_file_name</b>
                parameters to the builder.
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations.  Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
                instead.
                 <br> 
                
         @return part_info (@link PartBuilder.PartFileNameData NXOpen.PDM.PartBuilder.PartFileNameData@endlink): .
        """
        pass
    
    ##  This method generates a part number given an input part type and
    ##         assigns this part number to the builder.
    ## 
    ##          <br> The input part type will also be assigned to the builder. If the
    ##         input part type is NULL then this method will fail unless the part
    ##         type has already been set on the builder via a previous call to this method
    ##         or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
    ##          <br> 
    ## 
    ##          <br> 
    ##         If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         (as will typically be the case) then the <b>part_type</b> and
    ##         <b>part_number</b> parameters of
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         should be set to NULL so that the builder will use the values assigned
    ##         by this method. Otherwise, CreatePartSpec will override the values assigned
    ##         here and assign the values of the <b>part_type</b> and <b>part_number</b>
    ##         parameters to the builder.
    ##          <br> 
    ## 
    ##          <br> 
    ##         The output part_number:
    ##         In case of Default Domain: it is Teamcenter item ID.
    ##         In case of non-Default Domain: it is the multifield key.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
    ##         for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
    ##         To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
    ##         @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_NO attribute.
    ##          <br> 
    ##         
    ##  @return part_number (str):  the assigned multifield key .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartBuilder NXOpen.PDM.PartBuilder@endlink) </param>
    ## <param name="part_type"> (str)  the part type </param>
    @overload
    def AssignPartNumber(self, part_type: str) -> str:
        """
         This method generates a part number given an input part type and
                assigns this part number to the builder.
        
                 <br> The input part type will also be assigned to the builder. If the
                input part type is NULL then this method will fail unless the part
                type has already been set on the builder via a previous call to this method
                or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
                 <br> 
        
                 <br> 
                If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                (as will typically be the case) then the <b>part_type</b> and
                <b>part_number</b> parameters of
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                should be set to NULL so that the builder will use the values assigned
                by this method. Otherwise, CreatePartSpec will override the values assigned
                here and assign the values of the <b>part_type</b> and <b>part_number</b>
                parameters to the builder.
                 <br> 
        
                 <br> 
                The output part_number:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
                for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
                To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
                @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_NO attribute.
                 <br> 
                
         @return part_number (str):  the assigned multifield key .
        """
        pass
    
    ##  This method generates a part number given an input part type and
    ##         sets this part number to the builder.
    ## 
    ##          <br> The input part type will also be assigned to the builder. If the
    ##         input part type is NULL then this method will fail unless the part
    ##         type has already been set on the builder via a previous call to this method
    ##         or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
    ##          <br> 
    ## 
    ##          <br> 
    ##         If this overloaded method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         then the <b>part_number</b> parameter of
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         should be set to NULL so that the builder will use the value assigned
    ##         by this method. Otherwise, CreatePartSpec will override the value assigned
    ##         here and assign the value of <b>part_number</b>
    ##         parameter to the builder.
    ##          <br> 
    ## 
    ##          <br> 
    ##         The output part_number in part_info structure:
    ##         In case of Default Domain: it is Teamcenter item ID.
    ##         In case of non-Default Domain: it is the multifield key.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
    ##         for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
    ##         To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
    ##         @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_NO attribute.
    ##          <br> 
    ##         
    ##  @return part_info (@link PartBuilder.PartNumberData NXOpen.PDM.PartBuilder.PartNumberData@endlink):  Contains part number information.
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartBuilder NXOpen.PDM.PartBuilder@endlink) </param>
    ## <param name="old_part_number"> (str)  Old part number </param>
    ## <param name="part_type"> (str)  Part type </param>
    @overload
    def AssignPartNumber(self, old_part_number: str, part_type: str) -> PartBuilder.PartNumberData:
        """
         This method generates a part number given an input part type and
                sets this part number to the builder.
        
                 <br> The input part type will also be assigned to the builder. If the
                input part type is NULL then this method will fail unless the part
                type has already been set on the builder via a previous call to this method
                or to @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink .
                 <br> 
        
                 <br> 
                If this overloaded method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                then the <b>part_number</b> parameter of
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                should be set to NULL so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the value of <b>part_number</b>
                parameter to the builder.
                 <br> 
        
                 <br> 
                The output part_number in part_info structure:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
                for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
                To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
                @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_NO attribute.
                 <br> 
                
         @return part_info (@link PartBuilder.PartNumberData NXOpen.PDM.PartBuilder.PartNumberData@endlink):  Contains part number information.
        """
        pass
    
    ## This method generates a part revision and assigns this part revision
    ##         to the builder.
    ## 
    ##          <br> 
    ##         This method depends on the part type and part number already being
    ##         set on the builder. Therefore, a call to
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
    ##         more likely, to @link AssignPartNumber AssignPartNumber@endlink  must be made
    ##         before calling this method.
    ##          <br> 
    ## 
    ##          <br> 
    ##         If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         (as will typically be the case) then the <b>part_revision</b> parameter of
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         should be set to NULL so that the builder will use the value assigned
    ##         by this method. Otherwise, CreatePartSpec will override the value assigned
    ##         here and assign the value of the <b>part_revision</b>
    ##         parameters to the builder.
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
    ##         for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
    ##         To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
    ##         @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_REV attribute.
    ##          <br> 
    ##         
    ##  @return part_revision (str):  the assigned part revision .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartBuilder NXOpen.PDM.PartBuilder@endlink) </param>
    @overload
    def AssignPartRevision(self) -> str:
        """
        This method generates a part revision and assigns this part revision
                to the builder.
        
                 <br> 
                This method depends on the part type and part number already being
                set on the builder. Therefore, a call to
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
                more likely, to @link AssignPartNumber AssignPartNumber@endlink  must be made
                before calling this method.
                 <br> 
        
                 <br> 
                If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                (as will typically be the case) then the <b>part_revision</b> parameter of
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                should be set to NULL so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the value of the <b>part_revision</b>
                parameters to the builder.
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
                for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
                To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
                @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_REV attribute.
                 <br> 
                
         @return part_revision (str):  the assigned part revision .
        """
        pass
    
    ##  This method generates a part revision and sets this part revision to the builder.
    ## 
    ##          <br> 
    ##         This method depends on the part type and part number already being
    ##         set on the builder. Therefore, a call to
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
    ##         more likely, to @link AssignPartNumber AssignPartNumber@endlink  must be made
    ##         before calling this method.
    ##          <br> 
    ## 
    ##          <br> If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         then the <b>part_revision</b> parameter of
    ##         @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##         should be set to NULL so that the builder will use the value assigned
    ##         by this method. Otherwise, CreatePartSpec will override the value assigned
    ##         here and assign the value of the <b>part_revision</b>
    ##         parameters to the builder.
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
    ##         for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
    ##         To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
    ##         @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_REV attribute.
    ##          <br> 
    ##         
    ##  @return part_info (@link PartBuilder.PartRevisionData NXOpen.PDM.PartBuilder.PartRevisionData@endlink):  Contains part revision information .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartBuilder NXOpen.PDM.PartBuilder@endlink) </param>
    ## <param name="overload"> (int)  Dummy parameter to call this overloaded method</param>
    @overload
    def AssignPartRevision(self, overload: int) -> PartBuilder.PartRevisionData:
        """
         This method generates a part revision and sets this part revision to the builder.
        
                 <br> 
                This method depends on the part type and part number already being
                set on the builder. Therefore, a call to
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink  or,
                more likely, to @link AssignPartNumber AssignPartNumber@endlink  must be made
                before calling this method.
                 <br> 
        
                 <br> If this method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                then the <b>part_revision</b> parameter of
                @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                should be set to NULL so that the builder will use the value assigned
                by this method. Otherwise, CreatePartSpec will override the value assigned
                here and assign the value of the <b>part_revision</b>
                parameters to the builder.
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
                for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
                To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
                @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to create DB_PART_REV attribute.
                 <br> 
                
         @return part_info (@link PartBuilder.PartRevisionData NXOpen.PDM.PartBuilder.PartRevisionData@endlink):  Contains part revision information .
        """
        pass
    
    ##  Create an instance of a @link NXOpen::PDM::PartCreationObject NXOpen::PDM::PartCreationObject@endlink 
    ##         class that acts as a proxy for a part in NX Manager mode prior to that part
    ##         being created. 
    ##  @return creation_object (@link PartCreationObject NXOpen.PDM.PartCreationObject@endlink):  the new @link NXOpen::PDM::PartCreationObject NXOpen::PDM::PartCreationObject@endlink  instance .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 

    ## License requirements: None.
    def CreatePartCreationObject(self) -> PartCreationObject:
        """
         Create an instance of a @link NXOpen::PDM::PartCreationObject NXOpen::PDM::PartCreationObject@endlink 
                class that acts as a proxy for a part in NX Manager mode prior to that part
                being created. 
         @return creation_object (@link PartCreationObject NXOpen.PDM.PartCreationObject@endlink):  the new @link NXOpen::PDM::PartCreationObject NXOpen::PDM::PartCreationObject@endlink  instance .
        """
        pass
    
    ##  Create the specification for the new part that will be created.
    ##         For the input part_number:
    ##         In case of Default Domain: it is Teamcenter item ID.
    ##         In case of non-Default Domain: it is the multifield key.
    ##         e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         And the encoded part filename would be containing the MFK.
    ## 
    ##          <br> 
    ##         NOTE: The part_file_name argument is the Dataset Name and is applicable only while creating
    ##         specs for non-master parts.
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
    ##         instead.
    ##          <br> 
    ##         
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part_type"> (str)  the part type </param>
    ## <param name="part_number"> (str)  the multifield key </param>
    ## <param name="part_revision"> (str)  the part revision </param>
    ## <param name="part_file_type"> (str)  the part file type </param>
    ## <param name="part_file_name"> (str)  the dataset name </param>
    def CreatePartSpec(self, part_type: str, part_number: str, part_revision: str, part_file_type: str, part_file_name: str) -> None:
        """
         Create the specification for the new part that will be created.
                For the input part_number:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
        
                 <br> 
                NOTE: The part_file_name argument is the Dataset Name and is applicable only while creating
                specs for non-master parts.
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
                instead.
                 <br> 
                
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Create an instance of a @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink 
    ##         class that will be used to create alternate ID information while creating the new part. 
    ##  @return alternate_id_manager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink):  the new @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink  instance .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def NewAlternateIdManager(self) -> AlternateIdManager:
        """
         Create an instance of a @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink 
                class that will be used to create alternate ID information while creating the new part. 
         @return alternate_id_manager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink):  the new @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink  instance .
        """
        pass
    
    ##  Create an instance of a @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink 
    ##         class that will be used to modify database attributes while creating the new part. 
    ##  @return attribute_manager (@link DatabaseAttributeManager NXOpen.PDM.DatabaseAttributeManager@endlink):  the new @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink  instance .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def NewDatabaseAttributeManager(self) -> DatabaseAttributeManager:
        """
         Create an instance of a @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink 
                class that will be used to modify database attributes while creating the new part. 
         @return attribute_manager (@link DatabaseAttributeManager NXOpen.PDM.DatabaseAttributeManager@endlink):  the new @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink  instance .
        """
        pass
    
    ## 
    ##         Sets the part number explicitly into builder.   <br> 
    ##         This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
    ##         for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
    ##         To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
    ##         @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to set the DB_PART_NO attribute.
    ##          <br> 
    ##         
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part_number"> (str)  the part number </param>
    def SetAssignPartNumber(self, part_number: str) -> None:
        """
        
                Sets the part number explicitly into builder.   <br> 
                This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink 
                for Create and @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  for Save As instead.
                To assign part number, use @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  and
                @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  to set the DB_PART_NO attribute.
                 <br> 
                
        """
        pass
    
    ## 
    ##         Sets the part type explicitly into builder.   <br> 
    ##         This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
    ##          <br> 
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
    ##         instead.
    ##          <br> 
    ##         
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part_type"> (str) </param>
    def SetAssignPartType(self, part_type: str) -> None:
        """
        
                Sets the part type explicitly into builder.   <br> 
                This method is called before @link PDM::PartBuilder::CreatePartSpec PDM::PartBuilder::CreatePartSpec@endlink 
                 <br> 
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
                instead.
                 <br> 
                
        """
        pass
    
    ## 
    ##         Sets explicitly the place from where part selection dialog invoked into builder.
    ## 
    ##          <br> 
    ##         Deprecated in NX10 except for Save As Non Master part and
    ##         Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
    ##         instead.
    ##          <br> 
    ##          
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="operation"> (@link PartBuilder.Operation NXOpen.PDM.PartBuilder.Operation@endlink)  Token identifying place from where UG/Manager part selection dialog invoked </param>
    def SetContextOperation(self, operation: PartBuilder.Operation) -> None:
        """
        
                Sets explicitly the place from where part selection dialog invoked into builder.
        
                 <br> 
                Deprecated in NX10 except for Save As Non Master part and
                Save As to New Item Type operations. Use @link NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects NXOpen::PDM::PartOperationBuilder::CreateSpecificationsForLogicalObjects@endlink 
                instead.
                 <br> 
                 
        """
        pass
    
import NXOpen
## 
##     Represents an @link NXOpen::PDM::PartCreationObjectAttributePropertiesBuilder NXOpen::PDM::PartCreationObjectAttributePropertiesBuilder@endlink .
##      <br> To create a new instance of this class, use @link NXOpen::PDM::PartCreationObject::CreateAttributePropertiesBuilder  NXOpen::PDM::PartCreationObject::CreateAttributePropertiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BooleanValue </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## DataType </term> <description> 
##  
## String </description> </item> 
## 
## <item><term> 
##  
## IntegerValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## NumberValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ObjectPicker (deprecated) </term> <description> 
##  
## Object </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX8.0.0  <br> 
## 
##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link NXOpen::AttributePropertiesBuilder NXOpen::AttributePropertiesBuilder@endlink  instead.  <br> 

class PartCreationObjectAttributePropertiesBuilder(NXOpen.AttributePropertiesBaseBuilder): 
    """
    Represents an <ja_class>NXOpen.PDM.PartCreationObjectAttributePropertiesBuilder</ja_class>.
    """
    pass


import NXOpen
##  This class is a proxy for a to-be-created part prior to the part being created.
##         Used only in NX Manager mode.  <br> Use @link PDM::PartBuilder::CreatePartCreationObject PDM::PartBuilder::CreatePartCreationObject@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX8.0.0  <br> 

class PartCreationObject(NXOpen.NXObject): 
    """ This class is a proxy for a to-be-created part prior to the part being created.
        Used only in NX Manager mode. """


    ##  Create the PartCreationObjectAttributePropertiesBuilder 
    ##  @return builder (@link PartCreationObjectAttributePropertiesBuilder NXOpen.PDM.PartCreationObjectAttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX8.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.5.0.  Use @link AttributeManager::CreateAttributePropertiesBuilder AttributeManager::CreateAttributePropertiesBuilder@endlink  instead.  <br> 

    ## License requirements: None.
    def CreateAttributePropertiesBuilder(self) -> PartCreationObjectAttributePropertiesBuilder:
        """
         Create the PartCreationObjectAttributePropertiesBuilder 
         @return builder (@link PartCreationObjectAttributePropertiesBuilder NXOpen.PDM.PartCreationObjectAttributePropertiesBuilder@endlink): .
        """
        pass
    
##  This enum is used to specify the treatment to be used for Part Family Members.
##         JA_ICLONE_OPERATION_PartFamilyTreatment_TreatAsLostPart - Any Part Family Members taking part in the export operation
##         will be treated as lost parts by setting their state to 'Lost', and will not be exported.
##         JA_ICLONE_OPERATION_PartFamilyTreatment_TurnIntoNormalPart - Any Part Family Members taking part in the export operation
##         will be turned into normal parts by setting their state to 'Present' and individually adding them in the export operation,
##         and will be exported.
##     
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## TreatAsLostPart</term><description> 
## </description> </item><item><term> 
## TurnIntoNormalPart</term><description> 
## </description> </item></list>
class PartFamilyTreatment(Enum):
    """
    Members Include: <TreatAsLostPart> <TurnIntoNormalPart>
    """
    TreatAsLostPart: int
    TurnIntoNormalPart: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PartFamilyTreatment:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


##  This class provides the methods necessary to create a new part in NX Manager
##     from an existing part.
## 
##      <br> 
##     This class is <b>deprecated in NX10</b> for "Save As of master parts" operation.
##     This class should only be used in case of Save As Non Master parts and
##     Save As New Item Type Operations.
##     For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink .
##     This class will not support Save As if there are duplicate item ids in database.
##      <br> 
## 
##      <br> 
##     The operation that this builder supports is equivalent to the file save as operation which can:
##     <ol>
##        <li>Copy a non-master dataset into a previously existing item revision,</li>
##        <li>Save a master dataset (and possibly non-master datasets) into a new revision of the same item,</li>
##        <li>Save any master or non-master dataset as a completely new item.</li>
##     </ol>
##      <br> 
## 
##      <br> The part that is saved is always the work part. If the save is successful, then the newly
##     saved part will be the display part. <br> 
## 
##      <br> This class is a singleton meaning only one instance of it can be exist at a time. <br> 
##     
## 
##   <br>  Created in NX4.0.0  <br> 

class PartFromPartBuilder(PartBuilder): 
    """ This class provides the methods necessary to create a new part in NX Manager
    from an existing part.

    <para>
    This class is <b>deprecated in NX10</b> for "Save As of master parts" operation.
    This class should only be used in case of Save As Non Master parts and
    Save As New Item Type Operations.
    For Save As of master parts, use <ja_class>NXOpen.PDM.PartOperationCopyBuilder</ja_class>.
    This class will not support Save As if there are duplicate item ids in database.
    </para>

    <para>
    The operation that this builder supports is equivalent to the file save as operation which can:
    <ol>
       <li>Copy a non-master dataset into a previously existing item revision,</li>
       <li>Save a master dataset (and possibly non-master datasets) into a new revision of the same item,</li>
       <li>Save any master or non-master dataset as a completely new item.</li>
    </ol>
    </para>

    <para>The part that is saved is always the work part. If the save is successful, then the newly
    saved part will be the display part.</para>

    <para>This class is a singleton meaning only one instance of it can be exist at a time.</para>
    """


    ##  This enum is used to specify which non-master parts and dependent files
    ##         should be saved during the save as operation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Some</term><description> 
    ##  save selected during save as </description> </item><item><term> 
    ## All</term><description> 
    ##  save all during save as </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  save none during save as </description> </item></list>
    class FileSaveAs(Enum):
        """
        Members Include: <Some> <All> <NotSet>
        """
        Some: int
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartFromPartBuilder.FileSaveAs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) DependentFileSaveAsOption
    ##  Returns the dependent files to save during the save as operation
    ##   
    ##   
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption@endlink .
    ##          <br> 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return PartFromPartBuilder.FileSaveAs
    @property
    def DependentFileSaveAsOption(self) -> PartFromPartBuilder.FileSaveAs:
        """
        Getter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) DependentFileSaveAsOption
         Returns the dependent files to save during the save as operation
          
          
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption@endlink .
                 <br> 
                   
         
        """
        pass
    
    ## Setter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) DependentFileSaveAsOption

    ##  Returns the dependent files to save during the save as operation
    ##   
    ##   
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption@endlink .
    ##          <br> 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @DependentFileSaveAsOption.setter
    def DependentFileSaveAsOption(self, save_option: PartFromPartBuilder.FileSaveAs):
        """
        Setter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) DependentFileSaveAsOption
         Returns the dependent files to save during the save as operation
          
          
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption@endlink .
                 <br> 
                   
         
        """
        pass
    
    ## Getter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) NonmasterSaveAsOption
    ##  Returns the non-master parts to save during the save as operation
    ##   
    ##   
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption@endlink .
    ##          <br> 
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return PartFromPartBuilder.FileSaveAs
    @property
    def NonmasterSaveAsOption(self) -> PartFromPartBuilder.FileSaveAs:
        """
        Getter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) NonmasterSaveAsOption
         Returns the non-master parts to save during the save as operation
          
          
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption@endlink .
                 <br> 
                  
         
        """
        pass
    
    ## Setter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) NonmasterSaveAsOption

    ##  Returns the non-master parts to save during the save as operation
    ##   
    ##   
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption@endlink .
    ##          <br> 
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @NonmasterSaveAsOption.setter
    def NonmasterSaveAsOption(self, save_option: PartFromPartBuilder.FileSaveAs):
        """
        Setter for property: (@link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink) NonmasterSaveAsOption
         Returns the non-master parts to save during the save as operation
          
          
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption@endlink .
                 <br> 
                  
         
        """
        pass
    
    ##  Creates the new part that has been fully-specified by calling methods on this
    ##         builder.
    ## 
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As Non Master parts and Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link Builder::Commit Builder::Commit@endlink 
    ##         instead.
    ##          <br>  
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Commit(self) -> None:
        """
         Creates the new part that has been fully-specified by calling methods on this
                builder.
        
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As Non Master parts and Save As New Item Type Operations. 
                For Save As of master parts, use @link Builder::Commit Builder::Commit@endlink 
                instead.
                 <br>  
        """
        pass
    
    ##  Initializes the list of non-master parts that can be saved during the
    ##         save as operation.
    ## 
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::CreateNonMasterListForCopyLogicalObject NXOpen::PDM::PartOperationCopyBuilder::CreateNonMasterListForCopyLogicalObject@endlink .
    ##          <br> 
    ##         
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def CreateNonmasterList(self) -> None:
        """
         Initializes the list of non-master parts that can be saved during the
                save as operation.
        
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::CreateNonMasterListForCopyLogicalObject NXOpen::PDM::PartOperationCopyBuilder::CreateNonMasterListForCopyLogicalObject@endlink .
                 <br> 
                
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Sets the name the non-master part will get saved as. It will get saved as the
    ##         original non-master name if this method is not called.
    ## 
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::EditNonMasterToCopyName NXOpen::PDM::PartOperationCopyBuilder::EditNonMasterToCopyName@endlink .
    ##          <br> 
    ##         
    ##  @return is_name_valid (bool):  Whether  or not the name is a valid data set
    ##                 name. The name will get set on the builder no matter if it is valid or not. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="old_name"> (str)  the non-master part whose save as name is being set here </param>
    ## <param name="new_name"> (str)  the new name </param>
    def EditNonmasterNameToSaveAs(self, old_name: str, new_name: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called.
        
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::EditNonMasterToCopyName NXOpen::PDM::PartOperationCopyBuilder::EditNonMasterToCopyName@endlink .
                 <br> 
                
         @return is_name_valid (bool):  Whether  or not the name is a valid data set
                        name. The name will get set on the builder no matter if it is valid or not. .
        """
        pass
    
    ##  Gets the list of non-master parts.
    ## 
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::GetNonMasterListForCopyLogicalObject NXOpen::PDM::PartOperationCopyBuilder::GetNonMasterListForCopyLogicalObject@endlink .
    ##          <br> 
    ##         
    ##  @return part_filenames (List[str]):  Non-master part file names .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetNonmasterList(self) -> List[str]:
        """
         Gets the list of non-master parts.
        
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::GetNonMasterListForCopyLogicalObject NXOpen::PDM::PartOperationCopyBuilder::GetNonMasterListForCopyLogicalObject@endlink .
                 <br> 
                
         @return part_filenames (List[str]):  Non-master part file names .
        """
        pass
    
    ##  Returns whether or not the non-master part specified will actually
    ##         get saved during the save as operation.
    ## 
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::IsNonMasterForLogicalObjectBeingCopied NXOpen::PDM::PartOperationCopyBuilder::IsNonMasterForLogicalObjectBeingCopied@endlink .
    ##          <br> 
    ##         
    ##  @return do_save_as (bool):  True means that this non-master will be saved.
    ##                 False means that this non-master will not be saved. .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part_name"> (str)  the non-master part that the caller
    ##                 wants to save or not save </param>
    def GetNonmasterToSaveAs(self, part_name: str) -> bool:
        """
         Returns whether or not the non-master part specified will actually
                get saved during the save as operation.
        
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::IsNonMasterForLogicalObjectBeingCopied NXOpen::PDM::PartOperationCopyBuilder::IsNonMasterForLogicalObjectBeingCopied@endlink .
                 <br> 
                
         @return do_save_as (bool):  True means that this non-master will be saved.
                        False means that this non-master will not be saved. .
        """
        pass
    
    ##  Sets whether or not the non-master part specified will actually
    ##         get saved during the save as operation. True means that it will be
    ##         saved. False means that it will not be saved.
    ## 
    ##          <br> 
    ##         Deprecated in NX10 for "Save As of master parts" operation. 
    ##         This should only be used in case of Save As New Item Type Operations. 
    ##         For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::SetSelectedNonMasterToCopy NXOpen::PDM::PartOperationCopyBuilder::SetSelectedNonMasterToCopy@endlink .
    ##          <br> 
    ##         
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part_name"> (str)  the non-master part whose save option is being set here </param>
    ## <param name="do_save_as"> (bool)  True means that this non-master part will be saved.
    ##                 False means that this non-master part will not be saved. </param>
    def SetNonmasterToSaveAs(self, part_name: str, do_save_as: bool) -> None:
        """
         Sets whether or not the non-master part specified will actually
                get saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.
        
                 <br> 
                Deprecated in NX10 for "Save As of master parts" operation. 
                This should only be used in case of Save As New Item Type Operations. 
                For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder::SetSelectedNonMasterToCopy NXOpen::PDM::PartOperationCopyBuilder::SetSelectedNonMasterToCopy@endlink .
                 <br> 
                
        """
        pass
    
import NXOpen
##  This class provides the methods necessary to create a new part in NX Manager
##     from a template part.
## 
##      <br> 
##     Deprecated in NX10.0.0.  Use @link PDM::PartOperationCreateBuilder PDM::PartOperationCreateBuilder@endlink   instead.
##      <br> 
## 
##      <br> 
##     The operation that this builder supports is equivalent to the file new operation which
##     creates a new part from a template (or seed) part.
##      <br> 
## 
##      <br> If the operation is successful, then the newly created part will be the display part. <br> 
##     
##      <br> This class is a singleton meaning only one instance of it can be exist at a time. <br> 
##     
## 
##   <br>  Created in NX4.0.0  <br> 

class PartFromTemplateBuilder(PartBuilder): 
    """ This class provides the methods necessary to create a new part in NX Manager
    from a template part.

    <para>
    Deprecated in NX10.0.0.  Use <ja_class>PDM.PartOperationCreateBuilder</ja_class>  instead.
    </para>

    <para>
    The operation that this builder supports is equivalent to the file new operation which
    creates a new part from a template (or seed) part.
    </para>

    <para>If the operation is successful, then the newly created part will be the display part.</para>
    
    <para>This class is a singleton meaning only one instance of it can be exist at a time.</para>
    """


    ##  Creates the new part that has been fully-specified by calling methods on this
    ##         builder. The new part will be set to display part after it is created. 
    ##  @return new_part (@link NXOpen.BasePart NXOpen.BasePart@endlink):  newly created part .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link PDM::PartOperationCreateBuilder PDM::PartOperationCreateBuilder@endlink  instead.  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartFromTemplateBuilder NXOpen.PDM.PartFromTemplateBuilder@endlink) </param>
    @overload
    def Commit(self) -> NXOpen.BasePart:
        """
         Creates the new part that has been fully-specified by calling methods on this
                builder. The new part will be set to display part after it is created. 
         @return new_part (@link NXOpen.BasePart NXOpen.BasePart@endlink):  newly created part .
        """
        pass
    
    ##  Creates the new part that has been fully-specified by calling methods on this
    ##         builder. The caller specifies whether
    ##         the new part should be set as the display after it is created. 
    ##  @return new_part (@link NXOpen.BasePart NXOpen.BasePart@endlink):  newly created part .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link PDM::PartOperationCreateBuilder PDM::PartOperationCreateBuilder@endlink  instead.  <br> 

    ## License requirements: None.
    ## <param name="part_builder"> (@link PartFromTemplateBuilder NXOpen.PDM.PartFromTemplateBuilder@endlink) </param>
    ## <param name="set_as_display_part"> (bool)  True means the new part will
    ##                 set as the display part. False means that it will not. </param>
    @overload
    def Commit(self, set_as_display_part: bool) -> NXOpen.BasePart:
        """
         Creates the new part that has been fully-specified by calling methods on this
                builder. The caller specifies whether
                the new part should be set as the display after it is created. 
         @return new_part (@link NXOpen.BasePart NXOpen.BasePart@endlink):  newly created part .
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Sets the seed part on which the new part will be based. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link PDM::PartOperationCreateBuilder PDM::PartOperationCreateBuilder@endlink  instead.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="seed_name"> (str)  display name of the seed part. E.g. "Metric" </param>
    def SetSeedPart(self, seed_name: str) -> None:
        """
         Sets the seed part on which the new part will be based. 
        """
        pass
    
import NXOpen.Assemblies
##  This is can be used to create partition search filter term.
##     * Such filter terms can be used to provide filtering.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::SearchRecipeFilterBuilder::CreatePartitionTerm  NXOpen::PDM::SearchRecipeFilterBuilder::CreatePartitionTerm @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PartitionSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create partition search filter term.
    * Such filter terms can be used to provide filtering.
    """


    ##  This function adds the partitions to partition term. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="partition"> (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink) </param>
    def AddPartitions(self, partition: List[NXOpen.Assemblies.Partition]) -> None:
        """
         This function adds the partitions to partition term. 
        """
        pass
    
    ##  This function gets the flag whether to inverse partition term or not. 
    ##  @return excludeToggle (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse partition term or not. 
         @return excludeToggle (bool): .
        """
        pass
    
    ##  This function sets the flag whether to include child partitions or not. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="includeChildPartitionToggle"> (bool) </param>
    def IncludeChildPartition(self, includeChildPartitionToggle: bool) -> None:
        """
         This function sets the flag whether to include child partitions or not. 
        """
        pass
    
    ##  This function gets the flag whether to include child partitions or not. 
    ##  @return includeChildPartitionToggle (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def IsChildPartitionIncluded(self) -> bool:
        """
         This function gets the flag whether to include child partitions or not. 
         @return includeChildPartitionToggle (bool): .
        """
        pass
    
    ##  This function removes the partitions from partition term. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partition"> (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink) </param>
    def RemovePartitions(self, partition: List[NXOpen.Assemblies.Partition]) -> None:
        """
         This function removes the partitions from partition term. 
        """
        pass
    
    ##  This function sets the flag whether to inverse partition term or not. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="excludeToggle"> (bool) </param>
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse partition term or not. 
        """
        pass
    
import NXOpen
##  This class contains methods to create and manage parts in NX Manager mode.
##      <br> Use @link NXOpen::PartCollection::PDMPartManager NXOpen::PartCollection::PDMPartManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PartManager(NXOpen.Object): 
    """ This class contains methods to create and manage parts in NX Manager mode.
    """


    ##  Create or get a Clone Manager that can execute a CAE Clone process for a Simulation File or a FeModel File.  
    ##         Creates a Clone Manager for a Simulation tag or a FeModel tag, if it does not already exist.
    ##         Creates part from part builder @link NXOpen::PDM::PartFromPartBuilder NXOpen::PDM::PartFromPartBuilder@endlink  objects for cloning a Simulation File or a FeModel File.
    ##         If called for a FeModel tag, the function will create Part Builders for FeModel Part , associated Idealized Part and CAD master part.
    ##         If called for a Simulation tag, the function will create Part Builders for Simulation Part, associated FeModel Part, Idealized Part and CAD master part.
    ##         
    ##  @return manager (@link CaeCloneManager NXOpen.PDM.CaeCloneManager@endlink):  the clone manager .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling") OR nx_design_sim ("NX Design Simulation")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  the part </param>
    def GetCaeCloneManager(part: NXOpen.BasePart) -> CaeCloneManager:
        """
         Create or get a Clone Manager that can execute a CAE Clone process for a Simulation File or a FeModel File.  
                Creates a Clone Manager for a Simulation tag or a FeModel tag, if it does not already exist.
                Creates part from part builder @link NXOpen::PDM::PartFromPartBuilder NXOpen::PDM::PartFromPartBuilder@endlink  objects for cloning a Simulation File or a FeModel File.
                If called for a FeModel tag, the function will create Part Builders for FeModel Part , associated Idealized Part and CAD master part.
                If called for a Simulation tag, the function will create Part Builders for Simulation Part, associated FeModel Part, Idealized Part and CAD master part.
                
         @return manager (@link CaeCloneManager NXOpen.PDM.CaeCloneManager@endlink):  the clone manager .
        """
        pass
    
    ##  Create an instance of a part builder that creates a new part from an existing part.
    ##             This is analagous to a File SaveAs operation in NX Manager mode.
    ##         
    ##              <br> This method will throw an error if the session is not running in
    ##             NX Manager mode. <br> 
    ## 
    ##              <br> @link NXOpen::PDM::PartFromTemplateBuilder NXOpen::PDM::PartFromTemplateBuilder@endlink  is a singleton
    ##             meaning only one instance of it can exist at one time. Calling this method
    ##             will destroy the builder if one already exists and return a new instance. <br> 
    ## 
    ##              <br> 
    ##             Deprecated in NX10 for "Save As of master parts" operation. 
    ##             This should only be used in case of Save As Non Master parts and Save As New Item Type Operations.
    ##             For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.
    ##              <br> 
    ##         
    ##  @return part_builder (@link PartFromPartBuilder NXOpen.PDM.PartFromPartBuilder@endlink):  the part builder .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def NewPartFromPartBuilder() -> PartFromPartBuilder:
        """
         Create an instance of a part builder that creates a new part from an existing part.
                    This is analagous to a File SaveAs operation in NX Manager mode.
                
                     <br> This method will throw an error if the session is not running in
                    NX Manager mode. <br> 
        
                     <br> @link NXOpen::PDM::PartFromTemplateBuilder NXOpen::PDM::PartFromTemplateBuilder@endlink  is a singleton
                    meaning only one instance of it can exist at one time. Calling this method
                    will destroy the builder if one already exists and return a new instance. <br> 
        
                     <br> 
                    Deprecated in NX10 for "Save As of master parts" operation. 
                    This should only be used in case of Save As Non Master parts and Save As New Item Type Operations.
                    For Save As of master parts, use @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  instead.
                     <br> 
                
         @return part_builder (@link PartFromPartBuilder NXOpen.PDM.PartFromPartBuilder@endlink):  the part builder .
        """
        pass
    
    ##  Create an instance of a part builder that creates a new part from a template part.
    ##             This is analagous to a File New operation in NX Manager mode.
    ##         
    ##              <br> This method will throw an error if the session is not running in
    ##             NX Manager mode.  <br> 
    ## 
    ##              <br> @link NXOpen::PDM::PartFromTemplateBuilder NXOpen::PDM::PartFromTemplateBuilder@endlink  is a singleton
    ##             meaning only one instance of it can exist at one time. Calling this method
    ##             will destroy the builder if one already exists and return a new instance. <br> 
    ##         
    ##  @return part_builder (@link PartFromTemplateBuilder NXOpen.PDM.PartFromTemplateBuilder@endlink):  the part builder .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  instead.  <br> 

    ## License requirements: None.
    def NewPartFromTemplateBuilder() -> PartFromTemplateBuilder:
        """
         Create an instance of a part builder that creates a new part from a template part.
                    This is analagous to a File New operation in NX Manager mode.
                
                     <br> This method will throw an error if the session is not running in
                    NX Manager mode.  <br> 
        
                     <br> @link NXOpen::PDM::PartFromTemplateBuilder NXOpen::PDM::PartFromTemplateBuilder@endlink  is a singleton
                    meaning only one instance of it can exist at one time. Calling this method
                    will destroy the builder if one already exists and return a new instance. <br> 
                
         @return part_builder (@link PartFromTemplateBuilder NXOpen.PDM.PartFromTemplateBuilder@endlink):  the part builder .
        """
        pass
    
    ##  Creates a pending component manager for a given part. Pending components
    ##             are ones that have been added from Teamcenter, but are not yet present in NX.
    ##         
    ##  @return pending_mgr (@link PendingComponentsManager NXOpen.PDM.PendingComponentsManager@endlink): .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  the part </param>
    def NewPendingComponentsManager(part: NXOpen.BasePart) -> PendingComponentsManager:
        """
         Creates a pending component manager for a given part. Pending components
                    are ones that have been added from Teamcenter, but are not yet present in NX.
                
         @return pending_mgr (@link PendingComponentsManager NXOpen.PDM.PendingComponentsManager@endlink): .
        """
        pass
    
import NXOpen
##  Represents the PartNameGenerator  <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX1899.0.0  <br> 

class PartNameGenerator(NXOpen.Object): 
    """ Represents the PartNameGenerator """


    ##  PartAssignInputInfo struct for input to AutoAssignPartParametersForCreate 
    ## @link PartNameGeneratorPartAssignInputInfo_Struct NXOpen.PDM.PartNameGeneratorPartAssignInputInfo_Struct@endlink is an alias for @link PartNameGenerator.PartAssignInputInfo NXOpen.PDM.PartNameGenerator.PartAssignInputInfo@endlink.
    class PartAssignInputInfo:
        """
         PartAssignInputInfo struct for input to AutoAssignPartParametersForCreate 
        @link PartNameGeneratorPartAssignInputInfo_Struct NXOpen.PDM.PartNameGeneratorPartAssignInputInfo_Struct@endlink is an alias for @link PartNameGenerator.PartAssignInputInfo NXOpen.PDM.PartNameGenerator.PartAssignInputInfo@endlink.
        """
        ## Getter for property :(str) ItemType@return str
        @property
        def ItemType(self) -> str:
            """
            Getter for property ItemType
            """
            pass
        
        ## Setter for property :(str) ItemType
        @ItemType.setter
        def ItemType(self, value: str):
            """
            Getter for property ItemTypeSetter for property ItemType
            """
            pass
        
        ## Getter for property :(str) ModelType@return str
        @property
        def ModelType(self) -> str:
            """
            Getter for property ModelType
            """
            pass
        
        ## Setter for property :(str) ModelType
        @ModelType.setter
        def ModelType(self, value: str):
            """
            Getter for property ModelTypeSetter for property ModelType
            """
            pass
        
        ## Getter for property :(str) BasePartNumber@return str
        @property
        def BasePartNumber(self) -> str:
            """
            Getter for property BasePartNumber
            """
            pass
        
        ## Setter for property :(str) BasePartNumber
        @BasePartNumber.setter
        def BasePartNumber(self, value: str):
            """
            Getter for property BasePartNumberSetter for property BasePartNumber
            """
            pass
        
        ## Getter for property :(str) BasePartRevision@return str
        @property
        def BasePartRevision(self) -> str:
            """
            Getter for property BasePartRevision
            """
            pass
        
        ## Setter for property :(str) BasePartRevision
        @BasePartRevision.setter
        def BasePartRevision(self, value: str):
            """
            Getter for property BasePartRevisionSetter for property BasePartRevision
            """
            pass
        
        ## Getter for property :(str) BasePartName@return str
        @property
        def BasePartName(self) -> str:
            """
            Getter for property BasePartName
            """
            pass
        
        ## Setter for property :(str) BasePartName
        @BasePartName.setter
        def BasePartName(self, value: str):
            """
            Getter for property BasePartNameSetter for property BasePartName
            """
            pass
        
        ## Getter for property :(bool) GenerateNextItemId@return bool
        @property
        def GenerateNextItemId(self) -> bool:
            """
            Getter for property GenerateNextItemId
            """
            pass
        
        ## Setter for property :(bool) GenerateNextItemId
        @GenerateNextItemId.setter
        def GenerateNextItemId(self, value: bool):
            """
            Getter for property GenerateNextItemIdSetter for property GenerateNextItemId
            """
            pass
        
    
    
    ## 
    ##             This Method will auto assign the required parameters for creating new part in managed mode.
    ##             It will error out if part type is not fully auto assignable. i.e. If part type has key identifiers / create descriptors
    ##             which are required but cannot be auto-assigned.
    ##         
    ##  @return cliSpec (str): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="inputInfoPtr"> (@link PartNameGenerator.PartAssignInputInfo NXOpen.PDM.PartNameGenerator.PartAssignInputInfo@endlink) </param>
    def AutoAssignPartParametersForCreate(inputInfoPtr: PartNameGenerator.PartAssignInputInfo) -> str:
        """
        
                    This Method will auto assign the required parameters for creating new part in managed mode.
                    It will error out if part type is not fully auto assignable. i.e. If part type has key identifiers / create descriptors
                    which are required but cannot be auto-assigned.
                
         @return cliSpec (str): .
        """
        pass
    
import NXOpen
## 
##         Represents an @link NXOpen::PDM::PartOperationAttributePropertiesBuilder NXOpen::PDM::PartOperationAttributePropertiesBuilder@endlink  to be used for 
##         creating attributes in part operation.
##         The attribute will be distributed to all objects supplied in the selected object list.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::PdmManager::CreatePartOperationAttributePropertiesBuilder  NXOpen::PDM::PdmManager::CreatePartOperationAttributePropertiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BooleanValue </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## DataType </term> <description> 
##  
## String </description> </item> 
## 
## <item><term> 
##  
## IntegerValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## NumberValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ObjectPicker (deprecated) </term> <description> 
##  
## Object </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationAttributePropertiesBuilder(NXOpen.AttributePropertiesBuilder): 
    """
        Represents an <ja_class>NXOpen.PDM.PartOperationAttributePropertiesBuilder</ja_class> to be used for 
        creating attributes in part operation.
        The attribute will be distributed to all objects supplied in the selected object list.
    """


    ## Getter for property: (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) ReferenceObject
    ##  Returns the referenced logical object from this attribute.  
    ##    Only used for attribute
    ##             of Reference Part.    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return LogicalObject
    @property
    def ReferenceObject(self) -> LogicalObject:
        """
        Getter for property: (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) ReferenceObject
         Returns the referenced logical object from this attribute.  
           Only used for attribute
                    of Reference Part.    
         
        """
        pass
    
    ## Setter for property: (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) ReferenceObject

    ##  Returns the referenced logical object from this attribute.  
    ##    Only used for attribute
    ##             of Reference Part.    
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ReferenceObject.setter
    def ReferenceObject(self, referencedLogicalObject: LogicalObject):
        """
        Setter for property: (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) ReferenceObject
         Returns the referenced logical object from this attribute.  
           Only used for attribute
                    of Reference Part.    
         
        """
        pass
    
    ##  Create the attribute from the data set in the builder.  Unlike calling commit,
    ##             this method will not perform an update. 
    ##  @return changed (bool):  True if the attribute was created/edited successfully .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def CreateOrModifyAttribute(self) -> bool:
        """
         Create the attribute from the data set in the builder.  Unlike calling commit,
                    this method will not perform an update. 
         @return changed (bool):  True if the attribute was created/edited successfully .
        """
        pass
    
import NXOpen
##  Represents a builder class that performs various design element operations. 
##         The operation can be one of @link NXOpen::PDM::PartOperationBuilder::OperationType NXOpen::PDM::PartOperationBuilder::OperationType@endlink   <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX9.0.0  <br> 

class PartOperationBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs various design element operations. 
        The operation can be one of <ja_enum>NXOpen.PDM.PartOperationBuilder.OperationType</ja_enum> """


    ##  This enum is used to specify which dependent files
    ##         should be saved during the save as operation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ##  save all during save as </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  save none during save as </description> </item></list>
    class DependentFileSaveAs(Enum):
        """
        Members Include: <All> <NotSet>
        """
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationBuilder.DependentFileSaveAs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify which non-master parts 
    ##         should be saved during the save as operation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ##  save all during save as </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  save none during save as </description> </item></list>
    class NonMasterSaveAs(Enum):
        """
        Members Include: <All> <NotSet>
        """
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationBuilder.NonMasterSaveAs:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents an operation type that can be performed on a part 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SaveAs</term><description> 
    ##  Save As Part </description> </item><item><term> 
    ## Revise</term><description> 
    ##  Revise Part </description> </item><item><term> 
    ## Create</term><description> 
    ##  Create Part </description> </item><item><term> 
    ## Import</term><description> 
    ##  Import Part </description> </item><item><term> 
    ## Clone</term><description> 
    ##  Clone Part  </description> </item></list>
    class OperationType(Enum):
        """
        Members Include: <SaveAs> <Revise> <Create> <Import> <Clone>
        """
        SaveAs: int
        Revise: int
        Create: int
        Import: int
        Clone: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationBuilder.OperationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) DefaultDestinationFolder
    ##  Returns the default destination folder string for the part being created .  
    ##    It will be ignored in case of 
    ##         revise and creation of non-masters.
    ##         The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
    ##         In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DefaultDestinationFolder(self) -> str:
        """
        Getter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the part being created .  
           It will be ignored in case of 
                revise and creation of non-masters.
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    
    ## Setter for property: (str) DefaultDestinationFolder

    ##  Returns the default destination folder string for the part being created .  
    ##    It will be ignored in case of 
    ##         revise and creation of non-masters.
    ##         The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
    ##         In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultDestinationFolder.setter
    def DefaultDestinationFolder(self, defaultDestinationFolder: str):
        """
        Setter for property: (str) DefaultDestinationFolder
         Returns the default destination folder string for the part being created .  
           It will be ignored in case of 
                revise and creation of non-masters.
                The default destination folder string can be &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, or :&lt;folder&gt;:&lt;folder&gt; means username is optional.
                In case of :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container.
                   
         
        """
        pass
    
    ## Getter for property: (@link PartOperationBuilder.DependentFileSaveAs NXOpen.PDM.PartOperationBuilder.DependentFileSaveAs@endlink) DependentFileSaveAsOption
    ##  Returns the Dependent files Save As option.  
    ##    Save As option can be one of these
    ##         @link PartOperationBuilder::DependentFileSaveAsAll PartOperationBuilder::DependentFileSaveAsAll@endlink  and 
    ##         @link PartOperationBuilder::DependentFileSaveAsNone PartOperationBuilder::DependentFileSaveAsNone@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption NXOpen::PDM::PartOperationCopyBuilder::DependentFilesToCopyOption@endlink  instead  <br> 

    ## @return PartOperationBuilder.DependentFileSaveAs
    @property
    def DependentFileSaveAsOption(self) -> PartOperationBuilder.DependentFileSaveAs:
        """
        Getter for property: (@link PartOperationBuilder.DependentFileSaveAs NXOpen.PDM.PartOperationBuilder.DependentFileSaveAs@endlink) DependentFileSaveAsOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                @link PartOperationBuilder::DependentFileSaveAsAll PartOperationBuilder::DependentFileSaveAsAll@endlink  and 
                @link PartOperationBuilder::DependentFileSaveAsNone PartOperationBuilder::DependentFileSaveAsNone@endlink   
         
        """
        pass
    
    ## Setter for property: (@link PartOperationBuilder.DependentFileSaveAs NXOpen.PDM.PartOperationBuilder.DependentFileSaveAs@endlink) DependentFileSaveAsOption

    ##  Returns the Dependent files Save As option.  
    ##    Save As option can be one of these
    ##         @link PartOperationBuilder::DependentFileSaveAsAll PartOperationBuilder::DependentFileSaveAsAll@endlink  and 
    ##         @link PartOperationBuilder::DependentFileSaveAsNone PartOperationBuilder::DependentFileSaveAsNone@endlink   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::SetDependentFilesToCopyOption NXOpen::PDM::PartOperationCopyBuilder::SetDependentFilesToCopyOption@endlink  instead  <br> 

    @DependentFileSaveAsOption.setter
    def DependentFileSaveAsOption(self, saveOption: PartOperationBuilder.DependentFileSaveAs):
        """
        Setter for property: (@link PartOperationBuilder.DependentFileSaveAs NXOpen.PDM.PartOperationBuilder.DependentFileSaveAs@endlink) DependentFileSaveAsOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                @link PartOperationBuilder::DependentFileSaveAsAll PartOperationBuilder::DependentFileSaveAsAll@endlink  and 
                @link PartOperationBuilder::DependentFileSaveAsNone PartOperationBuilder::DependentFileSaveAsNone@endlink   
         
        """
        pass
    
    ## Getter for property: (bool) ReplaceAllComponents
    ##  Returns the replace all components.  
    ##    This option specifies whether part will be replaced or copied.             
    ##             Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::ReplaceAllComponentsInSession NXOpen::PDM::PartOperationCopyBuilder::ReplaceAllComponentsInSession@endlink  instead  <br> 

    ## @return bool
    @property
    def ReplaceAllComponents(self) -> bool:
        """
        Getter for property: (bool) ReplaceAllComponents
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
         
        """
        pass
    
    ## Setter for property: (bool) ReplaceAllComponents

    ##  Returns the replace all components.  
    ##    This option specifies whether part will be replaced or copied.             
    ##             Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::SetReplaceAllComponentsInSession NXOpen::PDM::PartOperationCopyBuilder::SetReplaceAllComponentsInSession@endlink  instead  <br> 

    @ReplaceAllComponents.setter
    def ReplaceAllComponents(self, replaceAllComponents: bool):
        """
        Setter for property: (bool) ReplaceAllComponents
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
         
        """
        pass
    
    ##  Add related part to the part undergoing an operation. Example: if user selects a part
    ##             for Save As which has Linked Part Modules that should also undergo Save As, they should
    ##             be added as related parts.
    ##             Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::AddRelatedPartsToCopy NXOpen::PDM::PartOperationCopyBuilder::AddRelatedPartsToCopy@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="basePart"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="relatedParts"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    ## <param name="relatedPartsReasons"> (List[str]) </param>
    ## <param name="operation"> (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink) </param>
    def AddRelatedPartToOperate(self, basePart: NXOpen.BasePart, relatedParts: List[NXOpen.BasePart], relatedPartsReasons: List[str], operation: PartOperationBuilder.OperationType) -> None:
        """
         Add related part to the part undergoing an operation. Example: if user selects a part
                    for Save As which has Linked Part Modules that should also undergo Save As, they should
                    be added as related parts.
                    Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
        """
        pass
    
    ##  Executes method ClearWarningCodeToLogicalObjectsSetMap() which clears m_warningCodeToLogicalObjectsSetMap 
    ##         
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def ClearWarnings(self) -> None:
        """
         Executes method ClearWarningCodeToLogicalObjectsSetMap() which clears m_warningCodeToLogicalObjectsSetMap 
                
        """
        pass
    
    ##  Creates the pre-creation objects for the parts 
    ##  @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def CreateLogicalObjects(self) -> List[LogicalObject]:
        """
         Creates the pre-creation objects for the parts 
         @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
    ##  Create NonMaster list for the selected logical Object 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::CreateNonMasterListForCopyLogicalObject NXOpen::PDM::PartOperationCopyBuilder::CreateNonMasterListForCopyLogicalObject@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def CreateNonMasterListForLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
         Create NonMaster list for the selected logical Object 
        """
        pass
    
    ##  Create new specifications for Logical Objects 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObjects"> (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink) </param>
    def CreateSpecificationsForLogicalObjects(self, logicalObjects: List[LogicalObject]) -> None:
        """
         Create new specifications for Logical Objects 
        """
        pass
    
    ##  Sets the name the non-master part will get saved as. It will get saved as the
    ##         original non-master name if this method is not called. 
    ##  @return isNameValid (bool):  flag to indicate whether the newName is valid .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::EditNonMasterToCopyName NXOpen::PDM::PartOperationCopyBuilder::EditNonMasterToCopyName@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="oldName"> (str)  the non-master part whose save as name is being set here </param>
    ## <param name="newName"> (str)  the new name </param>
    def EditNonMasterName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called. 
         @return isNameValid (bool):  flag to indicate whether the newName is valid .
        """
        pass
    
    ##  Create an instance of a @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink 
    ##         class that will be used to create alternate ID information while creating the new part.
    ##         CreateSpec call should happen before calling this method.
    ##  @return alternateIDManager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink):  the new @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink  instance .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetAlternateIDManager(self, logicalObject: LogicalObject) -> AlternateIdManager:
        """
         Create an instance of a @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink 
                class that will be used to create alternate ID information while creating the new part.
                CreateSpec call should happen before calling this method.
         @return alternateIDManager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink):  the new @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink  instance .
        """
        pass
    
    ##  Returns Commited Objects 
    ##  @return commitedParts (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def GetCreatedParts(self) -> List[NXOpen.BasePart]:
        """
         Returns Commited Objects 
         @return commitedParts (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink): .
        """
        pass
    
    ##  Returns the dialog operation Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
    ##  @return dialogOperation (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def GetDialogOperation(self) -> PartOperationBuilder.OperationType:
        """
         Returns the dialog operation Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
         @return dialogOperation (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink): .
        """
        pass
    
    ##  Returns ErrorMessageHandler 
    ##  @return errorMessageHandler (@link ErrorMessageHandler NXOpen.PDM.ErrorMessageHandler@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="refresh"> (bool) </param>
    def GetErrorMessageHandler(self, refresh: bool) -> ErrorMessageHandler:
        """
         Returns ErrorMessageHandler 
         @return errorMessageHandler (@link ErrorMessageHandler NXOpen.PDM.ErrorMessageHandler@endlink): .
        """
        pass
    
    ## Get the nonmasters saveAs option for given logical object. Save As option can be one of these
    ##         @link PartOperationBuilder::NonMasterSaveAsAll PartOperationBuilder::NonMasterSaveAsAll@endlink  and 
    ##         @link PartOperationBuilder::NonMasterSaveAsNone PartOperationBuilder::NonMasterSaveAsNone@endlink 
    ##  @return saveOption (@link PartOperationBuilder.NonMasterSaveAs NXOpen.PDM.PartOperationBuilder.NonMasterSaveAs@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption NXOpen::PDM::PartOperationCopyBuilder::GetCopyNonMasterPartsOption@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetNonMasterCopyOption(self, logicalObject: LogicalObject) -> PartOperationBuilder.NonMasterSaveAs:
        """
        Get the nonmasters saveAs option for given logical object. Save As option can be one of these
                @link PartOperationBuilder::NonMasterSaveAsAll PartOperationBuilder::NonMasterSaveAsAll@endlink  and 
                @link PartOperationBuilder::NonMasterSaveAsNone PartOperationBuilder::NonMasterSaveAsNone@endlink 
         @return saveOption (@link PartOperationBuilder.NonMasterSaveAs NXOpen.PDM.PartOperationBuilder.NonMasterSaveAs@endlink): .
        """
        pass
    
    ##  Gets NonMaster list for the given logical Object 
    ##  @return partFileNames (List[str]):  Non-master part file names .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::GetNonMasterListForCopyLogicalObject NXOpen::PDM::PartOperationCopyBuilder::GetNonMasterListForCopyLogicalObject@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetNonMasterList(self, logicalObject: LogicalObject) -> List[str]:
        """
         Gets NonMaster list for the given logical Object 
         @return partFileNames (List[str]):  Non-master part file names .
        """
        pass
    
    ##  Returns part operation failures 
    ##  @return operationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX12.0.0.  Use @link NXOpen::PDM::PartOperationBuilder::GetErrorMessageHandler NXOpen::PDM::PartOperationBuilder::GetErrorMessageHandler@endlink  instead  <br> 

    ## License requirements: None.
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns part operation failures 
         @return operationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
        """
        pass
    
    ##  Returns whether or not the non master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually get
    ##          saved during the save as operation. 
    ##  @return do_save_as (bool):  True means that this non-master will be saved. False means that this non master will not be saved. .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::IsNonMasterForLogicalObjectBeingCopied NXOpen::PDM::PartOperationCopyBuilder::IsNonMasterForLogicalObjectBeingCopied@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="part_name"> (str)  the non-master part that the caller wants to save or not save </param>
    def IsNonMasterBeingCopied(self, logicalObject: LogicalObject, part_name: str) -> bool:
        """
         Returns whether or not the non master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually get
                 saved during the save as operation. 
         @return do_save_as (bool):  True means that this non-master will be saved. False means that this non master will not be saved. .
        """
        pass
    
    ##  Sets the dialog operation. Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="dialogOperation"> (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink) </param>
    def SetDialogOperation(self, dialogOperation: PartOperationBuilder.OperationType) -> None:
        """
         Sets the dialog operation. Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
        """
        pass
    
    ## Set the nonmasters saveAs option for given logical object
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::SetCopyNonMasterPartsOption NXOpen::PDM::PartOperationCopyBuilder::SetCopyNonMasterPartsOption@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="saveOption"> (@link PartOperationBuilder.NonMasterSaveAs NXOpen.PDM.PartOperationBuilder.NonMasterSaveAs@endlink) </param>
    def SetNonMasterSaveAsOption(self, logicalObject: LogicalObject, saveOption: PartOperationBuilder.NonMasterSaveAs) -> None:
        """
        Set the nonmasters saveAs option for given logical object
        """
        pass
    
    ##  Sets whether or not the non-master part specified will actually get
    ##         saved during the save as operation. True means that it will be
    ##         saved. False means that it will not be saved.  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::SetSelectedNonMasterToCopy NXOpen::PDM::PartOperationCopyBuilder::SetSelectedNonMasterToCopy@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="partName"> (str)  the non-master part whose save option is being set here </param>
    def SetSelectedNonMasterToSaveAs(self, logicalObject: LogicalObject, partName: str) -> None:
        """
         Sets whether or not the non-master part specified will actually get
                saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.  
        """
        pass
    
    ##  Sets the selected parts. Applicable only for operation types
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
    ##             Also returns an array of parts failed to added, these are not removed from the input array though.
    ##             @link NXOpen::PDM::PartOperationBuilder::GetOperationFailures NXOpen::PDM::PartOperationBuilder::GetOperationFailures@endlink  can be called to get the errors occurred
    ##             during this operation.
    ##             
    ##  @return failedParts (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PartOperationCopyBuilder::SetSelectedPartsToCopy NXOpen::PDM::PartOperationCopyBuilder::SetSelectedPartsToCopy@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedParts"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    def SetSelectedParts(self, selectedParts: List[NXOpen.BasePart]) -> List[NXOpen.BasePart]:
        """
         Sets the selected parts. Applicable only for operation types
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
                    Also returns an array of parts failed to added, these are not removed from the input array though.
                    @link NXOpen::PDM::PartOperationBuilder::GetOperationFailures NXOpen::PDM::PartOperationBuilder::GetOperationFailures@endlink  can be called to get the errors occurred
                    during this operation.
                    
         @return failedParts (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink): .
        """
        pass
    
    ##  Validates @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  objects with this builder and udpates the operation failuers.
    ##         @link NXOpen::PDM::PartOperationBuilder::GetOperationFailures NXOpen::PDM::PartOperationBuilder::GetOperationFailures@endlink  can be called to get the errors occurred
    ##         during this operation. 
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: None.
    def ValidateLogicalObjectsToCommit(self) -> None:
        """
         Validates @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink  objects with this builder and udpates the operation failuers.
                @link NXOpen::PDM::PartOperationBuilder::GetOperationFailures NXOpen::PDM::PartOperationBuilder::GetOperationFailures@endlink  can be called to get the errors occurred
                during this operation. 
        """
        pass
    
import NXOpen
##  Represents a builder class that performs various Save As operations.  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateCopyOperationBuilder  NXOpen::PDM::PdmSession::CreateCopyOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationCopyBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs various Save As operations. """


    ##  This enum is used to specify which dependent files
    ##         should be copied to new part during the save as operation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ##  save all during save as </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  save none during save as </description> </item></list>
    class CopyDependentFiles(Enum):
        """
        Members Include: <All> <NotSet>
        """
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationCopyBuilder.CopyDependentFiles:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify which non-master parts 
    ##         should be copied to new part during the save as operation. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## All</term><description> 
    ##  save all during save as </description> </item><item><term> 
    ## NotSet</term><description> 
    ##  save none during save as </description> </item></list>
    class CopyNonMasterParts(Enum):
        """
        Members Include: <All> <NotSet>
        """
        All: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationCopyBuilder.CopyNonMasterParts:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents an operation sub type for copying a part 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Default</term><description> 
    ##  Save As dialog </description> </item><item><term> 
    ## MakeUnique</term><description> 
    ##  MakeUnique flavour of Save As dialog </description> </item></list>
    class OperationSubType(Enum):
        """
        Members Include: <Default> <MakeUnique>
        """
        Default: int
        MakeUnique: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationCopyBuilder.OperationSubType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link PartOperationCopyBuilder.CopyDependentFiles NXOpen.PDM.PartOperationCopyBuilder.CopyDependentFiles@endlink) DependentFilesToCopyOption
    ##  Returns the Dependent files Save As option.  
    ##    Save As option can be one of these
    ##         @link PartOperationCopyBuilder::CopyDependentFilesAll PartOperationCopyBuilder::CopyDependentFilesAll@endlink  and 
    ##         @link PartOperationCopyBuilder::CopyDependentFilesNone PartOperationCopyBuilder::CopyDependentFilesNone@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PartOperationCopyBuilder.CopyDependentFiles
    @property
    def DependentFilesToCopyOption(self) -> PartOperationCopyBuilder.CopyDependentFiles:
        """
        Getter for property: (@link PartOperationCopyBuilder.CopyDependentFiles NXOpen.PDM.PartOperationCopyBuilder.CopyDependentFiles@endlink) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                @link PartOperationCopyBuilder::CopyDependentFilesAll PartOperationCopyBuilder::CopyDependentFilesAll@endlink  and 
                @link PartOperationCopyBuilder::CopyDependentFilesNone PartOperationCopyBuilder::CopyDependentFilesNone@endlink   
         
        """
        pass
    
    ## Setter for property: (@link PartOperationCopyBuilder.CopyDependentFiles NXOpen.PDM.PartOperationCopyBuilder.CopyDependentFiles@endlink) DependentFilesToCopyOption

    ##  Returns the Dependent files Save As option.  
    ##    Save As option can be one of these
    ##         @link PartOperationCopyBuilder::CopyDependentFilesAll PartOperationCopyBuilder::CopyDependentFilesAll@endlink  and 
    ##         @link PartOperationCopyBuilder::CopyDependentFilesNone PartOperationCopyBuilder::CopyDependentFilesNone@endlink   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DependentFilesToCopyOption.setter
    def DependentFilesToCopyOption(self, saveOption: PartOperationCopyBuilder.CopyDependentFiles):
        """
        Setter for property: (@link PartOperationCopyBuilder.CopyDependentFiles NXOpen.PDM.PartOperationCopyBuilder.CopyDependentFiles@endlink) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
           Save As option can be one of these
                @link PartOperationCopyBuilder::CopyDependentFilesAll PartOperationCopyBuilder::CopyDependentFilesAll@endlink  and 
                @link PartOperationCopyBuilder::CopyDependentFilesNone PartOperationCopyBuilder::CopyDependentFilesNone@endlink   
         
        """
        pass
    
    ## Getter for property: (bool) ReplaceAllComponentsInSession
    ##  Returns the replace all components.  
    ##    This option specifies whether part will be replaced or copied.             
    ##             Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ReplaceAllComponentsInSession(self) -> bool:
        """
        Getter for property: (bool) ReplaceAllComponentsInSession
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
         
        """
        pass
    
    ## Setter for property: (bool) ReplaceAllComponentsInSession

    ##  Returns the replace all components.  
    ##    This option specifies whether part will be replaced or copied.             
    ##             Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ReplaceAllComponentsInSession.setter
    def ReplaceAllComponentsInSession(self, replaceAllComponents: bool):
        """
        Setter for property: (bool) ReplaceAllComponentsInSession
         Returns the replace all components.  
           This option specifies whether part will be replaced or copied.             
                    Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink   
         
        """
        pass
    
    ##  Add related part to the part undergoing an operation. Example: if user selects a part
    ##             for Save As which has Linked Part Modules that should also undergo Save As, they should
    ##             be added as related parts.
    ##             Applicable only for operation types 
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="basePart"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    ## <param name="relatedParts"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    ## <param name="relatedPartsReasons"> (List[str]) </param>
    ## <param name="operation"> (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink) </param>
    def AddRelatedPartsToCopy(self, basePart: NXOpen.BasePart, relatedParts: List[NXOpen.BasePart], relatedPartsReasons: List[str], operation: PartOperationBuilder.OperationType) -> None:
        """
         Add related part to the part undergoing an operation. Example: if user selects a part
                    for Save As which has Linked Part Modules that should also undergo Save As, they should
                    be added as related parts.
                    Applicable only for operation types 
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
        """
        pass
    
    ##  Create NonMaster list for the selected logical Object 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::CreateNonMasterListForLogicalObject NXOpen::PDM::NonMasterData::CreateNonMasterListForLogicalObject@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def CreateNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> None:
        """
         Create NonMaster list for the selected logical Object 
        """
        pass
    
    ##  Sets the name the non-master part will get saved as. It will get saved as the
    ##         original non-master name if this method is not called. 
    ##  @return isNameValid (bool):  flag to indicate whether the newName is valid .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::EditNonMasterToCopyName NXOpen::PDM::NonMasterData::EditNonMasterToCopyName@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="oldName"> (str)  the non-master part whose save as name is being set here </param>
    ## <param name="newName"> (str)  the new name </param>
    def EditNonMasterToCopyName(self, logicalObject: LogicalObject, oldName: str, newName: str) -> bool:
        """
         Sets the name the non-master part will get saved as. It will get saved as the
                original non-master name if this method is not called. 
         @return isNameValid (bool):  flag to indicate whether the newName is valid .
        """
        pass
    
    ## Get the nonmasters saveAs option for given logical object. Save As option can be one of these
    ##         @link PartOperationCopyBuilder::CopyNonMasterPartsAll PartOperationCopyBuilder::CopyNonMasterPartsAll@endlink  and 
    ##         @link PartOperationCopyBuilder::CopyNonMasterPartsNone PartOperationCopyBuilder::CopyNonMasterPartsNone@endlink 
    ##  @return saveOption (@link PartOperationCopyBuilder.CopyNonMasterParts NXOpen.PDM.PartOperationCopyBuilder.CopyNonMasterParts@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::GetCopyNonMasterPartsOption NXOpen::PDM::NonMasterData::GetCopyNonMasterPartsOption@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetCopyNonMasterPartsOption(self, logicalObject: LogicalObject) -> PartOperationCopyBuilder.CopyNonMasterParts:
        """
        Get the nonmasters saveAs option for given logical object. Save As option can be one of these
                @link PartOperationCopyBuilder::CopyNonMasterPartsAll PartOperationCopyBuilder::CopyNonMasterPartsAll@endlink  and 
                @link PartOperationCopyBuilder::CopyNonMasterPartsNone PartOperationCopyBuilder::CopyNonMasterPartsNone@endlink 
         @return saveOption (@link PartOperationCopyBuilder.CopyNonMasterParts NXOpen.PDM.PartOperationCopyBuilder.CopyNonMasterParts@endlink): .
        """
        pass
    
    ##  Gets NonMaster list for the given logical Object 
    ##  @return partFileNames (List[str]):  Non-master part file names .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::GetNonMasterListForCopyLogicalObject NXOpen::PDM::NonMasterData::GetNonMasterListForCopyLogicalObject@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetNonMasterListForCopyLogicalObject(self, logicalObject: LogicalObject) -> List[str]:
        """
         Gets NonMaster list for the given logical Object 
         @return partFileNames (List[str]):  Non-master part file names .
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::PartOperationCopyBuilder::OperationSubType NXOpen::PDM::PartOperationCopyBuilder::OperationSubType@endlink  for Create. 
    ##  @return dialogOperation (@link PartOperationCopyBuilder.OperationSubType NXOpen.PDM.PartOperationCopyBuilder.OperationSubType@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetOperationSubType(self) -> PartOperationCopyBuilder.OperationSubType:
        """
         Returns the @link NXOpen::PDM::PartOperationCopyBuilder::OperationSubType NXOpen::PDM::PartOperationCopyBuilder::OperationSubType@endlink  for Create. 
         @return dialogOperation (@link PartOperationCopyBuilder.OperationSubType NXOpen.PDM.PartOperationCopyBuilder.OperationSubType@endlink): .
        """
        pass
    
    ##  Returns the source part of this logical object. 
    ##  @return sourcePart (@link NXOpen.Part NXOpen.Part@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetSourcePartFromLogicalObject(self, logicalObject: LogicalObject) -> NXOpen.Part:
        """
         Returns the source part of this logical object. 
         @return sourcePart (@link NXOpen.Part NXOpen.Part@endlink): .
        """
        pass
    
    ##  Returns whether or not the non-master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually
    ##         get saved during the save as operation. 
    ##  @return do_save_as (bool):  True means that this non-master will be saved.
    ##                 False means that this non-master will not be saved. .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::IsNonMasterForLogicalObjectBeingCopied NXOpen::PDM::NonMasterData::IsNonMasterForLogicalObjectBeingCopied@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="part_name"> (str)  the non-master part that the caller wants to save or not save </param>
    def IsNonMasterForLogicalObjectBeingCopied(self, logicalObject: LogicalObject, part_name: str) -> bool:
        """
         Returns whether or not the non-master part specified for the given @link NXOpen::PDM::LogicalObject NXOpen::PDM::LogicalObject@endlink will actually
                get saved during the save as operation. 
         @return do_save_as (bool):  True means that this non-master will be saved.
                        False means that this non-master will not be saved. .
        """
        pass
    
    ##  Sets the Engineering Change Notice for the parts undergoing save-as 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ecnCliSpec"> (str)  CLI specification of the Engineering Change Notice </param>
    def SetChangeNotice(self, ecnCliSpec: str) -> None:
        """
         Sets the Engineering Change Notice for the parts undergoing save-as 
        """
        pass
    
    ## Set the nonmasters saveAs option for given logical object. Save As option can be one of these
    ##         @link PartOperationCopyBuilder::CopyNonMasterPartsAll PartOperationCopyBuilder::CopyNonMasterPartsAll@endlink  and 
    ##         @link PartOperationCopyBuilder::CopyNonMasterPartsNone PartOperationCopyBuilder::CopyNonMasterPartsNone@endlink 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::SetNonMasterSaveAsOption NXOpen::PDM::NonMasterData::SetNonMasterSaveAsOption@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="saveOption"> (@link PartOperationCopyBuilder.CopyNonMasterParts NXOpen.PDM.PartOperationCopyBuilder.CopyNonMasterParts@endlink) </param>
    def SetCopyNonMasterPartsOption(self, logicalObject: LogicalObject, saveOption: PartOperationCopyBuilder.CopyNonMasterParts) -> None:
        """
        Set the nonmasters saveAs option for given logical object. Save As option can be one of these
                @link PartOperationCopyBuilder::CopyNonMasterPartsAll PartOperationCopyBuilder::CopyNonMasterPartsAll@endlink  and 
                @link PartOperationCopyBuilder::CopyNonMasterPartsNone PartOperationCopyBuilder::CopyNonMasterPartsNone@endlink 
        """
        pass
    
    ##  Sets the @link NXOpen::PDM::PartOperationCopyBuilder::OperationSubType NXOpen::PDM::PartOperationCopyBuilder::OperationSubType@endlink  for Create. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="operationSubType"> (@link PartOperationCopyBuilder.OperationSubType NXOpen.PDM.PartOperationCopyBuilder.OperationSubType@endlink) </param>
    def SetOperationSubType(self, operationSubType: PartOperationCopyBuilder.OperationSubType) -> None:
        """
         Sets the @link NXOpen::PDM::PartOperationCopyBuilder::OperationSubType NXOpen::PDM::PartOperationCopyBuilder::OperationSubType@endlink  for Create. 
        """
        pass
    
    ##  Sets whether or not the non-master part specified will actually
    ##         get saved during the save as operation. True means that it will be
    ##         saved. False means that it will not be saved.  
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.0.  Use @link NXOpen::PDM::NonMasterData::SetSelectedNonMasterToCopy NXOpen::PDM::NonMasterData::SetSelectedNonMasterToCopy@endlink  instead  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="partName"> (str)  the non-master part whose save option is being set here </param>
    def SetSelectedNonMasterToCopy(self, logicalObject: LogicalObject, partName: str) -> None:
        """
         Sets whether or not the non-master part specified will actually
                get saved during the save as operation. True means that it will be
                saved. False means that it will not be saved.  
        """
        pass
    
    ##  Sets the selected parts. Applicable only for operation types
    ##             @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
    ##             @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
    ##             Also returns an array of parts failed to added, these are not removed from the input array though.
    ##             @link NXOpen::PDM::PartOperationBuilder::GetOperationFailures NXOpen::PDM::PartOperationBuilder::GetOperationFailures@endlink  can be called to get the errors occurred
    ##             during this operation.
    ##             
    ##  @return failedParts (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="selectedParts"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    def SetSelectedPartsToCopy(self, selectedParts: List[NXOpen.BasePart]) -> List[NXOpen.BasePart]:
        """
         Sets the selected parts. Applicable only for operation types
                    @link PartOperationBuilder::OperationTypeSaveAs PartOperationBuilder::OperationTypeSaveAs@endlink  and 
                    @link PartOperationBuilder::OperationTypeRevise PartOperationBuilder::OperationTypeRevise@endlink 
                    Also returns an array of parts failed to added, these are not removed from the input array though.
                    @link NXOpen::PDM::PartOperationBuilder::GetOperationFailures NXOpen::PDM::PartOperationBuilder::GetOperationFailures@endlink  can be called to get the errors occurred
                    during this operation.
                    
         @return failedParts (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink): .
        """
        pass
    
import NXOpen
##  Represents a builder class that performs Create operations  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateCreateOperationBuilder  NXOpen::PDM::PdmSession::CreateCreateOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationCreateBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs Create operations """


    ##  Represents an operation sub type for creating a part 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## FromTemplate</term><description> 
    ##  Create New Part from template </description> </item><item><term> 
    ## SelectTemplate</term><description> 
    ##  Populate Part already created in Teamcenter </description> </item><item><term> 
    ## Rename</term><description> 
    ##  Rename Existing Part </description> </item><item><term> 
    ## CreateSpecification</term><description> 
    ##  Create Specification and not a Part </description> </item><item><term> 
    ## RenameNativePartInTc</term><description> 
    ##  Rename Existing native part in session </description> </item></list>
    class OperationSubType(Enum):
        """
        Members Include: <FromTemplate> <SelectTemplate> <Rename> <CreateSpecification> <RenameNativePartInTc>
        """
        FromTemplate: int
        SelectTemplate: int
        Rename: int
        CreateSpecification: int
        RenameNativePartInTc: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationCreateBuilder.OperationSubType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) UnmanagedPartsSaveOperation
    ##  Returns the flag whether 'Assign Teamcenter IDs to Unmanaged Parts' dialog is launched in save context.  
    ##    
    ##             Currently assigning IDs to unmanaged parts via save operation is supported only in managed lite NX.
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return bool
    @property
    def UnmanagedPartsSaveOperation(self) -> bool:
        """
        Getter for property: (bool) UnmanagedPartsSaveOperation
         Returns the flag whether 'Assign Teamcenter IDs to Unmanaged Parts' dialog is launched in save context.  
           
                    Currently assigning IDs to unmanaged parts via save operation is supported only in managed lite NX.
                   
         
        """
        pass
    
    ## Setter for property: (bool) UnmanagedPartsSaveOperation

    ##  Returns the flag whether 'Assign Teamcenter IDs to Unmanaged Parts' dialog is launched in save context.  
    ##    
    ##             Currently assigning IDs to unmanaged parts via save operation is supported only in managed lite NX.
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @UnmanagedPartsSaveOperation.setter
    def UnmanagedPartsSaveOperation(self, isUnmanagedSave: bool):
        """
        Setter for property: (bool) UnmanagedPartsSaveOperation
         Returns the flag whether 'Assign Teamcenter IDs to Unmanaged Parts' dialog is launched in save context.  
           
                    Currently assigning IDs to unmanaged parts via save operation is supported only in managed lite NX.
                   
         
        """
        pass
    
    ##  Creates @link PDM::LogicalObject PDM::LogicalObject@endlink  using the seed part provided. The part with provided name must exist in Teamcenter.
    ##  @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="seedPartName"> (str) </param>
    ## <param name="numOfPartsToCreate"> (int) </param>
    def CreateLogicalObjectsUsingSeedPart(self, seedPartName: str, numOfPartsToCreate: int) -> List[LogicalObject]:
        """
         Creates @link PDM::LogicalObject PDM::LogicalObject@endlink  using the seed part provided. The part with provided name must exist in Teamcenter.
         @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
    ##  Returns logical value to indicate whether master to be added as child component 
    ##  @return addMaster (bool):  whether master to be added as child component .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetAddMaster(self) -> bool:
        """
         Returns logical value to indicate whether master to be added as child component 
         @return addMaster (bool):  whether master to be added as child component .
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  for Create. 
    ##  @return dialogOperation (@link PartOperationCreateBuilder.OperationSubType NXOpen.PDM.PartOperationCreateBuilder.OperationSubType@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetOperationSubType(self) -> PartOperationCreateBuilder.OperationSubType:
        """
         Returns the @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  for Create. 
         @return dialogOperation (@link PartOperationCreateBuilder.OperationSubType NXOpen.PDM.PartOperationCreateBuilder.OperationSubType@endlink): .
        """
        pass
    
    ##  Get Result Part Specifications.
    ##  @return resultPartsSpecs (List[str]): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetResultPartSpecs(self) -> List[str]:
        """
         Get Result Part Specifications.
         @return resultPartsSpecs (List[str]): .
        """
        pass
    
    ##  Get smart save context object.
    ##          
    ##  @return smartSaveContext (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetSmartSaveContext(self) -> SmartSaveContext:
        """
         Get smart save context object.
                 
         @return smartSaveContext (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink): .
        """
        pass
    
    ##  Sets the Add Master Flag 
    ##             Use this only in case creating a new Altrep.
    ##             This will add master as a component to newly created master.
    ##             This will be set to false if tempalte selected doesn't supports creating new altrep.
    ##            
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="addMaster"> (bool) </param>
    def SetAddMaster(self, addMaster: bool) -> None:
        """
         Sets the Add Master Flag 
                    Use this only in case creating a new Altrep.
                    This will add master as a component to newly created master.
                    This will be set to false if tempalte selected doesn't supports creating new altrep.
                   
        """
        pass
    
    ##  Sets the selected Item Type 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="itemType"> (str) </param>
    def SetItemType(self, itemType: str) -> None:
        """
         Sets the selected Item Type 
        """
        pass
    
    ##  Sets the Master Part 
    ##             Use this only in case the part your are trying to create supports master model.
    ##            
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="masterPart"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    def SetMasterPart(self, masterPart: NXOpen.BasePart) -> None:
        """
         Sets the Master Part 
                    Use this only in case the part your are trying to create supports master model.
                   
        """
        pass
    
    ##  Sets the selected Model Type 
    ##             This is same as the Relation Type that is set by @link NXOpen::FileNew::RelationType NXOpen::FileNew::RelationType@endlink  and is same as
    ##             the relation type specified in Template PAX files.
    ##             This is needed to be set only when the @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  is set 
    ##             to @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeCreateSpecification NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeCreateSpecification@endlink . In other cases
    ##             this is read from the Template. If not set this is always assumed to be "master".
    ##             Example strings are "specification", "manifestation", etc.
    ##             
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="modelType"> (str) </param>
    def SetModelType(self, modelType: str) -> None:
        """
         Sets the selected Model Type 
                    This is same as the Relation Type that is set by @link NXOpen::FileNew::RelationType NXOpen::FileNew::RelationType@endlink  and is same as
                    the relation type specified in Template PAX files.
                    This is needed to be set only when the @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  is set 
                    to @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeCreateSpecification NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeCreateSpecification@endlink . In other cases
                    this is read from the Template. If not set this is always assumed to be "master".
                    Example strings are "specification", "manifestation", etc.
                    
        """
        pass
    
    ##  Sets the @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  for Create. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="operatioSubType"> (@link PartOperationCreateBuilder.OperationSubType NXOpen.PDM.PartOperationCreateBuilder.OperationSubType@endlink) </param>
    def SetOperationSubType(self, operatioSubType: PartOperationCreateBuilder.OperationSubType) -> None:
        """
         Sets the @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  for Create. 
        """
        pass
    
    ##  Sets the Part Spec of the part to open in case of Select Template Dialog
    ##             This is only applicable if @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  is set to
    ##             @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeSelectTemplate NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeSelectTemplate@endlink 
    ##             partSpecTopOpen can be a CLI format (
    ## \@DB/MFKID/RevId) or full TCIN file specification (starting with %UGMGR)
    ##            
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partSpecToOpen"> (str) </param>
    def SetPartSpecToOpen(self, partSpecToOpen: str) -> None:
        """
         Sets the Part Spec of the part to open in case of Select Template Dialog
                    This is only applicable if @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  is set to
                    @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeSelectTemplate NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeSelectTemplate@endlink 
                    partSpecTopOpen can be a CLI format (
        \@DB/MFKID/RevId) or full TCIN file specification (starting with %UGMGR)
                   
        """
        pass
    
    ##  Sets the Parts To Rename on the Builder.
    ##             This is only applicable if @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  is set to
    ##             @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeRename NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeRename@endlink 
    ##            
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partsToRename"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink) </param>
    def SetPartsToRename(self, partsToRename: List[NXOpen.BasePart]) -> None:
        """
         Sets the Parts To Rename on the Builder.
                    This is only applicable if @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubType NXOpen::PDM::PartOperationCreateBuilder::OperationSubType@endlink  is set to
                    @link NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeRename NXOpen::PDM::PartOperationCreateBuilder::OperationSubTypeRename@endlink 
                   
        """
        pass
    
    ##  Set smart save context object.
    ##          
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="smartSaveContext"> (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink) </param>
    def SetSmartSaveContext(self, smartSaveContext: SmartSaveContext) -> None:
        """
         Set smart save context object.
                 
        """
        pass
    
import NXOpen
##  Represents a builder class that performs Create operations  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateImportOperationBuilder  NXOpen::PDM::PdmSession::CreateImportOperationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## CheckedoutCommentNotMatchError </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## CheckoutOption </term> <description> 
##  
## NoChange </description> </item> 
## 
## <item><term> 
##  
## ConversionType </term> <description> 
##  
## AsID </description> </item> 
## 
## <item><term> 
##  
## DefaultAction </term> <description> 
##  
## Overwrite </description> </item> 
## 
## <item><term> 
##  
## IncludeComponentParts </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## IncludeDependentParts </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## NotCheckedoutError </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## NumberingSource </term> <description> 
##  
## PartIDGenerator </description> </item> 
## 
## <item><term> 
##  
## PublishJTData </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## UseItemTypeFromPartFile </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ValidationAbortImportOnFail </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ValidationMode </term> <description> 
##  
## Off </description> </item> 
## 
## <item><term> 
##  
## ValidationRuleSetBrowseOption </term> <description> 
##  
## Native </description> </item> 
## 
## <item><term> 
##  
## ValidationTreatOutdatedAsPass </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ValidationTreatWarningAsPass </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationImportBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs Create operations """


    ##  This enum is used to specify the checkout condition of the dataset for the part to be imported. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Checkin</term><description> 
    ## </description> </item><item><term> 
    ## Checkout</term><description> 
    ## </description> </item><item><term> 
    ## NoChange</term><description> 
    ## </description> </item></list>
    class CheckoutOptionType(Enum):
        """
        Members Include: <Checkin> <Checkout> <NoChange>
        """
        Checkin: int
        Checkout: int
        NoChange: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.CheckoutOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the conversion rule for @link NXOpen::PDM::PartOperationImportBuilder::NumberingSourceOptionOSFilename NXOpen::PDM::PartOperationImportBuilder::NumberingSourceOptionOSFilename@endlink . 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AsID</term><description> 
    ## </description> </item><item><term> 
    ## AsIDandRevision</term><description> 
    ## </description> </item><item><term> 
    ## WithPrefix</term><description> 
    ## </description> </item><item><term> 
    ## WithSuffix</term><description> 
    ## </description> </item><item><term> 
    ## WithReplaceString</term><description> 
    ## </description> </item><item><term> 
    ## MixedRule</term><description> 
    ## </description> </item></list>
    class ConversionRule(Enum):
        """
        Members Include: <AsID> <AsIDandRevision> <WithPrefix> <WithSuffix> <WithReplaceString> <MixedRule>
        """
        AsID: int
        AsIDandRevision: int
        WithPrefix: int
        WithSuffix: int
        WithReplaceString: int
        MixedRule: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.ConversionRule:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the default action for import. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Overwrite</term><description> 
    ## </description> </item><item><term> 
    ## UseExisting</term><description> 
    ## </description> </item><item><term> 
    ## NewRevision</term><description> 
    ## </description> </item><item><term> 
    ## Default</term><description> 
    ## </description> </item></list>
    class ExistingPartAction(Enum):
        """
        Members Include: <Overwrite> <UseExisting> <NewRevision> <Default>
        """
        Overwrite: int
        UseExisting: int
        NewRevision: int
        Default: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.ExistingPartAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the default behavior for auto assign. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## PartIDGenerator</term><description> 
    ## </description> </item><item><term> 
    ## OSFilename</term><description> 
    ## </description> </item><item><term> 
    ## Attribute</term><description> 
    ## </description> </item></list>
    class NumberingSourceOption(Enum):
        """
        Members Include: <PartIDGenerator> <OSFilename> <Attribute>
        """
        PartIDGenerator: int
        OSFilename: int
        Attribute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.NumberingSourceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the treatment to be used for Part Family Members.
    ##         Famliy Treatment can be one of @link NXOpen::PDM::PartOperationImportBuilder::PartFamilyTreatment NXOpen::PDM::PartOperationImportBuilder::PartFamilyTreatment@endlink 
    ##         @link NXOpen::PDM::PartOperationImportBuilder::PartFamilyTreatment::TreatAsLostPart NXOpen::PDM::PartOperationImportBuilder::PartFamilyTreatment::TreatAsLostPart@endlink  - Any Part Family Members taking part in the import operation
    ##         will be treated as lost parts by setting their state to 'Lost', and will not be imported.
    ##         @link NXOpen::PDM::PartOperationImportBuilder::PartFamilyTreatment::TurnIntoNormalPart NXOpen::PDM::PartOperationImportBuilder::PartFamilyTreatment::TurnIntoNormalPart@endlink  - Any Part Family Members taking part
    ##         in the import operation will be turned into normal parts by setting their state to 'Present' and will be imported.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## TreatAsLostPart</term><description> 
    ## </description> </item><item><term> 
    ## TurnIntoNormalPart</term><description> 
    ## </description> </item></list>
    class PartFamilyTreatment(Enum):
        """
        Members Include: <TreatAsLostPart> <TurnIntoNormalPart>
        """
        TreatAsLostPart: int
        TurnIntoNormalPart: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.PartFamilyTreatment:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the validation mode. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Off</term><description> 
    ## </description> </item><item><term> 
    ## ImportFromPart</term><description> 
    ## </description> </item><item><term> 
    ## RunValidation</term><description> 
    ## </description> </item><item><term> 
    ## RunValidationHybrid</term><description> 
    ## </description> </item><item><term> 
    ## Default</term><description> 
    ## </description> </item></list>
    class Validation(Enum):
        """
        Members Include: <Off> <ImportFromPart> <RunValidation> <RunValidationHybrid> <Default>
        """
        Off: int
        ImportFromPart: int
        RunValidation: int
        RunValidationHybrid: int
        Default: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.Validation:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the option to browse the validation rule set file from. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Native</term><description> 
    ## </description> </item><item><term> 
    ## Teamcenter</term><description> 
    ## </description> </item></list>
    class ValidationRuleSetFileBrowseOption(Enum):
        """
        Members Include: <Native> <Teamcenter>
        """
        Native: int
        Teamcenter: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AddCAENonMastersToImport
    ##  Returns the add non master to import   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def AddCAENonMastersToImport(self) -> bool:
        """
        Getter for property: (bool) AddCAENonMastersToImport
         Returns the add non master to import   
            
         
        """
        pass
    
    ## Setter for property: (bool) AddCAENonMastersToImport

    ##  Returns the add non master to import   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @AddCAENonMastersToImport.setter
    def AddCAENonMastersToImport(self, addCAENonMasters: bool):
        """
        Setter for property: (bool) AddCAENonMastersToImport
         Returns the add non master to import   
            
         
        """
        pass
    
    ## Getter for property: (bool) AddDfaMixins
    ##  Returns the add dfa mixins   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def AddDfaMixins(self) -> bool:
        """
        Getter for property: (bool) AddDfaMixins
         Returns the add dfa mixins   
            
         
        """
        pass
    
    ## Setter for property: (bool) AddDfaMixins

    ##  Returns the add dfa mixins   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AddDfaMixins.setter
    def AddDfaMixins(self, addDfaMixins: bool):
        """
        Setter for property: (bool) AddDfaMixins
         Returns the add dfa mixins   
            
         
        """
        pass
    
    ## Getter for property: (bool) AssignAlternateIds
    ##  Returns the method returns the value indicating whether alternate IDs should be created during import   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return bool
    @property
    def AssignAlternateIds(self) -> bool:
        """
        Getter for property: (bool) AssignAlternateIds
         Returns the method returns the value indicating whether alternate IDs should be created during import   
            
         
        """
        pass
    
    ## Setter for property: (bool) AssignAlternateIds

    ##  Returns the method returns the value indicating whether alternate IDs should be created during import   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @AssignAlternateIds.setter
    def AssignAlternateIds(self, createAlternateIDs: bool):
        """
        Setter for property: (bool) AssignAlternateIds
         Returns the method returns the value indicating whether alternate IDs should be created during import   
            
         
        """
        pass
    
    ## Getter for property: (str) AssociatedFilesRootDirectory
    ##  Returns the associated files root directory   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def AssociatedFilesRootDirectory(self) -> str:
        """
        Getter for property: (str) AssociatedFilesRootDirectory
         Returns the associated files root directory   
            
         
        """
        pass
    
    ## Setter for property: (str) AssociatedFilesRootDirectory

    ##  Returns the associated files root directory   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @AssociatedFilesRootDirectory.setter
    def AssociatedFilesRootDirectory(self, foldername: str):
        """
        Setter for property: (str) AssociatedFilesRootDirectory
         Returns the associated files root directory   
            
         
        """
        pass
    
    ## Getter for property: (bool) CheckedoutCommentNotMatchError
    ##  Returns the method gets the status of the 'Notify if Checkout Comment not Match' Flag so as to pop an error that the previous checkout
    ##         comment of file which user is trying to override does not match with the checkout comment entered through the dialog.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def CheckedoutCommentNotMatchError(self) -> bool:
        """
        Getter for property: (bool) CheckedoutCommentNotMatchError
         Returns the method gets the status of the 'Notify if Checkout Comment not Match' Flag so as to pop an error that the previous checkout
                comment of file which user is trying to override does not match with the checkout comment entered through the dialog.  
          
                  
         
        """
        pass
    
    ## Setter for property: (bool) CheckedoutCommentNotMatchError

    ##  Returns the method gets the status of the 'Notify if Checkout Comment not Match' Flag so as to pop an error that the previous checkout
    ##         comment of file which user is trying to override does not match with the checkout comment entered through the dialog.  
    ##   
    ##           
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CheckedoutCommentNotMatchError.setter
    def CheckedoutCommentNotMatchError(self, checkedoutCommentNotMatchError: bool):
        """
        Setter for property: (bool) CheckedoutCommentNotMatchError
         Returns the method gets the status of the 'Notify if Checkout Comment not Match' Flag so as to pop an error that the previous checkout
                comment of file which user is trying to override does not match with the checkout comment entered through the dialog.  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) CheckoutComment
    ##  Returns the method is used to get the comment added by the user while checking in or checking out   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def CheckoutComment(self) -> str:
        """
        Getter for property: (str) CheckoutComment
         Returns the method is used to get the comment added by the user while checking in or checking out   
            
         
        """
        pass
    
    ## Setter for property: (str) CheckoutComment

    ##  Returns the method is used to get the comment added by the user while checking in or checking out   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CheckoutComment.setter
    def CheckoutComment(self, checkoutComment: str):
        """
        Setter for property: (str) CheckoutComment
         Returns the method is used to get the comment added by the user while checking in or checking out   
            
         
        """
        pass
    
    ## Getter for property: (@link PartOperationImportBuilder.CheckoutOptionType NXOpen.PDM.PartOperationImportBuilder.CheckoutOptionType@endlink) CheckoutOption
    ##  Returns the method is used to identify id user want to checkout or checkin the file while import   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PartOperationImportBuilder.CheckoutOptionType
    @property
    def CheckoutOption(self) -> PartOperationImportBuilder.CheckoutOptionType:
        """
        Getter for property: (@link PartOperationImportBuilder.CheckoutOptionType NXOpen.PDM.PartOperationImportBuilder.CheckoutOptionType@endlink) CheckoutOption
         Returns the method is used to identify id user want to checkout or checkin the file while import   
            
         
        """
        pass
    
    ## Setter for property: (@link PartOperationImportBuilder.CheckoutOptionType NXOpen.PDM.PartOperationImportBuilder.CheckoutOptionType@endlink) CheckoutOption

    ##  Returns the method is used to identify id user want to checkout or checkin the file while import   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @CheckoutOption.setter
    def CheckoutOption(self, checkoutOption: PartOperationImportBuilder.CheckoutOptionType):
        """
        Setter for property: (@link PartOperationImportBuilder.CheckoutOptionType NXOpen.PDM.PartOperationImportBuilder.CheckoutOptionType@endlink) CheckoutOption
         Returns the method is used to identify id user want to checkout or checkin the file while import   
            
         
        """
        pass
    
    ## Getter for property: (@link PartOperationImportBuilder.ConversionRule NXOpen.PDM.PartOperationImportBuilder.ConversionRule@endlink) ConversionType
    ##  Returns the conversion type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PartOperationImportBuilder.ConversionRule
    @property
    def ConversionType(self) -> PartOperationImportBuilder.ConversionRule:
        """
        Getter for property: (@link PartOperationImportBuilder.ConversionRule NXOpen.PDM.PartOperationImportBuilder.ConversionRule@endlink) ConversionType
         Returns the conversion type   
            
         
        """
        pass
    
    ## Setter for property: (@link PartOperationImportBuilder.ConversionRule NXOpen.PDM.PartOperationImportBuilder.ConversionRule@endlink) ConversionType

    ##  Returns the conversion type   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ConversionType.setter
    def ConversionType(self, conversionType: PartOperationImportBuilder.ConversionRule):
        """
        Setter for property: (@link PartOperationImportBuilder.ConversionRule NXOpen.PDM.PartOperationImportBuilder.ConversionRule@endlink) ConversionType
         Returns the conversion type   
            
         
        """
        pass
    
    ## Getter for property: (@link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink) DefaultAction
    ##  Returns the default action   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PartOperationImportBuilder.ExistingPartAction
    @property
    def DefaultAction(self) -> PartOperationImportBuilder.ExistingPartAction:
        """
        Getter for property: (@link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink) DefaultAction
         Returns the default action   
            
         
        """
        pass
    
    ## Setter for property: (@link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink) DefaultAction

    ##  Returns the default action   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultAction.setter
    def DefaultAction(self, defaultAction: PartOperationImportBuilder.ExistingPartAction):
        """
        Setter for property: (@link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink) DefaultAction
         Returns the default action   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultAlternateIdContext
    ##  Returns the method returns the IdContext to be used while assigning alternate IDs during import   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def DefaultAlternateIdContext(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdContext
         Returns the method returns the IdContext to be used while assigning alternate IDs during import   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultAlternateIdContext

    ##  Returns the method returns the IdContext to be used while assigning alternate IDs during import   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DefaultAlternateIdContext.setter
    def DefaultAlternateIdContext(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdContext
         Returns the method returns the IdContext to be used while assigning alternate IDs during import   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultAlternateIdType
    ##  Returns the method returns the IdType to be used while assigning alternate IDs during import  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def DefaultAlternateIdType(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdType
         Returns the method returns the IdType to be used while assigning alternate IDs during import  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultAlternateIdType

    ##  Returns the method returns the IdType to be used while assigning alternate IDs during import  
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @DefaultAlternateIdType.setter
    def DefaultAlternateIdType(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdType
         Returns the method returns the IdType to be used while assigning alternate IDs during import  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultChangeNotice
    ##  Returns the default change notice for import operation in CLI format.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return str
    @property
    def DefaultChangeNotice(self) -> str:
        """
        Getter for property: (str) DefaultChangeNotice
         Returns the default change notice for import operation in CLI format.  
             
         
        """
        pass
    
    ## Setter for property: (str) DefaultChangeNotice

    ##  Returns the default change notice for import operation in CLI format.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @DefaultChangeNotice.setter
    def DefaultChangeNotice(self, defaultChangeNotice: str):
        """
        Setter for property: (str) DefaultChangeNotice
         Returns the default change notice for import operation in CLI format.  
             
         
        """
        pass
    
    ## Getter for property: (str) DefaultDescription
    ##  Returns the default description   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DefaultDescription(self) -> str:
        """
        Getter for property: (str) DefaultDescription
         Returns the default description   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultDescription

    ##  Returns the default description   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultDescription.setter
    def DefaultDescription(self, defaultDescription: str):
        """
        Setter for property: (str) DefaultDescription
         Returns the default description   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultItemType
    ##  Returns the default item type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DefaultItemType(self) -> str:
        """
        Getter for property: (str) DefaultItemType
         Returns the default item type   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultItemType

    ##  Returns the default item type   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultItemType.setter
    def DefaultItemType(self, defaultItemType: str):
        """
        Setter for property: (str) DefaultItemType
         Returns the default item type   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultName
    ##  Returns the default name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DefaultName(self) -> str:
        """
        Getter for property: (str) DefaultName
         Returns the default name   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultName

    ##  Returns the default name   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultName.setter
    def DefaultName(self, defaultName: str):
        """
        Setter for property: (str) DefaultName
         Returns the default name   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultOwningGroup
    ##  Returns the default owning group   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DefaultOwningGroup(self) -> str:
        """
        Getter for property: (str) DefaultOwningGroup
         Returns the default owning group   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultOwningGroup

    ##  Returns the default owning group   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultOwningGroup.setter
    def DefaultOwningGroup(self, defaultOwningGroup: str):
        """
        Setter for property: (str) DefaultOwningGroup
         Returns the default owning group   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultOwningUser
    ##  Returns the default owning user   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def DefaultOwningUser(self) -> str:
        """
        Getter for property: (str) DefaultOwningUser
         Returns the default owning user   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultOwningUser

    ##  Returns the default owning user   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @DefaultOwningUser.setter
    def DefaultOwningUser(self, defaultOwningUser: str):
        """
        Setter for property: (str) DefaultOwningUser
         Returns the default owning user   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeComponentParts
    ##  Returns the include component parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def IncludeComponentParts(self) -> bool:
        """
        Getter for property: (bool) IncludeComponentParts
         Returns the include component parts   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeComponentParts

    ##  Returns the include component parts   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @IncludeComponentParts.setter
    def IncludeComponentParts(self, includeComponentParts: bool):
        """
        Setter for property: (bool) IncludeComponentParts
         Returns the include component parts   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeDependentParts
    ##  Returns the include dependent parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def IncludeDependentParts(self) -> bool:
        """
        Getter for property: (bool) IncludeDependentParts
         Returns the include dependent parts   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeDependentParts

    ##  Returns the include dependent parts   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @IncludeDependentParts.setter
    def IncludeDependentParts(self, includeDependentParts: bool):
        """
        Setter for property: (bool) IncludeDependentParts
         Returns the include dependent parts   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeSubfoldersToggle
    ##  Returns the method returns the value indicating whether original folder structure should be created during import or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def IncludeSubfoldersToggle(self) -> bool:
        """
        Getter for property: (bool) IncludeSubfoldersToggle
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeSubfoldersToggle

    ##  Returns the method returns the value indicating whether original folder structure should be created during import or not   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @IncludeSubfoldersToggle.setter
    def IncludeSubfoldersToggle(self, includeSubfolders: bool):
        """
        Setter for property: (bool) IncludeSubfoldersToggle
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) MaintainOriginalFolderStructure
    ##  Returns the method returns the value indicating whether original folder structure should be created during import or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## @return bool
    @property
    def MaintainOriginalFolderStructure(self) -> bool:
        """
        Getter for property: (bool) MaintainOriginalFolderStructure
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) MaintainOriginalFolderStructure

    ##  Returns the method returns the value indicating whether original folder structure should be created during import or not   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    @MaintainOriginalFolderStructure.setter
    def MaintainOriginalFolderStructure(self, maintainOriginalFolderStructure: bool):
        """
        Setter for property: (bool) MaintainOriginalFolderStructure
         Returns the method returns the value indicating whether original folder structure should be created during import or not   
            
         
        """
        pass
    
    ## Getter for property: (bool) NotCheckedoutError
    ##  Returns the method gets the status of the 'Notify if Not Checkout' Flag so as to pop an error that the file which
    ##         user is trying to override is not check-out.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def NotCheckedoutError(self) -> bool:
        """
        Getter for property: (bool) NotCheckedoutError
         Returns the method gets the status of the 'Notify if Not Checkout' Flag so as to pop an error that the file which
                user is trying to override is not check-out.  
          
                  
         
        """
        pass
    
    ## Setter for property: (bool) NotCheckedoutError

    ##  Returns the method gets the status of the 'Notify if Not Checkout' Flag so as to pop an error that the file which
    ##         user is trying to override is not check-out.  
    ##   
    ##           
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NotCheckedoutError.setter
    def NotCheckedoutError(self, notCheckedoutError: bool):
        """
        Setter for property: (bool) NotCheckedoutError
         Returns the method gets the status of the 'Notify if Not Checkout' Flag so as to pop an error that the file which
                user is trying to override is not check-out.  
          
                  
         
        """
        pass
    
    ## Getter for property: (str) NumberAttr
    ##  Returns the number attr   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def NumberAttr(self) -> str:
        """
        Getter for property: (str) NumberAttr
         Returns the number attr   
            
         
        """
        pass
    
    ## Setter for property: (str) NumberAttr

    ##  Returns the number attr   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberAttr.setter
    def NumberAttr(self, numberAttr: str):
        """
        Setter for property: (str) NumberAttr
         Returns the number attr   
            
         
        """
        pass
    
    ## Getter for property: (@link PartOperationImportBuilder.NumberingSourceOption NXOpen.PDM.PartOperationImportBuilder.NumberingSourceOption@endlink) NumberingSource
    ##  Returns the numbering source   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PartOperationImportBuilder.NumberingSourceOption
    @property
    def NumberingSource(self) -> PartOperationImportBuilder.NumberingSourceOption:
        """
        Getter for property: (@link PartOperationImportBuilder.NumberingSourceOption NXOpen.PDM.PartOperationImportBuilder.NumberingSourceOption@endlink) NumberingSource
         Returns the numbering source   
            
         
        """
        pass
    
    ## Setter for property: (@link PartOperationImportBuilder.NumberingSourceOption NXOpen.PDM.PartOperationImportBuilder.NumberingSourceOption@endlink) NumberingSource

    ##  Returns the numbering source   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @NumberingSource.setter
    def NumberingSource(self, numberingSource: PartOperationImportBuilder.NumberingSourceOption):
        """
        Setter for property: (@link PartOperationImportBuilder.NumberingSourceOption NXOpen.PDM.PartOperationImportBuilder.NumberingSourceOption@endlink) NumberingSource
         Returns the numbering source   
            
         
        """
        pass
    
    ## Getter for property: (str) OutputLogFile
    ##  Returns the output log file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def OutputLogFile(self) -> str:
        """
        Getter for property: (str) OutputLogFile
         Returns the output log file   
            
         
        """
        pass
    
    ## Setter for property: (str) OutputLogFile

    ##  Returns the output log file   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @OutputLogFile.setter
    def OutputLogFile(self, filename: str):
        """
        Setter for property: (str) OutputLogFile
         Returns the output log file   
            
         
        """
        pass
    
    ## Getter for property: (str) PrefixStr
    ##  Returns the prefix str   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def PrefixStr(self) -> str:
        """
        Getter for property: (str) PrefixStr
         Returns the prefix str   
            
         
        """
        pass
    
    ## Setter for property: (str) PrefixStr

    ##  Returns the prefix str   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @PrefixStr.setter
    def PrefixStr(self, prefixStr: str):
        """
        Setter for property: (str) PrefixStr
         Returns the prefix str   
            
         
        """
        pass
    
    ## Getter for property: (bool) ProductInterfaces
    ##  Returns the product interfaces   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.2.  It is no longer supported.  <br> 

    ## @return bool
    @property
    def ProductInterfaces(self) -> bool:
        """
        Getter for property: (bool) ProductInterfaces
         Returns the product interfaces   
            
         
        """
        pass
    
    ## Setter for property: (bool) ProductInterfaces

    ##  Returns the product interfaces   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.2.  It is no longer supported.  <br> 

    @ProductInterfaces.setter
    def ProductInterfaces(self, productInterfaces: bool):
        """
        Setter for property: (bool) ProductInterfaces
         Returns the product interfaces   
            
         
        """
        pass
    
    ## Getter for property: (bool) PublishJTData
    ##  Returns the flag for JT data publishing   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def PublishJTData(self) -> bool:
        """
        Getter for property: (bool) PublishJTData
         Returns the flag for JT data publishing   
            
         
        """
        pass
    
    ## Setter for property: (bool) PublishJTData

    ##  Returns the flag for JT data publishing   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PublishJTData.setter
    def PublishJTData(self, publishJTData: bool):
        """
        Setter for property: (bool) PublishJTData
         Returns the flag for JT data publishing   
            
         
        """
        pass
    
    ## Getter for property: (bool) PublishOptionalInfo
    ##  Returns the optional information publishing   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def PublishOptionalInfo(self) -> bool:
        """
        Getter for property: (bool) PublishOptionalInfo
         Returns the optional information publishing   
            
         
        """
        pass
    
    ## Setter for property: (bool) PublishOptionalInfo

    ##  Returns the optional information publishing   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @PublishOptionalInfo.setter
    def PublishOptionalInfo(self, publishOptionalInfo: bool):
        """
        Setter for property: (bool) PublishOptionalInfo
         Returns the optional information publishing   
            
         
        """
        pass
    
    ## Getter for property: (str) ReplaceWithStr
    ##  Returns the replace with str   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ReplaceWithStr(self) -> str:
        """
        Getter for property: (str) ReplaceWithStr
         Returns the replace with str   
            
         
        """
        pass
    
    ## Setter for property: (str) ReplaceWithStr

    ##  Returns the replace with str   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ReplaceWithStr.setter
    def ReplaceWithStr(self, replaceWithStr: str):
        """
        Setter for property: (str) ReplaceWithStr
         Returns the replace with str   
            
         
        """
        pass
    
    ## Getter for property: (str) RevisionAttr
    ##  Returns the revision attr   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def RevisionAttr(self) -> str:
        """
        Getter for property: (str) RevisionAttr
         Returns the revision attr   
            
         
        """
        pass
    
    ## Setter for property: (str) RevisionAttr

    ##  Returns the revision attr   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @RevisionAttr.setter
    def RevisionAttr(self, revisionAttr: str):
        """
        Setter for property: (str) RevisionAttr
         Returns the revision attr   
            
         
        """
        pass
    
    ## Getter for property: (str) StringToReplace
    ##  Returns the string to replace   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def StringToReplace(self) -> str:
        """
        Getter for property: (str) StringToReplace
         Returns the string to replace   
            
         
        """
        pass
    
    ## Setter for property: (str) StringToReplace

    ##  Returns the string to replace   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @StringToReplace.setter
    def StringToReplace(self, stringToReplace: str):
        """
        Setter for property: (str) StringToReplace
         Returns the string to replace   
            
         
        """
        pass
    
    ## Getter for property: (str) SuffixStr
    ##  Returns the suffix str   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def SuffixStr(self) -> str:
        """
        Getter for property: (str) SuffixStr
         Returns the suffix str   
            
         
        """
        pass
    
    ## Setter for property: (str) SuffixStr

    ##  Returns the suffix str   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @SuffixStr.setter
    def SuffixStr(self, suffixStr: str):
        """
        Setter for property: (str) SuffixStr
         Returns the suffix str   
            
         
        """
        pass
    
    ## Getter for property: (bool) SyncArrangements
    ##  Returns the sync arrangements   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.2.  It is no longer supported.  <br> 

    ## @return bool
    @property
    def SyncArrangements(self) -> bool:
        """
        Getter for property: (bool) SyncArrangements
         Returns the sync arrangements   
            
         
        """
        pass
    
    ## Setter for property: (bool) SyncArrangements

    ##  Returns the sync arrangements   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.2.  It is no longer supported.  <br> 

    @SyncArrangements.setter
    def SyncArrangements(self, syncArrangements: bool):
        """
        Setter for property: (bool) SyncArrangements
         Returns the sync arrangements   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseItemTypeFromPartFile
    ##  Returns the flag to specify if Import can use the Item Type already present in the part during import   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def UseItemTypeFromPartFile(self) -> bool:
        """
        Getter for property: (bool) UseItemTypeFromPartFile
         Returns the flag to specify if Import can use the Item Type already present in the part during import   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseItemTypeFromPartFile

    ##  Returns the flag to specify if Import can use the Item Type already present in the part during import   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @UseItemTypeFromPartFile.setter
    def UseItemTypeFromPartFile(self, useItemTypeFromPartFile: bool):
        """
        Setter for property: (bool) UseItemTypeFromPartFile
         Returns the flag to specify if Import can use the Item Type already present in the part during import   
            
         
        """
        pass
    
    ## Getter for property: (bool) ValidationAbortImportOnFail
    ##  Returns the validation abort import on fail   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ValidationAbortImportOnFail(self) -> bool:
        """
        Getter for property: (bool) ValidationAbortImportOnFail
         Returns the validation abort import on fail   
            
         
        """
        pass
    
    ## Setter for property: (bool) ValidationAbortImportOnFail

    ##  Returns the validation abort import on fail   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ValidationAbortImportOnFail.setter
    def ValidationAbortImportOnFail(self, validationAbortImportOnFail: bool):
        """
        Setter for property: (bool) ValidationAbortImportOnFail
         Returns the validation abort import on fail   
            
         
        """
        pass
    
    ## Getter for property: (@link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink) ValidationMode
    ##  Returns the validation mode   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PartOperationImportBuilder.Validation
    @property
    def ValidationMode(self) -> PartOperationImportBuilder.Validation:
        """
        Getter for property: (@link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink) ValidationMode
         Returns the validation mode   
            
         
        """
        pass
    
    ## Setter for property: (@link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink) ValidationMode

    ##  Returns the validation mode   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ValidationMode.setter
    def ValidationMode(self, validationMode: PartOperationImportBuilder.Validation):
        """
        Setter for property: (@link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink) ValidationMode
         Returns the validation mode   
            
         
        """
        pass
    
    ## Getter for property: (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink) ValidationRuleSetBrowseOption
    ##  Returns the validation rule set browse option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PartOperationImportBuilder.ValidationRuleSetFileBrowseOption
    @property
    def ValidationRuleSetBrowseOption(self) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
        """
        Getter for property: (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink) ValidationRuleSetBrowseOption
         Returns the validation rule set browse option   
            
         
        """
        pass
    
    ## Setter for property: (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink) ValidationRuleSetBrowseOption

    ##  Returns the validation rule set browse option   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ValidationRuleSetBrowseOption.setter
    def ValidationRuleSetBrowseOption(self, validationRuleSetBrowseOption: PartOperationImportBuilder.ValidationRuleSetFileBrowseOption):
        """
        Setter for property: (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink) ValidationRuleSetBrowseOption
         Returns the validation rule set browse option   
            
         
        """
        pass
    
    ## Getter for property: (str) ValidationRuleSetFile
    ##  Returns the validation rule set file   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return str
    @property
    def ValidationRuleSetFile(self) -> str:
        """
        Getter for property: (str) ValidationRuleSetFile
         Returns the validation rule set file   
            
         
        """
        pass
    
    ## Setter for property: (str) ValidationRuleSetFile

    ##  Returns the validation rule set file   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ValidationRuleSetFile.setter
    def ValidationRuleSetFile(self, filename: str):
        """
        Setter for property: (str) ValidationRuleSetFile
         Returns the validation rule set file   
            
         
        """
        pass
    
    ## Getter for property: (bool) ValidationTreatOutdatedAsPass
    ##  Returns the validation treat outdated as pass   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ValidationTreatOutdatedAsPass(self) -> bool:
        """
        Getter for property: (bool) ValidationTreatOutdatedAsPass
         Returns the validation treat outdated as pass   
            
         
        """
        pass
    
    ## Setter for property: (bool) ValidationTreatOutdatedAsPass

    ##  Returns the validation treat outdated as pass   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ValidationTreatOutdatedAsPass.setter
    def ValidationTreatOutdatedAsPass(self, validationTreatOutdatedAsPass: bool):
        """
        Setter for property: (bool) ValidationTreatOutdatedAsPass
         Returns the validation treat outdated as pass   
            
         
        """
        pass
    
    ## Getter for property: (bool) ValidationTreatWarningAsPass
    ##  Returns the validation treat warning as pass   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return bool
    @property
    def ValidationTreatWarningAsPass(self) -> bool:
        """
        Getter for property: (bool) ValidationTreatWarningAsPass
         Returns the validation treat warning as pass   
            
         
        """
        pass
    
    ## Setter for property: (bool) ValidationTreatWarningAsPass

    ##  Returns the validation treat warning as pass   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    @ValidationTreatWarningAsPass.setter
    def ValidationTreatWarningAsPass(self, validationTreatWarningAsPass: bool):
        """
        Setter for property: (bool) ValidationTreatWarningAsPass
         Returns the validation treat warning as pass   
            
         
        """
        pass
    
    ##  Add parts to import 
    ##  @return errorMsgs (List[str]): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="parts"> (List[str]) </param>
    def AddParts(self, parts: List[str]) -> List[str]:
        """
         Add parts to import 
         @return errorMsgs (List[str]): .
        """
        pass
    
    ##  Add parts to import from selected folder 
    ##  @return errorMsgs (List[str]): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="folderPath"> (str) </param>
    def AddPartsFromFolder(self, folderPath: str) -> List[str]:
        """
         Add parts to import from selected folder 
         @return errorMsgs (List[str]): .
        """
        pass
    
    ##  Add parts using log file either clone log file or import log file 
    ##  @return errorMsgs (List[str]): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="logFilePath"> (str) </param>
    def AddPartsUsingLogFile(self, logFilePath: str) -> List[str]:
        """
         Add parts using log file either clone log file or import log file 
         @return errorMsgs (List[str]): .
        """
        pass
    
    ##  Execute the dry run 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ExecuteDryRun(self) -> None:
        """
         Execute the dry run 
        """
        pass
    
    ##  Get default projects information 
    ##  @return A tuple consisting of (project_names, assignment_states). 
    ##  - project_names is: List[str]. names of the projects .
    ##  - assignment_states is: @link NXOpen.Session.ProjectAssignmentState List[NXOpen.Session.ProjectAssignmentState]@endlink. assignment states .

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetDefaultProjectInformation(self) -> Tuple[List[str], List[NXOpen.Session.ProjectAssignmentState]]:
        """
         Get default projects information 
         @return A tuple consisting of (project_names, assignment_states). 
         - project_names is: List[str]. names of the projects .
         - assignment_states is: @link NXOpen.Session.ProjectAssignmentState List[NXOpen.Session.ProjectAssignmentState]@endlink. assignment states .

        """
        pass
    
    ##  Get the dfa files 
    ##  @return dfaFiles (List[str]): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetDfaFiles(self) -> List[str]:
        """
         Get the dfa files 
         @return dfaFiles (List[str]): .
        """
        pass
    
    ##  Gets the external file objects for the given part. 
    ##  @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetExternalFileObjects(self, logicalObject: LogicalObject) -> List[NXOpen.NXObject]:
        """
         Gets the external file objects for the given part. 
         @return objects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  Gets the known logical object for the given part filename. 
    ##  @return logicalObject (@link LogicalObject NXOpen.PDM.LogicalObject@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part_filename"> (str) </param>
    def GetLogicalObjectForPart(self, part_filename: str) -> LogicalObject:
        """
         Gets the known logical object for the given part filename. 
         @return logicalObject (@link LogicalObject NXOpen.PDM.LogicalObject@endlink): .
        """
        pass
    
    ##  Gets the updated logical object objects for the parts after item type, relation type or
    ##             master part for nonmaster is set or changed. 
    ##  @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetUpdatedLogicalObjects(self) -> List[LogicalObject]:
        """
         Gets the updated logical object objects for the parts after item type, relation type or
                    master part for nonmaster is set or changed. 
         @return logicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
    ##  Remove the dfa file 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="filename"> (str) </param>
    def RemoveDfaFile(self, filename: str) -> None:
        """
         Remove the dfa file 
        """
        pass
    
    ##  Clear all attributes from the selected logical objects 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="logicalObjects"> (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink) </param>
    def ResetAttributes(self, logicalObjects: List[LogicalObject]) -> None:
        """
         Clear all attributes from the selected logical objects 
        """
        pass
    
    ##  Set default projects information 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="project_names"> (List[str])  names of the projects to assign </param>
    ## <param name="assignment_states"> (@link NXOpen.Session.ProjectAssignmentState List[NXOpen.Session.ProjectAssignmentState]@endlink)  assignment states </param>
    def SetDefaultProjectInformation(self, project_names: List[str], assignment_states: List[NXOpen.Session.ProjectAssignmentState]) -> None:
        """
         Set default projects information 
        """
        pass
    
    ##  Set the dfa files 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="dfaFiles"> (List[str]) </param>
    def SetDfaFiles(self, dfaFiles: List[str]) -> None:
        """
         Set the dfa files 
        """
        pass
    
    ##  Set attributes of existing part on the given logical object so that 
    ##             the part gets imported into specified existing item based on action. 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    ## <param name="existingPartCliSpec"> (str) </param>
    def SetExistingPartAttributes(self, logicalObject: LogicalObject, existingPartCliSpec: str) -> None:
        """
         Set attributes of existing part on the given logical object so that 
                    the part gets imported into specified existing item based on action. 
        """
        pass
    
    ##  This API will decide how to treat the Part Family members present in import operation depending on 
    ##             the partFamilyTreatment input value.
    ## 
    ##             This API should be used only after assembly has been added for import operation as it will
    ##             iterate over all the Part Family Members added in import operation and set their behavior specified by
    ##             the partFamilyTreatment input value.
    ## 
    ##             Note 1: If 'Ignore Part Family Member - Include Template Part' customer default is enabled then it will always treat
    ##             Part Family Members as 'Lost' in import, So please do not use this API if this customer default is enabled,
    ##             since using this API to change the behavior of Part Family Members will not work in that case. 
    ##             Note 2: If 'Ignore Part Family Member - Include Template Part' customer default is disabled then the user must use this API
    ##             to set the desired behavior of Part Family Members. If the desired behavior is not set using this API then 
    ##             Part Family Members will not participate anymore in import operation.
    ##         
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partFamilyTreatment"> (@link PartOperationImportBuilder.PartFamilyTreatment NXOpen.PDM.PartOperationImportBuilder.PartFamilyTreatment@endlink) </param>
    def SetPartFamilyTreatment(self, partFamilyTreatment: PartOperationImportBuilder.PartFamilyTreatment) -> None:
        """
         This API will decide how to treat the Part Family members present in import operation depending on 
                    the partFamilyTreatment input value.
        
                    This API should be used only after assembly has been added for import operation as it will
                    iterate over all the Part Family Members added in import operation and set their behavior specified by
                    the partFamilyTreatment input value.
        
                    Note 1: If 'Ignore Part Family Member - Include Template Part' customer default is enabled then it will always treat
                    Part Family Members as 'Lost' in import, So please do not use this API if this customer default is enabled,
                    since using this API to change the behavior of Part Family Members will not work in that case. 
                    Note 2: If 'Ignore Part Family Member - Include Template Part' customer default is disabled then the user must use this API
                    to set the desired behavior of Part Family Members. If the desired behavior is not set using this API then 
                    Part Family Members will not participate anymore in import operation.
                
        """
        pass
    
    ## The method updates the destination folder for parts getting imported into Teamcenter  
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    def UpdateDestinationFolderForParts(self) -> None:
        """
        The method updates the destination folder for parts getting imported into Teamcenter  
        """
        pass
    
    ##  Update the Teamcenter information string attribute TCIN_IMPORT_TEAMCENTER_INFORMATION on given logical objects 
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="logicalObjects"> (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink) </param>
    def UpdateTeamcenterInformation(self, logicalObjects: List[LogicalObject]) -> None:
        """
         Update the Teamcenter information string attribute TCIN_IMPORT_TEAMCENTER_INFORMATION on given logical objects 
        """
        pass
    
    ##  Validate the user inputs for following things:
    ##             - Validates whether the input property values are valid according to defined naming rules and specified user exits for the input property.
    ##             - Check for duplicate Ids/Mfk-Ids
    ##             - Check if all required attributes have been set
    ##             - Check for cyclic references
    ##             - Check if the part to import already exists in database and has no read access
    ##             - Check if the part to import already exists in database and belong to an invalid type for import(e.g. Shape Design)
    ##             - Check for duplicate non-master dataset names under same master
    ##             - Check if it is trying to create two new revisions of same item.
    ##             - Check if the final name given to the imported part already open in session
    ##             - Validate master for a non-master being imported; the master should be present in import operation or has to exist in database for successful creation of non-master.
    ##             - Validate validation parameters e.g. user has selected Run Validation option which requires the user to specify the validation rule set file.
    ##             - Update Teamcenter information attribute on logical objects
    ##         
    ## 
    ##   <br>  Created in NX10.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ValidateLogicalObjects(self) -> None:
        """
         Validate the user inputs for following things:
                    - Validates whether the input property values are valid according to defined naming rules and specified user exits for the input property.
                    - Check for duplicate Ids/Mfk-Ids
                    - Check if all required attributes have been set
                    - Check for cyclic references
                    - Check if the part to import already exists in database and has no read access
                    - Check if the part to import already exists in database and belong to an invalid type for import(e.g. Shape Design)
                    - Check for duplicate non-master dataset names under same master
                    - Check if it is trying to create two new revisions of same item.
                    - Check if the final name given to the imported part already open in session
                    - Validate master for a non-master being imported; the master should be present in import operation or has to exist in database for successful creation of non-master.
                    - Validate validation parameters e.g. user has selected Run Validation option which requires the user to specify the validation rule set file.
                    - Update Teamcenter information attribute on logical objects
                
        """
        pass
    
import NXOpen
##  JA interface for PartOperationImportCallbackData object  <br> This cannot be created  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationImportCallbackData(NXOpen.TaggedObject): 
    """ JA interface for PartOperationImportCallbackData object """


    ## Getter for property: (@link PartOperationImportBuilder NXOpen.PDM.PartOperationImportBuilder@endlink) ImportBuilder
    ##  Returns the @link NXOpen::PDM::PartOperationImportBuilder NXOpen::PDM::PartOperationImportBuilder@endlink  builder used in this operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return PartOperationImportBuilder
    @property
    def ImportBuilder(self) -> PartOperationImportBuilder:
        """
        Getter for property: (@link PartOperationImportBuilder NXOpen.PDM.PartOperationImportBuilder@endlink) ImportBuilder
         Returns the @link NXOpen::PDM::PartOperationImportBuilder NXOpen::PDM::PartOperationImportBuilder@endlink  builder used in this operation   
            
         
        """
        pass
    
    ##  Gets the logical objects for parts participating in import operation 
    ##  @return logicalObjects (@link NativePartLogicalObject List[NXOpen.PDM.NativePartLogicalObject]@endlink):  .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetLogicalObjects(self) -> List[NativePartLogicalObject]:
        """
         Gets the logical objects for parts participating in import operation 
         @return logicalObjects (@link NativePartLogicalObject List[NXOpen.PDM.NativePartLogicalObject]@endlink):  .
        """
        pass
    
import NXOpen
## 
##     * This class is responsible for invoking registered callbacks at different stages in import operation.
##     *
##     * NOTE: Use callback data @link NXOpen::PDM::PartOperationImportCallbackData NXOpen::PDM::PartOperationImportCallbackData@endlink , which is
##     * passed as input to these callback functions, to get the logical objects participating in the current
##     * import operation. It is recommended not to hold onto these logical objects since there lifecycle is
##     * controlled by the key attributes viz. Item type, Relation type; which could be updated during this
##     * operation, resulting in redefining the logical object.
##     * 
##      <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationImportObserver(NXOpen.TaggedObjectCollection): 
    """
    * This class is responsible for invoking registered callbacks at different stages in import operation.
    *
    * NOTE: Use callback data <ja_class>NXOpen.PDM.PartOperationImportCallbackData</ja_class>, which is
    * passed as input to these callback functions, to get the logical objects participating in the current
    * import operation. It is recommended not to hold onto these logical objects since there lifecycle is
    * controlled by the key attributes viz. Item type, Relation type; which could be updated during this
    * operation, resulting in redefining the logical object.
    * 
    """


    ##  User defined Initialize callback that is called during initialization of import builder 
    ## A callback definition with the following input arguments: 
    ##  - @link PartOperationImportCallbackData NXOpen.PDM.PartOperationImportCallbackData@endlink
    ##  and no return type
    InitializeCb = Callable[[PartOperationImportCallbackData], None]
    
    
    ##  Registers a user defined Initialize callback that is called during initialization of import builder 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="initialize_cb"> (@link PartOperationImportObserver.InitializeCb NXOpen.PDM.PartOperationImportObserver.InitializeCb@endlink)  method to register </param>
    def AddInitializeCallback(initialize_cb: PartOperationImportObserver.InitializeCb) -> int:
        """
         Registers a user defined Initialize callback that is called during initialization of import builder 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PostCommit callback that is called after commit of import operation 
    ## A callback definition with the following input arguments: 
    ##  - @link PartOperationImportCallbackData NXOpen.PDM.PartOperationImportCallbackData@endlink
    ##  and no return type
    PostCommitCb = Callable[[PartOperationImportCallbackData], None]
    
    
    ##  Registers a user defined PostCommit callback that is called after commit of import operation 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="post_commit_cb"> (@link PartOperationImportObserver.PostCommitCb NXOpen.PDM.PartOperationImportObserver.PostCommitCb@endlink)  method to register </param>
    def AddPostCommitCallback(post_commit_cb: PartOperationImportObserver.PostCommitCb) -> int:
        """
         Registers a user defined PostCommit callback that is called after commit of import operation 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PreAutoAssign callback that is called before auto-assigning attributes
    ##         * NOTE: You may use this callback to override the Item Type or Relation type for the part being imported.
    ##         
    ## A callback definition with the following input arguments: 
    ##  - @link PartOperationImportCallbackData NXOpen.PDM.PartOperationImportCallbackData@endlink
    ##  and no return type
    PreAutoassignCb = Callable[[PartOperationImportCallbackData], None]
    
    
    ##  Registers a user defined PreAutoAssign callback that is called before auto-assigning attributes 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="pre_autoassign_cb"> (@link PartOperationImportObserver.PreAutoassignCb NXOpen.PDM.PartOperationImportObserver.PreAutoassignCb@endlink)  method to register </param>
    def AddPreAutoassignCallback(pre_autoassign_cb: PartOperationImportObserver.PreAutoassignCb) -> int:
        """
         Registers a user defined PreAutoAssign callback that is called before auto-assigning attributes 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PreCommit callback that is called before commit of import operation 
    ## A callback definition with the following input arguments: 
    ##  - @link PartOperationImportCallbackData NXOpen.PDM.PartOperationImportCallbackData@endlink
    ##  and no return type
    PreCommitCb = Callable[[PartOperationImportCallbackData], None]
    
    
    ##  Registers a user defined PreCommit callback that is called before commit of import operation 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="pre_commit_cb"> (@link PartOperationImportObserver.PreCommitCb NXOpen.PDM.PartOperationImportObserver.PreCommitCb@endlink)  method to register </param>
    def AddPreCommitCallback(pre_commit_cb: PartOperationImportObserver.PreCommitCb) -> int:
        """
         Registers a user defined PreCommit callback that is called before commit of import operation 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PreValidate callback that is called at start of validate objects of import operation 
    ## A callback definition with the following input arguments: 
    ##  - @link PartOperationImportCallbackData NXOpen.PDM.PartOperationImportCallbackData@endlink
    ##  and no return type
    PreValidateCb = Callable[[PartOperationImportCallbackData], None]
    
    
    ##  Registers a user defined PreValidate callback that is called at start of validate objects of import operation 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="pre_validate_cb"> (@link PartOperationImportObserver.PreValidateCb NXOpen.PDM.PartOperationImportObserver.PreValidateCb@endlink)  method to register </param>
    def AddPreValidateCallback(pre_validate_cb: PartOperationImportObserver.PreValidateCb) -> int:
        """
         Registers a user defined PreValidate callback that is called at start of validate objects of import operation 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined Terminate callback that is called during destruction of import builder 
    ## A callback definition with the following input arguments: 
    ##  - @link PartOperationImportCallbackData NXOpen.PDM.PartOperationImportCallbackData@endlink
    ##  and no return type
    TerminateCb = Callable[[PartOperationImportCallbackData], None]
    
    
    ##  Registers a user defined Terminate callback that is called during destruction of import builder 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="terminate_cb"> (@link PartOperationImportObserver.TerminateCb NXOpen.PDM.PartOperationImportObserver.TerminateCb@endlink)  method to register </param>
    def AddTerminateCallback(terminate_cb: PartOperationImportObserver.TerminateCb) -> int:
        """
         Registers a user defined Terminate callback that is called during destruction of import builder 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  Unregisters the user defined Initialize callback 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemoveInitializeCallback(id: int) -> None:
        """
         Unregisters the user defined Initialize callback 
        """
        pass
    
    ##  Unregisters the user defined PostCommit callback 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePostCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PostCommit callback 
        """
        pass
    
    ##  Unregisters the user defined PreAutoAssign callback 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePreAutoassignCallback(id: int) -> None:
        """
         Unregisters the user defined PreAutoAssign callback 
        """
        pass
    
    ##  Unregisters the user defined PreCommit callback 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePreCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PreCommit callback 
        """
        pass
    
    ##  Unregisters the user defined PreValidate callback 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePreValidateCallback(id: int) -> None:
        """
         Unregisters the user defined PreValidate callback 
        """
        pass
    
    ##  Unregisters the user defined Terminate callback 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemoveTerminateCallback(id: int) -> None:
        """
         Unregisters the user defined Terminate callback 
        """
        pass
    
import NXOpen
##  Represents a @link NXOpen::PDM::PartOperationMakeUniqueBuilder NXOpen::PDM::PartOperationMakeUniqueBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmManager::CreateMakeUniqueOperationBuilder  NXOpen::PDM::PdmManager::CreateMakeUniqueOperationBuilder @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationMakeUniqueBuilder(PartOperationCopyBuilder): 
    """ Represents a <ja_class>NXOpen.PDM.PartOperationMakeUniqueBuilder</ja_class> builder """


    ## Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedComponents
    ##  Returns the selected components to be made unique are returned.  
    ##       
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObjectList
    @property
    def SelectedComponents(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObjectList NXOpen.SelectDisplayableObjectList@endlink) SelectedComponents
         Returns the selected components to be made unique are returned.  
              
         
        """
        pass
    
import NXOpen
## 
##         Represents an @link NXOpen::PDM::PartOperationValidationPropertiesBuilder NXOpen::PDM::PartOperationValidationPropertiesBuilder@endlink  to be used 
##         for overriding the default validation parameters for a part in import operation.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::PdmManager::CreatePartOperationValidationPropertiesBuilder  NXOpen::PDM::PdmManager::CreatePartOperationValidationPropertiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BooleanValue </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## DataType </term> <description> 
##  
## String </description> </item> 
## 
## <item><term> 
##  
## IntegerValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## NumberValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ObjectPicker (deprecated) </term> <description> 
##  
## Object </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX10.0.0  <br> 

class PartOperationValidationPropertiesBuilder(NXOpen.AttributePropertiesBuilder): 
    """
        Represents an <ja_class>NXOpen.PDM.PartOperationValidationPropertiesBuilder</ja_class> to be used 
        for overriding the default validation parameters for a part in import operation.
    """


    ##  Gets the validation rule set browse option 
    ##  @return validationRuleSetBrowseOption (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetValidationRuleSetBrowseOption(self) -> PartOperationImportBuilder.ValidationRuleSetFileBrowseOption:
        """
         Gets the validation rule set browse option 
         @return validationRuleSetBrowseOption (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink): .
        """
        pass
    
    ##  Gets the validation rule set file 
    ##  @return filename (str): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetValidationRuleSetFile(self) -> str:
        """
         Gets the validation rule set file 
         @return filename (str): .
        """
        pass
    
    ##  Gets the validation treat outdated as pass flag 
    ##  @return validationTreatOutdatedAsPass (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetValidationTreatOutdatedAsPass(self) -> bool:
        """
         Gets the validation treat outdated as pass flag 
         @return validationTreatOutdatedAsPass (bool): .
        """
        pass
    
    ##  Gets the validation treat warning as pass flag 
    ##  @return validationTreatWarningAsPass (bool): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetValidationTreatWarningAsPass(self) -> bool:
        """
         Gets the validation treat warning as pass flag 
         @return validationTreatWarningAsPass (bool): .
        """
        pass
    
    ##  Sets the validation rule set browse option 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="validationRuleSetBrowseOption"> (@link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink) </param>
    def SetValidationRuleSetBrowseOption(self, validationRuleSetBrowseOption: PartOperationImportBuilder.ValidationRuleSetFileBrowseOption) -> None:
        """
         Sets the validation rule set browse option 
        """
        pass
    
    ##  Sets the validation rule set file 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="filename"> (str) </param>
    def SetValidationRuleSetFile(self, filename: str) -> None:
        """
         Sets the validation rule set file 
        """
        pass
    
    ##  Sets the validation treat outdated as pass flag 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="validationTreatOutdatedAsPass"> (bool) </param>
    def SetValidationTreatOutdatedAsPass(self, validationTreatOutdatedAsPass: bool) -> None:
        """
         Sets the validation treat outdated as pass flag 
        """
        pass
    
    ##  Sets the validation treat warning as pass flag 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="validationTreatWarningAsPass"> (bool) </param>
    def SetValidationTreatWarningAsPass(self, validationTreatWarningAsPass: bool) -> None:
        """
         Sets the validation treat warning as pass flag 
        """
        pass
    
import NXOpen
## 
##         Represents an @link NXOpen::PDM::PdmCopyOrEditOperationAttributePropertiesBuilder NXOpen::PDM::PdmCopyOrEditOperationAttributePropertiesBuilder@endlink  to be used 
##         for overriding the default values for a part in clone operation.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::PdmManager::CreatePdmCopyOrEditOperationAttributePropertiesBuilder  NXOpen::PDM::PdmManager::CreatePdmCopyOrEditOperationAttributePropertiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BooleanValue </term> <description> 
##  
## False </description> </item> 
## 
## <item><term> 
##  
## DataType </term> <description> 
##  
## String </description> </item> 
## 
## <item><term> 
##  
## IntegerValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## NumberValue </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ObjectPicker (deprecated) </term> <description> 
##  
## Object </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class PdmCopyOrEditOperationAttributePropertiesBuilder(NXOpen.AttributePropertiesBuilder): 
    """
        Represents an <ja_class>NXOpen.PDM.PdmCopyOrEditOperationAttributePropertiesBuilder</ja_class> to be used 
        for overriding the default values for a part in clone operation.
    """
    pass


import NXOpen
##  Represents a builder class that performs Copy or Edit(Clone) operation  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreatePdmCopyOrEditOperationBuilder  NXOpen::PDM::PdmSession::CreatePdmCopyOrEditOperationBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DefaultAction </term> <description> 
##  
## Clone </description> </item> 
## 
## <item><term> 
##  
## NumberingSource </term> <description> 
##  
## AutoGenerate </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1980.0.0  <br> 

class PdmCopyOrEditOperationBuilder(PartOperationBuilder): 
    """ Represents a builder class that performs Copy or Edit(Clone) operation """


    ##  This enum is used to specify the related CAE types to be loaded. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SimFemIdeal</term><description> 
    ## </description> </item><item><term> 
    ## FemIdeal</term><description> 
    ## </description> </item><item><term> 
    ## Ideal</term><description> 
    ## </description> </item><item><term> 
    ## NotSet</term><description> 
    ## </description> </item></list>
    class CaeRelationTraversalOption(Enum):
        """
        Members Include: <SimFemIdeal> <FemIdeal> <Ideal> <NotSet>
        """
        SimFemIdeal: int
        FemIdeal: int
        Ideal: int
        NotSet: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the default action for clone. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Clone</term><description> 
    ## </description> </item><item><term> 
    ## Retain</term><description> 
    ## </description> </item><item><term> 
    ## Revise</term><description> 
    ## </description> </item><item><term> 
    ## Replace</term><description> 
    ## </description> </item><item><term> 
    ## Overwrite</term><description> 
    ## </description> </item></list>
    class CloneAction(Enum):
        """
        Members Include: <Clone> <Retain> <Revise> <Replace> <Overwrite>
        """
        Clone: int
        Retain: int
        Revise: int
        Replace: int
        Overwrite: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.CloneAction:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the conversion rule for @link NXOpen::PDM::PdmCopyOrEditOperationBuilder::NumberingSourceOptionNamingRule NXOpen::PDM::PdmCopyOrEditOperationBuilder::NumberingSourceOptionNamingRule@endlink . 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## WithPrefix</term><description> 
    ## </description> </item><item><term> 
    ## WithSuffix</term><description> 
    ## </description> </item><item><term> 
    ## WithReplaceString</term><description> 
    ## </description> </item><item><term> 
    ## WithRenumber</term><description> 
    ## </description> </item><item><term> 
    ## MixedRule</term><description> 
    ## </description> </item></list>
    class ConversionRule(Enum):
        """
        Members Include: <WithPrefix> <WithSuffix> <WithReplaceString> <WithRenumber> <MixedRule>
        """
        WithPrefix: int
        WithSuffix: int
        WithReplaceString: int
        WithRenumber: int
        MixedRule: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.ConversionRule:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the default behavior for auto assign. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AutoGenerate</term><description> 
    ## </description> </item><item><term> 
    ## NamingRule</term><description> 
    ## </description> </item><item><term> 
    ## UserName</term><description> 
    ## </description> </item></list>
    class NumberingSourceOption(Enum):
        """
        Members Include: <AutoGenerate> <NamingRule> <UserName>
        """
        AutoGenerate: int
        NamingRule: int
        UserName: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PdmCopyOrEditOperationBuilder.NumberingSourceOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AssignAlternateIds
    ##  Returns the function returns/sets the flag to assign alternate IDs during Pdm copy or edit operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def AssignAlternateIds(self) -> bool:
        """
        Getter for property: (bool) AssignAlternateIds
         Returns the function returns/sets the flag to assign alternate IDs during Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Setter for property: (bool) AssignAlternateIds

    ##  Returns the function returns/sets the flag to assign alternate IDs during Pdm copy or edit operation   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @AssignAlternateIds.setter
    def AssignAlternateIds(self, createAlternateIDs: bool):
        """
        Setter for property: (bool) AssignAlternateIds
         Returns the function returns/sets the flag to assign alternate IDs during Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Getter for property: (bool) AssignDefaultChangeNotice
    ##  Returns the function returns/sets the flag to assign the default change notice set on builder to target objects created in pdm copy or edit operation.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def AssignDefaultChangeNotice(self) -> bool:
        """
        Getter for property: (bool) AssignDefaultChangeNotice
         Returns the function returns/sets the flag to assign the default change notice set on builder to target objects created in pdm copy or edit operation.  
             
         
        """
        pass
    
    ## Setter for property: (bool) AssignDefaultChangeNotice

    ##  Returns the function returns/sets the flag to assign the default change notice set on builder to target objects created in pdm copy or edit operation.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @AssignDefaultChangeNotice.setter
    def AssignDefaultChangeNotice(self, assignDefaultChangeNotice: bool):
        """
        Setter for property: (bool) AssignDefaultChangeNotice
         Returns the function returns/sets the flag to assign the default change notice set on builder to target objects created in pdm copy or edit operation.  
             
         
        """
        pass
    
    ## Getter for property: (bool) AttachLogFile
    ##  Returns the function returns/sets the flag to attach the output log file as associated file to the top part of the input assembly   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def AttachLogFile(self) -> bool:
        """
        Getter for property: (bool) AttachLogFile
         Returns the function returns/sets the flag to attach the output log file as associated file to the top part of the input assembly   
            
         
        """
        pass
    
    ## Setter for property: (bool) AttachLogFile

    ##  Returns the function returns/sets the flag to attach the output log file as associated file to the top part of the input assembly   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @AttachLogFile.setter
    def AttachLogFile(self, attachLogFile: bool):
        """
        Setter for property: (bool) AttachLogFile
         Returns the function returns/sets the flag to attach the output log file as associated file to the top part of the input assembly   
            
         
        """
        pass
    
    ## Getter for property: (@link PdmCopyOrEditOperationBuilder.ConversionRule NXOpen.PDM.PdmCopyOrEditOperationBuilder.ConversionRule@endlink) ConversionType
    ##  Returns the function returns/sets the conversion type to use for generating a new part ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PdmCopyOrEditOperationBuilder.ConversionRule
    @property
    def ConversionType(self) -> PdmCopyOrEditOperationBuilder.ConversionRule:
        """
        Getter for property: (@link PdmCopyOrEditOperationBuilder.ConversionRule NXOpen.PDM.PdmCopyOrEditOperationBuilder.ConversionRule@endlink) ConversionType
         Returns the function returns/sets the conversion type to use for generating a new part ID   
            
         
        """
        pass
    
    ## Setter for property: (@link PdmCopyOrEditOperationBuilder.ConversionRule NXOpen.PDM.PdmCopyOrEditOperationBuilder.ConversionRule@endlink) ConversionType

    ##  Returns the function returns/sets the conversion type to use for generating a new part ID   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ConversionType.setter
    def ConversionType(self, conversionType: PdmCopyOrEditOperationBuilder.ConversionRule):
        """
        Setter for property: (@link PdmCopyOrEditOperationBuilder.ConversionRule NXOpen.PDM.PdmCopyOrEditOperationBuilder.ConversionRule@endlink) ConversionType
         Returns the function returns/sets the conversion type to use for generating a new part ID   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyAltrep
    ##  Returns the function returns/sets the flag to copy non-master altrep   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CopyAltrep(self) -> bool:
        """
        Getter for property: (bool) CopyAltrep
         Returns the function returns/sets the flag to copy non-master altrep   
            
         
        """
        pass
    
    ## Setter for property: (bool) CopyAltrep

    ##  Returns the function returns/sets the flag to copy non-master altrep   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopyAltrep.setter
    def CopyAltrep(self, copyAltrep: bool):
        """
        Setter for property: (bool) CopyAltrep
         Returns the function returns/sets the flag to copy non-master altrep   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyAssociatedFiles
    ##  Returns the function returns/sets the flag to copy associated files   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CopyAssociatedFiles(self) -> bool:
        """
        Getter for property: (bool) CopyAssociatedFiles
         Returns the function returns/sets the flag to copy associated files   
            
         
        """
        pass
    
    ## Setter for property: (bool) CopyAssociatedFiles

    ##  Returns the function returns/sets the flag to copy associated files   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopyAssociatedFiles.setter
    def CopyAssociatedFiles(self, copyAssociatedFiles: bool):
        """
        Setter for property: (bool) CopyAssociatedFiles
         Returns the function returns/sets the flag to copy associated files   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyCaeMotion
    ##  Returns the function returns/sets the flag to copy non-master cae-motion   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CopyCaeMotion(self) -> bool:
        """
        Getter for property: (bool) CopyCaeMotion
         Returns the function returns/sets the flag to copy non-master cae-motion   
            
         
        """
        pass
    
    ## Setter for property: (bool) CopyCaeMotion

    ##  Returns the function returns/sets the flag to copy non-master cae-motion   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopyCaeMotion.setter
    def CopyCaeMotion(self, copyCaeMotion: bool):
        """
        Setter for property: (bool) CopyCaeMotion
         Returns the function returns/sets the flag to copy non-master cae-motion   
            
         
        """
        pass
    
    ## Getter for property: (@link PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption@endlink) CopyCaeRelationOption
    ##  Returns the function returns/sets the option to include cae components in Pdm copy or edit operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption
    @property
    def CopyCaeRelationOption(self) -> PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption:
        """
        Getter for property: (@link PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption@endlink) CopyCaeRelationOption
         Returns the function returns/sets the option to include cae components in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Setter for property: (@link PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption@endlink) CopyCaeRelationOption

    ##  Returns the function returns/sets the option to include cae components in Pdm copy or edit operation   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopyCaeRelationOption.setter
    def CopyCaeRelationOption(self, copyCaeRelationOption: PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption):
        """
        Setter for property: (@link PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption@endlink) CopyCaeRelationOption
         Returns the function returns/sets the option to include cae components in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyCaeRelations
    ##  Returns the function returns/sets the flag to include cae related components in Pdm copy or edit operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CopyCaeRelations(self) -> bool:
        """
        Getter for property: (bool) CopyCaeRelations
         Returns the function returns/sets the flag to include cae related components in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Setter for property: (bool) CopyCaeRelations

    ##  Returns the function returns/sets the flag to include cae related components in Pdm copy or edit operation   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopyCaeRelations.setter
    def CopyCaeRelations(self, copyCaeRelations: bool):
        """
        Setter for property: (bool) CopyCaeRelations
         Returns the function returns/sets the flag to include cae related components in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyDrawingRelations
    ##  Returns the function returns/sets the flag to include master drawings of the assembly/parts added in Pdm copy or edit operation   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CopyDrawingRelations(self) -> bool:
        """
        Getter for property: (bool) CopyDrawingRelations
         Returns the function returns/sets the flag to include master drawings of the assembly/parts added in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Setter for property: (bool) CopyDrawingRelations

    ##  Returns the function returns/sets the flag to include master drawings of the assembly/parts added in Pdm copy or edit operation   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopyDrawingRelations.setter
    def CopyDrawingRelations(self, copyDrawingRelations: bool):
        """
        Setter for property: (bool) CopyDrawingRelations
         Returns the function returns/sets the flag to include master drawings of the assembly/parts added in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Getter for property: (bool) CopyManifestation
    ##  Returns the function returns/sets the flag to copy non-master menifestation  
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CopyManifestation(self) -> bool:
        """
        Getter for property: (bool) CopyManifestation
         Returns the function returns/sets the flag to copy non-master menifestation  
            
         
        """
        pass
    
    ## Setter for property: (bool) CopyManifestation

    ##  Returns the function returns/sets the flag to copy non-master menifestation  
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopyManifestation.setter
    def CopyManifestation(self, copyManifestation: bool):
        """
        Setter for property: (bool) CopyManifestation
         Returns the function returns/sets the flag to copy non-master menifestation  
            
         
        """
        pass
    
    ## Getter for property: (bool) CopySpecification
    ##  Returns the function returns/sets the flag to copy non-master specification   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def CopySpecification(self) -> bool:
        """
        Getter for property: (bool) CopySpecification
         Returns the function returns/sets the flag to copy non-master specification   
            
         
        """
        pass
    
    ## Setter for property: (bool) CopySpecification

    ##  Returns the function returns/sets the flag to copy non-master specification   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @CopySpecification.setter
    def CopySpecification(self, copySpecification: bool):
        """
        Setter for property: (bool) CopySpecification
         Returns the function returns/sets the flag to copy non-master specification   
            
         
        """
        pass
    
    ## Getter for property: (@link PdmCopyOrEditOperationBuilder.CloneAction NXOpen.PDM.PdmCopyOrEditOperationBuilder.CloneAction@endlink) DefaultAction
    ##  Returns the function returns/sets the default clone action to use for Pdm copy or edit operation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PdmCopyOrEditOperationBuilder.CloneAction
    @property
    def DefaultAction(self) -> PdmCopyOrEditOperationBuilder.CloneAction:
        """
        Getter for property: (@link PdmCopyOrEditOperationBuilder.CloneAction NXOpen.PDM.PdmCopyOrEditOperationBuilder.CloneAction@endlink) DefaultAction
         Returns the function returns/sets the default clone action to use for Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Setter for property: (@link PdmCopyOrEditOperationBuilder.CloneAction NXOpen.PDM.PdmCopyOrEditOperationBuilder.CloneAction@endlink) DefaultAction

    ##  Returns the function returns/sets the default clone action to use for Pdm copy or edit operation   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DefaultAction.setter
    def DefaultAction(self, defaultAction: PdmCopyOrEditOperationBuilder.CloneAction):
        """
        Setter for property: (@link PdmCopyOrEditOperationBuilder.CloneAction NXOpen.PDM.PdmCopyOrEditOperationBuilder.CloneAction@endlink) DefaultAction
         Returns the function returns/sets the default clone action to use for Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultAlternateIdContext
    ##  Returns the function returns/sets the IdContext to be used while assigning alternate IDs during clone   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def DefaultAlternateIdContext(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdContext
         Returns the function returns/sets the IdContext to be used while assigning alternate IDs during clone   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultAlternateIdContext

    ##  Returns the function returns/sets the IdContext to be used while assigning alternate IDs during clone   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DefaultAlternateIdContext.setter
    def DefaultAlternateIdContext(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdContext
         Returns the function returns/sets the IdContext to be used while assigning alternate IDs during clone   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultAlternateIdType
    ##  Returns the function returns/sets the IdType to be used while assigning alternate IDs during clone  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def DefaultAlternateIdType(self) -> str:
        """
        Getter for property: (str) DefaultAlternateIdType
         Returns the function returns/sets the IdType to be used while assigning alternate IDs during clone  
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultAlternateIdType

    ##  Returns the function returns/sets the IdType to be used while assigning alternate IDs during clone  
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DefaultAlternateIdType.setter
    def DefaultAlternateIdType(self, filename: str):
        """
        Setter for property: (str) DefaultAlternateIdType
         Returns the function returns/sets the IdType to be used while assigning alternate IDs during clone  
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultChangeNotice
    ##  Returns the function returns/sets the default change notice for Pdm copy or edit operation in CLI format.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def DefaultChangeNotice(self) -> str:
        """
        Getter for property: (str) DefaultChangeNotice
         Returns the function returns/sets the default change notice for Pdm copy or edit operation in CLI format.  
             
         
        """
        pass
    
    ## Setter for property: (str) DefaultChangeNotice

    ##  Returns the function returns/sets the default change notice for Pdm copy or edit operation in CLI format.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DefaultChangeNotice.setter
    def DefaultChangeNotice(self, defaultChangeNotice: str):
        """
        Setter for property: (str) DefaultChangeNotice
         Returns the function returns/sets the default change notice for Pdm copy or edit operation in CLI format.  
             
         
        """
        pass
    
    ## Getter for property: (str) DefaultOwningGroup
    ##  Returns the function returns/sets the default owning group to be assigned to the cloned parts   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def DefaultOwningGroup(self) -> str:
        """
        Getter for property: (str) DefaultOwningGroup
         Returns the function returns/sets the default owning group to be assigned to the cloned parts   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultOwningGroup

    ##  Returns the function returns/sets the default owning group to be assigned to the cloned parts   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DefaultOwningGroup.setter
    def DefaultOwningGroup(self, defaultOwningGroup: str):
        """
        Setter for property: (str) DefaultOwningGroup
         Returns the function returns/sets the default owning group to be assigned to the cloned parts   
            
         
        """
        pass
    
    ## Getter for property: (str) DefaultOwningUser
    ##  Returns the function returns/sets the default owning user to be assigned to the cloned parts   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def DefaultOwningUser(self) -> str:
        """
        Getter for property: (str) DefaultOwningUser
         Returns the function returns/sets the default owning user to be assigned to the cloned parts   
            
         
        """
        pass
    
    ## Setter for property: (str) DefaultOwningUser

    ##  Returns the function returns/sets the default owning user to be assigned to the cloned parts   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @DefaultOwningUser.setter
    def DefaultOwningUser(self, defaultOwningUser: str):
        """
        Setter for property: (str) DefaultOwningUser
         Returns the function returns/sets the default owning user to be assigned to the cloned parts   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeComponentParts
    ##  Returns the function returns/sets the flag to include component parts of the assembly added in Pdm copy or edit operation   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def IncludeComponentParts(self) -> bool:
        """
        Getter for property: (bool) IncludeComponentParts
         Returns the function returns/sets the flag to include component parts of the assembly added in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeComponentParts

    ##  Returns the function returns/sets the flag to include component parts of the assembly added in Pdm copy or edit operation   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @IncludeComponentParts.setter
    def IncludeComponentParts(self, includeComponentParts: bool):
        """
        Setter for property: (bool) IncludeComponentParts
         Returns the function returns/sets the flag to include component parts of the assembly added in Pdm copy or edit operation   
            
         
        """
        pass
    
    ## Getter for property: (@link PdmCopyOrEditOperationBuilder.NumberingSourceOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.NumberingSourceOption@endlink) NumberingSource
    ##  Returns the function returns/sets the numbering source to use for Part ID generation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return PdmCopyOrEditOperationBuilder.NumberingSourceOption
    @property
    def NumberingSource(self) -> PdmCopyOrEditOperationBuilder.NumberingSourceOption:
        """
        Getter for property: (@link PdmCopyOrEditOperationBuilder.NumberingSourceOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.NumberingSourceOption@endlink) NumberingSource
         Returns the function returns/sets the numbering source to use for Part ID generation   
            
         
        """
        pass
    
    ## Setter for property: (@link PdmCopyOrEditOperationBuilder.NumberingSourceOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.NumberingSourceOption@endlink) NumberingSource

    ##  Returns the function returns/sets the numbering source to use for Part ID generation   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @NumberingSource.setter
    def NumberingSource(self, numberingSource: PdmCopyOrEditOperationBuilder.NumberingSourceOption):
        """
        Setter for property: (@link PdmCopyOrEditOperationBuilder.NumberingSourceOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.NumberingSourceOption@endlink) NumberingSource
         Returns the function returns/sets the numbering source to use for Part ID generation   
            
         
        """
        pass
    
    ## Getter for property: (str) OutputLogFile
    ##  Returns the function returns/sets the output log file to dump Pdm copy or edit operation information   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def OutputLogFile(self) -> str:
        """
        Getter for property: (str) OutputLogFile
         Returns the function returns/sets the output log file to dump Pdm copy or edit operation information   
            
         
        """
        pass
    
    ## Setter for property: (str) OutputLogFile

    ##  Returns the function returns/sets the output log file to dump Pdm copy or edit operation information   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @OutputLogFile.setter
    def OutputLogFile(self, filename: str):
        """
        Setter for property: (str) OutputLogFile
         Returns the function returns/sets the output log file to dump Pdm copy or edit operation information   
            
         
        """
        pass
    
    ## Getter for property: (str) PrefixStr
    ##  Returns the function returns/sets the prefix str to be applied to the source part ID to generate a new part ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def PrefixStr(self) -> str:
        """
        Getter for property: (str) PrefixStr
         Returns the function returns/sets the prefix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    
    ## Setter for property: (str) PrefixStr

    ##  Returns the function returns/sets the prefix str to be applied to the source part ID to generate a new part ID   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @PrefixStr.setter
    def PrefixStr(self, prefixStr: str):
        """
        Setter for property: (str) PrefixStr
         Returns the function returns/sets the prefix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    
    ## Getter for property: (str) RenumberStr
    ##  Returns the function returns/sets the renumber string to generate a new part ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def RenumberStr(self) -> str:
        """
        Getter for property: (str) RenumberStr
         Returns the function returns/sets the renumber string to generate a new part ID   
            
         
        """
        pass
    
    ## Setter for property: (str) RenumberStr

    ##  Returns the function returns/sets the renumber string to generate a new part ID   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RenumberStr.setter
    def RenumberStr(self, numberAttr: str):
        """
        Setter for property: (str) RenumberStr
         Returns the function returns/sets the renumber string to generate a new part ID   
            
         
        """
        pass
    
    ## Getter for property: (str) ReplaceWithStr
    ##  Returns the function returns/sets the string to replace with, to generate a new part ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def ReplaceWithStr(self) -> str:
        """
        Getter for property: (str) ReplaceWithStr
         Returns the function returns/sets the string to replace with, to generate a new part ID   
            
         
        """
        pass
    
    ## Setter for property: (str) ReplaceWithStr

    ##  Returns the function returns/sets the string to replace with, to generate a new part ID   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @ReplaceWithStr.setter
    def ReplaceWithStr(self, replaceWithStr: str):
        """
        Setter for property: (str) ReplaceWithStr
         Returns the function returns/sets the string to replace with, to generate a new part ID   
            
         
        """
        pass
    
    ## Getter for property: (bool) RetainOwnership
    ##  Returns the function returns/sets the flag to retain ownership of the parts during clone   
    ##     
    ##  
    ## Getter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def RetainOwnership(self) -> bool:
        """
        Getter for property: (bool) RetainOwnership
         Returns the function returns/sets the flag to retain ownership of the parts during clone   
            
         
        """
        pass
    
    ## Setter for property: (bool) RetainOwnership

    ##  Returns the function returns/sets the flag to retain ownership of the parts during clone   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @RetainOwnership.setter
    def RetainOwnership(self, retainOwnership: bool):
        """
        Setter for property: (bool) RetainOwnership
         Returns the function returns/sets the flag to retain ownership of the parts during clone   
            
         
        """
        pass
    
    ## Getter for property: (str) StringToReplace
    ##  Returns the function returns/sets the string in the source part ID to replace, to generate a new part ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def StringToReplace(self) -> str:
        """
        Getter for property: (str) StringToReplace
         Returns the function returns/sets the string in the source part ID to replace, to generate a new part ID   
            
         
        """
        pass
    
    ## Setter for property: (str) StringToReplace

    ##  Returns the function returns/sets the string in the source part ID to replace, to generate a new part ID   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @StringToReplace.setter
    def StringToReplace(self, stringToReplace: str):
        """
        Setter for property: (str) StringToReplace
         Returns the function returns/sets the string in the source part ID to replace, to generate a new part ID   
            
         
        """
        pass
    
    ## Getter for property: (str) SuffixStr
    ##  Returns the function returns/sets the suffix str to be applied to the source part ID to generate a new part ID   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return str
    @property
    def SuffixStr(self) -> str:
        """
        Getter for property: (str) SuffixStr
         Returns the function returns/sets the suffix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    
    ## Setter for property: (str) SuffixStr

    ##  Returns the function returns/sets the suffix str to be applied to the source part ID to generate a new part ID   
    ##     
    ##  
    ## Setter License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @SuffixStr.setter
    def SuffixStr(self, suffixStr: str):
        """
        Setter for property: (str) SuffixStr
         Returns the function returns/sets the suffix str to be applied to the source part ID to generate a new part ID   
            
         
        """
        pass
    
    ##  This function adds parts to the Pdm copy or edit operation 
    ##  @return errorMsgs (List[str]): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="parts"> (List[str]) </param>
    def AddParts(self, parts: List[str]) -> List[str]:
        """
         This function adds parts to the Pdm copy or edit operation 
         @return errorMsgs (List[str]): .
        """
        pass
    
    ##  This function adds parts to the Pdm copy or edit operation using clone log file 
    ##  @return errorMsgs (List[str]): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="logFilePath"> (str) </param>
    def AddPartsUsingCloneLogFile(self, logFilePath: str) -> List[str]:
        """
         This function adds parts to the Pdm copy or edit operation using clone log file 
         @return errorMsgs (List[str]): .
        """
        pass
    
    ##  This function creates/updates the operation objects of the parts participating in the Pdm copy or edit operation.
    ##             Note: The operation object needs to be updated in certain cases, e.g. after item type is changed.
    ##         
    ##  @return copyOperationObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="doUpdate"> (bool) </param>
    def CreateOrUpdatePdmCopyOrEditOperationObjects(self, doUpdate: bool) -> List[PdmCopyOrEditOperationObject]:
        """
         This function creates/updates the operation objects of the parts participating in the Pdm copy or edit operation.
                    Note: The operation object needs to be updated in certain cases, e.g. after item type is changed.
                
         @return copyOperationObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
        """
        pass
    
    ##  This function executes the dry run 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ExecuteDryRun(self) -> None:
        """
         This function executes the dry run 
        """
        pass
    
    ##  This function gets the default projects information 
    ##  @return A tuple consisting of (project_names, assignment_states). 
    ##  - project_names is: List[str]. names of the projects .
    ##  - assignment_states is: @link NXOpen.Session.ProjectAssignmentState List[NXOpen.Session.ProjectAssignmentState]@endlink. assignment states .

    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetDefaultProjectInformation(self) -> Tuple[List[str], List[NXOpen.Session.ProjectAssignmentState]]:
        """
         This function gets the default projects information 
         @return A tuple consisting of (project_names, assignment_states). 
         - project_names is: List[str]. names of the projects .
         - assignment_states is: @link NXOpen.Session.ProjectAssignmentState List[NXOpen.Session.ProjectAssignmentState]@endlink. assignment states .

        """
        pass
    
    ##  This function gets the operation object for the given part spec. 
    ##  @return operationObject (@link PdmCopyOrEditOperationObject NXOpen.PDM.PdmCopyOrEditOperationObject@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="part_filename"> (str) </param>
    def GetPdmCopyOrEditOperationObject(self, part_filename: str) -> PdmCopyOrEditOperationObject:
        """
         This function gets the operation object for the given part spec. 
         @return operationObject (@link PdmCopyOrEditOperationObject NXOpen.PDM.PdmCopyOrEditOperationObject@endlink): .
        """
        pass
    
    ##  This function gets all the operation objects participating in the Pdm copy or edit operation. 
    ##  @return copyOperationObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetPdmCopyOrEditOperationObjects(self) -> List[PdmCopyOrEditOperationObject]:
        """
         This function gets all the operation objects participating in the Pdm copy or edit operation. 
         @return copyOperationObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
        """
        pass
    
    ##  This function cleara all attributes from the selected operation objects 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def ResetAttributes(self, objects: List[NXOpen.NXObject]) -> None:
        """
         This function cleara all attributes from the selected operation objects 
        """
        pass
    
    ##  This function sets the clone action on given operation objects, this change in action 
    ##         might cause clone action change on related operation objects. Operation objects
    ##         whose action got changed will be returned 
    ##  @return modifiedLogicalObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="operationObject"> (@link PdmCopyOrEditOperationObject NXOpen.PDM.PdmCopyOrEditOperationObject@endlink) </param>
    ## <param name="cloneAction"> (@link PdmCopyOrEditOperationBuilder.CloneAction NXOpen.PDM.PdmCopyOrEditOperationBuilder.CloneAction@endlink) </param>
    def SetCloneAction(self, operationObject: PdmCopyOrEditOperationObject, cloneAction: PdmCopyOrEditOperationBuilder.CloneAction) -> List[PdmCopyOrEditOperationObject]:
        """
         This function sets the clone action on given operation objects, this change in action 
                might cause clone action change on related operation objects. Operation objects
                whose action got changed will be returned 
         @return modifiedLogicalObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
        """
        pass
    
    ##  This function sets the configuration context using the Revision Rule Name. 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="setDefault"> (bool) </param>
    ## <param name="revisionRuleName"> (str) </param>
    def SetConfigurationContextUsingRevRule(self, setDefault: bool, revisionRuleName: str) -> int:
        """
         This function sets the configuration context using the Revision Rule Name. 
         @return status (int): .
        """
        pass
    
    ##  This function sets the default projects information 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="project_names"> (List[str])  names of the projects to assign </param>
    ## <param name="assignment_states"> (@link NXOpen.Session.ProjectAssignmentState List[NXOpen.Session.ProjectAssignmentState]@endlink)  assignment states </param>
    def SetDefaultProjectInformation(self, project_names: List[str], assignment_states: List[NXOpen.Session.ProjectAssignmentState]) -> None:
        """
         This function sets the default projects information 
        """
        pass
    
    ##  This function sets the assembly load option for managed mode. 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="loadOption"> (@link NXOpen.LoadOptions.ManagedModeLoadMethod NXOpen.LoadOptions.ManagedModeLoadMethod@endlink) </param>
    def SetLoadOption(self, loadOption: NXOpen.LoadOptions.ManagedModeLoadMethod) -> None:
        """
         This function sets the assembly load option for managed mode. 
        """
        pass
    
    ##  This function sets the transient part to overwrite for the given operation object, this is needed for OVERWRITE action 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="operationObject"> (@link PdmCopyOrEditOperationObject NXOpen.PDM.PdmCopyOrEditOperationObject@endlink) </param>
    ## <param name="transientPartCliSpec"> (str) </param>
    def SetOverwritePart(self, operationObject: PdmCopyOrEditOperationObject, transientPartCliSpec: str) -> int:
        """
         This function sets the transient part to overwrite for the given operation object, this is needed for OVERWRITE action 
         @return status (int): .
        """
        pass
    
    ##  This function sets the replacement part for the given operation object, this is needed for Replace action 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="operationObject"> (@link PdmCopyOrEditOperationObject NXOpen.PDM.PdmCopyOrEditOperationObject@endlink) </param>
    ## <param name="replacePartCliSpec"> (str) </param>
    def SetReplacePart(self, operationObject: PdmCopyOrEditOperationObject, replacePartCliSpec: str) -> int:
        """
         This function sets the replacement part for the given operation object, this is needed for Replace action 
         @return status (int): .
        """
        pass
    
    ##  For the input master part, this function updates all nonmaster dataset names by honoring the UGPART_saveas_pattern TC preference 
    ##  @return status (int): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="operationObject"> (@link PdmCopyOrEditOperationObject NXOpen.PDM.PdmCopyOrEditOperationObject@endlink)  Operation object of master part </param>
    def UpdateNonMasterDatasetNameMatchingSaveAsPattern(self, operationObject: PdmCopyOrEditOperationObject) -> int:
        """
         For the input master part, this function updates all nonmaster dataset names by honoring the UGPART_saveas_pattern TC preference 
         @return status (int): .
        """
        pass
    
    ##  This function updates the Teamcenter information string attribute 'TCIN_CLONE_TEAMCENTER_INFORMATION' on given operation objects 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def UpdateTeamcenterInformation(self, objects: List[NXOpen.NXObject]) -> None:
        """
         This function updates the Teamcenter information string attribute 'TCIN_CLONE_TEAMCENTER_INFORMATION' on given operation objects 
        """
        pass
    
    ##  This function validates the user inputs for following things:
    ##             - Validates whether the input property values are valid according to defined naming rules and specified user exits for the input property.
    ##             - Check for duplicate Ids/Mfk-Ids
    ##             - Check if all required attributes have been set
    ##         
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def ValidateOperationObjects(self) -> None:
        """
         This function validates the user inputs for following things:
                    - Validates whether the input property values are valid according to defined naming rules and specified user exits for the input property.
                    - Check for duplicate Ids/Mfk-Ids
                    - Check if all required attributes have been set
                
        """
        pass
    
import NXOpen
##  JA interface for PdmCopyOrEditOperationCallbackData object  <br> This cannot be created  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class PdmCopyOrEditOperationCallbackData(NXOpen.TaggedObject): 
    """ JA interface for PdmCopyOrEditOperationCallbackData object """


    ##  The @link NXOpen::PDM::PdmCopyOrEditOperationBuilder NXOpen::PDM::PdmCopyOrEditOperationBuilder@endlink  Builder used in this operation 
    ##  @return builder (@link PdmCopyOrEditOperationBuilder NXOpen.PDM.PdmCopyOrEditOperationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetBuilder(self) -> PdmCopyOrEditOperationBuilder:
        """
         The @link NXOpen::PDM::PdmCopyOrEditOperationBuilder NXOpen::PDM::PdmCopyOrEditOperationBuilder@endlink  Builder used in this operation 
         @return builder (@link PdmCopyOrEditOperationBuilder NXOpen.PDM.PdmCopyOrEditOperationBuilder@endlink): .
        """
        pass
    
import NXOpen
## 
##         Represents the class for object participating in the Copy operation.
##      <br> Instances of this class can only be accessed through @link NXOpen::PDM::PdmCopyOrEditOperationBuilder NXOpen::PDM::PdmCopyOrEditOperationBuilder@endlink  builder.  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class PdmCopyOrEditOperationObject(NXOpen.NXObject): 
    """
        Represents the class for object participating in the Copy operation.
    """


    ##  Gets the primary logical object represented by this operation object 
    ##  @return primaryLogicalObject (@link LogicalObject NXOpen.PDM.LogicalObject@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetCurrentPrimaryLogicalObject(self) -> LogicalObject:
        """
         Gets the primary logical object represented by this operation object 
         @return primaryLogicalObject (@link LogicalObject NXOpen.PDM.LogicalObject@endlink): .
        """
        pass
    
    ##  Gets the final name of this object. 
    ##  @return finalName (str):  the final name assigned to the part being cloned .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetFinalName(self) -> str:
        """
         Gets the final name of this object. 
         @return finalName (str):  the final name assigned to the part being cloned .
        """
        pass
    
    ##  Gets the initial name of this object. 
    ##  @return initialName (str):  the filename of added for copy .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetInitialName(self) -> str:
        """
         Gets the initial name of this object. 
         @return initialName (str):  the filename of added for copy .
        """
        pass
    
    ##  Gets the nonmaster logical objects associated with the copy operation object. 
    ##  @return secondaryLogicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def GetSecondaryLogicalObjects(self) -> List[LogicalObject]:
        """
         Gets the nonmaster logical objects associated with the copy operation object. 
         @return secondaryLogicalObjects (@link LogicalObject List[NXOpen.PDM.LogicalObject]@endlink): .
        """
        pass
    
import NXOpen
## 
##     * This class is responsible for invoking registered callbacks at different stages in clone operation.
##     *
##     * NOTE: Use callback data @link NXOpen::PDM::PdmCopyOrEditOperationCallbackData NXOpen::PDM::PdmCopyOrEditOperationCallbackData@endlink , which is
##     * passed as input to these callback functions, to get the logical objects participating in the current
##     * clone operation. It is recommended not to hold onto these logical objects since there lifecycle is
##     * controlled by the key attributes viz. Item type, Relation type; which could be updated during this
##     * operation, resulting in redefining the logical object.
##     * 
##      <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX1980.0.0  <br> 

class PdmCopyOrEditOperationObserver(NXOpen.TaggedObjectCollection): 
    """
    * This class is responsible for invoking registered callbacks at different stages in clone operation.
    *
    * NOTE: Use callback data <ja_class>NXOpen.PDM.PdmCopyOrEditOperationCallbackData</ja_class>, which is
    * passed as input to these callback functions, to get the logical objects participating in the current
    * clone operation. It is recommended not to hold onto these logical objects since there lifecycle is
    * controlled by the key attributes viz. Item type, Relation type; which could be updated during this
    * operation, resulting in redefining the logical object.
    * 
    """


    ##  User defined Initialize callback that is called during the initialization of clone builder 
    ## A callback definition with the following input arguments: 
    ##  - @link PdmCopyOrEditOperationCallbackData NXOpen.PDM.PdmCopyOrEditOperationCallbackData@endlink
    ##  and no return type
    InitializeCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    
    
    ##  Registers a user defined Initialize callback that is called during the initialization of clone builder 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="initializeCb"> (@link PdmCopyOrEditOperationObserver.InitializeCallback NXOpen.PDM.PdmCopyOrEditOperationObserver.InitializeCallback@endlink)  method to register </param>
    def AddInitializeCallback(initializeCb: PdmCopyOrEditOperationObserver.InitializeCallback) -> int:
        """
         Registers a user defined Initialize callback that is called during the initialization of clone builder 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PostCommit callback that is called after commit of clone operation 
    ## A callback definition with the following input arguments: 
    ##  - @link PdmCopyOrEditOperationCallbackData NXOpen.PDM.PdmCopyOrEditOperationCallbackData@endlink
    ##  and no return type
    PostCommitCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    
    
    ##  Registers a user defined PostCommit callback that is called after commit of clone operation 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="postCommitCb"> (@link PdmCopyOrEditOperationObserver.PostCommitCallback NXOpen.PDM.PdmCopyOrEditOperationObserver.PostCommitCallback@endlink)  method to register </param>
    def AddPostCommitCallback(postCommitCb: PdmCopyOrEditOperationObserver.PostCommitCallback) -> int:
        """
         Registers a user defined PostCommit callback that is called after commit of clone operation 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PreAutoAssign callback that is called before auto-assigning attributes
    ##         * NOTE: You may use this callback to override the Item Type or Relation type for the part being cloned.
    ##         
    ## A callback definition with the following input arguments: 
    ##  - @link PdmCopyOrEditOperationCallbackData NXOpen.PDM.PdmCopyOrEditOperationCallbackData@endlink
    ##  and no return type
    PreAutoassignCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    
    
    ##  Registers a user defined PreAutoAssign callback that is called before auto-assigning attributes 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="preAutoassignCb"> (@link PdmCopyOrEditOperationObserver.PreAutoassignCallback NXOpen.PDM.PdmCopyOrEditOperationObserver.PreAutoassignCallback@endlink)  method to register </param>
    def AddPreAutoassignCallback(preAutoassignCb: PdmCopyOrEditOperationObserver.PreAutoassignCallback) -> int:
        """
         Registers a user defined PreAutoAssign callback that is called before auto-assigning attributes 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PreCommit callback that is called before commit of clone operation 
    ## A callback definition with the following input arguments: 
    ##  - @link PdmCopyOrEditOperationCallbackData NXOpen.PDM.PdmCopyOrEditOperationCallbackData@endlink
    ##  and no return type
    PreCommitCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    
    
    ##  Registers a user defined PreCommit callback that is called before commit of clone operation 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="preCommitCb"> (@link PdmCopyOrEditOperationObserver.PreCommitCallback NXOpen.PDM.PdmCopyOrEditOperationObserver.PreCommitCallback@endlink)  method to register </param>
    def AddPreCommitCallback(preCommitCb: PdmCopyOrEditOperationObserver.PreCommitCallback) -> int:
        """
         Registers a user defined PreCommit callback that is called before commit of clone operation 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined PreValidate callback that is called at start of validate objects of clone operation 
    ## A callback definition with the following input arguments: 
    ##  - @link PdmCopyOrEditOperationCallbackData NXOpen.PDM.PdmCopyOrEditOperationCallbackData@endlink
    ##  and no return type
    PreValidateCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    
    
    ##  Registers a user defined PreValidate callback that is called at start of validate objects of clone operation 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="preValidateCb"> (@link PdmCopyOrEditOperationObserver.PreValidateCallback NXOpen.PDM.PdmCopyOrEditOperationObserver.PreValidateCallback@endlink)  method to register </param>
    def AddPreValidateCallback(preValidateCb: PdmCopyOrEditOperationObserver.PreValidateCallback) -> int:
        """
         Registers a user defined PreValidate callback that is called at start of validate objects of clone operation 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  User defined Terminate callback that is called during the destruction of clone builder 
    ## A callback definition with the following input arguments: 
    ##  - @link PdmCopyOrEditOperationCallbackData NXOpen.PDM.PdmCopyOrEditOperationCallbackData@endlink
    ##  and no return type
    TerminateCallback = Callable[[PdmCopyOrEditOperationCallbackData], None]
    
    
    ##  Registers a user defined Terminate callback that is called during the destruction of clone builder 
    ##  @return id (int):  identifier of registered method (used to unregister the method) .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="terminateCb"> (@link PdmCopyOrEditOperationObserver.TerminateCallback NXOpen.PDM.PdmCopyOrEditOperationObserver.TerminateCallback@endlink)  method to register </param>
    def AddTerminateCallback(terminateCb: PdmCopyOrEditOperationObserver.TerminateCallback) -> int:
        """
         Registers a user defined Terminate callback that is called during the destruction of clone builder 
         @return id (int):  identifier of registered method (used to unregister the method) .
        """
        pass
    
    ##  Unregisters the user defined Initialize callback 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemoveInitializeCallback(id: int) -> None:
        """
         Unregisters the user defined Initialize callback 
        """
        pass
    
    ##  Unregisters the user defined PostCommit callback 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePostCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PostCommit callback 
        """
        pass
    
    ##  Unregisters the user defined PreAutoAssign callback 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePreAutoassignCallback(id: int) -> None:
        """
         Unregisters the user defined PreAutoAssign callback 
        """
        pass
    
    ##  Unregisters the user defined PreCommit callback 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePreCommitCallback(id: int) -> None:
        """
         Unregisters the user defined PreCommit callback 
        """
        pass
    
    ##  Unregisters the user defined PreValidate callback 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemovePreValidateCallback(id: int) -> None:
        """
         Unregisters the user defined PreValidate callback 
        """
        pass
    
    ##  Unregisters the user defined Terminate callback 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to unregister </param>
    def RemoveTerminateCallback(id: int) -> None:
        """
         Unregisters the user defined Terminate callback 
        """
        pass
    
import NXOpen
##   @brief  Contains methods for accessing PDM file data.  
## 
##   
## 
##   <br>  Created in NX11.0.0  <br> 

class PdmFile(NXOpen.TransientObject): 
    """ <summary> Contains methods for accessing PDM file data. </summary> """


    ##  Free resources associated with the instance. After this method
    ##         is called, it is illegal to use the object.  In .NET, this method
    ##         is automatically called when the object is deleted by the garbage
    ##         collector. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                is called, it is illegal to use the object.  In .NET, this method
                is automatically called when the object is deleted by the garbage
                collector. 
        """
        pass
    
    ##  Get the last modified date of a PDM file. 
    ##  @return lastModifiedDate (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetFileLastModifiedDate(self) -> str:
        """
         Get the last modified date of a PDM file. 
         @return lastModifiedDate (str): .
        """
        pass
    
    ##  Get the file name of a PDM file. 
    ##  @return fileName (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetFileName(self) -> str:
        """
         Get the file name of a PDM file. 
         @return fileName (str): .
        """
        pass
    
    ##  Get the file size of a PDM file. 
    ##  @return size (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetFileSize(self) -> str:
        """
         Get the file size of a PDM file. 
         @return size (str): .
        """
        pass
    
import NXOpen
##  Contains various PDM utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PdmManager(NXOpen.Object): 
    """ Contains various PDM utility methods """


    ##  Creates a new @link NXOpen::PDM::SearchRecipeFilterBuilder NXOpen::PDM::SearchRecipeFilterBuilder@endlink  object which supports Filtering of 
    ##         structure discovery indexed BVR assembly. 
    ##  @return builder (@link SearchRecipeFilterBuilder NXOpen.PDM.SearchRecipeFilterBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## <param name="topPart"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateBVRSearchRecipeFilterBuilder(topPart: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new @link NXOpen::PDM::SearchRecipeFilterBuilder NXOpen::PDM::SearchRecipeFilterBuilder@endlink  object which supports Filtering of 
                structure discovery indexed BVR assembly. 
         @return builder (@link SearchRecipeFilterBuilder NXOpen.PDM.SearchRecipeFilterBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::ExportWorksetForReferenceBuilder NXOpen::PDM::ExportWorksetForReferenceBuilder@endlink  object used for
    ##             exporting workset outside Teamcenter for reference. 
    ##  @return builder (@link ExportWorksetForReferenceBuilder NXOpen.PDM.ExportWorksetForReferenceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="workset"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  workset assembly to export </param>
    def CreateExportWorksetForReferenceBuilder(workset: NXOpen.BasePart) -> ExportWorksetForReferenceBuilder:
        """
         Creates a new @link NXOpen::PDM::ExportWorksetForReferenceBuilder NXOpen::PDM::ExportWorksetForReferenceBuilder@endlink  object used for
                    exporting workset outside Teamcenter for reference. 
         @return builder (@link ExportWorksetForReferenceBuilder NXOpen.PDM.ExportWorksetForReferenceBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::PartOperationMakeUniqueBuilder NXOpen::PDM::PartOperationMakeUniqueBuilder@endlink  object
    ##  @return builder (@link PartOperationMakeUniqueBuilder NXOpen.PDM.PartOperationMakeUniqueBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    def CreateMakeUniqueOperationBuilder(part: NXOpen.BasePart) -> PartOperationMakeUniqueBuilder:
        """
        Returns a new @link NXOpen::PDM::PartOperationMakeUniqueBuilder NXOpen::PDM::PartOperationMakeUniqueBuilder@endlink  object
         @return builder (@link PartOperationMakeUniqueBuilder NXOpen.PDM.PartOperationMakeUniqueBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::PartOperationAttributePropertiesBuilder NXOpen::PDM::PartOperationAttributePropertiesBuilder@endlink  object. 
    ##  @return builder (@link PartOperationAttributePropertiesBuilder NXOpen.PDM.PartOperationAttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreatePartOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> PartOperationAttributePropertiesBuilder:
        """
         Creates a new @link NXOpen::PDM::PartOperationAttributePropertiesBuilder NXOpen::PDM::PartOperationAttributePropertiesBuilder@endlink  object. 
         @return builder (@link PartOperationAttributePropertiesBuilder NXOpen.PDM.PartOperationAttributePropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
    ##  @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreatePartOperationValidationPropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
         @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
    ##  @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreatePdmCopyOrEditOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
         @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::SearchRecipeFilterBuilder NXOpen::PDM::SearchRecipeFilterBuilder@endlink  object which supports Filtering of Design Workset. 
    ##  @return builder (@link SearchRecipeFilterBuilder NXOpen.PDM.SearchRecipeFilterBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## <param name="worksetPart"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="subsetPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateSearchRecipeFilterBuilder(worksetPart: NXOpen.NXObject, subsetPartOcc: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new @link NXOpen::PDM::SearchRecipeFilterBuilder NXOpen::PDM::SearchRecipeFilterBuilder@endlink  object which supports Filtering of Design Workset. 
         @return builder (@link SearchRecipeFilterBuilder NXOpen.PDM.SearchRecipeFilterBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink  object. 
    ##  @return builder (@link VariantRulesConfigurationBuilder NXOpen.PDM.VariantRulesConfigurationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="partTag"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  The part that owns the builder. The builder owner is not
    ##                                                     strictly required (that is, it can be NULL), but it is
    ##                                                     highly suggested to ensure proper cleanup of the builder in
    ##                                                     case the client does not explicitly clean it up properly.  </param>
    def CreateVariantRulesConfigurationBuilder(partTag: NXOpen.BasePart) -> VariantRulesConfigurationBuilder:
        """
         Creates a new @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink  object. 
         @return builder (@link VariantRulesConfigurationBuilder NXOpen.PDM.VariantRulesConfigurationBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a PdmNavigatorNode 
## 
##   <br>  Created in NX6.0.4  <br> 

class PdmNavigatorNode(NXOpen.TreeListNode): 
    """ Represents a PdmNavigatorNode """


    ##  Returns the type of the PdmNavigatorNode in PDM 
    ##  @return type (str):  .
    ## 
    ##   <br>  Created in NX6.0.4  <br> 

    ## License requirements: None.
    def GetNodeType(self) -> str:
        """
         Returns the type of the PdmNavigatorNode in PDM 
         @return type (str):  .
        """
        pass
    
    ##  Returns the unique identifier of the PdmNavigatorNode in PDM 
    ##  @return uid (str):  .
    ## 
    ##   <br>  Created in NX6.0.4  <br> 

    ## License requirements: None.
    def GetUid(self) -> str:
        """
         Returns the unique identifier of the PdmNavigatorNode in PDM 
         @return uid (str):  .
        """
        pass
    
import NXOpen
##  This class serves as a gateway to part-specific tools for NX Manager mode.
##      <br> To obtain an instance of this class, refer to @link NXOpen::BasePart  NXOpen::BasePart @endlink  <br> 
## 
##   <br>  Created in NX4.0.0  <br> 

class PdmPart(NXOpen.Object): 
    """ This class serves as a gateway to part-specific tools for NX Manager mode.
    """


    ##  Reservation check-in input struct 
    ## @link PdmPartCheckinInput_Struct NXOpen.PDM.PdmPartCheckinInput_Struct@endlink is an alias for @link PdmPart.CheckinInput NXOpen.PDM.PdmPart.CheckinInput@endlink.
    class CheckinInput:
        """
         Reservation check-in input struct 
        @link PdmPartCheckinInput_Struct NXOpen.PDM.PdmPartCheckinInput_Struct@endlink is an alias for @link PdmPart.CheckinInput NXOpen.PDM.PdmPart.CheckinInput@endlink.
        """
        ## Getter for property :(bool) AllowRemote
        ## True to allow remote check in, false otherwise
        ## @return bool
        @property
        def AllowRemote(self) -> bool:
            """
            Getter for property AllowRemote
            True to allow remote check in, false otherwise

            """
            pass
        
        ## Setter for property :(bool) AllowRemote
        @AllowRemote.setter
        def AllowRemote(self, value: bool):
            """
            Getter for property AllowRemote
            True to allow remote check in, false otherwise
            Setter for property AllowRemote
            True to allow remote check in, false otherwise

            """
            pass
        
        ## Getter for property :(bool) ExplicitCheckIn
        ## True to perform explicit check in, false otherwise
        ## @return bool
        @property
        def ExplicitCheckIn(self) -> bool:
            """
            Getter for property ExplicitCheckIn
            True to perform explicit check in, false otherwise

            """
            pass
        
        ## Setter for property :(bool) ExplicitCheckIn
        @ExplicitCheckIn.setter
        def ExplicitCheckIn(self, value: bool):
            """
            Getter for property ExplicitCheckIn
            True to perform explicit check in, false otherwise
            Setter for property ExplicitCheckIn
            True to perform explicit check in, false otherwise

            """
            pass
        
        ## Getter for property :(bool) IncludeSecondary
        ## True to check out secondary dataset, false otherwise
        ## @return bool
        @property
        def IncludeSecondary(self) -> bool:
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
        
        ## Setter for property :(bool) IncludeSecondary
        @IncludeSecondary.setter
        def IncludeSecondary(self, value: bool):
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise
            Setter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
        
    
    
    ##  Reservation check-out input struct 
    ## @link PdmPartCheckoutInput_Struct NXOpen.PDM.PdmPartCheckoutInput_Struct@endlink is an alias for @link PdmPart.CheckoutInput NXOpen.PDM.PdmPart.CheckoutInput@endlink.
    class CheckoutInput:
        """
         Reservation check-out input struct 
        @link PdmPartCheckoutInput_Struct NXOpen.PDM.PdmPartCheckoutInput_Struct@endlink is an alias for @link PdmPart.CheckoutInput NXOpen.PDM.PdmPart.CheckoutInput@endlink.
        """
        ## Getter for property :(str) InputComment@return str
        @property
        def InputComment(self) -> str:
            """
            Getter for property InputComment
            """
            pass
        
        ## Setter for property :(str) InputComment
        @InputComment.setter
        def InputComment(self, value: str):
            """
            Getter for property InputCommentSetter for property InputComment
            """
            pass
        
        ## Getter for property :(str) InputChangeId@return str
        @property
        def InputChangeId(self) -> str:
            """
            Getter for property InputChangeId
            """
            pass
        
        ## Setter for property :(str) InputChangeId
        @InputChangeId.setter
        def InputChangeId(self, value: str):
            """
            Getter for property InputChangeIdSetter for property InputChangeId
            """
            pass
        
        ## Getter for property :(bool) AllowRemote
        ## True to allow remote check out, false otherwise
        ## @return bool
        @property
        def AllowRemote(self) -> bool:
            """
            Getter for property AllowRemote
            True to allow remote check out, false otherwise

            """
            pass
        
        ## Setter for property :(bool) AllowRemote
        @AllowRemote.setter
        def AllowRemote(self, value: bool):
            """
            Getter for property AllowRemote
            True to allow remote check out, false otherwise
            Setter for property AllowRemote
            True to allow remote check out, false otherwise

            """
            pass
        
        ## Getter for property :(bool) ExplicitCheckOut
        ## True to perform explicit check out, false otherwise
        ## @return bool
        @property
        def ExplicitCheckOut(self) -> bool:
            """
            Getter for property ExplicitCheckOut
            True to perform explicit check out, false otherwise

            """
            pass
        
        ## Setter for property :(bool) ExplicitCheckOut
        @ExplicitCheckOut.setter
        def ExplicitCheckOut(self, value: bool):
            """
            Getter for property ExplicitCheckOut
            True to perform explicit check out, false otherwise
            Setter for property ExplicitCheckOut
            True to perform explicit check out, false otherwise

            """
            pass
        
        ## Getter for property :(bool) IncludeSecondary
        ## True to check out secondary dataset, false otherwise
        ## @return bool
        @property
        def IncludeSecondary(self) -> bool:
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
        
        ## Setter for property :(bool) IncludeSecondary
        @IncludeSecondary.setter
        def IncludeSecondary(self, value: bool):
            """
            Getter for property IncludeSecondary
            True to check out secondary dataset, false otherwise
            Setter for property IncludeSecondary
            True to check out secondary dataset, false otherwise

            """
            pass
        
    
    
    ##  Part Expressions input struct 
    ## @link PdmPartPcaexpressionsInput_Struct NXOpen.PDM.PdmPartPcaexpressionsInput_Struct@endlink is an alias for @link PdmPart.PcaexpressionsInput NXOpen.PDM.PdmPart.PcaexpressionsInput@endlink.
    class PcaexpressionsInput:
        """
         Part Expressions input struct 
        @link PdmPartPcaexpressionsInput_Struct NXOpen.PDM.PdmPartPcaexpressionsInput_Struct@endlink is an alias for @link PdmPart.PcaexpressionsInput NXOpen.PDM.PdmPart.PcaexpressionsInput@endlink.
        """
        ## Getter for property :(str) Name
        ## Name of PCA Expression
        ## @return str
        @property
        def Name(self) -> str:
            """
            Getter for property Name
            Name of PCA Expression

            """
            pass
        
        ## Setter for property :(str) Name
        @Name.setter
        def Name(self, value: str):
            """
            Getter for property Name
            Name of PCA Expression
            Setter for property Name
            Name of PCA Expression

            """
            pass
        
        ## Getter for property :(str) Value
        ## Value of PCA Expression
        ## @return str
        @property
        def Value(self) -> str:
            """
            Getter for property Value
            Value of PCA Expression

            """
            pass
        
        ## Setter for property :(str) Value
        @Value.setter
        def Value(self, value: str):
            """
            Getter for property Value
            Value of PCA Expression
            Setter for property Value
            Value of PCA Expression

            """
            pass
        
        ## Getter for property :(str) Unit
        ## Unit of PCA Expression
        ## @return str
        @property
        def Unit(self) -> str:
            """
            Getter for property Unit
            Unit of PCA Expression

            """
            pass
        
        ## Setter for property :(str) Unit
        @Unit.setter
        def Unit(self, value: str):
            """
            Getter for property Unit
            Unit of PCA Expression
            Setter for property Unit
            Unit of PCA Expression

            """
            pass
        
        ## Getter for property :(str) SavedVariants
        ## Saved Variant Rule of PCA Expression
        ## @return str
        @property
        def SavedVariants(self) -> str:
            """
            Getter for property SavedVariants
            Saved Variant Rule of PCA Expression

            """
            pass
        
        ## Setter for property :(str) SavedVariants
        @SavedVariants.setter
        def SavedVariants(self, value: str):
            """
            Getter for property SavedVariants
            Saved Variant Rule of PCA Expression
            Setter for property SavedVariants
            Saved Variant Rule of PCA Expression

            """
            pass
        
        ## Getter for property :(str) Optionfamily
        ## Option Family of PCA Expression
        ## @return str
        @property
        def Optionfamily(self) -> str:
            """
            Getter for property Optionfamily
            Option Family of PCA Expression

            """
            pass
        
        ## Setter for property :(str) Optionfamily
        @Optionfamily.setter
        def Optionfamily(self, value: str):
            """
            Getter for property Optionfamily
            Option Family of PCA Expression
            Setter for property Optionfamily
            Option Family of PCA Expression

            """
            pass
        
        ## Getter for property :(str) OptionName
        ## This input should not be specified and is deprecated
        ## @return str
        @property
        def OptionName(self) -> str:
            """
            Getter for property OptionName
            This input should not be specified and is deprecated

            """
            pass
        
        ## Setter for property :(str) OptionName
        @OptionName.setter
        def OptionName(self, value: str):
            """
            Getter for property OptionName
            This input should not be specified and is deprecated
            Setter for property OptionName
            This input should not be specified and is deprecated

            """
            pass
        
    
    
    ##  Apply the variant expressions to the part. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pcaexpressionsInInput"> (@link PdmPart.PcaexpressionsInput List[NXOpen.PDM.PdmPart.PcaexpressionsInput]@endlink)  Input PCA Expressions which need to be applied to the part </param>
    def ApplyVariantExpressions(self, pcaexpressionsInInput: List[PdmPart.PcaexpressionsInput]) -> None:
        """
         Apply the variant expressions to the part. 
        """
        pass
    
    ##  Assign a permanent name to the temporary part 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="new_file_name"> (str)  name of new part file to create </param>
    def AssignPermanentName(self, new_file_name: str) -> None:
        """
         Assign a permanent name to the temporary part 
        """
        pass
    
    ##  Given an array of parts, check in the parts. 
    ##  @return pdmOperationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered during the checkin .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partsToCheckIn"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink)  Array of parts to check in  </param>
    ## <param name="checkInInput"> (@link PdmPart.CheckinInput NXOpen.PDM.PdmPart.CheckinInput@endlink)  Input which control the check in behavior </param>
    def CheckinParts(self, partsToCheckIn: List[NXOpen.BasePart], checkInInput: PdmPart.CheckinInput) -> OperationErrors:
        """
         Given an array of parts, check in the parts. 
         @return pdmOperationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered during the checkin .
        """
        pass
    
    ##  Checkout the part 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Checkout(self) -> None:
        """
         Checkout the part 
        """
        pass
    
    ##  Given an array of parts, check out the parts. 
    ##  @return pdmOperationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered during the checkout .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partsToCheckOut"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink)  Array of parts to check out  </param>
    ## <param name="checkOutInput"> (@link PdmPart.CheckoutInput NXOpen.PDM.PdmPart.CheckoutInput@endlink)  Input which control the check out behavior </param>
    def CheckoutParts(self, partsToCheckOut: List[NXOpen.BasePart], checkOutInput: PdmPart.CheckoutInput) -> OperationErrors:
        """
         Given an array of parts, check out the parts. 
         @return pdmOperationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered during the checkout .
        """
        pass
    
    ##  Given an array of parts, this API will remove the 'Precise Structure on Save' on all the parts 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="cancelPreciseOnSave"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink)  Array of parts to cancel precise structure on save </param>
    def ClearPreciseStructureOnSave(self, cancelPreciseOnSave: List[NXOpen.BasePart]) -> None:
        """
         Given an array of parts, this API will remove the 'Precise Structure on Save' on all the parts 
        """
        pass
    
    ##  Returns Checked out status of part and Checked out by. 
    ##  @return A tuple consisting of (isCheckedOut, checkedOutBy). 
    ##  - isCheckedOut is: bool. Checked out status of given part .
    ##  - checkedOutBy is: str. Checked out by user .

    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    def GetCheckedoutStatusAndUser(self) -> Tuple[bool, str]:
        """
         Returns Checked out status of part and Checked out by. 
         @return A tuple consisting of (isCheckedOut, checkedOutBy). 
         - isCheckedOut is: bool. Checked out status of given part .
         - checkedOutBy is: str. Checked out by user .

        """
        pass
    
    ##  Returns owner and group for part. Loads value from Teamcenter if not available with NX. 
    ##  @return A tuple consisting of (owner, group). 
    ##  - owner is: str.
    ##  - group is: str.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetOwnerAndGroup(self) -> Tuple[str, str]:
        """
         Returns owner and group for part. Loads value from Teamcenter if not available with NX. 
         @return A tuple consisting of (owner, group). 
         - owner is: str.
         - group is: str.

        """
        pass
    
    ##  Returns the assigned project names array. Project names information is retrieved from Teamcenter. Loads value from Teamcenter if not available with NX. 
    ##  @return projects (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetProjects(self) -> List[str]:
        """
         Returns the assigned project names array. Project names information is retrieved from Teamcenter. Loads value from Teamcenter if not available with NX. 
         @return projects (List[str]): .
        """
        pass
    
    ##  Get the related drawings specs of loaded part. Returns part specifications of master and non-master drawings, filtering out the diagrams 
    ##  @return relatedDrawingsCliSpecs (List[str]):  Array of part specification names for the related drawings .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetRelatedDrawingSpecs(self) -> List[str]:
        """
         Get the related drawings specs of loaded part. Returns part specifications of master and non-master drawings, filtering out the diagrams 
         @return relatedDrawingsCliSpecs (List[str]):  Array of part specification names for the related drawings .
        """
        pass
    
    ##  Get the related drawings of loaded part. Returns part specifications of master and non-master drawings 
    ##  @return relatedDrawingsCliSpecs (List[str]):  Array of part specification names for the related drawings .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def GetRelatedDrawings(self) -> List[str]:
        """
         Get the related drawings of loaded part. Returns part specifications of master and non-master drawings 
         @return relatedDrawingsCliSpecs (List[str]):  Array of part specification names for the related drawings .
        """
        pass
    
    ##  Get the related geometry representation specs of loaded part. Returns part specifications of the master and altreps, with some error handling 
    ##  @return relatedGeometryCliSpecs (List[str]):  Array of part specification names for the related geometry representation .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetRelatedGeometryRepresentationSpecs(self) -> List[str]:
        """
         Get the related geometry representation specs of loaded part. Returns part specifications of the master and altreps, with some error handling 
         @return relatedGeometryCliSpecs (List[str]):  Array of part specification names for the related geometry representation .
        """
        pass
    
    ##  Returns release status of part. Loads value from Teamcenter if not available with NX. 
    ##  @return releaseStatus (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetReleaseStatus(self) -> str:
        """
         Returns release status of part. Loads value from Teamcenter if not available with NX. 
         @return releaseStatus (str): .
        """
        pass
    
    ##  Returns true if the part is modifiable. 
    ##  @return isModifiable (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def IsModifiable(self) -> bool:
        """
         Returns true if the part is modifiable. 
         @return isModifiable (bool): .
        """
        pass
    
    ##  Given a part, get the names of the non-master types.
    ##         This function returns a list of all the non-master models of a particular model type
    ##         that are attached to a part revision.
    ##         For each possible model type, it obtains all the non-master files of a part revision.
    ##         This supports following dataset types and Allowed input strings(case-sensitive):
    ##         <ol>
    ##         <li>NX dataset types and Allowed Input String(case-sensitive)</li>
    ##         <li>NX Model Type         Allowed Input String(case-sensitive)</li>
    ##         <li>SPEC_MODEL            "specification"</li>
    ##         <li>MAN_MODEL             "manifestation"</li>
    ##         <li>ALTREP_MODEL          "altrep"</li>
    ##         <li>FOREIGN_MODEL         "multi-CAD"</li>
    ##         </ol>
    ##         Dataset types for "multi-CAD" should be defined in Teamcenter preference "TC_NX_Foreign_Datasets".
    ##         Format for multi-CAD parts should be in be of the form multi-CAD-datasettype
    ##         e.g. multi-CAD-catia
    ##         
    ##  @return nonMasterFileNames (List[str]):  Array of names of non-master files .
    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    ## 
    ## <param name="nonMasterFileType"> (str) </param>
    def ListNonMasters(self, nonMasterFileType: str) -> List[str]:
        """
         Given a part, get the names of the non-master types.
                This function returns a list of all the non-master models of a particular model type
                that are attached to a part revision.
                For each possible model type, it obtains all the non-master files of a part revision.
                This supports following dataset types and Allowed input strings(case-sensitive):
                <ol>
                <li>NX dataset types and Allowed Input String(case-sensitive)</li>
                <li>NX Model Type         Allowed Input String(case-sensitive)</li>
                <li>SPEC_MODEL            "specification"</li>
                <li>MAN_MODEL             "manifestation"</li>
                <li>ALTREP_MODEL          "altrep"</li>
                <li>FOREIGN_MODEL         "multi-CAD"</li>
                </ol>
                Dataset types for "multi-CAD" should be defined in Teamcenter preference "TC_NX_Foreign_Datasets".
                Format for multi-CAD parts should be in be of the form multi-CAD-datasettype
                e.g. multi-CAD-catia
                
         @return nonMasterFileNames (List[str]):  Array of names of non-master files .
        """
        pass
    
    ##  Create an instance of a @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink 
    ##         class that will be used to create alternate ID information on the part. 
    ##  @return alternate_id_manager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink):  the new @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink  instance .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def NewAlternateIdManager(self) -> AlternateIdManager:
        """
         Create an instance of a @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink 
                class that will be used to create alternate ID information on the part. 
         @return alternate_id_manager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink):  the new @link NXOpen::PDM::AlternateIdManager NXOpen::PDM::AlternateIdManager@endlink  instance .
        """
        pass
    
    ##  Create an instance of a @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink 
    ##         class that will be used to modify database attributes of the part. 
    ##  @return attribute_manager (@link DatabaseAttributeManager NXOpen.PDM.DatabaseAttributeManager@endlink):  the new @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink  instance .
    ## 
    ##   <br>  Created in NX5.0.0  <br> 

    ## License requirements: None.
    def NewDatabaseAttributeManager(self) -> DatabaseAttributeManager:
        """
         Create an instance of a @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink 
                class that will be used to modify database attributes of the part. 
         @return attribute_manager (@link DatabaseAttributeManager NXOpen.PDM.DatabaseAttributeManager@endlink):  the new @link NXOpen::PDM::DatabaseAttributeManager NXOpen::PDM::DatabaseAttributeManager@endlink  instance .
        """
        pass
    
    ##  Publish high-definition images for disclosed model views in the input displayed part. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="imageWidth"> (int) </param>
    ## <param name="imageHight"> (int) </param>
    def PublishHdImagesForModelViews(self, imageWidth: int, imageHight: int) -> None:
        """
         Publish high-definition images for disclosed model views in the input displayed part. 
        """
        pass
    
    ##  Set default folder for the part in which it is to be saved 
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def SetDefaultFolderForPart(self) -> None:
        """
         Set default folder for the part in which it is to be saved 
        """
        pass
    
    ##  Given an array of parts, Parts to set precise structure on save. 
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="partsToSetPreciseOnSave"> (@link NXOpen.BasePart List[NXOpen.BasePart]@endlink)  Array of parts to set precise structure on save </param>
    def SetPreciseStructureOnSave(self, partsToSetPreciseOnSave: List[NXOpen.BasePart]) -> None:
        """
         Given an array of parts, Parts to set precise structure on save. 
        """
        pass
    
import NXOpen
##  Represents search manager class  <br> Use @link NXOpen::Session::PdmSearchManager NXOpen::Session::PdmSearchManager@endlink  to get the instance of this class.  <br> 
## 
##   <br>  Created in NX6.0.0  <br> 

class PdmSearchManager(NXOpen.Object): 
    """ Represents search manager class """


    ##  Creates a new pdm search list of values
    ##  @return pdmListOfValues (@link ListOfValues NXOpen.PDM.ListOfValues@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def NewPdmListofvalues() -> ListOfValues:
        """
         Creates a new pdm search list of values
         @return pdmListOfValues (@link ListOfValues NXOpen.PDM.ListOfValues@endlink):  .
        """
        pass
    
    ##  Creates a new pdm search 
    ##  @return tcinPdmSearch (@link PdmSearch NXOpen.PDM.PdmSearch@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def NewPdmSearch() -> PdmSearch:
        """
         Creates a new pdm search 
         @return tcinPdmSearch (@link PdmSearch NXOpen.PDM.PdmSearch@endlink):  .
        """
        pass
    
    ##  Creates a new pdm search result 
    ##  @return pdmSearchResult (@link SearchResult NXOpen.PDM.SearchResult@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def NewPdmSearchresult() -> SearchResult:
        """
         Creates a new pdm search result 
         @return pdmSearchResult (@link SearchResult NXOpen.PDM.SearchResult@endlink):  .
        """
        pass
    
    ##  Creates a new pdm search soa query
    ##  @return pdmSoaQuery (@link SoaQuery NXOpen.PDM.SoaQuery@endlink):  .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX9.0.0.  This method is not useful. For NX Search use @link NXOpen::PDM::PdmSearchManager::NewPdmSearch NXOpen::PDM::PdmSearchManager::NewPdmSearch@endlink  instead  <br> 

    ## License requirements: None.
    def NewPdmSoaquery() -> SoaQuery:
        """
         Creates a new pdm search soa query
         @return pdmSoaQuery (@link SoaQuery NXOpen.PDM.SoaQuery@endlink):  .
        """
        pass
    
import NXOpen
##  Represents search query 
## 
##   <br>  Created in NX6.0.0  <br> 

class PdmSearch(NXOpen.TransientObject): 
    """ Represents search query """


    ##  This API performs advanced search in the teamcenter and returns the result vector .Internally it will execute the NX standard Queries
    ##             "__NX_STD_ANY_ITEM_QUERY","__NX_STD_ANY_REV_QUERY" and "__NX_STD_ANY_DS_QUERY". Advanced search takes in detailed inputs to perform the search. 
    ##             The parameters "entries" and "values" are the internal property names and their values to be searched.
    ##             The attribute/value pairs are combined logically using AND so that only objects matching ALL of the specified
    ##             criteria are returned.
    ##             The method can only be used to search for matches on Teamcenter properties that are string valued.
    ##             It does not work for properties which are Object/LOV valued.
    ##             For example "owning_user" is TC Object valued so the search does not find any matches when attempting to search on it.
    ##             <b>
    ##             Please note, this functionality is available starting in Teamcenter 2007.1 MP2.
    ##             To see how to spell the "real" attribute names rather than the displayed attribute (column) names,
    ##             use Edit-> Options...-> General-> UI-> Sys Admin-> Real Property Name in the Rich Client.
    ##             </b>
    ##              
    ##  @return srchResVec (@link SearchResult NXOpen.PDM.SearchResult@endlink):  search result .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="entries"> (List[str])  search criteria entries </param>
    ## <param name="values"> (List[str])  search criteria values </param>
    def Advanced(self, entries: List[str], values: List[str]) -> SearchResult:
        """
         This API performs advanced search in the teamcenter and returns the result vector .Internally it will execute the NX standard Queries
                    "__NX_STD_ANY_ITEM_QUERY","__NX_STD_ANY_REV_QUERY" and "__NX_STD_ANY_DS_QUERY". Advanced search takes in detailed inputs to perform the search. 
                    The parameters "entries" and "values" are the internal property names and their values to be searched.
                    The attribute/value pairs are combined logically using AND so that only objects matching ALL of the specified
                    criteria are returned.
                    The method can only be used to search for matches on Teamcenter properties that are string valued.
                    It does not work for properties which are Object/LOV valued.
                    For example "owning_user" is TC Object valued so the search does not find any matches when attempting to search on it.
                    <b>
                    Please note, this functionality is available starting in Teamcenter 2007.1 MP2.
                    To see how to spell the "real" attribute names rather than the displayed attribute (column) names,
                    use Edit-> Options...-> General-> UI-> Sys Admin-> Real Property Name in the Rich Client.
                    </b>
                     
         @return srchResVec (@link SearchResult NXOpen.PDM.SearchResult@endlink):  search result .
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Perform simple search in the teamcenter and returns the result vector. 
    ##             Internally it will execute the NX standard Query "__NX_STD_SIMPLE_ITEM_QUERY". 
    ##             ItemId should be given as the searchCriteria for searching the items
    ##             <b>
    ##             Please note,  this functionality is available starting in Teamcenter 2007.1 MP2.
    ##             </b>
    ##             
    ##  @return srchResVec (@link SearchResult NXOpen.PDM.SearchResult@endlink):  search result .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="searchCriteria"> (str)  search criteria as string </param>
    def Simple(self, searchCriteria: str) -> SearchResult:
        """
         Perform simple search in the teamcenter and returns the result vector. 
                    Internally it will execute the NX standard Query "__NX_STD_SIMPLE_ITEM_QUERY". 
                    ItemId should be given as the searchCriteria for searching the items
                    <b>
                    Please note,  this functionality is available starting in Teamcenter 2007.1 MP2.
                    </b>
                    
         @return srchResVec (@link SearchResult NXOpen.PDM.SearchResult@endlink):  search result .
        """
        pass
    
import NXOpen
import NXOpen.PDM.SaveManagement
##  Represents the NX Manager session  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX7.5.0  <br> 

class PdmSession(NXOpen.Object): 
    """ Represents the NX Manager session """


    ##   @brief  Input struct to get configured revision of items.  
    ## 
    ##   
    ## @link PdmSessionGetConfiguredRevisionInput_Struct NXOpen.PDM.PdmSessionGetConfiguredRevisionInput_Struct@endlink is an alias for @link PdmSession.GetConfiguredRevisionInput NXOpen.PDM.PdmSession.GetConfiguredRevisionInput@endlink.
    class GetConfiguredRevisionInput:
        """
          @brief  Input struct to get configured revision of items.  
        
          
        @link PdmSessionGetConfiguredRevisionInput_Struct NXOpen.PDM.PdmSessionGetConfiguredRevisionInput_Struct@endlink is an alias for @link PdmSession.GetConfiguredRevisionInput NXOpen.PDM.PdmSession.GetConfiguredRevisionInput@endlink.
        """
        ## Getter for property :(str) ItemId
        ## item id
        ## @return str
        @property
        def ItemId(self) -> str:
            """
            Getter for property ItemId
            item id

            """
            pass
        
        ## Setter for property :(str) ItemId
        @ItemId.setter
        def ItemId(self, value: str):
            """
            Getter for property ItemId
            item id
            Setter for property ItemId
            item id

            """
            pass
        
        ## Getter for property :(str) RevisionRuleName
        ## revision rule
        ## @return str
        @property
        def RevisionRuleName(self) -> str:
            """
            Getter for property RevisionRuleName
            revision rule

            """
            pass
        
        ## Setter for property :(str) RevisionRuleName
        @RevisionRuleName.setter
        def RevisionRuleName(self, value: str):
            """
            Getter for property RevisionRuleName
            revision rule
            Setter for property RevisionRuleName
            revision rule

            """
            pass
        
    
    
    ##   @brief  Structure to return the result of get configured revisions of items.  
    ## 
    ##   
    ## @link PdmSessionGetConfiguredRevisionResult_Struct NXOpen.PDM.PdmSessionGetConfiguredRevisionResult_Struct@endlink is an alias for @link PdmSession.GetConfiguredRevisionResult NXOpen.PDM.PdmSession.GetConfiguredRevisionResult@endlink.
    class GetConfiguredRevisionResult:
        """
          @brief  Structure to return the result of get configured revisions of items.  
        
          
        @link PdmSessionGetConfiguredRevisionResult_Struct NXOpen.PDM.PdmSessionGetConfiguredRevisionResult_Struct@endlink is an alias for @link PdmSession.GetConfiguredRevisionResult NXOpen.PDM.PdmSession.GetConfiguredRevisionResult@endlink.
        """
        ## Getter for property :(str) ItemId
        ## item id
        ## @return str
        @property
        def ItemId(self) -> str:
            """
            Getter for property ItemId
            item id

            """
            pass
        
        ## Setter for property :(str) ItemId
        @ItemId.setter
        def ItemId(self, value: str):
            """
            Getter for property ItemId
            item id
            Setter for property ItemId
            item id

            """
            pass
        
        ## Getter for property :(str) RevisionRuleName
        ## revision rule
        ## @return str
        @property
        def RevisionRuleName(self) -> str:
            """
            Getter for property RevisionRuleName
            revision rule

            """
            pass
        
        ## Setter for property :(str) RevisionRuleName
        @RevisionRuleName.setter
        def RevisionRuleName(self, value: str):
            """
            Getter for property RevisionRuleName
            revision rule
            Setter for property RevisionRuleName
            revision rule

            """
            pass
        
        ## Getter for property :(str) ItemRevisionCliSpec
        ## configured item revision cli spec
        ## @return str
        @property
        def ItemRevisionCliSpec(self) -> str:
            """
            Getter for property ItemRevisionCliSpec
            configured item revision cli spec

            """
            pass
        
        ## Setter for property :(str) ItemRevisionCliSpec
        @ItemRevisionCliSpec.setter
        def ItemRevisionCliSpec(self, value: str):
            """
            Getter for property ItemRevisionCliSpec
            configured item revision cli spec
            Setter for property ItemRevisionCliSpec
            configured item revision cli spec

            """
            pass
        
        ## Getter for property :(bool) HasFailed
        ## failed to fetch item revision using given revision rule
        ## @return bool
        @property
        def HasFailed(self) -> bool:
            """
            Getter for property HasFailed
            failed to fetch item revision using given revision rule

            """
            pass
        
        ## Setter for property :(bool) HasFailed
        @HasFailed.setter
        def HasFailed(self, value: bool):
            """
            Getter for property HasFailed
            failed to fetch item revision using given revision rule
            Setter for property HasFailed
            failed to fetch item revision using given revision rule

            """
            pass
        
    
    
    ##  Returns a collection of @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink  objects representing
    ##             attribute group types.  The collection contains attribute group descriptions for
    ##             @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink  objects loaded within the NX session.
    ##             Use the @link NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroupDescriptions NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroupDescriptions@endlink 
    ##             to get the specific attribute group descriptions for an attribute group owner.  
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## @link AttributeGroupDescriptionCollection NXOpen.PDM.AttributeGroupDescriptionCollection@endlink
    @property
    def AttributeGroupDescriptions() -> AttributeGroupDescriptionCollection:
        """
         Returns a collection of @link NXOpen::PDM::AttributeGroupDescription NXOpen::PDM::AttributeGroupDescription@endlink  objects representing
                    attribute group types.  The collection contains attribute group descriptions for
                    @link NXOpen::PDM::IAttributeGroupOwner NXOpen::PDM::IAttributeGroupOwner@endlink  objects loaded within the NX session.
                    Use the @link NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroupDescriptions NXOpen::PDM::IAttributeGroupOwner::GetAttributeGroupDescriptions@endlink 
                    to get the specific attribute group descriptions for an attribute group owner.  
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::PartOperationImportObserver NXOpen::PDM::PartOperationImportObserver@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## @link PartOperationImportObserver NXOpen.PDM.PartOperationImportObserver@endlink
    @property
    def PartOperationImportObserver() -> PartOperationImportObserver:
        """
         Returns the @link NXOpen::PDM::PartOperationImportObserver NXOpen::PDM::PartOperationImportObserver@endlink  belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::SaveManagement::SaveObserver NXOpen::PDM::SaveManagement::SaveObserver@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## @link NXOpen.PDM.SaveManagement.SaveObserver NXOpen.PDM.SaveManagement.SaveObserver@endlink
    @property
    def SaveObserver() -> NXOpen.PDM.SaveManagement.SaveObserver:
        """
         Returns the @link NXOpen::PDM::SaveManagement::SaveObserver NXOpen::PDM::SaveManagement::SaveObserver@endlink  belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::SaveAsReviseObserver NXOpen::PDM::SaveAsReviseObserver@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @link SaveAsReviseObserver NXOpen.PDM.SaveAsReviseObserver@endlink
    @property
    def SaveAsReviseObserver() -> SaveAsReviseObserver:
        """
         Returns the @link NXOpen::PDM::SaveAsReviseObserver NXOpen::PDM::SaveAsReviseObserver@endlink  belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::TcinUtils NXOpen::PDM::TcinUtils@endlink  instance belonging to this session 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @link TcinUtils NXOpen.PDM.TcinUtils@endlink
    @property
    def TcinUtils() -> TcinUtils:
        """
         Returns the @link NXOpen::PDM::TcinUtils NXOpen::PDM::TcinUtils@endlink  instance belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::PartNameGenerator NXOpen::PDM::PartNameGenerator@endlink  instance belonging to this session 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @link PartNameGenerator NXOpen.PDM.PartNameGenerator@endlink
    @property
    def PartNameGenerator() -> PartNameGenerator:
        """
         Returns the @link NXOpen::PDM::PartNameGenerator NXOpen::PDM::PartNameGenerator@endlink  instance belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::PartAttributeAssignmentObserver NXOpen::PDM::PartAttributeAssignmentObserver@endlink  instance belonging to this session 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @link PartAttributeAssignmentObserver NXOpen.PDM.PartAttributeAssignmentObserver@endlink
    @property
    def PartAttributeAssignmentObserver() -> PartAttributeAssignmentObserver:
        """
         Returns the @link NXOpen::PDM::PartAttributeAssignmentObserver NXOpen::PDM::PartAttributeAssignmentObserver@endlink  instance belonging to this session 
        """
        pass
    
    ##  Returns the @link NXOpen::PDM::PdmCopyOrEditOperationObserver NXOpen::PDM::PdmCopyOrEditOperationObserver@endlink  belonging to this session 
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @link PdmCopyOrEditOperationObserver NXOpen.PDM.PdmCopyOrEditOperationObserver@endlink
    @property
    def PdmCopyOrEditOperationObserver() -> PdmCopyOrEditOperationObserver:
        """
         Returns the @link NXOpen::PDM::PdmCopyOrEditOperationObserver NXOpen::PDM::PdmCopyOrEditOperationObserver@endlink  belonging to this session 
        """
        pass
    
    ##  Apply the given workflow on the given list of parts 
    ##  @return operationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="parts"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  the array of parts </param>
    ## <param name="workflowName"> (str) </param>
    def AssignReleaseStatus(parts: List[NXOpen.TaggedObject], workflowName: str) -> OperationErrors:
        """
         Apply the given workflow on the given list of parts 
         @return operationErrors (@link OperationErrors NXOpen.PDM.OperationErrors@endlink):  Errors encountered .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  object
    ##  @return builder (@link PartOperationCopyBuilder NXOpen.PDM.PartOperationCopyBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="operation"> (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink) </param>
    def CreateCopyOperationBuilder(operation: PartOperationBuilder.OperationType) -> PartOperationCopyBuilder:
        """
        Returns a new @link NXOpen::PDM::PartOperationCopyBuilder NXOpen::PDM::PartOperationCopyBuilder@endlink  object
         @return builder (@link PartOperationCopyBuilder NXOpen.PDM.PartOperationCopyBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  object
    ##  @return builder (@link PartOperationCreateBuilder NXOpen.PDM.PartOperationCreateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="operation"> (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink) </param>
    def CreateCreateOperationBuilder(operation: PartOperationBuilder.OperationType) -> PartOperationCreateBuilder:
        """
        Returns a new @link NXOpen::PDM::PartOperationCreateBuilder NXOpen::PDM::PartOperationCreateBuilder@endlink  object
         @return builder (@link PartOperationCreateBuilder NXOpen.PDM.PartOperationCreateBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::CreateSessionBuilder NXOpen::PDM::CreateSessionBuilder@endlink  object
    ##  @return builder (@link CreateSessionBuilder NXOpen.PDM.CreateSessionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="operation"> (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink) </param>
    def CreateCreateSessionBuilder(operation: PartOperationBuilder.OperationType) -> CreateSessionBuilder:
        """
        Returns a new @link NXOpen::PDM::CreateSessionBuilder NXOpen::PDM::CreateSessionBuilder@endlink  object
         @return builder (@link CreateSessionBuilder NXOpen.PDM.CreateSessionBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object which supports Selective Export of Configured Assembly.
    ##  @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateExportFromTeamcenterBuilderForConfiguredAssembly(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object which supports Selective Export of Configured Assembly.
         @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object which supports Selective Export of Design Workset.
    ##  @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateExportFromTeamcenterBuilderForDesignWorkset(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object which supports Selective Export of Design Workset.
         @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object
    ##  @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def CreateExportFromTeamcenterBuilderForPartFamily(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object
         @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::ExportWorksetForReferenceBuilder NXOpen::PDM::ExportWorksetForReferenceBuilder@endlink  object used for
    ##             exporting workset outside Teamcenter for reference. 
    ##  @return builder (@link ExportWorksetForReferenceBuilder NXOpen.PDM.ExportWorksetForReferenceBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::PDM::PdmManager::CreateExportWorksetForReferenceBuilder NXOpen::PDM::PdmManager::CreateExportWorksetForReferenceBuilder@endlink  instead  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="workset"> (@link NXOpen.BasePart NXOpen.BasePart@endlink)  workset assembly to export </param>
    def CreateExportWorksetForReferenceBuilder(workset: NXOpen.BasePart) -> ExportWorksetForReferenceBuilder:
        """
         Creates a new @link NXOpen::PDM::ExportWorksetForReferenceBuilder NXOpen::PDM::ExportWorksetForReferenceBuilder@endlink  object used for
                    exporting workset outside Teamcenter for reference. 
         @return builder (@link ExportWorksetForReferenceBuilder NXOpen.PDM.ExportWorksetForReferenceBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::ExternalFileReferenceListBuilder NXOpen::PDM::ExternalFileReferenceListBuilder@endlink  object. 
    ##  @return builder (@link ExternalFileReferenceListBuilder NXOpen.PDM.ExternalFileReferenceListBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreateExternalFileReferenceListBuilder(objects: List[NXOpen.NXObject]) -> ExternalFileReferenceListBuilder:
        """
         Creates a new @link NXOpen::PDM::ExternalFileReferenceListBuilder NXOpen::PDM::ExternalFileReferenceListBuilder@endlink  object. 
         @return builder (@link ExternalFileReferenceListBuilder NXOpen.PDM.ExternalFileReferenceListBuilder@endlink): .
        """
        pass
    
    ##  Create folder in Teamcenter with newFolderName under parentFolderName.
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="newFolderName"> (str)  Name of new folder to be created </param>
    ## <param name="parentFolderName"> (str)  Name of parent folder specified in form "user:[folder1:][folderN:]", if empty API will try to use default or root folder as parent </param>
    def CreateFolder(newFolderName: str, parentFolderName: str) -> None:
        """
         Create folder in Teamcenter with newFolderName under parentFolderName.
                
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::PartOperationImportBuilder NXOpen::PDM::PartOperationImportBuilder@endlink  object
    ##  @return builder (@link PartOperationImportBuilder NXOpen.PDM.PartOperationImportBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def CreateImportOperationBuilder() -> PartOperationImportBuilder:
        """
        Returns a new @link NXOpen::PDM::PartOperationImportBuilder NXOpen::PDM::PartOperationImportBuilder@endlink  object
         @return builder (@link PartOperationImportBuilder NXOpen.PDM.PartOperationImportBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::PartOperationMakeUniqueBuilder NXOpen::PDM::PartOperationMakeUniqueBuilder@endlink  object
    ##  @return builder (@link PartOperationMakeUniqueBuilder NXOpen.PDM.PartOperationMakeUniqueBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::PDM::PdmManager::CreateMakeUniqueOperationBuilder NXOpen::PDM::PdmManager::CreateMakeUniqueOperationBuilder@endlink  instead  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="part"> (@link NXOpen.BasePart NXOpen.BasePart@endlink) </param>
    def CreateMakeUniqueOperationBuilder(part: NXOpen.BasePart) -> PartOperationMakeUniqueBuilder:
        """
        Returns a new @link NXOpen::PDM::PartOperationMakeUniqueBuilder NXOpen::PDM::PartOperationMakeUniqueBuilder@endlink  object
         @return builder (@link PartOperationMakeUniqueBuilder NXOpen.PDM.PartOperationMakeUniqueBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::ObjectCreateBuilder NXOpen::PDM::ObjectCreateBuilder@endlink  object
    ##  @return builder (@link ObjectCreateBuilder NXOpen.PDM.ObjectCreateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="tcTypes"> (List[str]) </param>
    ## <param name="baseTCTypes"> (List[str]) </param>
    def CreateObjectCreateBuilder(tcTypes: List[str], baseTCTypes: List[str]) -> ObjectCreateBuilder:
        """
        Returns a new @link NXOpen::PDM::ObjectCreateBuilder NXOpen::PDM::ObjectCreateBuilder@endlink  object
         @return builder (@link ObjectCreateBuilder NXOpen.PDM.ObjectCreateBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::PartOperationBuilder NXOpen::PDM::PartOperationBuilder@endlink  object
    ##  @return builder (@link PartOperationBuilder NXOpen.PDM.PartOperationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link NXOpen::PDM::PdmSession::CreateCopyOperationBuilder NXOpen::PDM::PdmSession::CreateCopyOperationBuilder@endlink  instead  <br> 

    ## License requirements: None.
    ## <param name="operation"> (@link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink) </param>
    def CreateOperationBuilder(operation: PartOperationBuilder.OperationType) -> PartOperationBuilder:
        """
        Returns a new @link NXOpen::PDM::PartOperationBuilder NXOpen::PDM::PartOperationBuilder@endlink  object
         @return builder (@link PartOperationBuilder NXOpen.PDM.PartOperationBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::PartOperationAttributePropertiesBuilder NXOpen::PDM::PartOperationAttributePropertiesBuilder@endlink  object. 
    ##  @return builder (@link PartOperationAttributePropertiesBuilder NXOpen.PDM.PartOperationAttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::PDM::PdmManager::CreatePartOperationAttributePropertiesBuilder NXOpen::PDM::PdmManager::CreatePartOperationAttributePropertiesBuilder@endlink  instead  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreatePartOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> PartOperationAttributePropertiesBuilder:
        """
         Creates a new @link NXOpen::PDM::PartOperationAttributePropertiesBuilder NXOpen::PDM::PartOperationAttributePropertiesBuilder@endlink  object. 
         @return builder (@link PartOperationAttributePropertiesBuilder NXOpen.PDM.PartOperationAttributePropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
    ##  @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::PDM::PdmManager::CreatePartOperationValidationPropertiesBuilder NXOpen::PDM::PdmManager::CreatePartOperationValidationPropertiesBuilder@endlink  instead  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreatePartOperationValidationPropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
         @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
    ##  @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::PDM::PdmManager::CreatePdmCopyOrEditOperationAttributePropertiesBuilder NXOpen::PDM::PdmManager::CreatePdmCopyOrEditOperationAttributePropertiesBuilder@endlink  instead  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## <param name="objects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink)  the array of objects </param>
    def CreatePdmCopyOrEditOperationAttributePropertiesBuilder(objects: List[NXOpen.NXObject]) -> NXOpen.AttributePropertiesBuilder:
        """
         Creates a new @link AttributePropertiesBuilder AttributePropertiesBuilder@endlink  object. 
         @return builder (@link NXOpen.AttributePropertiesBuilder NXOpen.AttributePropertiesBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::PdmCopyOrEditOperationBuilder NXOpen::PDM::PdmCopyOrEditOperationBuilder@endlink  object
    ##  @return builder (@link PdmCopyOrEditOperationBuilder NXOpen.PDM.PdmCopyOrEditOperationBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def CreatePdmCopyOrEditOperationBuilder() -> PdmCopyOrEditOperationBuilder:
        """
        Returns a new @link NXOpen::PDM::PdmCopyOrEditOperationBuilder NXOpen::PDM::PdmCopyOrEditOperationBuilder@endlink  object
         @return builder (@link PdmCopyOrEditOperationBuilder NXOpen.PDM.PdmCopyOrEditOperationBuilder@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::SaveAsNewItemTypeBuilder NXOpen::PDM::SaveAsNewItemTypeBuilder@endlink  object
    ##  @return builder (@link SaveAsNewItemTypeBuilder NXOpen.PDM.SaveAsNewItemTypeBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def CreateSaveAsNewItemTypeBuilder() -> SaveAsNewItemTypeBuilder:
        """
        Returns a new @link NXOpen::PDM::SaveAsNewItemTypeBuilder NXOpen::PDM::SaveAsNewItemTypeBuilder@endlink  object
         @return builder (@link SaveAsNewItemTypeBuilder NXOpen.PDM.SaveAsNewItemTypeBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link NXOpen::PDM::SearchRecipeFilterBuilder NXOpen::PDM::SearchRecipeFilterBuilder@endlink  object which supports Filtering of Design Workset. 
    ##  @return builder (@link SearchRecipeFilterBuilder NXOpen.PDM.SearchRecipeFilterBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX2312.0.0.  Use @link NXOpen::PDM::PdmManager::CreateSearchRecipeFilterBuilder NXOpen::PDM::PdmManager::CreateSearchRecipeFilterBuilder@endlink  instead  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## <param name="worksetPart"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    ## <param name="subsetPartOcc"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def CreateSearchRecipeFilterBuilder(worksetPart: NXOpen.NXObject, subsetPartOcc: NXOpen.NXObject) -> SearchRecipeFilterBuilder:
        """
         Creates a new @link NXOpen::PDM::SearchRecipeFilterBuilder NXOpen::PDM::SearchRecipeFilterBuilder@endlink  object which supports Filtering of Design Workset. 
         @return builder (@link SearchRecipeFilterBuilder NXOpen.PDM.SearchRecipeFilterBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link SmartSaveBuilder SmartSaveBuilder@endlink  object. 
    ##  @return builder (@link SmartSaveBuilder NXOpen.PDM.SmartSaveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX11.0.1.  Use @link NXOpen::PDM::PdmSession::CreateSmartSaveBuilderWithContext NXOpen::PDM::PdmSession::CreateSmartSaveBuilderWithContext@endlink  instead  <br> 

    ## License requirements: None.
    ## <param name="saveType"> (@link SmartSaveBuilder.SaveType NXOpen.PDM.SmartSaveBuilder.SaveType@endlink) </param>
    def CreateSmartSaveBuilder(saveType: SmartSaveBuilder.SaveType) -> SmartSaveBuilder:
        """
         Creates a new @link SmartSaveBuilder SmartSaveBuilder@endlink  object. 
         @return builder (@link SmartSaveBuilder NXOpen.PDM.SmartSaveBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link SmartSaveBuilder SmartSaveBuilder@endlink  object. 
    ##  @return builder (@link SmartSaveBuilder NXOpen.PDM.SmartSaveBuilder@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## <param name="smartSaveContext"> (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink) </param>
    def CreateSmartSaveBuilderWithContext(smartSaveContext: SmartSaveContext) -> SmartSaveBuilder:
        """
         Creates a new @link SmartSaveBuilder SmartSaveBuilder@endlink  object. 
         @return builder (@link SmartSaveBuilder NXOpen.PDM.SmartSaveBuilder@endlink): .
        """
        pass
    
    ##  Creates a new @link SmartSaveContext SmartSaveContext@endlink  object. 
    ##  @return smartSaveContext (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink): .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## <param name="saveType"> (@link SmartSaveBuilder.SaveType NXOpen.PDM.SmartSaveBuilder.SaveType@endlink) </param>
    def CreateSmartSaveContext(saveType: SmartSaveBuilder.SaveType) -> SmartSaveContext:
        """
         Creates a new @link SmartSaveContext SmartSaveContext@endlink  object. 
         @return smartSaveContext (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink): .
        """
        pass
    
    ##  Creates a new @link SmartSaveContext SmartSaveContext@endlink  object. 
    ##  @return smartSaveContext (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink): .
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    ## <param name="dialogType"> (@link SmartSaveBuilder.DialogType NXOpen.PDM.SmartSaveBuilder.DialogType@endlink) </param>
    ## <param name="saveType"> (@link SmartSaveBuilder.SaveType NXOpen.PDM.SmartSaveBuilder.SaveType@endlink) </param>
    def CreateSmartSaveContextWithDialogType(dialogType: SmartSaveBuilder.DialogType, saveType: SmartSaveBuilder.SaveType) -> SmartSaveContext:
        """
         Creates a new @link SmartSaveContext SmartSaveContext@endlink  object. 
         @return smartSaveContext (@link SmartSaveContext NXOpen.PDM.SmartSaveContext@endlink): .
        """
        pass
    
    ## Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object
    ##  @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink) </param>
    def ExportFromTeamcenterCreate(part: NXOpen.TaggedObject) -> ExportFromTeamcenter:
        """
        Returns a new @link NXOpen::PDM::ExportFromTeamcenter NXOpen::PDM::ExportFromTeamcenter@endlink  object
         @return builder (@link ExportFromTeamcenter NXOpen.PDM.ExportFromTeamcenter@endlink): .
        """
        pass
    
    ## 
    ##            Returns the checkedout status (checkedout/non checkedout) of all the objects open in NX.
    ##         
    ##  @return A tuple consisting of (checkedOutObjects, uncheckedOutObjects). 
    ##  - checkedOutObjects is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. Array of NXObjects which are open in session and checked out .
    ##  - uncheckedOutObjects is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. Array of NXObjects which are open in session but not checkout .

    ## 
    ##   <br>  Created in NX12.0.2  <br> 

    ## License requirements: None.
    def GetCheckedoutStatusOfAllObjectsInSession() -> Tuple[List[NXOpen.NXObject], List[NXOpen.NXObject]]:
        """
        
                   Returns the checkedout status (checkedout/non checkedout) of all the objects open in NX.
                
         @return A tuple consisting of (checkedOutObjects, uncheckedOutObjects). 
         - checkedOutObjects is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. Array of NXObjects which are open in session and checked out .
         - uncheckedOutObjects is: @link NXOpen.NXObject List[NXOpen.NXObject]@endlink. Array of NXObjects which are open in session but not checkout .

        """
        pass
    
    ##  Get the configured item revisions on the provided item using given revision rule. 
    ##  @return A tuple consisting of (operationErrors, configuredItemRevisionResult). 
    ##  - operationErrors is: @link OperationErrors NXOpen.PDM.OperationErrors@endlink. Errors encountered .
    ##  - configuredItemRevisionResult is: @link PdmSession.GetConfiguredRevisionResult List[NXOpen.PDM.PdmSession.GetConfiguredRevisionResult]@endlink. Item Revision clis .

    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="itemInputs"> (@link PdmSession.GetConfiguredRevisionInput List[NXOpen.PDM.PdmSession.GetConfiguredRevisionInput]@endlink)  The parts to be imported </param>
    def GetConfiguredRevisionOfItems(itemInputs: List[PdmSession.GetConfiguredRevisionInput]) -> Tuple[OperationErrors, List[PdmSession.GetConfiguredRevisionResult]]:
        """
         Get the configured item revisions on the provided item using given revision rule. 
         @return A tuple consisting of (operationErrors, configuredItemRevisionResult). 
         - operationErrors is: @link OperationErrors NXOpen.PDM.OperationErrors@endlink. Errors encountered .
         - configuredItemRevisionResult is: @link PdmSession.GetConfiguredRevisionResult List[NXOpen.PDM.PdmSession.GetConfiguredRevisionResult]@endlink. Item Revision clis .

        """
        pass
    
    ##  Gets the @link NXOpen::PDM::DatabaseObjectManager NXOpen::PDM::DatabaseObjectManager@endlink  object. 
    ##  @return databaseObjectManager (@link DatabaseObjectManager NXOpen.PDM.DatabaseObjectManager@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetDatabaseObjectManager() -> DatabaseObjectManager:
        """
         Gets the @link NXOpen::PDM::DatabaseObjectManager NXOpen::PDM::DatabaseObjectManager@endlink  object. 
         @return databaseObjectManager (@link DatabaseObjectManager NXOpen.PDM.DatabaseObjectManager@endlink): .
        """
        pass
    
    ##  Returns array of all available Teamcenter Item Types
    ##         
    ##  @return tcItemsTypes (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetItemTypes() -> List[str]:
        """
         Returns array of all available Teamcenter Item Types
                
         @return tcItemsTypes (List[str]): .
        """
        pass
    
    ##  Get the NX workflows from Teamcenter for the given list of parts 
    ##  @return A tuple consisting of (operationErrors, workflowNames). 
    ##  - operationErrors is: @link OperationErrors NXOpen.PDM.OperationErrors@endlink. Errors encountered .
    ##  - workflowNames is: List[str]. the array of workflow names .

    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="parts"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  the array of parts </param>
    def GetNXWorkflows(parts: List[NXOpen.TaggedObject]) -> Tuple[OperationErrors, List[str]]:
        """
         Get the NX workflows from Teamcenter for the given list of parts 
         @return A tuple consisting of (operationErrors, workflowNames). 
         - operationErrors is: @link OperationErrors NXOpen.PDM.OperationErrors@endlink. Errors encountered .
         - workflowNames is: List[str]. the array of workflow names .

        """
        pass
    
    ##   Returns the SSO credentials, if SSO is available 
    ##              The client applications can use these settings to connect to the same Tcserver that NX
    ##              is using.
    ##         
    ##  @return A tuple consisting of (isSsoEnabled, ssoServerUrl, ssoAppID). 
    ##  - isSsoEnabled is: bool. if SSO is enabled .
    ##  - ssoServerUrl is: str. the SSO server URL .
    ##  - ssoAppID is: str. the SSO app id .

    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetSsoSettings() -> Tuple[bool, str, str]:
        """
          Returns the SSO credentials, if SSO is available 
                     The client applications can use these settings to connect to the same Tcserver that NX
                     is using.
                
         @return A tuple consisting of (isSsoEnabled, ssoServerUrl, ssoAppID). 
         - isSsoEnabled is: bool. if SSO is enabled .
         - ssoServerUrl is: str. the SSO server URL .
         - ssoAppID is: str. the SSO app id .

        """
        pass
    
    ##   Returns the connect string and discriminator used by NX session to connect to the Tcserver.
    ##              The client applications can use these settings to connect to the same Tcserver that NX
    ##              is using.
    ##              
    ##              Tcserver connect string: The connect string is path of the server hosting the services.
    ##              The connect string for the different transport protocols will be in the following form:
    ##              4-Tier(HTTP mode): similar to "http:
    ##              2-Tier(IIOP mode): The Tcserver IOR string; e.g corbaloc:iiop:localhost:PORTNO/localserver
    ##              2-tier(TCTP mode): the TCTP connect string; e.g "tctp:
    ##              
    ##              Discriminator: The discriminator is a unique identifier and contains unique information related 
    ##              to a given TC server. This unique identifier (discriminator) is recognized by TC pool manager as
    ##              the session number that ties the server process to the client. The discriminator functionality 
    ##              is part of the SOA package. The discriminator allows multiple clients to connect to the same TC server.
    ##              In 2-Tier(IIOP or TCTP mode), the discriminator will be an empty string.
    ## 
    ##              To connect to the same Tcserver as NX, the client can create a Teamcenter::Soa::Client::Connection 
    ##              object using the connect string and then use the Teamcenter::Services::Core::SessionService to login
    ##              to Teamcenter Server with the discriminator and the connection object. More information about
    ##              connecting to the Teamcenter server can be found in the TC SOA API Documentation.
    ## 
    ##         
    ##  @return A tuple consisting of (connectString, discriminator). 
    ##  - connectString is: str. the connection string .
    ##  - discriminator is: str. the discriminator .

    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    def GetTcserverSettings() -> Tuple[str, str]:
        """
          Returns the connect string and discriminator used by NX session to connect to the Tcserver.
                     The client applications can use these settings to connect to the same Tcserver that NX
                     is using.
                     
                     Tcserver connect string: The connect string is path of the server hosting the services.
                     The connect string for the different transport protocols will be in the following form:
                     4-Tier(HTTP mode): similar to "http:
                     2-Tier(IIOP mode): The Tcserver IOR string; e.g corbaloc:iiop:localhost:PORTNO/localserver
                     2-tier(TCTP mode): the TCTP connect string; e.g "tctp:
                     
                     Discriminator: The discriminator is a unique identifier and contains unique information related 
                     to a given TC server. This unique identifier (discriminator) is recognized by TC pool manager as
                     the session number that ties the server process to the client. The discriminator functionality 
                     is part of the SOA package. The discriminator allows multiple clients to connect to the same TC server.
                     In 2-Tier(IIOP or TCTP mode), the discriminator will be an empty string.
        
                     To connect to the same Tcserver as NX, the client can create a Teamcenter::Soa::Client::Connection 
                     object using the connect string and then use the Teamcenter::Services::Core::SessionService to login
                     to Teamcenter Server with the discriminator and the connection object. More information about
                     connecting to the Teamcenter server can be found in the TC SOA API Documentation.
        
                
         @return A tuple consisting of (connectString, discriminator). 
         - connectString is: str. the connection string .
         - discriminator is: str. the discriminator .

        """
        pass
    
    ##  Gets the Teamcenter user group for the current user
    ##         
    ##  @return userGroup (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetUserGroup() -> str:
        """
         Gets the Teamcenter user group for the current user
                
         @return userGroup (str): .
        """
        pass
    
    ##  Gets the Teamcenter user name for the current user
    ##         
    ##  @return userName (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetUserName() -> str:
        """
         Gets the Teamcenter user name for the current user
                
         @return userName (str): .
        """
        pass
    
    ##  Gets the Teamcenter role for the current user
    ##         
    ##  @return userRole (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetUserRole() -> str:
        """
         Gets the Teamcenter role for the current user
                
         @return userRole (str): .
        """
        pass
    
    ##  Returns a new @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink  object 
    ##  @return upload (@link CAEFileContainer NXOpen.PDM.CAEFileContainer@endlink): .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def NewCaeFileContainer() -> CAEFileContainer:
        """
         Returns a new @link NXOpen::PDM::CAEFileContainer NXOpen::PDM::CAEFileContainer@endlink  object 
         @return upload (@link CAEFileContainer NXOpen.PDM.CAEFileContainer@endlink): .
        """
        pass
    
    ##  Returns a new @link NXOpen::PDM::FileManagement NXOpen::PDM::FileManagement@endlink  object 
    ##  @return fileManagement (@link FileManagement NXOpen.PDM.FileManagement@endlink): .
    ## 
    ##   <br>  Created in NX7.5.4  <br> 

    ## License requirements: None.
    def NewFileManagement() -> FileManagement:
        """
         Returns a new @link NXOpen::PDM::FileManagement NXOpen::PDM::FileManagement@endlink  object 
         @return fileManagement (@link FileManagement NXOpen.PDM.FileManagement@endlink): .
        """
        pass
    
    ##  Sets active Engineering Change Notice (ECN) for the session.
    ##             All objects created will be added to solution items of this Engineering Change Notice.
    ##             The input will be in the format of Change Notice MFK ID and Change Notice Revision ID.
    ##             Note: Please make sure to set it at the start of the NXOpen program, before object creation.
    ##         
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.NXObject NXOpen.NXObject@endlink)  tag of the displayed part, can be null </param>
    ## <param name="ecnMFKId"> (str)  Change Notice MFKID to be set, can not be empty </param>
    ## <param name="ecnRevsionId"> (str)  Change Notice Revision ID to be set, can not be empty </param>
    def SetActiveEngineeringChangeNotice(part: NXOpen.NXObject, ecnMFKId: str, ecnRevsionId: str) -> None:
        """
         Sets active Engineering Change Notice (ECN) for the session.
                    All objects created will be added to solution items of this Engineering Change Notice.
                    The input will be in the format of Change Notice MFK ID and Change Notice Revision ID.
                    Note: Please make sure to set it at the start of the NXOpen program, before object creation.
                
        """
        pass
    
    ##  Sets default folder.
    ##         The input default folder path in format &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, where username is optional.
    ##         In that case, in :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container
    ##         
    ## 
    ##   <br>  Created in NX7.5.0  <br> 

    ## License requirements: None.
    ## <param name="default_folder_spec"> (str)  Default folder path including default folder name to be set </param>
    def SetDefaultFolder(default_folder_spec: str) -> None:
        """
         Sets default folder.
                The input default folder path in format &lt;username&gt;:&lt;folder&gt;:&lt;folder&gt;, where username is optional.
                In that case, in :&lt;folder&gt;:&lt;folder&gt;, the first : indicates Home, for example, :Newstuff, is the Newstuff folder in current user's Home container
                
        """
        pass
    
    ##  Sets or unsets native mode for the session based on the value of input.
    ##         
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## <param name="enable"> (bool)  flag to specify whether to set or unset native mode </param>
    ## <param name="rereadTemplateInformation"> (bool)  flag to specify whether to re-initialize managed templates </param>
    def SetNativeMode(enable: bool, rereadTemplateInformation: bool) -> None:
        """
         Sets or unsets native mode for the session based on the value of input.
                
        """
        pass
    
    ##  Set the revision rule 
    ## 
    ##   <br>  Created in NX2406.0.0  <br> 

    ## License requirements: None.
    ## <param name="setDefault"> (bool) </param>
    ## <param name="revisionRule"> (str)  The revision rule to be set </param>
    def SetRevisionRule(setDefault: bool, revisionRule: str) -> None:
        """
         Set the revision rule 
        """
        pass
    
##  NX Manager search field data type 
## <list type="table"> 
## <listheader><term> 
## Enumerator</term><description> 
## Comment</description> </listheader><item><term> 
## Char</term><description> 
##  Char type </description> </item><item><term> 
## Date</term><description> 
##  Date </description> </item><item><term> 
## Double</term><description> 
##  Double </description> </item><item><term> 
## Float</term><description> 
##  Float </description> </item><item><term> 
## Int</term><description> 
##  Integer </description> </item><item><term> 
## Bool</term><description> 
##  Boolean </description> </item><item><term> 
## Short</term><description> 
##  Short </description> </item><item><term> 
## String</term><description> 
##  String </description> </item><item><term> 
## Reference</term><description> 
##  Reference </description> </item><item><term> 
## UntypedReference</term><description> 
##  Untyped reference </description> </item><item><term> 
## ExternalReference</term><description> 
##  External reference </description> </item></list>
class PdmSoaqueryNxmgrfielddatatype(Enum):
    """
    Members Include: <Char> <Date> <Double> <Float> <Int> <Bool> <Short> <String> <Reference> <UntypedReference> <ExternalReference>
    """
    Char: int
    Date: int
    Double: int
    Float: int
    Int: int
    Bool: int
    Short: int
    String: int
    Reference: int
    UntypedReference: int
    ExternalReference: int
    ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
    ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
    @staticmethod
    def ValueOf(value: int) -> PdmSoaqueryNxmgrfielddatatype:
        """
        Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        """
        pass


import NXOpen
import NXOpen.Assemblies
##  This class is used for managing a part's pending components, that
##         is, those that have been added within Teamcenter but are not yet
##         present in NX. An instance of this class for a particular part can
##         be created by calling @link PDM::PartManager::NewPendingComponentsManager PDM::PartManager::NewPendingComponentsManager@endlink .
##     
## 
##   <br>  Created in NX4.0.1  <br> 

class PendingComponentsManager(NXOpen.TransientObject): 
    """ This class is used for managing a part's pending components, that
        is, those that have been added within Teamcenter but are not yet
        present in NX. An instance of this class for a particular part can
        be created by calling <ja_method>PDM.PartManager.NewPendingComponentsManager</ja_method>.
    """


    ##  Adds a pending component. 
    ##  @return A tuple consisting of (component, load_status). 
    ##  - component is: @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink.
    ##  - load_status is: @link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink. result of loading the component part .

    ## 
    ##   <br>  Created in NX4.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="handle"> (str)  the handle for the pending component </param>
    def AddComponent(self, handle: str) -> Tuple[NXOpen.Assemblies.Component, NXOpen.PartLoadStatus]:
        """
         Adds a pending component. 
         @return A tuple consisting of (component, load_status). 
         - component is: @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink.
         - load_status is: @link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink. result of loading the component part .

        """
        pass
    
    ##  Adds a pending NGC component. 
    ##  @return A tuple consisting of (component, load_status). 
    ##  - component is: @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink.
    ##  - load_status is: @link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink. result of loading the ngc component part .

    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="handle"> (str)  the handle for the pending ngc component </param>
    def AddNgcComponent(self, handle: str) -> Tuple[NXOpen.Assemblies.Component, NXOpen.PartLoadStatus]:
        """
         Adds a pending NGC component. 
         @return A tuple consisting of (component, load_status). 
         - component is: @link NXOpen.Assemblies.Component NXOpen.Assemblies.Component@endlink.
         - load_status is: @link NXOpen.PartLoadStatus NXOpen.PartLoadStatus@endlink. result of loading the ngc component part .

        """
        pass
    
    ##  Determines whether a given pending component has been positioned
    ##             by Teamcenter. If @link PDM::PendingComponentsManager::AddComponent PDM::PendingComponentsManager::AddComponent@endlink 
    ##             is called regarding a component without a position, it will automatically
    ##             be positioned at the origin.
    ##         
    ##  @return has_position (bool): .
    ## 
    ##   <br>  Created in NX4.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="handle"> (str)  the handle for the pending component </param>
    def ComponentHasPosition(self, handle: str) -> bool:
        """
         Determines whether a given pending component has been positioned
                    by Teamcenter. If @link PDM::PendingComponentsManager::AddComponent PDM::PendingComponentsManager::AddComponent@endlink 
                    is called regarding a component without a position, it will automatically
                    be positioned at the origin.
                
         @return has_position (bool): .
        """
        pass
    
    ##  Deletes a pending component. 
    ## 
    ##   <br>  Created in NX4.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="handle"> (str)  the handle for the pending component </param>
    def DeleteComponent(self, handle: str) -> None:
        """
         Deletes a pending component. 
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##             is called, it is illegal to use the object.  In .NET, this method
    ##             is automatically called when the object is deleted by the garbage
    ##             collector. 
    ## 
    ##   <br>  Created in NX4.0.1  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
        """
        pass
    
    ##  Gets the NX Manager file name for the part corresponding to
    ##             a pending component.
    ##         
    ##  @return file_name (str): .
    ## 
    ##   <br>  Created in NX4.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="handle"> (str)  the handle for the pending component </param>
    def GetComponentPartFileName(self, handle: str) -> str:
        """
         Gets the NX Manager file name for the part corresponding to
                    a pending component.
                
         @return file_name (str): .
        """
        pass
    
    ##  Gets "handles" for the pending components of the part associated
    ##             with this object.
    ##         
    ##  @return components (List[str]): .
    ## 
    ##   <br>  Created in NX4.0.1  <br> 

    ## License requirements: None.
    def GetComponents(self) -> List[str]:
        """
         Gets "handles" for the pending components of the part associated
                    with this object.
                
         @return components (List[str]): .
        """
        pass
    
import NXOpen
##  Persistently held settings for a Teamcenter user account. Any changes will only
##         take effect when @link PDM::PersistentSettings::Apply PDM::PersistentSettings::Apply@endlink  is callsed. 
## 
##   <br>  Created in NX4.0.0  <br> 

class PersistentSettings(NXOpen.TransientObject): 
    """ Persistently held settings for a Teamcenter user account. Any changes will only
        take effect when <ja_method>PDM.PersistentSettings.Apply</ja_method> is callsed. """


    ## Getter for property: (str) Group
    ##  Returns the Teamcenter group in which the user acts by default.  
    ##    Should be
    ##             one of those given by @link PDM::PersistentSettings::GetGroups PDM::PersistentSettings::GetGroups@endlink 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return str
    @property
    def Group(self) -> str:
        """
        Getter for property: (str) Group
         Returns the Teamcenter group in which the user acts by default.  
           Should be
                    one of those given by @link PDM::PersistentSettings::GetGroups PDM::PersistentSettings::GetGroups@endlink 
                   
         
        """
        pass
    
    ## Setter for property: (str) Group

    ##  Returns the Teamcenter group in which the user acts by default.  
    ##    Should be
    ##             one of those given by @link PDM::PersistentSettings::GetGroups PDM::PersistentSettings::GetGroups@endlink 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Group.setter
    def Group(self, group: str):
        """
        Setter for property: (str) Group
         Returns the Teamcenter group in which the user acts by default.  
           Should be
                    one of those given by @link PDM::PersistentSettings::GetGroups PDM::PersistentSettings::GetGroups@endlink 
                   
         
        """
        pass
    
    ## Getter for property: (str) Volume
    ##  Returns the Teamcenter volume to which the user used by default.  
    ##    Should be
    ##             one of those given by @link PDM::PersistentSettings::GetVolumes PDM::PersistentSettings::GetVolumes@endlink    
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return str
    @property
    def Volume(self) -> str:
        """
        Getter for property: (str) Volume
         Returns the Teamcenter volume to which the user used by default.  
           Should be
                    one of those given by @link PDM::PersistentSettings::GetVolumes PDM::PersistentSettings::GetVolumes@endlink    
         
        """
        pass
    
    ## Setter for property: (str) Volume

    ##  Returns the Teamcenter volume to which the user used by default.  
    ##    Should be
    ##             one of those given by @link PDM::PersistentSettings::GetVolumes PDM::PersistentSettings::GetVolumes@endlink    
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Volume.setter
    def Volume(self, volume: str):
        """
        Setter for property: (str) Volume
         Returns the Teamcenter volume to which the user used by default.  
           Should be
                    one of those given by @link PDM::PersistentSettings::GetVolumes PDM::PersistentSettings::GetVolumes@endlink    
         
        """
        pass
    
    ##  Applies any changes to the settings 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Apply(self) -> None:
        """
         Applies any changes to the settings 
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##             is called, it is illegal to use the object.  In .NET, this method
    ##             is automatically called when the object is deleted by the garbage
    ##             collector. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
        """
        pass
    
    ##  Gets the names of the Teamcenter groups to which the
    ##             user belongs. 
    ##         
    ##  @return groups (List[str]):  the names of the groups .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetGroups(self) -> List[str]:
        """
         Gets the names of the Teamcenter groups to which the
                    user belongs. 
                
         @return groups (List[str]):  the names of the groups .
        """
        pass
    
    ##  Gets the names of the Teamcenter volumes which the
    ##             user may use, given the current group returned by @link PDM::PersistentSettings::GetGroups PDM::PersistentSettings::GetGroups@endlink .
    ##         
    ##  @return volumes (List[str]):  the names of the volumes .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetVolumes(self) -> List[str]:
        """
         Gets the names of the Teamcenter volumes which the
                    user may use, given the current group returned by @link PDM::PersistentSettings::GetGroups PDM::PersistentSettings::GetGroups@endlink .
                
         @return volumes (List[str]):  the names of the volumes .
        """
        pass
    
import NXOpen
##  
##         Represents a base class that provides common methods for port artifact in a @link NXOpen::PDM::LogicalElementRevision NXOpen::PDM::LogicalElementRevision@endlink .
##      <br>   <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class PortArtifact(NXOpen.NXObject): 
    """ 
        Represents a base class that provides common methods for port artifact in a <ja_class>NXOpen.PDM.LogicalElementRevision</ja_class>.
    """
    pass


import NXOpen
##  
##         Represents a predefined volume object and this maps to PDM::PredefinedVolumeObject
##      <br> A PredefinedVolumeObject is obtained from an @link NXOpen::PDM::SearchRecipeFilterBuilder NXOpen::PDM::SearchRecipeFilterBuilder@endlink   <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PredefinedVolumeObject(NXOpen.NXObject): 
    """ 
        Represents a predefined volume object and this maps to PDM::PredefinedVolumeObject
    """


    ##  Returns a name representing this @link NXOpen::PDM::PredefinedVolumeObject NXOpen::PDM::PredefinedVolumeObject@endlink .
    ##         
    ##  @return volumeName (str): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    def GetVolumeName(self) -> str:
        """
         Returns a name representing this @link NXOpen::PDM::PredefinedVolumeObject NXOpen::PDM::PredefinedVolumeObject@endlink .
                
         @return volumeName (str): .
        """
        pass
    
import NXOpen
##  This is can be used to create volume search filter term.
##     * Such filter terms can be used to provide filtering.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::SearchRecipeFilterBuilder::CreatePredefinedVolumeTerm  NXOpen::PDM::SearchRecipeFilterBuilder::CreatePredefinedVolumeTerm @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class PredefinedVolumeSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create volume search filter term.
    * Such filter terms can be used to provide filtering.
    """


    ##  This function adds the predefined volume to volume term. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="volume"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def AddVolume(self, volume: NXOpen.NXObject) -> None:
        """
         This function adds the predefined volume to volume term. 
        """
        pass
    
    ##  This function gets the flag whether to inverse volume term or not. 
    ##  @return excludeToggle (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse volume term or not. 
         @return excludeToggle (bool): .
        """
        pass
    
    ##  This function gets the volume operator from volume term. 
    ##  @return volumeOperator (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetOperator(self) -> VolumeSearchFilterTerm.Operator:
        """
         This function gets the volume operator from volume term. 
         @return volumeOperator (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink): .
        """
        pass
    
    ##  This function gets the already added predefined volumes from volume term. 
    ##  @return volumes (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetVolumes(self) -> List[NXOpen.NXObject]:
        """
         This function gets the already added predefined volumes from volume term. 
         @return volumes (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  This function removes the predefined volume from volume term. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="volume"> (@link NXOpen.NXObject NXOpen.NXObject@endlink) </param>
    def RemoveVolume(self, volume: NXOpen.NXObject) -> None:
        """
         This function removes the predefined volume from volume term. 
        """
        pass
    
    ##  This function sets the flag whether to inverse volume term or not. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="excludeToggle"> (bool) </param>
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse volume term or not. 
        """
        pass
    
    ##  This function sets the volume operator to volume term. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="volumeOperator"> (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink) </param>
    def SetOperator(self, volumeOperator: VolumeSearchFilterTerm.Operator) -> None:
        """
         This function sets the volume operator to volume term. 
        """
        pass
    
import NXOpen
##  This is can be used to create proximity search filter term.
##     * Such filter terms can be used to provide filtering.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::SearchRecipeFilterBuilder::CreateProximityTerm  NXOpen::PDM::SearchRecipeFilterBuilder::CreateProximityTerm @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class ProximitySearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create proximity search filter term.
    * Such filter terms can be used to provide filtering.
    """


    ##  This function gets the distance and it's unit from proximity term. 
    ##  @return A tuple consisting of (distance, unitType). 
    ##  - distance is: float.
    ##  - unitType is: @link NXOpen.Unit NXOpen.Unit@endlink.

    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetDistance(self) -> Tuple[float, NXOpen.Unit]:
        """
         This function gets the distance and it's unit from proximity term. 
         @return A tuple consisting of (distance, unitType). 
         - distance is: float.
         - unitType is: @link NXOpen.Unit NXOpen.Unit@endlink.

        """
        pass
    
    ##  This function gets the flag whether to inverse proximity term or not. 
    ##  @return excludeToggle (bool): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse proximity term or not. 
         @return excludeToggle (bool): .
        """
        pass
    
    ##  This function gets the targets from proximity term. 
    ##  @return targets (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetTargets(self) -> List[NXOpen.NXObject]:
        """
         This function gets the targets from proximity term. 
         @return targets (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  This function sets the distance and it's unit to proximity term. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="distance"> (float) </param>
    ## <param name="unitType"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    def SetDistance(self, distance: float, unitType: NXOpen.Unit) -> None:
        """
         This function sets the distance and it's unit to proximity term. 
        """
        pass
    
    ##  This function sets the flag whether to inverse proximity term or not. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="excludeToggle"> (bool) </param>
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse proximity term or not. 
        """
        pass
    
    ##  This function sets the targets to proximity term. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="targets"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def SetTargets(self, targets: List[NXOpen.NXObject]) -> None:
        """
         This function sets the targets to proximity term. 
        """
        pass
    
import NXOpen
##  Collection of PDM utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX6.0.3  <br> 

class RequirementUtils(NXOpen.Object): 
    """ Collection of PDM utility methods """


    ##  Creates Trace Links from @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink s to @link NXOpen::Part NXOpen::Part@endlink s
    ##         For the input requirement_item_numbers:
    ##         In case of Default Domain: it is Teamcenter item ID.
    ##         In case of non-Default Domain: it is the multifield key.
    ##         e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         And the encoded part filename would be containing the MFK.
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="requirement_item_numbers"> (List[str])  requirement multifield key </param>
    ## <param name="requirement_revisions"> (List[str])  requirement item revisions. Must be same size as the item number array </param>
    ## <param name="parts"> (List[str])  part CLI names </param>
    def CreateTraceLinks(requirement_item_numbers: List[str], requirement_revisions: List[str], parts: List[str]) -> None:
        """
         Creates Trace Links from @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink s to @link NXOpen::Part NXOpen::Part@endlink s
                For the input requirement_item_numbers:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
        """
        pass
    
    ##  Returns a Tracelink query object 
    ##  @return tracelink_query (@link TracelinkQuery NXOpen.PDM.TracelinkQuery@endlink):   .
    ## 
    ##   <br>  Created in NX6.0.3  <br> 

    ## License requirements: None.
    def NewTracelinkQuery() -> TracelinkQuery:
        """
         Returns a Tracelink query object 
         @return tracelink_query (@link TracelinkQuery NXOpen.PDM.TracelinkQuery@endlink):   .
        """
        pass
    
    ##  Removes Trace Links between @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink s and @link NXOpen::Part NXOpen::Part@endlink s
    ##         For the input requirement_item_numbers:
    ##         In case of Default Domain: it is Teamcenter item ID.
    ##         In case of non-Default Domain: it is the multifield key.
    ##         e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         And the encoded part filename would be containing the MFK.
    ##         
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    ## <param name="requirement_item_numbers"> (List[str])  requirement multifield Key </param>
    ## <param name="requirement_revisions"> (List[str])  requirement item revisions. Must be same size as the item number array </param>
    ## <param name="parts"> (List[str])  part CLI names </param>
    def RemoveTraceLinks(requirement_item_numbers: List[str], requirement_revisions: List[str], parts: List[str]) -> None:
        """
         Removes Trace Links between @link NXOpen::Validate::Requirement NXOpen::Validate::Requirement@endlink s and @link NXOpen::Part NXOpen::Part@endlink s
                For the input requirement_item_numbers:
                In case of Default Domain: it is Teamcenter item ID.
                In case of non-Default Domain: it is the multifield key.
                e.g.  %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                And the encoded part filename would be containing the MFK.
                
        """
        pass
    
##  Represents a builder class that performs save as new item type operation  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateSaveAsNewItemTypeBuilder  NXOpen::PDM::PdmSession::CreateSaveAsNewItemTypeBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## DefaultAction </term> <description> 
##  
## Clone </description> </item> 
## 
## <item><term> 
##  
## NumberingSource </term> <description> 
##  
## AutoGenerate </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2312.0.0  <br> 

class SaveAsNewItemTypeBuilder(PdmCopyOrEditOperationBuilder): 
    """ Represents a builder class that performs save as new item type operation """


    ## Getter for property: (int) DependentFilesToCopyOption
    ##  Returns the Dependent files Save As option.  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## @return int
    @property
    def DependentFilesToCopyOption(self) -> int:
        """
        Getter for property: (int) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
            
         
        """
        pass
    
    ## Setter for property: (int) DependentFilesToCopyOption

    ##  Returns the Dependent files Save As option.  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    @DependentFilesToCopyOption.setter
    def DependentFilesToCopyOption(self, saveAsOption: int):
        """
        Setter for property: (int) DependentFilesToCopyOption
         Returns the Dependent files Save As option.  
            
         
        """
        pass
    
    ##  Adds the selected parts.
    ##  @return errorMsgs (List[str]): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="parts"> (List[str]) </param>
    def AddSelectedParts(self, parts: List[str]) -> List[str]:
        """
         Adds the selected parts.
         @return errorMsgs (List[str]): .
        """
        pass
    
    ##  This function creates/updates the operation objects for the participating parts.
    ##         Note: The operation object needs to be updated in certain cases, e.g. after the item type is changed.
    ##         
    ##  @return copyOperationObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="doUpdate"> (bool) </param>
    def CreateOrUpdateSaveAsNewItemTypeOperationObjects(self, doUpdate: bool) -> List[PdmCopyOrEditOperationObject]:
        """
         This function creates/updates the operation objects for the participating parts.
                Note: The operation object needs to be updated in certain cases, e.g. after the item type is changed.
                
         @return copyOperationObjects (@link PdmCopyOrEditOperationObject List[NXOpen.PDM.PdmCopyOrEditOperationObject]@endlink): .
        """
        pass
    
    ##  Sets the Engineering Change Notice for the parts undergoing save-as new item type operation
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="ecnCliSpec"> (str)  CLI specification of the Engineering Change Notice </param>
    def SetChangeNotice(self, ecnCliSpec: str) -> None:
        """
         Sets the Engineering Change Notice for the parts undergoing save-as new item type operation
        """
        pass
    
    ##  Sets the selected Item Type 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="itemType"> (str) </param>
    def SetItemType(self, itemType: str) -> None:
        """
         Sets the selected Item Type 
        """
        pass
    
import NXOpen
##  JA interface for SaveAsReviseCallbackData object  <br> This cannot be created  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SaveAsReviseCallbackData(NXOpen.TaggedObject): 
    """ JA interface for SaveAsReviseCallbackData object """


    ##  Gets the source objects tags along with copied objects tags after saveas or revise operation 
    ##  @return copiedObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  array of copied objects to be saveas or revise .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="sourceObjects"> (@link NXOpen.TaggedObject NXOpen.TaggedObject@endlink)  tag of source object for which copied objects are required </param>
    def GetCopiedObjects(self, sourceObjects: NXOpen.TaggedObject) -> List[NXOpen.TaggedObject]:
        """
         Gets the source objects tags along with copied objects tags after saveas or revise operation 
         @return copiedObjects (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink):  array of copied objects to be saveas or revise .
        """
        pass
    
    ##  Gets the source objects tags participating in saveas or revise operation 
    ##  @return A tuple consisting of (nObjects, sourceObjects). 
    ##  - nObjects is: int. get number of source objects going for SaveAs or Revise .
    ##  - sourceObjects is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink. array of source objects to be saveas or revise .

    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetSourceObjects(self) -> Tuple[int, List[NXOpen.TaggedObject]]:
        """
         Gets the source objects tags participating in saveas or revise operation 
         @return A tuple consisting of (nObjects, sourceObjects). 
         - nObjects is: int. get number of source objects going for SaveAs or Revise .
         - sourceObjects is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink. array of source objects to be saveas or revise .

        """
        pass
    
import NXOpen
##  This class is responsible for invoking registered callback when objects goes for SaveAs and Revise and after the process.  <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SaveAsReviseObserver(NXOpen.TaggedObjectCollection): 
    """ This class is responsible for invoking registered callback when objects goes for SaveAs and Revise and after the process. """


    ##  User defined postcopyoperation callback that is called after SaveAs and Revise process
    ## A callback definition with the following input arguments: 
    ##  - @link SaveAsReviseCallbackData NXOpen.PDM.SaveAsReviseCallbackData@endlink
    ##  and no return type
    PostcopyoperationCb = Callable[[SaveAsReviseCallbackData], None]
    
    
    ##  Registers a user defined postcopyoperation callback that is called just before SaveAs and Revise process 
    ##  @return id (int):  identifier of registered method (used to deregister the method) .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="postcopyoperation_cb"> (@link SaveAsReviseObserver.PostcopyoperationCb NXOpen.PDM.SaveAsReviseObserver.PostcopyoperationCb@endlink)  method to register </param>
    def AddPostcopyoperationCallback(postcopyoperation_cb: SaveAsReviseObserver.PostcopyoperationCb) -> int:
        """
         Registers a user defined postcopyoperation callback that is called just before SaveAs and Revise process 
         @return id (int):  identifier of registered method (used to deregister the method) .
        """
        pass
    
    ##  User defined precopyoperation callback that is called just before SaveAs and Revise process
    ## A callback definition with the following input arguments: 
    ##  - @link SaveAsReviseCallbackData NXOpen.PDM.SaveAsReviseCallbackData@endlink
    ##  and no return type
    PrecopyoperationCb = Callable[[SaveAsReviseCallbackData], None]
    
    
    ##  Registers a user defined precopyoperation callback that is called just before SaveAs and Revise process 
    ##  @return id (int):  identifier of registered method (used to deregister the method) .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## <param name="precopyoperation_cb"> (@link SaveAsReviseObserver.PrecopyoperationCb NXOpen.PDM.SaveAsReviseObserver.PrecopyoperationCb@endlink)  method to register </param>
    def AddPrecopyoperationCallback(precopyoperation_cb: SaveAsReviseObserver.PrecopyoperationCb) -> int:
        """
         Registers a user defined precopyoperation callback that is called just before SaveAs and Revise process 
         @return id (int):  identifier of registered method (used to deregister the method) .
        """
        pass
    
    ##  Deregister the user defined postcopyoperation callback 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to deregister </param>
    def RemovePostcopyoperationCallback(id: int) -> None:
        """
         Deregister the user defined postcopyoperation callback 
        """
        pass
    
    ##  Deregister the user defined precopyoperation callback 
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    ## <param name="id"> (int)  identifier for method to deregister </param>
    def RemovePrecopyoperationCallback(id: int) -> None:
        """
         Deregister the user defined precopyoperation callback 
        """
        pass
    
import NXOpen
##  This is search filter term which can be used to create recipe filter.
##     *   Collections of such filter terms will be used provide filtering.
##      <br> This is an abstract class, and cannot be instantiated  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SearchFilterTerm(NXOpen.NXObject): 
    """ This is search filter term which can be used to create recipe filter.
    *   Collections of such filter terms will be used provide filtering.
    """


    ##  This enum is used to specify the type of search filter term. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Proximity</term><description> 
    ## </description> </item><item><term> 
    ## Volume</term><description> 
    ## </description> </item><item><term> 
    ## Invalid</term><description> 
    ## </description> </item><item><term> 
    ## Partition</term><description> 
    ## </description> </item><item><term> 
    ## Attribute</term><description> 
    ## </description> </item></list>
    class Type(Enum):
        """
        Members Include: <Proximity> <Volume> <Invalid> <Partition> <Attribute>
        """
        Proximity: int
        Volume: int
        Invalid: int
        Partition: int
        Attribute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SearchFilterTerm.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This function returns type of search filter term. 
    ##  @return type (@link SearchFilterTerm.Type NXOpen.PDM.SearchFilterTerm.Type@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetTermType(self) -> SearchFilterTerm.Type:
        """
         This function returns type of search filter term. 
         @return type (@link SearchFilterTerm.Type NXOpen.PDM.SearchFilterTerm.Type@endlink): .
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Represents a builder class that performs search filtering  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmManager::CreateBVRSearchRecipeFilterBuilder  NXOpen::PDM::PdmManager::CreateBVRSearchRecipeFilterBuilder @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class SearchRecipeFilterBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs search filtering """


    ##  This enum is used to specify the recipe logic. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Include</term><description> 
    ## </description> </item><item><term> 
    ## Exclude</term><description> 
    ## </description> </item></list>
    class RecipeLogicValue(Enum):
        """
        Members Include: <Include> <Exclude>
        """
        Include: int
        Exclude: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SearchRecipeFilterBuilder.RecipeLogicValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum is used to specify the volume type. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Reference</term><description> 
    ## </description> </item><item><term> 
    ## PreDefined</term><description> 
    ## </description> </item><item><term> 
    ## New</term><description> 
    ## </description> </item></list>
    class VolumeTypeValue(Enum):
        """
        Members Include: <Reference> <PreDefined> <New>
        """
        Reference: int
        PreDefined: int
        New: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SearchRecipeFilterBuilder.VolumeTypeValue:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This function creates the attribute type search filter term based on the provided attribute values. 
    ##  @return createdTerm (@link AttributeSearchFilterTerm NXOpen.PDM.AttributeSearchFilterTerm@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="objectType"> (str) </param>
    ## <param name="operatorValue"> (str) </param>
    ## <param name="internalTitle"> (str) </param>
    ## <param name="displayTitle"> (str) </param>
    ## <param name="doExclude"> (bool) </param>
    def CreateAttributeTerm(self, objectType: str, operatorValue: str, internalTitle: str, displayTitle: str, doExclude: bool) -> AttributeSearchFilterTerm:
        """
         This function creates the attribute type search filter term based on the provided attribute values. 
         @return createdTerm (@link AttributeSearchFilterTerm NXOpen.PDM.AttributeSearchFilterTerm@endlink): .
        """
        pass
    
    ##  This function creates the partition type search filter term based on the provided partitions.
    ##             All the provided partitions are expected to be of same partition scheme. 
    ##  @return createdTerm (@link PartitionSearchFilterTerm NXOpen.PDM.PartitionSearchFilterTerm@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="partitionScheme"> (@link NXOpen.Assemblies.PartitionScheme NXOpen.Assemblies.PartitionScheme@endlink) </param>
    ## <param name="partition"> (@link NXOpen.Assemblies.Partition List[NXOpen.Assemblies.Partition]@endlink) </param>
    ## <param name="includeChildrenPartition"> (bool) </param>
    ## <param name="doExclude"> (bool) </param>
    def CreatePartitionTerm(self, partitionScheme: NXOpen.Assemblies.PartitionScheme, partition: List[NXOpen.Assemblies.Partition], includeChildrenPartition: bool, doExclude: bool) -> PartitionSearchFilterTerm:
        """
         This function creates the partition type search filter term based on the provided partitions.
                    All the provided partitions are expected to be of same partition scheme. 
         @return createdTerm (@link PartitionSearchFilterTerm NXOpen.PDM.PartitionSearchFilterTerm@endlink): .
        """
        pass
    
    ##  This function creates the volume type search filter term based on the predefined volumes. 
    ##  @return createdTerm (@link PredefinedVolumeSearchFilterTerm NXOpen.PDM.PredefinedVolumeSearchFilterTerm@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="volumes"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="volumeOperator"> (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink) </param>
    ## <param name="doExclude"> (bool) </param>
    def CreatePredefinedVolumeTerm(self, volumes: List[NXOpen.NXObject], volumeOperator: VolumeSearchFilterTerm.Operator, doExclude: bool) -> PredefinedVolumeSearchFilterTerm:
        """
         This function creates the volume type search filter term based on the predefined volumes. 
         @return createdTerm (@link PredefinedVolumeSearchFilterTerm NXOpen.PDM.PredefinedVolumeSearchFilterTerm@endlink): .
        """
        pass
    
    ##  This function creates the proximity type search filter term based on the provided values. 
    ##  @return createdTerm (@link ProximitySearchFilterTerm NXOpen.PDM.ProximitySearchFilterTerm@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="targets"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="distance"> (float) </param>
    ## <param name="unitType"> (@link NXOpen.Unit NXOpen.Unit@endlink) </param>
    ## <param name="doExclude"> (bool) </param>
    def CreateProximityTerm(self, targets: List[NXOpen.NXObject], distance: float, unitType: NXOpen.Unit, doExclude: bool) -> ProximitySearchFilterTerm:
        """
         This function creates the proximity type search filter term based on the provided values. 
         @return createdTerm (@link ProximitySearchFilterTerm NXOpen.PDM.ProximitySearchFilterTerm@endlink): .
        """
        pass
    
    ##  This function creates the volume type search filter term based on the provided values. 
    ##  @return createdTerm (@link VolumeSearchFilterTerm NXOpen.PDM.VolumeSearchFilterTerm@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="boundingBoxes"> (@link VolumeSearchFilterTerm.BoundingBox List[NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox]@endlink) </param>
    ## <param name="boxZoneOperator"> (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink) </param>
    ## <param name="doExclude"> (bool) </param>
    def CreateVolumeTerm(self, boundingBoxes: List[VolumeSearchFilterTerm.BoundingBox], boxZoneOperator: VolumeSearchFilterTerm.Operator, doExclude: bool) -> VolumeSearchFilterTerm:
        """
         This function creates the volume type search filter term based on the provided values. 
         @return createdTerm (@link VolumeSearchFilterTerm NXOpen.PDM.VolumeSearchFilterTerm@endlink): .
        """
        pass
    
    ##  This function creates the volume type search filter term based on the provided objects. 
    ##  @return createdTerm (@link SelectedVolumeSearchFilterTerm NXOpen.PDM.SelectedVolumeSearchFilterTerm@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="selectedObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    ## <param name="volumeOperator"> (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink) </param>
    ## <param name="doExclude"> (bool) </param>
    def CreateVolumeTermFromSelectedObjects(self, selectedObjects: List[NXOpen.NXObject], volumeOperator: VolumeSearchFilterTerm.Operator, doExclude: bool) -> SelectedVolumeSearchFilterTerm:
        """
         This function creates the volume type search filter term based on the provided objects. 
         @return createdTerm (@link SelectedVolumeSearchFilterTerm NXOpen.PDM.SelectedVolumeSearchFilterTerm@endlink): .
        """
        pass
    
    ##  This function deletes the provided search filter term. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="termToDelete"> (@link SearchFilterTerm NXOpen.PDM.SearchFilterTerm@endlink) </param>
    def DeleteSearchFilterTerm(self, termToDelete: SearchFilterTerm) -> None:
        """
         This function deletes the provided search filter term. 
        """
        pass
    
    ##  This function gets all the predefined volumes. 
    ##  @return predefinedVolumes (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    def GetPredefinedVolumes(self) -> List[NXOpen.NXObject]:
        """
         This function gets all the predefined volumes. 
         @return predefinedVolumes (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  This function gets all the search filter terms.
    ##             It includes already created search terms which are based on existing filter of ProductSubset.
    ##             It also includes search terms created using "CreateProximityTerm" and "CreateVolumeTerm". 
    ##  @return terms (@link SearchFilterTerm List[NXOpen.PDM.SearchFilterTerm]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    def GetSearchFilterTerms(self) -> List[SearchFilterTerm]:
        """
         This function gets all the search filter terms.
                    It includes already created search terms which are based on existing filter of ProductSubset.
                    It also includes search terms created using "CreateProximityTerm" and "CreateVolumeTerm". 
         @return terms (@link SearchFilterTerm List[NXOpen.PDM.SearchFilterTerm]@endlink): .
        """
        pass
    
    ##  This function loads all the partitions from every partition schemes available on server. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    def LoadPartitions(self) -> None:
        """
         This function loads all the partitions from every partition schemes available on server. 
        """
        pass
    
    ##  This function loads all the predefined volumes from server. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    def LoadPredefinedVolumes(self) -> None:
        """
         This function loads all the predefined volumes from server. 
        """
        pass
    
import NXOpen
##  Represents search query 
## 
##   <br>  Created in NX6.0.0  <br> 

class SearchResult(NXOpen.TransientObject): 
    """ Represents search query """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets a list of the item_ids from the search result. If Multifield Key environment is enabled, 
    ##         then use Multifield key function @link PDM::SearchResult::GetResultMfkIds PDM::SearchResult::GetResultMfkIds@endlink , as 
    ##         this function may return us duplicate item ids if the corresponding parts belong to different domains. 
    ##  @return itemIds (List[str]):  array of item_ids .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX10.0.0.  Use @link PDM::SearchResult::GetResultMfkIds PDM::SearchResult::GetResultMfkIds@endlink  instead.  <br> 

    ## License requirements: None.
    def GetResultItemIds(self) -> List[str]:
        """
         Gets a list of the item_ids from the search result. If Multifield Key environment is enabled, 
                then use Multifield key function @link PDM::SearchResult::GetResultMfkIds PDM::SearchResult::GetResultMfkIds@endlink , as 
                this function may return us duplicate item ids if the corresponding parts belong to different domains. 
         @return itemIds (List[str]):  array of item_ids .
        """
        pass
    
    ##  Gets a list of the Multifield Keys from the search results. If Multifield Key
    ##         environment is enabled then always use this function 
    ##         Multifield Key: e.g. %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x 
    ##  @return mfkIds (List[str]):  array of mfk_ids .
    ## 
    ##   <br>  Created in NX10.0.0  <br> 

    ## License requirements: None.
    def GetResultMfkIds(self) -> List[str]:
        """
         Gets a list of the Multifield Keys from the search results. If Multifield Key
                environment is enabled then always use this function 
                Multifield Key: e.g. %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x 
         @return mfkIds (List[str]):  array of mfk_ids .
        """
        pass
    
    ##  Gets a list of the object names from the search result 
    ##  @return objectNames (List[str]):  array of object names .
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def GetResultObjectNames(self) -> List[str]:
        """
         Gets a list of the object names from the search result 
         @return objectNames (List[str]):  array of object names .
        """
        pass
    
    ##  Gets a list of the object types from the search result 
    ##  @return objectTypes (List[str]):  array of object types .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetResultObjectTypes(self) -> List[str]:
        """
         Gets a list of the object types from the search result 
         @return objectTypes (List[str]):  array of object types .
        """
        pass
    
import NXOpen
##  This is can be used to create volume search filter term using objects.
##     * Such filter terms can be used to provide filtering.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::SearchRecipeFilterBuilder::CreateVolumeTermFromSelectedObjects  NXOpen::PDM::SearchRecipeFilterBuilder::CreateVolumeTermFromSelectedObjects @endlink  <br> 
## 
##   <br>  Created in NX2312.0.0  <br> 

class SelectedVolumeSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create volume search filter term using objects.
    * Such filter terms can be used to provide filtering.
    """


    ##  This function gets the bounding boxes from volume term. 
    ##  @return boundingBox (@link VolumeSearchFilterTerm.BoundingBox NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetBoundingBox(self) -> VolumeSearchFilterTerm.BoundingBox:
        """
         This function gets the bounding boxes from volume term. 
         @return boundingBox (@link VolumeSearchFilterTerm.BoundingBox NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox@endlink): .
        """
        pass
    
    ##  This function gets the flag whether to inverse volume term or not. 
    ##  @return excludeToggle (bool): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse volume term or not. 
         @return excludeToggle (bool): .
        """
        pass
    
    ##  This function gets the bounding box operator from volume term. 
    ##  @return volumeOperator (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetOperator(self) -> VolumeSearchFilterTerm.Operator:
        """
         This function gets the bounding box operator from volume term. 
         @return volumeOperator (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink): .
        """
        pass
    
    ##  This function gets the selected objects from volume term. 
    ##  @return selectedObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: None.
    def GetSelectedObjects(self) -> List[NXOpen.NXObject]:
        """
         This function gets the selected objects from volume term. 
         @return selectedObjects (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink): .
        """
        pass
    
    ##  This function sets the bounding boxes to volume term. It will overwrite bounding box computed earlier from selected objects. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="boundingBox"> (@link VolumeSearchFilterTerm.BoundingBox NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox@endlink) </param>
    def SetBoundingBox(self, boundingBox: VolumeSearchFilterTerm.BoundingBox) -> None:
        """
         This function sets the bounding boxes to volume term. It will overwrite bounding box computed earlier from selected objects. 
        """
        pass
    
    ##  This function sets the flag whether to inverse volume term or not. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="excludeToggle"> (bool) </param>
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse volume term or not. 
        """
        pass
    
    ##  This function sets the bounding box operator to volume term. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="volumeOperator"> (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink) </param>
    def SetOperator(self, volumeOperator: VolumeSearchFilterTerm.Operator) -> None:
        """
         This function sets the bounding box operator to volume term. 
        """
        pass
    
    ##  This function sets the selected object to volume term. It also recomputes bounding box based on provided objects. 
    ## 
    ##   <br>  Created in NX2312.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="selectedObjects"> (@link NXOpen.NXObject List[NXOpen.NXObject]@endlink) </param>
    def SetSelectedObjects(self, selectedObjects: List[NXOpen.NXObject]) -> None:
        """
         This function sets the selected object to volume term. It also recomputes bounding box based on provided objects. 
        """
        pass
    
import NXOpen
##  To obtain an instance of this class, refer to @link NXOpen::Session::NewDatabaseSessionOptions NXOpen::Session::NewDatabaseSessionOptions@endlink  
##         Values for the settings that affect the current Teamcenter session. Any changes will only
##         take effect when @link PDM::SessionSettings::Apply PDM::SessionSettings::Apply@endlink  is callsed. 
## 
##   <br>  Created in NX4.0.0  <br> 

class SessionSettings(NXOpen.TransientObject): 
    """ To obtain an instance of this class, refer to <ja_method>NXOpen.Session.NewDatabaseSessionOptions</ja_method> 
        Values for the settings that affect the current Teamcenter session. Any changes will only
        take effect when <ja_method>PDM.SessionSettings.Apply</ja_method> is callsed. """


    ## Getter for property: (bool) AdministrationBypass
    ##  Returns a flag controlling the Teamcenter administrator's bypass option.  
    ##    Only available to administrators.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def AdministrationBypass(self) -> bool:
        """
        Getter for property: (bool) AdministrationBypass
         Returns a flag controlling the Teamcenter administrator's bypass option.  
           Only available to administrators.   
         
        """
        pass
    
    ## Setter for property: (bool) AdministrationBypass

    ##  Returns a flag controlling the Teamcenter administrator's bypass option.  
    ##    Only available to administrators.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @AdministrationBypass.setter
    def AdministrationBypass(self, admin_bypass_on: bool):
        """
        Setter for property: (bool) AdministrationBypass
         Returns a flag controlling the Teamcenter administrator's bypass option.  
           Only available to administrators.   
         
        """
        pass
    
    ## Getter for property: (bool) AdministrationLogging
    ##  Returns a flag controlling Teamcenter administration logging.  
    ##    Only available to administrators.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def AdministrationLogging(self) -> bool:
        """
        Getter for property: (bool) AdministrationLogging
         Returns a flag controlling Teamcenter administration logging.  
           Only available to administrators.   
         
        """
        pass
    
    ## Setter for property: (bool) AdministrationLogging

    ##  Returns a flag controlling Teamcenter administration logging.  
    ##    Only available to administrators.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @AdministrationLogging.setter
    def AdministrationLogging(self, admin_logging_on: bool):
        """
        Setter for property: (bool) AdministrationLogging
         Returns a flag controlling Teamcenter administration logging.  
           Only available to administrators.   
         
        """
        pass
    
    ## Getter for property: (bool) ApplicationLogging
    ##  Returns a flag controlling Teamcenter application logging   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def ApplicationLogging(self) -> bool:
        """
        Getter for property: (bool) ApplicationLogging
         Returns a flag controlling Teamcenter application logging   
            
         
        """
        pass
    
    ## Setter for property: (bool) ApplicationLogging

    ##  Returns a flag controlling Teamcenter application logging   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @ApplicationLogging.setter
    def ApplicationLogging(self, app_logging_on: bool):
        """
        Setter for property: (bool) ApplicationLogging
         Returns a flag controlling Teamcenter application logging   
            
         
        """
        pass
    
    ## Getter for property: (str) Group
    ##  Returns the Teamcenter group in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetGroups PDM::SessionSettings::GetGroups@endlink 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return str
    @property
    def Group(self) -> str:
        """
        Getter for property: (str) Group
         Returns the Teamcenter group in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetGroups PDM::SessionSettings::GetGroups@endlink 
                   
         
        """
        pass
    
    ## Setter for property: (str) Group

    ##  Returns the Teamcenter group in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetGroups PDM::SessionSettings::GetGroups@endlink 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Group.setter
    def Group(self, group: str):
        """
        Setter for property: (str) Group
         Returns the Teamcenter group in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetGroups PDM::SessionSettings::GetGroups@endlink 
                   
         
        """
        pass
    
    ## Getter for property: (bool) IsAdministrator
    ##  Returns a flag indicating if the user has Teamcenter administator privileges.  
    ##    Some
    ##             settings can are only available to administrators, and will raise errors
    ##             if non-administrators try to access them.
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def IsAdministrator(self) -> bool:
        """
        Getter for property: (bool) IsAdministrator
         Returns a flag indicating if the user has Teamcenter administator privileges.  
           Some
                    settings can are only available to administrators, and will raise errors
                    if non-administrators try to access them.
                  
         
        """
        pass
    
    ## Getter for property: (bool) Journaling
    ##  Returns a flag controlling Teamcenter journaling   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def Journaling(self) -> bool:
        """
        Getter for property: (bool) Journaling
         Returns a flag controlling Teamcenter journaling   
            
         
        """
        pass
    
    ## Setter for property: (bool) Journaling

    ##  Returns a flag controlling Teamcenter journaling   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Journaling.setter
    def Journaling(self, journaling_on: bool):
        """
        Setter for property: (bool) Journaling
         Returns a flag controlling Teamcenter journaling   
            
         
        """
        pass
    
    ## Getter for property: (str) LocalVolume
    ##  Returns the Teamcenter local volume.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetLocalVolumes PDM::SessionSettings::GetLocalVolumes@endlink 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def LocalVolume(self) -> str:
        """
        Getter for property: (str) LocalVolume
         Returns the Teamcenter local volume.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetLocalVolumes PDM::SessionSettings::GetLocalVolumes@endlink 
                   
         
        """
        pass
    
    ## Setter for property: (str) LocalVolume

    ##  Returns the Teamcenter local volume.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetLocalVolumes PDM::SessionSettings::GetLocalVolumes@endlink 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LocalVolume.setter
    def LocalVolume(self, localVolume: str):
        """
        Setter for property: (str) LocalVolume
         Returns the Teamcenter local volume.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetLocalVolumes PDM::SessionSettings::GetLocalVolumes@endlink 
                   
         
        """
        pass
    
    ## Getter for property: (str) LocationCode
    ##  Returns the Teamcenter location code.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetLocationCodes PDM::SessionSettings::GetLocationCodes@endlink 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## @return str
    @property
    def LocationCode(self) -> str:
        """
        Getter for property: (str) LocationCode
         Returns the Teamcenter location code.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetLocationCodes PDM::SessionSettings::GetLocationCodes@endlink 
                   
         
        """
        pass
    
    ## Setter for property: (str) LocationCode

    ##  Returns the Teamcenter location code.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetLocationCodes PDM::SessionSettings::GetLocationCodes@endlink 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    @LocationCode.setter
    def LocationCode(self, locationCode: str):
        """
        Setter for property: (str) LocationCode
         Returns the Teamcenter location code.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetLocationCodes PDM::SessionSettings::GetLocationCodes@endlink 
                   
         
        """
        pass
    
    ## Getter for property: (str) Project
    ##  Returns the Teamcenter project in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetProjects PDM::SessionSettings::GetProjects@endlink 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## @return str
    @property
    def Project(self) -> str:
        """
        Getter for property: (str) Project
         Returns the Teamcenter project in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetProjects PDM::SessionSettings::GetProjects@endlink 
                   
         
        """
        pass
    
    ## Setter for property: (str) Project

    ##  Returns the Teamcenter project in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetProjects PDM::SessionSettings::GetProjects@endlink 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    @Project.setter
    def Project(self, project: str):
        """
        Setter for property: (str) Project
         Returns the Teamcenter project in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetProjects PDM::SessionSettings::GetProjects@endlink 
                   
         
        """
        pass
    
    ## Getter for property: (str) Role
    ##  Returns the Teamcenter role in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetRoles PDM::SessionSettings::GetRoles@endlink 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return str
    @property
    def Role(self) -> str:
        """
        Getter for property: (str) Role
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetRoles PDM::SessionSettings::GetRoles@endlink 
                   
         
        """
        pass
    
    ## Setter for property: (str) Role

    ##  Returns the Teamcenter role in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetRoles PDM::SessionSettings::GetRoles@endlink 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Role.setter
    def Role(self, role: str):
        """
        Setter for property: (str) Role
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetRoles PDM::SessionSettings::GetRoles@endlink 
                   
         
        """
        pass
    
    ## Getter for property: (bool) SecurityLogging
    ##  Returns a flag controlling Teamcenter security logging.  
    ##    Only available to administrators.   
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return bool
    @property
    def SecurityLogging(self) -> bool:
        """
        Getter for property: (bool) SecurityLogging
         Returns a flag controlling Teamcenter security logging.  
           Only available to administrators.   
         
        """
        pass
    
    ## Setter for property: (bool) SecurityLogging

    ##  Returns a flag controlling Teamcenter security logging.  
    ##    Only available to administrators.   
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @SecurityLogging.setter
    def SecurityLogging(self, security_logging_on: bool):
        """
        Setter for property: (bool) SecurityLogging
         Returns a flag controlling Teamcenter security logging.  
           Only available to administrators.   
         
        """
        pass
    
    ## Getter for property: (str) Volume
    ##  Returns the Teamcenter role in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetVolumes PDM::SessionSettings::GetVolumes@endlink 
    ##            
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## @return str
    @property
    def Volume(self) -> str:
        """
        Getter for property: (str) Volume
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetVolumes PDM::SessionSettings::GetVolumes@endlink 
                   
         
        """
        pass
    
    ## Setter for property: (str) Volume

    ##  Returns the Teamcenter role in which the user acts.  
    ##    Should be
    ##             one of those given by @link PDM::SessionSettings::GetVolumes PDM::SessionSettings::GetVolumes@endlink 
    ##            
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    @Volume.setter
    def Volume(self, volume: str):
        """
        Setter for property: (str) Volume
         Returns the Teamcenter role in which the user acts.  
           Should be
                    one of those given by @link PDM::SessionSettings::GetVolumes PDM::SessionSettings::GetVolumes@endlink 
                   
         
        """
        pass
    
    ##  Applies any changes to the settings 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Apply(self) -> None:
        """
         Applies any changes to the settings 
        """
        pass
    
    ##  Applies any changes to the session settings and reloads the data model as per the new group and role (if changed). 
    ##             The following settings are reloaded in this operation:
    ##             1. Reload Templates 
    ##             2. Reload Teamcenter preferences 
    ##             3. Refresh Teamcenter Type customizations
    ##             
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## License requirements: None.
    def ApplyAndRefresh(self) -> None:
        """
         Applies any changes to the session settings and reloads the data model as per the new group and role (if changed). 
                    The following settings are reloaded in this operation:
                    1. Reload Templates 
                    2. Reload Teamcenter preferences 
                    3. Refresh Teamcenter Type customizations
                    
        """
        pass
    
    ##  Free resources associated with the instance. After this method
    ##             is called, it is illegal to use the object.  In .NET, this method
    ##             is automatically called when the object is deleted by the garbage
    ##             collector. 
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Free resources associated with the instance. After this method
                    is called, it is illegal to use the object.  In .NET, this method
                    is automatically called when the object is deleted by the garbage
                    collector. 
        """
        pass
    
    ##  Dump the validation info .This API can be used to expose the current state from the 
    ##             UGMGR session, typically the information about the session,assembly,components,their states
    ##             etc. 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="log_file_name"> (str)  log file name </param>
    def DumpValidationInfo(self, log_file_name: str) -> None:
        """
         Dump the validation info .This API can be used to expose the current state from the 
                    UGMGR session, typically the information about the session,assembly,components,their states
                    etc. 
        """
        pass
    
    ##  Gets the names of the Teamcenter groups to which the
    ##             user belongs. 
    ##         
    ##  @return groups (List[str]):  the names of the groups .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetGroups(self) -> List[str]:
        """
         Gets the names of the Teamcenter groups to which the
                    user belongs. 
                
         @return groups (List[str]):  the names of the groups .
        """
        pass
    
    ##  Gets the names of the Teamcenter local volumes which the user may use,
    ##            given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
    ##         
    ##  @return localVolumes (List[str]):  the names of the local volumes .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetLocalVolumes(self) -> List[str]:
        """
         Gets the names of the Teamcenter local volumes which the user may use,
                   given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
                
         @return localVolumes (List[str]):  the names of the local volumes .
        """
        pass
    
    ##  Gets the names of the Teamcenter location codes which the user may use, 
    ##             given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
    ##         
    ##  @return locationCodes (List[str]):  the names of the location codes .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    def GetLocationCodes(self) -> List[str]:
        """
         Gets the names of the Teamcenter location codes which the user may use, 
                    given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
                
         @return locationCodes (List[str]):  the names of the location codes .
        """
        pass
    
    ##  Gets the names of the Teamcenter projects to which the user belongs also
    ##             the first entry of the returned projects list is always empty.
    ##         
    ##  @return projects (List[str]):  the names of the projects .
    ## 
    ##   <br>  Created in NX8.5.0  <br> 

    ## License requirements: None.
    def GetProjects(self) -> List[str]:
        """
         Gets the names of the Teamcenter projects to which the user belongs also
                    the first entry of the returned projects list is always empty.
                
         @return projects (List[str]):  the names of the projects .
        """
        pass
    
    ##  Gets the names of the Teamcenter roles in which the
    ##             user may act, given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
    ##         
    ##  @return roles (List[str]):  the names of the roles .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetRoles(self) -> List[str]:
        """
         Gets the names of the Teamcenter roles in which the
                    user may act, given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
                
         @return roles (List[str]):  the names of the roles .
        """
        pass
    
    ##  Gets the names of the Teamcenter volumes which the
    ##             user may use, given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
    ##         
    ##  @return volumes (List[str]):  the names of the volumes .
    ## 
    ##   <br>  Created in NX4.0.0  <br> 

    ## License requirements: None.
    def GetVolumes(self) -> List[str]:
        """
         Gets the names of the Teamcenter volumes which the
                    user may use, given the current group returned by @link PDM::SessionSettings::Group PDM::SessionSettings::Group@endlink .
                
         @return volumes (List[str]):  the names of the volumes .
        """
        pass
    
##  
##         Represents a base class that provides common methods for various model elements in a @link NXOpen::CollaborativeDesign NXOpen::CollaborativeDesign@endlink .
##      <br> Use the static method in this class to obtain an instance.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SheetRevision(ConditionalElementRevision): 
    """ 
        Represents a base class that provides common methods for various model elements in a <ja_class>NXOpen.CollaborativeDesign</ja_class>.
    """
    pass


import NXOpen
##  Represents a builder class that performs Save Management operations.
##         This can be used to query or update smart save objects  that participate in the save management operations.
##         Every smart save object represents NX object that is undergoing save operation. <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateSmartSaveBuilderWithContext  NXOpen::PDM::PdmSession::CreateSmartSaveBuilderWithContext @endlink  <br> 
## 
##   <br>  Created in NX10.0.0  <br> 

class SmartSaveBuilder(NXOpen.Builder): 
    """ Represents a builder class that performs Save Management operations.
        This can be used to query or update smart save objects  that participate in the save management operations.
        Every smart save object represents NX object that is undergoing save operation."""


    ##  Represents the Dialog type 
    ##             This is used for commands that use save management dialog with special customizations. 
    ##             @link SmartSaveBuilder::DialogTypeSave SmartSaveBuilder::DialogTypeSave@endlink  means that the save management is invoked for save operations.
    ##             @link PDM::SmartSaveBuilder::SaveType PDM::SmartSaveBuilder::SaveType@endlink  is only applicable for this case.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Save</term><description> 
    ## </description> </item><item><term> 
    ## StageModelSaveAs</term><description> 
    ##  For Stage Model Save As operation </description> </item><item><term> 
    ## DesignSessionSaveAs</term><description> 
    ##  For Design Session Save As </description> </item></list>
    class DialogType(Enum):
        """
        Members Include: <Save> <StageModelSaveAs> <DesignSessionSaveAs>
        """
        Save: int
        StageModelSaveAs: int
        DesignSessionSaveAs: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmartSaveBuilder.DialogType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Represents a File Save type
    ##             Note: Setting the Save type as PDM.SmartSaveBuilder.SaveType.SaveAndClose in a custom program will only Save the parts but will not close the parts. 
    ##             The user needs to explicitly call JA_BASE_PART_close to close the parts.
    ##             However, if the user records a journal by selecting SaveType as PDM.SmartSaveBuilder.SaveType.SaveAndClose, it will automatically record the extra 
    ##             JA call to close the parts.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Save</term><description> 
    ##  File Save </description> </item><item><term> 
    ## SaveAll</term><description> 
    ##  File SaveAll </description> </item><item><term> 
    ## SavePreciseAssembly</term><description> 
    ##  File SavePreciseAssembly </description> </item><item><term> 
    ## SaveWorkPartOnly</term><description> 
    ##  File SaveWorkPartOnly </description> </item><item><term> 
    ## SaveAndClose</term><description> 
    ##  File Save And Close </description> </item><item><term> 
    ## SaveDesignElements</term><description> 
    ##  Save Design Elements </description> </item><item><term> 
    ## ForceSaveAll</term><description> 
    ##  File ForceSaveAll </description> </item></list>
    class SaveType(Enum):
        """
        Members Include: <Save> <SaveAll> <SavePreciseAssembly> <SaveWorkPartOnly> <SaveAndClose> <SaveDesignElements> <ForceSaveAll>
        """
        Save: int
        SaveAll: int
        SavePreciseAssembly: int
        SaveWorkPartOnly: int
        SaveAndClose: int
        SaveDesignElements: int
        ForceSaveAll: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmartSaveBuilder.SaveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) DebugDumpEnabled
    ##  Returns the debug dump enabled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## @return bool
    @property
    def DebugDumpEnabled(self) -> bool:
        """
        Getter for property: (bool) DebugDumpEnabled
         Returns the debug dump enabled   
            
         
        """
        pass
    
    ## Setter for property: (bool) DebugDumpEnabled

    ##  Returns the debug dump enabled   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    @DebugDumpEnabled.setter
    def DebugDumpEnabled(self, debugDumpEnabled: bool):
        """
        Setter for property: (bool) DebugDumpEnabled
         Returns the debug dump enabled   
            
         
        """
        pass
    
    ## Getter for property: (bool) UseNewSortForDebug
    ##  Returns the new debug sort enabled   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## @return bool
    @property
    def UseNewSortForDebug(self) -> bool:
        """
        Getter for property: (bool) UseNewSortForDebug
         Returns the new debug sort enabled   
            
         
        """
        pass
    
    ## Setter for property: (bool) UseNewSortForDebug

    ##  Returns the new debug sort enabled   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    @UseNewSortForDebug.setter
    def UseNewSortForDebug(self, useNewSortForDebug: bool):
        """
        Setter for property: (bool) UseNewSortForDebug
         Returns the new debug sort enabled   
            
         
        """
        pass
    
    ## Adds the modified related drawing non-master smart save objects and sets them valid for Save operation
    ##  @return foundDependentPartsForSave (bool): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def AddRelatedDrawingsAndSetValidForSave(self) -> bool:
        """
        Adds the modified related drawing non-master smart save objects and sets them valid for Save operation
         @return foundDependentPartsForSave (bool): .
        """
        pass
    
    ##   Assign or remove projects to/from objects
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="smartSaveObjects"> (@link SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink)  Array of objects to assign/remove projects to </param>
    ## <param name="project_names"> (List[str])  names of the projects to assign </param>
    ## <param name="assignment_states"> (@link NXOpen.Session.ProjectAssignmentState List[NXOpen.Session.ProjectAssignmentState]@endlink)  assignment states </param>
    def AssignRemoveProjects(self, smartSaveObjects: List[SmartSaveObject], project_names: List[str], assignment_states: List[NXOpen.Session.ProjectAssignmentState]) -> None:
        """
          Assign or remove projects to/from objects
        """
        pass
    
    ##  Checks whether smart save operation can be performed with default operation type set 
    ##  @return canPerformDefaultSave (bool): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def CanPerformDefaultSave(self) -> bool:
        """
         Checks whether smart save operation can be performed with default operation type set 
         @return canPerformDefaultSave (bool): .
        """
        pass
    
    ##  Clears operation failures if any 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def ClearValidationFailures(self) -> None:
        """
         Clears operation failures if any 
        """
        pass
    
    ##  Create new specifications for Logical Objects 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="smartSaveObjects"> (@link SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink) </param>
    def CreateSpecificationsForSmartSaveObjects(self, smartSaveObjects: List[SmartSaveObject]) -> None:
        """
         Create new specifications for Logical Objects 
        """
        pass
    
    ##  Create an instance of a NXOpen.PDM.AlternateIdManager which will be used to create alternate ID information while creating the new part.
    ##  @return alternateIDManager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="logicalObject"> (@link LogicalObject NXOpen.PDM.LogicalObject@endlink) </param>
    def GetAlternateIDManager(self, logicalObject: LogicalObject) -> AlternateIdManager:
        """
         Create an instance of a NXOpen.PDM.AlternateIdManager which will be used to create alternate ID information while creating the new part.
         @return alternateIDManager (@link AlternateIdManager NXOpen.PDM.AlternateIdManager@endlink): .
        """
        pass
    
    ##   Gets CLI names of Change Notice associated with Objects involved in Save operation 
    ##  @return changeNoticeNames (List[str]): .
    ## 
    ##   <br>  Created in NX12.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="smartSaveObjects"> (@link SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink) </param>
    def GetAssociatedChangeNoticeNames(self, smartSaveObjects: List[SmartSaveObject]) -> List[str]:
        """
          Gets CLI names of Change Notice associated with Objects involved in Save operation 
         @return changeNoticeNames (List[str]): .
        """
        pass
    
    ##  Returns ErrorMessageHandler 
    ##  @return errorMessageHandler (@link ErrorMessageHandler NXOpen.PDM.ErrorMessageHandler@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="refresh"> (bool) </param>
    def GetErrorMessageHandler(self, refresh: bool) -> ErrorMessageHandler:
        """
         Returns ErrorMessageHandler 
         @return errorMessageHandler (@link ErrorMessageHandler NXOpen.PDM.ErrorMessageHandler@endlink): .
        """
        pass
    
    ##  Returns operation failures 
    ##  @return operationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetOperationFailures(self) -> NXOpen.ErrorList:
        """
         Returns operation failures 
         @return operationFailures (@link NXOpen.ErrorList NXOpen.ErrorList@endlink): .
        """
        pass
    
    ##  Gets the smart save objects for the modified objects in session. 
    ##  @return smartSaveObjects (@link SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetSmartSaveObjects(self) -> List[SmartSaveObject]:
        """
         Gets the smart save objects for the modified objects in session. 
         @return smartSaveObjects (@link SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink): .
        """
        pass
    
    ##  Updates the given smart save objects after operation type change. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="smartSaveObjects"> (@link SmartSaveObject List[NXOpen.PDM.SmartSaveObject]@endlink)  the objects for which operation type is changed</param>
    ## <param name="operationType"> (@link NXOpen.AttributePropertiesBuilder.OperationType NXOpen.AttributePropertiesBuilder.OperationType@endlink)  the new operation type </param>
    def OnOperationTypeChanged(self, smartSaveObjects: List[SmartSaveObject], operationType: NXOpen.AttributePropertiesBuilder.OperationType) -> None:
        """
         Updates the given smart save objects after operation type change. 
        """
        pass
    
    ##  Updates the smart save objects with valid operation type and dependencies 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def UpdateSmartSaveObjectsOnBuilder(self) -> None:
        """
         Updates the smart save objects with valid operation type and dependencies 
        """
        pass
    
    ##  Validates whether the save operation can be performed on the smart save objects 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def ValidateSmartSaveObjects(self) -> None:
        """
         Validates whether the save operation can be performed on the smart save objects 
        """
        pass
    
import NXOpen
##  Represents smart save context  <br> To create a new instance of this class, use @link NXOpen::PDM::PdmSession::CreateSmartSaveContext  NXOpen::PDM::PdmSession::CreateSmartSaveContext @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class SmartSaveContext(NXOpen.TransientObject): 
    """ Represents smart save context """


    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Returns the save operation type 
    ##  @return saveType (@link SmartSaveBuilder.SaveType NXOpen.PDM.SmartSaveBuilder.SaveType@endlink):   .
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetSaveType(self) -> SmartSaveBuilder.SaveType:
        """
         Returns the save operation type 
         @return saveType (@link SmartSaveBuilder.SaveType NXOpen.PDM.SmartSaveBuilder.SaveType@endlink):   .
        """
        pass
    
    ##  Returns the set of work object to root object pairs from the context 
    ##  @return A tuple consisting of (workObjects, rootObjects). 
    ##  - workObjects is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink. array of work objects to be saved .
    ##  - rootObjects is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink. array of root objects  .

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    def GetWorkObjectToRootObjectMap(self) -> Tuple[List[NXOpen.TaggedObject], List[NXOpen.TaggedObject]]:
        """
         Returns the set of work object to root object pairs from the context 
         @return A tuple consisting of (workObjects, rootObjects). 
         - workObjects is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink. array of work objects to be saved .
         - rootObjects is: @link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink. array of root objects  .

        """
        pass
    
    ##  Adds the given set of work object to root object pairs to the context 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="workObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  array of work objects to be saved </param>
    ## <param name="rootObjects"> (@link NXOpen.TaggedObject List[NXOpen.TaggedObject]@endlink)  array of root objects </param>
    def SetWorkObjectToRootObjectMap(self, workObjects: List[NXOpen.TaggedObject], rootObjects: List[NXOpen.TaggedObject]) -> None:
        """
         Adds the given set of work object to root object pairs to the context 
        """
        pass
    
import NXOpen
## 
##         Represents the class for object participating in the smart save operation.
##         It is an object that wraps actual NXObject that is modified in the session and processes it to be able to display in Save dialog's table. 
##         Refer to technical documentation to know more about Save Management.
##      <br> Instances of this class can be accessed through smart save builder.  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class SmartSaveObject(NXOpen.NXObject): 
    """
        Represents the class for object participating in the smart save operation.
        It is an object that wraps actual NXObject that is modified in the session and processes it to be able to display in Save dialog's table. 
        Refer to technical documentation to know more about Save Management.
    """


    ## 
    ##             Specifies operation type. 
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  Invalid/Ignore </description> </item><item><term> 
    ## Create</term><description> 
    ##  Create </description> </item><item><term> 
    ## Revise</term><description> 
    ##  Revise </description> </item><item><term> 
    ## SaveAs</term><description> 
    ##  SaveAs </description> </item><item><term> 
    ## Save</term><description> 
    ##  Save </description> </item><item><term> 
    ## Delete</term><description> 
    ##  Delete/Discontinue </description> </item></list>
    class OperationType(Enum):
        """
        Members Include: <NotSet> <Create> <Revise> <SaveAs> <Save> <Delete>
        """
        NotSet: int
        Create: int
        Revise: int
        SaveAs: int
        Save: int
        Delete: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SmartSaveObject.OperationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns the current operation type @link NXOpen::PDM::SmartSaveObject::OperationType NXOpen::PDM::SmartSaveObject::OperationType@endlink  for this smart save object. 
    ##  @return currentOperationType (@link SmartSaveObject.OperationType NXOpen.PDM.SmartSaveObject.OperationType@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetCurrentOperationType(self) -> SmartSaveObject.OperationType:
        """
         Returns the current operation type @link NXOpen::PDM::SmartSaveObject::OperationType NXOpen::PDM::SmartSaveObject::OperationType@endlink  for this smart save object. 
         @return currentOperationType (@link SmartSaveObject.OperationType NXOpen.PDM.SmartSaveObject.OperationType@endlink): .
        """
        pass
    
    ##  Returns the current effectivity formula for this object. 
    ##  @return effectivityFormula (str): .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def GetEffectivityFormula(self) -> str:
        """
         Returns the current effectivity formula for this object. 
         @return effectivityFormula (str): .
        """
        pass
    
    ##  Returns the modification reason for this smart save object. This reason is used to calculate valid and current operation/s to be performed. 
    ##  @return modificationReason (str): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetModificationReason(self) -> str:
        """
         Returns the modification reason for this smart save object. This reason is used to calculate valid and current operation/s to be performed. 
         @return modificationReason (str): .
        """
        pass
    
    ##  Returns the Teamcenter object type for this object. 
    ##  @return objectTcType (str): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetTeamcenterObjectType(self) -> str:
        """
         Returns the Teamcenter object type for this object. 
         @return objectTcType (str): .
        """
        pass
    
    ##  Returns the valid operation types (array of @link NXOpen::PDM::SmartSaveObject::OperationType NXOpen::PDM::SmartSaveObject::OperationType@endlink ) for this object. 
    ##  @return currentValidOperationTypes (@link SmartSaveObject.OperationType List[NXOpen.PDM.SmartSaveObject.OperationType]@endlink): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def GetValidOperationTypes(self) -> List[SmartSaveObject.OperationType]:
        """
         Returns the valid operation types (array of @link NXOpen::PDM::SmartSaveObject::OperationType NXOpen::PDM::SmartSaveObject::OperationType@endlink ) for this object. 
         @return currentValidOperationTypes (@link SmartSaveObject.OperationType List[NXOpen.PDM.SmartSaveObject.OperationType]@endlink): .
        """
        pass
    
    ##  This is applicable only for 4G components. Returns if the current user can add new components to the Product. 
    ##  @return addContentPrivilege (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def HasAddContentPrivilege(self) -> bool:
        """
         This is applicable only for 4G components. Returns if the current user can add new components to the Product. 
         @return addContentPrivilege (bool): .
        """
        pass
    
    ##  This is applicable only for 4G components. Returns if the current user can remove components to the Product. 
    ##  @return removeContentPrivilege (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def HasRemoveContentPrivilege(self) -> bool:
        """
         This is applicable only for 4G components. Returns if the current user can remove components to the Product. 
         @return removeContentPrivilege (bool): .
        """
        pass
    
    ##  Returns if the object is currently checkedout by another user. 
    ##  @return isCheckedOutByAnotherUser (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsCheckedOutByAnotherUser(self) -> bool:
        """
         Returns if the object is currently checkedout by another user. 
         @return isCheckedOutByAnotherUser (bool): .
        """
        pass
    
    ##  Returns if this object is currently being shown on the save dialog. 
    ##  @return isDisplayedOnDialog (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsDisplayedOnTheSaveDialog(self) -> bool:
        """
         Returns if this object is currently being shown on the save dialog. 
         @return isDisplayedOnDialog (bool): .
        """
        pass
    
    ##  Returns if the object being saved need to be explicitly checked out. 
    ##  @return isExplicitCheckOutNeeded (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsExplicitCheckOutNeeded(self) -> bool:
        """
         Returns if the object being saved need to be explicitly checked out. 
         @return isExplicitCheckOutNeeded (bool): .
        """
        pass
    
    ##  Returns the state of object in Teamcenter. An object state is considered frozen if the released status on this object marks it to be final. 
    ##  @return isFrozenByStatus (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsFrozenByStatus(self) -> bool:
        """
         Returns the state of object in Teamcenter. An object state is considered frozen if the released status on this object marks it to be final. 
         @return isFrozenByStatus (bool): .
        """
        pass
    
    ##  Returns if the object is major revisable in Teamcenter. 
    ##  @return isMajorRevisable (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsMajorRevisable(self) -> bool:
        """
         Returns if the object is major revisable in Teamcenter. 
         @return isMajorRevisable (bool): .
        """
        pass
    
    ##  Returns if this object is modifiable by the current user. 
    ##  @return isModifiable (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsModifiable(self) -> bool:
        """
         Returns if this object is modifiable by the current user. 
         @return isModifiable (bool): .
        """
        pass
    
    ##  Returns if this part is a non-master. For non-part objects this will return false. 
    ##  @return isNonMaster (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsNonMaster(self) -> bool:
        """
         Returns if this part is a non-master. For non-part objects this will return false. 
         @return isNonMaster (bool): .
        """
        pass
    
    ##  Returns if the object being saved has status applied in Teamcenter. 
    ##  @return isReleased (bool): .
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    def IsReleased(self) -> bool:
        """
         Returns if the object being saved has status applied in Teamcenter. 
         @return isReleased (bool): .
        """
        pass
    
    ##  Set whether this object is to be shown on the dialog (i.e. valid for user interaction). 
    ##             Setting this to false will remove the object from the Save dialog's table but it will still be processed for set operation. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="markDisplayedOnDialog"> (bool) </param>
    def SetAsDisplayedOnTheSaveDialog(self, markDisplayedOnDialog: bool) -> None:
        """
         Set whether this object is to be shown on the dialog (i.e. valid for user interaction). 
                    Setting this to false will remove the object from the Save dialog's table but it will still be processed for set operation. 
        """
        pass
    
    ##  Sets the new operation type @link NXOpen::PDM::SmartSaveObject::OperationType NXOpen::PDM::SmartSaveObject::OperationType@endlink  for this smart save object. This operation should be from among the valid operation types or
    ##             else the operation will fail. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="newOperationType"> (@link SmartSaveObject.OperationType NXOpen.PDM.SmartSaveObject.OperationType@endlink) </param>
    def SetCurrentOperationType(self, newOperationType: SmartSaveObject.OperationType) -> None:
        """
         Sets the new operation type @link NXOpen::PDM::SmartSaveObject::OperationType NXOpen::PDM::SmartSaveObject::OperationType@endlink  for this smart save object. This operation should be from among the valid operation types or
                    else the operation will fail. 
        """
        pass
    
    ##  Sets the new effectivity formula to be applied on this object. 
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    ## 
    ## <param name="effectivityFormula"> (str) </param>
    ## <param name="effectivityDisplayString"> (str) </param>
    def SetEffectivityFormula(self, effectivityFormula: str, effectivityDisplayString: str) -> None:
        """
         Sets the new effectivity formula to be applied on this object. 
        """
        pass
    
    ##  Sets the new valid operation types for this object. These operations should be from among the ones returned by 
    ##             @link NXOpen::PDM::SmartSaveObject::GetValidOperationTypes NXOpen::PDM::SmartSaveObject::GetValidOperationTypes@endlink  or they might be invalid. 
    ## 
    ##   <br>  Created in NX12.0.1  <br> 

    ## License requirements: None.
    ## 
    ## <param name="newValidOperationTypes"> (@link SmartSaveObject.OperationType List[NXOpen.PDM.SmartSaveObject.OperationType]@endlink) </param>
    def SetValidOperationTypes(self, newValidOperationTypes: List[SmartSaveObject.OperationType]) -> None:
        """
         Sets the new valid operation types for this object. These operations should be from among the ones returned by 
                    @link NXOpen::PDM::SmartSaveObject::GetValidOperationTypes NXOpen::PDM::SmartSaveObject::GetValidOperationTypes@endlink  or they might be invalid. 
        """
        pass
    
import NXOpen
##  Represents search soa query to perform Teamcenter search
## 
##   <br>  Created in NX6.0.0  <br> 

class SoaQuery(NXOpen.TransientObject): 
    """ Represents search soa query to perform Teamcenter search"""


    ##  Add the field description to create an SOA query 
    ## 
    ##   <br>  Created in NX6.0.0  <br> 
    ## 
    ##   <br>  @deprecated Deprecated in NX8.0.0.  It's not needed in any context of search based on queries.  <br> 

    ## License requirements: None.
    ## 
    ## <param name="searchVar"> (@link PdmSearch NXOpen.PDM.PdmSearch@endlink)  pdm search structure </param>
    ## <param name="type"> (@link PdmSoaqueryNxmgrfielddatatype NXOpen.PDM.PdmSoaqueryNxmgrfielddatatype@endlink)  search field data type </param>
    ## <param name="name"> (str)  name of search </param>
    ## <param name="attrName"> (str)  search attribute  name </param>
    ## <param name="defaultValue"> (str)  default value </param>
    ## <param name="logicalOperation"> (str)  logical operation for search criteria </param>
    ## <param name="mathOperation"> (str)  math operation for search criteria </param>
    ## <param name="lov"> (@link ListOfValues NXOpen.PDM.ListOfValues@endlink)  List of values </param>
    def AddFieldDescription(self, searchVar: PdmSearch, type: PdmSoaqueryNxmgrfielddatatype, name: str, attrName: str, defaultValue: str, logicalOperation: str, mathOperation: str, lov: ListOfValues) -> None:
        """
         Add the field description to create an SOA query 
        """
        pass
    
    ##  Frees the object from memory.  After this method is called,
    ##         it is illegal to use the object.  In .NET, this method is automatically
    ##         called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.0  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                it is illegal to use the object.  In .NET, this method is automatically
                called when the object is deleted by the garbage collector.  
        """
        pass
    
import NXOpen
import NXOpen.Assemblies
##  Contains various TCIN utility methods  <br> To obtain an instance of this class, refer to @link NXOpen::PDM::PdmSession  NXOpen::PDM::PdmSession @endlink  <br> 
## 
##   <br>  Created in NX11.0.1  <br> 

class TcinUtils(NXOpen.Object): 
    """ Contains various TCIN utility methods """


    ##  Convert legacy Design Control Elements to Stand-alone Design Features 
    ##  @return A tuple consisting of (legacyDCEIds, newDesignFeatureIds). 
    ##  - legacyDCEIds is: List[str]. array containing list of DCE_ID#REV_ID of DCEs .
    ##  - newDesignFeatureIds is: List[str]. array containing list of DF_ID#REV_ID of new Stand-alone design features .

    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: nx_4gd_integration ("4th Generation Design")
    ## <param name="designControlElements"> (@link NXOpen.Assemblies.Component List[NXOpen.Assemblies.Component]@endlink) </param>
    def ConvertLegacyDesignControlElements(designControlElements: List[NXOpen.Assemblies.Component]) -> Tuple[List[str], List[str]]:
        """
         Convert legacy Design Control Elements to Stand-alone Design Features 
         @return A tuple consisting of (legacyDCEIds, newDesignFeatureIds). 
         - legacyDCEIds is: List[str]. array containing list of DCE_ID#REV_ID of DCEs .
         - newDesignFeatureIds is: List[str]. array containing list of DF_ID#REV_ID of new Stand-alone design features .

        """
        pass
    
import NXOpen
##  Represents the Trace link query  <br> To obtain an instance of this class use @link NXOpen::PDM::RequirementUtils NXOpen::PDM::RequirementUtils@endlink   <br> 
## 
##   <br>  Created in NX6.0.3  <br> 

class TracelinkQuery(NXOpen.TransientObject): 
    """ Represents the Trace link query """


    ##  Frees the object from memory.  After this method is called,
    ##          it is illegal to use the object.  In .NET, this method is automatically
    ##          called when the object is deleted by the garbage collector.  
    ## 
    ##   <br>  Created in NX6.0.3  <br> 

    ## License requirements: None.
    def Dispose(self) -> None:
        """
         Frees the object from memory.  After this method is called,
                 it is illegal to use the object.  In .NET, this method is automatically
                 called when the object is deleted by the garbage collector.  
        """
        pass
    
    ##  Gets the Traceline Relations. 
    ##  @return xml_stream (str):  the XML .
    ## 
    ##   <br>  Created in NX6.0.3  <br> 

    ## License requirements: None.
    def GetTracelinkRelationsXml(self) -> str:
        """
         Gets the Traceline Relations. 
         @return xml_stream (str):  the XML .
        """
        pass
    
import NXOpen
import NXOpen.GeometricUtilities
##  Represents a builder class that performs variant rule configuration. 
## 
##   <br>  Created in NX9.0.0  <br> 

class VariantConfigurationBuilder(NXOpen.TaggedObject): 
    """ Represents a builder class that performs variant rule configuration. """


    ##  Adds given variant rules in case of multiple variant rules to @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink 
    ##         The input contextIds comprising of multifield key and itemRev_id:
    ##         In case of default domain: contextId should contain Teamcenter item ID.
    ##         In case of non-default domain: contextId should contain the multifield keys.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="contextIds"> (List[str])  context id comprising of multifield key and itemRev_id in which variant rule resides </param>
    ## <param name="variantRules"> (List[str])  variant rules of corresponding context ids to be added </param>
    def AddMultipleVariantRules(self, contextIds: List[str], variantRules: List[str]) -> None:
        """
         Adds given variant rules in case of multiple variant rules to @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink 
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
        """
        pass
    
    ##  Returns the saved variant rules for the give context ID
    ##         The input contextId:
    ##         In case of default domain: it should be Teamcenter item ID.
    ##         In case of non-default domain: it should be the multifield key.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         
    ##  @return variantRules (List[str]):  variant rules from the given context .
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="contextId"> (str)  multifield key in case of product assembly or collaborative design id </param>
    ## <param name="revId"> (str)  itemRev_id in case of product assembly</param>
    def AskAvailableVariantRules(self, contextId: str, revId: str) -> List[str]:
        """
         Returns the saved variant rules for the give context ID
                The input contextId:
                In case of default domain: it should be Teamcenter item ID.
                In case of non-default domain: it should be the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         @return variantRules (List[str]):  variant rules from the given context .
        """
        pass
    
    ##  Returns selected variant rules stored inside @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink 
    ##         The input contextIds comprising of multifield key and itemRev_id:
    ##         In case of default domain: contextId should contain Teamcenter item ID.
    ##         In case of non-default domain: contextId should contain the multifield keys.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         
    ##  @return A tuple consisting of (contextIds, variantRules). 
    ##  - contextIds is: List[str]. array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected .
    ##  - variantRules is: List[str]. array of selected variant rules .

    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetVariantRuleTableInformation(self) -> Tuple[List[str], List[str]]:
        """
         Returns selected variant rules stored inside @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink 
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         @return A tuple consisting of (contextIds, variantRules). 
         - contextIds is: List[str]. array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected .
         - variantRules is: List[str]. array of selected variant rules .

        """
        pass
    
    ##  Removes the given variant rule from @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink  if applicable
    ##         The input contextId comprising of multifield key and itemRev_id:
    ##        In case of default domain: contextId should contain Teamcenter item ID.
    ##         In case of non-default domain: contextId should contain the multifield keys.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         
    ## 
    ##   <br>  Created in NX9.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="contextId"> (str)  context id comprising of multifield key and itemRev_id in which variant rule resides </param>
    ## <param name="variantRule"> (str)  variant rule to be removed </param>
    def RemoveVariantRule(self, contextId: str, variantRule: str) -> None:
        """
         Removes the given variant rule from @link NXOpen::PDM::VariantConfigurationBuilder NXOpen::PDM::VariantConfigurationBuilder@endlink  if applicable
                The input contextId comprising of multifield key and itemRev_id:
               In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
        """
        pass
    
import NXOpen
## 
##         Represents an @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink  to be used for variant rules configuration.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::PdmManager::CreateVariantRulesConfigurationBuilder  NXOpen::PDM::PdmManager::CreateVariantRulesConfigurationBuilder @endlink  <br> 
## 
##   <br>  Created in NX1872.0.0  <br> 

class VariantRulesConfigurationBuilder(NXOpen.Builder): 
    """
        Represents an <ja_class>NXOpen.PDM.VariantRulesConfigurationBuilder</ja_class> to be used for variant rules configuration.
    """


    ##  Adds given variant rules in case of multiple variant rules to @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink 
    ##         The input contextIds comprising of multifield key and itemRev_id:
    ##         In case of default domain: contextId should contain Teamcenter item ID.
    ##         In case of non-default domain: contextId should contain the multifield keys.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="contextIds"> (List[str])  context id comprising of multifield key and itemRev_id in which variant rule resides </param>
    ## <param name="variantRules"> (List[str])  variant rules of corresponding context ids to be added </param>
    def AddVariantRulesToConfigure(self, contextIds: List[str], variantRules: List[str]) -> None:
        """
         Adds given variant rules in case of multiple variant rules to @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink 
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
        """
        pass
    
    ##  Returns the saved variant rules for the give context ID
    ##         The input contextId:
    ##         In case of default domain: it should be Teamcenter item ID.
    ##         In case of non-default domain: it should be the multifield key.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         
    ##  @return variantRules (List[str]):  variant rules from the given context .
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    ## 
    ## <param name="contextId"> (str)  multifield key in case of product assembly or collaborative design id </param>
    ## <param name="revId"> (str)  itemRev_id in case of product assembly</param>
    def GetVariantRulesForProductAssembly(self, contextId: str, revId: str) -> List[str]:
        """
         Returns the saved variant rules for the give context ID
                The input contextId:
                In case of default domain: it should be Teamcenter item ID.
                In case of non-default domain: it should be the multifield key.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         @return variantRules (List[str]):  variant rules from the given context .
        """
        pass
    
    ##  Returns selected variant rules stored inside @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink 
    ##         The input contextIds comprising of multifield key and itemRev_id:
    ##         In case of default domain: contextId should contain Teamcenter item ID.
    ##         In case of non-default domain: contextId should contain the multifield keys.
    ##         e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
    ##         
    ##  @return A tuple consisting of (contextIds, variantRules). 
    ##  - contextIds is: List[str]. array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected .
    ##  - variantRules is: List[str]. array of selected variant rules .

    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: assemblies ("ASSEMBLIES MODULE")
    def GetVariantRulesSelectedForConfiguration(self) -> Tuple[List[str], List[str]]:
        """
         Returns selected variant rules stored inside @link NXOpen::PDM::VariantRulesConfigurationBuilder NXOpen::PDM::VariantRulesConfigurationBuilder@endlink 
                The input contextIds comprising of multifield key and itemRev_id:
                In case of default domain: contextId should contain Teamcenter item ID.
                In case of non-default domain: contextId should contain the multifield keys.
                e.g.   %#MFK#%,=item_id=001, object_type=SupplierPart, supplier_code=x
                
         @return A tuple consisting of (contextIds, variantRules). 
         - contextIds is: List[str]. array of contextIds comprising of multifield key and itemRev_id from which variant rules are selected .
         - variantRules is: List[str]. array of selected variant rules .

        """
        pass
    
import NXOpen
##  This is can be used to create volume search filter term.
##     * Such filter terms can be used to provide filtering.
##      <br> To create a new instance of this class, use @link NXOpen::PDM::SearchRecipeFilterBuilder::CreateVolumeTerm  NXOpen::PDM::SearchRecipeFilterBuilder::CreateVolumeTerm @endlink  <br> 
## 
##   <br>  Created in NX2306.0.0  <br> 

class VolumeSearchFilterTerm(SearchFilterTerm): 
    """ This is can be used to create volume search filter term.
    * Such filter terms can be used to provide filtering.
    """


    ##  This enum is used to specify the operator for volume search filter. 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Inside</term><description> 
    ## </description> </item><item><term> 
    ## Outside</term><description> 
    ## </description> </item><item><term> 
    ## Intersects</term><description> 
    ## </description> </item><item><term> 
    ## InsideOrIntersects</term><description> 
    ## </description> </item><item><term> 
    ## OutsideOrIntersects</term><description> 
    ## </description> </item></list>
    class Operator(Enum):
        """
        Members Include: <Inside> <Outside> <Intersects> <InsideOrIntersects> <OutsideOrIntersects>
        """
        Inside: int
        Outside: int
        Intersects: int
        InsideOrIntersects: int
        OutsideOrIntersects: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> VolumeSearchFilterTerm.Operator:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This struct represents one bounding box. 
    ## @link VolumeSearchFilterTermBoundingBox_Struct NXOpen.PDM.VolumeSearchFilterTermBoundingBox_Struct@endlink is an alias for @link VolumeSearchFilterTerm.BoundingBox NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox@endlink.
    class BoundingBox:
        """
         This struct represents one bounding box. 
        @link VolumeSearchFilterTermBoundingBox_Struct NXOpen.PDM.VolumeSearchFilterTermBoundingBox_Struct@endlink is an alias for @link VolumeSearchFilterTerm.BoundingBox NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox@endlink.
        """
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) BottomCorner
        ## Bottom vertex of bounding box in coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def BottomCorner(self) -> NXOpen.Point3d:
            """
            Getter for property BottomCorner
            Bottom vertex of bounding box in coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) BottomCorner
        @BottomCorner.setter
        def BottomCorner(self, value: NXOpen.Point3d):
            """
            Getter for property BottomCorner
            Bottom vertex of bounding box in coordinates
            Setter for property BottomCorner
            Bottom vertex of bounding box in coordinates

            """
            pass
        
        ## Getter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) TopCorner
        ## Top vertex of bounding box in coordinates
        ## @return @link NXOpen.Point3d NXOpen.Point3d@endlink
        @property
        def TopCorner(self) -> NXOpen.Point3d:
            """
            Getter for property TopCorner
            Top vertex of bounding box in coordinates

            """
            pass
        
        ## Setter for property :(@link NXOpen.Point3d NXOpen.Point3d@endlink) TopCorner
        @TopCorner.setter
        def TopCorner(self, value: NXOpen.Point3d):
            """
            Getter for property TopCorner
            Top vertex of bounding box in coordinates
            Setter for property TopCorner
            Top vertex of bounding box in coordinates

            """
            pass
        
    
    
    ##  This function gets the bounding boxes from volume term. 
    ##  @return boundingBoxes (@link VolumeSearchFilterTerm.BoundingBox List[NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox]@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetBoundingBoxes(self) -> List[VolumeSearchFilterTerm.BoundingBox]:
        """
         This function gets the bounding boxes from volume term. 
         @return boundingBoxes (@link VolumeSearchFilterTerm.BoundingBox List[NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox]@endlink): .
        """
        pass
    
    ##  This function gets the flag whether to inverse volume term or not. 
    ##  @return excludeToggle (bool): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetExcludeToggle(self) -> bool:
        """
         This function gets the flag whether to inverse volume term or not. 
         @return excludeToggle (bool): .
        """
        pass
    
    ##  This function gets the bounding box operator from volume term. 
    ##  @return boxZoneOperator (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink): .
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    def GetOperator(self) -> VolumeSearchFilterTerm.Operator:
        """
         This function gets the bounding box operator from volume term. 
         @return boxZoneOperator (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink): .
        """
        pass
    
    ##  This function sets the bounding boxes to volume term. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="boundingBoxes"> (@link VolumeSearchFilterTerm.BoundingBox List[NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox]@endlink) </param>
    def SetBoundingBoxes(self, boundingBoxes: List[VolumeSearchFilterTerm.BoundingBox]) -> None:
        """
         This function sets the bounding boxes to volume term. 
        """
        pass
    
    ##  This function sets the flag whether to inverse volume term or not. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="excludeToggle"> (bool) </param>
    def SetExcludeToggle(self, excludeToggle: bool) -> None:
        """
         This function sets the flag whether to inverse volume term or not. 
        """
        pass
    
    ##  This function sets the bounding box operator to volume term. 
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: nx_smartdiscovery (" Smart Discovery")
    ## 
    ## <param name="boxZoneOperator"> (@link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink) </param>
    def SetOperator(self, boxZoneOperator: VolumeSearchFilterTerm.Operator) -> None:
        """
         This function sets the bounding box operator to volume term. 
        """
        pass
    
import NXOpen
##  Represents the Web App session  <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX11.0.0  <br> 

class WebAppSession(NXOpen.Object): 
    """ Represents the Web App session """


    ##  Create a custom WebApp menu handler. 
    ##  @return menuWrap (@link CustomWebAppMenuHandler NXOpen.PDM.CustomWebAppMenuHandler@endlink):  .
    ## 
    ##   <br>  Created in NX11.0.0  <br> 

    ## License requirements: None.
    def CreateCustomWebAppMenuHandler() -> CustomWebAppMenuHandler:
        """
         Create a custom WebApp menu handler. 
         @return menuWrap (@link CustomWebAppMenuHandler NXOpen.PDM.CustomWebAppMenuHandler@endlink):  .
        """
        pass
    
    ##  Send data to Active Workspace from NX 
    ## 
    ##   <br>  Created in NX11.0.1  <br> 

    ## License requirements: None.
    ## <param name="uid"> (str) </param>
    ## <param name="objType"> (str) </param>
    ## <param name="classId"> (str) </param>
    def ShowSummary(uid: str, objType: str, classId: str) -> None:
        """
         Send data to Active Workspace from NX 
        """
        pass
    
## @package NXOpen.PDM
## Classes, Enums and Structs under NXOpen.PDM namespace

## @link AlternateIdManagerAlternateIdsData_Struct NXOpen.PDM.AlternateIdManagerAlternateIdsData_Struct@endlink is an alias for @link AlternateIdManager.AlternateIdsData NXOpen.PDM.AlternateIdManager.AlternateIdsData@endlink.
AlternateIdManagerAlternateIdsData_Struct = AlternateIdManager.AlternateIdsData


## @link AlternateIdManagerAssignAlternateRevData_Struct NXOpen.PDM.AlternateIdManagerAssignAlternateRevData_Struct@endlink is an alias for @link AlternateIdManager.AssignAlternateRevData NXOpen.PDM.AlternateIdManager.AssignAlternateRevData@endlink.
AlternateIdManagerAssignAlternateRevData_Struct = AlternateIdManager.AssignAlternateRevData


##  @link AttributeGroupReviseBuilderSaveAsActionType NXOpen.PDM.AttributeGroupReviseBuilderSaveAsActionType @endlink is an alias for @link AttributeGroupReviseBuilder.SaveAsActionType NXOpen.PDM.AttributeGroupReviseBuilder.SaveAsActionType@endlink
AttributeGroupReviseBuilderSaveAsActionType = AttributeGroupReviseBuilder.SaveAsActionType


##  @link CaeCloneManagerCloneOption NXOpen.PDM.CaeCloneManagerCloneOption @endlink is an alias for @link CaeCloneManager.CloneOption NXOpen.PDM.CaeCloneManager.CloneOption@endlink
CaeCloneManagerCloneOption = CaeCloneManager.CloneOption


##  @link ConfigurationContextBuilderConfigContextMode NXOpen.PDM.ConfigurationContextBuilderConfigContextMode @endlink is an alias for @link ConfigurationContextBuilder.ConfigContextMode NXOpen.PDM.ConfigurationContextBuilder.ConfigContextMode@endlink
ConfigurationContextBuilderConfigContextMode = ConfigurationContextBuilder.ConfigContextMode


##  @link ConfigurationContextBuilderConfigContextType NXOpen.PDM.ConfigurationContextBuilderConfigContextType @endlink is an alias for @link ConfigurationContextBuilder.ConfigContextType NXOpen.PDM.ConfigurationContextBuilder.ConfigContextType@endlink
ConfigurationContextBuilderConfigContextType = ConfigurationContextBuilder.ConfigContextType


##  @link ConfigurationContextBuilderConfigurationDetail NXOpen.PDM.ConfigurationContextBuilderConfigurationDetail @endlink is an alias for @link ConfigurationContextBuilder.ConfigurationDetail NXOpen.PDM.ConfigurationContextBuilder.ConfigurationDetail@endlink
ConfigurationContextBuilderConfigurationDetail = ConfigurationContextBuilder.ConfigurationDetail


##  @link DesignElementRevisionDesignElementCategory NXOpen.PDM.DesignElementRevisionDesignElementCategory @endlink is an alias for @link DesignElementRevision.DesignElementCategory NXOpen.PDM.DesignElementRevision.DesignElementCategory@endlink
DesignElementRevisionDesignElementCategory = DesignElementRevision.DesignElementCategory


##  @link FileManagementFileType NXOpen.PDM.FileManagementFileType @endlink is an alias for @link FileManagement.FileType NXOpen.PDM.FileManagement.FileType@endlink
FileManagementFileType = FileManagement.FileType


##  @link ModelElementRevisionPositioningStatus NXOpen.PDM.ModelElementRevisionPositioningStatus @endlink is an alias for @link ModelElementRevision.PositioningStatus NXOpen.PDM.ModelElementRevision.PositioningStatus@endlink
ModelElementRevisionPositioningStatus = ModelElementRevision.PositioningStatus


##  @link NonMasterDataCopyNonMasterPartsOption NXOpen.PDM.NonMasterDataCopyNonMasterPartsOption @endlink is an alias for @link NonMasterData.CopyNonMasterPartsOption NXOpen.PDM.NonMasterData.CopyNonMasterPartsOption@endlink
NonMasterDataCopyNonMasterPartsOption = NonMasterData.CopyNonMasterPartsOption


##  @link PartBuilderOperation NXOpen.PDM.PartBuilderOperation @endlink is an alias for @link PartBuilder.Operation NXOpen.PDM.PartBuilder.Operation@endlink
PartBuilderOperation = PartBuilder.Operation


## @link PartBuilderPartFileNameData_Struct NXOpen.PDM.PartBuilderPartFileNameData_Struct@endlink is an alias for @link PartBuilder.PartFileNameData NXOpen.PDM.PartBuilder.PartFileNameData@endlink.
PartBuilderPartFileNameData_Struct = PartBuilder.PartFileNameData


## @link PartBuilderPartNumberData_Struct NXOpen.PDM.PartBuilderPartNumberData_Struct@endlink is an alias for @link PartBuilder.PartNumberData NXOpen.PDM.PartBuilder.PartNumberData@endlink.
PartBuilderPartNumberData_Struct = PartBuilder.PartNumberData


## @link PartBuilderPartRevisionData_Struct NXOpen.PDM.PartBuilderPartRevisionData_Struct@endlink is an alias for @link PartBuilder.PartRevisionData NXOpen.PDM.PartBuilder.PartRevisionData@endlink.
PartBuilderPartRevisionData_Struct = PartBuilder.PartRevisionData


##  @link PartFromPartBuilderFileSaveAs NXOpen.PDM.PartFromPartBuilderFileSaveAs @endlink is an alias for @link PartFromPartBuilder.FileSaveAs NXOpen.PDM.PartFromPartBuilder.FileSaveAs@endlink
PartFromPartBuilderFileSaveAs = PartFromPartBuilder.FileSaveAs


## @link PartNameGeneratorPartAssignInputInfo_Struct NXOpen.PDM.PartNameGeneratorPartAssignInputInfo_Struct@endlink is an alias for @link PartNameGenerator.PartAssignInputInfo NXOpen.PDM.PartNameGenerator.PartAssignInputInfo@endlink.
PartNameGeneratorPartAssignInputInfo_Struct = PartNameGenerator.PartAssignInputInfo


##  @link PartOperationBuilderDependentFileSaveAs NXOpen.PDM.PartOperationBuilderDependentFileSaveAs @endlink is an alias for @link PartOperationBuilder.DependentFileSaveAs NXOpen.PDM.PartOperationBuilder.DependentFileSaveAs@endlink
PartOperationBuilderDependentFileSaveAs = PartOperationBuilder.DependentFileSaveAs


##  @link PartOperationBuilderNonMasterSaveAs NXOpen.PDM.PartOperationBuilderNonMasterSaveAs @endlink is an alias for @link PartOperationBuilder.NonMasterSaveAs NXOpen.PDM.PartOperationBuilder.NonMasterSaveAs@endlink
PartOperationBuilderNonMasterSaveAs = PartOperationBuilder.NonMasterSaveAs


##  @link PartOperationBuilderOperationType NXOpen.PDM.PartOperationBuilderOperationType @endlink is an alias for @link PartOperationBuilder.OperationType NXOpen.PDM.PartOperationBuilder.OperationType@endlink
PartOperationBuilderOperationType = PartOperationBuilder.OperationType


##  @link PartOperationCopyBuilderCopyDependentFiles NXOpen.PDM.PartOperationCopyBuilderCopyDependentFiles @endlink is an alias for @link PartOperationCopyBuilder.CopyDependentFiles NXOpen.PDM.PartOperationCopyBuilder.CopyDependentFiles@endlink
PartOperationCopyBuilderCopyDependentFiles = PartOperationCopyBuilder.CopyDependentFiles


##  @link PartOperationCopyBuilderCopyNonMasterParts NXOpen.PDM.PartOperationCopyBuilderCopyNonMasterParts @endlink is an alias for @link PartOperationCopyBuilder.CopyNonMasterParts NXOpen.PDM.PartOperationCopyBuilder.CopyNonMasterParts@endlink
PartOperationCopyBuilderCopyNonMasterParts = PartOperationCopyBuilder.CopyNonMasterParts


##  @link PartOperationCopyBuilderOperationSubType NXOpen.PDM.PartOperationCopyBuilderOperationSubType @endlink is an alias for @link PartOperationCopyBuilder.OperationSubType NXOpen.PDM.PartOperationCopyBuilder.OperationSubType@endlink
PartOperationCopyBuilderOperationSubType = PartOperationCopyBuilder.OperationSubType


##  @link PartOperationCreateBuilderOperationSubType NXOpen.PDM.PartOperationCreateBuilderOperationSubType @endlink is an alias for @link PartOperationCreateBuilder.OperationSubType NXOpen.PDM.PartOperationCreateBuilder.OperationSubType@endlink
PartOperationCreateBuilderOperationSubType = PartOperationCreateBuilder.OperationSubType


##  @link PartOperationImportBuilderCheckoutOptionType NXOpen.PDM.PartOperationImportBuilderCheckoutOptionType @endlink is an alias for @link PartOperationImportBuilder.CheckoutOptionType NXOpen.PDM.PartOperationImportBuilder.CheckoutOptionType@endlink
PartOperationImportBuilderCheckoutOptionType = PartOperationImportBuilder.CheckoutOptionType


##  @link PartOperationImportBuilderConversionRule NXOpen.PDM.PartOperationImportBuilderConversionRule @endlink is an alias for @link PartOperationImportBuilder.ConversionRule NXOpen.PDM.PartOperationImportBuilder.ConversionRule@endlink
PartOperationImportBuilderConversionRule = PartOperationImportBuilder.ConversionRule


##  @link PartOperationImportBuilderExistingPartAction NXOpen.PDM.PartOperationImportBuilderExistingPartAction @endlink is an alias for @link PartOperationImportBuilder.ExistingPartAction NXOpen.PDM.PartOperationImportBuilder.ExistingPartAction@endlink
PartOperationImportBuilderExistingPartAction = PartOperationImportBuilder.ExistingPartAction


##  @link PartOperationImportBuilderNumberingSourceOption NXOpen.PDM.PartOperationImportBuilderNumberingSourceOption @endlink is an alias for @link PartOperationImportBuilder.NumberingSourceOption NXOpen.PDM.PartOperationImportBuilder.NumberingSourceOption@endlink
PartOperationImportBuilderNumberingSourceOption = PartOperationImportBuilder.NumberingSourceOption


##  @link PartOperationImportBuilderPartFamilyTreatment NXOpen.PDM.PartOperationImportBuilderPartFamilyTreatment @endlink is an alias for @link PartOperationImportBuilder.PartFamilyTreatment NXOpen.PDM.PartOperationImportBuilder.PartFamilyTreatment@endlink
PartOperationImportBuilderPartFamilyTreatment = PartOperationImportBuilder.PartFamilyTreatment


##  @link PartOperationImportBuilderValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilderValidationRuleSetFileBrowseOption @endlink is an alias for @link PartOperationImportBuilder.ValidationRuleSetFileBrowseOption NXOpen.PDM.PartOperationImportBuilder.ValidationRuleSetFileBrowseOption@endlink
PartOperationImportBuilderValidationRuleSetFileBrowseOption = PartOperationImportBuilder.ValidationRuleSetFileBrowseOption


##  @link PartOperationImportBuilderValidation NXOpen.PDM.PartOperationImportBuilderValidation @endlink is an alias for @link PartOperationImportBuilder.Validation NXOpen.PDM.PartOperationImportBuilder.Validation@endlink
PartOperationImportBuilderValidation = PartOperationImportBuilder.Validation


##  @link PdmCopyOrEditOperationBuilderCaeRelationTraversalOption NXOpen.PDM.PdmCopyOrEditOperationBuilderCaeRelationTraversalOption @endlink is an alias for @link PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption@endlink
PdmCopyOrEditOperationBuilderCaeRelationTraversalOption = PdmCopyOrEditOperationBuilder.CaeRelationTraversalOption


##  @link PdmCopyOrEditOperationBuilderCloneAction NXOpen.PDM.PdmCopyOrEditOperationBuilderCloneAction @endlink is an alias for @link PdmCopyOrEditOperationBuilder.CloneAction NXOpen.PDM.PdmCopyOrEditOperationBuilder.CloneAction@endlink
PdmCopyOrEditOperationBuilderCloneAction = PdmCopyOrEditOperationBuilder.CloneAction


##  @link PdmCopyOrEditOperationBuilderConversionRule NXOpen.PDM.PdmCopyOrEditOperationBuilderConversionRule @endlink is an alias for @link PdmCopyOrEditOperationBuilder.ConversionRule NXOpen.PDM.PdmCopyOrEditOperationBuilder.ConversionRule@endlink
PdmCopyOrEditOperationBuilderConversionRule = PdmCopyOrEditOperationBuilder.ConversionRule


##  @link PdmCopyOrEditOperationBuilderNumberingSourceOption NXOpen.PDM.PdmCopyOrEditOperationBuilderNumberingSourceOption @endlink is an alias for @link PdmCopyOrEditOperationBuilder.NumberingSourceOption NXOpen.PDM.PdmCopyOrEditOperationBuilder.NumberingSourceOption@endlink
PdmCopyOrEditOperationBuilderNumberingSourceOption = PdmCopyOrEditOperationBuilder.NumberingSourceOption


## @link PdmPartCheckinInput_Struct NXOpen.PDM.PdmPartCheckinInput_Struct@endlink is an alias for @link PdmPart.CheckinInput NXOpen.PDM.PdmPart.CheckinInput@endlink.
PdmPartCheckinInput_Struct = PdmPart.CheckinInput


## @link PdmPartCheckoutInput_Struct NXOpen.PDM.PdmPartCheckoutInput_Struct@endlink is an alias for @link PdmPart.CheckoutInput NXOpen.PDM.PdmPart.CheckoutInput@endlink.
PdmPartCheckoutInput_Struct = PdmPart.CheckoutInput


## @link PdmPartPcaexpressionsInput_Struct NXOpen.PDM.PdmPartPcaexpressionsInput_Struct@endlink is an alias for @link PdmPart.PcaexpressionsInput NXOpen.PDM.PdmPart.PcaexpressionsInput@endlink.
PdmPartPcaexpressionsInput_Struct = PdmPart.PcaexpressionsInput


## @link PdmSessionGetConfiguredRevisionInput_Struct NXOpen.PDM.PdmSessionGetConfiguredRevisionInput_Struct@endlink is an alias for @link PdmSession.GetConfiguredRevisionInput NXOpen.PDM.PdmSession.GetConfiguredRevisionInput@endlink.
PdmSessionGetConfiguredRevisionInput_Struct = PdmSession.GetConfiguredRevisionInput


## @link PdmSessionGetConfiguredRevisionResult_Struct NXOpen.PDM.PdmSessionGetConfiguredRevisionResult_Struct@endlink is an alias for @link PdmSession.GetConfiguredRevisionResult NXOpen.PDM.PdmSession.GetConfiguredRevisionResult@endlink.
PdmSessionGetConfiguredRevisionResult_Struct = PdmSession.GetConfiguredRevisionResult


##  @link SearchFilterTermType NXOpen.PDM.SearchFilterTermType @endlink is an alias for @link SearchFilterTerm.Type NXOpen.PDM.SearchFilterTerm.Type@endlink
SearchFilterTermType = SearchFilterTerm.Type


##  @link SearchRecipeFilterBuilderRecipeLogicValue NXOpen.PDM.SearchRecipeFilterBuilderRecipeLogicValue @endlink is an alias for @link SearchRecipeFilterBuilder.RecipeLogicValue NXOpen.PDM.SearchRecipeFilterBuilder.RecipeLogicValue@endlink
SearchRecipeFilterBuilderRecipeLogicValue = SearchRecipeFilterBuilder.RecipeLogicValue


##  @link SearchRecipeFilterBuilderVolumeTypeValue NXOpen.PDM.SearchRecipeFilterBuilderVolumeTypeValue @endlink is an alias for @link SearchRecipeFilterBuilder.VolumeTypeValue NXOpen.PDM.SearchRecipeFilterBuilder.VolumeTypeValue@endlink
SearchRecipeFilterBuilderVolumeTypeValue = SearchRecipeFilterBuilder.VolumeTypeValue


##  @link SmartSaveBuilderDialogType NXOpen.PDM.SmartSaveBuilderDialogType @endlink is an alias for @link SmartSaveBuilder.DialogType NXOpen.PDM.SmartSaveBuilder.DialogType@endlink
SmartSaveBuilderDialogType = SmartSaveBuilder.DialogType


##  @link SmartSaveBuilderSaveType NXOpen.PDM.SmartSaveBuilderSaveType @endlink is an alias for @link SmartSaveBuilder.SaveType NXOpen.PDM.SmartSaveBuilder.SaveType@endlink
SmartSaveBuilderSaveType = SmartSaveBuilder.SaveType


##  @link SmartSaveObjectOperationType NXOpen.PDM.SmartSaveObjectOperationType @endlink is an alias for @link SmartSaveObject.OperationType NXOpen.PDM.SmartSaveObject.OperationType@endlink
SmartSaveObjectOperationType = SmartSaveObject.OperationType


## @link VolumeSearchFilterTermBoundingBox_Struct NXOpen.PDM.VolumeSearchFilterTermBoundingBox_Struct@endlink is an alias for @link VolumeSearchFilterTerm.BoundingBox NXOpen.PDM.VolumeSearchFilterTerm.BoundingBox@endlink.
VolumeSearchFilterTermBoundingBox_Struct = VolumeSearchFilterTerm.BoundingBox


##  @link VolumeSearchFilterTermOperator NXOpen.PDM.VolumeSearchFilterTermOperator @endlink is an alias for @link VolumeSearchFilterTerm.Operator NXOpen.PDM.VolumeSearchFilterTerm.Operator@endlink
VolumeSearchFilterTermOperator = VolumeSearchFilterTerm.Operator


