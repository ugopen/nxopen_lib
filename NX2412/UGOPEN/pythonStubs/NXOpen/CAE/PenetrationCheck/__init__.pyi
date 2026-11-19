from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddSetBuilder(NXOpen.Builder): 
    """ Represents a CAE.PenetrationCheck.AddSet builder """
    class InterferenceBetweenType(Enum):
        """
        Members Include: 
         |MeshCollectorContainers|  
         |Meshes|  
         |ComponentFEMs| 

        """
        MeshCollectorContainers: int
        Meshes: int
        ComponentFEMs: int
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.InterferenceBetweenType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class InterferenceType(Enum):
        """
        Members Include: 
         |All|  
         |Intersections|  
         |Penetrations| 

        """
        All: int
        Intersections: int
        Penetrations: int
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.InterferenceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectionTypeOptions(Enum):
        """
        Members Include: 
         |MeshObjects|  
         |ContactDefinitions| 

        """
        MeshObjects: int
        ContactDefinitions: int
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.SelectionTypeOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessBoundaryType(Enum):
        """
        Members Include: 
         |Sharp|  
         |Round| 

        """
        Sharp: int
        Round: int
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.ThicknessBoundaryType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ThicknessSourceType(Enum):
        """
        Members Include: 
         |ElementAssociatedData|  
         |UserDefined| 

        """
        ElementAssociatedData: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> AddSetBuilder.ThicknessSourceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BoundaryType(self) -> AddSetBuilder.ThicknessBoundaryType:
        """
        Getter for property: ( AddSetBuilder.ThicknessBoundaryType NXOpen.CAE.Pe) BoundaryType
         Returns the interference option   
            
         
        """
        pass
    @BoundaryType.setter
    def BoundaryType(self, boundaryOption: AddSetBuilder.ThicknessBoundaryType):
        """
        Setter for property: ( AddSetBuilder.ThicknessBoundaryType NXOpen.CAE.Pe) BoundaryType
         Returns the interference option   
            
         
        """
        pass
    @property
    def ElemThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ElemThickness
         Returns the elem thickness   
            
         
        """
        pass
    @property
    def InterferenceBetween(self) -> AddSetBuilder.InterferenceBetweenType:
        """
        Getter for property: ( AddSetBuilder.InterferenceBetweenType NXOpen.CAE.Pe) InterferenceBetween
         Returns the interference between   
            
         
        """
        pass
    @InterferenceBetween.setter
    def InterferenceBetween(self, interferenceBetween: AddSetBuilder.InterferenceBetweenType):
        """
        Setter for property: ( AddSetBuilder.InterferenceBetweenType NXOpen.CAE.Pe) InterferenceBetween
         Returns the interference between   
            
         
        """
        pass
    @property
    def InterferenceOption(self) -> AddSetBuilder.InterferenceType:
        """
        Getter for property: ( AddSetBuilder.InterferenceType NXOpen.CAE.Pe) InterferenceOption
         Returns the interference option   
            
         
        """
        pass
    @InterferenceOption.setter
    def InterferenceOption(self, interferenceOption: AddSetBuilder.InterferenceType):
        """
        Setter for property: ( AddSetBuilder.InterferenceType NXOpen.CAE.Pe) InterferenceOption
         Returns the interference option   
            
         
        """
        pass
    @property
    def PenetrationSetName(self) -> str:
        """
        Getter for property: (str) PenetrationSetName
         Returns the clearance set name.  
             
         
        """
        pass
    @PenetrationSetName.setter
    def PenetrationSetName(self, setName: str):
        """
        Setter for property: (str) PenetrationSetName
         Returns the clearance set name.  
             
         
        """
        pass
    @property
    def Selection(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) Selection
         Returns the selection   
            
         
        """
        pass
    @property
    def SelectionType(self) -> AddSetBuilder.SelectionTypeOptions:
        """
        Getter for property: ( AddSetBuilder.SelectionTypeOptions NXOpen.CAE.Pe) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @SelectionType.setter
    def SelectionType(self, selectionType: AddSetBuilder.SelectionTypeOptions):
        """
        Setter for property: ( AddSetBuilder.SelectionTypeOptions NXOpen.CAE.Pe) SelectionType
         Returns the selection type   
            
         
        """
        pass
    @property
    def SelfInterferenceOption(self) -> bool:
        """
        Getter for property: (bool) SelfInterferenceOption
         Returns the self interference toggle   
            
         
        """
        pass
    @SelfInterferenceOption.setter
    def SelfInterferenceOption(self, selfInterferenceOption: bool):
        """
        Setter for property: (bool) SelfInterferenceOption
         Returns the self interference toggle   
            
         
        """
        pass
    @property
    def ThicknessFactor(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ThicknessFactor
         Returns the scaling factor   
            
         
        """
        pass
    @property
    def ThicknessSource(self) -> AddSetBuilder.ThicknessSourceType:
        """
        Getter for property: ( AddSetBuilder.ThicknessSourceType NXOpen.CAE.Pe) ThicknessSource
         Returns the thickness source   
            
         
        """
        pass
    @ThicknessSource.setter
    def ThicknessSource(self, thicknessSource: AddSetBuilder.ThicknessSourceType):
        """
        Setter for property: ( AddSetBuilder.ThicknessSourceType NXOpen.CAE.Pe) ThicknessSource
         Returns the thickness source   
            
         
        """
        pass
import NXOpen
class AddSet(NXOpen.DisplayableObject): 
    """  Represents a PenetrationCheck  """
    pass
import NXOpen
class AnalysisSet(NXOpen.NXObject): 
    """  The Penetration Check AnalysisSet class offers means to delete, create, edit, and switch NXOpen.CAE.PenetrationCheck.AnalysisSet instances. """
    def ChangeActiveSet(self) -> None:
        """
         Set this clearance set as active
        """
        pass
    def DeleteSet(self) -> None:
        """
         Delete this clearance set 
        """
        pass
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
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
    def PlotContours(self, viewIndex: int) -> None:
        """
         Set this clearance set as active
        """
        pass
    def Print(self) -> None:
        """
         Print autotest XML data
        """
        pass
    def RunInterferenceCheck(self) -> None:
        """
         Set this clearance set as active
        """
        pass
import NXOpen
class AutomaticResolveBuilder(NXOpen.Builder): 
    """ Represents a CAE.PenetrationCheck.AutomaticResolve builder """
    class ResolveType(Enum):
        """
        Members Include: 
         |All|  
         |WithinLimits| 

        """
        All: int
        WithinLimits: int
        @staticmethod
        def ValueOf(value: int) -> AutomaticResolveBuilder.ResolveType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def MaxInterference(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MaxInterference
         Returns the max interference   
            
         
        """
        pass
    @property
    def MeshesToFreeze(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) MeshesToFreeze
         Returns the selection for freezing meshes from translate  
            
         
        """
        pass
    @property
    def MinInterference(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) MinInterference
         Returns the min interference   
            
         
        """
        pass
    @property
    def ResolveOptions(self) -> AutomaticResolveBuilder.ResolveType:
        """
        Getter for property: ( AutomaticResolveBuilder.ResolveType NXOpen.CAE.Pe) ResolveOptions
         Returns the resolve options   
            
         
        """
        pass
    @ResolveOptions.setter
    def ResolveOptions(self, resolveOptions: AutomaticResolveBuilder.ResolveType):
        """
        Setter for property: ( AutomaticResolveBuilder.ResolveType NXOpen.CAE.Pe) ResolveOptions
         Returns the resolve options   
            
         
        """
        pass
    def ResolveButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
class AutomaticResolve(NXOpen.DisplayableObject): 
    """  Represents a PenetrationCheck  """
    pass
import NXOpen
class Manager(NXOpen.Object): 
    """  The Quality Audit Manager class offers means to check for errors at assembly level  """
    @property
    def ActiveSet(self) -> AnalysisSet:
        """
        Getter for property: ( AnalysisSet NXOpen.CAE.Pe) ActiveSet
         Returns the quality audit action list.  
          
                       
         
        """
        pass
    def ClearManager(num: int) -> None:
        """
         Delete object
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
    def PlotContours(viewIndex: int, pObjects: List[ResultObject]) -> None:
        """
         Contour plot
        """
        pass
    def RefreshResults(pObjects: List[ResultObject]) -> None:
        """
         Refresh results object
        """
        pass
    def ResultObjectAutomaticResolve(pObjects: List[ResultObject]) -> None:
        """
         Refresh results object
        """
        pass
import NXOpen
class ResultList(NXOpen.NXObject): 
    """  The Penetration Check AnalysisSet class offers means to find NXOpen.CAE.PenetrationCheck.ResultObject instances. """
    def FindObject(self, journal_identifier: str) -> NXOpen.INXObject:
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
import NXOpen
class ResultObject(NXOpen.NXObject): 
    """  The Penetration Check AnalysisSet class offers means to delete, and edit NXOpen.CAE.PenetrationCheck.ResultObject instances. """
    def DeleteResultObject(self) -> None:
        """
         Delete object
        """
        pass
    def FreezeComponent(self, compToFreeze: int) -> None:
        """
         Set freeze mesh component
        """
        pass
import NXOpen
import NXOpen.CAE
class TranslateNodesBuilder(NXOpen.Builder): 
    """
        Represents a NXOpen.CAE.PenetrationCheck.TranslateNodesBuilder
        """
    class MethodOptions(Enum):
        """
        Members Include: 
         |AlongNodeNormals|  
         |OppositeofNodeNormals|  
         |AlongDirection|  
         |WithOrientation|  
         |PointToPoint|  
         |AlignVectors|  
         |ScaleModel| 

        """
        AlongNodeNormals: int
        OppositeofNodeNormals: int
        AlongDirection: int
        WithOrientation: int
        PointToPoint: int
        AlignVectors: int
        ScaleModel: int
        @staticmethod
        def ValueOf(value: int) -> TranslateNodesBuilder.MethodOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Csys(self) -> NXOpen.CoordinateSystem:
        """
        Getter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @Csys.setter
    def Csys(self, csys: NXOpen.CoordinateSystem):
        """
        Setter for property: ( NXOpen.CoordinateSystem) Csys
         Returns the csys   
            
         
        """
        pass
    @property
    def DirectionVector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) DirectionVector
         Returns the direction vector   
            
         
        """
        pass
    @DirectionVector.setter
    def DirectionVector(self, directionVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) DirectionVector
         Returns the direction vector   
            
         
        """
        pass
    @property
    def Distance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Distance
         Returns the distance   
            
         
        """
        pass
    @property
    def Method(self) -> TranslateNodesBuilder.MethodOptions:
        """
        Getter for property: ( TranslateNodesBuilder.MethodOptions NXOpen.CAE.Pe) Method
         Returns the method   
            
         
        """
        pass
    @Method.setter
    def Method(self, method: TranslateNodesBuilder.MethodOptions):
        """
        Setter for property: ( TranslateNodesBuilder.MethodOptions NXOpen.CAE.Pe) Method
         Returns the method   
            
         
        """
        pass
    @property
    def MoveAdjacentNodes(self) -> bool:
        """
        Getter for property: (bool) MoveAdjacentNodes
         Returns the move adjacent nodes   
            
         
        """
        pass
    @MoveAdjacentNodes.setter
    def MoveAdjacentNodes(self, moveAdjacentNodes: bool):
        """
        Setter for property: (bool) MoveAdjacentNodes
         Returns the move adjacent nodes   
            
         
        """
        pass
    @property
    def NumberOfLayers(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) NumberOfLayers
         Returns the number of layers   
            
         
        """
        pass
    @property
    def PAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) PAngle
         Returns the p angle   
            
         
        """
        pass
    @property
    def PointSource(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointSource
         Returns the source point   
            
         
        """
        pass
    @PointSource.setter
    def PointSource(self, sourcePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointSource
         Returns the source point   
            
         
        """
        pass
    @property
    def PointTarget(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointTarget
         Returns the target point   
            
         
        """
        pass
    @PointTarget.setter
    def PointTarget(self, targetPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointTarget
         Returns the target point   
            
         
        """
        pass
    @property
    def SelectNodes(self) -> NXOpen.CAE.SelectFENodeList:
        """
        Getter for property: ( NXOpen.CAE.SelectFENodeList) SelectNodes
         Returns the select nodes   
            
         
        """
        pass
    @property
    def TAngle(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TAngle
         Returns the t angle   
            
         
        """
        pass
    @property
    def VectorSource(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) VectorSource
         Returns the source vector   
            
         
        """
        pass
    @VectorSource.setter
    def VectorSource(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) VectorSource
         Returns the source vector   
            
         
        """
        pass
    @property
    def VectorTarget(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) VectorTarget
         Returns the target vector   
            
         
        """
        pass
    @VectorTarget.setter
    def VectorTarget(self, vector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) VectorTarget
         Returns the target vector   
            
         
        """
        pass
    @property
    def XDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) XDistance
         Returns the x distance   
            
         
        """
        pass
    @property
    def XScaleFactor(self) -> float:
        """
        Getter for property: (float) XScaleFactor
         Returns the x scale factor   
            
         
        """
        pass
    @XScaleFactor.setter
    def XScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) XScaleFactor
         Returns the x scale factor   
            
         
        """
        pass
    @property
    def YDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) YDistance
         Returns the y distance   
            
         
        """
        pass
    @property
    def YScaleFactor(self) -> float:
        """
        Getter for property: (float) YScaleFactor
         Returns the y scale factor   
            
         
        """
        pass
    @YScaleFactor.setter
    def YScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) YScaleFactor
         Returns the y scale factor   
            
         
        """
        pass
    @property
    def ZDistance(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ZDistance
         Returns the z distance   
            
         
        """
        pass
    @property
    def ZScaleFactor(self) -> float:
        """
        Getter for property: (float) ZScaleFactor
         Returns the z scale factor   
            
         
        """
        pass
    @ZScaleFactor.setter
    def ZScaleFactor(self, scaleFactor: float):
        """
        Setter for property: (float) ZScaleFactor
         Returns the z scale factor   
            
         
        """
        pass
