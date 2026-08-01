from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class ContactObjectCollection(NXOpen.TaggedObjectCollection): 
    """  The ContactPreview Manager class offers means to edit NXOpen.CAE.ContactPreview.ContactObjectCollection   """
    def ChangeFolderOrganization(folderType: int) -> None:
        """
         Change folder organization
        """
        pass
    def ClearCollection() -> None:
        """
         Delete object
        """
        pass
    def EnableCalculations(enabled: bool) -> None:
        """
         DisableEnable Calculations
        """
        pass
    def FindObject(journal_identifier: str) -> NXOpen.INXObject:
        """
         Finds the  NXOpen.INXObject  with the given identifier as recorded in a journal. 
                    An object may not return the same value as its JournalIdentifier in different versions of 
                    the software. However newer versions of the software should find the same object when 
                    FindObject is passed older versions of its journal identifier. In general, this method 
                    should not be used in handwritten code and exists to support record and playback of journals.
                    An exception will be thrown if no object can be found with the given journal identifier. 
         Returns found ( NXOpen.INXObject):  An object matching the journal identifier .
        """
        pass
    def PlotContactLinesWithView(viewIndex: int, pObjects: List[ContactObject]) -> None:
        """
         Contour plot 
        """
        pass
    def PlotContours(viewIndex: int, pObjects: List[ContactObject]) -> None:
        """
         Contour plot 
        """
        pass
    def Populate() -> None:
        """
         Populate contacts and generate preview 
        """
        pass
    def Print() -> None:
        """
         Print Information 
        """
        pass
    def RefreshResults(pObjects: List[ContactObject]) -> None:
        """
         Refresh results object
        """
        pass
import NXOpen
class ContactObject(NXOpen.NXObject): 
    """  The ContactPreview ContactObject class offers means to delete, and edit NXOpen.CAE.ContactPreview.ContactObject instances. """
    def DeleteResultObject(self) -> None:
        """
         Delete object
        """
        pass
import NXOpen
class SettingsBuilder(NXOpen.Builder): 
    """ Represents a CAE.ContactPreview.SettingsBuilder builder """
    class ContactSideOptions(Enum):
        """
        Members Include: 
         |Both|  
         |Contact|  
         |Target| 

        """
        Both: int
        Contact: int
        Target: int
        @staticmethod
        def ValueOf(value: int) -> SettingsBuilder.ContactSideOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ContactSide(self) -> SettingsBuilder.ContactSideOptions:
        """
        Getter for property: ( SettingsBuilder.ContactSideOptions NXOpen.CAE.C) ContactSide
         Returns the selection type   
            
         
        """
        pass
    @ContactSide.setter
    def ContactSide(self, selectionType: SettingsBuilder.ContactSideOptions):
        """
        Setter for property: ( SettingsBuilder.ContactSideOptions NXOpen.CAE.C) ContactSide
         Returns the selection type   
            
         
        """
        pass
