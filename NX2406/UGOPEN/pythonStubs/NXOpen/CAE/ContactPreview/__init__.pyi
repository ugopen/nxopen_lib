from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   @brief  The ContactPreview Manager class offers means to edit @link NXOpen::CAE::ContactPreview::ContactObjectCollection NXOpen::CAE::ContactPreview::ContactObjectCollection@endlink    
## 
##    <br> To obtain an instance of this class, refer to @link NXOpen::CAE::CaeSession  NXOpen::CAE::CaeSession @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ContactObjectCollection(NXOpen.TaggedObjectCollection): 
    """ <summary> The ContactPreview Manager class offers means to edit <ja_class>NXOpen.CAE.ContactPreview.ContactObjectCollection</ja_class>  </summary> """


    ##  Change folder organization
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    ## <param name="folderType"> (int) </param>
    def ChangeFolderOrganization(folderType: int) -> None:
        """
         Change folder organization
        """
        pass
    
    ##  Delete object
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def ClearCollection() -> None:
        """
         Delete object
        """
        pass
    
    ##  Disable/Enable Calculations
    ## 
    ##   <br>  Created in NX2306.0.0  <br> 

    ## License requirements: None.
    ## <param name="enabled"> (bool) </param>
    def EnableCalculations(enabled: bool) -> None:
        """
         Disable/Enable Calculations
        """
        pass
    
    ##  Finds the @link  NXOpen::INXObject   NXOpen::INXObject @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="journal_identifier"> (str)  Journal identifier of the object </param>
    def FindObject(journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the @link  NXOpen::INXObject   NXOpen::INXObject @endlink  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
        
                    An exception will be thrown if no object can be found with the given journal identifier. 
         @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier .
        """
        pass
    
    ##  Contour plot 
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## <param name="viewIndex"> (int) </param>
    ## <param name="pObjects"> (@link ContactObject List[NXOpen.CAE.ContactPreview.ContactObject]@endlink)  The objects to be used by the actions. </param>
    def PlotContactLinesWithView(viewIndex: int, pObjects: List[ContactObject]) -> None:
        """
         Contour plot 
        """
        pass
    
    ##  Contour plot 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="viewIndex"> (int) </param>
    ## <param name="pObjects"> (@link ContactObject List[NXOpen.CAE.ContactPreview.ContactObject]@endlink)  The objects to be used by the actions. </param>
    def PlotContours(viewIndex: int, pObjects: List[ContactObject]) -> None:
        """
         Contour plot 
        """
        pass
    
    ##  Populate contacts and generate preview 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def Populate() -> None:
        """
         Populate contacts and generate preview 
        """
        pass
    
    ##  Print Information 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def Print() -> None:
        """
         Print Information 
        """
        pass
    
    ##  Refresh results object
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="pObjects"> (@link ContactObject List[NXOpen.CAE.ContactPreview.ContactObject]@endlink)  The objects to be used by the actions. </param>
    def RefreshResults(pObjects: List[ContactObject]) -> None:
        """
         Refresh results object
        """
        pass
    
import NXOpen
##   @brief  The ContactPreview ContactObject class offers means to delete, and edit @link NXOpen::CAE::ContactPreview::ContactObject NXOpen::CAE::ContactPreview::ContactObject@endlink  instances. 
## 
##    <br> Instances of this object can be accessed from @link NXOpen::CAE::ContactPreview::ContactObjectCollection NXOpen::CAE::ContactPreview::ContactObjectCollection@endlink   <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class ContactObject(NXOpen.NXObject): 
    """ <summary> The ContactPreview ContactObject class offers means to delete, and edit <ja_class>NXOpen.CAE.ContactPreview.ContactObject</ja_class> instances.</summary> """


    ##  Delete object
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    def DeleteResultObject(self) -> None:
        """
         Delete object
        """
        pass
    
import NXOpen
##  Represents a @link CAE::ContactPreview::SettingsBuilder CAE::ContactPreview::SettingsBuilder@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::CaePart::CreateContactPreviewSettingsBuilder  NXOpen::CAE::CaePart::CreateContactPreviewSettingsBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## ContactSide </term> <description> 
##  
## Both </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2007.0.0  <br> 

class SettingsBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>CAE.ContactPreview.SettingsBuilder</ja_class> builder """


    ##  The selection types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Both</term><description> 
    ##  </description> </item><item><term> 
    ## Contact</term><description> 
    ##  </description> </item><item><term> 
    ## Target</term><description> 
    ## </description> </item></list>
    class ContactSideOptions(Enum):
        """
        Members Include: <Both> <Contact> <Target>
        """
        Both: int
        Contact: int
        Target: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> SettingsBuilder.ContactSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link SettingsBuilder.ContactSideOptions NXOpen.CAE.ContactPreview.SettingsBuilder.ContactSideOptions@endlink) ContactSide
    ##  Returns the selection type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return SettingsBuilder.ContactSideOptions
    @property
    def ContactSide(self) -> SettingsBuilder.ContactSideOptions:
        """
        Getter for property: (@link SettingsBuilder.ContactSideOptions NXOpen.CAE.ContactPreview.SettingsBuilder.ContactSideOptions@endlink) ContactSide
         Returns the selection type   
            
         
        """
        pass
    
    ## Setter for property: (@link SettingsBuilder.ContactSideOptions NXOpen.CAE.ContactPreview.SettingsBuilder.ContactSideOptions@endlink) ContactSide

    ##  Returns the selection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ContactSide.setter
    def ContactSide(self, selectionType: SettingsBuilder.ContactSideOptions):
        """
        Setter for property: (@link SettingsBuilder.ContactSideOptions NXOpen.CAE.ContactPreview.SettingsBuilder.ContactSideOptions@endlink) ContactSide
         Returns the selection type   
            
         
        """
        pass
    
## @package NXOpen.CAE.ContactPreview
## Classes, Enums and Structs under NXOpen.CAE.ContactPreview namespace

##  @link SettingsBuilderContactSideOptions NXOpen.CAE.ContactPreview.SettingsBuilderContactSideOptions @endlink is an alias for @link SettingsBuilder.ContactSideOptions NXOpen.CAE.ContactPreview.SettingsBuilder.ContactSideOptions@endlink
SettingsBuilderContactSideOptions = SettingsBuilder.ContactSideOptions


