from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents a @link CAE::PenetrationCheck::AddSet CAE::PenetrationCheck::AddSet@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::CaePart::CreatePenetrationCheckAddSetBuilder  NXOpen::CAE::CaePart::CreatePenetrationCheckAddSetBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## BoundaryType </term> <description> 
##  
## Sharp </description> </item> 
## 
## <item><term> 
##  
## ElemThickness.Value </term> <description> 
##  
## 10 (millimeters part), 2.5 (inches part) </description> </item> 
## 
## <item><term> 
##  
## InterferenceBetween </term> <description> 
##  
## MeshCollectorContainers </description> </item> 
## 
## <item><term> 
##  
## InterferenceOption </term> <description> 
##  
## All </description> </item> 
## 
## <item><term> 
##  
## SelectionType </term> <description> 
##  
## MeshObjects </description> </item> 
## 
## <item><term> 
##  
## SelfInterferenceOption </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ThicknessFactor.Value </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## ThicknessSource </term> <description> 
##  
## ElementAssociatedData </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class AddSetBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>CAE.PenetrationCheck.AddSet</ja_class> builder """


    ##  the interference between types 
    ##  
    class InterferenceBetweenType(Enum):
        """
        Members Include: <MeshCollectorContainers> <Meshes> <ComponentFEMs>
        """
        MeshCollectorContainers: int
        Meshes: int
        ComponentFEMs: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.InterferenceBetweenType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the intereference types 
    ##  
    class InterferenceType(Enum):
        """
        Members Include: <All> <Intersections> <Penetrations>
        """
        All: int
        Intersections: int
        Penetrations: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.InterferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  The selection types 
    ##  
    class SelectionTypeOptions(Enum):
        """
        Members Include: <MeshObjects> <ContactDefinitions>
        """
        MeshObjects: int
        ContactDefinitions: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.SelectionTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the edge discretization types 
    ##  
    class ThicknessBoundaryType(Enum):
        """
        Members Include: <Sharp> <Round>
        """
        Sharp: int
        Round: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.ThicknessBoundaryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  the thickness definition types 
    ##  
    class ThicknessSourceType(Enum):
        """
        Members Include: <ElementAssociatedData> <UserDefined>
        """
        ElementAssociatedData: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.ThicknessSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link AddSetBuilder.ThicknessBoundaryType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessBoundaryType@endlink) BoundaryType
    ##   the interference option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddSetBuilder.ThicknessBoundaryType
    @property
    def BoundaryType(self) -> AddSetBuilder.ThicknessBoundaryType:
        """
        Getter for property: (@link AddSetBuilder.ThicknessBoundaryType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessBoundaryType@endlink) BoundaryType
          the interference option   
            
         
        """
        pass
    
    ## Setter for property: (@link AddSetBuilder.ThicknessBoundaryType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessBoundaryType@endlink) BoundaryType

    ##   the interference option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @BoundaryType.setter
    def BoundaryType(self, boundaryOption: AddSetBuilder.ThicknessBoundaryType):
        """
        Setter for property: (@link AddSetBuilder.ThicknessBoundaryType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessBoundaryType@endlink) BoundaryType
          the interference option   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ElemThickness
    ##   the elem thickness   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ElemThickness(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ElemThickness
          the elem thickness   
            
         
        """
        pass
    
    ## Getter for property: (@link AddSetBuilder.InterferenceBetweenType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceBetweenType@endlink) InterferenceBetween
    ##   the interference between   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddSetBuilder.InterferenceBetweenType
    @property
    def InterferenceBetween(self) -> AddSetBuilder.InterferenceBetweenType:
        """
        Getter for property: (@link AddSetBuilder.InterferenceBetweenType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceBetweenType@endlink) InterferenceBetween
          the interference between   
            
         
        """
        pass
    
    ## Setter for property: (@link AddSetBuilder.InterferenceBetweenType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceBetweenType@endlink) InterferenceBetween

    ##   the interference between   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InterferenceBetween.setter
    def InterferenceBetween(self, interferenceBetween: AddSetBuilder.InterferenceBetweenType):
        """
        Setter for property: (@link AddSetBuilder.InterferenceBetweenType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceBetweenType@endlink) InterferenceBetween
          the interference between   
            
         
        """
        pass
    
    ## Getter for property: (@link AddSetBuilder.InterferenceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceType@endlink) InterferenceOption
    ##   the interference option   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddSetBuilder.InterferenceType
    @property
    def InterferenceOption(self) -> AddSetBuilder.InterferenceType:
        """
        Getter for property: (@link AddSetBuilder.InterferenceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceType@endlink) InterferenceOption
          the interference option   
            
         
        """
        pass
    
    ## Setter for property: (@link AddSetBuilder.InterferenceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceType@endlink) InterferenceOption

    ##   the interference option   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @InterferenceOption.setter
    def InterferenceOption(self, interferenceOption: AddSetBuilder.InterferenceType):
        """
        Setter for property: (@link AddSetBuilder.InterferenceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceType@endlink) InterferenceOption
          the interference option   
            
         
        """
        pass
    
    ## Getter for property: (str) PenetrationSetName
    ##   the clearance set name.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return str
    @property
    def PenetrationSetName(self) -> str:
        """
        Getter for property: (str) PenetrationSetName
          the clearance set name.  
             
         
        """
        pass
    
    ## Setter for property: (str) PenetrationSetName

    ##   the clearance set name.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PenetrationSetName.setter
    def PenetrationSetName(self, setName: str):
        """
        Setter for property: (str) PenetrationSetName
          the clearance set name.  
             
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Selection
    ##   the selection   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def Selection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) Selection
          the selection   
            
         
        """
        pass
    
    ## Getter for property: (@link AddSetBuilder.SelectionTypeOptions NXOpen.CAE.PenetrationCheck.AddSetBuilder.SelectionTypeOptions@endlink) SelectionType
    ##   the selection type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddSetBuilder.SelectionTypeOptions
    @property
    def SelectionType(self) -> AddSetBuilder.SelectionTypeOptions:
        """
        Getter for property: (@link AddSetBuilder.SelectionTypeOptions NXOpen.CAE.PenetrationCheck.AddSetBuilder.SelectionTypeOptions@endlink) SelectionType
          the selection type   
            
         
        """
        pass
    
    ## Setter for property: (@link AddSetBuilder.SelectionTypeOptions NXOpen.CAE.PenetrationCheck.AddSetBuilder.SelectionTypeOptions@endlink) SelectionType

    ##   the selection type   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SelectionType.setter
    def SelectionType(self, selectionType: AddSetBuilder.SelectionTypeOptions):
        """
        Setter for property: (@link AddSetBuilder.SelectionTypeOptions NXOpen.CAE.PenetrationCheck.AddSetBuilder.SelectionTypeOptions@endlink) SelectionType
          the selection type   
            
         
        """
        pass
    
    ## Getter for property: (bool) SelfInterferenceOption
    ##   the self interference toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def SelfInterferenceOption(self) -> bool:
        """
        Getter for property: (bool) SelfInterferenceOption
          the self interference toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) SelfInterferenceOption

    ##   the self interference toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @SelfInterferenceOption.setter
    def SelfInterferenceOption(self, selfInterferenceOption: bool):
        """
        Setter for property: (bool) SelfInterferenceOption
          the self interference toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessFactor
    ##   the scaling factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ThicknessFactor(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ThicknessFactor
          the scaling factor   
            
         
        """
        pass
    
    ## Getter for property: (@link AddSetBuilder.ThicknessSourceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessSourceType@endlink) ThicknessSource
    ##   the thickness source   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AddSetBuilder.ThicknessSourceType
    @property
    def ThicknessSource(self) -> AddSetBuilder.ThicknessSourceType:
        """
        Getter for property: (@link AddSetBuilder.ThicknessSourceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessSourceType@endlink) ThicknessSource
          the thickness source   
            
         
        """
        pass
    
    ## Setter for property: (@link AddSetBuilder.ThicknessSourceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessSourceType@endlink) ThicknessSource

    ##   the thickness source   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ThicknessSource.setter
    def ThicknessSource(self, thicknessSource: AddSetBuilder.ThicknessSourceType):
        """
        Setter for property: (@link AddSetBuilder.ThicknessSourceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessSourceType@endlink) ThicknessSource
          the thickness source   
            
         
        """
        pass
    
import NXOpen
##   @brief  Represents a PenetrationCheck  
## 
##    <br> To create or edit an instance of this class, use @link NXOpen::CAE::PenetrationCheck::AddSetBuilder  NXOpen::CAE::PenetrationCheck::AddSetBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AddSet(NXOpen.DisplayableObject): 
    """ <summary> Represents a PenetrationCheck </summary> """
    pass


import NXOpen
##   @brief  The Penetration Check AnalysisSet class offers means to delete, create, edit, and switch @link NXOpen::CAE::PenetrationCheck::AnalysisSet NXOpen::CAE::PenetrationCheck::AnalysisSet@endlink  instances. 
## 
##    <br> Currently we don't support KF at this time.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AnalysisSet(NXOpen.NXObject): 
    """ <summary> The Penetration Check AnalysisSet class offers means to delete, create, edit, and switch <ja_class>NXOpen.CAE.PenetrationCheck.AnalysisSet</ja_class> instances.</summary> """


    ##  Set this clearance set as active
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def ChangeActiveSet(analysisSet: AnalysisSet) -> None:
        """
         Set this clearance set as active
        """
        pass
    
    ##  Delete this clearance set 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeleteSet(analysisSet: AnalysisSet) -> None:
        """
         Delete this clearance set 
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
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    def FindObject(objectValue: AnalysisSet, journal_identifier: str) -> NXOpen.INXObject:
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
    
    ##  Set this clearance set as active
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="viewIndex"> (int) </param>
    def PlotContours(analysisSet: AnalysisSet, viewIndex: int) -> None:
        """
         Set this clearance set as active
        """
        pass
    
    ##  Print autotest XML data
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def Print(analysisSet: AnalysisSet) -> None:
        """
         Print autotest XML data
        """
        pass
    
    ##  Set this clearance set as active
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def RunInterferenceCheck(analysisSet: AnalysisSet) -> None:
        """
         Set this clearance set as active
        """
        pass
    
import NXOpen
##  Represents a @link CAE::PenetrationCheck::AutomaticResolve CAE::PenetrationCheck::AutomaticResolve@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::CAE::CaePart::CreatePenetrationCheckAutomaticResolveBuilder  NXOpen::CAE::CaePart::CreatePenetrationCheckAutomaticResolveBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## MaxInterference.Value </term> <description> 
##  
## 0.5 </description> </item> 
## 
## <item><term> 
##  
## MinInterference.Value </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## ResolveOptions </term> <description> 
##  
## All </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class AutomaticResolveBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>CAE.PenetrationCheck.AutomaticResolve</ja_class> builder """


    ##  resolve types 
    ##  
    class ResolveType(Enum):
        """
        Members Include: <All> <WithinLimits>
        """
        All: int
        WithinLimits: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> AutomaticResolveBuilder.ResolveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxInterference
    ##   the max interference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MaxInterference(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MaxInterference
          the max interference   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MeshesToFreeze
    ##   the selection for freezing meshes from translate  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectNXObjectList
    @property
    def MeshesToFreeze(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: (@link NXOpen.SelectNXObjectList NXOpen.SelectNXObjectList@endlink) MeshesToFreeze
          the selection for freezing meshes from translate  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinInterference
    ##   the min interference   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def MinInterference(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) MinInterference
          the min interference   
            
         
        """
        pass
    
    ## Getter for property: (@link AutomaticResolveBuilder.ResolveType NXOpen.CAE.PenetrationCheck.AutomaticResolveBuilder.ResolveType@endlink) ResolveOptions
    ##   the resolve options   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AutomaticResolveBuilder.ResolveType
    @property
    def ResolveOptions(self) -> AutomaticResolveBuilder.ResolveType:
        """
        Getter for property: (@link AutomaticResolveBuilder.ResolveType NXOpen.CAE.PenetrationCheck.AutomaticResolveBuilder.ResolveType@endlink) ResolveOptions
          the resolve options   
            
         
        """
        pass
    
    ## Setter for property: (@link AutomaticResolveBuilder.ResolveType NXOpen.CAE.PenetrationCheck.AutomaticResolveBuilder.ResolveType@endlink) ResolveOptions

    ##   the resolve options   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ResolveOptions.setter
    def ResolveOptions(self, resolveOptions: AutomaticResolveBuilder.ResolveType):
        """
        Setter for property: (@link AutomaticResolveBuilder.ResolveType NXOpen.CAE.PenetrationCheck.AutomaticResolveBuilder.ResolveType@endlink) ResolveOptions
          the resolve options   
            
         
        """
        pass
    
    ##  TODO: fill in a description for this 
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_masterfem ("Finite Element Modeling")
    @staticmethod
    def ResolveButton(builder: AutomaticResolveBuilder) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    
import NXOpen
##   @brief  Represents a PenetrationCheck  
## 
##    <br> To create or edit an instance of this class, use @link NXOpen::CAE::PenetrationCheck::AutomaticResolveBuilder  NXOpen::CAE::PenetrationCheck::AutomaticResolveBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class AutomaticResolve(NXOpen.DisplayableObject): 
    """ <summary> Represents a PenetrationCheck </summary> """
    pass


import NXOpen
##   @brief  The Quality Audit Manager class offers means to check for errors at assembly level  
## 
##    <br> To obtain an instance of this class use @link NXOpen::CAE::CaeSession::PenetrationCheckManager NXOpen::CAE::CaeSession::PenetrationCheckManager@endlink .  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class Manager(NXOpen.Object): 
    """ <summary> The Quality Audit Manager class offers means to check for errors at assembly level </summary> """


    ## Getter for property: (@link AnalysisSet NXOpen.CAE.PenetrationCheck.AnalysisSet@endlink) ActiveSet
    ##   the quality audit action list.  
    ##   
    ##                
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return AnalysisSet
    @property
    def ActiveSet(self) -> AnalysisSet:
        """
        Getter for property: (@link AnalysisSet NXOpen.CAE.PenetrationCheck.AnalysisSet@endlink) ActiveSet
          the quality audit action list.  
          
                       
         
        """
        pass
    
    ##  Delete object
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="num"> (int) </param>
    @staticmethod
    def ClearManager(num: int) -> None:
        """
         Delete object
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
    ##   <br>  Created in NX1926.0.0  <br> 

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
    
    ##  Contour plot
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The objects to be used by the actions. 
    def PlotContours(viewIndex: int, pObjects: List[ResultObject]) -> None:
        """
         Contour plot
        """
        pass
    
    ##  Refresh results object
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The objects to be used by the actions. 
    @staticmethod
    def RefreshResults(pObjects: List[ResultObject]) -> None:
        """
         Refresh results object
        """
        pass
    
    ##  Refresh results object
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  The objects to be used by the actions. 
    @staticmethod
    def ResultObjectAutomaticResolve(pObjects: List[ResultObject]) -> None:
        """
         Refresh results object
        """
        pass
    
import NXOpen
##   @brief  The Penetration Check AnalysisSet class offers means to find @link NXOpen::CAE::PenetrationCheck::ResultObject NXOpen::CAE::PenetrationCheck::ResultObject@endlink  instances. 
## 
##    <br> Currently we don't support KF at this time.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ResultList(NXOpen.NXObject): 
    """ <summary> The Penetration Check AnalysisSet class offers means to find <ja_class>NXOpen.CAE.PenetrationCheck.ResultObject</ja_class> instances.</summary> """


    ##  Finds the @link  NXOpen::INXObject   NXOpen::INXObject @endlink  with the given identifier as recorded in a journal. 
    ##             An object may not return the same value as its JournalIdentifier in different versions of 
    ##             the software. However newer versions of the software should find the same object when 
    ##             FindObject is passed older versions of its journal identifier. In general, this method 
    ##             should not be used in handwritten code and exists to support record and playback of journals.
    ## 
    ##             An exception will be thrown if no object can be found with the given journal identifier. 
    ##  @return found (@link NXOpen.INXObject NXOpen.INXObject@endlink):  An object matching the journal identifier .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ##  Journal identifier of the object 
    def FindObject(objectValue: ResultList, journal_identifier: str) -> NXOpen.INXObject:
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
    
import NXOpen
##   @brief  The Penetration Check AnalysisSet class offers means to delete, and edit @link NXOpen::CAE::PenetrationCheck::ResultObject NXOpen::CAE::PenetrationCheck::ResultObject@endlink  instances. 
## 
##    <br> Currently we don't support KF at this time.  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class ResultObject(NXOpen.NXObject): 
    """ <summary> The Penetration Check AnalysisSet class offers means to delete, and edit <ja_class>NXOpen.CAE.PenetrationCheck.ResultObject</ja_class> instances.</summary> """


    ##  Delete object
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    @staticmethod
    def DeleteResultObject(pSelfResult: ResultObject) -> None:
        """
         Delete object
        """
        pass
    
    ##  Set freeze mesh component
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="compToFreeze"> (int) </param>
    def FreezeComponent(pSelfResult: ResultObject, compToFreeze: int) -> None:
        """
         Set freeze mesh component
        """
        pass
    
import NXOpen
import NXOpen.CAE
## 
##         Represents a @link NXOpen::CAE::PenetrationCheck::TranslateNodesBuilder NXOpen::CAE::PenetrationCheck::TranslateNodesBuilder@endlink 
##          <br> To create a new instance of this class, use @link NXOpen::CAE::CaePart::CreatePenetrationCheckTranslateNodesBuilder  NXOpen::CAE::CaePart::CreatePenetrationCheckTranslateNodesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Distance.Value </term> <description> 
##  
## 1 (millimeters part), 1 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Method </term> <description> 
##  
## AlongNodeNormals </description> </item> 
## 
## <item><term> 
##  
## MoveAdjacentNodes </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## NumberOfLayers.Value </term> <description> 
##  
## 3 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1926.0.0  <br> 

class TranslateNodesBuilder(NXOpen.Builder): 
    """
        Represents a <ja_class>NXOpen.CAE.PenetrationCheck.TranslateNodesBuilder</ja_class>
        """


    ##  the translate method options
    ##  
    class MethodOptions(Enum):
        """
        Members Include: <AlongNodeNormals> <OppositeofNodeNormals> <AlongDirection> <WithOrientation> <PointToPoint> <AlignVectors> <ScaleModel>
        """
        AlongNodeNormals: int
        OppositeofNodeNormals: int
        AlongDirection: int
        WithOrientation: int
        PointToPoint: int
        AlignVectors: int
        ScaleModel: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TranslateNodesBuilder.MethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
    ##   the csys   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CoordinateSystem
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys

    ##   the csys   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: (@link NXOpen.CoordinateSystem NXOpen.CoordinateSystem@endlink) Csys
          the csys   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
    ##   the direction vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def DirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
          the direction vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector

    ##   the direction vector   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @DirectionVector.setter
    def DirectionVector(self, directionVector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) DirectionVector
          the direction vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
    ##   the distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) Distance
          the distance   
            
         
        """
        pass
    
    ## Getter for property: (@link TranslateNodesBuilder.MethodOptions NXOpen.CAE.PenetrationCheck.TranslateNodesBuilder.MethodOptions@endlink) Method
    ##   the method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TranslateNodesBuilder.MethodOptions
    @property
    def Method(self) -> TranslateNodesBuilder.MethodOptions:
        """
        Getter for property: (@link TranslateNodesBuilder.MethodOptions NXOpen.CAE.PenetrationCheck.TranslateNodesBuilder.MethodOptions@endlink) Method
          the method   
            
         
        """
        pass
    
    ## Setter for property: (@link TranslateNodesBuilder.MethodOptions NXOpen.CAE.PenetrationCheck.TranslateNodesBuilder.MethodOptions@endlink) Method

    ##   the method   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @Method.setter
    def Method(self, method: TranslateNodesBuilder.MethodOptions):
        """
        Setter for property: (@link TranslateNodesBuilder.MethodOptions NXOpen.CAE.PenetrationCheck.TranslateNodesBuilder.MethodOptions@endlink) Method
          the method   
            
         
        """
        pass
    
    ## Getter for property: (bool) MoveAdjacentNodes
    ##   the move adjacent nodes   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return bool
    @property
    def MoveAdjacentNodes(self) -> bool:
        """
        Getter for property: (bool) MoveAdjacentNodes
          the move adjacent nodes   
            
         
        """
        pass
    
    ## Setter for property: (bool) MoveAdjacentNodes

    ##   the move adjacent nodes   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @MoveAdjacentNodes.setter
    def MoveAdjacentNodes(self, moveAdjacentNodes: bool):
        """
        Setter for property: (bool) MoveAdjacentNodes
          the move adjacent nodes   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfLayers
    ##   the number of layers   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def NumberOfLayers(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) NumberOfLayers
          the number of layers   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PAngle
    ##   the p angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def PAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) PAngle
          the p angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointSource
    ##   the source point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointSource(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointSource
          the source point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointSource

    ##   the source point   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PointSource.setter
    def PointSource(self, sourcePoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointSource
          the source point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointTarget
    ##   the target point   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Point
    @property
    def PointTarget(self) -> NXOpen.Point:
        """
        Getter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointTarget
          the target point   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointTarget

    ##   the target point   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PointTarget.setter
    def PointTarget(self, targetPoint: NXOpen.Point):
        """
        Setter for property: (@link NXOpen.Point NXOpen.Point@endlink) PointTarget
          the target point   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) SelectNodes
    ##   the select nodes   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.CAE.SelectFENodeList
    @property
    def SelectNodes(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: (@link NXOpen.CAE.SelectFENodeList NXOpen.CAE.SelectFENodeList@endlink) SelectNodes
          the select nodes   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TAngle
    ##   the t angle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def TAngle(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) TAngle
          the t angle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorSource
    ##   the source vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def VectorSource(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorSource
          the source vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorSource

    ##   the source vector   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @VectorSource.setter
    def VectorSource(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorSource
          the source vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorTarget
    ##   the target vector   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Direction
    @property
    def VectorTarget(self) -> NXOpen.Direction:
        """
        Getter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorTarget
          the target vector   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorTarget

    ##   the target vector   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @VectorTarget.setter
    def VectorTarget(self, vector: NXOpen.Direction):
        """
        Setter for property: (@link NXOpen.Direction NXOpen.Direction@endlink) VectorTarget
          the target vector   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XDistance
    ##   the x distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def XDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) XDistance
          the x distance   
            
         
        """
        pass
    
    ## Getter for property: (float) XScaleFactor
    ##   the x scale factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def XScaleFactor(self) -> float:
        """
        Getter for property: (float) XScaleFactor
          the x scale factor   
            
         
        """
        pass
    
    ## Setter for property: (float) XScaleFactor

    ##   the x scale factor   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @XScaleFactor.setter
    def XScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) XScaleFactor
          the x scale factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YDistance
    ##   the y distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def YDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) YDistance
          the y distance   
            
         
        """
        pass
    
    ## Getter for property: (float) YScaleFactor
    ##   the y scale factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def YScaleFactor(self) -> float:
        """
        Getter for property: (float) YScaleFactor
          the y scale factor   
            
         
        """
        pass
    
    ## Setter for property: (float) YScaleFactor

    ##   the y scale factor   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @YScaleFactor.setter
    def YScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) YScaleFactor
          the y scale factor   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZDistance
    ##   the z distance   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.Expression
    @property
    def ZDistance(self) -> NXOpen.Expression:
        """
        Getter for property: (@link NXOpen.Expression NXOpen.Expression@endlink) ZDistance
          the z distance   
            
         
        """
        pass
    
    ## Getter for property: (float) ZScaleFactor
    ##   the z scale factor   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return float
    @property
    def ZScaleFactor(self) -> float:
        """
        Getter for property: (float) ZScaleFactor
          the z scale factor   
            
         
        """
        pass
    
    ## Setter for property: (float) ZScaleFactor

    ##   the z scale factor   
    ##     
    ##  
    ## Setter License requirements: nx_masterfem ("Finite Element Modeling")
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @ZScaleFactor.setter
    def ZScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) ZScaleFactor
          the z scale factor   
            
         
        """
        pass
    
## @package NXOpen.CAE.PenetrationCheck
## Classes, Enums and Structs under NXOpen.CAE.PenetrationCheck namespace

##  @link AddSetBuilderInterferenceBetweenType NXOpen.CAE.PenetrationCheck.AddSetBuilderInterferenceBetweenType @endlink is an alias for @link AddSetBuilder.InterferenceBetweenType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceBetweenType@endlink
AddSetBuilderInterferenceBetweenType = AddSetBuilder.InterferenceBetweenType


##  @link AddSetBuilderInterferenceType NXOpen.CAE.PenetrationCheck.AddSetBuilderInterferenceType @endlink is an alias for @link AddSetBuilder.InterferenceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.InterferenceType@endlink
AddSetBuilderInterferenceType = AddSetBuilder.InterferenceType


##  @link AddSetBuilderSelectionTypeOptions NXOpen.CAE.PenetrationCheck.AddSetBuilderSelectionTypeOptions @endlink is an alias for @link AddSetBuilder.SelectionTypeOptions NXOpen.CAE.PenetrationCheck.AddSetBuilder.SelectionTypeOptions@endlink
AddSetBuilderSelectionTypeOptions = AddSetBuilder.SelectionTypeOptions


##  @link AddSetBuilderThicknessBoundaryType NXOpen.CAE.PenetrationCheck.AddSetBuilderThicknessBoundaryType @endlink is an alias for @link AddSetBuilder.ThicknessBoundaryType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessBoundaryType@endlink
AddSetBuilderThicknessBoundaryType = AddSetBuilder.ThicknessBoundaryType


##  @link AddSetBuilderThicknessSourceType NXOpen.CAE.PenetrationCheck.AddSetBuilderThicknessSourceType @endlink is an alias for @link AddSetBuilder.ThicknessSourceType NXOpen.CAE.PenetrationCheck.AddSetBuilder.ThicknessSourceType@endlink
AddSetBuilderThicknessSourceType = AddSetBuilder.ThicknessSourceType


##  @link AutomaticResolveBuilderResolveType NXOpen.CAE.PenetrationCheck.AutomaticResolveBuilderResolveType @endlink is an alias for @link AutomaticResolveBuilder.ResolveType NXOpen.CAE.PenetrationCheck.AutomaticResolveBuilder.ResolveType@endlink
AutomaticResolveBuilderResolveType = AutomaticResolveBuilder.ResolveType


##  @link TranslateNodesBuilderMethodOptions NXOpen.CAE.PenetrationCheck.TranslateNodesBuilderMethodOptions @endlink is an alias for @link TranslateNodesBuilder.MethodOptions NXOpen.CAE.PenetrationCheck.TranslateNodesBuilder.MethodOptions@endlink
TranslateNodesBuilderMethodOptions = TranslateNodesBuilder.MethodOptions


