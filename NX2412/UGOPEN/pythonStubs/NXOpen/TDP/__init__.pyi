from __future__ import annotations
from typing import overload, Tuple, List, Callable
from enum import Enum
from abc import abstractmethod
import NXOpen
class AttributesToExcludeBuilder(NXOpen.TaggedObject): 
    """ Represents attributes to exclude builder """
    def GetAttributeState(self, attributeName: str) -> bool:
        """
         Get the modified state of attributes 
         Returns attributeState (bool): .
        """
        pass
    def SetAttributeState(self, attributeName: str, attributeState: bool) -> None:
        """
         Set the modified state of attributes 
        """
        pass
import NXOpen
import NXOpen.Annotations
class Manager(NXOpen.Object): 
    """ Represents the TDP Manager class."""
    class AdditionalPdfResult(Enum):
        """
        Members Include: 
         |Success| 
         |SuccessWithMalformedAttachment| 
         |Fail| 

        """
        Success: int
        SuccessWithMalformedAttachment: int
        Fail: int
        @staticmethod
        def ValueOf(value: int) -> Manager.AdditionalPdfResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def AddAdditionalPdf(src: str, additionalPdfs: List[str], dest: str) -> Manager.AdditionalPdfResult:
        """
         This method adds additional PDF files to the end of a TDP. 
         Returns result ( Manager.AdditionalPdfResult NXOp):  final results of adding additional PDFs .
        """
        pass
    def CreateTdpPublisherBuilder(part: NXOpen.Part) -> PublisherBuilder:
        """
         Creates the TDP Publisher builder 
         Returns builder ( PublisherBuilder NXOp): .
        """
        pass
    def CreateTemplateAutomaticTableBuilder(part: NXOpen.Part, automaticTable: TemplateAutomaticTable) -> TemplateAutomaticTableBuilder:
        """
         Creates the Template Automatic Table builder 
         Returns builder ( TemplateAutomaticTableBuilder NXOp): .
        """
        pass
    def CreateTemplateDiagramareaBuilder(part: NXOpen.Part, printview: TemplateDiagramArea) -> TemplateDiagramAreaBuilder:
        """
         Creates the Template Diagram Area builder 
         Returns builder ( TemplateDiagramAreaBuilder NXOp): .
        """
        pass
    def CreateTemplateEditcellBuilder(part: NXOpen.Part, tableCell: NXOpen.DisplayableObject) -> TemplateEditCellBuilder:
        """
         Creates the Template Edit cell builder 
         Returns builder ( TemplateEditCellBuilder NXOp): .
        """
        pass
    def CreateTemplateFormFieldBuilder(part: NXOpen.Part, formFieldTag: TemplateFormField) -> TemplateFormFieldBuilder:
        """
         Creates the Template Form Field builder 
         Returns builder ( TemplateFormFieldBuilder NXOp): .
        """
        pass
    def CreateTemplateImageBuilder(part: NXOpen.Part, imageToEdit: TemplateImage) -> TemplateImageBuilder:
        """
         Creates the Template Image builder 
         Returns builder ( TemplateImageBuilder NXOp): .
        """
        pass
    def CreateTemplateNoteBuilder(part: NXOpen.Part, annotation: NXOpen.Annotations.SimpleDraftingAid) -> TemplateNoteBuilder:
        """
         Creates the Template Note builder 
         Returns builder ( TemplateNoteBuilder NXOp): .
        """
        pass
    def CreateTemplatePageBuilder(part: NXOpen.Part, pageToEdit: TemplatePage) -> TemplatePageBuilder:
        """
         Creates the Template Page builder 
         Returns builder ( TemplatePageBuilder NXOp): .
        """
        pass
    def CreateTemplatePrintViewBuilder(part: NXOpen.Part, printview: TemplatePrintView) -> TemplatePrintViewBuilder:
        """
         Creates the Template Print View builder 
         Returns builder ( TemplatePrintViewBuilder NXOp): .
        """
        pass
    def CreateTemplatePropertiesBuilder(part: NXOpen.Part) -> TemplatePropertiesBuilder:
        """
         Creates the Template Properties builder 
         Returns builder ( TemplatePropertiesBuilder NXOp): .
        """
        pass
    def CreateTemplateRectangleBuilder(part: NXOpen.Part, rectangle: TemplateRectangle) -> TemplateRectangleBuilder:
        """
         Creates the Template Rectangle builder 
         Returns builder ( TemplateRectangleBuilder NXOp): .
        """
        pass
    def CreateTemplateTableSectionBuilder(part: NXOpen.Part, tableSectionToEdit: NXOpen.Annotations.TableSection) -> TemplateTableSectionBuilder:
        """
         Creates the Template Table builder 
         Returns builder ( TemplateTableSectionBuilder NXOp): .
        """
        pass
    def CreateTemplateViewCarouselBuilder(part: NXOpen.Part, viewCarousel: TemplateViewCarousel) -> TemplateViewCarouselBuilder:
        """
         Creates the Template View Carousel builder 
         Returns builder ( TemplateViewCarouselBuilder NXOp): .
        """
        pass
    def CreateTemplateViewListBuilder(part: NXOpen.Part, viewlist: TemplateViewList) -> TemplateViewListBuilder:
        """
         Creates the Template View List builder 
         Returns builder ( TemplateViewListBuilder NXOp): .
        """
        pass
    def CreateTemplateViewportBuilder(part: NXOpen.Part, viewport: TemplateViewport) -> TemplateViewportBuilder:
        """
         Creates the Template Viewport builder 
         Returns builder ( TemplateViewportBuilder NXOp): .
        """
        pass
    def Lock(templateObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Locks the specified template objects. 
        """
        pass
    def SetObjectOrigin(objectTag: NXOpen.DisplayableObject, objOrigin: NXOpen.Point3d) -> None:
        """
         Set origin to the given template displayable object 
        """
        pass
    def SetPageOrder(part: NXOpen.Part, pageObjects: List[TemplatePage]) -> None:
        """
         Set page order and updates page numbers. 
        """
        pass
    def Unlock(templateObjects: List[NXOpen.DisplayableObject]) -> None:
        """
         Unlocks the specified template objects. 
        """
        pass
import NXOpen
class PublisherBuilder(NXOpen.Builder): 
    """ 
        This builder is used to publish Technical Data Package, or TDP for short.
        It collects all the necessary inputs from a TDP template and other user options
        before publishing TDP.
    """
    class ModelAccuracyType(Enum):
        """
        Members Include: 
         |Maximum| 
         |High| 
         |Medium| 
         |Low| 

        """
        Maximum: int
        High: int
        Medium: int
        Low: int
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.ModelAccuracyType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PublishResult(Enum):
        """
        Members Include: 
         |Success| 
         |SuccessWithInconsistency| 
         |SuccessWithError| 
         |Fail| 

        """
        Success: int
        SuccessWithInconsistency: int
        SuccessWithError: int
        Fail: int
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.PublishResult:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class SaveToOptionType(Enum):
        """
        Members Include: 
         |Teamcenter| 
         |OperatingSystem| 

        """
        Teamcenter: int
        OperatingSystem: int
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.SaveToOptionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ViewSelectionType(Enum):
        """
        Members Include: 
         |SelectedViews| 
         |AllDisclosedViews| 
         |AllUserDefinedViews| 
         |AllViews| 
         |AllSectionViews| 

        """
        SelectedViews: int
        AllDisclosedViews: int
        AllUserDefinedViews: int
        AllViews: int
        AllSectionViews: int
        @staticmethod
        def ValueOf(value: int) -> PublisherBuilder.ViewSelectionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def AttachSVG(self) -> bool:
        """
        Getter for property: (bool) AttachSVG
         Returns 
                    the flag whether to attach SVG to the PDF or not.  
          
                  
         
        """
        pass
    @AttachSVG.setter
    def AttachSVG(self, attachSVG: bool):
        """
        Setter for property: (bool) AttachSVG
         Returns 
                    the flag whether to attach SVG to the PDF or not.  
          
                  
         
        """
        pass
    @property
    def AttributesToExclude(self) -> AttributesToExcludeBuilder:
        """
        Getter for property: ( AttributesToExcludeBuilder NXOp) AttributesToExclude
         Returns
                the attributes to exclude builder, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @property
    def BackgroundColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) BackgroundColor
         Returns
                the Background color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @BackgroundColor.setter
    def BackgroundColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) BackgroundColor
         Returns
                the Background color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @property
    def Compression(self) -> bool:
        """
        Getter for property: (bool) Compression
         Returns 
                    the flag whether to use lossy compression for 3D PDF model, 
                    if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @Compression.setter
    def Compression(self, compression: bool):
        """
        Setter for property: (bool) Compression
         Returns 
                    the flag whether to use lossy compression for 3D PDF model, 
                    if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @property
    def ModelAccuracy(self) -> PublisherBuilder.ModelAccuracyType:
        """
        Getter for property: ( PublisherBuilder.ModelAccuracyType NXOp) ModelAccuracy
         Returns 
                    the 3D PDF model accuracy, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @ModelAccuracy.setter
    def ModelAccuracy(self, modelAccuracy: PublisherBuilder.ModelAccuracyType):
        """
        Setter for property: ( PublisherBuilder.ModelAccuracyType NXOp) ModelAccuracy
         Returns 
                    the 3D PDF model accuracy, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @property
    def OutputFilename(self) -> str:
        """
        Getter for property: (str) OutputFilename
         Returns the output filename for the TDP   
            
         
        """
        pass
    @OutputFilename.setter
    def OutputFilename(self, filename: str):
        """
        Setter for property: (str) OutputFilename
         Returns the output filename for the TDP   
            
         
        """
        pass
    @property
    def OverrideColors(self) -> bool:
        """
        Getter for property: (bool) OverrideColors
         Returns
                the flag whether to override ViewPort Background and PMI color,
                in case of publishing to 3D PDF
                  
            
         
        """
        pass
    @OverrideColors.setter
    def OverrideColors(self, overrideColors: bool):
        """
        Setter for property: (bool) OverrideColors
         Returns
                the flag whether to override ViewPort Background and PMI color,
                in case of publishing to 3D PDF
                  
            
         
        """
        pass
    @property
    def PmiColor(self) -> NXOpen.NXColor:
        """
        Getter for property: ( NXOpen.NXColor) PmiColor
         Returns
                the PMI color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @PmiColor.setter
    def PmiColor(self, color: NXOpen.NXColor):
        """
        Setter for property: ( NXOpen.NXColor) PmiColor
         Returns
                the PMI color, if the template to be published is a 3D PDF template
                  
            
         
        """
        pass
    @property
    def SaveToOption(self) -> PublisherBuilder.SaveToOptionType:
        """
        Getter for property: ( PublisherBuilder.SaveToOptionType NXOp) SaveToOption
         Returns 
                    the save-to option, if the part to be published is in managed mode
                  
            
         
        """
        pass
    @SaveToOption.setter
    def SaveToOption(self, saveToOption: PublisherBuilder.SaveToOptionType):
        """
        Setter for property: ( PublisherBuilder.SaveToOptionType NXOp) SaveToOption
         Returns 
                    the save-to option, if the part to be published is in managed mode
                  
            
         
        """
        pass
    @property
    def SelectedViews(self) -> NXOpen.SelectViewList:
        """
        Getter for property: ( NXOpen.SelectViewList) SelectedViews
         Returns 
                    the selected views to publish TDP for, if the view selection method is set to 
                     NXOpen::TDP::PublisherBuilder::ViewSelectionTypeSelectedViews 
                  
            
         
        """
        pass
    @property
    def UsePassword(self) -> bool:
        """
        Getter for property: (bool) UsePassword
         Returns the flag whether to use password or not   
            
         
        """
        pass
    @UsePassword.setter
    def UsePassword(self, usePassword: bool):
        """
        Setter for property: (bool) UsePassword
         Returns the flag whether to use password or not   
            
         
        """
        pass
    @property
    def ViewSelection(self) -> PublisherBuilder.ViewSelectionType:
        """
        Getter for property: ( PublisherBuilder.ViewSelectionType NXOp) ViewSelection
         Returns the view selection method   
            
         
        """
        pass
    @ViewSelection.setter
    def ViewSelection(self, viewSelection: PublisherBuilder.ViewSelectionType):
        """
        Setter for property: ( PublisherBuilder.ViewSelectionType NXOp) ViewSelection
         Returns the view selection method   
            
         
        """
        pass
    def AddAttachment(self, filename: str) -> None:
        """
         This method adds the new attachment filename to the end of the attachment list.
        """
        pass
    def DeleteAttachmentAtIndices(self, indices: List[int]) -> None:
        """
         
                    This method deletes the attachment filenames at the indicated indices 
                    and re-populate the attachment filename list with new continuous indices. 
                
        """
        pass
    def GetAttachments(self) -> List[str]:
        """
         This method returns the list of attachment filenames 
         Returns attachments (List[str]): .
        """
        pass
    def GetTextLabels(self) -> List[str]:
        """
         This method returns the list of text labels.
         Returns labels (List[str]): .
        """
        pass
    def GetTextValueOfLabel(self, label: str) -> Tuple[bool, str]:
        """
         This method returns the value of the text with the given label, if the text exists.
         Returns A tuple consisting of (exists, value). 
         - exists is: bool.
         - value is: str.

        """
        pass
    def GetViewportLabels(self) -> List[str]:
        """
         This method returns the list of viewport labels.
         Returns labels (List[str]): .
        """
        pass
    def GetWorkTemplateFilename(self) -> str:
        """
         This method returns the name of the template file that is being worked on.
         Returns templateFilename (str): .
        """
        pass
    def HasTextOfLabel(self, label: str) -> bool:
        """
         This method checks to see if a text with the given label exists for the selected template.
         Returns exists (bool): .
        """
        pass
    def HasViewportOfLabel(self, label: str) -> bool:
        """
         This method checks to see if a viewport with the given label exists for the selected template.
         Returns exists (bool): .
        """
        pass
    def Publish(self) -> PublisherBuilder.PublishResult:
        """
         This method publishes the TDP with builder's data.
         Returns result ( PublisherBuilder.PublishResult NXOp): .
        """
        pass
    def SetPassword(self, password: str) -> None:
        """
         This method sets the password.
        """
        pass
    def SetTextValueOfLabel(self, label: str, value: str) -> bool:
        """
         This method sets the value of the text with the given label, if the text exists.
         Returns exists (bool): .
        """
        pass
    def SetViewPortViewValueOfViewPortLabel(self, label: str, value: str) -> bool:
        """
         This method sets the value of the viewport view with the given label, if the viewport exists.
         Returns exists (bool): .
        """
        pass
    def SetWorkTemplateFile(self, templateFilename: str) -> None:
        """
         This method sets the template to publish TDP and repopulates the text table.
        """
        pass
import NXOpen
class TemplateAutomaticTableBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Automatic Table Builder """
    class ContentType(Enum):
        """
        Members Include: 
         |Bom|  Bill Of Materials Table 
         |Pmi|  PMI Table 
         |View| 
         |Icd|  ICD Table 
         |Pad|  PAD Table 
         |Kpi|  KPI Table 

        """
        Bom: int
        Pmi: int
        View: int
        Icd: int
        Pad: int
        Kpi: int
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.ContentType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaTdpTemplateAutomaticTableBomColumnType(Enum):
        """
        Members Include: 
         |Index| 
         |PartName| 
         |Quantity| 
         |Attribute| 

        """
        Index: int
        PartName: int
        Quantity: int
        Attribute: int
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaTdpTemplateAutomaticTableIcdColumnType(Enum):
        """
        Members Include: 
         |Index| 
         |Components| 
         |AssemblyConstraints| 
         |ElectricalRouting| 
         |InterPartExpressions| 
         |InterPartMeasurements| 
         |Join| 
         |MechanicalRouting| 
         |WaveLinks| 
         |Welds| 
         |Attribute| 

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
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaTdpTemplateAutomaticTableKpiColumnType(Enum):
        """
        Members Include: 
         |Name| 
         |Value| 
         |Formula| 
         |Type| 
         |Description| 
         |Source| 
         |SourceDetails| 
         |Result| 
         |ValueType| 
         |PartName| 
         |Attribute| 

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
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaTdpTemplateAutomaticTablePadColumnType(Enum):
        """
        Members Include: 
         |Index| 
         |Components| 
         |AssemblyConstraints| 
         |ElectricalRouting| 
         |InterPartExpressions| 
         |InterPartMeasurements| 
         |Join| 
         |MechanicalRouting| 
         |WaveLinks| 
         |Welds| 
         |Attribute| 

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
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class JaTdpTemplateAutomaticTablePmiColumnType(Enum):
        """
        Members Include: 
         |Index| 
         |PmiName| 
         |Value| 
         |Attribute| 
         |PmiType| 
         |PmiId| 

        """
        Index: int
        PmiName: int
        Value: int
        Attribute: int
        PmiType: int
        PmiId: int
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class KpiFilterLevel(Enum):
        """
        Members Include: 
         |Part| 
         |ProductInterface| 
         |Expression| 
         |Check| 
         |PartOccurence| 
         |CombinedView| 

        """
        Part: int
        ProductInterface: int
        Expression: int
        Check: int
        PartOccurence: int
        CombinedView: int
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.KpiFilterLevel:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class PositionType(Enum):
        """
        Members Include: 
         |NotSet|  Not placed in 3D PDF 
         |Above|  Placed above the PMI table in 3D PDF 
         |Below|  Placed below the PMI table in 3D PDF 

        """
        NotSet: int
        Above: int
        Below: int
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.PositionType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class ScopeType(Enum):
        """
        Members Include: 
         |AllLevels|  Assemblies and Sub Assemblies placed in 3D PDF 
         |TopLevelOnly|  Placed Top Level Assembly in 3D PDF 
         |ComponentsOnly|  Placed Leaf level component in 3D PDF 

        """
        AllLevels: int
        TopLevelOnly: int
        ComponentsOnly: int
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTableBuilder.ScopeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def BomScope(self) -> TemplateAutomaticTableBuilder.ScopeType:
        """
        Getter for property: ( TemplateAutomaticTableBuilder.ScopeType NXOp) BomScope
         Returns the bom scope type   
            
         
        """
        pass
    @BomScope.setter
    def BomScope(self, scope: TemplateAutomaticTableBuilder.ScopeType):
        """
        Setter for property: ( TemplateAutomaticTableBuilder.ScopeType NXOp) BomScope
         Returns the bom scope type   
            
         
        """
        pass
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    @property
    def Contents(self) -> TemplateAutomaticTableBuilder.ContentType:
        """
        Getter for property: ( TemplateAutomaticTableBuilder.ContentType NXOp) Contents
         Returns the content   
            
         
        """
        pass
    @Contents.setter
    def Contents(self, content: TemplateAutomaticTableBuilder.ContentType):
        """
        Setter for property: ( TemplateAutomaticTableBuilder.ContentType NXOp) Contents
         Returns the content   
            
         
        """
        pass
    @property
    def DecimalPlaces(self) -> int:
        """
        Getter for property: (int) DecimalPlaces
         Returns the decimal place value   
            
         
        """
        pass
    @DecimalPlaces.setter
    def DecimalPlaces(self, decimalPlaces: int):
        """
        Setter for property: (int) DecimalPlaces
         Returns the decimal place value   
            
         
        """
        pass
    @property
    def FilterLevel(self) -> TemplateAutomaticTableBuilder.KpiFilterLevel:
        """
        Getter for property: ( TemplateAutomaticTableBuilder.KpiFilterLevel NXOp) FilterLevel
         Returns the filter level type   
            
         
        """
        pass
    @FilterLevel.setter
    def FilterLevel(self, filterLevel: TemplateAutomaticTableBuilder.KpiFilterLevel):
        """
        Setter for property: ( TemplateAutomaticTableBuilder.KpiFilterLevel NXOp) FilterLevel
         Returns the filter level type   
            
         
        """
        pass
    @property
    def MaintainBomAssemOrder(self) -> bool:
        """
        Getter for property: (bool) MaintainBomAssemOrder
         Returns the maintain bom assembly order toggle   
            
         
        """
        pass
    @MaintainBomAssemOrder.setter
    def MaintainBomAssemOrder(self, maintainBomAssemOrder: bool):
        """
        Setter for property: (bool) MaintainBomAssemOrder
         Returns the maintain bom assembly order toggle   
            
         
        """
        pass
    @property
    def PmiFilter(self) -> TemplateAutomaticTablePMIFilterBuilder:
        """
        Getter for property: ( TemplateAutomaticTablePMIFilterBuilder NXOp) PmiFilter
         Returns the PMI Filter   
            
         
        """
        pass
    @property
    def PmiFilterPos(self) -> TemplateAutomaticTableBuilder.PositionType:
        """
        Getter for property: ( TemplateAutomaticTableBuilder.PositionType NXOp) PmiFilterPos
         Returns the pmi Filter position   
            
         
        """
        pass
    @PmiFilterPos.setter
    def PmiFilterPos(self, position: TemplateAutomaticTableBuilder.PositionType):
        """
        Setter for property: ( TemplateAutomaticTableBuilder.PositionType NXOp) PmiFilterPos
         Returns the pmi Filter position   
            
         
        """
        pass
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    @property
    def ShowCheckedOnly(self) -> bool:
        """
        Getter for property: (bool) ShowCheckedOnly
         Returns the show checked only result toggle   
            
         
        """
        pass
    @ShowCheckedOnly.setter
    def ShowCheckedOnly(self, showCheckedOnly: bool):
        """
        Setter for property: (bool) ShowCheckedOnly
         Returns the show checked only result toggle   
            
         
        """
        pass
    @property
    def ShowFailed(self) -> bool:
        """
        Getter for property: (bool) ShowFailed
         Returns the show failed result toggle   
            
         
        """
        pass
    @ShowFailed.setter
    def ShowFailed(self, showFailed: bool):
        """
        Setter for property: (bool) ShowFailed
         Returns the show failed result toggle   
            
         
        """
        pass
    @property
    def ShowPassed(self) -> bool:
        """
        Getter for property: (bool) ShowPassed
         Returns the show passed result toggle   
            
         
        """
        pass
    @ShowPassed.setter
    def ShowPassed(self, showPassed: bool):
        """
        Setter for property: (bool) ShowPassed
         Returns the show passed result toggle   
            
         
        """
        pass
    @property
    def ShowPassedWithInfo(self) -> bool:
        """
        Getter for property: (bool) ShowPassedWithInfo
         Returns the show passed with information result toggle   
            
         
        """
        pass
    @ShowPassedWithInfo.setter
    def ShowPassedWithInfo(self, showPassedWithInfo: bool):
        """
        Setter for property: (bool) ShowPassedWithInfo
         Returns the show passed with information result toggle   
            
         
        """
        pass
    @property
    def ShowPassedWithWarning(self) -> bool:
        """
        Getter for property: (bool) ShowPassedWithWarning
         Returns the show passed with warning result toggle   
            
         
        """
        pass
    @ShowPassedWithWarning.setter
    def ShowPassedWithWarning(self, showPassedWithWarning: bool):
        """
        Setter for property: (bool) ShowPassedWithWarning
         Returns the show passed with warning result toggle   
            
         
        """
        pass
    @property
    def ShowPhysicalParameter(self) -> bool:
        """
        Getter for property: (bool) ShowPhysicalParameter
         Returns the show physical parameters result toggle   
            
         
        """
        pass
    @ShowPhysicalParameter.setter
    def ShowPhysicalParameter(self, showPhysicalParameters: bool):
        """
        Setter for property: (bool) ShowPhysicalParameter
         Returns the show physical parameters result toggle   
            
         
        """
        pass
    @property
    def ShowPhysicalParametersFolder(self) -> bool:
        """
        Getter for property: (bool) ShowPhysicalParametersFolder
         Returns the show physical parameters folder result toggle   
            
         
        """
        pass
    @ShowPhysicalParametersFolder.setter
    def ShowPhysicalParametersFolder(self, showPhysicalParametersFolder: bool):
        """
        Setter for property: (bool) ShowPhysicalParametersFolder
         Returns the show physical parameters folder result toggle   
            
         
        """
        pass
    @property
    def ShowProductInterfaces(self) -> bool:
        """
        Getter for property: (bool) ShowProductInterfaces
         Returns the show product interface toggle   
            
         
        """
        pass
    @ShowProductInterfaces.setter
    def ShowProductInterfaces(self, showProductInterfaces: bool):
        """
        Setter for property: (bool) ShowProductInterfaces
         Returns the show product interface toggle   
            
         
        """
        pass
    @property
    def ShowSuppressed(self) -> bool:
        """
        Getter for property: (bool) ShowSuppressed
         Returns the show suppressed result toggle   
            
         
        """
        pass
    @ShowSuppressed.setter
    def ShowSuppressed(self, showSuppressed: bool):
        """
        Setter for property: (bool) ShowSuppressed
         Returns the show suppressed result toggle   
            
         
        """
        pass
    @property
    def ShowUnusedCheckedExps(self) -> bool:
        """
        Getter for property: (bool) ShowUnusedCheckedExps
         Returns the show unused check expression toggle   
            
         
        """
        pass
    @ShowUnusedCheckedExps.setter
    def ShowUnusedCheckedExps(self, showUnusedCheckedExps: bool):
        """
        Setter for property: (bool) ShowUnusedCheckedExps
         Returns the show unused check expression toggle   
            
         
        """
        pass
    @property
    def ShowUnusedExpCheckFolder(self) -> bool:
        """
        Getter for property: (bool) ShowUnusedExpCheckFolder
         Returns the show unused expression check folder result toggle   
            
         
        """
        pass
    @ShowUnusedExpCheckFolder.setter
    def ShowUnusedExpCheckFolder(self, showUnusedExpCheckFolder: bool):
        """
        Setter for property: (bool) ShowUnusedExpCheckFolder
         Returns the show unused expression check folder result toggle   
            
         
        """
        pass
    @property
    def ShowUnvalidatedReqFolder(self) -> bool:
        """
        Getter for property: (bool) ShowUnvalidatedReqFolder
         Returns the show unvalidated requirements folder result toggle   
            
         
        """
        pass
    @ShowUnvalidatedReqFolder.setter
    def ShowUnvalidatedReqFolder(self, showUnvalidatedReqFolder: bool):
        """
        Setter for property: (bool) ShowUnvalidatedReqFolder
         Returns the show unvalidated requirements folder result toggle   
            
         
        """
        pass
    @property
    def ShowUnvalidatedReqs(self) -> bool:
        """
        Getter for property: (bool) ShowUnvalidatedReqs
         Returns the show unvalidated requirements toggle   
            
         
        """
        pass
    @ShowUnvalidatedReqs.setter
    def ShowUnvalidatedReqs(self, showUnvalidatedReqs: bool):
        """
        Setter for property: (bool) ShowUnvalidatedReqs
         Returns the show unvalidated requirements toggle   
            
         
        """
        pass
    @property
    def ShowWorkPartOnly(self) -> bool:
        """
        Getter for property: (bool) ShowWorkPartOnly
         Returns the show work part only result toggle   
            
         
        """
        pass
    @ShowWorkPartOnly.setter
    def ShowWorkPartOnly(self, showWorkPartOnly: bool):
        """
        Setter for property: (bool) ShowWorkPartOnly
         Returns the show work part only result toggle   
            
         
        """
        pass
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextCfw
         Returns the font, and width of Automatic table text   
            
         
        """
        pass
    @property
    def ZoomToPmiPos(self) -> TemplateAutomaticTableBuilder.PositionType:
        """
        Getter for property: ( TemplateAutomaticTableBuilder.PositionType NXOp) ZoomToPmiPos
         Returns the Zoom To PMI position   
            
         
        """
        pass
    @ZoomToPmiPos.setter
    def ZoomToPmiPos(self, position: TemplateAutomaticTableBuilder.PositionType):
        """
        Setter for property: ( TemplateAutomaticTableBuilder.PositionType NXOp) ZoomToPmiPos
         Returns the Zoom To PMI position   
            
         
        """
        pass
    def AddColumn(self) -> bool:
        """
         To add the row in the table
         Returns exists (bool): .
        """
        pass
    def DeleteColumn(self, index: int) -> bool:
        """
         To delete the row in the table
         Returns exists (bool): .
        """
        pass
    def SetICDColumnType(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableIcdColumnType) -> bool:
        """
         To modify the ICD column type in the table
         Returns exists (bool): .
        """
        pass
    def SetKPIColumnType(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableKpiColumnType) -> bool:
        """
         To modify the KPI column type in the table
         Returns exists (bool): .
        """
        pass
    def SetPADColumnType(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePadColumnType) -> bool:
        """
         To modify the PAD column type in the table
         Returns exists (bool): .
        """
        pass
    def SwapColumns(self, index1: int, index2: int, length: int) -> bool:
        """
         To swap the columns in the table
         Returns exists (bool): .
        """
        pass
    def UpdateAttribute(self, rowIndex: int, value: str) -> bool:
        """
         To modify the Attribute name in the table
         Returns exists (bool): .
        """
        pass
    def UpdateBomColumn(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTableBomColumnType) -> bool:
        """
         To modify the Bom column type in the table
         Returns exists (bool): .
        """
        pass
    def UpdateHeader(self, rowIndex: int, value: str) -> bool:
        """
         To modify the header column in table
         Returns exists (bool): .
        """
        pass
    def UpdatePmiColumn(self, rowIndex: int, colType: TemplateAutomaticTableBuilder.JaTdpTemplateAutomaticTablePmiColumnType) -> bool:
        """
         To modify the Pmi column type in the table
         Returns exists (bool): .
        """
        pass
    def UpdateWidth(self, rowIndex: int, value: float) -> bool:
        """
         To modify the Width value in the table
         Returns exists (bool): .
        """
        pass
import NXOpen
class TemplateAutomaticTablePMIFilterBuilder(NXOpen.TaggedObject): 
    """ Represents a Template Automatic Table PMIFilter Builder """
    class Filter(Enum):
        """
        Members Include: 
         |Dimension|  Dimension PMI Filter        
         |AnnotationNote|  Annotation Notes PMI Filter        
         |AnnotationFCF|  Annotation Feature Control Frame PMI Filter        
         |AnnotationDatumFeature|  Annotation Datum Feature PMI Filter        
         |AnnotationSurfaceFinish|  Annotation Surface Finish PMI Filter        
         |AnnotationDatumTarget|  Annotation Datum Target PMI Filter        
         |AnnotationWeldSymbol|  Annotation Weld Symbol PMI Filter        
         |AnnotationBalloon|  Annotation Balloon PMI Filter        
         |AnnotationSpecialtyNote|  Annotation Speciality Notes PMI Filter        
         |Table|  Table PMI Filter     
         |CustomSymbol|  Custom Symbol PMI Filter     
         |Centerline|  Centerline PMI Report Filter 
         |Region|  Region PMI Report Filter     
         |SecurityMarking|  Security Marking PMI Filter     
         |CuttingPlaneSymbol|  Cutting Plane Symbol PMI Filter     
         |AnnotationEdgeConditionSymbol|  Annotation Edge Condition Symbol PMI Filter        

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
        @staticmethod
        def ValueOf(value: int) -> TemplateAutomaticTablePMIFilterBuilder.Filter:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    def GetPmiFilterStatus(self, pmiFilterType: TemplateAutomaticTablePMIFilterBuilder.Filter) -> bool:
        """
         Returns PMI filter status 
         Returns pmiFilterStatus (bool): .
        """
        pass
    def SetPmiFilterStatus(self, pmiFilterType: TemplateAutomaticTablePMIFilterBuilder.Filter, pmiFilterStatus: bool) -> None:
        """
         Sets PMI filter status 
        """
        pass
import NXOpen
class TemplateAutomaticTable(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateAutomaticTable object.
    """
    pass
import NXOpen
class TemplateBaseRectangleBuilder(NXOpen.Builder): 
    """ Represents a Template Base Rectangle Builder """
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the height   
            
         
        """
        pass
    @Height.setter
    def Height(self, height: float):
        """
        Setter for property: (float) Height
         Returns the height   
            
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the length   
            
         
        """
        pass
    @Length.setter
    def Length(self, length: float):
        """
        Setter for property: (float) Length
         Returns the length   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Point3d:
        """
        Getter for property: ( NXOpen.Point3d) Origin
         Returns the origin   
            
         
        """
        pass
    @Origin.setter
    def Origin(self, origin: NXOpen.Point3d):
        """
        Setter for property: ( NXOpen.Point3d) Origin
         Returns the origin   
            
         
        """
        pass
import NXOpen
class TemplateDiagramAreaBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template DiagramArea Builder """
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
import NXOpen
class TemplateDiagramArea(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateDiagramArea object.
    """
    pass
import NXOpen
import NXOpen.Annotations
class TemplateEditCellBuilder(NXOpen.Builder): 
    """ Represents a Edit Cell builder """
    class TextJustificationType(Enum):
        """
        Members Include: 
         |Left| 
         |Center| 
         |Right| 

        """
        Left: int
        Center: int
        Right: int
        @staticmethod
        def ValueOf(value: int) -> TemplateEditCellBuilder.TextJustificationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Text(self) -> NXOpen.Annotations.TextWithEditControlsBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TextWithEditControlsBuilder) Text
         Returns the text   
            
         
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
    def TextHeight(self) -> float:
        """
        Getter for property: (float) TextHeight
         Returns the height of the cell   
            
         
        """
        pass
    @TextHeight.setter
    def TextHeight(self, height: float):
        """
        Setter for property: (float) TextHeight
         Returns the height of the cell   
            
         
        """
        pass
    @property
    def TextJustification(self) -> TemplateEditCellBuilder.TextJustificationType:
        """
        Getter for property: ( TemplateEditCellBuilder.TextJustificationType NXOp) TextJustification
         Returns the text alignment of the cell   
            
         
        """
        pass
    @TextJustification.setter
    def TextJustification(self, alignment: TemplateEditCellBuilder.TextJustificationType):
        """
        Setter for property: ( TemplateEditCellBuilder.TextJustificationType NXOp) TextJustification
         Returns the text alignment of the cell   
            
         
        """
        pass
import NXOpen
class TemplateFormFieldBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Form Field Builder """
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the placeholder text used to identify the Form Field in the TDP Template environment  
            
         
        """
        pass
    @Label.setter
    def Label(self, labelText: str):
        """
        Setter for property: (str) Label
         Returns the placeholder text used to identify the Form Field in the TDP Template environment  
            
         
        """
        pass
    @property
    def LabelHeight(self) -> float:
        """
        Getter for property: (float) LabelHeight
         Returns the label text height   
            
         
        """
        pass
    @LabelHeight.setter
    def LabelHeight(self, height: float):
        """
        Setter for property: (float) LabelHeight
         Returns the label text height   
            
         
        """
        pass
    @property
    def LineCfw(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) LineCfw
         Returns the color and width of the Form Field lines   
            
         
        """
        pass
    @property
    def ShowLabel(self) -> bool:
        """
        Getter for property: (bool) ShowLabel
         Returns the Display in Published PDF    
            
         
        """
        pass
    @ShowLabel.setter
    def ShowLabel(self, showLabel: bool):
        """
        Setter for property: (bool) ShowLabel
         Returns the Display in Published PDF    
            
         
        """
        pass
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextCfw
         Returns the color, font, and width of the Form Field text   
            
         
        """
        pass
import NXOpen
class TemplateFormField(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateFormField object. """
    pass
import NXOpen.Display
class TemplateImageBuilder(NXOpen.Display.ImageBaseBuilder): 
    """ Represents a Template Image Builder """
    pass
import NXOpen.Display
class TemplateImage(NXOpen.Display.ImageBase): 
    """  Represents the NXOpen.TDP.TemplateImage object.
    """
    pass
import NXOpen.Annotations
class TemplateNoteBuilder(NXOpen.Annotations.DraftingNoteBuilder): 
    """ Represents a TDP Template Note builder used to create Notes in the Template environment"""
    class NoteTypes(Enum):
        """
        Members Include: 
         |Static| 
         |Userdefined| 
         |Controlled| 

        """
        Static: int
        Userdefined: int
        Controlled: int
        @staticmethod
        def ValueOf(value: int) -> TemplateNoteBuilder.NoteTypes:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label used to identify the Note in Publish   
            
         
        """
        pass
    @Label.setter
    def Label(self, labelText: str):
        """
        Setter for property: (str) Label
         Returns the label used to identify the Note in Publish   
            
         
        """
        pass
    @property
    def NoteType(self) -> TemplateNoteBuilder.NoteTypes:
        """
        Getter for property: ( TemplateNoteBuilder.NoteTypes NXOp) NoteType
         Returns the template note type   
            
         
        """
        pass
    @NoteType.setter
    def NoteType(self, textType: TemplateNoteBuilder.NoteTypes):
        """
        Setter for property: ( TemplateNoteBuilder.NoteTypes NXOp) NoteType
         Returns the template note type   
            
         
        """
        pass
import NXOpen
class TemplatePageBuilder(NXOpen.Builder): 
    """ Represents a TDP.TemplatePage builder """
    class EnglishSizeType(Enum):
        """
        Members Include: 
         |A| 
         |B| 
         |C| 
         |D| 
         |E| 
         |F| 
         |H| 
         |J| 
         |Custom| 

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
        @staticmethod
        def ValueOf(value: int) -> TemplatePageBuilder.EnglishSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class MetricSizeType(Enum):
        """
        Members Include: 
         |A0| 
         |A1| 
         |A2| 
         |A3| 
         |A4| 
         |Custom| 

        """
        A0: int
        A1: int
        A2: int
        A3: int
        A4: int
        Custom: int
        @staticmethod
        def ValueOf(value: int) -> TemplatePageBuilder.MetricSizeType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    class OrientationType(Enum):
        """
        Members Include: 
         |Landscape| 
         |Portrait| 

        """
        Landscape: int
        Portrait: int
        @staticmethod
        def ValueOf(value: int) -> TemplatePageBuilder.OrientationType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def Height(self) -> float:
        """
        Getter for property: (float) Height
         Returns the custom or standard height for the page   
            
         
        """
        pass
    @Height.setter
    def Height(self, customHeight: float):
        """
        Setter for property: (float) Height
         Returns the custom or standard height for the page   
            
         
        """
        pass
    @property
    def Length(self) -> float:
        """
        Getter for property: (float) Length
         Returns the custom or standard length to be used for the page to be created or edited.  
             
         
        """
        pass
    @Length.setter
    def Length(self, customLength: float):
        """
        Setter for property: (float) Length
         Returns the custom or standard length to be used for the page to be created or edited.  
             
         
        """
        pass
    @property
    def Orientation(self) -> TemplatePageBuilder.OrientationType:
        """
        Getter for property: ( TemplatePageBuilder.OrientationType NXOp) Orientation
         Returns the orientation   
            
         
        """
        pass
    @Orientation.setter
    def Orientation(self, orientation: TemplatePageBuilder.OrientationType):
        """
        Setter for property: ( TemplatePageBuilder.OrientationType NXOp) Orientation
         Returns the orientation   
            
         
        """
        pass
    @property
    def PageName(self) -> str:
        """
        Getter for property: (str) PageName
         Returns the Page Name text   
            
         
        """
        pass
    @PageName.setter
    def PageName(self, pageName: str):
        """
        Setter for property: (str) PageName
         Returns the Page Name text   
            
         
        """
        pass
    @property
    def ShowPageNumber(self) -> bool:
        """
        Getter for property: (bool) ShowPageNumber
         Returns the show Page number   
            
         
        """
        pass
    @ShowPageNumber.setter
    def ShowPageNumber(self, showPageNumber: bool):
        """
        Setter for property: (bool) ShowPageNumber
         Returns the show Page number   
            
         
        """
        pass
    @property
    def StandardEnglishSize(self) -> TemplatePageBuilder.EnglishSizeType:
        """
        Getter for property: ( TemplatePageBuilder.EnglishSizeType NXOp) StandardEnglishSize
         Returns the standard english size to be used for the page to be created or edited.  
             
         
        """
        pass
    @StandardEnglishSize.setter
    def StandardEnglishSize(self, englishSize: TemplatePageBuilder.EnglishSizeType):
        """
        Setter for property: ( TemplatePageBuilder.EnglishSizeType NXOp) StandardEnglishSize
         Returns the standard english size to be used for the page to be created or edited.  
             
         
        """
        pass
    @property
    def StandardMetricSize(self) -> TemplatePageBuilder.MetricSizeType:
        """
        Getter for property: ( TemplatePageBuilder.MetricSizeType NXOp) StandardMetricSize
         Returns the standard metric size to be used for the page to be created or edited.  
             
         
        """
        pass
    @StandardMetricSize.setter
    def StandardMetricSize(self, metricSize: TemplatePageBuilder.MetricSizeType):
        """
        Setter for property: ( TemplatePageBuilder.MetricSizeType NXOp) StandardMetricSize
         Returns the standard metric size to be used for the page to be created or edited.  
             
         
        """
        pass
import NXOpen
class TemplatePage(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplatePage object.
    """
    def Activate(self) -> bool:
        """
         Activates the page so that it displays in the graphics area. 
                
                An update is performed as part of activating page. 
                
         Returns result (bool):  True if page was activated, false otherwise .
        """
        pass
import NXOpen
class TemplatePrintViewBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template PrintView Builder """
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    @property
    def SelectViewport(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectViewport
         Returns the selected viewport   
            
         
        """
        pass
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextCfw
         Returns the color, font, and width of the Print View text   
            
         
        """
        pass
import NXOpen
class TemplatePrintView(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplatePrintView object.
    """
    pass
import NXOpen
class TemplatePropertiesBuilder(NXOpen.Builder): 
    """ Represents a Template Properties Builder """
    class TemplateFormatEnum(Enum):
        """
        Members Include: 
         |Format3DPDF|  3D PDF format 
         |FormatJTplusPDF|  JT plus PDF format 

        """
        Format3DPDF: int
        FormatJTplusPDF: int
        @staticmethod
        def ValueOf(value: int) -> TemplatePropertiesBuilder.TemplateFormatEnum:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def PresentationName(self) -> str:
        """
        Getter for property: (str) PresentationName
         Returns the presentation name   
            
         
        """
        pass
    @PresentationName.setter
    def PresentationName(self, presentationName: str):
        """
        Setter for property: (str) PresentationName
         Returns the presentation name   
            
         
        """
        pass
    @property
    def TemplateFormat(self) -> TemplatePropertiesBuilder.TemplateFormatEnum:
        """
        Getter for property: ( TemplatePropertiesBuilder.TemplateFormatEnum NXOp) TemplateFormat
         Returns the template format   
            
         
        """
        pass
    @TemplateFormat.setter
    def TemplateFormat(self, templateFormat: TemplatePropertiesBuilder.TemplateFormatEnum):
        """
        Setter for property: ( TemplatePropertiesBuilder.TemplateFormatEnum NXOp) TemplateFormat
         Returns the template format   
            
         
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
class TemplateRectangleBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Rectangle Builder """
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ColorWidth
         Returns the color and width   
            
         
        """
        pass
import NXOpen
class TemplateRectangle(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateRectangle object.
    """
    pass
import NXOpen
import NXOpen.Annotations
class TemplateTableSectionBuilder(NXOpen.Builder): 
    """ Represents a NXOpen.TDP.TemplateTableSection builder """
    @property
    def ColumnWidth(self) -> float:
        """
        Getter for property: (float) ColumnWidth
         Returns the column width   
            
         
        """
        pass
    @ColumnWidth.setter
    def ColumnWidth(self, columnWidth: float):
        """
        Setter for property: (float) ColumnWidth
         Returns the column width   
            
         
        """
        pass
    @property
    def NumberOfColumns(self) -> int:
        """
        Getter for property: (int) NumberOfColumns
         Returns the number of columns of the table    
            
         
        """
        pass
    @NumberOfColumns.setter
    def NumberOfColumns(self, numberOfColumns: int):
        """
        Setter for property: (int) NumberOfColumns
         Returns the number of columns of the table    
            
         
        """
        pass
    @property
    def NumberOfRows(self) -> int:
        """
        Getter for property: (int) NumberOfRows
         Returns the number of rows of the table   
            
         
        """
        pass
    @NumberOfRows.setter
    def NumberOfRows(self, numberOfRows: int):
        """
        Setter for property: (int) NumberOfRows
         Returns the number of rows of the table   
            
         
        """
        pass
    @property
    def Origin(self) -> NXOpen.Annotations.OriginBuilder:
        """
        Getter for property: ( NXOpen.Annotations.OriginBuilder) Origin
         Returns the origin, where the table is going to be displayed   
            
         
        """
        pass
    @property
    def RowHeight(self) -> float:
        """
        Getter for property: (float) RowHeight
         Returns the row height   
            
         
        """
        pass
    @RowHeight.setter
    def RowHeight(self, rowHeight: float):
        """
        Setter for property: (float) RowHeight
         Returns the row height   
            
         
        """
        pass
    @property
    def Style(self) -> NXOpen.Annotations.TableStyleBuilder:
        """
        Getter for property: ( NXOpen.Annotations.TableStyleBuilder) Style
         Returns the style   
            
         
        """
        pass
import NXOpen
class TemplateTableSection(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateTableSection object.
    """
    pass
import NXOpen
class TemplateViewCarouselBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template View Carousel Builder """
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    @property
    def SelectViewport(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectViewport
         Returns the selected viewport   
            
         
        """
        pass
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextCfw
         Returns the font, and width of the View Carousel text   
            
         
        """
        pass
import NXOpen
class TemplateViewCarousel(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateViewCarousel object.
    """
    pass
import NXOpen
class TemplateViewListBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template ViewList Builder """
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    @property
    def SelectViewport(self) -> NXOpen.SelectDisplayableObject:
        """
        Getter for property: ( NXOpen.SelectDisplayableObject) SelectViewport
         Returns the selected viewport   
            
         
        """
        pass
    @property
    def TextCfw(self) -> NXOpen.TextColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.TextColorFontWidthBuilder) TextCfw
         Returns the color, font, and width of the View List text   
            
         
        """
        pass
import NXOpen
class TemplateViewList(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateViewList object.
    """
    pass
import NXOpen
class TemplateViewportBuilder(TemplateBaseRectangleBuilder): 
    """ Represents a Template Viewport Builder """
    class DefaultViewType(Enum):
        """
        Members Include: 
         |NotAssigned| 
         |Back| 
         |Bottom| 
         |Front| 
         |Isometric| 
         |Left| 
         |Right| 
         |Top| 
         |Trimetric| 
         |UserDefined| 

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
        @staticmethod
        def ValueOf(value: int) -> TemplateViewportBuilder.DefaultViewType:
            """
            Returns enum member equivalent to the value passed. Useful for bit operations of enum members.
            """
            pass
    @property
    def ColorWidth(self) -> NXOpen.LineColorFontWidthBuilder:
        """
        Getter for property: ( NXOpen.LineColorFontWidthBuilder) ColorWidth
         Returns the color and width   
            
         
        """
        pass
    @property
    def DefaultViewTypes(self) -> TemplateViewportBuilder.DefaultViewType:
        """
        Getter for property: ( TemplateViewportBuilder.DefaultViewType NXOp) DefaultViewTypes
         Returns the default viwe type   
            
         
        """
        pass
    @DefaultViewTypes.setter
    def DefaultViewTypes(self, defaultViewType: TemplateViewportBuilder.DefaultViewType):
        """
        Setter for property: ( TemplateViewportBuilder.DefaultViewType NXOp) DefaultViewTypes
         Returns the default viwe type   
            
         
        """
        pass
    @property
    def Label(self) -> str:
        """
        Getter for property: (str) Label
         Returns the label   
            
         
        """
        pass
    @Label.setter
    def Label(self, labelText: str):
        """
        Setter for property: (str) Label
         Returns the label   
            
         
        """
        pass
    @property
    def ShowBorder(self) -> bool:
        """
        Getter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    @ShowBorder.setter
    def ShowBorder(self, showBorder: bool):
        """
        Setter for property: (bool) ShowBorder
         Returns the show border toggle   
            
         
        """
        pass
    @property
    def UserDefinedView(self) -> str:
        """
        Getter for property: (str) UserDefinedView
         Returns the User Defined View   
            
         
        """
        pass
    @UserDefinedView.setter
    def UserDefinedView(self, userDefinedView: str):
        """
        Setter for property: (str) UserDefinedView
         Returns the User Defined View   
            
         
        """
        pass
import NXOpen
class TemplateViewport(NXOpen.DisplayableObject): 
    """  Represents the NXOpen.TDP.TemplateViewport object.
    """
    pass
