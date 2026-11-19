from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AddPMIOccNoteBuilder(NXOpen.Builder): 
    """Class for creating pmi occ note"""
    @property
    def ComponentSelection(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ComponentSelection
         Returns the component selection   
            
         
        """
        pass
    def AddButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def GetNoteTextFromListBox(self) -> List[str]:
        """
         Returns the note text 
         Returns noteText (List[str]): .
        """
        pass
    def SetNoteTextFromListBox(self, noteText: List[str]) -> None:
        """
         Sets the note text 
        """
        pass
import NXOpen
class AddTypeAttributeBuilder(NXOpen.Builder): 
    """Class for assignment of mapped type"""
    class MappedType(Enum):
        """
        Members Include: 
         |Mfg0MEEqupment| 

        """
        Mfg0MEEqupment: int
        @staticmethod
        def ValueOf(value: int) -> AddTypeAttributeBuilder.MappedType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentSelection(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) ComponentSelection
         Returns the component selection   
            
         
        """
        pass
    @property
    def MappedTypeName(self) -> str:
        """
        Getter for property: (str) MappedTypeName
         Returns the mapped type name   
            
         
        """
        pass
    @MappedTypeName.setter
    def MappedTypeName(self, name: str):
        """
        Setter for property: (str) MappedTypeName
         Returns the mapped type name   
            
         
        """
        pass
    @property
    def Type(self) -> AddTypeAttributeBuilder.MappedType:
        """
        Getter for property: ( AddTypeAttributeBuilder.MappedType NXOpen.Li) Type
         Returns the mapped type   
            
         
        """
        pass
    @Type.setter
    def Type(self, type: AddTypeAttributeBuilder.MappedType):
        """
        Setter for property: ( AddTypeAttributeBuilder.MappedType NXOpen.Li) Type
         Returns the mapped type   
            
         
        """
        pass
import NXOpen
class AddWorkareaBuilder(NXOpen.Builder): 
    """ use for creating workarea builder"""
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
    def ParentName(self) -> str:
        """
        Getter for property: (str) ParentName
         Returns the parentName   
            
         
        """
        pass
    @ParentName.setter
    def ParentName(self, parentName: str):
        """
        Setter for property: (str) ParentName
         Returns the parentName   
            
         
        """
        pass
    @property
    def ParentPartOccurance(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    @ParentPartOccurance.setter
    def ParentPartOccurance(self, parent: NXOpen.TaggedObject):
        """
        Setter for property: ( NXOpen.TaggedObject) ParentPartOccurance
         Returns an API that gets parent tag  
            
         
        """
        pass
    @property
    def WorkareaTypeName(self) -> str:
        """
        Getter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    @WorkareaTypeName.setter
    def WorkareaTypeName(self, workareaType: str):
        """
        Setter for property: (str) WorkareaTypeName
         Returns the type of workarea   
            
         
        """
        pass
    def GetAllowChildTypeForParent(self, internalName: str) -> List[str]:
        """
         Returns workareaTypes allow children type 
         Returns childrenType (List[str]):  This specifies allow workarea type.
        """
        pass
    def GetDefaultName(self) -> str:
        """
         Returns unique workarea name for creation 
         Returns workareaDefaultName (str): .
        """
        pass
    def GetWorkAreaTypeByParsingPaxFile(self) -> List[str]:
        """
         Returns workareaTypes from pax file 
         Returns workAreaType (List[str]): .
        """
        pass
    def SetInternalName(self, displayName: str, internalName: str) -> None:
        """
         Set Expression internal name  
        """
        pass
import NXOpen
class AlignComponentsBuilder(NXOpen.Builder): 
    """  """
    class ReferenceValues(Enum):
        """
        Members Include: 
         |AbsoluteinDisplayedPart| 
         |Wcs| 

        """
        AbsoluteinDisplayedPart: int
        Wcs: int
        @staticmethod
        def ValueOf(value: int) -> AlignComponentsBuilder.ReferenceValues:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectDirectionOptionEnum(Enum):
        """
        Members Include: 
         |X| 
         |Y| 
         |Z| 
         |UserDefinedDirection| 

        """
        X: int
        Y: int
        Z: int
        UserDefinedDirection: int
        @staticmethod
        def ValueOf(value: int) -> AlignComponentsBuilder.SelectDirectionOptionEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ComponentToAlignTo(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) ComponentToAlignTo
         Returns the component to align to   
            
         
        """
        pass
    @property
    def ComponentsToAlign(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) ComponentsToAlign
         Returns the components to align   
            
         
        """
        pass
    @property
    def Reference(self) -> AlignComponentsBuilder.ReferenceValues:
        """
        Getter for property: ( AlignComponentsBuilder.ReferenceValues NXOpen.Li) Reference
         Returns the reference   
            
         
        """
        pass
    @Reference.setter
    def Reference(self, reference: AlignComponentsBuilder.ReferenceValues):
        """
        Setter for property: ( AlignComponentsBuilder.ReferenceValues NXOpen.Li) Reference
         Returns the reference   
            
         
        """
        pass
    @property
    def SelectDirectionOption(self) -> AlignComponentsBuilder.SelectDirectionOptionEnum:
        """
        Getter for property: ( AlignComponentsBuilder.SelectDirectionOptionEnum NXOpen.Li) SelectDirectionOption
         Returns the component origin direction   
            
         
        """
        pass
    @SelectDirectionOption.setter
    def SelectDirectionOption(self, selectDirectionOption: AlignComponentsBuilder.SelectDirectionOptionEnum):
        """
        Setter for property: ( AlignComponentsBuilder.SelectDirectionOptionEnum NXOpen.Li) SelectDirectionOption
         Returns the component origin direction   
            
         
        """
        pass
    @property
    def SpecifyDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
    @SpecifyDirection.setter
    def SpecifyDirection(self, specifyDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
import NXOpen
class AllowWorkareaTypesBuilder(NXOpen.Builder): 
    """ """
    def AddButton(self) -> None:
        """
         This button is for adding entry from preference xml file 
        """
        pass
    def DeleteButton(self) -> None:
        """
         This button is for deleting entry from preference xml file 
        """
        pass
    def EditButton(self) -> None:
        """
         This button is for editing entry from preference xml file 
        """
        pass
    def RestoreButton(self) -> None:
        """
         This button is to restore data from preference xml file 
        """
        pass
import NXOpen
import NXOpen.Features
class ColumnFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a LineDesigner.ColumnFeature Features.FeatureBuilder
    """
    class ColumnBaseType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Rectangle| 
         |Circle| 
         |Cone| 
         |UserDefined| 

        """
        NotSet: int
        Rectangle: int
        Circle: int
        Cone: int
        UserDefined: int
        @staticmethod
        def ValueOf(value: int) -> ColumnFeatureBuilder.ColumnBaseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColumnType(Enum):
        """
        Members Include: 
         |IBeam| 
         |TBeam| 
         |Rectangle| 
         |Circle| 
         |UserDefine| 

        """
        IBeam: int
        TBeam: int
        Rectangle: int
        Circle: int
        UserDefine: int
        @staticmethod
        def ValueOf(value: int) -> ColumnFeatureBuilder.ColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BaseDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseDepth
         Returns the base depth of column feature   
            
         
        """
        pass
    @property
    def BaseDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseDiameter
         Returns the base diameter of column feature   
            
         
        """
        pass
    @property
    def BaseHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseHeight
         Returns the base height of column feature   
            
         
        """
        pass
    @property
    def BaseLowerDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseLowerDiameter
         Returns the base lower diameter of column feature   
            
         
        """
        pass
    @property
    def BaseStyleEnum(self) -> ColumnFeatureBuilder.ColumnBaseType:
        """
        Getter for property: ( ColumnFeatureBuilder.ColumnBaseType NXOpen.Li) BaseStyleEnum
         Returns the base cross section type of column feature   
            
         
        """
        pass
    @BaseStyleEnum.setter
    def BaseStyleEnum(self, baseStyleEnum: ColumnFeatureBuilder.ColumnBaseType):
        """
        Setter for property: ( ColumnFeatureBuilder.ColumnBaseType NXOpen.Li) BaseStyleEnum
         Returns the base cross section type of column feature   
            
         
        """
        pass
    @property
    def BaseUpperDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseUpperDiameter
         Returns the base upper diameter of column feature   
            
         
        """
        pass
    @property
    def BaseUserDefineSuperSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) BaseUserDefineSuperSection
         Returns the user define cross section for base of column feature   
            
         
        """
        pass
    @property
    def BaseWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) BaseWidth
         Returns the base width of column feature   
            
         
        """
        pass
    @property
    def ColumnDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnDepth
         Returns the column depth of column feature    
            
         
        """
        pass
    @property
    def ColumnDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnDiameter
         Returns the column diameter of column feature   
            
         
        """
        pass
    @property
    def ColumnHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnHeight
         Returns the column height of column feature    
            
         
        """
        pass
    @property
    def ColumnOriginPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ColumnOriginPoint
         Returns the column origin point is returns where colums is created  
            
         
        """
        pass
    @ColumnOriginPoint.setter
    def ColumnOriginPoint(self, columnOriginPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ColumnOriginPoint
         Returns the column origin point is returns where colums is created  
            
         
        """
        pass
    @property
    def ColumnStyleEnum(self) -> ColumnFeatureBuilder.ColumnType:
        """
        Getter for property: ( ColumnFeatureBuilder.ColumnType NXOpen.Li) ColumnStyleEnum
         Returns the column style of column feature    
            
         
        """
        pass
    @ColumnStyleEnum.setter
    def ColumnStyleEnum(self, columnStyleEnum: ColumnFeatureBuilder.ColumnType):
        """
        Setter for property: ( ColumnFeatureBuilder.ColumnType NXOpen.Li) ColumnStyleEnum
         Returns the column style of column feature    
            
         
        """
        pass
    @property
    def ColumnThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnThickness
         Returns the column thickness of column feature   
            
         
        """
        pass
    @property
    def ColumnUserDefineSuperSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ColumnUserDefineSuperSection
         Returns the user defined cross section of column feature   
            
         
        """
        pass
    @property
    def ColumnWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnWidth
         Returns the column width  of column feature   
            
         
        """
        pass
import NXOpen.Features
class ColumnFeature(NXOpen.Features.Feature): 
    """ Represents a column feature feature """
    pass
import NXOpen
class ColumnGridEquipmentBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.ColumnGridEquipment builder

    """
    class ColumnBaseType(Enum):
        """
        Members Include: 
         |NotSet| 
         |Rectangle| 
         |Circle| 
         |Cone| 
         |UserDefine| 

        """
        NotSet: int
        Rectangle: int
        Circle: int
        Cone: int
        UserDefine: int
        @staticmethod
        def ValueOf(value: int) -> ColumnGridEquipmentBuilder.ColumnBaseType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ColumnType(Enum):
        """
        Members Include: 
         |IBeam| 
         |TBeam| 
         |Rectangle| 
         |Circle| 
         |UserDefine| 

        """
        IBeam: int
        TBeam: int
        Rectangle: int
        Circle: int
        UserDefine: int
        @staticmethod
        def ValueOf(value: int) -> ColumnGridEquipmentBuilder.ColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BubbleDiameter(self) -> float:
        """
        Getter for property: (float) BubbleDiameter
         Returns the value of bubble diameter in column grid   
            
         
        """
        pass
    @BubbleDiameter.setter
    def BubbleDiameter(self, bubbleDiameter: float):
        """
        Setter for property: (float) BubbleDiameter
         Returns the value of bubble diameter in column grid   
            
         
        """
        pass
    @property
    def BubbleExtension(self) -> float:
        """
        Getter for property: (float) BubbleExtension
         Returns the value of bubble extension of column grid   
            
         
        """
        pass
    @BubbleExtension.setter
    def BubbleExtension(self, bubbleExtension: float):
        """
        Setter for property: (float) BubbleExtension
         Returns the value of bubble extension of column grid   
            
         
        """
        pass
    @property
    def BubbleExtensionOffset(self) -> float:
        """
        Getter for property: (float) BubbleExtensionOffset
         Returns the bubble extension offset value of column grid   
            
         
        """
        pass
    @BubbleExtensionOffset.setter
    def BubbleExtensionOffset(self, bubbleExtensionOffset: float):
        """
        Setter for property: (float) BubbleExtensionOffset
         Returns the bubble extension offset value of column grid   
            
         
        """
        pass
    @property
    def BubbleLeader(self) -> float:
        """
        Getter for property: (float) BubbleLeader
         Returns the bubble leader   
            
         
        """
        pass
    @BubbleLeader.setter
    def BubbleLeader(self, bubbleLeader: float):
        """
        Setter for property: (float) BubbleLeader
         Returns the bubble leader   
            
         
        """
        pass
    @property
    def BubblesUnallowedChars(self) -> str:
        """
        Getter for property: (str) BubblesUnallowedChars
         Returns the bubbles unallowed characters in column grid   
            
         
        """
        pass
    @BubblesUnallowedChars.setter
    def BubblesUnallowedChars(self, bubblesUnallowedChars: str):
        """
        Setter for property: (str) BubblesUnallowedChars
         Returns the bubbles unallowed characters in column grid   
            
         
        """
        pass
    @property
    def ColumnBaseCrossSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ColumnBaseCrossSection
         Returns the column base cross section of column grid   
            
         
        """
        pass
    @property
    def ColumnBaseDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnBaseDepth
         Returns the column base depth of column grid   
            
         
        """
        pass
    @property
    def ColumnBaseDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnBaseDiameter
         Returns the column base diameter of column grid   
            
         
        """
        pass
    @property
    def ColumnBaseHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnBaseHeight
         Returns the column base height of column grid   
            
         
        """
        pass
    @property
    def ColumnBaseLowerDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnBaseLowerDiameter
         Returnsthe column base lower diameter of column grid   
            
         
        """
        pass
    @property
    def ColumnBaseTypeEnum(self) -> ColumnGridEquipmentBuilder.ColumnBaseType:
        """
        Getter for property: ( ColumnGridEquipmentBuilder.ColumnBaseType NXOpen.Li) ColumnBaseTypeEnum
         Returns the column base type of column grid   
            
         
        """
        pass
    @ColumnBaseTypeEnum.setter
    def ColumnBaseTypeEnum(self, columnBaseTypeEnum: ColumnGridEquipmentBuilder.ColumnBaseType):
        """
        Setter for property: ( ColumnGridEquipmentBuilder.ColumnBaseType NXOpen.Li) ColumnBaseTypeEnum
         Returns the column base type of column grid   
            
         
        """
        pass
    @property
    def ColumnBaseUpperDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnBaseUpperDiameter
         Returns the column base upper diameter of column grid   
            
         
        """
        pass
    @property
    def ColumnBaseWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnBaseWidth
         Returns the column base width of column grid   
            
         
        """
        pass
    @property
    def ColumnCrossSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) ColumnCrossSection
         Returns the column cross section of columns of column grid   
            
         
        """
        pass
    @property
    def ColumnDataList(self) -> NXOpen.NXObjectList:
        """
        Getter for property: ( NXOpen.NXObjectList) ColumnDataList
         Returns the column data list   
            
         
        """
        pass
    @property
    def ColumnDepth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnDepth
         Returns the column depth of column grid    
            
         
        """
        pass
    @property
    def ColumnDiameter(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnDiameter
         Returnsthe column diameter of column grid   
            
         
        """
        pass
    @property
    def ColumnDisplayIDs(self) -> bool:
        """
        Getter for property: (bool) ColumnDisplayIDs
         Returns the status of column display ids in column grid   
            
         
        """
        pass
    @ColumnDisplayIDs.setter
    def ColumnDisplayIDs(self, columnDisplayIDs: bool):
        """
        Setter for property: (bool) ColumnDisplayIDs
         Returns the status of column display ids in column grid   
            
         
        """
        pass
    @property
    def ColumnElevation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnElevation
         Returns the column elevation of column grid   
            
         
        """
        pass
    @property
    def ColumnHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnHeight
         Returns the column height of columns of column grid   
            
         
        """
        pass
    @property
    def ColumnRotate90Degrees(self) -> bool:
        """
        Getter for property: (bool) ColumnRotate90Degrees
         Returns the status of 90 degree column rotation for column grid   
            
         
        """
        pass
    @ColumnRotate90Degrees.setter
    def ColumnRotate90Degrees(self, columnRotate90Degrees: bool):
        """
        Setter for property: (bool) ColumnRotate90Degrees
         Returns the status of 90 degree column rotation for column grid   
            
         
        """
        pass
    @property
    def ColumnSpacingDouble(self) -> float:
        """
        Getter for property: (float) ColumnSpacingDouble
         Returns the spacing between columns   
            
         
        """
        pass
    @ColumnSpacingDouble.setter
    def ColumnSpacingDouble(self, columnSpacingDouble: float):
        """
        Setter for property: (float) ColumnSpacingDouble
         Returns the spacing between columns   
            
         
        """
        pass
    @property
    def ColumnThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnThickness
         Returns the column thickness of coulmn grid   
            
         
        """
        pass
    @property
    def ColumnTypeEnum(self) -> ColumnGridEquipmentBuilder.ColumnType:
        """
        Getter for property: ( ColumnGridEquipmentBuilder.ColumnType NXOpen.Li) ColumnTypeEnum
         Returns the column type of column grid   
            
         
        """
        pass
    @ColumnTypeEnum.setter
    def ColumnTypeEnum(self, columnTypeEnum: ColumnGridEquipmentBuilder.ColumnType):
        """
        Setter for property: ( ColumnGridEquipmentBuilder.ColumnType NXOpen.Li) ColumnTypeEnum
         Returns the column type of column grid   
            
         
        """
        pass
    @property
    def ColumnWideNumber(self) -> int:
        """
        Getter for property: (int) ColumnWideNumber
         Returns the number of column of columns in column grid   
            
         
        """
        pass
    @ColumnWideNumber.setter
    def ColumnWideNumber(self, columnWideNumber: int):
        """
        Setter for property: (int) ColumnWideNumber
         Returns the number of column of columns in column grid   
            
         
        """
        pass
    @property
    def ColumnWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ColumnWidth
         Returns the column width of column grid   
            
         
        """
        pass
    @property
    def CreateBottomBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateBottomBubblesToggle
         Returns the status to create bottom bubbles of column grid   
            
         
        """
        pass
    @CreateBottomBubblesToggle.setter
    def CreateBottomBubblesToggle(self, createBottomBubblesToggle: bool):
        """
        Setter for property: (bool) CreateBottomBubblesToggle
         Returns the status to create bottom bubbles of column grid   
            
         
        """
        pass
    @property
    def CreateLeftBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateLeftBubblesToggle
         Returns the status to create left bubbles of column grid   
            
         
        """
        pass
    @CreateLeftBubblesToggle.setter
    def CreateLeftBubblesToggle(self, createLeftBubblesToggle: bool):
        """
        Setter for property: (bool) CreateLeftBubblesToggle
         Returns the status to create left bubbles of column grid   
            
         
        """
        pass
    @property
    def CreateRightBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateRightBubblesToggle
         Returns the status to create right bubbles of column grid   
            
         
        """
        pass
    @CreateRightBubblesToggle.setter
    def CreateRightBubblesToggle(self, createRightBubblesToggle: bool):
        """
        Setter for property: (bool) CreateRightBubblesToggle
         Returns the status to create right bubbles of column grid   
            
         
        """
        pass
    @property
    def CreateTopBubblesToggle(self) -> bool:
        """
        Getter for property: (bool) CreateTopBubblesToggle
         Returns the status to create top bubbles in column grid   
            
         
        """
        pass
    @CreateTopBubblesToggle.setter
    def CreateTopBubblesToggle(self, createTopBubblesToggle: bool):
        """
        Setter for property: (bool) CreateTopBubblesToggle
         Returns the status to create top bubbles in column grid   
            
         
        """
        pass
    @property
    def DefineGlobalSizeToggle(self) -> bool:
        """
        Getter for property: (bool) DefineGlobalSizeToggle
         Returns the define global size toggle of column grid   
            
         
        """
        pass
    @DefineGlobalSizeToggle.setter
    def DefineGlobalSizeToggle(self, defineGlobalSizeToggle: bool):
        """
        Setter for property: (bool) DefineGlobalSizeToggle
         Returns the define global size toggle of column grid   
            
         
        """
        pass
    @property
    def DisplayGridToggle(self) -> bool:
        """
        Getter for property: (bool) DisplayGridToggle
         Returns the display grid status of column grid   
            
         
        """
        pass
    @DisplayGridToggle.setter
    def DisplayGridToggle(self, displayGridToggle: bool):
        """
        Setter for property: (bool) DisplayGridToggle
         Returns the display grid status of column grid   
            
         
        """
        pass
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: ( NXOpen.KFObject) KfObject
         Returns the kf object   
            
         
        """
        pass
    @property
    def RowDataList(self) -> NXOpen.NXObjectList:
        """
        Getter for property: ( NXOpen.NXObjectList) RowDataList
         Returns the row data list   
            
         
        """
        pass
    @property
    def RowDeepNumber(self) -> int:
        """
        Getter for property: (int) RowDeepNumber
         Returns the number of rows of columns in column grid   
            
         
        """
        pass
    @RowDeepNumber.setter
    def RowDeepNumber(self, rowDeepNumber: int):
        """
        Setter for property: (int) RowDeepNumber
         Returns the number of rows of columns in column grid   
            
         
        """
        pass
    @property
    def RowSpacingDouble(self) -> float:
        """
        Getter for property: (float) RowSpacingDouble
         Returns the value of row spacing between columns  
            
         
        """
        pass
    @RowSpacingDouble.setter
    def RowSpacingDouble(self, rowSpacingDouble: float):
        """
        Setter for property: (float) RowSpacingDouble
         Returns the value of row spacing between columns  
            
         
        """
        pass
    @property
    def SelectGridArea(self) -> PickRectanglePointsBuilder:
        """
        Getter for property: ( PickRectanglePointsBuilder NXOpen.Li) SelectGridArea
         Returns the selected grid area of column grid  
            
         
        """
        pass
    @SelectGridArea.setter
    def SelectGridArea(self, selectGridArea: PickRectanglePointsBuilder):
        """
        Setter for property: ( PickRectanglePointsBuilder NXOpen.Li) SelectGridArea
         Returns the selected grid area of column grid  
            
         
        """
        pass
    @property
    def UseSpacingToggle(self) -> bool:
        """
        Getter for property: (bool) UseSpacingToggle
         Returns the status for using column row spacing of column grid   
            
         
        """
        pass
    @UseSpacingToggle.setter
    def UseSpacingToggle(self, useSpacingToggle: bool):
        """
        Setter for property: (bool) UseSpacingToggle
         Returns the status for using column row spacing of column grid   
            
         
        """
        pass
    def ModifyColumnsButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
class ConnectionCreatorBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """
    class ConnectionType(Enum):
        """
        Members Include: 
         |MoveAndConnect| 
         |Move| 
         |Connect| 

        """
        MoveAndConnect: int
        Move: int
        Connect: int
        @staticmethod
        def ValueOf(value: int) -> ConnectionCreatorBuilder.ConnectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConectionOffset(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ConectionOffset
         Returns the connection offset   
            
         
        """
        pass
    @property
    def ConectionType(self) -> ConnectionCreatorBuilder.ConnectionType:
        """
        Getter for property: ( ConnectionCreatorBuilder.ConnectionType NXOpen.Li) ConectionType
         Returns the current connection type   
            
         
        """
        pass
    @ConectionType.setter
    def ConectionType(self, conectionType: ConnectionCreatorBuilder.ConnectionType):
        """
        Setter for property: ( ConnectionCreatorBuilder.ConnectionType NXOpen.Li) ConectionType
         Returns the current connection type   
            
         
        """
        pass
    @property
    def ExpressionString(self) -> str:
        """
        Getter for property: (str) ExpressionString
         Returns the connection expression RHS string   
            
         
        """
        pass
    @ExpressionString.setter
    def ExpressionString(self, expressionString: str):
        """
        Setter for property: (str) ExpressionString
         Returns the connection expression RHS string   
            
         
        """
        pass
    @property
    def SourceConnector(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SourceConnector
         Returns the source connector used in connection  
            
         
        """
        pass
    @property
    def TargetConnector(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) TargetConnector
         Returns the target connector used in connection   
            
         
        """
        pass
import NXOpen
class ConveyorStationFeatureBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.ConveyorStationFeature builder
    """
    class Type(Enum):
        """
        Members Include: 
         |Load| 
         |Unload| 
         |ProcessRun| 
         |ProcessStop| 
         |Idle| 
         |Decision| 
         |Marriage| 
         |Disassembly| 
         |Assembly| 
         |Stop| 
         |LimitSwitch| 
         |ProximitySwitch| 
         |Reader| 
         |Pusher| 

        """
        Load: int
        Unload: int
        ProcessRun: int
        ProcessStop: int
        Idle: int
        Decision: int
        Marriage: int
        Disassembly: int
        Assembly: int
        Stop: int
        LimitSwitch: int
        ProximitySwitch: int
        Reader: int
        Pusher: int
        @staticmethod
        def ValueOf(value: int) -> ConveyorStationFeatureBuilder.Type:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Capacity(self) -> float:
        """
        Getter for property: (float) Capacity
         Returns the conveyor station capacity   
            
         
        """
        pass
    @Capacity.setter
    def Capacity(self, capacity: float):
        """
        Setter for property: (float) Capacity
         Returns the conveyor station capacity   
            
         
        """
        pass
    @property
    def ProcessTime(self) -> float:
        """
        Getter for property: (float) ProcessTime
         Returns  the Process time   
            
         
        """
        pass
    @ProcessTime.setter
    def ProcessTime(self, processTime: float):
        """
        Setter for property: (float) ProcessTime
         Returns  the Process time   
            
         
        """
        pass
    @property
    def StationLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StationLocation
         Returns the conveyor station location   
            
         
        """
        pass
    @StationLocation.setter
    def StationLocation(self, stationLocation: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StationLocation
         Returns the conveyor station location   
            
         
        """
        pass
    @property
    def StationName(self) -> str:
        """
        Getter for property: (str) StationName
         Returns the station name   
            
         
        """
        pass
    @StationName.setter
    def StationName(self, stationName: str):
        """
        Setter for property: (str) StationName
         Returns the station name   
            
         
        """
        pass
    @property
    def StationType(self) -> ConveyorStationFeatureBuilder.Type:
        """
        Getter for property: ( ConveyorStationFeatureBuilder.Type NXOpen.Li) StationType
         Returns the conveyor station type   
            
         
        """
        pass
    @StationType.setter
    def StationType(self, stationType: ConveyorStationFeatureBuilder.Type):
        """
        Setter for property: ( ConveyorStationFeatureBuilder.Type NXOpen.Li) StationType
         Returns the conveyor station type   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Description of conveyor station is return
         Returns description (List[str]): .
        """
        pass
    def SetDescription(self, description: List[str]) -> None:
        """
         Description for conveyor station is set
        """
        pass
    def SetSECNode(self, secNode: DBConveyorNode) -> None:
        """
             
        """
        pass
import NXOpen.Features
class ConveyorStationFeature(NXOpen.Features.Feature): 
    """ Represents a conveyor station feature feature """
    pass
import NXOpen
class CoverFeatureBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.CoverFeature builder
    """
    @property
    def CoverThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CoverThickness
         Returnsthe cover thickness   
            
         
        """
        pass
    @property
    def LoadRequirements(self) -> float:
        """
        Getter for property: (float) LoadRequirements
         Returnsthe load requirement   
            
         
        """
        pass
    @LoadRequirements.setter
    def LoadRequirements(self, loadRequirements: float):
        """
        Setter for property: (float) LoadRequirements
         Returnsthe load requirement   
            
         
        """
        pass
    @property
    def UseCoverOffset(self) -> bool:
        """
        Getter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
    @UseCoverOffset.setter
    def UseCoverOffset(self, useCoverOffset: bool):
        """
        Setter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
import NXOpen.Features
class CoverFeature(NXOpen.Features.BodyFeature): 
    """ Represents a cover feature """
    pass
import NXOpen
class CreateFactoryElementBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.CreateFactoryElement builder
    """
    class TypeAPI(Enum):
        """
        Members Include: 
         |Plant|  Represents the Plant type 
         |Station|  Represents the Station type 
         |Line|  Represents the Line type 
         |Zone|  Represents the Zone type 
         |Partition|  Represents the Partition type 

        """
        Plant: int
        Station: int
        Line: int
        Zone: int
        Partition: int
        @staticmethod
        def ValueOf(value: int) -> CreateFactoryElementBuilder.TypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FactoryType(self) -> CreateFactoryElementBuilder.TypeAPI:
        """
        Getter for property: ( CreateFactoryElementBuilder.TypeAPI NXOpen.Li) FactoryType
         Returns an API that gets element type   
            
         
        """
        pass
    @FactoryType.setter
    def FactoryType(self, factoryType: CreateFactoryElementBuilder.TypeAPI):
        """
        Setter for property: ( CreateFactoryElementBuilder.TypeAPI NXOpen.Li) FactoryType
         Returns an API that gets element type   
            
         
        """
        pass
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns an API that gets name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns an API that gets name   
            
         
        """
        pass
    @property
    def Position(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) Position
         Returns an API that gets position   
            
         
        """
        pass
    @Position.setter
    def Position(self, position: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) Position
         Returns an API that gets position   
            
         
        """
        pass
import NXOpen
class CreateFactoryElement(NXOpen.DisplayableObject): 
    """ Represents a create factory element """
    pass
import NXOpen
class CreateFenceBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.CreateFence builder
    """
    @property
    def CurveSectionBuilder(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) CurveSectionBuilder
         Returns the curve section builder is return   
            
         
        """
        pass
    @property
    def PostFileBrowser(self) -> str:
        """
        Getter for property: (str) PostFileBrowser
         Returns the post file browser   
            
         
        """
        pass
    @PostFileBrowser.setter
    def PostFileBrowser(self, filename: str):
        """
        Setter for property: (str) PostFileBrowser
         Returns the post file browser   
            
         
        """
        pass
    @property
    def SectionFileBrowser(self) -> str:
        """
        Getter for property: (str) SectionFileBrowser
         Returns the section file browser   
            
         
        """
        pass
    @SectionFileBrowser.setter
    def SectionFileBrowser(self, filename: str):
        """
        Setter for property: (str) SectionFileBrowser
         Returns the section file browser   
            
         
        """
        pass
    @property
    def StartPointPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) StartPointPoint
         Returns the start point of fence  
            
         
        """
        pass
    @StartPointPoint.setter
    def StartPointPoint(self, startPointPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) StartPointPoint
         Returns the start point of fence  
            
         
        """
        pass
import NXOpen
class CreateFence(NXOpen.DisplayableObject): 
    """ Represents a create fence """
    pass
import NXOpen
class CreateSystemBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.CreateSystem builder
    """
    @property
    def ArchPartPath(self) -> str:
        """
        Getter for property: (str) ArchPartPath
         Returns an API that gets arch part path   
            
         
        """
        pass
    @ArchPartPath.setter
    def ArchPartPath(self, filename: str):
        """
        Setter for property: (str) ArchPartPath
         Returns an API that gets arch part path   
            
         
        """
        pass
    @property
    def JigOnPlane(self) -> JigOnPlaneBuilder:
        """
        Getter for property: ( JigOnPlaneBuilder NXOpen.Li) JigOnPlane
         Returns an API that gets jig on plane   
            
         
        """
        pass
    @property
    def LinePartPath(self) -> str:
        """
        Getter for property: (str) LinePartPath
         Returns an API that gets line part path   
            
         
        """
        pass
    @LinePartPath.setter
    def LinePartPath(self, filename: str):
        """
        Setter for property: (str) LinePartPath
         Returns an API that gets line part path   
            
         
        """
        pass
    def InitPreview(self) -> None:
        """
         An API that preview the system 
        """
        pass
    def Update(self) -> None:
        """
         An API that updates system 
        """
        pass
import NXOpen
class CreateSystem(NXOpen.DisplayableObject): 
    """ Represents a create system """
    pass
class DBColumnGridNode(DBSmartComplexEquipmentNode): 
    """ Represents DB column grid  node """
    pass
class DBConveyorNode(DBSmartComplexEquipmentNode): 
    """ Represents DB conveyor node """
    pass
class DBFactoryCadGeoNode(DBSmartComplexEquipmentNode): 
    """ Represents DB import factory cad geo node """
    pass
class DBFactoryNode(DBNode): 
    """ Represents DB factory node """
    class NodeType(Enum):
        """
        Members Include: 
         |Plant| 
         |Station| 
         |Line| 
         |Zone| 
         |Partition| 
         |Unknown| 

        """
        Plant: int
        Station: int
        Line: int
        Zone: int
        Partition: int
        Unknown: int
        @staticmethod
        def ValueOf(value: int) -> DBFactoryNode.NodeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
class DBFenceNode(DBSmartComplexEquipmentNode): 
    """ Represents DB factory node """
    pass
class DBFloorEquipmentNode(DBSmartComplexEquipmentNode): 
    """ Represents DB Floor equipment node """
    pass
class DBNodeContainer(DBSmartComplexEquipmentNode): 
    """ Represents DB node container"""
    pass
import NXOpen
class DBNodeManager(NXOpen.Object): 
    """ Represents a manager of line designer db nodes """
    def CreateDBColumnGridNode(part: NXOpen.Part) -> DBColumnGridNode:
        """
        Creates column grid node 
         Returns node ( DBColumnGridNode NXOpen.Li):  .
        """
        pass
    def CreateDBConveyorNode(part: NXOpen.Part) -> DBConveyorNode:
        """
         Creates conveyor node 
         Returns node ( DBConveyorNode NXOpen.Li):  .
        """
        pass
    def CreateDBFactoryCadGeoNode(part: NXOpen.Part) -> DBFactoryCadGeoNode:
        """
         Creates FactoryCad node 
         Returns node ( DBFactoryCadGeoNode NXOpen.Li):  .
        """
        pass
    def CreateDBFactoryNode(part: NXOpen.Part, type: DBFactoryNode.NodeType) -> DBFactoryNode:
        """
         Factory node creation API
         Returns node ( DBFactoryNode NXOpen.Li):  .
        """
        pass
    def CreateDBFenceNode(part: NXOpen.Part) -> DBFenceNode:
        """
         Creates fence node 
         Returns node ( DBFenceNode NXOpen.Li):  .
        """
        pass
    def CreateDBFloorEquipmentNode(part: NXOpen.Part) -> DBFloorEquipmentNode:
        """
         Creates floor equipment node 
         Returns node ( DBFloorEquipmentNode NXOpen.Li):  .
        """
        pass
    def CreateDBNodeContainer(part: NXOpen.Part) -> DBNodeContainer:
        """
         Creates node container  
         Returns node ( DBNodeContainer NXOpen.Li):  .
        """
        pass
    def CreateDBPlatformEquipmentNode(part: NXOpen.Part) -> DBPlatformEquipmentNode:
        """
         Creates platform equipment node 
         Returns node ( DBPlatformEquipmentNode NXOpen.Li):  .
        """
        pass
    def CreateDBStairwayEquipmentNode(part: NXOpen.Part) -> DBStairwayEquipmentNode:
        """
         Creates stairway equipment node 
         Returns node ( DBStairwayEquipmentNode NXOpen.Li):  .
        """
        pass
import NXOpen
class DBNodeUtils(NXOpen.Object): 
    """ Represents a utils of line designer for journaling uinode methods """
    def ContainsDBNode(partTag: NXOpen.Part) -> None:
        """
         An API to check if part has db node 
        """
        pass
import NXOpen
class DBNode(NXOpen.NXObject): 
    """ Represents DB node """
    pass
class DBPlatformEquipmentNode(DBSmartComplexEquipmentNode): 
    """ Represents DB platform equipment node """
    pass
class DBSmartComplexEquipmentNode(DBSmartEquipmentNode): 
    """ Represents DB factory node """
    pass
class DBSmartEquipmentNode(DBNode): 
    """ Represents DB factory node """
    pass
class DBStairwayEquipmentNode(DBSmartComplexEquipmentNode): 
    """ Represents DB stairway equipment node """
    def AddLeftRailing(self) -> None:
        """
         An API to add left railing to stairway 
        """
        pass
    def AddRightRailing(self) -> None:
        """
         An API to add right railing to stairway 
        """
        pass
    def RemoveBothRailing(self) -> None:
        """
         An API to remove both railings to stairway 
        """
        pass
    def RemoveLeftRailing(self) -> None:
        """
         An API to remove left railing to stairway 
        """
        pass
    def RemoveRightRailing(self) -> None:
        """
         An API to remove right railing to stairway 
        """
        pass
import NXOpen
class DefineRobotBuilder(NXOpen.Builder): 
    """ Define Robot"""
    @property
    def BaseFrameCompitableTypeName(self) -> str:
        """
        Getter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    @BaseFrameCompitableTypeName.setter
    def BaseFrameCompitableTypeName(self, baseFrameCompitableTypeName: str):
        """
        Setter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    @property
    def BaseFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    @BaseFrameDirectionOfConnector.setter
    def BaseFrameDirectionOfConnector(self, baseFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    @property
    def BaseFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    @BaseFrameParallelToObjectDirection.setter
    def BaseFrameParallelToObjectDirection(self, baseFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    @property
    def BaseFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    @BaseFramePoint.setter
    def BaseFramePoint(self, baseFramePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    @property
    def BaseFrameReversePropagation(self) -> bool:
        """
        Getter for property: (bool) BaseFrameReversePropagation
         Returns the base frame reverse propagation   
            
         
        """
        pass
    @BaseFrameReversePropagation.setter
    def BaseFrameReversePropagation(self, baseFrameReversePropagation: bool):
        """
        Setter for property: (bool) BaseFrameReversePropagation
         Returns the base frame reverse propagation   
            
         
        """
        pass
    @property
    def ToolFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    @ToolFrameDirectionOfConnector.setter
    def ToolFrameDirectionOfConnector(self, toolFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    @property
    def ToolFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    @ToolFrameParallelToObjectDirection.setter
    def ToolFrameParallelToObjectDirection(self, toolFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    @property
    def ToolFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    @ToolFramePoint.setter
    def ToolFramePoint(self, toolFramePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    def GetBaseFrameCompatibleTypeList(self) -> List[str]:
        """
          The base frame compatible connector types are returns 
         Returns baseFrameCompatibleTypeList (List[str]): .
        """
        pass
    def GetBaseFramePropagatedExpression(self) -> List[NXOpen.Expression]:
        """
         The base frame connector propagated expressions 
         Returns baseFramePropagatedExpression ( NXOpen.Expression Li): .
        """
        pass
    def GetToolFramePropagatedExpression(self) -> List[NXOpen.Expression]:
        """
         The tool frame connector propagated expressions 
         Returns toolFramePropagatedExpression ( NXOpen.Expression Li): .
        """
        pass
    def SetBaseFrameCompatibleTypeList(self, baseFrameCompatibleTypeList: List[str]) -> None:
        """
         The base connector compatible types are set 
        """
        pass
    def SetBaseFramePropagatedExpression(self, baseFramePropagatedExpression: List[NXOpen.Expression]) -> None:
        """
        The base frame connector propagated expressions are set 
        """
        pass
    def SetNthBaseFramePropagatedExpression(self, nthBaseFramePropagatedExpression: int, baseFramePropagatedExpression: NXOpen.Expression) -> None:
        """
         The Nth expressions from base frame connector propagated expressions are set
        """
        pass
    def SetNthToolFramePropagatedExpression(self, nthToolFramePropagatedExpression: int, toolFramePropagatedExpression: NXOpen.Expression) -> None:
        """
         The Nth expressions from tool frame connector propagated expressions are set
        """
        pass
    def SetToolFramePropagatedExpression(self, toolFramePropagatedExpression: List[NXOpen.Expression]) -> None:
        """
        The tool frame connector propagated expressions are set 
        """
        pass
import NXOpen
class DefineToolBuilder(NXOpen.Builder): 
    """ Define Tool """
    class ToolType(Enum):
        """
        Members Include: 
         |Gun| 
         |ServoGun| 
         |PneumaticServoGun| 
         |Gripper| 
         |AdhesiveGun| 
         |ClinchGun| 
         |PaintGun| 
         |RivetGun| 
         |SealerGun| 
         |WeldGun| 
         |NutWelder| 
         |StudWelder| 
         |FlowDrillScrew| 
         |MultiTool| 

        """
        Gun: int
        ServoGun: int
        PneumaticServoGun: int
        Gripper: int
        AdhesiveGun: int
        ClinchGun: int
        PaintGun: int
        RivetGun: int
        SealerGun: int
        WeldGun: int
        NutWelder: int
        StudWelder: int
        FlowDrillScrew: int
        MultiTool: int
        @staticmethod
        def ValueOf(value: int) -> DefineToolBuilder.ToolType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BaseFrameCompitableTypeName(self) -> str:
        """
        Getter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    @BaseFrameCompitableTypeName.setter
    def BaseFrameCompitableTypeName(self, baseFrameCompitableTypeName: str):
        """
        Setter for property: (str) BaseFrameCompitableTypeName
         Returns the base frame compitable type name   
            
         
        """
        pass
    @property
    def BaseFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    @BaseFrameDirectionOfConnector.setter
    def BaseFrameDirectionOfConnector(self, baseFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) BaseFrameDirectionOfConnector
         Returns the base frame direction of connector   
            
         
        """
        pass
    @property
    def BaseFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    @BaseFrameParallelToObjectDirection.setter
    def BaseFrameParallelToObjectDirection(self, baseFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) BaseFrameParallelToObjectDirection
         Returns the base frame parallel to object direction   
            
         
        """
        pass
    @property
    def BaseFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    @BaseFramePoint.setter
    def BaseFramePoint(self, baseFramePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) BaseFramePoint
         Returns the base frame point   
            
         
        """
        pass
    @property
    def DefineToolTypeToggle(self) -> bool:
        """
        Getter for property: (bool) DefineToolTypeToggle
         Returns the define tool type toggle   
            
         
        """
        pass
    @DefineToolTypeToggle.setter
    def DefineToolTypeToggle(self, defineToolTypeToggle: bool):
        """
        Setter for property: (bool) DefineToolTypeToggle
         Returns the define tool type toggle   
            
         
        """
        pass
    @property
    def SelectGunTips(self) -> NXOpen.SelectPart:
        """
        Getter for property: ( NXOpen.SelectPart) SelectGunTips
         Returns the select gun tips   
            
         
        """
        pass
    @property
    def ToolFrameDirectionOfConnector(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    @ToolFrameDirectionOfConnector.setter
    def ToolFrameDirectionOfConnector(self, toolFrameDirectionOfConnector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToolFrameDirectionOfConnector
         Returns the tool frame direction of connector   
            
         
        """
        pass
    @property
    def ToolFrameParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    @ToolFrameParallelToObjectDirection.setter
    def ToolFrameParallelToObjectDirection(self, toolFrameParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ToolFrameParallelToObjectDirection
         Returns the tool frame parallel to object direction   
            
         
        """
        pass
    @property
    def ToolFramePoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    @ToolFramePoint.setter
    def ToolFramePoint(self, toolFramePoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ToolFramePoint
         Returns the tool frame point   
            
         
        """
        pass
    @property
    def ToolTypeList(self) -> DefineToolBuilder.ToolType:
        """
        Getter for property: ( DefineToolBuilder.ToolType NXOpen.Li) ToolTypeList
         Returns the tool type list   
            
         
        """
        pass
    @ToolTypeList.setter
    def ToolTypeList(self, enumToolType: DefineToolBuilder.ToolType):
        """
        Setter for property: ( DefineToolBuilder.ToolType NXOpen.Li) ToolTypeList
         Returns the tool type list   
            
         
        """
        pass
    def GetBaseFrameCompatibleTypeList(self) -> List[str]:
        """
          The base frame compatible connector types are returns 
         Returns baseFrameCompatibleTypeList (List[str]): .
        """
        pass
    def GetBaseFramePropagatedExpression(self) -> List[NXOpen.Expression]:
        """
         The base frame connector propagated expressions 
         Returns baseFramePropagatedExpression ( NXOpen.Expression Li): .
        """
        pass
    def RemoveButton(self) -> None:
        """
         To remove objects
        """
        pass
    def SetBaseFrameCompatibleTypeList(self, baseFrameCompatibleTypeList: List[str]) -> None:
        """
         The base connector compatible types are set 
        """
        pass
    def SetBaseFramePropagatedExpression(self, baseFramePropagatedExpression: List[NXOpen.Expression]) -> None:
        """
        The base frame connector propagated expressions are set 
        """
        pass
    def SetNthBaseFramePropagatedExpression(self, nthBaseFramePropagatedExpression: int, baseFramePropagatedExpression: NXOpen.Expression) -> None:
        """
         The Nth expressions from base frame connector propagated expressions are set
        """
        pass
class DiamondConnectorFeature(TypedConnectorFeature): 
    """ Represents a typed connector feature feature """
    pass
import NXOpen
class DisconnectConnectionBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """
    @property
    def SelConnector(self) -> NXOpen.SelectPointList:
        """
        Getter for property: ( NXOpen.SelectPointList) SelConnector
         Returns an API that gives connector   
            
         
        """
        pass
    def Disconnect(self, selectedComponent: NXOpen.TaggedObject, componentToDisconnect: List[NXOpen.TaggedObject]) -> None:
        """
         This method is to disconnect selected components with current component 
        """
        pass
import NXOpen
class DistributeComponentsBuilder(NXOpen.Builder): 
    """ """
    @property
    def IsUserDefinedDirection(self) -> bool:
        """
        Getter for property: (bool) IsUserDefinedDirection
         Returns the user defined   
            
         
        """
        pass
    @IsUserDefinedDirection.setter
    def IsUserDefinedDirection(self, isUserDefinedDirection: bool):
        """
        Setter for property: (bool) IsUserDefinedDirection
         Returns the user defined   
            
         
        """
        pass
    @property
    def SelectedCompList(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectedCompList
         Returns the selected comp list   
            
         
        """
        pass
    @property
    def SpecifyDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
    @SpecifyDirection.setter
    def SpecifyDirection(self, specifyDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) SpecifyDirection
         Returns the specify direction   
            
         
        """
        pass
import NXOpen
class EndItemAssemblyStateBuilder(NXOpen.Builder): 
    """  """
    @property
    def AssemblyItemState(self) -> bool:
        """
        Getter for property: (bool) AssemblyItemState
         Returns the assembly item state   
            
         
        """
        pass
    @AssemblyItemState.setter
    def AssemblyItemState(self, assemblyItemState: bool):
        """
        Setter for property: (bool) AssemblyItemState
         Returns the assembly item state   
            
         
        """
        pass
    @property
    def AssemblyOccurenceState(self) -> bool:
        """
        Getter for property: (bool) AssemblyOccurenceState
         Returns the assembly occurence state   
            
         
        """
        pass
    @AssemblyOccurenceState.setter
    def AssemblyOccurenceState(self, assemblyOccurenceState: bool):
        """
        Setter for property: (bool) AssemblyOccurenceState
         Returns the assembly occurence state   
            
         
        """
        pass
import NXOpen
import NXOpen.Display
class EnhancedShadowOutLineBuilder(NXOpen.Builder): 
    """ use for creation of enhanced shadow outline builder """
    class DrawingPlaneOptions(Enum):
        """
        Members Include: 
         |Xcyc| 
         |Yczc| 
         |Zcxc| 
         |Custom| 

        """
        Xcyc: int
        Yczc: int
        Zcxc: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> EnhancedShadowOutLineBuilder.DrawingPlaneOptions:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutLineLevel(Enum):
        """
        Members Include: 
         |Simple| 
         |Detailed| 

        """
        Simple: int
        Detailed: int
        @staticmethod
        def ValueOf(value: int) -> EnhancedShadowOutLineBuilder.OutLineLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutLineScope(Enum):
        """
        Members Include: 
         |CompleteComponent| 
         |Objects| 

        """
        CompleteComponent: int
        Objects: int
        @staticmethod
        def ValueOf(value: int) -> EnhancedShadowOutLineBuilder.OutLineScope:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def DrawingPlaneOption(self) -> EnhancedShadowOutLineBuilder.DrawingPlaneOptions:
        """
        Getter for property: ( EnhancedShadowOutLineBuilder.DrawingPlaneOptions NXOpen.Li) DrawingPlaneOption
         Returns the drawing plane option   
            
         
        """
        pass
    @DrawingPlaneOption.setter
    def DrawingPlaneOption(self, drawingPlaneOption: EnhancedShadowOutLineBuilder.DrawingPlaneOptions):
        """
        Setter for property: ( EnhancedShadowOutLineBuilder.DrawingPlaneOptions NXOpen.Li) DrawingPlaneOption
         Returns the drawing plane option   
            
         
        """
        pass
    @property
    def InputText(self) -> str:
        """
        Getter for property: (str) InputText
         Returns the input text   
            
         
        """
        pass
    @InputText.setter
    def InputText(self, inputText: str):
        """
        Setter for property: (str) InputText
         Returns the input text   
            
         
        """
        pass
    @property
    def LayerSettings(self) -> NXOpen.Display.LayerSettingsBuilder:
        """
        Getter for property: ( NXOpen.Display.LayerSettingsBuilder) LayerSettings
         Returns the layer setting for elbows to be placed   
            
         
        """
        pass
    @property
    def LevelOfOutline(self) -> EnhancedShadowOutLineBuilder.OutLineLevel:
        """
        Getter for property: ( EnhancedShadowOutLineBuilder.OutLineLevel NXOpen.Li) LevelOfOutline
         Returns the out line enum   
            
         
        """
        pass
    @LevelOfOutline.setter
    def LevelOfOutline(self, levelOfOutline: EnhancedShadowOutLineBuilder.OutLineLevel):
        """
        Setter for property: ( EnhancedShadowOutLineBuilder.OutLineLevel NXOpen.Li) LevelOfOutline
         Returns the out line enum   
            
         
        """
        pass
    @property
    def LineColorFontWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LineColorFontWidth
         Returns the outline color font width   
            
         
        """
        pass
    @property
    def ReferenceSetToggle(self) -> bool:
        """
        Getter for property: (bool) ReferenceSetToggle
         Returns the reference set toggle   
            
         
        """
        pass
    @ReferenceSetToggle.setter
    def ReferenceSetToggle(self, referenceSetToggle: bool):
        """
        Setter for property: (bool) ReferenceSetToggle
         Returns the reference set toggle   
            
         
        """
        pass
    @property
    def ScopeOfOutline(self) -> EnhancedShadowOutLineBuilder.OutLineScope:
        """
        Getter for property: ( EnhancedShadowOutLineBuilder.OutLineScope NXOpen.Li) ScopeOfOutline
         Returns the description enum   
            
         
        """
        pass
    @ScopeOfOutline.setter
    def ScopeOfOutline(self, scopeOfOutline: EnhancedShadowOutLineBuilder.OutLineScope):
        """
        Setter for property: ( EnhancedShadowOutLineBuilder.OutLineScope NXOpen.Li) ScopeOfOutline
         Returns the description enum   
            
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectObject
         Returns the select object   
            
         
        """
        pass
    @property
    def SpecifyPlane(self) -> NXOpen.Plane:
        """
        Getter for property: ( NXOpen.Plane) SpecifyPlane
         Returns the specify plane   
            
         
        """
        pass
    @SpecifyPlane.setter
    def SpecifyPlane(self, specifyPlane: NXOpen.Plane):
        """
        Setter for property: ( NXOpen.Plane) SpecifyPlane
         Returns the specify plane   
            
         
        """
        pass
    @property
    def TextColorFontWidth(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextColorFontWidth
         Returns the text color font width   
            
         
        """
        pass
    @property
    def TextHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TextHeight
         Returns the text height   
            
         
        """
        pass
    @property
    def TextLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TextLocation
         Returns the text location   
            
         
        """
        pass
    @TextLocation.setter
    def TextLocation(self, textLocation: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TextLocation
         Returns the text location   
            
         
        """
        pass
    def GetSelectedReferenceSet(self) -> List[str]:
        """
         Returns the selected reference set 
         Returns selectedReferenceSet (List[str]): .
        """
        pass
    def SetSelectedReferenceSet(self, selectedReferenceSet: List[str]) -> None:
        """
         Sets the selected reference set 
        """
        pass
import NXOpen
class ExportPlantToDWGBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.ExportPlantToDWG builder
    """
    class SaveAsType(Enum):
        """
        Members Include: 
         |T2d|  Represents the 2D type 
         |T3d|  Represents the 3D type 

        """
        T2d: int
        T3d: int
        @staticmethod
        def ValueOf(value: int) -> ExportPlantToDWGBuilder.SaveAsType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name     
            
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the file name     
            
         
        """
        pass
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    @FolderName.setter
    def FolderName(self, foldername: str):
        """
        Setter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    @property
    def SaveAs(self) -> ExportPlantToDWGBuilder.SaveAsType:
        """
        Getter for property: ( ExportPlantToDWGBuilder.SaveAsType NXOpen.Li) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
    @SaveAs.setter
    def SaveAs(self, saveAs: ExportPlantToDWGBuilder.SaveAsType):
        """
        Setter for property: ( ExportPlantToDWGBuilder.SaveAsType NXOpen.Li) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
import NXOpen
class ExportPlantToDWG(NXOpen.NXObject): 
    """ Represents the export plant to dwg """
    pass
import NXOpen
class ExportToDWGBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.ExportToDWG builder
    """
    class SaveAsTypeAPI(Enum):
        """
        Members Include: 
         |T2d|  Represents the 2D type 
         |T3d|  Represents the 3D type 

        """
        T2d: int
        T3d: int
        @staticmethod
        def ValueOf(value: int) -> ExportToDWGBuilder.SaveAsTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TemplateTypeAPI(Enum):
        """
        Members Include: 
         |A0Size|  Represents the A0 type 
         |A1Size|  Represents the A1 type 
         |A2Size|  Represents the A2 type 
         |A3Size|  Represents the A3 type 
         |A4Size|  Represents the A4 type 

        """
        A0Size: int
        A1Size: int
        A2Size: int
        A3Size: int
        A4Size: int
        @staticmethod
        def ValueOf(value: int) -> ExportToDWGBuilder.TemplateTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FileName(self) -> str:
        """
        Getter for property: (str) FileName
         Returns the file name   
            
         
        """
        pass
    @FileName.setter
    def FileName(self, fileName: str):
        """
        Setter for property: (str) FileName
         Returns the file name   
            
         
        """
        pass
    @property
    def FolderName(self) -> str:
        """
        Getter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    @FolderName.setter
    def FolderName(self, foldername: str):
        """
        Setter for property: (str) FolderName
         Returns the folder name   
            
         
        """
        pass
    @property
    def MonochromeDisplay(self) -> bool:
        """
        Getter for property: (bool) MonochromeDisplay
         Returnsthe monochrome display is return  
            
         
        """
        pass
    @MonochromeDisplay.setter
    def MonochromeDisplay(self, monochromeDisplay: bool):
        """
        Setter for property: (bool) MonochromeDisplay
         Returnsthe monochrome display is return  
            
         
        """
        pass
    @property
    def SaveAs(self) -> ExportToDWGBuilder.SaveAsTypeAPI:
        """
        Getter for property: ( ExportToDWGBuilder.SaveAsTypeAPI NXOpen.Li) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
    @SaveAs.setter
    def SaveAs(self, saveAs: ExportToDWGBuilder.SaveAsTypeAPI):
        """
        Setter for property: ( ExportToDWGBuilder.SaveAsTypeAPI NXOpen.Li) SaveAs
         Returns an API to get save as type   
            
         
        """
        pass
    @property
    def TemplateSheet(self) -> ExportToDWGBuilder.TemplateTypeAPI:
        """
        Getter for property: ( ExportToDWGBuilder.TemplateTypeAPI NXOpen.Li) TemplateSheet
         Returns the template sheet type   
            
         
        """
        pass
    @TemplateSheet.setter
    def TemplateSheet(self, templateSheet: ExportToDWGBuilder.TemplateTypeAPI):
        """
        Setter for property: ( ExportToDWGBuilder.TemplateTypeAPI NXOpen.Li) TemplateSheet
         Returns the template sheet type   
            
         
        """
        pass
import NXOpen
class ExportToDWG(NXOpen.DisplayableObject): 
    """ Represents an export to dwg """
    pass
import NXOpen
class FactoryCadGeoEquipmentAssemblyBuilder(NXOpen.Builder): 
    """   """
    class UpdatedControlData:
        """
         Contains feature update status report 
         FactoryCadGeoEquipmentAssemblyBuilderUpdatedControlData_Struct NXOpen.Li is an alias for  FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData NXOpen.Li.
        """
        @property
        def SControlName(self) -> str:
            """
            Getter for property SControlName
            """
            pass
        @SControlName.setter
        def SControlName(self, value: str):
            """
            Getter for property SControlNameSetter for property SControlName
            """
            pass
        @property
        def DControlValue(self) -> float:
            """
            Getter for property DControlValue
            """
            pass
        @DControlValue.setter
        def DControlValue(self, value: float):
            """
            Getter for property DControlValueSetter for property DControlValue
            """
            pass
        @property
        def DMinValue(self) -> float:
            """
            Getter for property DMinValue
            """
            pass
        @DMinValue.setter
        def DMinValue(self, value: float):
            """
            Getter for property DMinValueSetter for property DMinValue
            """
            pass
        @property
        def DMaxValue(self) -> float:
            """
            Getter for property DMaxValue
            """
            pass
        @DMaxValue.setter
        def DMaxValue(self, value: float):
            """
            Getter for property DMaxValueSetter for property DMaxValue
            """
            pass
        @property
        def DIncrement(self) -> float:
            """
            Getter for property DIncrement
            """
            pass
        @DIncrement.setter
        def DIncrement(self, value: float):
            """
            Getter for property DIncrementSetter for property DIncrement
            """
            pass
        @property
        def VDblLov(self) -> str:
            """
            Getter for property VDblLov
            """
            pass
        @VDblLov.setter
        def VDblLov(self, value: str):
            """
            Getter for property VDblLovSetter for property VDblLov
            """
            pass
        @property
        def VStrLov(self) -> str:
            """
            Getter for property VStrLov
            """
            pass
        @VStrLov.setter
        def VStrLov(self, value: str):
            """
            Getter for property VStrLovSetter for property VStrLov
            """
            pass
        @property
        def BEnforceValues(self) -> bool:
            """
            Getter for property BEnforceValues
            """
            pass
        @BEnforceValues.setter
        def BEnforceValues(self, value: bool):
            """
            Getter for property BEnforceValuesSetter for property BEnforceValues
            """
            pass
        @property
        def BIsEditable(self) -> bool:
            """
            Getter for property BIsEditable
            """
            pass
        @BIsEditable.setter
        def BIsEditable(self, value: bool):
            """
            Getter for property BIsEditableSetter for property BIsEditable
            """
            pass
        @property
        def DConversionFactor(self) -> float:
            """
            Getter for property DConversionFactor
            """
            pass
        @DConversionFactor.setter
        def DConversionFactor(self, value: float):
            """
            Getter for property DConversionFactorSetter for property DConversionFactor
            """
            pass
    def ReadFcadDatasetFiles(self) -> None:
        """
            
        """
        pass
    def ReadFcadFiles(self) -> None:
        """
        Read the FactoryCAD files from folder for native mode
        """
        pass
    def SetStringToObjectMap(self, key: str, tagObject: NXOpen.TaggedObject) -> None:
        """
            
        """
        pass
    def UpdateData(self, updatedControlDatas: List[FactoryCadGeoEquipmentAssemblyBuilder.UpdatedControlData]) -> None:
        """
            
        """
        pass
import NXOpen
class FactoryCadGeoEquipmentBuilder(NXOpen.Builder): 
    """   """
    class UpdatedControlData:
        """
         Contains feature update status report 
         FactoryCadGeoEquipmentBuilderUpdatedControlData_Struct NXOpen.Li is an alias for  FactoryCadGeoEquipmentBuilder.UpdatedControlData NXOpen.Li.
        """
        @property
        def SControlName(self) -> str:
            """
            Getter for property SControlName
            """
            pass
        @SControlName.setter
        def SControlName(self, value: str):
            """
            Getter for property SControlNameSetter for property SControlName
            """
            pass
        @property
        def DControlValue(self) -> float:
            """
            Getter for property DControlValue
            """
            pass
        @DControlValue.setter
        def DControlValue(self, value: float):
            """
            Getter for property DControlValueSetter for property DControlValue
            """
            pass
        @property
        def DMinValue(self) -> float:
            """
            Getter for property DMinValue
            """
            pass
        @DMinValue.setter
        def DMinValue(self, value: float):
            """
            Getter for property DMinValueSetter for property DMinValue
            """
            pass
        @property
        def DMaxValue(self) -> float:
            """
            Getter for property DMaxValue
            """
            pass
        @DMaxValue.setter
        def DMaxValue(self, value: float):
            """
            Getter for property DMaxValueSetter for property DMaxValue
            """
            pass
        @property
        def DIncrement(self) -> float:
            """
            Getter for property DIncrement
            """
            pass
        @DIncrement.setter
        def DIncrement(self, value: float):
            """
            Getter for property DIncrementSetter for property DIncrement
            """
            pass
        @property
        def VDblLov(self) -> str:
            """
            Getter for property VDblLov
            """
            pass
        @VDblLov.setter
        def VDblLov(self, value: str):
            """
            Getter for property VDblLovSetter for property VDblLov
            """
            pass
        @property
        def VStrLov(self) -> str:
            """
            Getter for property VStrLov
            """
            pass
        @VStrLov.setter
        def VStrLov(self, value: str):
            """
            Getter for property VStrLovSetter for property VStrLov
            """
            pass
        @property
        def BEnforceValues(self) -> bool:
            """
            Getter for property BEnforceValues
            """
            pass
        @BEnforceValues.setter
        def BEnforceValues(self, value: bool):
            """
            Getter for property BEnforceValuesSetter for property BEnforceValues
            """
            pass
        @property
        def BIsEditable(self) -> bool:
            """
            Getter for property BIsEditable
            """
            pass
        @BIsEditable.setter
        def BIsEditable(self, value: bool):
            """
            Getter for property BIsEditableSetter for property BIsEditable
            """
            pass
    @property
    def Node(self) -> NXOpen.NXObject:
        """
        Getter for property: ( NXOpen.NXObject) Node
         Returns    
            
         
        """
        pass
    @Node.setter
    def Node(self, node: NXOpen.NXObject):
        """
        Setter for property: ( NXOpen.NXObject) Node
         Returns    
            
         
        """
        pass
import NXOpen
class FloorEquipmentBuilder(NXOpen.Builder): 
    """   """
    @property
    def FloorThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) FloorThickness
         Returns the floor thickness   
            
         
        """
        pass
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: ( NXOpen.KFObject) KfObject
         Returns the kf object   
            
         
        """
        pass
    @property
    def MakeSketchInternal(self) -> bool:
        """
        Getter for property: (bool) MakeSketchInternal
         Returns the make sketchiInternal    
            
         
        """
        pass
    @MakeSketchInternal.setter
    def MakeSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) MakeSketchInternal
         Returns the make sketchiInternal    
            
         
        """
        pass
    @property
    def SelectOutline(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectOutline
         Returns the outline used for creation of floor is return   
            
         
        """
        pass
import NXOpen
class GateFeatureBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.GateFeature builder
    """
    class GateOpeningStyle(Enum):
        """
        Members Include: 
         |Left| 
         |Middle| 
         |Right| 

        """
        Left: int
        Middle: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> GateFeatureBuilder.GateOpeningStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LinearDimElevation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimElevation
         Returns the elevation used for creation of gate   
            
         
        """
        pass
    @property
    def LinearDimGateThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimGateThickness
         Returns the gate thickness   
            
         
        """
        pass
    @property
    def OpeningStyleEnum(self) -> GateFeatureBuilder.GateOpeningStyle:
        """
        Getter for property: ( GateFeatureBuilder.GateOpeningStyle NXOpen.Li) OpeningStyleEnum
         Returns the opening style of gate   
            
         
        """
        pass
    @OpeningStyleEnum.setter
    def OpeningStyleEnum(self, openingStyleEnum: GateFeatureBuilder.GateOpeningStyle):
        """
        Setter for property: ( GateFeatureBuilder.GateOpeningStyle NXOpen.Li) OpeningStyleEnum
         Returns the opening style of gate   
            
         
        """
        pass
import NXOpen.Features
class GateFeature(NXOpen.Features.Feature): 
    """ Represents a gate feature """
    pass
import NXOpen
class GlobalSelectionBuilder(NXOpen.Builder): 
    """ Global Selection """
    @property
    def Selection(self) -> NXOpen.SelectTaggedObjectList:
        """
        Getter for property: ( NXOpen.SelectTaggedObjectList) Selection
         Returns the selected objects   
            
         
        """
        pass
class HeadConnectorFeature(TypedConnectorFeature): 
    """ Represents a typed connector feature feature """
    pass
import NXOpen
import NXOpen.Features
class HoleFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a LineDesigner.HoleFeature builder
    """
    @property
    def AddCover(self) -> bool:
        """
        Getter for property: (bool) AddCover
         Returns the presence of cover over hole is checked  
            
         
        """
        pass
    @AddCover.setter
    def AddCover(self, addCover: bool):
        """
        Setter for property: (bool) AddCover
         Returns the presence of cover over hole is checked  
            
         
        """
        pass
    @property
    def CoverThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) CoverThickness
         Returns the cover thickness   
            
         
        """
        pass
    @property
    def LoadRequirements(self) -> float:
        """
        Getter for property: (float) LoadRequirements
         Returns the load requirements   
            
         
        """
        pass
    @LoadRequirements.setter
    def LoadRequirements(self, loadRequirements: float):
        """
        Setter for property: (float) LoadRequirements
         Returns the load requirements   
            
         
        """
        pass
    @property
    def MakeSketchInternal(self) -> bool:
        """
        Getter for property: (bool) MakeSketchInternal
         Returns    
            
         
        """
        pass
    @MakeSketchInternal.setter
    def MakeSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) MakeSketchInternal
         Returns    
            
         
        """
        pass
    @property
    def SelectOutline(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectOutline
         Returns the selected outline for creation of hole   
            
         
        """
        pass
    @property
    def TextLocation(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) TextLocation
         Returns the text location of hole   
            
         
        """
        pass
    @TextLocation.setter
    def TextLocation(self, textLocation: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) TextLocation
         Returns the text location of hole   
            
         
        """
        pass
    @property
    def TextSize(self) -> float:
        """
        Getter for property: (float) TextSize
         Returns the text size   
            
         
        """
        pass
    @TextSize.setter
    def TextSize(self, textSize: float):
        """
        Setter for property: (float) TextSize
         Returns the text size   
            
         
        """
        pass
    @property
    def UseCoverOffset(self) -> bool:
        """
        Getter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
    @UseCoverOffset.setter
    def UseCoverOffset(self, useCoverOffset: bool):
        """
        Setter for property: (bool) UseCoverOffset
         Returns the cover offset is return, if cover is present over hole   
            
         
        """
        pass
    def GetEnterTextString(self) -> List[str]:
        """
         Get text string 
         Returns enterTextString (List[str]): .
        """
        pass
    def SetEnterTextString(self, enterTextString: List[str]) -> None:
        """
         Set text string 
        """
        pass
import NXOpen.Features
class HoleFeature(NXOpen.Features.BodyFeature): 
    """ Represents a hole feature feature """
    pass
import NXOpen
class ImportFactoryCadGeoBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """
    @property
    def DlgFileName(self) -> str:
        """
        Getter for property: (str) DlgFileName
         Returns the path of dlg file which user wants to import in NX   
            
         
        """
        pass
    @DlgFileName.setter
    def DlgFileName(self, dlgFileName: str):
        """
        Setter for property: (str) DlgFileName
         Returns the path of dlg file which user wants to import in NX   
            
         
        """
        pass
    @property
    def GeoFileName(self) -> str:
        """
        Getter for property: (str) GeoFileName
         Returns the path of geo file which user wants to import in NX   
            
         
        """
        pass
    @GeoFileName.setter
    def GeoFileName(self, geoFileName: str):
        """
        Setter for property: (str) GeoFileName
         Returns the path of geo file which user wants to import in NX   
            
         
        """
        pass
    @property
    def IsInEditMode(self) -> bool:
        """
        Getter for property: (bool) IsInEditMode
         Returns an in edit mode when dialog is opening before inserting object   
            
         
        """
        pass
    @IsInEditMode.setter
    def IsInEditMode(self, bIsInEditMode: bool):
        """
        Setter for property: (bool) IsInEditMode
         Returns an in edit mode when dialog is opening before inserting object   
            
         
        """
        pass
    @property
    def ParameterSetFileName(self) -> str:
        """
        Getter for property: (str) ParameterSetFileName
         Returns the path of parameter set file which user wants to import in NX   
            
         
        """
        pass
    @ParameterSetFileName.setter
    def ParameterSetFileName(self, parameterSetFileName: str):
        """
        Setter for property: (str) ParameterSetFileName
         Returns the path of parameter set file which user wants to import in NX   
            
         
        """
        pass
    def LoadFactoryCadGeoBuilderToData(self, factoryCadGeoPartTag: NXOpen.Part) -> None:
        """
           
        """
        pass
import NXOpen
class InsertSheetBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.InsertSheet builder
    """
    class APIUnits(Enum):
        """
        Members Include: 
         |Millimeters|  Represents the Millimeters type 
         |Inches|  Represents the Inches type 

        """
        Millimeters: int
        Inches: int
        @staticmethod
        def ValueOf(value: int) -> InsertSheetBuilder.APIUnits:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def NameString(self) -> str:
        """
        Getter for property: (str) NameString
         Returns the name string   
            
         
        """
        pass
    @NameString.setter
    def NameString(self, nameString: str):
        """
        Setter for property: (str) NameString
         Returns the name string   
            
         
        """
        pass
    @property
    def NumberString(self) -> str:
        """
        Getter for property: (str) NumberString
         Returns the number string   
            
         
        """
        pass
    @NumberString.setter
    def NumberString(self, numberString: str):
        """
        Setter for property: (str) NumberString
         Returns the number string   
            
         
        """
        pass
    @property
    def RevisionString(self) -> str:
        """
        Getter for property: (str) RevisionString
         Returns the revision string   
            
         
        """
        pass
    @RevisionString.setter
    def RevisionString(self, revisionString: str):
        """
        Setter for property: (str) RevisionString
         Returns the revision string   
            
         
        """
        pass
    @property
    def ScaleEnum(self) -> int:
        """
        Getter for property: (int) ScaleEnum
         Returns the scale enum   
            
         
        """
        pass
    @ScaleEnum.setter
    def ScaleEnum(self, scaleEnum: int):
        """
        Setter for property: (int) ScaleEnum
         Returns the scale enum   
            
         
        """
        pass
    @property
    def SecondaryNumberString(self) -> str:
        """
        Getter for property: (str) SecondaryNumberString
         Returns the secondary number string   
            
         
        """
        pass
    @SecondaryNumberString.setter
    def SecondaryNumberString(self, secondaryNumberString: str):
        """
        Setter for property: (str) SecondaryNumberString
         Returns the secondary number string   
            
         
        """
        pass
    @property
    def SizeEnum(self) -> int:
        """
        Getter for property: (int) SizeEnum
         Returns the size enum   
            
         
        """
        pass
    @SizeEnum.setter
    def SizeEnum(self, sizeEnum: int):
        """
        Setter for property: (int) SizeEnum
         Returns the size enum   
            
         
        """
        pass
    @property
    def UnitsEnum(self) -> InsertSheetBuilder.APIUnits:
        """
        Getter for property: ( InsertSheetBuilder.APIUnits NXOpen.Li) UnitsEnum
         Returns the units enum   
            
         
        """
        pass
    @UnitsEnum.setter
    def UnitsEnum(self, unitsEnum: InsertSheetBuilder.APIUnits):
        """
        Setter for property: ( InsertSheetBuilder.APIUnits NXOpen.Li) UnitsEnum
         Returns the units enum   
            
         
        """
        pass
import NXOpen.Drawings
class InsertSheet(NXOpen.Drawings.DrawingSheet): 
    """ Represents an insert sheet """
    pass
import NXOpen
import NXOpen.GeometricUtilities
class JigOnPlaneBuilder(NXOpen.TaggedObject): 
    """ Jig on plane """
    @property
    def SelectedPoints(self) -> NXOpen.SelectNXObjectList:
        """
        Getter for property: ( NXOpen.SelectNXObjectList) SelectedPoints
         Returnsthe selected points   
            
         
        """
        pass
    def GetJigPlaneParams(self) -> Tuple[NXOpen.Matrix3x3, NXOpen.Vector3d]:
        """
         Selected jig plane matrix 
         Returns A tuple consisting of (rotation, origin). 
         - rotation is:  NXOpen.Matrix3x3.
         - origin is:  NXOpen.Vector3d.

        """
        pass
import NXOpen
class LineDesignerApplicationBuilder(NXOpen.NXObject): 
    """
    Represents a class to create enter and exit the LineDesigner application
    """
    def Enter(self) -> None:
        """
         To enter lineDesigner application 
        """
        pass
    def Exit(self) -> None:
        """
         To exit LineDesigner application this call will destroy the builder
        """
        pass
    def GetGlobalSelectionBuilder(self) -> GlobalSelectionBuilder:
        """
         To get the global selection builder
         Returns selectionBuilder ( GlobalSelectionBuilder NXOpen.Li): .
        """
        pass
import NXOpen
import NXOpen.Drawings
class LineDesignerManager(NXOpen.Object): 
    """ Represents a manager of line designer builders """
    def ConsolidateUndoMarks(undoMarkId: int) -> None:
        """
          Consolidate Undo Marks 
        """
        pass
    def CreateAddPmiOccNoteBuilder(partOccTag: NXOpen.TaggedObject) -> AddPMIOccNoteBuilder:
        """
         Creates a Add PMI Occ Note Builder
         Returns builder ( AddPMIOccNoteBuilder NXOpen.Li):  .
        """
        pass
    def CreateAddTypeAttributeBuilder(part: NXOpen.Part) -> AddTypeAttributeBuilder:
        """
         Creates a Add Type Attribute Builder
         Returns builder ( AddTypeAttributeBuilder NXOpen.Li):  .
        """
        pass
    def CreateAddWorkareaBuilder(part: NXOpen.Part) -> AddWorkareaBuilder:
        """
         Creates a Add Workarea builder
         Returns builder ( AddWorkareaBuilder NXOpen.Li):  .
        """
        pass
    def CreateAlignComponentsBuilder(part: NXOpen.Part) -> AlignComponentsBuilder:
        """
         Creates a Align Component Dialoge Builder
         Returns builder ( AlignComponentsBuilder NXOpen.Li): .
        """
        pass
    def CreateAllowWorkareaTypesBuilder(part: NXOpen.Part) -> AllowWorkareaTypesBuilder:
        """
         Creates a AllowWorkareaTypes builder
         Returns builder ( AllowWorkareaTypesBuilder NXOpen.Li):  .
        """
        pass
    def CreateApplicationBuilder(part: NXOpen.Part) -> LineDesignerApplicationBuilder:
        """
         Create the application builder 
         Returns builder ( LineDesignerApplicationBuilder NXOpen.Li):  .
        """
        pass
    @overload
    def CreateColumnFeatureBuilder(part: NXOpen.Part, column_feature: ColumnFeature) -> ColumnFeatureBuilder:
        """
         Create column feature builder 
         Returns builder ( ColumnFeatureBuilder NXOpen.Li):  .
        """
        pass
    @overload
    def CreateColumnFeatureBuilder(part: NXOpen.Part, node: DBNode) -> ColumnFeatureBuilder:
        """
        Create column feature builder inside a node or using node 
         Returns builder ( ColumnFeatureBuilder NXOpen.Li):  .
        """
        pass
    def CreateColumnGridEquipmentBuilder(part: NXOpen.Part, dbnode: DBColumnGridNode) -> ColumnGridEquipmentBuilder:
        """
         Create column grid equipment Builder 
         Returns builder ( ColumnGridEquipmentBuilder NXOpen.Li):  .
        """
        pass
    def CreateConnectionCreatorBuilder(part: NXOpen.Part) -> ConnectionCreatorBuilder:
        """
         Create Connection Creator Builder
         Returns builder ( ConnectionCreatorBuilder NXOpen.Li):  .
        """
        pass
    def CreateConveyorStationFeatureBuilder(part: NXOpen.Part, railing_feature: ConveyorStationFeature) -> ConveyorStationFeatureBuilder:
        """
         Create conveyor station feature builder 
         Returns builder ( ConveyorStationFeatureBuilder NXOpen.Li):  .
        """
        pass
    def CreateCoverFeatureBuilder(part: NXOpen.Part, cover_feature: CoverFeature) -> CoverFeatureBuilder:
        """
         Create CoverFeature builder 
         Returns builder ( CoverFeatureBuilder NXOpen.Li):  .
        """
        pass
    def CreateCreateFactoryElementBuilder(part: NXOpen.Part, create_factory_element: CreateFactoryElement) -> CreateFactoryElementBuilder:
        """
        Create factory element builder 
         Returns builder ( CreateFactoryElementBuilder NXOpen.Li):  .
        """
        pass
    def CreateCreateFenceBuilder(part: NXOpen.Part, create_fence: CreateFence) -> CreateFenceBuilder:
        """
         Create fence builder 
         Returns builder ( CreateFenceBuilder NXOpen.Li):  .
        """
        pass
    def CreateCreateSystemBuilder(part: NXOpen.Part, create_system: CreateSystem) -> CreateSystemBuilder:
        """
         Create system builder 
         Returns builder ( CreateSystemBuilder NXOpen.Li):  .
        """
        pass
    def CreateDefineRobotBuilder(part: NXOpen.Part) -> DefineRobotBuilder:
        """
         Creates a Define Robot Dialoge Builder
         Returns builder ( DefineRobotBuilder NXOpen.Li): .
        """
        pass
    def CreateDefineToolBuilder(part: NXOpen.Part) -> DefineToolBuilder:
        """
         Creates a Define Tool Dialoge Builder
         Returns builder ( DefineToolBuilder NXOpen.Li): .
        """
        pass
    def CreateDisconnectConnectionBuilder(part: NXOpen.Part) -> DisconnectConnectionBuilder:
        """
         Create Disconnect Connection Builder
         Returns builder ( DisconnectConnectionBuilder NXOpen.Li):  .
        """
        pass
    def CreateDistributeComponentsBuilder(part: NXOpen.Part) -> DistributeComponentsBuilder:
        """
         To create distribute components builder
         Returns builder ( DistributeComponentsBuilder NXOpen.Li):  .
        """
        pass
    def CreateEndItemAssemblyStateBuilder(appObjectTag: NXOpen.TaggedObject) -> EndItemAssemblyStateBuilder:
        """
         Creates a End Item assembly State Builder
         Returns builder ( EndItemAssemblyStateBuilder NXOpen.Li):  .
        """
        pass
    def CreateEnhancedShadowOutLineBuilder(part: NXOpen.Part) -> EnhancedShadowOutLineBuilder:
        """
         Creates an Enhanced 2D shadow outline Dialoge Builder
         Returns builder ( EnhancedShadowOutLineBuilder NXOpen.Li):  .
        """
        pass
    def CreateExportPlantToDwgBuilder(part: NXOpen.Part, export_plant_to_dwg: ExportPlantToDWG) -> ExportPlantToDWGBuilder:
        """
         Create the export plant to DWG builder 
         Returns builder ( ExportPlantToDWGBuilder NXOpen.Li):  .
        """
        pass
    def CreateExportToDwgBuilder(part: NXOpen.Part, export_to_dwg: ExportToDWG) -> ExportToDWGBuilder:
        """
         Creates the export to DWG builder 
         Returns builder ( ExportToDWGBuilder NXOpen.Li):  .
        """
        pass
    def CreateFactorycadgeoequipmentBuilder(part: NXOpen.Part, dbnode: DBFactoryCadGeoNode) -> FactoryCadGeoEquipmentBuilder:
        """
         To create a rename factory cad geo equipment builder
         Returns builder ( FactoryCadGeoEquipmentBuilder NXOpen.Li):  .
        """
        pass
    def CreateFactorycadgeoequipmentassemblyBuilder(part: NXOpen.Part) -> FactoryCadGeoEquipmentBuilder:
        """
         To create a rename factory cad geo equipment assembly builder
         Returns builder ( FactoryCadGeoEquipmentBuilder NXOpen.Li):  .
        """
        pass
    def CreateFloorequipmentBuilder(part: NXOpen.Part, dbnode: DBFloorEquipmentNode) -> FloorEquipmentBuilder:
        """
        Create Floor builder 
         Returns builder ( FloorEquipmentBuilder NXOpen.Li):  .
        """
        pass
    def CreateGateFeatureBuilder(part: NXOpen.Part, cover_feature: GateFeature) -> GateFeatureBuilder:
        """
         Create GateFeature builder 
         Returns builder ( GateFeatureBuilder NXOpen.Li):  .
        """
        pass
    def CreateGlobalSelectionBuilder(part: NXOpen.Part) -> GlobalSelectionBuilder:
        """
         Create global selection builder 
         Returns builder ( GlobalSelectionBuilder NXOpen.Li): .
        """
        pass
    def CreateHoleFeatureBuilder(part: NXOpen.Part, hole_feature: HoleFeature) -> HoleFeatureBuilder:
        """
         Create HoleFeature builder 
         Returns builder ( HoleFeatureBuilder NXOpen.Li):  .
        """
        pass
    def CreateImportFactoryCadGeoBuilder(part: NXOpen.Part) -> ImportFactoryCadGeoBuilder:
        """
         To get the import factory cad geo builder 
         Returns builder ( ImportFactoryCadGeoBuilder NXOpen.Li): .
        """
        pass
    def CreateInsertSheetBuilder(part: NXOpen.Part, insert_sheet: InsertSheet) -> InsertSheetBuilder:
        """
         Creates the insert sheet builder 
         Returns builder ( InsertSheetBuilder NXOpen.Li):  .
        """
        pass
    def CreateJigOnPlaneBuilder(part: NXOpen.Part) -> JigOnPlaneBuilder:
        """
        Create the jig on plane builder 
         Returns builder ( JigOnPlaneBuilder NXOpen.Li):  .
        """
        pass
    def CreateListOfConnectorsBuilder(part: NXOpen.Part) -> ListOfConnectorsBuilder:
        """
         Creates a Connector List Builder
         Returns builder ( ListOfConnectorsBuilder NXOpen.Li):  .
        """
        pass
    def CreateModifyConnectedSystemBuilder(part: NXOpen.Part) -> ModifyConnectedSystemBuilder:
        """
         Creates a Modify Connected System Builder
         Returns builder ( ModifyConnectedSystemBuilder NXOpen.Li):  .
        """
        pass
    def CreateMountBuilder(part: NXOpen.Part) -> MountBuilder:
        """
         Creates a Mount Dialoge Builder
         Returns builder ( MountBuilder NXOpen.Li):  .
        """
        pass
    def CreatePickRectanglePointsBuilder(part: NXOpen.Part) -> PickRectanglePointsBuilder:
        """
        Create pick rectangle points builder 
         Returns builder ( PickRectanglePointsBuilder NXOpen.Li):  .
        """
        pass
    def CreatePlanViewManagerInstance(part: NXOpen.Part) -> PlanViewManager:
        """
         Creates the plan view manager instance 
         Returns planViewManager ( PlanViewManager NXOpen.Li): .
        """
        pass
    def CreatePlantSimExchangeBuilder(part: NXOpen.Part) -> PlantSimExchangeBuilder:
        """
         Creates a Plant Sim attribute exchange  Builder
         Returns builder ( PlantSimExchangeBuilder NXOpen.Li): .
        """
        pass
    def CreatePlatformEquipmentBuilder(part: NXOpen.Part, dbnode: DBPlatformEquipmentNode) -> PlatformEquipmentBuilder:
        """
         Create Platform Equipment Builder 
         Returns builder ( PlatformEquipmentBuilder NXOpen.Li):  .
        """
        pass
    def CreatePreferencesBuilder(part: NXOpen.Part) -> PreferencesBuilder:
        """
         Creates a Preferences builder
         Returns builder ( PreferencesBuilder NXOpen.Li):  .
        """
        pass
    def CreateProductionUnitCreatorBuilder(part: NXOpen.Part) -> ProductionUnitCreatorBuilder:
        """
         Create production unit creator builder 
         Returns builder ( ProductionUnitCreatorBuilder NXOpen.Li):  .
        """
        pass
    def CreateRailOpeningFeatureBuilder(part: NXOpen.Part, railing_feature: RailOpeningFeature) -> RailOpeningFeatureBuilder:
        """
         Create rail opening feature builder 
         Returns builder ( RailOpeningFeatureBuilder NXOpen.Li):  .
        """
        pass
    @overload
    def CreateRailingFeatureBuilder(part: NXOpen.Part, railing_feature: RailingFeature) -> RailingFeatureBuilder:
        """
         Create railing feature builder 
         Returns builder ( RailingFeatureBuilder NXOpen.Li):  .
        """
        pass
    @overload
    def CreateRailingFeatureBuilder(part: NXOpen.Part, node: DBNode) -> RailingFeatureBuilder:
        """
         Create railing feature builder 
         Returns builder ( RailingFeatureBuilder NXOpen.Li):  .
        """
        pass
    def CreateRenameDialogeBuilder(part: NXOpen.Part) -> RenameDialogeBuilder:
        """
         Creates a Rename Dialoge Builder
         Returns builder ( RenameDialogeBuilder NXOpen.Li): .
        """
        pass
    def CreateRenameItemRevisionBuilder(partOccTag: NXOpen.TaggedObject) -> RenameItemRevisionBuilder:
        """
         To create a rename ItemRevision Builder
         Returns builder ( RenameItemRevisionBuilder NXOpen.Li):  .
        """
        pass
    def CreateResizeConnectorBuilder(part: NXOpen.Part) -> ResizeConnectorBuilder:
        """
         Create resize connector Builder 
         Returns builder ( ResizeConnectorBuilder NXOpen.Li):  .
        """
        pass
    def CreateRotateComponentBuilder(part: NXOpen.Part) -> RotateComponentBuilder:
        """
         Creates a Rotate component builder
         Returns builder ( RotateComponentBuilder NXOpen.Li):  .
        """
        pass
    def CreateSelectionToolBuilder(part: NXOpen.Part) -> SelectionToolBuilder:
        """
         Creates a Selection Tool Builder
         Returns builder ( SelectionToolBuilder NXOpen.Li):  .
        """
        pass
    def CreateSingleElementConveyorBuilder(part: NXOpen.Part, node: DBConveyorNode) -> SingleElementConveyorBuilder:
        """
         Create single element conveyor builder    
         Returns builder ( SingleElementConveyorBuilder NXOpen.Li):  .
        """
        pass
    def CreateStairwayEquipmentBuilder(part: NXOpen.Part, dbnode: DBStairwayEquipmentNode) -> StairwayEquipmentBuilder:
        """
        Create StairwayEquipment builder 
         Returns builder ( StairwayEquipmentBuilder NXOpen.Li):  .
        """
        pass
    def CreateTypedConnectorFeatureBuilder(part: NXOpen.Part, typed_connector_feature: TypedConnectorFeature) -> TypedConnectorFeatureBuilder:
        """
         Create typed connector feature builder 
         Returns builder ( TypedConnectorFeatureBuilder NXOpen.Li):  .
        """
        pass
    def CreateUnmountBuilder(part: NXOpen.Part) -> UnmountBuilder:
        """
         Creates a Unmount Dialoge Builder
         Returns builder ( UnmountBuilder NXOpen.Li):  .
        """
        pass
    def DrawingSheetBuilder(owning_part: NXOpen.Part, sheet: NXOpen.Drawings.DrawingSheet) -> NXOpen.Drawings.DrawingSheetBuilder:
        """
        Create the drawing sheet builder 
         Returns builder ( NXOpen.Drawings.DrawingSheetBuilder):  the drawing sheet Builder with this identifier .
        """
        pass
    def GetApplicationBuilder() -> LineDesignerApplicationBuilder:
        """
         Application builder is return 
         Returns builder ( LineDesignerApplicationBuilder NXOpen.Li): .
        """
        pass
    def GetReuseLibraryUtilityBuilder() -> ReuseLibraryUtilityBuilder:
        """
         Returns the reuse library utility builder 
         Returns builder ( ReuseLibraryUtilityBuilder NXOpen.Li): .
        """
        pass
    def PlantCreateProductionUnitCreatorBuilder(part: NXOpen.Part) -> PlantProductionUnitCreatorBuilder:
        """
         To create a new navigator production unit builder
         Returns builder ( PlantProductionUnitCreatorBuilder NXOpen.Li):  .
        """
        pass
import NXOpen
import NXOpen.Assemblies
class LineDesignerUserCallBackManager(NXOpen.Object): 
    """ Represents a manager of line designer user callbacks """
    class EventType(Enum):
        """
        Members Include: 
         |PasteEvent| 
         |EndPasteEvent| 
         |ComponentReplaceEvent| 

        """
        PasteEvent: int
        EndPasteEvent: int
        ComponentReplaceEvent: int
        @staticmethod
        def ValueOf(value: int) -> LineDesignerUserCallBackManager.EventType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def CallUserdefinedFunctions(eventId: LineDesignerUserCallBackManager.EventType, src_occ: NXOpen.Assemblies.Component, target_occ: NXOpen.Assemblies.Component) -> None:
        """
         To call user defined function
        """
        pass
    CustomerCallbackHandler = Callable[[NXOpen.Assemblies.Component, NXOpen.Assemblies.Component], None]
    def IsUserdefinedFunctionAvailable(eventId: LineDesignerUserCallBackManager.EventType) -> None:
        """
         To check if user defined function is registered
        """
        pass
    def RegisterUserdefinedFunctions(handler: LineDesignerUserCallBackManager.CustomerCallbackHandler, eventId: LineDesignerUserCallBackManager.EventType) -> None:
        """
         To register user defined function
        """
        pass
    def UnregisterUserdefinedFunctions(eventId: LineDesignerUserCallBackManager.EventType) -> None:
        """
         To register user defined function
        """
        pass
import NXOpen
class ListOfConnectorsBuilder(NXOpen.Builder): 
    """ For creating and editing Connectors types in LineDesigner """
    def AddNewType(self) -> None:
        """
         Add a new Connector type 
        """
        pass
    def RestoreDefault(self) -> None:
        """
         Restore to defaults 
        """
        pass
import NXOpen
class ModelBaseObject(NXOpen.NXObject): 
    """ Represents Model Base Object """
    pass
import NXOpen
class ModelPlantManager(NXOpen.Object): 
    """ Represents a manager of line designer model """
    def ActivatePlantModel(modelPlantRoot: ModelPlantRoot, activate: bool) -> None:
        """
          Activate Plant Model  
        """
        pass
    def CleanPlantModel(modelPlantRoot: ModelPlantRoot) -> None:
        """
          Clean Plant Model  
        """
        pass
    def GetModelPlantRoot() -> ModelPlantRoot:
        """
          Establish Plant Model Root 
         Returns modelPlantRoot ( ModelPlantRoot NXOpen.Li):  .
        """
        pass
    def MoveResourceInstances(modelPlantRoot: ModelPlantRoot, resourceInstances: List[ModelResourceInstance], newParent: ModelBaseObject) -> None:
        """
          Move Resource Instances  
        """
        pass
    def ObsoleteProductionUnit(modelPlantRoot: ModelPlantRoot, productionUnitToObsolete: ModelProductionUnit) -> None:
        """
          Obsolete Production Unit  
        """
        pass
    def ReadPlantModel(modelPlantRoot: ModelPlantRoot) -> NXOpen.NXObject:
        """
          Read Plant Model  
         Returns plantRoot ( NXOpen.NXObject):  .
        """
        pass
    def RestoreTargetProductionUnit(modelPlantRoot: ModelPlantRoot) -> None:
        """
          Restore Target Production Unit  
        """
        pass
    def SetTargetProductionUnit(modelPlantRoot: ModelPlantRoot, productionUnit: ModelProductionUnit, keep: bool) -> None:
        """
          Set Target Production Unit  
        """
        pass
import NXOpen
class ModelPlantRoot(NXOpen.NXObject): 
    """ Represents a manager of line designer plant model """
    pass
class ModelProductionUnit(ModelBaseObject): 
    """ Represents Production Unit """
    pass
class ModelResourceInstance(ModelBaseObject): 
    """ Represents Resource Instance """
    pass
import NXOpen
class ModifyConnectedSystemBuilder(NXOpen.Builder): 
    """Class for assignment of mapped type"""
    def CollectExpressionValues(self, expressionTitle: str) -> List[str]:
        """
         Get the Expression Value
         Returns exp (List[str]): .
        """
        pass
    def CollectSharedExpression(self) -> int:
        """
         Collect shared Expression
         Returns numExpresssion (int): .
        """
        pass
    def GetExpressionTitle(self, expression: NXOpen.Expression) -> str:
        """
         Get the Expression Title
         Returns expTitle (str): .
        """
        pass
    def GetExpressionsArray(self) -> List[NXOpen.Expression]:
        """
         Get the expressions in the attribute
         Returns expressions ( NXOpen.Expression Li): .
        """
        pass
    def GetSelectedComponent(self) -> NXOpen.NXObject:
        """
         Set selected component  
         Returns selectedCompTag ( NXOpen.NXObject):  .
        """
        pass
    def GetToolTipMessage(self) -> str:
        """
         Get tooltipMessage component  
         Returns toolTipMessage (str):  .
        """
        pass
    def SetExpressionValue(self, name: str, value: float) -> None:
        """
         Set Expression Value  
        """
        pass
    def SetExpressionsArray(self, expressionValues: List[NXOpen.Expression]) -> None:
        """
         Set the expressions in the attribute 
        """
        pass
    def SetSelectedComponent(self, selectedCompTag: NXOpen.NXObject) -> None:
        """
         Set selected component  
        """
        pass
    def SetToolTipMessage(self, toolTipMessage: str) -> None:
        """
         Set tooltipMessage component  
        """
        pass
import NXOpen
class MountBuilder(NXOpen.Builder): 
    """
    MountBuilder Class: Used when mounting a tool on robot.
    """
    class FlipType(Enum):
        """
        Members Include: 
         |X| 
         |Y| 
         |Z| 

        """
        X: int
        Y: int
        Z: int
        @staticmethod
        def ValueOf(value: int) -> MountBuilder.FlipType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MountType(Enum):
        """
        Members Include: 
         |MoveandMount| 
         |MountOnly| 

        """
        MoveandMount: int
        MountOnly: int
        @staticmethod
        def ValueOf(value: int) -> MountBuilder.MountType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def FlipEnum(self) -> MountBuilder.FlipType:
        """
        Getter for property: ( MountBuilder.FlipType NXOpen.Li) FlipEnum
         Returns the flip enum   
            
         
        """
        pass
    @FlipEnum.setter
    def FlipEnum(self, flipEnum: MountBuilder.FlipType):
        """
        Setter for property: ( MountBuilder.FlipType NXOpen.Li) FlipEnum
         Returns the flip enum   
            
         
        """
        pass
    @property
    def MountEnum(self) -> MountBuilder.MountType:
        """
        Getter for property: ( MountBuilder.MountType NXOpen.Li) MountEnum
         Returns the mount enum   
            
         
        """
        pass
    @MountEnum.setter
    def MountEnum(self, mountEnum: MountBuilder.MountType):
        """
        Setter for property: ( MountBuilder.MountType NXOpen.Li) MountEnum
         Returns the mount enum   
            
         
        """
        pass
    @property
    def SelectSource(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectSource
         Returns the select source   
            
         
        """
        pass
    @property
    def SelectTarget(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectTarget
         Returns the select target   
            
         
        """
        pass
    def FlipButton(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
import NXOpen.GeometricUtilities
class PickRectanglePointsBuilder(NXOpen.TaggedObject): 
    """ Pick Rectangle Points """
    @property
    def AllowRotation(self) -> bool:
        """
        Getter for property: (bool) AllowRotation
         Returns the check for rotaion   
            
         
        """
        pass
    @AllowRotation.setter
    def AllowRotation(self, rotaion: bool):
        """
        Setter for property: (bool) AllowRotation
         Returns the check for rotaion   
            
         
        """
        pass
    @property
    def PointsSelection(self) -> NXOpen.SelectPartList:
        """
        Getter for property: ( NXOpen.SelectPartList) PointsSelection
         Returns the points of selection are return   
            
         
        """
        pass
    def ResetData(self) -> None:
        """
         To reset rectangle data 
        """
        pass
    def ResetWidthHeight(self) -> None:
        """
         To reset rectangle width and height 
        """
        pass
    def SetWidthHeight(self, width: float, height: float) -> None:
        """
         To set rectangle width and height 
        """
        pass
    def UpdateRecAngle(self, angle: float) -> None:
        """
         To update rectangle angle 
        """
        pass
    def UpdateRecHeight(self, height: float) -> None:
        """
         To update rectangle height 
        """
        pass
    def UpdateRecWidth(self, width: float) -> None:
        """
         To update rectangle width 
        """
        pass
    def UpdateRectangle(self) -> None:
        """
         To update rectangle points
        """
        pass
import NXOpen
class PlantProductionUnitCreatorBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """
    @property
    def ProductionUnitId(self) -> str:
        """
        Getter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    @ProductionUnitId.setter
    def ProductionUnitId(self, productionUnitId: str):
        """
        Setter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    @property
    def ProductionUnitName(self) -> str:
        """
        Getter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    @ProductionUnitName.setter
    def ProductionUnitName(self, productionUnitName: str):
        """
        Setter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    @property
    def ProductionUnitTypeString(self) -> str:
        """
        Getter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    @ProductionUnitTypeString.setter
    def ProductionUnitTypeString(self, productionUnitType: str):
        """
        Setter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    def AssignId(self) -> None:
        """
         The assign ID  of production unit
        """
        pass
    def GetProductionUnitDescription(self) -> List[str]:
        """
         The production unit description
         Returns productionUnitDescription (List[str]): .
        """
        pass
    def SetProductionUnitDescription(self, productionUnitDescription: List[str]) -> None:
        """
         The production unit description is set 
        """
        pass
    def SetProductionUnitParent(self, parent: NXOpen.NXObject) -> None:
        """
         The production unit parent is set
        """
        pass
import NXOpen
class PlantSimExchangeBuilder(NXOpen.Builder): 
    """ This class is used for sharing Attribute and JT with Plant Simulation"""
    @property
    def NativeFolderBrowser(self) -> str:
        """
        Getter for property: (str) NativeFolderBrowser
         Returns the native folder browser0   
            
         
        """
        pass
    @NativeFolderBrowser.setter
    def NativeFolderBrowser(self, foldername: str):
        """
        Setter for property: (str) NativeFolderBrowser
         Returns the native folder browser0   
            
         
        """
        pass
import NXOpen
class PlanViewManager(NXOpen.TaggedObject): 
    """ Represents a singleton JA for PlanViewManager """
    def SetTwoDPlanningView(self, setView: bool) -> None:
        """
          To setunset 2D planning view 
        """
        pass
import NXOpen
class PlatformEquipmentBuilder(NXOpen.Builder): 
    """  
    
    
    
    
    
    """
    class DeckSupportTypeAPI(Enum):
        """
        Members Include: 
         |NoSupports| 
         |CornersSupportsOnly| 
         |AutomaticSupportinGridPattern| 
         |ManualSupports| 

        """
        NoSupports: int
        CornersSupportsOnly: int
        AutomaticSupportinGridPattern: int
        ManualSupports: int
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.DeckSupportTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class DeckingMaterialTypeAPI(Enum):
        """
        Members Include: 
         |MetalGrate| 
         |CheckerPlate| 

        """
        MetalGrate: int
        CheckerPlate: int
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.DeckingMaterialTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OutlineTypeAPI(Enum):
        """
        Members Include: 
         |Polyline| 
         |Centerline| 

        """
        Polyline: int
        Centerline: int
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.OutlineTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SideFromCenterlineTypeAPI(Enum):
        """
        Members Include: 
         |RightTopSide| 
         |LeftBottomSide| 

        """
        RightTopSide: int
        LeftBottomSide: int
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.SideFromCenterlineTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class TypeAPI(Enum):
        """
        Members Include: 
         |Platform| 
         |Mezzanine| 

        """
        Platform: int
        Mezzanine: int
        @staticmethod
        def ValueOf(value: int) -> PlatformEquipmentBuilder.TypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddRailingToggle(self) -> bool:
        """
        Getter for property: (bool) AddRailingToggle
         Returns the railing toggle to check railing is prsent for platform or not  
            
         
        """
        pass
    @AddRailingToggle.setter
    def AddRailingToggle(self, addRailingToggle: bool):
        """
        Setter for property: (bool) AddRailingToggle
         Returns the railing toggle to check railing is prsent for platform or not  
            
         
        """
        pass
    @property
    def CenterlineJigOnPlane(self) -> JigOnPlaneBuilder:
        """
        Getter for property: ( JigOnPlaneBuilder NXOpen.Li) CenterlineJigOnPlane
         Returns the Centerlinejig on plane builder   
            
         
        """
        pass
    @CenterlineJigOnPlane.setter
    def CenterlineJigOnPlane(self, centerlineJigOnPlane: JigOnPlaneBuilder):
        """
        Setter for property: ( JigOnPlaneBuilder NXOpen.Li) CenterlineJigOnPlane
         Returns the Centerlinejig on plane builder   
            
         
        """
        pass
    @property
    def DeckCeilingHeightForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckCeilingHeightForCenterline
         Returns the deck ceiling height for centerline platform   
            
         
        """
        pass
    @property
    def DeckCeilingHeightForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckCeilingHeightForPolyline
         Returns the deck ceiling height for polyline platform   
            
         
        """
        pass
    @property
    def DeckElevationForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckElevationForCenterline
         Returns the deck elevation for centerline platform   
            
         
        """
        pass
    @property
    def DeckElevationForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckElevationForPolyline
         Returns the deck elevation for polyline platform   
            
         
        """
        pass
    @property
    def DeckHeightForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckHeightForCenterline
         Returns the deck height for centerline platform   
            
         
        """
        pass
    @property
    def DeckHeightForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckHeightForPolyline
         Returnsthe deck height for polyline platform   
            
         
        """
        pass
    @property
    def DeckLengthForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckLengthForCenterline
         Returns the deck length for centerline platform   
            
         
        """
        pass
    @property
    def DeckSupportEnum(self) -> PlatformEquipmentBuilder.DeckSupportTypeAPI:
        """
        Getter for property: ( PlatformEquipmentBuilder.DeckSupportTypeAPI NXOpen.Li) DeckSupportEnum
         Returns the deck support type for platform  
            
         
        """
        pass
    @DeckSupportEnum.setter
    def DeckSupportEnum(self, deckSupportEnum: PlatformEquipmentBuilder.DeckSupportTypeAPI):
        """
        Setter for property: ( PlatformEquipmentBuilder.DeckSupportTypeAPI NXOpen.Li) DeckSupportEnum
         Returns the deck support type for platform  
            
         
        """
        pass
    @property
    def DeckThicknessForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckThicknessForCenterline
         Returns the deck thickness for centerline platform   
            
         
        """
        pass
    @property
    def DeckThicknessForPolyline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckThicknessForPolyline
         Returns the deck thickness for polyline platform   
            
         
        """
        pass
    @property
    def DeckWidthForCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DeckWidthForCenterline
         Returns the deck width for centerline platform   
            
         
        """
        pass
    @property
    def DeckingMaterial(self) -> PlatformEquipmentBuilder.DeckingMaterialTypeAPI:
        """
        Getter for property: ( PlatformEquipmentBuilder.DeckingMaterialTypeAPI NXOpen.Li) DeckingMaterial
         Returns the decking material   
            
         
        """
        pass
    @DeckingMaterial.setter
    def DeckingMaterial(self, deckingMaterial: PlatformEquipmentBuilder.DeckingMaterialTypeAPI):
        """
        Setter for property: ( PlatformEquipmentBuilder.DeckingMaterialTypeAPI NXOpen.Li) DeckingMaterial
         Returns the decking material   
            
         
        """
        pass
    @property
    def DistanceFromCenterline(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) DistanceFromCenterline
         Returns the distance of platform from centerline   
            
         
        """
        pass
    @property
    def HorizontalGridSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) HorizontalGridSpacing
         Returns the horizontal grid spacing   
            
         
        """
        pass
    @property
    def IsSketchInternal(self) -> bool:
        """
        Getter for property: (bool) IsSketchInternal
         Returns the issketchiInternal    
            
         
        """
        pass
    @IsSketchInternal.setter
    def IsSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) IsSketchInternal
         Returns the issketchiInternal    
            
         
        """
        pass
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: ( NXOpen.KFObject) KfObject
         Returns the kf object   
            
         
        """
        pass
    @property
    def OutlineEnum(self) -> PlatformEquipmentBuilder.OutlineTypeAPI:
        """
        Getter for property: ( PlatformEquipmentBuilder.OutlineTypeAPI NXOpen.Li) OutlineEnum
         Returns the outline type enum   
            
         
        """
        pass
    @OutlineEnum.setter
    def OutlineEnum(self, outlineEnum: PlatformEquipmentBuilder.OutlineTypeAPI):
        """
        Setter for property: ( PlatformEquipmentBuilder.OutlineTypeAPI NXOpen.Li) OutlineEnum
         Returns the outline type enum   
            
         
        """
        pass
    @property
    def PolylineSuperSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) PolylineSuperSection
         Returns the polyline section for platform   
            
         
        """
        pass
    @property
    def SideFromCenterlineEnum(self) -> PlatformEquipmentBuilder.SideFromCenterlineTypeAPI:
        """
        Getter for property: ( PlatformEquipmentBuilder.SideFromCenterlineTypeAPI NXOpen.Li) SideFromCenterlineEnum
         Returns the side from center line    
            
         
        """
        pass
    @SideFromCenterlineEnum.setter
    def SideFromCenterlineEnum(self, sideFromCenterlineEnum: PlatformEquipmentBuilder.SideFromCenterlineTypeAPI):
        """
        Setter for property: ( PlatformEquipmentBuilder.SideFromCenterlineTypeAPI NXOpen.Li) SideFromCenterlineEnum
         Returns the side from center line    
            
         
        """
        pass
    @property
    def StatusOfPlatformCeilingHeightUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformCeilingHeightUpdation
         Returns the platform ceiling height updation status   
            
         
        """
        pass
    @StatusOfPlatformCeilingHeightUpdation.setter
    def StatusOfPlatformCeilingHeightUpdation(self, statusOfPlatformCeilingHeightUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformCeilingHeightUpdation
         Returns the platform ceiling height updation status   
            
         
        """
        pass
    @property
    def StatusOfPlatformElevationUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformElevationUpdation
         Returns the platform elevation updation status   
            
         
        """
        pass
    @StatusOfPlatformElevationUpdation.setter
    def StatusOfPlatformElevationUpdation(self, statusOfPlatformElevationUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformElevationUpdation
         Returns the platform elevation updation status   
            
         
        """
        pass
    @property
    def StatusOfPlatformHeightUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformHeightUpdation
         Returns the platform height updation status   
            
         
        """
        pass
    @StatusOfPlatformHeightUpdation.setter
    def StatusOfPlatformHeightUpdation(self, statusOfPlatformHeightUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformHeightUpdation
         Returns the platform height updation status   
            
         
        """
        pass
    @property
    def StatusOfPlatformSupportDefaultFromCeilingToggleUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformSupportDefaultFromCeilingToggleUpdation
         Returns the platform supportDefaultFromCeilingToggle updation status   
            
         
        """
        pass
    @StatusOfPlatformSupportDefaultFromCeilingToggleUpdation.setter
    def StatusOfPlatformSupportDefaultFromCeilingToggleUpdation(self, statusOfPlatformSupportDefaultFromCeilingToggleUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformSupportDefaultFromCeilingToggleUpdation
         Returns the platform supportDefaultFromCeilingToggle updation status   
            
         
        """
        pass
    @property
    def StatusOfPlatformSupportOptionUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformSupportOptionUpdation
         Returns the platform supportOption updation status   
            
         
        """
        pass
    @StatusOfPlatformSupportOptionUpdation.setter
    def StatusOfPlatformSupportOptionUpdation(self, statusOfPlatformSupportOptionUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformSupportOptionUpdation
         Returns the platform supportOption updation status   
            
         
        """
        pass
    @property
    def StatusOfPlatformThicknessUpdation(self) -> bool:
        """
        Getter for property: (bool) StatusOfPlatformThicknessUpdation
         Returns the platform thickness updation status   
            
         
        """
        pass
    @StatusOfPlatformThicknessUpdation.setter
    def StatusOfPlatformThicknessUpdation(self, statusOfPlatformThicknessUpdation: bool):
        """
        Setter for property: (bool) StatusOfPlatformThicknessUpdation
         Returns the platform thickness updation status   
            
         
        """
        pass
    @property
    def SupportsFromCeiling(self) -> bool:
        """
        Getter for property: (bool) SupportsFromCeiling
         Returns the option to check , if supports are from ceiling   
            
         
        """
        pass
    @SupportsFromCeiling.setter
    def SupportsFromCeiling(self, supportsFromCeiling: bool):
        """
        Setter for property: (bool) SupportsFromCeiling
         Returns the option to check , if supports are from ceiling   
            
         
        """
        pass
    @property
    def TypeEnum(self) -> PlatformEquipmentBuilder.TypeAPI:
        """
        Getter for property: ( PlatformEquipmentBuilder.TypeAPI NXOpen.Li) TypeEnum
         Returns the platform type enum   
            
         
        """
        pass
    @TypeEnum.setter
    def TypeEnum(self, typeEnum: PlatformEquipmentBuilder.TypeAPI):
        """
        Setter for property: ( PlatformEquipmentBuilder.TypeAPI NXOpen.Li) TypeEnum
         Returns the platform type enum   
            
         
        """
        pass
    @property
    def VerticalGridSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) VerticalGridSpacing
         Returns the vertical grid spacing   
            
         
        """
        pass
    def SupportCrossSectionButton(self) -> None:
        """
          
        """
        pass
import NXOpen
class PreferencesBuilder(NXOpen.Builder): 
    """ use for creating preferences builder"""
    pass
import NXOpen
import NXOpen.Assemblies
class ProductionUnitCreatorBuilder(NXOpen.Builder): 
    """ 
    
    
    
    
    
    """
    @property
    def ProductionUnitId(self) -> str:
        """
        Getter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    @ProductionUnitId.setter
    def ProductionUnitId(self, productionUnitId: str):
        """
        Setter for property: (str) ProductionUnitId
         Returns the production unit id   
            
         
        """
        pass
    @property
    def ProductionUnitName(self) -> str:
        """
        Getter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    @ProductionUnitName.setter
    def ProductionUnitName(self, productionUnitName: str):
        """
        Setter for property: (str) ProductionUnitName
         Returns the production unit name   
            
         
        """
        pass
    @property
    def ProductionUnitTypeString(self) -> str:
        """
        Getter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    @ProductionUnitTypeString.setter
    def ProductionUnitTypeString(self, productionUnitType: str):
        """
        Setter for property: (str) ProductionUnitTypeString
         Returns the type of a production unit   
            
         
        """
        pass
    def AssignId(self) -> None:
        """
         The assign ID  of production unit
        """
        pass
    def GetProductionUnitDescription(self) -> List[str]:
        """
         The production unit description
         Returns productionUnitDescription (List[str]): .
        """
        pass
    def SetProductionUnitDescription(self, productionUnitDescription: List[str]) -> None:
        """
         The production unit description is set 
        """
        pass
    def SetProductionUnitParent(self, parent: NXOpen.Assemblies.Partition) -> None:
        """
         The production unit parent is set
        """
        pass
import NXOpen
import NXOpen.Features
import NXOpen.GeometricUtilities
class RailingFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
        Represents a LineDesigner.RailingFeature Features.FeatureBuilder
    """
    class PostOffsetType(Enum):
        """
        Members Include: 
         |PostOnCurve| 
         |PostLeftOfCurve| 
         |PostRightOfCurve| 

        """
        PostOnCurve: int
        PostLeftOfCurve: int
        PostRightOfCurve: int
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.PostOffsetType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class RailCrossStyle(Enum):
        """
        Members Include: 
         |Rectangle| 
         |Circle| 

        """
        Rectangle: int
        Circle: int
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.RailCrossStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelPostcrossStyle(Enum):
        """
        Members Include: 
         |IBeam| 
         |Rectangle| 
         |Circle| 
         |UserDefine| 

        """
        IBeam: int
        Rectangle: int
        Circle: int
        UserDefine: int
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.SelPostcrossStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SpaceType(Enum):
        """
        Members Include: 
         |CountandSpan| 
         |PitchandSpan| 
         |CountandPitch| 

        """
        CountandSpan: int
        PitchandSpan: int
        CountandPitch: int
        @staticmethod
        def ValueOf(value: int) -> RailingFeatureBuilder.SpaceType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def EnumPostCrossStyle(self) -> RailingFeatureBuilder.SelPostcrossStyle:
        """
        Getter for property: ( RailingFeatureBuilder.SelPostcrossStyle NXOpen.Li) EnumPostCrossStyle
         Returns the post cross style enum   
            
         
        """
        pass
    @EnumPostCrossStyle.setter
    def EnumPostCrossStyle(self, enumPostCrossStyle: RailingFeatureBuilder.SelPostcrossStyle):
        """
        Setter for property: ( RailingFeatureBuilder.SelPostcrossStyle NXOpen.Li) EnumPostCrossStyle
         Returns the post cross style enum   
            
         
        """
        pass
    @property
    def EnumRailCrossStyle(self) -> RailingFeatureBuilder.RailCrossStyle:
        """
        Getter for property: ( RailingFeatureBuilder.RailCrossStyle NXOpen.Li) EnumRailCrossStyle
         Returns the railing cross style enum   
            
         
        """
        pass
    @EnumRailCrossStyle.setter
    def EnumRailCrossStyle(self, enumRailCrossStyle: RailingFeatureBuilder.RailCrossStyle):
        """
        Setter for property: ( RailingFeatureBuilder.RailCrossStyle NXOpen.Li) EnumRailCrossStyle
         Returns the railing cross style enum   
            
         
        """
        pass
    @property
    def EnumSpacingType(self) -> RailingFeatureBuilder.SpaceType:
        """
        Getter for property: ( RailingFeatureBuilder.SpaceType NXOpen.Li) EnumSpacingType
         Returns an API to get spacing type enum   
            
         
        """
        pass
    @EnumSpacingType.setter
    def EnumSpacingType(self, enumSpacingType: RailingFeatureBuilder.SpaceType):
        """
        Setter for property: ( RailingFeatureBuilder.SpaceType NXOpen.Li) EnumSpacingType
         Returns an API to get spacing type enum   
            
         
        """
        pass
    @property
    def IntegerCount(self) -> int:
        """
        Getter for property: (int) IntegerCount
         Returns an API to get integer count   
            
         
        """
        pass
    @IntegerCount.setter
    def IntegerCount(self, integerCount: int):
        """
        Setter for property: (int) IntegerCount
         Returns an API to get integer count   
            
         
        """
        pass
    @property
    def IsSketchInternal(self) -> bool:
        """
        Getter for property: (bool) IsSketchInternal
         Returns an API to check if sketch is internal    
            
         
        """
        pass
    @IsSketchInternal.setter
    def IsSketchInternal(self, makeSketchInternal: bool):
        """
        Setter for property: (bool) IsSketchInternal
         Returns an API to check if sketch is internal    
            
         
        """
        pass
    @property
    def LinearDimBottomElevation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimBottomElevation
         Returns an API to get bottom elevation   
            
         
        """
        pass
    @property
    def LinearDimPitchBy(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimPitchBy
         Returns an API to get pitch by   
            
         
        """
        pass
    @property
    def LinearDimPostCrossDia(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimPostCrossDia
         Returns the post cross dimension of railing feature   
            
         
        """
        pass
    @property
    def LinearDimPostCrossLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimPostCrossLength
         Returns the post cross length  of railing feature   
            
         
        """
        pass
    @property
    def LinearDimPostCrossTickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimPostCrossTickness
         Returns the post cross thickness  of railing feature    
            
         
        """
        pass
    @property
    def LinearDimPostCrossWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimPostCrossWidth
         Returns the post cross width  of railing feature   
            
         
        """
        pass
    @property
    def LinearDimPostHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimPostHeight
         Returns the post height of railing feature   
            
         
        """
        pass
    @property
    def LinearDimPostSpacing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimPostSpacing
         Returns the post spacing  of railing feature   
            
         
        """
        pass
    @property
    def LinearDimRailCrossDia(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimRailCrossDia
         Returns an API to get railing cross diamension   
            
         
        """
        pass
    @property
    def LinearDimRailCrossLength(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimRailCrossLength
         Returns the railing cross length of railing feature   
            
         
        """
        pass
    @property
    def LinearDimRailCrossWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimRailCrossWidth
         Returns the railing cross width  of railing feature   
            
         
        """
        pass
    @property
    def OnPathDimSpanBy(self) -> NXOpen.GeometricUtilities.OnPathDimensionBuilder:
        """
        Getter for property: ( NXOpen.GeometricUtilities.OnPathDimensionBuilder) OnPathDimSpanBy
         Returns an API to get on path dimension span by   
            
         
        """
        pass
    @property
    def PostOffset(self) -> RailingFeatureBuilder.PostOffsetType:
        """
        Getter for property: ( RailingFeatureBuilder.PostOffsetType NXOpen.Li) PostOffset
         Returns the post offset  of railing feature    
            
         
        """
        pass
    @PostOffset.setter
    def PostOffset(self, postOffset: RailingFeatureBuilder.PostOffsetType):
        """
        Setter for property: ( RailingFeatureBuilder.PostOffsetType NXOpen.Li) PostOffset
         Returns the post offset  of railing feature    
            
         
        """
        pass
    @property
    def SelectionCurves(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectionCurves
         Returns the selected curves are return   
            
         
        """
        pass
    @property
    def SelectionPostCrossSection(self) -> NXOpen.Section:
        """
        Getter for property: ( NXOpen.Section) SelectionPostCrossSection
         Returns the selection post cross section   
            
         
        """
        pass
import NXOpen.Features
class RailingFeature(NXOpen.Features.Feature): 
    """ Represents a rail feature """
    pass
import NXOpen
import NXOpen.Features
class RailOpeningFeatureBuilder(NXOpen.Builder): 
    """
    Represents a LineDesigner.RailOpeningFeature builder
    """
    class GateOpeningStyle(Enum):
        """
        Members Include: 
         |Left| 
         |Middle| 
         |Right| 

        """
        Left: int
        Middle: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> RailOpeningFeatureBuilder.GateOpeningStyle:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def LinearDimElevation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimElevation
         Returns the rail opening elevation   
            
         
        """
        pass
    @property
    def LinearDimGateThickness(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimGateThickness
         Returns the gate thickness   
            
         
        """
        pass
    @property
    def LinearDimOpeningWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) LinearDimOpeningWidth
         Returns the rail opening width   
            
         
        """
        pass
    @property
    def OpeningAddGate(self) -> bool:
        """
        Getter for property: (bool) OpeningAddGate
         Returns the opening add gate is return  
            
         
        """
        pass
    @OpeningAddGate.setter
    def OpeningAddGate(self, openingAddGate: bool):
        """
        Setter for property: (bool) OpeningAddGate
         Returns the opening add gate is return  
            
         
        """
        pass
    @property
    def OpeningStyleEnum(self) -> RailOpeningFeatureBuilder.GateOpeningStyle:
        """
        Getter for property: ( RailOpeningFeatureBuilder.GateOpeningStyle NXOpen.Li) OpeningStyleEnum
         Returns the rail opening style enum   
            
         
        """
        pass
    @OpeningStyleEnum.setter
    def OpeningStyleEnum(self, openingStyleEnum: RailOpeningFeatureBuilder.GateOpeningStyle):
        """
        Setter for property: ( RailOpeningFeatureBuilder.GateOpeningStyle NXOpen.Li) OpeningStyleEnum
         Returns the rail opening style enum   
            
         
        """
        pass
    @property
    def ReverseDirection(self) -> bool:
        """
        Getter for property: (bool) ReverseDirection
         Returns the reverse direction of rail opening   
            
         
        """
        pass
    @ReverseDirection.setter
    def ReverseDirection(self, reverseDirection: bool):
        """
        Setter for property: (bool) ReverseDirection
         Returns the reverse direction of rail opening   
            
         
        """
        pass
    @property
    def SelectPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SelectPoint
         Returns the selected point of rail opening feature   
            
         
        """
        pass
    @SelectPoint.setter
    def SelectPoint(self, selectPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SelectPoint
         Returns the selected point of rail opening feature   
            
         
        """
        pass
    def GetDirVector(self) -> NXOpen.Direction:
        """
         Direction of rail opening 
         Returns dirVector ( NXOpen.Direction): .
        """
        pass
    def SetDirVector(self, dirVector: NXOpen.Direction) -> None:
        """
              
        """
        pass
    def SetRailingFeature(self, railingFrec: NXOpen.Features.Feature) -> None:
        """
             
        """
        pass
import NXOpen.Features
class RailOpeningFeature(NXOpen.Features.Feature): 
    """ Represents a rail Opening feature """
    pass
import NXOpen
class RenameDialogeBuilder(NXOpen.Builder): 
    """  """
    class SelectionTypeAPI(Enum):
        """
        Members Include: 
         |ItemRevisionName| 
         |OccurenceName| 

        """
        ItemRevisionName: int
        OccurenceName: int
        @staticmethod
        def ValueOf(value: int) -> RenameDialogeBuilder.SelectionTypeAPI:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
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
    def NumberingStartAt(self) -> int:
        """
        Getter for property: (int) NumberingStartAt
         Returns the numbering start at   
            
         
        """
        pass
    @NumberingStartAt.setter
    def NumberingStartAt(self, numberingStartAt: int):
        """
        Setter for property: (int) NumberingStartAt
         Returns the numbering start at   
            
         
        """
        pass
    @property
    def SelectionEnum(self) -> RenameDialogeBuilder.SelectionTypeAPI:
        """
        Getter for property: ( RenameDialogeBuilder.SelectionTypeAPI NXOpen.Li) SelectionEnum
         Returns the item or occurence selection   
            
         
        """
        pass
    @SelectionEnum.setter
    def SelectionEnum(self, selectionEnum: RenameDialogeBuilder.SelectionTypeAPI):
        """
        Setter for property: ( RenameDialogeBuilder.SelectionTypeAPI NXOpen.Li) SelectionEnum
         Returns the item or occurence selection   
            
         
        """
        pass
import NXOpen
class RenameItemRevisionBuilder(NXOpen.Builder): 
    """  """
    @property
    def ItemRevisionName(self) -> str:
        """
        Getter for property: (str) ItemRevisionName
         Returns the item revision name   
            
         
        """
        pass
    @ItemRevisionName.setter
    def ItemRevisionName(self, itemRevisionName: str):
        """
        Setter for property: (str) ItemRevisionName
         Returns the item revision name   
            
         
        """
        pass
    @property
    def OccurrenceName(self) -> str:
        """
        Getter for property: (str) OccurrenceName
         Returns the occurrence name is return   
            
         
        """
        pass
    @OccurrenceName.setter
    def OccurrenceName(self, occurrenceName: str):
        """
        Setter for property: (str) OccurrenceName
         Returns the occurrence name is return   
            
         
        """
        pass
    @property
    def PartOccurence(self) -> NXOpen.TaggedObject:
        """
        Getter for property: ( NXOpen.TaggedObject) PartOccurence
         Returns the part occurence   
            
         
        """
        pass
import NXOpen
class ResizeConnectorBuilder(NXOpen.Builder): 
    """
    
    
    
    
    
     """
    @property
    def ConnectorSize(self) -> float:
        """
        Getter for property: (float) ConnectorSize
         Returnsthe current connector size   
            
         
        """
        pass
    @ConnectorSize.setter
    def ConnectorSize(self, connectorSize: float):
        """
        Setter for property: (float) ConnectorSize
         Returnsthe current connector size   
            
         
        """
        pass
import NXOpen
class ReuseLibraryDragData(NXOpen.NXObject): 
    """ Represents a manager of line designer plant model """
    @property
    def ActionType(self) -> int:
        """
        Getter for property: (int) ActionType
         Returns the action type of drag data   
            
         
        """
        pass
    @ActionType.setter
    def ActionType(self, actionType: int):
        """
        Setter for property: (int) ActionType
         Returns the action type of drag data   
            
         
        """
        pass
    @property
    def CategoryName(self) -> str:
        """
        Getter for property: (str) CategoryName
         Returns the category name of Drag Data   
            
         
        """
        pass
    @CategoryName.setter
    def CategoryName(self, categoryName: str):
        """
        Setter for property: (str) CategoryName
         Returns the category name of Drag Data   
            
         
        """
        pass
    @property
    def HasCsysImport(self) -> bool:
        """
        Getter for property: (bool) HasCsysImport
         Returns an API to check if drag data has csys import   
            
         
        """
        pass
    @HasCsysImport.setter
    def HasCsysImport(self, hasCsysImport: bool):
        """
        Setter for property: (bool) HasCsysImport
         Returns an API to check if drag data has csys import   
            
         
        """
        pass
    @property
    def HasSketchImport(self) -> bool:
        """
        Getter for property: (bool) HasSketchImport
         Returns an API to check if drag data has sketch to import   
            
         
        """
        pass
    @HasSketchImport.setter
    def HasSketchImport(self, hasSketchImport: bool):
        """
        Setter for property: (bool) HasSketchImport
         Returns an API to check if drag data has sketch to import   
            
         
        """
        pass
    @property
    def KrxFile(self) -> str:
        """
        Getter for property: (str) KrxFile
         Returns the krx file name   
            
         
        """
        pass
    @KrxFile.setter
    def KrxFile(self, krxFile: str):
        """
        Setter for property: (str) KrxFile
         Returns the krx file name   
            
         
        """
        pass
    @property
    def LibName(self) -> str:
        """
        Getter for property: (str) LibName
         Returns the library name of  Reuse Library Drag data  
            
         
        """
        pass
    @LibName.setter
    def LibName(self, libName: str):
        """
        Setter for property: (str) LibName
         Returns the library name of  Reuse Library Drag data  
            
         
        """
        pass
    @property
    def NativeItem(self) -> int:
        """
        Getter for property: (int) NativeItem
         Returns the native item   
            
         
        """
        pass
    @NativeItem.setter
    def NativeItem(self, nativeItem: int):
        """
        Setter for property: (int) NativeItem
         Returns the native item   
            
         
        """
        pass
    @property
    def ObjectId(self) -> str:
        """
        Getter for property: (str) ObjectId
         Returns the object id of Drag Data  
            
         
        """
        pass
    @ObjectId.setter
    def ObjectId(self, objectId: str):
        """
        Setter for property: (str) ObjectId
         Returns the object id of Drag Data  
            
         
        """
        pass
    @property
    def PartFile(self) -> str:
        """
        Getter for property: (str) PartFile
         Returns the part file name is return   
            
         
        """
        pass
    @PartFile.setter
    def PartFile(self, partFile: str):
        """
        Setter for property: (str) PartFile
         Returns the part file name is return   
            
         
        """
        pass
    @property
    def PartType(self) -> int:
        """
        Getter for property: (int) PartType
         Returns the part type of Reuse Library Drag data   
            
         
        """
        pass
    @PartType.setter
    def PartType(self, partType: int):
        """
        Setter for property: (int) PartType
         Returns the part type of Reuse Library Drag data   
            
         
        """
        pass
    @property
    def PathInLib(self) -> str:
        """
        Getter for property: (str) PathInLib
         Returns the path in library of drag data  
            
         
        """
        pass
    @PathInLib.setter
    def PathInLib(self, pathInLib: str):
        """
        Setter for property: (str) PathInLib
         Returns the path in library of drag data  
            
         
        """
        pass
    @property
    def SpareDialogForDragAndDrop(self) -> bool:
        """
        Getter for property: (bool) SpareDialogForDragAndDrop
         Returns an API to check if spare dialog for drag and drop is allowed   
            
         
        """
        pass
    @SpareDialogForDragAndDrop.setter
    def SpareDialogForDragAndDrop(self, spareDialogForDragAndDrop: bool):
        """
        Setter for property: (bool) SpareDialogForDragAndDrop
         Returns an API to check if spare dialog for drag and drop is allowed   
            
         
        """
        pass
    @property
    def TemplateName(self) -> str:
        """
        Getter for property: (str) TemplateName
         Returns the template name   
            
         
        """
        pass
    @TemplateName.setter
    def TemplateName(self, templateName: str):
        """
        Setter for property: (str) TemplateName
         Returns the template name   
            
         
        """
        pass
    @property
    def TypeName(self) -> str:
        """
        Getter for property: (str) TypeName
         Returns an API to get type name   
            
         
        """
        pass
    @TypeName.setter
    def TypeName(self, typeName: str):
        """
        Setter for property: (str) TypeName
         Returns an API to get type name   
            
         
        """
        pass
import NXOpen
class ReuseLibraryUtilityBuilder(NXOpen.TaggedObject): 
    """ Represents a JA for ReuseLibraryUtility """
    @property
    def DoNormalCloning(self) -> bool:
        """
        Getter for property: (bool) DoNormalCloning
         Returns the normal drop or cloning Drop   
            
         
        """
        pass
    @DoNormalCloning.setter
    def DoNormalCloning(self, doNormalCloning: bool):
        """
        Setter for property: (bool) DoNormalCloning
         Returns the normal drop or cloning Drop   
            
         
        """
        pass
    def CloneForFCADDataSet(self, part: NXOpen.NXObject, bRenameAssembly: bool) -> None:
        """
          To allows cloning of data set attched to FCAD object 
        """
        pass
    def CreateDragData(self) -> ReuseLibraryDragData:
        """
         To create drag data 
         Returns dragData ( ReuseLibraryDragData NXOpen.Li): .
        """
        pass
    def DragAndDropCompleted(self, part: NXOpen.NXObject) -> None:
        """
         Mark Drag and Drop as completed 
        """
        pass
    def DropFCADPartInNative(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
          To handle dropping of LD smart part 
         Returns droppedPart ( NXOpen.NXObject): .
        """
        pass
    def DropKnowledgeEnabledPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d, isSkipAddReusableCompUI: bool) -> NXOpen.NXObject:
        """
          To handle dropping of knowledge enabled part KRU_KE_PART 
         Returns droppedPart ( NXOpen.NXObject): .
        """
        pass
    def DropLDSmartPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
          To handle dropping of LD smart part 
         Returns droppedPart ( NXOpen.NXObject): .
        """
        pass
    def DropNormalPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
          To handle dropping of normal part 
         Returns droppedPart ( NXOpen.NXObject): .
        """
        pass
    def DropOtherPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> None:
        """
          To handle dropping of other part 
        """
        pass
    def DropPTSPart(self, reuseLibraryDragData: ReuseLibraryDragData, dropPoint: NXOpen.Vector3d) -> NXOpen.NXObject:
        """
         To handle dropping of PTS part 
         Returns droppedPart ( NXOpen.NXObject): .
        """
        pass
    def ExecuteRenameAssembly(self) -> None:
        """
          To executes the renaming of the cloned component when it is added under an assembly 
        """
        pass
    def GetDLGFile(self, part: NXOpen.NXObject) -> str:
        """
         Get dialog file name for object getting inserting  
         Returns dlgFilePath (str): .
        """
        pass
    def GetGEOFile(self, part: NXOpen.NXObject) -> str:
        """
         Get Geo file name for object getting inserting  
         Returns geoFileName (str): .
        """
        pass
    def GetParameterSetFile(self, part: NXOpen.NXObject) -> str:
        """
         Get Parameter file name for object getting inserting  
         Returns parameterSetFilePath (str): .
        """
        pass
    def KeepSourceLibraryID(self, part: NXOpen.NXObject, keepSourcePath: bool) -> None:
        """
          To keep source library item ID 
        """
        pass
    def LoadFCADGeoFile(self, part: NXOpen.NXObject) -> None:
        """
          To load data set attched to FCAD object 
        """
        pass
    def MountToolOnRobot(self, part: NXOpen.NXObject, connectorFaceTag: NXOpen.TaggedObject) -> None:
        """
          To mount tool from library on robot 
        """
        pass
    def MoveComponentToLocation(self, part: NXOpen.NXObject, position: NXOpen.Vector3d) -> None:
        """
         Move component to the location 
        """
        pass
    def PlacementByConnector(self, part: NXOpen.NXObject, connectorFaceTag: NXOpen.TaggedObject) -> None:
        """
          To place part from library using connector 
        """
        pass
    def PopulateMDOInfo(self, part: NXOpen.NXObject) -> None:
        """
          To populate MDO information 
        """
        pass
    def UpdateClonedPartTag(self, part: NXOpen.NXObject) -> None:
        """
          To update cloned part 
        """
        pass
import NXOpen
class RotateComponentBuilder(NXOpen.Builder): 
    """ Create a builder to rotate a component by 90 degrees."""
    @property
    def AngularDim(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) AngularDim
         Returns the angular dimension for rotate component   
            
         
        """
        pass
    @property
    def RotateAsGroup(self) -> bool:
        """
        Getter for property: (bool) RotateAsGroup
         Returns the toggle to rotate as group   
            
         
        """
        pass
    @RotateAsGroup.setter
    def RotateAsGroup(self, toggle: bool):
        """
        Setter for property: (bool) RotateAsGroup
         Returns the toggle to rotate as group   
            
         
        """
        pass
    @property
    def SelectObject(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectObject
         Returns the selected component   
            
         
        """
        pass
import NXOpen
class SelectionToolBuilder(NXOpen.Builder): 
    """
    
    
    
    
    
    """
    class RefSetOption(Enum):
        """
        Members Include: 
         |Add| 
         |Replace| 

        """
        Add: int
        Replace: int
        @staticmethod
        def ValueOf(value: int) -> SelectionToolBuilder.RefSetOption:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SelectionView(Enum):
        """
        Members Include: 
         |SixStandard| 
         |EightIsometric| 
         |AllFourteen| 

        """
        SixStandard: int
        EightIsometric: int
        AllFourteen: int
        @staticmethod
        def ValueOf(value: int) -> SelectionToolBuilder.SelectionView:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AddOption(self) -> SelectionToolBuilder.RefSetOption:
        """
        Getter for property: ( SelectionToolBuilder.RefSetOption NXOpen.Li) AddOption
         Returns the add option   
            
         
        """
        pass
    @AddOption.setter
    def AddOption(self, addOption: SelectionToolBuilder.RefSetOption):
        """
        Setter for property: ( SelectionToolBuilder.RefSetOption NXOpen.Li) AddOption
         Returns the add option   
            
         
        """
        pass
    @property
    def AddToReferenceSet(self) -> bool:
        """
        Getter for property: (bool) AddToReferenceSet
         Returns the add to Reference set   
            
         
        """
        pass
    @AddToReferenceSet.setter
    def AddToReferenceSet(self, addToRefSet: bool):
        """
        Setter for property: (bool) AddToReferenceSet
         Returns the add to Reference set   
            
         
        """
        pass
    @property
    def ExcludeConnectors(self) -> bool:
        """
        Getter for property: (bool) ExcludeConnectors
         Returns the exclude connectors toggle   
            
         
        """
        pass
    @ExcludeConnectors.setter
    def ExcludeConnectors(self, excludeConnectors: bool):
        """
        Setter for property: (bool) ExcludeConnectors
         Returns the exclude connectors toggle   
            
         
        """
        pass
    @property
    def ExcludeObjectSize(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) ExcludeObjectSize
         Returns the exclude small object size  
            
         
        """
        pass
    @property
    def ExcludeSmallObjects(self) -> bool:
        """
        Getter for property: (bool) ExcludeSmallObjects
         Returns the exclude object toggle   
            
         
        """
        pass
    @ExcludeSmallObjects.setter
    def ExcludeSmallObjects(self, excludeSmallObjects: bool):
        """
        Setter for property: (bool) ExcludeSmallObjects
         Returns the exclude object toggle   
            
         
        """
        pass
    @property
    def IncludeAboveZ(self) -> bool:
        """
        Getter for property: (bool) IncludeAboveZ
         Returns the include above z   
            
         
        """
        pass
    @IncludeAboveZ.setter
    def IncludeAboveZ(self, includeAboveZ: bool):
        """
        Setter for property: (bool) IncludeAboveZ
         Returns the include above z   
            
         
        """
        pass
    @property
    def SelectedRefSet(self) -> str:
        """
        Getter for property: (str) SelectedRefSet
         Returns the selected ref set name string   
            
         
        """
        pass
    @SelectedRefSet.setter
    def SelectedRefSet(self, refSetName: str):
        """
        Setter for property: (str) SelectedRefSet
         Returns the selected ref set name string   
            
         
        """
        pass
    @property
    def View(self) -> SelectionToolBuilder.SelectionView:
        """
        Getter for property: ( SelectionToolBuilder.SelectionView NXOpen.Li) View
         Returns the view   
            
         
        """
        pass
    @View.setter
    def View(self, view: SelectionToolBuilder.SelectionView):
        """
        Setter for property: ( SelectionToolBuilder.SelectionView NXOpen.Li) View
         Returns the view   
            
         
        """
        pass
    def CalculateSelection(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def InvertSelection(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def ShowAll(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
    def ShowOnly(self) -> None:
        """
         TODO: fill in a description for this 
        """
        pass
import NXOpen
class SingleElementConveyorBuilder(NXOpen.Builder): 
    """     """
    @property
    def FirstConveyingSurfaceCroner(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) FirstConveyingSurfaceCroner
         Returns the first conveying surface corner of conveyor  
            
         
        """
        pass
    @FirstConveyingSurfaceCroner.setter
    def FirstConveyingSurfaceCroner(self, firstConveyingSurfaceCroner: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) FirstConveyingSurfaceCroner
         Returns the first conveying surface corner of conveyor  
            
         
        """
        pass
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: ( NXOpen.KFObject) KfObject
         Returns the kf object   
            
         
        """
        pass
    @property
    def MovingDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) MovingDirection
         Returns the moving direction of conveyor   
            
         
        """
        pass
    @MovingDirection.setter
    def MovingDirection(self, dirVector: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) MovingDirection
         Returns the moving direction of conveyor   
            
         
        """
        pass
    @property
    def PointOnConveyingSurface(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) PointOnConveyingSurface
         Returns the point on surface of conveyor are return   
            
         
        """
        pass
    @PointOnConveyingSurface.setter
    def PointOnConveyingSurface(self, pointOnConveyingSurface: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) PointOnConveyingSurface
         Returns the point on surface of conveyor are return   
            
         
        """
        pass
    @property
    def Reversible(self) -> bool:
        """
        Getter for property: (bool) Reversible
         Returns the option to check whether conveyor is reversible   
            
         
        """
        pass
    @Reversible.setter
    def Reversible(self, reversible: bool):
        """
        Setter for property: (bool) Reversible
         Returns the option to check whether conveyor is reversible   
            
         
        """
        pass
    @property
    def SecondConveyingSurfaceCorner(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) SecondConveyingSurfaceCorner
         Returns the second conveying surface corner of conveyor   
            
         
        """
        pass
    @SecondConveyingSurfaceCorner.setter
    def SecondConveyingSurfaceCorner(self, secondConveyingSurfaceCorner: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) SecondConveyingSurfaceCorner
         Returns the second conveying surface corner of conveyor   
            
         
        """
        pass
import NXOpen
class StairwayEquipmentBuilder(NXOpen.Builder): 
    """   """
    @property
    def AddLeftRailingToggle(self) -> bool:
        """
        Getter for property: (bool) AddLeftRailingToggle
         Returns the left railing toggle   
            
         
        """
        pass
    @AddLeftRailingToggle.setter
    def AddLeftRailingToggle(self, addLeftRailingToggle: bool):
        """
        Setter for property: (bool) AddLeftRailingToggle
         Returns the left railing toggle   
            
         
        """
        pass
    @property
    def AddRightRailingToggle(self) -> bool:
        """
        Getter for property: (bool) AddRightRailingToggle
         Returns the right railing toggle   
            
         
        """
        pass
    @AddRightRailingToggle.setter
    def AddRightRailingToggle(self, addRightRailingToggle: bool):
        """
        Setter for property: (bool) AddRightRailingToggle
         Returns the right railing toggle   
            
         
        """
        pass
    @property
    def AddRiserToggle(self) -> bool:
        """
        Getter for property: (bool) AddRiserToggle
         Returns the riser toggle   
            
         
        """
        pass
    @AddRiserToggle.setter
    def AddRiserToggle(self, addRiserToggle: bool):
        """
        Setter for property: (bool) AddRiserToggle
         Returns the riser toggle   
            
         
        """
        pass
    @property
    def AddStringerToggle(self) -> bool:
        """
        Getter for property: (bool) AddStringerToggle
         Returns the stringer toggle   
            
         
        """
        pass
    @AddStringerToggle.setter
    def AddStringerToggle(self, addStringerToggle: bool):
        """
        Setter for property: (bool) AddStringerToggle
         Returns the stringer toggle   
            
         
        """
        pass
    @property
    def EndElevation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) EndElevation
         Returns the end elevation of stairway  
            
         
        """
        pass
    @property
    def KfObject(self) -> NXOpen.KFObject:
        """
        Getter for property: ( NXOpen.KFObject) KfObject
         Returns the kf object is return  
            
         
        """
        pass
    @property
    def NoOfStairs(self) -> int:
        """
        Getter for property: (int) NoOfStairs
         Returns the number of stairs   
            
         
        """
        pass
    @NoOfStairs.setter
    def NoOfStairs(self, noOfStairs: int):
        """
        Setter for property: (int) NoOfStairs
         Returns the number of stairs   
            
         
        """
        pass
    @property
    def Rise(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Rise
         Returns the vertical distance between two steps   
            
         
        """
        pass
    @property
    def Run(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) Run
         Returns the run   
            
         
        """
        pass
    @property
    def StairNosing(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StairNosing
         Returns the stair nosing   
            
         
        """
        pass
    @property
    def StairWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StairWidth
         Returns the stair width   
            
         
        """
        pass
    @property
    def StartElevation(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StartElevation
         Returns the start elevation of stairway   
            
         
        """
        pass
    @property
    def StringerHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StringerHeight
         Returns the stringer height   
            
         
        """
        pass
    @property
    def StringerWidth(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) StringerWidth
         Returns the stringer width   
            
         
        """
        pass
    @property
    def TotalRise(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TotalRise
         Returns the total rise   
            
         
        """
        pass
    @property
    def TotalRun(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TotalRun
         Returns the total run   
            
         
        """
        pass
    @property
    def TreadHeight(self) -> NXOpen.Expression:
        """
        Getter for property: ( NXOpen.Expression) TreadHeight
         Returns the tread height   
            
         
        """
        pass
class TailConnectorFeature(TypedConnectorFeature): 
    """ Represents a typed connector feature feature """
    pass
import NXOpen
import NXOpen.Features
class TypedConnectorFeatureBuilder(NXOpen.Features.FeatureBuilder): 
    """
    Represents a LineDesigner.TypedConnectorFeature Features.FeatureBuilder
    """
    class BehaviorOnMismatch(Enum):
        """
        Members Include: 
         |Dontcreatetheconnection| 
         |Continuewithoutpropagatingtheparticularone| 

        """
        Dontcreatetheconnection: int
        Continuewithoutpropagatingtheparticularone: int
        @staticmethod
        def ValueOf(value: int) -> TypedConnectorFeatureBuilder.BehaviorOnMismatch:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ConnectorColor(self) -> int:
        """
        Getter for property: (int) ConnectorColor
         Returns the connector color   
            
         
        """
        pass
    @ConnectorColor.setter
    def ConnectorColor(self, connectorColor: int):
        """
        Setter for property: (int) ConnectorColor
         Returns the connector color   
            
         
        """
        pass
    @property
    def ConnectorCompatibleTypeName(self) -> str:
        """
        Getter for property: (str) ConnectorCompatibleTypeName
         Returns the connector compatible type name   
            
         
        """
        pass
    @ConnectorCompatibleTypeName.setter
    def ConnectorCompatibleTypeName(self, connectorCompatibleTypeName: str):
        """
        Setter for property: (str) ConnectorCompatibleTypeName
         Returns the connector compatible type name   
            
         
        """
        pass
    @property
    def ConnectorDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ConnectorDirection
         Returns the connector direction   
            
         
        """
        pass
    @ConnectorDirection.setter
    def ConnectorDirection(self, connectorDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ConnectorDirection
         Returns the connector direction   
            
         
        """
        pass
    @property
    def ConnectorName(self) -> str:
        """
        Getter for property: (str) ConnectorName
         Returns the connector name   
            
         
        """
        pass
    @ConnectorName.setter
    def ConnectorName(self, connectorName: str):
        """
        Setter for property: (str) ConnectorName
         Returns the connector name   
            
         
        """
        pass
    @property
    def ConnectorParallelToObjectDirection(self) -> NXOpen.Direction:
        """
        Getter for property: ( NXOpen.Direction) ConnectorParallelToObjectDirection
         Returns the connector parallel to object direction   
            
         
        """
        pass
    @ConnectorParallelToObjectDirection.setter
    def ConnectorParallelToObjectDirection(self, connectorParallelToObjectDirection: NXOpen.Direction):
        """
        Setter for property: ( NXOpen.Direction) ConnectorParallelToObjectDirection
         Returns the connector parallel to object direction   
            
         
        """
        pass
    @property
    def ConnectorPoint(self) -> NXOpen.Point:
        """
        Getter for property: ( NXOpen.Point) ConnectorPoint
         Returns the connector point   
            
         
        """
        pass
    @ConnectorPoint.setter
    def ConnectorPoint(self, connectorPoint: NXOpen.Point):
        """
        Setter for property: ( NXOpen.Point) ConnectorPoint
         Returns the connector point   
            
         
        """
        pass
    @property
    def ConnectorTypeName(self) -> str:
        """
        Getter for property: (str) ConnectorTypeName
         Returns the connector type name   
            
         
        """
        pass
    @ConnectorTypeName.setter
    def ConnectorTypeName(self, connectorTypeName: str):
        """
        Setter for property: (str) ConnectorTypeName
         Returns the connector type name   
            
         
        """
        pass
    @property
    def DefaultConnector(self) -> bool:
        """
        Getter for property: (bool) DefaultConnector
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    @DefaultConnector.setter
    def DefaultConnector(self, defaultConnector: bool):
        """
        Setter for property: (bool) DefaultConnector
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    @property
    def MismatchBehavior(self) -> TypedConnectorFeatureBuilder.BehaviorOnMismatch:
        """
        Getter for property: ( TypedConnectorFeatureBuilder.BehaviorOnMismatch NXOpen.Li) MismatchBehavior
         Returns the status of behavior on mismatch property   
            
         
        """
        pass
    @MismatchBehavior.setter
    def MismatchBehavior(self, mismatchBehavior: TypedConnectorFeatureBuilder.BehaviorOnMismatch):
        """
        Setter for property: ( TypedConnectorFeatureBuilder.BehaviorOnMismatch NXOpen.Li) MismatchBehavior
         Returns the status of behavior on mismatch property   
            
         
        """
        pass
    @property
    def ReversePropagation(self) -> bool:
        """
        Getter for property: (bool) ReversePropagation
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    @ReversePropagation.setter
    def ReversePropagation(self, reversePropagation: bool):
        """
        Setter for property: (bool) ReversePropagation
         Returns the status of if reverse propagation is on   
            
         
        """
        pass
    @property
    def TypedConnectorName(self) -> str:
        """
        Getter for property: (str) TypedConnectorName
         Returns the typed connector name   
            
         
        """
        pass
    @TypedConnectorName.setter
    def TypedConnectorName(self, typedConnectorName: str):
        """
        Setter for property: (str) TypedConnectorName
         Returns the typed connector name   
            
         
        """
        pass
    def GetConnectorCompatibleTypeList(self) -> List[str]:
        """
          The compatible connector types are returns 
         Returns connectorCompatibleTypeList (List[str]): .
        """
        pass
    def GetConnectorExpressionPropagationList(self) -> List[NXOpen.Expression]:
        """
         The connectors propagated expressions 
         Returns connectorExpressionPropagationList ( NXOpen.Expression Li): .
        """
        pass
    def SelectPropagatedExpressions(self) -> None:
        """
         The propagated expressions is set during creation of connector 
        """
        pass
    def SetConnectorCompatibleTypeList(self, connectorCompatibleTypeList: List[str]) -> None:
        """
         The connector compatible types are set 
        """
        pass
    def SetConnectorExpressionPropagationList(self, connectorExpressionPropagationList: List[NXOpen.Expression]) -> None:
        """
        The connectors propagated expressions are set 
        """
        pass
    def SetNthConnectorExpressionPropagationList(self, nthExpressionPropagationList: int, connectorExpressionPropagationList: NXOpen.Expression) -> None:
        """
         The Nth expressions from connectors propagated expressions are set
        """
        pass
import NXOpen.Features
class TypedConnectorFeature(NXOpen.Features.Feature): 
    """ Represents a typed connector feature feature """
    pass
import NXOpen
import NXOpen.Assemblies
import NXOpen.PDM
class UINodeUtils(NXOpen.Object): 
    """ Represents a utils of line designer for journaling uinode methods """
    def BVRModelIgnoreCallbacks(ignore: bool) -> None:
        """
         To control execution of BVR Model callbacks 
        """
        pass
    def CalculateAndSetNameOfAGAttr(attributeGroup: NXOpen.PDM.AttributeGroup, subAGName: str, resourceName: str) -> None:
        """
         To calculate and set attribute group name 
        """
        pass
    def DeleteConnectionInfoNode(sourcePartOcc: NXOpen.NXObject, targetPartOcc: NXOpen.NXObject) -> None:
        """
         Set column occurrence type For Edit In Cell 
        """
        pass
    def DeleteConstraint(constraintTag: NXOpen.NXObject) -> None:
        """
         To delete constraint 
        """
        pass
    def DeleteDragAndDropUndoMark(undoMarkName: str) -> None:
        """
         To Delete DragAndDrop Undo Mark
        """
        pass
    def DisconnectNXConnection(sourcePartOcc: NXOpen.NXObject, targetPartOcc: NXOpen.NXObject) -> None:
        """
         To delete connection between two objects 
        """
        pass
    def DisplayPMIThroughShadedModel() -> None:
        """
         To display Assembly PMI Through Shaded Model 
        """
        pass
    def DragAndDropStation(stationProcessTag: NXOpen.NXObject) -> None:
        """
         To DragAndDrop Station
        """
        pass
    def ExpandCollapsEndItem(selectedEndItem: List[NXOpen.NXObject]) -> None:
        """
         To ExpandCollaps End Item
        """
        pass
    def GetItemRevisionName(partTag: NXOpen.Part) -> str:
        """
         To get item revision name 
         Returns itemRevName (str): .
        """
        pass
    def GetOccurrenceName(instanceTag: NXOpen.NXObject) -> str:
        """
         To get occurence name 
         Returns occurrenceName (str): .
        """
        pass
    def LoadChildrenParts(owningPartOccurrence: NXOpen.NXObject) -> bool:
        """
         To partially load the children with LD connectors 
         Returns found (bool): .
        """
        pass
    def MoveConnectors(partOccTag: NXOpen.NXObject, targ: NXOpen.NXObject, value: float, isNotBondConstraint: bool, isPropogationAllowed: bool) -> None:
        """
         To move connectors while DnD of assembly 
        """
        pass
    def MoveToolToOriginalPosition(mountBuilder: MountBuilder, toolBaseConnectorTag: NXOpen.NXObject) -> None:
        """
         Move Tool to original position 
        """
        pass
    def MoveToolToRobotAndOrientAsPerConnector(mountBuilder: MountBuilder) -> None:
        """
         Move Tool to Robot and orient as per connector 
        """
        pass
    def Rename(objtg: ModelProductionUnit, newName: str) -> None:
        """
         To rename partition 
        """
        pass
    def RenamePartition(objtg: NXOpen.Assemblies.Partition, newName: str) -> None:
        """
         To rename partition in new PLNAV 
        """
        pass
    def ResizeConnectors(connectors: List[NXOpen.NXObject], connectorSize: float) -> None:
        """
         To resize the Connectors per the Zoom Level 
        """
        pass
    def RetreiveFinalTransformedToolConnectorDetailsAfterMoveAndMount(builderTag: MountBuilder) -> Tuple[NXOpen.Point3d, NXOpen.Vector3d, NXOpen.Vector3d]:
        """
         Retreive final tool transformation parameters 
         Returns A tuple consisting of (finalTransformedToolConnectorPointAfterMoveAndMount, finalTransformedToolConnectorXDirAfterMoveAndMount, finalTransformedToolConnectorYDirAfterMoveAndMount). 
         - finalTransformedToolConnectorPointAfterMoveAndMount is:  NXOpen.Point3d.
         - finalTransformedToolConnectorXDirAfterMoveAndMount is:  NXOpen.Vector3d.
         - finalTransformedToolConnectorYDirAfterMoveAndMount is:  NXOpen.Vector3d.

        """
        pass
    def RotateComponent(partOccTags: List[NXOpen.NXObject], isClockwise: bool, rotateAsGroup: bool, angleStep: float) -> None:
        """
         To rotate a given component in clockwise or anticlockwise direction by 90 degrees 
        """
        pass
    def SaveFinalTransformedToolConnectorDetailsAfterMoveAndMount(builderTag: MountBuilder, finalTransformedToolConnectorPointAfterMoveAndMount: NXOpen.Point3d, finalTransformedToolConnectorXDirAfterMoveAndMount: NXOpen.Vector3d, finalTransformedToolConnectorYDirAfterMoveAndMount: NXOpen.Vector3d) -> None:
        """
         Save final tool transformation parameters 
        """
        pass
    def SetColumnOccurrenceType(partOcc: NXOpen.NXObject, newPropertyValu: str) -> None:
        """
         Set column occurrence type For Edit In Cell 
        """
        pass
    def SetItemRevisionName(partTag: NXOpen.Part, itemRevName: str) -> None:
        """
         To set item revision name 
        """
        pass
    def SetOccurrenceName(instanceTag: NXOpen.NXObject, occurrenceName: str) -> None:
        """
         To set occurence name 
        """
        pass
    def SetProductionUnitAsWorkPart(constraintTag: NXOpen.NXObject) -> None:
        """
         Set Target Production Unit 
        """
        pass
    def ShowAssemblyPMI() -> None:
        """
         To enable assembly PMI 
        """
        pass
import NXOpen
class UnmountBuilder(NXOpen.Builder): 
    """
    UnmountBuilder Class: Used when unmounting a tool from robot.
    """
    @property
    def SelectUnmountEntity(self) -> NXOpen.SelectDisplayableObjectList:
        """
        Getter for property: ( NXOpen.SelectDisplayableObjectList) SelectUnmountEntity
         Returns the select unmount entity   
            
         
        """
        pass
    def SetSelectedUnmountEntity(self, selectedUnmountEntityTag: NXOpen.TaggedObject) -> None:
        """
         The set selected unmount entity
        """
        pass
