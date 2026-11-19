from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##   @brief  The Model Dependency Check Utilities class offers means for utilities methods  
## 
##    <br> To obtain an instance of this class use @link NXOpen::CAE::CaeSession::ModelDependencyCheckManager NXOpen::CAE::CaeSession::ModelDependencyCheckManager@endlink .  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Manager(NXOpen.Object): 
    """ <summary> The Model Dependency Check Utilities class offers means for utilities methods </summary> """


    ##  Auto resolve all results
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def AutoResolveAllResults() -> None:
        """
         Auto resolve all results
        """
        pass
    
    ##  Auto resolve subset of results
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultsToResolve"> (@link Result List[NXOpen.CAE.ModelDependencyCheck.Result]@endlink) </param>
    @staticmethod
    def AutoResolveSubsetResults(resultsToResolve: List[Result]) -> None:
        """
         Auto resolve subset of results
        """
        pass
    
    ##  Export results in txt file
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="resultsFile"> (str) </param>
    @staticmethod
    def ExportResults(resultsFile: str) -> None:
        """
         Export results in txt file
        """
        pass
    
    ##  Finds the @link  NXOpen::INXObject   NXOpen::INXObject @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    @staticmethod
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
    
    ##  Get results obtained from the latest check
    ##  @return results (@link Result List[NXOpen.CAE.ModelDependencyCheck.Result]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetResults() -> List[Result]:
        """
         Get results obtained from the latest check
         @return results (@link Result List[NXOpen.CAE.ModelDependencyCheck.Result]@endlink): .
        """
        pass
    
    ##  Performs check to find dependency model conflicts
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def PerformCheck() -> None:
        """
         Performs check to find dependency model conflicts
        """
        pass
    
import NXOpen
import NXOpen.CAE
##   @brief  The Model Dependency Check Result class offers informations about the conflicts found. 
## 
##    <br> Results can be obtained from @link CAE::ModelDependencyCheck::Manager CAE::ModelDependencyCheck::Manager@endlink  after checks have been performed via @link NXOpen::CAE::ModelDependencyCheck::Manager::GetResults NXOpen::CAE::ModelDependencyCheck::Manager::GetResults@endlink .  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class Result(NXOpen.NXObject): 
    """ <summary> The Model Dependency Check Result class offers informations about the conflicts found.</summary> """


    ## Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) FirstElement
    ##   the first element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CAE.FEElement
    @property
    def FirstElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) FirstElement
          the first element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.Mesh NXOpen.CAE.Mesh@endlink) FirstMesh
    ##   the first mesh   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CAE.Mesh
    @property
    def FirstMesh(self) -> NXOpen.CAE.Mesh:
        """
        Getter for property: (@link NXOpen.CAE.Mesh NXOpen.CAE.Mesh@endlink) FirstMesh
          the first mesh   
            
         
        """
        pass
    
    ## Getter for property: (str) Id
    ##   the id   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return str
    @property
    def Id(self) -> str:
        """
        Getter for property: (str) Id
          the id   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SecondElement
    ##   the second element   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CAE.FEElement
    @property
    def SecondElement(self) -> NXOpen.CAE.FEElement:
        """
        Getter for property: (@link NXOpen.CAE.FEElement NXOpen.CAE.FEElement@endlink) SecondElement
          the second element   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.Mesh NXOpen.CAE.Mesh@endlink) SecondMesh
    ##   the second mesh   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.CAE.Mesh
    @property
    def SecondMesh(self) -> NXOpen.CAE.Mesh:
        """
        Getter for property: (@link NXOpen.CAE.Mesh NXOpen.CAE.Mesh@endlink) SecondMesh
          the second mesh   
            
         
        """
        pass
    
    ##  Get the conflicting dofs 
    ##  @return pDofs (List[int]): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConflictingDofs(pResult: Result) -> List[int]:
        """
         Get the conflicting dofs 
         @return pDofs (List[int]): .
        """
        pass
    
    ##  Get the conflicting nodes 
    ##  @return pNodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def GetConflictingNodes(pResult: Result) -> List[NXOpen.CAE.FENode]:
        """
         Get the conflicting nodes 
         @return pNodes (@link NXOpen.CAE.FENode List[NXOpen.CAE.FENode]@endlink): .
        """
        pass
    
## @package NXOpen.CAE.ModelDependencyCheck
## Classes, Enums and Structs under NXOpen.CAE.ModelDependencyCheck namespace

