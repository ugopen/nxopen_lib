from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents the StageModelTemplate Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Represents the StageModelTemplate Manager class."""


    ##  Creates a @link StageModelTemplate::StageSetTemplateBuilder StageModelTemplate::StageSetTemplateBuilder@endlink  
    ##  @return builder (@link StageSetTemplateBuilder NXOpen.StageModelTemplate.StageSetTemplateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stagesettemplate"> (@link StageSetTemplate NXOpen.StageModelTemplate.StageSetTemplate@endlink) </param>
    def CreateStageSetTemplateBuilder(part: NXOpen.Part, stagesettemplate: StageSetTemplate) -> StageSetTemplateBuilder:
        """
         Creates a @link StageModelTemplate::StageSetTemplateBuilder StageModelTemplate::StageSetTemplateBuilder@endlink  
         @return builder (@link StageSetTemplateBuilder NXOpen.StageModelTemplate.StageSetTemplateBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModelTemplate::TemplatePropertiesBuilder StageModelTemplate::TemplatePropertiesBuilder@endlink  
    ##  @return builder (@link StageTemplateBuilder NXOpen.StageModelTemplate.StageTemplateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stageTemplate"> (@link StageTemplate NXOpen.StageModelTemplate.StageTemplate@endlink) </param>
    def CreateStageTemplateBuilder(part: NXOpen.Part, stageTemplate: StageTemplate) -> StageTemplateBuilder:
        """
         Creates a @link StageModelTemplate::TemplatePropertiesBuilder StageModelTemplate::TemplatePropertiesBuilder@endlink  
         @return builder (@link StageTemplateBuilder NXOpen.StageModelTemplate.StageTemplateBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModelTemplate::StockPartTemplateBuilder StageModelTemplate::StockPartTemplateBuilder@endlink  
    ##  @return builder (@link StockPartTemplateBuilder NXOpen.StageModelTemplate.StockPartTemplateBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="stockPartTemplate"> (@link StockPartTemplate NXOpen.StageModelTemplate.StockPartTemplate@endlink) </param>
    def CreateStockPartTemplateBuilder(part: NXOpen.Part, stockPartTemplate: StockPartTemplate) -> StockPartTemplateBuilder:
        """
         Creates a @link StageModelTemplate::StockPartTemplateBuilder StageModelTemplate::StockPartTemplateBuilder@endlink  
         @return builder (@link StockPartTemplateBuilder NXOpen.StageModelTemplate.StockPartTemplateBuilder@endlink): .
        """
        pass
    
    ##  Creates a @link StageModelTemplate::TemplatePropertiesBuilder StageModelTemplate::TemplatePropertiesBuilder@endlink  
    ##  @return builder (@link TemplatePropertiesBuilder NXOpen.StageModelTemplate.TemplatePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="templateproperties"> (@link TemplateProperties NXOpen.StageModelTemplate.TemplateProperties@endlink) </param>
    def CreateTemplatePropertiesBuilder(part: NXOpen.Part, templateproperties: TemplateProperties) -> TemplatePropertiesBuilder:
        """
         Creates a @link StageModelTemplate::TemplatePropertiesBuilder StageModelTemplate::TemplatePropertiesBuilder@endlink  
         @return builder (@link TemplatePropertiesBuilder NXOpen.StageModelTemplate.TemplatePropertiesBuilder@endlink): .
        """
        pass
    
import NXOpen
##  Represents a @link StageModelTemplate::StageSetTemplate StageModelTemplate::StageSetTemplate@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::StageModelTemplate::Manager::CreateStageSetTemplateBuilder  NXOpen::StageModelTemplate::Manager::CreateStageSetTemplateBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## NumStages </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class StageSetTemplateBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModelTemplate.StageSetTemplate</ja_class> builder """


    ## Getter for property: (str) DesignModelFileSpec
    ##   the design model name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def DesignModelFileSpec(self) -> str:
        """
        Getter for property: (str) DesignModelFileSpec
          the design model name   
            
         
        """
        pass
    
    ## Setter for property: (str) DesignModelFileSpec

    ##   the design model name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DesignModelFileSpec.setter
    def DesignModelFileSpec(self, designModelFileSpec: str):
        """
        Setter for property: (str) DesignModelFileSpec
          the design model name   
            
         
        """
        pass
    
    ## Getter for property: (int) NumStages
    ##   the num stages   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def NumStages(self) -> int:
        """
        Getter for property: (int) NumStages
          the num stages   
            
         
        """
        pass
    
    ## Setter for property: (int) NumStages

    ##   the num stages   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @NumStages.setter
    def NumStages(self, numStages: int):
        """
        Setter for property: (int) NumStages
          the num stages   
            
         
        """
        pass
    
    ## Getter for property: (str) StageSetName
    ##   the stage set name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def StageSetName(self) -> str:
        """
        Getter for property: (str) StageSetName
          the stage set name   
            
         
        """
        pass
    
    ## Setter for property: (str) StageSetName

    ##   the stage set name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @StageSetName.setter
    def StageSetName(self, stageSetName: str):
        """
        Setter for property: (str) StageSetName
          the stage set name   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link StageModelTemplate::StageSetTemplate StageModelTemplate::StageSetTemplate@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::StageModelTemplate::StageSetTemplateBuilder  NXOpen::StageModelTemplate::StageSetTemplateBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class StageSetTemplate(NXOpen.NXObject): 
    """ Represents a <ja_class>StageModelTemplate.StageSetTemplate</ja_class> object."""


    ##  Delete the stages from this staged model set
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="stagesToDelete"> (@link StageTemplate List[NXOpen.StageModelTemplate.StageTemplate]@endlink) </param>
    def DeleteStages(stageSetTemplate: StageSetTemplate, stagesToDelete: List[StageTemplate]) -> None:
        """
         Delete the stages from this staged model set
        """
        pass
    
import NXOpen
##  Represents a @link StageModelTemplate::StageTemplate StageModelTemplate::StageTemplate@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::StageModelTemplate::Manager::CreateStageTemplateBuilder  NXOpen::StageModelTemplate::Manager::CreateStageTemplateBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class StageTemplateBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModelTemplate.StageTemplate</ja_class> builder """


    ## Getter for property: (str) Name
    ##   the stage template name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the stage template name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the stage template name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the stage template name   
            
         
        """
        pass
    
    ##  The template description 
    ##  @return description (List[str]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetDescription(self) -> List[str]:
        """
         The template description 
         @return description (List[str]): .
        """
        pass
    
    ##  Get order 
    ##  @return positionIndex (int): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    @staticmethod
    def GetPositionIndex(builder: StageTemplateBuilder) -> int:
        """
         Get order 
         @return positionIndex (int): .
        """
        pass
    
    ##  Sets the template description 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ##  
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the template description 
        """
        pass
    
    ##  Set order 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ## 
    ## <param name="positionIndex"> (int) </param>
    def SetPositionIndex(builder: StageTemplateBuilder, positionIndex: int) -> None:
        """
         Set order 
        """
        pass
    
import NXOpen
##  Represents a @link StageModelTemplate::StageTemplate StageModelTemplate::StageTemplate@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::StageModelTemplate::StageTemplateBuilder  NXOpen::StageModelTemplate::StageTemplateBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class StageTemplate(NXOpen.NXObject): 
    """ Represents a <ja_class>StageModelTemplate.StageTemplate</ja_class> object."""
    pass


import NXOpen
##  Represents a @link StageModelTemplate::StockPartTemplate StageModelTemplate::StockPartTemplate@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::StageModelTemplate::Manager::CreateStockPartTemplateBuilder  NXOpen::StageModelTemplate::Manager::CreateStockPartTemplateBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## SpecifyStockPart </term> <description> 
##  
## 1 </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class StockPartTemplateBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModelTemplate.StockPartTemplate</ja_class> builder """


    ## Getter for property: (str) Name
    ##   the name   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def Name(self) -> str:
        """
        Getter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Setter for property: (str) Name

    ##   the name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @Name.setter
    def Name(self, name: str):
        """
        Setter for property: (str) Name
          the name   
            
         
        """
        pass
    
    ## Getter for property: (bool) SpecifyStockPart
    ##   the specify stock part   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def SpecifyStockPart(self) -> bool:
        """
        Getter for property: (bool) SpecifyStockPart
          the specify stock part   
            
         
        """
        pass
    
    ## Setter for property: (bool) SpecifyStockPart

    ##   the specify stock part   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @SpecifyStockPart.setter
    def SpecifyStockPart(self, specifyStockPart: bool):
        """
        Setter for property: (bool) SpecifyStockPart
          the specify stock part   
            
         
        """
        pass
    
    ## Getter for property: (str) StockPartFileSpec
    ##   the design model name   
    ##     
    ##  
    ## Getter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def StockPartFileSpec(self) -> str:
        """
        Getter for property: (str) StockPartFileSpec
          the design model name   
            
         
        """
        pass
    
    ## Setter for property: (str) StockPartFileSpec

    ##   the design model name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @StockPartFileSpec.setter
    def StockPartFileSpec(self, designModelFileSpec: str):
        """
        Setter for property: (str) StockPartFileSpec
          the design model name   
            
         
        """
        pass
    
    ##  Returns the description 
    ##  @return description (List[str]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         @return description (List[str]): .
        """
        pass
    
    ##  Sets the description 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ##  
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    
import NXOpen
##  Represents a @link StageModelTemplate::StockPartTemplate StageModelTemplate::StockPartTemplate@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::StageModelTemplate::StockPartTemplateBuilder  NXOpen::StageModelTemplate::StockPartTemplateBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class StockPartTemplate(NXOpen.NXObject): 
    """ Represents a <ja_class>StageModelTemplate.StockPartTemplate</ja_class> object."""
    pass


import NXOpen
##  Represents a @link StageModelTemplate::TemplateProperties StageModelTemplate::TemplateProperties@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::StageModelTemplate::Manager::CreateTemplatePropertiesBuilder  NXOpen::StageModelTemplate::Manager::CreateTemplatePropertiesBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## IncludeGeometry </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IncludeModelViews </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## IncludePMI </term> <description> 
##  
## 0 </description> </item> 
## 
## <item><term> 
##  
## NumStages </term> <description> 
##  
## 1 </description> </item> 
## 
## <item><term> 
##  
## TemplateType </term> <description> 
##  
## Set </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX2212.0.0  <br> 

class TemplatePropertiesBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>StageModelTemplate.TemplateProperties</ja_class> builder """


    ##  the template part type 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Set</term><description> 
    ## </description> </item><item><term> 
    ## Stage</term><description> 
    ## </description> </item></list>
    class TemplatePartType(Enum):
        """
        Members Include: <Set> <Stage>
        """
        Set: int
        Stage: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplatePropertiesBuilder.TemplatePartType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) IncludeGeometry
    ##   the include geometry   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def IncludeGeometry(self) -> bool:
        """
        Getter for property: (bool) IncludeGeometry
          the include geometry   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeGeometry

    ##   the include geometry   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @IncludeGeometry.setter
    def IncludeGeometry(self, includeGeometry: bool):
        """
        Setter for property: (bool) IncludeGeometry
          the include geometry   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludeModelViews
    ##   the include model views   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def IncludeModelViews(self) -> bool:
        """
        Getter for property: (bool) IncludeModelViews
          the include model views   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludeModelViews

    ##   the include model views   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @IncludeModelViews.setter
    def IncludeModelViews(self, includeModelViews: bool):
        """
        Setter for property: (bool) IncludeModelViews
          the include model views   
            
         
        """
        pass
    
    ## Getter for property: (bool) IncludePMI
    ##   the include pmi   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def IncludePMI(self) -> bool:
        """
        Getter for property: (bool) IncludePMI
          the include pmi   
            
         
        """
        pass
    
    ## Setter for property: (bool) IncludePMI

    ##   the include pmi   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @IncludePMI.setter
    def IncludePMI(self, includePMI: bool):
        """
        Setter for property: (bool) IncludePMI
          the include pmi   
            
         
        """
        pass
    
    ## Getter for property: (int) NumStages
    ##   the number of stages   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def NumStages(self) -> int:
        """
        Getter for property: (int) NumStages
          the number of stages   
            
         
        """
        pass
    
    ## Setter for property: (int) NumStages

    ##   the number of stages   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @NumStages.setter
    def NumStages(self, numStages: int):
        """
        Setter for property: (int) NumStages
          the number of stages   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectModelView
    ##   the select model view   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return NXOpen.SelectTaggedObject
    @property
    def SelectModelView(self) -> NXOpen.SelectTaggedObject:
        """
        Getter for property: (@link NXOpen.SelectTaggedObject NXOpen.SelectTaggedObject@endlink) SelectModelView
          the select model view   
            
         
        """
        pass
    
    ## Getter for property: (str) TemplateName
    ##   the template name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return str
    @property
    def TemplateName(self) -> str:
        """
        Getter for property: (str) TemplateName
          the template name   
            
         
        """
        pass
    
    ## Setter for property: (str) TemplateName

    ##   the template name   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TemplateName.setter
    def TemplateName(self, templateName: str):
        """
        Setter for property: (str) TemplateName
          the template name   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplatePropertiesBuilder.TemplatePartType NXOpen.StageModelTemplate.TemplatePropertiesBuilder.TemplatePartType@endlink) TemplateType
    ##   the template type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return TemplatePropertiesBuilder.TemplatePartType
    @property
    def TemplateType(self) -> TemplatePropertiesBuilder.TemplatePartType:
        """
        Getter for property: (@link TemplatePropertiesBuilder.TemplatePartType NXOpen.StageModelTemplate.TemplatePropertiesBuilder.TemplatePartType@endlink) TemplateType
          the template type   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplatePropertiesBuilder.TemplatePartType NXOpen.StageModelTemplate.TemplatePropertiesBuilder.TemplatePartType@endlink) TemplateType

    ##   the template type   
    ##     
    ##  
    ## Setter License requirements: stage_model (" Stage Model")
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @TemplateType.setter
    def TemplateType(self, templateType: TemplatePropertiesBuilder.TemplatePartType):
        """
        Setter for property: (@link TemplatePropertiesBuilder.TemplatePartType NXOpen.StageModelTemplate.TemplatePropertiesBuilder.TemplatePartType@endlink) TemplateType
          the template type   
            
         
        """
        pass
    
    ##  Returns the template description 
    ##  @return templateDescription (List[str]): .
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: None.
    def GetTemplateDescription(self) -> List[str]:
        """
         Returns the template description 
         @return templateDescription (List[str]): .
        """
        pass
    
    ##  Sets the template description 
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## License requirements: stage_model (" Stage Model")
    ##  
    def SetTemplateDescription(self, templateDescription: List[str]) -> None:
        """
         Sets the template description 
        """
        pass
    
import NXOpen
##  Represents a @link StageModelTemplate::TemplateProperties StageModelTemplate::TemplateProperties@endlink  object. <br> To create or edit an instance of this class, use @link NXOpen::StageModelTemplate::TemplatePropertiesBuilder  NXOpen::StageModelTemplate::TemplatePropertiesBuilder @endlink  <br> 
## 
##   <br>  Created in NX2212.0.0  <br> 

class TemplateProperties(NXOpen.NXObject): 
    """ Represents a <ja_class>StageModelTemplate.TemplateProperties</ja_class> object."""
    pass


## @package NXOpen.StageModelTemplate
## Classes, Enums and Structs under NXOpen.StageModelTemplate namespace

##  @link TemplatePropertiesBuilderTemplatePartType NXOpen.StageModelTemplate.TemplatePropertiesBuilderTemplatePartType @endlink is an alias for @link TemplatePropertiesBuilder.TemplatePartType NXOpen.StageModelTemplate.TemplatePropertiesBuilder.TemplatePartType@endlink
TemplatePropertiesBuilderTemplatePartType = TemplatePropertiesBuilder.TemplatePartType


