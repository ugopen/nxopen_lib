from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
##  Represents attributes to exclude builder 
## 
##   <br>  Created in NX2007.0.0  <br> 

class AttributesToExcludeBuilder(NXOpen.TaggedObject): 
    """ Represents attributes to exclude builder """


    ##  Get the modified state of attributes 
    ##  @return attributeState (bool): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeName"> (str) </param>
    def GetAttributeState(self, attributeName: str) -> bool:
        """
         Get the modified state of attributes 
         @return attributeState (bool): .
        """
        pass
    
    ##  Set the modified state of attributes 
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="attributeName"> (str) </param>
    ## <param name="attributeState"> (bool) </param>
    def SetAttributeState(self, attributeName: str, attributeState: bool) -> None:
        """
         Set the modified state of attributes 
        """
        pass
    
import NXOpen
import NXOpen.Annotations
##  Represents the TDP Manager class. <br> To obtain an instance of this class, refer to @link NXOpen::Session  NXOpen::Session @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class Manager(NXOpen.Object): 
    """ Represents the TDP Manager class."""


    ##  This enum indicates the results of adding additional PDFs to the end of a TDP.
    ##             Success = All additional PDFs were successfully appended.
    ##             SuccessWithMalformedAttachment = Most additional PDFs were successfully attached, but there may be complications with certain inputs.
    ##             Fail = There was a critical error processing your request.
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Success</term><description> 
    ## </description> </item><item><term> 
    ## SuccessWithMalformedAttachment</term><description> 
    ## </description> </item><item><term> 
    ## Fail</term><description> 
    ## </description> </item></list>
    class AdditionalPdfResult(Enum):
        """
        Members Include: <Success> <SuccessWithMalformedAttachment> <Fail>
        """
        Success: int
        SuccessWithMalformedAttachment: int
        Fail: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> Manager.AdditionalPdfResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This method adds additional PDF files to the end of a TDP. 
    ##  @return result (@link Manager.AdditionalPdfResult NXOpen.TDP.Manager.AdditionalPdfResult@endlink):  final results of adding additional PDFs .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: nx_tdp (" NX Technical Data Package")
    ## <param name="src"> (str)  input PDF to attach to </param>
    ## <param name="additionalPdfs"> (List[str])  list of PDF's to attach </param>
    ## <param name="dest"> (str)  output PDF containing input and attached PDFs at the end </param>
    def AddAdditionalPdf(src: str, additionalPdfs: List[str], dest: str) -> Manager.AdditionalPdfResult:
        """
         This method adds additional PDF files to the end of a TDP. 
         @return result (@link Manager.AdditionalPdfResult NXOpen.TDP.Manager.AdditionalPdfResult@endlink):  final results of adding additional PDFs .
        """
        pass
    
    ##  Creates the TDP Publisher builder 
    ##  @return builder (@link PublisherBuilder NXOpen.TDP.PublisherBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateTdpPublisherBuilder(part: NXOpen.Part) -> PublisherBuilder:
        """
         Creates the TDP Publisher builder 
         @return builder (@link PublisherBuilder NXOpen.TDP.PublisherBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Automatic Table builder 
    ##  @return builder (@link TemplateAutomaticTableBuilder NXOpen.TDP.TemplateAutomaticTableBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="automaticTable"> (@link TemplateAutomaticTable NXOpen.TDP.TemplateAutomaticTable@endlink) </param>
    def CreateTemplateAutomaticTableBuilder(part: NXOpen.Part, automaticTable: TemplateAutomaticTable) -> TemplateAutomaticTableBuilder:
        """
         Creates the Template Automatic Table builder 
         @return builder (@link TemplateAutomaticTableBuilder NXOpen.TDP.TemplateAutomaticTableBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Diagram Area builder 
    ##  @return builder (@link TemplateDiagramAreaBuilder NXOpen.TDP.TemplateDiagramAreaBuilder@endlink): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="printview"> (@link TemplateDiagramArea NXOpen.TDP.TemplateDiagramArea@endlink) </param>
    def CreateTemplateDiagramareaBuilder(part: NXOpen.Part, printview: TemplateDiagramArea) -> TemplateDiagramAreaBuilder:
        """
         Creates the Template Diagram Area builder 
         @return builder (@link TemplateDiagramAreaBuilder NXOpen.TDP.TemplateDiagramAreaBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Edit cell builder 
    ##  @return builder (@link TemplateEditCellBuilder NXOpen.TDP.TemplateEditCellBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="tableCell"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    def CreateTemplateEditcellBuilder(part: NXOpen.Part, tableCell: NXOpen.DisplayableObject) -> TemplateEditCellBuilder:
        """
         Creates the Template Edit cell builder 
         @return builder (@link TemplateEditCellBuilder NXOpen.TDP.TemplateEditCellBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Form Field builder 
    ##  @return builder (@link TemplateFormFieldBuilder NXOpen.TDP.TemplateFormFieldBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="formFieldTag"> (@link TemplateFormField NXOpen.TDP.TemplateFormField@endlink) </param>
    def CreateTemplateFormFieldBuilder(part: NXOpen.Part, formFieldTag: TemplateFormField) -> TemplateFormFieldBuilder:
        """
         Creates the Template Form Field builder 
         @return builder (@link TemplateFormFieldBuilder NXOpen.TDP.TemplateFormFieldBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Image builder 
    ##  @return builder (@link TemplateImageBuilder NXOpen.TDP.TemplateImageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="imageToEdit"> (@link TemplateImage NXOpen.TDP.TemplateImage@endlink) </param>
    def CreateTemplateImageBuilder(part: NXOpen.Part, imageToEdit: TemplateImage) -> TemplateImageBuilder:
        """
         Creates the Template Image builder 
         @return builder (@link TemplateImageBuilder NXOpen.TDP.TemplateImageBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Note builder 
    ##  @return builder (@link TemplateNoteBuilder NXOpen.TDP.TemplateNoteBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="annotation"> (@link NXOpen.Annotations.SimpleDraftingAid NXOpen.Annotations.SimpleDraftingAid@endlink)  @link NXOpen::Annotations::SimpleDraftingAid NXOpen::Annotations::SimpleDraftingAid@endlink  to be edited </param>
    def CreateTemplateNoteBuilder(part: NXOpen.Part, annotation: NXOpen.Annotations.SimpleDraftingAid) -> TemplateNoteBuilder:
        """
         Creates the Template Note builder 
         @return builder (@link TemplateNoteBuilder NXOpen.TDP.TemplateNoteBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Page builder 
    ##  @return builder (@link TemplatePageBuilder NXOpen.TDP.TemplatePageBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="pageToEdit"> (@link TemplatePage NXOpen.TDP.TemplatePage@endlink) </param>
    def CreateTemplatePageBuilder(part: NXOpen.Part, pageToEdit: TemplatePage) -> TemplatePageBuilder:
        """
         Creates the Template Page builder 
         @return builder (@link TemplatePageBuilder NXOpen.TDP.TemplatePageBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Print View builder 
    ##  @return builder (@link TemplatePrintViewBuilder NXOpen.TDP.TemplatePrintViewBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="printview"> (@link TemplatePrintView NXOpen.TDP.TemplatePrintView@endlink) </param>
    def CreateTemplatePrintViewBuilder(part: NXOpen.Part, printview: TemplatePrintView) -> TemplatePrintViewBuilder:
        """
         Creates the Template Print View builder 
         @return builder (@link TemplatePrintViewBuilder NXOpen.TDP.TemplatePrintViewBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Properties builder 
    ##  @return builder (@link TemplatePropertiesBuilder NXOpen.TDP.TemplatePropertiesBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    def CreateTemplatePropertiesBuilder(part: NXOpen.Part) -> TemplatePropertiesBuilder:
        """
         Creates the Template Properties builder 
         @return builder (@link TemplatePropertiesBuilder NXOpen.TDP.TemplatePropertiesBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Rectangle builder 
    ##  @return builder (@link TemplateRectangleBuilder NXOpen.TDP.TemplateRectangleBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="rectangle"> (@link TemplateRectangle NXOpen.TDP.TemplateRectangle@endlink) </param>
    def CreateTemplateRectangleBuilder(part: NXOpen.Part, rectangle: TemplateRectangle) -> TemplateRectangleBuilder:
        """
         Creates the Template Rectangle builder 
         @return builder (@link TemplateRectangleBuilder NXOpen.TDP.TemplateRectangleBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Table builder 
    ##  @return builder (@link TemplateTableSectionBuilder NXOpen.TDP.TemplateTableSectionBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="tableSectionToEdit"> (@link NXOpen.Annotations.TableSection NXOpen.Annotations.TableSection@endlink) </param>
    def CreateTemplateTableSectionBuilder(part: NXOpen.Part, tableSectionToEdit: NXOpen.Annotations.TableSection) -> TemplateTableSectionBuilder:
        """
         Creates the Template Table builder 
         @return builder (@link TemplateTableSectionBuilder NXOpen.TDP.TemplateTableSectionBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template View Carousel builder 
    ##  @return builder (@link TemplateViewCarouselBuilder NXOpen.TDP.TemplateViewCarouselBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="viewCarousel"> (@link TemplateViewCarousel NXOpen.TDP.TemplateViewCarousel@endlink) </param>
    def CreateTemplateViewCarouselBuilder(part: NXOpen.Part, viewCarousel: TemplateViewCarousel) -> TemplateViewCarouselBuilder:
        """
         Creates the Template View Carousel builder 
         @return builder (@link TemplateViewCarouselBuilder NXOpen.TDP.TemplateViewCarouselBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template View List builder 
    ##  @return builder (@link TemplateViewListBuilder NXOpen.TDP.TemplateViewListBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="viewlist"> (@link TemplateViewList NXOpen.TDP.TemplateViewList@endlink) </param>
    def CreateTemplateViewListBuilder(part: NXOpen.Part, viewlist: TemplateViewList) -> TemplateViewListBuilder:
        """
         Creates the Template View List builder 
         @return builder (@link TemplateViewListBuilder NXOpen.TDP.TemplateViewListBuilder@endlink): .
        """
        pass
    
    ##  Creates the Template Viewport builder 
    ##  @return builder (@link TemplateViewportBuilder NXOpen.TDP.TemplateViewportBuilder@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="viewport"> (@link TemplateViewport NXOpen.TDP.TemplateViewport@endlink) </param>
    def CreateTemplateViewportBuilder(part: NXOpen.Part, viewport: TemplateViewport) -> TemplateViewportBuilder:
        """
         Creates the Template Viewport builder 
         @return builder (@link TemplateViewportBuilder NXOpen.TDP.TemplateViewportBuilder@endlink): .
        """
        pass
    
    ##  Locks the specified template objects. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_tdp (" NX Technical Data Package")
    ## <param name="templateObjects"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  List of template objects </param>
    def Lock(templateObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Locks the specified template objects. 
        """
        pass
    
    ##  Set origin to the given template displayable object 
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: nx_tdp (" NX Technical Data Package")
    ## <param name="objectTag"> (@link NXOpen.DisplayableObject NXOpen.DisplayableObject@endlink) </param>
    ## <param name="objOrigin"> (@link NXOpen.Point3d NXOpen.Point3d@endlink)  Origin for the template displayable object </param>
    def SetObjectOrigin(objectTag: NXOpen.DisplayableObject, objOrigin: NXOpen.Point3d) -> None:
        """
         Set origin to the given template displayable object 
        """
        pass
    
    ##  Set page order and updates page numbers. 
    ## 
    ##   <br>  Created in NX1872.0.0  <br> 

    ## License requirements: nx_tdp (" NX Technical Data Package")
    ## <param name="part"> (@link NXOpen.Part NXOpen.Part@endlink) </param>
    ## <param name="pageObjects"> (@link TemplatePage List[NXOpen.TDP.TemplatePage]@endlink)  List of page objects </param>
    def SetPageOrder(part: NXOpen.Part, pageObjects: List[TemplatePage]) -> None:
        """
         Set page order and updates page numbers. 
        """
        pass
    
    ##  Unlocks the specified template objects. 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_tdp (" NX Technical Data Package")
    ## <param name="templateObjects"> (@link NXOpen.DisplayableObject List[NXOpen.DisplayableObject]@endlink)  List of template objects </param>
    def Unlock(templateObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Unlocks the specified template objects. 
        """
        pass
    
import NXOpen
##  
##         This builder is used to publish Technical Data Package, or TDP for short.
##         It collects all the necessary inputs from a TDP template and other user options
##         before publishing TDP.
##      <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTdpPublisherBuilder  NXOpen::TDP::Manager::CreateTdpPublisherBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class PublisherBuilder(NXOpen.Builder): 
    """ 
        This builder is used to publish Technical Data Package, or TDP for short.
        It collects all the necessary inputs from a TDP template and other user options
        before publishing TDP.
    """


    ##  This enum indicates the level of accuracy for publishing a 3D PDF TDP.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Maximum</term><description> 
    ## </description> </item><item><term> 
    ## High</term><description> 
    ## </description> </item><item><term> 
    ## Medium</term><description> 
    ## </description> </item><item><term> 
    ## Low</term><description> 
    ## </description> </item></list>
    class ModelAccuracyType(Enum):
        """
        Members Include: <Maximum> <High> <Medium> <Low>
        """
        Maximum: int
        High: int
        Medium: int
        Low: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.ModelAccuracyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum indicates the results of publishing the TDP.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Success</term><description> 
    ## </description> </item><item><term> 
    ## SuccessWithInconsistency</term><description> 
    ## </description> </item><item><term> 
    ## SuccessWithError</term><description> 
    ## </description> </item><item><term> 
    ## Fail</term><description> 
    ## </description> </item></list>
    class PublishResult(Enum):
        """
        Members Include: <Success> <SuccessWithInconsistency> <SuccessWithError> <Fail>
        """
        Success: int
        SuccessWithInconsistency: int
        SuccessWithError: int
        Fail: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.PublishResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum indicates save-to option for publishing the TDP in managed mode.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Teamcenter</term><description> 
    ## </description> </item><item><term> 
    ## OperatingSystem</term><description> 
    ## </description> </item></list>
    class SaveToOptionType(Enum):
        """
        Members Include: <Teamcenter> <OperatingSystem>
        """
        Teamcenter: int
        OperatingSystem: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.SaveToOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  This enum indicates how the views are selected for publishing TDP.
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## SelectedViews</term><description> 
    ## </description> </item><item><term> 
    ## AllDisclosedViews</term><description> 
    ## </description> </item><item><term> 
    ## AllUserDefinedViews</term><description> 
    ## </description> </item><item><term> 
    ## AllViews</term><description> 
    ## </description> </item><item><term> 
    ## AllSectionViews</term><description> 
    ## </description> </item></list>
    class ViewSelectionType(Enum):
        """
        Members Include: <SelectedViews> <AllDisclosedViews> <AllUserDefinedViews> <AllViews> <AllSectionViews>
        """
        SelectedViews: int
        AllDisclosedViews: int
        AllUserDefinedViews: int
        AllViews: int
        AllSectionViews: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.ViewSelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (bool) AttachSVG
    ##  Returns 
    ##             the flag whether to attach SVG to the PDF or not.  
    ##   
    ##           
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return bool
    @property
    def AttachSVG(self) -> bool:
        """
        Getter for property: (bool) AttachSVG
         Returns 
                    the flag whether to attach SVG to the PDF or not.  
          
                  
         
        """
        pass
    
    ## Setter for property: (bool) AttachSVG

    ##  Returns 
    ##             the flag whether to attach SVG to the PDF or not.  
    ##   
    ##           
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @AttachSVG.setter
    def AttachSVG(self, attachSVG: bool):
        """
        Setter for property: (bool) AttachSVG
         Returns 
                    the flag whether to attach SVG to the PDF or not.  
          
                  
         
        """
        pass
    
    ## Getter for property: (@link AttributesToExcludeBuilder NXOpen.TDP.AttributesToExcludeBuilder@endlink) AttributesToExclude
    ##  Returns
    ##         the attributes to exclude builder, if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.3000.0  <br> 

    ## @return AttributesToExcludeBuilder
    @property
    def AttributesToExclude(self) -> AttributesToExcludeBuilder:
        """
        Getter for property: (@link AttributesToExcludeBuilder NXOpen.TDP.AttributesToExcludeBuilder@endlink) AttributesToExclude
         Returns
                the attributes to exclude builder, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
    ##  Returns
    ##         the Background color, if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def BackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
         Returns
                the Background color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor

    ##  Returns
    ##         the Background color, if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @BackgroundColor.setter
    def BackgroundColor(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) BackgroundColor
         Returns
                the Background color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Getter for property: (bool) Compression
    ##  Returns 
    ##             the flag whether to use lossy compression for 3D PDF model, 
    ##             if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def Compression(self) -> bool:
        """
        Getter for property: (bool) Compression
         Returns 
                    the flag whether to use lossy compression for 3D PDF model, 
                    if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Setter for property: (bool) Compression

    ##  Returns 
    ##             the flag whether to use lossy compression for 3D PDF model, 
    ##             if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Compression.setter
    def Compression(self, compression: bool):
        """
        Setter for property: (bool) Compression
         Returns 
                    the flag whether to use lossy compression for 3D PDF model, 
                    if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Getter for property: (@link PublisherBuilder.ModelAccuracyType NXOpen.TDP.PublisherBuilder.ModelAccuracyType@endlink) ModelAccuracy
    ##  Returns 
    ##             the 3D PDF model accuracy, if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PublisherBuilder.ModelAccuracyType
    @property
    def ModelAccuracy(self) -> PublisherBuilder.ModelAccuracyType:
        """
        Getter for property: (@link PublisherBuilder.ModelAccuracyType NXOpen.TDP.PublisherBuilder.ModelAccuracyType@endlink) ModelAccuracy
         Returns 
                    the 3D PDF model accuracy, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Setter for property: (@link PublisherBuilder.ModelAccuracyType NXOpen.TDP.PublisherBuilder.ModelAccuracyType@endlink) ModelAccuracy

    ##  Returns 
    ##             the 3D PDF model accuracy, if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ModelAccuracy.setter
    def ModelAccuracy(self, modelAccuracy: PublisherBuilder.ModelAccuracyType):
        """
        Setter for property: (@link PublisherBuilder.ModelAccuracyType NXOpen.TDP.PublisherBuilder.ModelAccuracyType@endlink) ModelAccuracy
         Returns 
                    the 3D PDF model accuracy, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Getter for property: (str) OutputFilename
    ##  Returns the output filename for the TDP   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def OutputFilename(self) -> str:
        """
        Getter for property: (str) OutputFilename
         Returns the output filename for the TDP   
            
         
        """
        pass
    
    ## Setter for property: (str) OutputFilename

    ##  Returns the output filename for the TDP   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @OutputFilename.setter
    def OutputFilename(self, filename: str):
        """
        Setter for property: (str) OutputFilename
         Returns the output filename for the TDP   
            
         
        """
        pass
    
    ## Getter for property: (bool) OverrideColors
    ##  Returns
    ##         the flag whether to override ViewPort Background and PMI color,
    ##         in case of publishing to 3D PDF
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return bool
    @property
    def OverrideColors(self) -> bool:
        """
        Getter for property: (bool) OverrideColors
         Returns
                the flag whether to override ViewPort Background and PMI color,
                in case of publishing to 3D PDF
                  
            
         
        """
        pass
    
    ## Setter for property: (bool) OverrideColors

    ##  Returns
    ##         the flag whether to override ViewPort Background and PMI color,
    ##         in case of publishing to 3D PDF
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @OverrideColors.setter
    def OverrideColors(self, overrideColors: bool):
        """
        Setter for property: (bool) OverrideColors
         Returns
                the flag whether to override ViewPort Background and PMI color,
                in case of publishing to 3D PDF
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PmiColor
    ##  Returns
    ##         the PMI color, if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## @return NXOpen.NXColor
    @property
    def PmiColor(self) -> NXOpen.NXColor:
        """
        Getter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PmiColor
         Returns
                the PMI color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PmiColor

    ##  Returns
    ##         the PMI color, if the template to be published is a 3D PDF template
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    @PmiColor.setter
    def PmiColor(self, color: NXOpen.NXColor):
        """
        Setter for property: (@link NXOpen.NXColor NXOpen.NXColor@endlink) PmiColor
         Returns
                the PMI color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    
    ## Getter for property: (@link PublisherBuilder.SaveToOptionType NXOpen.TDP.PublisherBuilder.SaveToOptionType@endlink) SaveToOption
    ##  Returns 
    ##             the save-to option, if the part to be published is in managed mode
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return PublisherBuilder.SaveToOptionType
    @property
    def SaveToOption(self) -> PublisherBuilder.SaveToOptionType:
        """
        Getter for property: (@link PublisherBuilder.SaveToOptionType NXOpen.TDP.PublisherBuilder.SaveToOptionType@endlink) SaveToOption
         Returns 
                    the save-to option, if the part to be published is in managed mode
                  
            
         
        """
        pass
    
    ## Setter for property: (@link PublisherBuilder.SaveToOptionType NXOpen.TDP.PublisherBuilder.SaveToOptionType@endlink) SaveToOption

    ##  Returns 
    ##             the save-to option, if the part to be published is in managed mode
    ##           
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @SaveToOption.setter
    def SaveToOption(self, saveToOption: PublisherBuilder.SaveToOptionType):
        """
        Setter for property: (@link PublisherBuilder.SaveToOptionType NXOpen.TDP.PublisherBuilder.SaveToOptionType@endlink) SaveToOption
         Returns 
                    the save-to option, if the part to be published is in managed mode
                  
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectViewList NXOpen.SelectViewList@endlink) SelectedViews
    ##  Returns 
    ##             the selected views to publish TDP for, if the view selection method is set to 
    ##             @link NXOpen::TDP::PublisherBuilder::ViewSelectionTypeSelectedViews NXOpen::TDP::PublisherBuilder::ViewSelectionTypeSelectedViews@endlink 
    ##           
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectViewList
    @property
    def SelectedViews(self) -> NXOpen.SelectViewList:
        """
        Getter for property: (@link NXOpen.SelectViewList NXOpen.SelectViewList@endlink) SelectedViews
         Returns 
                    the selected views to publish TDP for, if the view selection method is set to 
                    @link NXOpen::TDP::PublisherBuilder::ViewSelectionTypeSelectedViews NXOpen::TDP::PublisherBuilder::ViewSelectionTypeSelectedViews@endlink 
                  
            
         
        """
        pass
    
    ## Getter for property: (bool) UsePassword
    ##  Returns the flag whether to use password or not   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def UsePassword(self) -> bool:
        """
        Getter for property: (bool) UsePassword
         Returns the flag whether to use password or not   
            
         
        """
        pass
    
    ## Setter for property: (bool) UsePassword

    ##  Returns the flag whether to use password or not   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @UsePassword.setter
    def UsePassword(self, usePassword: bool):
        """
        Setter for property: (bool) UsePassword
         Returns the flag whether to use password or not   
            
         
        """
        pass
    
    ## Getter for property: (@link PublisherBuilder.ViewSelectionType NXOpen.TDP.PublisherBuilder.ViewSelectionType@endlink) ViewSelection
    ##  Returns the view selection method   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return PublisherBuilder.ViewSelectionType
    @property
    def ViewSelection(self) -> PublisherBuilder.ViewSelectionType:
        """
        Getter for property: (@link PublisherBuilder.ViewSelectionType NXOpen.TDP.PublisherBuilder.ViewSelectionType@endlink) ViewSelection
         Returns the view selection method   
            
         
        """
        pass
    
    ## Setter for property: (@link PublisherBuilder.ViewSelectionType NXOpen.TDP.PublisherBuilder.ViewSelectionType@endlink) ViewSelection

    ##  Returns the view selection method   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ViewSelection.setter
    def ViewSelection(self, viewSelection: PublisherBuilder.ViewSelectionType):
        """
        Setter for property: (@link PublisherBuilder.ViewSelectionType NXOpen.TDP.PublisherBuilder.ViewSelectionType@endlink) ViewSelection
         Returns the view selection method   
            
         
        """
        pass
    
    ##  This method adds the new attachment filename to the end of the attachment list.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="filename"> (str) </param>
    def AddAttachment(self, filename: str) -> None:
        """
         This method adds the new attachment filename to the end of the attachment list.
        """
        pass
    
    ##  
    ##             This method deletes the attachment filenames at the indicated indices 
    ##             and re-populate the attachment filename list with new continuous indices. 
    ##         
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="indices"> (List[int]) </param>
    def DeleteAttachmentAtIndices(self, indices: List[int]) -> None:
        """
         
                    This method deletes the attachment filenames at the indicated indices 
                    and re-populate the attachment filename list with new continuous indices. 
                
        """
        pass
    
    ##  This method returns the list of attachment filenames 
    ##  @return attachments (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetAttachments(self) -> List[str]:
        """
         This method returns the list of attachment filenames 
         @return attachments (List[str]): .
        """
        pass
    
    ##  This method returns the list of text labels.
    ##  @return labels (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetTextLabels(self) -> List[str]:
        """
         This method returns the list of text labels.
         @return labels (List[str]): .
        """
        pass
    
    ##  This method returns the value of the text with the given label, if the text exists.
    ##  @return A tuple consisting of (exists, value). 
    ##  - exists is: bool.
    ##  - value is: str.

    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    def GetTextValueOfLabel(self, label: str) -> Tuple[bool, str]:
        """
         This method returns the value of the text with the given label, if the text exists.
         @return A tuple consisting of (exists, value). 
         - exists is: bool.
         - value is: str.

        """
        pass
    
    ##  This method returns the list of viewport labels.
    ##  @return labels (List[str]): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    def GetViewportLabels(self) -> List[str]:
        """
         This method returns the list of viewport labels.
         @return labels (List[str]): .
        """
        pass
    
    ##  This method returns the name of the template file that is being worked on.
    ##  @return templateFilename (str): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetWorkTemplateFilename(self) -> str:
        """
         This method returns the name of the template file that is being worked on.
         @return templateFilename (str): .
        """
        pass
    
    ##  This method checks to see if a text with the given label exists for the selected template.
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    def HasTextOfLabel(self, label: str) -> bool:
        """
         This method checks to see if a text with the given label exists for the selected template.
         @return exists (bool): .
        """
        pass
    
    ##  This method checks to see if a viewport with the given label exists for the selected template.
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    def HasViewportOfLabel(self, label: str) -> bool:
        """
         This method checks to see if a viewport with the given label exists for the selected template.
         @return exists (bool): .
        """
        pass
    
    ##  This method publishes the TDP with builder's data.
    ##  @return result (@link PublisherBuilder.PublishResult NXOpen.TDP.PublisherBuilder.PublishResult@endlink): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: nx_tdp (" NX Technical Data Package")
    def Publish(self) -> PublisherBuilder.PublishResult:
        """
         This method publishes the TDP with builder's data.
         @return result (@link PublisherBuilder.PublishResult NXOpen.TDP.PublisherBuilder.PublishResult@endlink): .
        """
        pass
    
    ##  This method sets the password.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="password"> (str) </param>
    def SetPassword(self, password: str) -> None:
        """
         This method sets the password.
        """
        pass
    
    ##  This method sets the value of the text with the given label, if the text exists.
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    ## <param name="value"> (str) </param>
    def SetTextValueOfLabel(self, label: str, value: str) -> bool:
        """
         This method sets the value of the text with the given label, if the text exists.
         @return exists (bool): .
        """
        pass
    
    ##  This method sets the value of the viewport view with the given label, if the viewport exists.
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="label"> (str) </param>
    ## <param name="value"> (str) </param>
    def SetViewPortViewValueOfViewPortLabel(self, label: str, value: str) -> bool:
        """
         This method sets the value of the viewport view with the given label, if the viewport exists.
         @return exists (bool): .
        """
        pass
    
    ##  This method sets the template to publish TDP and repopulates the text table.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="templateFilename"> (str) </param>
    def SetWorkTemplateFile(self, templateFilename: str) -> None:
        """
         This method sets the template to publish TDP and repopulates the text table.
        """
        pass
    
import NXOpen
##  Represents a Template Automatic Table Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateAutomaticTableBuilder  NXOpen::TDP::Manager::CreateTemplateAutomaticTableBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateAutomaticTableBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Automatic Table Builder """


    ##  represents the automatic table contents 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Bom</term><description> 
    ##  Bill Of Materials Table </description> </item><item><term> 
    ## Pmi</term><description> 
    ##  PMI Table </description> </item><item><term> 
    ## View</term><description> 
    ## </description> </item><item><term> 
    ## Icd</term><description> 
    ##  ICD Table </description> </item><item><term> 
    ## Pad</term><description> 
    ##  PAD Table </description> </item><item><term> 
    ## Kpi</term><description> 
    ##  KPI Table </description> </item></list>
    class ContentType(Enum):
        """
        Members Include: <Bom> <Pmi> <View> <Icd> <Pad> <Kpi>
        """
        Bom: int
        Pmi: int
        View: int
        Icd: int
        Pad: int
        Kpi: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.ContentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents BOM column types for automatic table editor 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Index</term><description> 
    ## </description> </item><item><term> 
    ## PartName</term><description> 
    ## </description> </item><item><term> 
    ## Quantity</term><description> 
    ## </description> </item><item><term> 
    ## Attribute</term><description> 
    ## </description> </item></list>
    class JaTdpTemplateAutomaticTableBomColumnType(Enum):
        """
        Members Include: <Index> <PartName> <Quantity> <Attribute>
        """
        Index: int
        PartName: int
        Quantity: int
        Attribute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents ICD column types for automatic table editor 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Index</term><description> 
    ## </description> </item><item><term> 
    ## Components</term><description> 
    ## </description> </item><item><term> 
    ## AssemblyConstraints</term><description> 
    ## </description> </item><item><term> 
    ## ElectricalRouting</term><description> 
    ## </description> </item><item><term> 
    ## InterPartExpressions</term><description> 
    ## </description> </item><item><term> 
    ## InterPartMeasurements</term><description> 
    ## </description> </item><item><term> 
    ## Join</term><description> 
    ## </description> </item><item><term> 
    ## MechanicalRouting</term><description> 
    ## </description> </item><item><term> 
    ## WaveLinks</term><description> 
    ## </description> </item><item><term> 
    ## Welds</term><description> 
    ## </description> </item><item><term> 
    ## Attribute</term><description> 
    ## </description> </item></list>
    class JaTdpTemplateAutomaticTableIcdColumnType(Enum):
        """
        Members Include: <Index> <Components> <AssemblyConstraints> <ElectricalRouting> <InterPartExpressions> <InterPartMeasurements> <Join> <MechanicalRouting> <WaveLinks> <Welds> <Attribute>
        """
        Index: int
        Components: int
        AssemblyConstraints: int
        ElectricalRouting: int
        InterPartExpressions: int
        InterPartMeasurements: int
        Join: int
        MechanicalRouting: int
        WaveLinks: int
        Welds: int
        Attribute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents KPI column types for automatic table editor 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Name</term><description> 
    ## </description> </item><item><term> 
    ## Value</term><description> 
    ## </description> </item><item><term> 
    ## Formula</term><description> 
    ## </description> </item><item><term> 
    ## Type</term><description> 
    ## </description> </item><item><term> 
    ## Description</term><description> 
    ## </description> </item><item><term> 
    ## Source</term><description> 
    ## </description> </item><item><term> 
    ## SourceDetails</term><description> 
    ## </description> </item><item><term> 
    ## Result</term><description> 
    ## </description> </item><item><term> 
    ## ValueType</term><description> 
    ## </description> </item><item><term> 
    ## PartName</term><description> 
    ## </description> </item><item><term> 
    ## Attribute</term><description> 
    ## </description> </item></list>
    class JaTdpTemplateAutomaticTableKpiColumnType(Enum):
        """
        Members Include: <Name> <Value> <Formula> <Type> <Description> <Source> <SourceDetails> <Result> <ValueType> <PartName> <Attribute>
        """
        Name: int
        Value: int
        Formula: int
        Type: int
        Description: int
        Source: int
        SourceDetails: int
        Result: int
        ValueType: int
        PartName: int
        Attribute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents PAD column types for automatic table editor 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Index</term><description> 
    ## </description> </item><item><term> 
    ## Components</term><description> 
    ## </description> </item><item><term> 
    ## AssemblyConstraints</term><description> 
    ## </description> </item><item><term> 
    ## ElectricalRouting</term><description> 
    ## </description> </item><item><term> 
    ## InterPartExpressions</term><description> 
    ## </description> </item><item><term> 
    ## InterPartMeasurements</term><description> 
    ## </description> </item><item><term> 
    ## Join</term><description> 
    ## </description> </item><item><term> 
    ## MechanicalRouting</term><description> 
    ## </description> </item><item><term> 
    ## WaveLinks</term><description> 
    ## </description> </item><item><term> 
    ## Welds</term><description> 
    ## </description> </item><item><term> 
    ## Attribute</term><description> 
    ## </description> </item></list>
    class JaTdpTemplateAutomaticTablePadColumnType(Enum):
        """
        Members Include: <Index> <Components> <AssemblyConstraints> <ElectricalRouting> <InterPartExpressions> <InterPartMeasurements> <Join> <MechanicalRouting> <WaveLinks> <Welds> <Attribute>
        """
        Index: int
        Components: int
        AssemblyConstraints: int
        ElectricalRouting: int
        InterPartExpressions: int
        InterPartMeasurements: int
        Join: int
        MechanicalRouting: int
        WaveLinks: int
        Welds: int
        Attribute: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents PMI column types for automatic table editor 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Index</term><description> 
    ## </description> </item><item><term> 
    ## PmiName</term><description> 
    ## </description> </item><item><term> 
    ## Value</term><description> 
    ## </description> </item><item><term> 
    ## Attribute</term><description> 
    ## </description> </item><item><term> 
    ## PmiType</term><description> 
    ## </description> </item><item><term> 
    ## PmiId</term><description> 
    ## </description> </item></list>
    class JaTdpTemplateAutomaticTablePmiColumnType(Enum):
        """
        Members Include: <Index> <PmiName> <Value> <Attribute> <PmiType> <PmiId>
        """
        Index: int
        PmiName: int
        Value: int
        Attribute: int
        PmiType: int
        PmiId: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents the Kpi Filter level in 3D PDF 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Part</term><description> 
    ## </description> </item><item><term> 
    ## ProductInterface</term><description> 
    ## </description> </item><item><term> 
    ## Expression</term><description> 
    ## </description> </item><item><term> 
    ## Check</term><description> 
    ## </description> </item><item><term> 
    ## PartOccurence</term><description> 
    ## </description> </item><item><term> 
    ## CombinedView</term><description> 
    ## </description> </item></list>
    class KpiFilterLevel(Enum):
        """
        Members Include: <Part> <ProductInterface> <Expression> <Check> <PartOccurence> <CombinedView>
        """
        Part: int
        ProductInterface: int
        Expression: int
        Check: int
        PartOccurence: int
        CombinedView: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.KpiFilterLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents the position in 3D PDF 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotSet</term><description> 
    ##  Not placed in 3D PDF </description> </item><item><term> 
    ## Above</term><description> 
    ##  Placed above the PMI table in 3D PDF </description> </item><item><term> 
    ## Below</term><description> 
    ##  Placed below the PMI table in 3D PDF </description> </item></list>
    class PositionType(Enum):
        """
        Members Include: <NotSet> <Above> <Below>
        """
        NotSet: int
        Above: int
        Below: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.PositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  represents the BOM Scope level in 3D PDF 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## AllLevels</term><description> 
    ##  Assemblies and Sub Assemblies placed in 3D PDF </description> </item><item><term> 
    ## TopLevelOnly</term><description> 
    ##  Placed Top Level Assembly in 3D PDF </description> </item><item><term> 
    ## ComponentsOnly</term><description> 
    ##  Placed Leaf level component in 3D PDF </description> </item></list>
    class ScopeType(Enum):
        """
        Members Include: <AllLevels> <TopLevelOnly> <ComponentsOnly>
        """
        AllLevels: int
        TopLevelOnly: int
        ComponentsOnly: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.ScopeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link TemplateAutomaticTableBuilder.ScopeType NXOpen.TDP.TemplateAutomaticTableBuilder.ScopeType@endlink) BomScope
    ##  Returns the bom scope type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return TemplateAutomaticTableBuilder.ScopeType
    @property
    def BomScope(self) -> TemplateAutomaticTableBuilder.ScopeType:
        """
        Getter for property: (@link TemplateAutomaticTableBuilder.ScopeType NXOpen.TDP.TemplateAutomaticTableBuilder.ScopeType@endlink) BomScope
         Returns the bom scope type   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateAutomaticTableBuilder.ScopeType NXOpen.TDP.TemplateAutomaticTableBuilder.ScopeType@endlink) BomScope

    ##  Returns the bom scope type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @BomScope.setter
    def BomScope(self, scope: TemplateAutomaticTableBuilder.ScopeType):
        """
        Setter for property: (@link TemplateAutomaticTableBuilder.ScopeType NXOpen.TDP.TemplateAutomaticTableBuilder.ScopeType@endlink) BomScope
         Returns the bom scope type   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
    ##  Returns the color and width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateAutomaticTableBuilder.ContentType NXOpen.TDP.TemplateAutomaticTableBuilder.ContentType@endlink) Contents
    ##  Returns the content   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TemplateAutomaticTableBuilder.ContentType
    @property
    def Contents(self) -> TemplateAutomaticTableBuilder.ContentType:
        """
        Getter for property: (@link TemplateAutomaticTableBuilder.ContentType NXOpen.TDP.TemplateAutomaticTableBuilder.ContentType@endlink) Contents
         Returns the content   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateAutomaticTableBuilder.ContentType NXOpen.TDP.TemplateAutomaticTableBuilder.ContentType@endlink) Contents

    ##  Returns the content   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Contents.setter
    def Contents(self, content: TemplateAutomaticTableBuilder.ContentType):
        """
        Setter for property: (@link TemplateAutomaticTableBuilder.ContentType NXOpen.TDP.TemplateAutomaticTableBuilder.ContentType@endlink) Contents
         Returns the content   
            
         
        """
        pass
    
    ## Getter for property: (int) DecimalPlaces
    ##  Returns the decimal place value   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return int
    @property
    def DecimalPlaces(self) -> int:
        """
        Getter for property: (int) DecimalPlaces
         Returns the decimal place value   
            
         
        """
        pass
    
    ## Setter for property: (int) DecimalPlaces

    ##  Returns the decimal place value   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @DecimalPlaces.setter
    def DecimalPlaces(self, decimalPlaces: int):
        """
        Setter for property: (int) DecimalPlaces
         Returns the decimal place value   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateAutomaticTableBuilder.KpiFilterLevel NXOpen.TDP.TemplateAutomaticTableBuilder.KpiFilterLevel@endlink) FilterLevel
    ##  Returns the filter level type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return TemplateAutomaticTableBuilder.KpiFilterLevel
    @property
    def FilterLevel(self) -> TemplateAutomaticTableBuilder.KpiFilterLevel:
        """
        Getter for property: (@link TemplateAutomaticTableBuilder.KpiFilterLevel NXOpen.TDP.TemplateAutomaticTableBuilder.KpiFilterLevel@endlink) FilterLevel
         Returns the filter level type   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateAutomaticTableBuilder.KpiFilterLevel NXOpen.TDP.TemplateAutomaticTableBuilder.KpiFilterLevel@endlink) FilterLevel

    ##  Returns the filter level type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @FilterLevel.setter
    def FilterLevel(self, filterLevel: TemplateAutomaticTableBuilder.KpiFilterLevel):
        """
        Setter for property: (@link TemplateAutomaticTableBuilder.KpiFilterLevel NXOpen.TDP.TemplateAutomaticTableBuilder.KpiFilterLevel@endlink) FilterLevel
         Returns the filter level type   
            
         
        """
        pass
    
    ## Getter for property: (bool) MaintainBomAssemOrder
    ##  Returns the maintain bom assembly order toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return bool
    @property
    def MaintainBomAssemOrder(self) -> bool:
        """
        Getter for property: (bool) MaintainBomAssemOrder
         Returns the maintain bom assembly order toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) MaintainBomAssemOrder

    ##  Returns the maintain bom assembly order toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    @MaintainBomAssemOrder.setter
    def MaintainBomAssemOrder(self, maintainBomAssemOrder: bool):
        """
        Setter for property: (bool) MaintainBomAssemOrder
         Returns the maintain bom assembly order toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateAutomaticTablePMIFilterBuilder NXOpen.TDP.TemplateAutomaticTablePMIFilterBuilder@endlink) PmiFilter
    ##  Returns the PMI Filter   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return TemplateAutomaticTablePMIFilterBuilder
    @property
    def PmiFilter(self) -> TemplateAutomaticTablePMIFilterBuilder:
        """
        Getter for property: (@link TemplateAutomaticTablePMIFilterBuilder NXOpen.TDP.TemplateAutomaticTablePMIFilterBuilder@endlink) PmiFilter
         Returns the PMI Filter   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) PmiFilterPos
    ##  Returns the pmi Filter position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return TemplateAutomaticTableBuilder.PositionType
    @property
    def PmiFilterPos(self) -> TemplateAutomaticTableBuilder.PositionType:
        """
        Getter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) PmiFilterPos
         Returns the pmi Filter position   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) PmiFilterPos

    ##  Returns the pmi Filter position   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    @PmiFilterPos.setter
    def PmiFilterPos(self, position: TemplateAutomaticTableBuilder.PositionType):
        """
        Setter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) PmiFilterPos
         Returns the pmi Filter position   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowBorder
    ##  Returns the show border toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBorder

    ##  Returns the show border toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowCheckedOnly
    ##  Returns the show checked only result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowCheckedOnly(self) -> bool:
        """
        Getter for property: (bool) ShowCheckedOnly
         Returns the show checked only result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowCheckedOnly

    ##  Returns the show checked only result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowCheckedOnly.setter
    def ShowCheckedOnly(self, showCheckedOnly: bool):
        """
        Setter for property: (bool) ShowCheckedOnly
         Returns the show checked only result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowFailed
    ##  Returns the show failed result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowFailed(self) -> bool:
        """
        Getter for property: (bool) ShowFailed
         Returns the show failed result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowFailed

    ##  Returns the show failed result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowFailed.setter
    def ShowFailed(self, showFailed: bool):
        """
        Setter for property: (bool) ShowFailed
         Returns the show failed result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPassed
    ##  Returns the show passed result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowPassed(self) -> bool:
        """
        Getter for property: (bool) ShowPassed
         Returns the show passed result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPassed

    ##  Returns the show passed result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowPassed.setter
    def ShowPassed(self, showPassed: bool):
        """
        Setter for property: (bool) ShowPassed
         Returns the show passed result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPassedWithInfo
    ##  Returns the show passed with information result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowPassedWithInfo(self) -> bool:
        """
        Getter for property: (bool) ShowPassedWithInfo
         Returns the show passed with information result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPassedWithInfo

    ##  Returns the show passed with information result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowPassedWithInfo.setter
    def ShowPassedWithInfo(self, showPassedWithInfo: bool):
        """
        Setter for property: (bool) ShowPassedWithInfo
         Returns the show passed with information result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPassedWithWarning
    ##  Returns the show passed with warning result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowPassedWithWarning(self) -> bool:
        """
        Getter for property: (bool) ShowPassedWithWarning
         Returns the show passed with warning result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPassedWithWarning

    ##  Returns the show passed with warning result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowPassedWithWarning.setter
    def ShowPassedWithWarning(self, showPassedWithWarning: bool):
        """
        Setter for property: (bool) ShowPassedWithWarning
         Returns the show passed with warning result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPhysicalParameter
    ##  Returns the show physical parameters result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowPhysicalParameter(self) -> bool:
        """
        Getter for property: (bool) ShowPhysicalParameter
         Returns the show physical parameters result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPhysicalParameter

    ##  Returns the show physical parameters result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowPhysicalParameter.setter
    def ShowPhysicalParameter(self, showPhysicalParameters: bool):
        """
        Setter for property: (bool) ShowPhysicalParameter
         Returns the show physical parameters result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPhysicalParametersFolder
    ##  Returns the show physical parameters folder result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowPhysicalParametersFolder(self) -> bool:
        """
        Getter for property: (bool) ShowPhysicalParametersFolder
         Returns the show physical parameters folder result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPhysicalParametersFolder

    ##  Returns the show physical parameters folder result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowPhysicalParametersFolder.setter
    def ShowPhysicalParametersFolder(self, showPhysicalParametersFolder: bool):
        """
        Setter for property: (bool) ShowPhysicalParametersFolder
         Returns the show physical parameters folder result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowProductInterfaces
    ##  Returns the show product interface toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowProductInterfaces(self) -> bool:
        """
        Getter for property: (bool) ShowProductInterfaces
         Returns the show product interface toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowProductInterfaces

    ##  Returns the show product interface toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowProductInterfaces.setter
    def ShowProductInterfaces(self, showProductInterfaces: bool):
        """
        Setter for property: (bool) ShowProductInterfaces
         Returns the show product interface toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowSuppressed
    ##  Returns the show suppressed result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowSuppressed(self) -> bool:
        """
        Getter for property: (bool) ShowSuppressed
         Returns the show suppressed result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowSuppressed

    ##  Returns the show suppressed result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowSuppressed.setter
    def ShowSuppressed(self, showSuppressed: bool):
        """
        Setter for property: (bool) ShowSuppressed
         Returns the show suppressed result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowUnusedCheckedExps
    ##  Returns the show unused check expression toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowUnusedCheckedExps(self) -> bool:
        """
        Getter for property: (bool) ShowUnusedCheckedExps
         Returns the show unused check expression toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowUnusedCheckedExps

    ##  Returns the show unused check expression toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowUnusedCheckedExps.setter
    def ShowUnusedCheckedExps(self, showUnusedCheckedExps: bool):
        """
        Setter for property: (bool) ShowUnusedCheckedExps
         Returns the show unused check expression toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowUnusedExpCheckFolder
    ##  Returns the show unused expression check folder result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowUnusedExpCheckFolder(self) -> bool:
        """
        Getter for property: (bool) ShowUnusedExpCheckFolder
         Returns the show unused expression check folder result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowUnusedExpCheckFolder

    ##  Returns the show unused expression check folder result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowUnusedExpCheckFolder.setter
    def ShowUnusedExpCheckFolder(self, showUnusedExpCheckFolder: bool):
        """
        Setter for property: (bool) ShowUnusedExpCheckFolder
         Returns the show unused expression check folder result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowUnvalidatedReqFolder
    ##  Returns the show unvalidated requirements folder result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowUnvalidatedReqFolder(self) -> bool:
        """
        Getter for property: (bool) ShowUnvalidatedReqFolder
         Returns the show unvalidated requirements folder result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowUnvalidatedReqFolder

    ##  Returns the show unvalidated requirements folder result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowUnvalidatedReqFolder.setter
    def ShowUnvalidatedReqFolder(self, showUnvalidatedReqFolder: bool):
        """
        Setter for property: (bool) ShowUnvalidatedReqFolder
         Returns the show unvalidated requirements folder result toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowUnvalidatedReqs
    ##  Returns the show unvalidated requirements toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowUnvalidatedReqs(self) -> bool:
        """
        Getter for property: (bool) ShowUnvalidatedReqs
         Returns the show unvalidated requirements toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowUnvalidatedReqs

    ##  Returns the show unvalidated requirements toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowUnvalidatedReqs.setter
    def ShowUnvalidatedReqs(self, showUnvalidatedReqs: bool):
        """
        Setter for property: (bool) ShowUnvalidatedReqs
         Returns the show unvalidated requirements toggle   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowWorkPartOnly
    ##  Returns the show work part only result toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowWorkPartOnly(self) -> bool:
        """
        Getter for property: (bool) ShowWorkPartOnly
         Returns the show work part only result toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowWorkPartOnly

    ##  Returns the show work part only result toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowWorkPartOnly.setter
    def ShowWorkPartOnly(self, showWorkPartOnly: bool):
        """
        Setter for property: (bool) ShowWorkPartOnly
         Returns the show work part only result toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
    ##  Returns the font, and width of Automatic table text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
         Returns the font, and width of Automatic table text   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) ZoomToPmiPos
    ##  Returns the Zoom To PMI position   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return TemplateAutomaticTableBuilder.PositionType
    @property
    def ZoomToPmiPos(self) -> TemplateAutomaticTableBuilder.PositionType:
        """
        Getter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) ZoomToPmiPos
         Returns the Zoom To PMI position   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) ZoomToPmiPos

    ##  Returns the Zoom To PMI position   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    @ZoomToPmiPos.setter
    def ZoomToPmiPos(self, position: TemplateAutomaticTableBuilder.PositionType):
        """
        Setter for property: (@link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink) ZoomToPmiPos
         Returns the Zoom To PMI position   
            
         
        """
        pass
    
    ##  To add the row in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    def AddColumn(self) -> bool:
        """
         To add the row in the table
         @return exists (bool): .
        """
        pass
    
    ##  To delete the row in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index"> (int)  index of the column to be deleted </param>
    def DeleteColumn(self, index: int) -> bool:
        """
         To delete the row in the table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the ICD column type in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="colType"> (@link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType@endlink)  column type to be updated </param>
    def SetICDColumnType(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType) -> bool:
        """
         To modify the ICD column type in the table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the KPI column type in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="colType"> (@link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType@endlink)  column type to be updated </param>
    def SetKPIColumnType(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType) -> bool:
        """
         To modify the KPI column type in the table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the PAD column type in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="colType"> (@link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType@endlink)  column type to be updated </param>
    def SetPADColumnType(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType) -> bool:
        """
         To modify the PAD column type in the table
         @return exists (bool): .
        """
        pass
    
    ##  To swap the columns in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="index1"> (int)  location of the first item </param>
    ## <param name="index2"> (int)  location of the second item </param>
    ## <param name="length"> (int)  number of rows selected for swapping </param>
    def SwapColumns(self, index1: int, index2: int, length: int) -> bool:
        """
         To swap the columns in the table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the Attribute name in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="value"> (str)  Value to be updated </param>
    def UpdateAttribute(self, rowIndex: int, value: str) -> bool:
        """
         To modify the Attribute name in the table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the Bom column type in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="colType"> (@link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType@endlink)  column type to be updated </param>
    def UpdateBomColumn(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType) -> bool:
        """
         To modify the Bom column type in the table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the header column in table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="value"> (str)  Value to be updated </param>
    def UpdateHeader(self, rowIndex: int, value: str) -> bool:
        """
         To modify the header column in table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the Pmi column type in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1899.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="colType"> (@link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType@endlink)  column type to be updated </param>
    def UpdatePmiColumn(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType) -> bool:
        """
         To modify the Pmi column type in the table
         @return exists (bool): .
        """
        pass
    
    ##  To modify the Width value in the table
    ##  @return exists (bool): .
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="rowIndex"> (int)  index of the column to be updated </param>
    ## <param name="value"> (float)  Value to be updated </param>
    def UpdateWidth(self, rowIndex: int, value: float) -> bool:
        """
         To modify the Width value in the table
         @return exists (bool): .
        """
        pass
    
import NXOpen
##  Represents a Template Automatic Table PMIFilter Builder 
## 
##   <br>  Created in NX1953.0.0  <br> 

class TemplateAutomaticTablePMIFilterBuilder(NXOpen.TaggedObject): 
    """ Represents a Template Automatic Table PMIFilter Builder """


    ##  Represents PMI Filter options 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Dimension</term><description> 
    ##  Dimension PMI Filter        </description> </item><item><term> 
    ## AnnotationNote</term><description> 
    ##  Annotation Notes PMI Filter        </description> </item><item><term> 
    ## AnnotationFCF</term><description> 
    ##  Annotation Feature Control Frame PMI Filter        </description> </item><item><term> 
    ## AnnotationDatumFeature</term><description> 
    ##  Annotation Datum Feature PMI Filter        </description> </item><item><term> 
    ## AnnotationSurfaceFinish</term><description> 
    ##  Annotation Surface Finish PMI Filter        </description> </item><item><term> 
    ## AnnotationDatumTarget</term><description> 
    ##  Annotation Datum Target PMI Filter        </description> </item><item><term> 
    ## AnnotationWeldSymbol</term><description> 
    ##  Annotation Weld Symbol PMI Filter        </description> </item><item><term> 
    ## AnnotationBalloon</term><description> 
    ##  Annotation Balloon PMI Filter        </description> </item><item><term> 
    ## AnnotationSpecialtyNote</term><description> 
    ##  Annotation Speciality Notes PMI Filter        </description> </item><item><term> 
    ## Table</term><description> 
    ##  Table PMI Filter     </description> </item><item><term> 
    ## CustomSymbol</term><description> 
    ##  Custom Symbol PMI Filter     </description> </item><item><term> 
    ## Centerline</term><description> 
    ##  Centerline PMI Report Filter </description> </item><item><term> 
    ## Region</term><description> 
    ##  Region PMI Report Filter     </description> </item><item><term> 
    ## SecurityMarking</term><description> 
    ##  Security Marking PMI Filter     </description> </item><item><term> 
    ## CuttingPlaneSymbol</term><description> 
    ##  Cutting Plane Symbol PMI Filter     </description> </item><item><term> 
    ## AnnotationEdgeConditionSymbol</term><description> 
    ##  Annotation Edge Condition Symbol PMI Filter        </description> </item></list>
    class Filter(Enum):
        """
        Members Include: <Dimension> <AnnotationNote> <AnnotationFCF> <AnnotationDatumFeature> <AnnotationSurfaceFinish> <AnnotationDatumTarget> <AnnotationWeldSymbol> <AnnotationBalloon> <AnnotationSpecialtyNote> <Table> <CustomSymbol> <Centerline> <Region> <SecurityMarking> <CuttingPlaneSymbol> <AnnotationEdgeConditionSymbol>
        """
        Dimension: int
        AnnotationNote: int
        AnnotationFCF: int
        AnnotationDatumFeature: int
        AnnotationSurfaceFinish: int
        AnnotationDatumTarget: int
        AnnotationWeldSymbol: int
        AnnotationBalloon: int
        AnnotationSpecialtyNote: int
        Table: int
        CustomSymbol: int
        Centerline: int
        Region: int
        SecurityMarking: int
        CuttingPlaneSymbol: int
        AnnotationEdgeConditionSymbol: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTablePMIFilterBuilder.Filter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  Returns PMI filter status 
    ##  @return pmiFilterStatus (bool): .
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pmiFilterType"> (@link TemplateAutomaticTablePMIFilterBuilder.Filter NXOpen.TDP.TemplateAutomaticTablePMIFilterBuilder.Filter@endlink) </param>
    def GetPmiFilterStatus(self, pmiFilterType: TemplateAutomaticTablePMIFilterBuilder.Filter) -> bool:
        """
         Returns PMI filter status 
         @return pmiFilterStatus (bool): .
        """
        pass
    
    ##  Sets PMI filter status 
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="pmiFilterType"> (@link TemplateAutomaticTablePMIFilterBuilder.Filter NXOpen.TDP.TemplateAutomaticTablePMIFilterBuilder.Filter@endlink) </param>
    ## <param name="pmiFilterStatus"> (bool) </param>
    def SetPmiFilterStatus(self, pmiFilterType: TemplateAutomaticTablePMIFilterBuilder.Filter, pmiFilterStatus: bool) -> None:
        """
         Sets PMI filter status 
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateAutomaticTable NXOpen::TDP::TemplateAutomaticTable@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateAutomaticTableBuilder  NXOpen::TDP::TemplateAutomaticTableBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateAutomaticTable(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateAutomaticTable</ja_class> object.
    """
    pass


import NXOpen
##  Represents a Template Base Rectangle Builder  <br> This is an abstract class and cannot be instantiated.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateBaseRectangleBuilder(NXOpen.Builder): 
    """ Represents a Template Base Rectangle Builder """


    ## Getter for property: (float) Height
    ##  Returns the height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height   
            
         
        """
        pass
    
    ## Setter for property: (float) Height

    ##  Returns the height   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height   
            
         
        """
        pass
    
    ## Getter for property: (float) Length
    ##  Returns the length   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length   
            
         
        """
        pass
    
    ## Setter for property: (float) Length

    ##  Returns the length   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
    ##  Returns the origin   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Point3d
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
         Returns the origin   
            
         
        """
        pass
    
    ## Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin

    ##  Returns the origin   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: (@link NXOpen.Point3d NXOpen.Point3d@endlink) Origin
         Returns the origin   
            
         
        """
        pass
    
import NXOpen
##  Represents a Template DiagramArea Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateDiagramareaBuilder  NXOpen::TDP::Manager::CreateTemplateDiagramareaBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class TemplateDiagramAreaBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template DiagramArea Builder """


    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
    ##  Returns the color and width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowBorder
    ##  Returns the show border toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    ## @return bool
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBorder

    ##  Returns the show border toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2007.0.0  <br> 

    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateDiagramArea NXOpen::TDP::TemplateDiagramArea@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateDiagramAreaBuilder  NXOpen::TDP::TemplateDiagramAreaBuilder @endlink  <br> 
## 
##   <br>  Created in NX2007.0.0  <br> 

class TemplateDiagramArea(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateDiagramArea</ja_class> object.
    """
    pass


import NXOpen
import NXOpen.Annotations
##  Represents a Edit Cell builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateEditcellBuilder  NXOpen::TDP::Manager::CreateTemplateEditcellBuilder @endlink  <br> 
## Default values.
## <list type="table"> 
##  
## <listheader><term> 
## Property</term>  <description> 
## Value</description> </listheader>
## <item><term> 
##  
## Text.TextBlock.CustomSymbolScale </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolAspectRatio </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolHeight </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolLength </term> <description> 
##  
## 25.4 (millimeters part), 1.0 (inches part) </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolPreferences </term> <description> 
##  
## UseCurrent </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolScale </term> <description> 
##  
## 1.0 </description> </item> 
## 
## <item><term> 
##  
## Text.TextBlock.SymbolSizeMethod </term> <description> 
##  
## ScaleAndAspectRatio </description> </item> 
## 
## </list> 

## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateEditCellBuilder(NXOpen.Builder): 
    """ Represents a Edit Cell builder """


    ##  Represents the option @link NXOpen::TDP::TemplateEditCellBuilder::TextJustificationType NXOpen::TDP::TemplateEditCellBuilder::TextJustificationType@endlink 
    ##            for a @link NXOpen::TDP::TemplateEditCellBuilder NXOpen::TDP::TemplateEditCellBuilder@endlink .
    ##         
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Center</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item></list>
    class TextJustificationType(Enum):
        """
        Members Include: <Left> <Center> <Right>
        """
        Left: int
        Center: int
        Right: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateEditCellBuilder.TextJustificationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.Annotations.TextWithEditControlsBuilder NXOpen.Annotations.TextWithEditControlsBuilder@endlink) Text
    ##  Returns the text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Annotations.TextWithEditControlsBuilder
    @property
    def Text(self) -> NXOpen.Annotations.TextWithEditControlsBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.TextWithEditControlsBuilder NXOpen.Annotations.TextWithEditControlsBuilder@endlink) Text
         Returns the text   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextColorFontWidth
    ##  Returns the text color font width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextColorFontWidth(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextColorFontWidth
         Returns the text color font width   
            
         
        """
        pass
    
    ## Getter for property: (float) TextHeight
    ##  Returns the height of the cell   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def TextHeight(self) -> float:
        """
        Getter for property: (float) TextHeight
         Returns the height of the cell   
            
         
        """
        pass
    
    ## Setter for property: (float) TextHeight

    ##  Returns the height of the cell   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @TextHeight.setter
    def TextHeight(self, height: float):
        """
        Setter for property: (float) TextHeight
         Returns the height of the cell   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateEditCellBuilder.TextJustificationType NXOpen.TDP.TemplateEditCellBuilder.TextJustificationType@endlink) TextJustification
    ##  Returns the text alignment of the cell   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TemplateEditCellBuilder.TextJustificationType
    @property
    def TextJustification(self) -> TemplateEditCellBuilder.TextJustificationType:
        """
        Getter for property: (@link TemplateEditCellBuilder.TextJustificationType NXOpen.TDP.TemplateEditCellBuilder.TextJustificationType@endlink) TextJustification
         Returns the text alignment of the cell   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateEditCellBuilder.TextJustificationType NXOpen.TDP.TemplateEditCellBuilder.TextJustificationType@endlink) TextJustification

    ##  Returns the text alignment of the cell   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @TextJustification.setter
    def TextJustification(self, alignment: TemplateEditCellBuilder.TextJustificationType):
        """
        Setter for property: (@link TemplateEditCellBuilder.TextJustificationType NXOpen.TDP.TemplateEditCellBuilder.TextJustificationType@endlink) TextJustification
         Returns the text alignment of the cell   
            
         
        """
        pass
    
import NXOpen
##  Represents a Template Form Field Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateFormFieldBuilder  NXOpen::TDP::Manager::CreateTemplateFormFieldBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateFormFieldBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Form Field Builder """


    ## Getter for property: (str) Label
    ##  Returns the placeholder text used to identify the Form Field in the TDP Template environment  
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the placeholder text used to identify the Form Field in the TDP Template environment  
            
         
        """
        pass
    
    ## Setter for property: (str) Label

    ##  Returns the placeholder text used to identify the Form Field in the TDP Template environment  
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Label.setter
    def Label(self, labelText: str):
        """
        Setter for property: (str) Label
         Returns the placeholder text used to identify the Form Field in the TDP Template environment  
            
         
        """
        pass
    
    ## Getter for property: (float) LabelHeight
    ##  Returns the label text height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the label text height   
            
         
        """
        pass
    
    ## Setter for property: (float) LabelHeight

    ##  Returns the label text height   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @LabelHeight.setter
    def LabelHeight(self, height: float):
        """
        Setter for property: (float) LabelHeight
         Returns the label text height   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) LineCfw
    ##  Returns the color and width of the Form Field lines   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def LineCfw(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) LineCfw
         Returns the color and width of the Form Field lines   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowLabel
    ##  Returns the Display in Published PDF    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    ## @return bool
    @property
    def ShowLabel(self) -> bool:
        """
        Getter for property: (bool) ShowLabel
         Returns the Display in Published PDF    
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowLabel

    ##  Returns the Display in Published PDF    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2212.0.0  <br> 

    @ShowLabel.setter
    def ShowLabel(self, showLabel: bool):
        """
        Setter for property: (bool) ShowLabel
         Returns the Display in Published PDF    
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
    ##  Returns the color, font, and width of the Form Field text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
         Returns the color, font, and width of the Form Field text   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateFormField NXOpen::TDP::TemplateFormField@endlink  object.  <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateFormFieldBuilder  NXOpen::TDP::TemplateFormFieldBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateFormField(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateFormField</ja_class> object. """
    pass


import NXOpen.Display
##  Represents a Template Image Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateImageBuilder  NXOpen::TDP::Manager::CreateTemplateImageBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateImageBuilder(NXOpen.Display.ImageBaseBuilder): 
    """ Represents a Template Image Builder """
    pass


import NXOpen.Display
##   Represents the @link NXOpen::TDP::TemplateImage NXOpen::TDP::TemplateImage@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateImageBuilder  NXOpen::TDP::TemplateImageBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateImage(NXOpen.Display.ImageBase): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateImage</ja_class> object.
    """
    pass


import NXOpen.Annotations
##  Represents a TDP Template Note builder used to create Notes in the Template environment <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateNoteBuilder  NXOpen::TDP::Manager::CreateTemplateNoteBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateNoteBuilder(NXOpen.Annotations.DraftingNoteBuilder): 
    """ Represents a TDP Template Note builder used to create Notes in the Template environment"""


    ##  available template note types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Static</term><description> 
    ## </description> </item><item><term> 
    ## Userdefined</term><description> 
    ## </description> </item><item><term> 
    ## Controlled</term><description> 
    ## </description> </item></list>
    class NoteTypes(Enum):
        """
        Members Include: <Static> <Userdefined> <Controlled>
        """
        Static: int
        Userdefined: int
        Controlled: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateNoteBuilder.NoteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) Label
    ##  Returns the label used to identify the Note in Publish   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label used to identify the Note in Publish   
            
         
        """
        pass
    
    ## Setter for property: (str) Label

    ##  Returns the label used to identify the Note in Publish   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Label.setter
    def Label(self, labelText: str):
        """
        Setter for property: (str) Label
         Returns the label used to identify the Note in Publish   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateNoteBuilder.NoteTypes NXOpen.TDP.TemplateNoteBuilder.NoteTypes@endlink) NoteType
    ##  Returns the template note type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TemplateNoteBuilder.NoteTypes
    @property
    def NoteType(self) -> TemplateNoteBuilder.NoteTypes:
        """
        Getter for property: (@link TemplateNoteBuilder.NoteTypes NXOpen.TDP.TemplateNoteBuilder.NoteTypes@endlink) NoteType
         Returns the template note type   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateNoteBuilder.NoteTypes NXOpen.TDP.TemplateNoteBuilder.NoteTypes@endlink) NoteType

    ##  Returns the template note type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NoteType.setter
    def NoteType(self, textType: TemplateNoteBuilder.NoteTypes):
        """
        Setter for property: (@link TemplateNoteBuilder.NoteTypes NXOpen.TDP.TemplateNoteBuilder.NoteTypes@endlink) NoteType
         Returns the template note type   
            
         
        """
        pass
    
import NXOpen
##  Represents a @link TDP::TemplatePage TDP::TemplatePage@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplatePageBuilder  NXOpen::TDP::Manager::CreateTemplatePageBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplatePageBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>TDP.TemplatePage</ja_class> builder """


    ##  english template standard size 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## A</term><description> 
    ## </description> </item><item><term> 
    ## B</term><description> 
    ## </description> </item><item><term> 
    ## C</term><description> 
    ## </description> </item><item><term> 
    ## D</term><description> 
    ## </description> </item><item><term> 
    ## E</term><description> 
    ## </description> </item><item><term> 
    ## F</term><description> 
    ## </description> </item><item><term> 
    ## H</term><description> 
    ## </description> </item><item><term> 
    ## J</term><description> 
    ## </description> </item><item><term> 
    ## Custom</term><description> 
    ## </description> </item></list>
    class EnglishSizeType(Enum):
        """
        Members Include: <A> <B> <C> <D> <E> <F> <H> <J> <Custom>
        """
        A: int
        B: int
        C: int
        D: int
        E: int
        F: int
        H: int
        J: int
        Custom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplatePageBuilder.EnglishSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  metric template standard size 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## A0</term><description> 
    ## </description> </item><item><term> 
    ## A1</term><description> 
    ## </description> </item><item><term> 
    ## A2</term><description> 
    ## </description> </item><item><term> 
    ## A3</term><description> 
    ## </description> </item><item><term> 
    ## A4</term><description> 
    ## </description> </item><item><term> 
    ## Custom</term><description> 
    ## </description> </item></list>
    class MetricSizeType(Enum):
        """
        Members Include: <A0> <A1> <A2> <A3> <A4> <Custom>
        """
        A0: int
        A1: int
        A2: int
        A3: int
        A4: int
        Custom: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplatePageBuilder.MetricSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ##  template orientation 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Landscape</term><description> 
    ## </description> </item><item><term> 
    ## Portrait</term><description> 
    ## </description> </item></list>
    class OrientationType(Enum):
        """
        Members Include: <Landscape> <Portrait>
        """
        Landscape: int
        Portrait: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplatePageBuilder.OrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (float) Height
    ##  Returns the custom or standard height for the page   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the custom or standard height for the page   
            
         
        """
        pass
    
    ## Setter for property: (float) Height

    ##  Returns the custom or standard height for the page   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Height.setter
    def Height(self, customHeight: float):
        """
        Setter for property: (float) Height
         Returns the custom or standard height for the page   
            
         
        """
        pass
    
    ## Getter for property: (float) Length
    ##  Returns the custom or standard length to be used for the page to be created or edited.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the custom or standard length to be used for the page to be created or edited.  
             
         
        """
        pass
    
    ## Setter for property: (float) Length

    ##  Returns the custom or standard length to be used for the page to be created or edited.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Length.setter
    def Length(self, customLength: float):
        """
        Setter for property: (float) Length
         Returns the custom or standard length to be used for the page to be created or edited.  
             
         
        """
        pass
    
    ## Getter for property: (@link TemplatePageBuilder.OrientationType NXOpen.TDP.TemplatePageBuilder.OrientationType@endlink) Orientation
    ##  Returns the orientation   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TemplatePageBuilder.OrientationType
    @property
    def Orientation(self) -> TemplatePageBuilder.OrientationType:
        """
        Getter for property: (@link TemplatePageBuilder.OrientationType NXOpen.TDP.TemplatePageBuilder.OrientationType@endlink) Orientation
         Returns the orientation   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplatePageBuilder.OrientationType NXOpen.TDP.TemplatePageBuilder.OrientationType@endlink) Orientation

    ##  Returns the orientation   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @Orientation.setter
    def Orientation(self, orientation: TemplatePageBuilder.OrientationType):
        """
        Setter for property: (@link TemplatePageBuilder.OrientationType NXOpen.TDP.TemplatePageBuilder.OrientationType@endlink) Orientation
         Returns the orientation   
            
         
        """
        pass
    
    ## Getter for property: (str) PageName
    ##  Returns the Page Name text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def PageName(self) -> str:
        """
        Getter for property: (str) PageName
         Returns the Page Name text   
            
         
        """
        pass
    
    ## Setter for property: (str) PageName

    ##  Returns the Page Name text   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PageName.setter
    def PageName(self, pageName: str):
        """
        Setter for property: (str) PageName
         Returns the Page Name text   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowPageNumber
    ##  Returns the show Page number   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ShowPageNumber(self) -> bool:
        """
        Getter for property: (bool) ShowPageNumber
         Returns the show Page number   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowPageNumber

    ##  Returns the show Page number   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ShowPageNumber.setter
    def ShowPageNumber(self, showPageNumber: bool):
        """
        Setter for property: (bool) ShowPageNumber
         Returns the show Page number   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplatePageBuilder.EnglishSizeType NXOpen.TDP.TemplatePageBuilder.EnglishSizeType@endlink) StandardEnglishSize
    ##  Returns the standard english size to be used for the page to be created or edited.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TemplatePageBuilder.EnglishSizeType
    @property
    def StandardEnglishSize(self) -> TemplatePageBuilder.EnglishSizeType:
        """
        Getter for property: (@link TemplatePageBuilder.EnglishSizeType NXOpen.TDP.TemplatePageBuilder.EnglishSizeType@endlink) StandardEnglishSize
         Returns the standard english size to be used for the page to be created or edited.  
             
         
        """
        pass
    
    ## Setter for property: (@link TemplatePageBuilder.EnglishSizeType NXOpen.TDP.TemplatePageBuilder.EnglishSizeType@endlink) StandardEnglishSize

    ##  Returns the standard english size to be used for the page to be created or edited.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StandardEnglishSize.setter
    def StandardEnglishSize(self, englishSize: TemplatePageBuilder.EnglishSizeType):
        """
        Setter for property: (@link TemplatePageBuilder.EnglishSizeType NXOpen.TDP.TemplatePageBuilder.EnglishSizeType@endlink) StandardEnglishSize
         Returns the standard english size to be used for the page to be created or edited.  
             
         
        """
        pass
    
    ## Getter for property: (@link TemplatePageBuilder.MetricSizeType NXOpen.TDP.TemplatePageBuilder.MetricSizeType@endlink) StandardMetricSize
    ##  Returns the standard metric size to be used for the page to be created or edited.  
    ##      
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TemplatePageBuilder.MetricSizeType
    @property
    def StandardMetricSize(self) -> TemplatePageBuilder.MetricSizeType:
        """
        Getter for property: (@link TemplatePageBuilder.MetricSizeType NXOpen.TDP.TemplatePageBuilder.MetricSizeType@endlink) StandardMetricSize
         Returns the standard metric size to be used for the page to be created or edited.  
             
         
        """
        pass
    
    ## Setter for property: (@link TemplatePageBuilder.MetricSizeType NXOpen.TDP.TemplatePageBuilder.MetricSizeType@endlink) StandardMetricSize

    ##  Returns the standard metric size to be used for the page to be created or edited.  
    ##      
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @StandardMetricSize.setter
    def StandardMetricSize(self, metricSize: TemplatePageBuilder.MetricSizeType):
        """
        Setter for property: (@link TemplatePageBuilder.MetricSizeType NXOpen.TDP.TemplatePageBuilder.MetricSizeType@endlink) StandardMetricSize
         Returns the standard metric size to be used for the page to be created or edited.  
             
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplatePage NXOpen::TDP::TemplatePage@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplatePageBuilder  NXOpen::TDP::TemplatePageBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplatePage(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplatePage</ja_class> object.
    """


    ##  Activates the page so that it displays in the graphics area. 
    ##          <br> 
    ##         An update is performed as part of activating page.  <br> 
    ##         
    ##  @return result (bool):  True if page was activated, false otherwise .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def Activate(self) -> bool:
        """
         Activates the page so that it displays in the graphics area. 
                 <br> 
                An update is performed as part of activating page.  <br> 
                
         @return result (bool):  True if page was activated, false otherwise .
        """
        pass
    
import NXOpen
##  Represents a Template PrintView Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplatePrintViewBuilder  NXOpen::TDP::Manager::CreateTemplatePrintViewBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class TemplatePrintViewBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template PrintView Builder """


    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
    ##  Returns the color and width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectViewport
    ##  Returns the selected viewport   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1953.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectViewport(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectViewport
         Returns the selected viewport   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
    ##  Returns the color, font, and width of the Print View text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
         Returns the color, font, and width of the Print View text   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplatePrintView NXOpen::TDP::TemplatePrintView@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplatePrintViewBuilder  NXOpen::TDP::TemplatePrintViewBuilder @endlink  <br> 
## 
##   <br>  Created in NX1953.0.0  <br> 

class TemplatePrintView(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplatePrintView</ja_class> object.
    """
    pass


import NXOpen
##  Represents a Template Properties Builder  <br> No KF support.  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplatePropertiesBuilder(NXOpen.Builder): 
    """ Represents a Template Properties Builder """


    ##  represents the template format 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## Format3DPDF</term><description> 
    ##  3D PDF format </description> </item><item><term> 
    ## FormatJTplusPDF</term><description> 
    ##  JT plus PDF format </description> </item></list>
    class TemplateFormatEnum(Enum):
        """
        Members Include: <Format3DPDF> <FormatJTplusPDF>
        """
        Format3DPDF: int
        FormatJTplusPDF: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplatePropertiesBuilder.TemplateFormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (str) PresentationName
    ##  Returns the presentation name   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return str
    @property
    def PresentationName(self) -> str:
        """
        Getter for property: (str) PresentationName
         Returns the presentation name   
            
         
        """
        pass
    
    ## Setter for property: (str) PresentationName

    ##  Returns the presentation name   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @PresentationName.setter
    def PresentationName(self, presentationName: str):
        """
        Setter for property: (str) PresentationName
         Returns the presentation name   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplatePropertiesBuilder.TemplateFormatEnum NXOpen.TDP.TemplatePropertiesBuilder.TemplateFormatEnum@endlink) TemplateFormat
    ##  Returns the template format   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return TemplatePropertiesBuilder.TemplateFormatEnum
    @property
    def TemplateFormat(self) -> TemplatePropertiesBuilder.TemplateFormatEnum:
        """
        Getter for property: (@link TemplatePropertiesBuilder.TemplateFormatEnum NXOpen.TDP.TemplatePropertiesBuilder.TemplateFormatEnum@endlink) TemplateFormat
         Returns the template format   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplatePropertiesBuilder.TemplateFormatEnum NXOpen.TDP.TemplatePropertiesBuilder.TemplateFormatEnum@endlink) TemplateFormat

    ##  Returns the template format   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @TemplateFormat.setter
    def TemplateFormat(self, templateFormat: TemplatePropertiesBuilder.TemplateFormatEnum):
        """
        Setter for property: (@link TemplatePropertiesBuilder.TemplateFormatEnum NXOpen.TDP.TemplatePropertiesBuilder.TemplateFormatEnum@endlink) TemplateFormat
         Returns the template format   
            
         
        """
        pass
    
    ##  Returns the description 
    ##  @return description (List[str]): .
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    def GetDescription(self) -> List[str]:
        """
         Returns the description 
         @return description (List[str]): .
        """
        pass
    
    ##  Sets the description 
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## License requirements: None.
    ## 
    ## <param name="description"> (List[str])  </param>
    def SetDescription(self, description: List[str]) -> None:
        """
         Sets the description 
        """
        pass
    
import NXOpen
##  Represents a Template Rectangle Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateRectangleBuilder  NXOpen::TDP::Manager::CreateTemplateRectangleBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateRectangleBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Rectangle Builder """


    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
    ##  Returns the color and width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateRectangle NXOpen::TDP::TemplateRectangle@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateRectangleBuilder  NXOpen::TDP::TemplateRectangleBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateRectangle(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateRectangle</ja_class> object.
    """
    pass


import NXOpen
import NXOpen.Annotations
##  Represents a @link NXOpen::TDP::TemplateTableSection NXOpen::TDP::TemplateTableSection@endlink  builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateTableSectionBuilder  NXOpen::TDP::Manager::CreateTemplateTableSectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateTableSectionBuilder(NXOpen.Builder): 
    """ Represents a <ja_class>NXOpen.TDP.TemplateTableSection</ja_class> builder """


    ## Getter for property: (float) ColumnWidth
    ##  Returns the column width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def ColumnWidth(self) -> float:
        """
        Getter for property: (float) ColumnWidth
         Returns the column width   
            
         
        """
        pass
    
    ## Setter for property: (float) ColumnWidth

    ##  Returns the column width   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ColumnWidth.setter
    def ColumnWidth(self, columnWidth: float):
        """
        Setter for property: (float) ColumnWidth
         Returns the column width   
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfColumns
    ##  Returns the number of columns of the table    
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
         Returns the number of columns of the table    
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfColumns

    ##  Returns the number of columns of the table    
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfColumns.setter
    def NumberOfColumns(self, numberOfColumns: int):
        """
        Setter for property: (int) NumberOfColumns
         Returns the number of columns of the table    
            
         
        """
        pass
    
    ## Getter for property: (int) NumberOfRows
    ##  Returns the number of rows of the table   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return int
    @property
    def NumberOfRows(self) -> int:
        """
        Getter for property: (int) NumberOfRows
         Returns the number of rows of the table   
            
         
        """
        pass
    
    ## Setter for property: (int) NumberOfRows

    ##  Returns the number of rows of the table   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @NumberOfRows.setter
    def NumberOfRows(self, numberOfRows: int):
        """
        Setter for property: (int) NumberOfRows
         Returns the number of rows of the table   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
    ##  Returns the origin, where the table is going to be displayed   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Annotations.OriginBuilder
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.OriginBuilder NXOpen.Annotations.OriginBuilder@endlink) Origin
         Returns the origin, where the table is going to be displayed   
            
         
        """
        pass
    
    ## Getter for property: (float) RowHeight
    ##  Returns the row height   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return float
    @property
    def RowHeight(self) -> float:
        """
        Getter for property: (float) RowHeight
         Returns the row height   
            
         
        """
        pass
    
    ## Setter for property: (float) RowHeight

    ##  Returns the row height   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @RowHeight.setter
    def RowHeight(self, rowHeight: float):
        """
        Setter for property: (float) RowHeight
         Returns the row height   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.Annotations.TableStyleBuilder NXOpen.Annotations.TableStyleBuilder@endlink) Style
    ##  Returns the style   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.Annotations.TableStyleBuilder
    @property
    def Style(self) -> NXOpen.Annotations.TableStyleBuilder:
        """
        Getter for property: (@link NXOpen.Annotations.TableStyleBuilder NXOpen.Annotations.TableStyleBuilder@endlink) Style
         Returns the style   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateTableSection NXOpen::TDP::TemplateTableSection@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateTableSectionBuilder  NXOpen::TDP::TemplateTableSectionBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateTableSection(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateTableSection</ja_class> object.
    """
    pass


import NXOpen
##  Represents a Template View Carousel Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateViewCarouselBuilder  NXOpen::TDP::Manager::CreateTemplateViewCarouselBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateViewCarouselBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template View Carousel Builder """


    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
    ##  Returns the color and width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectViewport
    ##  Returns the selected viewport   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectViewport(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectViewport
         Returns the selected viewport   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowBorder
    ##  Returns the show border toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBorder

    ##  Returns the show border toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
    ##  Returns the font, and width of the View Carousel text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
         Returns the font, and width of the View Carousel text   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateViewCarousel NXOpen::TDP::TemplateViewCarousel@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateViewCarouselBuilder  NXOpen::TDP::TemplateViewCarouselBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateViewCarousel(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateViewCarousel</ja_class> object.
    """
    pass


import NXOpen
##  Represents a Template ViewList Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateViewListBuilder  NXOpen::TDP::Manager::CreateTemplateViewListBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class TemplateViewListBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template ViewList Builder """


    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
    ##  Returns the color and width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectViewport
    ##  Returns the selected viewport   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1926.0.0  <br> 

    ## @return NXOpen.SelectDisplayableObject
    @property
    def SelectViewport(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: (@link NXOpen.SelectDisplayableObject NXOpen.SelectDisplayableObject@endlink) SelectViewport
         Returns the selected viewport   
            
         
        """
        pass
    
    ## Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
    ##  Returns the color, font, and width of the View List text   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1980.0.0  <br> 

    ## @return NXOpen.TextColorFontWidthBuilder
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.TextColorFontWidthBuilder NXOpen.TextColorFontWidthBuilder@endlink) TextCfw
         Returns the color, font, and width of the View List text   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateViewList NXOpen::TDP::TemplateViewList@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateViewListBuilder  NXOpen::TDP::TemplateViewListBuilder @endlink  <br> 
## 
##   <br>  Created in NX1926.0.0  <br> 

class TemplateViewList(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateViewList</ja_class> object.
    """
    pass


import NXOpen
##  Represents a Template Viewport Builder  <br> To create a new instance of this class, use @link NXOpen::TDP::Manager::CreateTemplateViewportBuilder  NXOpen::TDP::Manager::CreateTemplateViewportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateViewportBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Viewport Builder """


    ##  represents the default view types 
    ## <list type="table"> 
    ## <listheader><term> 
    ## Enumerator</term><description> 
    ## Comment</description> </listheader><item><term> 
    ## NotAssigned</term><description> 
    ## </description> </item><item><term> 
    ## Back</term><description> 
    ## </description> </item><item><term> 
    ## Bottom</term><description> 
    ## </description> </item><item><term> 
    ## Front</term><description> 
    ## </description> </item><item><term> 
    ## Isometric</term><description> 
    ## </description> </item><item><term> 
    ## Left</term><description> 
    ## </description> </item><item><term> 
    ## Right</term><description> 
    ## </description> </item><item><term> 
    ## Top</term><description> 
    ## </description> </item><item><term> 
    ## Trimetric</term><description> 
    ## </description> </item><item><term> 
    ## UserDefined</term><description> 
    ## </description> </item></list>
    class DefaultViewType(Enum):
        """
        Members Include: <NotAssigned> <Back> <Bottom> <Front> <Isometric> <Left> <Right> <Top> <Trimetric> <UserDefined>
        """
        NotAssigned: int
        Back: int
        Bottom: int
        Front: int
        Isometric: int
        Left: int
        Right: int
        Top: int
        Trimetric: int
        UserDefined: int
        ## Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
        ## <param name="value" type="int"> Any integer value or bit operation result of enum </param>
        @staticmethod
        def ValueOf(value: int) -> TemplateViewportBuilder.DefaultViewType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    
    
    ## Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
    ##  Returns the color and width   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return NXOpen.LineColorFontWidthBuilder
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: (@link NXOpen.LineColorFontWidthBuilder NXOpen.LineColorFontWidthBuilder@endlink) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    
    ## Getter for property: (@link TemplateViewportBuilder.DefaultViewType NXOpen.TDP.TemplateViewportBuilder.DefaultViewType@endlink) DefaultViewTypes
    ##  Returns the default viwe type   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return TemplateViewportBuilder.DefaultViewType
    @property
    def DefaultViewTypes(self) -> TemplateViewportBuilder.DefaultViewType:
        """
        Getter for property: (@link TemplateViewportBuilder.DefaultViewType NXOpen.TDP.TemplateViewportBuilder.DefaultViewType@endlink) DefaultViewTypes
         Returns the default viwe type   
            
         
        """
        pass
    
    ## Setter for property: (@link TemplateViewportBuilder.DefaultViewType NXOpen.TDP.TemplateViewportBuilder.DefaultViewType@endlink) DefaultViewTypes

    ##  Returns the default viwe type   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @DefaultViewTypes.setter
    def DefaultViewTypes(self, defaultViewType: TemplateViewportBuilder.DefaultViewType):
        """
        Setter for property: (@link TemplateViewportBuilder.DefaultViewType NXOpen.TDP.TemplateViewportBuilder.DefaultViewType@endlink) DefaultViewTypes
         Returns the default viwe type   
            
         
        """
        pass
    
    ## Getter for property: (str) Label
    ##  Returns the label   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label   
            
         
        """
        pass
    
    ## Setter for property: (str) Label

    ##  Returns the label   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @Label.setter
    def Label(self, labelText: str):
        """
        Setter for property: (str) Label
         Returns the label   
            
         
        """
        pass
    
    ## Getter for property: (bool) ShowBorder
    ##  Returns the show border toggle   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    ## @return bool
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
    ## Setter for property: (bool) ShowBorder

    ##  Returns the show border toggle   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX1847.0.0  <br> 

    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    
    ## Getter for property: (str) UserDefinedView
    ##  Returns the User Defined View   
    ##     
    ##  
    ## Getter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    ## @return str
    @property
    def UserDefinedView(self) -> str:
        """
        Getter for property: (str) UserDefinedView
         Returns the User Defined View   
            
         
        """
        pass
    
    ## Setter for property: (str) UserDefinedView

    ##  Returns the User Defined View   
    ##     
    ##  
    ## Setter License requirements: None.
    ## 
    ##   <br>  Created in NX2206.0.0  <br> 

    @UserDefinedView.setter
    def UserDefinedView(self, userDefinedView: str):
        """
        Setter for property: (str) UserDefinedView
         Returns the User Defined View   
            
         
        """
        pass
    
import NXOpen
##   Represents the @link NXOpen::TDP::TemplateViewport NXOpen::TDP::TemplateViewport@endlink  object.
##      <br> To create or edit an instance of this class, use @link NXOpen::TDP::TemplateViewportBuilder  NXOpen::TDP::TemplateViewportBuilder @endlink  <br> 
## 
##   <br>  Created in NX1847.0.0  <br> 

class TemplateViewport(NXOpen.DisplayableObject): 
    """  Represents the <ja_class>NXOpen.TDP.TemplateViewport</ja_class> object.
    """
    pass


## @package NXOpen.TDP
## Classes, Enums and Structs under NXOpen.TDP namespace

##  @link ManagerAdditionalPdfResult NXOpen.TDP.ManagerAdditionalPdfResult @endlink is an alias for @link Manager.AdditionalPdfResult NXOpen.TDP.Manager.AdditionalPdfResult@endlink
ManagerAdditionalPdfResult = Manager.AdditionalPdfResult


##  @link PublisherBuilderModelAccuracyType NXOpen.TDP.PublisherBuilderModelAccuracyType @endlink is an alias for @link PublisherBuilder.ModelAccuracyType NXOpen.TDP.PublisherBuilder.ModelAccuracyType@endlink
PublisherBuilderModelAccuracyType = PublisherBuilder.ModelAccuracyType


##  @link PublisherBuilderPublishResult NXOpen.TDP.PublisherBuilderPublishResult @endlink is an alias for @link PublisherBuilder.PublishResult NXOpen.TDP.PublisherBuilder.PublishResult@endlink
PublisherBuilderPublishResult = PublisherBuilder.PublishResult


##  @link PublisherBuilderSaveToOptionType NXOpen.TDP.PublisherBuilderSaveToOptionType @endlink is an alias for @link PublisherBuilder.SaveToOptionType NXOpen.TDP.PublisherBuilder.SaveToOptionType@endlink
PublisherBuilderSaveToOptionType = PublisherBuilder.SaveToOptionType


##  @link PublisherBuilderViewSelectionType NXOpen.TDP.PublisherBuilderViewSelectionType @endlink is an alias for @link PublisherBuilder.ViewSelectionType NXOpen.TDP.PublisherBuilder.ViewSelectionType@endlink
PublisherBuilderViewSelectionType = PublisherBuilder.ViewSelectionType


##  @link TemplateAutomaticTableBuilderContentType NXOpen.TDP.TemplateAutomaticTableBuilderContentType @endlink is an alias for @link TemplateAutomaticTableBuilder.ContentType NXOpen.TDP.TemplateAutomaticTableBuilder.ContentType@endlink
TemplateAutomaticTableBuilderContentType = TemplateAutomaticTableBuilder.ContentType


##  @link TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableBomColumnType NXOpen.TDP.TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableBomColumnType @endlink is an alias for @link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType@endlink
TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableBomColumnType = TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType


##  @link TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableIcdColumnType NXOpen.TDP.TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableIcdColumnType @endlink is an alias for @link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType@endlink
TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableIcdColumnType = TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType


##  @link TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableKpiColumnType NXOpen.TDP.TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableKpiColumnType @endlink is an alias for @link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType@endlink
TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTableKpiColumnType = TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType


##  @link TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTablePadColumnType NXOpen.TDP.TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTablePadColumnType @endlink is an alias for @link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType@endlink
TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTablePadColumnType = TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType


##  @link TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTablePmiColumnType NXOpen.TDP.TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTablePmiColumnType @endlink is an alias for @link TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType NXOpen.TDP.TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType@endlink
TemplateAutomaticTableBuilderJaTdpTemplateAutomaticTablePmiColumnType = TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType


##  @link TemplateAutomaticTableBuilderKpiFilterLevel NXOpen.TDP.TemplateAutomaticTableBuilderKpiFilterLevel @endlink is an alias for @link TemplateAutomaticTableBuilder.KpiFilterLevel NXOpen.TDP.TemplateAutomaticTableBuilder.KpiFilterLevel@endlink
TemplateAutomaticTableBuilderKpiFilterLevel = TemplateAutomaticTableBuilder.KpiFilterLevel


##  @link TemplateAutomaticTableBuilderPositionType NXOpen.TDP.TemplateAutomaticTableBuilderPositionType @endlink is an alias for @link TemplateAutomaticTableBuilder.PositionType NXOpen.TDP.TemplateAutomaticTableBuilder.PositionType@endlink
TemplateAutomaticTableBuilderPositionType = TemplateAutomaticTableBuilder.PositionType


##  @link TemplateAutomaticTableBuilderScopeType NXOpen.TDP.TemplateAutomaticTableBuilderScopeType @endlink is an alias for @link TemplateAutomaticTableBuilder.ScopeType NXOpen.TDP.TemplateAutomaticTableBuilder.ScopeType@endlink
TemplateAutomaticTableBuilderScopeType = TemplateAutomaticTableBuilder.ScopeType


##  @link TemplateAutomaticTablePMIFilterBuilderFilter NXOpen.TDP.TemplateAutomaticTablePMIFilterBuilderFilter @endlink is an alias for @link TemplateAutomaticTablePMIFilterBuilder.Filter NXOpen.TDP.TemplateAutomaticTablePMIFilterBuilder.Filter@endlink
TemplateAutomaticTablePMIFilterBuilderFilter = TemplateAutomaticTablePMIFilterBuilder.Filter


##  @link TemplateEditCellBuilderTextJustificationType NXOpen.TDP.TemplateEditCellBuilderTextJustificationType @endlink is an alias for @link TemplateEditCellBuilder.TextJustificationType NXOpen.TDP.TemplateEditCellBuilder.TextJustificationType@endlink
TemplateEditCellBuilderTextJustificationType = TemplateEditCellBuilder.TextJustificationType


##  @link TemplateNoteBuilderNoteTypes NXOpen.TDP.TemplateNoteBuilderNoteTypes @endlink is an alias for @link TemplateNoteBuilder.NoteTypes NXOpen.TDP.TemplateNoteBuilder.NoteTypes@endlink
TemplateNoteBuilderNoteTypes = TemplateNoteBuilder.NoteTypes


##  @link TemplatePageBuilderEnglishSizeType NXOpen.TDP.TemplatePageBuilderEnglishSizeType @endlink is an alias for @link TemplatePageBuilder.EnglishSizeType NXOpen.TDP.TemplatePageBuilder.EnglishSizeType@endlink
TemplatePageBuilderEnglishSizeType = TemplatePageBuilder.EnglishSizeType


##  @link TemplatePageBuilderMetricSizeType NXOpen.TDP.TemplatePageBuilderMetricSizeType @endlink is an alias for @link TemplatePageBuilder.MetricSizeType NXOpen.TDP.TemplatePageBuilder.MetricSizeType@endlink
TemplatePageBuilderMetricSizeType = TemplatePageBuilder.MetricSizeType


##  @link TemplatePageBuilderOrientationType NXOpen.TDP.TemplatePageBuilderOrientationType @endlink is an alias for @link TemplatePageBuilder.OrientationType NXOpen.TDP.TemplatePageBuilder.OrientationType@endlink
TemplatePageBuilderOrientationType = TemplatePageBuilder.OrientationType


##  @link TemplatePropertiesBuilderTemplateFormatEnum NXOpen.TDP.TemplatePropertiesBuilderTemplateFormatEnum @endlink is an alias for @link TemplatePropertiesBuilder.TemplateFormatEnum NXOpen.TDP.TemplatePropertiesBuilder.TemplateFormatEnum@endlink
TemplatePropertiesBuilderTemplateFormatEnum = TemplatePropertiesBuilder.TemplateFormatEnum


##  @link TemplateViewportBuilderDefaultViewType NXOpen.TDP.TemplateViewportBuilderDefaultViewType @endlink is an alias for @link TemplateViewportBuilder.DefaultViewType NXOpen.TDP.TemplateViewportBuilder.DefaultViewType@endlink
TemplateViewportBuilderDefaultViewType = TemplateViewportBuilder.DefaultViewType


