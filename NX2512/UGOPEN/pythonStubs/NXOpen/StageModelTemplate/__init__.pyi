from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class Manager(NXOpen.Object): 
    """ Represents the StageModelTemplate Manager class."""
    def CreateStageSetTemplateBuilder(part: NXOpen.Part, stagesettemplate: StageSetTemplate) -> StageSetTemplateBuilder:
        """
         Creates a StageModelTemplate.StageSetTemplateBuilder 
         Returns builder ( StageSetTemplateBuilder NXOpen.Stage): .
        """
        pass
    def CreateStageTemplateBuilder(part: NXOpen.Part, stageTemplate: StageTemplate) -> StageTemplateBuilder:
        """
         Creates a StageModelTemplate.TemplatePropertiesBuilder 
         Returns builder ( StageTemplateBuilder NXOpen.Stage): .
        """
        pass
    def CreateStockPartTemplateBuilder(part: NXOpen.Part, stockPartTemplate: StockPartTemplate) -> StockPartTemplateBuilder:
        """
         Creates a StageModelTemplate.StockPartTemplateBuilder 
         Returns builder ( StockPartTemplateBuilder NXOpen.Stage): .
        """
        pass
    def CreateTemplatePropertiesBuilder(part: NXOpen.Part, templateproperties: TemplateProperties) -> TemplatePropertiesBuilder:
        """
         Creates a StageModelTemplate.TemplatePropertiesBuilder 
         Returns builder ( TemplatePropertiesBuilder NXOpen.Stage): .
        """
        pass
import NXOpen
class StageSetTemplateBuilder(NXOpen.Builder): 
    """ Represents a StageModelTemplate.StageSetTemplate builder """
    @property
    def DesignModelFileSpec(self) -> str:
        """
        Getter for property: (str) DesignModelFileSpec
         Returns the design model name   
            
         
        """
        pass
    @DesignModelFileSpec.setter
    def DesignModelFileSpec(self, designModelFileSpec: str):
        """
        Setter for property: (str) DesignModelFileSpec
         Returns the design model name   
            
         
        """
        pass
    @property
    def NumStages(self) -> int:
        """
        Getter for property: (int) NumStages
         Returns the num stages   
            
         
        """
        pass
    @NumStages.setter
    def NumStages(self, numStages: int):
        """
        Setter for property: (int) NumStages
         Returns the num stages   
            
         
        """
        pass
    @property
    def StageSetName(self) -> str:
        """
        Getter for property: (str) StageSetName
         Returns the stage set name   
            
         
        """
        pass
    @StageSetName.setter
    def StageSetName(self, stageSetName: str):
        """
        Setter for property: (str) StageSetName
         Returns the stage set name   
            
         
        """
        pass
import NXOpen
class StageSetTemplate(NXOpen.NXObject): 
    """ Represents a StageModelTemplate.StageSetTemplate object."""
    def DeleteStages(self, stagesToDelete: List[StageTemplate]) -> None:
        """
         Delete the stages from this staged model set
        """
        pass
import NXOpen
class StageTemplateBuilder(NXOpen.Builder): 
    """ Represents a StageModelTemplate.StageTemplate builder """
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
         Returns the stage template name   
            
         
        """
        pass
    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
         Returns the stage template name   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         The template description 
         Returns description (List[str]): .
        """
        pass
    def GetPositionIndex(self) -> int:
        """
         Get order 
         Returns positionIndex (int): .
        """
        pass
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the template description 
        """
        pass
    def SetPositionIndex(self, positionIndex: int) -> None:
        """
         Set order 
        """
        pass
import NXOpen
class StageTemplate(NXOpen.NXObject): 
    """ Represents a StageModelTemplate.StageTemplate object."""
    pass
import NXOpen
class StockPartTemplateBuilder(NXOpen.Builder): 
    """ Represents a StageModelTemplate.StockPartTemplate builder """
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
    def SpecifyStockPart(self) -> bool:
        """
        Getter for property: (bool) SpecifyStockPart
         Returns the specify stock part   
            
         
        """
        pass
    @SpecifyStockPart.setter
    def SpecifyStockPart(self, specifyStockPart: bool):
        """
        Setter for property: (bool) SpecifyStockPart
         Returns the specify stock part   
            
         
        """
        pass
    @property
    def StockPartFileSpec(self) -> str:
        """
        Getter for property: (str) StockPartFileSpec
         Returns the design model name   
            
         
        """
        pass
    @StockPartFileSpec.setter
    def StockPartFileSpec(self, designModelFileSpec: str):
        """
        Setter for property: (str) StockPartFileSpec
         Returns the design model name   
            
         
        """
        pass
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         Returns description (List[str]): .
        """
        pass
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
import NXOpen
class StockPartTemplate(NXOpen.NXObject): 
    """ Represents a StageModelTemplate.StockPartTemplate object."""
    pass
import NXOpen
class TemplatePropertiesBuilder(NXOpen.Builder): 
    """ Represents a StageModelTemplate.TemplateProperties builder """
    class TemplatePartType(Enum):
        """
        Members Include: 
         |Set| 
         |Stage| 

        """
        Set: int
        Stage: int
        @staticmethod
        def ValueOf(value: int) -> TemplatePropertiesBuilder.TemplatePartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def IncludeGeometry(self) -> bool:
        """
        Getter for property: (bool) IncludeGeometry
         Returns the include geometry   
            
         
        """
        pass
    @IncludeGeometry.setter
    def IncludeGeometry(self, includeGeometry: bool):
        """
        Setter for property: (bool) IncludeGeometry
         Returns the include geometry   
            
         
        """
        pass
    @property
    def IncludeModelViews(self) -> bool:
        """
        Getter for property: (bool) IncludeModelViews
         Returns the include model views   
            
         
        """
        pass
    @IncludeModelViews.setter
    def IncludeModelViews(self, includeModelViews: bool):
        """
        Setter for property: (bool) IncludeModelViews
         Returns the include model views   
            
         
        """
        pass
    @property
    def IncludePMI(self) -> bool:
        """
        Getter for property: (bool) IncludePMI
         Returns the include pmi   
            
         
        """
        pass
    @IncludePMI.setter
    def IncludePMI(self, includePMI: bool):
        """
        Setter for property: (bool) IncludePMI
         Returns the include pmi   
            
         
        """
        pass
    @property
    def NumStages(self) -> int:
        """
        Getter for property: (int) NumStages
         Returns the number of stages   
            
         
        """
        pass
    @NumStages.setter
    def NumStages(self, numStages: int):
        """
        Setter for property: (int) NumStages
         Returns the number of stages   
            
         
        """
        pass
    @property
    def SelectModelView(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: ( NXOpen.SelectTaggedObject) SelectModelView
         Returns the select model view   
            
         
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
    def TemplateType(self) -> TemplatePropertiesBuilder.TemplatePartType:
        """
        Getter for property: ( TemplatePropertiesBuilder.TemplatePartType NXOpen.Stage) TemplateType
         Returns the template type   
            
         
        """
        pass
    @TemplateType.setter
    def TemplateType(self, templateType: TemplatePropertiesBuilder.TemplatePartType):
        """
        Setter for property: ( TemplatePropertiesBuilder.TemplatePartType NXOpen.Stage) TemplateType
         Returns the template type   
            
         
        """
        pass
    def GetTemplateDescription(self) -> List[str]:
        """
         Returns the template description 
         Returns templateDescription (List[str]): .
        """
        pass
    def SetTemplateDescription(self, templateDescription: List[str]) -> None:
        """
         Sets the template description 
        """
        pass
import NXOpen
class TemplateProperties(NXOpen.NXObject): 
    """ Represents a StageModelTemplate.TemplateProperties object."""
    pass
