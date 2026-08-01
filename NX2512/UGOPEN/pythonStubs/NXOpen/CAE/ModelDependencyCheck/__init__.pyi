from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Manager(NXOpen.Object): 
    """  The Model Dependency Check Utilities class offers means for utilities methods  """
    def AutoResolveAllResults() -> None:
        """
         Auto resolve all results
        """
        pass
    def AutoResolveSubsetResults(resultsToResolve: List[Result]) -> None:
        """
         Auto resolve subset of results
        """
        pass
    def ExportResults(resultsFile: str) -> None:
        """
         Export results in txt file
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
    def GetResults() -> List[Result]:
        """
         Get results obtained from the latest check
         Returns results ( Result List[NXOpen.CAE.Mo): .
        """
        pass
    def PerformCheck() -> None:
        """
         Performs check to find dependency model conflicts
        """
        pass
import NXOpen
import NXOpen.CAE
class Result(NXOpen.NXObject): 
    """  The Model Dependency Check Result class offers informations about the conflicts found. """
    @property
    def FirstElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: ( NXOpen.CAE.FEElement) FirstElement
         Returns the first element   
            
         
        """
        pass
    @property
    def FirstMesh(self) -> NXOpen.CAE.Mesh:
        """
        Getter for property: ( NXOpen.CAE.Mesh) FirstMesh
         Returns the first mesh   
            
         
        """
        pass
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
         Returns the id   
            
         
        """
        pass
    @property
    def SecondElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: ( NXOpen.CAE.FEElement) SecondElement
         Returns the second element   
            
         
        """
        pass
    @property
    def SecondMesh(self) -> NXOpen.CAE.Mesh:
        """
        Getter for property: ( NXOpen.CAE.Mesh) SecondMesh
         Returns the second mesh   
            
         
        """
        pass
    def GetConflictingDofs(self) -> List[int]:
        """
         Get the conflicting dofs 
         Returns pDofs (List[int]): .
        """
        pass
    def GetConflictingNodes(self) -> List[NXOpen.CAE.FENode]:
        """
         Get the conflicting nodes 
         Returns pNodes ( NXOpen.CAE.FENode Li): .
        """
        pass
